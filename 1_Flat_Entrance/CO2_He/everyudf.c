
/**************************************************************************/
/*                                                                        */
/* User-Defined Functions used in the CFD-based adsorption model          */
/* ANSYS Fluent v19.2                                                     */
/*                                                                        */
/* Author: Henry S. Fabian Ramos                                          */
/*   Date: June 2023                                                      */
/*                                                                        */
/* Original work made open-access.                                        */
/*   If used or found helpful, please cite the authors.                   */
/*                                                                        */
/**************************************************************************/

#include "udf.h"
#include "unsteady.h"

/* IMPORTANT:
    CO2 is considered the 1st component
    N2 is considered the 2nd component
    He (non-adsorbing) is considered the 3rd component.
    (E.g. Mm3_kg refers to the molar mass of He in kilograms, 
    q1 refers to the solid phase loading of CO2, and so on.)
  
  However, note that for indices that start at i = 0:
    i = 0 ---> CO2
    i = 1 ---> N2
    (E.g. C_YI(c,t,1) refers to the mass fraction of N2)
*/


/******* SPECIFY GLOBAL VARIABLES *******/
/* These variables will be visible to all functions or macros below */
/* Use "static" when the variable values need to be conserved across iterations and time steps (like counter) */
/* Important: make sure that these quantities are cell-independent. Their values should not change as a function of space (unlike T, conductivity, etc.) */
static double GlobalIterCounter;
static double LocalIterCounter;
static double counter_EAE;
static int last_ts;
static double opng_pres; /* Calls the operating pressure specified in Fluent */
double poro_p = 0.35;
double poro_fb = 0.40;
double tort = 3;
double rho_p = 1050;
double Mm1_kg = 0.04400995;
double Mm2_kg = 0.02801340;
double Mm3_kg = 0.004002602;
static double Mm1_g, Mm2_g, Mm3_g;
double Sum_Dv1 = 26.9;
double Sum_Dv2 = 17.9;
double Sum_Dv3 = 2.88;
double part_diam = 0.001;
static double part_rad;
double euler = 2.71828183;
double Rconst = 8.3144626;
static int FirstAbsIter;


/******* UDF MACRO FOR INITIALIZING VARIABLES AND PARAMETERS *******/
/* The initial values of solid concentrations q_i for the LDF equation must be defined here */
DEFINE_INIT(my_init_func,d)
{
  cell_t c;
  Thread *t;

  GlobalIterCounter = 0.0;
  LocalIterCounter = 0.0;
  counter_EAE = 0.0;
  last_ts = -1;
  opng_pres = RP_Get_Real("operating-pressure");
  Mm1_g = Mm1_kg*1000;
  Mm2_g = Mm2_kg*1000;
  Mm3_g = Mm3_kg*1000;
  part_rad = part_diam/2;
  FirstAbsIter = 1;
  
  /* loop over all cell threads in the domain */
  thread_loop_c(t,d)
  {
    /* loop over all cells */
    begin_c_loop_all(c,t)
    {
      C_UDMI(c,t,0) = 0.00000001; /* Initial value of q1 */
      C_UDMI(c,t,1) = 0.00000001; /* Initial value of q2 */
      /* A ~zero value of q_i implies that species i is not adsorbed in the bed */
      
      C_UDMI(c,t,12) = C_UDMI(c,t,0);
      C_UDMI(c,t,13) = C_UDMI(c,t,1);
      C_UDMI(c,t,16) = C_T(c, t);
    }
    end_c_loop_all(c,t)
  }
}


/******* UDF MACRO FOR DEFINING THE EFFECTIVE POROUS-ZONE THERMAL CONDUCTIVITY [Archived] *******/
/* Use this macro only if a custom formulation of effective conductivity is required */
DEFINE_PROPERTY(porous_thermk,c,t)
{
  
  /* Definition of variables */
  int i;
  double newk, ktc;
  double ksolid = 0.20; /* Typical value for a 1000 kg/m3 Zeolite 13X particle */
  double kgas = 0.0;

  /* Definition of pointers */
  Material *sp;
  Property *prop;

  /* Calculation of the mixture thermal conductivity by weighted summation */
  mixture_species_loop(THREAD_MATERIAL(t),sp,i)
  {
      prop = (MATERIAL_PROPERTY(sp));
      ktc = generic_property(c,t,prop,PROP_ktc,C_T(c,t));
      kgas += C_YI(c,t,i)*ktc;
  }

  /* Custom modification/recalculation of conductivity for porous zone */
  /* newk = [CUSTOM EXPRESSION]; */
  newk = poro_fb*kgas + (1-poro_fb)*ksolid;

  return newk;
}


/******* UDF MACRO FOR DEFINING THE POROUS-ZONE DIFFUSIVITY *******/
DEFINE_DIFFUSIVITY(porous_diff,c,t,i)
{
  
  /* Definition of variables */
  double Dm, DL;
  double abs_pres, temp;
  double ints_vel;
  /* double Le = 1; */

  /* Determination of local pressure, temperature, and interstitial velocity */
  abs_pres = C_P(c,t) + opng_pres; /* Absolute pressure */
  temp = C_T(c, t); /* Temperature */
  ints_vel = pow(pow(C_U(c,t),2) + pow(C_V(c,t),2) + pow(C_W(c,t),2),0.5); /* Interstitial/physical velocity */

  /* Calculation of Molecular Diffusivity (Dm) at the local temperature using the Fuller correlation for 2 species */
  Dm = (0.01013*pow(temp,1.75)*pow(1/Mm1_g + 1/Mm3_g,0.5))/(abs_pres*pow(pow(Sum_Dv1,1.0/3.0) + pow(Sum_Dv3,1.0/3.0),2));
  
  /* [Alternative] Calculation of the bulk gas phase diffusivity, using the Lewis unity assumption */
  /* Dm = C_K_L(c,t)/(C_R(c,t)*C_CP(c,t)*Le); */
  
  C_UDMI(c,t,5) = Dm; /* We store the value of the variable in a User-Defined Memory (UDMi) to be used in other UDF macros */

  /* Calculation of the dispersion coefficient FOR THE POROUS ZONE */
  DL = 0.7*Dm + 0.5*ints_vel*part_diam; /* Macromixing dispersion approach used */

  C_UDMI(c,t,4) = DL; /* We can also store the value of the variable in a UDMi to monitor it in Fluent and post-process it */

  return DL;

}


/******* UDF MACRO FOR SOLVING THE LDF EQUATION NUMERICALLY *******/
DEFINE_ADJUST(my_adjust,d)
{

  int curr_ts;
  double h;
  int PorousZoneID = 6; /* This refers to the adsorbent bed zone where this routine will be executed */

  Thread *t = Lookup_Thread(d, PorousZoneID);
  cell_t c;

  /* curr_ts = N_TIME; */
  h = CURRENT_TIMESTEP;
  /* last_ts = curr_ts; */
  GlobalIterCounter = GlobalIterCounter + 1;
  LocalIterCounter = LocalIterCounter + 1;

  thread_loop_c(t, d)
  {
    begin_c_loop(c, t)
    {
      
      /* -------------------------------------------------- START IMPLEMENTATION -------------------------------------------------- */
      
      /* Definition and declaration of variables */
      int i; /* Not actually used. Just if needed */
      double temp, abs_pres, c1, c2;
      double dq1dt, dq2dt, q1star, q2star, k1, k2;
      double large1, large2;
      double qsb1, qsb2, qsd1, qsd2;
      double b1, b2, d1, d2;
      double b01, b02, d01, d02;
      double dUb1, dUb2, dUd1, dUd2;
      double source = 0.0;
      double Dm, Dp;

      double q1_M1, f1_M1, RK_q1_k1, RK_q1_k2, RK_q1_k3, RK_q1_k4, q1_new;
      double q2_M1, f2_M1, RK_q2_k1, RK_q2_k2, RK_q2_k3, RK_q2_k4, q2_new;

      double RLX = 0.15;

      /* Definition of adsorption isotherm parameters. Values taken from Wilkins & Rajendran (2019) */
      b01 = 2.09*pow(10,-7);
      b02 = 2.13*pow(10,-6);
      d01 = 1.06*pow(10,-7);
      d02 = 2.13*pow(10,-6);

      qsb1 = 3.257;
      qsb2 = 3.257;
      qsd1 = 3.240;
      qsd2 = 3.240;

      dUb1 = -42670;
      dUb2 = -16250;
      dUd1 = -32210;
      dUd2 = -16250;

      /* We call the relevant variables for this case, from Fluent */
      abs_pres = C_P(c,t) + opng_pres;
      temp = C_T(c, t); /* Temperature */
      c1 = (C_YI(c,t,0)/Mm1_kg)/(C_YI(c,t,0)/Mm1_kg + C_YI(c,t,1)/Mm2_kg + (1-C_YI(c,t,0)-C_YI(c,t,1))/Mm3_kg)*abs_pres/(Rconst*temp); /* These two equations are used to convert from mass fraction into molar concentration, assuming  ideal gas law. */
      c2 = (C_YI(c,t,1)/Mm2_kg)/(C_YI(c,t,0)/Mm1_kg + C_YI(c,t,1)/Mm2_kg + (1-C_YI(c,t,0)-C_YI(c,t,1))/Mm3_kg)*abs_pres/(Rconst*temp);

      /* We call the local Molecular Diffusivity (Dm) from DEFINE_DIFFUSIVITY */
      Dm = C_UDMI(c,t,5);
      Dp = Dm/tort;

      /* Formulation of adsorption equilibrium equations */
      
      /* Adsorption equilibrium constants */
      b1 = b01*pow(euler,-dUb1/(Rconst*temp));
      b2 = b02*pow(euler,-dUb2/(Rconst*temp));
      d1 = d01*pow(euler,-dUd1/(Rconst*temp));
      d2 = d02*pow(euler,-dUd2/(Rconst*temp));

      /* Equilibrium solid phase loadings (q*) */
      large1 = qsb1*b1/(1 + b1*c1 + b2*c2) + qsd1*d1/(1 + d1*c1 + d2*c2);
      large2 = qsb2*b2/(1 + b1*c1 + b2*c2) + qsd2*d2/(1 + d1*c1 + d2*c2);
      q1star = c1*large1;
      q2star = c2*large2;

      /* LDF mass transfer coefficients (k) */
      k1 = (15*poro_p*Dp/pow(part_rad,2))*(1/(large1*rho_p*(1 - poro_fb)/poro_fb)); /* We calculate LDF k using these equations assuming that... */
      k2 = (15*poro_p*Dp/pow(part_rad,2))*(1/(large2*rho_p*(1 - poro_fb)/poro_fb)); /* ... molecular diffusion in the macropores control the transport into the solid phase. */

      /* -------------------------------- CALCULATION OF qi and dqi/dt STARTS -------------------------------- */
      
      /* This loads the existing qi_M1 values into the "handle" variable qi_M1 -- Done for better readability */
      q1_M1 = C_UDMI(c,t,12);
      q2_M1 = C_UDMI(c,t,13);

      /* This is executed in the very first absolute iteration in order to calculate fi_M1(0) || fi = dqi/dt = ki*(qistar - qi) */
      if(N_ITER == 0)
      {
        C_UDMI(c,t,14) = k1*(q1star - q1_M1);
        C_UDMI(c,t,15) = k2*(q2star - q2_M1);
        /* FirstAbsIter = 0; */
        printf("XXXXXXXXXXXXXXXXXXXXXX First Absolute Iteration: DONE | Global Iter: %g XXXXXXXXXXXXXXXXXXXXXX \n", GlobalIterCounter);
        fflush(stdout);
        printf("XXXXXXXXXXXXXXXXXXXXXX N_ITER: %d XXXXXXXXXXXXXXXXXXXXXX \n", N_ITER);
        fflush(stdout);
      }
      
      /* This loads the existing fi_M1 values into the "handle" variable fi_M1 -- Done for better readability */
      f1_M1 = C_UDMI(c,t,14);
      f2_M1 = C_UDMI(c,t,15);

      /* ----------------------- Actual IMPLICIT Method START ------------------------ */

      /* q1_new = (q1_M1 + h*k1*q1star)/(1 + h*k1); <--- 1st Order implicit (Euler's Implicit Method) */
      q1_new = (2*q1_M1 + h*k1*q1star + h*f1_M1)/(2 + h*k1); /* <--- 2nd Order implicit (Trapezoidal Method) */
      q1_new = RLX*q1_new + (1 - RLX)*C_UDMI(c,t,0); /* Here, C_UDMI(c,t,0) is storing the value of q1 from the immediate previous iteration */
      

      /* q2_new = (q2_M1 + h*k2*q2star)/(1 + h*k2); <--- 1st Order implicit (Euler's Implicit Method) */
      q2_new = (2*q2_M1 + h*k2*q2star + h*f2_M1)/(2 + h*k2); /* <--- 2nd Order implicit (Trapezoidal Method) */
      q2_new = RLX*q2_new + (1 - RLX)*C_UDMI(c,t,1); /* Here, C_UDMI(c,t,1) is storing the value of q2 from the immediate previous iteration */

      /* NOTE: qi_new can be interpreted as qi_current */

      /* ----------------------- Actual IMPLICIT Method ENDS ------------------------ */


      /* Calculation of dqi/dt */
      dq1dt = (q1_new - q1_M1)/h;
      dq2dt = (q2_new - q2_M1)/h;


      /* Update memory with the new values for the variables */
      C_UDMI(c,t,0) = q1_new;
      C_UDMI(c,t,1) = q2_new;
      C_UDMI(c,t,2) = dq1dt;
      C_UDMI(c,t,3) = dq2dt;

      C_UDMI(c,t,6) = k1;
      C_UDMI(c,t,7) = k2;
      C_UDMI(c,t,8) = q1star;
      C_UDMI(c,t,9) = q2star;
      C_UDMI(c,t,10) = c1;
      C_UDMI(c,t,11) = c2;

      /* -------------------------------- CALCULATION OF qi and dqi/dt ENDS -------------------------------- */

      
      /* -------------------------------------------------- IMPLEMENTATION ENDS -------------------------------------------------- */
      
      
    }
    end_c_loop(c, t)
  }

}


/******* UDF MACRO TO EXECUTE INSTRUCTIONS AT THE END OF EVERY TIME STEP *******/
DEFINE_EXECUTE_AT_END(execute_only_at_end)
{

    Domain *d;
    Thread *t;
    cell_t c;
    d = Get_Domain(1);

    if (CURRENT_TIME>0)
    {
      
      /* Definition of general equations: */
      counter_EAE = counter_EAE + 1.0;

      /* Definition of cell equations: */
      thread_loop_c(t,d)
      {
          begin_c_loop(c,t)
          {
            /* Definition of variables: */

            /* We update qi_M1 here: */
            C_UDMI(c,t,12) = C_UDMI(c,t,0);
            C_UDMI(c,t,13) = C_UDMI(c,t,1);

            /* We update fi_M1 here: */
            C_UDMI(c,t,14) = C_UDMI(c,t,6)*(C_UDMI(c,t,8) - C_UDMI(c,t,0));
            C_UDMI(c,t,15) = C_UDMI(c,t,7)*(C_UDMI(c,t,9) - C_UDMI(c,t,1));

            /* We update T_M1 here: */
            C_UDMI(c,t,16) = C_T(c, t);

          }
          end_c_loop(c,t)
      }

      /* Printing progress messages to console. Disable if not needed */

      printf("XXXXXXXXXXXXXXXXXXXXXX # of Iterations in this time-step: %g XXXXXXXXXXXXXXXX \n", LocalIterCounter);
      fflush(stdout);

      printf("XXXXXXXXXXXXXXXXXXXXXX # of Time-steps finished in this run: %g XXXXXXXXXXXXX \n", counter_EAE);
      fflush(stdout);

      printf("XXXXXXXXXXXXXXXXXXXXXX # of Global Iterations: %g XXXXXXXXXXXXXXXXXXXXXXXXXXX \n", GlobalIterCounter);
      fflush(stdout);

      printf("XXXXXXXXXXXXXXXXXXXXXX N_ITER: %d XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \n", N_ITER);
      fflush(stdout);

      LocalIterCounter = 0.0;

    }

}


/******* SOURCE UDF MACRO FOR THE CONTINUITY EQUATION *******/
DEFINE_SOURCE(udf_source_term_masscontinuity,c,t,dS,eqn)
{

  /* Definition and declaration of variables */
  int i;
  double dq1dt, dq2dt;
  double source;

  /* We call the relevant variables for this source term, from Fluent */
  dq1dt = C_UDMI(c,t,2);
  dq2dt = C_UDMI(c,t,3);  

  /* Formulation of equations */

  source = -((1-poro_fb)/1.00)*rho_p*(Mm1_kg*dq1dt + Mm2_kg*dq2dt);

  /* We determine the derivative dS/dphi, in order to aid the convergence (optional) */
  dS[eqn] = 0.0;

  /* The adsorption continuity source term (or rather sink term) is returned */
  return source;

}


/******* SOURCE UDF MACRO FOR THE ENERGY EQUATION - Part 1 *******/
DEFINE_SOURCE(udf_source_term_energy,c,t,dS,eqn)
{

  /* Definition and declaration of variables */
  int i;
  double q1, q2, dq1dt, dq2dt;
  double dH1, dH2, dU2;
  double temp;
  double source;

  /* We call the relevant variables for this source term, from Fluent */
  q1 = C_UDMI(c,t,0);
  q2 = C_UDMI(c,t,1);
  dq1dt = C_UDMI(c,t,2);
  dq2dt = C_UDMI(c,t,3);
  temp = C_T(c, t);

  /* Formulation of equations */

  dU2 = -16250;
  dH1 = -(-5156*q1 + 50907);
  dH2 = dU2 - Rconst*temp;

  source = ((1-poro_fb)/1.00)*rho_p*((-dH1)*dq1dt + (-dH2)*dq2dt);

  /* We determine the derivative dS/dphi, in order to aid the convergence (optional) */
  dS[eqn] = 0.0;

  /* The enthalpy-based energy source term is returned */
  return source;

}


/******* SOURCE UDF MACRO FOR THE ENERGY EQUATION - Part 2 *******/
DEFINE_SOURCE(udf_source_term_energy_2,c,t,dS,eqn)
{

  /* Definition and declaration of variables */
  int i;
  double q1, q2, dq1dt, dq2dt;
  double cpg_1, cpg_2, cpa_1, cpa_2;
  double temp, T_M1, dt, dTdt;
  double source_1, source_2, source;

  /* We call the relevant variables for this source term, from Fluent */
  q1 = C_UDMI(c,t,0);
  q2 = C_UDMI(c,t,1);
  dq1dt = C_UDMI(c,t,2);
  dq2dt = C_UDMI(c,t,3);
  temp = C_T(c, t);
  T_M1 = C_UDMI(c,t,16); /* This loads the existing T_M1 values into the "handle" variable T_M1 -- Done for better readability */
  dt = CURRENT_TIMESTEP;


  /* Formulation of equations */

  cpg_1 = 429.9289 + 1.874473*temp - 0.001966485*pow(temp,2) + 0.000001297251*pow(temp,3) - 0.0000000003999956*pow(temp,4);
  cpg_2 = 979.043 + 0.4179639*temp - 0.001176279*pow(temp,2) + 0.000001674394*pow(temp,3) - 0.0000000007256297*pow(temp,4);
  cpa_1 = cpg_1 - Rconst/Mm1_kg;
  cpa_2 = cpg_2 - Rconst/Mm2_kg;

  dTdt = (temp - T_M1)/dt;
  
  source_1 = -((1-poro_fb)/1.00)*rho_p*temp*(cpa_1*Mm1_kg*dq1dt + cpa_2*Mm2_kg*dq2dt);
  source_2 = -((1-poro_fb)/1.00)*rho_p*dTdt*(cpa_1*Mm1_kg*q1 + cpa_2*Mm2_kg*q2);

  source = source_1 + source_2;
  

  /* We determine the derivative dS/dphi, in order to aid the convergence (optional) */
  dS[eqn] = 0.0;

  /* The adsorbed matter contribution energy source term is returned */
  return source;

}


/******* SOURCE UDF MACRO FOR THE SPECIES CONSERVATION EQUATION - CO2 *******/
DEFINE_SOURCE(udf_source_term_species_CO2,c,t,dS,eqn)
{

  /* Definition and declaration of variables */
  int i;
  double dq1dt, dq2dt;
  double source;

  /* We call the relevant variables for this source term, from Fluent */
  dq1dt = C_UDMI(c,t,2);
  dq2dt = C_UDMI(c,t,3);
  

  /* Formulation of equations */

  source = -((1-poro_fb)/1.00)*rho_p*(Mm1_kg*dq1dt);
  
  /* We determine the derivative dS/dphi, in order to aid the convergence (optional) */
  dS[eqn] = 0.0;

  /* The source (sink) term for species 1 due to adsorption is returned */
  return source;

}


/******* SOURCE UDF MACRO FOR THE SPECIES CONSERVATION EQUATION - N2 *******/
DEFINE_SOURCE(udf_source_term_species_N2,c,t,dS,eqn)
{

  /* Definition and declaration of variables */
  int i;
  double dq1dt, dq2dt;
  double source;

  /* We call the relevant variables for this source term, from Fluent */
  dq1dt = C_UDMI(c,t,2);
  dq2dt = C_UDMI(c,t,3);

  /* Formulation of equations */

  source = -((1-poro_fb)/1.00)*rho_p*(Mm2_kg*dq2dt);
  
  /* We determine the derivative dS/dphi, in order to aid the convergence (optional) */
  dS[eqn] = 0.0;

  /* The source (sink) term for species 2 due to adsorption is returned */
  return source;

}

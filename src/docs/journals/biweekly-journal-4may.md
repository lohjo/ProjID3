Bi-Weekly Journal #1: 4 May 2026
Following NUS and SUTD briefings, many administrative details have been laid out. Our design project title has changed to: “CO2 Adsorption in Packed-Bed Column using Polymer-based Sorbent: Parametric Study and Model Prediction”. This bi-weekly journal outlines the administrative details, project scope and an 18-week Gantt chart.

Student: Loh John Ray, Saraswati Eloise Gunawan
Institution supervisors (SUTD/NUS): Dr. Prapatsorn Borisut, Prof. Erik Birgerhesson
NP Supervisor: Dr. Pham the Hanh
Project code: 3
Plan prepared: Monday 20 April 2026 (Week 1, Day 1); revised 30 April 2026 – scope change: regeneration ? adsorption breakthrough.
Submission deadlines: Interim Report Mon 1 Jun 2026 (Wk 7); Final Report Mon 10 Aug 2026 (Wk 17); Final Presentation 17–19 Aug 2026 (Wk 18)

Administrative Details

* Every Friday starting (9/05/2026): conduct experiments at SUTD as in Fig. 1).
* Last Friday of each month, send one-page email to Prof. Erik + Dr. Prapatsorn + NP supervisor.
* Set up Google Drive & Microsoft Teams for document sharing
* Created Excel spreadsheet to document progress

Appendices

* 7 research papers Google Drive: https://drive.google.com/drive/folders/1JvF3PfUU05b_RmShMsFQ3KfBLCPmzAwt?usp=sharing 
* Interim report draft: [interim_report_draft.docx]( https://connectnpedu.sharepoint.com/:w:/s/DPDACO2AdsorptioninPackedBedColumns/IQCEF0_goXQSQ4MLTD5e67gXASJTFIMda2V_Gw-QobM0XOE?e=mcyrXH )
* 18-week Gantt chart: https://docs.google.com/spreadsheets/d/18sq36Vg-FqNCxkZenRcN9-HxAKQlgACT/edit?usp=sharing&ouid=109399668662392411148&rtpof=true&sd=true 

Description: Weeks 1-2 were a triage period. The original project scope (CO2 regeneration process of a sorbent) was pivoted on 30 April to CO2 adsorption breakthrough on a polymer-based sorbent anchored to Stampi-Bombelli et al. (2024) as the primary experimental benchmark. These two weeks’ progress have been substantial: (i) lectures on transport phenomena taught us on volume elements, the stress tensor, and exposed us to the foundations of fluid mechanics; (ii) (WIP) literature review gave us deeper insights about the design project—how amine sorbents can transform into a full direct air capture (DAC) application, as well as providing the mathematical foundations for this design project. The deliverables for this bi-weekly journal are to: (a) read the seven papers given by Dr. Prapatsorn; (b) plan the 18-week design project scope using a Gantt chart. Although mainly, I want to be as transparent as possible about the inner-workings of this design project, so as to set the stage for open-communication and collaboration between the supervisors and us during the year-long research project.

What I have done

* Started read the four (out of seven) papers sent by Dr. Prapatsorn (Stampi-Bombelli 2024, Myers & Font 2020, Pedrozo 2026, de Joannis 2025) and started reading Evans Ch. 3 on first-order PDEs.
* Wrote out equations of change by hand in Bird Ch. 11, referenced to gas-phase equation from Myers & Font.
* Set up Python environment, cloned the heat-equation MOL template, and confirmed scipy.integrate.solve_ivp with LSODA runs on my machine.
* Started LaTeX skeleton for the Interim Report so the derivation has somewhere to live in when I write it.

The journal is also where I am forcing myself to define every term I have been using loosely. Most of what follows is to organise my own vocabulary so that next week’s non-dimensionalisation won’t collapse under my own sloppy notation.

What I have learnt

Breakthrough time, the width of the mass-transfer zone (MTZ) and the fraction of sorbent capacity all fall out of the structure of PDE governing the adsorption process. Understanding the equations allows me to predict (in advance) how each parameter affects one another.

A study plan was initially generated on 20 April [2024]( https://claude.ai/share/4aa6c3f9-e818-4428-8326-40b8bb001073 ). [Seven research sources] (https://drive.google.com/file/d/1B3InpW9EL_gGY75DWKDmGKcD5UipV0n4/view?usp=sharing ) connected to each sub-topic is what grounded the initial project scope, with a deep emphasis on mathematical learning. I also explored [F1-Prompting]( https://arxiv.org/html/2601.19302v2__ )—an equations-first prompting technique that leverages on model chain-of-thought (CoT) to optimize its search space and guide strategy selection. The result is a [derivation]( https://claude.ai/share/eb3361cf-cfed-4171-b0cd-97770dcd0ecd ) (also in [PDF format]( https://drive.google.com/file/d/1PDBZWOFETXoauvdPSHS0LDUnGlzcXwF-/view?usp=sharing)) of the 4-PDE system that describes one-dimensional packed-bed regeneration under some assumptions. I also tested the [well-posedness]( https://drive.google.com/file/d/11NB-xMR_7muwxEdV2-EdM2QVQHlNbnDK/view?usp=sharing) of the derived solution. Eventually, I decided that reading the literature given, word-by-word, is far more effective in developing an intuitive understanding for the proposed CO2 adsorption breakthrough in packed-bed columns. On 30 April, 7 helpful research sources were sent by Dr. Prapatsorn, of which 3 was read—developing a foundational understanding of transport phenomena, advective-diffusive equations, CO2 adsorption theory and modelling—which was documented in the [interim report draft]( https://connectnpedu.sharepoint.com/:w:/s/DPDACO2AdsorptioninPackedBedColumns/IQCEF0_goXQSQ4MLTD5e67gXASJTFIMda2V_Gw-QobM0XOE?e=mcyrXH). The current version of the [study plan]( https://drive.google.com/file/d/1hzWBKR85mmANV1E_-TnGk3tLCnI00ZGM/view?usp=sharing)describes lays the design project scope—particularly in the 18-week master plan, mathematical learning track, literature anchor map and risk register—proving to be an additional layer of project shepherding required to tackle the complex research topic.

Blockers & Questions

I realise from Prof. Erik’s first meeting that the research topic is open-ended. As I tend to sometimes be obsessive over the work that I do, there would be times when I go cold-turkey researching on the topic on my own. A fraction of this habit was mirrored during the first two weeks until 3 May when I was drafting my bi-weekly journal. I fear that during these periods of no-feedback, the project direction would be led astray. Saraswati and I have consulted each other and have managed to clarify any doubts or pressures that may be a weight on our shoulders. Thus, this was identified as a potential blocker—in terms of modelling and experiment—with further clarification needed on the project direction.

Gantt Chart

Design Project Objectives

* Study the effect of adsorption process parameters on breakthrough curve and breakthrough parameters.  
* Adsorption parameters i.e., adsorption temperature, inlet gas flow rate, packed height, amount of material etc.
* Investigate adsorption performance and energy consumption of the process.


Figure 4. Gantt Chart (in-progress)

The next steps

* Myers & Font 2020 §2–3: the full derivation of the traveling-wave shock solution
* LeVeque, Numerical Methods for Conservation Laws Ch 3: scalar conservation laws and Rankine–Hugoniot conditions
* Work problem: Derive v_shock for a Langmuir isotherm, then for Toth; draw both chords on a q^* vs C graph
* Understanding Peclet number for axial dispersion, NTU (number of transfer units) for mass-transfer rate vs convective residence time, ?=?_p  (1-?)?q/(? ?C) for solid-phase vs gas-phase CO? capacity which sets the adsorption shock speed relative to u and, ?=(-?H_ads )?q/(c_pg· T_ads ) for heat-of-adsorption feedback strength on temperature rise. 
Project Title: CO2 Adsorption in Packed-Bed Column using Polymer-based Sorbent: Parametric Study and Model Prediction



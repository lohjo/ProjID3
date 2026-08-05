"""Reconcile every number quoted in sensitivity-analysis.md against the workbook."""
import re, sys, pandas as pd, numpy as np
x = pd.ExcelFile('src/docs/sensitivity_anova_tables.xlsx')
md = open('src/docs/sensitivity-analysis.md', encoding='utf-8').read()
md = md.replace('−', '-').replace(' ', '').replace(' ', '')

sup = {'⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9','⁻':'-'}
toks = set()
for m in re.findall(r'-?\d[\d ]*\.?\d*(?:\s*×\s*10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)?|-?\d*\.\d+e?-?\d*', md):
    s = m.replace(' ', '')
    e = re.search(r'×10([⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)', s)
    if e:
        try: s = float(s.split('×')[0]) * 10 ** int(''.join(sup[c] for c in e.group(1)))
        except Exception: continue
    try: toks.add(float(s))
    except ValueError: pass

fails = []
n_checked = 0
def check(tag, v, tol=0.02):
    global n_checked
    if not np.isfinite(v):
        return
    n_checked += 1
    if not any(abs(v-t) <= tol*max(abs(v), abs(t), 1e-30) for t in toks):
        fails.append(f'{tag} = {v:.6g}')

f = x.parse('E2_factorial_anova')
for _, r in f.iterrows():
    for c in ('F_flow','F_conc','F_int','eta2_flow','eta2_conc','eta2_int','eta2_resid'):
        check(f'E2 {r.response}.{c}', r[c])
rp = x.parse('E2b_replicate_reproducibility')
for _, r in rp.iterrows():
    for c in ('pure_error_sd','total_sd','pure_error_frac_of_total_var',
              'median_within_cell_CV','worst_cell_ratio'):
        check(f'E2b {r.response}.{c}', r[c])
e1 = x.parse('E1_cluster_anova_exp')
for _, r in e1[e1.scope.str.startswith('grid')].iterrows():
    check(f'E1 {r.factor[:4]}/{r.response}.F', r.F); check(f'E1 {r.factor[:4]}/{r.response}.eta2', r.eta2)
e3 = x.parse('E3_regression_exp')
for _, r in e3[(e3.scope.str.startswith('grid')) & (e3.term != '(Intercept)')].iterrows():
    check(f'E3 {r.response}/{r.term}.beta', r.beta); check(f'E3 {r.response}/{r.term}.std_coef', r.std_coef)
e4 = x.parse('E4_regression_summary_exp')
for _, r in e4.iterrows():
    for c in ('R2','AdjR2','SEE'): check(f'E4 {r.scope}/{r.response}.{c}', r[c])
t1 = x.parse('T1_param_distribution')
for _, r in t1.iterrows():
    for c in ('min','max','median','mean','sd','CV'): check(f'T1 {r.model}.{r.parameter}.{c}', r[c])
p1 = x.parse('P1_param_vs_conditions')
for _, r in p1[p1.term == 'Q [lpm]'].iterrows():
    check(f'P1 {r.model}.{r.parameter}.beta_Q', r.beta); check(f'P1 {r.model}.{r.parameter}.b_Q', r.std_coef)
p3 = x.parse('P3_param_cluster_anova')
for _, r in p3.iterrows():
    check(f'P3 {r.model}.{r.parameter}/{r.factor[:4]}.F', r.F)
    check(f'P3 {r.model}.{r.parameter}/{r.factor[:4]}.eta2', r.eta2)
t4 = x.parse('T4_cluster_anova_MC')
for _, r in t4[(t4.model=='M11') & (t4.scheme=='independent')].iterrows():
    check(f'T4 M11.{r.parameter}/{r.response}.F', r.F); check(f'T4 M11.{r.parameter}/{r.response}.eta2', r.eta2)
for _, r in t4[(t4.model=='M24') & (t4.scheme=='independent') & (t4.response=='t_b [s]')].iterrows():
    check(f'T4 M24.{r.parameter}/t_b.F', r.F)
t3 = x.parse('T3_regression_summary_MC')
# only the rows the document actually quotes in its Table 3 excerpt
QUOTED = {('M11','independent'): None,
          ('M11','rank-correlated'): {'t_b [s]','t_E [s]','q_dyn [mol/kg]'},
          ('M24','independent'): {'t_b [s]','t_E [s]','q_dyn [mol/kg]'}}
for _, r in t3.iterrows():
    key = (r.model, r.scheme)
    if key in QUOTED and (QUOTED[key] is None or r.response in QUOTED[key]):
        check(f'T3 {r.model}/{r.scheme}/{r.response}.R2', r.R2)

print(f'numeric tokens in document : {len(toks)}')
print(f'workbook claims checked    : {n_checked}')
print(f'mismatches                 : {len(fails)}')
print('\n>>> ALL CHECKS PASSED' if not fails else '\n>>> MISMATCHES:')
for q in fails: print('  -', q)
sys.exit(1 if fails else 0)

# May-2026 diagnostic runs — engineered-prompt deliverables

*Assembled from stored `breakthrough_out/` fits; no re-fitting.*

### Table 1 — Derived physical parameters (May-2026 runs)

**FLAG — geometrically inconsistent inputs.** Format-A sensor logs carry no flow/mass/geometry, so every value below uses the engineered prompt's assumptions: d = 85 mm, bed L = 21 cm, m = 8.00 g, ρ_p = 800 kg/m³. With these, EC-1 gives ρ_b = **6.7 kg/m³** and EC-2 gives ε = **0.992** — an essentially empty column. 8 g cannot pack a 21 cm × 85 mm bed (that volume ≈ 953 g at ρ_p = 800). ρ_b, ε(EC-2) and the ε-based interstitial velocity below are therefore unphysical; the real packed-bed geometry of these runs is the missing input (owner: Prof. Birgersson / SUTD rig). The U column (EC-5) depends only on flow + column area and is reliable; v is also reported against a typical packed-bed ε = 0.40 as a usable fallback.

| Run | conc (%) | flow (lpm) | ρ_b [kg/m³] | ε (EC-2) | U [m/s] (EC-5) | v [m/s] @ε(EC-2) | v [m/s] @ε=0.40 |
|---|---|---|---|---|---|---|---|
| May-20-2026Run2conc5_flow0.1 | 5 | 0.10 | 6.7 | 0.992 | 2.937e-04 | 2.962e-04 | 7.343e-04 |
| May-20-2026conc5_flow1.5 | 5 | 1.50 | 6.7 | 0.992 | 4.406e-03 | 4.443e-03 | 1.101e-02 |
| May-20-2026conc5_flow1.5(2) | 5 | 1.50 | 6.7 | 0.992 | 4.406e-03 | 4.443e-03 | 1.101e-02 |
| May-20-2026conc5_flow1.5(3) | 5 | 1.50 | 6.7 | 0.992 | 4.406e-03 | 4.443e-03 | 1.101e-02 |
| May-22-2026-conc10-flow0.05 | 10 | 0.05 | 6.7 | 0.992 | 1.469e-04 | 1.481e-04 | 3.671e-04 |
| May-22-2026-conc10-flow0.1 | 10 | 0.10 | 6.7 | 0.992 | 2.937e-04 | 2.962e-04 | 7.343e-04 |
| May-22-2026-conc10_flow-0.1(2) | 10 | 0.10 | 6.7 | 0.992 | 2.937e-04 | 2.962e-04 | 7.343e-04 |

### Table 2 — Model fit statistics (9 prompt models × 7 runs)

Read straight from the stored `results_<run>.csv`. AdjR² < 0 means the model is worse than a horizontal line through the mean. Wolborska (M05) is fitted on the early window only (C/C0 ≤ 0.15), so its statistics are not comparable to the complete-curve models — see Table 3 note.

| Run | Model | p | AdjR² | χ²_ν | AICc | RMSE | key params |
|---|---|---|---|---|---|---|---|
| May-20-2026Run2conc5_flow0.1 | Logistic (BA/Thomas/YN) | 2 | 0.2329 | 0.2077 | -2981 | 0.4557 | k_YN=0.1035, tau=1541 |
| May-20-2026Run2conc5_flow0.1 | Clark | 3 | 0.4503 | 0.1488 | -3612 | 0.3857 | r=0.001674, A=2.989e+04 |
| May-20-2026Run2conc5_flow0.1 | Modified Dose-Response | 2 | 0.3438 | 0.1777 | -3277 | 0.4215 | a=1.706, t50=2067 |
| May-20-2026Run2conc5_flow0.1 | Wolborska (early, C/C0<=0.15) | 2 | -0.004683 | 0.001405 | -3748 | 0.03748 | slope=1e-06, intercept=-3.13 |
| May-20-2026Run2conc5_flow0.1 | Gudermannian | 2 | 0.2329 | 0.2077 | -2981 | 0.4557 | k=0.08671, tau=1541 |
| May-20-2026Run2conc5_flow0.1 | Error function | 2 | 0.2329 | 0.2077 | -2981 | 0.4557 | k=0.04246, tau=1541 |
| May-20-2026Run2conc5_flow0.1 | Weibull | 2 | 0.3823 | 0.1673 | -3392 | 0.409 | tau=3453, k=1.247 |
| May-20-2026Run2conc5_flow0.1 | Klinkenberg | 2 | 0.32 | 0.1841 | -3210 | 0.4291 | K_fa=1, K=4122 |
| May-20-2026Run2conc5_flow0.1 | Fractal-BA (fractal YN) | 3 | 0.3967 | 0.1634 | -3436 | 0.4041 | k_YN0=0.001188, tau=3177 |
| May-20-2026conc5_flow1.5 | Logistic (BA/Thomas/YN) | 2 | 0.8929 | 0.01057 | -1349 | 0.1028 | k_YN=0.09132, tau=2168 |
| May-20-2026conc5_flow1.5 | Clark | 3 | 0.7245 | 0.02718 | -1068 | 0.1646 | r=0.008014, A=6.655e+05 |
| May-20-2026conc5_flow1.5 | Modified Dose-Response | 2 | 0.6976 | 0.02984 | -1041 | 0.1727 | a=20, t50=2147 |
| May-20-2026conc5_flow1.5 | Wolborska (early, C/C0<=0.15) | 2 | -0.004487 | 7.775e-05 | -2326 | 0.008818 | slope=1e-06, intercept=-3.994 |
| May-20-2026conc5_flow1.5 | Gudermannian | 2 | 0.8927 | 0.01059 | -1349 | 0.1029 | k=0.07653, tau=2168 |
| May-20-2026conc5_flow1.5 | Error function | 2 | 0.8932 | 0.01054 | -1350 | 0.1027 | k=0.0375, tau=2168 |
| May-20-2026conc5_flow1.5 | Weibull | 2 | 0.6171 | 0.03778 | -971 | 0.1944 | tau=2225, k=10 |
| May-20-2026conc5_flow1.5 | Klinkenberg | 2 | -0.8157 | 0.1791 | -508.7 | 0.4232 | K_fa=1, K=1e+04 |
| May-20-2026conc5_flow1.5 | Fractal-BA (fractal YN) | 3 | -0.2023 | 0.1186 | -630.1 | 0.3438 | k_YN0=38.7, tau=4.389e+05 |
| May-20-2026conc5_flow1.5(2) | Logistic (BA/Thomas/YN) | 2 | -1837 | 0.02334 | -166.8 | 0.1528 | k_YN=0.1318, tau=1 |
| May-20-2026conc5_flow1.5(2) | Clark | 3 | -1101 | 0.01399 | -188.6 | 0.1169 | r=1, A=1e-06 |
| May-20-2026conc5_flow1.5(2) | Modified Dose-Response | 2 | -3328 | 0.04229 | -140.1 | 0.2056 | a=16.52, t50=1 |
| May-20-2026conc5_flow1.5(2) | Wolborska (early, C/C0<=0.15) | 2 | — | — | — | — | slope=—, intercept=— |
| May-20-2026conc5_flow1.5(2) | Gudermannian | 2 | -1848 | 0.02349 | -166.6 | 0.1533 | k=0.1138, tau=1 |
| May-20-2026conc5_flow1.5(2) | Error function | 2 | -1821 | 0.02314 | -167.2 | 0.1521 | k=0.05104, tau=1 |
| May-20-2026conc5_flow1.5(2) | Weibull | 2 | -3328 | 0.04229 | -140.1 | 0.2056 | tau=1.277, k=1.5 |
| May-20-2026conc5_flow1.5(2) | Klinkenberg | 2 | -1075 | 0.01367 | -190.9 | 0.1169 | K_fa=1, K=1 |
| May-20-2026conc5_flow1.5(2) | Fractal-BA (fractal YN) | 3 | -1785 | 0.02269 | -166.9 | 0.1489 | k_YN0=4, tau=1 |
| May-20-2026conc5_flow1.5(3) | Logistic (BA/Thomas/YN) | 2 | 0.5898 | 0.1233 | -1804 | 0.3511 | k_YN=0.09773, tau=1771 |
| May-20-2026conc5_flow1.5(3) | Clark | 3 | 0.5805 | 0.1261 | -1784 | 0.3549 | r=0.01067, A=9.995e+05 |
| May-20-2026conc5_flow1.5(3) | Modified Dose-Response | 2 | 0.5153 | 0.1457 | -1660 | 0.3817 | a=2.33, t50=1887 |
| May-20-2026conc5_flow1.5(3) | Wolborska (early, C/C0<=0.15) | 2 | -0.003138 | 0.0004723 | -1790 | 0.02173 | slope=8.807e-05, intercept=-4.133 |
| May-20-2026conc5_flow1.5(3) | Gudermannian | 2 | 0.5898 | 0.1233 | -1804 | 0.3511 | k=0.08176, tau=1771 |
| May-20-2026conc5_flow1.5(3) | Error function | 2 | 0.5898 | 0.1233 | -1804 | 0.3511 | k=0.0402, tau=1771 |
| May-20-2026conc5_flow1.5(3) | Weibull | 2 | 0.5063 | 0.1484 | -1645 | 0.3852 | tau=3022, k=1.186 |
| May-20-2026conc5_flow1.5(3) | Klinkenberg | 2 | 0.3636 | 0.1913 | -1425 | 0.4373 | K_fa=1, K=4018 |
| May-20-2026conc5_flow1.5(3) | Fractal-BA (fractal YN) | 3 | 0.5132 | 0.1463 | -1656 | 0.3823 | k_YN0=1.545, tau=1907 |
| May-22-2026-conc10-flow0.05 | Logistic (BA/Thomas/YN) | 2 | -0.3057 | 1.372 | 727.2 | 1.171 | k_YN=0.224, tau=477.4 |
| May-22-2026-conc10-flow0.05 | Clark | 3 | -0.3072 | 1.374 | 731 | 1.172 | r=0.0406, A=1e+06 |
| May-22-2026-conc10-flow0.05 | Modified Dose-Response | 2 | -0.307 | 1.374 | 729.5 | 1.172 | a=20, t50=456.7 |
| May-22-2026-conc10-flow0.05 | Wolborska (early, C/C0<=0.15) | 2 | -0.002539 | 0.0005438 | -3899 | 0.02332 | slope=1e-06, intercept=-3.892 |
| May-22-2026-conc10-flow0.05 | Gudermannian | 2 | -0.3057 | 1.372 | 727.2 | 1.171 | k=0.1934, tau=477.5 |
| May-22-2026-conc10-flow0.05 | Error function | 2 | -0.3057 | 1.372 | 727.2 | 1.171 | k=0.08685, tau=477.4 |
| May-22-2026-conc10-flow0.05 | Weibull | 2 | -0.3069 | 1.374 | 729.4 | 1.172 | tau=466.1, k=10 |
| May-22-2026-conc10-flow0.05 | Klinkenberg | 2 | -0.3212 | 1.389 | 754.3 | 1.178 | K_fa=1, K=202.2 |
| May-22-2026-conc10-flow0.05 | Fractal-BA (fractal YN) | 3 | -0.3062 | 1.373 | 729.2 | 1.171 | k_YN0=0.9515, tau=477.4 |
| May-22-2026-conc10-flow0.1 | Logistic (BA/Thomas/YN) | 2 | -0.01073 | 7.432e-06 | -4013 | 0.002726 | k_YN=4.538e-06, tau=1e+06 |
| May-22-2026-conc10-flow0.1 | Clark | 3 | -0.006496 | 7.401e-06 | -4014 | 0.002716 | r=1e-06, A=1e+06 |
| May-22-2026-conc10-flow0.1 | Modified Dose-Response | 2 | -4.143 | 3.782e-05 | -3460 | 0.00615 | a=0.6888, t50=1e+06 |
| May-22-2026-conc10-flow0.1 | Wolborska (early, C/C0<=0.15) | 2 | -0.004709 | 7.072e-06 | -4018 | 0.002659 | slope=1e-06, intercept=-4.541 |
| May-22-2026-conc10-flow0.1 | Gudermannian | 2 | -0.01003 | 7.427e-06 | -4014 | 0.002725 | k=4.096e-06, tau=1e+06 |
| May-22-2026-conc10-flow0.1 | Error function | 2 | -15.49 | 0.0001213 | -3064 | 0.01101 | k=0.774, tau=4.389e+05 |
| May-22-2026-conc10-flow0.1 | Weibull | 2 | -4.165 | 3.798e-05 | -3459 | 0.006163 | tau=1e+06, k=0.69 |
| May-22-2026-conc10-flow0.1 | Klinkenberg | 2 | -2.632e+04 | 0.1935 | -556.4 | 0.4399 | K_fa=1, K=9832 |
| May-22-2026-conc10-flow0.1 | Fractal-BA (fractal YN) | 3 | -0.01373 | 7.454e-06 | -4011 | 0.002726 | k_YN0=4.538e-06, tau=1e+06 |
| May-22-2026-conc10_flow-0.1(2) | Logistic (BA/Thomas/YN) | 2 | -0.1798 | 1.008 | 16.99 | 1.004 | k_YN=1, tau=357.6 |
| May-22-2026-conc10_flow-0.1(2) | Clark | 3 | -0.1804 | 1.008 | 18.99 | 1.004 | r=0.04389, A=9.93e+05 |
| May-22-2026-conc10_flow-0.1(2) | Modified Dose-Response | 2 | -0.1798 | 1.008 | 16.99 | 1.004 | a=20, t50=357.5 |
| May-22-2026-conc10_flow-0.1(2) | Wolborska (early, C/C0<=0.15) | 2 | 0.05898 | 0.0005737 | -856.2 | 0.02395 | slope=0.0005998, intercept=-5.115 |
| May-22-2026-conc10_flow-0.1(2) | Gudermannian | 2 | -0.1798 | 1.008 | 16.99 | 1.004 | k=1, tau=357.6 |
| May-22-2026-conc10_flow-0.1(2) | Error function | 2 | -0.1798 | 1.008 | 16.99 | 1.004 | k=1, tau=357.6 |
| May-22-2026-conc10_flow-0.1(2) | Weibull | 2 | -0.1798 | 1.008 | 16.99 | 1.004 | tau=477, k=8.135 |
| May-22-2026-conc10_flow-0.1(2) | Klinkenberg | 2 | -0.1839 | 1.011 | 23.83 | 1.005 | K_fa=1, K=153.2 |
| May-22-2026-conc10_flow-0.1(2) | Fractal-BA (fractal YN) | 3 | -0.1804 | 1.008 | 18.99 | 1.004 | k_YN0=0.4654, tau=362.2 |

### Table 3 — Model ranking by mean Adj. R² across the 7 May runs

| Rank | Model | mean Adj.R² | median Adj.R² | n runs | validity flag |
|---|---|---|---|---|---|
| 1 | Wolborska (early, C/C0<=0.15) | 0.00657 | -0.003813 | 6 | INVALID for complete curves (early-window exponential) |
| 2 | Clark | -157.1 | -0.006496 | 7 | complete-curve model |
| 3 | Fractal-BA (fractal YN) | -255 | -0.1804 | 7 | complete-curve model |
| 4 | Error function | -262.2 | -0.1798 | 7 | complete-curve model |
| 5 | Logistic (BA/Thomas/YN) | -262.2 | -0.01073 | 7 | complete-curve model |
| 6 | Gudermannian | -263.8 | -0.01003 | 7 | complete-curve model |
| 7 | Modified Dose-Response | -475.9 | -0.1798 | 7 | complete-curve model |
| 8 | Weibull | -475.9 | -0.1798 | 7 | complete-curve model |
| 9 | Klinkenberg | -3914 | -0.3212 | 7 | CONDITIONAL (ζ≥2 & τ_K≥1 only) |

### Table 4 — Nested F-test: BA/logistic (M01) ⊂ fractal-BA (M23)

F = [(RSS₁−RSS₂)/(p₂−p₁)] / [RSS₂/(n−p₂)], recomputed from stored RSS/n/p. Valid because M23 reduces to M01 at h = 0. p < 0.05 ⇒ the fractal term is warranted.

| Run | RSS(M01) | RSS(M23) | n | F | p-value | fractal warranted? |
|---|---|---|---|---|---|---|
| May-20-2026Run2conc5_flow0.1 | 393.8 | 309.6 | 1898 | 515.5 | 3.81e-101 | yes |
| May-20-2026conc5_flow1.5 | 3.117 | 34.87 | 297 | -267.7 | 1 | no |
| May-20-2026conc5_flow1.5(2) | 1.004 | 0.953 | 45 | 2.235 | 0.142 | no |
| May-20-2026conc5_flow1.5(3) | 106.2 | 125.8 | 863 | -134.5 | 1 | no |
| May-22-2026-conc10-flow0.05 | 3141 | 3141 | 2291 | -0.0004546 | 1 | no |
| May-22-2026-conc10-flow0.1 | 0.002512 | 0.002512 | 340 | 0.0003413 | 0.985 | no |
| May-22-2026-conc10_flow-0.1(2) | 2006 | 2006 | 1993 | 0.0002374 | 0.988 | no |
# New experimental runs (3/4/5/6/8) — engineered-prompt deliverables

*Assembled from stored `breakthrough_out/` fits; no re-fitting.*

### Table 1 — Derived physical parameters (5 real runs, EC-1 to EC-6)

EC-1: ρ_b = m / (A_c · L_bed). EC-2: ε = 1 − ρ_b / ρ_p; ρ_p = 800 kg/m³ assumed (nominal PEI–SiO₂; open input — real ρ_p not yet supplied). Raw ε (EC-2) ≈ 0.16–0.18 in all runs (bulk density ~656–672 kg/m³ with ρ_p = 800); floored at 0.30 in the pipeline. **U is reliable** (depends only on Q and A_c); **v and ε-derived quantities should not be treated as physical** until ρ_p is confirmed. Outlet flow available for runs 3/4/5 (from pressure-drop table); runs 6/8 outlet = NaN — inlet flow used as operating flow per the prompt.

| Run | Q (lpm) | m (g) | L_bed (cm) | C₀ (ppm) | ρ_b (kg/m³) | ε (EC-2, floored) | U (cm/s) | v (cm/s)* |
|---|---|---|---|---|---|---|---|---|
| run 3 | 0.15 | 8.0076 | 21.0 | — | 672.0 | 0.30 (0.160 raw) | 4.406 | 14.686 |
| run 4 | 0.05 | 8.0000 | 21.3 | — | 661.9 | 0.30 (0.173 raw) | 1.469 | 4.895 |
| run 5 | 0.10 | 8.0000 | 21.2 | — | 665.0 | 0.30 (0.169 raw) | 2.937 | 9.790 |
| run 6 | 0.15 | 8.0000 | 21.5 | — | 655.7 | 0.30 (0.180 raw) | 4.406 | 14.686 |
| run 8 | 0.10 | 8.0000 | 21.5 | — | 655.7 | 0.30 (0.180 raw) | 2.937 | 9.790 |

*v computed with ε floored at 0.30. C₀ is per-run measured from the CSV plateau (see pipeline output).

### Table 2 — Model fit statistics (9 prompt models × 5 runs)

Read straight from stored `results_<run>.csv`. AdjR² < 0 means the model is worse than a horizontal line through the mean. Wolborska (M05) is fitted on the early window only (C/C₀ ≤ 0.15), so its statistics are not comparable to the complete-curve models — see Table 3 note. F-tests between non-nested models (e.g. M01 vs M04, M01 vs M14) use ΔAICc, not F-statistic; see Table 4 for the only valid nested pair (M01 ⊂ M23).

| Run | Model | p | AdjR² | χ²_ν | AICc | RMSE | key params |
|---|---|---|---|---|---|---|---|
| run 3 | Logistic (BA/Thomas/YN) | 2 | 0.9135 | 0.00425 | -2089 | 0.06519 | k_YN=0.002123, tau=507.5 |
| run 3 | Clark | 3 | 0.9386 | 0.003019 | -2219 | 0.05487 | r=0.001655, A=0.0155 |
| run 3 | Modified Dose-Response | 2 | 0.993 | 0.0003459 | -3050 | 0.0186 | a=1.178, t50=342.7 |
| run 3 | Wolborska (early, C/C0≤0.15) | 2 | 0.9253 | 0.0002692 | -19.65 | 0.01641 | slope=0.03247, intercept=-3.609 |
| run 3 | Gudermannian | 2 | 0.9191 | 0.003977 | -2115 | 0.06306 | k=0.001707, tau=500.8 |
| run 3 | Error function | 2 | 0.9052 | 0.00466 | -2054 | 0.06826 | k=0.00092, tau=515.7 |
| run 3 | Weibull | 2 | 0.9977 | 0.0001107 | -3487 | 0.01052 | tau=600.8, k=0.635 |
| run 3 | Klinkenberg | 2 | 0.3704 | 0.03093 | -1329 | 0.1759 | K_fa=1, K=1092 |
| run 3 | Fractal-BA (fractal YN) | 3 | 0.9971 | 0.00014 | -3396 | 0.01182 | k_YN0=0.3768, tau=349.9 |
| run 4 | Logistic (BA/Thomas/YN) | 2 | 0.963 | 0.003848 | -7960 | 0.06203 | k_YN=0.001549, tau=1004 |
| run 4 | Clark | 3 | 0.9811 | 0.001971 | -8918 | 0.04438 | r=0.001089, A=0.01937 |
| run 4 | Modified Dose-Response | 2 | 0.9947 | 0.0005521 | -1.074e+04 | 0.0235 | a=1.409, t50=740.7 |
| run 4 | Wolborska (early, C/C0≤0.15) | 2 | 0.9329 | 0.0001283 | -275.4 | 0.01133 | slope=0.01094, intercept=-3.393 |
| run 4 | Gudermannian | 2 | 0.964 | 0.003745 | -7999 | 0.0612 | k=0.001258, tau=996.3 |
| run 4 | Error function | 2 | 0.961 | 0.004056 | -7885 | 0.06368 | k=0.0006631, tau=1015 |
| run 4 | Weibull | 2 | 0.9996 | 4.104e-05 | -1.446e+04 | 0.006406 | tau=1202, k=0.8105 |
| run 4 | Klinkenberg | 2 | 0.03267 | 0.1007 | -3285 | 0.3173 | K_fa=1, K=1870 |
| run 4 | Fractal-BA (fractal YN) | 3 | 0.9988 | 0.0001276 | -1.284e+04 | 0.01129 | k_YN0=0.245, tau=775.7 |
| run 5 | Logistic (BA/Thomas/YN) | 2 | 0.9439 | 0.00402 | -4527 | 0.06341 | k_YN=0.003852, tau=342.6 |
| run 5 | Clark | 3 | 0.9659 | 0.00244 | -4936 | 0.04937 | r=0.002822, A=0.01721 |
| run 5 | Modified Dose-Response | 2 | 0.9934 | 0.0004729 | -6284 | 0.02175 | a=1.301, t50=236 |
| run 5 | Wolborska (early, C/C0≤0.15) | 2 | 0.9557 | 9.5e-05 | -89.13 | 0.009747 | slope=0.04379, intercept=-3.649 |
| run 5 | Gudermannian | 2 | 0.9466 | 0.003827 | -4567 | 0.06186 | k=0.003113, tau=338.6 |
| run 5 | Error function | 2 | 0.9395 | 0.004335 | -4465 | 0.06584 | k=0.00166, tau=347.6 |
| run 5 | Weibull | 2 | 0.999 | 7.204e-05 | -7829 | 0.008488 | tau=398.3, k=0.7128 |
| run 5 | Klinkenberg | 2 | 0.1797 | 0.05873 | -2325 | 0.2423 | K_fa=1, K=671 |
| run 5 | Fractal-BA (fractal YN) | 3 | 0.9975 | 0.0001806 | -7073 | 0.01343 | k_YN0=0.3754, tau=244.5 |
| run 6 | Logistic (BA/Thomas/YN) | 2 | 0.9416 | 0.003255 | -1630 | 0.05706 | k_YN=0.003949, tau=349.7 |
| run 6 | Clark | 3 | 0.9605 | 0.002204 | -1740 | 0.04686 | r=0.002847, A=0.0178 |
| run 6 | Modified Dose-Response | 2 | 0.9969 | 0.0001716 | -2469 | 0.0131 | a=1.239, t50=239.9 |
| run 6 | Wolborska (early, C/C0≤0.15) | 2 | 0.9474 | 0.0001382 | — | 0.01176 | slope=0.04009, intercept=-3.739 |
| run 6 | Gudermannian | 2 | 0.9439 | 0.00313 | -1641 | 0.05595 | k=0.003164, tau=346.7 |
| run 6 | Error function | 2 | 0.9382 | 0.003449 | -1614 | 0.05873 | k=0.001719, tau=353.3 |
| run 6 | Weibull | 2 | 0.9973 | 0.0001506 | -2506 | 0.01227 | tau=417.7, k=0.6726 |
| run 6 | Klinkenberg | 2 | 0.3249 | 0.03765 | -932.6 | 0.194 | K_fa=1, K=715.6 |
| run 6 | Fractal-BA (fractal YN) | 3 | 0.999 | 5.841e-05 | -2775 | 0.007629 | k_YN0=0.5289, tau=245.9 |
| run 8 | Logistic (BA/Thomas/YN) | 2 | 0.9416 | 0.00272 | -1504 | 0.05215 | k_YN=0.003933, tau=348 |
| run 8 | Clark | 3 | 0.9616 | 0.001788 | -1610 | 0.0422 | r=0.002901, A=0.01807 |
| run 8 | Modified Dose-Response | 2 | 0.9974 | 0.0001199 | -2300 | 0.01095 | a=1.331, t50=250.4 |
| run 8 | Wolborska (early, C/C0≤0.15) | 2 | — | — | — | — | slope=—, intercept=— |
| run 8 | Gudermannian | 2 | 0.9446 | 0.002582 | -1518 | 0.05081 | k=0.003159, tau=344.5 |
| run 8 | Error function | 2 | 0.937 | 0.002933 | -1485 | 0.05416 | k=0.001708, tau=352.2 |
| run 8 | Weibull | 2 | 0.9962 | 0.0001758 | -2203 | 0.01326 | tau=415.6, k=0.7175 |
| run 8 | Klinkenberg | 2 | 0.3689 | 0.0294 | -897.3 | 0.1715 | K_fa=1, K=696.7 |
| run 8 | Fractal-BA (fractal YN) | 3 | 0.999 | 4.834e-05 | -2531 | 0.006939 | k_YN0=0.5947, tau=253.9 |

### Table 3 — Model ranking by mean Adj. R² across 5 real runs

Note: among the full 24-model library, Fractal Error-Function (M11, Hu 2024) ranks first in 3/5 runs and second in the remaining 2 — it consistently outperforms all 9 prompt-listed models. It is not one of the 9 prompt-specified groups but is reported separately in the interpretation section.

| Rank | Model | mean Adj.R² | median Adj.R² | n runs | validity flag |
|---|---|---|---|---|---|
| 1 | Fractal-BA (fractal YN) | 0.9983 | 0.9988 | 5 | complete-curve model |
| 2 | Weibull | 0.998 | 0.9977 | 5 | complete-curve model |
| 3 | Modified Dose-Response | 0.9951 | 0.9947 | 5 | complete-curve model |
| 4 | Clark | 0.9615 | 0.9616 | 5 | complete-curve model |
| 5 | Gudermannian | 0.9436 | 0.9446 | 5 | complete-curve model |
| 6 | Logistic (BA/Thomas/YN) | 0.9407 | 0.9416 | 5 | complete-curve model |
| 7 | Wolborska (early, C/C0≤0.15) | 0.9403 | 0.9401 | 4 | INVALID for complete curves (early-window exponential only) |
| 8 | Error function | 0.9362 | 0.9382 | 5 | complete-curve model |
| 9 | Klinkenberg | 0.2553 | 0.3249 | 5 | CONDITIONAL (requires ζ ≥ 2 and τ_K ≥ 1) |

### Table 4 — Nested F-test: BA/logistic (M01) ⊂ fractal-BA (M23)

F = [(RSS₁−RSS₂)/(p₂−p₁)] / [RSS₂/(n−p₂)], recomputed from stored RSS/n/p. Valid because M23 reduces to M01 at h = 0. p < 0.05 ⇒ the fractal term is warranted. M01 vs M04/M14 are NOT nested — use ΔAICc for those comparisons (homoscedasticity caveat applies to all F-tests on bounded C/C₀ ∈ [0,1] data; see interpretation section).

| Run | RSS(M01) | RSS(M23) | n | F | p-value | fractal warranted? |
|---|---|---|---|---|---|---|
| run 3 | 1.619 | 0.05321 | 383 | 1.118e+04 | 6.15e-284 | yes |
| run 4 | 5.503 | 0.1824 | 1432 | 4.168e+04 | 0 | yes |
| run 5 | 3.293 | 0.1477 | 821 | 1.742e+04 | 0 | yes |
| run 6 | 0.9213 | 0.01647 | 285 | 1.549e+04 | 1.84e-248 | yes |
| run 8 | 0.688 | 0.01218 | 255 | 1.398e+04 | 9.32e-223 | yes |
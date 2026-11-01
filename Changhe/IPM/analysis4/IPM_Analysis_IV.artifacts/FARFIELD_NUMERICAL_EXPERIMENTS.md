# Numerical experiments: the stationary far-field series for self-similar IPM

Status: final for this campaign (all computations finished 2026-10-31T22:59Z); updated 2026-10-31T23:04Z (sections 5.11, 5.11b, 5.13b, 5.13c and 6 carry the final state). Run start T0 = 2026-10-31T01:57:42Z. All numbers below are finite-order
computations; none is a proof of convergence of the infinite series. Classification per item: NUMERICAL EVIDENCE unless
marked PROVED (exact finite arithmetic identities) or CONJECTURAL.


File references of the form code/..., logs/..., notes/..., jobs/... and ckpt/... are relative to the numerics/ folder of the accompanying artifacts; outputs of the theory part (for example tq_cert_Q6.out) are in its theory_code/ folder (subfolder tuned/).

## 1. Setting and conventions

rho = sum_n r^{p_n} f_n(theta), psi = sum_n r^{p_n+1} g_n, chi = sum_n r^{p_n+3} C_n, p_n = 1 - n delta, delta = 1 - 1/c_l,
rho = -d_y Lap chi, psi = chi_xy, u = (-psi_y, psi_x), equation (c_l X + u).grad rho - rho = 0.
f_n = sum_k a_{n,k} sin((2k+1)theta), g_n = sum_{j>=1} b_{n,j} sin(2j theta), C_n = sum_m c_{n,m} cos(2m theta).
Poisson inverse (prompt eq. 4) and recursion (prompt eq. 5) exactly as in the conventions of the theory report (same signs, same
ordered convolution). z = r^{-delta}; r^{-gamma} rho = sum z^{n-1} f_n.
Norms: alpha_n = ||f_n||_l1 = sum_k |a_{n,k}|; l2 = (sum a_k^2)^{1/2}; L2 = sqrt(pi) l2 = ||f_n||_{L2(0,2pi)};
Linf = grid sup (8 points per harmonic, indicative); A_sigma = sum |a_k| exp(sigma(2k+1)); beta_n = ||g_n||_l1,
beta'_n = ||g_n'||_l1; Lambda_n = max(beta'_n, |p_n+1| beta_n)/alpha_n; d_n = dist(n delta, 2Z); y_n = n alpha_n/d_n.
Amplitude: f_1 -> eps f_1 gives f_n -> eps^n f_n exactly, so results are quoted for the stated amplitude and the
convergence radius scales as 1/eps. Unit amplitude means a_{1,0} = 1 for sin(theta).

## 2. Implementation (code/)

- ffcore.py: coefficient lists; products g f' and g' f by two polynomial multiplications each (sum and difference
  frequencies), with python-flint fmpq_poly (exact), arb_poly (ball arithmetic, rigorous error radii, precision chosen
  per run), or numpy float64 (smoke tests only). Bandwidth is adaptive: K_n = len(f_n) - 1 grows exactly as n(K_1+1)-1.
  The angular band is never fixed: every order carries its full bandwidth K_n = n(K_1+1)-1 (pure series) and the full
  frequency support of the products (log series), so the computations are not subject to the fixed-band caution of the
  verifier's (fixed angular cutoffs converge for every delta and cannot show small-divisor divergence).
  Poisson inverse mode by mode; exact resonances (decided exactly from the rational parameter) are detected: the mode is set
  to zero (canonical free multipole) and the compatibility numerator recorded with three statuses (compatible = exactly zero,
  incompatible = certified nonzero, open = ball containing zero -> error); a run stops at the first incompatible resonance.
  In arb a denominator ball containing zero without a proven exact resonance raises an error (precision failure). Chi reconstruction C_n from f_n (downward triangular solve; raises at p_n = -1).
  Checkpoints: pickled state (all f_i, g_i, stats) every k orders; restart with --resume.
- run_recursion.py: CLI driver (ring, precision, c_l as exact rational string or 'sqrt5' or 'cand007', f_1 spec, N).
- extract007.py: exact extraction of (c_l, f_1) from Candidate 007 and comparison with its branches 2..8.
- check_chi_sympy.py: independent direct substitution into the chi equation (sympy, exact).
- fit_growth.py, analyze_log.py: ratio/root fits. evaluate_series.py: section 13 (truncated sums and residuals).
- resonance_report.py, resonance_scan.py, prime_congruence_check.py: exact compatibility coefficients at resonant orders.
- logff.py: logarithmic series at rational delta (canonical normalization B_(n,j)(0) = 0); per-pair block products by Kronecker
  substitution (exactly equal to the column-pair version in fmpq tests); --resume from checkpoints; statistics per t-power for
  density and stream columns. logseries_table.py: per-order tables. theoremE_constants_arb.py: ball-arithmetic certificate.
- export_coeffs.py: compact float64 export (with log10 scales) of checkpoints for the artifacts.
Cost: order n needs n-1 pairs of polynomial products of degree about n K_1; a 512-bit run of sin(theta) to N = 362
took 3 minutes on one core; Candidate 007's profile (K_1 = 9) to N = 227 took 25 minutes at 512 bits.

## 3. Validation (PROVED finite identities / exact agreement)

- Grid tests of the product identities and of -(g'' + (p+1)^2 g) = p cos f - sin f' (errors 1e-13, float).
- Sympy direct substitution (check_chi_sympy.py): c_l = 9/5 with f_1 = sin + sin3/3 (N = 4); c_l = 7/4 with
  f_1 = 2 sin - sin3/5 + sin5/7 (N = 3); c_l = 2 with sin + sin3/2 (N = 3). In each case every r^{p_n}, n <= N, cancels
  identically and the first surviving sector equals +N(c_l-1) f_{N+1}(theta) (the forcing of order N+1). ALL PASS.
- Candidate 007: my exact recursion from its exact (c_l, f_1) reproduces its stationary branches j = 1..7 (orders 2..8)
  exactly, all rational coefficients equal (10n harmonics at order n, highest index K = 10n - 1, i.e. 19, 29, ..., 79). This is an independent code path
  (the source used Cartesian differentiation of homogeneous potentials).
- Precision: exact vs 512-bit (orders 1..19): identical to 16 digits; 256 vs 512 bits: identical through order 110,
  relative difference 6e-13 at order 115 where the 256-bit rigorous coefficient-wise relative radius reached 1.3e-6 (run stopped
  by the then stop rule max_rel_rad > 1e-6; since 02:44Z the rule uses the norm-relative radius rad_over_max > 1e-6). Rigorous radii grow by about 10^0.6 per order for the 007 profile and 10^0.4
  per order for sin(theta); precision is chosen so that the radius stays below 1e-6 relative at the target order.

## 4. Candidate 007 leading data (exact)

c_l = 4076476460239181/2251799813685248 = 1.810319210199998, gamma = 0.5523887689892676, delta = 0.44761123101073247,
delta = 1824676646553933/4076476460239181 in lowest terms (odd/odd): first exact stream resonance at n = 2*4076476460239181.
f_1 = sum_{k=0}^{9} a_k sin((2k+1)theta) with a = (18.56782229755, 2.107321631475, 0.6247347944873, 0.1511119117034,
-0.1016674009550, 0.02814322689785, 0.002309093254678, 0.0003658523972799, -0.0008585850168560, 0.001896735774558)
(exact rationals of about 280 bits in notes/cand007_f1.json). Quarter-circle L2 norm 16.571000263028825 (manifest
Theta_0 quarter_norm 16.57100026302882); alpha_1 = 21.586; Linf = 16.826 at theta = 0.454 pi. Positive on (0, pi),
one interior maximum on (0, pi/2) (not monotone), symmetric about pi/2 (odd harmonics only).

## 5. Experiments (per-order logs in logs/<tag>.jsonl, checkpoints in ckpt/<tag>.pkl)

### 5.1 f_1 = sin(theta), unit amplitude
| tag | c_l | delta | ring | N reached | L (l2 fit) | a (l2 fit) | rms | root_N (l2) |
|---|---|---|---|---|---|---|---|---|
| sin1_c007_arb512 | 007 rational | 0.447611 | arb 512 | 362 (radius stop) | 0.4676 | - | - | 0.454 |
| sqrt5_sin1_p1024 | (5+sqrt5)/4 | 0.447214 | arb 1024 | 700 (finished; the fits of 5.8 and 5.10 use orders <= 625) | 0.46821 | 2.031 | 2e-7 | 0.4537 |
| sin1_cl9_5_p1024 | 9/5 (arb) | 4/9 | arb 1024 | 500 | (ARTIFICIAL: b = 0 continuation after the failed exact resonance at n = 9; not a solution; excluded) | | | |
| nearres_eps1e-3_p512 | 1000/599 | 0.401 | arb 512 | 120 | 0.5597 | 2.06 | 1.3e-4 | 0.514 |
Ratio law: l2 ratio = L (1 - a/n) with a = 2.03 to rms 2e-7 over the second half of the orders (fit_growth.py); with the
statistics recomputed in scaled arithmetic (code/regen_log.py) the sqrt5 run gives L = 0.468205, a = 2.028, rms 7e-8 at N = 625.
Runs at rational c_l with an exact resonance below N (c_l = 9/5, 5/3, 2, 10/7, 20/13, 20/11, 19/10) are ARTIFICIAL b = 0
continuations beyond their first failed resonance and are excluded from all growth tables; new runs stop at that order.
The l1 (alpha_n) ratio gives the same L with a = 1.82-1.85 and rms 1e-3 (l1 is less smooth).
Dominant mode index argmax_k = 0.74 n (frequency 1.5 n); max frequency 2n - 1; min active |4j^2 - P_n^2| fluctuates
(logged 2|4j^2 - P^2|: 0.23 at n = 9; 10.5 at n = 125; 352 at n = 252) with no visible effect on the smooth ratio for this profile.
Lambda_n in 0.6..1.2; y_n = n alpha_n/d_n decays geometrically with fluctuations from d_n.

### 5.2 Candidate 007 profile at its own c_l (alpha_1 = 21.586)
| tag | ring | N | L2 ratio (n -> n+1) | root test (L2)^(1/n) | notes |
|---|---|---|---|---|---|
| c007_exact | fmpq | 23 (stopped; exact arithmetic too slow beyond this order) | 2.4-3.2 (n <= 9), 15.9 at n = 10 | 2.5-3.1 | 21477 bits at n = 8, 42k bits at n = 11 |
| c007_arb512 | arb 512 | 233 (finished; superseded by c007_p2048) | oscillates 1.9..5.2 | 3.12 (10), 2.96 (20), 3.17 (40), 3.26 (50), 3.34 (70), 3.36 (90), 3.46 (208) | rel radius 1e-83 at n = 115 |
| c007_arb256 | arb 256 | 115 (radius stop) | same values as 512 to 1e-13 | | precision check |
| c007_p2048 | arb 2048 | 500 (finished 19:27Z) | agrees with c007_arb512 to 1e-15 through 233; the verifier audited every stored 2048-bit coefficient ball, the exact inputs and every differential Poisson identity through 390 in 2304-bit arithmetic (independently checked), and checked the full Cartesian nonlinear convolution at orders 2, 3, 6, 10, 20, 40, 80, 160, 233, 300, 390 at 2304 bits (independently checked); this is an audit of the stored coefficients, not an independent regeneration of all of them | 3.479 at N = 396 (verifier: l2 root 3.4797, l1 root 3.4985 at 390); at N = 500: l1 root 3.5113, l2 root 3.4990, max-coefficient root 3.4953; l1 roots 3.4981 (400), 3.5078 (450), 3.5111 (480), 3.5113 (500) | root test still rising slowly: +0.013 (l1) from 400 to 500; code/fit_growth.py at 500: ratio fit L = 3.66 (l1; rms 0.7, the ratio oscillates 2..5 after the small divisors), 10-step smoothed ratio 3.47 (N/2) and 3.52 (N); relative radius 10^-301 at 500 (rigorous through 500) |
The jump 15.9 at n = 10 is the near-resonance 9 delta = 4.0285 (quadratic divisor |4j^2 - P_9^2| = |4 - 2.0285^2| = 0.1148 at
j = 1; the logged min_active_den is 2|4j^2 - P^2| = 0.2296): g_9 is amplified accordingly and f_10 inherits it. Root test still rising at N = 227; smoothed 10-step ratio 3.34 (N/2), 3.56 (N).
If the root test settles near 3.5, the series converges (in L2 angular norm) for z < 0.29, i.e. r > 3.5^{1/delta} = 16.

### 5.3 Exact resonances, rational delta (fmpq; PROVED finite facts, notes/resonance_report.json)
| c_l | delta | f_1 | first stream resonance n (j) | a_{n,j-1} (must be 0 for compatibility) | chi-level n delta = 2 |
|---|---|---|---|---|---|
| 2 | 1/2 | sin | 8 (1) | 126709539517/969699666604032000 = 1.3067e-7 (exact; verifier's forcing value is -2j times this) | n = 4: f_4(pi/2) = 359/401310 != 0 |
| 9/5 | 4/9 | sin | 9 (1) | 4.1801e-8 (exact in file) | none |
| 5/3 | 2/5 | sin | 10 (1) | -1.1701e-7 (exact in file) | n = 5 |
| 5/3 | 2/5 | sin + sin3/2 | 10 (1) | -5.9636e-3 | n = 5: f_5(pi/2) = 4.2447e-2 != 0 |
| 20/11 | 9/20 | sin | 40 (8) | -2.3817e-21 (exact in file; the independent verifier agrees) | none |
| 5/3 | 2/5 | Candidate 007 f_1 | 10 (1) | 3.1343e+4 (alpha_10 = 7.6e2 at n = 5; exact in file) | n = 5: f_5(pi/2) = -694.0 != 0 |
| 9/5 | 4/9 | Candidate 007 f_1 | 9 (1) | -8.5962e+2 (exact in file) | none |
Conclusion (PROVED for these inputs): the pure power ansatz is obstructed at the first exact resonance; no tested
sin(theta) profile satisfied the compatibility condition (and the verifier's audited congruence kappa == (-1)^((a-4)/2) mod p
proves kappa != 0 for every delta = a/p with p an odd prime >= 5 and even 4 <= a < p, which is consistent with all 21 prime
cases of the scan), except the support-selected profiles found by the verifier (independently checked): at c_l = 9/5,
f_1 = sin(11 theta) and sin(13 theta) have a_{9,0} = 0 exactly (first resonance compatible), but with the canonical choice
b_{9,1} = 0 the second resonance n = 18 (j = 3) is incompatible for both (kappa = a_{18,2} = +2.2055e-4 and +2.666e-5, exact in
this implementation; confirmed by the independent verifier): obstructed one period later (with the free stream amplitude at n = 9 fixed to zero). Orders beyond the first failure in these runs are the b = 0 continuation
and carry no meaning as a solution. Verifier's independent exact values agree (theirs = -2j times mine).

### 5.4 Near resonance delta = 2/5 + eps, f_1 = sin(theta), arb 512, N = 120
(The companion run at eps = 0, c_l = 5/3 in arb, is an artificial b = 0 continuation after n = 10 and is not used.)
| eps | c_l | divisor at n = 10 | beta_10 = ||g_10||_l1 | alpha_11 | alpha_120 |
|---|---|---|---|---|---|
| 1e-3 | 1000/599 | 1.0e-2 | 8.35e-6 | 2.47e-5 | 8.8e-35 |
| 1e-6 | 1000000/599999 | 1.0e-5 | 5.85e-3 | 1.78e-3 | 2.1e+19 |
| 1e-9 | 10^9/599999999 | 1.0e-8 | 5.85 | 1.755 | 1.5e+84 |
beta_10 and alpha_11 scale like 1/eps (asymptotically constants/eps; the three samples agree with this to 3 digits); the near-resonant orders are n = 5m, m >= 2 (10, 15, 20, ...), not only the multiples of 10 as an earlier version of this
paragraph said; the verifier's exact computation (independently checked) shows that the stream coefficients at 10, 15, 20 have poles in eps of order 1, 2, 3
with constants R/20, R sigma_2/600, R sigma_2 sigma_3/24000, so the amplification compounds from resonance to resonance (the earlier conjecture of a
single constant factor exp(1/(10 eps)) is withdrawn). Finite observation: for eps = 1e-3 the per-order ratio had returned to its smooth law by n = 120.

### 5.5 Direct evaluation (section 13), sin(theta) at 007's delta, unit amplitude (code/evaluate_series.py)
sup over theta of R^{-gamma} |(c_l X + u_N).grad rho_N - rho_N| for the truncation at order N (E_n for N < n <= 2N
computed from the same coefficients; orders <= N cancel identically):
| N | R = 1 (z = 1) | R = 2 | R = 4 | R = 8 | d/dtheta residual at R = 1 | tail z^N sup|f_{N+1}| at R = 1 |
|---|---|---|---|---|---|---|
| 10 | 2.4e-5 | 1.1e-6 | 5.0e-8 | 2.3e-9 | 3.4e-4 | 3.2e-6 |
| 20 | 6.8e-9 | 1.4e-11 | 2.9e-14 | 5.9e-17 | 2.0e-7 | 4.6e-10 |
| 40 | 1.0e-15 | 4.2e-21 | 1.7e-26 | 7.2e-32 | 5.9e-14 | 3.4e-17 |
| 80 | 3.6e-29 | 6.2e-40 | 1.0e-50 | 1.8e-61 | 4.3e-27 | 6.1e-31 |
Partial sums R^{-gamma} rho_N(R, theta) at R = 1: 0.21796078 (theta = 0.3), 0.60603445 (0.9), 0.77841471 (1.3),
stable to 8 digits from N = 20 on. The decay rate per order is L = 0.47 at z = 1, as predicted by the ratio law.
No cancellation problems: the evaluation uses float64 on the arb midpoints (terms decrease geometrically).

### 5.6 Shape dependence of L at Candidate 007's delta (arb 512, N = 200, l2 fit; unit leading amplitude unless stated)
| f_1 | alpha_1 | L | a | L/alpha_1 |
|---|---|---|---|---|
| sin | 1 | 0.4676 | 2.03 | 0.468 |
| sin + 0.2 sin3 | 1.2 | 0.511 | 1.58 | 0.426 |
| sin + 0.5 sin3 | 1.5 | 1.891 | 1.68 | 1.26 |
| sin + sin3 | 2 | 4.245 | 1.69 | 2.12 |
| sin - 0.2 sin3 | 1.2 | 1.408 | 1.74 | 1.17 |
| sin - 0.5 sin3 | 1.5 | 2.822 | 1.72 | 1.88 |
| sin - sin3 | 2 | 5.178 | 1.71 | 2.59 |
| sin3 | 1 | 4.711 | 1.69 | 4.71 |
| sin5 | 1 | 2.424 | 1.73 | 2.42 |
| sin7 | 1 | 2.232 | 1.74 | 2.23 |
| sin + 2 sin3 | 3 | 8.956 | 1.70 | 2.99 |
| sin - 2 sin3 | 3 | 9.890 | 1.71 | 3.30 |
| sin - 0.1 sin3 | 1.1 | 0.935 | 1.76 | 0.85 |
| sin + 0.05 sin3 | 1.05 | 0.319 | 2.00 | 0.304 |
| sin + 0.06 sin3 | 1.06 | 0.292 (N = 287) | 2.00 | 0.276 |
| sin + 0.08 sin3 | 1.08 | 0.251 (N = 265; rms 1e-3; root test 0.243) | 0.64 | 0.232 |
| sin + 0.12 sin3 | 1.12 | about 0.30 (N = 276; spiky; root 0.291) | | 0.27 |
| sin + 0.14 sin3 | 1.14 | about 0.34 (N = 320; spiky; root 0.338) | | 0.30 |
| sin + 0.16 sin3 | 1.16 | about 0.39 (N = 320; spiky; root 0.380) | | 0.34 |
| sin + 0.18 sin3 | 1.18 | about 0.44 (N = 320; root 0.423) | | 0.37 |
| sin + 0.1 sin3 | 1.1 | about 0.25 (N = 274; smoothed 10-step ratio 0.253, root test 0.245; spiky ratio sequence, dominant mode switching) | | 0.23 |
| sin + 0.3 sin3 | 1.3 | 0.956 | 1.65 | 0.735 |
| 18.57 sin - 2.107 sin3 + 0.625 sin5 (007 first 3 harmonics, sign of sin3 flipped) | 21.30 | 20.30 | 1.74 | 0.953 |
| 007 profile, first 1 harmonic (18.57 sin) | 18.57 | 8.68 (exact by homogeneity) | 2.03 | 0.468 |
| 007 profile, first 2 harmonics | 20.68 | 5.2 (ratio irregular) | | 0.25 |
| 007 profile, first 3 harmonics | 21.30 | 3.80 | | 0.178 |
| 007 profile, first 5 harmonics | 21.55 | 3.52 | | 0.163 |
| 007 profile, all 10 harmonics | 21.59 | about 3.5 (root test 3.46 at N = 233, rising) | | 0.16 |
L is a degree-1 homogeneous but strongly shape-dependent functional of f_1: adding a sin3 component of either sign
increases L for a <= -0.1 or a >= 0.2 (for |a| >= 0.5 by factors 4 to 11), while a SMALL POSITIVE a decreases L: 0.319, 0.292,
0.251, about 0.25, about 0.30, 0.51 at a = 0.05, 0.06, 0.08, 0.10, 0.12, 0.20 against 0.468 at a = 0: the minimum of L over the
two-mode family is about 0.25 near a = 0.08..0.10, where the ratio sequence becomes spiky (two growth mechanisms of comparable
strength; the dominant mode index switches between 0 and about 0.2 n). Candidate
007 has a_1/a_0 = +0.113, in this favourable direction, and its higher harmonics decrease L by a factor 2.5 relative to its
leading harmonic alone (saturating at 5 harmonics); flipping the sign of its sin3 component raises L from 3.8 to 20.3. CONJECTURE: profiles close to the far field
of an actual solution have a comparatively small L; a minimization of L over shapes was not attempted.

### 5.6b Three-mode family sin + a sin3 + b sin5 at 007's delta (arb 512, N = 200, unit leading amplitude)
| a | b | L (fit / smoothed 10-step / root test at N) | remark |
|---|---|---|---|
| 0.08 | -0.03 | 0.343 / 0.339 / 0.325 | clean (a = 1.96) |
| 0.08 | 0 | 0.253 / 0.250 / 0.241 | |
| 0.08 | 0.03 | 0.254 / 0.225 / 0.229 | spiky |
| 0.08 | 0.06 | 0.37 / 0.354 / 0.350 | spiky |
| 0.11 | -0.03 | 0.364 / 0.360 / 0.343 | |
| 0.11 | 0 | 0.270 / 0.273 / 0.263 | |
| 0.11 | 0.03 | 0.171 / 0.171 / 0.166 | smallest L found |
| 0.11 | 0.06 | 0.18 / 0.260 / 0.259 (N = 97, radius stop) | spiky |
Candidate 007's leading profile has a_1/a_0 = 0.1135 and a_2/a_0 = 0.0336: its first three harmonic ratios coincide with the
best tested grid point of this small family (L/a_0 = 3.5/18.57 = 0.19 for the full 007 profile, 0.17 for (1, 0.11, 0.03)); the
12-point grid does not locate a minimizer over the continuous family, let alone over all profiles. The
growth constant per unit leading amplitude is therefore about 2.7 times smaller for 007-like shapes than for pure sin(theta)
and 25 times smaller than for sin(theta) + sin(3theta). CONJECTURE (suggested by the grid, not established): the far field of an actual solution has a leading profile
with a small growth constant of the recursion among profiles with the same leading amplitude.

### 5.6c Candidate 007 profile with one Fourier coefficient rescaled (arb 512, N = 200, own c_l; prompt section 12 item 2)
| change | L (fit / smoothed 10-step / root test) |
|---|---|
| sin3 coefficient x 0.5 | 8.44 / 8.37 / 8.08 (clean ratio) |
| sin3 coefficient x 0.75 | about 5.3..5.8 (spiky) / 5.31 / 5.12 |
| sin3 coefficient x 1 (original) | about 3.5 (root test 3.46 at N = 233) |
| sin3 coefficient x 1.25 | about 5.1..5.6 (spiky) / 5.36 / 5.14 (N = 200) |
| sin3 coefficient x 1.5 | 7.33 / 7.27 / 7.04 (clean ratio) |
| sin5 coefficient x 0.5 | about 5.0 (spiky) / 4.97 / 4.72 (N = 196) |
| sin5 coefficient x 1.5 | 4.05 / 4.12 / 3.99 (N = 200) |
Rescaling the sin3 component in either direction increases the finite-order growth statistics at N = 200 (x 0.5: 8.4, x 0.75: 5.3,
x 1: 3.5, x 1.25: 5.3, x 1.5: 7.3), and rescaling the sin5 component raises them too (x 0.5: about 5.0, x 1.5: about 4.0); the original
coefficients give the smallest values among the tested rescalings (finite statistics, N = 200). The theory part's structural reading (theory 8.3, verifier): positive sin3 and sin5 components cancel the low stream
modes; the exact cancellation family (ratios 0.1260, 0.0555, 0.0327, 0.0221 at the stored gamma) converges to the zero-velocity
shear sign(y)|y|^gamma, and 007's profile is a smooth perturbation of it with a sin(2theta) stream mode 10 times smaller than for
sin(theta). Runs of the family truncations K = 1, 2, 3, 5, 9 at the stored c_l (exact inputs from the verifier's, copied to
notes/shear_family_K*.json; arb 512, N = 200, unit sin theta coefficient; tags shear_K*_c007_p512):
| K | ratios of the first harmonics | root test (l2)^(1/N) at N = 100 / 200 | smoothed 10-step ratio at N |
|---|---|---|---|
| 1 | 0.1260 | 0.2899 / 0.3001 | 0.315 |
| 2 | 0.1260, 0.0555 | 0.2197 / 0.2245 | 0.238 |
| 3 | 0.1260, 0.0555, 0.0327 | 0.1963 / 0.2015 | 0.209 |
| 5 | + 0.0221, ... | 0.1763 / 0.1802 | 0.189 |
| 9 | ... | 0.1511 / 0.1555 | 0.166 |
Both finite statistics (the root test and the smoothed ten-step ratio) decrease across the five tested values K = 1, 2, 3, 5, 9 (the theory part's
double-precision values at delta = 1/sqrt5: 0.304, 0.230, 0.207, 0.185, 0.162 at N = 200, within a few percent); this is a statement about
finite statistics at N = 200, not about the growth constant itself; the ratio sequences are spiky (rms of the fit 0.03..0.3), as for the 007 profile.

### 5.7 Location of the dominant z-singularities: OPEN (an earlier inference withdrawn)
The modulus of the nearest singularities is estimated as 1/L with the fitted L (ratio and root tests through the computed orders;
Pade pole moduli 2.17..2.24 against 1/L = 2.14); a rigorous LOWER bound for the growth constant from the top Fourier mode
(verifier): L >= 1/R_top = 0.3896 at delta = 1/sqrt5 for sin(theta) (observed 0.468).
An earlier inference from the first two correlation lags of consecutive normalized coefficient vectors (|<f_n,f_{n+1}>| = 0.242,
|<f_n,f_{n+2}>| = 0.877, read as a fixed rotation by 76 degrees and hence a complex conjugate pair of singularities) was
REFUTED by the verifier (independently checked, 2048-bit interval check on the same checkpoints): the lag-64 correlation is -0.030 where a fixed
rotation predicts -0.977, and orders 636 and 700 are at distance 0.9995 and 0.99999999 from the span of orders 572, 573.
The signed-max normalization also cannot carry phase information. Pade approximants of the scalar functional a_{n,0} give
pole arguments that change with the approximant order (+-86, +-116, +-150 degrees at [50/50]). Therefore: the argument of
the dominant singularities, and whether a singularity lies on the positive real z axis at |z| = 1/L, are OPEN. The sign of
the dominant coefficient of f_n alternates with n (339 changes in 361 steps for sin theta), and the ratio-law exponent a = 2.03
corresponds to coefficients ~ n^{-2} (CONJECTURAL singularity type (1 - z/z_0) log(1 - z/z_0)).

### 5.8 Comparison with the theory part's Theorem A constants (delta = 1/sqrt5, f_1 = sin theta, N = 625)
(n alpha_n)^{1/n} = 0.4645 at N = 625 (limit L = 0.4682); limsup y_n^{1/n} = L (y_n = n alpha_n/d_n differs from alpha_n by
polynomial factors; smallest d_n = 0.0014 at n = 161); Lambda_n in 0.74..0.75 for n >= 300. Rigorous A < 84218 of Theorem A
exceeds the observed growth constant by 1.8e5. For the 007 profile the relevant rigorous constants are A < 12725638 at
delta = 1/sqrt5 (Theorem A/D) against the observed (n alpha_n)^{1/n} = 3.605 at N = 300 (run sqrt5_c007f1_p1024, alpha_1 = 21.586;
l2 root test 3.513; factor 3.5e6), and A_rat < 13178350 for the finite prefix n < 8.15e15 at the stored rational c_l (Theorem E) against the observed
root test 3.46 at N = 233 there.

### 5.9 Exact kappa scan for Theorem C hypothesis (H) (code/resonance_scan.py, fmpq)
f_1 = sin(theta): all 55 rationals delta = A/B in (0.40, 0.50) with first stream resonance n0 <= 60 give kappa = a_{n0,j0-1}
!= 0, with |kappa|/alpha_{n0} between 4e-6 and 4e-3 (exact values in notes/resonance_scan_sin1.json). This statement is
about f_1 = sin(theta) only: for other inputs compatible first resonances exist (independently checked; section 5.3). 007 profile at the
rationals with n0 <= 17: notes/resonance_scan_cand007.json. PROVED finite facts for the listed rationals; no kappa = 0 found.
Independent arithmetic check of the verifier's congruence (code/prime_congruence_check.py, exact fmpq recursion to n = p): for all
122 rationals delta = a/p with p prime, 5 <= p <= 61, a even, delta in (0.25, 0.75), the residue of kappa modulo p equals
(-1)^((a-4)/2) (notes/prime_congruence_sin1.json: 122 OK, 0 mismatch, 0 skipped). The 007-profile version (kappa == alpha_1 (-1)^((a-4)/2)
mod p, with alpha_1 = a_{1,0} of Candidate 007) holds in all 29 cases with p <= 29 (notes/prime_congruence_cand007.json).
Size of kappa (theory part's hypothesis (H_kappa)): log10|kappa|/p for the 122 exact cases lies in [-1.008, -0.214]; the mean over a at fixed p
rises from -0.929 (p = 7) to -0.514 (p = 61) and the minimum over a lies in [-1.008, -0.822]. Ball-arithmetic extension (code/kappa_scan_arb.py,
256 bits, all kappa certified nonzero): per-prime mean / min of log10|kappa|/p = -0.530/-0.880 (p = 67), -0.506/-0.841 (71), -0.523/-0.863 (73),
-0.500/-0.848 (79), -0.514/-0.879 (83), -0.509/-0.876 (89), -0.503/-0.867 (97), -0.485/-0.834 (101), -0.483/-0.856 (103), -0.494/-0.858 (107), -0.480/-0.840 (109), -0.494/-0.867 (113), -0.473/-0.852 (127), -0.482/-0.852 (131), -0.479/-0.866 (137), -0.481/-0.849 (139), -0.465/-0.846 (149), -0.465/-0.853 (151); p = 157 partial (a = 40..78 only, 20 of the 40 cases, when the 90-minute budget ended): min -0.460. Final scan: 502 cases, 7 <= p <= 157 together with the exact cases, all kappa certified nonzero (ball radii at most 1e-78 relative to values of order 10^-60 and smaller); log10|kappa|/p over the 482 complete-prime ball cases lies in [-0.880, -0.093] (the maxima over a at fixed p, attained at the smallest even a, rise from -0.208 at p = 67 to -0.106 at p = 151) (notes/kappa_scan_arb.jsonl, logs/kappa_scan_arb.out). So |kappa| is about 10^(-0.5 p) on average over a and never below 10^(-0.88 p) in the scanned range; the per-prime means drift slowly upward with p (-0.53 at 67 to -0.465 at 151). Finite facts for the listed (p, a) only.

Odd numerators (theory part's theory 10.1; code/kappa_odd_check.py, exact fmpq, notes/kappa_odd_check_sin1.out): for delta = a/p with p in {5, 7, 11, 13, 17, 19, 23}
and 3 <= a < p odd (37 pairs), f_1 = sin theta, the first stream resonance is at n0 = 2p, j0 = a - 1, and the compatibility coefficient kappa_odd = a_(2p, a-2)
(coefficient of sin((2a-3) theta) in f_(2p)) is nonzero in all 37 cases, with p-adic valuation -2, -1 or 0 (0 only at (11, 5)); the p-adic digits at valuations
-4..1 agree with the theory part's independent computation (code/oddnum/digits_sin1.out) in all 37 cases (PROVED finite facts, two independent exact implementations).

### 5.10 Dependence of L on delta for f_1 = sin(theta), unit amplitude (arb 512/1024, l2 fits; non-resonant parameters only)
| delta | c_l | N | L | a | L (c_l - 1) | source |
|---|---|---|---|---|---|---|
| 0.2501 | 1.33351 | 300 | 1.0810 | 2.13 | 0.3605 | dsw2_sin1_d2501 |
| 0.31235 | 1.45420 | 300 | 0.8066 | 2.10 | 0.3664 | dsw4_sin1_d31234567 |
| 0.36235 | 1.56822 | 300 | 0.6528 | 2.07 | 0.3710 | dsw4_sin1_d36234567 |
| 0.41235 | 1.70168 | 268 | 0.5354 | 2.05 | 0.3757 | dsw4_sin1_d41234567 |
| 0.46235 | 1.85992 | 300 | 0.4423 | 2.01 | 0.3803 | dsw4_sin1_d46234567 |
| 0.51235 | 2.05064 | 300 | 0.3654 (rms 8e-3, 0.0123 from 1/2) | 1.36 | 0.3839 | dsw4_sin1_d51234567 |
| 0.3001 | 1.42878 | 300 | 0.8518 | 2.11 | 0.3652 | dsw2_sin1_d3001 |
| 0.3501 | 1.53870 | 300 | 0.6866 | 2.08 | 0.3699 | dsw2_sin1_d3501 |
| 0.4010 | 1.66945 | 120 | 0.5597 | 2.06 | 0.3747 | nearres_eps1e-3 (delta = 2/5 + 1e-3) |
| 0.44598 | 1.805 | 458 | 0.4704 | 2.03 | 0.3786 | sin1_cl361_200_p1024 |
| 0.44721 | 1.809017 (sqrt5) | 625 | 0.46821 | 2.03 | 0.3788 | sqrt5_sin1_p1024 (regen) |
| 0.44761 | 1.810319 (007) | 362 | 0.4676 | 2.03 | 0.3788 | sin1_c007_arb512 |
| 0.44904 | 1.815 | 500 | 0.4632 | 2.03 | 0.3775 | sin1_cl363_200_p1024 |
| 0.45010 | 1.818512 | 300 | 0.4631 | 2.03 | 0.3791 | dsw2_sin1_d4501 |
| 0.45055 | 1.82 | 182 (stopped: exact resonance 182 delta = 82) | 0.4624 | 2.03 | 0.3791 | sin1_cl91_50_p1024 |
| 0.45058 | 1.8201 | 300 | 0.4623 | 2.03 | 0.3791 | dsw3_sin1_cl18201_10000 |
| 0.47371 | 1.9001 | 300 | 0.4236 | 2.03 | 0.3813 | dsw3_sin1_cl19001_10000 |
Across the tested non-resonant values the fitted L decreases with delta and L (c_l - 1) increases slowly from 0.36 to 0.38 (finite fitted estimates at these parameters only: the actual limsup ||f_n||^(1/n) is, by Theorems A and C*, finite at Brjuno points and infinite on a dense set of irrationals, hence discontinuous at every Brjuno point, verifier), so the natural scale of the fitted L is 1/(c_l - 1)
(the prefactor of the recursion). Runs at delta within about 1e-4 of a rational with small denominator (0.4001, 0.5001, 0.5501,
0.6001, 0.6501, 0.7001, and c_l = 1.7501, 1.8001, 2.0001 whose delta are within 3e-5 of 3/7, 4/9, 1/2) have irregular ratios up
to N = 300 with inflated finite-order growth (e.g. smoothed ratio 0.544 at c_l = 1.8001 against the smooth value 0.471) because of the near-resonances at the multiples of the
rational's resonance order (divisors 10 m 1e-4 etc.); they are not used for L. A sweep at quasi-irrational delta (d + 0.01234567)
is queued (dsw4_*).
Effect of c_l on the Candidate 007 profile (1024 bits, N = 250): root test (l2)^(1/N) at N = 250 is 3.72 at c_l = 1.805
(delta = 0.44598; the near-resonance 9 delta = 4.0138 has divisor 0.0138 instead of 0.0285 and the ratio sequence is very
irregular), 3.44 at c_l = 1.815 (delta = 0.44904), 3.46 at the stored c_l (N = 233), and 3.51 at delta = 1/sqrt5 (N = 300, smoothed
10-step ratio 3.53; run sqrt5_c007f1_p1024, finished). So the growth constant of the 007 profile is about 3.4 to 3.7 for all four nearby
parameters, with the finite-order ratio sequence shaped by the small divisors of the low modes it populates. For the 007 profile the growth constant
depends sensitively on c_l through the small divisors of the low modes it populates; for sin(theta) it is smooth in c_l.

### 5.11 Logarithmic series at rational delta (code/logff.py, arb 512; the correct object past an exact resonance)
f_n = sum_q t^q f_{n,q}(theta), t = log r. For delta = 4/9 (c_l = 9/5), f_1 = sin(theta), resonances at n = 9m, log degree
of f_n equal to floor((n-1)/9) (as predicted by the theory part), run log_sin1_c9_5_p512 (N = 300 target):
| n | log degree | log10 l1 of t^0, t^1, t^2, t^3, t^4 columns | ratio of t^0 column |
|---|---|---|---|
| 15 | 1 | -6.88, -10.53 | 0.414 |
| 30 | 3 | -12.33, -15.84, -18.08, -20.08 | 0.446 |
| 60 | 6 | -22.63, -25.93, -28.86, -30.89, -33.22 | 0.462 |
| 90 | 9 | -32.69, -35.84, -38.93, -40.98, -43.27 | 0.461 |
| 118 | 13 | -42.00, -45.03, -48.13, -50.27, -52.70 | 0.466 |
The t^0 column follows the smooth pure-series law (L(1 - 2/n) with L about 0.474 at delta = 4/9, consistent with the
L(delta) table) and each higher log power is smaller by about three decades; the full t-polynomial evaluated at
the tested t = log r values therefore decays geometrically through the computed orders with the same L (NUMERICAL EVIDENCE,
finite prefix; the run reached 300). Implementation cross-checks: equals the pure series off resonance (exact, c_l = 9/5,
n <= 8) and agrees with the theory part's independent float implementation (logseries.py, complex Fourier arrays and FFT products)
in every column l1 norm to relative 6e-14 for all n <= 60 (log degrees identical); the theory part's data were in turn checked
exactly by the verifier through order 73 (independently checked).
Column structure at N = 153 (03:10Z): log10(|f_{n,k}|_l1 / |f_{n,0}|_l1) = s_k log10 n + c_k with s_1 = 0.90, s_2 = 0.45,
s_3 = 0.10, s_4 = -0.20 (fits over n >= 9(k+1)+20); at n = 153 the ratios are 1.2e-3, 5.1e-7 (k! times them: 1.2e-3,
2.0e-6, 3.9e-8, 5.2e-10, 4.5e-12 for k = 1..5). The weighted sums sum_k |f_{n,k}| t^k have per-order ratio 0.4618, 0.4653,
0.4670 (n = 60..90, 90..120, 120..153) at each of the four tested values t = log r in {1, 5, 10, 30}: through these orders
and at these radii the log terms do not change the growth rate.
This is NUMERICAL EVIDENCE that the generalized expansion converges with the same L as the pure series would have, and that
the factorial factor floor((n-1)/n_r)! of the proved Gevrey bound is not attained. Further rational cases (1/2, 2/5, 9/20,
2/3, and the 007 profile at 4/9) follow below.

Interim tables (04:29Z, regenerated from checkpoints; density c_k = ||f_{n,k}||_l1, stream g_k = ||g_{n,k}||_l1):
| delta | n | log degree | M_n^{1/n} | max_{k>=1} log10(k! c_k/c_0) | max_{k>=1} log10(k! g_k/g_0) |
|---|---|---|---|---|---|
| 2/3 | 30 | 8 | 0.1737 | -1.13 | -0.34 |
| 2/3 | 60 | 18 | 0.1822 | -0.88 | -0.22 |
| 2/3 | 90 | 28 | 0.1865 | -0.83 | -0.19 |
| 2/3 | 120 | 38 | 0.1889 | -0.79 | -0.26 |
| 2/3 | 150 | 48 | 0.1905 | -0.74 | -0.46 |
| 2/3 | 180 | 58 | 0.1917 | -0.69 | -0.30 |
| 4/9 | 40 | 4 | 0.4027 | -3.45 | -3.19 |
| 4/9 | 80 | 8 | 0.4296 | -3.19 | -3.08 |
| 4/9 | 120 | 13 | 0.4411 | -3.03 | -2.98 |
| 4/9 | 160 | 17 | 0.4475 | -2.91 | -2.87 |
| 4/9 | 200 | 22 | 0.4516 | -2.82 | -2.79 |
| 4/9 | 240 | 26 | 0.4545 | -2.74 | -2.71 |
| 4/9 | 260 | 28 | 0.4557 | -2.70 | -2.68 |
| 4/9 | 300 | 33 | 0.4576 | -2.64 (k = 1) | -2.63 |
| 2/3 | 230 | 75 | 0.1931 | -0.613 (k = 1) | -0.30 |
| 2/3 | 235 | 77 | 0.1932 | -0.562 (k = 40) | -0.52 |
| 2/3 | 240 | 78 | 0.1933 | -0.235 (k = 42) | -0.40 |
| 2/3 | 245 | 80 | 0.1934 | +0.173 (k = 42) | -0.13 (k = 42) |
| 2/3 | 250 | 82 | 0.1935 | +0.543 (k = 44) | +0.20 (k = 44) |
| 2/3 | 260 | 85 | 0.19365 | +1.356 (k = 46) | +1.001 (k = 46) |
| 2/3 | 270 | 88 | 0.19382 | +2.155 (k = 48) | +1.701 (k = 48) |
| 2/3 | 280 | 92 | 0.19400 | +3.040 (k = 50) | +2.291 (k = 50) |
| 2/3 | 290 | 95 | 0.19417 | +3.940 (k = 57) | +2.646 (k = 54) |
| 2/3 | 300 | 98 | 0.19433 | +4.897 (k = 59) | +4.020 (k = 59) |
| 2/3 | 310 | 102 | 0.19448 | +5.952 (k = 61) | +4.912 (k = 61) |
| 1/2 | 40 | 8 | 0.3296 | -2.59 | |
| 1/2 | 80 | 18 | 0.3502 | -2.34 | |
| 1/2 | 100 | 23 | 0.35526 | -2.261 (k = 1) | -2.204 |
| 1/2 | 150 | 36 | 0.36276 | -2.093 (k = 1) | -2.060 |
| 1/2 | 200 | 48 | 0.36696 | -1.970 (k = 1) | -1.947 |
| 1/2 | 250 | 61 | 0.36968 | -1.874 (k = 1) | -1.856 |
| 1/2 | 300 | 73 | 0.37159 | -1.796 (k = 1) | -1.780 |
| 2/5 | 80 | 14 | 0.5078 | -3.14 (k = 1) | -3.06 |
| 2/5 | 160 | 30 | 0.5300 | -2.86 (k = 1) | -2.83 |
| 2/5 | 240 | 46 | 0.5387 | -2.69 (k = 1) | -2.67 |
| 9/20 | 120 | 2 | 0.4319 | -5.44 (k = 1) | -4.79 |
| 9/20 | 240 | 5 | 0.4450 | -5.25 (k = 1) | -4.95 |
The largest normalized factorial-weighted log coefficient drifts upward slowly (about 0.05 decades per 30 orders at 2/3, 0.04 per
40 orders at 4/9) and stays below 10^-0.66 (2/3, n <= 197) and 10^-2.7 (4/9, n <= 260); at 2/3 the INTERIOR columns rise much
faster: log10(k! c_k/c_0) at k = 40 goes from -11.65 (n = 150) to -4.79 (n = 197), at k = 50 from -41.9 (n = 155) to -7.7
(n = 197) (code/hump_report.py), consistent with the theory part's long-double observation of an interior maximum taking over near
n = 240 and becoming positive by n = 250 (the arb run reached 290 and confirmed it, below); at n = 230 (arb): k = 30, 40, 50, 60
give -1.41, -0.91, -2.43, -6.13 while k = 1 gives -0.61. HUMP CONFIRMED: at n = 235 the maximum over k >= 1 moves to k = 40
(-0.562), and at n = 240 it is -0.235 at k = 42 (profile at k = 1, 10, 20, 30, 40, 50, 60: -0.60, -2.49, -2.72, -1.48, -0.31,
-1.01, -3.81), reproducing the theory part's long-double value (-0.24 at k = 42) in 512-bit ball arithmetic with rigorous relative
radii about 1e-60: the interior growth of the factorial-weighted log columns at delta = 2/3 is real, not roundoff. At delta = 4/9
(N = 300) there is no hump: the maximum stays at k = 1 (-2.64) and the interior columns are at -20.3, -36.7, -54.1 (k = 10, 20, 30).
At delta = 2/5 (resonance period 5, run log_sin1_c5_3_p512, N = 240) there is no hump either: the maximum stays at k = 1 (-2.69 at
n = 240) and the interior columns are at -17.7, -31.1, -41.9, -55.3 (k = 10, 20, 30, 40). At delta = 9/20 (resonance period 40, run log_sin1_c20_11_p512, N = 240) the log degree is only 5 at n = 240 and the maximum
stays at k = 1 (-5.25). So the interior hump appears at the resonance period 3 (delta = 2/3) and not, through the computed orders,
at periods 5 (2/5), 9 (4/9) and 40 (9/20).
The 2/3 run is finished at 290. At n = 241..245 the maximum is -0.135 (k = 39), -0.027 (41), -0.024 (43), +0.071 (40), +0.173 (42):
the factorial-weighted interior log coefficients exceed c_0 from n = 244 on (+0.543 at k = 44 for n = 250, equal to the theory part's
long-double +0.54); the stream maximum moves to k = 41..42 from n = 242 and turns positive at n = 248 (+0.197 at k = 44 for n = 250); +1.127 at k = 47
(density) and +0.842 (stream) at n = 258. Ball-arithmetic evaluation of the t-polynomials (code/tprofile.py): at t = log r = 40 the
sum sum_k t^k f_{n,k} cancels 8.6, 9.5, 9.9, 10.0, 10.3 decades at n = 220, 240, 250, 255, 260 (log10 ||F_260(40)|| = -177.546 against
log10 c_0 = -185.501 and log10 of the l1 radius -217.9; the verifier's independent 640-bit interval Horner evaluation (independently checked) gives
-177.5459000989296 with 10.284 decades of cancellation, and an independent check confirms the n = 260 maxima +1.35620895838414 (density) and
+1.00138076893503 (stream) at k = 46 with relative radii below 2.1e-33) (radii 40 decades below the values, so the
cancellation is certified), and the per-order increments of log10 ||F_n(t)|| are -0.69 (t = +-20), -0.65..-0.67 (t = 40),
-0.64..-0.70 (t = -40) between n = 240 and 255. Per-deficit rates (code/deficit_rates.py): the top log column decays by -2.93
decades per block of three orders (the verifier's explicit top chain), the interior deficits d = 12..60 by about -1.9 per block
(-0.63 per order) against -0.70 per order for the t^0 column, which quantifies the relative growth of the factorial-weighted
interior columns (about +0.07 decades per order). Decomposition by distance to the resonant diagonal (code/diagonal_bands.py; s = m + 3 -
n delta for density modes m = 2k+1, s = m + 2 - n delta for stream modes m = 2j; the density offset was off by one (s = 2k+3 instead of 2k+4) in
the tables posted before 09:15Z (the independent verifier); the far-band statements below are unaffected, the corrected density fractions at 320 are
q = 0: 0.027/0.000/0.973, q = 10: 0.162/0.309/0.529, q = 20: 0.048/0.062/0.889, q = 40: 0.001/0.002/0.997, k* = 63: 0.000/0.000/1.000 (0.99998)): the interior-maximum columns (q = k* = 42..48 at n = 240..270) and all
columns q >= 40 have 99..100 percent of their l1 mass at |s| > q, i.e. far from the diagonal, for density and stream alike; the
near-diagonal mass (|s| <= q/4) is 30..50 percent only in the low stream columns q <= 30. The hump is therefore not a
near-resonant phenomenon in the frequency sense (NUMERICAL EVIDENCE through n = 280; at n = 280 the k* = 50 column is 99.9 percent
far for density and stream). The near-diagonal share of the stream t^0 column grows with n (0.12, 0.15, 0.17, 0.31, 0.47 at n = 240,
250, 260, 270, 280). At n = 280 the theory part's long-double hump value +3.04 at k = 50 is reproduced (+3.040), with 11.1 certified decades
of cancellation in the t-polynomial at t = 40. State at N = 300 (run extended): hump +4.897 at k = 59 (density), +4.020 at k = 59 (stream), cancellation 11.9 decades at t = 40,
stream 9-window increments -0.67..-0.72 (class 0: -0.93..-0.95; class 1: -0.71..-0.72; class 2: -0.38..-0.50). At N = 290: hump +3.940 at
k = 57 (density), +2.646 at k = 54 (stream); cancellation 11.5 decades at t = 40; per-order increments 280 -> 290 of log10 ||F_n(t)||: -0.698, -0.675, -0.672, -0.673
at t = 20, -20, 40, -40; stream 9-order-window increments -0.667..-0.695 overall for n = 264..290, split by residue class n mod 3 into
-0.77..-0.92 (class 0), -0.63..-0.71 (class 1), -0.39..-0.68 (class 2, slowest, -0.39..-0.45 in the last windows); the
near-diagonal share of the stream t^0 column reaches 0.81 at n = 290. Whether the hump growth (about +0.1 decades per order in the
factorial-weighted maximum) eventually affects the plain norms M_n (root test 0.19417 at 290, still following the smooth law)
is OPEN; through n = 290 the plain density and stream norms show no departure. The theory part's weighted factorial norm
W_n = log10 sum_q q! 12^q ||[t^q] F_n||_l1 decays about 10^-0.3 per order (10-order increments between -0.27 and -0.33 for
n = 200..290, density and stream alike) against 10^-0.70 for the plain norm, so W_n - log10 M_n grows by about 0.4 decades per order
(50.3 at n = 200, 86.2 at n = 290). In 30-order windows (multiples of the resonance period) the per-order increment of W_n is
-0.362, -0.339, -0.320, -0.303, -0.288 for the windows 140..170, ..., 260..290 (stream: -0.367 .. -0.290), drifting by +0.023,
+0.020, +0.017, +0.015 per window, while the plain norms stay at -0.702..-0.704 (density) and -0.671..-0.707 (stream). The
norm-relative error radius of the arb run grows steadily by 0.455 decades per order from n = 150 on (log10 -86.3 at 150, -62.7 at
202, -20.7 at 294), so the 512-bit computation is rigorous through n = 328 (radius 1e-6) and 329 (2.5e-6). CAUTION for the continuation beyond
329 run with the radius rule disabled: arb's polynomial multiplication reduces the midpoint precision to what the radii warrant, so once the
radii were large (10^-4.9 at 330, order one at 344..346, infinite at 349, where the run crashed) the logged midpoints were no longer 512-bit
values: recomputing order 346 from the reset midpoints of the 345 state changed log10 M_346 by 0.02. The per-order values 330..348 posted on
10:31Z..11:21Z are therefore UNCONFIRMED (the t-profile values at 330 and 340 remain enclosures: their radii were 6..10 decades below the
values). They are being recomputed by (i) a continuation from the archived 329 checkpoint with the radii reset to zero at 329 (tag
log_sin1_c3_from329; its radii then measure the propagation error from the 329 midpoints, which are accurate to about 2.5e-6 of the
maximum) and (ii) two independent float64 runs (log23_full_float and its amplitude-perturbed twin). Status: the restarted run reached 350 at 13:52Z; section 5.11b has the table 330..350 and the comparison with the first continuation.
Candidate 007 profile at delta = 4/9 (c_l = 9/5), canonical log series, arb 512, N = 80 (log_c007f1_c9_5_p512):
| n | log degree | log10 M_n | M_n^{1/n} | max_{k>=1} log10(k! c_k/c_0) | max_k log10(k! g_k/g_0) |
|---|---|---|---|---|---|
| 9 | 0 | 4.10 | 2.8558 | nan | -0.51 |
| 10 | 1 | 4.63 | 2.9072 | -1.21 | -0.92 |
| 20 | 2 | 10.03 | 3.1730 | -1.20 | -0.86 |
| 30 | 3 | 15.65 | 3.3250 | -1.09 | -0.99 |
| 40 | 4 | 21.36 | 3.4200 | -0.99 | -0.96 |
| 50 | 5 | 27.12 | 3.4858 | -0.91 | -0.99 |
| 60 | 6 | 32.89 | 3.5333 | -0.86 | -0.97 |
| 70 | 7 | 38.63 | 3.5636 | -0.78 | -0.89 |
| 80 | 8 | 44.35 | 3.5842 | -0.70 | -0.82 |
(For the pure series at the stored c_l the root test of this profile is 3.46 at N = 233; at 4/9 the pure ansatz fails at n = 9 and the
canonical log series above is the continuation.)
 Stream increments (code/stream_increments.py): the 9-order window mean of
log10(N_n/N_{n-1}), N_n = sum_k ||g_{n,k}||_l1, is -0.706 +- 0.006 for n = 160..230 (by residue class mod 3: -0.76..-0.83, -0.61..-0.64,
-0.68..-0.73), the density window mean is -0.703..-0.704; the roots M_n^{1/n} increase like the non-resonant law
L(1 - 2/n). Agreement with the theory part's float data: 0.4475 at n = 160 (4/9), 0.1909 at 160 (2/3), 0.3296 at 40 (1/2). The runs
continue (2/3 to 240 to test the theory part's suspected bump at n > 200 in arb; 4/9 to 300; 1/2 to 300 afterwards).
The 1/2 run (log_sin1_c2_p512, resumed from 200 at 17:45Z, finished at N = 300 at 21:49Z; rigorous balls, norm-relative radius 10^-24.2 at 300, every resonance
at n = 4k handled canonically with B_(n,j)(0) = 0): no interior hump through 300. The factorial-weighted maximum max_(k >= 1) log10(k! c_k/c_0) stays at k = 1 at
every order and rises slowly, -2.261 (100), -1.970 (200), -1.874 (250), -1.796 (300) (stream -1.780); the interior columns rise relative to c_0 but remain far below
it: log10(k! c_k/c_0) at k = 40, 50, 60 is -30.4, (absent), (absent) at n = 200, -26.2, -33.7, -63.2 at 250 and -26.3, -28.5, -35.1 at 300 (the k = 60 column
gained 28 decades in 50 orders), so a hump at a later order is not excluded by these data (at 2/3 the k = 40 column had reached -4.8 by n = 197 and the hump
appeared at 235). Plain norms: M_n^(1/n) = 0.35526 (100), 0.36696 (200), 0.36968 (250), 0.37159 (300); stream N_n^(1/n) = 0.36376 at 300, log10(N/M) = -2.78
(the stream sum stays 2.3 .. 2.8 decades below the density sum, decreasing); the ratio M_n/M_(n-1) follows L(1 - a/n) with L = 0.38386, a = 1.84 on 200..300
(rms 7e-4), per-order increment -0.4187 (-0.4173 .. -0.4204 on 271..300): the smooth non-resonant law, no regime change. Top log degree 73 at 300 (one new
column per 4 orders). NUMERICAL EVIDENCE through 300; the hump question at 1/2 beyond 300 is OPEN.

### 5.11b Canonical log series at delta = 2/3, orders 330..350: midpoint continuation relative to the certified 329 state (log_sin1_c3_from329)
Setting: f_1 = sin theta, delta = 2/3 (c_l = 3), canonical normalization, arb 512 bits, 4 workers; the run was restarted from the verifier's archived
N = 329 checkpoint (byte-identical to the 09:29Z state of this run, whose balls are rigorous: norm-relative radius 2.5e-6 at 329) with every ball replaced
by its midpoint at 329 (--reset-radii), so that the radii of orders 330..350 measure the propagation error from the 329 midpoints only
(the independent verifier). SCOPE (the independent verifier): the radii of the continuation, 10^-151 .. 10^-125 relative to the largest coefficient, bound the
arithmetic error of the continuation from the loaded midpoint arrays only; they do NOT include the discarded input uncertainty of the 329 state
(2.5e-6 relative, certified), and the propagated effect of that uncertainty on orders 330..350 has not been bounded (it is OPEN). The values below
are therefore the continuation's values for the loaded 329 midpoints to all printed digits, conditional on those midpoints. A sensitivity diagnostic
(run log_sin1_c3_pert329: the verifier's archived 329 state, SHA256 0f078b05..., 941530134 bytes, restored and continued at 512 bits with every ball
[m +/- r] replaced by the boundary point m + s r, s = +/-1 chosen at random with seed 20261031, logff.py --perturb-radii; 2 workers) measures the
response of orders 330..350 to one sample of the input uncertainty; it is a diagnostic, not a bound; its result is reported below when available. All statements are
finite-order observations (NUMERICAL EVIDENCE).
PROVENANCE (the independent verifier): the per-order rows of logs/log_sin1_c3_from329.jsonl from 330 on do not carry the flags radii_reset_at / midpoint_only
(the process was launched at 11:52Z with code that wrote the reset marker only into the run header; the resume at 350 then loaded a checkpoint
without the marker): every row with n >= 330 in that file, and every checkpoint of that tag, is the reset continuation relative to the 329
midpoints, whatever its flags say. logff.py now stores radii_reset_at and perturbed_seed in the checkpoint and recovers them on load (the
verifier's patch, applied 14:53Z); the perturbed run's rows carry radii_reset_at = 329 (and its header perturbed_seed = 20261031).
Per-order values (M_n = sum of the l1 norms of the log columns of f_n, N_n the same for g_n; incr = log10 M_n - log10 M_(n-1); hump max = max over
k >= 1 of log10(k! c_k/c_0) over the density columns with its k*; log10 rad = norm-relative radius of the new run; old = the first, precision-trimmed
continuation of 09:29Z..11:21Z with its radii; the 'old' rows 346, 347 are the two orders recomputed from the 345 checkpoint with reset radii):
| n | class | log10 M_n (new) | incr | log10 N_n (new) | log10 N/M | hump max (k*) | log10 rad (new) | log10 M_n (old) | log10 rad (old) | new - old (M) |
|---|---|---|---|---|---|---|---|---|---|---|
| 330 | 0 | -234.153 |  | -235.313 | -1.159 | +7.78 (65) | -150.7 | -234.153 | -4.9 | -2.5e-12 |
| 331 | 1 | -234.885 | -0.732 | -236.117 | -1.232 | +7.95 (67) | -150.6 | -234.885 | -4.7 | -2.0e-10 |
| 332 | 2 | -235.611 | -0.726 | -235.436 | +0.175 | +8.06 (69) | -136.5 | -235.611 | -4.1 | -2.0e-10 |
| 333 | 0 | -235.788 | -0.177 | -236.350 | -0.561 | +7.68 (66) | -136.2 | -235.788 | -4.6 | -2.9e-10 |
| 334 | 1 | -236.483 | -0.695 | -236.993 | -0.509 | +7.88 (68) | -135.6 | -236.483 | -4.2 | -1.1e-09 |
| 335 | 2 | -237.217 | -0.734 | -237.249 | -0.031 | +8.01 (67) | -134.6 | -237.217 | -3.6 | -3.6e-09 |
| 336 | 0 | -237.555 | -0.338 | -238.126 | -0.571 | +7.75 (69) | -133.7 | -237.555 | -3.5 | -1.9e-08 |
| 337 | 1 | -238.261 | -0.706 | -238.755 | -0.494 | +7.94 (66) | -133.3 | -238.261 | -3.1 | -1.2e-07 |
| 338 | 2 | -238.988 | -0.727 | -238.755 | +0.233 | +8.10 (68) | -132.2 | -238.988 | -2.5 | -4.1e-07 |
| 339 | 0 | -239.140 | -0.151 | -239.650 | -0.511 | +7.58 (70) | -131.8 | -239.140 | -2.7 | -6.9e-07 |
| 340 | 1 | -239.838 | -0.699 | -240.281 | -0.442 | +7.76 (67) | -131.4 | -239.838 | -2.3 | -4.7e-06 |
| 341 | 2 | -240.574 | -0.736 | -240.424 | +0.150 | +7.94 (69) | -130.3 | -240.574 | -1.8 | -1.4e-05 |
| 342 | 0 | -240.793 | -0.219 | -241.312 | -0.519 | +7.49 (71) | -129.8 | -240.793 | -1.8 | -4.9e-05 |
| 343 | 1 | -241.495 | -0.702 | -241.940 | -0.445 | +7.67 (70) | -129.4 | -241.495 | -1.4 | -3.5e-04 |
| 344 | 2 | -242.228 | -0.733 | -242.038 | +0.190 | +7.83 (70) | -128.4 | -242.227 | -0.8 | -1.1e-03 |
| 345 | 0 | -242.417 | -0.189 | -242.929 | -0.512 | +7.34 (72) | -128.1 | -242.414 | -0.9 | -2.9e-03 |
| 346 | 1 | -243.118 | -0.701 | -243.557 | -0.440 | +7.57 (71) | -127.7 | -243.118 | -150.6 | +1.5e-10 |
| 347 | 2 | -243.852 | -0.734 | -243.679 | +0.173 | +7.69 (73) | -126.7 | -243.852 | -137.6 | -4.4e-10 |
| 348 | 0 | -244.054 | -0.202 | -244.568 | -0.514 | +7.23 (70) | -126.3 | -243.874 | 0.2 | -1.8e-01 |
| 349 | 1 | -244.755 | -0.701 | -245.196 | -0.441 | +7.47 (72) | -126.0 | | | |
| 350 | 2 | -245.489 | -0.734 | -245.308 | +0.181 | +7.59 (74) | -125.1 | | | |
Reading of the comparison: the first continuation's logged values are right to 1e-6 through 339 and to 1e-3 through 344 although its radii were
10^-5 .. 10^-1 there (the radii were pessimistic by four to six decades); at 345 its logged value is off by 2.9e-3, at 346 by 2.0e-2 (-243.097 against
-243.118) and at 348 by 0.18, i.e. once the ball radii reached the size of the values, arb trimmed the midpoint precision and the logged statistics
(computed from wide balls) and the propagated coefficients both lost accuracy. The 345 checkpoint itself was still accurate: the two orders
recomputed from it with reset radii (old rows 346, 347) agree with the from329 continuation to 1.5e-10 and 4.4e-10. Every qualitative feature
posted for 330..348 therefore stands, with the quantitative values of this table replacing the old ones from 345 on.
What the orders 330..350 show (all relative to the certified 329 state):
(a) Residue-class structure. At every class-2 order (n = 332, 335, 338, 341, 344, 347, 350) the stream plain sum N_n is comparable to or larger than
the density plain sum M_n: log10(N_n/M_n) = +0.175, -0.031, +0.233, +0.150, +0.190, +0.173, +0.181, against -0.44 .. -0.57 at the other orders and
-1.2 at 330, 331. The stream excess sits in the Poisson-shift-2/3 modes (section 5.11, stream-mode shares 0.9 at these orders through 340; the 341..350
shares are in notes/stream_ratio_modes_341_350.json and notes/stream_shares_341_350.txt: on 341..350 the pattern is exactly 3-periodic: class 2: 0.92 of N_n in the shift-2/3 modes, col-0 share 0.49, far share 0.02; class 0: density near-resonant share 0.75 against 0.07 at the other classes, stream shift shares 0; class 1: 0.60 of N_n in the shift-4/3 modes; the shares repeat to three digits at 341/344/347/350, 342/345/348 and 343/346/349). At the class-0 order following each excess the density increment collapses: -0.177 (333),
-0.338 (336), -0.151 (339), -0.219 (342), -0.189 (345), -0.202 (348), while the class-1 and class-2 increments stay at -0.695 .. -0.736, the values of the
smooth law before 330. The three-order period therefore now loses 1.63 decades (0.544 per order) instead of 2.10 (0.70 per order) before 330.
(b) Slopes. 27-order least-squares slopes of log10 M_n / log10 N_n on the merged certified (<= 329) and continued (>= 330) data (code/merge_logs.py,
code/slopes_q.py): ending 300: -0.7010 / -0.6839; 310: -0.7011 / -0.6968; 320: -0.6977 / -0.6644; 326: -0.6920 / -0.6428; 330: -0.6869 / -0.6446;
338: -0.6623 / -0.6167; 342: -0.6340 / -0.5953; 346: -0.6047 / -0.5709; 350: -0.5794 / -0.5500 (difference N - M: +0.017, +0.004, +0.033, +0.049, +0.042,
+0.046, +0.039, +0.034, +0.029). The 9-order window means ending 350: density -0.546, stream -0.543 (by class: 0: -0.889, 1: -0.628, 2: -0.110). So from
about 330 the decay rate of both plain sums has weakened from 10^-0.70 to about 10^-0.55 per order over the last nine orders, and the two rates are
now equal within the window noise; the ratio N_n/M_n no longer drifts upward on average (the class-2 excess is stationary at +0.15 .. +0.23 and the
other classes at -0.44 .. -0.57). Root tests: M_350^(1/350) = 10^(-245.489/350) = 0.1989 (0.1942 at 290, 0.1952 at 329; 0.2014 at 360, 0.2031 at 370, 0.2047 at 380, 0.2070 at 390, 0.2086 at 400; stream 0.1991, 0.2007, 0.2025, 0.2050, 0.2064, 0.2081).
(b2) Per-period decrements (notes/period3_decrements_300_353.txt). The 3-order decrement log10 M_(n+3) - log10 M_n between consecutive class-0 orders
isolates the transition that the 27-order slopes smear:
300 -> 303: M -2.099   N -1.838
303 -> 306: M -2.106   N -2.185
306 -> 309: M -2.104   N -2.112
309 -> 312: M -2.064   N -1.553
312 -> 315: M -2.113   N -2.489
315 -> 318: M -2.004   N -1.313
318 -> 321: M -2.096   N -2.324
321 -> 324: M -1.974   N -1.595
324 -> 327: M -2.013   N -2.028
327 -> 330: M -2.143   N -2.429
330 -> 333: M -1.635   N -1.037
333 -> 336: M -1.767   N -1.776
336 -> 339: M -1.585   N -1.524
339 -> 342: M -1.653   N -1.662
342 -> 345: M -1.624   N -1.617
345 -> 348: M -1.637   N -1.639
348 -> 351: M -1.631   N -1.630
Through 327 -> 330 the density loses 2.00 .. 2.14 decades per period (the 10^-0.70 law) and the stream decrement fluctuates (-1.3 .. -2.5, the
concentration episodes); at 330 -> 333 both drop to -1.6 .. -1.8, and from 336 -> 339 on the density decrement is -1.63 +/- 0.02 per period with the
stream decrement equal to it from 339 on: a stationary period-3 cycle decaying by 10^-0.544 per order (the mode shares of (a) repeat to three digits).
If it persists the plain sums are geometric with ratio 0.286 per order (coefficient-norm radius 3.5 in z = r^(-2/3); because of the log r factors this is
not the physical convergence boundary, only the geometric rate of the coefficient norms) and the hypothesis of the theory part's
Propositions 14.17/14.19 holds with A_0 about 0.29 (conditional NUMERICAL EVIDENCE; a further regime change cannot be excluded, the first one
appeared in the plain sums without warning at 330).
Orders 361..370 (same run):
| 361 | 1 | -251.276 |  | -251.716 | -0.439 | +6.98 (78) | -119.8 | | | |
| 362 | 2 | -252.010 | -0.734 | -251.824 | +0.187 | +7.14 (75) | -119.0 | | | |
| 363 | 0 | -252.202 | -0.192 | -252.714 | -0.512 | +6.68 (77) | -118.8 | | | |
| 364 | 1 | -252.903 | -0.701 | -253.342 | -0.439 | +6.87 (76) | -118.4 | | | |
| 365 | 2 | -253.637 | -0.734 | -253.448 | +0.189 | +7.01 (78) | -117.6 | | | |
| 366 | 0 | -253.827 | -0.190 | -254.338 | -0.512 | +6.55 (78) | -117.4 | | | |
| 367 | 1 | -254.528 | -0.701 | -254.967 | -0.439 | +6.79 (77) | -117.0 | | | |
| 368 | 2 | -255.262 | -0.734 | -255.071 | +0.191 | +6.93 (79) | -116.2 | | | |
| 369 | 0 | -255.450 | -0.188 | -255.961 | -0.511 | +6.44 (76) | -116.0 | | | |
| 370 | 1 | -256.151 | -0.701 | -256.590 | -0.439 | +6.69 (78) | -115.6 | | | |
3-order decrements 360 -> 363 -> 366 -> 369: density -1.627, -1.625, -1.623; stream -1.626, -1.625, -1.623 (a drift of +0.002 per period toward weaker decay,
the same as the drift of the signed multiplier in (b5); not a power-law prefactor effect, see (b5)); 27-order slopes ending 365: -0.5459 / -0.5417, ending 370: -0.5421 / -0.5453; 9-window means ending 370:
-0.542 / -0.542 (classes 0, 1, 2 of the stream: -0.890, -0.628, -0.106). Hump maximum +6.4 .. +7.1 (k* 75..79), still slowly decreasing; W -0.26 per order on 340..370.
Orders 371..380 (same run):
| 371 | 2 | -256.885 |  | -256.692 | +0.193 | +6.83 (80) | -114.9 | | | |
| 372 | 0 | -257.072 | -0.187 | -257.583 | -0.511 | +6.33 (77) | -114.7 | | | |
| 373 | 1 | -257.773 | -0.701 | -258.211 | -0.438 | +6.58 (79) | -114.3 | | | |
| 374 | 2 | -258.507 | -0.734 | -258.312 | +0.195 | +6.72 (81) | -113.5 | | | |
| 375 | 0 | -258.692 | -0.185 | -259.202 | -0.510 | +6.24 (80) | -113.4 | | | |
| 376 | 1 | -259.393 | -0.701 | -259.831 | -0.438 | +6.45 (80) | -113.0 | | | |
| 377 | 2 | -260.127 | -0.734 | -259.930 | +0.196 | +6.62 (79) | -112.2 | | | |
| 378 | 0 | -260.311 | -0.184 | -260.821 | -0.510 | +6.15 (81) | -112.1 | | | |
| 379 | 1 | -261.011 | -0.701 | -261.449 | -0.438 | +6.35 (83) | -111.7 | | | |
| 380 | 2 | -261.745 | -0.734 | -261.547 | +0.198 | +6.52 (80) | -111.0 | | | |
3-order decrements 369 -> 372 -> 375 -> 378: density -1.622, -1.620, -1.619; stream -1.621, -1.620, -1.618. The drift sits entirely in the class-0 (resonant)
step: its increment weakens -0.193 (360), -0.190 (366), -0.187 (372), -0.185 (375), -0.184 (378) while the class-1 and class-2 increments stay at -0.701 and -0.734
to three decimals since 330. 27-order slopes ending 375 / 380: -0.5414 / -0.5415 and -0.5433 / -0.5392; 9-window means ending 380: -0.540 / -0.539. Hump maximum
+6.2 .. +6.8 (k* 77..83), decreasing about 0.05 per order; W -0.25 per order on 350..380.
Orders 381..390 (same run):
| 381 | 0 | -261.927 |  | -262.437 | -0.510 | +6.06 (82) | -110.8 | | | |
| 382 | 1 | -262.628 | -0.701 | -263.066 | -0.438 | +6.26 (84) | -110.4 | | | |
| 383 | 2 | -263.362 | -0.734 | -263.162 | +0.200 | +6.41 (81) | -109.7 | | | |
| 384 | 0 | -263.543 | -0.181 | -264.052 | -0.509 | +5.95 (83) | -109.6 | | | |
| 385 | 1 | -264.243 | -0.701 | -264.681 | -0.437 | +6.16 (82) | -109.2 | | | |
| 386 | 2 | -264.978 | -0.734 | -264.775 | +0.202 | +6.32 (84) | -108.5 | | | |
| 387 | 0 | -265.157 | -0.179 | -265.666 | -0.509 | +5.83 (84) | -108.3 | | | |
| 388 | 1 | -265.857 | -0.700 | -266.294 | -0.437 | +6.08 (83) | -107.9 | | | |
| 389 | 2 | -266.591 | -0.734 | -266.387 | +0.204 | +6.24 (85) | -107.2 | | | |
| 390 | 0 | -266.769 | -0.177 | -267.278 | -0.509 | +5.73 (82) | -107.1 | | | |
3-order decrements 378 -> 381 -> 384 -> 387 -> 390: density -1.617, -1.615, -1.614, -1.612; stream -1.617, -1.615, -1.613, -1.612 (drift +0.0015 .. 0.002 per period, still
entirely in the class-0 increment: -0.181, -0.179, -0.177 at 384, 387, 390; classes 1 and 2 at -0.700/-0.701 and -0.734). 27-order slopes ending 385 / 390: -0.5394 / -0.5426
and -0.5387 / -0.5388; 9-window means ending 390: -0.538 / -0.538. Hump maximum +5.7 .. +6.4 (k* 81..85), decreasing about 0.05 per order; W -0.25 per order on 360..390.
Orders 391..400 (same run; the run ended at 400 at 18:13Z):
| 391 | 1 | -267.469 |  | -267.906 | -0.437 | +5.99 (84) | -106.7 | | | |
| 392 | 2 | -268.203 | -0.734 | -267.997 | +0.206 | +6.15 (86) | -106.0 | | | |
| 393 | 0 | -268.379 | -0.176 | -268.888 | -0.509 | +5.64 (88) | -105.9 | | | |
| 394 | 1 | -269.080 | -0.700 | -269.516 | -0.437 | +5.88 (85) | -105.5 | | | |
| 395 | 2 | -269.814 | -0.734 | -269.606 | +0.208 | +6.05 (87) | -104.8 | | | |
| 396 | 0 | -269.988 | -0.174 | -270.496 | -0.508 | +5.57 (86) | -104.7 | | | |
| 397 | 1 | -270.689 | -0.700 | -271.125 | -0.436 | +5.78 (88) | -104.3 | | | |
| 398 | 2 | -271.423 | -0.734 | -271.213 | +0.210 | +5.94 (85) | -103.6 | | | |
| 399 | 0 | -271.596 | -0.173 | -272.103 | -0.508 | +5.49 (87) | -103.6 | | | |
| 400 | 1 | -272.296 | -0.700 | -272.732 | -0.436 | +5.71 (89) | -103.2 | | | |
3-order decrements 390 -> 393 -> 396 -> 399: density -1.611, -1.609, -1.607; stream -1.610, -1.609, -1.607 (class-0 increments -0.176, -0.174, -0.173; classes 1, 2 at
-0.700 and -0.734). 27-order slopes ending 395 / 400: -0.5407 / -0.5365 and -0.5367 / -0.5400; 9-window means ending 400: -0.536 / -0.536. Root tests at 400:
density 0.2086, stream 0.2081. Hump maximum +5.5 .. +6.2 (k* 84..89), decreasing about 0.05 per order; W -0.24 per order on 370..400.
Orders 401..410 (second continuation, launched 18:17Z from the 400 checkpoint; same columns; the radii of the second continuation bound its own arithmetic from the loaded 400 midpoints in the same way):
| 401 | 2 | -273.030 |  | -272.818 | +0.212 | +5.85 (86) | -102.5 | | | |
| 402 | 0 | -273.201 | -0.171 | -273.709 | -0.507 | +5.40 (88) | -102.4 | | | |
| 403 | 1 | -273.901 | -0.700 | -274.337 | -0.436 | +5.62 (90) | -102.0 | | | |
| 404 | 2 | -274.636 | -0.734 | -274.421 | +0.214 | +5.75 (89) | -101.3 | | | |
| 405 | 0 | -274.805 | -0.169 | -275.312 | -0.507 | +5.30 (89) | -101.2 | | | |
| 406 | 1 | -275.505 | -0.700 | -275.941 | -0.436 | +5.52 (91) | -100.8 | | | |
| 407 | 2 | -276.240 | -0.734 | -276.023 | +0.216 | +5.69 (90) | -100.2 | | | |
| 408 | 0 | -276.407 | -0.168 | -276.914 | -0.507 | +5.18 (90) | -100.1 | | | |
| 409 | 1 | -277.107 | -0.700 | -277.543 | -0.436 | +5.44 (89) | -99.7 | | | |
| 410 | 2 | -277.842 | -0.734 | -277.624 | +0.218 | +5.62 (91) | -99.0 | | | |
3-order decrements 399 -> 402 -> 405 -> 408 -> 411: density -1.606, -1.604, -1.602, -1.601; stream -1.605, -1.604, -1.602, -1.600 (class-0 increments -0.171, -0.169, -0.168;
classes 1, 2 at -0.700 and -0.734 unchanged since 330; log10(N/M) at class 2 drifts up, +0.212 (401) .. +0.218 (410)). 27-order slopes ending 405 / 410: -0.5360 / -0.5361
and -0.5380 / -0.5338; 9-window means ending 410: -0.535 / -0.534. Root tests at 410: density 0.2100, stream 0.2103 (log10 M -277.842, log10 N -277.624); at 411:
0.2107 / 0.2101. Hump maximum +5.2 .. +5.9 (k* 86..91). W -0.24 per order on 380..410. (Scripts: code/table_511b.py, code/period3_decrements.py, code/slopes_q.py
on the merged log, code/report_order.py.)
Orders 411..420 (same continuation; propagation radii 10^-99 .. 10^-95.6):
| 411 | 0 | -278.008 |  | -278.514 | -0.506 | +5.11 (93) | -99.0 | | | |
| 412 | 1 | -278.708 | -0.700 | -279.143 | -0.435 | +5.35 (90) | -98.6 | | | |
| 413 | 2 | -279.442 | -0.734 | -279.222 | +0.220 | +5.53 (92) | -97.9 | | | |
| 414 | 0 | -279.607 | -0.164 | -280.113 | -0.506 | +5.03 (94) | -97.9 | | | |
| 415 | 1 | -280.307 | -0.700 | -280.742 | -0.435 | +5.25 (91) | -97.5 | | | |
| 416 | 2 | -281.041 | -0.734 | -280.819 | +0.222 | +5.44 (93) | -96.8 | | | |
| 417 | 0 | -281.204 | -0.163 | -281.710 | -0.506 | +4.96 (92) | -96.7 | | | |
| 418 | 1 | -281.904 | -0.700 | -282.339 | -0.435 | +5.19 (94) | -96.3 | | | |
| 419 | 2 | -282.638 | -0.735 | -282.414 | +0.224 | +5.33 (91) | -95.7 | | | |
| 420 | 0 | -282.799 | -0.161 | -283.305 | -0.505 | +4.89 (93) | -95.6 | | | |
3-order decrements 408 -> 411 -> 414 -> 417 -> 420: density -1.601, -1.599, -1.597, -1.595 (stream the same); class-0 increments -0.164, -0.163, -0.161 (from -0.197 at
354: the signed resonant increment rises by about +0.0016 per period, its magnitude decreasing); classes 1, 2 at -0.700 and -0.734/-0.735; log10(N/M) at class 2 +0.220 .. +0.224. 27-order slopes ending
415 / 420: -0.5340 / -0.5373 and -0.5332 / -0.5334; 9-window means ending 420: -0.532 / -0.532. Root tests at 420: density 0.2122, stream 0.2116. Hump maximum
+4.9 .. +5.5 (k* 90..94), still decreasing about 0.04 per order; W -0.24 per order on 390..420.
Orders 421..430 (same continuation; propagation radii 10^-95.2 .. 10^-92.0):
| 421 | 1 | -283.499 |  | -283.934 | -0.435 | +5.12 (95) | -95.2 | | | |
| 422 | 2 | -284.234 | -0.735 | -284.007 | +0.226 | +5.25 (97) | -94.6 | | | |
| 423 | 0 | -284.393 | -0.159 | -284.898 | -0.505 | +4.80 (94) | -94.5 | | | |
| 424 | 1 | -285.093 | -0.700 | -285.527 | -0.434 | +5.04 (96) | -94.2 | | | |
| 425 | 2 | -285.827 | -0.735 | -285.599 | +0.229 | +5.18 (95) | -93.5 | | | |
| 426 | 0 | -285.985 | -0.158 | -286.490 | -0.505 | +4.71 (95) | -93.5 | | | |
| 427 | 1 | -286.685 | -0.700 | -287.119 | -0.434 | +4.95 (97) | -93.1 | | | |
| 428 | 2 | -287.419 | -0.735 | -287.188 | +0.231 | +5.13 (96) | -92.4 | | | |
| 429 | 0 | -287.575 | -0.156 | -288.080 | -0.504 | +4.62 (98) | -92.4 | | | |
| 430 | 1 | -288.275 | -0.700 | -288.709 | -0.434 | +4.86 (95) | -92.0 | | | |
3-order decrements 420 -> 423 -> 426 -> 429: density -1.594, -1.592, -1.590 (stream the same); class-0 increments -0.159, -0.158, -0.156; classes 1, 2 at -0.700 and
-0.735; log10(N/M) at class 2 +0.226 .. +0.231. 27-order slopes ending 425 / 430: -0.5352 / -0.5310 and -0.5312 / -0.5345; 9-window means ending 430: -0.531 / -0.531.
Root tests at 430: density 0.2136, stream 0.2131. Hump maximum +4.6 .. +5.3 (k* 94..98); W -0.23 per order on 400..430.
Orders 431..440 (same continuation; the run ENDED at 440 at 22:59Z; propagation radii 10^-91.3 .. 10^-88.2; final checkpoint ckpt/log_sin1_c3_from329.pkl, 2.2 GB):
| 431 | 2 | -289.009 |  | -288.777 | +0.233 | +5.06 (97) | -91.3 | | | |
| 432 | 0 | -289.164 | -0.154 | -289.668 | -0.504 | +4.56 (99) | -91.3 | | | |
| 433 | 1 | -289.863 | -0.700 | -290.297 | -0.434 | +4.78 (96) | -90.9 | | | |
| 434 | 2 | -290.598 | -0.735 | -290.363 | +0.235 | +4.98 (98) | -90.3 | | | |
| 435 | 0 | -290.750 | -0.153 | -291.254 | -0.504 | +4.49 (100) | -90.3 | | | |
| 436 | 1 | -291.450 | -0.699 | -291.883 | -0.433 | +4.70 (99) | -89.9 | | | |
| 437 | 2 | -292.184 | -0.735 | -291.947 | +0.237 | +4.89 (99) | -89.2 | | | |
| 438 | 0 | -292.335 | -0.151 | -292.839 | -0.503 | +4.41 (98) | -89.2 | | | |
| 439 | 1 | -293.035 | -0.699 | -293.468 | -0.433 | +4.65 (100) | -88.8 | | | |
| 440 | 2 | -293.769 | -0.735 | -293.530 | +0.239 | +4.80 (102) | -88.2 | | | |
3-order decrements 429 -> 432 -> 435 -> 438: density -1.588, -1.587, -1.585 (stream the same); class-0 increments -0.154, -0.153, -0.151; classes 1, 2 at -0.699/-0.700
and -0.735; log10(N/M) at class 2 +0.233 .. +0.239. 27-order slopes ending 435 / 440: -0.5304 / -0.5305 and -0.5324 / -0.5281; 9-window means ending 440: -0.529 / -0.528.
Root tests at 440: density 0.2150, stream 0.2152 (the stream root test now equals the density root test to 0.0002). Hump maximum over the orders 431..440: +4.4 .. +5.1
(k* 96..102); at 440 alone +4.80 at k = 102; W -0.23 per order on 410..440. Final state of the series of tables: from 333 to 440 (36 periods) the cycle never broke; the
signed class-0 increment rose monotonically from -0.197 (354) to -0.151 (438), i.e. by +0.00165 per period (its magnitude decreasing; the verifier's exact value is
+0.0016502584 per period over these endpoints), while the two other increments stayed at -0.700 and -0.734/-0.735 (to 0.001); the period decrement went from -1.632 to -1.585.
(b4) Referee comment (external referee by a second model, on this subsection's interpretation): repeating aggregate mass shares do not establish repeating signed vectors; the
crossing N_n = M_n has no intrinsic meaning (a correlation, not a cause); equal density and stream decrements follow algebraically once N_n/M_n repeats;
ten periods are weak spectral evidence (a slower mode excited at a small level, nonnormal transients, or the growing number of log columns can produce a
temporary plateau); the factorial-column statistic is invariant under a common factor per order and cannot exclude super-geometric growth of the
columns together. Recommended checks, computed below where feasible: signed projections a_n = <x_(n-3), x_n>/||x_(n-3)||^2 with the relative residual
e_n = ||x_n - a_n x_(n-3)||/||x_n|| (zero-padded new log columns; raw and resonance-shifted mode indices), projections on a fixed reference per residue
class, the one-step linearization error of the recursion restricted to pairs with min(i, j) <= L, and the migration of mass into new log columns.
(b5) Signed-vector diagnostics (code/cycle_diag.py on ckpt/log_sin1_c3_N350.pkl, orders 300..350; notes/cycle_diag_300_350.txt). With x_n the full float
array of midpoints of F_n (or G_n) over (log column, mode), zero-padded, a_n = <x_(n-3), x_n>/||x_(n-3)||^2 and e_n = ||x_n - a_n x_(n-3)||_2/||x_n||_2:
raw alignment of the mode indices gives e_n = 0.65 .. 0.95 at every order (the pattern is not stationary in the raw modes); with the mode index shifted by
one per period (the resonant frequency n delta moves by 2 per period, i.e. one sine mode) e_n is 0.48 .. 0.72 for the density through 329 and then falls
geometrically after the transition: 0.303 (336), 0.149 (339), 0.064 (342), 0.026 (345), 0.012 (348), 0.014 (350); stream: 0.098, 0.045, 0.021, 0.008, 0.004,
0.001. The multiplier converges to a_n = -0.0229 (density, 348..350: -2.284e-2, -2.290e-2, -2.293e-2) and -0.0228 .. -0.0235 (stream), i.e. |a| = 10^-1.64 per
period, the norm decrement, with a NEGATIVE sign: the signed profile changes sign every period (period 6 in the signs) while travelling one mode per period.
The residual halves every period (factor 2.2 .. 2.5), consistent with a second component decaying faster by that factor; the l1 residual is twice the l2 one.
So the generated sequence is a single period-3 mode with per-period multiplier -0.0229 up to a residual of 6.4 .. 7.8 percent at 342..344, 2.6 .. 3.1 percent
at 345..347 and 1.2 .. 1.4 percent at 348..350 (exact tested ranges; NUMERICAL EVIDENCE, conditional on the 329 midpoints; the verifier's directed audit 207
confirms the multipliers and residuals through 365). If this mode persists, the coefficient norms decay like 0.0229^(n/3), i.e. the coefficient-norm radius in z = r^(-2/3) is 0.0229^(-1/3) = 3.52. No
conclusion about the arguments of the singularities follows: the shift by one mode per period carries the phase factor exp(+-2 i theta) on the complex
Fourier branches, so the singularity locations of sum_n z^n F_n(theta) depend on theta (verifier's exact counterexample: F_n = (-a)^k sin((2k+1) theta)
has shifted multiplier exactly -a and residual zero, yet a positive-real pole at theta = pi/2); an earlier sentence here claiming singularities at the
arguments 60, 180, 300 degrees and none on the positive axis was wrong and is withdrawn (independently checked). The singularity location of 5.7 stays OPEN.
On the live checkpoint (orders 348..365, notes/cycle_diag_348_365.txt) the shifted-alignment residual is 0.001 .. 0.002 (density) and below 0.001 (stream) from
357 on, so the sequence is a single period-3 mode to 0.1 .. 0.2 percent there; the multiplier is not constant: a_n = -0.02350 (357), -0.02356 (360), -0.02366
(363), -0.02375 (365), i.e. |a_n| grows by about 0.1 percent per order (log10 |a| from -1.629 to -1.624 over eight orders), the same drift as the per-period
decrements (-1.632, -1.630, -1.628, ...). This drift is NOT a power-law prefactor effect: a multiplier A (1 - c/n) or a norm A^n n^(-beta) changes the per-period
decrement by about 9 beta/(n^2 ln 10) < 2e-5 per period at n = 360 (the independent verifier, correcting an earlier sentence here); +0.002 per period is a genuine slow drift of
the dominant multiplier with n. Two models fit the twelve periods equally: a saturating transient, or a power |a_n| proportional to n^beta with beta about 0.5
(3 beta/(n ln 10) = 0.002 at n = 360), which would make the coefficient norms grow like A^n (n!)^(beta/3), i.e. Gevrey-type, and the series divergent. The drift
is tracked as the run continues; OPEN. Fits on 348..370 (notes/drift_fit_345_370.txt; density multiplier -0.02284 at 348 to -0.02383 at 370, +0.0025 per
period in log10; the shifted residual e_n over this window is 0.012 .. 0.014 at 348..350, 0.005 .. 0.007 at 351..356 and 0.001 .. 0.002 from 357 on; the exact
norm identity ||x_n||/||x_(n-3)|| = |a_n|/sqrt(1 - e_n^2) of the verifier's converts the multiplier into the norm ratio): log10 |a_n| = beta log10 n + c gives beta = 0.555 (rms 2.4e-3; Gevrey exponent beta/3 = 0.19 if it persisted); log10 |a_n| = c0 + c1/n gives
c1 = -86.6 with the limit |a_inf| = 0.0409 (rms 2.3e-3; per-order decrement -0.463, coefficient-norm radius 2.9 in z if it persisted); the stream multiplier gives
beta = 0.50 or c1 = -77.5. The two models are indistinguishable on 22 orders. Refit with 372..380 (notes/drift_fit_348_380.txt; multiplier -0.02392, -0.02401,
-0.02409 at 372, 375, 378): the per-period change of log10 |a_n| fell from +0.0025 (348..370) to +0.0014 (370..380); both 348..370 fits overpredict 372..380 (errors
-0.0005 .. -0.0025 in log10, the 1/n model slightly less wrong); on 357..380 the fits give beta = 0.44 or |a_inf| = 0.0370 (rms 5e-4). With 381..390 (notes/drift_fit_348_390.txt; multiplier -0.02418, -0.02427, -0.02436, -0.02445 at 381..390) the picture
is: the per-period increment of log10 |a_n| at the class-0 orders is +0.00164, +0.00164, +0.00163, +0.00144, +0.00162, +0.00161, +0.00161, +0.00160 for the
periods 366..390, i.e. constant to 0.00004 apart from one lower step (the 'deceleration' noted at 380 was that single step). Fits on 357..390: power model beta = 0.456
(rms 5.0e-4), 1/n model |a_inf| = 0.0377 (rms 5.1e-4); a third model, log10 |a_n| linear in n (the multiplier growing exponentially, which would make log10 M_n
quadratic in n and the series divergent faster than any Gevrey class), fits the constant increments at least as well. On a window of eleven periods the three
models differ by less than the fit residual (verifier for the first two). Through 400 (notes/cycle_diag_386_400.txt, notes/drift_fit_348_400.txt):
multipliers -0.02454 (393), -0.02464 (396), -0.02473 (399), residual 0.001; per-period increments of log10 |a_n| +0.00160, +0.00177, +0.00158 for the last three
periods; fits on 357..400: power beta = 0.464 (rms 5.0e-4), 1/n |a_inf| = 0.0383 (rms 5.5e-4), linear in n with slope 0.000533 per order (rms 4.8e-4): still
unseparable. OPEN. Through 410 (notes/cycle_diag_396_410.txt, notes/drift_fit_348_410.txt, now produced by code/drift_fit.py, whose rms values are the rms of the
residual of log10 |a_n| and are therefore not comparable with the earlier inline rms numbers): multipliers -0.02482 (402), -0.02492 (405), -0.02502 (408), shifted
residual 0.001; per-period increments +0.00158, +0.00175, +0.00174 for the periods ending 402, 405, 408 (the mean since 366 is +0.0016; the last two steps are the
largest since 366). Fits on 357..408: power beta = 0.471 (rms 2.7e-4), 1/n |a_inf| = 0.0388 (rms 4.1e-4), linear in n with slope 0.000536 per order (rms 1.3e-4);
on 381..408: beta = 0.497 (9.9e-5), |a_inf| = 0.0404 (1.4e-4), slope 0.000548 (6.1e-5); on 390..408: beta = 0.509 (6.7e-5), |a_inf| = 0.0411 (8.3e-5), slope
0.000554 (5.4e-5). The power exponent and the 1/n limit both rise as the window start moves later (0.464 -> 0.509 and 0.0383 -> 0.0411), while the linear model
has the smallest residual on every window tested at 410 and a nearly stable slope (0.000533 -> 0.000554): among the three models the exponential-weakening one fits the
printed multipliers best through 408, but the residual differences (6e-5 .. 3e-4) are at the level of the four-significant-digit rounding of the printed
multipliers (about 9e-5 in log10), so the three models are still not separated by these data; the verifier's full-precision multipliers (independently checked) decide this
better than the printed ones. OPEN. Through 420 (notes/cycle_diag_406_420.txt, notes/drift_fit_348_420.txt): multipliers -0.02511 (411), -0.02521 (414), -0.02531 (417),
-0.02541 (420), shifted residual 0.001 (density) and 0.000 (stream); per-period increments of log10 |a_n| +0.00156, +0.00173, +0.00172, +0.00171 for the periods
ending 411..420 (mean since 366 now +0.00164). Fits on 357..420: power beta = 0.483 (rms 3.8e-4), 1/n |a_inf| = 0.0395 (6.0e-4), linear slope 0.000541 per order
(1.7e-4); on 390..420: 0.519 (9.9e-5), 0.0419 (1.5e-4), 0.000557 (5.6e-5); on 400..420: 0.534 (4.7e-5), 0.0428 (6.1e-5), 0.000564 (4.1e-5). The pattern of 410
continues: the power exponent (0.46 -> 0.53) and the 1/n limit (0.038 -> 0.043) rise monotonically with the window start, the linear slope rises slightly (0.000533 ->
0.000564) and has the smallest residual on every window tested at 420 (357.., 370.., 381.., 390.., 400..420). Finite statistics on printed four-digit multipliers; the models are not separated. OPEN. Through 430 (notes/cycle_diag_416_430.txt, notes/drift_fit_348_430.txt): multipliers -0.02551 (423), -0.02562 (426), -0.02572 (429), residual 0.001;
per-period increments of log10 |a_n| +0.00171, +0.00171, +0.00187, +0.00169 for the periods ending 420..429. Fits: 357..429: power beta = 0.493 (rms 5.1e-04); 1/n: |a_inf| = 0.04014, c1 = -83.6 (rms 7.9e-04); linear in n: slope 0.000546/order (rms 2.2e-04); 390..429: power beta = 0.531 (rms 1.8e-04); 1/n: |a_inf| = 0.04260, c1 = -94.2 (rms 2.6e-04); linear in n: slope 0.000563/order (rms 9.4e-05); 410..429: power beta = 0.561 (rms 5.5e-05); 1/n: |a_inf| = 0.04451, c1 = -102.2 (rms 7.3e-05); linear in n: slope 0.000580/order (rms 3.9e-05). Same pattern as at
420 (power exponent and 1/n limit rising with the window start, linear model with the smallest residual on the windows tested at 430); unseparated; OPEN. Through 440, the end of the run (notes/cycle_diag_426_440.txt, notes/drift_fit_348_440.txt): multipliers -0.02582 (432), -0.02593 (435), -0.02603 (438), residual
0.001; per-period increments of log10 |a_n| +0.00169, +0.00169, +0.00185, +0.00167 for the periods ending 429..438. Fits: 357..438: power beta = 0.502 (rms 6.3e-04); 1/n: |a_inf| = 0.04074, c1 = -86.1 (rms 9.9e-04); linear in n: slope 0.000551/order (rms 2.7e-04); 390..438: power beta = 0.540 (rms 2.4e-04); 1/n: |a_inf| = 0.04326, c1 = -96.9 (rms 3.7e-04); linear in n: slope 0.000568/order (rms 1.1e-04); 420..438: power beta = 0.576 (rms 4.3e-05); 1/n: |a_inf| = 0.04574, c1 = -107.2 (rms 5.2e-05); linear in n: slope 0.000583/order (rms 4.4e-05). Final
reading: over 357..438 the three models fit the printed multipliers with residuals 2e-4 .. 9e-4 in log10 (rounding noise about 9e-5); the exponential model has the
smallest residual on the longer windows (357.., 370.., 381.., 390.., 400.., 410..438), while on the final seven-point window 420..438 the power model is marginally better
(rms 4.27e-5 against 4.35e-5, the independent verifier); the power exponent and the 1/n limit rise monotonically with the window start (0.46 -> 0.58 and 0.038 -> 0.046), which is
what a drift faster than either model predicts would produce, but no model is excluded at this precision or on this length of window (an earlier version of this
sentence said 'smallest residual on every window'; corrected after an independent check). Separately labeled unrounded-data comparison (the independent verifier, not reproducible from the printed table): with the
class-0 multipliers taken from the unrounded coefficient vectors, the exponential model has the least residual on all seven windows (420..438: 1.10e-5 against 3.22e-5
for the power model), so the printed-data reversal on 420..438 is rounding-induced; this ranks the fits on the available orders and selects no asymptotic model. The multiplier |a_n| grew from 0.0228 (348)
to 0.0260 (438), i.e. the contraction per period weakened from 10^-1.64 to 10^-1.585; if the exponential model held indefinitely log10 M_n would be quadratic in n and the
series divergent, if the 1/n model held the series would converge with coefficient-norm radius about 1/0.29 = 3.4 .. 3.5 in z (the log factors make this a coefficient-norm
radius, not the physical boundary), and the power model gives Gevrey-type growth: OPEN, with the data through 440 not deciding among them. (All drift fits in this subsection use the multipliers as printed by cycle_diag.py with four significant digits; the verifier's
full-precision fits (independently checked) differ in the last printed digits for that reason only.)
(b6) One-step linearization error (suggested by the external referee; code/onestep_edge_error.py on the 350 checkpoint, notes/onestep_edge_error_350.txt): recomputing f_350 from the
stored lower orders with the pair sum restricted to min(i, j) <= L (same linear solve as the full step) gives the relative l1 error 0.703 (L = 1), 0.169 (3), 0.0099 (10),
7.4e-5 (30), 6.3e-6 (60), 2.1e-6 (100); with all pairs the recomputation reproduces the stored f_350 exactly (same summation order). So at order 350 the new order is produced to one percent by the pairs with min(i, j) <= 10 and to
1e-4 by min(i, j) <= 30; the departure of the K = 30 edge-only RUN from the full run (5.12) is therefore an accumulated feedback effect over many orders, not a
one-step one, and the recursion at these orders is close to linear in the newest orders with the first ten orders as fixed coefficients (finite-order observation).
(c) Factorial-weighted columns. The interior hump max_k log10(k! c_k/c_0) stays between +7.2 and +8.1 (k* = 65..74) on 330..350 after rising by about
+0.1 per order through 329 (+7.70 at 329); its stream counterpart falls from +5.9 (330) to +4.1 .. +4.8. The theory part's weighted factorial norm
W_n = log10 sum_q q! 12^q ||[t^q] F_n|| decays -0.25 per order on 340..350 (-0.30 on 280..290). The t-profile, diagonal-band and stream-mode shares
at 350 are in notes/tprofile_350.txt, notes/bands_350.txt and notes/stream_ratio_modes_341_350.json.
(b3) Orders 351..360 (same run, continued; same columns as the table above, no old values exist):
| 351 | 0 | -245.685 |  | -246.198 | -0.513 | +7.11 (71) | -124.7 | | | |
| 352 | 1 | -246.386 | -0.701 | -246.826 | -0.440 | +7.35 (73) | -124.4 | | | |
| 353 | 2 | -247.120 | -0.734 | -246.940 | +0.180 | +7.47 (75) | -123.5 | | | |
| 354 | 0 | -247.317 | -0.197 | -247.830 | -0.513 | +6.98 (74) | -123.2 | | | |
| 355 | 1 | -248.019 | -0.701 | -248.458 | -0.440 | +7.22 (74) | -122.8 | | | |
| 356 | 2 | -248.752 | -0.734 | -248.569 | +0.183 | +7.37 (73) | -121.9 | | | |
| 357 | 0 | -248.947 | -0.195 | -249.460 | -0.513 | +6.89 (75) | -121.7 | | | |
| 358 | 1 | -249.648 | -0.701 | -250.088 | -0.440 | +7.07 (77) | -121.3 | | | |
| 359 | 2 | -250.382 | -0.734 | -250.197 | +0.185 | +7.26 (74) | -120.5 | | | |
| 360 | 0 | -250.575 | -0.193 | -251.088 | -0.512 | +6.79 (76) | -120.2 | | | |
3-order decrements 351 -> 354 -> 357 -> 360: density -1.632, -1.630, -1.628; stream -1.632, -1.629, -1.628. 27-order slopes ending 355: -0.5510 / -0.5345;
ending 360: -0.5444 / -0.5421 (difference +0.002): the slopes have converged to the cycle value -0.544 per order. The three increments of the cycle are
frozen at -0.701 (class 1), -0.734 (class 2), -0.193 .. -0.197 (class 0) with log10(N/M) = +0.180 .. +0.185 at class 2 and -0.513 / -0.440 at classes 0 / 1.
The interior hump maximum decreases slowly (+7.59 at 350, +6.79 at 360, k* = 71..77); the weighted factorial norm W decays -0.23 per order on 350..360.
Sensitivity diagnostic (log_sin1_c3_pert329, first order): at 330 the boundary-perturbed continuation differs from the midpoint continuation by -1.5e-7 in
log10 M_330, -8.1e-7 in log10 N_330 and at most 3.6e-7 in any of the 109 log10 column norms, i.e. by the size of the 329 input uncertainty itself (2.5e-6
relative, 1.1e-6 in log10) without amplification at the first step; 331: -3.4e-7 / -2.5e-6; 332: -4.6e-7 / -1.1e-7; 333: -1.0e-7 / -2.9e-8; 334: -4.3e-8 /
+5.6e-8; 335: -1.6e-8 / -1.5e-8; 336: +6.1e-9 / +7.7e-10; 337: +1.3e-8 / +1.2e-8; 338: +6.3e-9 / -2.3e-9; 339: +2.5e-10 / -2.1e-10; 340: +1.5e-9 / +1.9e-9 (log10 M / log10 N differences; largest column difference
6.3e-9 at 340): for this one displacement the effect on the logged quantities is largest at 331 (2.5e-6 in log10 N, the size of the input displacement
itself), is not monotone (it rises from 336 to 337 and the column difference rises again at 338), and is below 2e-9 in both sums at 339 and 340. In the
natural relative full-vector l1 metric d_n = ||perturbed - reference||_1 / ||reference||_1 (the independent verifier, 768-bit directed sums) the input displacement
is D_in = 3.58e-6 (stream, 329) and the stream output is amplified at first, d_330 = 4.39e-6 (factor 1.23) and d_331 = 6.86e-6 (factor 1.92), then falls below
D_in at every order through 340: a temporary amplification by a factor below 2 followed by attenuation (one sample; a diagnostic, not a bound; the earlier
wording 'no amplification' referred to the weaker metric of the log sums and is withdrawn; notes/compare_pert.txt). Final table through 350 (log10 M / log10 N differences): 341: +1.2e-09 / -5.5e-10, 342: +4.6e-10 / +1.7e-11, 343: +6.8e-10 / +5.1e-10, 344: +4.2e-10 / -1.5e-10, 345: -1.3e-11 / -4.1e-11, 346: +6.6e-11 / +7.9e-11, 347: +3.5e-11 / -3.0e-11, 348: -2.1e-11 / -1.0e-11, 349: -8.9e-12 / +1.9e-11, 350: -4.5e-11 / -4.7e-12; largest column difference over 341..350 6.3e-09; over the whole continuation 330..350 the largest difference in the log sums is 2.5e-6 (log10 N at 331) and the largest at the end is 4.5e-11 at 350: the displaced start is attenuated by three orders of magnitude by 350 in this metric (one sample). The differences are computed from the logged float64
statistics (log10 values near -245), so entries below 1e-10 carry only two reliable significant digits (the verifier's directed 768-bit recomputation gives
3.49e-11 at 347 where this table prints 3.50e-11).
(d) Status. Through 400 (where the continuation ended) the density sum M_n decreases at every order; the stream sum N_n rose once (+0.681 decades at 332) and was flat at 338, and
decreases at every order from 339 on; both decline by 1.63 .. 1.61 decades per period since 333 (through 399), so Proposition 14.17/14.19 of
the theory part's theory (geometric stream or density sums are equivalent to exterior convergence of the canonical log series) is neither confirmed nor
refuted by these data: the decay changed at 330 from 10^-0.70 to 10^-0.544 per order and has held that rate, with a drift of +0.002 per period located in the resonant class-0 step, for twenty-two periods (333..399); whether the cycle
persists is OPEN. The continuation ended at 400 (checkpoint ckpt/log_sin1_c3_from329.pkl, 1.6 GB); a further continuation to 440 was started at 18:17Z and has
ended at 440 (22:59Z): through 440 the cycle holds with the same two frozen increments, the class-0 increment weakening steadily (-0.197 at 354, -0.173 at 399,
-0.161 at 420, -0.151 at 438), the period decrement -1.585 at 435 -> 438, the 27-order slopes -0.528 .. -0.532 (density and stream alike) and the root tests 0.2150 / 0.2152.
No further continuation was run; the final checkpoint (2.2 GB, order 440) was kept with the run records and is not included in the accompanying artifacts.

### 5.12 Edge-only (linearized) variants of the canonical log recursion at delta = 2/3 (theory part's request (s), 07:37Z)
Definition: code/logff.py --edge K replaces the quadratic sum Q_n = sum_{i+j=n} [ ... ] by its restriction to the pairs with
min(i, j) <= K (K = 1: only (1, n-1) and (n-1, 1), i.e. the recursion linearized around the first order; the canonical Poisson
inverse with zero resonant constants and the canonical normalization are unchanged; f_1 = sin theta). These are NOT the stationary
series; they isolate which pairs produce the growth rate, the slower stream rate and the interior hump of the full canonical run.
Float64 runs to N = 300 (logs/log23_edge1_float.jsonl, log23_edge3_float.jsonl; the independent verifier checked the edge-1 float checkpoint
against an exact Cartesian table through n = 18, 830 coefficients, maximal error 3.8e-16 relative to the order norm):
| pairs kept | M_300^(1/300) | 27-order slopes of log10 M_n / log10 N_n ending at 100, 200, 300 | log10(N_300/M_300) |
|---|---|---|---|
| min(i, j) <= 1 | 0.16267 | -0.786/-0.791, -0.781/-0.784, -0.780/-0.782 | -2.840 |
| min(i, j) <= 3 | 0.18699 | -0.725/-0.731, -0.721/-0.723, -0.719/-0.721 | -2.785 |
| all (canonical run, arb 512) | 0.19433 | -0.709/-0.720, -0.704/-0.709, -0.701/-0.684 | -2.010 (fluctuating by residue class) |
Roots at n = 100 / 200: 0.1574 / 0.1611 (K = 1), 0.1807 / 0.1852 (K = 3), 0.1874 / 0.1923 (full). In the edge variants the
density and stream slopes agree to 0.002 per order and N/M decreases smoothly, whereas the full run has a stream slope about
0.015 decades per order above the density slope at 300..316 and a residue-class fluctuation of N/M. Factorial statistic
max_{k>=1} log10(k! c_k/c_0) among the retained floating columns (float64 drops the smallest top log columns beyond n about 200,
so the maximum over the dropped columns is not certified by these runs; see the independent verification): -9.90 (K = 1) and -7.62 (K = 3) at n = 300, both at
k = 1, with interior columns far below (K = 3 at 300: -15.8, -19.2, -22.6, -26.3, -30.7 at k = 10, 20, 30, 40, 50) against +4.897 at
k = 59 for the full run. K = 10 (float64, N = 300, log23_edge10_float): M_300^(1/300) = 0.19311; slopes -0.711/-0.718 (100), -0.706/-0.709 (200), -0.705/-0.706 (300);
log10(N/M) = -2.775 at 300 (smooth); maximum of log10(k! c_k/c_0) among retained columns at k = 1: -0.97 (100), -0.72 (200), -0.55 (300), with
the interior columns rising with n but still far below (k = 40: -20.4 at 200, -17.9 at 300; k = 50: -29.2, -20.2): no hump through 300 at K = 10,
so pairs with min(i, j) > 10 are needed for the hump, the residue-class fluctuation and the stream-rate gap of the full run.
Rigorous 1024-bit ball run of K = 1 (log23_edge1_p1024, N = 300, all columns kept, norm-relative radii 10^-248 (n = 100) to 10^-127 (300) for
density and stream): root 0.16267, slopes -0.780/-0.782 at 300, log10(N/M) = -2.840, and the maximum of log10(k! c_k/c_0) over ALL k >= 1 is
at k = 1: -8.299 (100), -9.311 (200), -9.635 (250), -9.900 (300) (stream -9.843), with the interior columns at k = 10, 20, 30, 40, 50, 60 for
n = 300: -32.2, -50.8, -59.5, -64.4, -69.1, -74.4: certified absence of a hump in the K = 1 variant through 300. The top column has
log10 l1 = -415.4 at n = 250 (q = 82; the verifier's exact t^82 sin(165 theta) coefficient is 10^-415.54, independently checked) and -504.8 at 300 (q = 98).
Float64 against the ball run: the plain norms and the low columns agree to 1e-13 relative at n = 100; at n >= 200 the float run has lost the
columns below 10^-308 (64 of 65 retained at 200, 49 of 82 at 250, 27 of 98 at 300) and its retained subnormal columns are off by up to 0.29
in log10 at 300, while the maxima at k = 1 and the plain sums agree to all printed digits. K = 3 ball run (log23_edge3_p1024, 1024 bits, N = 300, radii 10^-207 at 200 and 10^-156 at 300): the maximum of log10(k! c_k/c_0) over ALL
columns is at k = 1: -7.107 (200), -7.396 (250), -7.620 (300) (stream -7.608), interior columns at 300 (k = 10..60): -15.8, -19.2, -22.6, -26.3,
-30.7, -35.8; root 0.18699, slopes -0.719/-0.721 at 300: certified absence of a hump for K = 3 through 300 as well.
K = 30 (float64, N = 300, log23_edge30_float): a DIFFERENT behaviour. Through n = 265 its plain density sum tracks the full run within 0.08
decades (the K = 10 truncation is 0.5..0.7 decades below) with the same increments -0.70 per order; from n = 263 the stream increments at the
class-2 orders (n = 2 mod 3) shrink (+0.01 at 263, -0.11, -0.20, -0.25, ... ) and turn positive (+0.73 at 292, +0.41 at 295, +0.25 at 298), the
density increments at the following class-0 orders turn positive (+0.30 at 293, +0.15 at 296, +0.03 at 299), and M_300 ends 3.8 decades
ABOVE the full run (root 0.2000 against 0.1943; 27-order slopes -0.582 (M) / -0.554 (N) ending at 300 against -0.704/-0.706 ending at 200;
log10(N/M) = +0.60 at 295, -0.50 at 300, from -2.57 at 200). The factorial statistic among retained columns is at k = 1 (-0.37 density,
+0.12 stream at 300) with the interior columns at -1..-4 (k = 40..60), unlike the full run's hump (+4.9 at k = 59) and unlike K <= 10.
Caveat: float64 only; the departure begins where a roundoff perturbation of relative size 1e-16 amplified by a factor of about 1.14 per
order would reach order one, so an unstable direction of the truncated recursion seeded by roundoff cannot be excluded from this run alone.
Roundoff probe (log23_edge30_float_pert, same run with the leading amplitude 1 + 1e-10, which changes every rounding pattern while the exact
normalized values log10 M_n - n log10(1 + 1e-10) are unchanged): the two float64 runs agree in log10 M_n / log10 N_n to 2.6e-12 / 1.0e-10 through
263, 1.3e-10 / 1.5e-9 through 281 and 6.4e-6 / 1.3e-5 through 300 (verifier's exact maxima, independently checked). This is empirical sensitivity evidence
against rounding-pattern-dependent error; it cannot exclude an error component shared by both runs (independently checked), so the decades-large
departure of K = 30 from the full run is attributed to the truncated recursion only with that qualification; the 512-bit ball run below is the
proper check.
K = 30 at 512-bit balls (log23_edge30_p512, N = 300, finished 13:10Z; the verifier's independent selected Cartesian audit at order 300 (independently checked) reproduces log10 M = -212.3586, log10 N = -212.9767 and the norm-relative radii 6.5e-21 / 8.5e-21): through n = 250 (norm-relative radii 10^-40 for density and stream) the
ball midpoints agree with the float64 run to 2.6e-13 (log10 M) and 3.6e-12 (log10 N), so the float values through 250 are certified to that
accuracy, including the departure of the stream: N_k30 - N_full = -0.17 (230), +0.53 (240), +1.06 (245), +0.89 (250) decades, M_k30 - M_full =
-0.08 .. -0.04; 27-order slopes ending 250: K = 30 M -0.7015 / N -0.6588 against the full run's -0.7028 / -0.7052 (rigorous for both).
Values at 270: M -192.277, N -193.261 (M - M_full = +0.125, N - N_full = +1.542; agreement with float 1.8e-9 / 1.1e-8; radius 10^-32.3);
slopes ending 270: K = 30 M -0.6990 / N -0.6818, full -0.7024 / -0.6977. 290: log10 M = -205.881, log10 N = -206.706; M - M_full = +0.550, N - N_full = +1.327; agreement with the float run -8.4e-02 / -5.4e-01; norm-relative radius 10^-23.6 (rigorous); 27-order slopes ending 290: K = 30 M -0.6740 / N -0.6563; full M -0.7015 / N -0.6737. 300: log10 M = -212.359, log10 N = -212.977; M - M_full = +1.078, N - N_full = +2.470; float - ball = +2.70 / +2.82; norm-relative radius 10^-19.9 (rigorous); 27-order slopes ending 300: K = 30 M -0.6813 / N -0.6780; full M -0.7010 / N -0.6839 (run finished at 300).
FLOAT64 IS NOT VALID FOR THE FULL RECURSION BEYOND ABOUT 270: the full float64 run (log23_full_float) agrees with the certified 512-bit run
to 1e-12 in every retained column through 240, loses the columns below 1e-308 from 250 on (79 of 82 at 250, 75 of 98 at 300), and then its
low columns depart: column 0 off by 5.6e-6 (log10) at 270, 0.23 at 280, 3.5 at 290, 6.2 decades at 300 (stream 7.7), while its amplitude-
perturbed twin agrees with it to 1e-6 (a shared error, invisible to the probe; the independent verifier). The K = 30 float run holds longer (agreement
with its 512-bit ball run 1e-8 at 270) but also departs from the balls afterwards: float - ball = 270: +1.8e-09 / +1.1e-08; 275: -3.7e-07 / -1.6e-05; 280: -1.3e-04 / -6.4e-04; 285: -9.3e-03 / -2.4e-02; 290: +8.4e-02 / +5.4e-01 (log10 M / log10 N), so its values
beyond about 280 are superseded by the ball run. Both float twins were stopped at 300/302; they are kept only as
evidence of this ill-conditioning. All statements about the canonical 2/3 series beyond 270 rest on ball arithmetic. A 256-bit ball run of K = 30 lost its rigorous radii at n = 166 (ball growth 0.455 decades per order from 77 digits) and
was replaced by the 512-bit run (log23_edge30_p512, N = 300, finished); the float run with K = 60 (N = 400, paused at 240) and the full float64 run (all pairs,
log23_full_float, stopped at 302) were withdrawn as evidence beyond 270 for the reason given above.
Reading (finite data, tentative): most of the geometric rate is produced by the products of the first three orders with the previous
orders (K = 3 recovers 0.187 of 0.194), while the interior hump of the factorial-weighted log columns and the slower stream rate of
the full run are absent from both edge variants through n = 300 and therefore need the interior pairs min(i, j) > 3.

### 5.13 The tuned convergent series at c = 3 (theory part's Theorem T and Corollary T.3): independent ball-arithmetic computation (code/tuned_c3.py)
Setting (theory 12.4): c_l = 3, delta = 2/3, f_1 = sin theta + b sin 3theta with b a real root of the degree-6 polynomial P6 (b_1 = 0.2806616627...,
b_2 = 0.6463522898...), pure power ansatz (no logarithms); at every resonant order n = 3k the free multipole coefficient H_n of sin((2k-2) theta)
in g_n is chosen so that the next obstruction O_(3k+3) = a_(3k+3, 2k-1) vanishes (H_n = -R_k/sigma_k, Lemma T.1). Implementation: b enclosed by
interval Newton (radius 1e-300 at 1024 bits); phi_1, phi_2, phi_3 and sigma_k by this implementation's own sine-series products and Poisson inverses; R_k from a
provisional (H_n = 0) computation of orders 3k+1..3k+3; affine correction f_(3k+i) += H_n phi_i; every tuned obstruction must be a ball containing
zero (the code raises otherwise). Independent of the theory part's FFT/double code and of the verifier's exact Cartesian code.
Validation (b_1, 256 bits, N = 30): H_6 = 1.30682168595985916901520703386e-6, H_9 = 2.255085806559639e-9, H_12 = 1.724168205113161e-10,
H_15 = -1.796939693571644e-11, sigma_2 = -2.7939862742779614540e-4, sigma_3 = -7.5793360667520917730e-4, sigma_4 = -3.8124461471579738968e-5:
equal to the theory part's exact/40-digit values to every printed digit; tuned obstructions: balls containing zero with radii 1e-79..1e-81.
Production run tuned_b1_p1024 (1024 bits, N = 400 target; radii: norm-relative 10^-271 at n = 60, 10^-226 at 137; tuned obstruction radii
about 1e-300): root tests ||f_n||_l1^(1/n) = 0.1448 (6), 0.1506 (12), 0.1991 (18), 0.2180 (24), 0.2261 (30), 0.2359 (60), 0.2406 (90), 0.2454
(120), 0.2477 (150), 0.2500 (210), 0.2520 (300), 0.2532 (360), 0.2533 (390) (run finished at 398; norm-relative radius 10^-84 at 390,
tuned obstruction radii 10^-309 .. 10^-316 at every resonant order, i.e. certified zero to that level); the theory part's double-precision values
0.151 (12), 0.241 (90), 0.251 (240) agree. ||g_n||^(1/n) and |H_n|^(1/n) track the density root (0.2531 and 0.2531 at 390). Least-squares
fit log10 ||f_n|| = n log10 A + beta log10 n + c: A = 0.2587 (n >= 200; beta = -1.16), 0.2592 (n >= 120) (theory part: 0.259, 0.261). sigma_k
decreases monotonically from -1.389e-4 (k = 20) to -1.851e-4 (k = 130) toward the theory part's sigma_infinity = -1.948e-4; the smallest |sigma_k|
is at k = 4 (3.812e-5, the verifier's topic-123 minimum). The signs of H_(3k) change in irregular runs of two to four (an earlier claim of an
exact period 6 was refuted by the independent verifier: H_30 < 0 and H_48 > 0 break it); no inference about singularity angles is made. Top frequency
exactly 4n - 1 at every order.
Second root b_2 = 0.646352289880934644313296909064086106711277... (run tuned_b2_p1024, 1024 bits, N = 300): root tests 0.6756 (60), 0.6874 (90),
0.6960 (120), 0.7011 (150), 0.7053 (180), 0.7092 (210), 0.7108 (240), 0.7131 (270) (theory part's double value 0.711 at 240); ||g_n||^(1/n) and
|H_n|^(1/n) 0.7110, 0.7107 at 270; fit A = 0.7314 (n >= 120), 0.7256 (n >= 200) (theory part: 0.733, 0.731); sigma_k from -7.49e-3 (k = 20) to -9.18e-3
(k = 90), smallest |sigma_k| = 1.5684e-3 at k = 4 (verifier's topic-123 minimum); tuned obstruction radii 10^-231 .. 10^-290; norm-relative radii
10^-280 .. 10^-191; the signs of H_(3k) show no simple period. Both tuned series thus have geometric growth with the theory part's constants in
certified arithmetic through 270..390 orders (NUMERICAL EVIDENCE for the constants; convergence is the theorem).
Direct evaluation (section 13; code/evaluate_series.py on the n <= 93 checkpoint; weighted stationary residual sup_theta |R^(-gamma) residual|
of the truncation rho_N, psi_N with the tuned stream coefficients, resid0, and its angular derivative, resid1):
| R | z = R^(-2/3) | resid0 at N = 10, 20, 40, 80 | resid1 at N = 80 | tail0 at N = 80 |
|---|---|---|---|---|
| 0.25 | 2.520 | 9.6e-5, 2.3e-5, 2.7e-9, 8.3e-17 | 4.5e-15 | 6.3e-19 |
| 0.5 | 1.587 | 1.0e-6, 2.6e-9, 2.3e-17, 7.8e-33 | 4.2e-31 | 5.6e-35 |
| 1 | 1 | 1.0e-8, 2.7e-13, 2.1e-25, 7.1e-49 | 4.0e-47 | 4.9e-51 |
| 2 | 0.630 | 1.0e-10, 2.8e-17, 2.1e-33, 6.5e-65 | 3.7e-63 | 4.3e-67 |
| 4 | 0.397 | 1.0e-12, 2.8e-21, 2.1e-41, 5.9e-81 | 3.3e-79 | 3.8e-83 |
Deeper check on the final checkpoint (orders <= 393 used; notes/eval_tuned_b1_p1024_N320.json): resid0 at N = 40, 80, 160, 320: R = 0.2 (z = 2.92):
1.2e-6, 1.2e-11, 1.3e-21, 8.8e-41; R = 0.25: 2.7e-9, 8.3e-17, 6.1e-32, 1.3e-61; R = 0.5: 2.3e-17, 7.8e-33, 5.0e-64, 8.4e-126; R = 1: 2.1e-25, 7.1e-49,
4.1e-96, 5.5e-190 (resid1 two decades larger): the decay rate per doubling of N is itself geometric at every R, consistent with radius about
1/0.259 = 3.9 in z (r > 0.13).
The residual decays geometrically in N at every tested radius down to R = 0.2 (z = 2.92, inside the apparent radius 3.9 in z),
and the partial sums R^(-gamma) rho_N(theta) at theta = 0.3, 0.9, 1.3 are stable to 8 digits from N = 20 on at R >= 0.5 (midpoint evaluation on a
grid; the verifier's interval machinery can certify selected values). Convergence itself is PROVED by Theorem T (no explicit radius); these
finite-order data indicate the exterior radius r > about 0.13 (b_1), consistent with the theory part's estimate A^(3/2) = 0.26^(1.5).

### 5.13b Tuned series at other rational delta (Q = 4, Q = 5, delta = 4/9, delta = 1/3): the theory part's Theorem T_Q, Corollary T_(9,2) and Corollary T_6 (code/tuned_cQ.py, code/tuned_general.py)
Same construction as 5.13 with the period of the resonances set by delta (2/Q: resonances at n = kQ, k >= 2; 4/9: n = 9k, k >= 1, free stream mode sin((4k-2) theta));
the first obstruction polynomial in b is the theory part's (Q = 4, 6) or the verifier's (Q = 5, 4/9) exact polynomial; every run at 1024 bits with every tuned obstruction a ball
containing zero (the code raises otherwise). All growth constants below are finite-order fits (NUMERICAL EVIDENCE); convergence is the respective theorem.
Q = 4 (c = 2, delta = 1/2; code/tuned_cQ.py with the theory part's degree-8 obstruction polynomial; root b = 0.62678749907802936230022892011...):
run tunedQ4_r6_p1024 (1024 bits, N = 300): root tests ||f_n||^(1/n) = 1.7957 (40), 1.9707 (80), 2.0136 (120), 2.0341 (160), 2.0460 (200),
2.0596 (240), 2.0716 (280), 2.0818 (300); ||g_n||^(1/n), |H_n|^(1/n) within 0.03; fit A = 2.146 (n >= 120), 2.148 (n >= 200); |H_n| grows like
A^n (log10 |H_280| = 89.05); sigma_k: -0.31823 (k = 2), +0.82170 (3), +0.11346 (4), minimum |sigma_k| = 3.2001e-3 at k = 5 (the theory part's value), then
increasing to +6.888e-3 (k = 74); tuned obstruction radii 10^-282 (n = 40) .. 10^-59 (300) (they grow with |H|; still certified zero);
norm-relative radii 10^-291 .. 10^-154. So for this root the series in z = r^(-1/2) has an apparent radius 1/2.15 = 0.47, i.e. r > about 4.6
(the theory part's proved radius 2^82 is far outside). Section-13 residuals of this truncation (notes/eval_tunedQ4_r6.json; weighted sup residual
resid0 at N = 10, 20, 40, 80): R = 32 (z = 0.177): 6.0e-6, 4.6e-11, 5.8e-19, 2.2e-35; R = 16: 1.9e-4, 4.7e-8, 6.0e-13, 2.5e-23; R = 8 (z = 0.354):
6.1e-3, 4.7e-5, 6.0e-7, 3.0e-11; R = 4 (z = 0.5): 0.19, 0.047, 0.61, 1.1e3 (growing from N = 40); R = 2: 6.1, 51, 3e10, 8e25: geometric decay exactly
inside the apparent radius and divergence outside, as for a convergent series with radius about 0.47 in z. Q = 4, root b = 0.35150441784454223759135039156600... (tunedQ4_r5_p1024, N = 300): root tests 0.7846 (40), 0.8473 (80), 0.8588 (120),
0.8665 (160), 0.8731 (200), 0.8806 (240), 0.8825 (280), 0.8837 (300), still rising; fits A = 0.92 (n >= 120) / 0.89 (n >= 200) with an unstable
beta, so only the root test is quoted; |H_n|^(1/n) = 0.8828 at 280; sigma_k: -1.115e-2 (2), +4.467e-2 (3), +9.37e-3 (4), minimum |sigma_k| =
1.2089e-3 at k = 5 (the theory part's value), then rising to +2.56e-3 (k = 74); obstruction radii 10^-296 .. 10^-195, norm-relative radii
10^-291 .. 10^-179 (certified). Q = 4, root b = 0.18776307412587226606863351909196... (tunedQ4_r4_p1024, N = 300): root tests 0.3398 (40), 0.3553 (80), 0.3609 (120), 0.3632 (160),
0.3673 (200), 0.3689 (240), 0.3701 (280), 0.3709 (300); |H_n|^(1/n) = 0.3696 at 280; fits A = 0.38 / 0.37 (beta unstable); sigma_k: +4.453e-4 (2),
+1.146e-3 (3), +3.567e-4 (4), minimum 1.1417e-4 at k = 5 (the theory part's value), rising to +3.27e-4 (k = 74); obstruction radii 10^-308 .. 10^-299;
norm-relative radii 10^-289 .. 10^-170 (certified).
Q = 4, root b = -0.2796388302190664589294172954459... (tunedQ4_r1_p1024, N = 300): root tests 1.1863 (40), 1.2606 (80), 1.2896 (120), 1.3048 (160), 1.3144 (200), 1.3221 (240), 1.3269 (280), 1.3286 (300); |H_n|^(1/n) = 1.3160 at 280; sigma_k: -1.419e-01 (2), +2.544e-01 (3), +4.139e-02 (4), minimum 3.6425e-02 at k = 5, last +5.323e-02 (k = 74); norm-relative radius 10^-210 at 300.
Q = 4, root b = 0.07714673875509530562896574408498... (tunedQ4_r3_p1024, N = 300): root tests 0.2016 (40), 0.2113 (80), 0.2170 (120), 0.2186 (160), 0.2202 (200), 0.2216 (240), 0.2220 (280), 0.2225 (300); |H_n|^(1/n) = 0.2195 at 280; sigma: -2.429e-04 (n = 8), -3.872e-04, +1.393e-04, minimum |sigma| = 5.1502e-05 at n = 296, last +5.150e-05 (n = 296); obstruction radii 10^-309 .. 10^-292; norm-relative radius 10^-96 at 300.
The verifier confirmed the root-6 prefix through 40 by an independent two-continuation Cartesian
construction (independently checked) and the root-5 prefix through 40 (independently checked). Q = 4, root b = 0.03993569519011528687411717583713... (tunedQ4_r2_p1024, N = 300): root tests 0.2577 (40), 0.2725 (80), 0.2787 (120), 0.2823 (160), 0.2846 (200), 0.2862 (240), 0.2874 (280), 0.2879 (300); |H_n|^(1/n) = 0.2747 at 280; sigma: -6.882e-04 (k = 2), -1.207e-04 (3), +6.364e-04 (4), minimum |sigma| = 1.2073e-04 at k = 3, last +7.203e-04 (k = 74); obstruction radii 10^-310 .. 10^-323; norm-relative radius 10^-162 at 300.
Q = 4 summary (root -> root test at 300): 0.6268 -> 2.082, 0.3515 -> 0.884, 0.1878 -> 0.371, 0.0771 -> 0.2225, 0.0399 -> 0.2879, -0.2796 -> 1.329; all six
verified-zero obstructions throughout. Q = 5 (six roots of the verifier's degree-10 polynomial), delta = 4/9 (five roots) and delta = 1/3 (six roots) follow.
Q = 5 (c = 5/3, delta = 2/5, period 5), root b = 0.55998105347197690323396509054213... (tunedQ5_r6_p1024, N = 300): root tests 2.9360 (50), 3.2691 (100), 3.3370 (150), 3.3704 (200), 3.3959 (250), 3.4202 (300); fit A = 3.5878 (n >= 150); |H_n|^(1/n) = 3.4320 at 295; sigma: -6.9863e-01 (n = 10), +4.4035e+00 (15), -8.0785e+00 (20), minimum |sigma| = 6.8492e-03 at n = 25, last +1.4145e-01 (n = 295); obstruction radii (absolute) 10^-302 .. 10^-48 against coefficient scale 10^160; norm-relative radius 10^-207 at 300; apparent radius r > A^(5/2) = 24.4.
delta = 2/5 (c = 5/3, period 5), root b = 0.3152765949879686488030044345731622... (tunedQ5_r5_p1024, N = 300): root tests 1.4487 (50), 1.6109 (100), 1.6411 (150), 1.6534 (200), 1.6713 (250), 1.6821 (300); fit A = 1.7324 (n >= 150; power exponent -1.4; straight-line slope 1.7213); |H_n|^(1/n) = 1.6871 at 295; sigma: +3.3548e-02 (n = 10), -3.4830e-03 (n = 15), -2.6770e-01 (n = 20), minimum |sigma| = 1.1522e-03 at n = 25, last +2.7461e-03 (n = 295); obstruction radii (absolute) 10^-304 .. 10^-120 against coefficient scale 10^67; norm-relative radius 10^-187 at 300; z = r^(-2/5), apparent radius r > A^(5/2) = 3.95.
delta = 2/5 (c = 5/3, period 5), root b = 0.2120921308796327686714721499491465... (tunedQ5_r4_p1024, N = 300): root tests 0.7861 (50), 0.8508 (100), 0.8619 (150), 0.8709 (200), 0.8746 (250), 0.8781 (300); fit A = 0.9010 (n >= 150; power exponent -1.6; straight-line slope 0.8945); |H_n|^(1/n) = 0.8771 at 295; sigma: +4.3162e-03 (n = 10), -1.4912e-02 (n = 15), -1.9109e-02 (n = 20), minimum |sigma| = 4.1783e-04 at n = 30, last -1.2374e-03 (n = 295); obstruction radii (absolute) 10^-306 .. 10^-206 against coefficient scale 10^-18; norm-relative radius 10^-189 at 300; z = r^(-2/5), apparent radius r > A^(5/2) = 0.771.
delta = 2/5 (c = 5/3, period 5), root b = 0.1253337788213112811670214739011123... (tunedQ5_r3_p1024, N = 300): root tests 0.3945 (50), 0.4123 (100), 0.4161 (150), 0.4216 (200), 0.4250 (250), 0.4271 (300); fit A = 0.4403 (n >= 150; power exponent -2.7; straight-line slope 0.4348); |H_n|^(1/n) = 0.4254 at 295; sigma: -4.1899e-04 (n = 10), -8.5117e-04 (n = 15), -3.5011e-04 (n = 20), minimum |sigma| = 1.5819e-04 at n = 25, last -3.0992e-04 (n = 295); obstruction radii (absolute) 10^-309 .. 10^-295 against coefficient scale 10^-112; norm-relative radius 10^-185 at 300; z = r^(-2/5), apparent radius r > A^(5/2) = 0.129. (theory part's exact minimum for this root: 1.5818609e-4 at k = 5: reproduced.)
Direct evaluation (section 13) for the Q = 5 root 0.5600 (notes/eval_tunedQ5_r6.json; weighted stationary residual sup_theta |R^(-gamma) residual| of the
truncation rho_N, psi_N with the tuned stream coefficients, resid0, its angular derivative resid1, and the weighted tail z^N sup|f_(N+1)|, tail0):
| R | z = R^(-2/5) | resid0 at N = 10, 20, 40, 80 | resid1 at N = 80 | tail0 at N = 80 |
|---|---|---|---|---|
| 4 | 0.574 | 2.0e+02, 2.2e+06, 5.1e+19, 1.1e+46 | 3.1e+47 | 6.5e+21 |
| 8 | 0.435 | 6.5e+00, 8.8e+01, 1.4e+10, 7.6e+26 | 2.1e+28 | 1.5e+12 |
| 16 | 0.330 | 4.0e-01, 2.9e-01, 2.4e+01, 1.8e+08 | 1.9e+09 | 3.5e+02 |
| 32 | 0.250 | 2.6e-02, 1.2e-03, 3.6e-04, 5.6e-06 | 1.7e-04 | 8.1e-08 |
| 64 | 0.189 | 1.6e-03, 4.7e-06, 5.1e-09, 1.2e-15 | 3.7e-14 | 1.9e-17 |
| 128 | 0.144 | 1.0e-04, 1.9e-08, 7.3e-14, 2.6e-25 | 8.0e-24 | 4.4e-27 |
The residual decreases geometrically in N for R >= 32 (z <= 0.25; A z = 0.9 at R = 32, so slowly there) and grows for R <= 16 (z >= 0.33, A z >= 1.2): the
truncations behave as a convergent series with exterior radius between 16 and 32, consistent with the fitted A^(5/2) = 24 (finite-order observation).
delta = 2/5 (c = 5/3, period 5), root b = 0.0489986661750143195402286095098221... (tunedQ5_r2_p1024, N = 300): root tests 0.3488 (50), 0.3635 (100), 0.3698 (150), 0.3742 (200), 0.3766 (250), 0.3788 (300); fit A = 0.3932 (n >= 150; power exponent -3.9; straight-line slope 0.3863); |H_n|^(1/n) = 0.3744 at 295; sigma: -6.3756e-05 (n = 10), +6.8946e-04 (n = 15), +6.3860e-05 (n = 20), minimum |sigma| = 2.1770e-06 at n = 40, last +7.1085e-05 (n = 295); obstruction radii (absolute) 10^-309 .. 10^-263 against coefficient scale 10^-128; norm-relative radius 10^-137 at 300; z = r^(-2/5), apparent radius r > A^(5/2) = 0.097. (theory part's exact minimum for this root: 2.1770197e-6 at k = 8: reproduced.)
delta = 2/5 (c = 5/3, period 5), root b = -0.489757991348773502845123350728471... (tunedQ5_r1_p1024, N = 300): root tests 3.3540 (50), 3.6850 (100), 3.7356 (150), 3.7705 (200), 3.7986 (250), 3.8163 (300); fit A = 3.9097 (n >= 150; power exponent -0.7; straight-line slope 3.8981); |H_n|^(1/n) = 3.8225 at 295; sigma: +1.1014e+01 (n = 10), -2.3000e+01 (n = 15), +1.2839e+01 (n = 20), minimum |sigma| = 4.0131e-01 at n = 25, last -8.1347e-01 (n = 295); obstruction radii (absolute) 10^-302 .. 10^-34 against coefficient scale 10^173; norm-relative radius 10^-208 at 300; z = r^(-2/5), apparent radius r > A^(5/2) = 30.2. (theory part's exact minimum for this root: 0.40131060 at k = 5: reproduced.)
Q = 5 summary (root -> fitted A -> apparent exterior radius r > A^(5/2)): 0.5600 -> 3.59 -> 24; 0.3153 -> 1.73 -> 3.9; 0.2121 -> 0.90 -> 0.77; 0.1253 -> 0.44 ->
0.13; 0.0490 -> 0.39 -> 0.10; -0.4898 -> see the line above (all six roots, 1024 bits, 300 orders, obstructions certified zero; the theory part's Corollary T_5 proves
convergence for all six, sufficient radii 2^(61/2) .. 2^(73/2) (the independent verifier); the theory part's exact |sigma_k| minima are reproduced for every root).
delta = 4/9 (c = 9/5, period 9), root b = 1.85667533841492522806473426344601... (tuned49_r5_p1024, N = 306): root tests 7.348 (36), 9.129 (72), 9.551 (108), 9.613 (144), 9.795 (180), 9.828 (216), 9.873 (252), 9.964 (288), 10.005 (300); fit A = 10.687 (n >= 150); |H_n|^(1/n) = 10.035 at 288; sigma: +6.4737e+04 (n = 9), -1.2422e+06 (18), +3.9890e+06 (27), minimum |sigma| = 4.1140e+03 at n = 45, last +5.8325e+03 (n = 297); obstruction radii (absolute) 10^-299 (n = 9) .. 10^93 (n = 306), against coefficient magnitudes 10^300 at 306, i.e. about 10^-207 relative to the coefficient scale; norm-relative radius 10^-211 at 306; z = r^(-4/9), apparent radius r > A^(9/4) = 206. (The theory part's Corollary T_(9,2) proves convergence for all five roots; the finite data give the growth constants.)
Direct evaluation (section 13) for the delta = 4/9 root 1.8567 (notes/eval_tuned49_r5.json; resid0 = weighted stationary residual sup_theta |R^(-gamma) residual| of the truncation with the tuned
stream coefficients at N = 10, 20, 40, 80; resid1 = its angular derivative; tail0 = z^N sup|f_(N+1)|):
| R | z = R^(-4/9) | resid0 at N = 10, 20, 40, 80 | resid1 at N = 80 | tail0 at N = 80 |
|---|---|---|---|---|
| 32 | 0.2143 | 1.8e+03, 6.5e+07, 4.4e+17, 2.5e+49 | 6.3e+50 | 2.8e+24 |
| 64 | 0.1575 | 3.0e+01, 7.0e+02, 1.5e+07, 4.7e+28 | 1.4e+30 | 5.6e+13 |
| 128 | 0.1157 | 1.4e+00, 8.8e-01, 4.2e-01, 9.0e+08 | 1.7e+10 | 1.1e+03 |
| 256 | 0.0850 | 6.6e-02, 1.9e-03, 1.9e-06, 1.3e-06 | 3.9e-05 | 2.2e-08 |
| 512 | 0.0625 | 3.0e-03, 4.1e-06, 8.8e-12, 2.6e-17 | 8.0e-16 | 4.4e-19 |
| 1024 | 0.0459 | 1.4e-04, 8.6e-09, 3.9e-17, 5.3e-28 | 1.7e-26 | 8.7e-30 |
Geometric decay for R >= 512, marginal at R = 256 (A z = 0.91: 6.6e-2, 1.9e-3, 1.9e-6, 1.3e-6), growth for R <= 128: apparent exterior radius between 128 and 256, consistent with the fitted A^(9/4) = 206 (finite-order observation).
delta = 4/9, root b = 0.06343727445510858384755005843447... (tuned49_r1_p1024, N = 306): root tests 0.2411 (36), 0.2767 (72), 0.2869 (108), 0.2915 (144), 0.2946 (180), 0.2964 (216), 0.2979 (252), 0.2996 (288), 0.3007 (300); fit A = 0.3041 (n >= 150); |H_n|^(1/n) = 0.2969 at 288; sigma: +7.4564e-07 (n = 9), -3.9694e-07 (18), +2.9089e-07 (27), minimum |sigma| = 8.4467e-09 at n = 63, last -1.4300e-08 (n = 297); obstruction radii (absolute) 10^-309 .. 10^-288 against coefficient scale 10^-160; norm-relative radius 10^-128 at 306; apparent radius r > A^(9/4) = 0.069.
delta = 4/9, root b = 0.42237648278718953668667357425680... (tuned49_r4_p1024, N = 306): root tests 1.3631 (36), 1.5470 (72), 1.6884 (108), 1.7129 (144), 1.7214 (180), 1.7369 (216), 1.7508 (252), 1.7490 (288), 1.7578 (300); fit A = 1.7143 (n >= 150); |H_n|^(1/n) = 1.7495 at 288; sigma: -5.4546e-02 (n = 9), -1.4998e+00 (18), +1.6209e+00 (27), minimum |sigma| = 8.6003e-04 at n = 297, last -8.6003e-04 (n = 297); obstruction radii (absolute) 10^-304 .. 10^-121 against coefficient scale 10^75; norm-relative radius 10^-193 at 306; apparent radius r > A^(9/4) = 3.36.
delta = 4/9, root b = 0.26983083939689934318860471083821... (tuned49_r3_p1024, N = 306): root tests 0.7348 (36), 0.7744 (72), 0.8414 (108), 0.8846 (144), 0.9017 (180), 0.8940 (216), 0.9092 (252), 0.9104 (288), 0.9143 (300); fit A = 1.0307 (n >= 150); |H_n|^(1/n) = 0.9169 at 288; sigma: +1.9375e-05 (n = 9), -9.5222e-03 (18), +9.0432e-03 (27), minimum |sigma| = 2.3570e-07 at n = 117, last +2.0621e-05 (n = 297); obstruction radii (absolute) 10^-306 .. 10^-191 against coefficient scale 10^-12; norm-relative radius 10^-177 at 306; apparent radius r > A^(9/4) = 1.07.
delta = 4/9, root b = 0.15242998751865186514116857902085... (tuned49_r2_p1024, N = 306): root tests 0.3249 (36), 0.3721 (72), 0.3786 (108), 0.3857 (144), 0.3860 (180), 0.3896 (216), 0.3909 (252), 0.3929 (288), 0.3939 (300); fit A = 0.4075 (n >= 150); |H_n|^(1/n) = 0.3927 at 288; sigma: +1.9657e-06 (n = 9), +9.6271e-06 (18), +3.5617e-06 (27), minimum |sigma| = 4.3512e-07 at n = 36, last +1.3061e-06 (n = 297); obstruction radii (absolute) 10^-308 .. 10^-304 against coefficient scale 10^-124; norm-relative radius 10^-180 at 306; apparent radius r > A^(9/4) = 0.13.
delta = 4/9 summary (root -> fitted A -> apparent exterior radius r > A^(9/4)): 1.8567 -> 10.7 -> 206; 0.4224 -> 1.71 -> 3.4; 0.2698 -> 1.03 -> 1.07;
0.1524 -> 0.408 -> 0.13; 0.0634 -> 0.304 -> 0.07 (all five roots, 1024 bits, 306 orders each, obstructions certified zero; the theory part's
Corollary T_(9,2) proves convergence for all five; these finite data give the growth constants and are NUMERICAL EVIDENCE for the radii).
delta = 1/3 (c = 3/2, Q = 6, h = 1; the theory part's Corollary T_6, PROVED): f_1 = sin + b sin 3, b one of the six real roots of the degree-12 polynomial P_12 of the theory part's tq_cert_Q6.out (notes/tuned13_poly.json; roots -0.6087, 0.0886, 0.1407, 0.1965, 0.2785, 0.5122); resonances at n = 6k, k >= 2 (first obstruction at 12, free stream constants H_(6k) of sin((2k-2) theta) fixed by the obstruction at 6k+6); code/tuned_general.py --a 1 --b 3, 1024 bits, N = 300, every obstruction a ball containing zero; the theory part's exact minima of |sigma_k| (tq_minima_Q6.out: k_i = 6, 5, 6, inf, inf, 6 with values 17.36, 1.7476e-4, 3.0928e-4, 1.4533e-3 (infimum), 1.8986e-2 (infimum), 0.48351) are compared root by root. Fit A is the three-parameter fit log10 ||f_n||_l1 = n log10 A + beta log10 n + C on n >= 150 used for every tuned run in this section; the straight-line slope of log10 ||f_n|| on the same orders is quoted beside it because the power exponents are large.
delta = 1/3 (c = 3/2, period 6), root b = 0.5121564736203559821898692379837996... (tuned13_r6_p1024, N = 300): root tests 3.7922 (36), 4.3837 (72), 4.7456 (108), 4.8088 (144), 4.7963 (180), 4.8342 (216), 4.8892 (252), 4.8960 (288), 4.8900 (300); fit A = 5.2423 (n >= 150; power exponent -9.0; straight-line slope 5.0328); |H_n|^(1/n) = 4.8873 at 294; sigma: +4.7136e+01 (n = 12), -2.5134e+02 (n = 18), +2.0438e+02 (n = 24), minimum |sigma| = 4.8351e-01 at n = 36, last -6.1715e-01 (n = 294); obstruction radii (absolute) 10^-299 .. 10^-2 against coefficient scale 10^206; norm-relative radius 10^-207 at 300; z = r^(-1/3), apparent radius r > A^(3/1) = 144. (sigma_k for k >= 7: -0.6605 (7), -0.6407 (10), -0.6271 (20), -0.6219 (30), -0.6172 (49): the minimum over k is attained at k = 6 only, as the theory part proved; H_(6k) grows like A^n: 1.0e16 at 36, 5.0e81 at 120, 2.2e199 at 288.)
Direct evaluation (section 13) for the delta = 1/3 root 0.5122 (notes/eval_tuned13_r6.json; resid0 = weighted stationary residual sup_theta |R^(-gamma) residual| of the truncation with the tuned
stream coefficients at N = 10, 20, 40, 80; resid1 = its angular derivative; tail0 = z^N sup|f_(N+1)|):
| R | z = R^(-1/3) | resid0 at N = 10, 20, 40, 80 | resid1 at N = 80 | tail0 at N = 80 |
|---|---|---|---|---|
| 16 | 0.3969 | 1.8e+02, 2.7e+06, 4.1e+15, 2.5e+44 | 2.6e+45 | 2.1e+21 |
| 32 | 0.3150 | 9.8e+00, 3.7e+02, 4.2e+07, 4.9e+28 | 4.8e+29 | 2.0e+13 |
| 64 | 0.2500 | 9.4e-01, 2.0e+00, 1.1e+01, 9.8e+12 | 9.0e+13 | 1.8e+05 |
| 128 | 0.1984 | 9.6e-02, 2.1e-02, 1.0e-03, 5.2e-02 | 1.4e+00 | 1.7e-03 |
| 256 | 0.1575 | 9.8e-03, 2.1e-04, 1.0e-07, 5.4e-10 | 1.4e-08 | 1.6e-11 |
| 512 | 0.1250 | 9.9e-04, 2.1e-06, 1.0e-11, 5.4e-18 | 1.3e-16 | 1.5e-19 |
Geometric decay for R >= 256, marginal at R = 128 (A z = 1.0: 9.6e-2, 2.1e-2, 1.0e-3, 5.2e-2), growth for R <= 64: apparent exterior radius between 128 and 256, consistent with the fitted A^3 = 127 .. 144 (finite-order observation).
delta = 1/3 (c = 3/2, period 6), root b = -0.608726913792658140660299015107817... (tuned13_r1_p1024, N = 300): root tests 5.8576 (36), 6.5786 (72), 7.1229 (108), 7.1814 (144), 7.2196 (180), 7.2959 (216), 7.3316 (252), 7.3616 (288), 7.3539 (300); fit A = 7.6054 (n >= 150; power exponent -0.9; straight-line slope 7.5732); |H_n|^(1/n) = 7.3737 at 294; sigma: +5.1765e+02 (n = 12), -2.7450e+03 (n = 18), +1.9892e+03 (n = 24), minimum |sigma| = 1.7362e+01 at n = 36, last -2.3810e+01 (n = 294); obstruction radii (absolute) 10^-297 .. 10^40 against coefficient scale 10^259; norm-relative radius 10^-219 at 300; z = r^(-1/3), apparent radius r > A^(3/1) = 440. (the theory part's exact minimum for this root: |sigma_6| = 17.36197658, k_i = 6, sign -1: reproduced.)
Direct evaluation (section 13) for the delta = 1/3 root -0.6087 (notes/eval_tuned13_r1.json; same quantities):
| R | z = R^(-1/3) | resid0 at N = 10, 20, 40, 80 | resid1 at N = 80 | tail0 at N = 80 |
|---|---|---|---|---|
| 64 | 0.2500 | 1.5e+02, 1.2e+06, 7.2e+14, 4.7e+40 | 6.5e+41 | 2.6e+19 |
| 128 | 0.1984 | 9.5e+00, 2.2e+02, 7.4e+06, 8.2e+24 | 1.1e+26 | 2.4e+11 |
| 256 | 0.1575 | 9.5e-01, 1.5e+00, 5.1e+00, 2.2e+09 | 2.4e+10 | 2.3e+03 |
| 512 | 0.1250 | 1.0e-01, 1.6e-02, 5.2e-04, 7.5e-04 | 2.1e-02 | 2.1e-05 |
| 1024 | 0.0992 | 1.0e-02, 1.7e-04, 5.3e-08, 7.6e-12 | 2.1e-10 | 2.0e-13 |
| 2048 | 0.0787 | 1.1e-03, 1.7e-06, 5.3e-12, 7.4e-20 | 2.1e-18 | 1.9e-21 |
At R = 1024 and 2048 the residual decreases at every step (certified by the verifier's interval evaluation, independently checked); at R = 512 it decreases to N = 40
and then rises by a factor 1.44 at N = 80 (A z = 0.95), at R <= 256 it grows: apparent exterior radius between 512 and 1024, against the fitted A^3 = 440
(finite-order observation; the independent verifier refuted an earlier 'decay at R >= 512' wording).
delta = 1/3 (c = 3/2, period 6), root b = 0.0885568921011810330656069674715213... (tuned13_r2_p1024, N = 300): root tests 0.4075 (36), 0.4458 (72), 0.4540 (108), 0.4609 (144), 0.4613 (180), 0.4655 (216), 0.4683 (252), 0.4692 (288), 0.4691 (300); fit A = 0.4781 (n >= 150; power exponent +0.4; straight-line slope 0.4790); |H_n|^(1/n) = 0.4676 at 294; sigma: +3.9794e-04 (n = 12), +6.3173e-04 (n = 18), +2.7884e-04 (n = 24), minimum |sigma| = 1.7476e-04 at n = 30, last +3.0776e-04 (n = 294); obstruction radii (absolute) 10^-308 .. 10^-291 against coefficient scale 10^-100; norm-relative radius 10^-193 at 300; z = r^(-1/3), apparent radius r > A^(3/1) = 0.109. (theory part's exact minimum for this root: 1.7476099892e-4 at k = 5: reproduced.)
delta = 1/3 (c = 3/2, period 6), root b = 0.2784978894387364365588337772903038... (tuned13_r5_p1024, N = 300): root tests 1.7938 (36), 1.9542 (72), 2.1090 (108), 2.1555 (144), 2.1729 (180), 2.1708 (216), 2.1921 (252), 2.1963 (288), 2.2003 (300); fit A = 2.4135 (n >= 150; power exponent -16.0; straight-line slope 2.2443); |H_n|^(1/n) = 2.2005 at 294; sigma: +3.5610e-01 (n = 12), -2.7758e+00 (n = 18), +2.9332e+00 (n = 24), minimum |sigma| = 2.0146e-02 at n = 294, last -2.0146e-02 (n = 294); obstruction radii (absolute) 10^-302 .. 10^-104 against coefficient scale 10^101; norm-relative radius 10^-205 at 300; z = r^(-1/3), apparent radius r > A^(3/1) = 14.1. (For this root the theory part proves that inf_k |sigma_k| = |sigma_inf| = 1.8985699e-2 is attained at no finite k; the computed |sigma_k| decrease toward it, 2.0146e-2 at k = 49. The three-parameter fit is unstable here (power exponent -16); the straight-line slope 2.24 and the root test 2.20 at 300 put the growth constant at 2.2 .. 2.4, i.e. r > 11 .. 14.)
delta = 1/3 (c = 3/2, period 6), root b = 0.1407241790948268834091125533136830... (tuned13_r3_p1024, N = 300): root tests 0.6880 (36), 0.7831 (72), 0.8102 (108), 0.8180 (144), 0.8233 (180), 0.8262 (216), 0.8311 (252), 0.8317 (288), 0.8354 (300); fit A = 0.8187 (n >= 150; power exponent +8.5; straight-line slope 0.8511); |H_n|^(1/n) = 0.8353 at 294; sigma: -2.3488e-03 (n = 12), +6.5506e-03 (n = 18), +1.4110e-02 (n = 24), minimum |sigma| = 3.0928e-04 at n = 36, last +8.2676e-04 (n = 294); obstruction radii (absolute) 10^-305 .. 10^-223 against coefficient scale 10^-24; norm-relative radius 10^-199 at 300; z = r^(-1/3), apparent radius r > A^(3/1) = 0.549. (theory part's exact minimum for this root: 3.0928362e-4 at k = 6: reproduced.)
delta = 1/3 (c = 3/2, period 6), root b = 0.1965153635114627782322358601186488... (tuned13_r4_p1024, N = 300): root tests 1.1098 (36), 1.2246 (72), 1.3113 (108), 1.3333 (144), 1.3399 (180), 1.3461 (216), 1.3567 (252), 1.3590 (288), 1.3605 (300); fit A = 1.5279 (n >= 150; power exponent -20.2; straight-line slope 1.3936); |H_n|^(1/n) = 1.3598 at 294; sigma: -5.8972e-03 (n = 12), -1.0273e-01 (n = 18), +2.1146e-01 (n = 24), minimum |sigma| = 1.7533e-03 at n = 294, last -1.7533e-03 (n = 294); obstruction radii (absolute) 10^-304 .. 10^-157 against coefficient scale 10^39; norm-relative radius 10^-196 at 300; z = r^(-1/3), apparent radius r > A^(3/1) = 3.57. (For this root the theory part proves inf_k |sigma_k| = |sigma_inf| = 1.4532895e-3, not attained; the computed |sigma_k| decrease toward it, 1.7533e-3 at k = 49. The three-parameter fit is unstable (power exponent -20): straight-line slope 1.39, root test 1.36 at 300, so A = 1.36 .. 1.53 and r > 2.5 .. 3.6.)
delta = 1/3 summary (root -> growth constant A -> apparent exterior radius r > A^3; A from the three-parameter fit where its power exponent is moderate, otherwise
the range straight-line slope .. fit): -0.6087 -> 7.6 -> 440; 0.5122 -> 5.0..5.2 -> 130..145; 0.2785 -> 2.2..2.4 -> 11..14; 0.1965 -> 1.39..1.53 -> 2.7..3.6;
0.1407 -> 0.82..0.85 -> 0.55..0.61; 0.0886 -> 0.478 -> 0.11 (all six roots, 1024 bits, 300 orders, obstructions certified zero; the theory part's Corollary T_6 proves
convergence for all six with sufficient radii 2^38 .. 2^43 (the independent verifier); these finite data give the growth constants, NUMERICAL EVIDENCE for the radii).

delta = 3/5 (c = 5/2, h = 3, Q = 10, odd numerator; the theory part's Part IX extension, Corollary T_(10,3) in preparation): f_1 = sin + b sin 3, b one of the four real
roots of the degree-10 polynomial P_10 of the theory part's tq_certh_Q10h3.log (notes/tuned35_poly.json; roots 0.0659, 0.1093, 0.3506, 0.5942); resonances at n = 10k,
k >= 1 (first obstruction at 10: density mode sin 3theta; free stream constants H_(10k) of sin((6k-2) theta) fixed by the obstruction at 10k+10); no potential
logarithm for h >= 3 (theory part's Proposition T_(Q,h).3). code/tuned_general.py --a 3 --b 5, 1024 bits, N = 300; z = r^(-3/5), apparent radius A^(5/3).
delta = 3/5 (c = 5/2, period 10), root b = 0.5942044254804745659189704200081632... (tuned35_r4_p1024, N = 300): root tests 0.8396 (50), 1.0140 (100), 1.0365 (150), 1.0429 (200), 1.0558 (250), 1.0655 (300); fit A = 1.2151 (n >= 150; power exponent -23.7; straight-line slope 1.0908); |H_n|^(1/n) = 1.0722 at 290; sigma: -1.5205e-03 (n = 10), +1.5137e-02 (n = 20), -3.5147e-05 (n = 30), minimum |sigma| = 1.2318e-06 at n = 60, last +3.0913e-05 (n = 290); obstruction radii (absolute) 10^-306 .. 10^-183 against coefficient scale 10^7; norm-relative radius 10^-190 at 300; z = r^(-3/5), apparent radius r > A^(5/3) = 1.38. (sigma_k, k = n/10: -1.52e-3, +1.51e-2, -3.51e-5, -1.90e-5, -8.36e-6, -1.23e-6 (k = 6, the minimum), then rising to +3.09e-5 at k = 29; the three-parameter fit
is unstable (power exponent -24): straight-line slope 1.09, root test 1.07 at 300, so A = 1.07 .. 1.22 and r > 1.1 .. 1.4. The theory part's exact minima for this family
were not yet available for comparison.)
delta = 3/5 (c = 5/2, period 10), root b = 0.0659472179394786691837643182492378... (tuned35_r1_p1024, N = 300): root tests 0.1691 (50), 0.1858 (100), 0.1912 (150), 0.1918 (200), 0.1932 (250), 0.1947 (300); fit A = 0.2419 (n >= 150; power exponent -46.2; straight-line slope 0.1960); |H_n|^(1/n) = 0.1940 at 290; sigma: +1.4270e-08 (n = 10), -3.4262e-09 (n = 20), +4.8181e-10 (n = 30), minimum |sigma| = 1.6029e-12 at n = 150, last -3.8895e-11 (n = 290); obstruction radii (absolute) 10^-328 .. 10^-310 against coefficient scale 10^-214; norm-relative radius 10^-114 at 300; z = r^(-3/5), apparent radius r > A^(5/3) = 0.0939. (The three-parameter fit is meaningless here (power exponent -46); straight-line slope 0.196, root test 0.195 at 300: A = 0.195 .. 0.20, r > 0.065 .. 0.07. The
responses are tiny for this root (|sigma_k| down to 1.6e-12 at k = 15), so the norm-relative radius at 300, 10^-114, is larger than for the other roots but still certified.)
delta = 3/5 (c = 5/2, period 10), root b = 0.3505637599344622834745700575826032... (tuned35_r3_p1024, N = 300): root tests 0.3863 (50), 0.4203 (100), 0.4417 (150), 0.4483 (200), 0.4527 (250), 0.4537 (300); fit A = 0.4333 (n >= 150; power exponent +15.8; straight-line slope 0.4655); |H_n|^(1/n) = 0.4541 at 290; sigma: +5.7878e-07 (n = 10), +1.4024e-05 (n = 20), -1.8846e-07 (n = 30), minimum |sigma| = 2.1970e-09 at n = 110, last +5.6191e-08 (n = 290); obstruction radii (absolute) 10^-309 .. 10^-272 against coefficient scale 10^-104; norm-relative radius 10^-167 at 300; z = r^(-3/5), apparent radius r > A^(5/3) = 0.248. (The three-parameter fit has power exponent +16; straight-line slope 0.466, root test 0.454 at 300: A = 0.43 .. 0.47, r > 0.25 .. 0.28.)
delta = 3/5 (c = 5/2, period 10), root b = 0.1093408009627109099338174506940033... (tuned35_r2_p1024, N = 300): root tests 0.1539 (50), 0.1647 (100), 0.1699 (150), 0.1726 (200), 0.1741 (250), 0.1752 (300); fit A = 0.1833 (n >= 150; power exponent -4.6; straight-line slope 0.1795); |H_n|^(1/n) = 0.1744 at 290; sigma: +2.2607e-09 (n = 10), -1.2466e-09 (n = 20), +1.3909e-11 (n = 30), minimum |sigma| = 1.7804e-12 at n = 40, last -5.0382e-12 (n = 290); obstruction radii (absolute) 10^-335 .. 10^-310 against coefficient scale 10^-228; norm-relative radius 10^-107 at 300; z = r^(-3/5), apparent radius r > A^(5/3) = 0.0592. (straight-line slope 0.180, root test 0.175 at 300: A = 0.175 .. 0.183, r > 0.055 .. 0.06.)
delta = 3/5 summary (root -> growth constant A -> apparent exterior radius r > A^(5/3)): 0.5942 -> 1.07 .. 1.22 -> 1.1 .. 1.4; 0.3506 -> 0.43 .. 0.47 -> 0.25 .. 0.28;
0.1093 -> 0.18 -> 0.06; 0.0659 -> 0.195 .. 0.20 -> 0.065 .. 0.07 (all four roots, 1024 bits, 300 orders, obstructions certified zero; the responses |sigma_k| of the
three small roots are tiny, down to 1.6e-12 .. 2.2e-9; the independent verifier prove convergence for all four roots with the explicit radius 2^(65/3) |eps|^(5/3) for
the root 0.5942; these finite data are NUMERICAL EVIDENCE for the growth constants).

### 5.13c Single-harmonic tuned series (theory part's Corollary T_(Q,h).9 centers; theory part's request 18:03Z; code/tuned_general.py --f1-single M, added 19:30Z)
Leading profile f_1 = sin(M theta) alone (unit amplitude), tuned pure series (free stream constants H_n at the resonant orders n = Q k fixed by the affine
response so that the next obstruction vanishes; the same program and tuning rule as in 5.13b, the period and the mode bookkeeping unchanged; the h = 2
structure, first resonance at n = Q with free mode sin 2theta and obstruction mode sin((4k+1) theta) at order Q(k+1), is automatic in the code). 1024 bits,
N = 300, every tuned obstruction a ball containing zero. Smoke tests at 256 bits (logs/smoke_sin7_45.jsonl, smoke_sin11_49.jsonl) reproduce the theory part's exact
responses to every printed digit: sin7 at 4/5 sigma_1..5 = 1.9470147e-5, 4.9232519e-4, -2.6232570e-3, 7.4295139e-4, 3.8905918e-4; sin11 at 4/9 sigma_1..3 =
0.17639587, 8.7814679, 0.12418638. All growth constants and radii below are NUMERICAL EVIDENCE for the size of the convergence radius; convergence itself
is the theory part's and verifier's theorem for each center, with the certified sufficient radii quoted from the theory part's table.
(a) sin(7 theta) at delta = 4/5 (c = 5, Q = 5, z = r^(-4/5); run single_sin7_45_p1024, finished 19:47Z, 15 minutes on one core; proved exterior radius
bracket (0.0902973, 2^20) times |eps|^(5/4)). Root tests ||f_n||_l1^(1/n): 0.4066 (36), 0.4773 (50), 0.5134 (100), 0.5381 (150), 0.5442 (200), 0.5444 (250),
0.5526 (300); |H_n|^(1/n) = 0.5535 at 295. The per-order growth is irregular: 10-order slopes of log10 ||f_n||_l1 between -0.169 and -0.336 per order on
100..300 (mean -0.2415 per order over 100..300, i.e. endpoint base A = 0.5734), so the three-parameter fit is unstable (A = 0.563, 0.589, 0.653 on the windows
100..300, 150..300, 200..300 with power exponents +2.3, -7.2, -34; not used) and the straight-line slope is the robust statistic: A = 0.5703 (100..300), 0.5703
(150..300), 0.5692 (200..300). Apparent exterior radius A^(5/4) = 0.494 .. 0.496 from the line fits and 0.499 from the endpoint base, times |eps|^(5/4) (theory part's float
value 0.49; an earlier version of this paragraph gave '0.50 .. 0.52', which mixed the endpoint base rounded up with the unstable three-parameter fit: corrected per the
the independent verifier). Responses: sigma_k > 0 for k = 1, 2, 4, 5, negative from k = 3 and from k = 6 on, decreasing slowly in modulus, -2.96e-5 (k = 6),
-1.22e-5 (20), -8.80e-6 (40), -7.67e-6 (59, the minimum through 300); H_n tracks ||f_n|| (log10 |H_295| = -75.8 against log10 ||f_300|| = -77.3). Obstruction
radii 10^-312 .. 10^-252 against a coefficient scale 10^-78; norm-relative radius 10^-174 at 300. Direct evaluation (code/evaluate_series.py on the final
checkpoint, notes/eval_single_sin7_45.json; weighted stationary residual of the truncation with the tuned stream, resid0, its angular derivative resid1, and
the weighted tail term tail0 = z^N max |f_(N+1)|; all three are maxima over a theta grid of at least 8 x (2K + 1) points evaluated in float64 on the arb midpoints,
indicative rather than certified, as for every section-13 table in this report; the verifier's derive certified enclosures separately):
| R | z = R^(-4/5) | resid0 at N = 10, 20, 40, 80 | resid1 at N = 80 | tail0 at N = 80 |
|---|---|---|---|---|
| 0.125 | 5.278 | 2.1e5, 2.9e11, 8.1e29, 6.1e72 | 3.9e74 | (grows) |
| 0.25 | 3.031 | 16, 1.4e2, 1.1e11, 6.7e34 | 2.7e36 | (grows) |
| 0.5 | 1.741 | 6.7e-2, 1.5e-3, 4.5e-3, 2.9e-1 | 17 | 7.8e-4 |
| 1 | 1 | 2.5e-4, 2.1e-8, 9.4e-13, 1.4e-20 | 8.9e-19 | 4.2e-23 |
| 2 | 0.574 | 9.7e-7, 3.1e-13, 2.2e-22, 7.6e-40 | 4.7e-38 | 2.3e-42 |
| 4 | 0.330 | 3.7e-9, 4.7e-18, 5.1e-32, 4.0e-59 | 2.5e-57 | 8.1e-60 |
The residual decays geometrically at R >= 1, is marginal at R = 0.5 (z A = 1.74 x 0.573 = 0.998) and grows at R <= 0.25: apparent radius about 0.5 for unit
amplitude, consistent with the growth fit and six to seven decades inside the certified bracket.
Extension to N = 500 (run single_sin7_45_p1024_N500, a fresh run of the same program, finished 22:01Z, 81 minutes; it reproduces the N = 300 run exactly at the common
orders; norm-relative radius 10^-76 at 500; all 99 tuned obstructions balls containing zero, radii 10^-312 .. 10^-202 against a coefficient scale 10^-127): the regular
law persists through 500. Root tests 0.5526 (300), 0.5559 (350), 0.5543 (400), 0.5573 (450), 0.5610 (500), rising toward the growth constant; |H_495|^(1/495) = 0.5616;
10-order slopes between -0.12 and -0.31 per order on 300..500 (irregular as before, mean -0.2412 per order on 300..500 against -0.2415 on 100..300); least-squares line
fits A = 0.5710 (100..500), 0.5713 (150..500), 0.5714 (200..500), 0.5723 (300..500), 0.5738 (400..500); endpoint bases 0.5734 (100..300), 0.5739 (300..500), 0.5736
(100..500); radius diagnostics A^(5/4) = 0.4964 .. 0.4994 (line fits) and 0.4990 .. 0.4995 (endpoint bases), times |eps|^(5/4): the diagnostics of the orders 300..500 lie
within 0.004 of those of 100..300. Responses keep decreasing slowly in modulus: sigma_60 = -7.633e-6, sigma_80 = -7.039e-6, sigma_99 = -6.694e-6 (the smallest through
500); H_n tracks ||f_n|| throughout. Finite statistics; they fix no asymptotic law.
(b) sin(9 theta) at delta = 4/7 (c = 7/3, Q = 7, z = r^(-4/7); run single_sin9_47_p1024, finished 20:07Z, 19 minutes; proved exterior radius bracket (0.2365977, 2^(147/4))
times |eps|^(7/4)). Every tuned obstruction at n = 7k, k = 1..43, is a ball containing zero (radii 10^-311 .. 10^-106 against a coefficient scale 10^86); norm-relative
radius 10^-190 at 301. Root tests ||f_n||_l1^(1/n): 1.1169 (36), 1.1473 (50), 1.6527 (100), 1.9247 (150), 1.9029 (200), 1.9006 (250), 1.9506 (300); |H_294|^(1/294) =
1.962. The growth has not settled by N = 300: the 10-order slope of log10 ||f_n||_l1 is +0.09 per order through n = 70 and +0.15 .. +0.77 per order from
n = 77 on (code/single_slopes.py single_sin9_47_p1024 60 100), where the responses sigma_k have become small and decrease like roughly 1.1e-3/k (sigma_10 = 1.79e-4,
sigma_20 = 5.58e-5, sigma_42 = 2.43e-5, the smallest through 301); the tuned constants H_(7k) = -R_k/sigma_k are observed to grow faster per period in this range,
but the tuning identity alone does not determine the growth because the obstruction numerator R_k varies as well (the independent verifier): the finite growth transition
is an observed association with small responses, not a consequence of the identity. The verifier's exact limit of the response sequence is S(0) = 1.9908e-7 (independently checked), and
sigma_42 / S(0) = 122, i.e. the current responses are two decades above their positive limit. The finite
constants depend on the window and on the statistic: least-squares line fits A = 2.031 (100..301), 1.982 (150..301), 2.119 (200..301), endpoint base 2.113 (100..301,
mean slope +0.325 per order); apparent radius diagnostics A^(7/4) = 3.46, 3.31, 3.72 (line fits) and 3.70 (endpoint), times |eps|^(7/4), varying non-monotonically
with the window start; the three-parameter fits vary sharply with the window (bases 1.78, 3.17, 4.79 with power exponents +25, -103, -202) and are not used. These are
finite statistics: they neither bound the true radius from above nor establish that the diagnostic decreases with N or that the slope follows an acceleration law
(the independent verifier; an earlier version of this paragraph said 'upper estimate that will decrease with N' and 'three decades', both withdrawn). The sign pattern of sigma_k
is irregular through k = 9 (-9.60e-3, +7.03e-2, -4.10e-1, -6.81e-1, -8.30e-2, +1.13, +5.03e-4, -5.88e-1, +2.32e-4) and positive from k = 10 on. Direct evaluation
(notes/eval_single_sin9_47.json; float64 grid maxima on the midpoints, indicative):
| R | z = R^(-4/7) | resid0 at N = 10, 20, 40, 80 | resid1 at N = 80 | tail0 at N = 80 |
|---|---|---|---|---|
| 0.5 | 1.486 | 1.5e3, 1.3e8, 4.5e18, 4.1e48 | 1.7e50 | (grows) |
| 1 | 1 | 6.7, 64, 9.2e4, 4.8e21 | 2.0e23 | 1.9e11 |
| 2 | 0.673 | 0.11, 1.9e-2, 6.5e-4, 6.5e-3 | 0.34 | 3.4e-3 |
| 4 | 0.453 | 2.3e-3, 7.3e-6, 9.2e-11, 1.2e-16 | 5.9e-15 | 5.8e-17 |
| 8 | 0.305 | 4.5e-5, 2.8e-9, 1.3e-17, 2.1e-30 | 9.7e-29 | 1.0e-30 |
Decay at R >= 4 (strict at each step, the independent verifier), a decrease from N = 20 to 40 and an increase from 40 to 80 at R = 2 (the verifier's continuum enclosure of
the N = 80 value at R = 2 is 6.546e-3 .. 6.560e-3, agreeing with the grid value), growth at R <= 1: at these truncation orders the residual behaves as if the radius
were between 2 and 4, consistent with the growth diagnostics of the same orders. The finite reversal at R = 2 does not decide eventual convergence there. All values
are inside the proved bracket by at least a decade on each side.
(c) sin(11 theta) at delta = 4/9 (c = 9/5, Q = 9, z = r^(-4/9); run single_sin11_49_p1024, finished 20:37Z, 27 minutes; proved exterior radius bracket (0.507476, 2^(213/4))
times |eps|^(9/4)). Every tuned obstruction at n = 9k, k = 1..34, is a ball containing zero (radii 10^-311 .. 10^-58 against a coefficient scale 10^161); norm-relative
radius 10^-215 at 306. sigma_1..3 equal the theory part's exact values (0.17640, 8.7815, 0.12419); sigma_4..10 = -15.32, -26.14, +7.823, -55.89, +14.09, +30.20, -138.3, then
small: sigma_11 = -2.4575e-3, sigma_12 = +26.80, sigma_13 = +9.499, and from k = 14 on negative and decreasing in modulus, -1.0245e-3 (14), -4.245e-4 (20), -2.489e-4
(27), -1.8458e-4 (33, the smallest through 306; the theory part's lower bound is 2^-29). Root tests ||f_n||_l1^(1/n): 1.9102 (36), 1.9651 (50), 2.0527 (100), 2.2206 (150),
3.0407 (200), 3.2721 (250), 3.4201 (300); |H_297|^(1/297) = 3.425. The 10-order slope of log10 ||f_n||_l1 is +0.328 .. +0.335 per order through n = 130 (regular) and
+0.43 .. +1.30 per order from 140 on, where the responses have become small (code/single_slopes.py single_sin11_49_p1024 60 100; the theory part's float runs located the
break near 130). Finite growth statistics: least-squares line fits A = 4.965 (100..306), 4.984 (150..306), 4.202 (200..306), endpoint base 4.321 (100..306; mean slope
+0.636 per order); radius diagnostics A^(9/4) = 36.8, 37.1, 25.3 (line fits) and 26.9 (endpoint), times |eps|^(9/4); the three-parameter fit (base 1.19, exponent +319)
is not used. On the early window n <= 130 the slope +0.33 gives A = 2.15 and A^(9/4) = 5.6. Direct evaluation (notes/eval_single_sin11_49.json; float64 grid maxima on the
midpoints, indicative):
| R | z = R^(-4/9) | resid0 at N = 10, 20, 40, 80 | resid1 at N = 80 | tail0 at N = 80 |
|---|---|---|---|---|
| 2 | 0.735 | 79, 1.1e5, 4.9e12, 4.7e28 | 2.4e30 | (grows) |
| 4 | 0.540 | 2.3, 8.5, 2.3e2, 1.9e7 | 9.6e8 | 1.1e6 |
| 8 | 0.397 | 9.8e-2, 1.7e-2, 6.4e-4, 1.7e-6 | 9.3e-4 | 2.2e-5 |
| 16 | 0.292 | 4.3e-3, 3.4e-5, 3.2e-9, 3.8e-17 | 2.1e-14 | 4.3e-16 |
| 32 | 0.214 | 1.9e-4, 7.6e-8, 1.5e-14, 8.2e-28 | 4.4e-25 | 8.4e-27 |
| 128 | 0.116 | 4.2e-7, 3.7e-13, 3.3e-25, 3.5e-49 | 1.9e-46 | 3.3e-48 |
Decay at R >= 8, growth at R <= 4 through N = 80: at these truncation orders (which lie in the regular early window) the residual behaves as if the radius were between
4 and 8, consistent with the early-window constant 5.6; the later-window diagnostics (25 .. 37) are finite statistics of orders 140..306 and neither bound the true
radius nor fix a trend. All values lie inside the proved bracket.
Summary of the three single-harmonic centers (NUMERICAL EVIDENCE, finite): sin7 at 4/5 has a regular geometric law with radius diagnostic 0.494 .. 0.499 x |eps|^(5/4);
sin9 at 4/7 and sin11 at 4/9 have a regular early window (slopes +0.09 and +0.33 per order to n = 70 and 130) followed by faster, irregular growth; the finite growth
transitions occur in the ranges where the computed responses sigma_k are small (those of sin9 tend to the exact limit 1.99e-7, those of sin11 are at 1.8e-4 and
decreasing at k = 33), an observed association: the tuning identity H = -R/sigma alone does not determine the eventual growth because the obstruction numerator R also
varies (independently checked). Radius diagnostics 3.3 .. 3.7 x |eps|^(7/4) and 25 .. 37 x |eps|^(9/4) on the late windows; the tuned constants H_n track ||f_n|| in all three cases.


### 5.5b Direct evaluation (section 13) for the Candidate 007 profile at its own c_l and amplitude (ckpt c007_arb512, notes/eval_c007_arb512.json)
sup over theta of R^{-gamma} |(c_l X + u_N).grad rho_N - rho_N| (float64 sums of the arb E_n coefficients; tail = z^N sup|f_{N+1}|):
| N | R = 16 (z = 0.289) | R = 32 (z = 0.212) | R = 64 | R = 128 | tail at R = 32 | d/dtheta residual at R = 32 |
|---|---|---|---|---|---|---|
| 10 | 2.26e+00 | 1.07e-01 | 4.97e-03 | 2.29e-04 | 1.61e-02 | 8.92e-01 |
| 25 | 1.47e+00 | 6.45e-04 | 3.09e-07 | 1.45e-10 | 5.48e-05 | 1.31e-02 |
| 50 | 4.32e+00 | 1.02e-06 | 2.01e-13 | 3.91e-20 | 3.49e-08 | 2.99e-05 |
| 100 | 9.16e+00 | 3.15e-13 | 1.23e-26 | 4.65e-40 | 7.44e-15 | 1.11e-11 |
| 150 | 6.08e+01 | 3.72e-19 | 2.70e-39 | 1.88e-59 | 6.14e-21 | 1.64e-17 |
| 200 | 1.58e+02 | 1.60e-25 | 2.11e-52 | 2.68e-79 | 1.95e-27 | 6.64e-24 |
At R = 32, 64, 128 the residual decreases geometrically (per-order rate 0.75 at R = 32, equal to L z with L = 3.5), at R = 16
it grows slowly (L z = 1.01): through these orders the apparent exterior radius of the truncations (raw amplitude) lies between
16 and 32, consistent with the fitted R_* = L^{1/delta} = 3.5^{2.234} = 16.4. Finer radius scan (notes/eval_c007_fineR.json,
N = 50 against N = 100): the residual increases from N = 50 to N = 100 at R = 14 (165 -> 8.4e4) and R = 16 (4.3 -> 9.2) and
decreases at R = 18 (0.35 -> 0.039), 20 (3.4e-2 -> 3.6e-4), 22 (4.2e-3 -> 5.3e-6), 24, 26, 28 (2.0e-5 -> 1.2e-10): the apparent
exterior radius at these orders is between 16 and 18. Finite-order
behaviour only: the infinite series at the stored rational c_l is OPEN (exact resonance at n = 8152952920478362). Partial sums at R = 32: R^{-gamma} rho_N(32, 0.9) =
13.57845234 stable to 8 digits from N = 50. The angular-derivative residual decays at the same rate.

### 5.5c Direct evaluation for f_1 = sin(theta), delta = 1/sqrt5 (the certified parameter of Theorem D), unit amplitude (ckpt sqrt5_sin1_p1024, N <= 700)
sup over theta of R^{-gamma} |(c_l X + u_N).grad rho_N - rho_N| (float64 sums of the arb E_n coefficients):
| N | R = 0.25 (z = 1.86) | R = 0.5 (z = 1.36) | R = 1 | R = 2 | R = 4 | d/dtheta residual at R = 1 |
|---|---|---|---|---|---|---|
| 10 | 1.07e-02 | 5.09e-04 | 2.39e-05 | 1.11e-06 | 5.09e-08 | 3.47e-04 |
| 20 | 1.53e-03 | 3.29e-06 | 6.95e-09 | 1.45e-11 | 3.01e-14 | 2.10e-07 |
| 40 | 5.64e-05 | 2.46e-10 | 1.06e-15 | 4.48e-21 | 1.88e-26 | 6.23e-14 |
| 80 | 1.27e-07 | 2.29e-18 | 4.05e-29 | 7.07e-40 | 1.22e-50 | 4.79e-27 |
| 160 | 1.11e-12 | 3.39e-34 | 1.02e-55 | 3.02e-77 | 8.90e-99 | 2.42e-53 |
| 320 | 1.45e-22 | 1.28e-65 | 1.11e-108 | 9.47e-152 | 8.03e-195 | 5.24e-106 |
The verifier's rigorous full-circle enclosures (independently checked, 1024-bit Cartesian coefficients, 2048 interval samples) contain these
values: N = 80: R = 0.25 in [1.263e-7, 1.561e-7], R = 1 in [3.999e-29, 4.944e-29], R = 4 in [1.206e-50, 1.491e-50]; N = 160:
[1.100e-12, 1.621e-12], [1.011e-55, 1.490e-55], [8.817e-99, 1.301e-98]. Through N = 320 the residual decreases geometrically at every tested radius, including R = 0.25 where z = 1.86 is inside the
fitted radius 1/L = 2.14 (per-order rate at R = 0.25: 10^{-(22.0-12.0)/160} = 0.87 = L z); the rigorous Theorem D radius for this
case is 2^36. Finite-order observation; convergence for r > 2^36 is PROVED (theory part, independently verified), the interval 0.18 < r < 2^36 is
covered only by this evidence.

## 6. Evidence summary (current, 2026-10-31T19:54Z; every item is a finite-order observation unless marked PROVED)
- Pure series, f_1 = sin(theta), non-resonant delta (1/sqrt5, Candidate 007's rational, 0.401, 0.446, 0.4476): geometric growth with the
  smooth correction L(1 - 2/n) through N = 625 (sqrt5) and 458 (0.446); apparent radius 1/L = 2.1 in z = r^(-delta) for unit amplitude
  (NUMERICAL EVIDENCE). Convergence itself is PROVED by the theory part and verifier for Brjuno delta (Theorem A; rigorous radius 2^36 at 1/sqrt5)
  and below the first resonance for rational delta (Theorem E); the measured constants are far inside the proved bounds (5.8).
- Candidate 007's own profile at its own c_l: the 2048-bit run finished at N = 500 (rigorous through 500, relative radius 10^-301): root tests
  3.5113 (l1), 3.4990 (l2), 3.4953 (max coefficient), still rising slowly (+0.013 in l1 from 400 to 500; the independent verifier confirms every stored
  coefficient at 500); apparent radius about 1/3.5 in z (r > 16 for its amplitude); the truncation residual decreases at R >= 32 and increases at R = 16
  through N = 200 (5.5b). The infinite continuation at the stored rational (first exact resonance at n = 8.15e15) is OPEN; its sin theta coefficient
  makes it divergent on a dense set of nearby irrational delta and convergent almost everywhere (theory part's theorems; not numerics).
- Shape: among the tested finite grids, small positive sin 3theta and sin 5theta admixtures with Candidate 007's own ratios have the
  smallest growth constant per unit leading amplitude (L = 0.17 for sin + 0.11 sin3 + 0.03 sin5 against 0.468 for sin theta); the shear
  family of the independent verifier continues this trend (root tests 0.300 .. 0.1555 for K = 1 .. 9) (5.6, 5.6b, 5.6c).
- Exact resonances at rational delta obstruct the pure ansatz for f_1 = sin theta (PROVED finite facts for every tested rational, 5.3, 5.9: 55
  rationals in (0.40, 0.50), 122 prime cases of the verifier's congruence, 502 ball-arithmetic cases with 67 <= p <= 157, and the 37 odd-numerator
  pairs a/p with p <= 23, all with nonzero compatibility coefficient; |kappa| about 10^(-0.5 p) on average and >= 10^(-0.88 p) in the ball cases).
- Tuned pure series at rational delta (the theory part's Theorems T, T_Q, T_(Q,h); 5.13, 5.13b, 5.13c): for c = 3 (two roots), Q = 4 (six), Q = 5 (six), delta = 4/9
  (five), delta = 1/3 (six) and delta = 3/5 (four), 29 two-mode profiles f_1 = sin + b sin3 in all, the ball-arithmetic series to 300..400 orders has every
  obstruction certified zero, geometric growth with constants A between 0.18 and 10.7, the theory part's exact |sigma_k| minima reproduced in every case, and
  section-13 residuals that decay inside and grow outside a radius bracketing A^(1/delta) (NUMERICAL EVIDENCE for the radii; convergence is PROVED by the
  theorems with sufficient radii 2^16 .. 2^60, far outside the apparent ones). The verifier's independent 2048/3072-bit prefixes (orders 27..90)
  agree coefficientwise with these runs for every root checked. Single-harmonic centers (5.13c): sin7 at delta = 4/5 to 500 orders, regular law with radius diagnostics
  0.494 .. 0.4995 x |eps|^(5/4) (line fits and endpoint bases on every window of 100..500) inside the proved bracket (0.0902973, 2^20); sin9 at 4/7 to 301 orders, per-order growth not settled by 300
  (slope +0.09 per order to n = 70, then +0.15 .. +0.77; responses two decades above their exact limit 2e-7), finite radius diagnostics 3.3 .. 3.7 x |eps|^(7/4)
  depending on window and statistic; sin11 at 4/9 to 306 orders, regular slope +0.33 per order to n = 130 then +0.43 .. +1.30, finite radius diagnostics
  25 .. 37 x |eps|^(9/4) on 100..306 (5.6 on the early window), residuals decaying at R >= 8 and growing at R <= 4 through N = 80 (proved bracket (0.507476, 2^(213/4))). One Q9 (delta = 2/9) root of the theory part's
  P_18 checked to order 99 in 512-bit balls (obstructions zero, sigma_2..10 in notes/q9_r10_check_p512.txt).
- Canonical logarithmic series at rational delta (5.11, 5.11b): the plain norms decrease geometrically in every case computed, at a rate that depends on delta
  (mean per-order increment of log10 M_n over the last 30 orders of each run, with the root test M_N^(1/N); notes/logrun_rates_by_run.json): 4/9: -0.328 per order on
  271..300, root 0.4576 (N 300); 2/5: -0.254 on 211..240, root 0.5387 (N 240); 9/20: -0.338 on 211..240, root 0.4450 (N 240); 1/2: -0.419 on 271..300, root 0.3716
  (N 300; no hump; interior columns rising but 26 .. 35 decades below c_0); 2/3: -0.691 on 300..329 (the certified part), root 0.1952 at 329. The consecutive ratios of
  each run are fitted by L(1 - a/n) with a near 2 (finite fits; independently checked for 1/2). At delta = 2/3 only: an interior hump of the
  factorial-weighted log columns from n = 235 on (+7.7 at k = 68 for n = 329, far from the resonant diagonal), a stream sum N_n concentrating at the
  Poisson-shift-2/3 modes at the orders n = 2 mod 3 and exceeding the density sum M_n there from 332 on, and, at 330, a regime change of the plain sums:
  the 3-order decrement drops from -2.10 to -1.63 decades per period and then weakens slowly, -1.63 (333) .. -1.61 (399) .. -1.60 (408), density and stream
  alike, the two non-resonant increments frozen at -0.700 and -0.734 and the resonant class-0 increment weakening from -0.197 to -0.168 (a period-3 cycle
  decaying by 10^-0.53 per order with a drift of +0.0016 per period in log10 of its signed multiplier; the drift is fitted through 438 by a power
  n^0.502 (Gevrey-type), by a 1/n approach to a limit multiplier 0.041 (geometric) and by exponential growth in n (slope 0.000551 per order), the
  last with the smallest residual on the longer windows (the power model marginally better on the final seven-point window 420..438) and the first two with
  parameters rising as the window start moves later; no model is excluded). Orders >= 330 are conditional on the loaded 329 midpoints
  (the propagated effect of their certified 2.5e-6 uncertainty is not bounded; the boundary-perturbed continuation 330..350 showed a temporary
  amplification below a factor 2 at 330..331 in the relative l1 metric and attenuation to 5e-11 in the log sums by 350: one sample, a diagnostic, not a
  bound). Whether the cycle persists beyond 440, and which tail model holds, is OPEN; the continuation ended at 440 (22:59Z), 36 periods after the regime change.
- Linearized (edge-only) variants of the 2/3 recursion (5.12): the pairs with min(i, j) <= K reproduce 0.84 (K = 1), 0.96 (K = 3) and 0.994
  (K = 10) of the full geometric rate but none of the hump through n = 300; K = 30 departs upward from the full run from about 265 (certified by
  a 512-bit ball run to 300); the one-step linearization error at order 350 is 0.70 (K = 1) .. 2.1e-6 (K = 100), so the departure is an accumulated
  feedback effect (5.11b (b6)). Float64 fails for the full recursion beyond about 270 (shared error of two rounding-perturbed twins).
- Direct evaluation (section 13 of the prompt; 5.5, 5.5b, 5.5c, 5.13, 5.13b, 5.13c): truncation residuals (function and derivative) decay geometrically
  with N at every radius inside the apparent convergence region and grow outside it, with no precision failure through N = 320 in ball
  arithmetic; the verifier's certified residual enclosures (independently checked) agree with the midpoint values to one percent or better.
- Open numerically: the tail model of the period-3 cycle at 2/3 (three models unseparated through 438, the end of the run); the hump question at delta = 1/2 beyond 300 (through
  300 the factorial maximum stays at k = 1, -1.80, the root test M_n^(1/n) is 0.3716 at 300 while the consecutive ratios M_n/M_(n-1) follow L(1 - 1.84/n) with
  L = 0.3839 on 200..300 (two different statistics: the root test lags the ratio), and the interior columns k = 50..60 rise relative to c_0 but are still 28 .. 35
  decades below it); the limit of the 007 root test (3.51 at 500 and rising).

## 7. Reproducibility map (which files support which table)
| section | runs (logs/<tag>.jsonl, ckpt/<tag>.pkl) |
|---|---|
| 3 validation | extract007.py output; check_chi_sympy.py (logs/check_chi_sympy.out); c007_exact (fmpq, N 22) vs c007_arb512 vs c007_arb256; c007_p2048 |
| 4 | notes/cand007_f1.json |
| 5.1 | sin1_c007_arb512, sqrt5_sin1_p1024 (.regen), sin1_cl361_200_p1024, sin1_cl363_200_p1024, sin1_cl91_50_p1024, nearres_eps1e-3_p512 |
| 5.2 | c007_exact, c007_arb512, c007_arb256, c007_p2048 |
| 5.3 | res_*_exact, sin1_cl2_exact (notes/resonance_report.json); resonance_scan_* (notes/resonance_scan_*.json) |
| 5.4 | nearres_eps1e-3/1e-6/1e-9_p512 |
| 5.5, 5.5b | notes/eval_sin1_c007_test.json, notes/eval_c007_arb512.json, notes/eval_c007_fineR.json, notes/eval_sqrt5_sin1_p1024.json |
| 5.6, 5.6b | shape_*, shape2_*, shape3_*, shape4_*, pert007_* |
| 5.8 | logs/sqrt5_sin1_p1024.regen.jsonl, logs/sqrt5_c007f1_p1024.jsonl (theoremA_compare.py) |
| 5.9 | notes/resonance_scan_sin1.json, notes/resonance_scan_cand007.json, notes/prime_congruence_*.json, notes/kappa_scan_arb.jsonl, notes/kappa_odd_check_sin1.out (code/kappa_odd_check.py) |
| 5.10 | dsw2_*, dsw3_*, dsw4_* |
| 5.11 | log_sin1_c9_5_p512, log_sin1_c3_p512, log_sin1_c2_p512, log_c007f1_c9_5_p512, log_sin1_c5_3_p512, log_sin1_c20_11_p512 (notes/log_*_table.json) |
| 5.13 | tuned_b1_p1024, tuned_b2_p1024 (code/tuned_c3.py; notes/eval_tuned_b1_p1024.json, notes/eval_tuned_b1_p1024_N320.json; ckpt/tuned_*_H.json) |
| 5.13b | tunedQ4_r1..r6_p1024 (code/tuned_cQ.py --Q 4), tunedQ5_r1..r6_p1024 (--Q 5), tuned49_r1..r5_p1024 (code/tuned_general.py --a 4 --b 9, notes/tuned49_poly.json), tuned13_r1..r6_p1024 (--a 1 --b 3, notes/tuned13_poly.json), tuned35_r1..r4_p1024 (--a 3 --b 5, notes/tuned35_poly.json); summaries by code/tuned_summary.py TAG; notes/eval_tunedQ4_r6.json, eval_tunedQ5_r6.json, eval_tuned49_r5.json, eval_tuned13_r6.json, eval_tuned13_r1.json |
| 5.11b | log_sin1_c3_from329 (continuation of log_sin1_c3_p512 from the archived 329 checkpoint with --reset-radii; ckpt/log_sin1_c3_N350.pkl is the 350 state); log_sin1_c3_pert329 (boundary-perturbed continuation, seed 20261031; code/compare_pert.py -> notes/compare_pert.txt); merged per-order table by code/merge_logs.py + code/slopes_q.py; code/table_511b.py -> notes/table_511b_*.md; notes/period3_decrements_300_353.txt; code/cycle_diag.py -> notes/cycle_diag_*.txt, notes/drift_fit_345_370.txt; code/onestep_edge_error.py -> notes/onestep_edge_error_350.txt; notes/tprofile_350.txt, notes/bands_350.txt, notes/stream_ratio_modes_341_350.json, notes/stream_shares_341_350.txt |
| 5.13c | single_sin7_45_p1024, single_sin9_47_p1024, single_sin11_49_p1024 (code/tuned_general.py --f1-single 7/9/11 --a 4 --b 5/7/9 --prec 1024 --N 300; ckpt/<tag>_H.json; smoke_sin7_45, smoke_sin11_49 at 256 bits; code/tuned_summary.py, code/single_slopes.py; notes/eval_single_sin7_45.json, notes/eval_single_sin9_47.json, notes/eval_single_sin11_49.json); Q9 root check q9_r10_check_p512 (--a 2 --b 9 --poly-coeffs @notes/tunedQ9_poly.json --root-guess 0.421494658566 --prec 512 --N 99; notes/q9_r10_check_p512.txt) |
| 5.12 | log23_edge1_float, log23_edge3_float, log23_edge10_float, log23_edge30_float, log23_edge30_float_pert, log23_edge60_float, log23_edge1_p1024, log23_edge3_p1024, log23_edge30_p512 (rigorous K = 30), log23_full_float, log23_full_float_pert (withdrawn beyond 270) (code/slopes_q.py, code/hump_report.py, code/report_order.py, code/crosscheck_float_arb.py) |

# Analysis: symbolic check scripts (Boussinesq Setting A2)

Independent symbolic checks of exact identities used in the analysis of the self-similar profile equations (P) of Setting A2
(U = (-Psi_y, Psi_x), W = beta X + U, transport equations (T) for Theta and (V) for Omega). No candidate profile was found in this
study; these scripts check exact algebraic and formal identities only and do not produce or certify any profile.

Software: Python 3.9 with sympy 1.14 (fp_axis.py uses numpy and scipy). Each script is self-contained, takes no arguments, prints its
results and writes no files. Run from inside this folder (analysis/) with `python3 <script>.py`.

| script | what it checks | report section (as stated in the script) | command |
|---|---|---|---|
| check_family6.py | the exact local family Psi = (beta x + (b/2) sin 2x) y, Omega = 2 b sin(2x) y, Theta = 2 b d sin^2(x) y (b = beta + 2, d = 2 beta + 1) solves (P); prints W, a0 and c = Psi_xy(0) | not stated | `python3 check_family6.py` |
| sinh_family_check.py | exact check that the sine and hyperbolic-sine separated families solve (P) on R^2 (Omega + Lap Psi, R_V, R_T, c, a0) | Remark 4.1 and Section 4 | `python3 sinh_family_check.py` |
| fam1d_b.py | for the sin and sinh families Psi = w(x) y: Theta obtained from (V), residual of (T), -Lap Psi - Omega, W1 on the axis, Psi_xy(0), a0; uniqueness of the odd/even power-series recursion to order 21 | not stated | `python3 fam1d_b.py` |
| fam1d_c.py | coefficient recursion of the one-dimensional reduction (T), (V) for v(x) = -(beta+2) x + ..., F(x): solvability coefficients at each order and agreement of the recursive solution with the series of the sin and sinh families | not stated | `python3 fam1d_c.py` |
| check_r1mode.py | single-mode ansatz Psi = x y h(q), q = x^2 + y^2, h = c + d q + e q^2: local jet of the residual R_Theta to fifth order, with c = 2 beta + 2, the solved e and the roots in beta of the remaining condition | not stated | `python3 check_r1mode.py` |
| check_thm10_labels.py | single angular mode: identifies the fifth-degree coefficients (x^4 y, x^2 y^3) of R_Theta and their factorized forms | Theorem 10 | `python3 check_thm10_labels.py` |
| check_traces.py | y-derivative traces of (T) and (V) on the x-axis under the A2 parity, with div W = 2 beta imposed up to order y^2 | not stated | `python3 check_traces.py` |
| check_third_trace.py | beta = 2 origin resonance coefficient for the trace h = Theta_yyy(x, 0): coefficient C of x^6 log x, the relation C + D/4 = 0, vanishing of the log forcing, and the value of D for the trigonometric family | not stated | `python3 check_third_trace.py` |
| check_yaxis_vorticity.py | y-axis temperature/vorticity traces: the ODE for s = K/E, limits at negative and positive simple zeros of the axis velocity, the exponent identities, an integral identity, the far-field solution s = -2 + C y^(1/beta), the exact identity for D = Omega + Theta_x and the transport of J_1 along the axis orbit | not stated (y-axis trace lemma) | `python3 check_yaxis_vorticity.py` |
| check88.py | energy flux identity with pressure: rcurl identities, div(W e + Pi U) - (4 beta - 2) e = U.M + y T for arbitrary Psi, Theta, Pi, the local expansions at O with c = 2 beta + 2 and the resulting quarter-disc integrals; prints PASS and the number of passed assertions | Theorem 88 | `python3 check88.py` |
| rec.py | exact-fraction implementation of the beta = 2 formal far-field recursion (Remark 39.1 form), z-independent orders up to G_7; library used by check68_later.py, also runnable on its own | Remark 39.1, Theorem 68 | `python3 rec.py` |
| check68_later.py | exact-fraction check of (68.16): the coefficient of c t^2 in [S_(K+2)] G_(J0+4), J0 = 2K+3, in a truncated ring, with logarithmic terms checked rather than assumed; any nonzero resonant forcing raises an error. Imports rec.py from this folder | Theorem 68 | `python3 check68_later.py` |
| fp_axis.py | numerical model study (scipy quadrature, not an exact check): sign of the finite-part integral F that decides K'_0 = 0 on the x-axis orbit from P to O, for several model profiles R(z) and beta = 2, 3, 6, 20 | not stated | `python3 fp_axis.py` |

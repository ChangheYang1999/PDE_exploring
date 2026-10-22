# SPEC (ipmA-lead): target theorem, spaces, splitting, bounds and owners

Version 3.43, 2026-10-22T00:42Z (shift 7; status lines only). Supersedes v3.42 (2026-10-21T14:25Z, notes/status_history/SPEC_v3.42_before_v3.43.md), v3.41 (14:00Z, notes/SPEC_v3.41_backup.md), v3.40 (08:36Z, notes/SPEC_v3.40_backup.md), v3.39 (06:18Z, notes/SPEC_v3.39_backup.md), v3.38 (06:03Z, notes/SPEC_v3.38_backup.md), v3.37 (05:38Z, notes/SPEC_v3.37_backup.md), v3.36 (05:23Z, notes/SPEC_v3.36_backup.md), v3.35 (04:59Z, notes/SPEC_v3.35_backup.md), v3.34 (04:25Z, notes/SPEC_v3.34_backup.md), v3.33 (03:49Z, notes/SPEC_v3.33_backup.md), v3.32 (03:25Z, notes/SPEC_v3.32_backup.md), v3.31 (03:09Z, notes/SPEC_v3.31_backup.md), v3.30 (03:04Z, notes/SPEC_v3.30_backup.md), v3.29 (02:53Z, notes/SPEC_v3.29_backup.md), v3.28 (02:41Z, notes/SPEC_v3.28_backup.md), v3.27 (02:24Z, notes/SPEC_v3.27_backup.md), v3.26 (02:13Z, notes/SPEC_v3.26_backup.md), v3.25 (02:10Z, notes/SPEC_v3.25_backup.md), v3.24 (02:06Z, notes/SPEC_v3.24_backup.md), v3.23 (02:02Z, notes/SPEC_v3.23_backup.md), v3.22 (01:51Z, notes/SPEC_v3.22_backup.md), v3.21 (01:17Z, notes/SPEC_v3.21_backup.md), v3.20 (01:09Z, notes/SPEC_v3.20_backup.md), v3.19 (00:58Z, notes/SPEC_v3.19_backup.md), v3.18 (00:35Z, notes/SPEC_v3.18_backup.md), v3.17 (00:06Z, notes/SPEC_v3.17_backup.md), v3.16 (23:18Z, notes/SPEC_v3.16_backup.md), v3.15 (23:15Z, notes/SPEC_v3.15_backup.md), v3.14 (22:48Z, notes/SPEC_v3.14_backup.md), v3.13 (22:29Z, notes/SPEC_v3.13_backup.md), v3.12 (21:58Z, notes/SPEC_v3.12_backup.md), v3.11 (21:32Z, notes/SPEC_v3.11_backup.md), v3.10 (21:19Z, notes/SPEC_v3.10_backup.md), v3.9 (20:53Z, notes/SPEC_v3.9_backup.md), v3.8 (19:01Z, notes/SPEC_v3.8_backup.md), v3.7 (18:37Z, notes/SPEC_v3.7_backup.md), v3.6 (18:19Z, notes/SPEC_v3.6_backup.md), v3.5 (18:01Z, notes/SPEC_v3.5_backup.md), v3.4 (17:23Z, notes/SPEC_v3.4_backup.md), v3.3 (17:14Z, notes/SPEC_v3.3_backup.md), v3.2 (16:54Z, notes/SPEC_v3.2_backup.md), v3.1 (16:38Z, notes/SPEC_v3.1_backup.md), v3 (15:53Z, notes/SPEC_v3_backup.md), v2.1 (15:24Z,
notes/SPEC_v2.1_backup.md), v2 (14:57Z), v1 (14:15Z). Change log at the end. Status labels: PROVED (place of proof), VERIFIED (independently
reproduced by the verifier), AUDITED (checked by an astra audit only), CONDITIONAL, HEURISTIC, REFUTED.

Version 3.44, 2026-10-22T12:18Z (shift 9, final; status line only; v3.43 kept verbatim in
notes/status_history/SPEC_v3.43_before_v3.44.md). Final state at the end of the run: the targeted theorem is not proved
(no bounded inverse of the linearization is known in any realization; verdict UNRESOLVED). Items verified after v3.43
(direct whole-plane X bounds of the exact trial, 1.49546805188731021373656 and 2464.68293019825564964515; the centre quasimodes in X, 5(p); the factor
supremum quasimodes, 5(r); the lower bound ||K||_X > 170.953964620623929217261 and the necessary same-X constant
C > 0.069361443018) are recorded with their scopes in FINAL_REPORT.md sections 3, 5, 6, 8 and 10, which supersede the
status labels below where they differ.

## 0. Decisions (v3)
- The verdict target for this run is realistic: UNRESOLVED with (a) a certified residual of the explicit trial, (b) the
  verified frozen and local theorems, (c) the conditional two-norm theorem T2N with named constants, (d) a precise
  structural account of WHY the reference route fails, and (e) ranked obstructions. No decisive `P_infty` route (the
  `B_3` exclusion is formal at every achieved radius). A YES would need a global inverse that nobody has; we keep
  the formulation below ready in case one becomes available.
- Structural picture (section 3.7, CONDITIONAL): every realization is fixed by its type at the source P (above or below
  the fast threshold) and at infinity (tails `gamma > k` or `gamma < k`). v3.7: the earlier claim "smooth-at-P classes
  with free tails (R+) are overdetermined by one after normalization (index -1)" is WITHDRAWN: it rested on the scalar
  germ count (kernel `y`, cokernel `f_y(P)`) of pure transport, which does not transfer to the coupled operator
  (astra pcusp1 Q5 counterexample, checked by lead), and at the frozen level smoothness at P costs infinitely many
  conditions (pcusp1 Q2, eq. (15)). The problem's own class `P_2` is of MIXED type
  (below threshold at P, tails up to `gamma < 1`): its linearization has a formal kernel containing the tail traces,
  so a Newton argument in `P_2` must fix a complement. The target formulation is F- (section 4): tail fixed to the
  trial's, remainder decaying relative to `r^k`, exponent `k'` and one tail parameter as scalar unknowns, scale fixed by
  the tail and J normalized afterwards by exact scaling.
- Weight convention (corrected after the verifier, spec_audit final section): "allowed growth gamma" means the norm
  `sup W / [m (1+u)^{gamma-k}]`, `m = u^3 (1+u^2)^{(k-3)/2}`, `u = r/L`. v3.1 correction (ver 16:17Z): the numerics
  code multiplies `W/m` by `(1+u)^{1/2}` (not `(1+u)^{1/2-k}`), i.e. allowed growth `k - 1/2 = -0.3206`; it is a
  valid UPPER bound for every allowed growth `gamma_Y >= -0.3206`, in particular for the F- forcing class
  (`2k - 1 < gamma_Y < k`). Reports must state the exponent actually used.

## 1. Equation and notation (fixed)
- `F(rho) = (c_l X + U[rho]).grad rho - rho`, `U = (-psi_y, psi_x)`, `-Lap psi = d_x rho` (canonical inverse, no
  `lambda x y`), `c[rho] = psi_xy(0)`, `c_l = (1 + c[rho])/3` built in (so `J(F(rho)) = 0` identically; realize1 C3:
  a separate closure equation would be redundant with the J-equation). Parity: rho even in x, odd in y; `rho = x^2 y a`
  near 0; `J(rho) := a(0)`. The y-axis ODE forces `rho(0, y) = 0`.
- `V = c_l X + U[rho]`; `DV(0) = diag(-A, D)`, `A = 2c_l - 1`, `D = 2A + 1`. Axis source `P = (x_*, 0)`,
  `DV(P) = diag(2c_l - mu, mu)`, `mu = 1` at exact solutions with `g := rho_y(P) != 0` (VERIFIED, ver local_geometry,
  scaling_index). `g' := rho_xy(P)`, `d := 1 + g`, `k := 1/c_l`, `b_0 := (A+3)/2`.
- X3 values: `c_l = 5.5753626`, `A = 10.1507252`, `D = 21.3014504`, `x_* = 8.60006`, `g = 29.7495`, `k = 0.17936`,
  `L = 7.6514`. Trial balls (num S1, rigorous): `x_* = 8.600063805157177 +/- 2.9e-13`, `mu~ - 1 in [-2.2529e-8,
  -2.2527e-8]`, `g in [29.749490663330, 29.749490663337]`, `g' in [0.2734114439768, 0.2734114439777]`.
- Linearization `L h = (V.grad - 1) h + B h`, `B h = W[h].grad rho`, `W[h] = Gamma h = U[h] + (c[h]/3) X`.
- Scaling: `rho_a(X) = a rho(X/a)`, `F(rho_a) = (F rho)_a`, `c[rho_a] = c[rho]`, `J(rho_a) = a^{-2} J(rho)`;
  `K = rho - X.grad rho`, `L K = eps - X.grad eps`, `c[K] = 0`, `J(K) = -2 J(rho)` (VERIFIED, ver scaling_index, under
  the stated differentiability / membership hypotheses; bare `P_2` does not put K in the same trace space: ver's
  oscillatory-factor example). A tail `r^k Theta` scales to `a^{1-k} r^k Theta`.

## 2. The trial (decided)
num's explicit modal trial `rho~` (exponential-polynomial splines in `t = log r`, even polynomial core, explicit far
form `x^2 y r^{k-3} (...)`), closed-form Green integrals, `c_l := 1/k`, `c~ = 3/k - 1` by exactified dependent
coefficients (VERIFIED: ver modal_repair, total exactification cost `< 4.080e-10`). Only residual: `eps~ = F(rho~)`.
Its tail is `r^k Theta_0~(theta)` with the trial's own angular profile.

## 3. Analytic facts

### 3.1 Source box, pure transport (VERIFIED, ver source_transport; AUDITED realize1 C1)
`L_A h = A s h_s + y h_y - h`, odd f in `C^{m,alpha}`, m >= 1: solvable in `C^{m,alpha}` iff `f_y(0) = 0`; kernel `y`;
`R f = int_0^inf e^t f(T_t X) dt`; `|D^beta R f| <= |D^beta f|/(A a + b - 1)` for `|beta| = a + b >= 2`. No derivative
gain. Dini modulus necessary.

### 3.2 Frozen coupled operator at P (VERIFIED, ver frozen_conjugation, coupled_thresholds, frozen_cokernel)
`L_P = A s d_s + y d_y - 1 - g M`, `M = xi^2/|zeta|^2`.
- Exact conjugation: with `a = g/(A-1)` (= 3.2511) and `Lambda = (-Lap)^{1/2}`, `Lambda^a L_P Lambda^{-a} = T + a - 1`;
  on `H_a` the inverse norm is exactly `1/|a - b_0|`.
- Sobolev thresholds `s_fast = (g + b_0)/A = 3.57855` (3.5785476; not "3.5786", which lies above it),
  `s_slow = b_0 = 6.5754`. Ordinary `H^s`: bijective for
  `0 <= s < s_fast` (so `3 < s < 3.57855` gives a `C^{2,s-3}` realization dissipative at P); infinite-dimensional
  adjoint kernel for every `s > s_fast`. Energy identity `Re <L_P h, h>_{H_s} = int [s - b_0 + (s(A-1) - g) m] |F|^2`.
- Hoelder (local cusp regularity at P): fast `d/A = 3.0293`, slow 1. Degree-d cusps `sgn y |y|^d F(s/|y|^A)` and the planar
  layer `|n|^{g/A}` (`C^{2.93}`) lie below the fast threshold.
- REFUTED (v2): Weyl sequences in every space below threshold; the rule "both T2N norms above threshold".
- Uniform coupled source inverse through resonance (VERIFIED, ver source_pole, 16:29Z):
  `A x d_x + mu y d_y - 1 - g M` is bijective from its maximal graph domain onto ordinary `H^{31/10}` (also with
  parity), inverse norm `<= 500/1687`, uniformly on `10 <= A <= 51/5`, `99/100 <= mu <= 101/100`, `29 <= g <= 30`
  (contains the trial's coefficients); source derivative bound `(500/1687)[8 pi (s-1)(s-2)]^{-1/2}`. Energy margins:
  `b - s mu >= 1687/500`, `b + g - s A >= 159/40`, `b = 1 + (A + mu)/2`.
- Variable-coefficient obstruction (VERIFIED conditional theorem, ver source_localization): if V is `C^{N+1}` near
  a fixed point (N > s), coupling = finite sum of bounded coefficients (`C^N` near P) times degree-zero multipliers,
  and the frozen model has normalized approximate adjoint kernels in `dot H^{-s}` (true for
  `A x d_x + y d_y - 1 - g M` when `(g + b_0)/A < s < b_0`), then no ordinary `H^s` graph realization plus finite rank
  is Fredholm. So "above threshold at P" is excluded for the variable operator in ordinary Sobolev graph form.
- The frozen homotopy pure transport -> coupled crosses `s_fast(tau) = (tau g + b_0)/A` (0.648 -> 3.579) (AUDITED
  realize1 C1): no fixed `3 < s < 3.579` is Fredholm-stable along it, so indices below threshold cannot be computed
  from pure transport by that homotopy.

### 3.3 Saddle (AUDITED realize1 C2; my derivation agrees)
Linear saddle `T_0 = -A x d_x + D y d_y - 1`. Incoming data G on `|x| = 1`: `h = |x|^{-1/A} G(y |x|^{D/A})`, modes
`|x|^{p_b} y^b`, `p_b = 2b + (b-1)/A`, `p_3 = 6.19703`. Exit data H on `|y| = 1`: `h = sgn y |y|^{1/D} H(x |y|^{A/D})`,
modes `x^{2j} sgn y |y|^{beta_j}`, `beta_j = j - (j-1)/D`: `beta_1 = 1` (the J mode), `beta_2 = 1.95305` (not `C^2`
across the stable segment), `beta_3 = 2.90611`. For smooth traces removing the `j = 2` singular coefficient suffices
for `C^{2,alpha}`, `alpha < 0.90611`; in `H^s` the `j = 3` term is forbidden for `s >= 3.40611`. The obstruction is the
singular coefficient after subtracting the particular solution (raw `H_4` need not vanish: `h = x^4 y`), and it is one
scalar only in a trace space smoother than `C^{2,alpha}` (`|x|^{2+nu}` traces give infinitely many independent
obstructions). Energy at the saddle: `S(0,(0,1)) = sD - (1 + c_l) > 0` for `s > 3`: isotropic `H^s` estimates fail
there in either direction; a separate (conormal / anisotropic) saddle space is required.
v3.2: the proposed saddle/edge spaces are in notes/conormal_framework.md (revision 2, after the astra conormal1
audit; PROPOSED): weighted b-Sobolev inverse of `T_0` with sharp norm `1/|bD - aA - b_0|` on the maximal graph domain
(forward iff `bD - aA < b_0`; AUDITED VALID; VERIFIED ver conormal_saddle (V6) 17:20Z, with the norm made precise:
`1/|delta|` in the base norm, `1 + 1/|delta|` into the sum graph norm); exit-trace regularity `C^{4+nu}`, `nu >= 2 alpha + (1 + alpha)/A`, as a
SUFFICIENT condition for a one-scalar saddle count, which also needs a regular particular solution (`J(L h) = 0`
excludes the resonant `x^2 y` forcing), `H_0 = 0` from global y-axis hypotheses, and a specified trace class;
triangular axis jet system; the ordinary disc at P is a design choice (a point blow-up resolves the coupling symbol).
Revision 1's local inclusion of the b-space in `H^s` was FALSE; the repair `b > s` forces the corner weight
`a - 1/2 > [D(s - 1/2) - 1]/A > 5.148 + 2.099 alpha`; the inequalities are feasible for `alpha < 0.406` (feasibility
only). The fixed-cutoff Taylor modification of the velocity is unbounded on the face weights (astra counterexample);
the x-face velocity remainder with global or frequency-adapted extensions is proved in notes/weighted_velocity.md
(Lemmas W1, W1'; EXACT; AUDITED VALID by astra weightedvel1 for N >= 1; VERIFIED ver edge_velocity (V7) 17:10-17:20Z,
with Arb/iv constants `C_{3,2.6} < 78.7988`, `C' < 82.2601`, `C_{3,3.4} < 151.0602`, `C' < 156.1241`). v3.3: the COUPLING is not bounded
on the pure power weight `L^2(|y|^{-2b})` (constant-norm dilates `R^{b-1} F(X/R)` give edge forcing `~ R^{b-2} c[F]` on a
fixed collar; weighted_velocity 4.2): the edge traces are controlled by W1 only in homogeneous norms, and their low
frequencies must be bounded by the far weight (`gamma' < 2` bounds `c[h]`). v3.5: the near/far splitting on BOUNDED
collars `I x (-d/2, d/2)`, `I` compact in `(0, inf)` avoiding nothing but the corner (`x_1 > 2d`), is in
notes/collar_coupling.md revision 2 (Lemma NF: fixed cutoff, inhomogeneous edge norms `H^{b-j-1/2}`, far part via the
parity-symmetrized kernel, `gamma' < 2` sharp; Lemma E: edge components; Corollary CC: coupling = `chi_0 y q + R_W`
with `R_W in L^2_b`, under finite strain `N_c(h) < inf`; `q_n` gains `b - 3/2`, the edge part `q_e` is order zero in the
edge coefficient). EXACT, AUDITED astra collar1 (single model; CC of revision 1 INVALID as stated, repaired), VERIFIED
ver V10 (18:24:59Z; endpoint `gamma' = 2` and "finite strain from collar norms" REFUTED; constants b = 3.403:
`K_n < 1211.755`, `A_0 < 1759.316`, `K_f < 9.3453e6`; FINAL_REPORT 5(i)). Open: P-disc transition, corner (Mellin), conic large x (cross-annulus summation), y-face (with the local
`-h` term of `U_2`), derivative/Hoelder versions. The edge forcing gains `b - 3/2` (not `b - 1/2`) derivatives.
v3.6 (conditioning, EXACT arithmetic on the VERIFIED V6 norm): in the window, `|delta| < 8.6507 - 21.3015 alpha`, so the
corner model inverse costs at least `0.13` (`alpha = 0.05`) up to `7.7` (`alpha = 0.4`); the old example `alpha = 0.4`,
`b = 3.403`, `a = 6.495` costs `64.6`. Working choice from v3.6: `alpha = 0.05`, `s = 3.06`, `b = 3.07`, `a = 6.45`,
`delta = -6.652` (cost `0.150`); inheritance of the lower bound by the variable operator is HEURISTIC.
v3.7 (source cusps of the FROZEN model; AUDITED astra pcusp1, single model, full argument astra/pcusp1/PROOF.md;
lead checked the conjugation `|zeta|^a L^ |zeta|^{-a} = -D - q` and the counterexample; ver V13 pending). For
`L_P = A s d_s + y d_y - 1 - g M`, `q = A + 2 - a`, `d = 1 + g`:
- (C1) forward inverse `h^(zeta) = -|zeta|^{-a} int_0^1 r^{q-1} |delta_r zeta|^a f^(delta_r zeta) dr`,
  `delta_r(s, y) = (r^A s, r y)`; for smooth compact odd f: `h = h_reg + chi K_f + h_rem`, `K_f = sgn(y)|y|^d F_f(s/|y|^A)`
  (finite-part definition; no logarithms since `d - A i` = 30.75, 20.60, 10.45, 0.297 for i = 0..3),
  `h_rem in H^r_loc` for `r < s_1 = s_fast + 2 - 2/A = 5.3815`.
- (C2) `F_f != 0` for an explicit f; then `h notin H^{s_fast}` at P, `h in C^{3, alpha_*}`, `alpha_* = d/A - 3 = 0.029290`
  (endpoint INCLUDED, sharp), `h notin C^4`; trace `d_y h(s, 0) = P_2(s) + c_f |s|^{g/A} + O(|s|^3)`, `g/A = 2.93077`, and
  `c_f` is one scalar functional (F_f != 0 does not force `c_f != 0`). h is smooth near P iff `F_f = 0`, an infinite-
  codimensional closed condition; the functionals are exactly the adjoint kernel elements for `s_fast < sigma < (A+3)/2`.
- (C3) `L(chi K_f) in H^r_loc`, `r < 5.3815`; frozen graph density: smooth trials have arbitrarily small residual in
  `H^sigma`, `sigma < s_fast`, with errors also small there. Ordinary mollification need NOT have small residual above
  `s_fast` (transport commutator at the cusp scale).
- (C4, CONDITIONAL) variable coefficients: the slow invariant curve `s = c y^2` displaces more than the cusp width
  `|y|^A`; the cusp must be centred in adapted coordinates (`S = s - c y^2`); the original-coordinate homogeneity is
  unjustified. A variable-coefficient theorem needs adapted coordinates, global realization and exclusion of other
  singular terms.
- (C5) REFUTED: "`f_y(P) = 0` is a cokernel condition of the coupled operator". Counterexample: `k = chi_0 (s^2 y - y^3/3)`,
  `u = -Lap k` vanishes near P, `f = L_P u = (T - 1) u + g d_s^2 k = 2 g y` near P. Correct jet identity
  `f_y(0) = (mu - 1) h_y(0) - g (M h)_y(0)` (nonlocal).
Consequences. Frozen level, local regularity at P only (ver V13: this is NOT membership in the global classes `P_m`,
which constrain the centre factorization, the canonical law and the growth; the earlier wording is withdrawn): generic
forcing gives local `C^{3,alpha}` with `alpha <= 0.0293` at P, not `C^4`; whether exact
F- solutions near X3 are cusped at P is CONDITIONAL (C4 plus the nonlinear problem). The F- spaces (`3 < s_H < 3.406` at
P, below `s_fast`) are compatible with a cusp. A numerical residual near P is meaningful in `H^sigma`, `sigma < s_fast`
(`sigma = 3.06` in the working choice), not in `C^4` or `H^4` (a smooth trial cannot be `C^4`-close to a cusped solution).
Floating diagnostics (code/energy_conormal.py): face flows have zeros only at 0 and `x_*`; `mu > 0`, `V_2(0,y) > 0`.
v3.7 (G1 status): y-face collar coupling in notes/yface_collar.md (Lemmas S, NF-Y, E-Y, Corollary CC-Y; EXACT, by swap
reduction to collar_coupling rev 2; revision 2 after astra yface1, single model, NEEDS-FIX with all repairs
incorporated: jets defined by continuous extension, exact localized edge decomposition `h = h_n + H_2 + H_4 + h_f`,
finite-regularity ranges (near `q_2 in H^{min(a-3/2,4)}`, `q_4 in H^{min(a-7/2,2)}`, far `W^{4,inf}`, `W^{2,inf}`), axis
condition `h(0,.) = 0` conditional on listed global hypotheses and kept as a class assumption; ver V12 on rev 2). Key difference from the x-face: the
full velocity jets of y-face edge components are smoothing (order `-1`; the local `-h` of `U_2` cancels the order-zero
part), so the coupling does not change the principal part of the y-face edge system on bounded collars. Corner: astra
corner1 (single model; lead checks in notes/corner_coupling.md): the double remainder `T_x^{N_x} T_y^{N_y} U_i` is
bounded on `L^2_{a,b}` for `N_x - 1/2 < a < N_x + 1/2`, `N_y - 1/2 < b < N_y + 1/2`; rectangular corner subtraction is
REFUTED globally (annular trace spaces needed; resonance at even integer `A = a + b`); with unit-box data the corner
coefficients are bounded iff `A > k + 1`; the coupling decomposes as `y q_1(x) + x^2 q_2(y) + x^4 q_4(y) - J x^2 y - K x^4 y
+ f_rem` with `J = 0` (strain cancellation) and `f_rem` bounded on unit-box data, unbounded on the pure global weight.
v3.8: notes/corner_coupling.md written (lead sympy checks of `J = 0`, `K`, `q_1, q_2, q_4` and the degree-7 obstruction).
Consequence: face traces near the corner need subtraction of ALL parity-allowed corner powers below `A - j - 1` (resp.
`A - l - 1`), i.e. corner coefficients up to degree 7 at `A = 9.52`; `A` must avoid even integers (resonance); the
parity `alpha` even in x and y is automatic in the class; `alpha in C^8` near 0 for the trial is OPEN.

### 3.4 Far field (AUDITED realize1 C3, C6; my derivation agrees)
`(c_l r d_r - 1)(r^sigma H) = (c_l sigma - 1) r^sigma H`; at `sigma = k` every angular trace is free (exterior kernel).
Energy at infinity `S = c_l gamma - 1`: forward (R-) estimates need `gamma < k`. The scalar term
`(c[h]/3) X.grad rho ~ (k c[h]/3) r^k Theta` is outside every `gamma < k` target; it is cancelled exactly by the log
tail: `(c_l r d_r - 1)(r^k log r Theta) = c_l r^k Theta`, with `delta k = -(k^2/3) c[h]`.

### 3.5 Source functional and scaling (VERIFIED, ver scaling_index)
`d_y(L h)(P) = (mu - 1) h_y(P) + g d_y W[h]_2(P) + g' W[h]_1(P)` (h only `C^1`). At an exact solution
`w'(x_*) g' + g mu'(x_*) = 0` and `d_y(L K)(P) = 0`. v3.1 correction: the cost `1/|mu~ - 1|` (`~ 4.4e7`) belongs to
the isolated pure-transport jet equation only; it is NOT a lower bound for the coupled inverse (REFUTED as an
inference by ver source_pole: the frozen coupled operator is uniformly invertible through `mu = 1`, and at `mu = 1`
the nonlocal term solves forcings with `f_y(0) != 0`). `f -> f_y(P)` is not the full cokernel functional of L
(index1: `l = j - j B M^{-1} R Pi`, CONDITIONAL on a global transport inverse). Consequence for F-: no bordering at P
is needed below threshold.

### 3.6 Codimension-one bookkeeping (VERIFIED, ver scaling_index)
If L is Fredholm on a graph domain D and J is continuous and nonzero on D, then `ind(L|ker J) = ind L - 1`. A
norm-continuous Fredholm path on fixed spaces has constant index. Neither the initial index nor Fredholmness along a
path is proved for the IPM operator. J is not continuous in plain `C^{2,alpha}` or `H^s` (realize1:
`h_eps = x^2 y chi(X/eps)`, `J = 1`, norms `O(eps^{1-alpha})`, `O(eps^{4-s})`), so factor control is part of every
realization.

### 3.7 Realization types (CONDITIONAL structural picture; the local pieces are 3.1-3.4)
| type | at P | at infinity | saddle | formal count after normalization |
|---|---|---|---|---|
| R+ | above `d/A` (e.g. `C^{4,alpha}`), values from P | `k < gamma < 1`, tail determined | incoming modes `|x|^{p_b} y^b` | v3.7: NO count. The old "index -1" is withdrawn (pcusp1 C5); frozen level: infinite-codimensional range (C2) |
| R- | below `s_fast` (`H^s`, `3 < s < 3.406`) | `gamma < k`, tail fixed | one singular exit coefficient (`beta_2`) in a smooth-trace space | see F- (section 4) |
| mixed (= the class `P_2`) | below `s_fast` | `k < gamma < 1` | as R- | formal kernel contains the tail traces (infinite-dimensional) |
| opposite mixed | above | `gamma < k` | as R+ | infinite cokernel (frozen whole-plane model: VERIFIED) |
Reasoning (CONDITIONAL): along transport orbits from P to infinity, a solution is fixed by one end. R+ fixes it at P
(finitely many jets, so the tail is determined); R- fixes it at infinity (the tail is data). In the mixed class both
ends are free: the tail traces `r^k H(theta)` are formal kernel directions (each corrected by an R- solve and by the
log mode for its `c[.]`), and the saddle and source conditions are absorbed by tail freedom. (v3.5: revision 3.4 said
"`c_l` moves along the family"; that is NOT established: first-order variation is the undecided functional `ell` of
notes/tail_family.md section 5.) Consequences:
(a) In `P_2`, an exact solution near X3 (if any) is not expected to be isolated: the expected solution set is a family
parametrized by tail data, modulo finitely many conditions. v3.5: this is now a CONDITIONAL theorem, VERIFIED as a
conditional statement (ver V8, 17:44Z) and AUDITED (astra family1): notes/tail_family.md revision 2 (Lemma T tail
uniqueness, unconditional; Theorem FL kernel `~ Tau/span Theta_1` on `X_+`; Theorem FN injective family on an affine
slice, normalized on a codimension-two slice, non-isolation in `G_gamma` under embeddings; `c_l = 1/k'` on members;
`ell` decides only first-order variation). The hypotheses (S1)-(S5) (F- mapping, bounded F- inverse, uniform closure,
continuity, differentiability) are open. Answer to PROMPT 5(ii) in FINAL_REPORT section 10 (realize1 C5: the numerics
alone cannot distinguish). Corroboration only: the first run's numerics found states with
`c_l` in [5.29, 5.60] at equal residual, softest directions in the far field near the y-axis, and `c_l` pinned only
when smoothness at P was enforced (h(P) row, Taylor patch).
(b) v3.7 (replaces "non-generic (index -1)"): in smooth-at-P classes the frozen source already imposes infinitely
many conditions (pcusp1 C2: smoothness iff `F_f = 0`), so such a class is not a Fredholm realization at the frozen
level and no finite index is assigned. Whether an exact solution near X3 is smooth at P is open; at the frozen level
it would require the vanishing of the whole cusp profile. The pure-transport germ count (kernel `y`, cokernel
`f_y(P)`, 3.1) concerns `T - 1` only. A Newton argument cannot close there (3.8); a nonexistence argument would need
the same missing inverse.
(c) `P_infty` constrains only the centre (`a` in `C^infty` near 0: the centre modes `|x|^{p_b} y^b`, b = 3, 5, ...,
must vanish); it does not require smoothness at P (VERIFIED scope, ver scaling_index).

### 3.8 Unnormalized contraction lower bound (VERIFIED as a conditional statement, ver scaling_index)
In unnormalized spaces satisfying all T2N hypotheses with K in the high and low domains:
`K_L C_B K_H eta >= eta ||B(K,K)||_{Y_L}/(||LK||_{Y_H} ||LK||_{Y_L})`, `L K~ = eps~ - X.grad eps~`. No numerical ratio
is claimed until the three norms and eta are validated (num R5).

### 3.9 Global flow and pure transport (VERIFIED as conditional statements, ver topics 52-54; AUDITED flow1, flow2)
notes/global_flow.md rev 3 (FINAL_REPORT 5(l)). Under the flow hypotheses H0-H4 every open-quadrant orbit comes from
P and escapes to infinity; on the maximal L^2(w0) domain `||(V.grad - 1)^{-1}|| <= e^{C_kappa/2}/kappa` with the box cost
`C_kappa <= 2 sum tau_i t_i`; instance (conditional on the box inequalities) `5 exp(1111/5000) < 6.245` at
`kappa = 1/5` and `(50/11) exp(2929/13000) < 5.695` at `kappa = 11/50`; far lower bound `1/kappa_inf`,
`kappa_inf in (0.2807, 0.281)`. Exterior part of H4 certified for the trial (`r >= 3634`, topic 53). OPEN: the bounded-region
inequalities (num N1'), a smooth weight for the coupled estimate, the coupled inverse.

### 3.10 Centre coefficient B_3 and P_infty (lead notes/pinf_B3.md rev 1 from astra pinf1; V16(b) VERIFIED ver topic 59 with a sign fix in A4; ver topic 60: the trial's reconstructed Q has nonzero resonant logarithms, so the polynomial-only B1/B4 premise fails for this trial; no value of a generalized B3 is proved)
`B_3 = -FP int_0^{x_*} H f/w` is a criterion only: smooth `a` (C^{6,alpha}, `alpha > p_3 - 6`) forces `B_3 = 0`; it is
not a `P_2` obstruction; at exact solutions w alone determines B_3. The trial's B_3 estimators are dominated by its
centre defects (x < 0.03; floating code/b3_axis.py), so the trial cannot decide B_3. A scoped P_infty exclusion would
need a centre-regular reference with `w0'(L0) = -w0'(0)`, a validated 1D evaluation and a uniform corner bound; its
meaningfulness as a NO is doubtful (pinf_B3 section 4). Not a current target.

### 3.11 Axis jets and the P-row (J3-J7 of notes/global_flow.md section 12; V16(a) VERIFIED ver topic 58 with scoped refutations (J3 bound needs normalized evaluations; J5 does not control a separate outer branch; J7 needs a Dini condition); prow1 collected; V17(a,d) VERIFIED ver topic 61, V17(c) topic 62, V17(b) topic 63)
x-axis jet `b = h_y(x,0)`: `w b' + (mu - 1) b + U_1[h](x,0) G_1' + d_y U_2[h](x,0) G_1 + (c[h]/3)(x G_1' + G_1) = f_y`,
`T G_1 = 0` at exact solutions. At P the pure jet transport is not onto (`mu_P = 1`).
prow1 (21:00Z, AUDITED, lead checked (1), (45)-(47) arithmetic; V17 requested):
- (1) `(mu_P - 1) h_y(P) + l_P(h) = f_y(P)` is the y-derivative of `L h = f` at P, so the P-row is IMPLIED by the
  equation (no extra condition). J3 is a statement about the split jet operator, not about L.
- Origin matching (7): if the incoming trace `b_1` at `x_1` is prescribed independently, normalization imposes one
  scalar equation; at exact solutions it is consistent with the scaling direction K (LK = 0); at the trial
  `L K~ = (X.grad - 1) F(rho~)`.
- Scale collapse (18): a strip-to-disc transition with `lambda -> 0` adds `(b_x - sigma) w lambda'/lambda` to the
  transverse rate, unboundedly positive if `b_x < sigma`. Characteristic-set form (21).
- Induced jet operators (31)-(33): `B_chi` of order -1, `P_chi = I - S_chi` (smoothing), `c[Eb] = -(P_chi b)(0)`,
  `N_chi b = G_1' B_chi b - G_1 P_chi b - ((x G_1' + G_1)/3)(P_chi b)(0)`; Volterra bound `M/(1 - M n)` (36).
- Closure: Schur complement `S = A - B D^{-1} C`, `sigma_min(S) >= s > 0`, `||L^{-1}|| <= d + (1 + d||C||) s^{-1}(1 + ||B|| d)`
  (41); a homotopy switching the coupling off is NOT justified (needs `t > 0.888` at sigma = 13/4).
- Uniform frozen window over the F1 box: `kappa_y = 6 - (sigma - 1/2) 101/100`, `kappa_x = 99/200 + 30 - (sigma - 1/2) 51/5`,
  `3 < sigma < 2373/680`; `||L_P^{-1}||_{H^{13/4}} <= 200/489` (47).
- Corner constraints (49)-(50): a generic `x^p y^q` remainder term needs `a < p + 1/2`, `b < q + 1/2`; with only the y-jet
  removed, `x^2 y^3` forces `a < 5/2` and then `delta > 0`.
Decision (v3.10): the strip/collar design of v3.9 is SET ASIDE (scale collapse; no x-axis jets are needed once the
P-row is redundant). Replacement: D_b (3.12).

### 3.12 Design D_b / D_b' (PROPOSED; floating diagnostics only; AUDITED by astra dib1 (obstructions O1-O5) and dib2 (D1-D10))
- Vector fields `Z_1 = g_1^{1/2} d_x`, `Z_2 = g_2^{1/2} d_y`, `g_2 = <r>^2 = 1 + (r/L)^2`,
  `g_1 = <r>^2 x^2/(x^2 + lam^2 <r>^2)` (b-type `x d_x/lam` near the y-axis, scaled ordinary elsewhere, ordinary and
  nearly isotropic near P). Weight `omega = |x|^{-2a} (1 + (r/L_w)^2)^{a - gamma'} e^{+phi}`. Correction of v3.10
  (dib1 (20)): the sign is `e^{+phi}`, since the weight contributes `-(1/2) V.grad phi` to the rate. phi is bounded
  with `V.grad phi >= 2 (E + kappa)^+` for a strict margin kappa > 0; this needs a smooth majorant of E with
  derivative bounds.
- Space: direct sum `X = E_2 J_2 (+) E_4 J_4 (+) R`; the weighted integral is infinite on jets, so the jets carry
  their own norms. Locally `R = x^alpha H^s_b(dx dy/x)` with `alpha = a - 1/2`, and `x^m b(y)` lies in R iff
  `m > alpha`. The jet norms at infinity are `int <y>^{4j + 1 - 2 gamma'} |a_{2j}|^2` (dib1 (12)).
  y-axis jets only (`a_0 = 0` is invariant since `rho(0, y) = 0`); no x-axis jets, no y-weight.
- Parameters: `s = 3.06`, `(sD - c_0)/A = 5.77 < a < 6.5`, `gamma' = 1.129 < 1 + 1/c_l`, `lam = 0.5`. By dib1
  (5)-(7) the projected Riesz constant is `C (1 + 1/dist(alpha, Z))`, so `a = 6.45` (`alpha = 5.95`) is a poor
  choice. By that constant `a = 6.0` (`alpha = 5.5`) is best; the corner rate is then `-c_0 - aA + sD = -2.30`
  (see the trade-off after the rate table).
- Identities from dib1, elementary, checked by the lead at 21:28Z (V18 requested):
  (1) `U_2(0, .)^ = k int_0^inf e^{-kz} h~ dz`.
  (8) `u_0 = B`, `u_2 = -a_2 - B''/2`, `u_4 = -a_4 + a_2''/12 + B''''/24`, `u_1 = -B'`, `u_3 = a_2'/3 + B'''/6`,
  `u_5 = -u_4'/5`, `c[h] = B'(0)`.
  (23) `[x^2 y] L h = 0` for every admissible h, so the target must satisfy `[x^2 y] f = 0` (cf. `J_c = 0`, 5(k)).
  (14) An exact profile is not in `L^2(<r>^{-2 gamma})` for `gamma < 1 + 1/c_l`. Proof by flow scaling:
  `rho(Phi_t X) = e^t rho(X)` and `det D Phi_t = e^{2 c_l t}`.
- Obstructions found by dib1 (to be repaired):
  (O1) Far field. For compactly supported h with zero jets and `c[h] != 0`, outside the support
  `L h = U[h].grad rho + (c[h]/3) X.grad rho` (correction 22:07Z after a verifier objection: the nonlocal velocity
  does not vanish outside supp h; dib1 (17) keeps it). For compact h, `U[h] = O(r^{-2})`, so `U[h].grad rho =
  O(r^{k-3})` lies in the far weighted space, while `(c[h]/3) X.grad rho` does not (18). Repair: use the fixed-tail formulation (section 4,
  F-) and add the log-tail direction `chi r^k log r Theta_0` to the domain. Since
  `(V.grad - 1)(r^k log r Theta_0) ~ c_l r^k Theta_0`, it balances `(c[h]/3) k r^k Theta_0`.
  (O2) Scaling. K is not in the far space (30), so scaling contributes no kernel and no `[x^2 y] h = 0`
  normalization is needed; the scale is fixed by the tail amplitude, as in F-.
  (O3) Jets. At `t = s` the jet blocks have positive top-order rates `D (t - 1/2 - p_j)` (29). In the diagonal
  model each jet row has one matching condition `int_0^inf F/(v H_j) = 0` (28), because the homogeneous solution
  `H_j ~ y^{k - 2j}` at infinity is excluded by `gamma' < 1 + k`. In the coupled system these become coupled
  constraints. A tail-profile parameter tau (F-) with a nonzero x^4-jet at the y-axis may balance the a_4 row; the
  a_2 row is consistent with `[x^2 y] f = 0`.
  (O4) Fredholm route. Compactness fails for translation-invariant smoothing in log variables. An index argument
  along `L - tau I` needs Fredholmness on the whole path, and switching off the coupling is unsafe (F1).
  (O5) Orbit cost. Norm comparison loses a factor `e^{W/2}`, which is 77.5 at W = 8.7.
- Floating principal rates (code/energy_b.py; maxima of E over the region):

  | region | a = 6.45, L_w/L = 1 (runs/energy_b_l0.5.json) | a = 6.0, L_w/L = 1 (runs/energy_b_a6_lw1.json) | a = 6.0, L_w/L = 0.5 (runs/energy_b_a6_lw0.5.json) |
  |---|---|---|---|
  | corner `r < 0.1` | -6.86 (limit -6.865) | -2.29 (limit -2.30) | -2.27 |
  | `0.1 <= r < 1` | -6.12 | -1.72 | +0.45 (x-axis, r = 0.98) |
  | incoming x-axis `0.05 < x < 8.5` | <= -0.88 | up to +1.52 (x = 4.0) | up to +11.8 (x = 4.0) |
  | `\|X - P\| < 1` | <= -2.08 | <= -2.23 | <= -2.94 |
  | y-axis | <= -0.58 | <= -0.55 | <= -0.55 |
  | far field | -> -0.281 | -> -0.281 | -> -0.281 |
  | off-axis maximum | 10.3 at r = 10.6 | 10.4 at r = 10.6 | 8.9 at r = 5.1 |

  On the incoming x-axis the y-derivatives see the transverse expansion `s d_y V_2` and the inflow makes the far-weight
  term positive; at a = 6.45 the term `a V_1/x` compensates. These rates cover the remainder only; the jet blocks are
  not covered (O3). Trade-off: a = 6.0 has the better Riesz constant (`1 + 1/dist(alpha, Z) = 3` against 21 at
  a = 6.45) but a smaller corner margin and a positive x-axis segment; a = 6.25 (`alpha = 5.75`, factor 5) is the
  compromise to test. a = 6.25 (runs/energy_b_a6.25_lw*.json, 21:44-21:50Z): corner `r < 0.1` -4.80 / -4.83,
  `0.1 <= r < 1` -1.88 / -4.17, incoming x-axis up to +11.0 / +0.19, `|X - P| < 1` -2.99 / -2.14 (L_w/L = 0.5 / 1);
  backward costs with `kappa = 0.1`: 7.18 (L_w/L = 0.5), 8.94 (L_w/L = 1).
- Orbit costs by backward integration (code/orbit_back.py, runs/orbit_back_*.json; forward shooting under-samples
  the orbits). sweep_b1/b2: `sup W = 8.72` at the base point, range 5.4-12.7, `L_w/L = 0.35-0.5` gives 6.5-6.9.
  sweep_b3 (runs/sweep_b3.log; Rt = 1e4 unless noted): a = 6.0, `L_w/L = 0.5`: `W = 7.18` (`kappa = 0`; 7.179 at
  Rt = 400), 7.33 (`kappa = 0.1`), 7.48 (`kappa = 0.2`); a = 6.45, `L_w/L = 0.5`, `kappa = 0.1`: 7.06; a = 6.0,
  `L_w/L = 1`, `kappa = 0.1`: 9.01. Strict margins up to 0.2 cost about 0.15 per 0.1 (the far rate -0.281 bounds
  kappa).
- astra dib2 (21:36:55Z, collected 21:55Z; astra/dib2/answer.md) on D_b' = D_b local spaces + fixed tail F-
  (log tail q = chi r^k log r Theta_0, tau-tail t = chi r^k Theta_1, e = chi r^k Theta_0). Lead checks (21:58Z):
  items marked [checked] were rederived by hand.
  (D1) Count. Conditional on an index-zero remainder block and admissible couplings, the unnormalized count is
  `0 - 1 + (1 - 1) + 1 = 0` (a_2 row 0, a_4 row -1, (k', far scalar) 0, tau +1). Imposing `a(0) = 1`
  (`[x^2 y] h = 0`) gives -1, so F- must solve the unnormalized fixed-tail problem and normalize afterwards by the
  scaling `rho_lambda = lambda^{-1} rho(lambda X)` (which changes the tail amplitude), as section 4 already states.
  (D2) a_2 row [checked]: `[y] F_2 = [y] f_2` including the nonlocal terms (`r_2 = y + O(y^3)`, `B = c y + O(y^3)`,
  coefficient `-2c + c + c = 0`), so the only local condition is `[x^2 y] f = 0`; the solution from infinity
  `a = -H_1 int_y^inf F/(v H_1)` is unique (H_j not in the far jet space since `gamma' < 1 + k`). Needs `v > 0` on the
  whole y-axis, `s' > 3/2`, a graph domain for `v d_y` and endpoint Hardy estimates. This solves the row only for
  known forcing; B depends on all of h.
  (D3) a_4 row [checked]: the raw matching integral diverges for `F'(0) != 0` (`T_2 y = D(1 - p_2) y`). Regularized
  functional `ell_4^0(F) = int_0^inf (F - T_2 S_F)/(v H_2)`, `S_F = F'(0) y chi_0/(D(1 - p_2))`, independent of
  chi_0 since `T_2 S/(v H_2) = (S/H_2)'`. One condition, for `s' > p_2 + 1/2 = 2.453`. The row contains `a_2'` and
  `B'''`, not `a_2''`, `B''''`.
  (D4) Tail jets [checked]: `r^k Theta = theta_2 x^2 y^{k-2} + (theta_4 + (k-2) theta_2/2) x^4 y^{k-4} + ...`;
  log-tail jets include the extra term `theta_2 y^{k-4}/2` in the x^4 jet. Tail directions are not jet + remainder:
  at the far corner `||y^beta b(x/y)||_R^2 ~ int y^{2 beta + 1 - 2 gamma'} dy int t^{-2a} |b|^2 dt` diverges at
  `beta = k`; they must be carried as full functions. No extra matching at the far corner for the exact far
  transport (gap `kappa_inf = 1 - c_l (gamma' - 1) = 0.2808` [checked], equal to minus the far rate of 3.12); uniformity for the full operator is unproved.
  (D5) Mapping: transport is unbounded on a same-order Sobolev space (`h_n = n^{-s} chi e^{i n xi.X}`), so the
  domain must be a graph domain `{h in X : V.grad h in X}` (jets likewise). Far subtraction (11)-(12):
  `L(h, kappa, tau) = (A h + a kappa + b_tau tau, d(h) + m kappa + n tau)`, `A h = (V.grad - 1) h + U[h].grad rho
  + c[h] w`, `w = (X.grad rho - k e)/3`, `d(h) = k c[h]/3`, `a = L q - m e`, `m = c_l + k c[q]/3`, `b_tau = L t - n e`,
  `n = k c[t]/3` [checked]; columns admissible since `2k - 1 = -0.641 < gamma' - 1` under far symbol hypotheses (13).
  (D6) Velocity: `B^(eta) = |eta| int_0^inf e^{-|eta| x} h^(x, eta) dx` (h vanishing on the axis) [checked against
  dib1 (1)]; remainder supported off the axis has `B != 0`; local smoothing `B_R in H^{s + a - 1/2}_y`
  (flat model, (15)); jets `B ~ 2 |D_y|^{-2} a_2`, `24 |D_y|^{-4} a_4` [checked]; keep the cancellations in `u_2`,
  `u_3`. `c[h] = int_{x>0} 2y(3x^2 - y^2)/(pi r^6) h` [checked] is bounded on R for `2 < a`, `gamma' < 2`. The global estimate
  for the projected product `h -> U[h].grad rho` is unproved; U does not preserve X.
  (D7) Source: with `mu_P = 1` the pure-transport inverse from infinity is not regular at P (smooth `f = y phi(s)
  psi(y)`, phi = 0 near 0, gives `d_y h(s, 0) = -(1/A) int_s^inf phi(z)/z dz` for s > 0, hence a jump
  across s = 0 [checked; VERIFIED ver topic 68, 22:41Z: no C^1 representative, not H^sigma_loc for sigma > 2, not H^1_loc for A >= 3, FR 5(l)]; for phi(0) != 0 a log singularity); the remainder reference block near P must contain the
  nonlocal term (G1), as in 5(a)-(b) of the report.
  (D8) Blocks: no triangular structure (C_2, C_4 of (19) are explicit and nonzero; the extension cutoff contributes
  `(V.grad chi) x^{2j} a_{2j}`). Conditional closure (20)-(24): `mu_J = 1 - C_J eps_JJ`, `mu_R = 1 - C_R eps_RR`,
  `theta = C_J C_R C_JR C_RJ/(mu_J mu_R) < 1`, `C_H` (22), bordered Schur complement `S = D_f - C H^{-1} B` and
  `||L^{-1}|| <= C_H + (1 + C_H ||B||) C_S (1 + ||C|| C_H)`.
  (D9) Transversality: eliminate kappa (`T = A - a d/m`, `b = b_tau - (n/m) a`); with `T^* ell = 0` the condition is
  `ell(b) != 0`, not `ell_4^0` of the raw x^4 jet of `L t`. Counterexample to the angular criterion [checked]:
  `Theta_1 = sin theta cos^2 theta (1 + (3 - k) cos^2 theta/2)` has `cos^4` coefficient `(2 - k)/2 != 0` but zero
  x^4 jet. `Theta_1 proportional to Theta_0` puts the scaling kernel `K - (k - 1) t` in the enlarged domain; num's
  C2 tau-column (`Theta_0 cos 2 theta` in this notation) is not proportional to Theta_0. (Here Theta_1 is the
  tau-profile, not the asymptotic correction `r^{k-1} Theta_1` of the task statement.) Checking `ell(b) != 0` needs an enclosure (30) with
  validated adjoint stability; far truncation error decays only like `R^{-(1 + k - gamma')} = R^{-0.050}` from
  the weighted target norm alone.
  (D10) Size: `e^{W/2}/kappa_inf = 130-276` before projection, localization, coupling and Schur losses; a
  successful bound plausibly `1e3-1e4` (planning estimate, not a bound). Remaining analytic gaps: the global
  projected velocity estimate near the axis and corner, the extension transition, a source estimate retaining the
  nonlocal term, the far-corner uniformity, Fredholmness/surjectivity, and a validated nonzero coupled Schur
  complement.
- Requirements on the trial (lead analysis). Near 0, a non-polynomial homogeneous term `r^m E(theta)` of the
  correction or of the residual is admissible only if `m > a + s - 1` (8.06 at a = 6.0). The present trial has
  `m = 5` (section 4 of the report), and its residual has `H^3 ~ 1` on the P-disc. D_b therefore needs N7
  (`j <= 4`) and a P-disc refit (chainR).
- Phase-space orbit cost (v3.18, HEURISTIC, floating; code/bichar_back.py). Along the backward flow carry the
  frequency direction by `zeta' = J^T zeta` and take the cost of an orbit as the supremum over sub-segments of
  `int 2(R_s + kappa)` with the full symbol rate in direction zeta. At `s = 3.1`, `a = 6.25`, `gamma' = 1.129`,
  `lambda = 0.5`, `L_w/L = 0.5`, `kappa = 0.1`: pointwise (direction-maximized) cost 7.410, bicharacteristic cost
  7.069 (`e^{C/2}` 40.6 against 34.3); at `s = 3.06`: 7.176 against 6.850. The order-0 part contributes 0 on every
  orbit; the cost is the order-s term. So a phase-space escape function gains about 5 percent over a weight in X
  only; the remaining cost is intrinsic to the weight design (x-axis band 1 < x < 7, rate up to +11.6).

### 3.13 Lower-order route (PROPOSED; floating diagnostics only; AUDITED by astra dib3; lead checks 22:23-22:29Z, code/chk_dib3.py; obstructions B2, B3 (identity), B5-B8, B10 VERIFIED ver topic 70, 23:03Z, FR 5(n); B8 only for the explicit annular norm)
Proposal (lead, 22:07Z). Prove existence through T2N in a D_b'-type realization of local order `2 < sigma_H < 3` (low
order `sigma_L = sigma_H - 1`), where the trial's residual near P is smaller, then upgrade the solution to `C^{2,alpha}`
(`P_2`) by a separate regularity theorem.
- Floating inputs. Residual of the trial near P (num, FFT of `chi eps~`, NUM_REPORT 7.5):

  | patch | sup | H^2 | H^2.25 | H^2.5 | H^2.75 | H^3 | H^3.06 |
  |---|---|---|---|---|---|---|---|
  | 0.5-disc | 1.14e-5 | 7.34e-3 | 2.28e-2 | 7.43e-2 | 0.253 | 0.890 | 1.208 |
  | 1.0-disc | 1.67e-5 | 4.40e-2 | 0.159 | 0.580 | 2.13 | 7.86 | 10.76 |

  A factor 3.2-3.6 per quarter derivative (knot-scale structure). Rates and orbit costs at lower order (sweep_b4,
  WORKLOG 22:18Z): `e^{W/2} = 5.6-20.6` for `s = 2.25-2.75` against 39-91 at `s = 3.06`. Corner limit
  `-c_0 - aA + sD`: -9.40 at (2.25, 5.0), -4.08 at (2.5, 5.0); at (2.75, 5.0) it is +1.25 (inadmissible, a = 6 used).
- Audit dib3. Items marked [checked] were rederived by the lead (V20 requested).
  (B1) [checked; VERIFIED ver topic 68, FR 5(l)] At any exact solution with `rho, V in C^1`, `V(P) = 0`, `grad rho(P) = (0, g_P)`, `g_P != 0`:
  `mu_P = 1` and `A_P = 2c_l - 1`. Proof: `V.grad rho - rho` is differentiable at P with derivative
  `DV(P)^T grad rho(P) - grad rho(P)`; DV(P) is diagonal by parity; the y-component is `g_P (mu_P - 1)`; `div V = 2c_l`.
  (B2) [checked, sympy] Frozen counterexamples to a local bootstrap. For odd n with `p = (g + 1 - n)/A > 1`
  nonintegral, `H_n = sum_{j <= (n-1)/2} b_j |s|^{p+2j} y^{n-2j}`, `b_0 = 1`,
  `b_{j+1} = -[g + 2j(A-1)](n-2j)(n-2j-1) / [2(j+1)(A-1)(p+2j+2)(p+2j+1)] b_j`, satisfies `-Lap L_P H_n = 0` (mu = 1),
  using `-Lap M = -d_s^2` and `-Lap L_P w = (g + 1 - lambda) d_s^2 w + (1 - lambda) d_y^2 w` for `w = |s|^q y^r`,
  `lambda = Aq + r`, `lambda_j = g + 1 + 2j(A-1)`. So `L_P(chi H_n)` is harmonic where `chi = 1`, while
  `chi H_n in H^t_loc` iff `t < p + 1/2`. n = 7: p = 2.33974 (in H^2.5, not in H^3.1); n = 11: p = 1.94568 (not C^2).
  Hence "u in H^{sigma_0}, L u in H^{sigma_1} locally implies u in H^{sigma_1} locally" is FALSE for the frozen
  operator. No conflict with (G1): the global forcing of `chi H_n` is rough on `supp grad chi`. Any upgrade must be
  global, with the same operator, domain and target at both orders.
  (B3) [checked] Uniqueness transfer: if A is injective on `D_0` and maps `D_1 c D_0` onto `Y_1 c Y_0`, then
  `u in D_0`, `A u in Y_1` imply `u in D_1`. For the nonlinear problem the exact identity is `A_h h = -f_0` with
  `A_h u = (V_rho.grad - 1) u + (Gamma u).grad rho~`, `f_0 = F(rho~)`; its transport coefficient `V_rho` is only
  `C^{1,beta}`, `beta < sigma_0 - 2`. Using `DF(rho)` instead is circular (`DF(rho) h = -f_0 + (Gamma h).grad h`).
  Possible repair: a global tame estimate, uniform under a regularization `J_eps`:
  `||J_eps h||_{X_1} <= C (||f_0||_{Y_1} + ||h||_{X_0}) + theta ||J_eps h||_{X_1}`, `theta < 1`. Not proved.
  (B4) [checked] Lipschitz transport alone does not propagate `H^{sigma_1}`: `B(y) d_x u - u = 0`, `u(0, y) = 1`,
  `B = 1 + eps chi(y) |y|^p`, `u = exp(x/B(y))`, `sigma_0 - 1/2 < p < sigma_1 - 1/2`. The active-scalar structure may
  allow tame commutator estimates (Kato-Ponce); not proved for this realization.
  (B5) [checked] Regularity does not give the factorization: `rho = chi(r) x^2 y r^{-eps}` is `C^{2,alpha}`
  (`alpha <= 1 - eps`) and `H^s_loc` for `s < 4 - eps`, but `rho/(x^2 y)` is unbounded. Continuity of the factor must
  come from the realization (jets plus weighted remainder) or from the equation.
  (B6) [checked] c at low order: `|c[h]| <= C_s ||h||_{H^s}` iff `s > 2` (`int^inf r^{3-2s} dr`). For `t = sigma_H - 1 < 2`
  the family `e_eps = eps^{t-1} phi(X/eps)` (phi annular, even in x, odd in y, `c[phi] != 0`) has `||e_eps||_{H^t} ~ 1`
  and `c[e_eps] = eps^{t-2} c[phi] -> infinity`. So C_B fails for the unaugmented `E = H^{sigma_H - 1}`. In D_b' the
  corner weight may control c (`|K_c| <~ r^{-3}`; the near-origin bound is finite for a > 2), with separate jet bounds.
  (B7) [checked] Corner and jet window at lower order: `max{9/2, (sD - c_0)/A} < a < 13/2`,
  `(sD - c_0)/A = 2s - 1/2 + (s - 3/2)/A`; s = 2.5: `a > 4.5985`, a = 5.0 gives -4.0754. The mode `y^{p_2}` stays excluded
  from the a_4 jet space iff `s' > p_2 + 1/2 = 2.4531`, independently of s; keep `s' >= 2.46` (count of 3.12 unchanged).
  If `s' < 2.4531` the domain gains one dimension and tau must be dropped or one scalar condition added (conditional on
  the actual matching map). A `y^{p_2}` jet term with a rectangular cutoff is not `C^2` across `y = 0` at `x != 0`;
  with a conical cutoff (`|x| <~ |y|`) it is.
  (B8) [checked] Centre condition `m > a + s - 1` (radial integral), 6.5 at (2.5, 5.0). Correction of the lead's question:
  the trial's residual is `r^5 E(theta)` at 0 (report section 4: m = 5 in density units; the factor has the
  non-polynomial `r^2 D(theta)`), not "degree five in the factor"; dib3's conclusion that degree 8 passes rests on this
  misstatement. The centre condition fails at both orders; N7 is needed for any D_b' route.
  (B9) [checked] The source estimate still needs the nonlocal term for `2 < s < 3`: `beta_fast = sA - c_0 - g`,
  `beta_slow = s - c_0`, both negative; without gM, `beta_fast = sA - c_0 > 0`. The pure-transport resonance
  `(A s d_s + y d_y - 1)(y log|y|) = y` persists.
  (B10) [checked] Residual norms: `||chi f||_{H^s} <= (eps ||chi||_2)^{1 - s/3} ||chi f||_{H^3}^{s/3}`, constant 1
  (Hoelder on the Fourier side); illustration with eps = 1e-4, radius 0.5, `B_3 = 0.9`: 0.090, 0.193, 0.417 at
  s = 2.25, 2.5, 2.75 (num's direct values are smaller: 2.28e-2, 7.43e-2, 0.253). Fractional norms can also be certified
  directly (Gagliardo double integral, constant `4^theta Gamma(1+theta)/(2 pi |Gamma(-theta)|)`). dib3's warning on
  spline interfaces (a `C^2` cubic spline gives a residual outside `H^{5/2}`) does not apply to X3: its modes are
  degree-7 splines with exact `C^6` joins, so `eps~` is `C^5` across joins and cellwise derivative bounds of order
  `<= 5` are bounds on global weak derivatives.
- Lead assessment. The route is conditional on (L1) low-norm control of c in the realization; (L2) a high-order a
  priori estimate for `A_h` in the same realization at some `sigma_1 in (3, s_fast)`, with lower-order part bounded by
  `||h||_{X_0}` and quasilinear part `<= C ||h||_{X_0} ||u||_{X_1}`, so that `theta = K_1 C ||h||_{X_0} < 1` (only finiteness
  of `f_0` in `Y_1` is needed, not smallness); (L3) a regularization family compatible with the weighted b-structure;
  (L4) preservation of the factorization and the far bound. In addition the low-order closing inequality needs
  `K_L C_B K_H eta_0 < 1` with `eta_0 ~ 7e-2` (H^2.5, 0.5-disc, floating) and `e^{W/2} ~ 11-21` inside K_H, K_L.
  The route stays a proposal and does not change the verdict.

### 3.14 Hoelder scale at the source (AUDITED astra holder1, single model; lead checked (3)-(5), (8)-(11), (19), (20) and the endpoint table against notes/holder_heuristic.md; frozen model VERIFIED ver topic 74 (V21), 00:03Z; variable-coefficient transfer and the log at sigma = a OPEN)
Frozen model only: `L_P = A s d_s + y d_y - 1 - g M` (mu = 1), `R = L^2`-selected inverse `-int_0^inf S_t dt`,
`S_t = e^{-t} D_t Q_t`, `D_t f(z) = f(e^{tB} z)`, `B = diag(A, 1)`, `Q^_t = ((xi^2 + eta^2)/(e^{2(A-1)t} xi^2 + eta^2))^{a/2}`,
`a = g/(A - 1) = 3.2511`, `q = (1 + g)/A = 3.0293` (cusp order of G2), `C_*^sigma = B^sigma_{inf,inf}`; forcing
supported in a fixed compact K, constants depend on K; assumes `A > 1`, `1 < a < A + 1`.
- (H1) `||R f||_{C_*^{r(sigma)}} <= C_K ||f||_{C_*^sigma}` for `1 < sigma < a`, `r(sigma) = sigma - (sigma - 1)/A`; the
  exponent cannot be raised, even for smooth forcing supported in an arbitrarily small neighbourhood of P, even in s and
  odd in y. Packets `f_N = N^{-sigma} phi(s) psi(y) sin(N y)`, `N = 2^n`: `||R f_N||_{C_*^sigma(B_r(P))} ~ 2^{n(sigma-1)/(A-1)}`
  for `1 < sigma < q` (mechanism: the transverse frequency is carried for time `log N`, then the slow direction
  amplifies by `e^{(sigma-1)t}` until the s-scale `l N^A` is reached; my heuristic gives the same exponent).
- (H2) Endpoints: `0 < sigma < 1` bounded on `C_*^sigma`; `sigma = 1` loses a logarithm, necessarily
  (`d_y R f_N(0) = -phi(0) psi(0) log N/(A - 1) + O(1)` with `f_N = N^{-1} phi psi sin(N y)`, and a dyadic sum in `C_*^1`);
  `sigma = a` log upper bound, sharpness for odd forcing open; `sigma > a` output `C_*^q` (optimal by G2); at
  `sigma = q` the uniform output order is `r(q) = 2.8294`, not q.
- (H3) In `C^{2,alpha}` language: forcing `C^{2+alpha}` gives at best `C^{2+alpha'}`, `alpha' = ((A-1) alpha - 1)/A`,
  positive iff `alpha > 1/(A-1) = 0.1093`. A correction of order beta needs forcing order
  `tau(beta) = (A beta - 1)/(A - 1)` (2.6639 for beta = 2.5).
- (H4) Weighted and anisotropic Hoelder spaces: power weights do not embed in unweighted `C^sigma`; anisotropic
  orders keep the packet growth `N^{(r-1)/(A-1)}`. A mixed space (Sobolev `3 + alpha < sigma_H < s_fast` near P, Hoelder
  elsewhere) is not ruled out by the frozen obstruction and needs `alpha < 0.5786`; cutoff commutators, nonlocal tails
  and interface compatibility are open.
- (H5) Conditional persistence (Q4): if the transport and coupling coefficients are smooth near P, the global norm
  controls the nonlocal tails and is locally equivalent to `C_*^sigma` on compact corrections, a two-parameter Weyl
  sequence (truncated, mollified frozen packets, then an isotropic dilation `eps^sigma w_j(z/eps)` at P) rules out
  `||h||_{C_*^sigma} <= C (||L h||_{C_*^sigma} + ||h||_lower)`. Not proved for exact `P_2` profiles (whose `grad rho` is
  only `C^{1,alpha}`) or for every Hoelder-type space.
- (H6) Consequences: same-order Hoelder Newton at `C^{2,alpha}` is obstructed in the frozen model; a standard smooth tame
  Nash-Moser theorem does not apply directly (smooth forcing produces the cusp; the loss `(sigma - 1)/A` depends on the
  order). A two-norm scheme with a stronger forcing norm, a restricted range or a cusp-adapted scale is not excluded.
- Lead assessment. This supports local order `3 < sigma_H < s_fast` near P (3.2, G1) over a native Hoelder realization,
  and it explains the role of `s_fast`. It changes no verdict.

### 3.15 Local H^s a priori estimate at the source (AUDITED astra srcloc1, single model; lead checked (3)-(5), (10)-(18), (21), (22), (26), (28)-(34), (45), (48) by hand and with code/chk_srcloc1.py, chk_srcloc1_kernel.py (floating); S1-S5 VERIFIED ver topic 77 (V23), 00:41:39Z, conditional on the box and E < kappa; S6 VERIFIED ver topic 78, 00:46:04Z; strain sign correction VERIFIED ver topic 80, 00:56Z; coefficient bounds M_rho, M_V VERIFIED ver items 84, 85, 01:32Z, 01:44Z; trial instance of every hypothesis of S1-S6 VERIFIED ver topic 89, 02:09Z)
Setting. `s = 31/10`, `t = 21/10`; P the trial's source with `V(P) = 0`, `DV(P) = D = diag(A_P, mu_P)`,
`grad rho~(P) = a_P = (0, g)`, `div V = tr D`; `(A_P, mu_P, g)` in the box `10 <= A <= 51/5`, `99/100 <= mu <= 101/100`,
`29 <= g <= 30`; `V in C^4`, `rho~ in C^5` on `B_{3 delta}(P)` with certified derivative bounds, `0 < delta <= 1`,
`3 delta < |P|/2`. Inhomogeneous `H^r` (`J^r = (1 - Lap)^{r/2}`, unitary Fourier transform), restriction norms
`||h||_{H^r(Omega)} = inf ||H||_{H^r}` over extensions. `h in C_c^infty` with `h(0) = 0`, `grad h(0) = 0` (true for
`h = x^2 y b`), and the completion in the graph norms. Cutoffs centred at P: chi (1 on `B_{5 delta/4}`, support in
`B_{7 delta/4}`), tau (1 on supp chi, support in `B_{9 delta/4}`), theta (1 on `B_{2 delta}`, support in `B_{3 delta}`),
zeta (1 on `B_{5 delta/2}`, support in `B_{3 delta}`).
- (S1) Frozen margin [checked]. `Re <L_P u, u>_{H^s} <= -kappa ||u||_{H^s}^2`, `kappa = 1687/500 = 3.374` over the box:
  the inhomogeneous symbol `-(A + mu)/2 - 1 + s (A xi^2 + mu eta^2)/<zeta>^2 - g xi^2/|zeta|^2` is bounded by the
  homogeneous one, which is affine in `xi^^2`; slow direction at `A = 10`, `mu = 101/100` gives 3.374, fast direction
  `35.595 - 10.2 s` (= 3.975 at s = 3.1). The box version reaches only `s < 3.4897`; larger s needs narrower enclosures.
- (S2) Energy estimate [checked]. With `w = theta (V - D z)`, `q = theta (grad rho~ - a_P)` and the whole-plane auxiliary
  operator `A = L_P + w.grad + q.U`:
  `Re <A u, u>_{H^s} <= -(kappa - E) ||u||_{H^s}^2 + R ||u||_{H^{s-1}} ||u||_{H^s}`,
  `E = (1/2) ||div w||_inf + s ||Dw||_{inf,F} + ||q||_inf`, `R = T_s(w) + sum_i P_s(q_i)`.
  The point is the expansion `[J^s, w.grad] = -s sum (d_j w_i) d_ij J^{s-2} + R_w` with
  `||R_w u||_2 <= T_s(w) ||u||_{H^{s-1}}`, `T_s(w) = s(s-1) 2^{s-4} sum_i (W_2(w_i) + beta_{s-1} ||w_i||_{H^s})`: only first
  derivatives of w and values of q enter E. Taylor bounds: `E <= C_V delta`,
  `C_V = [3s + (9/2)(s + 1/2) C_theta] M_V + 3 M_rho`, `M_V = sup ||D^2 V||_F`, `M_rho = sup ||D^2 rho~||_F` on `B_{3 delta}`,
  `C_theta = delta ||grad theta||_inf`; `C_theta = 2` gives `C_V = 41.7 M_V + 3 M_rho`. (The FR calls this constant
  `C_src`, to keep it apart from the T2N velocity constant `C_V` of section 5.)
- (S3) Explicit constants [checked]. `W_r(f) = (2 pi)^{-1} int <k>^r |f^|`, `alpha_r = 1/(2 sqrt(pi (r-1)))`,
  `beta_r = 1/(2 sqrt(pi (r-1)(r-2)))`; `P_s(f) = s 2^{s-2} (W_1(f) + alpha_{s-1} ||f||_{H^s})` bounds `[J^s, f]` from
  `H^{s-1}` to `L^2`; `B_s(f) = ||f||_inf + P_s(f)` bounds multiplication on `H^s` (given the `H^{s-1}` norm);
  `M_r(f) = 2^{r/2} W_r(f)` on `H^r`. `||[U, chi] v||_{H^s} <= 2 * 3^s W_s(chi) ||v||_{H^{s-1}}` (symbol `|m| <= 1`,
  `|Dm| <= 1/|zeta|`). Kernels `K_1 = -xy/(pi |X|^4)`, `K_2 = (x^2 - y^2)/(2 pi |X|^4)` (imaginary and real parts of
  `(x + iy)^{-2}/(2 pi)`), `|D^gamma K_i| <= (|gamma| + 1)!/(2 pi) |X|^{-2-|gamma|}`. Far part
  `|D^gamma U_i[(1 - zeta) h]| <= k_j N_far(h)` on `B_{9 delta/4}`, `k_j = 100 (j+1)!/(2 pi) (4/delta)^j`,
  `N_far(h) = int_{|X-P| >= 5 delta/2} |h|/|X-P|^2 + int_{R^2 \ B_{3 delta}(P)} |h|/|X|^3`. Strain
  `|c[h]| <= C_c ||h||_{H^t(B_{3 delta})} + N_far(h)/pi`, `C_c = 3 delta/(sqrt(pi) (|P| - 3 delta)^3)` (kernel
  `|d_y K_2| <= 1/(pi |X|^3)`; the vanishing of h and grad h at 0 removes the local terms).
- (S4) Local estimate [checked]. Localization identity
  `A(chi h) = chi L h + (V.grad chi) h + (a_P + q).[U, chi] h - chi ell c[h]`, `ell = X.grad rho~/3`. Result:
  `||chi h||_{H^s} <= K_1 ||tau L h||_{H^s} + K_2 A_h + K_3 H_h + K_4 N_far(h)`, `K_1 = 1/(kappa - E)`,
  `A_h = ||h||_{H^s(B_{2 delta} \ B_delta)}`, `H_h = ||h||_{H^t(B_{3 delta})}`, `K_2, K_3, K_4` explicit (srcloc1 (24), (31),
  (34)). Exactly `K_1 = 1/(kappa - E)` (instead of `B_s(chi)/(kappa - E)`) uses inner/outer partitions with separation
  `delta/8` and the off-diagonal kernel bound `|K_{J^s}(X)| <= D_s |X|^{-2-s}`, `D_s = 2^s Gamma(1 + s/2)/(pi |Gamma(-s/2)|)`
  (1.62874 at s = 3.1; checked by quadrature), giving `J_delta = (4 pi D_s/s)(8/delta)^s`. Inputs: `D^j V`, `j <= 4`,
  `D^j rho~`, `j <= 5`, on `B_{3 delta}`, and cutoff derivatives through order 5. Size: `delta <= kappa/(2 C_V)` gives
  `K_1 <= 1000/1687 = 0.59277`; keeping the knot-scale radius `delta = 0.0165` needs `C_V <= 102.24`. For fixed cutoff
  shapes the conservative constants scale as `K_2 = O(delta^{3-2s})`, `K_3 = O(delta^{3-3s})`, `K_4 = O(delta^{-s-2})`
  (not optimal).
- (S5) Outflow and the outer estimate [checked]. `V.grad chi >= -eps chi` is impossible for a cutoff that orbits leave
  (`chi(Phi_t z) >= e^{-eps t} chi(z)`); on a factor-two annulus `sup |V.grad chi| >= A_P/log 2` in the frozen
  calculation. So the annular term `A_h` is intrinsic. An outer estimate O(h) must give
  `||h||_{H^s(B_{2 delta} \ B_delta)} <= C_A O(h)` in ordinary `H^s` (an `H^{s-eps}` or `C^{2,alpha}` outer estimate does not);
  with `S <= aF + bO + dR_0`, `O <= cF + eps S + eR_0` the two combine iff `b eps < 1` (b contains `K_2 C_A`), giving
  `S <= ((a + bc) F + (d + be) R_0)/(1 - b eps)`. The lower-order quantity `R_0` (here `H_h`, `N_far`) still needs a
  separate bound or a Fredholm argument with the kernel excluded.
- (S6) Auxiliary whole-plane inverse (VERIFIED ver topic 78: maximal domain `{u in H^3.1: b.grad u in H^3.1}`, L^2 transport
  graph core, semigroup by J^s conjugation and a Dyson series, `||S_A(t)|| <= (1 + R/d)^s e^{-(kappa - E) t}` with
  `d = 1 + (A + mu)/2 - kappa + s ||Dw||_F >= 3121/1000`, for global real `C_c^4` w, q and the source box). If `a_s = kappa - E > 0`, then with `a_0 = 1 + tr D/2 - ||div w||_inf/2 - ||q||_inf`
  (`a_0 - a_s = 1 + tr D/2 - kappa + s ||Dw||_{inf,F} > 0`): `||A^{-1}||_{H^s -> H^s} <= (1/a_s)(1 + R/(a_0 - a_s))^s`,
  `A^{-1} = -int_0^inf S_A(t) dt`. Not a Neumann series (w.grad is unbounded on `H^s`). It solves an auxiliary problem
  only: it does not match outer data, and the localized rank-one strain term needs a certified
  `|1 + c[A^{-1} ell_delta]| > 0`. Sign convention (VERIFIED ver topic 80, 00:56Z; assumes `ell_delta in H^s` and bounded strain): with the prompt's `-Lap psi = d_x h`,
  `U = (-psi_y, psi_x)`, the canonical strain is `sigma = -h_y(0)/4 - PV(K_s * h)(0)`, `K_s = y(3x^2 - y^2)/(pi r^6)`;
  the denominator is `1 + sigma[A^{-1} ell]` in this convention (`1 - sigma_minus[...]` in the opposite one). All
  K_1-K_4 bounds use `|sigma|` and are unchanged. No denominator has been enclosed.
- (S7) Exact residual identity [checked]. `d_y F(rho~)(P) = (mu_P - 1) g` (parity and `V(P) = 0`); at the trial's floating
  values `-6.70198e-7`. This is the identity behind the trial-centred jet exclusion of FINAL_REPORT section 7 (VERIFIED
  ver topic 76, 00:24Z: `|(mu~ - 1) g| > 6.70e-7`, `30.0229 < C < 30.0230` for `C = |mu~ - 1| + g + |g'|`, margin above
  `9.69e-9` at radius `2.2e-8`; the upper constant 30.0229 of v3.17 was refuted and replaced by 30.0230).
- Lead assessment. (S1)-(S5) give the local source piece of the linear hypothesis of T2N at order 3.1 with explicit
  constants, conditional on certified coefficient bounds on `B_{3 delta}(P)` (N8) and on an outer estimate in ordinary
  `H^s` with `b eps < 1`. It is not a global inverse, and the residual must still be small in `||tau eps~||_{H^s}` on
  `B_{9 delta/4}(P)` (floating, 0.5-disc: `H^{3.06}` about 1.2). Changes no verdict.
- N8 (num RUN_STATUS as read at 00:55Z): floating `C_V = 13.1 <= 102.2` at delta = 0.0165 and `17.7 <= 33.7` at 0.05 (fails at 0.1, 0.2);
  rigorous test at 0.0165: `M_V <= 0.30245`, `M_rho <= 0.47604`, `C_V <= 14.04`, so `E <= 0.2317` and `K_1 <= 0.3183`
  (pending ver). Floating `||tau eps~||_{H^{3.1}} = 1.56, 1.07, 0.81, 1.37` for delta = 0.0165, 0.05, 0.1, 0.2, dominated by
  cutoff-scale content. So the local source estimate is available at delta = 0.0165, and the forcing it must absorb is
  of order one: `K_1 ||tau eps~||_{H^{3.1}}` is about 0.5 before any coupling constant.
- N8 fine pass (num TO_TEAM addendum 00:59Z, runs/n8/cert_n8_fine0165.json): interval bounds on `B_{0.0495}(P)`:
  `M_V <= 0.28728`, `M_rho <= 0.45336`, `C_V <= 13.34`, so `E <= 0.2202`, `K_1 <= 0.3171` (num's figures). Ver audit
  (topic 82, CONFIRMED limited scope 01:10Z): exact implications `C_V < 13.34` on the full delta = 0.0165 disc
  `=> E < 0.22011, K_1 < 0.318`, and `C_V < 18.634` on the full delta = 0.05 disc `=> E < 0.9317, K_1 < 0.41`; the
  v1 fine output's delta = 0.05, 0.1, 0.2 rows do not cover their discs (three exact missing-point comparisons). The
  actual coefficient suprema are neither accepted nor disproved. OPEN: directed runtime geometry, the geometric
  exclusion filter, the Bernstein/coordinate sub-interval pairing, and the Green/Taylor/Cartesian/Frobenius arithmetic.
  Num v2 (TO_TEAM 01:13Z): drops rows with delta > delta_max, one common exact sub-interval `[kk hk_f, (kk+1) hk_f]`
  for modes and `e^{-t}`, an interval lower bound for the cell distance to P, exact angular partition and radial
  coverage assertions; v2 fine pass reproduces v1 (24457 cells, same bounds); reruns (runs/n8/cert_chain3.sh) end about
  01:30Z. Astra n8ref1 (num) confirmed most v1 code items and found the same three defects plus a one-ulp `x_*` ball.
  Ver item 83 (01:25Z, CONFIRMED): geometry of the exported v2 coordinate masks (all omitted boxes disjoint from the
  discs, selected nodes covered; fine mask covers the delta = 0.0165 disc). Ver item 84 (01:32Z, CONFIRMED):
  independent density Hessian `M_rho < 0.5059` on `B_{0.0495}(P)` (Arb512 + iv180, no producer filter). Ver topic 85
  (01:44Z, CONFIRMED): independent velocity Hessian `M_V < 743/2500 = 0.2972` on `B_{0.0495}(P)` for every P in the
  exact source bracket (Arb512 + iv180, all 8320 boxes). With 84: `C_V < 13.91094`, `E < 0.22953051`, `K_1 < 0.3181`
  (ver topic 86 FINAL 01:52Z, CONFIRMED: exact closure; E bound written `E < 0.22953051`). OPEN: num's tighter suprema, MR conversions, Bernstein pairing. Num v2 final (TO_TEAM 01:32Z): fine `C_V <= 13.3395`, full `C_V <= 14.0736` (0.0165),
  `18.6333` (0.05). Num mid run (TO_TEAM 01:51Z, RIGOROUS per num, not verified): `C_V <= 18.16, 19.67, 21.23` at
  delta = 0.05, 0.06, 0.07, so `C_V delta < kappa/2` up to 0.07 on num's numbers. Num 01:40Z: by the mean value
  theorem `||DV - DV(P)||_op <= M_V |X - P|`; with ver's `M_V < 0.2972` this is `< 0.0148 < mu_P/2` on
  `B_{0.0495}(P)`, so (E3) of 3.16 holds there with verified input (num's larger-ball values up to 0.3 unverified).
  Ver topic 89 (FINAL 02:09:44Z, CONFIRMED): the canonical trial velocity has a zero P = (p, 0), unique in the bracket
  (4841405518533377/2^49, 4841405518533711/2^49) (width 5.9e-13); DV(P) = diag(A, mu), A in [10, 10.2], mu in
  [0.9999999774, 0.9999999776] (strictly below 1); grad rho~(P) = (0, g), g in [29, 30]; cut-off fields C_c^6 / C_c^5;
  so all hypotheses (1) of S1-S6 hold and the local estimate holds for the trial with K_1 < 0.3181, every annular,
  lower-order and remote term retained; auxiliary maximal-domain inverse exists with finite, numerically UNEVALUATED R;
  d >= 3121/1000. (E3) base point: sym DV(P) >= 0.99 I and variation < 0.0147114 < 0.495 on B_0.0495(P): cutoff sign
  holds for the trial. OPEN: R, rank-one denominator, outer matching, global inverse. Statements about the trial only.

### 3.16 Outer estimate with a vanishing source cutoff, escape weight, assembly (AUDITED astra escape1, single model; lead checked the far threshold, the far log identity, the c[h] Beta identity, the kernel of psi_xy, the commutator symbol inequalities, the saddle ratio and the Q4 numbers with code/chk_escape1.py (floating) and by hand; V25 CONFIRMED conditional, ver topic 88, 02:04Z: E1-E5, E7, E9 and the stated constants under the stated hypotheses; OPEN: actual escape weight, weighted/conormal fractional norms, equivalence for unspecified A_s, E6 parametrix, outer assembly)
Setting: the remainder realization of 3.12/3.13 with weight `omega = e^phi |x|^{-2a} (1 + r^2/L_w^2)^{a - gamma'}`,
`a = 6.25`, `gamma' = 1.129`, `L_w = 0.5`, and an order-s differentiation operator A_s (not yet fixed; the constants depend
on its quantization).
- (E1) Realization defect at the axis [checked]. For `h = O(x^6)`, `U_1[h] = x u_1(y) + O(x^3)`, `U_2[h] = u_0(y) + O(x^2)`,
  so `U[h].grad rho~ = x^2 (2 a_2 u_1 + a_2' u_0) + O(x^4)` with `rho~ = x^2 a_2(y) + O(x^4)`. The remainder block is not
  preserved; the remainder operator needs an explicitly defined jet projection (an `x^4` output is not in `L^2(x^{-12.5})`,
  while `x^6` is: `int_0^eps x^{12 - 2a} dx < inf` for `a < 6.5`).
- (E2) Far-field defect [checked]. Away from the axes `omega ~ r^{-2 gamma'}` and `X.grad rho~ ~ k r^k Theta`, so
  `X.grad rho~ in L^2(omega)` iff `gamma' > 1 + k = 1.179361`; at `gamma' = 1.129` the radial exponent is
  `2k - 2 gamma' + 1 = -0.89928 > -1` (divergent). A negative far energy rate `c_l (gamma' - 1) - 1 < 0` needs
  `gamma' < 1 + k`. Hence a compactly supported remainder with `c[h] != 0` has `Lh` outside the forcing space for every
  admissible `gamma'`: the strain term cannot be absorbed by changing the far exponent. Repair: an explicit far component.
  Exact: `(c_l r d_r - 1)(r^k log r Theta) = c_l r^k Theta` (since `c_l k = 1`), so the far response to the strain is
  `h_log ~ -(c[h]/(3 c_l^2)) r^k log r Theta` (here `c[h] = psi[h]_xy(0)` raw, section 1; with the prompt's
  `c = psi_xy(0)/3` the same coefficient reads `-c/c_l^2`; ver V25 01:43Z used the prompt's c); neither this nor `r^k Theta` is in the remainder space. This is the same
  far parameter as the `(k', tau)` columns of F- (section 4) and agrees with 3.12 O1-O5 and garding1 Q5 (3.17 G6).
- (E3) Vanishing source cutoff [checked by hand]. If `||DV - DV(P)||_op <= mu_P/2` on `B_delta(P)`, then
  `w.V(P + w) >= (mu_P/2)|w|^2` and every nondecreasing radial cutoff `zeta_P = chi(|X - P|/delta)` (0 on `[0, 1/2]`, 1 on
  `[1, inf)`) has `V.grad zeta_P >= 0`. In the signed transport identity for `H = A_s h`,
  `Re int zeta_P^2 omega H^* V.grad H = -(1/2) int zeta_P^2 div(omega V)|H|^2 - int zeta_P (V.grad zeta_P) omega |H|^2`,
  the cutoff term has the favourable sign: there is no top-order inner forcing. Estimating `L(zeta_P h)` term by term
  instead reintroduces a top-order transition-region norm. `||zeta_P A_s h||` and `||A_s(zeta_P h)||` differ by
  commutators; division by `zeta_P` is not available. The large frozen coupling gives
  `Re <m(-gM f), m f> = -g ||M^{1/2}(m f)||^2 + g Re <[M, m] f, m f>`: no hidden top-order coupling from `-gM`, but a
  possibly large commutator constant at order s - 1.
- (E4) Explicit commutator constants [checked: symbol inequalities and the two Sobolev integrals]. Unitary Fourier
  transform, `Lambda^s = (1 - Lap)^{s/2}`, `M_t(b) = int <p>^t |b^(p)| dp`, `N_s(b) = int |p| <p>^{s-1} |b^(p)| dp`:
  `||b f||_{H^t} <= (2^{t/2}/(2 pi)) M_t(b) ||f||_{H^t}` (t >= 0, Peetre);
  `||[Lambda^s, b] f||_2 <= D_s(b) ||f||_{H^{s-1}}`, `D_s(b) = s 2^{(s-1)/2} N_s(b)/(2 pi)`;
  `||[U, b] f||_2 <= (2 sqrt 2/(2 pi)) M_1(b) ||f||_{H^{-1}}` (the lead's sharper symbol bound is
  `|m(eta + p) - m(eta)| = |sin angle(eta + p, eta)| <= sqrt 2 <p>/<eta>`; astra's `2 sqrt 2` is valid);
  `||[U, b] h||_{H^s} <= ((2 sqrt 2/(2 pi)) M_1(b) + 2 D_s(b)) ||h||_{H^{s-1}}`; `M_1(b) <= sqrt(pi) ||b||_{H^3}`,
  `N_s(b) <= M_s(b) <= sqrt(pi/(4 - s)) ||b||_{H^5}`. Separated inputs: `|D^alpha K(z)| <= (|alpha| + 1)!/(2 pi |z|^{|alpha|+2})`
  (as in 3.15 S3). Off-diagonal kernel of `Lambda^s`: the bound `2^s Gamma(1 + s/2)/(pi |Gamma(-s/2)|) |z|^{-2-s}` is the
  homogeneous constant D_s of 3.15 S4; for the inhomogeneous operator it was NOT checked by the lead.
- (E5) Strain functional on the remainder [checked: Beta identity to 3e-31 and the kernel `d_xxy(-(2 pi)^{-1} log r) =
  y (y^2 - 3x^2)/(pi r^6)`, modulus `|sin 3 theta|/(pi r^3)`; VERIFIED ver topic 88 with corrections]. For a remainder
  with `h(0) = 0` and `h_y(0) = 0` (ver 88: `h(0) = 0` alone does not remove the local strain derivative; alternatively a
  weighted-domain premise that forces both), the raw strain satisfies
  `|c[h]| <= (e^{-inf phi/2} L_w^{a-2}/pi) sqrt(B(a - 2, 2 - gamma') B(a + 1/2, 1/2)) ||h||_{L^2(omega)}` for `a > 2`,
  `gamma' < 2`; at the working parameters with `inf phi = 0` the constant lies in `(0.0078147, 0.0078149)`, safe ceiling
  `C_raw < 0.0078149` (the earlier decimal 0.0078148 is inward as an upper bound); for the prompt's `c = psi_xy(0)/3`
  the ceiling is `0.002605`. The input functional is lower order; this does not repair the output defect (E2).
- (E6) C_A recipe (AUDITED only). With `t(X, xi) = eta(X) <xi>^s/(m(X) a_s(X, xi))`, `m = zeta_P sqrt(omega)`,
  `C_A = (2 pi)^{-1} int sup_xi |t^(p, xi)| dp <= (4 pi)^{-1} sup_xi ||(1 - Lap_X)^2 t(., xi)||_{L^1}`, and
  `||h||_{H^s(annulus)} <= C_A ||m A_s h||_2 + ||D_A h||_2` with an order s - 1 remainder D_A. Not evaluated. Pointwise symbol
  negativity is not an operator estimate; remaining order -1 operators need Schur bounds of their kernels; the listed
  floating margins do not determine these constants.
- (E7) Escape weight [checked: the two-pulse example]. With a smooth majorant `f >= 2(E + kappa)^+` vanishing on certified
  neighbourhoods of the equilibria, `phi(X) = int_{-inf}^0 f(Phi_t X) dt` solves `V.grad phi = f` and
  `||phi||_inf <= sup_X int f(Phi_t X) dt`: the positive-part integral, which is NOT bounded by the signed excursion cost
  (7.07 or 7.41 of 3.12; two positive pulses separated by a negative interval have signed cost one pulse). The reflected
  construction `phi(t) = sup_{a <= t} int_a^t 2(E + kappa)` is bounded by the signed cost and satisfies
  `V.grad phi >= 2(E + kappa)` a.e., but is not smooth; its regularization and separatrix compatibility are unproved.
  Lead floating check (01:04Z, runs/bichar_s3.1_a6.25_lw0.5_k0.1.json, 85 orbits): the positive-part integral equals the
  signed cost on every sampled orbit (max 7.40994 vs 7.40993; one positive excursion per orbit), so for this field
  and weight the distinction does not change the number; the cost tends to 3.4392 as theta -> pi/2 (floating A_*).
  Saddle compatibility: if f > 0 somewhere on the heteroclinic x-axis orbit from P to 0, a continuous weight needs
  `phi(0) - phi(P) >= A_* = int_{P -> 0} f dt`, inherited by the trace transported out along the y-axis; independent zero
  normalizations at the equilibria are wrong. Saddle exponent `beta/alpha = 2.098536`: the transported weight
  `F(y (x/eps)^{beta/alpha})` is b-regular (`(x d_x)^j x^p = p^j x^p`) but not `C^3` for generic F (even F: `y^2 x^{4.19707}`).
  Derivative bounds: recursion `A_{iw,beta} = Z_i A_{w,beta} + sum_j (Z_i Phi_t^j) A_{w,beta - e_j}`,
  `||Z_w phi||_inf <= B_w` under the stated integrability; a far modification `(1 - chi(r)) phi + chi(r) A` (A >= sup phi)
  keeps `V.grad phi_new >= 0` where `V.grad r > 0` and f = 0. An X-only weight suffices for the symbol sign; the
  phase-space improvement 40.65 -> 34.30 does not justify phase-space calculus.
- (E8) Assembly [checked: algebra]. From `S <= aF + K_2 O + d R`, `N <= HF + d_o R`, `O <= C_A N + d_A R`,
  `||h||_X <= c_S S + c_N N + d_X R` (F = `||Lh||_Y`, `H = Gamma C_F/kappa_*`, `Gamma = e^{osc phi/2}`):
  `||h||_X <= K F + K' R` with `K = c_S a + (c_N + c_S K_2 C_A) Gamma C_F/kappa_*`,
  `K' = (c_N + c_S K_2 C_A) d_o + c_S (K_2 d_A + d) + d_X`. No denominator `1 - K_2 eps` (triangularity); the large
  lower-order constants move into K'.
- (E9) Non-compact remainder [checked: scaling]. The remainder `R(h) = ||h||_{H_Z^{s-1}(omega_0)} + ||chi_P h||_{H^{s-1}} +
  int_{r > R_*} r^{-3}|h| + |c[h]|` is not compact relative to X: far dilates `h_n = R_n^{gamma' - 1} f(X/R_n)` and y-axis
  translates `h_n = e^{-(a - 1/2) n} f(t - n, y)`, `t = -log x`, keep both norms comparable with disjoint supports.
  Far normal model: `c_l d_t - kappa_inf`, `kappa_inf = 1 - c_l (gamma' - 1) = 0.28078`, inverse norm `<= 3.5615`.
  Completion routes: (i) a low-norm estimate `R(h) <= A' F + eps ||h||_X` with `K' eps < 1`, giving
  `K_H <= (K + K' A')/(1 - K' eps)` (injectivity only; surjectivity separate); (ii) an analytic normal/high-frequency
  parametrix B with certified `||(L - LBL) h||_Y <= d_1 ||h||_X`, `R((I - BL) h) <= d_0 ||h||_X`, `K d_1 + K' d_0 < 1`,
  `K_H <= ||B||/(1 - K d_1 - K' d_0)`, plus `||I - LB|| < 1` or an index statement. A purely finite-rank approximate
  inverse cannot work.
- (E10) Feasibility [checked numbers]. Nominal `K_H = e^{C/2}/0.1 = 342.95` (C = 7.07) or `406.50` (C = 7.41); the closing
  condition `K_L C_B K_H eta < 1` needs `eta < 0.002916`, resp. `0.002460`, at `K_L C_B = 1`; the floating residual 1.2
  (`H^{3.06}`, 0.5-disc) is 412-488 times too large, before the norm conversion `C_res` from the disc norm to Y. An
  `H^{3.06}` bound does not bound `H^{3.1}`. The quadratic term `(U[h] + (c[h]/3) X).grad h` loses one derivative, so a
  same-order bilinear bound `X x X -> Y` does not exist; T2N needs its two norms (section 5) or a tame estimate.
  Parameters: `R_s(0) = R_0 + s D`, `D = 2A + 1`, `R_{3.1}(0) = -3.98231`, critical order 3.28695 (consistent with
  `D = 21.3015`); the x^6 remainder needs `a < 6.5`; `d/d kappa log(e^{C_+/2}/kappa) = T_active - 1/kappa`.
- Lead assessment. escape1 does not change the verdict. It sharpens three points recorded in FINAL_REPORT 5 and 10:
  the remainder realization needs a jet projection and an explicit far strain component (E1, E2), the signed orbit cost
  of 3.12 is not the oscillation of a smooth escape weight (E7), and the remainder is not compact, so the outer estimate
  must close with a low-norm estimate or an analytic parametrix (E9). The quantitative gap (E10) is a factor of about
  400-500 in the residual even with optimistic constants.

### 3.17 Sum-of-squares Garding bound for the coupling (AUDITED astra garding1, single model; lead checked (19)-(23) and the table, the identity behind (3) at the symbol level, the Riesz commutator constants; V24 requested)
- (G1) Identity. For `a = rho~_x`, `c = rho~_y` and the coupling `T v = U[v].grad rho~` written with Riesz transforms R_i,
  `T = b - S + sum [R_i, B_ij] R_j` with `B = [[b + c, -a/2], [-a/2, b]] >= 0` for a majorant b with `b >= b_+`,
  `b_+ = (|grad rho~| - rho~_y)/2` (the largest eigenvalue of the coupling symbol), and `S >= 0`.
- (G2) Bound. `Re <T v, v> <= <b v, v> + C_B ||v||_2 ||v||_{H^{-1}}`, `C_B = 2 (W_1(b + c) + W_1(a) + W_1(b))`, no theta
  dependence. Commutators: `||[R_j, f]||_{L^2 -> L^2} <= 2 W_0(f)`, `||[R_j, f]||_{H^{-1} -> L^2}` and
  `||[R_j, f]||_{L^2 -> H^1} <= 2 W_1(f)`; velocity `||[U_j, f] v||_{H^r} <= 2^{(r+1)/2} W_r(f) ||v||_{H^{r-1}}`.
  At order s: `J^s` conjugation adds `C_J = G_s(a)/2 + G_s(c)`, `G_s(f) = s 2^{s-2}(W_1(f) + W_s(f))`; weighted versions
  and a square partition of unity `sum chi_nu^2 = 1` (garding1 (13)-(18)).
- (G3) Near P [checked]. With `H_delta = sup_{B_{3 delta}(P)} ||D^2 rho~||_op`, `eps_delta = 3 delta H_delta`,
  `b_+ <= F_g(eps_delta)`, `F_g(eps) = eps^2/(4g)` for `eps <= 2g` (since `q(X, n) <= -g t^2 + eps t`, `t = |n_1|`), and the
  direct energy bound `Re <Tv, v> <= -g ||R_1 v||^2 + eps_delta ||R_1 v|| ||v||` (`||U[v]|| = ||R_1 v||`). Table
  (4g = 119): positive coupling `2.0590e-5, 1.8908e-4, 7.5630e-4` times `H_delta^2` at delta = 0.0165, 0.05, 0.1; the linear
  perturbation bound `3 delta H_delta < 3.374` needs `H_delta < 68.16, 22.49, 11.25`. WARNING (exact counterexample): the
  quadratic number cannot be subtracted from a frozen margin that already used `-gM`; that needs an unused directional gap
  `r_frozen(n) <= -3.374 - lambda n_1^2`, after which the bound is `-3.374 + F_lambda(eps_delta)` (lambda = g:
  `H_delta < 404.80, 133.58, 66.79`). The local estimate 3.15 uses the linear form (E = ... + ||q||_inf), which is safe.
  N8 (num, floating; rigorous test at 0.0165) gives `M_rho <= 0.476` at delta = 0.0165, far inside every column.
- (G4) Axis jets. `t_2 = a_2' B - 2 a_2 B'` and `t_4` (garding1 (27)); the axis norm alone does not control the jets
  (dilates `h_R`; outside data have zero collar norm). The remainder is not compact (consistent with 3.16 E9).
- (G5) Oscillation. An oscillation 3.5 of E gives only `E_max/E_min = e^{1.75}` and bounds neither `W_1(E)` nor `W_s(E)`.
- (G6) Strain [checked]. `X.grad rho~ in L^2(r^{-2 gamma'})` iff `gamma' > 1 + k = 1.1794`; at `gamma' = 1.129` it diverges:
  the strain term is not bounded into the remainder space (same as 3.16 E2).
- Lead assessment. garding1 removes the theta loss of the earlier square-root factorization and gives explicit
  Wiener-norm constants; it does not supply W-norms of the actual coefficients (these need Fourier-side enclosures of
  `rho~_x`, `rho~_y` and the majorant on each patch) and does not touch the far or axis realization defects. Changes no
  verdict.

### 3.18 Centre normalization in the weak graph topology (VERIFIED, ver topics 137, 138, 139 conditional; AUDITED astra fr136a, fr136b, fr139a with its required changes adopted)
X = diagnostic weighted H^1 space (C2 Gram, `w = m^{-2}(1+u^2)^{-3/2}`). Under explicit background bounds
(`C^{2,alpha}_loc`, `|grad rho| <= A r^{1+alpha}`, `|D^2 rho| <= A r^alpha` (r <= 1), `D r^{k-1}`, `D r^{k-2}` (r >= 1), V
`C^1` near the unit disc, `V(0) = 0`): compact bumps `h_delta = x^2 y (1 - r^2/delta^2)_+^6` have `J = 1`,
`c = delta^2/56`, graph norm -> 0; `b_delta = (4 h_delta - h_{2 delta})/3` has `J = 1`, `c = 0`. So J levels are
graph-dense (also at fixed strain) and `J = 0` never improves `||h||_X <= C ||Lh||_X` (topic 137). For the exact
modal trial, K = rho~ - X.grad rho~ lies in an explicit graph domain D, `J(K) = -2`, `c[K] = 0`,
`0 < ||LK||_X < inf`, so `C >= ||K||_X/||LK||_X` on `D cap {J = 0, c = 0}` (unevaluated); K has the nonzero
leading far term `(1 - k) r^k Theta` (topic 138). Conditionally on an exact profile with explicit centre and far
derivative bounds, no residual-to-error modulus holds in X alone at fixed J and strain (dilate, then restore J with
`b_delta`; topic 139). Consequence for F-: the scale must be fixed by the tail (section 4, "No J constraint"), or the
norm must control the centre factor (as F- does: "near 0 a factor norm"); a J-normalized weak X formulation is not a
candidate for the a posteriori theorem. The C2 floating sections are diagnostics of the image norm only.

### 3.19 Quadratic term in the weak X norm alone (VERIFIED, ver topic 141; AUDITED astra fr141a with its required changes adopted)
Four concentrating packets `a H((X - p)/epsilon)`, `H(Z) = Z_1^2 Z_2 (1 - |Z|^2)_+^6`, `p = (+-4, +-4)`, `epsilon = 1/n^2`,
`a = 1/n`, plus the fixed compensator `(a epsilon^3/172032) g`, `g = -(56/3)(h_1 - h_2)`, give compact `C^5` densities h_n with
`J = c = 0`, `||h_n||_X -> 0` and `liminf ||W[h_n].grad h_n||_X > 0` (order-zero velocity, `a^2 = epsilon`). So the quadratic
term is not continuous at 0 in X and no `||W[h].grad h||_X <= C ||h||_X^2` holds on any X-ball about 0. Consequence for F-:
the nonlinear step must measure h in the stronger (high) norm of T2N (section 5; FR section 7), with the quadratic term
controlled by the high norm as there; a closure with X as the only perturbation norm is excluded. Not covered: stronger or graph norms for h, weaker
image norms, finite-dimensional classes.

## 4. Target formulation F- (CONDITIONAL; the a posteriori theorem we would prove if the inverse were available)
- Ansatz `rho = rho~_{k', tau} + h`, where `rho~_{k',tau}` replaces the trial's tail `r^k Theta_0~` by
  `r^{k'} (Theta_0~ + tau Theta_1)` outside a fixed radius (smooth cutoff), `Theta_1` a fixed admissible angular
  profile (odd about theta = 0, vanishing at theta = pi/2). Unknowns `(h, k', tau)`.
- Spaces (v3.1: concrete proposal in notes/conormal_framework.md section 2.3): h has allowed growth
  `gamma_E < k - margin` at infinity; near P `H^{s_H}`, `3 < s_H < 3.406` (high) and
  `H^{s_H - 1}` (low); along the stable segment a conormal space carrying `x^{2j} |y|^{beta_j}`, j >= 3, with the
  `beta_2` coefficient absent; near 0 a factor norm with positive-power remainder (index1: continuous-factor centre
  norms admit infinite cokernels from log forcings); high regularity in the exit region near the y-axis (so exit traces
  are smooth enough for the one-scalar saddle count). Forcing: `Y_- (+) R`, the scalar being the coefficient of the
  `r^{k'} Theta` term (it equals `(c_l[rho] k' - 1)` times the tail amplitude).
- No J constraint (the tail amplitude fixes the scale); after solving, rescale by `a = J^{1/2}` to normalize.
  v3.41: 3.18 shows that J = 0 in a weak graph topology does not fix the scale (topics 137-139).
- Formal count: R- transport injective; source 0 (frozen bijective below `s_fast`); saddle -1; `(k', far scalar)` 0;
  `tau` +1. Index 0 if the saddle functional is nonzero on the `tau`-direction. Unproved: the global Fredholm estimate
  (source localization, saddle transmission, nonlocal tails, compactness at infinity; realize1 C6) and K_H, K_L.
- T2N then applies on this complement (the inverse is unique on the chosen complement, so the identity
  `R_h - R_h' = -R_h (A_h - A_h') R_h'` used in T2N holds).
- Alternative R+ (+) span(eta) (one singular source mode): index 0 iff `l(L eta) != 0` (index1), but the nonlinear term
  `(Gamma eta).grad eta` is not in a high forcing space and moving layers are not differentiable in fixed
  `C^{2,alpha}`; not pursued. v3.7: at the frozen level one singular mode does not suffice (the cusp profile `F_f` is
  a function, pcusp1 C2), so this alternative is also unsupported as an index-0 realization.

## 5. T2N (VERIFIED as a conditional theorem, ver two_norm_scheme)
`A_h u = L u + (Gamma h).grad u`, `B(e, u) = (Gamma e).grad u`. Hypotheses: `||R_h f||_X <= K_H ||f||_{Y_H}`;
`||u||_E <= K_L ||A_h u||_{Y_L}`; `||B(e,u)||_{Y_L} <= C_B ||e||_E ||u||_X`; `||Gamma h||_V <= C_V ||h||_X`; ball closed in
E. Closing: `K_H eta <= r`, `K_L C_B K_H eta < 1`, `C_V r <= r_V`. Conclusion: unique h in the ball, `||h||_X <= K_H eta`,
`F(rho~ + h) = 0`. In F- the scalar unknowns `(k', tau)` are adjoined to X and E and the far scalar to Y.

## 6. Owners and tasks

### 6.1 num (priority order)
N1' (v3.9, priority below chains 4/5) certified bounded-region flow inequalities of 3.9 (src/cert_flow.py, chainN1):
    `T_0 <= -0.22` off the box, box inequalities, root of w with `w' > 0`; also `sup |rho~(0,y)|/y` (floating).
    Status 2026-10-21T11:46Z: ver topic 93 (radial Taylor models, middle cells 0, 4102, 7808, all 261 modes) and topic 125
    (composition into s, v_2, v_1, T on nine rectangles of those cells, two methods; CONFIRMED finite, conditional on
    the topic 73/93/75 input boxes) in FR 5(l), sections 4 and 8; canonical membership, other cells, full flow OPEN.
    Status 2026-10-22T00:42Z: ver 162 FINAL (finite-input radial Taylor models on all 7809 middle cells, all 261 modes) and
    167 FINAL (canonical meaning on every closed middle cell, via 173 Green boundary and 99 density memberships), with
    175 (canonical flow ranges on the nine rectangles): FR fr182/fr183 (5(l), sections 3, 4, 8). OPEN: angular linkage
    beyond the nine rectangles, angular products, box classification, flow inequalities on e^{t_a} < r < e^{t_b+5}.
    Status 2026-10-21T11:54Z: ver topic 126 (analytic, tau >= 5): T < -0.22, s, v_i > 5.57 on r >= e^{t_b+5} (R < 510000); FR
    11:53Z after astra fr126a; uncovered annulus of the flow hypotheses now e^{t_a} < r < e^{t_b+5}.
N7  centre-regular variant of the trial (floating first; v3.10: remove r^{2j} cos(2 m theta), m > j, j <= 4, needed by
    D_b, 3.12); if it exists, centre Taylor data of w up to x^9. Cost estimate first. P-disc refit (chainR) for H^{3.06}.
R0  Rigorous weighted residual by region (num middle rerun DONE in chain5, 10-20 22:54-23:38Z, sup W/m <= 2.5964e-4, not
    independently accepted; FR section 6 compares the verified cell bounds only with the historical num output; the verifier's independent full middle
    pass is complete with one method, VERIFIED inner/exterior; whole-plane `N_0 < 1.904e-3`, FINAL_REPORT 6; joining of
    the three regions CONFIRMED by ver topic 124, 11:16Z, PRIMARY middle input only; FR 6 item stays provisional). Report `sup W/m`, the shell values, and
    `sup W/[m (1+u)^{gamma_Y - k}]` for `gamma_Y = 0` and `gamma_Y = k - 1/2` (the current multiplier `(1+u)^{1/2}`).
R1  `r^j grad^j eps~`, j = 1, 2 globally; R3 Taylor bounds of eps~ to order 4 on the disc `|X - P| < x_*/4`.
    Status 2026-10-21T11:05Z: num chain6 COMPLETE (NUM_REPORT 7.3b): on `5.155e-5 <= r <= 8.228e10`
    `r |grad eps~|/m <= 0.4195`, `r^2 |partial^2 eps~|/m <= 713.2` (any second partial; largest at the lobe next to
    P), both tails not covered; NOT verified; FR section 6 and section 10 item 4 quote them as unverified (notes/fr_c6).
    2026-10-21T14:54Z: ver topic 142 CONFIRMED the finite aggregation only (all 19389 saved rows, exact rational, max A < 0.4195,
    max B < 713.2, B bounds each Cartesian second partial, not Frobenius; conditional on valid cell majorants, weight lower
    bound, coverage); physical bounds still NOT verified; FR via notes/fr142. R5: num's 0.427 is inward of its own saved
    majorant maximum (in (0.427, 0.427444)); not cited in the FR.
    2026-10-22T00:42Z: ver 143 (13 points) and 144/145 (63 majorants verified on cells 4102, 4125, 4211) no longer carry the
    inherited centre-moment condition (ver 174 second integration, FINAL 00:23Z); ver 163 + 178 give the full-plane
    X bounds 0.385656000027 / 585.874000000002 conditional only on the 19389 annular majorants; ver 179 (direct full
    derivative X norm) v2 running. FR fr182/fr183.
    2026-10-22T01:30Z: 178 inherits the velocity constants C_r, C_theta of the earlier analytic inner majorant (T=0
    row) and the coefficient bounds C_(gamma,l) of the earlier coarse exterior majorant, not the cell certificates;
    FR provenance corrected (fr186, fr186b). Ver 179 v2 full run at cell 939/7809 (01:27Z), computation ends about
    07:45Z; its integration is prepared (notes/fr187), scope: coarse direct whole-plane X bounds, exterior-dominated,
    no annular majorant discharged.
R5  `||eps~ - X.grad eps~||` and `||K~||` in the R0/R1 norms (for 3.8).
N8  (v3.17) certified (Arb) sup bounds on `B_{3 delta}(P)` of `||D^j V||_F`, `j <= 4`, and `||D^j rho~||_F`, `j <= 5`, for
    `delta in {0.0165, 0.05, 0.1, 0.2}` (floating first); report `M_V`, `M_rho` and `C_V = 41.7 M_V + 3 M_rho`
    against `kappa/(2 delta)` (3.15 S2, S4); also the floating `||tau eps~||_{H^{3.1}}` with tau = 1 on `B_{7 delta/4}`,
    support in `B_{9 delta/4}`, for the same delta. Status 01:07Z: floating DONE, interval fine pass at 0.0165 reported
    (`C_V <= 13.34`); ver asks to suppress or mark the fine-output rows for larger delta (incomplete radial coverage)
    and to close the cell-width and distance-filter rounding points. Status 01:17Z: v2 addresses all three, reruns
    running (3.15); re-audit by ver needed.
RES Three resolutions (variants v3, v4, v5) through the same pipeline (section 6 of the report needs >= 3).
C2  (floating point, after R0) unchanged from v2: finite sections of L, two smallest singular values; add the F-
    columns (k', tau) if feasible.
    Status 2026-10-21T11:46Z: num chain8d (NUM_REPORT 7.4b, floating) M16/s16 conditioned section at ppc 2/4/6: H1m sigma_min
    0.1208/0.1698/0.2067 (C^0), per sqrt(rows) stable within 9 percent, no J or tail content; in FR section 10 next
    step 1. M24/s8 pending.
    Status 2026-10-21T12:07Z: ver topic 127: the raw J and J_inner references are not in the H1m space (their cosines are
    piecewise-gradient correlations) and a(0) is unbounded in H1m; FR section 10 next step 1 after astra fr127a.
N10 (v3.35, low priority, foreground) reproduce the lead's floating decomposition of the localized forcing at P
    (lead code/forcing_cutoff.py, NOTES 04:57Z): at delta = 0.0165, ||tau eps~||_{H^3.1} 1.55 (two grids), of which
    tau times a degree-5 least-squares polynomial model of eps~ (odd in y) gives 1.56 and the remainder 0.61;
    ||tau||_{H^3.1} 7.7e6, sup |tau eps~| 3.3e-7; Gaussian window sigma = 0.01: 0.029; delta 0.033 / 0.066: 1.67 / 0.87.
    Lead reading: at delta = 0.0165 the localized norm is the cutoff transition acting on the smooth part of eps~, not
    knot-scale structure (the 0.5-disc attribution is unaffected). FR section 10 item 4 states both (04:57Z).
    ANSWERED (num 05:09Z, own code src/forcing_decomp.py): 1.5521 / 1.5587 / 0.6138 / 0.02878 reproduced at
    delta = 0.0165; 0.5-disc decomposition: model 0.0143 of 1.4526. Astra frmid5: the ratio and the non-orthogonal
    model/remainder split do not determine the origin; FR wording is "consistent with a substantial contribution from
    the localization" (notes/fr0520).

### 6.2 ver
V1  Independent reproduction of S1 and R0 (ongoing).
V3' Audit of 3.7 (the realization table and the mixed-class formal kernel claim) and of the F- count in section 4;
    counterexamples welcome. (index1 and realize1 were single-model audits: Opus unavailable for both.)
V6  Audit of notes/conormal_framework.md (revision 2) sections 1.2, 1.3, 1.4, 2.1, 2.4 (exact local lemmas) and, with
    interval arithmetic where cheap, the axis facts of 4.1 (D1): `mu > 0` on the x-axis, `V_2(0,y) > 0`, a single zero
    of `w` on `(0, inf)`. Your axis-velocity machinery covers points; a full-axis statement needs a covering argument
    and the far-field expansion.
V7  Audit of notes/weighted_velocity.md revision 2 (Lemmas W1, W1': Taylor-modified velocity bounded on `L^2(|y|^{-2b})`,
    `N - 1/2 < b < N + 1/2`, explicit constants; edge coefficients in `dot H^{b-j-1/2}`). Elementary (partial Fourier,
    dilation, Hilbert-Schmidt/Schur); a rigorous evaluation of the constants `C_{3,b}`, `C'_{3,b}` is cheap.
V12 (v3.8: REVISION 2 of notes/yface_collar.md, 18:56Z) Audit: Lemma S (swap), the reduction of NF-Y to collar_coupling
    rev 2, the full-jet multiplier bounds of E-Y (E2-Y), the localized decomposition (1.2), the exact remainder (5.2) and
    the ranges (5.4). Do not use code/check_yface.py (2) as an accuracy check (its smoothing-jet quadrature is wrong by
    three orders, see rev 2 section 7).
V13 (v3.7) Independent check of the frozen cusp theorem of astra pcusp1 (3.3 C1-C3, C5): the conjugation, the
    exponents `s_fast, s_1, alpha_*, g/A`, the explicit `F_f != 0` example, the counterexample to the `f_y(P)` cokernel.
V14 (v3.8: notes/corner_coupling.md now exists, 18:59Z) Check of Lemma D (double remainder window, section 2), the
    trace criterion (T1) with its table and (T3) resonance, (K3), and section 5 (`J_c = 0`, `K_c`, `q_1, q_2, q_4`, the
    unit-box bound of `f_rem`, the degree-7 obstruction); code/corner/check_corner1.py, check_corner_q.py.
V16 (v3.9) J3-J7 of notes/global_flow.md section 12 and notes/pinf_B3.md sections 1-2 (A1, A3, A5, B1, B2, B4, B5),
    sanity check of C1. Topics 50-57 done (V14 = topics 51, 55-57; V15 = topics 52-54); middle second method running.
V17 (v3.10) astra prow1: (45)-(47) incl. the existence argument of (47); (1) with its regularity hypotheses;
    (31)-(33); (18), (21) (lowest).
V18 (v3.11) astra dib1 (astra/dib1/answer.md): (14)-(18) far exclusion and the c[h] obstruction; (23) `[x^2 y] L h = 0`;
    the identities (1), (8); (28)-(30) jet matching, jet rates, K not in the far space. Priority below V16(b), V17.
V19 (v3.12, low priority) elementary items of astra dib2 (SPEC 3.12 D1-D10; list in NOTES_FOR_TEAM 22:03Z).
V20 (v3.13, low priority) elementary items of astra dib3 (3.13 B1-B10): the H_n recurrence and `-Lap L_P H_n = 0`,
    the c[e_eps] scaling, `mu_P = 1` from C^1, the factorization example, the interpolation constant 1.
V21 (v3.16) astra holder1 (3.14 H1-H6): the dyadic upper bound, packet sharpness, the two order-1 logarithms.
V22 (v3.17) frrev1 corrections now in FINAL_REPORT: (a) the trial-centred jet exclusion of section 7 (identity S7, the
    bound `|d_y F(rho~ + h)(P) - (mu~ - 1) g| <= C delta + 2 delta^2` in the four jet quantities and the radius about
    2.2e-8); (b) the normalized face-coupling coefficient `(2/3) c (2 G_1 - x G_1')` of 5(f); (c) the Dini non-necessity
    example; (d) `s_fast = 3.57855` wherever a threshold is stated. (a)-(c) CONFIRMED ver topic 76 (00:24Z), with
    `30.0229 < C < 30.0230` (the bound with 30.0229 refuted), `2 g - x_* g' > 57.1`; in FINAL_REPORT 00:32Z.
V21 CONFIRMED ver topic 74 (00:03Z) for the frozen model; in FINAL_REPORT 00:14Z.
V23 (v3.17) astra srcloc1 (3.15): CONFIRMED ver topic 77 (00:41:39Z); auxiliary inverse CONFIRMED topic 78 (00:46:04Z);
    strain sign correction CONFIRMED topic 80 (00:56Z). All in FINAL_REPORT 5(o) (01:01Z, 01:07Z).
V26 (v3.19) N8 interval bounds (num cert_n8): ver topic 82 CONFIRMED limited scope (01:10Z: exact implications to
    `E`, `K_1`; v1 larger-delta rows refuted as disc bounds); the coefficient suprema stay OPEN; re-audit on num's v2
    outputs (due about 01:30Z). In FINAL_REPORT 5(o), sections 3 and 8 (01:17Z). CLOSED independently: ver items 84,
    85 (M_rho < 0.5059, M_V < 0.2972) and topic 86 (C_V < 13.91094, E < 0.22953051, K_1 < 0.3181 at delta = 0.0165);
    FR 5(o), timeline 01:44/01:52, section 8 (02:02Z). Num's tighter N8 v2 suprema remain OPEN (not needed).
Ver topics outside the task list (in FINAL_REPORT 01:07Z): 79 (N7: density C^12 not C^13, factor C^9 not C^10, first
    non-polynomial homogeneity 13, normalized residual likewise; exact exterior velocity identity with the first
    trial REFUTED, frequency 522; N7 residual bounds OPEN); 81 (radial ODE defect criterion for the modal Green
    equations, abstract; actual anchors and defects OPEN).
V24 (v3.19, low priority) astra garding1 (3.17): identity (6) and the commutator bounds (3)-(5) with their symbol
    inequality (4); C_B of (7); (20)-(23) with the counterexample to subtracting the quadratic number; (26)-(27) jets;
    the strain threshold (G6). CONFIRMED ver topic 87 (01:49Z) under stated global hypotheses (square identity, first
    and second commutator bounds, fractional conjugation, source symbol and localized L2 bounds, the double-counting
    counterexample, unused directional gap 449/1000 in the 3.15 box); OPEN: actual global Wiener constants, global
    positive coefficient extension, weighted fractional errors, axis jets, far block, invertibility. In FR section 10
    item 1 and section 8.
V25 (v3.19, low priority) astra escape1 (3.16): E1 jet expansion, E2 far threshold and the log identity, E3 cutoff sign
    under `||DV - DV(P)|| <= mu_P/2`, E4 commutator constants, E5 c[h] bound, E7 two-pulse example and saddle
    compatibility, E9 non-compactness sequences. CONFIRMED conditional ver topic 88 (02:04Z; SPEC v3.22 raw-c E2
    correct; E5 repaired in v3.24). Earlier progress note (01:52Z): E2 coefficient agreed in the prompt
    convention (-c'/c_l^2 = -sigma/(3 c_l^2)); C_sigma in (0.0078147, 0.0078149), C_c < 0.002605; ver notes that
    h(0) = 0 alone does not remove the local strain derivative (needs h_y(0) = 0); E3 perturbation part
    `||DV - DV(P)||_op < 0.0147114` on B_0.0495(P) from topic 85.
V27 (v3.22) jet-exclusion strain arithmetic for X3 - trial (NOTES 01:51Z): VERIFIED ver topic 90 (02:13Z):
    -2.95309e-8 < p c[h]/3 < -2.95294e-8 (raw c, trial source p); W[h]_1(P) = U_1[h](P) + p c[h]/3 with U_1 unevaluated,
    so no jet-ball membership or nonmembership; rests on the one rigorous whole-integral summation of c[X3] (no second
    one). In FR section 7, section 4 list, section 8 (02:23Z).
V28 (v3.22) semigroup decay implies the stationary inverse (NOTES 01:53Z): VERIFIED ver topic 91 (02:13Z), with the
    scope correction "a route BASED ON exponential decay must prove it; not every dynamic method". FR section 10 item 1
    bullet "Dynamic rescaling" (02:23Z).
V29 (v3.22, optional) local source constants for s in [3.05, 3.1]: VERIFIED ver topic 92 (02:22Z): kappa(s) =
    1301/200 - (101/100) s, C_src(s) = (12 s + 4.5) M_V + 3 M_rho (C_theta <= 2); whole interval K_1 < 0.3181,
    d >= 3.0705; s = 3.06: K_1 < 0.313753. Auxiliary inverse norm contains unevaluated R_s. FR 5(o) bullet "Order
    family", timeline, section 4, section 8 (02:41Z).
V30 (v3.27) source shift lemma notes/source_shift/LEMMA.md (S0-S5; lead derivation): VERIFIED ver topic 94 (02:34Z;
    one printed mu-margin correction, already applied); astra srcshift1 and srcshift2 audits: no issue, scope
    qualifications applied (LEMMA r3, 02:39Z). Location |p_h - p| <= eps_0/m, m > 10.1360138 for R < 0.0495; source
    data and box margins; mu_h = 1 at an exact solution gives the moving-source lower bound eps_0, eps_2 > 2.1886e-8
    (too narrow, not an endpoint); S5 transported local K_1 <= 0.40709660 (m_2 <= 1), <= 0.56549268 (m_2 <= 2) at
    delta' <= delta_h. FR 5(o) bullet "Perturbed profiles and the moving source", section 7 paragraph "Moving-source
    form", section 4, section 8, section 10 K_H line, timeline (02:41Z).
    GAP (astra frmid3, 03:30Z, accepted): S5 assumes W[h] in C^4 on B_0.0495(P); the proposed H^{3.06} correction ball
    gives W[h] only in C^{2,alpha}, alpha < 0.06. So K_1 uniformity holds on the admissible C^4 family, not yet on the
    correction ball; needs a rough-coefficient extension (or a smoother correction space). In FR 5(o), K_H line, item 4.
V31 (v3.29) dilation corollary of the auxiliary inverse (topic 78; NOTES 02:52Z; astra dilation1): (D_ell u)(Y) =
    u(P + ell Y) conjugates A_op to the same form with w~ = w(P + ell Y)/ell, q~ = q(P + ell Y), same E and d; so
    ||A_op^{-1}||_{N_{1/ell}} <= (1 + R~/d)^s/(kappa - E), N_lam(u)^2 = int (lam^2 + |xi|^2)^s |u^|^2, and
    ||A_op^{-1}||_{H^s} <= ell^{-s} times that. Floating (code/aux_R_scaled.py): R~ about 22.6 (ell = delta = 0.0165),
    5.4 (ell = 0.0035); bounds about 190, 6.4; best H^3.1 bound about 5.5e7 (ell = 0.01). In FR section 10 item 4 as
    "an elementary corollary, not yet verified". N9 (num): R, R~ and the forcing reproduced by num's own code (TO_TEAM
    02:52Z, 02:56Z; floating; N9 closed 03:06Z).
    Lead forcing (03:00Z, code/aux_R_scaled.py, N = 256 and 512 agree): N_{1/ell}(tau eps~) about 1.56-1.60 for
    ell >= 0.007, 1.65 (0.005), 1.80 (0.0035); H^3.1 value 1.5576 (num 1.56, same sampled fields). Product bound x
    forcing about 291 (ell = delta), 55 (0.01), minimum about 11.4 (0.0035); 2.9e12 unscaled. In FR item 4 (03:04Z).
    VERIFIED: ver topic 96 (03:03Z, CONFIRMED all (a)-(e) for each s in [3.05, 3.1]; same E, a_s = kappa(s) - E, d
    exactly; maximal domains correspond; no support-size condition; floating R~ not certified). In FR 5(o) bullet
    "Isotropic dilation", section 4, 8, timeline 03:03, item 4 relabelled (03:09Z).
V32 (v3.30, proposal to ver after V31) certified scaled auxiliary bound: apply the V31 dilation to the topic 95
    machinery (explicit C^4 cutoff, Frobenius ceilings of D^3-D^5 rho and D^3-D^4 U) at ell = delta and one or two
    smaller ell, giving a certified bound of ||A_op^{-1}|| in N_{1/ell}. Topic 95 (02:55Z, VERIFIED): unscaled
    ||A_s^{-1}||_{H^s} < 1.2e35 for s in [3.05, 3.1] (2.672e34, 3.518e34, 1.068e35 at 3.05, 3.06, 3.1); in FR 5(o)
    bullet "Explicit auxiliary inverse bound", section 4, 8, 10 item 4, timeline 02:55 (03:04Z). Not a closing constant.
    Ver queued topic 97 (03:03Z): sharpen the topic 95 cutoff derivative constants by exact radial integrals and apply
    the dilation (short rational arithmetic, alongside the middle run); this is V32.
    VERIFIED: ver topic 97 (verdict 03:18Z, note 03:19Z, CONFIRMED; exact weighted radial tensor integrals of the
    cutoff, imported derivative ceilings, V31 dilation; two methods + output audit + strict non-finite guard).
    Same topic 95 C^4 cutoff (support the CLOSED ball of radius 23 delta/8, inside open B_{3 delta}; fields C_c^4).
    s = 3.1: ell = delta R* < 679.382, N bound < 5.7e6; ell = 7/2000 R* < 48.225, < 1874; ell = 1/500 R* < 29.812,
    < 473. N_500: < 608 (3.05), < 554 (3.06), < 473 (3.1), < 922 uniformly on [3.05, 3.1]. H^s: < 5.743e10 (3.06,
    ell = 3/1000), < 6.968e10 (3.1, ell = 11/4000), < 1.223e11 uniformly (ell = 3/1000). Finite list of scales, upper
    bounds only; no rank-one term, outer matching, residual. Not to be compared term by term with the floating
    smooth-cutoff numbers (R~ 22.6 at delta). In FR 5(o) "Isotropic dilation" and "Explicit auxiliary inverse bound",
    trial-instance regularity wording, sections 4, 8, 10 item 4, timeline 03:18 (notes/fr0326/apply.py).
V33 (v3.33; VERIFIED 04:16Z, ver topic 100, FINAL CONFIRMED conditional, verdict SHA a4d8ef26...) rough-coefficient extension
    (notes/rough_coeff/LEMMA.md r2, lead derivation; astra rough1 audit applied): L1 product bound
    ||fg||_{H^r} <= 2^{r-1}(||f||_{H^r} W_0(g) + W_0(f) ||g||_{H^r}) and W_0 <= alpha_r H^r (r > 1),
    W_1 <= alpha_{r-1} H^r (r > 2). L2: the topic 78 auxiliary inverse at order s holds for w in H^sigma, q in
    H^sigma (sigma >= s, sigma > 3; compact support), by mollification, weak limits and an L^2 dissipativity
    injectivity argument. L3: the topic 77 local estimate holds for V = V_0 + W, V_0 in C^4, W in H^sigma, with e_A
    replaced by e_A' = sum_i 2^{t-1}(alpha_t ||pcut V_i||_{H^t} + W_0(pcut V_i)) (e_A enters only in (25)); proved
    for smooth admissible h, extended by completion. L5 (r3/r4, astra rough2: argument valid, scope sharpened): the
    completion contains every h in H^s(R^2) with h(0) = grad h(0) = 0 and L h in H^s on a neighbourhood of supp tau
    (Friedrichs commutator [V~.grad, j_eps] uniformly bounded on H^s for V~_i in H^s with W_1 finite). L4: S5 with
    h in H^{3.06} instead of W[h] in C^4 (same K_1 ceilings at s = 3.06 under the same budgets). Would close the C^4
    GAP above for the K_1 statement on that class; the scheme still needs R_h f in X and A_h R_h f = f (not supplied).
    r5 (after ver's preliminary findings 03:59Z): N is the full topic 77 (15) quantity including the origin term
    int_{R^2 \ B_3delta(P)} |h|/|X|^3, continuous only on the zero-jet subspace (N <= [2 sqrt(pi)/(5 delta) + pi gamma_s
    + sqrt(pi/2)] ||.||_{H^s}); approximants are compared in N only with exact zero jets. L3 uses the actual E (the
    identity div V = A + mu enters topic 77 only via the budget (13)); for V_0 + W[h] the divergence is constant, so the
    identity holds at the source. Ver topic 100 (04:16Z) CONFIRMED all of V33 (a)-(e) in its reconstructed scope:
    auxiliary inverse for compact H^sigma coefficients (existence and uniqueness on the maximal domain, any base point);
    local estimate with actual E for V_0 (C^4) + W (H^sigma loc), fixed C^5 density, only e_A in K_2 changed; explicit
    budgets need div V = A + mu; completion contains global H^s zero-jet u with tau' L u in H^s near supp tau, with
    N(f) <= [2 sqrt(pi)/(5 delta) + pi R gamma_s + sqrt(pi/2) R^{-2}] ||f||_{H^s} (every R > 0, zero-jet f only);
    topic 94 K_1 ceilings valid at 3.06 under the same source/box/divergence/Hessian budgets; global H^s Hessian
    constant gamma_s = [2 pi (s-1)(s-2)(s-3)]^{-1/2}; rough dilation. Not: uniform K_2-K_4/R, rough semigroup,
    weighted completion, physical inverse, residual, contraction. r3 intermediate N claims REFUTED (odd cubic).
    In FR (notes/fr0430): 5(o) "Rough coefficients" bullet and the transported-estimate sentence, sections 4, 8
    (rederived; resolved objection), 10 (K_H line, item 4 uniformity clause), timeline 04:16.
V34 (v3.34; VERIFIED = ver topic 102 FINAL CONFIRMED 2026-10-21T05:09:57Z, 80 pins, two scalar engines, output audit;
    strict delta_h < 33/2000 refuted (equality at h = 0; LEMMA r4 2026-10-21T04:58Z, repairs agree); the r3 inference
    from the radius/supremum comparison rejected; ver's K_1 value 0.32123200 (a hand-rounded 0.32123 is false); in FR
    2026-10-21T05:23Z (notes/fr0530: 5(o) bullet "Whole-plane Sobolev ball", transported-estimate sentence, sections 4, 7, 8,
    10 K_H line, item 4, item 5, timeline 05:09)) whole-plane Sobolev
    ball for the moving-source hypotheses (notes/sobolev_box/LEMMA.md r4, code/sobolev_box.py; astra sobbox1 04:30Z applied: numbers correct, |x| bound and
    threshold quotient restated, code xmax made rigorous, u/h distinguished). For
    3 < s <= 31/10, h in H^s(R^2) real, even in x, odd in y (unitary FT): sup|U_1| <= (32 pi (s-1))^{-1/2} ||h||,
    |c[h]|, sup|d_1 U_1|, sup|d_2 U_2| <= C_c ||h||, C_c = (64 pi (s-1)(s-2))^{-1/2}, sup|h_y| <= (8 pi (s-1)(s-2))^{-1/2}
    ||h||, sup||D^2 U||_F <= (4 pi (s-1)(s-2)(s-3))^{-1/2} ||h|| (angular averages 1/8, 1/16, 1/2, 1/2; radial integral
    pi j! Gamma(s-j-1)/Gamma(s)). At s = 153/50: eps_0 <= 0.20709004 ||h|| (|x| < 8.64956381), eps_{1,2} <= 0.06363372 ||h||,
    (B1) coefficient 0.06970585 (radius threshold > 0.14345856), (B2) 0.10152270, (B3, S5 form) 0.01033610. On
    ||h||_{H^{3.06}} <= 7/50, R_I = 49/1000: S1(b), (c) hold, d_h < 0.00286036, delta_h > 0.01554654, m_2 <= 0.10910910,
    and with V33 K_1 < 0.32123200 uniformly for every delta' <= min(delta_h, 33/2000) (E < 0.30138506,
    kappa(3.06) = 3.4144). Uniformity of K_1 only; whole-plane H^s only (no weighted embedding); not a closing radius.
    (e) (r3): no exact solution rho~ + h with ||h||_{H^{3.06}} <= 3.2318e-7 (S3 with (B1)); about the trial only, not X3;
    too narrow, disclosed only, never an endpoint; the radius/supremum comparison is a judgement, not a proof.
    Num floating four jets of h = X3 - trial at P (num TO_TEAM 02:02Z, grids 6000x256 and 12000x512, NOT certified):
    c[h] raw -1.0301e-8 (matches the certified enclosure to 5 digits), z = h_y(P) about -5.6e-9, v = h_xy(P) below 4e-10
    (unresolved), u = W[h]_1(P) about 1.58e-8, w = d_y W[h]_2(P) about -1.3e-9. So X3 plausibly lies inside the 2.2e-8
    four-jet ball; a certified version would exclude exact solutions only within about 6e-9 of X3 in these jets
    (FR section 7 says this; still a formal, too-narrow exclusion, not a decisive endpoint). Low priority.
V35 (v3.37; verifier-originated; VERIFIED = ver topic 103 FINAL 2026-10-21T05:22:11Z, 44 pins, two interval engines,
    exact audit of the coefficient files) Leading-tail separation: uniformly in angle r^{-k} X3 -> Theta_X and
    r^{-k} rho~ -> Theta_M; Theta_X = L^{3-k} cos^2 sin exp(B + D |cos|^{p-2} sin^2), D = T(1) > 0, 6 < p < 7, not C^7 at
    the y-axis; Theta_M a trigonometric polynomial; Theta_X - Theta_M at pi/4 in (8.2716924477e-10, 8.2716924478e-10).
    Hence X3 - rho~ in L^2((1+r^2)^{-gamma}) iff gamma > 1 + k; in no H^s(R^2), s >= 0. Consequence: the V34 balls do
    not contain X3. Distance statement only, no exclusion. Lead astra farprof1 (proof and FR wording) launched
    2026-10-21T05:38Z, collected 05:43Z (proof correct; wording repairs); in FR 2026-10-21T05:45Z (notes/fr0550).
    Ver topic 104 (preliminary, 05:31Z): no stationary canonical correction rho~ + h with h in L^2 for any finite c
    (nonzero far residual coefficient of sin theta e^{(2k-1) tau}, in (-2.000282880e-4, -2.000282879e-4)); by V35 this
    class does not contain X3 and has empty interior in the weighted factor topology: not a decisive NO. Into FR only
    when FINAL, as a disclosed obstruction for the affine L^2 class.
V36 (v3.38; VERIFIED = ver topic 104 FINAL 2026-10-21T05:37:55Z, 65 pins, and topic 105 FINAL 05:53:35Z, 98 pins;
    both two interval engines, exact output audit, proof plus mandatory addendum) (a) Topic 104: eps~ = r^{2k-1} Eps +
    o(r^{2k-1}) uniformly, Eps_1 (sin theta coefficient) in (-0.03688201144, -0.03688201143); no stationary rho~ + h,
    h in L^2, any c, in the class: locally regular, parities, ||U||_{L^2(B_S)} = o(S^2) (includes P_2); eps~ in
    L^2(<r>^{-2 beta}) iff beta > 2k. (b) Topic 105: exactly normalized tail repairs rho_T (T >= max(R_b, L, 1)),
    kinematic P_2, F(rho_T) in L^2 (norm unquantified), rho_T - rho~ not in L^2, factor distance < 0.334616 T^{k-1};
    leading r^k profile unchanged. Neither is decisive. In FR 2026-10-21T06:02Z (notes/fr0610: sections 1, 2, 3, 4,
    6, 7 "Affine L^2 class", 8, 10 items 4, 5). Lead astra farres1 (proof outline, corollary, wording) launched 06:02Z.
    Open, asked of ver 06:00Z: (c) corollary eps~ not in dot H^{-1}(R^2) by the unscaled ring test (PROMPT audit
    item; FR section 6 sentence only after ver and farres1); (d) is kinematic P_2 membership of rho~ itself verified
    (which topic)? Astra farres1 collected 06:11Z (claims A, C correct; B correct given ver's A4 remainder), wording
    repairs in FR 06:12Z (notes/fr0615, fr0615b). Asked of ver 06:13Z: (c) also not in inhomogeneous H^{-1};
    (e) ||F(rho_T)||_{L^2} >= c T^{2k} for large T; (f) X3 - rho_T in L^2(<r>^{-2 sigma}) exactly for sigma > 1 + k.
    Ver 06:27Z: (d) answered by topic 15 (modal_repair admissibility; FR section 2, notes/fr0635); topic 108
    preliminary (not FINAL): (a, c, e, e', f) reconstructed, C_L > 0.03135338258 (L^2 and H^{-1}, both repairs),
    C_D > 0.0022215507882 (dot H^{-1}, 106), asymptotic only. Topic 108 FINAL 06:32:13Z (207 pins): VERIFIED; in FR
    2026-10-21T06:34Z (notes/fr108: sections 2, 3, 6, 10 item 4). (g) = ver topic 109 (D_d row nonzero), OPEN pending review.
V37 (v3.39; VERIFIED = ver topic 106 CONFIRMED 2026-10-21T06:04:05Z, 146 pins; two independent readings of the
    binary64 input, exact nonresonance and identity checks, independent output audit, proof plus mandatory addendum)
    Higher tail repairs rho'_T: counterterms chi(r/T) r^{a_i} H_i at a1 = 2k-1 (H1 as in 105), a2 = 3k-2, d = k-2
    (Hd = -Dd) and exact strain compensator; kinematic P_2, c_l = 1/k, density unchanged on r <= T; residual
    eps_T = O(r^{4k-3} (1 + log r)^{12}) for fixed T, 4k - 3 < -2 (k < 1/4), so ||eps_T||_{dot H^{-1}} <=
    ||r eps_T||_2 < infinity (angular primitive), eps_T in L^1 with zero integral; factor distance <= C_1 T^{k-1} +
    C_2 T^{2k-2} + C_d T^{-2}, C_1 < 0.334616, C_2, C_d unevaluated; rho'_T - rho_T in L^2; X.grad rho'_T not in
    dot H^{-1}; sufficiency only (a2, d rows of rho_T not shown nonzero). No norm ceiling; not decisive. In FR
    2026-10-21T06:17Z (notes/fr0620: sections 3, 4, 6, 8, 10 item 4). Lead astra farres2 (audit of C1-C7 and the FR
    texts) launched 06:18Z, collected 06:26Z (C1-C7 valid; wording repairs in FR 06:27Z, notes/fr0630). Open: a
    quantitative bound of eps_T in a forcing norm with an available linear inverse; asked of ver 06:28Z: (e') residual
    norms of rho'_T grow (L^2 like T^{2k}, dot H^{-1} like T^{2k+1}); (g) nonzero a2 / d rows of eps(rho_T).
    (e') DONE: ver topic 110 CONFIRMED 06:39:14Z (liminf T^{-2k-1} ||r eps_T||_2 > 0.0022215507882, corollary of
    106 and 108); in FR 2026-10-21T06:54Z (notes/fr110: timeline, section 10 item 4). (g) d row: ver topic 109
    (L_d in (184130.6880969186, 184130.6880969187), rho_T residual not in dot H^{-1}, r eps_T not in L^2, Hd necessary
    in the ADDENDUM's finite class); lead review and astra tail109 VALID (notes/fr109/LEAD_REVIEW.md, 06:52Z); enters
    FR when ver marks FINAL (notes/fr_tail/apply_tail.py, which supersedes notes/fr109/apply.py); d row DONE: ver
    topic 109 FINAL 07:19:16Z, in FR 2026-10-21T07:22Z (--t109 07:19; backup notes/fr109b). a2 row DONE: ver
    topic 112 FINAL 07:03:10Z (C_{2,0} in (-2734.192205182, -2734.192205181), H2_0 = k C_{2,0}/(2(1-k)) in
    (-298.795137988, -298.795137987); rho_T residual not in dot H^{-1}, r eps_T not in L^2, from the a2 row alone;
    H2 necessary in the finite class); lead recomputation by the B_(k,k) route and astra str112 VALID
    (notes/fr112/LEAD_REVIEW.md); in FR 2026-10-21T07:15Z (notes/fr_tail, --t112 07:03).
    Ver topic 111 (local velocity of the compensated corrections, |d_y F(rho_T)(P)| > 3.69e-7 for every admissible
    T): ver FINAL 07:19:16Z with the C^4 centre correction; lead review and astra tlv111 VALID WITH REPAIR (C^4, not
    C^6, at the origin), notes/fr111; in FR 2026-10-21T07:25Z (section 10 item 4, timeline, sections 4 and 8; backup
    notes/fr111b). Ver topic 113 FINAL 07:19:17Z (C_2 < 947.4716170719, C_d < 11225.91941797 in the factor distance
    of rho'_T; local jets at R = 9 below 1e-8 for T >= 10^4, so |d_y F(rho'_T)(P)| > 3.69e-7 for T >= 10^4; nothing
    for R_b <= T < 10^4): lead review VALID (notes/fr113, 2026-10-21T07:25Z), astra tq113 VALID x4 + scope repair
    (same constants suffice from T = 4509; V38 to ver 2026-10-21T07:34Z); in FR 2026-10-21T07:34Z (notes/fr113/apply.py).
    V38 superseded by ver topic 114 FINAL 07:33:31Z (finite-mode interior bounds with the sin(5 theta)
    coefficients separated: every admissible T, |X| <= 9, jets 0..3 below 1.006144e-11, 3.394241e-12, 7.827257e-13,
    1.056035e-13; |d_y F(rho'_T)(P)| > 6.6989e-7): lead check notes/fr114/check.py PASS 2026-10-21T07:52Z, astra tq114
    VALID x4 + wording repair (independent reconstruction of H1, H2, Hd, h_(i,2), N_i from the NPZ); in FR 2026-10-21T08:01Z
    (notes/fr114/apply.py). V39 (rho_T is the row-1 member; |d_y F(rho_T)(P)| > 6.70e-7, astra claim 4 VALID) DONE:
    ver topic 116 FINAL 08:14:06Z (row-1 jets on |X| <= 9 below 1.523891e-12, 5.139245e-13, 1.184002e-13,
    1.590300e-14; |d_y F(rho_T)(P)| > 6.7015e-7 for every admissible T); in FR 2026-10-21T08:36Z (notes/frmid9/apply.py).
V40 (topic 115) num 7.10 localized forcing ||tau eps~||_{H^{31/10}}, N_500(tau eps~) for tau_poly9 at delta = 0.0165:
    ver 08:25:16Z finite components CONFIRMED (geometry boxes, cutoff entries, saved-row aggregates, two methods
    each); 22 of 36 printed num ceilings inward; conditional outward ceilings lambda 1: 2.84903 (order 3), 2696.18
    (order 4), 5.65330 (order 3.1); lambda 500: 4.43139, 4583.92, 8.87175. Physical forcing OPEN (kernel
    arithmetic, inherited Green/radial TMs, full composed residual enclosures, r2 sums). FR: open objection only
    (section 8); no forcing number used. Enters 5(o)/10 item 4 only when ver marks the physical bound FINAL plus an
    astra check.
    Topic 117 (ver FINAL 08:37Z): the saved 7.10 output lacks per-cell Hessian bounds (G2F/T2F); conditional
    replacement (cutoff TL bound on |t''|+|t'|/r, Frobenius Hessian of eps~ < 9363/1000000 from saved second
    partials) gives ceilings lambda 1 (2.99137, 2898.53, 5.94978), lambda 500 (4.55066, 4779.82, 9.12448);
    still conditional. Num 08:28Z claims v1.1 (H^3.1 2.1207, N_500 4.2064) and v2.1 (1.5700, 3.5769), not
    audited; ver topic 118 (angular r2 replay) OPEN, v2.1 next. FR section 8 bullet updated 2026-10-21T08:38Z (notes/fr117).
    Topic 118 (08:44Z) angular r2 reductions CONFIRMED (contemporary replay). Topic 119 (08:58Z) v2.1 finite
    components CONFIRMED, conditional ceilings lambda 1 (0.7759, 893.16, 1.5700), lambda 500 (1.8107, 1638.56,
    3.5769); series operands, residual models, kernel conditions OPEN. FR section 8 updated 2026-10-21T09:01Z (notes/fr119).
    Astra frmid8 (far-tail passages) applied 2026-10-21T07:49Z (eps'_T notation; notes/fr_mid8).
    Topics 120, 121 contemporary replays CONFIRMED. Topic 122 (10:13Z) pinned v2.2 (cert_forcing2.py 012e106b,
    v22_p9_merged.json b5f597c9) finite components CONFIRMED, same conditional ceilings; OPEN: H0 physical residual,
    H1 G enclosures (27447 rows), H2 composed F enclosures (16502 transition rows), 15 partial suprema on B_3delta;
    five nonlinear residual jets of cert_resid.py not certified (98/99/101 would not suffice). FR section 8 bullet
    rewritten 2026-10-21T10:24Z (notes/fr122). Forcing chain is not on the critical path; no further request to ver.
    Topic 123 (10:29Z) exact log-radial residual-jet identities CONFIRMED (selected source expressions only; no
    numerical path, no physical jet). Astra frmid11 (11:11Z) checked the FR forcing bullet: numbers correct; H0/H1/H2
    (26079 rows with tau = 1, 1368 straddling, 16502 transition) and the disc suprema (B_{9 delta/4}, B_{3 delta})
    stated precisely in FR section 8 at 2026-10-21T11:12Z (notes/frmid11).
V5  Audit of the energy-symbol diagnostic (lead code/energy_symbol.py, runs/energy_s3.25_N*.json): formula and the
    reported values; floating point only.

### 6.3 lead
L2 Explicit C_B, C_V for the F- spaces at the frozen-source level (Sobolev products and the Riesz bound for U).
L3 Strongest linear statement: the verified frozen and local theorems plus the realization analysis (3.7).
L4 FINAL_REPORT.md.
L5 Edge/corner framework (notes/conormal_framework.md rev. 2): G1 x-face velocity remainder done (W1, W1'; VERIFIED
   V7); bounded-collar near/far splitting and coupling done (collar_coupling rev 2; AUDITED collar1; VERIFIED V10);
   y-face collar done (notes/yface_collar.md rev 2, AUDITED yface1 with repairs; V12); corner splitting from astra
   corner1 (notes/corner_coupling.md, V14: corner coefficients and double remainder VERIFIED, T2 traces open);
   global flow (3.9, VERIFIED conditional); P-row redundant (3.11, prow1, V17); design D_b (3.12, dib1 obstructions O1-O5, repair through F-); next the P-disc transition, the conic large-r collars, derivative versions, the
   edge problems G3; G5 conditional index reduction (notes/index_deformation.md, unaudited).

## Change log
- v3.43 2026-10-22T00:42Z: status lines only (6.1 N1', R1): ver 162, 167, 174 FINAL and integrated (FR fr182, fr183); no
  change of the argument.
- v1 2026-10-20T14:15Z: initial.
- v2 2026-10-20T14:57Z: same-order spaces; common power far weight; W[h] includes `(c[h]/3) X`; T2N adopted;
  thresholds from packets1; centre exponent corrected; source functional with `g' W_1`; index obstruction added.
- v2.1 2026-10-20T15:24Z: 3.2 corrected after the verifier's refutation; rule "both norms above threshold" withdrawn;
  realizations R+, R- added.
- v3 2026-10-20T15:53Z: realization table with the mixed class `P_2` (formal tail kernel) and the soft-`c_l`
  interpretation; F- target formulation (tail fixed, no J constraint, `(k', tau)` unknowns); saddle and far-field facts
  from realize1; J discontinuity in plain norms; frozen conjugation and homotopy-crossing facts; weight convention
  corrected; tasks V3', V5, RES added.
- v3.1 2026-10-20T16:38Z: weight exponent of the numerics multiplier corrected (`k - 1/2`); 3.5 corrected (the
  `1/|mu - 1|` cost is not a coupled-inverse bound; ver source_pole); 3.2 gains the uniform frozen inverse through
  `mu = 1` and the variable-coefficient Sobolev obstruction above threshold; 3.3 and 4 point to the edge/corner
  framework; tasks V6, L5.
- v3.2 2026-10-20T16:54Z: 3.3 rewritten after the astra conormal1 audit (framework revision 2: sufficient, not iff;
  false Sobolev inclusion replaced by `b > s` and the stronger corner weight; P disc a design choice; fixed-cutoff
  velocity splitting unbounded, frequency-adapted splitting proved in notes/weighted_velocity.md); task V7.
- v3.3 2026-10-20T17:14Z: astra weightedvel1 incorporated (notes/weighted_velocity.md revision 2): W1, W1' valid (constant `2^{|b|}`
  for `N = 0`, `b < 0`; W1' bounded for `-1/2 < b < N + 1/2`); homogeneous-trace qualification; the bounded-coupling
  claim of revision 1 section 4 withdrawn (counterexample); the global Hardy-type expectation false as worded; edge
  forcing gains `b - 3/2`. V7 now refers to revision 2.
- v3.4 2026-10-20T17:23Z: V6 and V7 CONFIRMED by ver (saddle model inverse, exit-trace sufficient condition, feasibility point;
  face splitting with constants; dilation obstruction). Ver V6 caveat recorded: for `a = 9/2 + nu`, `b = 5/2 + alpha` the
  arithmetic `delta < 0` coincides with the trace condition, but the generic `C^{4,nu}` remainder `|x|^{4+nu}` sits at the
  critical x-weight (log divergence), so a positive x-margin or a separate trace component is needed.
- v3.5 2026-10-20T18:01Z: tail family theory (notes/tail_family.md rev 2) VERIFIED as conditional statements by ver V8
  and AUDITED by astra family1; 3.7 no longer asserts that `c_l` moves along the family. Bounded-collar near/far
  splitting (notes/collar_coupling.md rev 2) after astra collar1 (CC repaired: finite strain hypothesis, Sobolev edge
  data, finite-regularity profile; (E3) restricted to `j < 3`; `x_1 > 2d`); ver V10 pending. Ver V9 CONFIRMED the
  isotropic saddle energy symbol with the scope correction that indefiniteness rules out coercivity in that pairing
  only. Ver topic39: complete coarse exterior residual majorant (`W/m < 5740483`).
- v3.6 2026-10-20T18:19Z: saddle conditioning bound `|delta| < 8.6507 - 21.3015 alpha` and the working parameters
  `alpha = 0.05`, `s = 3.06`, `b = 3.07`, `a = 6.45` (3.3); source cusp heuristic (3.3, astra pcusp1 pending); astra corner1
  (corner double Taylor splitting) pending; num asked for H^3/H^4 residual norms on the P-disc (R3 preview: high
  derivatives of eps~ near P are large).
- v3.7 2026-10-20T18:37Z: astra pcusp1 incorporated (3.3 C1-C5, AUDITED single model): frozen source cusp theorem
  (`C^{3,0.0293}` endpoint included, not `C^4`, smooth iff the cusp profile vanishes, infinitely many conditions);
  the coupled `f_y(P)` cokernel REFUTED; adapted coordinates needed for variable coefficients. Section 0, the R+ row of
  3.7, 3.7(b) and the R+ alternative of section 4: the "index -1" count is WITHDRAWN. G1 status: y-face collar note,
  astra corner1 (rectangular corner subtraction refuted globally; `J = 0`). Tasks V12-V14. Ver V10 CONFIRMED (collar
  lemma, FINAL_REPORT 5(i)); ver topic43 complete exterior certificate (`W/m < 9.4957e-5` on `r >= R_e`, FINAL_REPORT 6).
- v3.8 2026-10-20T19:01Z: pcusp wording restricted to local regularity at P (ver V13 refuted the inference to `P_2`/`P_3`
  membership); y-face note revision 2 after astra yface1 (NEEDS-FIX, repaired); notes/corner_coupling.md written with lead
  checks; V12 and V14 updated. Ver topic45: complete inner certificate (`W/m < 9.3285e-6` on `r <= e^{t_a}`, FINAL_REPORT 6).
- v3.9 2026-10-20T20:53Z: 3.9 global flow and pure transport (ver topics 52-54, constants corrected: 6.2 withdrawn);
  3.10 B_3 is a criterion only (pinf1); 3.11 axis jets J3-J7 and the P-row design decision (no jet splitting on the
  P-disc); V14 closed by topics 51 and 55 (double remainder constant < 4.725e17); verifier's full middle pass
  (one method) and whole-plane zeroth-order `N_0 < 1.904e-3`; tasks N1', N7, V16.
- v3.10 2026-10-20T21:19Z: 3.11 rewritten after astra prow1 (P-row implied by L h = f; scale-collapse obstruction of the
  strip/collar design, which is set aside; jet operators; Schur closure; uniform frozen window, 200/489 at 13/4;
  corner constraints); new 3.12 design D_b (y-axis jets only, |x|^{-2a}, flow weight) with floating rates and
  backward orbit costs, and its requirements on the trial (m > a + s - 1 at 0; P-disc refit); N7 extended; V17.
- v3.11 2026-10-20T21:32Z: 3.12 revised after astra dib1: weight sign e^{+phi} with a strict margin; direct-sum
  space; a = 6.0 (alpha away from the integers); identities (1), (8), (23) and the far exclusion (14) checked by the
  lead; obstructions O1-O5; repair route through the fixed-tail formulation F- (log-tail and tail-profile
  parameters); V18.
- v3.12 2026-10-20T21:58Z (O1 wording corrected 22:08Z): 3.12 extended with astra dib2 (D1-D10: unnormalized count 0 conditional; regularized a_4
  matching; tail jets; graph domain; far subtraction (11)-(12); source needs the nonlocal term; block closure;
  transversality ell(b) != 0 with a counterexample to the angular criterion; size estimate) and the a = 6.0 / 6.25
  rate tables; V18 extended.
- v3.13 2026-10-20T22:29Z: new 3.13 lower-order route (astra dib3 B1-B10, lead checks; the local bootstrap is false
  for the frozen operator; c unbounded on the unaugmented low space; centre condition fails at both orders for the
  present trial (m = 5); conditions L1-L4); lower-order residual norms and orbit costs; V19, V20.
- v3.14 2026-10-20T22:48Z: 3.12 D7 and 3.13 B1 VERIFIED (ver topic 68) and in FR 5(l). Band-restriction reading of the
  P-disc refits (NOTES 22:45Z; heuristic): band-supported corrections cannot cancel a transport residual, so the refits
  do not test convergence of X3 on its knots; FR section 10 item 4 reworded.
- v3.15 2026-10-20T23:15Z: 3.13 obstructions VERIFIED (ver topic 70) and in FR 5(n) and section 4; exact strain norm
  `1/(8 sqrt(pi(sigma-1)(sigma-2)))` on H^sigma (c = psi_xy(0)); weight window `s < (14A+3)/(4A+2)`. Hoelder question at P
  sent (astra holder1, notes/holder_heuristic.md).
- v3.16 2026-10-20T23:18Z: 3.10 and 3.11 status labels brought up to date (V16, V17 complete in ver topics 58-63).
  New 3.14 Hoelder scale at the source (astra holder1, AUDITED, lead checked): sharp loss `(sigma - 1)/A` in
  `C_*^sigma`, `1 < sigma < a`; endpoints; mixed Sobolev-near-P space not excluded; V21 requested.
- v3.17 2026-10-21T00:06Z: `s_fast = 3.57855` (3.2; "3.5786" is above it). New 3.15 local `H^{3.1}` a priori estimate at the
  source (astra srcloc1, AUDITED, lead checked): `K_1 = 1/(kappa - E)`, `E <= C_V delta`, outflow term intrinsic, outer
  estimate condition `b eps < 1`, auxiliary whole-plane inverse; tasks V21, V22 (frrev1 corrections), V23, N8.
- v3.19 2026-10-21T00:58Z: new 3.16 (astra escape1: jet projection and far strain defects of the remainder realization,
  vanishing source cutoff, explicit commutator constants, c[h] bound, escape weight vs signed cost, saddle offset,
  assembly, non-compactness, feasibility) and 3.17 (astra garding1: sum-of-squares Garding without theta loss, near-P
  quadratic bound and its counterexample, strain threshold). 3.15: V23 and the auxiliary inverse VERIFIED (ver topics 77,
  78), strain sign convention, N8 floating and first rigorous numbers. Tasks V24, V25.
- v3.21 2026-10-21T01:17Z: ver topic 82 (limited scope) and num's N8 v2 fixes (3.15, N8, V26). Later 2026-10-21T01:34Z: ver items 83, 84 (3.15).
- v3.20 2026-10-21T01:09Z: strain sign VERIFIED (topic 80); N8 fine pass and ver's preliminary objections (3.15); E7
  floating check (positive-part integral = signed cost on all sampled orbits; A_* about 3.439); V26 in progress; ver
  topics 79, 81 recorded.
- v3.18 2026-10-21T00:35Z: V21, V22 CONFIRMED (ver topics 74, 76; S7 constant 30.0229 < C < 30.0230); 3.12 phase-space
  orbit-cost diagnostic (code/bichar_back.py, about 5 percent gain, HEURISTIC). Astra escape1 (outer estimate with a
  weight vanishing at P) and garding1 (sum-of-squares Garding at order s) running.
- v3.22 2026-10-21T01:51Z: ver items 84, 85 (independent M_rho, M_V on the delta = 0.0165 disc) in 3.15 and N8;
  FR name C_src for the 3.15 constant; E2 convention note (V25: raw c, no change of the formula).
- v3.23 2026-10-21T02:02Z: ver topics 86 (coefficient closure), 87 (V24 CONFIRMED); V25 progress; V27, V28 listed.
- v3.24 2026-10-21T02:06Z: ver topic 88 (V25 CONFIRMED conditional); E5 premise h_y(0) = 0 and outward ceilings 0.0078149 / 0.002605.
- v3.25 2026-10-21T02:10Z: num floating four jets of X3 - trial at P recorded under V27 (not certified).
- v3.26 2026-10-21T02:13Z: ver topic 89 (trial instance of the source hypotheses and of the E3 base point) in 3.15 header and N8.
- v3.27 2026-10-21T02:24Z: V27 = topic 90 and V28 = topic 91 VERIFIED (FR 02:23Z); V30 source shift lemma listed.
- v3.28 2026-10-21T02:41Z: V29 = topic 92 and V30 = topic 94 VERIFIED; both in FR (02:41Z); lemma r3 (srcshift2).
- v3.29 2026-10-21T02:53Z: V31 (dilation corollary of the auxiliary inverse) requested; floating scaled R.
- v3.30 2026-10-21T03:04Z: V31 lead forcing numbers; V32 proposed; topics 93 (radial instance, three cells) and 95 (certified
  unscaled auxiliary bound < 1.2e35) VERIFIED and in FR (03:04Z, notes/fr0305/apply.py, with the astra frmid2 repairs).
- v3.31 2026-10-21T03:09Z: V31 VERIFIED (ver topic 96); V32 = ver topic 97 queued.
- v3.32 2026-10-21T03:25Z: V32 VERIFIED (ver topic 97); in FR (notes/fr0326).
- 2026-10-21T03:30Z: astra frmid3 repairs in FR (notes/fr0335); S5 C^4 gap recorded (no version change).
- v3.33 2026-10-21T03:49Z: V33 proposed (rough-coefficient lemma r2 after astra rough1).
- 2026-10-21T04:00Z: V33 text updated for LEMMA r4 (L5 completion class; astra rough2) (no version change).
- 2026-10-21T04:06Z: V33 text: LEMMA r5 (full N with the origin term; divergence identity) after ver's preliminary findings (no version change).
- v3.34 2026-10-21T04:25Z: V33 VERIFIED (ver topic 100, 04:16Z), in FR (notes/fr0430); V34 proposed (whole-plane Sobolev ball, notes/sobolev_box).
- v3.35 2026-10-21T04:59Z: V34 = ver topic 102 status, LEMMA r4 and (e); N10 (forcing decomposition at P, floating).
- v3.36 2026-10-21T05:23Z: V34 VERIFIED (topic 102 FINAL 05:09Z), in FR; N10 answered (num 05:09Z).
- 2026-10-21T06:28Z: V37 farres2 collected and applied; open (e'), (g) (no version change).
- 2026-10-21T06:29Z: V36 (d) answered (ver topic 15), in FR; topic 108 preliminary noted (no version change).
- 2026-10-21T06:34Z: V36 topic 108 FINAL, in FR (notes/fr108) (no version change).
- 2026-10-21T06:54Z: V37 (e') topic 110 in FR (notes/fr110); (g) topic 109 reviewed (lead, astra tail109); topic 111 astra tlv111 (no version change).
- 2026-10-21T07:15Z: V37 (g) a2 row: ver topic 112 FINAL, lead and astra str112 reviews, in FR (notes/fr_tail) (no version change).
- 2026-10-21T07:25Z: V37 (g) d row (topic 109) and topic 111 FINAL at ver, in FR (notes/fr109b, notes/fr111b); topic 113 FINAL at ver, lead review, astra tq113 pending (no version change).
- 2026-10-21T07:34Z: V37 topic 113 in FR after astra tq113; V38 (threshold T >= 4509) asked of ver (no version change).
- 2026-10-21T07:52Z: frmid8 applied to FR (07:49Z); V38 superseded by ver topic 114; lead check PASS, astra tq114 pending (no version change).
- 2026-10-21T08:01Z: V37 topic 114 in FR after astra tq114; V39 asked of ver (no version change).
- v3.40 2026-10-21T08:36Z: V39 DONE (ver topic 116; FR 6.7015e-7 for rho_T); V40 topic 115 status recorded; R0 middle rerun
  status; FR referee reviews frmid10 (sections 5, 10; 08:26Z) and frmid9 (sections 1-4, 6-9) applied; artifact
  manifest ARTIFACT_MANIFEST.md (notes/manifest/build.py).
- v3.42 2026-10-21T14:25Z: new 3.19 (ver topic 141, X-only quadratic obstruction; FR via notes/fr141).
- v3.41 2026-10-21T14:00Z: new 3.18 (ver topics 137, 138, 139; centre normalization in the weak graph topology; FR via
  notes/fr136, notes/fr136c, notes/fr139); section 4 note. Topics 128-136 (C2 Gram and joins) are in the FR only.
- 2026-10-21T08:38Z: V40 amended with ver topic 117 and num v1.1/v2.1 claims (no version change).
- 2026-10-21T11:14Z: R1 status (num chain6 complete, not verified); V40 amended with topics 119-123 and astra frmid11 (no
  version change).
- 2026-10-21T11:30Z: R0 status: ver topic 124 whole-plane assembly (primary middle) in FR 11:26Z (no version change).
- 2026-10-21T11:46Z: N1' status (ver topics 93, 125; astra fr125a VALID); C2 status (chain8d ppc 6) (no version change).
- 2026-10-21T11:54Z: N1' status (ver topic 126, astra fr126a; annulus to e^{t_b+5}) (no version change).
- 2026-10-21T12:07Z: C2 status (ver topic 127, astra fr127a) (no version change).
- v3.39 2026-10-21T06:18Z: V36 farres1 collected and applied, open (e), (f); V37 (ver topic 106 CONFIRMED; higher tail repairs with dot H^{-1} residual; in FR via notes/fr0620).
- v3.38 2026-10-21T06:03Z: V36 (ver topics 104, 105 FINAL; affine L^2 obstruction and tail repairs; in FR via notes/fr0610); open (c), (d).
- v3.37 2026-10-21T05:38Z: V35 (ver topic 103 FINAL, leading-tail separation; V34 balls do not contain X3); topic 104 preliminary noted.

Status 2026-10-22T02:16Z (lead): ver 185 FINAL 02:07Z (centre quasimodes): in the diagnostic weighted H^1-type norm X (centre
weight r^-6, degree-two critical) L at the exactly normalized trial is not bounded below on compact densities with
J = c = 0; FR 5(p). Consequence for the a posteriori argument: X cannot serve as the correction norm with a same-norm
(or X-forcing) low estimate; the two-norm theorem needs E, Y_L chosen so that the frozen centre saddle has no
critical homogeneous solutions in the angular regularity class of the norm (heuristic design requirement, not proved necessary); forcing norms stronger than X and right
inverses are not excluded. Ver 186 FINAL 02:12Z: sequence H^{5/2}-small and weakly null in X; no estimate with an
H^{5/2} or compact remainder, defect >= 1 for bounded approximate left inverses, no closed realization in X containing
it is Fredholm (FR 02:25Z). Status 2026-10-22T02:26Z (lead): unverified referee analysis (lead astra quasigen) of frozen centre
powers: radial centre weight critical at degree m, derivative order j >= 1, survives only for M_p(j) < m < M_q(j),
M_p = (d(j-1/2)+1)/v, M_q = (d(j-1/2)-1)/u (u = 2c_l-1, v = 4c_l-1, d = u+v); degree-five leakage of L on compact
J = c = 0 densities; at a = 6, s = 3.06 the anisotropic remainder excludes the critical candidate at the y-axis and a
mixed b/ordinary frozen model is invertible (rate about -2.297). CLAIMS ONLY; passed to ver as optional (NOTES 02:25Z);
ver 187 (higher centre powers) FINAL 02:23Z. Status 2026-10-22T02:42Z (lead): ver 187 integrated (FR 02:42Z, lead astra quasi187
CORRECT): the 5(p) obstruction holds in X_m for every fixed m >= 2 with velocity jets of degree <= m-2 cancelled
(constants not uniform in m); raising the radial centre power alone does not repair the norm. Ver 189 FINAL 02:37Z
(literal stored trial interface terms) integrated FR 02:48Z after lead astra iface189 CORRECT; concerns the stored
representation and floating diagnostics only, rho~ unaffected. Status 2026-10-22T03:15Z (lead): ver 191-193 FINAL integrated as FR 5(q) (FR 03:14Z, lead astra
aniso191 CORRECT). Axis-weighted logarithmic norm Y_(a,s) (||e^{(1/2-a)z} h(e^z,y)||_{H^s}, z = log x): frozen centre
transport invertible on its maximal domain when delta_Y = D(s-1/2) - A(a-1/2) - 1 < 0 (norm <= 1/|delta_Y|, below
0.435298231926 at (6, 153/50)); but for a >= 5/2, any s >= 0, the full L maps a compact J = c = 0 density away from
both axes outside Y (L h >= c x^2 near the y-axis); on T_0 image membership <=> all interior even moments Gamma_n = 0
(infinite codimension, compatible class infinite-dimensional). Design consequence: an axis-weighted realization needs a
nonlocal moment-compatible domain or a < 5/2; at s >= 3/2 every weight with delta_Y < 0 has a > 5/2 (CORRECTED
wording: not 'every frozen-invertible a'; Y also has a negative-time inverse when -Aa - b0 > 0). Ver 195 FINAL 03:08Z: the same holds for the quadrant Euler norms of 5(e) for every b and
m (pending astra leak190). Ver 190 FINAL 02:44Z: J = c = 0 alone does not keep L h in X_m for m >= 5 (pending leak190).
Status 2026-10-22T03:29Z (lead): 190, 195 in FR (fr195, 03:16Z); fr195chk fixes in FR (fr196, 03:26Z); ver 196 FINAL
03:20Z (forward thresholds a_Y(s) - 5/2 = (D/A)(s - 3/2), a_e(b) - 5/2 = (D/A)(b - 3/2), set containment; delta < 0
only sufficient) in FR (fr197, 03:28Z). Ver 194 FINAL 03:13Z (trial residual eps~ has eps~_xx(0,y)/2 = Q y^3 + o(y^3),
Q in (6.087210e-6, 6.087213e-6), so eps~ is in no Y_(a,s) and no Z_(a,b,m) with a >= 5/2): astra resid194 CORRECT; integrated in FR 5(q) "Trial residual", section 4, section 10 (fr198, 03:35Z).
Consequence for the design: strong forward axis weights fail already for the forcing (the trial residual itself), not
only for compact test densities; any axis-weighted realization at the trial needs a < 5/2 (hence s < 3/2 for forward
decay) or an axis-jet subtraction of the residual.

Status 2026-10-22T03:46Z: ver 197 (complete frozen spectrum of T_0 in Y_(a,s): closed strip [delta_-, delta_Y],
invertible iff 0 outside with norm 1/dist, otherwise not Fredholm; for a >= 0 iff delta_Y < 0) FINAL 03:28Z, astra
spec197 CORRECT, integrated in FR 5(q) (fr199, 03:44Z). Ver 194 wording fixes fr198b (03:42Z).

Status 2026-10-22T04:26Z: ver 198 (range of T_0 inside the strip: closed, Mellin moment conditions, inverse on the range of norm
at most m^{-1/2}) FINAL 03:39Z, astra spec198 CORRECT, integrated (fr200, 03:51Z; fr200b 03:58Z). Ver 199 (frozen graph
domain: for s = 153/50 and every real a, compact potentials near P give h_n with bounded T_0 graph norm, L h_n in
Y_(a,s), ||L h_n|| -> infinity; so no closed linear realization of L in Y_(a,s) has domain containing Dom(T_0), and
L - T_0 is not T_0-bounded there) FINAL 03:57Z, astra spec199 CORRECT, integrated in FR 5(q) "Frozen graph domain"
and sections 1, 4, 5, 8, 10 (fr201, 04:25Z). Consequence for the target theorem: a realization of L in Y_(a,s) must
use a domain adapted to the actual transport near P (for example the graph of V.grad), not the frozen centre domain;
the frozen inverse of 5(q) can at most serve as a local centre piece of an assembled realization.

Status 2026-10-22T04:43Z: ver 200 (Mellin moment map of the frozen range: bounded onto two weighted L^2 copies with exact norm
sqrt N, N = Gamma(u/D)Gamma(v/D)/(2Gamma(s)), about 1.10492 at (0, 153/50); unweighted bound with the same norm,
not attained), ver 201 (conditional aggregation of the fit-variant rows; changes are of upper bounds only) and ver
202 (for s = 153/50 and 0 <= a < 5/2 every compact parity test density away from the axes with c = 0 is mapped into
Y_(a,s); with 192 the threshold 5/2 is exact for T_ann,0) FINAL 04:08Z, 04:20Z, 04:28Z; astra spec200 (A) CORRECT,
(B) CORRECT IN SUBSTANCE, spec202 NEEDS FIX (scope wording only), fixes adopted; integrated (fr203 04:41Z, fr204
04:42Z). Consequence for the design: at s = 153/50 the weak weights 0 <= a < 5/2 accept every compact zero-strain
test density, so the nonlocal moment conditions are a strong-weight phenomenon; the remaining obstruction in every
Y_(a,s) is the graph-domain one (no closed realization with domain containing Dom(T_0)), and for 0 <= a < 5/2 at
s = 153/50 the frozen centre transport is not invertible (a < a_Y(s)), so a weak-weight realization needs its own
inverse on the closed range of infinite codimension or a different centre model.

Status 2026-10-22T04:54Z: ver 203 FINAL 04:41Z (astra spec203 CORRECT IN SUBSTANCE, wording fixes adopted; integrated fr205
04:53Z): the residual of the exactly joined trial lies in Y_(a,153/50), a >= 0, exactly when 2k < a < 5/2 (qualitative,
no ceiling; lower endpoint from the r^{2k-1} tail with nonzero sine-3 coefficient e_1, upper from Q). Consequence:
forcing data and compact tests both fit the weak weights 2k < a < 5/2 at s = 153/50, where T_0 has closed range of
infinite codimension; a realization there needs a range-compatibility mechanism (the Mellin moment conditions) and
an inverse on that range, and a norm bound of the residual in Y_(a,153/50) would still be a separate computation.
Open at the verifier: logarithmic_strain_functional (c[h] bounded on Y_(b,s) for 0 <= b < 2, s + b > 2).

Status 2026-10-22T05:20Z: ver 204 (strain functional) and 205 (higher orders) FINAL 04:50Z and 04:57Z (astra spec204
CORRECT IN SUBSTANCE, fixes adopted; integrated fr206 05:16Z): c is bounded on Y_(a,s) for s >= 0, 0 <= a < 2,
s + a > 2 (explicit non-sharp constant, below 0.263445900665 at (3/2, 153/50)) and unbounded for a >= 2; zero-strain
compact tests map into Y_(a,s) for 0 <= a < 5/2 and 0 <= s < 6 - a. Ver 206 FINAL 05:05Z (scaling rank one): at
s = 153/50 the trial and X.grad rho~ lie in Y_(a,s) exactly when 1 + k < a < 5/2, the scaling term (c[h]/3) X.grad rho~
is bounded exactly when 1 + k < a < 2 (then rank one and compact), and all compact tests away from both axes map into
Y exactly when 1 + k < a < 5/2 (draft fr207, astra spec205 audit running). Consequence for the design: the window
1 + k < a < 2 at s = 153/50 (about 1.179 < a < 2) is the only weight range where residual, trial, compact tests and a
compact rank-one scaling term all fit; there T_0 is not Fredholm (closed range of infinite codimension) and the graph
domain obstruction persists, so a realization needs a range-compatibility mechanism and an inverse for the variable
transport on a domain not containing Dom(T_0). No such inverse is known or in progress; the endpoint stays UNRESOLVED.

Status 2026-10-22T05:42Z: ver 206 integrated (fr207 05:28Z). Ver 207 (centre trace, FINAL 05:16Z; fr208 05:29Z) and ver 208 (full
graph centre trace, FINAL 05:31Z; astra spec208 CORRECT IN SUBSTANCE, fixes adopted; fr209 05:42Z): for every real
a < 5/2 there are smooth compact strain-zero densities h_delta equal to x^2 y near 0 (J = 1) with compact canonical
velocity and ||h_delta||_Y + ||T_0 h_delta||_Y -> 0 for every finite s, and ||h_delta||_Y + ||L h_delta||_Y -> 0 for
0 <= s < 4. So J is not closable in Y_(a,s), in the frozen graph norm or (s < 4) in the graph norm of L, and the
normalized classes J = 0, J = 1 are not closed there. Consequence for the design: in the window 1 + k < a < 2,
s = 153/50, a normalized realization needs in addition a trace-controlling norm (for example adding |J(h)| or a
centre Holder seminorm of h/(x^2 y)) or a selected closed domain on which J is continuous; none is constructed or
verified. s = 4 and higher orders are open for the graph norm of L. Endpoint UNRESOLVED.

Status 2026-10-22T06:36Z: ver 209 (FINAL 05:40Z; fr210), 211 (FINAL 05:57Z; fr211) and 212 (FINAL 06:07Z; astra spec212
NEEDS FIX, summary fixes adopted; fr214, fr215). For every real a and finite s >= 0, at the exactly joined trial, the
quadratic term Q(h) = W[h].grad h is not continuous at 0 from the graph norm ||h||_Y + ||L h||_Y into Y_(a,s) on the
compact-potential class D_cp (J = c = 0, all centre jets zero, compact canonical velocity), on every subspace of D_cp
of finite algebraic codimension (any finitely many linear constraints, no continuity), and on the zero set near 0 of
finitely many constraints Phi_cp that vanish at 0, are C^1 (Frechet) in the graph norm and have onto derivative at 0.
Only the maximum of the two polarized outputs is bounded below. Singular constraints (example
||h||_Y^2 + ||L h||_Y^2), infinitely many constraints, stronger domain norms, weaker targets and scales are open.
Consequence for the design: a closure that needs ||Q(h)||_Y <= C (||h||_Y + ||L h||_Y)^2 near 0 in a Y_(a,s) graph
norm, with or without a regular finite normalization or phase condition, is excluded; the nonlinear step must use the two-norm design of section 5 (Q measured in a weaker
target from a stronger domain norm), whose linear inputs K_H, K_L, C_B, C_V, eta are not available in one
realization. Endpoint UNRESOLVED.

Status 2026-10-22T09:51Z: ver 179v2 + 183 coarse (FINAL 08:42Z, 08:49Z; fr187, fr226): direct whole-plane bounds in the diagnostic
norm X, ||eps~||_X < 245653983.313885102003858 and ||eps~ - partial_t eps~||_X < 30665526224.2484290248531, without the
saved majorants (exterior term dominates; ver 180v2 exterior cells running, notes/fr227 template for 183 exterior).
Ver 213 (FINAL 09:35Z; astra fr228chk CORRECT IN SUBSTANCE, fixes adopted; fr228, FR 5(r)): in the factor norm of the
axis control, ||h||_F = sup |h|/(x^2 |y| (1 + r^2/L^2)^((k-3)/2)), on the space B_F of continuous even-even factors
vanishing at 0 and at infinity, slowly varying logarithmic annuli x^2 y beta((-log r - n)/n) with an exact strain
compensator give unit weak-null quasimodes with J = c = 0 at the exactly normalized trial. So no same-norm inverse
estimate, none with a bounded linear compact remainder, and no closed linear Fredholm realization in B_F containing
them. Consequence for the design: on domains containing the sequence, the norm of a same-norm inverse estimate cannot be
the bare factor supremum (which already fails to control the interior velocity, section 4 of the FR); other norms (for
example with a factor Hoelder or derivative component) or a domain excluding the sequence are needed. Hoelder factor norms are not excluded by 213 and no inverse in them is known.
Endpoint UNRESOLVED.
Status 2026-10-22T10:25Z: ver 180v2 (FINAL 10:18:52Z; 89 exterior Taylor-model cells on 0 <= log r - b_+ <= 17 plus the 178 tail)
and 183 exterior composition (FINAL 10:22:57Z; fr227): ||eps~||_X < 8.38010956871949018314234 and
||eps~ - partial_t eps~||_X < 2467.95347982509225629694 on the whole plane, without the saved majorants. The inner
disc (square 67.99) now dominates ||eps~||_X and the middle annulus (square 6074661.9) dominates
||eps~ - partial_t eps~||_X. Still about 22 and 4 times the conditional 0.385656/585.874 bounds; diagnostic norm X
only; no inverse in X (ver 185/186), so these give no a posteriori conclusion. Endpoint UNRESOLVED.


Status 2026-10-22T11:34Z: verified inner derivative cells (44 cells on [-5, 0] plus the accepted tail) and the both-mode composition give the direct whole-plane bounds ||eps~||_X < 1.49546805188731021373656 and ||eps~ - partial_t eps~||_X < 2464.68293019825564964515; the middle annulus dominates both; still about 3.9 and 4.2 times the conditional bounds 0.385656000027 and 585.874000000002. No saved majorant, inverse, nonlinear estimate, distance to X3 or endpoint follows. Verdict UNRESOLVED.

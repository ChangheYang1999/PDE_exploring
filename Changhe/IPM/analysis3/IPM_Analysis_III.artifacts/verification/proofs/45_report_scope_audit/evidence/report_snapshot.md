# S2 theory report: the full-plane IPM self-similar profile with x^2 y leading term (case 1, candidate X3)

Version of 2026-10-28T03:35Z. This report is self-contained. Proofs, computations, code and data are in the
accompanying artifacts listed in section 7. Verification records are cited by number (V001, V002, ...); they are the
entries of the accompanying verification report, each with claim, method, result, verdict and evidence.

Labels used throughout:
- THEOREM: a complete proof exists and the independent verifier has CONFIRMED it (record number given).
- CONDITIONAL THEOREM: a checked implication whose hypotheses are named and not all verified.
- DERIVED: a proof written by the theory author, with independent checking pending.
- NUMERICAL: a floating-point observation. It is never a bound.
- OPEN: not established.
- REFUTED: shown false, with the counterexample.
A statement is called a theorem in this report only if it has a CONFIRMED verdict.

## 0. Verdict

A complete nonlinear existence theorem is NOT established. Nothing found in this work proves or suggests that no exact
solution exists near X3. Every obstruction found is an obstruction to a particular norm or method.

What is established:
- exact frozen inverses at the three ends of the flow (origin saddle, source points, infinity), with explicit constants;
- a global Fredholm theorem of index 0 for the full nonlocal fixed-strain operator in radial weights, conditional on
  one pointwise margin inequality, which holds on a fine grid with value 2.590 and is not yet certified;
- the exact structure of the normalization (the strain functional c), with a bounded realization, an exact rank-one
  bordering by the log variation of the far exponent, a positive denominator, and a unique scalar normalization;
- a series of sharp negative results, each with an explicit counterexample, that rule out isotropic, radial and Hoelder
  formulations of the nonlinear problem;
- the inverse of the scalar y-axis row on explicit spaces (conditional on a positive axis rate), the inverse of the
  pure transport on the full jet-plus-remainder spaces (conditional on the axis rate, two angular coefficient bounds and
  a positive transport margin), and membership of the background residual in the matching anisotropic jet target;
- an abstract two-norm iteration theorem whose hypotheses are listed as concrete constants.

The first missing estimate is a weighted Garding inequality for the coupling in an anisotropic weight
|cos theta|^{-2a} e^{mu(log r)} near the outgoing y-axis, together with the boundedness and compactness of the jet
couplings (lemma (E), in the precise form (E0), (E-J), (E-G) of section 2.3; section 6.2). After it, the missing items are the
certified margins, a quantitative injectivity check, a high-norm inverse, a bilinear bound and a certified residual.

## 1. Problem, accepted state and exact equation

1.1 Equation. F(rho) = (c_l X + U[rho]).grad rho - rho on R^2, with U = (-psi_y, psi_x) and -Lap psi = d_x rho. The
density rho is even in x and odd in y, and rho = x^2 y a with a continuous and a(0) = 1. The canonical velocity is the
one given by the Riesz kernels with the standard subtraction for profiles growing slower than r. No harmonic velocity
is added.

1.2 Normalization. If F(rho) = 0 in this class (in the distributional sense when the factor a is merely continuous),
then 3 c_l - c[rho] = 1 with c[rho] = psi_xy(0). Consequently DV(0) = diag(-A, D) with A = 2 c_l - 1 and
D = 4 c_l - 1 = 2A + 1. THEOREM (derived independently twice; V002).

1.3 Accepted state and the rigorous background.
- The accepted numerical state is the published candidate X3, with c_l = 1/k and k = 1615536043799051/2^53, so
  c_l = 5.575362610641546..., A = 10.15073, D = 21.30145 and b_0 := c_l + 1 = 6.57536. No newer accepted state exists:
  the later collocation solves stagnated at a 2-norm residual of about 2e-4.
- X3 is not exactly normalized: 3/k - 1 - c[X3] lies in (1.0301137738456e-8, 1.0301137743913e-8) (THEOREM, V018). With
  the normalized exponent, F(X3) therefore contains a term that grows like r^k, and X3 cannot itself be the rigorous
  background.
- Every rigorous statement below uses the exactly joined, exactly normalized explicit modal trial rho~ instead. Its
  strain before repair is c0 in [15.7260878319246786225638146971829, 15.7260878319246786225638146971831], and a scalar
  repair z in [-1.198605236453734890460334164888e-20, -1.198605236453734890460334164887e-20] makes c[rho~] = 3/k - 1
  exactly (THEOREM, V005). An independent ball-arithmetic recomputation by three formulas gives
  c[rho~] - (3/k - 1) in [-1.62e-43, 1.62e-43] (certificate, one team).
- rho~ is C^{4,1} and not C^5 at the origin: the degree-5 inner term contains sin(521 theta) (THEOREM, V036). Every
  local estimate below uses at most four derivatives of rho~ at 0.
- The source point of rho~ is unique at x_P in (4841405518533377, 4841405518533711)/2^49, with transverse rate mu in
  (0.99999997745, 0.99999997750) and g = d_y rho~(P) in (29, 30) (THEOREM, V017). So rho~ is not stationary at P, and
  mu = 1 must not be substituted.

1.4 Full linearization and exact expansion (formulation N: c_l[rho] = (1 + c[rho])/3 is built in). For every background
with 3 c_l_bar - c[rho_bar] = 1,
    F(rho_bar + h) = F(rho_bar) + L h + N(h),   L h = V.grad h - h + W[h].grad rho_bar,   N(h) = W[h].grad h,
with V = c_l_bar X + U[rho_bar] and W[h] = U[h] + (c[h]/3) X. There are no cubic terms. Equivalently
F(rho_bar + h) = F(rho_bar) + A_h h with A_h g = (V + W[h]).grad g - g + W[g].grad rho_bar. Only the transport field
of A_h depends on h; its divergence is 2 c_l_bar + 2 c[h]/3, and its linear part at 0 is diag(-A', D') with
D' = 2A' + 1, so the normalization structure is preserved along an iteration. L = L_fix + (c[.]/3) X.grad rho_bar, where
L_fix h = V.grad h - h + U[h].grad rho_bar. The last term is a rank-one perturbation by a function that grows like r^k.
(THEOREM, V038, fixed-background expansion.)

1.5 Strain functional. c[h] = (1/pi) PV int sin(3 theta) r^{-3} h dX - (1/4) h_y(0). The local term vanishes in the
class above. THEOREM.

1.6 Scaling direction and the centre coordinate. The scaling tangent K = rho~ - X.grad rho~ has J(K) = -2, c[K] = 0 and
L K = eps~ - X.grad eps~ with eps~ = F(rho~); here J(h) is the x^2 y coefficient of h at 0. The constraint J(h) = 0
removes the scaling direction only if J is continuous on the correction space. In the diagnostic norm of the earlier
analysis of this case, and in its graph norm even at fixed strain, J is not continuous and {J = 0} is dense (THEOREM,
V012, zero-strain packets). J is a continuous coordinate of the jet-plus-remainder spaces of section 2.

1.7 Moving far exponent (THEOREM, V025 and V038). An exact solution with c[h] != 0 has far exponent 1/c_l[rho], which
differs from k. A fixed background plus a correction in any of the weighted spaces used here cannot contain such a
solution, and every smooth parameterization of the tail has a log^2 r second variation. The consistent formulation is
parametric: background family rho_bar_ell = rho~ + chi_inf (r^{1/ell} - r^k) Theta_0, unknowns (ell, h), and the scalar
equation 3 ell - c[rho_bar_ell + h] = 1 (section 4.3). d rho_bar_ell/d ell at ell = c_l is -k^2 KP, with
KP := chi_inf r^k log r Theta_0, the log variation of the far exponent.

## 2. Avenue I: weighted L^2 and Sobolev theory

2.1 The strongest rigorously valid weighted inverse estimates.

(a) Frozen origin saddle, Theorem O (THEOREM, V022). T_0 := -A x d_x + D y d_y - 1. Fix 5/2 < a < 9/2 and 0 <= b < 3/2
with a + b > 4. Put w = |x|^{-2a} |y|^{-2b}, kappa_0 := b_0 + A a - D b and sigma := a + b - 4.
- Domain: Z_0 = {h = x^2 y (J + beta_t(log r)) + h_R}, with beta_t' in G := L^2(e^{-2 sigma t} dt), beta_t(-inf) = 0,
  h_R and Y_0 h_R in R_w := L^2(w dX), Y_0 = -A x d_x + D y d_y. Range: Y = {x^2 y gamma(log r) + F_R : gamma in G,
  F_R in R_w}. The decomposition is unique because x^2 y is not in R_w for a > 5/2.
- On R_w, T_0 (maximal domain) is bijective with T_0^{-1} F = -int_0^inf e^{-s} F(Phi_s X) ds and
  ||T_0^{-1}|| = 1/kappa_0, sharp. The same holds on the conormal spaces generated by x d_x and y d_y, which commute
  with T_0.
- T_0 : Z_0 -> Y is bounded and onto, with kernel span{x^2 y}; J is a continuous coordinate; the right inverse with
  J = 0 has explicit norm.
- The strain functional extends continuously to Z_0 restricted to r < 1:
  |c[h 1_{r<1}]| <= |J|/8 + 0.069735617396310252 ||beta_t'||_G + 0.045183183318774124 ||h_R||_{R_w}.
- At a = 7/2, b = 6/5: kappa_0 = 16.54116035405294722844...; at a = 17/4, b = 0: kappa_0 = 49.7159.
- No approximate kernel exists modulo x^2 y. The degree-2 centre quasimodes and the jet packets that obstruct the
  earlier norms are excluded or have unbounded image norm.
- The pointwise reading of the strain extension is REFUTED: a thin flow-tube sum in Z_0 is not continuous at 0, so c
  on Z_0 is the continuous extension from a core.

(b) Frozen source (THEOREM, V011, V021, V024). L_P = A s d_s + mu y d_y - 1 - g M with M = -R_1^2, on the maximal
full-plane H^s graph domain. With delta_s = min(1 + (A + mu)/2 - s mu, 1 + (A + mu)/2 + g - s A) > 0 the operator is
bijective on H^s with inverse norm at most 1/delta_s. On the box A in [10, 10.2], mu in [0.99, 1.01], g in [29, 30]
and s = 31/10 the bound is 500/1687, and every s < 2373/680 is admissible. mu = 1 is not a pole. An auxiliary
variable-coefficient version has an explicit bound and a sharp strain norm (V021), and the neighbourhood of the actual
source satisfies the perturbation margin kappa - E >= 44699521/14000000 (V024).

(c) Global Fredholm theorem for the full nonlocal fixed-strain operator, Theorem R (CONDITIONAL THEOREM, V023 and V031).
- Hypotheses: V globally Lipschitz and C^1 with V(0) = 0 and div V = 2 c_l; the coupling coefficients continuous and
  tending to 0 at 0 and at infinity; the weight w = e^{mu(log r)} with mu Lipschitz and Lip(mu) < 2; and the margin
     (H_m)   m_* := inf_{X != 0} [ b_0 + (1/2) mu'(log|X|) q(X) - b_+(X) ] > 0,
  with q = X.V/|X|^2 and b_+ = (|grad rho~| - d_y rho~)/2, the top of the symbol of the coupling U[.].grad rho~.
- Domain: the maximal domain D_w = {h in L^2_P(w) : V.grad h in L^2_P(w)}. Range: L^2_P(w) (P: the parity class).
- Conclusion: L_fix : D_w -> L^2_P(w) is Fredholm of index 0, and there is a compact K with
  m_* ||h|| <= ||L_fix h|| + ||K h|| (no eps loss). L_fix is invertible if and only if it is injective.
- The hypotheses other than (H_m) hold for rho~. For the piecewise affine weight mu~ (sup|mu~'| = 7/4, e^{mu~} ~ r^{1/4}
  at 0 and r^{-5/4} at infinity) the grid minimum of the margin is 2.590 (NUMERICAL). A box certificate is in progress.
- Limits (THEOREM, V032): on this graph the strain c is not closable. Rescaled annular packets h_n with c[h_n] = 1 have
  h_n -> 0 and L_fix h_n -> 0 in L^2(w). So Theorem R covers L_fix and not the normalized operator L. Injectivity is
  OPEN; no kernel element is known.

(d) Necessary conditions for any space that carries the normalization (THEOREM, V025).
- N1: for product-conic weights r^{-2 beta_r} |cos theta|^{-2a} |sin theta|^{-2b} near 0, coercivity of the frozen
  saddle on every ray holds if and only if beta_L(b) < beta_r < beta_U(a), and beta_L(3/2) = beta_U(5/2) = 4 exactly.
  So if the frozen saddle is coercive in L^2(w) and x^2 y is not in L^2(w), then a >= 5/2 (endpoint allowed; the word
  "strictly" of the first version is REFUTED). This statement is for the coercive product-weight mechanism. Continuity
  of J alone does not force anisotropy (V035).
- N2: along the outgoing y-axis the angular exponent a(t) must be nondecreasing. Conditional on the positive axis rate
  q(0, y) > 0, which is NUMERICAL for rho~ (5.58 <= V_2/y <= 21.31 on the grid).
- N3: in such a space the x^2 coefficient along the whole y-axis is a separate unknown. Its row (the jet row of L) is
  V_2(0, y) g' + (2u - 1) g + 2 rho_2 (d_x U_1[h](0, y) + c[h]/3) + rho_2' (U_2[h](0, y) + c[h] y/3) = f_2(y),
  and the strain term cancels the leading coupling as y -> 0.
- N4: at infinity a far factor r^{-2 gamma} needs 2k < gamma < 1 + k (coercivity, exclusion of the homogeneous tails
  r^k Theta, and membership of the residual r^{2k-1} Eps).
- N5: the fixed-background obstruction of 1.7.

2.2 Older obstructions and whether they still apply.

| Obstruction (earlier record) | Applies to | Status in the present spaces |
|---|---|---|
| Degree-2 centre quasimodes (V006) | diagnostic norm with r^{-6} weight | excluded for a > 5/2; no approximate kernel (Theorem O) |
| Pointwise cubic coefficient of L h not controlled by C^{2,alpha} regularity and J = 0 (V007) | pointwise centre conditions | applies; the centre is handled by weighted L^2 conditions with J as a coordinate |
| Non-smooth homogeneous centre solutions below the integer modes (V009) | continuous-factor classes | no effect on Z_0: Theorem O gives a bounded remainder inverse, so cut-off homogeneous solutions are not approximate kernels |
| Radial local moment gap (V010) | radial or isotropic moment estimates | applies; no radial argument is used at 0 (N1) |
| J nonclosed, also at fixed strain (V012) | norms without a jet coordinate | evaded: J is a coordinate of Z_0 and Z |
| Negative potential energy at the saddle (V003) | energy pairing | applies to energy methods; not to the transport-weighted estimate |
| Mapping obstruction for a >= 5/2 without jets | conic weights without jets | consistent with N1 to N3: the y-axis jet is a required coordinate |
| No constant weight (b_+ reaches 10.14 > b_0) | constant or slowly varying weights | applies (NUMERICAL); avoided by the radial Lyapunov factor of Theorem R |
| Source Sobolev window | H^s at the source | applies: s < 2373/680 (V011) |
| Weak graph norm discontinuity of N (V019) | the diagnostic graph norm | applies; a high norm is needed (section 3.4) |
| Strain not closable on the radial graph (V032) | every A_2 radial weight | applies; the normalization needs the origin part of section 2.3 |
| Finite-section residuals are not inverse bounds (V014) | every finite section | applies; section 5 |

2.3 A consistent domain.
- Spaces (definitions; all functions with the IPM parity, t = log r, a = 17/4).
  - Weight w_a = |cos theta|^{-2a} e^{mu_a(t)}, mu_a' = -2a for t < 0 and -5/4 for t >= 0, mu_a(0) = 0. In r < 1 this is
    exactly |x|^{-2a}, the weight of Theorem O with b = 0. R := L^2_P(w_a).
  - Jet lift E gamma := x^2 y gamma(log r), and the scalar space G with
    ||gamma||_G^2 = int_{t<0} |gamma|^2 e^{-t/2} dt + int_{t>0} |gamma|^2 e^{27t/4} dt (the radial factor of |x^2 y|^2 w_a).
  - Target Y := E G (+) R (direct, since |cos theta|^{4-2a} is not integrable).
  - Axis row (THEOREM, V041, conditional on the axis hypothesis (A) below). With d(t) := V_2(0, e^t)/e^t and
    D = 4 c_l - 1, the y-axis component of the transport acting on g = y beta(log y) is
    A beta = d beta' + (D - d - 2d') beta. Put H := exp(-int_{-inf}^t (D - d - 2d')/d), beta = H z, and let B be the space
    of such beta with z' in L^2(omega), omega = e^{-t/2} (t < 0), e^{2(3/8 + k) t} (t > 0), z(+inf) = 0, normed by
    |J|^2 + ||z'||^2 + the two Hardy terms, where J := lim_{t -> -inf} beta(t) is the cubic coefficient. Then A is an
    isomorphism of B onto Gamma (||gamma||_Gamma = ||gamma/(d H)||_{L^2(omega)}, equivalent to G), with
    beta(t) = -H(t) int_t^inf gamma/(d H), J = -int gamma/(d H), and explicit constants. J is an output of the far
    condition; imposing J = 0 as well restricts the range to a closed hyperplane.
    Hypothesis (A): d_min <= d <= d_max with |d - D| + |d'| <= C e^{2t} (t <= 0) and |d - c_l| + |d'| <= C e^{-(1-k)t}
    (t >= 0). The endpoint orders hold for the modal field; positivity of d and the constants are not yet certified
    (grid: 5.58 <= d <= 21.31, NUMERICAL).
  - Domain Z := E B (+) D_R, with D_R the maximal domain of T = V.grad - 1 in R and the graph norm.
    In the parametric formulation the tail coordinate is ell.
- Membership checks: x^2 y chi_0 is in Z (J = 1); r^k Theta is not in Z; c is bounded on Z (Lemma C'4 below); the
  residual of the modal background lies in Y, with up to five conormal derivatives (THEOREM, V042: F(rho~) = x^2 y B,
  gamma = B(r, pi/2) in G, and the rest carries cos^4(theta) sin(theta); B = O(r^2) at 0 by the exact normalization
  and O(r^{2k-4}) at infinity); the parametric residual F(rho_bar_ell; ell) - nu(ell, 0) H_0 lies in Y, smoothly in
  ell, for max(q, k) < 5/16 (THEOREM, V042). These are membership statements; no value of the residual norm is
  certified.
- Every necessary condition of 2.1(d) is met: a = 17/4 lies in [5/2, 9/2); the angular factor is constant along the
  y-axis; the axis jet is a coordinate; the far exponent 5/8 lies in (2k, 1 + k).
- Margin: inf (kappa_{w_a} - b_+) has grid minimum 3.0908 (NUMERICAL), attained in the far field, with
  kappa_{w_a} = b_0 + (mu_a'/2) q + a tan(theta) V.grad(theta). The certificate is in progress.
- Theorem C' (DERIVED as a whole; its pure-transport part is a CONDITIONAL THEOREM, V046). The first version ("if (E)
  and the margin hold, L : Z -> Y is Fredholm by the proof of Theorem R") did not specify the lifting, the cross
  couplings, the remainder domain or the homotopy (V041). The present version does:
  - Lemma C'1 (CONDITIONAL THEOREM, V046): T(E beta) = E(A beta) + x^2 y cos^2(theta) [a_1 beta' + a_0 beta]. Under the
    coefficient bounds (CB) |a_1| <= M_Q and |a_0| <= M_P min(r^2, 1), the lift error is bounded from B to R by
    I_a^{1/2} (M_P ||min(e^{2t}, 1) beta||_G + M_Q ||beta'||_G), I_a = int |cos theta|^{8-2a} sin^2 theta = 6.99215...
    That the modal field satisfies (CB) is DERIVED (smoothness and evenness in x of q and p on annuli, the cubic
    expansion of V at 0, and V - c_l X = O(r^k) at infinity); M_Q and M_P are not yet computed. The error is not compact
    at 0, and the proof does not need it to be.
  - Lemma C'2 (THEOREM, V046): if kappa_* := ess inf kappa_{w_a} > 0 and kappa_{w_a} is bounded, the remainder transport
    T_R on its maximal domain D_R is bijective onto R with ||T_R^{-1}|| <= 1/kappa_* (characteristic formula through the
    weighted flow group).
  - Lemma C'3 (CONDITIONAL THEOREM, V046): under (A), (CB) and kappa_* > 0, T : Z -> Y is an isomorphism with the exact
    lower-triangular form [A, 0; Err, T_R] and the explicit inverse E gamma + f -> E A^{-1} gamma +
    T_R^{-1}(f - Err A^{-1} gamma). J is continuous on Z, and restricting to J = 0 leaves a closed range of codimension
    one.
  - Lemma C'4: c[E beta + h_R] = (1/4) int e^{2t} beta dt + (1/pi) int sin(3 theta) r^{-3} h_R, bounded on Z, with
    constant 0.207570 on R.
  - Why the strain term belongs to the coupling (THEOREM, V044). The fixed-strain operator L_fix = T + U[.].grad rho~
    does not map Z into Y: for h = x^4 y eta_0(r) with eta_0 >= 0 supported in 2 < r < 3 (so h is in R, J = 0 and
    c[h] = (3/16) int r^3 eta_0 dr > 0), L_fix h = -c[h] x^2 y + O(r^5) near 0, and a constant axis factor is not in G.
    The profile H_0 is not in Y either, so c[.] H_0 is not a bounded perturbation into Y. With the strain term in the
    coupling the image of this h is in Y. Theorem C' therefore cannot be read off from Theorem R plus a rank-one term.
  - Hypothesis (E), precisely: (E0) the renormalized coupling C h = [U[h] + chi_0 (c[h]/3) X].grad rho~ maps Z
    boundedly into Y; (E-J) its jet part is compact from Z to G; (E-G) its remainder part is bounded on R and satisfies
    Re <C_R h, h> <= int (b_+ + eps)|h|^2 w_a + Re <K_eps h, h> with K_eps compact.
  - Proved piece of (E0) (THEOREM, V045): input supported in |x| > 2R, output restricted to the bounded strip |x| < R,
    |y| < Y, after the x^2 axis subtraction, gives a compact operator in the weight w_a (any 0 < a < 9/2 and far
    exponent below 2), with smooth axis traces. Adjacent input, limits uniform at 0 and at infinity, and jet inputs are
    OPEN.
  - Conclusion: under (A), (E0), (E-J), (E-G) and (H_m') inf (kappa_{w_a} - b_+) > 0, the operator L_ren = T + C is
    Fredholm of index 0 from Z to Y, and so is the bordered operator L_red of 4.3. Proof: the homotopy T_R + s C_R has
    constant semi-Fredholm index and starts at the invertible T_R; the block lower-triangular part factors through the
    isomorphism A; the jet coupling and the rank-one bordering are compact.
- Answer: a domain exists that is consistent with every necessary condition found, on which the normalization is
  continuous and the modal residual lies in the target. On it the pure transport is an isomorphism (CONDITIONAL
  THEOREM, V046, under (A), (CB) and kappa_* > 0). That the full linearization is Fredholm on it is conditional on (A),
  (CB), (E) and the certified margin (Theorem C', DERIVED, coupled steps not yet verified). That it is invertible is
  OPEN.

## 3. Avenue II: direct Hoelder theory

3.1 Can h be controlled directly in C^alpha?
- At each end of the flow, yes, in the right anisotropic class.
- Globally, no Hoelder inverse of L is established. The Hoelder theory of the actual (non-frozen) transport near 0 is
  OPEN. The proposed transfer of the frozen estimate by a conjugacy was REFUTED (V028, Remark 2.1 of the accompanying
  Hoelder document).
- Frozen saddle (THEOREM, V028), on the whole-plane maximal domains:
  - S(a), S(b): isotropic C^alpha has an inverse only for alpha < 1/D = 0.0469, and this is sharp. For alpha > 1/D a
    smooth compactly supported forcing gives the bounded solution an exact |y|^{1/D} singularity along the whole
    incoming x-axis.
  - S(c): in the class C^alpha_p, whose y-Hoelder seminorm carries the weight |x|^p, T_0^{-1} is bounded if and only
    if 1 + pA > D alpha, with explicit constants and equality in the sharpness. At p = 2, the natural x^2 structure,
    every alpha < 1 is admissible.
  - H0: the weighted-sup analogue of N1. Coercivity together with exclusion of x^2 y forces |x|^a weights with a > 2,
    so the y-axis jet is a coordinate in the Hoelder setting too.
  - S(d), smooth-cutoff form: T_0 plus the coupling localized by a smooth cutoff chi_delta is invertible on the
    whole-plane class C^alpha_1 for alpha < (1 + A)/D = 0.5227 and delta small. This uses the frozen T_0, excludes the
    strain column, and needs rho~ in C^4 near 0 (V036). The indicator-cutoff form is REFUTED.
- Source (THEOREM, V013 for mu = 1 and V029 for the actual rate mu < 1): the frozen coupled source inverse maps compact
  C^alpha input to C^alpha for every 0 < alpha < 1. Above order 1 the loss is sharp (V013, at mu = 1): C^sigma maps into
  C^{sigma - (sigma - 1)/A} and no better, for 1 < sigma < g/(A - 1), and the regularity ceiling for fixed smooth
  forcing is (1 + g)/A.
- Strain (THEOREM, V028): c is bounded on C^alpha_p if and only if p + alpha > 1.

3.2 Admissible exponent range.

| Piece | Admissible alpha | Class | Status |
|---|---|---|---|
| frozen saddle, isotropic | alpha < 1/D = 0.0469 (sharp) | C^alpha | THEOREM (V028) |
| frozen saddle, axis-weighted | alpha < (1 + pA)/D (sharp); every alpha < 1 for p >= 2 | C^alpha_p | THEOREM (V028) |
| saddle plus localized coupling | alpha < (1 + A)/D = 0.5227 | C^alpha_1 | THEOREM (V028) |
| strain functional bounded | p + alpha > 1 | C^alpha_p | THEOREM (V028) |
| coupled source at the actual rate | every 0 < alpha < 1 | compact C^alpha input | THEOREM (V029) |
| pure transport at the source (no coupling) | alpha < 1/A = 0.0985 | illustration | DERIVED |
| infinity | weighted classes with 2k - 1 < gamma < k | scaled C^alpha | DERIVED |
| nonlinear closure, perturbative | none | any C^alpha-type norm | THEOREM (V030) |

3.3 The Riesz coupling and the source.
- Exact form: U[h].grad rho_bar = -(d_y rho_bar/2) h + [d_y rho_bar T_xx - d_x rho_bar T_xy] h, with T_xx, T_xy the
  principal-value convolutions with cos(2 theta)/(2 pi r^2) and sin(2 theta)/(2 pi r^2). The two Riesz factors are
  never estimated separately: this is one operator of order 0 with an explicit local part.
- Its symbol ranges over [-(d_y rho_bar + |grad rho_bar|)/2, b_+], with b_+ = (|grad rho_bar| - d_y rho_bar)/2. The
  local part damps where d_y rho_bar > 0, in particular at the source, where d_y rho~ = g is in (29, 30).
- Near 0 (|grad rho~| = O(r^2)) and at infinity (O(r^{k-1})) the coupling is a small perturbation. At the source it is
  not small, and the coupled frozen operator must be inverted as a whole. The coupling is essential there: without it
  the pure transport inverse loses Hoelder regularity above 1/A.
- The C^alpha operator norm of the principal-value part is not its symbol supremum. No Hoelder analogue of the sharp
  Garding inequality is known, so the global Lyapunov argument of Theorem R has no Hoelder counterpart with the same
  constants.

3.4 Is C^alpha(h_x) genuinely unnecessary?
- For the low-order linear theory, yes: the frozen saddle, the source and the far window bound h in C^alpha (or
  C^alpha_p) by the forcing in the same class, without h_x.
- For the nonlinear closure, no. Lemma N (THEOREM, V030): for every 0 < alpha < 1 and every space controlling the local
  C^alpha norms of h and U[h] near a regular axis point, h -> L^{-1} N(h) is unbounded on C^alpha-bounded sets. Two
  crossing plane waves of amplitude n^{-alpha} interact exactly into -n^{1 - 2 alpha} sin(2 n y), and the transport
  inverse does not regain y-derivatives where V is parallel to e_1. Lemma N' (THEOREM, V030): inputs with bounded
  C^alpha graph norm can have ||N||_{C^alpha} >= c n, and so do the solutions.
- In the weak graph norm of the earlier diagnostic space, N is not even continuous at the certified modal source
  (THEOREM, V019).
- A sufficient high-norm requirement for a quasilinear scheme is a Lipschitz transport velocity V + W[h], that is
  D U[h] in L^infinity; the entries of D U[h] are Riesz products applied to d_x h. d_x h in C^epsilon with decay is
  sufficient. Necessity of a Lipschitz velocity is not claimed, and the equivalence with d_x h in C^alpha is REFUTED by
  a compact parity-compatible C^1 counterexample (V025, V038).
- Only conormal derivatives are needed across the axes, because W_1 = 0 on {x = 0} and W_2 = 0 on {y = 0}.

## 4. Avenue III: the singular functional c[h]

4.1 A saddle-adapted local weighted estimate.
- Characteristic geometry: the flow of the frozen field is Phi_s(x, y) = (x e^{-As}, y e^{Ds}), with invariant
  |x|^D |y|^A. The x-axis is incoming and the y-axis outgoing. On a box the sides x = +-R_x are inflow and the sides
  y = +-R_y are outflow. This is the opposite of an expanding model, where every side is outflow.
- Prop M (THEOREM, V034, at the detailed domain scope of the verifier's proof). For p in [1, inf), the product weight
  w = |x|^{-ap} |y|^{-bp} and an outflow cutoff phi(y), with kappa_w = 2 c_l/p + 1 - a V_1/x - b V_2/y,
     int kappa_w |h|^p w phi = - int ((V.grad - 1) h) |h|^{p-2} h w phi + (1/p) Flux_in + (1/p) int |h|^p w (-V_2 phi'),
  with Flux_in <= 0. If V_1/x < 0, V_2/y > 0 and Delta := inf kappa_w > 0 on the box, then
     N <= Delta^{-1} ||(V.grad - 1) h|| + (2 Vhat/(p Delta))^{1/p} ||h||_{L^p(S_R, w)},
  where S_R is the outflow shell. kappa_w(0) = kappa_0(p) = 2 c_l/p + 1 + A a - D b is the adjoint weight.
- The inflow flux has the good sign. The outflow flux is not small; after y-averaging it is a shell norm along the
  outgoing axis. Iterating in y does not close, because the flux is transported to the next block. The global answer
  at p = 2 is Theorem O.
- Explicit frozen strain bound, Corollary C1 (THEOREM, V034): for h with J = 0 and T_0 h = x^2 y gamma(log r) + f,
  |c_<[h]| <= 0.0027316 ||f||_R + 0.0136875 ||gamma||_G, so the constant is C_c0 < 0.013958 at a = 7/2, b = 6/5, and
  C_c0 < 0.017231 at a = 17/4, b = 0.
- Radial and isotropic moment estimates cannot be coercive at the x^2 y scale (THEOREM, V010: smooth compact packets
  with J = c = 0, unit moment norm, image moment tending to 0 and H^s norm tending to 0).
- NUMERICAL: with the actual field of rho~ on boxes Q_{2R}, the sign conditions hold and Delta stays within 26 percent of
  kappa_0 up to R = 1 (for example Delta = 13.03 at p = 2, a = 7/2, b = 6/5, R = 1). This is not yet a certified bound.

4.2 Absorbing the nonlocal velocity remainders.
- Exact strain cancellation: U[h] = c[h](-x, y) + U^(2)[h] near 0, and (U[h] + (c[h]/3) X).grad(x^2 y) = 0 exactly.
  On the y-axis the x^2 coefficient of the strain terms also cancels to leading order: with traces
  U_2[h](0, y) = c y + O(y^3) and d_x U_1[h](0, y) = -c + O(y^2), the combination is O(y^3).
- Parity Mellin subtraction: U_1 is odd in x and U_2 even. Subtracting x d_x U_1(0, y) and U_2(0, y) moves the
  admissible weight windows to (3/2, 7/2) and (1/2, 5/2), which is exactly 5/2 < a < 9/2 for the coupling (DERIVED,
  one-dimensional model).
- Strip estimate (THEOREM, V026, local-strip scope, 5/2 < a < 9/2, no weight in y). For inputs supported in |x| < R
  and a background with d_x rho = 2x rho_2(y) + x^3 r_1 and d_y rho = x^2 rho_2'(y) + x^4 r_2,
     ||U[h].grad rho - x^2 (2 rho_2 d_x U_1[h](0, .) + rho_2' U_2[h](0, .))|| <= eta(R) ||h||,
     eta(R) = 2 C_a R ||rho_2|| + C_a R^2 ||rho_2'|| + D_a R^3 ||r_1|| + D_a R^4 ||r_2||,
  with explicit C_a (C_a = 1759/6 at a = 7/2, about 593 at a = 17/4) and D_a. The axis traces are bounded and the
  localized jet coupling is compact. So the remainder is absorbed on thin strips, with an explicit O(R) rate.
- OPEN, together forming lemma (E): (E1) the weight in y and the coupling of dyadic y-blocks; (E2) the origin corner,
  including the traces near y = 0 in the jet target; (E3) input outside the strip with output inside it; (E4) the
  Garding part for the product of the angular factor and e^{mu}.

4.3 Reducing the rank-one term.
- c is bounded on a domain that carries the normalization (Prop C2, THEOREM, V034). With Z_cap := {h : chi_1 h in Z_0,
  h in L^2(e^{mu~})} and the norm of the sum,
     |c[h]| <= |J|/8 + C_v ||v||_G + C_R ||u||_R + C_> ||h||_{mu~} <= C_cap ||h||_{Z_cap},
  C_> < 0.273629, C_cap < 0.312093 at a = 7/2, b = 6/5 and C_cap < 0.359253 at a = 17/4, b = 0. The origin part cannot
  be dropped (V032).
- Rank-one bordering by the log direction (Prop B, THEOREM, V034, conditional on an operator domain X embedded in Z_cap
  with L_ren : X -> Y). Write (1 - chi_0) X.grad rho~ = k Phi_hat + g_far with Phi_hat = chi_inf r^k Theta_0 (not in
  the target) and g_far in the target. For h = h_0 + kappa KP, L h lies in the target if and only if
  kappa (3 c_l + k c[KP]) = -k c[h_0]. Then
     L h = L_red h_0 := L_ren h_0 + c[h_0] zeta,   zeta = (c_l g_far - k y_KP)/d,   d := 3 c_l + k c[KP],
  where L_ren carries the strain only near 0, combined with the coupling as in 4.2.
- Denominator (THEOREM, V034): 37.63077494715565 < s_3/pi < 37.63077494715567 for the far angular moment
  s_3 = int sin(3 theta) Theta_0, so c[KP] >= 0 and d >= 3 c_l > 0 for every smooth cutoff 0 <= chi_inf <= 1 supported
  in r >= 1.
- What d != 0 gives and does not give (THEOREM, V038): it permits the exact elimination of the tail coordinate. It
  does not invert L_red. If L_ren is invertible, L_red is invertible if and only if 1 + c[L_ren^{-1} zeta] != 0. If
  L_ren is Fredholm of index 0, so is L_red.
- Scalar normalization (THEOREM, V038). In the parametric form, nu(ell, h) := 3 ell - 1 - c[rho_bar_ell] - c[h] has
  d nu/d ell >= 3, so for every finite c[h] there is exactly one ell(h) > 1 with nu = 0, and
  |ell(h) - c_l| <= |c[h]|/3. At h = 0, d nu/d ell = k d. For independent (ell, h) the residual contains the forbidden
  origin jet (1 + J(h)) nu x^2 y; the augmented map (F - (1 + J(h)) nu H_0, nu), H_0 = chi_0 X.grad rho~/3, removes it,
  and its derivative at the base point is exactly the bordered system above (V038 for J = 0; V042 for a free cubic
  coordinate J, where subtracting only nu H_0 leaves J nu x^2 y outside the target).
- Dual criterion (THEOREM, V035): |c[h]| <= C ||L h|| holds if and only if c = L^* phi with ||phi|| <= C (Hahn-Banach).
  It does not need an inverse of L. If ||c - L^* phi|| <= delta and ||h|| <= A' ||L h|| + B' |c[h]| with delta B' < 1,
  then |c[h]| <= (||phi|| + delta A')/(1 - delta B') ||L h||. Actual adjoint solvability is OPEN.
- Status of |c[h]| <= C_c ||L h||_Y for the full operator: OPEN. The obstruction is (E) (velocity remainders and
  weighted elliptic bounds at the corner and along the outgoing axis) and the absence of a quantitative inverse. It is
  not the adjoint weight (explicit, kappa_0 > 0), not the inflow fluxes (good sign) and not the elimination of the tail
  coordinate (exact).

## 5. Avenue IV: finite-basis certification

5.1 Is the finite basis conforming? Yes, since a repair made during this run.
- The columns are degree-7 splines in t = log r with C^6 joins, joined to the inner and outer power laws by exact
  rational jet solves, times cos(2m theta), with the factor x^2 y. The coordinates J (x^2 y times an exact C^6 cutoff),
  KP and TAU (the truncated tail product) are explicit columns.
- Conformity criterion (THEOREM, V014): at an interface the image jumps by (V.n)[d_n h], so H^1-type conformity needs
  exact cancellation of the derivative jumps; rounded joins do not suffice. The earlier archived basis failed this
  (jumps 1e-22 to 1e-14), and its tail column omitted the nonzero mode-260 coefficient (V015). The repaired basis is
  confirmed in its test-space interpretation (V027).
- Exact objects: the trial in exact rational spline form, Green boundary data for 261 modes at all 1559 cell
  boundaries in 320-bit ball arithmetic, exact operator images of the columns with the origin cancellation built in and
  the compensated far column phi + dk KP, dk = -k c[phi]/d (V020 confirms the formula). A 42-mode identity test
  reproduces the expected image to 1.7e-46; it checks the machinery and bounds nothing.

5.2 Is the finite inverse certified? No.
- The first exact section S0 (4 angular modes, 169 columns plus TAU, KP compensation) is assembled. The certificate
  method (sigma_min(Q_M L P_N) >= s if K - s^2 G is positive definite, K = B^T (Z + Z^T - Z^T G_Y Z) B for any real Z)
  is confirmed (V020). The verified value is pending at this version. The strain values of its two tail columns and
  the bordering denominator are independently enclosed: c[KP_shifted] = 0.07037233698866423364..., c[TAU] =
  0.06854755426283814823..., 3/k + k c[KP_shifted] = 16.73870985167530795... (THEOREM, V043, 34-digit balls). The
  column uses the shifted logarithm log r - t_+; the unshifted log r column has strain 0.56103503149402952743...
- The earlier production sections have smallest singular values 0.41312, 0.52004, ... (H^1 rows) and 0.16978, ...
  (L^2 rows), reproduced to the printed digits (NUMERICAL). They are not continuum bounds (V014, V015).

5.3 Off-basis residual bounds.
- Method (DERIVED, structure confirmed in V020 and V027): with R such that E = R^{-T} G R^{-1} - I has ||E||_inf < 1,
  ||(I - Q_M) L P_N|| <= |t^|_2/(1 - ||E||_inf)^{1/2}, t^_i = sum_j |(R^{-1})_{ji}| t_j, t_j a bound for
  ||(I - Q_M) L u_j||. A naive bound with absolute coordinates is invalid (2 x 2 counterexample). Every image has finite
  angular bandwidth (the trial has 260 angular modes), so nothing is truncated.
- The interval code has been audited three times. Defects found and repaired: wrong density lookups (V027), a
  zero-straddling product before a square root, nearest-float conversions, discarded small positive endpoints and a
  missing velocity term (V033); the repairs are confirmed (V037), and the two remaining arithmetic obligations of V037
  are reported fixed, with re-audit pending.
- No off-basis bound has been computed at this version.

5.4 Is the complement controlled? No.
- In the realization used for S0 it cannot be (Prop IV.O, THEOREM, V039). There the domain variable is h/(x^2 y) with
  angular H^1 norm and the target is f/r^3. (i) L maps the domain into the closed subspace {f(0, y) = 0} of infinite
  codimension, so it is not onto. (ii) Zero-strain angular packets h_eps = x^2 y beta(t) phi((pi/2 - theta)/eps), with
  int e^{2t} beta = 0, satisfy ||L h_eps||/||h_eps|| <= C eps^2. So no uniform inverse bound holds in these norms, and a
  certified sigma_min of a finite section in this realization cannot be uniform in the angular dimension. Enlarging the
  basis cannot repair this.
- A complement estimate in a consistent realization reduces to checkable items (Lemma IV.1, THEOREM as a conditional
  statement, V040). Let L : D(L) -> H be closed and densely defined, with
  (G) m ||g|| <= ||L g|| + ||K g||, (S) K = K_S + sum_{i<=n} <., phi_i> e_i with ||K_S|| <= delta and e_i orthonormal,
  (A) psi_i in D(L^*) with ||L^* psi_i - phi_i|| <= eps_i.
  If delta + eps < m (eps, Psi the l^2 norms of eps_i and ||psi_i||), then ||g|| <= (1 + Psi)/(m - delta - eps) ||L g||,
  and if L is Fredholm of index 0 this is a bound for the inverse. For transport perturbations A = L + W.grad in the
  weight with angular factor |cos theta|^{-2a}, the adjoint defects grow by at most
  p_i = dW ||r grad psi_i|| + (2|c|/3 + (M + 4a) dW) ||psi_i||, dW = ||DW||_infinity, M = sup|mu'|, so one set of psi_i
  serves the whole correction ball.
- In L^2(e^{mu~}) on both sides (the realization of Theorem R), (G) is Theorem R once the margin is certified. The
  finite-rank split (S) with an explicit delta is OPEN; it is an analytic high-frequency statement, and a generic
  commutator gain does not give it. The adjoint defects (A) are a finite computation of the kind the exact pipeline
  does. This realization covers L_fix only (V032). For the normalized operator the realization must be the jet space of
  2.3 with its jet rows.

5.5 Does the combination give a genuine inverse theorem? No. A genuine inverse in this avenue needs, in addition to the
pending finite certificates, the margin certificate, the split constant delta, certified adjoint solutions psi_i and,
for the normalized operator, the jet realization of 2.3 together with (E).

## 6. Final closure

6.1 Is a complete nonlinear existence theorem established? No.

6.2 The precise missing estimate.
The first missing inequality is the edge Garding lemma (E) for the anisotropic weight w_a = |cos theta|^{-2a} e^{mu_a},
a = 17/4: for the Taylor-subtracted coupling T_R h (the coupling minus its x^2 jet along the y-axis),
     Re <T_R h, h>_{w_a} <= int (b_+ + eps) |h|^2 w_a + Re <K h, h>_{w_a},   K compact,
together with bounded y-axis traces U_2[h](0, .), d_x U_1[h](0, .) that are compact into the jet target after
multiplication by rho_2 and rho_2'. Its parts are (E1) the weight in y, (E2) the origin corner, (E3) input outside a
strip with output inside it, and (E4) the Garding part for |cos theta|^{-2a} e^{mu_a}. The strip piece is proved
(V026). In the precise form of Theorem C' (section 2.3), (E) consists of (E0) boundedness of the renormalized coupling
from Z to Y, (E-J) compactness of its jet part and (E-G) the Garding inequality above for its remainder part. With (E),
the axis hypothesis (A), the coefficient bounds (CB) and the margin, Theorem C' gives Fredholm index 0 for the bordered
operator on Z (DERIVED; its uncoupled endpoint is V046). The separated part of (E3) is proved (V045).
After (E), the remaining items, in order:
1. the margin (H_m') inf (kappa_{w_a} - b_+) > 0 on all of R^2 \ {0}, certified (grid value 3.0908);
2. injectivity of L_red on Z with a quantitative inverse bound (the complement estimate of Lemma IV.1: the split
   constant delta and certified adjoint solutions);
3. the high-norm inverse in a space with Lipschitz velocity (conormal derivatives at 0 and across the axes, H^s with
   s < 2373/680 at the source), compatible with the low-norm inverse;
4. the bilinear bound for W[d].grad h with the x^2 jet decomposition along the y-axis (the product has a nonzero x^2
   jet there, which must lie in the jet row of the target; the O(x^4) rest is admissible for a < 9/2);
5. a certified enclosure of the residual F(rho_bar_ell) in the forcing norm (its membership, axis jet included, is
   THEOREM, V042);
6. the application of the two-norm theorem of 6.3 to the moving-tail equation: its hypotheses must be proved for the
   augmented parametric map, with the ell-dependence of the compact part bounded, and not by updating ell after a
   fixed-background step (V038).

6.3 What is proved (THEOREMS; record numbers in brackets).
- Conventions and normalization: canonical velocity and normalized expansion [V002]; normalization and strain of the
  modal background [V005]; X3 defect [V018]; origin regularity C^{4,1} [V036]; exact quadratic expansion [V038].
- Origin: Theorem O with sharp constant 1/kappa_0, continuous J and continuous strain extension [V022]; frozen local
  strain adjoint K_A < 0.032162163072022018 [V016]; strip remainder and trace estimates [V026]; Prop M and
  Corollary C1 [V034].
- Source: unique certified source with mu != 1 [V017]; frozen nonlocal source inverse on H^s, s < 2373/680 [V011];
  auxiliary source inverse and strain norm [V021]; source neighbourhood margin [V024]; Hoelder source inverse at mu = 1
  and at the actual rate [V013, V029].
- Global: Theorem R for L_fix in radial weights, CONDITIONAL on (H_m) [V023, V031]; c not closable on that graph
  [V032]; necessary conditions N1 to N5 [V025].
- Normalization: Prop C2 (c bounded on Z_cap) and Prop B (bordering, conditional on the operator domain), with
  d >= 3 c_l > 0 [V034]; dual criterion [V035]; unique scalar normalization ell(h), |ell(h) - c_l| <= |c[h]|/3, and the
  augmented map [V038].
- Hoelder: H0 and S(a) to S(d), sharp thresholds [V028]; Lemmas N and N' [V030].
- Finite basis: conformity criterion and complement requirement [V014]; Prop IV.O [V039]; Lemma IV.1 with the
  transport extension, as a conditional statement [V040]; code audits [V020, V027, V033, V037].
- Abstract two-norm theorem [V038]: let X_H be reflexive and embedded in X_L, A_0 : X_H -> Y_L bounded,
  B : X_L x X_H -> Y_L bilinear with ||B(d, h)|| <= C_B ||d||_{X_L} ||h||_{X_H}, and for each v in the r-ball of X_H a
  compatible solution operator R_v of A_v = A_0 + B(v, .) with ||R_v||_{Y_L -> X_L} <= K_L, ||R_v||_{Y_H -> X_H} <= K_H
  and ||g||_{X_L} <= K_L ||A_v g||_{Y_L}. If K_H eta <= r and K_L C_B K_H eta < 1, with eta = ||f||_{Y_H}, then
  A_0 h + B(h, h) = -f has a solution with ||h||_{X_H} <= K_H eta, unique in the ball if K_L C_B r < 1.
- Axis row and target: the scalar y-axis row is an isomorphism B -> Gamma with explicit constants, conditional on a
  positive axis rate with endpoint bounds [V041]; the pure transport T = V.grad - 1 is an isomorphism from
  Z = E B (+) D(T_R) onto E Gamma (+) L^2_P(w_a) with the explicit triangular inverse, conditional on (A), the angular
  coefficient bounds (CB) and kappa_* > 0 [V046]; L_fix does not map Z into Y and c[.] H_0 is not a bounded perturbation
  into Y [V044, counterexample]; the separated outside-to-inside strip coupling is compact in w_a [V045]; the modal residual and the parametric residual lie in the jet target
  Y = E G (+) L^2_P(w_a), and the augmented map with a free cubic coordinate subtracts (1 + J) nu H_0 [V042].
- Obstructions with explicit counterexamples: V006, V007, V009, V010, V012, V019, V030, V032, V039, and the refuted
  parts of V025, V028 and V038.

6.4 Constants and inequalities that require numerical certification.

| Quantity | Needed for | Status |
|---|---|---|
| c[rho~] = 3/k - 1 | every rigorous statement | THEOREM (V005); independent ball recomputation agrees |
| source x_P, mu, g; neighbourhood margin | source inverse | THEOREM (V017, V024) |
| s_3/pi, hence d >= 3 c_l | bordering | THEOREM (V034) |
| C_cap, C_c0, C_> | c bounded | THEOREM (V034) |
| kappa_0, K_A, C_a | origin | THEOREM (V022, V016, V026) |
| m_* for mu~ in (H_m) | Theorem R unconditional for L_fix | grid 2.590 (NUMERICAL); box certificate in progress |
| m_a for w_a in (H_m') | Theorem C', scheme | grid 3.0908 (NUMERICAL); box certificate in progress; global only if no box fails |
| axis rate d = V_2(0, y)/y > 0 with endpoint bounds, hypothesis (A) | N2, axis row (V041), Theorem C' | NUMERICAL (5.58 to 21.31); box enclosure requested |
| lift constants M_Q = sup abs(a_1), M_P = sup min(r^2,1)^{-1} abs(a_0) of (CB) | Lemmas C'1 to C'3 (V046), Theorem C' | not computed |
| transport margin kappa_* = ess inf kappa_{w_a} | Lemma C'2 (V046) | not computed; the grid value of kappa_{w_a} - b_+ is 3.09 and b_+ >= 0 (NUMERICAL) |
| S0 tail-column strains and denominator 3/k + k c[KP_shifted] | S0 bordering | THEOREM (V043) |
| Delta on boxes near 0 (Prop M) | local strain estimate | NUMERICAL |
| sigma_min of finite sections, off-basis bounds | finite statements only | in progress (interval defects repaired, V037) |
| split constant delta, adjoint defects eps_i, norms of psi_i | Lemma IV.1, K_L | OPEN |
| eta (residual in the forcing norm, with axis jet) | closure inequalities | membership THEOREM (V042); value OPEN |
| K_H, K_L, C_B, C_V | closure inequalities | OPEN |
| r_V, from the margin perturbation bound stated below the table | ball radius | explicit once the margin is certified (DERIVED) |

The closure inequalities are K_H eta <= r, K_L C_B K_H eta < 1 and C_V r <= r_V. Here C_V bounds
||D W[h]||_infinity + |c[h]| by ||h||_{X_H}, and r_V is the perturbation size that keeps the weighted margin above half
its value. For w_a the margin changes by at most |c[h]|/3 + (1/2)(sup|mu_a'| + 4a) ||D W[h]||_infinity (DERIVED; the
angular term uses tan(theta) W.grad(theta) = sin(theta) W_2/r - sin(theta)^2 W_1/x and W(0) = 0). This is a pointwise
statement. It does not give the global flow portrait, which the Garding argument does not need.

6.5 The closest avenue and why.
The closest route combines Avenues I and III and uses Avenue IV only for the complement: the anisotropic jet space Z
with weight w_a, the coordinate J and the y-axis jet, the parametric tail ell with the augmented map, and a certified
finite-dimensional injectivity check (Lemma IV.1) for the compact part of the Garding estimate. Reasons:
1. Every frozen piece is proved with explicit constants: Theorem O at the origin, the source inverses, the far window.
2. The global Fredholm mechanism is proved for radial weights (Theorem R). It transfers to w_a once (E) is proved, and
   V026 already proves the strip piece of (E).
3. The normalization is handled exactly: c is bounded on Z_cap, the origin part is necessary (V032), the tail
   coordinate is eliminated exactly with d >= 3 c_l > 0, and the scalar normalization ell(h) is unique with an explicit
   Lipschitz bound. The reduced operator still needs its own inverse.
4. The grid margins have room (3.09 for w_a, 2.59 for mu~), against a perturbation cost that is linear in
   ||D W[h]||_infinity.
5. For a fixed background the compact part of the Garding estimate does not depend on h, so uniformity over the
   correction ball reduces to the h = 0 complement estimate plus the explicit transport defect of V040. In the
   parametric form the ell-dependence of the compact part must also be bounded.
Avenue II is farther: there is no Hoelder Garding inequality, the Hoelder theory of the actual transport near 0 is
open, and Lemmas N and N' show that Hoelder norms alone cannot close the nonlinear problem. Avenue IV alone is farther:
a finite section is not an inverse bound without a complement estimate (V014), and in the realization used so far it
cannot be one (V039).

6.6 Checklist against the strict standards.

| Standard | Status |
|---|---|
| Every inverse states its domain and range | Theorem O (Z_0 -> Y); Theorem R (maximal domain D_w -> L^2_P(w)); source inverses (maximal H^s domains); axis row (B -> Gamma, V041); pure transport (Z = E B (+) D_R -> Y = E Gamma (+) L^2_P(w_a), V046, conditional); Theorem C' (Z -> Y, DERIVED, conditional); Prop IV.O (maximal S0 domain) |
| Membership of perturbations and images | checked: x^2 y chi_0 in Z (J = 1); r^k Theta not in Z; the modal residual and the parametric residual in Y (V042); c bounded on Z (Lemma C'4, DERIVED); L_fix h not in Y for an explicit h in Z (V044), so the strain term is part of the coupling |
| Normalization meaningful and closed | J continuous on Z_0 (V022); c bounded on Z_cap (V034); c not closable on the radial graph (V032) and J not closed in weak norms (V012), so those spaces are not used for the normalization; ell(h) unique (V038) |
| Log variations of exponent perturbations | KP = chi_inf r^k log r Theta_0 carried explicitly; parametric family; log^2 second variation noted (V025) |
| No unproved finite rank, compactness or small residual used as invertibility | complied with; Fredholm statements are labelled as such, and injectivity is OPEN |
| Counterexamples where a bound fails | V006, V007, V009, V010, V012, V019, V025, V028, V030, V032, V038, V039; code defects V020, V027, V033, V037 |
| Absence of a proof is not nonexistence | complied with (section 0) |

## 7. Accompanying artifacts

- S2_L2_THEORY.md: Theorem O, N1 to N5, Lemmas G1 to G3 and Theorem R, the jet-compatible weight, the spaces Z and Y
  with Lemmas C'1 to C'4 and Theorem C',
  regularity bookkeeping, the obstruction audit.
- S2_CALPHA_THEORY.md: the Hoelder theory (H0, S(a) to S(d), the source, Lemmas N and N').
- S2_C_FUNCTIONAL.md: Prop M, Corollary C1, Prop C2, the renormalized coupling, Prop B and the dual criterion.
- S2_BASIS_CERTIFICATION.md: Avenue IV, Prop IV.O and Lemma IV.1; a detailed companion document records the exact
  pipeline and its runs.
- S2_NUMERICAL_CERTIFICATES.md: every numerical inequality with its enclosure, method and status.
- S2_CLOSURE.md: the nonlinear structure, the two-norm scheme, the missing estimates and the constants.
- S2_RESTART.md: inputs and their hashes, reproduction steps, and how to continue.
- The conventions file (CONVENTIONS), the code and data (artifacts directory), and the verification report with proofs and
  evidence for every record cited.

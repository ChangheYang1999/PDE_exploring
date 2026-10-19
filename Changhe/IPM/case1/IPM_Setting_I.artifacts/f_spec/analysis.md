# Lead analysis notes (IPM Setting I), v2 2026-10-17T18:19Z (v1 2026-10-17T18:08Z, kept as notes/analysis_v1_backup.md)

Status tags:
- [AUDITED-1]: checked once by the external referee (astra audit1, 2026-10-17T18:10Z), with its corrections incorporated.
  The verifier audit is still pending.
- [PROVED-lead]: a complete argument is written here but has not been audited.
- [CONDITIONAL]: the argument uses a stated hypothesis.
- [HEURISTIC]: not a proof.
Nothing here enters FINAL_REPORT.md before the verifier and an external audit have checked it.

Notation as in SPEC.md section 0. Q = {x>0, y>0}. Phi_s = flow of W. A_m = class A of SPEC.md section 2 with
rho in C^{m,alpha}_loc for some alpha in (0,1), m >= 2. Holder regularity makes U = U[rho] lie in C^{m,alpha}_loc as well
(see 1.2). Throughout, w(x) = W_1(x,0), h(x) = d_y W_2(x,0) and g(x) = rho_y(x,0).

## 1. Velocity law

1.1 (Bound on U) [AUDITED-1]. Let rho be C^1 with the parity of the problem and
 |rho(X)| <= C(1+|X|)^gamma, |grad rho(X)| <= C(1+|X|)^{gamma-1}, 0 <= gamma < 1.
 Define U(X) = lim_{R->inf} [ PV int_{|Y|<R} K(X-Y) rho(Y) dY ] - (0, rho(X)/2), with K = (K1,K2) of SPEC 0.
 Then the limit exists, locally uniformly, and |U(X)| <= C'(1+|X|)^gamma (no logarithm).
 Proof. Fix X with |X| = s >= 1 and split Y-space into three regions:
  A = {|X-Y| < s}, B = {|Y| < 2s} \ A, C_R = {2s <= |Y| < R}.
 On A: K has zero mean on circles centred at X, so PV int_A K(X-Y) rho(Y) dY = int_A K(X-Y)(rho(Y)-rho(X)) dY. This is bounded by
  int_{|Z|<s} |Z|^{-2} sup_{B_{2s}}|grad rho| |Z| dZ <= C s (1+s)^{gamma-1} <= C s^gamma.
 On B: |K(X-Y)| <= s^{-2}/pi, |B| <= 4 pi s^2 and |rho| <= C(1+2s)^gamma, giving <= C s^gamma.
 On C_R: write K(X-Y) = [K(X-Y) - K(-Y)] + K(-Y). The integral of K(-Y) rho(Y) over the annulus C_R vanishes identically:
  K1(-Y) = K1(Y) is odd in y1 while rho is even in y1; K2(-Y) = K2(Y) is even in y2 while rho is odd in y2; and the annulus is
  invariant under both reflections. For |Y| >= 2s, |K(X-Y) - K(-Y)| <= C s |Y|^{-3}. So the rest converges absolutely as R->inf
  and is bounded by C s int_{2s}^inf t^{-3} t^gamma t dt = C' s^gamma (this uses gamma < 1).
 For |X| <= 1 the same split with s = 1 gives a bound C. QED.
 Remarks.
 - The vanishing of the K(-Y) term is the precise reason why parity-symmetric data need no subtraction.
 - For gamma >= 1 the bound fails and growth alone does not fix the gauge (SPEC 7).
 - For gamma < 0 only U = O(1) holds in general: rho = x^2 y e^{-r^2} has U_1(R,0) ~ 1/(4R^3) (referee).

1.2 (Equations) [AUDITED-1, standard]. With psi defined mode-wise by V1, U = grad^perp psi, div U = 0 and curl U = -d_x rho in
 D'(R^2). U_1 is odd in x and even in y; U_2 is even in x and odd in y. Local regularity: if rho in C^{m,alpha}_loc then
 U in C^{m,alpha}_loc. This follows from local Schauder theory for the Calderon-Zygmund part; the far part is smooth in X.

1.3 (Uniqueness, V3) [AUDITED-1]. Suppose U' is another field with div U' = 0, curl U' = -d_x rho in D', U'_1 odd in x,
 U'_2 odd in y, and |U'(X)| = o(|X|). Then U' = U.
 Proof. D = U - U' has div D = curl D = 0 in D', so each D_i is harmonic and smooth. Then f = D_1 - i D_2 is entire. The Cauchy
 estimate |f'(z)| <= R^{-1} sup_{|w-z|=R}|f(w)| -> 0 gives f constant. D_1(0) = 0 (odd in x) and D_2(0) = 0 (odd in y), so f = 0.
 The harmonic field (-lambda x, lambda y) from psi -> psi + lambda x y violates o(|X|) unless lambda = 0. The odd/odd harmonic
 polynomials Im(z^{2n}) (n >= 1) all grow at least like r^2.

1.4 (Mode formula V1 equals 1.1) [AUDITED-1]. The sin(2n theta) mode psi_n of psi solves
 psi_n'' + psi_n'/r - 4 n^2 psi_n / r^2 = -f_n, with psi_n = o(r^2) at infinity and psi_n = O(r^2) at 0. The homogeneous solutions
 are r^{2n} (excluded at infinity) and r^{-2n} (excluded at 0). Variation of constants gives the Green formula of SPEC 3 (V1).
 Convergence of the differentiated modal series is supplied by the elliptic construction 1.1/1.2, not by the individual tail
 integrals (referee remark).

1.5 (Formula for c) [AUDITED-1]. Under (A1),(A3) alone, with rho_m(r) = (1/pi) int_0^{2pi} rho sin((2m+1)theta) d theta,
   c = psi_xy(0) = (1/2) int_0^inf f_1(s)/s ds = int_0^inf rho_1(s) s^{-2} ds - rho_y(0)/4.
 Under (A2), rho_y(0) = 0 and rho_1 = O(s^3) at 0, so
   c = int_0^inf rho_1 s^{-2} ds = (1/pi) int_{R^2} rho sin(3 theta) |X|^{-3} dX   (absolutely convergent).
 Proof. As r -> 0, psi_1(r) = (r^2/4) int_0^inf f_1/s ds + o(r^2). Indeed r^{-2} int_0^r s^3 f_1 = O(r^2 sup_{s<r}|f_1|) = o(r^2),
 since f_1 = O(s) (rho in C^2, odd/odd d_x rho). Since sin(2 theta) r^2 = 2xy, psi_xy(0) = (1/2) int f_1/s.
 The mode identity gives f_1 = (1/2)(rho_0' - rho_0/r) + (1/2)(rho_1' + 3 rho_1/r). Integrating by parts,
   (1/2) int f_1/s = (1/4)[(rho_0 + rho_1)/s]_0^inf + int rho_1/s^2.
 The upper boundary term vanishes because gamma < 1. At 0, (rho_0 + rho_1)/s -> rho_y(0), since rho_0 + rho_1 is the
 sin(theta)-weighted angular average, with leading term rho_y(0) s. Counterexample without (A2): rho = y e^{-r^2} gives c = -1/4.
 Numerical check (verifier): x^2 y e^{-r^2} gives c = 1/8, and x^2 y (1+r^2)^{(k-3)/2} gives c = 1/(4(1-k)).
 Check of the boundary value: near 0, rho = rho_y(0) r sin(theta) + O(r^2) gives rho_0 = rho_y(0) r + O(r^2) and rho_1 = O(r^2),
 so (1/4)[(rho_0 + rho_1)/s]_0^inf = -rho_y(0)/4 (lead re-derivation, 2026-10-17T18:20Z).

## 2. Characteristics and growth

2.1 (Lemma 1: forced regime and growth) [AUDITED-1, repaired proof]. Let rho in A_2 be nonzero, with gamma witnessing (A3).
 Then:
 - 0 < gamma < 1 and c_l >= 1/gamma > 1.
 - Every bounded forward orbit carries rho = 0.
 - If rho(X0) != 0, then e^{-c_l s} Phi_s X0 -> V != 0 and rho(Phi_s X0)/|Phi_s X0|^{1/c_l} -> rho(X0)|V|^{-1/c_l}.
 - Uniformly, |rho(X)| <= C(1+|X|)^{1/c_l}.
 Proof.
 (a) Global flow. |U| <= C(1+|X|)^gamma (1.1), so the flow is global. rho(Phi_s X0) = e^s rho(X0).
 (b) Excluding gamma <= 0 and c_l <= 1/gamma.
     - If gamma <= 0, rho is bounded, so rho = 0, contradicting (A2). Hence gamma > 0.
     - If c_l < 0, W points inward outside a large ball, so forward orbits are bounded and rho = 0.
     - If c_l = 0, then for every eps > 0, |U| <= eps|X| + C_eps, so |Phi_s X0| <= C_eps e^{eps s}. Then
       e^s|rho(X0)| <= C e^{gamma eps s}, which is impossible.
     - If c_l > 0, the same comparison with |Phi_s X0| <= C_eps e^{(c_l+eps)s} gives gamma c_l >= 1.
 (c) Sharp asymptotics. With q = 1 + |X(s)|, q' <= c_l q + C q^gamma gives q <= C e^{c_l s}. Outside a fixed ball,
     c_l r/2 <= r' <= 3c_l r/2. An orbit with rho(X0) != 0 cannot remain bounded, so it escapes, exponentially in radius.
     Then int |U(X(s))|/|X(s)| ds < inf, so log r(s) - c_l s converges. Also d/ds[e^{-c_l s}X(s)] = e^{-c_l s}U(X(s)) is integrable.
 (d) Uniform bound. Choose R0 such that the radial inequalities hold for r >= R0. For an orbit starting on {r = R0} and staying
     outside for time t, |log(r(t)/R0) - c_l t| <= C int_0^t r^{gamma-1} ds <= C'. This is uniform, so e^t <= C r(t)^{1/c_l}.
     Since rho is bounded on {r = R0}, |rho| <= C r^{1/c_l} outside B_{R0}.
 QED.
 Why the qualitative U = o(r) is not enough: psi = -xy/log(e+r^2) gives U = o(r), yet e^{-c_l s} x(s) is unbounded on the
 x-axis (referee).
 Corollary.
 - c_l > 1, so a class-A profile describes finite-time blowup, rho_phys = (T-t)^alpha rho(X/(T-t)^{1+alpha}) with alpha = 1/(c_l-1).
 - The best growth exponent is gamma = 1/c_l =: k.
 - From the uniform bound and the (A3) gradient bound: U = O(r^k log r) (referee).

2.2 (Center) [AUDITED-1]. Let rho in A_2. Then:
 - 3 c_l - c = 1, and DW(0) = diag(lambda1, lambda2) with lambda1 = c_l - c = 1 - 2 c_l < 0 < lambda2 = c_l + c = 4 c_l - 1.
 - The origin is a hyperbolic saddle. Its stable manifold is the x-axis near 0 and its unstable manifold is the y-axis near 0.
 Proof (finite regularity; referee's version). Rescale rho_eps(X) = rho(eps X)/eps^3 -> x^2 y and W(eps X)/eps -> DW(0) X locally
 uniformly. The distributional transport equation passes to the limit:
   DW(0)X . grad(x^2 y) = x^2 y,  i.e.  2(c_l - c) + (c_l + c) = 1.
 The invariant-manifold statements hold because the axes are invariant (parity) and tangent to the eigendirections, and the
 local stable and unstable manifolds of a hyperbolic saddle are unique.
 Remark: the special relations lambda1 = -(2c_l - 1) and lambda2 = 2(2c_l - 1) + 1 link the center to P (2.4):
 mu1(P) = -lambda1, mu2(P) = 1 = 2 lambda1 + lambda2.

2.3 (No cycles; alpha-limits) [AUDITED-1]. For rho in A_2:
 (i) B_{R0} is backward invariant for R0 large (X.W > 0 on |X| = R0), so every backward orbit is bounded.
 (ii) W has no periodic orbit and no graphic bounding a Jordan region D: int_D div W = 2 c_l |D| > 0, while the flux of W
      through the boundary is 0.
 (iii) IF W has finitely many zeros, the alpha-limit set of every point is a single zero of W (planar limit-set theorem, with
      (ii) excluding the alternatives).
 (iv) The closed quadrant cl(Q) and Q itself are invariant.
 (v) Index: on |X| = R large, W is homotopic to c_l X through nonvanishing fields. If the zeros are isolated, their index sum is +1.
     The origin is a saddle (index -1).
 Finiteness or isolatedness of the zero set is a HYPOTHESIS; it is not derived from A1-A4.

2.4 (First axis stagnation point; Lemma 3) [AUDITED-1, strengthened]. Let rho in A_2.
 W_1(x,0) < 0 for small x > 0 and W_1(x,0) >= c_l x - C(1+x)^gamma -> +inf, so x* := min{x > 0: w(x) = 0} exists. Put P = (x*,0).
 The axis ODE is w g' = (1-h) g, and w' + h = 2c_l. Then automatically:
 (a) g > 0 on (0, x*);
 (b) mu1 := w'(x*) = 2c_l - 1 > 1 and mu2 := h(x*) = 1, so P is a hyperbolic source and psi_xy(P) = 1 - c_l < 0;
 (c) g(x*) > 0.
 Proof. Set A = 2c_l - 1 > 1; the ODE reads g'/g = (w' - A)/w.
 (a) g ~ x^2 > 0 near 0, and g solves a linear first-order ODE with continuous coefficients on (0, x*), so g has no zero there.
 (mu1 = 0 is excluded) Approaching x* from w < 0 gives mu1 >= 0. If mu1 = 0, then |w(x)| <= eps (x* - x) near x* for any eps > 0,
  so g'/g >= A/(2 eps (x* - x)) and g -> inf, contradicting continuity.
 (b),(c) With t = x* - x: w = -mu1 t + o(t), so log g = alpha log t + o(|log t|) with alpha = (mu1 - A)/mu1 < 1. If g(x*) = 0, then
  g <= M t (g in C^1), contradicting the lower bound g >= c t^{alpha + delta} with alpha + delta < 1. So g(x*) > 0. Evaluating the
  ODE at x* gives h(x*) = 1, and the trace identity gives mu1 = A. Parity kills the off-diagonal entries of DW(P).
 Same statements at -P by symmetry.

2.5 (Positivity in the minimal configuration) [PROVED-lead, CONDITIONAL on (Hmin)]. Hypothesis (Hmin): the zeros of W in cl(Q)
 are exactly 0 and P. Equivalently: w has the single positive zero x*, W_2(0,y) > 0 for all y > 0, and W has no zero in Q.
 Then rho > 0 in Q, rho(0,y) = 0 and d_x^2 rho(0,y) > 0 for all y > 0.
 Proof.
 - Under (Hmin) and symmetry, the zero set of W is {0, P, -P}, which is finite. By 2.3(iii), alpha(X) is 0 or P for X in Q.
 - alpha(X) = 0 would put X on the global unstable manifold of 0, i.e. on the y-axis (the forward orbits of the local unstable
   manifold stay on the invariant y-axis). But X is in Q. So alpha(X) = P.
 - By 2.6, rho = C eta_P on the basin of P, with C = g(x*) > 0 and eta_P > 0 in Q near P. Hence rho(X) = e^s rho(Phi_{-s} X) > 0.
 - On the y-axis, rho(0,y) solves W_2(0,y) d_y rho(0,y) = rho(0,y) and vanishes near 0 by (A2). Since W_2(0,y) > 0, backward
   orbits on the axis reach small y, so rho(0,y) = 0 for all y > 0.
 - k(y) := d_x^2 rho(0,y)/2 solves W_2(0,y) k' = (1 - 2 d_x W_1(0,y)) k, with k ~ y near 0 (a(0) = 1). This needs rho in C^3
   near the axis, or the same rescaling argument as in 2.2. Hence k > 0.
 QED.
 Note: index count -1 (origin) + 1 + 1 (P and -P) = 1. So (Hmin) is consistent with 2.3(v); any further zeros must have total
 index 0.

2.6 (Fixed-W rigidity at P; replaces v1 2.6) [AUDITED-1]. Write W_2 = y b(X), so b(P) = mu2 = 1 and b - 1 = O(|X-P|^alpha). For X in
 the basin B(P) = {X : Phi_{-t} X -> P}, define
   I(X) = int_{-inf}^0 [b(Phi_t X) - 1] dt,   eta_P(X) = y exp(-I(X)).
 The integral converges, because backward orbits converge to P exponentially (rate >= 1) and b - 1 is Holder. Moreover
 eta_P(Phi_s X) = e^s eta_P(X). Every C^1 solution of W.grad rho = rho that vanishes on the x-axis satisfies rho = C eta_P on
 B(P) cap {y > 0}, with C = rho_y(P).
 Proof. On each orbit, y(s) solves y' = y b, so rho/y satisfies (rho/y)' = (1 - b)(rho/y). Integrate from t to 0 and let
 t -> -inf; rho/y -> rho_y(P) at P. QED.
 Interpretation: for fixed W, rho on B(P) is determined by the single constant C. The coupled problem is therefore a fixed
 point problem for W: rho = C eta_P[W], W = c_l X + U[rho].
 This is NOT uniqueness of the coupled profile.

## 3. Regularity at the center

3.1 (Axis hierarchy and Frobenius) [AUDITED-1 for the ODE, exponents and the necessary condition]. Let G_j(x) = d_y^j rho(x,0)/j!
 (j odd), W_1 = sum_{i even} W_1^{(i)}(x) y^i and W_2 = sum_{i odd} W_2^{(i)}(x) y^i, to the order allowed by regularity.
 Then on (0, x*):
   w G_1' = (1 - h) G_1,
   w G_3' + (3h - 1) G_3 = F_3 := -W_1^{(2)} G_1' - W_2^{(3)} G_1,
 with w = W_1^{(0)} and h = W_2^{(1)}. Forming the j-th equation classically needs rho in C^{j+1}.
 Near x = 0: w = lambda1 x (1 + O(x^2)), h = lambda2 + O(x^2). The G_3 ODE has a regular singular point at 0 with exponent
   p_3 = (3 lambda2 - 1)/|lambda1| = 6 + 2/(2c_l - 1),
 which lies in (6,8) for c_l > 1 and is never an even integer.
 Homogeneous solution: H(x) = |x|^{p_3} e^{E(x)}, with E even, E(0) = 0, smooth if W is.
 Proved:
 (i) If rho is C^infinity near 0, every solution is G_3 = G_3^{sm} + B_3 H with G_3^{sm} smooth and even. The Taylor recursion
     has denominators A(p_3 - 2n) != 0, with A = 2c_l - 1. Hence C^infinity implies B_3 = 0.
 (ii) Trace bound: rho in C^m implies G_3 in C^{m-3}. A noncancellable B_3 != 0 therefore rules out C^10 (p_3 <= 7) and
      C^11 (7 < p_3 < 8).
 (iii) For general odd j = 2l+1, p_j = 4l + 2 + 2l/A. p_j is even exactly when l/A is an integer, so infinitely many j are
       nonresonant and each gives a necessary condition B_j = 0. Resonant j can force extra conditions that exclude logarithms.
 NOT proved: the 2D statement that B_3 != 0 implies "not C^7/C^8". The referee's counterexample x^2 y + B x^2 y^3 r^{p-2} has
 the same G_3 but is C^9; it is not a solution of the PDE. A saddle-passage argument (3.3) would be needed.

3.2 (B_3 as a functional of the axis data) [PROVED-lead, CONDITIONAL on rho in C^4 near [0, x*] x {0}; the sign convention is
 to be checked numerically, scripts/b3_diag.py].
 Near P, mu1 = A and mu2 = 1, so the homogeneous solution of the G_3 equation behaves like |x - x*|^{-(3 - 1)/A} = |x - x*|^{-2/A},
 which is unbounded. Boundedness of G_3 at P fixes G_3 on (0, x*):
   G_3(x) = H(x) int_x^{x*} [ -F_3(t) / (w(t) H(t)) ] dt,   0 < x < x*.
 Here H(x) = exp(int_{x0}^x (1 - 3h)/w) on (0, x*), normalized so that H(x) ~ x^{p_3} as x -> 0+. The integrand is
 O(|t - x*|^{2/A - 1}) at x*, which is integrable.
 As t -> 0+, -F_3/(wH) ~ t^{1 - p_3}(c0 + c2 t^2 + ...) times smooth corrections, so the integral diverges like x^{2 - p_3}.
 Write it as a finite part plus the divergent terms; the divergent terms reproduce the smooth even series G_3^{sm}. Then
   B_3 = f.p. int_0^{x*} [ -F_3(t)/(w(t) H(t)) ] dt.
 Since p_3 is not an even integer, no logarithm appears and the finite part is unambiguous.
 Diagnostic use: B_3 needs only w, W_1^{(2)}, h, W_2^{(3)} and G_1 on [0, x*]. These are 1D traces of the computed fields.
 B_3 depends on the normalization of H; with H ~ x^{p_3}, it is the coefficient of x^{p_3} in G_3.

3.3 (Transversal formulation of the C^infinity condition) [PROVED-lead for the formal part; CONDITIONAL on C^infinity
 linearization at the saddle].
 Suppose W is C^infinity near 0, and (xi, eta) are C^infinity linearizing coordinates near 0, symmetric with xi odd in x and eta
 odd in y. They exist for an already smooth profile (verifier/astra lemS, not yet checked in full by the lead), and by Sternberg
 under non-resonance. In these coordinates W = lambda1 xi d_xi + lambda2 eta d_eta.
 Let Sigma_0 = {xi = 1}, a transversal to the x-axis near 0, inside B(P). Let F(eta) := eta_P|_{Sigma_0}; it is odd in eta and
 F'(0) > 0. Every solution of W.grad rho = rho that vanishes on the x-axis has the form
   rho(xi, eta) = |xi|^{1/lambda1} Fhat(eta |xi|^{-lambda2/lambda1})  near 0, with Fhat = C F.
 If F(eta) = sum_j F_j eta^j, this gives rho = C sum_j F_j eta^j |xi|^{p_j}, with p_j = (j lambda2 - 1)/|lambda1|.
 Hence, in the non-resonant case, rho in C^infinity near 0 iff F is LINEAR. Up to the smooth change of coordinates, this is
 B_j = 0 for all odd j >= 3.
 In words: the eigenvalue-1 Koopman eigenfunction eta_P of the source P must coincide, near the saddle, with a multiple of the
 saddle eigenfunction xi^2 eta. The function eta_P/(xi^2 eta) is a first integral of the flow on the overlap of the two charts
 (eigenvalues 1 - (2 lambda1 + lambda2) = 0). The C^infinity condition says this first integral is CONSTANT.
 Other invariants: xi_P xi (eigenvalue A - A = 0) and eta |xi|^{2+1/A}. The x-axis segment (0, x*) is a heteroclinic orbit, and
 along it xi_P xi is constant.
 Consequence for the whole y-axis: if F_3 != 0, the term C F_3 eta^3 |xi|^{p_3} is transported along the unstable manifold (the
 y-axis). So rho has a |x|^{p_3}-type singularity across the whole positive y-axis, i.e. |pi/2 - theta|^{p_3} in angle, at every
 radius. Spectral methods in theta then converge algebraically.

3.4 (Counting) [HEURISTIC]. Normalize the scaling symmetry by x* = 1 instead of a(0) = 1. The remaining scalar unknowns are the
 amplitude C = rho_y(P) and c_l. The fixed-point map rho -> C E[W] is defined for every W with a source on the axis. Here
 E[W] = (eta'_P)^{1/mu2} and eta'_P is the eigenvalue-mu2 eigenfunction. It needs two scalar conditions:
 mu2(P) = 1 (C^1 at P) and 3c_l - c = 1 (x^2 y at 0). Two unknowns and two conditions suggest isolated A_2 profiles, as in the
 wall problem. The conditions B_3 = B_5 = ... = 0 then have no parameter left. So the expectation is that A_2 profiles exist but
 are not C^infinity. This is NOT a theorem: there is no existence, independence or nonvanishing proof. A hidden identity forcing
 B_j = 0 is not excluded. It must be tested by measuring B_3.
 Contrast with the wall problem (Wang et al.): there the origin is a source, rho ~ x^2 is the unique smooth eigenfunction, and
 no data passes through a saddle. So the wall problem has no analogue of the B_j conditions at the center. In Setting I the
 cubic odd-y normalization makes the origin a saddle (lambda1 = 1 - 2c_l < 0 for c_l > 1/2).

3.5 (What a B_3 measurement can and cannot see) [HEURISTIC, numerical analysis; lead 2026-10-17T20:38Z; not audited].
 (a) Residuals do not decide the class. |x|^{p_3} with p_3 = 6.197 is approximated by even polynomials of degree 2n on
     [-1, 1] with error of order n^{-p_3} (about 3e-8 for n = 16). So a smooth field and a field with B_3 != 0 can both
     have normalized residuals of 1e-6 away from a neighbourhood of 0 whose size shrinks with n. A small residual is not
     evidence for B_3 = 0 or for B_3 != 0. In a trial space that contains both smooth functions and B H, the coefficient
     of H is not determined by the residual: the smooth part absorbs (B_true - B_ansatz) H on [r0, x*] and the mismatch is
     pushed into r < r0. This is consistent with construct1: its origin layer at r0 = 0.153 and its B3_ansatz = 0.046
     natural units, against 0.31 from the axis traces.
 (b) The finite part is well conditioned for smooth errors and badly conditioned for localized ones. A smooth global
     relative error eps in the axis data changes B_3 by O(eps) natural units. An error of relative size eps localized at
     scale l changes it by about eps (l/x*)^{2 - p_3} / A natural units (for construct1, l/x* = 0.0174 gives a factor of
     about 2e6). So the measurement needs axis data whose error near 0 decays like (r/x*)^{p_3 - 2} or faster, or a low-degree
     least-squares fit (b3_ls) that smooths through a layer. With the w-only data on construct1, delta = 0.3 drifts as the
     degree grows from 8 to 16 (0.31 to 0.11), as expected once the fit starts to follow the layer or the noise; delta = 0.5
     stays at 0.30 to 0.34.
 (c) The w-only route (7.3) uses only w = W_1(x, 0), a nonlocal and smoothing functional of rho. But a2 = (g' - w'')/2
     and b3 = -a2'/3 contain w'' and w''', so B_3 is a very sensitive functional of w. Measured with
     scripts/b3_wonly_perturb.py on construct1 (2026-10-17T20:40Z): replacing w by w (1 + eps s^2 e^{-s^2}), s = x/l, eps = 1e-6,
     changes the w-only value (natural units; delta 0.4 and 0.5, degree 10 to 14) by
       l = 4: 9e-4;  l = 1.5: 1.2e-2 to 2.1e-2;  l = 0.5: 0.08 to 1.8;  l = 0.15: 0.23 to 3.9,
     and linearly in eps (the eps = 1e-8 runs give 1/100 of these, up to noise at l = 4). The scaling estimate of (b)
     underestimates this by 10^2 to 10^3 for l >= 0.5 (it ignores the derivatives of w in a2, b3). For l <= 0.5 the
     response depends on the fit degree, so the low-degree fit only regularizes; it does not remove the sensitivity.
     Consequence: a w-only value with an error of 0.03 natural units needs w to a relative accuracy of about 1e-6 at
     x ~ 1.5 and near P (a relative change 1e-6 of w within 1 of P moves the value by 0.019), and 1e-8 to 1e-7 at x <= 0.5.
     Convergence within construct1's basis family (2026-10-17T20:44Z, scripts/b3_wonly_perturb2.py): after removing the uniform
     factor A, w changes between the degree-160 and degree-200 exports by 2.5e-11 (x = 0.05), 1.9e-10 (0.15), 2.8e-9
     (0.5), 5.2e-9 (1.5), 1.1e-7 (4), 1.6e-6 (8, next to P). The w-only values (delta 0.4 and 0.5, degree 10 to 14) are
     0.14 to 0.19 (degree 80), 0.29 to 0.32 (120), 0.29 to 0.33 (160), 0.28 to 0.32 (200). So within the family the value
     is converged to about 0.01, with a spread of 0.04 over (delta, degree): 0.30 +- 0.03 natural units.
     Why w is so much more stable than the rho jets: U is an order-zero operator of rho, so a local relative error eps of
     rho at scale l changes w (of size A l) by a relative amount of about eps l^2 / A.
     Not excluded: an error common to the whole family (same trial structure, including the origin layer). So 0.30 +- 0.03
     is an estimate of the B_3 of an exact solution near construct1, not a measurement with a controlled error. The
     jet-based value agrees with it, but both routes share w and h. The decisive test is an independent solver.
     (Lead log: a first version of this item, 20:41Z, called the error bar possibly O(1) natural unit before the
     convergence check; that was too pessimistic and is replaced by the text above.)
 (d) Away from the origin, B_3 != 0 shows up only as the |cos theta|^{p_3} term across the whole y-axis (3.3). Along
     the y-axis the coefficient B(y) of |x|^{p_3} solves the homogeneous equation v B' + (p_3 omega - 1) B = 0, with
     v = W_2(0, y) and omega = d_x W_1(0, y). So B(y) has the sign of B_3 for all y > 0, and B(y) ~ y^{k - p_3} at
     infinity, k = 1/c_l. Fitting this term is as ill conditioned as (a); the axis finite part stays the primary route.
 (e) Two further within-solver checks (lead 2026-10-17T20:56Z; HEURISTIC).
     Singular-off trial space. The construct3b checkpoint s0_deg120 (chunk 2; degree-120 order-7 splines x 101 cosines,
     no singular functions, so the trial's own B_3 is exactly 0) gives w-only 0.31 to 0.34 and jet-route 0.31 natural
     units, c_l = 5.5763397, and w equal to construct1's to 7e-10 at x <= 0.15 and 3e-9 at x <= 1.5. By the D12 identity
     the whole 0.31 is then carried by the G_3 defect integral. This shows the value is not produced by the explicit
     singular functions, but it is a weak control: construct3b's projection shows the regular basis represents the
     singular-six H to 2.7e-9 on the grid, and the trial is genuinely smooth only below the first knot (q = 2.1e-3,
     r about 0.55), where the |x|^p3 y^3 term is at most about 1e-6 relative to x^2 y. It confirms (a) more than it tests B_3.
     Empirical residual-to-w calibration in construct1's family (REPORT table of max normalized residuals against the w
     difference from the degree-200 export):
       basis     R (r <= 2)   R (2 <= r <= 10)   dw/w at 0.5   dw/w at 1.5   w-only B_3 (delta 0.4/0.5, deg 8-12)
       80x60     6.0e-7       2.1e-4             -5.2e-7       -3.1e-6       0.15 to 0.19
       120x100   9.7e-8       8.4e-5              2.5e-8        3.0e-7       0.31 to 0.34
       160x100   8.1e-8       2.8e-5             -2.8e-9       -5.2e-9       0.31 to 0.34 (assess log)
       200x100   1.0e-7       1.8e-5              0             0            0.30 to 0.34
     The w error at x = 1.5 is about 1.5e-2 times the near-P residual at degree 80. If the same ratio held for the final
     export it would give dw/w about 3e-7 at 1.5 and 4e-8 at 0.5, i.e. a B_3 change of at most about 0.07 natural units
     by (c). This is an extrapolation within one solver family, not an error bound.

## 4. Exact identities (diagnostics)

4.1 (Weighted identities) [AUDITED-1]. Let phi be homogeneous of degree -d, smooth on the circle, and k + 2 < d < 5 with
 k = 1/c_l. Then
   (1 + (2 - d) c_l) int rho phi dX + int rho U.grad(phi) dX = 0.
 Proof: integrate div(rho W phi) = rho phi (2 c_l) + rho W.grad phi + phi W.grad rho over eps < |X| < R, and use W.grad rho = rho
 and X.grad phi = -d phi. Near 0 the boundary terms are O(eps^{5-d}). At infinity, by the uniform bound of 2.1 and |U| = O(r^gamma)
 with gamma close to k, they are O(R^{k+2-d}) and O(R^{k+gamma+1-d}).
 With phi = sin(3 theta) r^{-3}: int rho phi = pi c by 1.5, so pi (1 - c_l) c + int rho U.grad(phi) dX = 0, i.e.
   int rho U.grad(sin 3theta / r^3) dX = pi (c_l - 1)(3 c_l - 1) > 0.
4.2 (Invariant density) [PROVED-lead]. div(W F(rho)) = 2 c_l F + rho F'. In particular div(W |rho|^{-2 c_l}) = 0 where rho != 0.
4.3 (Consequences for the numbers) [follows from 2.2, 2.4]. c = 3 c_l - 1 > 2, psi_xy(P) = 1 - c_l < 0 and mu1(P) = 2 c_l - 1.
 The strain psi_xy changes sign on (0, x*).
4.4 (Sign of c under positivity) [PROVED-lead, trivial]. If rho > 0 in the upper half plane, then
   c = (4/pi) int_Q rho sin(3 theta) r^{-3} dX > 2.
 In Q, sin(3 theta) > 0 for theta < pi/3 and < 0 for pi/3 < theta < pi/2. So the weighted mass rho r^{-3} in the sector
 theta < pi/3 must dominate that in pi/3 < theta < pi/2: the profile concentrates toward the x-axis. No contradiction follows.

## 5. Problem variants and what each endpoint would mean

 P_inf (the prompt's strong setting): rho classical on R^2, and near 0, rho = x^2 y a with a in C^infinity, even/even, a(0) = 1.
   NO in P_inf would need B_j != 0 for EVERY A_2 profile (3.1, 3.3). No route to a proof is visible, and a computer-assisted
   enclosure of one profile would not exclude others. YES in P_inf would need numerical evidence that B_3 = 0 (and ideally
   B_5 = 0) to the accuracy of the computation. That is a non-generic outcome.
 P_m (distinguished weaker problem): rho in C^{m,alpha}_loc, with rho = x^2 y a near 0, a continuous and a(0) = 1. A profile with
   B_3 != 0 would lie in P_m only for m <= 10 at most (trace bound), and its expected regularity is C^6 or C^7 (unproved in 2D).
   In it, a = 1 + O(r^2) + B y^2 |x|^{p_3 - 2} + ..., so a in C^4 but not C^infinity near the center.
 Any YES must state which variant it addresses.

## 6. What would be needed for a NO theorem (open)

 - In A_2: no contradiction found. Positivity (2.5), the selection mu2(P) = 1 (2.4) and the counting 3.4 are consistent with
   existence.
 - In A_infinity: one would have to show B_3 != 0 (or some B_j != 0) for every A_2 profile. This is a global property of an
   unknown solution; no route to a rigorous proof without computer assistance is visible.
 - Out of class (c_l <= 1): requires a gauge rule; see SPEC 7.
 - Rigorous partial results available now (to be audited by the verifier):
   (a) no nonzero profile in class A with c_l <= 1, nor with gamma <= 0 (2.1);
   (b) center relation and saddle structure (2.2);
   (c) automatic source P with mu2 = 1 (2.4);
   (d) fixed-W rigidity (2.6);
   (e) positivity under (Hmin) (2.5);
   (f) the necessary conditions B_j = 0 for C^infinity (3.1);
   (g) the weighted identities (4.1).

## 7. Audit2 outcomes and new axis identities (2026-10-17T18:49Z)

7.1 Audit2 (astra, collected 18:45Z) verdicts on v2:
- 2.2, 2.3: CORRECT (finiteness of the zero set remains a hypothesis). Rescaling proof of 3c_l - c = 1 needs only continuous a
  and W in C^1 (weak form).
- 2.5 (positivity in Q under Hmin, rho = rho_y(P) eta_P): CORRECT WITH REPAIR, valid in A_2. Repair for the y-axis
  curvature: k(y) = rho_xx(0,y)/2 satisfies k(y_t) J(t)^2 = e^t k(y_0) along axis orbits, J = exp int W_{1,x}(0,y_s) ds, so
  k > 0 on the whole positive y-axis (needs only C^2). Positivity is in Q, not the whole upper half plane.
- 3.2: bounded branch at P CORRECT; the finite-part formula at 0 is CONDITIONAL on smooth axis data, or at least on an explicit
  expansion K = k0 + k2 x^2 + k4 x^4 + O(x^6) of the even integrand factor. C^4 alone does not give it (axis-ODE example
  with b3 = -|x|^{p-2}, which produces a |x|^p log|x| term).
- b3_diag.py: odd FFT coefficients (spurious, ~1e-10) were divided by 7 - p3, giving gross errors near c_l = 3/2
  (0.095 instead of 0.667 at c_l = 1.49999999). FIXED (b3_diag.py edit before 18:49Z): exact evenness is enforced (odd coefficients zeroed), the
  measured odd content is still reported. New results (notes/b3_diag_test_out_v2.txt): rel err 5e-10 at c_l = 1.3, 8.6e-11 at
  1.49999999, 4.9e-10 at 1.5, 5.0e-11 at 1.50000001, 3.0e-10 at 2.2; smooth target 3e-10.
- 3.3: the representation rho = |xi|^{-1/A} F(eta |xi|^q) is CORRECT; "smooth implies F linear" is WRONG (counterexample
  F(s) = s + s exp(-1/s^2); and resonant terms at special A). Correct statement: C^infinity iff F_j = 0 for every odd j with
  p_j not in 2N. Conditional sharp regularity theorem: if the linearizing chart and F are C^m, m = ceil(p3), and F_3 != 0,
  then rho is C^{floor p3, p3 - floor p3} and not C^{ceil p3} (p3 = 7: C^{6,1}, not C^7). Linking F_3 to the physical B_3 and
  getting a smooth enough chart for a finite-regularity coupled profile is NOT done. Note: if W is smooth near 0 then rho is
  smooth near 0 (rho_x = -curl W and rho(0,y) = 0), so a rough coupled profile has a rough field: the illustrative smooth-field
  computation does not directly apply.
- 3.4 and 5: heuristic status appropriate. "C^1 forces mu2 = 1" is false without g(P) > 0 (that is what Lemma 3 uses).
  Section 5 repairs: nonvanishing of a forbidden coefficient is one possible NO strategy, not a necessary one; the P_inf
  definition (smooth only near 0) is weaker than A_infinity unless a propagation theorem is supplied.
- 4.2: correct on {rho != 0}, no finite invariant measure across the axes. 4.4: c > 2 comes from c = 3c_l - 1 and c_l > 1, not
  from positivity. 1.1: the gradient estimate on B_{2s} must avoid the origin (use |X - Y| < s/2); the velocity bound survives.

7.2 Exact axis constraints (from div W = 2c_l and curl U = -rho_x, expanded at y = 0; audit2, rederived here):
   w' + h = 2c_l,   a2' + 3 b3 = 0,   h' - 2 a2 = -g',   hence a2 = (g' - w'')/2,
with w = W_1(x,0), h = d_y W_2(x,0), a2 = d_y^2 W_1(x,0)/2, b3 = d_y^3 W_2(x,0)/6, g = rho_y(x,0).

7.3 [PROVED-lead, numerically checked; audit3 (19:22Z): CORRECT WITH REPAIR, see 9.1] Closed form of the homogeneous solution and a w-only formula for B_3.
 Let A = 2c_l - 1. On (0, x*), g'/g = (w' - A)/w (the G_1 equation with h = 2c_l - w'). Then
   H := N g^{3 + 2/A} |w|^{-2/A},  N = A^{2/A} / g0^{3 + 2/A},  g0 = lim g/x^2 (= a(0) = 1 under the normalization),
 solves w H' + (3h - 1) H = 0 and H ~ x^{p3} at 0. Proof: w H'/H = (3 + 2/A)(w' - A) - (2/A) w' = 3w' - 3A - 2 = 1 - 3h.
 With b3 = -a2'/3: -F3 = a2 g' + b3 g = -(g^4/3)(a2/g^3)', so on (0, x*), with m := |w|/g,
   -F3/(w H) = (1/(3N)) (a2/g^3)' m^{2/A - 1},    m'/m = A/w,
 and therefore
   B_3 = (1/(3N)) f.p. int_0^{x*} (a2/g^3)' m^{2/A - 1} dx,   a2 = (g' - w'')/2.
 So B_3 is a functional of c_l and the single axis function w(x) = W_1(x,0) on [0, x*] (g is obtained from w by quadrature,
 with g0 = 1). At A = 2 (c_l = 3/2) the integrand is a derivative and B_3 = a2(P)/(6 g(P)^3) (g0 = 1), as in audit2.
 For 1 < A < 2 an integration by parts gives B_3 = -((2 - A)/(3N)) f.p. int_0^{x*} a2 g^{-3} m^{2/A-1} / w dx (the boundary
 term at x* vanishes since m(x*) = 0 and 2/A - 1 > 0; at 0 its finite part vanishes for non-integer 2/A - 1).
 Checks: scripts/test_b3_compatible.py (audit2 data at c_l = 3/2: b3_fp gives -1.000000009, exact -1; identity
 a2(P)/(6 g(P)^3) = -1) and scripts/test_b3_wonly.py (c_l = 1.3, 2.2, compatible data built from w alone: H identity and
 integrand identity hold to 3.6e-6 and 3.0e-6, a constant offset that is the error of the numerical g0).
 Consequence for diagnostics: an accurate w on [0, x*] (with w'' and w''') is enough to evaluate B_3. No sign of B_3 follows:
 a2 has no a priori sign.

## 8. The limit c_l -> infinity is degenerate (2026-10-17T19:07Z) [PROVED-lead; audit3 (19:22Z): Lemma 8 CORRECT, sequence use CONDITIONAL, see 9.2]

Purpose: several solvers (astra least squares, lead PTC) drift to large c_l, others to c_l < 1. Lemma 1 already excludes
c_l <= 1 in class A. This section shows that c_l = infinity is not a limit point at which a nontrivial profile survives,
under convergence strong enough to pass to the limit in the equation and in c = psi_xy(0).

8.1 Rescaling. Put eps = 1/c_l and F = eps rho. Since U is linear in rho, U[F] = eps U[rho], and W.grad rho = rho becomes
   (X + U[F]).grad F = eps F,     psi_xy[F](0) = eps c = 3 - eps   (from 3c_l - c = 1).
So a sequence of solutions with c_l -> infinity, normalized this way, can only converge to a solution of
   (L)  (X + U[F]).grad F = 0,   F even in x and odd in y,   psi_xy[F](0) = 3.
(The cubic jet of F is eps x^2 y -> 0: the normalization a(0) = 1 does not survive; c_F = 3 does.)

8.2 Lemma 8. Problem (L) has no solution F in C^1 with U[F] in C^1, U[F](X) = o(|X|) as |X| -> infinity, and finitely many
zeros of V := X + U[F].
Proof. (i) div V = 2 since div U = 0. (ii) On |X| = R, V.X >= R^2 - |U| R > 0 for R large, so V points outward on that circle and a backward orbit that starts
in the closed disc of radius R stays in it. Every point lies in such a disc, hence every backward orbit is bounded.
(iii) No periodic orbit: if Gamma were one, bounding the region D, then 0 = flux of V through Gamma = int_D div V = 2|D| > 0.
The same flux argument excludes a graphic (a closed curve made of equilibria and connecting orbits that bounds a region),
since V is tangent to such a curve away from finitely many points.
(iv) By (ii), (iii) and the Poincare-Bendixson theorem for flows with finitely many equilibria, the alpha-limit set of every
point is a single equilibrium E(X).
(v) V.grad F = 0 means F is constant on orbits; by continuity F(X) = F(E(X)). Hence F takes finitely many values on R^2.
A continuous function with finitely many values on the connected set R^2 is constant. F is odd in y, so F = 0, and then
psi_xy[F](0) = 0, contradicting psi_xy[F](0) = 3. QED.

8.3 Remarks.
- Lemma 8 is the bounded-density case of the self-similar ansatz (k = 1/c_l = 0: rho(t,x) = F(x/(T-t))); it says that no
  exactly self-similar IPM profile of this type with a C^1 velocity, sublinear growth and finitely many stagnation points
  exists. It uses neither the symmetry class beyond oddness in y nor positivity.
- It does not give a bound on c_l for actual solutions: it says only that solutions with c_l -> infinity cannot converge
  (in C^1_loc, with uniform control of the far field sufficient to pass to the limit in U and in psi_xy(0)) to a profile.
  A numerical iteration whose c_l grows without bound is therefore not converging to a profile; it is drifting toward this
  degenerate limit.
- Hypotheses to be checked by an auditor: the use of Poincare-Bendixson with finitely many equilibria on the whole plane
  (the alpha-limit of a bounded backward orbit is an equilibrium, a periodic orbit, or a graphic); the flux argument for a
  graphic; continuity of F at E(X) (F is C^1).

## 9. Audit3 outcomes (astra, collected 2026-10-17T19:22Z)

9.1 Section 7.3: CORRECT WITH REPAIR.
- (a) H identity and normalization N = A^beta / g0^{3+beta}, beta = 2/A: correct.
- (b) -F3/(wH) = (1/(3N)) q' m^{beta-1}, q = a2/g^3, m = |w|/g, m' = -A/g: correct, sign included.
- The finite part needs smooth axis data or the explicit expansion I = x^{1-p}(k0 + k2 x^2 + k4 x^4 + O(x^6)) (remainder
  O(x^{1-beta}) integrable); then B_3 = lim [int_eps^{x*} I + sum_{j=0}^{2} k_{2j} eps^{2-p+2j}/(2-p+2j)], no logarithm
  (no vanishing denominator for 0 < beta < 2). C^4 alone remains insufficient (audit2).
- IBP form for 1 < A < 2: correct (upper integrand O((x*-x)^{beta-2}), integrable). For A > 2 the boundary term at P
  diverges; the IBP form must not be used there.
- A = 2: B_3 = g0^4 a2(P)/(6 g(P)^3) = w''(P)(g(P) - 2)/(24 g(P)^3) (g0 = 1), using A g'(P) = w''(P) g(P).
- Test scripts: correct as diagnostic checks only (no assertions; the g-ODE residual is zero by construction in
  test_b3_wonly.py; its g is clipped below 1e-3, the diagnostic extrapolates from interior samples). The comment on the
  normalization in test_b3_compatible.py is misleading (there H = 2 g^4/|w| with the same normalization).

9.2 Section 8: Lemma 8 CORRECT. Cleaner proof (adopted): complete flow, outward on large circles, so backward orbits are
trapped; no invariant Jordan curve since det D Phi_t = e^{2t} (area of the enclosed invariant region would grow); by the
elementary Poincare-Bendixson theorem every alpha-limit set contains an equilibrium E; F(Phi_t X) = F(X) and continuity
along a subsequence Phi_{t_n} X -> E give F(X) = F(E); F takes finitely many values, so F is constant, hence 0 by oddness,
contradicting psi_xy[F](0) = 3. (Only an equilibrium subsequence is needed, not convergence of the full backward orbit.)
Application to sequences with c_l -> infinity: CONDITIONAL. A sufficient set of hypotheses: F_n -> F in C^{1,alpha}_loc;
uniform tails, lim_{R -> inf} sup_n int_{|Y|>R} |F_n(Y)|/|Y|^3 dY = 0 (implied by a uniform bound
|F_n| + (1+|X|)|grad F_n| <= C (1+|X|)^gamma, gamma < 1); finitely many zeros of the limit field. Without uniform tails
the conclusion fails: F_n(X) = R_n f(X/R_n) -> 0 in C^infinity_loc while psi_xy[F_n](0) = c_f != 0 (distant mass leaves a
linear strain). The exponent 1/c_{l,n} -> 0 gives no uniform tail by itself. So a solver drifting to large c_l is drifting
toward a degenerate limit only if its far field stays uniformly controlled; with far-field mass escaping, a nonzero strain
can survive in the limit.

9.3 Constructive question (sign of B_3): no sign from the local axis constraints. Compatible axis data, NOT coupled
profiles: for every A > 1 and L > 0, w = -A x (1-u^2)/(1+u^2), g = x^2/(1+u^2), u = x/L, with h, a2, b3 from the
compatibility relations, give B_3(L) = C_A L^{-4-2/A}(1 - S_A/L^2), C_A > 0, S_A = 6A(4A-3)/(8A-1); at A = 2,
B_3 = (L^2 - 4)/(3 L^7). All three signs occur. A sign of a2 does not fix the sign of B_3.

9.4 Two further exact relations (audit3, rederived here).
- From (w/g)' = A/g (equivalent to the G_1 equation) and w(x*) = 0: |w(x)|/g(x) = A int_x^{x*} dt/g(t) on (0, x*]. Since w/g
  is odd, its expansion at 0 is A/(g0 x) + O(x) with no constant term, hence
     f.p. int_0^{x*} dx/g = 0,   i.e.   int_0^{x*} (1/g(x) - 1/(g0 x^2)) dx = 1/(g0 x*).
  (So g < g0 x^2 somewhere on (0, x*); a usable check on numerical axis data: it ties g on [0, x*] to x*.)
- Nonlocal formula for the axis strain: with circular principal value,
     c_l - w'(x) = (1/pi) PV int_{R^2} rho(x+xi, eta) eta (3 xi^2 - eta^2)/(xi^2+eta^2)^3 dxi deta - g(x)/4,
  the local term -g(x)/4 coming from rho(x+xi, eta) = g(x) eta + O(r^{1+alpha}). At x = 0 it reduces to the strain formula
  (g(0) = 0). The kernel changes sign on the upper half plane, so positivity in Q gives no sign directly.
- At A = 2 a NO would follow from strict signs of w''(P) and g(P) - 2 for the full coupled problem; neither is known.

## 10. Searching for a bound c_l <= 1 (lead, 2026-10-17T19:46Z) [numerical tests and short computations; nothing here is a theorem]

10.1 Scale-invariant form of R8. Under the two-parameter group rho -> mu rho(X/lambda) (only mu = lambda preserves the
 profile equation), c -> (mu/lambda) c, a(0) -> (mu/lambda^3) a(0) and Q3 := int rho U.grad(sin 3theta/r^3) dX ->
 (mu/lambda)^2 Q3. So q := Q3/c^2 depends only on the shape. For a profile, R8 gives Q3 = pi (c_l - 1)(3c_l - 1) and
 c = 3c_l - 1, i.e.
   q = (pi/3)(1 - 2/c),   so in the class (c > 2):  0 < q < pi/3,
 and conversely the shape fixes c = 2/(1 - 3q/pi). A cheap diagnostic for any candidate.
10.2 Q3 has no sign on positive densities (scripts/q3_sign.py, FFT on [-40,40]^2, N = 1024; c checked against -d_x U_1(0)
 to 1 percent). rho = x^2 y exp(-(x/sx)^2 - (y/sy)^2): Q3 > 0 for all seven (sx, sy) tried, q from 0.99 (sx = 2, sy = 1) to
 12.2 (sx = 0.5, sy = 3). A core x^2 y exp(-r^2) plus a positive blob of amplitude 10 at (+-5, 1) or (+-1, 5): Q3 < 0.
 So R8 alone cannot give c_l <= 1; any argument must use the equation beyond R8. Shapes concentrated near the x-axis
 give the smallest q, consistent with 4.4.
10.3 The only weights with a signed quadratic part. For a weight phi on the upper half plane H, the profile equation gives
   int_H rho [ (1 + 2c_l) phi + c_l X.grad phi ] = - int_H rho U.grad phi
 (no wall term since W_2 = rho = 0 on y = 0). The quadratic form is a zero-order pseudodifferential form with principal
 symbol phi_x xi1 xi2 - phi_y xi1^2 (times |rho^|^2/|xi|^2); high-frequency perturbations of a positive background keep
 positivity, so a sign on the positive cone needs phi_x = 0. For phi = Phi(y), m = Phi', using psi = 0 on the wall,
   - int_H rho U_2 m = int_H m |grad psi|^2 - (1/2) int_H m'' psi^2,
 which is >= 0 when m >= 0 and m'' <= 0 (for example m = y^s, 0 < s <= 1). But every such weight is nondecreasing in y and
 independent of x, and int rho Phi(y) dx diverges at fixed y (rho ~ x^{k-1} y as x -> inf along y = const, k = 1/c_l > 0).
 So the energy-type route needs a localization in x, which reintroduces unsigned cross terms. Not pursued further here.
10.4 Remark (out of class, c_l < 1). rho_phys(t,x) = (T-t)^alpha P(x/(T-t)^beta), alpha = 1/(c_l - 1), beta = alpha + 1,
 so alpha - beta = -1 and grad rho_phys(t,x) = (T-t)^{-1} grad P(x (T-t)^{-beta}). For 0 < c_l < 1, beta < 0, the argument
 tends to 0 for fixed x, and with grad P = O(|xi|^2) at 0 the gradient on a fixed ball is O((T-t)^{-1 - 2 beta}), which
 tends to 0 when c_l > 1/3. So such a state (with any renormalized velocity law) is not a blowup profile: its centre
 flattens as t -> T. (Formal; sent to astra nobound1 item 3 for checking.)

## 11. Far-field closure error of a disk model (lead, 2026-10-17T21:24Z) [elementary computation, CONDITIONAL on the expansion (11.1); numerically confirmed; not audited]
11.1 Assume the far field has the expansion rho = r^k Theta_0(theta) + r^(2k-1) Theta_1(theta) + O(r^(3k-2)), k = 1/c_l
 (the first correction is relative r^(k-1); this is the form used by the two-term exterior of construct1). A disk model
 that replaces rho for r > R by the homogeneous extension (r/R)^k rho(R, theta) changes the sin 3 theta coefficient there by
   delta rho_1(r) = theta_1 (r^(2k-1) - r^k R^(k-1)) + O(r^(3k-2) + r^k R^(2k-2)),   theta_1 := (Theta_1)_1,
 so by c = int_0^inf rho_1 r^(-2) dr the closure error in c is
   delta c = theta_1 [ R^(2k-2)/(2-2k) - R^(2k-2)/(1-k) ] + ... = - theta_1 R^(2k-2) / (2 - 2k) + O(R^(3k-3)).
 For construct1, 2k - 2 = -1.641. With the two-term exterior the leading error moves to R^(3k-3) = R^(-2.46).
11.2 Check (notes/num_seed, the numerics lane's disk model evaluated read-only on the construct1 seed, (N, M) = (256, 96)
 or (256, 64), L = 8): 3c_l - 1 - c = -1.338e-3 (R = 1e3), -3.058e-5 (R = 1e4), -1.262e-6 (R = 7e4). Ratios 43.8 and 24.2
 against 10^1.641 = 43.8 and 7^1.641 = 24.4. So the c offset of the seed in that model is the closure error of 11.1, and
 the model needs R >= 7e4 physical (c to 1e-7 relative) or the second exterior term.

## 12. w-only B_3 integrated by parts (lead, 2026-10-17T21:38Z) [elementary identity; checked on manufactured data; numbers are estimator values for trial data, not B_3 of a solution; not audited]
12.1 Identity. Let w be odd with w ~ -A x at 0 and a simple zero at x* (w'(x*) = mu1 > 0), and define g > 0 on (0, x*] by
 (w/g)' = A_g/g with g ~ x^2 at 0 (A_g = A for an exact profile; analysis 7.3, SPEC R10). Put m = -w/g (so m' = -A_g/g),
 a2 = (g' - w'')/2, kappa = a2(x*)/g(x*)^3, beta = 2/A, N = A^beta. Then
   f.p. int_0^{x*} (a2/g^3)' m^(beta-1) dx = -(1 - beta) f.p. int_0^{x*} (a2/g^3 - kappa) m^(beta-2) (A_g/g) dx,
 hence  B_3 = -((1 - beta)/(3N)) f.p. int_0^{x*} (a2/g^3 - kappa) m^(beta-2) (A_g/g) dx.
 Proof. (a2/g^3)' = (a2/g^3 - kappa)'; integrate by parts on [eps, x* - eta]. At x*: a2/g^3 - kappa = O(x* - x) and
 m^(beta-1) = O((x* - x)^(beta-1)), so the boundary term is O(eta^beta) -> 0, and the new integrand is O((x* - x)^(beta-1)),
 integrable. At eps: by parity (a2 odd, g even, m = x^(-1) times an even function) the boundary term is a sum of powers
 eps^(-4-beta+2j) and eps^(1-beta+2j), none of which is eps^0 when beta is not a positive integer [verifier G17: the
 kappa term needs beta != 1 as well, i.e. A != 2, c_l != 3/2; the earlier wording 'not an even integer' was too weak]; so its finite
 part is 0 and the finite parts of the two integrals agree (no logarithmic terms arise for the same reason).
12.2 Why it matters. The original integrand contains a2' (w''' and g''); the new one needs only a2 (w'' and g'), and next
 to x*, where the trial data are least accurate (largest 2D residual, VERIFY_REPORT G12) and the weight (x* - x)^(beta-1)
 concentrates the integral, it is (x* - x)^(beta-1) times a smooth factor, handled by Gauss-Jacobi quadrature. If the data
 have mu1 != A (h(P) != 1), g from A_g = A has a pole of g'/g at x*; A_g(x) = A + (mu1 - A)(x/x*)^2 removes it (a change of
 relative size (mu1 - A)/A). Without this regularization the IBP form is unstable (values 1.4 to 4.0 on construct1).
12.3 Code and checks: notes/b3_ibp/b3_ibp.py ([0, xc]: even-polynomial least squares of x^(5+beta) f and x^beta f on
 [x_lo, xc] with exact finite parts; [xc, x*]: Gauss-Jacobi, weight (x* - x)^(beta-1)). Manufactured compatible w
 (x* = 1, c_l = 5.5763, exact derivatives; notes/b3_ibp/test_out.txt): both forms give 14.41017 at xc = 0.3, K = 7
 (near-0 fit 4e-12); low K or xc = 0.5 bias both forms (near-0 extrapolation), hence K in {7, 9}, xc in {0.3, 0.4} x*.
12.4 Values (natural units B_3 x*^(p3-2); 16 variants each: xc/x* 0.3, 0.4; x_lo/x* 0.03, 0.05; K 7, 9; Jacobi n 40, 80;
 A_g regularized; notes/b3_ibp/all_out.txt):
   export                         IBP median [range]          original form median [range], same data
   construct1 spline120           0.3049 [0.2982, 0.3061]     0.2988 [0.1956, 0.3215]
   construct1 spline160           0.3050 [0.3041, 0.3058]     0.3088 [0.2716, 0.3347]
   construct1 final (200 x 100)   0.3025 [0.3000, 0.3034]     0.3056 [0.2686, 0.3080]
   construct2 basis1              0.2877 [0.2401, 0.2984]     0.0869 [-0.2823, 0.7980]
   construct2 basis2              0.3047 [0.2643, 0.3872]     0.2194 [-0.0255, 1.4067]
   construct2 basis3              0.3016 [0.2803, 0.3525]     0.1154 [-0.3684, 0.3801]
   construct3b s0 (no singular)   0.3053 [0.3009, 0.3062]     0.3018 [0.2333, 0.3125]
   construct3b s6                 0.3053 [0.3010, 0.3062]     0.3019 [0.2352, 0.3123]
 The IBP estimator removes most of the estimator spread (on construct1 final: 0.0034 instead of 0.04). Over the eight
 trial exports (three constructions, bases 120 to 240, with and without singular functions) the medians are 0.288 to
 0.305. The singular-off control (s0) gives the same value as s6, so the value is not put in by the trial's singular
 functions. The numerics lane's unconverged disk solutions (runs/axis_w_rep_*.txt, w only, (mu1 - A)/A = -1e-5 to -3e-4)
 give -59 to +34 with spreads of tens (notes/b3_ibp/rep_out.txt): their w is not accurate enough for this functional.
12.5 Reading. For the trial family of construct1, the w-only finite part is 0.30 +- 0.02 natural units (3.6e-5 physical),
 positive. All eight exports descend from one construction (common-error risk). That it is B_3 of a solution needs
 (i) w of a solution to the accuracy this functional needs (D12) from an independent discretization, and (ii) the
 near-P region resolved; neither is available. Consistent with VERIFY_REPORT G14 (0.33 +- 0.06, end-treatment dominated).
12.6 Sensitivity of the IBP estimator to errors in w (lead, 2026-10-17T21:47Z) [numerical; notes/b3_ibp/sens.py, sens_c1.txt].
 Base construct1 final, w -> w + eps W0 phi, W0 = max |w| on [0, x*] = 27.77, max |phi| = 1, phi = O(x^3) at 0
 (w'(0) kept), x* recomputed, c_l fixed; dB_3/eps in natural units, linear to 1e-2 between eps = 1e-6 and 1e-5.
 - Smooth global perturbations phi = (x/x*)^3 T_j(x/x*), j = 0..8: |dB_3/eps| <= 6.3. A smooth relative error 1e-4
   in w moves B_3 by at most 6e-4.
 - Bumps (x/x*)^3 exp(-((x - x0)/s)^2): x0 = 0.6, 0.8 x*: about 1; x0 = 0.95, 1.0 x*: 110 to 160; x0 = 0.4 x*,
   s = 0.1 x*: 520 at one setting, -20 at the median; x0 <= 0.2 x*, s <= 0.05 x*: 1e6 to 4e6, with sign and size
   depending on the near-0 fit settings. So the functional is well conditioned for smooth errors and ill conditioned for
   errors localized near 0 (scale below 0.2 x* = 1.7 physical), as predicted in 3.5(b) (factor (l/x*)^(2 - p3)/A).
 - c_l -> c_l + eps with w fixed: dB_3/eps = -125 (inconsistent: w'(0) != -A). Consistent change, w -> w A(c_l + eps)/A(c_l)
   (sens_cl.py): dB_3/dc_l = -0.016 for eps = 1e-4, +-1e-3. So a c_l error of 1e-3 with consistent w is harmless.
 Consequences. (i) B_3 = 0.30 is robust against smooth (global, low-mode) errors in w of relative size up to about 1e-3;
 it is not robust against localized errors near 0 at the 1e-8 to 1e-7 relative level, which is where the unfitted centre
 layer (rows from 0.31 physical) and the origin multiplier (r_o = 0.15 physical) act. Empirically, in construct1's own
 refinement sequence the centre defect E grew from 0.0024 to 0.0076 while B_3 moved from 0.3049 to 0.3025, so the centre
 layer moves B_3 at the 1 percent level there; the construct4 refit with centre rows is the test. (ii) The numerics
 lane's w has high-mode noise (their elliptic residual 3e-4 to 1.5e-3) and a different c_l (by 2e-3; -125 x 2e-3 = -0.3
 alone), which explains their -59 to +34. (iii) A second-solver B_3 needs w to about 1e-8 relative near 0 and c_l to
 1e-4, i.e. more than residual-level agreement.

## 13. What pins c_l: smoothness at P (lead, 2026-10-17T21:49Z) [heuristic; not audited]
13.1 Local structure. At the source P, W = (A xi, h y) + O(|xi|^2 + y^2), xi = x - x*, A = d_x W_1(P) = 2c_l - 1 for
 h = 1 (trace 2c_l). Characteristics xi = xi_0 e^(A t), y = y_0 e^(h t) satisfy xi |y|^(-A/h) = const, and the linear model
 W.grad rho = rho has the general continuous odd-in-y solution rho = sgn(y) |y|^(1/h) Phi(xi |y|^(-A/h)), Phi arbitrary.
 Since A/h is about 10, generic characteristics leave P tangent to the y direction (the weak unstable direction) and the
 cusp xi ~ |y|^10 separates them only at P. With the nonlinear terms, Sternberg linearization (no resonance a A + b = 1,
 a, b >= 0 integers, other than (0, 1), for A not of the form 1/n) gives the same picture in smooth coordinates.
13.2 Smoothness at P (C^infinity; for h = 1 already continuity of rho/y at P) needs h(P) = 1 and Phi constant (finite
 regularity allows h(P) < 1 and non-constant Phi, with d_y rho(x, 0) ~ |xi|^kappa, kappa = (1 - h)/A). Then rho near P
 is a multiple of one function, and through the characteristics (all of which leave P) rho is fixed in the open quadrant
 by d_y rho(P) and W. With the identity 3c_l - c = 1 (smoothness of d_y rho on the axis at 0) and the normalization a(0) = 1
 this is the count behind "c_l is an isolated value" (and behind "B_3 = 0 has no parameter left", 3.4).
13.3 Consequence for numerics. Profiles that are smooth except in the cusp at P (Phi non-constant on scales below the grid)
 or have h(P) slightly different from 1 form a large nearby family along which c_l varies. A discretization penalizes them
 only through the cells touching P, so (i) the global residual does not control c_l, the residual at P and h(P) - 1 do;
 (ii) near-null directions of the discrete Jacobian supported where the characteristics from P end, in the far field, are
 expected (numerics lane: smallest singular vector 89 percent at r > 10, c_l component -0.065; their h(P) - 1 = 1.3e-4
 against construct1's -4e-6). The near-P residual of construct1 (3.2e-5, slow decay) may be the same tension. Test
 requested from the numerics lane (NOTES 2026-10-17T21:49Z): an explicit h(P) = 1 row.
13.4 Characteristic defect (lead, 2026-10-17T21:52Z) [numerical diagnostic; notes/char_defect/char_defect.py, probe.py].
 Along a characteristic an exact solution has d log rho/dt = 1; a trial has 1 + R/rho. J(X0) = int_{-inf}^0 (R/rho)(X(s)) ds
 (backward from X0 to P) is log rho_trial(X0) - log rho_tr(X0), rho_tr the transport solution with the trial's own W
 that matches the trial at P to first order (no nonlocal feedback). construct1 final, start points on r = 20, 8 angles,
 cubic interpolation of W and R/rho on the export grid:
 - J accumulates only within |X - P| < 2: at |X - P| = 4 it is 1e-8 to 6e-7; inside, R/rho oscillates with amplitude
   about 1e-4 (R/rho at (x*, 1) -1.3e-4, (x*, 2) +1.1e-4, (x* - 0.2, 2) -1.9e-4; at (x*, 0.03) -6.7e-6, the h(P) - 1
   level). All backward characteristics except those that pass by the origin reach P from straight above (end points
   (x - x*, y) = (-6e-6, 0.03)), as 13.1 says.
 - J (stopped at |X - P| = 0.03): -1.28e-4, -1.07e-4, -8.4e-5, -7.9e-5, -1.12e-4, -6.3e-5 for start angles 0.24 to 1.33,
   -5.1e-5 at 0.02, +1.6e-5 at 1.55 (passes by the origin and reaches P along the axis). Spread 1.4e-4.
 Reading. The pointwise normalized residual near P (3e-5) integrates to a relative inconsistency of about 1e-4 between the
 trial and the transport solution of its own velocity, with a label-dependent part of about 1e-4 (the trial is close to a
 transport solution whose data Phi at P varies by 1e-4, 13.1). Through the nonlocal law this is the size of the expected
 relative error of rho, hence of c = psi_xy(0) and c_l, assuming a well-conditioned linearization: about 1e-4 relative,
 i.e. c_l known to about 1e-3, not to the 1e-7 of its stability under refinement of one construction. This agrees with
 the spread of independent values: numerics lane 5.5728 to 5.5823 (h(P) - 1 = 1.3e-4), construct2 5.57625, construct1
 5.57632. [Consequence for reporting: quote c_l as 5.576 with an uncertainty of order 1e-3 until the near-P defect is
 reduced.] The far part of the trial (|X - P| > 4) is transport-consistent to below 1e-6.
 Basis dependence (notes/char_defect/cd_all.txt, same settings): spread of J over the 8 start angles
   construct1 spline120 6.2e-4, spline160 2.2e-4, final (200 x 100) 1.4e-4; construct3b deg160 s0 2.30e-4, s6 2.30e-4;
   construct2 basis3 (240 x 125, transport and residual-gradient rows around P) 7.5e-5.
 So the defect decreases under refinement (exponent about 3.6 from 120 to 160, 2.0 from 160 to 200) and is reduced by
 rows that weight the region around P, while the singular functions do not affect it.
13.5 Where the near-P residual sits, and why (lead, 2026-10-17T21:56Z) [numerical map notes/char_defect/nearP_map.py; heuristic].
 R/rho (x 1e5) on xi = x - x* in [-3, 3], y in [0.05, 4]: construct1 final has |R/rho| up to 1.7e-4 in a vertical strip
 |xi| <= 0.5, 0.05 <= y <= 2 above P, oscillating in xi on the scale 0.25 (about two radial knot spacings, 0.13
 physical); outside the strip below 1e-5. spline160: the same strip, amplitude 2.4e-4, sign pattern different (not a
 fixed function: a resolution-limited compromise). By 13.1 the characteristics leave P vertically and fan out like
 xi = c y^A (A = 10.15): the strip at y about 1 carries the characteristics that end at all far-field angles, so the far
 field Theta(theta) is encoded in a strip of width O(1) at y = 1 and O(2^-10) at y = 2. A least-squares objective sampled
 uniformly in (q, theta) gives that strip a small weight, so any inconsistency between the global constraints (far
 field, nonlocal law, centre) and smoothness at P is placed there, at a cost that shrinks with the strip area. That fits
 the slow decay of the near-P maximum (degree^-2.8) and the decrease of the characteristic defect (6.2e-4, 2.2e-4, 1.4e-4).
 A remedy to test after construct4 (if its local knot refinement does not fix it): weight the residual rows by the
 characteristic density (e.g. by the local horizontal compression |d c / d xi| = y^-A, capped), or add characteristic
 rows J(theta_0) - mean J = 0 for a set of start angles. construct2 basis3 (rows weighting the region around P) has the
 smallest defect so far (7.5e-5).
13.5a Correction to 13.5: geometry of the characteristic fan near P (lead, 2026-10-17T21:59Z) [numerical,
 notes/char_defect/labels.py, construct1 final, backward characteristics from r = 20].
 13.5 had the scaling direction inverted. Backward in time the flow near P contracts xi at rate A and y at rate 1, so the
 backward characteristics approach P tangent to the slow (vertical, eigenvalue h = 1) manifold through P, a curve
 xi = kappa y^2 + ..., kappa about -0.011 here, and their deviation from it scales like y^A. Crossing points xi at height y:
   start angle 0.24 to 1.22 at r = 20:  y = 1: xi in [-1.13e-2, -1.05e-2] (width 7e-4);  y = 0.5: [-2.86e-3, -2.81e-3];
   y = 2: [-0.21, +0.50] (width 0.7, ratio to y = 1 about 1e3 = 2^A);  y = 4: [-2.3, +4.9].
   start angles 0.02 and 1.55 (along the axes) and 1.44 cross |xi| < 5 at xi = +4.85, -4.75, -3.6 (y = 1).
 So the far field theta in [0.13, 1.33] is carried, for y <= 1, by a sliver of width about 1e-3 (y)^A around the slow
 manifold, and it opens to width O(1) only at y about 2. Points of the residual strip of 13.5 at |xi| about 0.25,
 y <= 1 lie on characteristics that leave the neighbourhood of P horizontally and reach the far field within about 0.1
 of the axes. Consequences: (i) for the characteristics of the open far field, R/rho is sampled along the slow manifold
 for y <= 1 (a common, label-independent contribution to J) and the label-dependent part of J is accumulated where the
 sliver opens, 1 <= y <= 4, consistent with 13.4 (J accumulated within |X - P| < 2); (ii) the underweighting argument
 of 13.5 applies to the sliver (area of order 1e-3 for y <= 1), not to the whole strip, so the remedy of 13.5 should
 weight the band 1 <= y <= 4, |xi| <= 5 and the slow manifold, or use J rows directly.
13.6 Correction to 13.2: C^1 at P already forces h(P) = 1 and Phi constant (lead, 2026-10-17T22:05Z) [sketch, not
 audited; uses a C^1 linearization at the hyperbolic source P (Hartman, planar case), whose hypotheses on W must be checked].
 The parenthetical of 13.2 ("finite regularity allows h(P) < 1 and non-constant Phi") came from the axis ODE alone and is
 wrong off the axis. In linearizing coordinates (xi, eta) with W = (A xi, h eta), write rho = |xi|^(1/A) F(t),
 t = eta |xi|^(-h/A) (xi != 0). Then d_xi rho = (1/A) sgn(xi) |xi|^(1/A - 1) (F(t) - h t F'(t)). Since 1/A < 1, boundedness
 of d_xi rho as xi -> 0 at fixed t forces F - h t F' = 0, i.e. F(t) = C_pm |t|^(1/h), so rho = C sgn(eta) |eta|^(1/h)
 near P (odd in eta). If h < 1 then d_eta rho(xi, 0) = 0 near P, so g = d_y rho(x, 0) vanishes on an interval next to x*,
 and by the axis ODE w g' = (1 - h) g on all of (0, x*), contradicting g > 0 there (Lemma 3). If h > 1, rho is not C^1.
 So rho in C^1 near P gives h(P) = 1 and rho = C eta in linearizing coordinates (Phi constant), as in Lemma 3 for A_2.
 Consequence: the "near-solutions" of 13.3 with non-constant Phi or h(P) != 1 are not C^1 at P, so they are not
 admissible; they explain a numerical near-null mode, not a family of profiles. The count of 13.2 (identity, h(P) = 1,
 a(0) = 1 fix c_l and the scale; nothing left for B_3 = 0, B_5 = 0, ...) applies to C^1 profiles. By Lemma 5 a profile
 smooth near 0 needs B_j = 0 for every odd j with p_j not an even integer: infinitely many conditions on a solution set
 that is expected to be discrete. This is the heuristic reason to expect the strong setting to fail generically, and it
 is consistent with the measured B_3 of about 0.30 on the computed branch. It is not a NO argument: nothing excludes
 B_j = 0 on some branch, and no rigidity result for the coupled problem is known.
13.4a Amendment to the reading of 13.4: c_l is much less sensitive to the near-P defect than "about 1e-3" (lead,
 2026-10-17T22:06Z) [numerical; c_l stored in the exports].
 construct1 refinement, same fit setup: degree 120 c_l = 5.5763606, 160: 5.5763231, 200: 5.5763219 (differences -3.7e-5,
 -1.3e-6: fast convergence), while the J spread went 6.2e-4, 2.2e-4, 1.4e-4 (slow). So a change of 4.8e-4 in the J spread
 moved c_l by 3.9e-5 (7e-6 relative), a ratio of about 0.015, not of order 1 as assumed in 13.4. All fits at degree >= 120:
 construct1 5.5763219 to 5.5763606; construct3b s0/s6 deg120/deg160 5.5763022 to 5.5763605; construct2 basis1-3
 (residual 100 times worse) 5.5762428 to 5.5763187. Spread 1.2e-4 (2e-5 relative). Reading: within this construction
 family c_l = 5.57632 with a spread of about 1e-4 over all variants; the remaining near-P defect, scaled by the ratio
 above, suggests an effect of order 1e-5 on c_l. The independent solver (numerics lane) gives 5.5728 to 5.5823, i.e.
 agreement to its own accuracy of a few 1e-3 only. The 1e-3 of 13.4 is withdrawn as an estimate; it remains an upper
 bound of the assumed-conditioning kind, which the data do not support.
12.7 B_3 under the centre correction (lead, 2026-10-17T22:10Z) [numerical; notes/b3_ibp/c4centre_out.txt].
 construct4 step 1 (rows to shape radius 1e-4 with (s_c/s)^2 weights and explicit D14 rows) moved the centre jet from
 E = 7.58e-3, D2 = -1.25e-2 to E = -4.6e-8, D2 = 9.6e-8 (residual r <= 0.1: 2.0e-6 -> 2.7e-9), c_l 5.5763219 -> 5.5763291.
 IBP estimator on c4_centre_fields.npz: median 0.3005, range [0.2965, 0.3017] (16 settings), against 0.302 to 0.305 on
 construct1. So the centre layer, the one localized near-0 error that 12.6 identified as able to move the estimator, was
 not what set B_3 = 0.30. The characteristic defect is unchanged (spread 1.44e-4, notes/char_defect/c4centre_cd.txt),
 as expected since step 1 does not touch P.

### 13.7 An identity-free c_l at fixed rho (2026-10-17T22:43Z; for VERIFY_REPORT G20 (b2)(iii))
Fix rho (hence U) of an export and let c_l vary in W = c_l X + U. Then w(x; c_l) = c_l x + U_1(x, 0), so the zero x*(c_l) moves
with dx*/dc_l = -x*/w'(x*) = -x*/A by R5 (w'(P) = d_x W_1(P) = A = 2 c_l - 1 for a profile). h(x; c_l) = d_y W_2(x, 0) =
c_l + d_y U_2(x, 0), so
   d h(P)/d c_l |_rho = 1 + h_x(P) dx*/dc_l = 1 - h'(P) x*/A,   h' = d/dx h(x, 0) at fixed c_l.
The root c_l^h of h(P; c_l) = 1 is a determination of c_l that does not use 3 c_l - c = 1 (it uses smoothness at P,
analysis 13.6 / VERIFY_REPORT G21). To first order c_l^h - c_l = -(h(P) - 1)/(1 - h'(P) x*/A).
Values (axis exports axis_w, axis_h, cubic splines on 5 < x < 12; one-off script in this session, numbers as printed):
   construct1 final_candidate: h(P) - 1 = -1.78e-6, h'(P) = -0.0940, dh/dc_l = 1.0797, c_l^h - c_l = +1.6e-6;
   construct4 c4_centre_fields: -4.53e-6, -0.0938, 1.0794, +4.2e-6;
   construct3b s0_deg160_fields: -3.4e-7, -0.0940, 1.0796, +3.2e-7.
Also w'(P) - A = 4e-6 on all three (R5 check). The numerics lane's batched finite-difference value of dh/dc_l on its own state
is 1.05 (NOTES_FOR_LEAD 22:09Z), consistent.
Scope: this shows that two independent scalar conditions (the c identity and smoothness at P) hold simultaneously on one trial
to a few 1e-6 in c_l. It is a consistency check of the trial, not an error bound for the c_l of an exact profile: the variant
spread across constructions (1.2e-4, VERIFY_REPORT G20 (c)) and the independent solver's values are larger.
13.4b Where J accumulates, by distance from P (lead, 2026-10-17T22:57Z) [numerical; notes/nearP/jsplit.py, map.py,
 line.py on c4_centre_fields.npz, 10 start angles on r = 20, backward to |X - P| = 0.03].
 Spread over labels of the part of J accumulated in each distance band: [0.03, 0.3) 5.6e-5, [0.3, 1) 3.0e-5,
 [1, 2) 7.2e-5, [2, 4) 4.9e-5, beyond 4: 1.4e-6; total 1.52e-4. The eight open-quadrant labels (start angles 0.19 to
 1.21) accumulate identical amounts inside distance 2 (-3.54e-5, -2.61e-5, about -6e-5: the shared stem along the slow
 manifold); their mutual spread arises in [2, 4) (+4.2e-5 to -7e-6). The labels along the axes (0.02, 1.38, 1.55) reach P
 horizontally and differ from the stem labels by up to 1.5e-4 already inside distance 0.3. The normalized residual
 |R/den| is below 1e-6 outside the box |x - x*| <= 1, 0.05 <= y <= 4 (max 3.4e-5 at about (x* - 0.3, 3)); along rays
 theta = 0.1 to 0.3 it changes sign every 0.15 to 0.3 in r, i.e. every one or two radial knot spacings (0.13 physical).
 Reading: the far trial (|X - P| > 4) is transport-consistent to 1e-6; the whole defect sits within distance 4 of P, at
 the radial knot scale. Whether it is a representation limit (it should then fall under radial refinement together with
 the J spread) or a global inconsistency placed where the fit is cheapest (the J spread should then stay near 1.5e-4
 while the pointwise residual falls) is decided by J on the refined construct4 fits (c4_r1, 215 functions), and by a
 fit that weights the region around P (lead work/c6, option --pweight of the local centre_fit.py copy).
13.4c J split under refinement, degree 160 against 200 (lead, 2026-10-17T23:06Z) [numerical; notes/nearP/
 s0deg160_jsplit.txt against 13.4b; construct3b s0 deg160 has no centre rows, c4_centre is construct1 final (deg200) with
 centre rows, which 12.7 found not to move J].
 | part of J | deg160 | deg200 |
 | shared stem, d < 2 (open-quadrant labels) | -2.24e-4 | -1.21e-4 |
 | label spread in [2, 4) | 9.0e-5 | 4.9e-5 |
 | label spread in [1, 2) | 1.16e-4 | 7.2e-5 |
 | d >= 4 | 9e-7 | 1.4e-6 |
 | total spread | 2.51e-4 | 1.52e-4 |
 Every near-P part falls by a factor of about 1.7 to 1.9 for a factor 1.25 in degree (rate about 2.3 to 2.8 in the
 radial spacing), the far part stays at 1e-6. This favours the representation-limit reading of 13.4b over a global
 inconsistency, provided the refined construct4 fits continue the trend (c4_r1 halves the radial spacing only in
 7.7 <= r <= 9.7; at rate 2 to 2.5 that predicts a J spread of about 3e-5 to 4e-5 and a near-P maximum lower by a
 factor 4 to 6, compatible with the 6144 x 640 scan of c4_r1, flux peak 1.25e-4 -> 3.07e-5). Extrapolation (not a
 result): two further local halvings would bring the near-P maximum to the 1e-6 level; each halving needs the fit grid
 radial spacing below half the local knot spacing (at the second halving, knot spacing 0.033 at r = 8.6, so nr about
 8192 on the present log grid).

### 13.8 External referee (astra audit4, answer 2026-10-18T00:08Z) on 13.1, 13.6, 13.7 and the section 1 class; lead check and corrections (lead, 2026-10-18T00:44Z)
(a) 13.1: the claim of smooth Sternberg coordinates is withdrawn. In P_2 the field W is only C^{2,alpha}_loc (Schauder
 for -Laplace psi = d_x rho with d_x rho in C^{1,alpha}_loc), so smooth linearization is not available. What holds: a C^1
 local conjugacy at P, from Hartman's C^1 theorem for a C^2 map at a hyperbolic contraction (planar case), applied to the
 backward time-one map (eigenvalues e^{-A}, e^{-h}); no resonance condition. The flow conjugacy follows from the averaging
 H(z) = int_0^1 e^{tB} K(Phi_{-t} z) dt, with K the map conjugacy and B = DW(P) (checked: H(Phi_{-s} z) = e^{-sB} H(z),
 DH(0) = I), and the chart can be symmetrized in y. 13.1's statements about the linear model are unchanged.
(b) 13.6 is wrong as a purely local lemma. Counterexample (checked): W = (2 xi, eta/3), rho = eta^3: W.grad rho = eta^3 =
 rho, rho smooth, P a source with A = 2 > 1, h = 1/3. Corrected local statement: in the C^1 symmetric chart, f = rho o
 H^{-1} satisfies f(e^{At} xi, e^{ht} eta) = e^t f(xi, eta); differentiating in xi gives f_xi(...) = e^{(1-A)t} f_xi, and
 boundedness as t -> -inf forces f_xi = 0 (A > 1), so f = C sgn(eta) |eta|^{1/h}. Cases: h < 1 allows C != 0 but then
 rho_y = 0 on the axis near P; h > 1 forces C = 0 (C^1); h = 1 gives f = C eta. The conclusion h(P) = 1 and C = rho_y(P)
 > 0 needs the global axis hypothesis: g = rho_y(x,0) > 0 on (0, x*), which in P_2 follows from w g' = (1 - h) g, g ~ x^2
 at 0 and w != 0 on (0, x*) (R10, R5). With it, 13.6's conclusion holds; it is a local reformulation of R5/R6, not a new
 result. 13.6's sentence "near-solutions with h(P) != 1 are not C^1" is wrong for approximate profiles (a smooth trial can
 have h(P) != 1 with a small nonzero residual); the correct reading is that exact C^1 solutions have h(P) = 1.
(c) 13.7: d h(P)/d c_l at fixed rho = 1 - h_x(P) x*/A confirmed; for a trial A = 2 c_l - h(P) (trace), not 2 c_l - 1. The
 root of h(P; c_l) = 1 is a determination of c_l without the origin identity if D = 1 - h_x(P) x*/A != 0; the Newton
 correction c_l^h - c_l = -(h(P) - 1)/D is first order. A consistency check, not an error bound.
(d) Section 1: P_inf contained in P_2 needs a common global regularity; FINAL_REPORT section 1 now requires rho in
 C^{2,alpha}_loc(R^2) in both problems (the report's choice of class; the prompt states regularity of a near 0 only).
(e) J (13.4): J = log rho - log rho_tr only when h(P) = 1 and rho_tr matches rho to first order at P; otherwise J_eps with a
 stated cutoff is a log density ratio from the cutoff section, and h(P) - 1 != 0 adds (h(P) - 1) log(1/eps)/h(P). The lead
 J tables (jsplit) report shells and spreads over labels with r0 and eps stated, so they are unaffected.
(f) Trial regularity (checked against trial.py by the referee; lead spot-check of the npz: c4_r1 and the 302 test shape
 have end knot multiplicity 8 and all interior knots simple, i.e. degree 7, C^{6,1}): a, rho in
 C^{4,alpha}_loc(R^2) for alpha < beta = p_3 - 6 (about 0.197); each mode b_m chi^{m-1} cos(2 m theta) analytic at 0;
 T(-1) = 1.6485 != 0 on c4_r1, so the trial's a is not smooth at 0 (by design; it says nothing about an exact profile).
 Section 4 draft repaired accordingly (notes/final_sec4_draft.md, (ii), (iii), 4.1, 4.2, 4.4a, 4.4b, 4.7).

### 13.9 What controls the c_l error of a trial (lead, 2026-10-18T01:22Z) [heuristic; first-order reasoning, assumes a nondegenerate exact profile; audited by the verifier G40: CONFIRMED as a labelled heuristic, with the precision note in (b), applied]
Setting. Trial (rho, c) with residual R = F(rho, c) = (c X + U[rho]).grad rho - rho; an exact profile (rho*, c*) nearby,
 assumed nondegenerate: the bordered linearization Lb(d rho, d c) = (D_rho F d rho + d c X.grad rho, l0(d rho)), with
 l0 the x^2 y Taylor coefficient (normalization a(0) = 1), is invertible between suitable spaces. This hypothesis is
 not proved.
(a) To first order (rho* - rho, c* - c) = -Lb^{-1}(R, 0), so c* - c = -<phi, R> with phi the first component of
 Lb^{-*} e_c (dual solution). The c_l error is the residual weighted by phi, not its maximum. Two trials with the same
 near-P maximum can have different c_l errors; G33 (c) observes this (construct5 against c4_r1: same maximum, c_l
 differs by 3.2e-5).
(b) Transport part. For fixed W, D_rho F contains W.grad - 1. Its C^1 inverse is explicit along characteristics: for g
 with g = O(|X - P|^{1+alpha}) at P for some alpha > 0 (or a Dini condition; o(|X - P|) is not enough: g ~ |X - P|/log(1/|X - P|)
 gives a log-divergent integral; correction from the verifier's audit G40 (b)), (W.grad - 1) u = g has the C^1 solutions u(X) = int_{-inf}^0 e^{-s} g(Phi_s X) ds + K rho(X)
 (proof: v(s) = e^{-s} u(Phi_s X) has v' = e^{-s} g(Phi_s X); e^{T} u(Phi_{-T} X) -> u_eta(P) eta_inf(X) as T -> inf
 when h(P) = 1). Since grad R(P) = (DW(P)^T - I) grad rho(P) = (0, (h(P) - 1) rho_y(P)), R = O(|X - P|^{1+alpha}) needs h(P) = 1
 (and then holds for a C^2 trial);
 otherwise the integral diverges like (h(P) - 1) times the log of the cutoff, which is the J_eps cutoff term of 13.8 (e).
 With g = -R and W.grad log rho = 1 + R/rho along the trial's characteristics, u(X) = -rho(X) J(X) (1 + O(J)) + K rho(X).
 So J is the relative first-order transport correction at fixed W; its constant part is a multiple of rho (absorbed by
 the normalization together with the nonlocal terms), and its non-constant part (the spread over labels) is what a
 transport step would change.
(c) The full linearization adds the nonlocal coupling U[d rho].grad rho and d c X.grad rho, so c* - c is a linear
 functional of the transport correction (J) and of its nonlocal feedback. It is not proportional to the J spread in
 general, and no bound follows without an estimate of |Lb^{-1}|. The numerics workstream's soft direction (00:46Z:
 3.2e-6 in |F|_2 per 1e-3 in c_l on their discretization) measures part of that norm on their discretization only.
(d) Consequence for reporting: quote c_l with the spread over fits; under refinement, test that the change of c_l between
 successive fits shrinks together with the J spread (and the near-P maximum). This is a consistency criterion, not an
 error bound.

### 13.10 Why residual norms pin c_l only weakly, and what the J pattern adds (lead, 2026-10-18T01:52Z) [SUPERSEDED IN PART by 13.11: (a) holds for frozen transport only, (c) withdrawn as stated; heuristic; audited as superseded, G41]
Setting as 13.9; assume an exact P_2 profile (rho*, c*) and, for small d, a nearby solution rho_d of the equation at
 c = c* + d that is smooth away from P but carries a label-dependent factor at P, rho_d = eta Phi_d(xi |eta|^(-A)) near P
 in linearizing coordinates (13.1), with log Phi_d spread over labels of size s|d| (s: the label spread per unit c_l).
 Such rho_d are not C^1 at P (13.6), so they are not profiles; they model the soft direction.
(a) A smooth trial near rho_d. Put rho_tr = rho_d exp(-phi) with phi chosen on
 each characteristic as phi = log(Phi_d(label)/Phi_0) chi(t), chi = 1 near P and chi = 0 after a transition window of
 time T. Then rho_tr is smooth at P (the label factor is removed there) and, at fixed W, R_tr/rho_tr = -d phi/dt, of size
 s|d|/T. Representability limits the start of the window: at height eta above P the labels occupy a strip of width about
 eta^A, so a trial with resolution h near P can carry label dependence only for eta above eta_h = h^(1/A). The window can
 then run from eta_h along the whole path towards the far field, so T is at least (1/A) log(1/h) and can be several
 units (A is about 10.15; h = 1e-3 gives 0.68). The nonlocal feedback of phi is of the same order s|d| and is part of the
 linear tangent problem.
(b) Consequence. At offset d, the best attainable residual on a basis is of order s|d|/T in sup norm, with T growing only
 logarithmically in the resolution (and with the length of the paths used). So a residual floor eps resolves c_l only
 to about eps T/s. With s of order 1e-2 (numerics lane's characteristic-row sensitivity 0.008 to 0.010 per unit c_l,
 NUM NOTES 01:25Z, on their states) and T about 1, a near-P floor of 3e-6 gives about 3e-4, and 1e-6 gives about 1e-4.
 This would explain why fits 3e-5 apart in c_l are equally good (G37), and the numerics lane's flat valley.
(c) The J pattern is not affected by where the trial puts the residual along a path: the label-dependent part of
 J = int (R/rho) dt along the full backward characteristic is the label spread of log rho_tr relative to the transport
 solution, s|d| plus representation error, whatever T is. So the J spread is the natural measure of the c_l
 inconsistency, and |c_l - c*| is estimated by the component of the measured J pattern along the soft pattern
 dJ/dc_l, divided by its size: c_l - c* ~ <J - mean J, S>/<S, S>, S(label) = dJ(label)/dc_l along the soft direction.
 This is a first-order estimate under the hypotheses of 13.9, not a bound; representation noise in J enters it
 directly.
(d) Measurement plan. soft_tangent.py gives the soft tangent on a basis (the shape change that absorbs a c_l change
 best in the fit objective) and shapes along it at c_l offsets; J at the offsets +-1e-3, +-3e-3 (run_tan.sh) gives S on
 that basis, and the estimate of (c) can then be applied to each fit. Expected if (a) holds: J spread rises by about
 s|d| (1e-5 at d = 1e-3 if s = 1e-2) while the objective and the near-P maximum rise much less.

### 13.11 External referee of 13.10 and corrections (lead, 2026-10-18T02:06Z; referee answer astra/softcl1/answer.md) [the referee's algebra below was rechecked by the lead where marked; CONFIRMED by the verifier, G41 (2026-10-18T02:17Z), which also withdraws its G38 (f), (g) offset rule]
(a) 13.10 (a) holds for frozen transport only. With rho~ = rho_d e^(-phi), f = rho~ - rho_d and W_d = c X + U[rho_d], the
 exact coupled identity is F(rho~, c)/rho~ = -W_d.grad phi + U[f].grad log rho~ (lead check: W~ = W_d + U[f] by linearity
 of the velocity law; W_d.grad rho_d = rho_d). The cutoff controls the first term at s|d|/T; the feedback term has no
 factor 1/T, and without uniform regularity bounds not even an O(|d|) estimate. The singular family rho_d itself was
 not constructed. Two illustrations of the feedback (lead checked both): F(k rho, c) = k(k - 1) U[rho].grad rho for an
 exact rho; the Gaussian trials x^2 y exp(-(1 + eps) r^2) have psi_xy(0) = 1/(8(1 + eps)) (sin(3 theta) coefficient
 r^3 e^(-(1+eps) r^2)/4), so the multiplier phi = eps r^2, with W.grad phi -> 0 at 0, still creates the centre defect
 eps/(8(1 + eps)). Status: 13.10 (a) withdrawn as a statement about the coupled problem; kept as a frozen-field mechanism.
(b) Non-closed range versus norms. If the bordered map B(u, d) = (L u + d q, N u) (q = X.grad rho, N the normalization
 coefficient) is a bounded isomorphism, as 13.9 assumes, then with l(r) the exponent component of B^(-1)(r, 0):
 l(L u + d q) = d for N u = 0, so |d| <= |l| |L u + d q| in the same norms, and the normalized shape range is the closed
 hyperplane ker l (lead check: immediate). A cheap exponent direction must therefore lose the norms in which the inverse
 is bounded. Model (referee): y u' = 0 on (0, 1), u(0) = d, u(1) = 0 has only the solution u = 0, d = 0, but
 u_T = d chi(log y / T) satisfies the boundary conditions with sup |y u_T'| <= C |d|/T while its C^1 norm grows like
 e^T. The measured residuals (normalized sup, discrete 2-norm) are of this weak kind. Reading for the numerics: a trial
 space with knot spacing h near P cannot represent cutoffs finer than h, so its c_l resolution is tied to h; residual
 softness in c_l is then a resolution property of the trial space and grid, not evidence of a family of profiles, and
 not evidence against one. 13.10 (b), (d): kept only in this form (local scale T_near about (1/A) log(1/h), 0.68 at
 h = 1e-3, plus 0.068 per halving; referee arithmetic agrees).
(c) The J-pattern estimator of 13.10 (c) is withdrawn as stated. (i) The sensitivity S must be centred like J.
 (ii) Nondegeneracy does not remove the shape-error term: with j = Pi J, S = Pi DJ(v, 1) and the error (d v + e, d),
 the estimate is d + <S, B_J e>/<S, S> + higher order. Counterexample (lead checked): F(a, d) = (a, d), J(a, d) =
 (a + d, -a - d); the fixed-d least-squares shape is a = 0, S = (1, -1), and the trial (eps, 0) has exponent error 0
 but estimate eps. Replacement (discrete dual-weighted step): with M the scaled shape columns of the full coupled
 Jacobian, b its exponent column, v = argmin |M v + b| and s = M v + b, the normal equations M^T s = 0 give
 <s, M e + b d> = d |s|^2 for every shape error e (lead check: <s, b> = <s, s> - <M^T s, v> = |s|^2). So
 dk = -<f, s>/|s|^2 is the exponent component of the Gauss-Newton step. On the fit rows this is the dk* that
 soft_tangent.py reports: where the least-squares minimizer of the fit lies in c_l (LSQR moves c_l by only 1e-7 per
 segment, G37, so the fit need not be at that minimizer). On an enriched grid with the tangent re-solved there
 (work/c6/dwr_eval.py) it is the same for the enriched objective. Neither is the error of c_l against an exact profile:
 that needs control of the discretization, the trial space and the nonlinear remainder. What can be reported is the
 Gauss-Newton corrected c_l of each basis (215, 244, 302, 375 radial functions) on fit and enriched grids, and how it
 converges.
(d) Reporting rules adopted from the referee (task 4). The spread over fits measures empirical reproducibility; it is
 not an uncertainty interval, and "lower bound" is informal: if the exponent is unique, two fits Delta apart imply only
 that one of them has error at least Delta/2. Agreement of c_l from h(P) = 1 at fixed rho with the identity value is a
 consistency check (that condition is fitted), not an accuracy. At a least-squares minimum with floor m0 the objective
 at offset delta along the soft direction is m(delta)^2 = m0^2 + sigma^2 delta^2 to second order, so an m(c) curve is
 flat until sigma |delta| is comparable to m0 (with the independent solver's sigma = 3.2e-3 and m0 = 6e-4, the norm
 rises by 8.2e-12 at delta = 3.1e-5); offsets for m(c) must be chosen from the measured sigma of the basis.
 Approved wording until better diagnostics exist: "The computed branch has a representative fitted exponent
 c_l = 5.57636 (approximately). Fits of comparable residual quality differ by approximately 3.1e-5 and exhibit a weakly
 penalized exponent direction. This spread measures empirical reproducibility, not an uncertainty interval. The
 available diagnostics do not yet calibrate the absolute exponent error or the accuracy of the last quoted digits."

### 13.12 What the c6b soft tangent says about c_l on the 244 basis (lead, 2026-10-18T04:43Z) [measured facts plus first-order reading; the reading is not audited]
Facts (tan_c6b, 10240 x 480, LSQR iterations 250 to 2500; m0 = |f0| = 1.8536e-5; sigma = |F_k + J_s v| k^2 per unit c_l).
(a) sigma: 0.244, 0.050, 0.024, 0.0147, 0.0093, 0.0064, 0.0051, 0.0044, 0.0040, 0.0036. LSQR iterates are feasible shape
 corrections, so sigma_244 := min_v |F_k + J_s v| k^2 on this basis and grid is at most 3.58e-3 (an upper bound, not an
 estimate; the limit is not known).
(b) The linear model m_lin(d)^2 = |f0 + d r|^2 matches the nonlinear objective along the tangent to 0.5 percent up to
 |d| = 1e-3 and to 20 percent at 3e-3 (m_nl 2.64e-5 / 2.59e-5 against m_lin 2.18e-5 / 2.11e-5 at -3e-3 / +3e-3).
(c) 3.8 percent of f0 lies along r (m_lin minimum / m0 = 0.99929), giving dcl* = +1.95e-4; dcl* grew with the
 iteration (-5e-6 at 1000, +1.3e-5, +4.5e-5, +9.0e-5, +1.4e-4, +1.95e-4 at 1500 to 2500) roughly like 1/sigma.
(d) Where the tangent residual sits (dwr_eval at 20480 x 640, iteration 0): |s|^2 fractions r in [2, 10) 0.63, [10,
 100) 0.16, [100, 1000) 0.16; by |X - P|: [0, 2) 0.17, [2, 4) 0.25, [4, 8) 0.24, >= 8 0.34. The residual of the cheapest
 c_l change is not concentrated at P.
Reading (first order).
(e) By (a) and m_lin(d)^2 = m0^2 + sigma^2 d^2 (r almost orthogonal to f0), the linearised objective on this basis stays
 below 2 m0 for |d| up to sqrt(3) m0 / sigma_244 >= 9.0e-3, and below 1.1 m0 for |d| up to 2.4e-3. On the 244 basis the
 L2 objective therefore resolves c_l only at the 1e-2 level, before the nonlinear terms and before any further fall of
 sigma. The six-digit agreement of the fitted c_l over the bases 215 to 375 (5.5763607 to 5.5763632) is a property of the
 solver path (common lineage; truncated LSQR moves c_l by about 1e-6 per segment, G37), not of the objective.
(f) Two readings remain. If sigma has a positive limit on each basis and the limit does not fall under refinement, the
 objective pins c_l at about m0 / sigma, and the Gauss-Newton corrected c_l per basis (c_fit + dcl*, with a converged
 tangent) is the quantity to follow under refinement (13.11 (c)). If sigma falls with iteration count and basis without
 a positive limit (non-closed range in the fit norm, 13.11 (b)), the fit norm does not determine c_l at all, and c_l can
 be resolved only in norms the trial space does not control well (near-P pointwise residual, J, or derivative bounds of
 the fitted shapes). The fixed-c fits at 5.60 (offset 2.4e-2, 2.7 times the linear factor-2 offset) and the 302 tangent
 (sigma_302 against sigma_244) separate the two.
(g) Reporting consequence (adopted now, before the fixed-c result): FINAL_REPORT does not quote c_l to more than three
 decimals without the fixed-c result; the six-digit value appears only with the 13.11 (d) disclaimer and this section.

### 13.13 Audit of 13.12 (verifier G53) and the between-node c_l intervals (G49, G51) (lead, 2026-10-18T05:29Z) [corrections adopted from the audit; G55 corrections applied 2026-10-18T05:49Z; measured facts; the reading in (d) is not audited]
(a) Corrections to 13.12, adopted from G53.
 - 13.12 (c), "dcl* grew roughly like 1/sigma", is withdrawn: over LSQR iterations 1500 to 2500 dcl* grew by a factor 15
   and 1/sigma by 1.8; the fraction of f0 along r/|r| (dcl* sigma / m0) grew linearly, 0.45 to 3.79 percent. dcl* is not
   converged on the 10240 x 480 tangent, and its iteration-2500 value is neither a bound nor an estimate of its limit. On
   the 20480 x 640 warm continuation (300 iterations, final) sigma fell from 3.531e-3 to 3.294e-3 and dcl* sigma rose
   from 5.61e-7 to 5.92e-7 (6 percent).
 - 13.12 (e): the linear-model offsets are lower bounds and read ">= 8.9e-3" (factor 2) and ">= 2.3e-3" (factor 1.1).
   The sentence "the L2 objective resolves c_l only at the 1e-2 level" is withdrawn. Along the tangent shapes the
   measured objective is m_nl^2 = m_lin^2 + |q|^2 d^4 with |q|^2 = 2.63 to 2.79 at |d| = 1e-3 and 3e-3 (absolute units of
   the fit objective), so the tangent objective is 1.02, 1.13, 1.41, 1.97 times m0 at |d| = 1e-3, 2e-3, 3e-3, 4.1e-3
   (shapes exist at 1e-3 and 3e-3 only; the values at 2e-3 and 4.1e-3 come from the fitted law).
   A fixed-c fit at c_fit + d has the tangent shape as a feasible start, so its objective (if solved at least as well) is
   at most m_nl(d); the doubling of the fixed-c objective is at |d| >= 4.1e-3 if sigma_244 = 3.58e-3, and nothing here
   bounds it from above. (Small wording note on G53 (b): rho = x^2 y exp(H) is not linear in the shape coefficients, so
   the tangent family is not exactly quadratic in d; the d^4 law is a measured fit.)
 - Check of that law at the fixed-c start (fixc_c6b_560_make.log): d = +2.3637e-2, m_lin = 8.66e-5, the law gives
   m_nl = 9.29e-4, the start shape (c6b segment 1 plus d times the tangent) has 9.271e-4. So the d^4 law holds within the
   2 percent set by the spread of |q|^2 (9.10e-4 to 9.37e-4) out to 2.4e-2, and the 5.60 start is dominated by the second-order term by a factor 11 in m.
 - 13.12 (f) misses a third case (G53 (c)): sigma may tend to 0 (non-closed range) while the second-order part that a
   fixed-c fit cannot absorb pins c_l, at about (sqrt(3) m0 / |q_res|)^(1/2). The fixed-c fit at 5.60 measures how much
   of the second-order term the 244 basis absorbs; it does not separate readings 1 and 2 of 13.12 (f). The 302 tangent
   at a budget equal to the 244 one does.
(b) Between-node intervals (verifier, linear tangent shapes on 244 = G49; field-level sum c6c + eps t with t the 244
 tangent = G51, two between-node resolutions). Inside every 30 percent band of the 04:47Z rule, with |h(P) - 1| <= 5.5e-8 (244, N 11250) and 4.5e-8 (302):
 offset -1e-3 on 244 (also -3e-4 to +3e-4); offsets -1.5e-3 to +3e-4 on 302 (c_l 5.57486 to 5.57666). No offset in
 [-3e-3, +3e-3] (244) or [-3e-3, +1e-3] (302) is excluded (near-P maximum below 2 times the fit throughout).
(c) Common pattern of the two levels (G49, G51; lead scans of the tangent shapes on 16384 x 640 agree in direction):
 - the near-P maximum falls toward lower c_l: 244 0.85 / 0.72 at -1e-3 / -3e-3; 302 0.75 / 0.70 / 0.69 at -1e-3 / -1.5e-3
   / -2e-3;
 - other regions rise (302: the global maximum moves into the 10-100 band next to the unrefined radial band, 1.30 at
   -2e-3; 244: the global maximum stays at the stem ring at every offset and rises, 1.11 at -3e-3), and J and the 10-100 band rise toward one side or the other (J rises toward higher c_l:
   1.46 at +1e-3 on 244, 2.2 on 302);
 - the linearised least-squares step points to higher c_l (dcl* +1.8e-4, not converged).
 The tested intervals are at least 1.3e-3 (244, [-1e-3, +3e-4], -1.5e-3 and -2e-3 not tested) and 1.8e-3 (302,
 [-1.5e-3, +3e-4], along a direction optimized on 244) wide, at near-P maxima 4.9e-6 and 2.3e-6. Both are lower bounds;
 nothing shows a shrinkage.
(d) Reading (first order; not audited). The fitted c_l of the L2 fits is held by the solver path (13.12 (e), confirmed),
 and their near-P maximum is not at a minimum over c_l: moving c_l down by 1e-3 to 2e-3 along the soft direction lowers
 it (302: by 25, 30, 31 percent at -1e-3, -1.5e-3, -2e-3; 244: by 15 percent at -1e-3, 28 percent at -3e-3) while
 other regions rise. On the 302 basis the region that rises (10-100 band) is the one the
 375 basis removed (8.0e-7 in c6d against 2.3e-6 in c6c, G48). So on c6d, and on the angularly enriched c6f, the same
 move may lower the global maximum: the max-norm (near-P) optimum in c_l of the trial family may lie 1e-3 to 2e-3 below
 the fitted 5.57636. This is a hypothesis about the trial family, not about the profile; it is tested by (i) the
 transplant of the 244 soft direction onto c6d and c6f in coefficient space (exact if the c6c, c6d and c6f bases
 contain the 244 basis by knot insertion and angular extension; for 375 see 13.14 (a)) with between-node scans, and (ii) a refitted fixed-c fit
 at about c_fit - 2e-3 on the final basis.
(e) Reporting: G50 (iii) and G51 give lower bounds on the c_l uncertainty, 1e-3 at the 244 level and 1e-3 (lower side
 1.5e-3, upper side 3e-4) at the 302 level; they are stated with the three-decimal value. If (d) holds on the final basis,
 c_l is quoted as an interval containing the tested values (SPEC section 8), reaching down at least to the lowest offset
 that is not excluded, not as 5.576.

### 13.14 Transplant of the 244 soft direction onto c6d, test of 13.13 (d) (lead, 2026-10-18T05:50Z; (e) added 2026-10-18T06:31Z) [(a) to (c), (e) measured facts; (d) and the reading in (e) heuristic; not audited]
(a) Construction (work/c6/transplant.py; outputs work/c8). t = (S(+1e-3) - S(-1e-3))/2e-3 with S(+-1e-3) the 244 tangent
 shapes tan_c6b_tan+-1e-03 (c_l 5.577363, 5.575363). The 244 knot multiset is contained in the 375 (c6d) knot multiset
 (asserted in the script; the knot vectors agree after insertion), so the transfer is exact in coefficient space; check:
 S(+1e-3) has objective 2.827574e-4 at 2048 x 480 on its own basis and on the 375 basis (agreement to 1e-9 relative).
 Shapes c6d_seg1 + d t for d = -3e-3, -2e-3, -1.5e-3, -1e-3, -5e-4, +5e-4, +1e-3; not refitted. For c6f (angular
 extension of c6d with zero coefficients) the same holds by construction.
(b) L2 objective at 20480 x 480 (c6d segment 1: 1.8870e-5): 2.739e-5, 2.201e-5, 2.057e-5, 1.969e-5, 1.917e-5, 1.875e-5,
 1.887e-5 at the d above. Minimum along t near d = +5e-4 (0.6 percent below c6d_seg1): the 244 direction is not the
 L2-soft direction of the 375 basis exactly, and c6d_seg1 is 0.6 percent above its minimum along it.
(c) Between-node scans (scripts/scansum.py; c6d_seg1 at 16384 x 640, the shapes at 32768 x 640):
     d          2-10 flux max   10-100 band   h(P) - 1
     0 (c6d)    2.43e-6         7.25e-7       +3.0e-8
     -3e-3      2.28e-6         1.20e-6       +7.0e-7
     -2e-3      1.83e-6         8.35e-7       +3.0e-7
     -1.5e-3    1.81e-6         7.89e-7       +1.7e-7
     -1e-3      1.81e-6         7.64e-7       +6.7e-8
     -5e-4      2.10e-6         7.45e-7       +7e-9
     +5e-4      2.78e-6         7.18e-7       +5e-9
     +1e-3      3.15e-6         7.04e-7       +6.3e-8
 So on the 375 basis, where the 10-100 band is no longer the limit, the global (near-P) between-node maximum falls by
 25 percent at d = -1e-3 to -1.5e-3, and the 10-100 band stays below 8.4e-7 down to -2e-3; at -3e-3 h(P) - 1 and the band
 rise. The L2 objective rises by 4 to 9 percent over the same range. The verifier's field-level run of the same pair
 (G56, in progress) is the check on the between-node numbers; their logs (not yet a report) show J(0.01) lowest near
 d = -1e-3.
(d) Reading (heuristic). The premise of 13.13 (d) holds on c6d: the max-norm optimum along the soft direction lies 1e-3
 to 1.5e-3 below the L2 fit's c_l, and the L2 optimum lies about 5e-4 above it. Neither norm is the profile's c_l. In the
 first-order picture of 13.9 to 13.11, a trial with residual size m (in either norm) and a soft direction with gain sigma
 per unit c_l determines c_l only to about m/sigma; with m0 about 1.9e-5 (L2, 375 basis at 20480 x 480) and sigma about
 3.3e-3 (244 value; not measured on 375) this is about 6e-3 for the L2 objective in the linear model (the measured d^4
 term of 13.13 (a) narrows the factor-2 width to about 4e-3 on 244), and the max-norm and J optima are different points
 in an interval of that width. The tests therefore bound the c_l uncertainty from below (13.13 (e))
 and do not show c_l to be undetermined: along the soft direction no diagnostic is flat (all rise on both sides of
 their optima, quadratically in h(P) - 1), and the soft direction is not a Phi-mode (13.6): J and the near-P maximum
 stay at the representation level along it, while a Phi-mode would show a near-P singularity growing linearly in d.
 Reporting consequence (13.13 (e) unchanged): c_l is quoted as 5.576 with the stated lower bounds, or as an interval
 reaching from the lowest non-excluded offset to the highest; the six-digit value is a reproducibility number only.
(e) Added 2026-10-18T06:31Z (measured facts; the last paragraph is a reading, not audited). G56 (verifier, field level, c6d + d t)
 confirms (c): global flux maximum 0.73 to 0.74 of the fit at d = -1e-3 (in the strip), 0.81 to 0.85 at -1.5e-3 (the
 stem ring r 8.76, theta 0.30 takes over), J(0.01) 0.68 at -1e-3; lower bound on the c_l uncertainty at the 375 level 1.5e-3
 below and 3e-4 above. G57 (c6f at LSQR it 500): every band away from P falls, the strip (r 8.28 to 8.36, theta 0.012)
 stays at 2.40e-6, J from all start angles rises by 2.1 to 2.5.
 c6f segment 1 final (it 750; objective 7.653e-6 at 20480 x 720, from 1.867e-5; c_l 5.5763624), lead scans at 32768 x 640
 (24576 x 960 in brackets), c6d segment 1 after the slash:
     2-10 flux max 2.45e-6 (2.47e-6) / 2.43e-6     10-100 4.41e-7 (4.40e-7) / 7.26e-7
     100-1000 7.2e-8 / 2.5e-7                       > 1000 1.8e-8 / 2.6e-7         rms 1.66e-8 / 5.55e-8
 J(eps_P 0.03) spread 3.05e-6 (c6d 1.1e-6). The split (jsplit, r0 20) puts 2.10e-6 of it in [0.03, 0.3) for every label
 that reaches P from above (end points (-1e-5, 0.03)) and -5.4e-7 there for the one label that reaches P from the left
 next to the axis (theta0 1.55, end point (-0.029, 0.009)); the other distance ranges contribute at most 2.6e-7. So J at
 this level measures the residual on the last 0.3 of the two approaches to P. B_3 (orig form) median 0.2999, range
 [0.2918, 0.3034]. The segment end confirms G57: the angular step lowers everything except the strip.
 Transplant of the 244 soft direction onto c6f_seg1 (fxs1_; transfer check 2.82751e-4 on both bases: exact), not refitted,
 lead scans at 32768 x 640, ratios to c6f_seg1:
     d          2-10 flux max    10-100          h(P) - 1    rms
     -1e-3      2.25e-6 (0.92)   5.12e-7 (1.16)  +1.2e-7     2.10e-8 (1.27)
     -3e-3      3.46e-6 (1.41)   9.06e-7 (2.05)  +8.5e-7     5.39e-8 (3.2)
     -1e-2      1.40e-5 (5.7)    6.72e-6 (15)    +8.3e-6     4.11e-7 (25)
 Reading: on c6f the unrefitted shift to -1e-3 gains 8 percent at the global maximum, against 25 percent on c6d. Either
 the 244 direction is a poorer approximation of the soft direction of the larger basis, or part of the strip residual on
 c6f does not move with c_l. The fixed-c fit at -1e-3 from this start (run_c6f_fixc.sh step 3, running from 06:23:21Z)
 shows whether the 375 x 150 basis reaches a lower global maximum at c_l 5.57536 than the free fit; it does not by itself
 separate the two explanations.
### 13.15 The near-axis strip left of P is an angular band-edge oscillation (lead, 2026-10-18T07:13Z) [(a) to (c) measured facts; (d) reading, heuristic, not audited. The verifier found the same independently (G61 (b) to (h), recorded 06:54Z, with the G57 wording withdrawn); (d) is revised to G61 (h)]
Signed flux-normalized residual R / (|W1 rho_x| + |W2 rho_y| + |rho|) evaluated from the coefficient files (no export) at
8192 x 2880 (theta spacing 5.5e-4) or 8192 x 1440; physical radius r, x* = 8.6008 (work/c9/strip_signed.py, strip_radial.py).
(a) Theta profile next to the axis. At r = 8.467:
    c6f_seg1 (375 radial functions, m <= 150): sign changes at theta 0.0044, 0.0185, 0.0300, 0.0415, 0.0529, 0.0638, 0.0747;
      lobes +2.46e-6 (0.0120), -1.67e-6 (0.0240), +1.23e-6 (0.0355), -9.4e-7 (0.0469); mean zero spacing 0.0117, the
      spacing of cos 2M theta with M = 134.
    c6d_seg1 (375 radial functions, m <= 100): sign changes at 0.0060, 0.0240, 0.0415, 0.0578, 0.0742; lobes +2.16e-6
      (0.0158), -2.21e-6 (0.0333), +1.74e-6 (0.0496), -1.70e-6 (0.0660); spacing 0.0170, M = 92.
 At r = 8.40 to 8.56 the spacings are 0.0116 to 0.0149 (c6f) and 0.0164 to 0.0175 (c6d). The period scales with the
 angular truncation (spacing ratio 1.45 for a truncation ratio 1.5); the amplitude does not decrease (2.2e-6 to 2.5e-6).
 G57 compared amplitudes only.
(b) Radial extent: max over theta < 0.08 at fixed r (in brackets the max over 0.08 <= theta < 0.3).
    r      0.5     1.5     4.0     6.0     7.0     7.6     8.0     8.2     8.4     8.5     8.6     8.7     9.0
    c6f  1.9e-8  1.2e-7  3.7e-7  3.8e-7  3.1e-7  2.6e-7  4.9e-7  8.2e-7  1.9e-6  2.2e-6  1.3e-6  5.0e-7  1.1e-7
    c6d    .       .       .     3.5e-7  9.1e-7  1.7e-6  2.2e-6  2.4e-6  2.3e-6    .     5.3e-7    .     1.4e-7
 (c6f off-axis band (0.08, 0.3): 6e-8 to 2e-7 for r <= 8.1, 3e-7 to 7e-7 for 8.2 <= r <= 8.8; c6d up to 1.6e-6 at 8.4 and
 1.7e-6 at 8.8.) On c6f the near-axis profile has 7 sign changes in theta < 0.08 for 3.5 <= r <= 7.5. The angular step
 100 -> 150 lowered the near-axis residual by a factor 3 to 5 on 6.6 <= r <= 8.3 and left it at 2.2e-6 on 8.4 <= r <= 8.6:
 the unresolved part moved toward P without decreasing.
(c) Dependence on c_l (unrefitted coefficient line of 13.14 on c6d, trd_<d>), largest lobe at r = 8.40 / 8.47 / 8.52:
    d = +1e-3: 2.9e-6 / 2.7e-6 / 2.4e-6;  d = 0: 2.2e-6 (8.47);  d = -1e-3: 1.8e-6 / 1.8e-6 / 1.4e-6;
    d = -3e-3: the alternating pattern breaks up (lobes 1.0e-6 to 1.4e-6, mostly positive; zero spacing 0.0125 to 0.015).
 Along this line the near-axis amplitude falls by about 5e-7 per -1e-3 in c_l, which is the G56 / G57 observation (the
 strip moves with c_l) resolved in theta. J (13.14 (e)): the one label that reaches P along the axis from the left
 (theta0 1.55, through this region) is the outlier on both bases (c6f -6.1e-7 against +1.8e-6 to +2.4e-6; c6d -1.24e-6
 against -7.8e-7 to -1.4e-7).
(d) Reading (heuristic), revised after G61 (h). The oscillation is the band-edge response of the truncated cos 2m theta
 expansion to H content next to the axis left of P that the basis carries only up to its cap. G61 (h): the content the
 cap step 100 -> 150 added (H_c6f - H_c6d) is an oscillation confined to theta < 0.08 with the same angular profile at
 every r from 7.6 to 8.56 (zeros near theta 0.007, 0.022, 0.04), amplitude growing toward P (theta = 0 values -4.2e-7 at
 r 7.6 to -9.3e-7 at 8.47) and changing sign at P; G61 (d): the H spectrum there decays algebraically (block exponents
 2 to 6, rough figure m^-3.4 at r 8.47) against 6 to 14 right of P. So the angular width does not shrink toward P (the
 first version of this item said it might); what moves toward P under the cap step is the place where the normalized
 residual stays at its cap value, because the content is largest and the normalization N_f smallest next to P.
 A possible origin, consistent with 13.1 but not tested: the characteristics that leave P almost along the axis to the
 left have labels s = xi |y|^(-A), A about 10.15, so a vertical segment at xi = -0.1, 0.05 <= y <= 0.4 carries labels |s|
 from about 1e3 to 1e12; a label-dependent inconsistency of the trial (the quantity J measures, 13.4) placed there is a
 slowly varying function of log|y| next to the axis, which is not smooth at y = 0 and has an algebraic angular spectrum.
 For a solution in P_2 the transport data at P are constant (13.6), so such structure would belong to the trial.
 Consequences: (i) the cap step 100 -> 150 did not lower the strip maximum (2.44e-6 converged on both, G61 (a)); a
 further cap step is predicted to lower it away from P only; (ii) the amplitude is tied to c_l ((c)) and to J, and the
 fixed-c_l fit at -1e-3 on c6f lowers the between-node maximum to 1.50e-6 at LSQR it 250 (G63; the control at equal
 iterations is c6f segment 2 at it 250); (iii) a representation adapted to the axis next to P (angular resolution
 concentrated at theta = 0 for r near x*, or near-axis layer functions) is the trial-class remedy if (ii) fails.

13.16 A non-C^3 structure at P in every fit (lead, 2026-10-18 about 08:05Z) [(c) is a measurement; (a), (b), (d), (e)
 are heuristic local analysis; not audited]
(a) Coupled axis system near P. Write rho = y q(x) + O(y^3), W_1 = w(x) + a_2(x) y^2 + O(y^4), W_2 = y h(x) + O(y^3).
 The O(y) parts of W.grad rho = rho, div W = 2c_l and curl W = -rho_x are
   w q' = (1 - h) q,    w' + h = 2c_l,    h' + q' = 2 a_2.
 At P: w = 0, h = 1, w' = A = 2c_l - 1, q = g* = rho_y(P). With v = q - g*, u = 1 - h and F_1 = 2 int_{x*}^x a_2 this is
 w v' = u (g* + v), u = v - F_1; linearized, A xi v' = g* (v - F_1). The homogeneous solutions are C_+ xi^lam (xi > 0)
 and C_- |xi|^lam (xi < 0), lam = g*/A, with h_sing = -q_sing at leading order. In the plane the matching structure is a
 |n|^lam layer across the weak unstable manifold of P (the characteristic leaving P vertically): across that line the
 leading part of -Delta psi = rho_x is one-dimensional, which gives U_2,sing = -rho_sing and U_1,sing of order lam + 1,
 as in the local example of the external referee answer on the strip (which is the case a_2 = 0). Whether the global
 problem admits C_+ or C_- different from 0 is not shown.
(b) Size. On the c6d_seg1 export g* = 29.7538 and A = 10.15272, so lam = 2.9306 (the same on c6f_seg1). Such terms are
 C^(2,0.93) and not C^3: they are admissible in P_2 (alpha <= 0.93) and excluded in P_3. Two corrections follow.
 13.2: "rho near P is a multiple of one function" holds for a fixed smooth W; in the coupled problem the lam-modes are
 further local solutions, excluded by C^3 and not by C^(2,alpha) with alpha < 0.93. 13.1 (referee answer (a)): Sternberg
 linearization also needs A != a A + b for a + b >= 2, that is A not an integer (A = 2j under the y-symmetry); A = 10.15
 satisfies both conditions, so the conclusion of 13.1 stands.
(c) Measurement (notes/lambda_mode/axisjump.py; H(x, 0) = log a from the shape coefficients alone; physical x = L r).
 Jump of the third x-derivative of H across x*, by separate polynomial fits on the two sides extrapolated to x* (windows
 0.05 <= |xi| <= 0.5 degree 6 / 0.1 to 0.8 degree 6 / 0.2 to 1.2 degree 7):
   c6a_seg1 +0.082 / +0.118 / +0.124      c6b_seg1 +0.132 / +0.115 / +0.127      c6c_seg1 +0.126 / +0.116 / +0.127
   c6d_seg1 +0.124 / +0.116 / +0.127      c6f_seg1 +0.120 / +0.115 / +0.126
   244 soft direction tan_c6b at d = -3e-3 / -1e-3 / +1e-3 / +3e-3 (middle window): 0.1134 / 0.1146 / 0.1160 / 0.1175;
   fxs1 at -1e-2: 0.1091; fixc_c6f_m1e-3 (last check, outer 2): 0.1155; fixc_c6b_560 (c_l 5.60 after 3 h): 0.1178.
 Controls with the same method at x* - 1.5, x* - 0.8, x* + 0.8, x* + 1.5 (smallest window): at most 0.0014 on every file.
 With the velocity (c6d_seg1 export, same windows): [q'''] = +3.70 / +3.50 / +3.79 and [h'''] = -3.37 / -3.33 / -2.99,
 so [h''']/[q'''] = -0.91 / -0.95 / -0.79 (lam-mode at leading order: -1; an exact cubic jump would need -3A/g* = -1.02);
 g* [H'''] = 3.5 agrees with [q''']. The one-window fits in axisjump.py (a smooth polynomial plus a |xi|^lam pair) do
 not determine lam: every non-integer lam in (2.2, 3.5) fits equally well. They are not quoted.
(d) Reading (heuristic). Every fit carries the same non-C^3 structure at P, [H'''] about 0.12, on five bases (215 to 375
 radial functions, m <= 100 and 150), along the soft c_l direction (slope about 0.7 per unit c_l on the 244 tangent, so
 no zero nearby: it does not select c_l) and at c_l = 5.60, with the h/q ratio of the lam-mode. Caveats: all fits share
 one lineage; the radial splines have order 7 (C^6), so the fitted H''' is smooth and the jump is a transition of
 width about two knot intervals (see (f)). Rough size of what this costs the transport residual on the axis: [H'''] delta^2 / 2 times
 |w| about A delta, with delta = 0.0065, is about 2e-7: it does not explain the 2.4e-6 strip at xi about -0.13. A test
 that separates "the problem wants it" from lineage is a refit from a start with the structure removed.
(e) Consequence for the count (heuristic). In P_2 the lam-modes add up to two local parameters at P. If the global
 linearized problem keeps them, the P_2 solutions near the branch form a family along which c_l can move; that would be
 one explanation of the soft c_l direction (13.12) and of the solver-path character of the six-digit c_l agreement. If
 (c) holds up under the verifier's check, the first lines of the report can add "not C^3 at the source point P
 (numerical, [H'''] about 0.12)" to the B_3 statement; the P_2 deliverable is unaffected.
(f) Shape of the transition (added 2026-10-18 about 08:11Z; notes/lambda_mode/h3profile.py, exact chain rule on the
 order-7 B-splines in q and on chi^j, no finite differences). The radial splines are of order 7, so H''' of every fit is
 smooth; the jump of (c) is a transition across x*. On c6d_seg1 (knot spacing 0.0165 near P) H''' goes from -0.13 at
 xi = -0.006 to +0.23 at xi = +0.016 and settles near 0 on the left, with ringing of amplitude about 0.015 at the knot
 scale on the left. [Corrected after VERIFY_REPORT G66 (d), (f): on the right it does not settle at 0.10 to 0.14; it
 decays, +0.066 at xi = 0.03, +0.089 at 0.06, +0.033 at 0.1, 0 at 0.2, -0.022 at 0.5 (c6d). The plateau sentence is
 REFUTED.] On c6b_seg1 (spacing 0.033) the transition is wider (about 0.05),
 from -0.036 at xi = -0.02 to +0.158 at xi = +0.04, with no overshoot. c6a_seg1 has spacing 0.066, which explains its
 lower value in the smallest window of (c) (0.08: the transition is wider than the 0.05 gap). So the net change stays
 at about 0.12 while its width follows the knot spacing over 0.066 / 0.033 / 0.0165. That is what a spline fit of a
 target with a jump (or an |xi|^(lam - 3) type behaviour) in H''' at P does. It does not by itself separate the problem
 from the lineage (the bases were fitted in sequence). An earlier per-knot jump script assumed cubic splines and was
 wrong; it was deleted and nothing from it is used.
(g) External referee answer (astra lam1, received 2026-10-18 about 08:18Z; claims, with lead checks). (i) The axis system,
 lam = g*/A and the polarization h_sing = -q_sing are confirmed within a conormal expansion across a curved invariant
 curve n = x - gamma(y), gamma = x* + beta y^2, beta = a_2(P)/(2 - A); on c6d a_2(P) = 0.0895, beta = -0.0110 (claim,
 not checked). The amplitude ODE along the curve propagates an amplitude but does not select it; no global count and no
 c_l family follow (agreed: 13.16 (e) stays heuristic). (ii) A pure |xi|^lam term has H''' of size |xi|^(lam - 3), with
 no finite jump; shrinking the windows by a factor 10 changes its contribution by 10^0.07, about 17 percent, so
 window stability of (c) is weak evidence. (iii) Checked by the lead: a paired cubic defect dq = J xi_+^3 / 6,
 dh = -dq, dw = J xi_+^4 / 24 changes the axis residual T = w q' + (h - 1) q by (3A - g*) J xi^3 / 6 + O(xi^4), since
 w dq' = A J xi^3 / 2 and q dh = -g* J xi^3 / 6, and the other terms are O(xi^4). With 3A - g* = 0.704 against
 3A = 30.46, this is 43 times less than the transport-only estimate. So because lam = 2.93 is close to 3, the
 least-squares fit can carry a paired cubic transition at P at very little cost, and (c) does not distinguish a
 lam-mode from such an artefact. (iv) The order-7 splines (found independently in (f)); the control values in (c)
 are small only in the smallest window (at x* + 0.8 the two larger windows reach across P). (v) Normalization: with
 the flux denominator |W_1 rho_x| + |W_2 rho_y| + |rho| the referee reproduces 2.447e-6 in the c6d strip; the stored
 'denominator' of the export gives 6.8e-7 at the same point, so every quoted residual must name its normalization (the
 report uses the flux normalization N_f throughout). Consequence: "not C^3 at P" is not put into the report. 13.16 is
 kept as a heuristic note; the decisive test (refit from a start with the transition removed, at fixed c_l, then free)
 is recorded and not scheduled (it does not bear on the P_2 deliverable).

### 13.17 B_3 across c_l, and a test that separates a P_2 family from a weakly pinned isolated profile (lead, 2026-10-18T08:26Z) [(a) measured facts; (b), (c) heuristic, not audited; (c) is a reading rule fixed before the results]
(a) B_3 (original form, median over variants, A_g = mu1; range over variants in brackets) on fits at different c_l:
 c6b_seg1 (c_l 5.5763633) 0.2991 [0.2971, 0.3015]; the 244 trial moved along its soft tangent by +1e-3 / -1e-3 in c_l
 (not refitted) 0.3003 [0.2993, 0.3021] / 0.2979 [0.2949, 0.3010]; fixc_c6b_560 after its 3 h fixed part (c_l 5.60,
 objective 1.97 times the free fit, still falling) 0.3067 [0.3037, 0.3155]; c6d_seg1 0.2972 [0.2935, 0.2997]; c6f_seg1
 0.2999 [0.2918, 0.3034]. The tangent pair gives dB_3/dc_l of about 1.2, the 5.60 fit about 0.32 per unit c_l; the ibp
 form (not converged in its end piece, G43, not quoted) moves the other way at 5.60 (0.3009 against 0.3060). So the
 sign of dB_3/dc_l is not resolved, and the variation over 5.5754 to 5.60 is at most about 0.008, against a value of
 0.30. Statement usable for first line (ii), once the verifier's estimator agrees on the candidate: B_3 is positive and
 about 0.30 on every fit with c_l between 5.5753 and 5.60, including fits with c_l held fixed. B_3 of the candidate
 fixc_c6f_m1.0e-03 is pending (its export is queued).
(b) Two pictures fit the weak pinning (13.11, 13.14, 13.16 (g)). (P1) P_2 contains a family of profiles through the free
 fit, parametrized by c_l, the members differing by conormal layers of exponent lam = g*/A = 2.93 along the invariant
 curve through P (lam > 2, so such a layer is C^(2, lam - 2), admissible in P_2 for alpha < 0.93; the referee's
 amplitude equation propagates the amplitude but does not select it). (P2) The profile is isolated in P_2 and the
 linearized operator has a small singular value in the c_l direction at the resolutions used. Under (P1) the residual
 of the best fit at a fixed offset Delta tends to 0 under refinement (the layer is resolved; a degree-7 spline with knot
 spacing h approximates |n|^lam with error about h^lam times its amplitude near the curve). Under (P2) it tends to a
 positive floor of order sigma |Delta| (sigma the least cost per unit c_l of the exact problem) while the free fit keeps
 improving. At Delta = -1e-3 the fixed fit is at the level of the free fit (8.47e-6 against 7.65e-6 in the objective),
 so this offset is below the floor of either picture at the present resolutions and does not separate them.
(c) Reading rule for the +2.4e-2 runs (fixed now, before fxv): let Q(N) = objective of the fixed fit at offset +2.4e-2
 divided by the objective of the free fit on the same basis N, both on the fit grid, after the same budget. Q(244) =
 1.97 (fixc_c6b_560; still falling about 2.5 percent per 250 iterations). If Q(375 x m <= 150) from fxv is at least 1.5
 times Q(244), the data favour (P2); if it is below Q(244) / 1.5, they favour (P1); in between, or if either fit is still
 falling by more than 2 percent per 250 iterations at its end, undecided. None of this enters the report as a statement
 about P_2; it decides only how section 4.8 (limits) words the c_l interval ("weakly pinned at the attained resolution"
 in every case; "consistent with a family" only under (P1)). Uniqueness within P_2 is not claimed in either case.
(h) Verifier audit G66 (recorded 2026-10-18T08:32Z; entered here 2026-10-18T08:37Z). (a) algebra CONFIRMED as an axis heuristic; the 2D
 local structure is not selected by the axis exponent (near P the homogeneous local solutions are rho_s = y^(1 + g*)
 F(xi / y^A) with F arbitrary). (b) CONFIRMED. (c) numbers CONFIRMED to 3 percent; the step is estimator dependent (0.05
 to 0.16) and vanishes when |xi| < 0.3 is excluded. (f) plateau REFUTED (corrected above). New verifier finding: off the
 axis the sharp feature follows the characteristic leaving P (xi_c = -a_2 y^2 / (A - 2), a_2 = 0.0897), not a radial knot
 line, and its H''' step changes sign near y = 0.5 (about -0.4 at y = 1), equal to 0.01 in c6b, c6d, c6f and the fixed-c_l
 candidate (one lineage). This contradicts a single lambda-mode layer at leading order (heuristic). "Not C^3 at P" is
 REFUTED as a first-line statement (the fits are C^6). Optional body wording (verifier): "every fit has a sharp change of
 the third derivative of log a across the characteristic leaving P (about +0.12 at P by separate polynomial fits on each
 side, changing sign near height y = 0.5 and reaching about -0.4 at y = 1); whether a solution has a C^(2, lambda - 2)
 singularity there is open." Lead decision: this sentence may go into section 4.8 (limits), nowhere else.

### 13.18 What R6 says about picture (P1) of 13.17 (b) (lead, 2026-10-18T12:05Z) [reading of the proved statement R6; heuristic; not audited]
(a) R6 (fixed-field rigidity): for a fixed field W with W_2 = y b, every C^1 solution of W.grad rho = rho on the basin of P
 that vanishes on the x-axis equals rho_y(P) y exp(-int_{-inf}^0 [b(Phi_t X) - 1] dt). So for a given W there is no local
 freedom at P: the only parameter is rho_y(P). A conormal layer of rho along a characteristic leaving P can be present only
 if this formula produces it, that is, only if b, hence W, is itself non-smooth across that characteristic.
(b) In linear coordinates at P (eigenvalues A = 2c_l - 1 and 1, R5) the characteristics are s = xi / y^A = const, so a layer
 of b of the form c(y) |s|^lam passes through the integral in (a) as a layer of rho with the same exponent lam. Since U has
 the Hoelder regularity of rho and not more (it is a singular-integral image of rho, R1), a layer of rho gives a layer of U
 of the same exponent. A member of a (P1) family therefore needs a self-consistent layer of the coupled problem: the
 nonlocal map rho -> U -> b -> rho must reproduce the layer with its amplitude. The referee's amplitude equation (13.17 (b))
 is the transport part of this map only.
(c) Reading: (a) and (b) do not exclude (P1); they say it needs the nonlocal coupling, not the transport alone, to sustain
 the layer, which makes (P1) the less economical of the two pictures. No report wording changes (13.17 (c) still decides
 the wording of 4.8). The verifier's G66 finding (the sharp change of the third derivative of log a across the
 characteristic leaving P changes sign near y = 0.5) is consistent with (b): a self-consistent layer need not have the
 single-mode amplitude of the transport part.

## 14. First-order far-field consistency of the formula (lead, 2026-10-18T17:59Z) [elementary computation, CONDITIONAL on the expansion (14.1); numerically checked on seven fits; audited by astra farfield1 (answer 18:11Z): see 14.8]
14.1 Assumption (as in 11.1, written multiplicatively). For r -> infinity
   rho = r^k Theta_0(theta) [1 + r^(k-1) Theta_1(theta) + O(r^(2k-2))],   psi = r^(k+1) F(theta) + O(r^(2k)),   k = 1/c_l,
 with the expansion differentiable term by term. (In the notation of 11.1, Theta_1 there = Theta_0 Theta_1 here.)
14.2 Orders. Polar velocity U_r = -(1/r) psi_theta, U_theta = psi_r, so U_0 = (U_r, U_theta) = (-r^k F', (k+1) r^k F).
 (a) Poisson, order r^(k-1): -Lap psi = d_x rho gives -[(k+1)^2 F + F''] = g := k cos(theta) Theta_0 - sin(theta) Theta_0'.
 With the symmetry of Setting I (psi odd in x and in y), F = sum_n F_n sin(2 n theta), g = sum_n G_n sin(2 n theta),
   F_n = G_n / (4 n^2 - (k+1)^2)   (n >= 1; no resonance since 1 < k+1 < 2).
 Growing harmonics r^(2n) sin(2 n theta) are excluded by U = O(r^k); decaying ones (the core) enter U at O(r^(-3)).
 (b) Transport, order r^k: (c_l k - 1) Theta_0 = 0, i.e. c_l = 1/k; Theta_0 is free at this order.
 (c) Transport, order r^(2k-1): c_l (2k-1) - 1 = 1 - c_l, and U_0.grad(r^k Theta_0) = r^(2k-1) [(k+1) F Theta_0' - k F' Theta_0], so
   (c_l - 1) Theta_0 Theta_1 = (k+1) F Theta_0' - k F' Theta_0.                                              (14.2c)
 Theta_1 is forced by Theta_0. The same holds at every order j >= 1 (j (1 - c_l) rho_j + [U.grad rho]_j = 0, algebraic in
 rho_j), so under 14.1 the whole far field is fixed by Theta_0 up to terms from the core. At the zeros of Theta_0 (theta = 0,
 pi/2) the right side of (14.2c) vanishes to the same order as Theta_0 since F(0) = F(pi/2) = 0.
14.3 What the formula does. With q = 1 - (1+u^2)^(-(1-k)/2), u = r/L, one has 1 - q = u^(k-1) (1 + O(u^(-2))), so the
 radial splines give b_m(q) = b_m(1) - b_m'(1) u^(k-1) + O(u^(2k-2)), and the formula has
   Theta_0 = L^(3-k) cos^2 sin exp(sum_m b_m(1) cos 2m theta + T(1) sin^2 |cos|^(p3-2)),
   Theta_1f = -L^(1-k) (sum_m b_m'(1) cos 2m theta + 2 T'(1) sin^2 |cos|^(p3-2)).
 Theta_1f is set by the endpoint slopes b_m'(1), T'(1); nothing in the formula ties it to (14.2c). Write Theta_1e for the
 right side of (14.2c) divided by (c_l - 1) Theta_0, evaluated on the formula's Theta_0. Then the residual of the formula
 for r -> infinity is
   R = (c_l X + U).grad rho - rho = (c_l - 1) r^(2k-1) Theta_0 (Theta_1e - Theta_1f) + O(r^(3k-2) Theta_0),
 and since N_v = r^k Theta_0 (1 + k + O(r^(k-1))),
   R / N_v = C(theta) r^(k-1) / (1 + k) + O(r^(2k-2)),   C := (c_l - 1)(Theta_1e - Theta_1f).
 So the formula's far residual decays like r^(k-1) (exponent -0.82) and its size is set by one coefficient function C.
14.4 Numbers (work/far/far1.py: Theta_0, Theta_1f from the stored coefficients; F by FFT on N points in theta;
 Theta_1e from (14.2c)). X3: max |Theta_1e - Theta_1f| = 4.083e-3 at theta = 1.5696 (Theta_1f = -42.5465 there; the
 figure -42.3 written here earlier and in the farfield1 question was wrong, corrected by the audit; relative 9.6e-5;
 the maximum is over 1e-3 < theta < pi/2 - 1e-3, the axis limit is 4.0843e-3), bulk (0.05 < theta < 1.4) maximum 7.9e-4; identical to 4 digits for N = 2^14, 2^15, 2^16. C(1.565) = +0.0186.
 Same quantities on the other fits (N = 2^15): F3 4.072e-3, C +0.01852; X2 4.132e-3, +0.01855; F2 4.105e-3, +0.01854;
 X1 4.301e-3, +0.01865; F0 4.178e-3, +0.01901; dom90g 4.115e-3, +0.01873 (C here at theta 1.565). The axis value of the
 coefficient error is the same on all seven, including the 90 L domain fit, within 6 percent (verifier G82: 4.07e-3 to
 4.31e-3 at pi/2); the off-axis maxima on 0.05 < theta < 1.4 are not (7.0e-4 to 1.44e-3; F0 and X1 1.5 to 1.8 times X3).
 Axis limit (far1_axis.py; Theta_0 ~ cos^2 there and V_theta ~ (k+1) V_r(pi/2) (pi/2 - theta) by div U = 0):
 Theta_1e(pi/2) = -(k+2) V_r(pi/2)/(c_l - 1), V_r = -F'. X3: V_r(pi/2) = 89.3339213, Theta_1e(pi/2) = -42.551998,
 Theta_1f(pi/2) = -42.556083, C(pi/2) = +0.018687 (N = 2^14 to 2^16 identical). The numerics lane's external referee derived
 the same identity independently and reports the same three numbers to all digits shown; the verifier confirmed the identity
 as formal algebra (G81, 17:59Z). The relative-r^(k-1) structure is the same as in 11.1 and R8 of the report.
14.5 Checks on the numerics lane's independent X3 export (24576 x 577, r to 1e4 L, closure at 1e4 L; work/far/far1_check.py,
 far1_split.py). (a) U - U_0, maximum over theta divided by max |U_theta,0|: U_theta 1.84e-3, 7.47e-4, 4.91e-4 and U_r
 2.84e-2, 1.16e-2, 7.60e-3 at r = 1000 L, 3000 L, 4999 L; both ratios to r^(k-1) are constant to 3 digits (2.83 and 43.7),
 so U - U_0 = O(r^(2k-1)) as 14.1 assumes. (b) With A = c_l X.grad rho - rho, B = U.grad rho and sc = r^(2k-1) Theta_0, at
 theta = 1.5653: (1 - c_l) Theta_1f = +193.7225 and (c_l - 1) Theta_1e = -193.7039 (sum C = +0.0186); A/sc = 175.14,
 186.48, 190.70, 191.98 and B/sc = -175.14, -186.48, -190.69, -191.97 at r = 300, 1000, 3000, 6002 L, with (A+B)/sc =
 1.4e-5, 3.3e-4, 4.5e-3, 8.6e-3 rising toward C. (c) Residual / N_v on the column theta = 1.5681 against the leading
 term C r^(k-1)/(1+k): 1.99e-7 vs 1.03e-5 (1000 L), 7.37e-7 vs 5.82e-6 (2000 L), 1.09e-6 vs 2.89e-6 (4701 L), 1.00e-6 vs
 1.87e-6 (7998 L), 9.45e-7 vs 1.62e-6 (9503 L); same sign; the ratio rises 0.02, 0.13, 0.38, 0.54, 0.58. In the bulk
 (theta = 0.818, C = -2.0e-3): -2.2e-7 vs -3.1e-7 at 4701 L, -1.8e-7 vs -1.8e-7 at 9503 L.
14.6 Reading [heuristic]. Inside the fit rows (r < 900 L) the fit has made the residual small (1e-8) by balancing the
 leading term against the next orders; beyond the rows that balance is not maintained and the residual turns toward its
 asymptote C r^(k-1)/(1+k). The far-band maximum of N_v (about 1.1e-6 at r about 3.6e4, that is 4700 L) is where the
 leading term, decaying like r^(-0.82), meets the faster decay of the balancing terms; the leading term there is 2.9e-6 and
 the observed value 0.38 of it. So: (i) the trial's far field carries a first-order inconsistency of relative size 1e-4 in
 Theta_1; the band is where its leading term is no longer offset by the higher orders; it decays at infinity;
 (ii) it is common to all fits measured; its origin is not established (the audit, 14.8: weakly constrained exterior
 coefficients, shared starts, regularization or incomplete optimization are all compatible with the data, and agreement with
 the 90 L fit does not single out the last knot interval r > 446 L); this does not establish an intrinsic floor of the family. (iii) It can be removed in principle by
 imposing (14.2c) at q = 1 (a constraint linear in b'(1), T'(1) once b(1), T(1) are given); not requested.
 Prediction (14.6 P), fixed before any reading at r > 1e4 L: in the formula-continued convention, next to the y-axis and at
 theta = 0.82, the ratio of r^(1-k) R / N_v to C(theta)/(1+k) (C from the stored coefficients by far1.py) is within 0.15 of 1
 at r = 1e5 L and closer to 1 at 5e5 L than at 1e5 L, on X3 and on any later fit. (A prediction of the form "the band
 r > 1e4 L changes by the factor by which C changes" would be unsound: on a fit with rows to 9000 L the balanced region moves out and the
 leading term itself is smaller there by (10)^(k-1) = 0.15 even with C unchanged.) Reading rule for step 44, fixed now: if
 the dom9000g band 1000 L < r <= 9000 L falls (ratio <= 0.5) while its C at the axis is within 10 percent of X3's, the fall
 is the rows balancing higher orders over a longer range, not removal of the first-order inconsistency, and the r -> infinity
 residual is unchanged.
14.7 Status. 14.2 is a formal computation under 14.1; 14.1 itself (existence of the expansion for a solution) is not
 proved. 14.4-14.5 are numerical facts about trial functions, not about a solution. Nothing here bears on P_2 or on c_l.
14.8 Audit and the third-order expansion (2026-10-18, after the farfield1 answer of 18:11Z). Verdicts on the question's
 claims: C1 (orders) CORRECT WITH QUALIFICATION: the recurrence j (1 - c_l) A_j + sum_{p+q=j-1} [-alpha_q F_p' A_q +
 beta_p F_p A_q'] = 0 (alpha_j = k + j (k-1), beta_j = alpha_j + 1; additive coefficients rho = sum r^alpha_j A_j) holds in
 the pure-power sector; no elliptic resonance beta_j = 2n for j <= 3; a compact core change gives streamfunction multipoles
 from r^-2 sin 2 theta, a transport term of relative order r^-4, between the j = 4 and j = 5 terms, so a full expansion must
 contain them. Axis limits Theta_1e(0) = F'(0)/(c_l - 1), Theta_1e(pi/2) = (k+2) F'(pi/2)/(c_l - 1) (the same as 14.4).
 C2 (formula side) CORRECT; the factors chi^j, s^(p3/2) and log(1+u^2) first enter at relative order u^-2, which lies
 between u^(2k-2) and u^(3k-3). C3 (residual limit) CORRECT WITH QUALIFICATION: needs c_l k = 1 exactly (with drift c~ the
 limit of R/N_v is (c~ k - 1)/(1+k); the export's identity value 5.57536260723 against 1/k = 5.57536261064 gives a constant
 offset -5.2e-10, negligible here) and control of the velocity remainder, which the canonical inversion supplies for this
 trial. C4 (numbers, reading) CORRECT WITH QUALIFICATION: numbers reproduced (4.0831e-3, 7.906e-4, axis 4.0843e-3); a single
 next term does not describe the approach; the export-closure explanation is excluded (correcting the exterior velocity
 beyond 1e4 L changes R/N_v by 1.4e-10 to 7.6e-10 on the near-axis column); the causal claim about the last spline interval
 is too strong (14.6 (ii) now reads accordingly). C5(a) CORRECT WITH QUALIFICATION: the constraint is linear in (b'(1),
 T'(1)) for fixed k, L, b(1), T(1); not exactly representable; sampled minimax 2.1e-5 over the quadrant, 6.0e-6 on
 1.4 < theta <= pi/2 with a weighted fit (6e-5 elsewhere). C5(b) WRONG: that was the "same factor within 30 percent"
 prediction, which I had already withdrawn before the answer (14.6) for the reason the audit gives; prediction P was not
 in the question and is not audited.
 Third order (work/far/far2.py, written by me without reading the referee's script; output far2_X3.txt, far2_x3far.json).
 With delta = r^(k-1) (r absolute) and eps = 1 - q = L^(1-k) delta (1 + O(r^-2)), H = (k-3) log u + E + sum_i (-1)^i eps^i
 D_i / i!, D_i = sum_m b_m^(i)(1) cos 2 m theta + 2^i T^(i)(1) v, v = cos^(p3-2) sin^2; so rho / (r^k Theta_0) = 1 + a_1 delta
 + a_2 delta^2 + a_3 delta^3 + h r^-2 + ..., with h = L^2 [(k-3)/2 - r_0^2 sum_m max(m-1,0) b_m(1) cos 2 m theta - (p3/2)
 T(1) v]. The pure-power residuals R_j follow from the recurrence with the formula's own A_j and F_p (p <= 2, by FFT); the
 geometric term gives R_h = (c_l (k-2) - 1) h = -2 c_l h, since at the power r^(k-2) only the drift acts and the exact
 expansion has no such term. Expanding N_v = |rho| + |X.grad rho| + |U.grad rho| to the same order:
   R / N_v = q_1 delta + q_2 delta^2 + q_h r^-2 + q_3 delta^3 + ...,
 on X3 at theta = 1.5681: q_1 = +0.0158217, q_2 = -88.782, q_h = +782.10, q_3 = +1.1900e5 (identical for 2^15 and 2^16
 points); the referee's independent values are 0.0158215, -88.783, 782.102, 119002 (agreement to 4-5 digits, the
 difference is the column position). The four terms give 1.258e-6 at 4701 L and 0.965e-6 at 9503 L, against the measured
 1.092e-6 and 0.945e-6; at 1000 L they give 1.9e-5 against 2.0e-7, so the series is of no use inside the fit rows. At theta
 0.818 the sums are -3.09e-7 (4701 L) and -1.85e-7 (9503 L) against -2.25e-7 and -1.77e-7. Reading [numerical]: the far band
 is the sum of the first-order mismatch (q_1), a second-order mismatch R_2 = -101.9 next to the axis (0.9 percent of the two
 terms it balances, 2 (1 - c_l) a_2 = -11526 and the transport term +11424, normalized by Theta_0; at third order R_3 =
 +1.24e5 against 3 (1 - c_l) a_3 = +5.59e5, 22 percent) and the geometric term; the r^-2 term is fixed by k, L,
 b(1), T(1) and the factors of the trial, so no choice of the slopes b^(i)(1), T^(i)(1) removes it; it decays faster than
 the others. On the same series P (14.6) is expected to hold on X3: the predicted ratio of r^(1-k) R/N_v to q_1 is 0.924 at
 1e5 L and 0.979 at 5e5 L next to the axis, 1.112 and 1.045 at theta 0.818 (the series, not a measurement).
14.9 My own reading of P (not the verifier's test; work/far/ptest.py, ptest_X3_R1e7.json, ptest_X3_R1e7_offset.txt;
 2026-10-18 about 18:24Z, after P was fixed at 18:04:24Z). X3 density everywhere; velocity by my modal inverse
 (diagnose.py, 24576 x 576, inverse domain r <= 1e7 L, two-term exterior beyond); residual with the identity value c_l =
 5.575362607209 of that inverse (stored 1/k = 5.575362610642), which adds the constant (c_l k - 1)/(1+k) = -5.22e-10 to
 R / N_v. Signed measured / leading q_1 delta: next to the axis (theta 1.56807) 0.378, 0.584, 0.810, 0.922, 0.962, 0.970,
 0.973 at 4699, 9500, 3e4, 1e5, 3e5, 5e5, 1e6 L; at theta 0.818: 0.716, 1.008, 1.157, 1.133, 1.114, 1.123, 1.165. P holds
 on both columns (1e5 L within 0.15 of 1; 5e5 L closer), at theta 0.818 narrowly. The departure at theta 0.818 is the
 constant: with it removed the ratios are 1.113 (1e5 L), 1.046 (5e5 L), 1.029 (1e6 L), 1.014 (3e6 L). Measured against
 series (14.8) + constant: 0.9990, 0.99990, 0.99995 ... 0.99995 next to the axis at 3e4 L ... 3e6 L, 1.0000 at theta 1.546,
 and 0.9989 to 1.0010 at theta 0.818 for 3e4 L ... 3e6 L. Reading [numerical]: beyond 3e4 L the trial's far residual is
 the third-order series of its own expansion plus the drift constant, to 1e-3 relative; nothing else is present at that
 level. The r -> infinity limit of R / N_v is the constant (c_l k - 1)/(1+k) of the evaluator's c_l (here -5.2e-10),
 consistent with the audit's C3 qualification.
 Verifier G82 (18:24:12Z, own code far1_ver.py and farP.py, R = 1e6 L and 1e8 L): G81 numbers CONFIRMED (V_r(pi/2) 89.3339213,
 forced -42.5519983, stored -42.5560826, C(pi/2) +0.0186871); P CONFIRMED at every named column in both c_l conventions, with
 qualifications: within 0.006 of the y-axis the node scatter at 3e5 to 5e5 L (0.80 to 1.08) does not resolve "closer"; on
 the first column outside it (1.56343) 0.921 at 1e5 L, 0.981 at 5e5 L; at 0.8173 the windows separate only with c_l = 1/k;
 beyond 1e6 L that evaluator scatters. My 18:13:30Z wording "off the axis the leading term is reached inside 1e4 L" is
 REFUTED: off the axis the ratio crosses 1 near 9500 L, overshoots to 1.15 to 1.18 at 3e4 L and returns slowly (1.05 to 1.08
 at 5e5 L with c_l = 1/k); where C is small (theta 0.1, 1.2) the higher orders dominate longer. Withdrawn.

14.10 (2026-10-18T19:34:10Z, after G88 (b)). Third order. On c6g next to the y-axis (theta 1.56811) the order-3 residual R3 / Theta_0 = +1.2424e5
is the pure-power part 3 (1 - c_l) a_3 = +5.5893e5 plus the velocity part -4.3468e5, 22 percent of the larger: a third-order
inconsistency of the same kind as the first two (1e-4 at first order, 0.9 percent at second), not a by-product of the series
division. At the band maximum (about 4860 L) the first- and second-order terms of R / N_v cancel (+2.810e-6, -2.801e-6), so
the band value there is the r^-2 term (5.66e-7) plus the third-order term (6.67e-7), series sum 1.242e-6 against the measured
1.10e-6. The relative sizes at orders 1, 2, 3 are the same on six fits (X3, F3, X2, F2, X1, F0: 0.96e-4 to 1.00e-4, 0.0088 to
0.0092, 0.221 to 0.233; work/far/far2_multi.json). The earlier statement here and in 4.5 that the band is a first- plus
second-order effect with the r^-2 terms is withdrawn (G88 (b) refuted it; G84 (d) had confirmed it and was withdrawn).
The third-order coefficients involve the end derivatives of the radial splines to order 3, so, unlike the r^-2 terms, they
are not fixed by the end values alone.

14.11 (2026-10-18T20:29:16Z, after step 44). The far-field coefficients of the 9000 L domain row dom9000g (c6g end, fixed c_l, fit rows
r < 9000 L, closure at 1e4 L, 20750 iterations; shape md5 269865ef) [measured facts on the lead's tools; the reading is
numerical, not audited; verifier check requested, NOTES 20:28:25Z]. Next to the y-axis (theta 1.56811, far2.py): q_1 =
+4.938e-4 (X3 +1.582e-2, factor 0.031), q_2 = -14.65 (X3 -88.78, factor 0.165), q_h = 782.10 (X3 782.10), q_3 = -3.461e4 (X3
+1.190e5). C at the axis (far1.py, stable in N from 16384 to 65536): -1.4129e-4 against c6g -4.0843e-3 (factor 0.035), i.e.
3.3e-6 of Theta_1(pi/2) = -42.55 against 9.6e-5. The relative inconsistencies at orders 1, 2, 3 (14.10 measure) are 3.0e-6,
1.5e-3, 0.101 against X3's 9.6e-5, 8.8e-3, 0.222. At theta 0.818: q_1 = +1.440e-3, q_2 = -44.55, q_h = 2388.9, q_3 = -1.120e5.
Series terms next to the axis (orders 1, 2, r^-2, 3):
  4701 L    +9.0e-8   -4.88e-7   +6.05e-7   -2.10e-7    sum -3.6e-9
  9503 L    +5.1e-8   -1.54e-7   +1.48e-7   -3.7e-8     sum +7.6e-9
  1e5 L     +7.3e-9   -3.2e-9    +1.3e-9    -1.1e-10    sum +5.3e-9
  5e5 L     +2.0e-9   -2.3e-10   +5.3e-11   -2e-12      sum +1.8e-9
The lead's evaluator (ptest.py, 24576 x 576, inverse to 1e7 L, formula continued) gives next to the axis 2.9e-9 (4699 L),
7.4e-9 (9500 L), 8.9e-9 (3e4 L), 5.3e-9 (1e5 L), 1.0e-9 (1e6 L), against X3's 1.09e-6, 9.46e-7, 5.11e-7, 2.17e-7, 3.5e-8; at
theta 0.818 the largest value is +2.5e-8 (3e4 L). Measured / series is 0.99 to 1.00 for r >= 3e4 L on the four columns.
Reading [numerical]: with the same basis and the same c_l, rows reaching 9000 L lower the first-order coefficient on the axis
about 30-fold, so the first-order inconsistency of X3 (14.1 to 14.10) is not a floor of the representation at that basis; it
is consistent with end slopes that rows ending at 900 L constrain only weakly. The r^-2 term is unchanged, as 14.8 says it must be when the end
values b(1), T(1) do not move; inside the fitted range it is cancelled by the second- and third-order terms (at 4701 L
+6.05e-7 against -4.88e-7 and -2.10e-7), and beyond 1e4 L the first-order term takes over again (at 1e5 L 7.3e-9 of the
5.3e-9 sum). This is a property of a domain row, not of the candidate X3, whose far band stays as stated in 4.5.

14.11 corrections (2026-10-18T21:10:26Z, after verifier G92 (B) 6, G92 addendum and G93 (A) 9).
(a) Attribution. "rows reaching 9000 L lower the first-order coefficient about 30-fold" is a measurement of dom9000g against c6g,
    and dom9000g differs from c6g by the rows AND by 20750 further iterations. Correct reading: "dom9000g (rows to 9000 L, c6g +
    20750 iterations) has a first-order coefficient on the axis about 30 times smaller". Attribution to the rows is OPEN until
    c6g2 (step 45: c6g + 20750 iterations, rows to 900 L) has its C at the axis and its far bands.
(b) Mechanism. The fall of the band 1000 L to 9000 L is not the removal of the first-order term alone. With X3's other
    coefficients and q_1 = 0 the series at X3's band maximum (4860 L) would read -2.80e-6 + 5.7e-7 + 6.7e-7 = -1.56e-6, larger
    in size than X3's value. On dom9000g q_2 is 0.165 of X3's and q_3 has the opposite sign, and the series sum at 4858 L
    (-2.5e-9) is a cancellation among orders 2, r^-2 and 3. The separate evaluator (G93 (A) 9 (iii)) measures R / N_v at 1000 L
    and 4701 L on six columns within 0.07 of the y-axis at -0.30 to +0.15 times dom9000g's own first-order term: its band value
    is set by the higher orders. The heuristic "consistent with end slopes that rows ending at 900 L constrain only weakly" is
    a labelled heuristic, not checked.
(c) ptest on dom9000g: "measured / series 0.99 to 1.00 for r >= 3e4 L on the four columns" is CONFIRMED on theta 0.818 and OPEN
    on the near-axis columns on the separate evaluator (its resolution there is about 1e-9 to 2e-9 in R / N_v, the size of the
    values). Not used in the report.

## 15. The two B_3 measurements of a trial: the defect identity with R10's H (lead, 2026-10-19T01:11:52Z) [elementary identity; checked symbolically, work/b3id/check_identity.py; external referee astra b3def1 (answer 2026-10-19T01:16Z): CONFIRMED with conditions and a correction of the quotient coefficients, see (e); verifier check requested NOTES 2026-10-19T01:23:32Z]

Setting. A trial rho (not a solution) with W = c_l X + U, U = (-psi_y, psi_x) for any stream function psi. On the x-axis write
rho = y g + y^3 G3 + O(y^5), W_1 = w + y^2 a2 + O(y^4), W_2 = y h + y^3 b3 + O(y^5). Since div U = 0 identically,
  w' + h = 2 c_l   and   a2' + 3 b3 = 0   hold exactly for every trial (orders y^0 and y^2 of div W = 2 c_l).
The equation W.grad rho = rho has on the x-axis the y^1 and y^3 coefficients (SPEC D12)
  T1 = w g' + (h - 1) g,     T3 = w G3' + (3h - 1) G3 + a2 g' + b3 g = w G3' + (3h - 1) G3 - F3,  F3 = -a2 g' - b3 g.
For an exact profile T1 = T3 = 0. Let beta = 2/A, A = 2 c_l - 1, and let H = N g^(3+beta) |w|^(-beta) be R10's function.

(a) Claim. On (0, x*), where w < 0,
      -F3/(w H) = -(G3/H)' + (T3 - (3 + beta) (G3/g) T1)/(w H).
    Proof. H'/H = (3 + beta) g'/g - beta w'/w. Write g'/g = (1 - h)/w + T1/(g w) (definition of T1) and w' = 2 c_l - h.
    Since 2 c_l beta = 2 + beta, w H'/H = (3 + beta)(1 - h) + (3 + beta) T1/g - beta (2 c_l - h) = 1 - 3h + (3 + beta) T1/g.
    Hence (G3/H)' = (w G3' - w (H'/H) G3)/(w H) = (w G3' + (3h - 1) G3 - (3 + beta) G3 T1/g)/(w H)
    = (T3 + F3 - (3 + beta) G3 T1/g)/(w H), which is the claim. (Symbolic check with arbitrary g, G3, a2, b3, w: residual 0.)
    For an exact profile T1 = 0 and H is the homogeneous solution of the G3 equation; for a trial it is not, and the T1 term
    is the correction. SPEC D12 states the identity with the homogeneous solution of the trial's own equation
    (H_h'/H_h = (1 - 3h)/w), for which only T3 appears; that is a different function from R10's H when T1 != 0.
(b) With b3 = -a2'/3, -F3/(w H) = (1/(3N)) (a2/g^3)' m^(beta - 1), m = |w|/g: the integrand of R10's B_3 (symbolic and numeric
    check). So R10's formula evaluated on the trial's axis data (w, g, a2) is f.p. int_0^{x*} -F3/(w H) dx.
(c) Finite parts. Near 0, g = g0 x^2 (1 + O(x^2)), |w| = A x (1 + O(x^2)) (w'(0) = 1 - 2 c_l by the identity c_l = (1 +
    psi_xy(0))/3, which the trials satisfy to 3e-9), so H = x^(p_3) (1 + O(x^2)) with N = A^beta / g0^(3+beta), p_3 = 6 + beta.
    If G3 = (even expansion starting at x^2) + B_own x^(p_3) (1 + o(1)), then G3/H = c_2 x^(2 - p_3) + c_4 x^(4 - p_3) +
    c_6 x^(6 - p_3) + B_own + o(1) (p_3 in (6, 8), never an even integer), and at x* G3/H -> 0 (beta > 0, w has a simple zero,
    G3 finite). So f.p. int_0^{x*} -(G3/H)' dx = B_own, and
      [R10's formula on the trial's axis data] = B_own + f.p. int_0^{x*} (T3 - (3 + beta)(G3/g) T1)/(w H) dx,
    provided the defect integrand has a finite-part expansion at 0 in the same powers (it does when T1, T3 are smooth
    multiples of the axis powers, as for the trials of 4.2). B_own is the trial's own coefficient of y^3 |x|^(p_3) (in R10's
    normalization H ~ x^(p_3)).
(d) Consequence for the report (4.1 remark, 4.8, (ii)). The difference estimator - own coefficient (0.30 - 0.046, about +0.25 in
    natural units) is the finite part of a weighted combination of the trial's defects in the y^1 AND y^3 coefficients of the
    equation on the x-axis, not of the y^3 defect alone, when the estimator is R10's formula. The other two quoted forms of the
    independent evaluator use further exact-profile relations and give values within the quoted range 0.291 to 0.311.
    Report wording to be corrected accordingly (NOTES; astra audit requested).
(e) External referee (astra b3def1, collected 2026-10-19T01:21:06Z). (1) CORRECT. (2) CORRECT wherever g > 0 (hypothesis g > 0 on (0, x*]
    needed for the real powers; the trials satisfy it). (3) CORRECT pointwise; the integrals agree when they exist under the
    same finite-part convention. (4) CONDITIONAL, conclusion correct under: H = x^(p_3) K(x), K = 1 + u2 x^2 + u4 x^4 + O(x^6)
    (even expansions of g/x^2 and |w|/(A x), true for the trials: g/x^2 = a(x, 0) is smooth and even, the fractional term
    vanishes on the x-axis, and its velocity contributes to w only at order x^(p_3 + 2) or higher), and g(x*) > 0 with
    smooth data at x* (then G3/H = O(s^beta) -> 0 and both integrands are O(s^(beta - 1)), s = x* - x). Correction to my (c):
    the coefficients of x^(4 - p_3), x^(6 - p_3) in G3/H are c4 - u2 c2 and c6 - u2 c4 + (u2^2 - u4) c2, not c4, c6; the
    constant term is B_own. The lower-endpoint step needs only the fundamental theorem of calculus on [eps, b], not a
    differentiated remainder. General form: R10 on the trial = B_own - lim_{x -> x*} G3/H + f.p. int (T3 - (3 + beta)(G3/g) T1)/(w H).
    (5) CORRECT as an objection to a T3-only formula with R10's H; the H_h alternative is correct pointwise, and after
    integration it needs lim G3/H_h = 0 at x*, guaranteed by h(x*) > 1/3 (the trials have h(P) = 1 to 1e-6); H/H_h =
    exp((3 + beta) int_0^x T1/(g w) dt) (T1 = O(x^4) at 0). Remark of the referee: at c_l = 3/2 the exponents become odd
    integers (not relevant here, c_l about 5.57). The referee could not consult its second model (credential failure).
    Status: (a) to (d) CONFIRMED by the external referee with the conditions above, all satisfied by the trials of 4.2;
    verifier check requested with the report diff.

## 16. The equal-budget fixed-c_l profile on 375 x m <= 150 (lead, 2026-10-19T01:32:41Z) [measured facts from G109 and the numerics relay of row 38; the models in (b) are heuristic; predictions recorded before rows 52 / 53 end; not audited; not for the report]
(a) L2 objective at 21500 iterations, ratio to F2 (free, 750 + 20750): d = -2e-3 (fxm2g) 0.926, -1e-3 (X2) 0.962, 0 (F2) 1, +2e-3
    (fxu2g, numerics relay; verifier reading pending) 1.078. Start objectives of the transplants F0 + d t: 1.466e-5 (d = -2e-3) and
    9.97e-6 (+2e-3), so the order of the ends is not inherited from the starts. The free fits F2, F3 moved c_l UP (+6.9e-6, +2.2e-7
    in 20750 iterations), the opposite direction from the profile's descent; the free c_l is set by the identity on the current rho
    and moves only along what LSQR reaches in a segment, so this is not a contradiction, but it means the free branch does not
    follow the profile's slope at these budgets.
(b) Fits (work/profile/fit_profile.py, d in units of 1e-3): line 1.0011 + 0.0381 d (residuals about 1e-3); parabola 0.99972 +
    0.03797 d + 5.97e-4 d^2 (residuals below 4e-4); floor model sqrt(a^2 + s^2 (d - d0)^2) with a 0.670, s 0.0513, d0 -14.5 (the
    form of picture (P2) of 13.17 (b) with a budget floor a; residuals below 4e-4). The curvature is at the level of the path noise
    (LSQR paths differ at 1e-4 relative after hundreds of iterations, 5 (b)), so it is only marginally detected. Predictions for
    the ratio at d = -4e-3: 0.849 (line), 0.857 (parabola), 0.859 (floor model); at d = -8e-3: 0.697, 0.734, 0.748.
(c) Reading (heuristic). If row 52 lands near 0.85 and row 53 near 0.70 to 0.75, the residual on this basis keeps falling toward
    smaller c_l through the tested span and the span's lower end stays unbracketed at this budget; the report then says exactly
    that. A turn (row 52 above row 37's 0.926) would bracket the minimum of this basis and budget between -4e-3 and -1e-3. Neither
    outcome locates the exponent of an exact profile (13.9 to 13.11), and neither changes the candidate (decided by G74).
(d) Outcome of row 52 (2026-10-19T02:47:37Z; numerics chain line, verifier reading pending): L2 3.654235e-6 = 0.858 of F2's, against the
    predictions 0.849 (line), 0.857 (parabola), 0.859 (floor model) of (b) and the verifier's quadratic in L2^2 (about 0.864,
    recorded before the run). The two curved fits of (b) are within 0.001 of row 52, the line 0.009 below it. Row 39 (G114, c_l
    5.6004662): L2 2.036, excluded at this level; the floor model of (b) gives sqrt(0.670^2 + 0.0513^2 (24 + 14.5)^2) = 2.08 at
    d = +24 (2.4 percent above), the parabola 2.25 (11 percent above); both computed, not hand-estimated. Prediction for
    row 53 (d = -8e-3) unchanged: 0.734 (parabola), 0.748 (floor model).
(e) Rows 40 and 53 (2026-10-19T03:45:47Z; numerics chain lines, verifier readings pending) and a prediction for rows 54 and 55 recorded
    before their results. Row 40 (d = +3e-3, c_l 5.5793640): L2 4.748455e-6 = 1.115 of F2's. Row 53 (d = -8e-3, c_l
    5.5683739): L2 3.157027e-6 = 0.741 of F2's, against the predictions 0.734 (parabola) and 0.748 (floor model) of (b).
    Ratios to F2 over d = -8, -4, -2, -1, 0, 2, 3, 24 (units 1e-3): 0.741, 0.858, 0.926, 0.962, 1, 1.078, 1.115, 2.036; the
    slope per 1e-3 falls from 0.039 (0 to 2) to 0.029 (-8 to -4). A quadratic in d for L2^2 (units 1e-12) fitted to the seven
    rows with d <= 3 gives 0.04276 d^2 + 1.3620 d + 18.122; it predicts 2.0395 at d = +24 (row 39: 2.036, not in the fit) and
    has its vertex at d = -15.9, ratio 0.633 there. Predictions, recorded now: row 54 (d = -16, c_l 5.5604082) about 0.633;
    row 55 (d = -24, c_l 5.5524653, start norm 1.48e-3 against 1.64e-3 for row 39) about 0.745, that is above row 54, so
    that row 55 would bracket the lower end of the tested span at this budget if the quadratic holds. Heuristic: a fit of
    equal-budget objectives from transplanted starts; it does not locate an exponent of an exact profile, and its vertex
    is a property of the objective at this basis and budget. If it holds, the objective at this budget is smallest near
    c_l 5.560, below both the candidate's 5.5753626 and the free fits' 5.57637; the report already states that the
    selection compares residual maxima of fits and that the equation is not seen to select c_l (iv), 4.3, 4.8.

## 17. The nested pair on m <= 200: what the two pictures predict (lead, 2026-10-19T03:55:22Z) [heuristic; recorded before steps 56 / 57 run; not audited; not for the report]
(a) Setting (NOTES_FOR_TEAM 2026-10-19T03:54:45Z, SPEC v4.16). Row 39 (fixed c_l 5.6004662, 375 x m <= 150, 21500
 iterations, flattened at -0.49 percent per 1000 iterations, L2 8.671252e-6 = 2.036 x F2) and row 53 (5.5683739, L2
 3.157027e-6 = 0.741 x F2, -0.44 percent per 1000) are continued on m <= 200 as X2 was continued to X3 (20750 iterations
 at 20480 x 960). On that step X2 -> X3 went 4.096686e-6 -> 1.6192702e-6 (factor 2.53) and F2 -> F3 4.258616e-6 ->
 1.6641961e-6 (2.56).
(b) Picture (P2) (isolated profile, least cost sigma per unit c_l): the objective of a fixed fit at offset Delta from the
 exact exponent behaves like (sigma^2 Delta^2 + e_N^2)^(1/2), e_N the discretization and budget error of the fits near
 the exponent. If the 375 x m <= 150 value of row 39 is split this way with e_150 = L2(F2), the mismatch part is
 (8.671^2 - 4.259^2)^(1/2) e-6 = 7.55e-6; with e_200 = L2(F3) the m <= 200 continuation of row 39 would end near
 (7.55^2 + 1.66^2)^(1/2) e-6 = 7.7e-6, Q_200 about 4.7 (above the 3.05 threshold). This assumes the exact exponent is
 within about 1e-2 of F2's, which the lower-end rows do not support (the objective at equal budget still falls at
 5.5684); with an exact exponent further down, both sides of the ratio carry mismatch and Q_200 is smaller.
(c) Picture (P1) (a family; the fixed fit at 5.60 approximates a member): the objective at 5.60 falls under refinement
 like the free fit's, Q_200 about Q_150 = 2.0 (undecided band 1.36 to 3.05), or less if the member's layer is better
 resolved on m <= 200.
(d) Row 57: under (P1) the ratio L2(57) / L2(X3) is expected near 0.771 (both members, same refinement); under (P2) with
 the exact exponent near or below 5.568 it may fall below 0.771, with the exact exponent near 5.576 it rises toward or
 above 1. No threshold is set; the values are reported.
(e) Prediction recorded now: Q_200 between 2 and 3 (undecided) is the most likely outcome given the softness of the
 lower end; a value above 3.05 would be the first datum favouring an isolated profile.

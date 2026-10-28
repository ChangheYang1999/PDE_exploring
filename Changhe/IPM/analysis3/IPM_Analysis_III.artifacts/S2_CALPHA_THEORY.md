# S2_CALPHA_THEORY.md: Hoelder estimates for h (Avenue II)

Final version at the end of the run (2026-10-28, 18:20 UTC), published with the S2 theory report; the dated list that
follows records its revision history. Labels and verification record numbers (V001, ...) are as in the report.

First version 2026-10-28T02:01Z (theory author), revised 2026-10-28T02:08Z after V022 to V025 and 2026-10-28T02:34Z after V028 to
V030, 02:54Z after V036 (C^4 hypothesis in S(d)), 03:08Z after V038 (Lipschitz velocity is sufficient, not shown necessary) and 04:46Z (C^{1,alpha} limit across the x-axis segment from Prop F4 of S2_L2_THEORY.md 6.2), and 12:04Z (section 10: status at 12:04Z, after V178), and 13:52Z (V201: the angular factor in the strain bound of section 6; the precise hypotheses of Lemmas N and N' in sections 0, 8 and 10), and 14:09Z (V203 to V208: S(e), the localized origin inverses on C^alpha_2 for every alpha < 1; sections 0, 2, 7 to 10), and 14:12Z (V211: Lemma N'' in sections 0, 4, 7 to 10), and 14:20Z (V213 to V217: 3.1(iii), the actual source operator on C^alpha intersected with L^2; the relative-domain density statement; sections 0, 2, 3, 7 to 10), and 14:34Z (V219: the sharp delta^2 rate of the normalized coupling, 2(e), 0, 8, 9), and 14:58Z (V222, V224, V226 to V228: 3.4, the common weighted target Y and the closed global realization; two far obstructions to a bounded inverse on Y, DERIVED; sections 0, 7 to 10) and 15:11Z (V232, V234: the far obstructions on Y are THEOREMS; V235, V236: the scaled far target Z, 3.4(g)) and 15:19Z (V229, V230, V238: sharpness of E_2 in 3.4(b); V239 in 3.4(g)) and 15:24Z (audit remarks on V235 in 3.4(g3), (g5)) and 15:29Z (V242: (g4) THEOREM; V243: (g6) and the candidate Z_2) and 15:34Z (V244: (g1) to (g3) THEOREM; V245: the
candidate Z_2) and 15:57Z (review corrections V253; V246, V247, V249 integrated: V239, V240, V241 and V243 are
THEOREMS, the Y statements hold on E_2 and for every gamma > 4k) and 16:01Z (V254: the Z_2 statements of 3.4(g) are
THEOREMS; V256: the turning-height non-surjectivity on Z_2, DERIVED; sections 0, 3.4(g), 7 to 10) and 16:14Z (V257:
the divided-velocity refinement, DERIVED; sections 0, 3.4(g), 7, 9, 10) and 16:20Z (V262: the turning-height
obstruction is a THEOREM; V261: the joint-cofactor candidate target, DERIVED; 3.4(g), 9, 10) and 16:25Z (V265: the
refinement V257 is a THEOREM; V264: nonlinear derivative loss on Z_cof, DERIVED; sections 0, 3.4(g), 7, 9, 10) and 16:36Z (V268: V261 is a THEOREM; V266: transport alone not onto Z_2 or Z_cof near the source, DERIVED; 0, 3.4(g), 9, 10) and 16:41Z (V271: V264 is a THEOREM; 3.4(g), 9, 10) and 16:43Z (V272: V266 is a THEOREM; 3.4(g), 9, 10) and 16:56Z (V274: review corrections; 3.4(g), 9) and 17:12Z (V278, V281: the renormalized tail rate is sharp, also on ker c, 3.4(b)) and 17:17Z (V287: that sharpness is a THEOREM) and 17:25Z (exterior inverses in the answer of section 4). Labels as in S2_L2_THEORY.md: THEOREM only after a verifier verdict, DERIVED
(proof written here, awaiting independent check), CONDITIONAL, NUMERICAL, OPEN, REFUTED. The verdict status of each
item is in section 9.

## 0. Summary of the answers

- Frozen origin saddle (section 2). Isotropic C^alpha has an inverse only for alpha < 1/D, about 0.0469 (Proposition S(a)).
  This is sharp: for alpha > 1/D a smooth compactly supported forcing gives the bounded solution an exact |y|^{1/D}
  singularity along the whole incoming x-axis (S(b)). Anisotropic classes C^alpha_p work. In these classes the
  y-Hoelder seminorm is weighted by |x|^p, the order to which the data vanish on the outgoing y-axis. T_0^{-1} is
  bounded on C^alpha_p iff 1 + pA > D alpha, with explicit constants (S(c)). At p = 2 (the natural x^2 structure)
  this holds for every alpha < 1. The weighted sup version of Proposition N1 also holds: coercivity together with
  exclusion of x^2 y forces |x|^a weights with a > 2 (Proposition H0), so the y-axis jet is a coordinate here too.
- Coupling (section 1). U[h].grad rho_bar = -(rho_bar_y / 2) h + (Beurling-type principal value part). The local
  part damps where rho_bar_y > 0, in particular at the sources (rho_bar_y(P) = g, about 29.75). The C^alpha norm of the
  principal value part is not its symbol supremum. No sharp Hoelder Garding inequality is available, so a Hoelder
  Lyapunov argument like Theorem R cannot be run with the same constants. Near the origin the coupling is small.
  Localized by a smooth cutoff chi_delta, it maps C^alpha_1 into C^alpha_1 with norm O(delta) (Proposition S(d),
  THEOREM, V028). Sharper (S(e), THEOREM, V203 to V207): U_1[h]/x is uniformly C^alpha in y for h in C^alpha_p,
  1 <= p <= 2, without any derivative of h, and the complete normalized localized coupling
  chi_delta (U[h] + c[h] X/3).grad rho_bar maps C^alpha_p into itself with norm O(delta^(3-p-alpha)); on C^alpha_2 its
  norm is in fact comparable to delta^2, which is sharp (V219: the exact strain cancellation made quantitative). Hence the
  frozen transport plus this coupling, and also the operator whose transport is the actual V on B_(delta/2) and the
  frozen saddle outside B_delta, are invertible on the whole-plane class C^alpha_2 for EVERY 0 < alpha < 1 and delta
  small (V206, V207). The first version of this bullet stated a barrier alpha < (1 + A)/D (about 0.5227) for the localized
  coupling and that above it an x-derivative of h must enter the norm; that is REFUTED (V203). Scope: localized
  operators only, qualitative constants and radii depending on the fixed alpha, no disk realization and no global inverse; the cubic coordinate J is not
  closable in the C^alpha_2 graph norm (V208).
- Source (section 3). The verifier-confirmed low-order theorem holds at the actual modal source rate mu < 1 (V029):
  the frozen coupled source inverse maps compact C^alpha input to C^alpha for every 0 < alpha < 1. The coupling is
  essential: without it the pure transport inverse at the source loses Hoelder regularity above 1/A (Remark 3.1).
  On C^alpha_b intersected with L^2 the forcing support restriction is removed, and the actual variable source
  transport and coupling are included on B_{delta/2} for every alpha < 1, unnormalized (3.1(iii), THEOREM, V213 to
  V215).
- Infinity (section 3). In scale-invariant weighted Hoelder norms the window is 2k - 1 <= gamma < k (gamma here is
  the far scaling exponent of 3.2, written beta in 3.4 and in the report, where gamma is the L^2 weight exponent).
- Global (3.4). The common target Y = E_2 intersected with L^2(w_gamma), w_gamma = (1 + |X|^2)^(-gamma/2),
  gamma > 4k, contains the residual F0 and carries the cut-off local inverses at the origin and at the sources (the
  cut-off maps act on Y; the uncut auxiliary inverses need not). For every gamma > 4k, and on E_2 itself, the complete
  coupling is bounded and the full chart operator A_0 is closed on its maximal domain (THEOREM, V222, V224, V228 for
  4k < gamma < 2; V241, audit V247, for E_2 and every gamma > 4k). The specified cutoff parametrix error is bounded
  but not compact (THEOREM, V227; a statement about that patch, not about every sum of patches), and the cubic
  coordinate J is not closable (V224). No bounded inverse on Y exists, and T, L_ren and A_0 are not even onto Y: they
  have infinite algebraic cokernel on E_2 and on every Y with gamma > 4k (THEOREM, V232 and V234, two independent
  far-field mechanisms, 3.4(e); V241 for E_2 and every gamma > 4k): Y is not a valid global target. The
  candidate target Z, local E_2 plus scaled far annular C^alpha norms with growth r^beta plus L^2(w_gamma), contains
  F0 and carries the bounded complete coupling with small tails and the closed full operator for 2k - 1 < beta < k
  (at the endpoint beta = 2k - 1 the full operator does not map the transport graph {h in Z : T h in Z} into Z,
  by a logarithmic m0 term; THEOREM, V235, audit recorded as V244), and the
  actual exterior operator is invertible on it (THEOREM, V236, V242). But Z
  is not a valid global target either (THEOREM, V243, audit recorded as V249; T, L_ren and A_0 have infinite
  algebraic cokernel on it, 3.4(g6)): ordinary far C^alpha
  allows forcings |x|^sigma, alpha < sigma < 1 + alpha, along the outgoing vertical axis, and the characteristics
  carry them to the origin region, where the local E_2 factor requires O(x^2). The target Z_2 with scaled quadratic
  control along every annulus carries the bounded complete coupling, the residual, the closed full operator and an
  actual exterior inverse (THEOREM, V245, audit recorded as V254; 3.4(g)). At a certified simple turning height of
  the axis rate d_x V_1(0, y), y_* in (9.1465, 9.1468), a stationary-phase forcing shows that T is not onto Z_2 for
  alpha > 1/2, and L_ren and A_0 are not onto Z_2 for alpha > 2/3 (THEOREM, V256, verifier proof with an interval
  certificate, independent audit recorded as V262); a stronger divided velocity bound (V257: U_1[x^2 g]/x is jointly
  C^alpha on bounded x-strips for g compactly supported, even in x, bounded and uniformly C^alpha in y; THEOREM, verifier
  proof, independent audit recorded as V265) extends the statement for A_0 and L_ren to every alpha > 1/2 (3.4(g)).
  Surjectivity of A_0 and L_ren for alpha <= 1/2 (transport alone is not onto Z_2 for alpha > 1/A_s, so for every
  alpha >= 1/10: THEOREM, V266, V272), a global inverse on
  Z_2, the patching across the middle annuli, and hence a global C^alpha linear estimate, are OPEN. No global Hoelder inverse is
  claimed.
- Nonlinear term (section 4). Lemma N is a rigorous obstruction (THEOREM in the repaired form of V030). For every
  0 < alpha < 1 and every normed space X that satisfies (H_X) of section 4 (it controls the local C^alpha norms of h
  and U[h] near a regular axis point, and |c[h]|) and in which the explicit sequence h_n of Lemma N stays bounded,
  h -> L^{-1} N(h) maps a bounded subset of X onto an unbounded one. The sequence is explicit: two crossing plane waves of amplitude n^{-alpha} interact exactly into
  -n^{1-2alpha} sin(2ny), and the transport inverse does not regain y-derivatives where V is parallel to e_1.
  Lemma N' (THEOREM, V030, in a stronger form than the sketch) carries the failure over to the C^alpha graph norm:
  inputs with bounded graph norm have ||N||_{C^alpha} >= c n, and so do the solutions. Hence, in every norm in
  which these explicit sequences stay bounded, control beyond C^alpha of h and U[h] (for example C^alpha(h_x)) is
  needed for a perturbative closure of the explicit semilinear map. Lemma N'' (THEOREM, V211, section 4) shows the same in the C^alpha_2 graph of
  the localized origin inverses of 2(e): bounded graph norm, J = c = 0, and ||N||_{C^alpha_2} >= c n. This does not
  show that every stronger C^alpha-type norm must control C^alpha(h_x); the statement is limited to the hypotheses
  of Lemmas N, N' and N'' (V030, V211). A sufficient condition for a quasilinear scheme is a Lipschitz transport
  velocity V + W[h]. Since DU[h] = Riesz^2(d_x h) exactly, this is the condition Riesz^2(d_x h) in L^infinity. It is
  implied by d_x h in C^epsilon (with decay); it is not equivalent to d_x h in C^alpha (verifier counterexample, V025).
  Necessity of a Lipschitz velocity is not claimed (V038 refuted the unrestricted necessity and equivalence wording of
  the closure document). Section 5 gives the compatible high/low formulation and its precise linear
  requirements (OPEN).
- First derivatives across the x-axis (S2_L2_THEORY.md 6.2, Prop F4; THEOREM for the frozen saddle, V067). For the frozen saddle, a smooth
  compactly supported source x^4 chi(x) psi(y) gives the exact solution -C x^4 sgn(y)|y|^{2 - 1/D} near the x-axis.
  This solution is locally C^{1,1-1/D} across the x-axis and is not C^{1,alpha} for any alpha > 1 - 1/D (about
  0.9531) (V067). So, for the frozen saddle, a same-order C^{1,alpha} bound across the stable manifold of the origin
  (the segment [0, x_P) of the x-axis, up to P) on a class containing this forcing is ruled out for alpha > 1 - 1/D,
  and the endpoint alpha = 1 - 1/D is attained by this example. No endpoint inverse and no statement about the actual
  operator follow from this local computation. A C^{1,eps} high norm (eps small) is compatible with it; a uniform
  C^{2,alpha} norm, or an H^s norm with s >= 5/2 - 1/D (the Sobolev endpoint is excluded), is not.

## 1. The complete coupling in Hoelder form

CONVENTIONS S2.1 to S2.2: U[h] = (-R_1 R_2 h, R_1^2 h), R_1^2 = T_xx - I/2, R_1 R_2 = T_xy, with T_xx, T_xy the principal
value convolutions with cos(2 theta)/(2 pi r^2), sin(2 theta)/(2 pi r^2). Hence, exactly,
    T h := U[h].grad rho_bar = -(rho_bar_y / 2) h + [ rho_bar_y T_xx - rho_bar_x T_xy ] h.        (1.1)
The symbol of T_xx is (nu_2^2 - nu_1^2)/2 = -cos(2 phi)/2 and that of T_xy is -sin(2 phi)/2 (nu = (cos phi, sin phi)).
So the principal value part has symbol -(rho_bar_y cos 2phi - rho_bar_x sin 2phi)/2, of mean zero and amplitude
|grad rho_bar|/2. The full symbol ranges over [-(rho_bar_y + |grad rho_bar|)/2, b_+], with
b_+ = (|grad rho_bar| - rho_bar_y)/2 as in S2_L2_THEORY.md. The two Riesz factors are never estimated separately:
(1.1) is a single zero-order operator with an explicit local part.

What this gives in C^alpha. Calderon-Zygmund operators of order 0 are bounded on C^alpha (locally, and globally on
weighted classes with the subtractions of CONVENTIONS S2.3). Their Hoelder operator norms exceed the symbol supremum and
blow up as alpha -> 0 or alpha -> 1, and no Hoelder analogue of the sharp Garding bound (Lemma G2 of
S2_L2_THEORY.md) is known to us. Consequently:
(i) wherever |grad rho_bar| is small (near 0, where |grad rho_bar| = O(r^2), and at infinity, where it is
O(r^{k-1})), T is a small perturbation in C^alpha and local frozen-transport estimates extend; (ii) near the sources,
|grad rho_bar| is about 30 and T is not small; there the coupled frozen operator must be inverted as a whole. This is
done in the verified source theorem of section 3, which uses the exact symbol xi^2/|xi|^2 and its sign. Section 3.3
explains why the global Hoelder patching remains open; that explanation is not a theorem.

## 2. The origin saddle in Hoelder classes

T_0 = -A x d_x + D y d_y - 1, D = 2A + 1, flow Phi_s(x, y) = (x e^{-As}, y e^{Ds}). Every bounded solution of T_0 h = F
on R^2 is h = T_0^{-1} F := -int_0^inf e^{-s} F(Phi_s X) ds. (If T_0 h = 0 then h(Phi_s X) = e^s h(X), so bounded
implies h = 0.) Throughout, F is in class P (even in x, odd in y), so F(x, 0) = 0.

Proposition H0 (weighted sup norms; the L^infinity form of N1; DERIVED). For a, b >= 0 let
||F||_{a,b} := sup |F(x, y)| / (|x|^a |y|^b). If kappa_inf := 1 + aA - bD > 0 then ||T_0^{-1} F||_{a,b} <=
||F||_{a,b} / kappa_inf, and the constant is sharp. x^2 y (cut off) has finite ||.||_{a,b} near 0 iff a <= 2 and
b <= 1. Hence coercivity together with exclusion of x^2 y forces a > 2: exclusion needs a > 2 or b > 1, and b > 1
together with kappa_inf > 0 gives a > (Db - 1)/A > (D - 1)/A = 2. The pair (a, b) = (2, 1) is exactly critical:
1 + 2A - D = 0.
Proof. |F(Phi_s X)| <= ||F||_{a,b} |x|^a |y|^b e^{(-aA + bD)s}; integrate against e^{-s}. Sharpness: the homogeneous
function |x|^a |y|^b sgn(y) is an eigenfunction, with T_0 applied to it giving -kappa_inf times it. QED.
As in the L^2 theory, data must therefore vanish on the outgoing y-axis to order more than 2, and the x^2 coefficient
along the y-axis must be a separate coordinate (Corollary N3 of S2_L2_THEORY.md).

Hoelder classes. For 0 < alpha < 1 and p >= 0 define, for bounded F on R^2,
    [F]_x := sup_{x != x', y} |F(x, y) - F(x', y)| / |x - x'|^alpha,
    [F]_{y,p} := sup_{x, y != y'} |F(x, y) - F(x, y')| / (|x|^p |y - y'|^alpha),
    C^alpha_p := {F in class P : ||F||_{alpha,p} := ||F||_inf + [F]_x + [F]_{y,p} < inf}.
C^alpha_0 is the ordinary bounded uniformly C^alpha class, up to norm equivalence. On {|x| <= R}, C^alpha_p is
contained in C^alpha with [F]_alpha <= [F]_x + R^p [F]_{y,p}. For p > 0, F in C^alpha_p is constant in y on the
y-axis, hence 0 there, by oddness.

Proposition S (frozen saddle in Hoelder classes; DERIVED).
(a) If 0 < alpha < 1/D, then ||T_0^{-1} F||_inf <= ||F||_inf and [T_0^{-1} F]_alpha <= [F]_alpha / (1 - D alpha) on
    C^alpha_0.
(b) Sharpness of (a). Let F be C^1, compactly supported, of class P, and put M_F := int_0^inf u^{-1-1/D} F(0, u) du
    (convergent, because F(0, u) = O(u)). Then for every fixed x, as y -> 0+,
        T_0^{-1} F(x, y) = -(M_F / D) y^{1/D} + o(y^{1/D}),   while T_0^{-1} F(x, 0) = 0.
    For F = y chi(r), with chi >= 0 a nonzero cutoff, M_F > 0. So for alpha > 1/D, T_0^{-1} does not map
    C_c^infinity into C^alpha. Hence no isotropic C^alpha inverse of the frozen saddle exists above 1/D (about 0.0469),
    whatever the norm on the data, unless the data satisfy the outgoing-axis condition M_F = 0.
(c) Anisotropic classes. If 1 + pA - D alpha > 0, then T_0^{-1} is bounded on C^alpha_p:
        ||h||_inf <= ||F||_inf,  [h]_x <= [F]_x / (1 + A alpha),  [h]_{y,p} <= [F]_{y,p} / (1 + pA - D alpha).
    The condition is sharp, including equality (V028). The test function first proposed here,
    F = |x|^p chi(x) psi(y), is not in C^alpha_p when 0 < p < alpha, because its x-Hoelder seminorm is infinite.
    The verifier's replacement is F = |x|^p sgn(y) |y|^alpha chi(x) chi(y/|x|^q), q = max(alpha - p, 0)/alpha, which
    belongs to C^alpha_p. For it the y-Hoelder quotient of T_0^{-1} F grows like int_0^T e^{-(1 + pA - D alpha)t} dt,
    which is unbounded in T when 1 + pA <= D alpha. (For 1 + pA < D alpha the original computation, valid when
    p >= alpha, shows T_0^{-1} F(x, y) ~ -C |x|^p y^{(1+pA)/D} for fixed small x != 0.)
    Thresholds: p = 0 gives alpha < 1/D (about 0.047); p = 1 gives alpha < (1 + A)/D (about 0.5227); p = 2 gives alpha < 1,
    because (1 + 2A)/D = 1. At p = 2 the threshold exponent is exactly 1 because x^2 y is the resonance. The
    forcing x^2 y chi(r) produces -(1/D) x^2 y log(1/|y|) to leading order, the log solution of the jet row in Theorem O.
(d) Coupling near the origin (THEOREM in the form below, V028; the first version used the indicator 1_{B_delta},
    which is REFUTED: multiplication by the indicator creates a jump, and U[h].grad rho = -c[h] x^2 y + o(r^3) is
    nonzero at interior-quadrant points of every small circle). Let rho_bar be C^4 near 0, even in x, odd in y, with
    rho_bar = x^2 y + O(r^4) and rho_bar(0, y) = 0. (The first version assumed C^5. The actual modal trial is C^{4,1}
    but not C^5 at 0: its degree-5 inner term has a nonzero sin(521 theta) coefficient. The verifier's proof needs only
    C^4, so the statement applies to the trial; V036.) (Parity is needed: rho = x^2 y + x y^3 meets the other
    hypotheses but has rho_x(0, y) = y^3.) Then d_x rho_bar = x a_1 and d_y rho_bar = x^2 a_2 with
    ||a_1||_inf <= C delta, ||D a_1||_inf, ||a_2||_inf, ||D a_2||_inf <= C on B_delta. Let chi_delta be smooth,
    supported in B_delta, equal to 1 on B_{delta/2}, with |D chi_delta| <= C/delta. If U is in C^alpha(B_delta) with
    U(0) = 0, then F := chi_delta U.grad rho_bar (extended by 0) satisfies
        ||F||_inf <= C delta^{2+alpha} ||U||_{C^alpha(B_delta)},  [F]_x <= C delta^2 ||U||_{C^alpha(B_delta)},
        [F]_{y,1} <= C delta ||U||_{C^alpha(B_delta)}.
    On E = C^alpha_1, with the parity-normalized velocity (far kernel subtracted at X = 0),
    ||U[h]||_{C^alpha(B_1)} <= C_alpha ||h||_E. Hence B_delta h := chi_delta U[h].grad rho_bar is bounded E -> E with
    norm C_alpha delta, and for alpha < (1 + A)/D the operator T_0 + B_delta : D(T_0) -> E is bijective for
    C_alpha delta max(1, 1/kappa_1) < 1, where kappa_1 = 1 + A - D alpha (Neumann series with (c) at p = 1).
    This is frozen transport with a globally defined, localized coupling. It does not include the strain column
    (c[h]/3) G_bar, does not replace T_0 by the actual V, and gives no boundary realization on B_delta. The first
    version added that the coupling does not map into C^alpha_p for p > 1 at the same alpha unless d_x U_1[h] is
    bounded, and that above 0.5227 an x-derivative of h must enter the norm. Both statements are REFUTED (V203); see
    (e), which supersedes the restriction alpha < 0.5227.
(e) Sharper coupling, strain column and actual transport near 0 (THEOREM, V203 to V207; independent cross-audits
    of V203 to V208 found no gap). Let E_p = C^alpha_p with the norm ||h||_inf + [h]_x + [h]_{y,p} of
    (c) (so h(0, y) = 0), 0 < alpha < 1, and let rho_bar be as in (d).
    - Directional velocity bound (V203). For 1 <= p <= 2,
          sup_{|x|<=1} ||U_1[h](x, .)/x||_{C^alpha([-1,1])} + sup_{|x|<=1} ||U_2[h](x, .)||_{C^alpha([-1,1])}
              <= C ||h||_{E_p}.
      Proof idea: Fourier transform in y only. U_1 = -i eta d_x (-d_x^2 + eta^2)^{-1} has the x-kernel
      i eta sgn(z) e^{-|eta||z|}/2. On a y-frequency band of size lambda the input is at most M |x|^p lambda^{-alpha},
      M = ||h||_{E_p}, and the bands of U_1 and d_x U_1 are at most C M lambda^{-alpha}(|x|^p + lambda^{-p}) and
      C M lambda^{1-alpha}(|x|^p + lambda^{-p}). For lambda |x| <= 1 integrate d_x U_1 from x = 0 (U_1 is odd in x),
      otherwise divide by x directly; either way the band of U_1/x is at most C M lambda^{-alpha}, which sums to a
      C^alpha_y bound. The low-frequency block is treated with the exact kernel. With rho_x = x a_1 and
      rho_y = x^2 a_2, B_delta h = x^2 chi_delta (a_1 U_1/x + a_2 U_2), and therefore
          ||B_delta h||_{E_p} <= C delta^{2-p} ||h||_{E_p},   1 <= p < 2.
    - Strain column (V204, V205). |c[h]| <= (4/pi) max(1, 1/(p + alpha - 1)) ||h||_{E_p} (with the angular factor
      of section 6, V201), and ||chi_delta X.grad rho_bar / 3||_{E_p} <= C delta^{3-p-alpha}. For every h in E_p,
      1 <= p <= 2, U(X) = c[h](-x, y) + O(r^{min(p+alpha, 2)}(1 + |log r|)) at 0, so the strain identity
      DU[h](0) = c[h] diag(-1, 1) and the cubic cancellation of the normalized coupling hold in E_p (V205).
    - Quadratic endpoint (V207). On |x| <= delta, |y| <= 2 delta, |U_2[h]| <= C M delta and its y-seminorm is at most
      C M delta^{1-alpha}. Hence the complete normalized localized coupling
      B_norm h = chi_delta (U[h] + c[h] X/3).grad rho_bar satisfies ||B_norm h||_{E_p} <= C delta^{3-p-alpha} ||h||_{E_p}
      for 1 <= p <= 2, in particular O(delta^{1-alpha}) on E_2 (for p = 2 the strain bound is 4/pi).
    - Sharp normalized rate (V219). On E_2, for the actual C^{4,1} background and fixed alpha < 1,
          c_0 delta^2 <= ||B_norm||_{E_2 -> E_2} <= C delta^2   (delta small),
      where B_norm = chi_delta (U[h] + c[h] X/3).grad rho~ is the complete normalized localized coupling. The rate
      delta^{1-alpha} above is an upper bound; it is the exact order of the coupling without the normalization term
      (DERIVED: the two differ by c[h] chi_delta X.grad rho_bar/3, whose E_2 norm is of exact order delta^{1-alpha}). Proof idea: subtract from each y-frequency
      band its own strain (these are absolutely summable to c[h]); then, with M the E_2 norm of h, U_2 - c y has local
      y-C^alpha size C M delta^2 and supremum C M delta^{2+alpha}, and U_1/x + c has size C M delta and supremum
      C M delta^{1+alpha}; the low band uses only the third potential derivatives d_x^2 d_y Q and d_y^3 Q, the high bands the exact
      kernels and dyadic reconstruction; the divided C^{4,1} remainders of the background make the leading
      cancellation exact. Lower bound: compact potentials with c = J = 0 and eps^alpha <= delta^{2+alpha}
      (x-wavelength much shorter than y-wavelength) give an x-seminorm of order delta^2. Consequence: the Neumann
      error is O(delta^2) for the frozen transport and, by V226, also for the actual one. Constants qualitative.
    - Inverses. kappa_2 = 1 + 2A - D alpha = D(1 - alpha) > 0 for every alpha < 1, so (c) at p = 2 and the
      factorization T_0 + B_norm = (I + B_norm T_0^{-1}) T_0 give a bounded inverse of T_0 + B_norm from D(T_0) onto
      E_2 for delta small, for every 0 < alpha < 1 (V204, V207; V203 gives the coupling without the strain column on
      E_p, p < 2, with 1 + pA > D alpha). Actual transport (V206, V207): write V = (-x A(x, y), y D(x, y)) near 0,
      A(0) = A0, D(0) = D0 = 2 A0 + 1 (for the trial A0 = 2 ell - 1 and D0 = 4 ell - 1), put
      A_delta = A0 + chi(X/delta)(A - A0), D_delta likewise, V_delta = (-x A_delta, y D_delta). Then
      L_delta = V_delta.grad - 1 + B_norm is invertible on its maximal domain in E_2, with inverse bounded uniformly
      as delta -> 0. Proof idea: divide by A_delta, so that the flow has x_t = e^{-t} x exactly; y-differences decay
      along the flow with the exponent q0 + p - alpha L, L = sup d_y(beta y) for the y-speed beta = D_delta/A_delta, and
      the x-difference produced by the variable y-speed is weighted by a delayed entry time
      t_0 = log^+(|x|/(2 delta)) into B_delta, which turns x^p exp(-(q0 + p + alpha) t_0) into at most (2 delta)^p;
      the variation of 1/A_delta is a multiplier of size O(delta^2) on E_2 (V226: it has supremum O(delta^2) and
      gradient O(delta), and the product difference is split at the supported endpoint; on the y-part the weighted
      bound |h| <= M |x|^p |y|^alpha, which uses oddness in y, is needed, on the x-part h(0, y) = 0 suffices; the
      first version had O(delta^{2-alpha})). The actual modal trial meets the
      hypotheses (V of class C^3 and rho_bar of class C^4 near 0).
    - Scope. The operators of (e) agree with the actual linearization only on B_{delta/2}; outside B_delta they are
      the frozen saddle. There is no boundary realization on a disk, no global inverse of L, and no numerical value
      of C or of the admissible delta (both are qualitative and depend on the fixed alpha). The cubic coordinate is not closed in this graph norm: there are smooth compact
      k_eps with J(k_eps) = 1, c[k_eps] = 0 and ||k_eps||_{E_2} + ||L_delta k_eps||_{E_2} = O(eps^{1-alpha}) (V208),
      so J, defined on smooth compactly supported functions in E_2, is unbounded in the graph norm even on ker c,
      hence not closable. In relative-domain form (V216): with S the smooth compactly supported functions in E_2 of
      both parities, ker J intersected with ker c intersected with S is graph-dense in S intersected with ker c, so the
      two have the same graph closure and J = 0 adds no closed constraint on that core. This is not density in the
      whole graph (c is continuous and nonzero there), and smooth functions are not dense in the full graph of this
      large Hoelder norm. Only boundedness of the coupling is used, not the smallness of V207.
      The explicit h = -Delta P, P compact and locally |x + y - const|^{2+alpha} away from the axes, has unbounded
      d_x U_1 while h and B_delta h lie in every E_p (V203); it shows that a bounded d_x U_1 is not necessary. The
      substantive refutation of the 0.5227 barrier is the bound for B_delta.

Proof. (a) |Phi_s X - Phi_s X'| <= e^{Ds} |X - X'|, so |h(X) - h(X')| <= [F]_alpha |X - X'|^alpha int e^{(D alpha - 1)s} ds.
(b) Substitute u = y e^{Ds}, so ds = du/(D u) and e^{-s} = (y/u)^{1/D}:
    T_0^{-1} F(x, y) = -(1/D) y^{1/D} int_y^inf u^{-1-1/D} F(x (y/u)^{A/D}, u) du.
The integrand converges pointwise to u^{-1-1/D} F(0, u) as y -> 0. It is dominated by ||d_y F||_inf u^{-1/D} for u <= 1
(F(x', 0) = 0) and by ||F||_inf u^{-1-1/D} for u >= 1, which is integrable. Dominated convergence gives the claim.
F(x, 0) = 0 gives the value on the axis.
(c) The x-difference: F(x e^{-As}, Y) - F(x' e^{-As}, Y) <= [F]_x e^{-A alpha s} |x - x'|^alpha. The y-difference:
|F(x e^{-As}, y e^{Ds}) - F(x e^{-As}, y' e^{Ds})| <= [F]_{y,p} |x|^p e^{-pAs} e^{D alpha s} |y - y'|^alpha. Integrate
against e^{-s}. Sharpness: the same substitution as in (b) with exponent (1 + pA)/D in place of 1/D. The x-factor
|x (y/u)^{A/D}|^p chi(...) produces |x|^p y^{pA/D} u^{-pA/D}, and dominated convergence applies when (1 + pA)/D < 1.
For F = x^2 y chi(r): e^{-s} e^{-2As} e^{Ds} = 1, so exactly T_0^{-1} F = -x^2 y int_0^inf chi(|Phi_s X|) ds. For chi
equal to 1 near 0 and compactly supported this integral is (1/D) log(1/|y|) + O(1) (it is the measure of
{s : |Phi_s X| in supp chi} only when chi is an indicator).
(d) Write F = x H_1 + x^2 H_2 with H_j = chi_delta a_j U_j. The cutoff gives [chi_delta a_1]_alpha <= C delta^{1-alpha}
and [chi_delta a_2]_alpha <= C delta^{-alpha}, and ||U||_inf <= delta^alpha [U]_alpha on B_delta since U(0) = 0. Hence
[H_1]_alpha <= C delta ||U||_{C^alpha} and [H_2]_alpha <= C ||U||_{C^alpha}, which gives the y-estimate at fixed x
(the factors x and x^2 are at most |x| delta^0 and |x| delta). The x-estimate follows from the product rule with
||chi_delta grad rho_bar||_inf <= C delta^2 and [chi_delta grad rho_bar]_alpha <= C delta^{2-alpha}. The bound on U[h]
splits h by a fixed radial cutoff and uses the standard Hoelder estimate of the kernel near and the Lipschitz
difference kernel far. The complete proof is the verifier's (V028). QED.

Remark 2.1 (actual transport; the transfer argument is REFUTED, V028). Near 0 the actual field is V = A_c X + O(r^3)
and is C^2, and a local C^1 linearizing conjugacy H exists. The first version claimed that (a), (c), (d) transfer to
the actual transport because H preserves the axes. That step is false for the anisotropic classes. For p > alpha the
verifier gives f in C^alpha_p and the smooth, parity-preserving, axis-preserving map H(x, y) = (x(1 + epsilon y^2), y),
with H(X) - X = O(r^3), such that f composed with H is not locally in C^alpha_p. The construction uses bumps in x of
height r_n^p and width r_n^{p/alpha}, times a fixed odd function of y. The reason is that the y-Hoelder quotient
weighted by |x|^p is not invariant under maps that shift x by an amount depending on y. Whether the actual flow admits
a conjugacy with the extra mapping properties that would be needed is OPEN. The localized actual-transport inverse
of (e) (V206, V207, V226) does not use a conjugacy; it is established on the whole-plane class C^alpha_2 for the
operator equal to the actual transport on B_{delta/2} and to the frozen saddle outside B_delta. What remains OPEN
near 0 is a realization on a disk or other bounded domain with boundary conditions, and the patching of the
localized inverse into a global one.

Remark 2.2 (relation with Theorem O). The L^2 theory needs the factor |x|^{-2a} with a >= 5/2, an L^2 vanishing order of at least
2 on the y-axis (the endpoint a = 5/2 is admissible, V025). The sup theory needs a > 2 (Proposition H0). The
Hoelder seminorm theory needs only p > (D alpha - 1)/A in the y-Hoelder weight, which is below 2 for every alpha < 1,
but it does not see the x^2 y jet: J is not continuous on C^alpha_p.
Within the weighted-sup construction of Proposition H0 (coercivity of T_0^{-1} in ||.||_{a,b} together with exclusion
of x^2 y) the weight must have a > 2, and a normalized C^alpha space built that way combines such a weighted sup part
(giving J as a coordinate) with the seminorms of (c). This is a necessity statement within that construction only,
not a classification of all norms carrying a continuous cubic trace. The naive graph repairs fail at their own scope:
J is not closable in the E_2 graph of (e) (V208) or on the Y and Z graphs of 3.4, and completing smooth zero-strain
inputs in the A_0 graph norm on Z plus |J| gives only the abstract completion G_sm (+) R, whose function projection
has a nonzero pure scalar kernel invisible to A_0 (THEOREM, V240, audit recorded as V246; G_sm is the smooth graph
closure only, not the entire maximal domain). Stronger genuine trace norms, for example an added cubic weighted sup
condition near 0 (section 6), are not excluded.

## 3. Source points, infinity and the global question

3.1 Source (THEOREM, verifier-confirmed V013 for mu = 1 and V029 for the actual rate; statements as verified).
(i) V013 (mu = 1). Let A > 1, g > 0, 1 < a := g/(A - 1) < A + 1, and L_P = A s d_s + y d_y - 1 - g M (s = x - x_P)
with Mhat = xi^2/|xi|^2, and let R be its L^2-selected inverse. Then R maps compactly supported C^alpha input into
C^alpha for every 0 < alpha < 1, with a finite constant. For 1 < sigma < a the sharp output order is
r(sigma) = sigma - (sigma - 1)/A, and the same-order estimate fails; for sigma > a the ceiling is q = (1 + g)/A,
attained by a fixed smooth forcing.
(ii) V029 (actual rate). The actual modal source has mu strictly below 1 (V017), so (i) does not apply literally. For
L = A x d_x + mu y d_y - 1 - g M on its maximal L^2 transport domain, with A > mu > 0, a := g/(A - mu) and
1 < a mu < A + 1, the selected inverse is bounded on compactly supported C_*^sigma input into C_*^sigma for every
0 < sigma < 1/mu. Above, the output order is ((A - mu)/A) sigma + 1/A, up to ceiling(1 + g)/A, with logarithmic
endpoint bounds. V017's parameter box for the modal source satisfies 3 < a mu < 10/3 < A + 1 and mu < 1.
Both constants are finite existence constants, not numerical bounds. The low-order statement (ii) is the answer to
Avenue II at the source: a same-order C^alpha inverse exists for all 0 < alpha < 1 at the actual modal source. The
higher-order loss does not decide the low-order problem. General-mu sharpness, the
rank-one correction and global inversion are OPEN; the localized variable-coefficient (unnormalized) source problem
is solved in (iii).
(iii) V213 to V215 (the actual source operator, unnormalized). Let X_alpha = C^alpha_b intersected with L^2, with
||f|| = ||f||_{C^alpha_b} + ||f||_{L^2}, and the maximal transport domains.
    - V213. For A > mu > 0, g > 0 and a mu > 1, the frozen coupled source inverse of (ii) is bounded on X_alpha for
      0 < alpha < min(1, 1/mu), with no restriction on the support of the forcing; the exact L^2 bound
      1/[1 + (A + mu)/2] holds. Proof idea: only the first annular branch of the L^2 semigroup is used; high dyadic
      blocks are bounded by N^{-alpha} ||f||_{C^alpha}, low blocks by the two-dimensional Bernstein bound N ||f||_2,
      and the time integration gives lambda^{-1/mu} times sums of N^{1/mu - alpha} (high) and N^{1 + 1/mu} (low).
      The Riesz multipliers are bounded on X_alpha (the L^2 part controls the low frequencies), so localized actual
      velocity coefficients perturb the inverse by O(delta^{1-alpha}) with the frozen transport kept. The upper
      condition a mu < A + 1 is not needed here.
    - V214. The actual source flow is smoothly conjugate near P to diag(A, mu): with 10 < A < 10.2 and mu just below
      1, A/mu lies in (10, 11), so no resonance of positive degree occurs; the Taylor degrees 2 to 11 are removed by
      their homological denominators (150 exact intervals, minimum lower end 0.150725 > 3/20), and the O(r^12)
      remainder by the limit H(Z) = lim e^{Bt} Phi_{-t}(Z), which converges with all derivatives since
      12 x 0.99 = 11.88 > A (the backward flow contracts in every direction). The load-bearing spectral fact is the
      strict inequality 10 mu < A: the degree-10 denominator 10 mu - A, about -0.1507, is the smallest of the 150,
      and degree 11 is margin. The source lies inside one spline span; the check certifies a disk of radius 1/1000
      inside that span, on which the trial is analytic by construction (finitely many angular modes times
      log-polynomials). A radial cutoff extends the conjugacy to a global diffeomorphism id + O(delta^2) with
      D - id = O(delta), bounded on X_alpha, with exact transfer of the maximal transport domain.
    - V215. With C h = h o Phi^{-1}, A = DPhi o Phi^{-1}, j = det A^{-1}, G = j A A^T, a_k = A e_k and
      P = grad Delta^{-1} div, the conjugated component P_(ik) is h -> a_i . w with w = P[j a_k h - (G - I) w]
      (the pulled-back weak Poisson equation, identified by the L^2 energy identity). Since ||G - I||_{C^alpha} and
      ||j a_k - e_k||_{C^alpha} are O(delta^{1-alpha}), this exact identity with an a priori X_alpha bound (a Neumann
      series gives the same) yields
      ||C P_(ik) C^{-1} - P_(ik)||_{X_alpha -> X_alpha} = O(delta^{1-alpha}). Combined with V213 and V214 this gives a
      whole-plane inverse on X_alpha, for every alpha < 1, of an explicit extension equal to the actual variable
      unnormalized source operator on B_{delta/2}. The forcing may be noncompact, which the commutator step needs.
      For each fixed alpha < 1 the admissible delta depends on alpha; nothing is uniform as alpha -> 1.
    - Scope. The full strain functional is not bounded in the X_alpha norm (on its natural domain): smooth bounded
      packets have c[h_eps] = eps^{alpha-1} c[H] (V213). Whether c is bounded relative to the graph norm of the source
      operator is not decided. A prescribed scalar times the localized strain column is admissible forcing, but closing
      b = c[h], the normalization and the global patching are OPEN. Constants and radius are qualitative. The velocity
      in V213 and V215 is the L^2 Fourier multiplier velocity; it differs from the canonical velocity by a constant
      vector that vanishes on the parity class (h even in x, odd in y), so the identification with the actual
      operator holds there.

Remark 3.1 (the coupling is what saves the source; DERIVED). For the pure transport A s d_s + y d_y - 1 (g = 0), the
bounded inverse integrates along trajectories leaving P. For F = y chi(X) with chi = 1 near P, the solution is
h = -(y/A) log(1/|s|) + O(|y|) on the region |y|^A << |s| << 1. Its x-Hoelder quotient on dyadic scales
|s| ~ |y|^A is about |y|^{1 - A alpha}, so the C^alpha norm is infinite for alpha > 1/A (about 0.0985). With g > A - 1 the
nonlocal term -g M removes this loss (verified theorem). The source is the place where the coupling must be kept
exactly.

3.2 Infinity (DERIVED). V = c_l X + O(r^k), and the frozen far operator is c_l X.grad - 1. In the scale-invariant
weighted Hoelder norm ||h||_{gamma, alpha} := sup_R R^{-gamma} ( ||h||_{L^inf(A_R)} + R^alpha [h]_{alpha, A_R} ),
A_R = {R <= r <= 2R}, the forward inverse -int_0^inf e^{-s} F(e^{c_l s} X) ds is bounded iff gamma c_l < 1, i.e.
gamma < k. The homogeneous outflow tails r^k Theta(theta) are excluded exactly when gamma < k, and the trial residual
r^{2k-1} Eps(theta) belongs to the target if gamma >= 2k - 1 (and only if, because Eps is not identically zero;
V025 notes that this necessity needs a nonzero leading coefficient). Window: 2k - 1 <= gamma < k, the L^infinity analogue
of Proposition N4 (L^2 weight r^{-2 gamma'} with gamma' = gamma + 1). The strain column (c[h]/3) G_bar ~ (k/3) c[h] r^k
Theta_0 is not in this target. As in Avenue I, the rank-one term must be bordered by the log-tail direction (KP, or the
parametric family rho_ell of Remark N5 of S2_L2_THEORY.md).

3.3 Global patching (OPEN). The transport inverse integrates along whole forward trajectories, which leave every
local neighbourhood. A local Hoelder bound therefore patches only if the Hoelder quotient is propagated along the
trajectory with a net decay. For pure transport the rate is -1 + alpha lambda(X), where lambda is the local expansion
rate transverse to the trajectory. It is negative near 0 in the class C^alpha_p (Proposition S(c)) and at infinity in
scaled norms, but positive near the sources. There only the coupled frozen theorem (3.1) helps, and that theorem is
not a perturbative Hoelder bound with an explicit constant. Two routes remain. (i) A Hoelder Lyapunov argument with
an explicit Hoelder bound on the principal value part of (1.1); expected to fail near P by a large factor, see
section 1. (ii) Deduce C^alpha bounds from the weighted Sobolev theory: in two dimensions H^{1 + alpha + eps}_loc is
contained in C^alpha, and section 6 of S2_L2_THEORY.md gives nonempty H^s windows for s up to 2.45 near the corner and
3.49 at P. Route (ii) is the one recommended: it controls h in C^alpha (and in C^{1,alpha} for s > 2 + alpha, V028) without a
separate Hoelder theory of the coupled operator.

3.4 The common weighted target and the global closed realization (THEOREM, V222, V224, V227, V228, V232, V234,
V241; in (g), (g1) to (g4) and (g6) are THEOREMS, V235, V236, V242, V243, V244, V249, the patch statement V239 is a
THEOREM (V246), (g5) is DERIVED, the Z_2 statements are THEOREMS (V245, V254), and the turning-height
non-surjectivity on Z_2 is a THEOREM (V256, V262)). Fix 0 < alpha < 1 and gamma > 4k. Let E_2 be C^alpha_2 with the parity class (even
in x, odd in y) and h(0, y) = 0, and put Y = E_2 intersected with L^2(w_gamma), w_gamma = (1 + |X|^2)^(-gamma/2), with

    ||h||_Y = ||h||_inf + [h]_x + [h]_(y,2) + ||h||_{L^2(w_gamma)},
    [h]_(y,2) = sup |h(x, y) - h(x, y')| / (x^2 |y - y'|^alpha).

The weight x^2 of the vertical seminorm is global. Let V = ell0 X + U[rho0], T = V.grad - 1, and let D_Y be the
maximal domain {h in Y : V.grad h in Y in the sense of distributions}.
(a) (V222) Y is a Banach space and |c[h]| <= (4/pi) ||h||_Y. The actual residual F0 lies in Y; it lies in
    L^2(w_gamma) if and only if gamma > 4k, and not in unweighted L^2. The cut-off origin inverse chi_o R_o eta_o and
    the paired reflected source construction chi_+ R_+ eta_+ are bounded Y -> Y (in fact E_2 -> Y). This does not
    assert that the uncut auxiliary inverses act on Y. For identities with the actual operator, the cutoffs must lie
    where the extension equals the actual operator (the independent audit, V231).
(b) (V224, V241) For every gamma > 4k, and on E_2 itself, the renormalized coupling C_ren h = U[h].grad rho0 + c[h]
    H0, with the compact cut-off strain column H0, is bounded, and ||beta_R C_ren||_(Y -> Y) <= C R^(k-1)(1 + log R),
    beta_R = 1 - chi(X/R) (V224 for 4k < gamma < 2; V241, audit V247, for E_2 and every gamma > 4k, with the bound C
    R^max(k-1, k-gamma/2)(1 + log R), which reduces to this for gamma >= 2 and on E_2). This rate is sharp: R^(k-1)
    log R from below as well, on E_2 and on every Y_gamma, also on the strain-zero inputs ker c, where C0 = C_ren
    (THEOREM, V278 with sign clarification V281, verifier proof, independent audit recorded as V287). The
    global velocity bounds are E_2 bounds: U_1[h]/x is uniformly bounded with y-Hoelder norm O(1 + |x|), U_2[h] has
    y-Hoelder norm O(1 + x^2), and U[h] is uniformly x-Hoelder. The weighted L^2(w_gamma) velocity bound used in V224
    needs gamma < 2 and is not extended; V241 uses the decay of grad rho0 instead. The operator L_ren = T + C_ren is
    closed on D_Y (and on its maximal domain in E_2). The cubic coordinate J is not closable on this graph. (The raw
    strain column X.grad rho0 grows like r^k and is not in Y for any gamma, which is why the cut-off column is used.)
    Both exponents of E_2 are sharp for this realization (THEOREM, V229, V230, V238). The vertical power 2 cannot be
    raised: for every p > 2 there is a smooth compact input with c = J = 0 whose transport image lies in E_p but whose
    coupling image does not (on the vertical axis the image divided by x^2 is -5 b y^3 + O(y^5), b a nonzero third
    velocity moment), so the maximal transport domain is not contained in the maximal domain of the full expression.
    The Lipschitz endpoint alpha = 1 is excluded: at a source there are inputs with c = J = 0, bounded in the
    Lipschitz transport graph, whose coupling norm is at least c1 log(1/epsilon) - C (the coupling has a -g y log r
    singularity, g = d_y rho0(P) > 29), although there |J(h)| <= [h]_(y,2,Lip), so the cubic coordinate would become
    continuous. Neither statement concerns every stronger Hoelder norm or a full inverse on a different domain.
(c) (V228) The moving-tail column m0 lies in Y: at the origin m0 = (U[zeta] + c[zeta] X/3).grad rho0 / n'_0 has a
    cofactor O(r^3), and at infinity the r^k terms cancel exactly and leave r^(2k-1)(1 + log r). Hence the full chart
    linearization A_0 = T + U[.].grad rho0 + c[.] M0 = L_ren + c[.] m0 is closed on D_Y, with coupling tail
    O(R^(2k - gamma/2)(1 + log R)) for 4k < gamma < 2 (V228) and O(R^max(2k-1, 2k-gamma/2)(1 + log R)) on E_2 and for
    every gamma > 4k (V241, audit V247; the E_2 tail R^(2k-1)(1 + log R) of M0 is retained), and the nonclosability of J and the noncompactness in (d) hold on its whole graph.
    H0 and M0 belong to Y. The actual-variable origin extension that contains the exact column chi(X/delta) m0
    differs from the normalized extension of 2(e) by O(delta^(3-alpha)), so with V226 the total factorization error
    stays O(delta^2).
(d) (V227) The cutoff commutator [L_ren, chi] and the parametrix error L_ren K - chi eta, K = chi R_o eta, are
    bounded but not compact on the maximal graph: there are bounded sequences of smooth compactly supported inputs
    with c = J = 0 (flow-box packets with transverse oscillation) whose images have no convergent subsequence. The
    reason is that the embedding of D_Y into Y is itself not compact; [C_ren, chi] alone is compact on inputs supported
    in a fixed compact set away from the vertical axis. So this specified patch error (and commutator) is not a
    compact perturbation; this does not exclude cancellations in a sum of patches or a different parametrix. That T, L_ren
    and A_0 have no bounded inverse on Y, and are not even onto Y, is proved separately in (e), by other arguments
    (V232, V234, V241).
(e) No bounded inverse on Y; the common target Y is not a valid global target (THEOREM, V232 and V234; both
    independently cross-audited, PASS WITH REMARKS, no gap; extended to E_2 and every gamma > 4k by V241, V247).
    - (V234: the theory author's argument, independently verified, with the orbit constant delta_1 = 4 C R_1^(k-1)/(ell0 (1 - k))).
      Let B be a bounded linear operator on Y with ||beta_R B||_(Y -> Y) -> 0 as R -> infinity (no rate is needed).
      Then T + B is not surjective from D_Y (or from any smaller domain) onto Y; in particular it has no bounded
      inverse. Surjectivity alone would give bounded solution choices by the open mapping theorem on the closed maximal
      graph, so no injectivity and no linear right inverse is assumed. By (b) and (c) this applies to L_ren and A_0,
      for every 0 < alpha < 1 and 4k < gamma < 2 (the range stated in V234; on E_2 and for every gamma > 4k
      non-surjectivity follows in any case from the infinite cokernel of V241 below). Mechanism: the far flow is the dilation X -> e^(ell0 tau) X up to
      factors e^(+-delta_1); along it x^2 |Delta y|^alpha grows like e^((2 + alpha) ell0 tau), and (2 + alpha) ell0 > 1.
      The forcing f = phi(|x|/X0) theta(X0 y) sigma(|x|^(2/alpha) y), concentrated near the x-axis at radius X0, has
      Y norm bounded uniformly in X0, because the global weight x^2 allows a jump of order one across
      |y| ~ X0^(-2/alpha). The forward representation u = -int_0^inf e^(-tau) (f - B u)(Phi_tau X) d tau gives, at a
      fixed radius R_1, [u]_(y,2) >= c X0^(2 + alpha - k), while the contribution of B u is small (split at
      R = X0^(1/2)).
    - (V232, a different mechanism). Smooth forcings x^2 phi(x) y^(-b), 1/2 < b < 1, on a strip along the vertical
      axis at large height lie in D_Y and have vanishing local jet (c = J = 0). Their forward characteristic integrals
      are of size x^(k+b) at a fixed height, while every element of Y is O(x^2) there, and the complete coupling,
      including the m0 column, contributes only O(x^2 log(1/x)). The coupling estimate uses both bounds
      |U[h].grad rho0| <= C ||h||_Y x^2 r^(k-2) and <= C ||h||_Y r^(k-1) log r, the exact identity ell0 k = 1 and the
      integrated far drift. Hence T, L_ren and A_0 have algebraic cokernel of continuum dimension on D_Y (distinct b
      give independent cosets), so none of them is onto Y or Fredholm there. The independent audit notes that the
      argument extends to b in (max(0, (1 - gamma)/2), 2 - k) and to every 0 < alpha < 1. V241 (THEOREM, audit
      V247) extends the conclusion to E_2 itself and to every gamma > 4k: with the coupling and closedness of (b),
      (c) on those spaces, the strip forcings lie in each transport domain, and T, L_ren and A_0 have infinite
      algebraic cokernel on E_2 and on every Y with gamma > 4k.
    Neither argument says anything about whether F0 lies in the range or whether the range is closed, about other
    targets, about the high/low
    Sobolev condition (I) of Theorem E, or about existence of a profile. The two mechanisms are dual: one uses the
    weak x^2 weight near the horizontal axis at infinity, the other the slow decay that Y allows along the vertical
    axis at infinity. Neither applies in dilation-scaled far norms.
(f) Consequence. Y is a correct common realization space for every gamma > 4k (it contains the residual, carries
    the cut-off local inverses and the bounded complete coupling, and the full operator is closed on it), but it is not a valid global target
    (THEOREM, (e)). A global target must replace the global x^2-weighted vertical seminorm at infinity by scaled far
    seminorms; (g) gives the candidate. No universal necessity of one particular replacement norm is claimed.
(g) The scaled far target Z (verifier proofs V235, V236, V243, V245, V256). (g1) to (g3) are THEOREMS (V235; independent
    audit recorded as V244) and (g4) is a THEOREM (V236; audit recorded as V242). The sharpening at the end of (g3)
    and the comparison (g5) come from the independent audit of V235 and are DERIVED. (g6) is a THEOREM (V243;
    independent audit recorded as V249). Let p = 2k - 1 and fix 0 < alpha < 1, p <= beta < k, gamma > 4k, a smooth radial cutoff chi equal
    to 1 on B_2 and 0 outside B_4, and the overlapping annuli A_j = {2^j <= |X| <= 2^(j+2)}, j >= 0. Z consists of the
    continuous functions with the parities of the problem and h(0, y) = 0 for which

        ||h||_Z = ||chi h||_(E_2) + sup_j 2^(-j beta) (||h||_(L^inf(A_j)) + 2^(j alpha) [h]_(C^alpha(A_j)))
                  + ||h||_(L^2(w_gamma))

    is finite; [.]_(C^alpha(A_j)) is the ordinary Euclidean seminorm. The x^2-weighted vertical seminorm of Y is
    imposed only near the origin.
    (g1) (V235) Z is a Banach space, |c[h]| <= C ||h||_Z and |h(X)| <= C ||h||_Z (1 + r)^beta. The canonical velocity is
         defined on Z and is O(R^beta) at radius R with the matching scaled Hoelder bound (for -2 < beta < 1). C_ren is
         bounded on Z, with ||beta_R U[.].grad rho0||_(Z -> Z) <= C (R^(k-1) + R^(beta + k - gamma/2)); the local E_2
         part uses the cutoff commutator [chi, U] h, which is bounded in C^(1,alpha), so no global E_2 assumption enters.
         F0 lies in Z (its leading far term r^p S_F(theta) is nonzero, so beta >= p is necessary, and gamma > 4k).
    (g2) (V235) For beta > p the full moving-tail column M0 lies in Z, with
         ||beta_R M0||_Z <= C (R^(p - beta) + R^(2k - gamma/2))(1 + log R). Hence A_0 = T + C0,
         C0 = C_ren + c[.](M0 - H0), is closed on the maximal domain D_Z = {h in Z : V.grad h in Z}, C0 has small
         output tails, and the cubic coordinate J is still not closable on the actual graph.
    (g3) (V235) The endpoint beta = p is excluded for the full operator: M0 = r^p log r S_M(theta) + O(r^p) with
         S_M = -2k^2 Q_k / n'_0, whose sin(1043 theta) coefficient k^2 (521 - k) a_521^2 / (2 n'_0 (523 + k)) is
         positive by exact signs. A compact smooth q with c[q] = 1, J(q) = 0 and q, T q in Z then has A_0 q outside Z.
         So at beta = p the full expression does not map the chosen transport graph {h in Z : T h in Z} into Z, and
         on that domain the window for the full operator is p < beta < k, open at both ends; the upper end excludes
         the homogeneous outflow tails r^k Theta(theta). This concerns that domain, not every conceivable closed
         restricted realization (see the next sentence). More precisely (DERIVED in the independent audit of V235): at
         beta = p the fixed-coefficient part T + U[.].grad rho0 still maps D_Z into Z, so for h in D_Z the image A_0 h
         lies in Z if and only if c[h] = 0; the failure is exactly the strain direction. The coefficient is about
         4e-21 (a_521 is about -9e-10), so the exclusion is exact but not visible numerically at any practical radius.
    (g4) (V236) Exterior inverse. On Omega_R = {|X| > R}, with the exterior version F_R of the scaled annular norm plus
         L^2(w_gamma) and no inner boundary condition, the actual exterior transport T_R = V.grad - 1 is, for all large
         R, a closed bijection from its maximal domain onto F_R, with inverse Q_R f = -int_0^inf e^(-t) f(Phi_t X) dt
         along the actual forward flow and a bound uniform in R. The scaled seminorm costs the factor
         1/(1 - ell0 beta) = k/(k - beta), from |Phi_t X| ~ r e^(ell0 t) and |D Phi_t| <= C e^(ell0 t); the weighted L^2
         part uses the exact Jacobian e^(2 ell0 t) for gamma < 2 + 2k and the pointwise growth bound for
         gamma >= 2 + 2k. Uniqueness needs no boundary condition, because beta < k excludes the homogeneous solutions
         h(Phi_t X) = e^t h(X). With a cutoff extension E_R (zero inside 5R/4, the identity outside 2R), the exterior
         operator T_R + P_R C0 E_R is a bijection with inverse bounded uniformly in large R (Neumann series with the
         small tails of (g2)), for p < beta < k and every gamma > 4k. It agrees with the actual A_0 only outside radius
         2R; for h in the exterior domain, A_0(E_R h) - (T_R + P_R C0 E_R) h = (eta_R - 1) T_R h + h V.grad eta_R on
         the exterior (V242). THEOREM (V236, V242).
    (g5) Neither obstruction mechanism of (e) transfers to Z (DERIVED, independent audit of V235). The strip
         argument of V232 needs the x^2-weighted vertical seminorm of the solution at infinity, which Z does not
         impose (its forcings themselves lie in Z when alpha <= beta + b). For the orbit argument of V234 the packets
         have Z norm of order X0^(2 + alpha - beta); after normalization the characteristic lower bound
         X0^(-(2 + alpha + k - beta)) stays below the Z upper bound X0^(-(2 + alpha)) precisely because beta < k. This
         is not a surjectivity statement; (g6) gives a third mechanism, which does apply on Z. (V244 records the same
         conclusion for V232: some of its strip forcings lie in Z, but the contradiction does not transfer.)
    (g6) (V243; THEOREM, independent audit recorded as V249) Z is not a valid global target either. For every 0 < alpha < 1,
         p < beta < k and gamma > 4k, the operators T, L_ren and A_0 on D_Z have infinite algebraic cokernel in Z, even
         before any normalization or domain restriction. V has no zero on the vertical axis other than 0, so
         V_2(0, y) > 0 for y > 0. For 0 < x < x0 the forward orbit of (x, 1/2) passes the saddle region in bounded
         time and then follows the outgoing vertical axis, with x_t comparable to x e^(ell0 t), y_t and r_t comparable
         to e^(ell0 t), and x_t/y_t < 1/4. Along it, U_1[h] is odd in x, so |U_1[h]| <= C ||h||_Z x_t^alpha
         r_t^(beta - alpha), while |rho0_x| <= C x_t r_t^(k-2) and |rho0_y| <= C x_t^2 r_t^(k-3). Hence the complete
         coupling, M0 column included, contributes O(||h||_Z x^(1 + alpha)) to the characteristic integral. The forcing
         F_sigma = |x|^sigma phi(x) g(y), with g odd, supported at heights in (Y, 2Y) and nonnegative there, and
         alpha < sigma < 1 + alpha, lies in D_Z, because V_1 d_x |x|^sigma = sigma a_1 |x|^sigma with V_1 = x a_1.
         After subtracting c[F_sigma] q for a fixed bump q off the axis cone with c[q] = 1, it has c = J = 0. Its
         characteristic integral from (x, 1/2) is a_sigma x^sigma + o(x^sigma) with a_sigma > 0. But a preimage h must
         satisfy |h(x, 1/2)| <= ||h||_Z x^2 (1/2)^alpha by the local E_2 factor, and sigma < 1 + alpha < 2.
         Distinct sigma give linearly independent cosets. The forcings are not globally smooth. Nothing is claimed
         about the range of F0 or about the target Z_2 below. The exterior inverse (g4) is unaffected, because its space imposes no quadratic
         condition at the origin. The cut-off local inverses of (a) have bounded Z norm (compact E_2 outputs, and compact C^alpha
         outputs away from the vertical axis, lie in Z).
    The scaled quadratic-axis target Z_2 (verifier proof V245; THEOREM at the scope of (a) to (c), the exclusion of
    the (g6) forcings and the nonclosability of J below, independent audit recorded as V254). For an annulus
    A = {R <= r <= 4R} put N_R(h) = ||h||_(L^inf(A)) + R^alpha [h]_(x, alpha; A) + R^(2 + alpha) [h]_(y, 2, alpha; A),
    where [h]_(x, alpha; A) is the horizontal Hoelder quotient at fixed y and [h]_(y, 2, alpha; A) the vertical quotient
    |h(x, y) - h(x, y')| / (x^2 |y - y'|^alpha) at fixed x, both points in A. Z_2 has the norm
    ||chi h||_(E_2) + sup_j 2^(-j beta) N_(2^j)(h) + ||h||_(L^2(w_gamma)), with p < beta < k and gamma > 4k. This is
    the theory author's earlier sketch Y_beta without the restriction beta <= 0. Every element of Z_2 is O(x^2 r^(beta - 2))
    near the vertical axis, by odd-y parity within one annulus. V245 proves: (a) Z_2 is Banach and embeds in Z, c is
    bounded, C0, C_ren and the unnormalized coupling are bounded on Z_2 with the small-tail bound
    ||tau_R C0|| <= C (R^(k-1) + R^(beta + k - gamma/2) + (R^(p - beta) + R^(2k - gamma/2))(1 + log R)), F0 lies in
    Z_2, and T and A_0 are closed on the maximal domain D_2; (b) on the exterior, with the exterior version of the
    Z_2 norm and no inner boundary condition, the actual T_R is a closed bijection from its maximal domain onto the
    exterior space for all large R, with inverse bounded uniformly in R; (c) the auxiliary operator T_R + P_R C0 E_R
    is a bijection with uniformly bounded inverse, and it agrees with A_0(E_R h) for r >= 2R. The exterior inverse
    uses the positive time change a = V_1/x: along the field V/a one has x_t = e^t x exactly, so vertical pairs keep
    a common abscissa and the vertical quotient is not mixed into the horizontal one (this removes the difficulty
    that the theory author's sketch had left open). The fractional-power forcings of (g6) are excluded from Z_2: along the
    orbits of (g6), x_t^2 r_t^(beta - 2) is comparable to x^2 e^(ell0 beta t), so forcings in Z_2 give
    characteristic integrals O(x^2). The strip forcings of V232 have scaled vertical quotient of order R^(2 - b - beta),
    and the orbit argument of V234 gives the decaying factor (X0/R_1)^(beta - k) (both DERIVED by the theory author). J is
    still not closable on the A_0 graph of Z_2. OPEN: a global inverse or Fredholm property on Z_2, and surjectivity
    of A_0 and L_ren for alpha <= 1/2 (T alone is not onto for alpha > 1/A_s, V266 below); for larger alpha see the
    next item.
    Turning-height obstruction on Z_2 (verifier proof V256 with an original-data interval certificate; THEOREM,
    independent audit recorded as V262). Mechanism: the axis rate a(0, y) = d_x V_1(0, y) changes sign, from -A (the origin
    rate of section 2) at the origin to ell0 at infinity. V256 certifies a simple zero y_*: log y_* lies in
    (4533/2048, 145057/65536), so y_* is in (9.1465, 9.1468), and da/d(log y) lies in (7.1952, 7.1954) on that whole
    interval. At y_* the near-axis orbits run parallel to the axis to second order: the orbit abscissa, as a function
    of height, has a nondegenerate minimum. A horizontal oscillation x^2 phi(x/q) cos(x/eps) g(y), with g supported
    near y_*, has bounded Z_2 norm when q^2 <= eps^alpha. Along orbits at abscissa about q it is sampled coherently
    over a height of order (eps/q)^(1/2) instead of eps/q. Stationary phase then gives two initial heights at distance
    of order eps/q whose preimage values differ by at least b q^2 (eps/q)^(1/2), more than the x^2-weighted vertical
    seminorm allows, about q^2 (eps/q)^alpha, when alpha > 1/2. For L_ren and A_0 the coupling difference bound
    adds a term that moves the threshold to 2/3. Statement: for 2k - 1 < beta < k and gamma > 4k, T: D_2 -> Z_2 is
    not onto for 1/2 < alpha < 1, and L_ren and A_0 are not onto Z_2 for 2/3 < alpha < 1, with the complete coupling
    and the full moving-tail column; bounded smooth zero-strain, zero-jet forcings have no uniformly bounded
    preimages, and open mapping on the closed graph gives non-surjectivity. Scope: no claim about high norms, the
    Sobolev condition (I), the range of F0, nonexistence of a profile or an infinite cokernel; degenerate turning
    heights are not covered; this mechanism gives nothing for alpha <= 1/2, where surjectivity of L_ren and A_0 is OPEN
    (the range 1/2 < alpha <= 2/3 for L_ren and A_0 is settled by the next refinement; T alone is not onto for
    alpha > 1/A_s, V266 below).
    Refinement (verifier proof V257; THEOREM, independent audit recorded as V265). For h = x^2 g with g compactly supported,
    even in x, bounded and uniformly C^alpha in y, U_1[h]/x is in the full joint C^alpha on bounded x-strips, with no horizontal
    regularity of g (y-frequency blocks and the exact partial Fourier kernel; near x = 0 the block is an average of
    the even part of d_x U_1). This bounds the full-future coupling difference by C N q^2 delta^alpha, and the same
    construction shows that L_ren and A_0 are not onto Z_2 for every 1/2 < alpha < 1. The open range is
    alpha <= 1/2 for A_0 and L_ren (for T alone see V266 below). Remedies: alpha <= 1/2 (heuristic), or the joint-cofactor target Z_cof (THEOREM, V261, verifier proof, independent audit recorded as V268): h = x^2 g with g in the
    full joint C^alpha locally and sup_R R^(2-beta)(||g||_inf + R^alpha [g]_(C^alpha)) on the dyadic annuli, plus
    L^2(w_gamma). For every 0 < alpha < 1 and 2k - 1 < beta < k the complete coupling is bounded with a small tail,
    the residual lies in Z_cof, T, L_ren and A_0 are closed on their maximal domains, and the actual auxiliary exterior
    operator is invertible; J is not closable. The turning-height forcings are unbounded in this norm, so V256 and V257
    do not apply to it; its global inverse is OPEN. Transport alone is not onto Z_2 or Z_cof near the source (THEOREM, V266, verifier proof, independent audit recorded as V272): with DV(P) = diag(A_s, mu_s) at the source P, 10 < A_s < 51/5, the cusp profiles s_+^a phi(y/s_+^b), a = 1/A_s, b = mu_s/A_s, of the conjugated transport give smooth compact forcings with c = J = 0 that span an infinite-dimensional subspace of the cokernel of T on either target for alpha > 1/A_s, so for every alpha >= 1/10. This excludes a Neumann series around T; it says nothing about A_0 or L_ren, since the full source coupling changes the equation. The nonlinear derivative loss persists on Z_cof (THEOREM, V264, verifier proof, independent audit recorded as V271): there are smooth
    inputs h_n with c = J = 0, supported in a fixed compact set away from both axes and bounded in the graph norms of T,
    L_ren and A_0, with ||N(h_n)|| >= b n for N(h) = (U[h] + (c[h]/3) X).grad h; so N has no continuous extension at 0
    in these graph topologies. This does not exclude a quasilinear scheme, stronger derivative norms or a profile.
    On Z_2 or any other target, the exterior inverse ((g4), or (b) and (c) above) and the cut-off local inverses at the origin and the
    sources must be matched across the middle annuli. The complete error of the specified cut-off origin patch is not
    compact on Z either, including the full M0 column and every gamma > 4k, for cutoffs satisfying the nonzero
    transport-derivative (flow-box) hypothesis (THEOREM, V239, audit recorded as V246); this concerns that single
    patch and does not exclude cancellation in a sum of patches or every parametrix. The non-surjectivity on Z is the
    separate argument of (g6) (V243), not a consequence of this patch statement; Z_2 is a separate problem. A bound ||A_0 K - I|| < 1 for an assembled
    parametrix K would give surjectivity only; injectivity on Z needs a separate lower estimate. The middle region has
    no small parameter; the transport part of the error is triangular along the flow, the coupling part is not. The cubic constraint, the nonlinear closure and condition (I) are separate.

## 4. The nonlinear term: why C^alpha(h) alone cannot close

N(h) = W[h].grad h, with W[h] = U[h] + (c[h]/3) X (CONVENTIONS S4.3, exact). In terms of Riesz transforms of h,
DU[h] = Riesz^2(d_x h) componentwise: d_x U_1 = -R_1 R_2 d_x h, d_y U_1 = -R_2^2 d_x h, d_x U_2 = R_1^2 d_x h, and
d_y U_2 = R_1 R_2 d_x h (from R_1 d_y = R_2 d_x). So U[h] is Lipschitz iff the three functions R_1^2 d_x h,
R_2^2 d_x h, R_1 R_2 d_x h are bounded; since R_1^2 + R_2^2 = -I this implies d_x h in L^infinity. It holds if d_x h
is in C^epsilon for some epsilon > 0 (with decay, or in a Dini class). It is not implied by h in C^alpha, nor by d_x h in
L^infinity, and it does not imply d_x h in C^alpha (V025).

Plane-wave algebra (exact). For a real wavevector xi let m(xi) := (nu_1 nu_2, -nu_1^2), nu = xi/|xi|, the symbol of U.
Since m is real and even, U acts on sin(xi.X) as multiplication by m(xi), and m(xi).xi = 0. For
S := sin(xi.X) - sin(eta.X),
    m(xi) sin(xi.X).grad S - m(eta) sin(eta.X).grad S
      = -(1/2)(m(xi).eta + m(eta).xi) sin((xi + eta).X) - (1/2)(m(xi).eta - m(eta).xi) sin((xi - eta).X).   (4.1)
With nu(xi) = (cos a, sin a) and nu(eta) = (cos b, sin b): m(xi).eta = |eta| cos a sin(a - b) and
m(eta).xi = -|xi| cos b sin(a - b). For xi = n(1, 1), eta = n(1, -1):
    S = 2 cos(nx) sin(ny) (class P),  U_S . grad S = -n sin(2ny),   U_S := m(xi) sin(xi.X) - m(eta) sin(eta.X).   (4.2)
The sum frequency drops out exactly. The self-interaction of each wave is zero because m(xi).xi = 0. The difference
frequency (0, 2n) points along e_2.

Lemma N (THEOREM in the repaired form of V030; the proof below is the theory author's first version, with the four defects the
verifier found listed after it). Let rho_bar be the exactly normalized modal background and
0 < alpha < 1. (The trial is analytic inside each of its radial pieces; the boxes below lie away from 0 inside one
such piece, V036.)
Fix x_0 in (0, x_P). Numerically V_1(x, 0) < 0 and d_y V_2(x, 0) > 0 on (0, x_P); only V(x_0, 0) = (V_1(x_0, 0), 0)
with V_1 != 0 and the regularity are used. Let K = B_+ union B_- with B_+ a closed box around X_0 = (x_0, 0) avoiding
0 and P, and B_- = -B_+ (reflection in x). Let X be any normed space of class-P functions on R^2 such that L g is a
distribution on a neighbourhood of K for g in X, and
    ||g||_{C^alpha(K)} + ||U[g]||_{C^alpha(K)} + |c[g]| <= C_X ||g||_X   for g in X.      (H_X)
Then there are h_n in C_c^infinity(K) of class P, with J(h_n) = 0, c[h_n] = 0 and sup_n ||h_n||_{C^alpha(R^2)} < inf,
such that
    (i) ||N(h_n)||_{L^inf} >= n^{1 - 2 alpha} - C n^{-2 alpha} and ||N(h_n)||_{C^alpha} >= c n^{1 - alpha};
    (ii) every g in X with L g = N(h_n) on a neighbourhood of K satisfies ||g||_X >= c_0 n^{1 - alpha} - C.
Consequently, if in addition sup_n ||h_n||_X < infinity (true for every norm dominated by a weighted C^alpha norm
plus |c|, with weights bounded above and below on K and on the compensator support), then h -> L^{-1} N(h) maps a
bounded subset of X onto an unbounded subset of X. The fixed-point map h -> -L^{-1}(F(rho_bar) + N(h)) cannot be
estimated in X in terms of ||h||_X: the inequality ||L^{-1} N(h)||_X <= Phi(||h||_X) fails for every function Phi.
This holds for all 0 < alpha < 1, with the strain term and the normalization included. Spaces in which h_n is
unbounded (for example C^{1,alpha}) are not affected.

Proof. Step 1 (construction). Let chi be a smooth even bump on R, equal to 1 on [-1/2, 1/2] and supported in [-1, 1].
Put phi(x, y) := chi((x - x_0)/delta) chi(y/delta) + chi((x + x_0)/delta) chi(y/delta), with delta small so that
supp phi is inside K. Then phi is even in x and in y. Let h_n^0 := n^{-alpha} phi S_n,
S_n = 2 cos(nx) sin(ny) = sin(xi.X) - sin(eta.X), with xi = n(1, 1) and eta = n(1, -1). Then h_n^0 is of class P,
supported in K, J(h_n^0) = 0 (the support avoids 0), and ||h_n^0||_{C^alpha} <= C. The weight sin(3 theta) r^{-3} is
smooth on K, so repeated integration by parts in y gives c[h_n^0] = O(n^{-M}) for every M. Fix a smooth class-P bump
zeta, supported away from K and from the forward trajectories through K, with c[zeta] = 1. Put
h_n := h_n^0 - c[h_n^0] zeta. Then c[h_n] = 0, and all terms involving zeta below are O(n^{-M}).
Step 2 (localized interaction). Write U[phi sin(xi.X)] = phi m(xi) sin(xi.X) + E_xi. In Fourier variables,
E_xi = Im( e^{i xi.X} int (m(xi + zeta') - m(xi)) phihat(zeta') e^{i zeta'.X} dzeta' / (2 pi)^2 ). Since m is
homogeneous of degree 0 and smooth away from 0, |m(xi + zeta') - m(xi)| <= C |zeta'| / |xi| for |zeta'| <= |xi|/2,
and phihat is a Schwartz function. Hence ||E_xi||_inf <= C/n and ||grad E_xi||_inf <= C. Therefore
U[h_n^0] = n^{-alpha} (phi U_S + E_n) and grad h_n^0 = n^{-alpha} (phi grad S + S grad phi), with ||E_n||_inf <= C/n.
By (4.2),
    N(h_n) = -n^{1 - 2 alpha} phi^2 sin(2ny) + e_n,   ||e_n||_inf <= C n^{-2 alpha}.          (4.3)
Here e_n collects phi U_S . S grad phi, E_n . grad h_n^0, the strain term (c[h_n]/3) X.grad h_n = 0, and the
zeta terms. This proves the L^inf part of (i). The C^alpha part follows from (4.3) by comparing the points
(x_0, 0) and (x_0, pi/(4n)).
Step 3 (flow-line identity). Let g in X with L g = f := N(h_n) near K. By (H_X), g, U[g] and T g = U[g].grad rho_bar
are in C^alpha(K), and V.grad g = f + g - T g - (c[g]/3) G_bar =: F is continuous on K. In flow-box coordinates for V
(V is C^1 and nonzero on K), F continuous implies that s -> g(Phi_s X) is C^1 with derivative F(Phi_s X), as long
as Phi_s X stays in K. Hence for X in K and s_0 such that Phi_s X stays in K for s in [0, s_0],
    e^{-s_0} g(Phi_{s_0} X) - g(X) = int_0^{s_0} e^{-s} [ f - T g - (c[g]/3) G_bar ](Phi_s X) ds.      (4.4)
Step 4 (two points). Take X = X_0 = (x_0, 0) and X' = (x_0, y_n), y_n = pi/(4n). On the x-axis f = 0 by oddness, so
the f-integral at X_0 vanishes. Along the trajectory of X', y(s) solves ydot = y beta(x, y) with
beta := int_0^1 d_y V_2(x, tau y) d tau in [beta_min, beta_max] on K, beta_min > 0. Let s_0 := min(log 2 / (2 beta_max), s_K),
where s_K is the exit time from the inner box {phi = 1} for trajectories starting within distance delta/4 of X_0. Then
y(s) in [y_n, sqrt(2) y_n] on [0, s_0], so 2n y(s) in [pi/2, pi/sqrt(2)] and sin(2n y(s)) >= sin(pi/sqrt(2)), about 0.796.
By (4.3),
    | int_0^{s_0} e^{-s} f(Phi_s X') ds | >= 0.796 (1 - e^{-s_0}) n^{1 - 2 alpha} - s_0 C n^{-2 alpha}.
Subtract (4.4) at X_0 from (4.4) at X'. The left side is at most (1 + e^{-s_0} Lip(Phi_{s_0})^alpha) [g]_{alpha,K} y_n^alpha.
The coupling term is at most s_0 Lip(Phi)^alpha [T g]_{alpha,K} y_n^alpha
<= C ||U[g]||_{C^alpha(K)} ||grad rho_bar||_{C^1(K)} n^{-alpha}. The strain term is at most C |c[g]| n^{-1}. With (H_X):
    0.796 (1 - e^{-s_0}) n^{1 - 2 alpha} - C n^{-2 alpha} <= C' ||g||_X n^{-alpha},
which is (ii). QED.

Repairs (V030). (1) The strain compensator zeta must lie inside the declared support set but outside the short flow
tube used in Step 4 (or the support must be enlarged); "away from the forward trajectories through K" is not enough as
stated. (2) The proof uses |beta| <= B; the lower bound beta_min > 0 was not proved and is not needed. (3) The lower
constant: sin(pi/sqrt(2)) is about 0.7957, so 0.796 is rounded upward; 0.79 is the correct lower constant. (4) Before
excluding arbitrary functions Phi, the bounded inputs are normalized to norm 1 and the quadratic homogeneity of N is
used: every solution of L g = N(H_n), H_n = h_n/||h_n||_X, has norm at least the lower bound divided by ||h_n||_X^2.
The verifier also notes that the hypotheses need only regular axis points x_0 > 0 near 0 (V_1(x, 0) = -Ax + o(x)),
so no sampled sign of V_1 along an interval is used.

Remark N.1 (where the loss comes from). N(h) has one derivative of h. L^{-1} gains a derivative only along V. At X_0,
V is parallel to e_1 while (4.2) puts the output frequency along e_2. The same construction works at every point X_1
with V(X_1) != 0, including points off the axes. Choose xi, eta with xi - eta perpendicular to V(X_1) and
m(xi).eta != m(eta).xi, and symmetrize the packet over the four reflections. The sum-frequency term of (4.1) is not
perpendicular to V and contributes O(n^{-2 alpha}) to the flow integral (integration by parts in s). Hence weights
that vanish on the axes do not remove the obstruction. (Sketch; the axis version above is the complete proof.)

Lemma N' (graph norms; THEOREM in the stronger form of V030, which replaces the sketch below). Verified statement:
there are smooth inputs h_n = h_1 + k_n, compactly supported away from 0, with J = c = 0 exactly, such that
||h_n||_{C^alpha} + ||L h_n||_{C^alpha} is bounded and ||N(h_n)||_{C^alpha} >= c n, and every g satisfying (H_X)
with L g = N(h_n) near K has ||g||_X >= c_X n. In the verified construction h_1 = -Lap P, with P compact, of class
P and quadratic on a flow box, so that U[h_1] = (-P_xy, P_xx) is a constant vector transverse to V there while
grad h_1 = 0 and c[h_1] = 0. The strips use an exact first integral z of the flow box instead of the signed distance:
k_n = n^{-alpha} Psi(n z) eta(s). A small exact strain compensator restores c = 0. The theory author's sketch, kept for the
mechanism: let X_gr := {h : h in C^alpha, L h in C^alpha} with the graph norm.
Lemma N does not apply directly, because ||h_n||_{X_gr} ~ n^{1 - alpha}. Take instead h = h_1 + k_n. Here h_1 is a
fixed smooth class-P function with W[h_1](X_1) not parallel to V(X_1) at a point X_1 off the axes.
k_n := n^{-alpha} Psi(n d(X)) psi(X), where d is the signed distance to the trajectory through X_1, Psi is a smooth
compactly supported profile and psi a cutoff. Then V.grad d = O(d), so ||k_n||_{X_gr} is bounded, but
N(h_1 + k_n) contains W[h_1].grad k_n = n^{1 - alpha} Psi'(n d) psi W[h_1].grad d. This term oscillates transversally
to V with amplitude n^{1 - alpha}. The two-point argument of Step 4, across the strip at distance 1/n, gives
||L^{-1} N(h_1 + k_n)||_{X_gr} >= c n^{1 - alpha}. So the explicit semilinear map fails to close in the C^alpha graph
norm as well. This is
the usual derivative loss of quasilinear transport. The L^2 counterpart is the verified weak-graph discontinuity of N
in the diagnostic weighted H^1 norm (V019).

Answer to "is C^alpha(h_x) genuinely unnecessary?". For the linear theory at low order, yes: Proposition S(c), the
source theorem 3.1 and the far window all bound h in C^alpha (or C^alpha_p) by the forcing in the same class, without
h_x; so do the actual exterior inverses on Z_sc, Z_2 and Z_cof (THEOREMS, V242, V254, V268; 3.4(g)), whose norms
contain no derivative of h. For the nonlinear closure of the explicit semilinear map, no. Lemmas N and N' show that the fixed-point map
h -> -L^{-1}(F(rho_bar) + N(h)) cannot be estimated in C^alpha(h) or its graph norm, nor in any norm satisfying (H_X)
in which their explicit packets stay bounded. They are not theorems about every scheme, every stronger space or
nonexistence of a profile. The quasilinear scheme of section 5 uses a Lipschitz transport velocity V + W[h] (sufficient, not shown
necessary). Since DU[h] = Riesz^2(d_x h) exactly, this is the condition Riesz^2(d_x h) in L^infinity, for which
d_x h in C^epsilon is sufficient. The
precise loss is one derivative, transverse to V. The derivative that enters the velocity is d_x h only. The
bilinear bound (Q3) of the scheme of section 5, as formulated there, uses grad h in L^infinity, so that scheme puts both
derivatives in its high norm; this is a property of that formulation, not a proved necessity. Only conormal
derivatives are needed across the axes: W_1 = 0 on {x = 0} and W_2 = 0 on {y = 0}, so
W.grad h = (W_1/x)(x h_x) + (W_2/y)(y h_y).

Lemma N'' (the localized origin graph; THEOREM, V211). Fix 0 < alpha < 1, E_2 = C^alpha_2 as in 2(e), and let
L_delta be either localized operator of 2(e) (frozen saddle, or actual transport on B_{delta/2}), with
||h||_gr = ||h||_{E_2} + ||L_delta h||_{E_2} on its maximal domain, and N(h) = (U[h] + c[h] X/3).grad h. There are a
fixed compact K inside B_{delta/2}, separated from both axes, and smooth h_n supported in K with J(h_n) = c[h_n] = 0,
sup_n ||h_n||_gr < infinity, ||N(h_n)||_{E_2} >= c_1 n and ||L_delta^{-1} N(h_n)||_{E_2} >= c_2 n. Rescaling by
n^{-1/2} shows that N and L_delta^{-1} N are discontinuous at 0 from the graph norm to E_2. Construction: a compact
potential P with U[-Delta P] = (-P_xy, P_xx) equal to a constant vector transverse to V_delta on a box around a
regular point Q (with zero strain), characteristic coordinates (s, z) near Q with V_delta.grad z = 0, and strips in z
of width 1/n, so that the large z-derivative is absent from V_delta.grad h_n while the transverse velocity of the
fixed part acts on it in N. Away from the axes the weight |x|^2 is bounded above and below, so E_2 membership is
local C^alpha membership; the nonlocal image near the axes is controlled by the global image bound of V207. A
two-trajectory identity on the maximal domain gives the lower bound for L_delta^{-1} N(h_n). This is the topic of
Lemma N' carried into the weighted graph that S(e) actually inverts; a counterexample in an unweighted graph does not
transfer to it by naming a weight, which is why the separate proof was needed.

## 5. A compatible high/low formulation (DERIVED reformulation; the linear estimates are OPEN)

Exact quasilinear form. With A_h g := (V + W[h]).grad g - g + W[g].grad rho_bar (linear in g, affine in h),
    F_N(rho_bar + h) = F_N(rho_bar) + A_h h   exactly.
Iteration: A_{h_j} h_{j+1} = -F_N(rho_bar). Differences: A_{h_j}(h_{j+1} - h_j) = -W[h_j - h_{j-1}].grad h_j.
At the origin, DW[h](0) = c[h] diag(-2/3, 4/3). So V + W[h] has eigenvalues -A' = -(A + 2c/3) and D' = D + 4c/3
with D' = 2A' + 1. The normalization structure is preserved and x^2 y stays the frozen kernel. The stagnation points
+-P move with h. At infinity the exponent changes to k' = 1/(c_l + c[h]/3), which is what the parametric family of
Remark N5 (S2_L2_THEORY.md) absorbs.

Requirements (each OPEN unless stated):
(Q1) Low norm X_lo (C^alpha_w-type with the weights of sections 2 and 3, or L^2(w)): A_h^{-1} is bounded on X_lo,
     uniformly for h in a small ball of the high norm. The frozen pieces are Proposition S(c, d), Theorem 3.1 (verified)
     and the far window. The global estimate is open (3.3).
(Q2) High norm X_hi (C^{1,alpha}_w-type, or H^{2+eps}(w) with the windows of section 6 of S2_L2_THEORY.md):
     ||A_h^{-1} F_N(rho_bar)||_{X_hi} <= C ||F_N(rho_bar)||_{Y_sigma}, for a smoother target Y_sigma, uniformly for h
     in a small ball of X_hi. A loss is
     allowed because the forcing is fixed: by the source theorem, order sigma gives output order
     sigma - (sigma - 1)/A. Order 1 + alpha in X_hi therefore needs sigma >= 1 + alpha A/(A - 1), below the ceiling
     (1 + g)/A, about 3.03.
(Q3) Bilinear bound: ||W[d].grad h||_{X_lo} <= C ||d||_{X_lo} ||h||_{X_hi}. This needs grad h in L^infinity (with the
     conormal structure above) and U bounded on X_lo. It must be proved for the particular pair, including its axis
     and tail mapping; a general statement about standard weighted pairs does not supply it.
(Q4) Smallness: ||F_N(rho_bar)||_{Y_sigma} small and the constants of (Q1) to (Q3) certified.
The precise conclusion is the two-norm theorem verified in V038. Let X_hi be reflexive and continuously and
injectively embedded in X_lo; for every v in the closed high ball of radius r let the solution operator of A_v be
compatible (one realization, defined on X_lo with values in X_lo and mapping Y_sigma into X_hi, with bounds K_L
and K_H); let the low inverse inequality ||g||_{X_lo} <= K_L ||A_v g||_{X_lo} hold for g in X_hi; let (Q3) hold with
constant C_B; and let K_H eta <= r and K_L C_B K_H eta < 1, eta = ||F_N(rho_bar)||_{Y_sigma}. Then the iterates stay
in the high ball and converge in X_lo, a weakly convergent subsequence in X_hi identifies the limit, and the limit
solves the equation. A nonreflexive high space (a Hoelder space, for example) needs in addition specified weak-star
compactness and weak-star continuity of the linear part and of the bilinear map in its second argument; unspecified
weak-star compactness is not enough (V038). For the actual moving-tail equation ell = ell(h) moves with h, and the
applicable form is the conditional theorem V062 of the closure document (assuming the positive axis rate), whose
inverse hypotheses are OPEN. This is a standard scheme and needs no Nash-Moser iteration, because the loss in (Q2) falls
only on the fixed forcing. The role of the rank-one term: c[h] enters A_h through W[h] (transport) and W[g].grad rho_bar
(the column (c[g]/3) G_bar). The first is harmless. The second needs the bordering of 3.2.

## 6. The rank-one term c[h] in the Hoelder setting

c[h] = (1/pi) int sin(3 theta) r^{-3} h for h = O(r^{1+eps}) at 0 (CONVENTIONS S3.2). On weighted sup spaces with
|h| <= M r^3 near 0 the integral converges absolutely, so c is bounded, with |c[h]| <= C M plus the far contribution.
This includes the jet x^2 y itself. At
infinity the integral converges for |h| <= M r^gamma, gamma < 1. Thus c is a bounded functional on the C^alpha
spaces of section 2 combined with the far window. Its column G_bar is not in the far target (3.2), so in any Hoelder
version the strain is handled exactly as in Avenue I: the full operator L = L_fix + (c[h]/3) G_bar is bordered by the
log-tail direction. The verified singular-adjoint identity at the frozen saddle (V016) gives, on the disk of radius R
and with zero outer flux, |c_R[h]| <= K_A R^2 ||T_0 h/(x^2 y)||_infinity with K_A <= 0.032163 (the certified value is
about 0.032162163; the earlier "K_A < 0.032162" did not follow, V028). This is a bound of the local strain by the
forcing in exactly the weighted sup norm of Proposition H0 at (a, b) = (2, 1).

Strain on the Hoelder classes C^alpha_p (THEOREM, V028; constant corrected by V201). For h in C^alpha_p, oddness
gives |h(x, y)| <= [h]_{y,p} |x|^p |y|^alpha, and the near-origin strain integral over B_R is bounded by
[h]_{y,p} R^{p+alpha-1} A_{p,alpha}/(pi (p + alpha - 1)) when p + alpha > 1, where
A_{p,alpha} = int_0^{2 pi} |sin 3theta| |cos theta|^p |sin theta|^alpha dtheta <= 4. The angular factor cannot be
dropped: for p = 1, alpha = 1/100 and R = 1 an explicit h = chi(x)|x|^{1+alpha} f(y/|x|) has
pi alpha |c_{<1}[h]| > 2.17 while [h]_{y,1} < 2.05, with a purely rational proof, and smooth compactly supported
parity examples with zero jet give the same violation (V201). The first version of this paragraph omitted
A_{p,alpha}; that factor-free inequality is REFUTED (V201). For p + alpha <= 1, c is unbounded on C^alpha_p:
for p + alpha < 1, h_e = e^{p+alpha} H(X/e) with a smooth annular class-P bump H, c[H] != 0, has bounded norm and
c[h_e] = e^{p+alpha-1} c[H]; at equality a degree-one angular function between radii e and 1 gives c ~ log(1/e). So a
Hoelder space carrying the rank-one term needs p + alpha > 1 or an added weighted sup condition near 0 (the cubic
sup norm of Proposition H0 suffices). The coupling class C^alpha_1 of (d) satisfies p + alpha > 1 for every alpha > 0.

## 7. What Avenue II establishes, and what it does not

Verified (THEOREM): Proposition H0 and S(a) to (c) (V028); S(d) in the smooth-cutoff form, with the whole-plane
inverse of T_0 + B_delta on C^alpha_1 (V028); S(e): the directional velocity bound, the normalized localized coupling
of size O(delta^{3-p-alpha}), and the inverses on C^alpha_2 for every alpha < 1 with frozen or (inside B_{delta/2})
actual transport (V203 to V207), with J not closable in that graph norm (V208); the strain bound on C^alpha_p for p + alpha > 1 and its failure for
p + alpha <= 1 (V028); the source theorem 3.1 at mu = 1 (V013) and at the actual rate mu < 1 (V029), and 3.1(iii), the
actual unnormalized source operator on C^alpha_b intersected with L^2 for every alpha < 1 (V213 to V215); the common
target Y of 3.4 with F0 in Y, the bounded complete coupling and the closed full operator A_0 on its maximal domain
(V222, V224, V228; on E_2 and for every gamma > 4k, V241, V247), the noncompact specified cutoff parametrix error
(V227), and the far obstructions on Y (V232, V234; infinite algebraic cokernel of T, L_ren and A_0 on E_2 and for every
gamma > 4k, V241); the scaled far target Z of 3.4(g1) to (g3) (V235, V244), the exterior inverse (g4) (V236, V242),
the infinite algebraic cokernel on Z of (g6) (V243, V249) and the noncompactness of the specified origin patch error
on Z (V239, V246); on the scaled quadratic-axis target Z_2 of 3.4(g), the bounded complete coupling with small
tails, F0 in Z_2, the closed full operator, the nonclosability of J and the actual exterior auxiliary inverse (V245,
V254), and the turning-height non-surjectivity on Z_2 (T for alpha > 1/2, V256, V262; L_ren and A_0 for
alpha > 1/2, V257, V265); the abstract completion with |J| added to the graph norm and its invisible scalar (V240, V246,
Remark 2.2);
Lemma N and the
stronger Lemma N' (V030); Lemma N'' in the C^alpha_2 graph of S(e) (V211). DERIVED, not submitted as theorems: the plane-wave identity (4.2) (used inside V030); the
identity DU[h] = Riesz^2(d_x h); the quasilinear identity of section 5. REFUTED: the indicator form of S(d) and the
norm transfer of Remark 2.1; the 0.5227 barrier and the necessity of an x-derivative of h for the localized coupling
(V203). Not established: the Hoelder theory of the actual transport near 0 beyond the localized whole-plane
operators of S(e) (in particular on a disk with boundary conditions); a global C^alpha
inverse of L; any C^alpha estimate with numerical constants; the high/low closure (Q1) to (Q4). No same-order global
C^alpha inverse is claimed.

## 8. Admissible alpha (summary)

| Piece | admissible alpha | space |
|---|---|---|
| frozen saddle, isotropic | 0 < alpha < 1/D, about 0.0469 (sharp) | C^alpha_0 |
| frozen saddle, axis-weighted p | alpha < (1 + pA)/D (sharp); all alpha < 1 for p >= 2 | C^alpha_p |
| saddle plus localized coupling (frozen transport, no strain column) | alpha < (1 + A)/D, about 0.5227, on C^alpha_1 (V028); every alpha < 1 on C^alpha_p with 1 <= p < 2 and 1 + pA > D alpha (V203) | C^alpha_p |
| normalized localized coupling alone, actual C^{4,1} background | operator norm comparable to delta^2, every 0 < alpha < 1 (V219, sharp) | C^alpha_2 |
| saddle plus complete normalized localized coupling (strain column included), frozen transport or actual transport on B_(delta/2) | every 0 < alpha < 1 (V204, V206, V207); J not closable in the graph norm (V208) | C^alpha_2 |
| strain functional bounded | p + alpha > 1 (verified; fails for p + alpha <= 1) | C^alpha_p |
| frozen coupled source, actual rate mu < 1 | all 0 < alpha < 1 (verified, V029) | C^alpha_* compact input |
| frozen coupled source, no support restriction | 0 < alpha < min(1, 1/mu), every alpha < 1 at the modal source (V213) | C^alpha_b intersected with L^2 |
| actual variable unnormalized source operator on B_(delta/2), whole-plane extension | every 0 < alpha < 1 (V214, V215); strain column only as prescribed forcing | C^alpha_b intersected with L^2 |
| pure transport source (no coupling) | alpha < 1/A, about 0.0985 | (illustration) |
| infinity | all alpha, gamma in [2k - 1, k) | scaled C^alpha |
| common target, bounded complete coupling and closed full operator A_0 | every 0 < alpha < 1 and every gamma > 4k, and on E_2 itself (V222, V224, V228 for 4k < gamma < 2; V241, V247) | E_2, and E_2 intersected with L^2(w_gamma) |
| bounded inverse, or even surjectivity, of T, L_ren or A_0 on the common target | none: infinite algebraic cokernel on E_2 and for every gamma > 4k (V232, V234, V241) | E_2, and E_2 intersected with L^2(w_gamma) |
| bounded complete coupling, closed full operator, residual included, on the scaled target | every 0 < alpha < 1, 2k - 1 < beta < k, gamma > 4k; at beta = 2k - 1 the full operator does not map the transport graph into Z (THEOREM, V235, V244) | Z of 3.4(g) |
| surjectivity of T, L_ren or A_0 onto the scaled target | none: infinite algebraic cokernel (THEOREM, V243, V249) | Z of 3.4(g) |
| bounded complete coupling, closed full operator, residual included, actual exterior inverse, on the scaled quadratic-axis target | every 0 < alpha < 1, 2k - 1 < beta < k, gamma > 4k (THEOREM, V245, V254) | Z_2 of 3.4(g) |
| surjectivity of T, L_ren or A_0, or a global inverse, on the scaled quadratic-axis target | T not onto for 1/2 < alpha < 1, L_ren and A_0 not onto for 2/3 < alpha < 1, 2k - 1 < beta < k, gamma > 4k (THEOREM, V256, V262, turning height); L_ren and A_0 not onto for 1/2 < alpha <= 2/3 (THEOREM, V257, V265); T not onto for 1/A_s < alpha < 1, A_s about 10.15, so for every alpha >= 1/10 (THEOREM, V266, V272); alpha <= 1/2 for L_ren and A_0, and a global inverse, OPEN | Z_2 of 3.4(g) |
| bounded complete coupling, residual included, closed T, L_ren and A_0, actual exterior inverse, on the joint-cofactor target (h = x^2 g, g in a scaled joint C^alpha) | every 0 < alpha < 1 (THEOREM, V261, V268); the exterior inverse formula is exterior only; a global inverse OPEN | Z_cof of 3.4(g) |
| surjectivity of T alone on Z_2 or Z_cof | none for 1/A_s < alpha < 1, so for every alpha >= 1/10: infinite algebraic cokernel from cusps at the source (THEOREM, V266, V272); no statement about L_ren or A_0 | Z_2 and Z_cof of 3.4(g) |
| nonlinear closure of the semilinear map in the graph norms of T, L_ren and A_0 on Z_cof | none: not continuous at 0, even with c = J = 0 (THEOREM, V264, V271); a quasilinear scheme is not excluded | graph norms on Z_cof |
| bounded complete coupling on the transport domain with vertical weight \|x\|^p | p = 2 only: fails for every p > 2 (V229) | E_p |
| bounded complete coupling at the Lipschitz endpoint | fails at alpha = 1 (logarithmic source blow-up, V230) | E_2 with alpha = 1 |
| actual exterior inverse of T_R + P_R C0 E_R, large R | every 0 < alpha < 1, 2k - 1 < beta < k, gamma > 4k (THEOREM, V236, V242) | exterior scaled space F_R |
| nonlinear closure in the localized C^alpha_2 graph of 2(e) | none (Lemma N'', V211; even with J = c = 0) | the graph norm of L_delta on E_2 |
| nonlinear closure of the explicit semilinear map (perturbative) | none (Lemma N, N') | any norm satisfying (H_X) in which the explicit sequences of Lemmas N and N' are bounded (for example weighted C^alpha plus \|c\| or the C^alpha graph norm) |
| grad h across the x-axis segment [0, x_P), data even in x, frozen saddle | the explicit smooth-forcing example (Prop F4 of S2_L2_THEORY.md 6.2) is locally C^{1,1-1/D} and rules out alpha > 1 - 1/D (about 0.9531); the endpoint is attained by it (V067); no endpoint inverse and no statement about the actual operator | C^{1,alpha} |
| conditional profile of Theorem E (CONDITIONAL THEOREM, V178) | alpha < 1/20 on compact subsets of the punctured plane (Sobolev embedding of order 41/20) | C^{1,alpha} |

## 9. Verification status

- V028 (2026-10-28T02:22Z): H0 and S(a) to (c) CONFIRMED on their whole-plane maximal domains, with the sharpness
  of (c) including equality via the replacement test function; S(d) CONFIRMED in the smooth-cutoff form; the
  indicator form and the norm transfer of Remark 2.1 REFUTED; strain bounded on C^alpha_p iff p + alpha > 1.
- V029 (02:26Z): the actual-rate source Hoelder theorem CONFIRMED.
- V030 (02:30Z): Lemma N CONFIRMED with the four repairs listed after its proof, and Lemma N' CONFIRMED in a stronger
  form (graph-bounded inputs, ||N||_{C^alpha} >= c n).
- V036 (02:50Z): the modal trial is C^{4,1} and not C^5 at 0 (REFUTED for C^5). The C^5 hypothesis of S(d) is
  weakened to C^4, which the verifier's proof uses, so S(d) applies to the trial. The smooth flow boxes of Lemma N lie
  away from 0 inside one analytic radial piece. Both conclusions stand (CONFIRMED with the corrected hypotheses).
- Remarks N.1 and 3.1, sections 5 and 6 (apart from the verified strain bound): DERIVED, not submitted as theorems.
- The C^{1,alpha} limit across the x-axis segment: Prop F4 of S2_L2_THEORY.md 6.2, THEOREM for the frozen formula
  (V067): the explicit solution is locally C^{1,1-1/D} and not C^{1,alpha} for alpha > 1 - 1/D, and the Sobolev
  endpoint s = 5/2 - 1/D is excluded; for the true operator OPEN. A strict Hoelder endpoint alpha < 1 - 1/D printed
  earlier for this example is REFUTED (V253).
- V201 (13:26Z): the strain bound of section 6 holds with the angular factor A_{p,alpha} <= 4 (CONFIRMED); the
  factor-free version first printed is false (REFUTED, explicit rational counterexample). The threshold p + alpha > 1
  is unchanged. Check by the theory author: the factor is the angular integral left after |h| <= [h]_{y,p} r^{p+alpha}
  |cos theta|^p |sin theta|^alpha is inserted in c[h] = (1/pi) int sin(3 theta) r^{-3} h.
- V203 (13:41Z): the directional velocity bound and ||B_delta||_{E_p} = O(delta^{2-p}) CONFIRMED; the derivative
  necessity and the 0.5227 barrier of (d) REFUTED. V204 (13:42Z): the strain column and the normalized frozen inverse
  CONFIRMED. V205 (13:46Z): the strain identity and cubic cancellation on E_p CONFIRMED. V206 (13:50Z): the inverse of
  the localized actual-transport operator CONFIRMED. V207 (13:52Z): the quadratic endpoint, inverses on E_2,
  CONFIRMED. V208 (13:53Z): J not closable in the E_2 graph CONFIRMED. Independent cross-audits of V203 to V206
  (recorded by the verifier as V212): PASS WITH REMARKS, no gap; remarks of presentation only (an implicit
  band-limitation step before Bernstein's inequality, the split of products across the cutoff boundary, the
  identification A0 = 2 ell - 1, D0 = 4 ell - 1 for the trial). The separate cross-audit of V207 and V208 (14:09Z): PASS
  WITH REMARKS, no gap. Its remarks: the domain of J should be stated (smooth compactly supported functions in E_2,
  both parities), the conclusion of V208 is best stated in density form, which the verifier qualified to the
  relative-domain statement given in 2(e) (V216), and the p-independent bounds of V203 and V204 used by V207 apply verbatim at p = 2.
- V211 (14:02Z): Lemma N'' (section 4), the nonlinear failure in the actual localized E_2 graph, CONFIRMED for both
  localized operators of V207 and the actual modal background; every input and image membership is checked. Not a
  theorem about every stronger Hoelder norm, nor about nonexistence of a profile. Independent cross-audit (theory author,
  14:17Z): PASS WITH REMARKS, no gap; remarks: the symmetry of the field under both reflections and the vanishing of
  the canonical far subtraction by parity are used without being stated; the actual velocity needs only C^3 near the
  strip, not C^infinity; "does not close" refers to the perturbative map about 0, not to a quasilinear scheme.
- V213 (14:08Z): the frozen source inverse on C^alpha_b intersected with L^2 without a support hypothesis, for
  0 < alpha < min(1, 1/mu), CONFIRMED; the full strain functional is unbounded there. V214 (14:12Z): the smooth
  transport conjugacy at the actual source and its original-data hypotheses CONFIRMED. V215 (14:14Z): the inverse of
  the whole-plane extension of the actual variable unnormalized source operator on C^alpha_b intersected with L^2,
  every alpha < 1, CONFIRMED; global normalized inversion OPEN. V216 (14:17Z): the cross-audit of V207 and V208
  recorded, with the relative-domain form of the density statement. V217 (14:18Z): that relative statement CONFIRMED
  and the unqualified density of smooth inputs in the whole maximal E_2 graph intersected with ker c REFUTED (a
  compact transverse |z|^alpha cusp with a smooth strain correction has distance at least a positive constant from
  every smooth input); V208 is unaffected. The separate cross-audit of V213 (14:25Z, recorded by the verifier as V221): PASS WITH REMARKS, no
  mathematical gap; the remarks concern wording (the high dyadic sum is finite and dominated by its top term because
  alpha < 1/mu; every alpha < 1 is covered because mu < 1, while a mu > 1 is a hypothesis), the velocity (the L^2
  multiplier velocity, canonical on the parity class) and the scope of the strain counterexample (unbounded in the
  X_alpha norm, not shown relative to the graph norm); all are reflected in 3.1(iii).
- V219 (14:22Z): the complete normalized localized coupling has E_2 operator norm comparable to delta^2 for the
  actual C^{4,1} background, every alpha < 1, and the rate is sharp (CONFIRMED, qualitative constants; 2(e)). An independent cross-audit found no mathematical gap (V225); its remarks are cosmetic, except that the constants are not uniform in alpha and that the sharp part of the norm is the x-seminorm. The separate cross-audit of
  V214 and V215 (V223): PASS WITH REMARKS, no gap; the remainder limit is smooth, not only C^2; the essential
  denominator is 10 mu - A; the analytic-disk wording rests on the structure of the trial; the cutoff is radial; the
  commutator uses an exact identity and an a priori bound; the velocity is the L^2 multiplier velocity (for odd-y
  inputs without x-parity the canonical one differs by a constant U_1 term, a further O(delta^{1-alpha})
  perturbation after localization); delta depends on alpha. All are reflected in 3.1(iii).
- V226: the actual-variable origin factorization error is O(delta^2), not only O(delta^{2-alpha}): the multiplier
  1/A_delta - 1/A0 has supremum O(delta^2) and gradient O(delta), and the supported-endpoint product estimate gives an
  E_2 operator bound O(delta^2) (CONFIRMED; 2(e)). An independent cross-audit found no mathematical gap; its remarks
  are that the x-seminorm needs only h(0, y) = 0, that the constant is independent of alpha and p, that the combined
  statement should fix a radial cutoff, and that sharpness is not claimed.
- V222 (14:28Z): the common target Y, F0 in Y exactly for gamma > 4k, |c| <= 4/pi, and the bounded cut-off local
  inverses CONFIRMED. V224 (14:33Z): the bounded complete coupling on Y with its tail, the global velocity bounds, the
  closedness of L_ren on D_Y and the nonclosability of J CONFIRMED. V227 (14:40Z): the noncompactness of the cutoff
  commutator and of the parametrix error CONFIRMED. V228 (14:42Z): m0 in Y, A_0 closed on D_Y with its tail, and the
  O(delta^(3-alpha)) column extension CONFIRMED. Independent cross-audits of all four and of V226 (recorded by the
  verifier as V231 and V233): PASS WITH REMARKS, no mathematical gap. Remarks: the bounded cutoff maps even map E_2
  into Y, so the weighted part of the input norm is unused and gamma > 4k is forced by F0 alone; the canonical velocity
  equals the L^2 multiplier velocity on compact inputs of the parity class (zero far subtraction), which is used in
  the band estimates; L_fix in V224 is the fixed-ell expression and agrees with A_0 only on c = 0; in V227 the
  mechanism is the noncompact embedding of D_Y into Y; in V228 the sharp U[zeta] = O(r^k (1 + log r)) follows from
  the modal formulas and is needed only for the tail rate. All are reflected in 3.4.
- V234 (14:58Z): the theory author's far obstruction, 3.4(e), CONFIRMED independently in the stronger non-surjective form,
  with the orbit constant 4 C R_1^(k-1)/(ell0 (1 - k)); B must be bounded and linear; abstractly gamma > 4k, in the
  applications 4k < gamma < 2. An earlier independent audit of the theory author's draft found the same repairs. No universal
  necessity of one replacement norm is asserted, and the scaled far space is called a candidate.
- V232 (14:53Z) with V237 (15:06Z): the infinite algebraic cokernel of T, L_ren and A_0 on Y (3.4(e)) PROVED by the
  verifier; independent cross-audit PASS WITH REMARKS, no gap (recorded as V237). Remarks: J(f_b) = 0 refers to the
  local smooth jet, not to an extension of the graph functional; the drift bound is 2 C Y^(k-1)/(ell0 (1 - k)); the
  coupling bound is marginal by ell0 k = 1 and is closed by a split of the time integral, giving O(x^2 log(1/x)); the
  cokernel has continuum dimension; the argument extends to b in (max(0, (1 - gamma)/2), 2 - k).
- V229, V230 (14:46Z) with V238 (15:10Z): the sharpness of p = 2 and the exclusion of alpha = 1 (3.4(b)) CONFIRMED
  after an independent cross-audit (PASS WITH REMARKS, no gap). Wording as corrected: the maximal transport domain is
  not contained in the maximal domain of the full expression; no reverse inclusion is claimed. The weight range
  4k < gamma < 2 in V230 is not a necessary threshold for the compact examples.
- V235 (15:01Z) and V236 (15:04Z): the scaled far target Z, its endpoint obstruction and the exterior inverse
  (3.4(g)). Both independent cross-audits passed with remarks; V236 is CONFIRMED (V242, 15:20Z) and V235 is CONFIRMED
  (V244, 15:25Z; one sentence claiming that Z excludes all earlier far packets was withdrawn, see (g5)).
- V239 (15:14Z) with V246 (15:33Z): the complete error of the specified full-column origin cutoff patch is
  noncompact on Z, for cutoffs satisfying the flow-box hypothesis (3.4(g)), CONFIRMED; not a statement about sums of
  patches or every parametrix; a norm-small complete right error would give onto only. V240 (15:14Z) with V246:
  completing smooth zero-strain inputs in the A_0 graph norm on Z plus |J| gives G_sm (+) R, whose function
  projection has a nonzero pure scalar kernel invisible to A_0 (Remark 2.2), CONFIRMED; G_sm is the smooth graph
  closure only; stronger genuine trace norms are not excluded.
- V241 (15:16Z) with V247 (15:33Z): bounded complete coupling and closed maximal realizations on E_2 and on every Y
  with gamma > 4k, and infinite algebraic cokernel of T, L_ren and A_0 on each (3.4(b), (c), (e)), CONFIRMED. The
  weighted L^2 velocity theorem is not extended. The range of F0 and closedness of the range remain OPEN.
- V243 (15:23Z): T, L_ren and A_0 have infinite algebraic cokernel on Z (3.4(g6)). Verifier proof; independent
  cross-audit PASS WITH REMARKS, no gap, recorded as V249 (15:38Z): CONFIRMED. The remarks (the C^alpha quotient V_1/x
  from the actual density regularity, the nonstationary orbit, negative beta in both radial comparisons, the higher
  transverse order of the coupling integrals) are clarifications. No conclusion about the range of F0 or about Z_2.
- V245 (15:27Z) with V254 (15:50Z): the scaled quadratic-axis target Z_2: bounded coupling with small tails,
  residual, closed full operator, nonclosability of J, and the actual exterior auxiliary inverse by the time change
  a = V_1/x (3.4(g)). Verifier proof; independent audit PASS WITH REMARKS (two typos clarified), recorded as V254:
  CONFIRMED at the original qualitative scope. No global inverse or certified radius. The turning-height
  obstruction is outside this statement (V256).
- V253 (15:46Z): review of this document. The strict Hoelder endpoint for the frozen x-axis example is REFUTED (the
  example is locally C^{1,1-1/D}, V067); sections 0, 8, 9 and 10 corrected. The other scope corrections (Remarks 2.1
  and 2.2, 3.1(ii), the proof of S(c), 3.4(d), (g3) and the patching paragraph, sections 4 and 5, status times,
  decimal notation) are applied.
- V256 (15:56Z): turning-height obstruction on Z_2 (3.4(g)): T is not onto Z_2 for alpha > 1/2, and L_ren and A_0
  are not onto Z_2 for alpha > 2/3, for 2k - 1 < beta < k and gamma > 4k. Verifier proof with an original-data
  interval certificate of a simple axis turn. Independent audit PASS WITH REMARKS, recorded as V262 (16:19Z):
  THEOREM at the stated thresholds; the two precisions of the certificate are not independent evidence.
  Non-surjectivity only: no infinite cokernel, no claim about F0 or profile existence; alpha <= 2/3 for the full
  operator was left OPEN there (1/2 < alpha <= 2/3 settled by V257, V265).
- V257 (16:05Z): joint C^alpha bound for the divided velocity U_1[x^2 g]/x (3.4(g)); it lowers the threshold for
  L_ren and A_0 on Z_2 to alpha > 1/2. Verifier proof; independent audit PASS WITH REMARKS, recorded as V265
  (16:23Z): THEOREM. The endpoint alpha = 1/2 and below are OPEN.
- V261 (16:17Z): the joint-cofactor target Z_cof (3.4(g)): mapping with small tail, F0 membership, closed maximal
  domains and the actual auxiliary exterior inverse for every alpha < 1 and 2k - 1 < beta < k; J not closable; the
  turning-height forcings are unbounded there. Verifier proof; independent audit PASS WITH REMARKS, recorded as V268
  (16:30Z): THEOREM. The cut-off formula of the exterior operator concerns the exterior only and says nothing about
  the nonlocal image inside the cut-off disk. Global inverse OPEN.
- V264 (16:21Z): on Z_cof the nonlinear derivative loss persists (3.4(g)): smooth compactly supported h_n with
  c = J = 0, bounded in the graph norms of T, L_ren and A_0, have ||N(h_n)|| >= b n; every v with L v = N(h_n) in the
  maximal domain has ||v|| >= b_L n. Verifier proof; independent audit PASS WITH REMARKS, recorded as V271 (16:39Z):
  THEOREM, in the semilinear graph scope. Not a nonexistence statement.
- V266 (16:28Z): transport alone on Z_2 and Z_cof (3.4(g)): at the source, DV(P) = diag(A_s, mu_s) with
  10 < A_s < 51/5, and the cusp profiles s_+^a phi(y/s_+^b), a = 1/A_s, b = mu_s/A_s, give smooth compact forcings
  with c = J = 0 spanning an infinite-dimensional subspace of the cokernel of T for alpha > 1/A_s, so for every
  alpha >= 1/10. Verifier proof; independent audit PASS WITH REMARKS, recorded as V272 (16:41Z): THEOREM, transport
  only. Not a statement about A_0 or
  L_ren, whose full source coupling changes the equation; it excludes only a Neumann series around T.

## 10. Status at 2026-10-28T12:04Z (updated 15:34Z, 15:57Z, 16:01Z, 16:20Z, 16:25Z, 16:36Z, 16:41Z, 16:43Z and 16:56Z)

The answers of section 0 stand at their stated scope. What had changed by 12:04Z is the role of Hoelder regularity
in the conditional existence theorem that was established.

- Regularity of the conditional profile. Theorem E (CONDITIONAL THEOREM, V178; the accompanying S2_L2_THEORY.md and the
  final report, section 6.2 item 6) is proved in Hilbert spaces: a variable-order Sobolev high space, of order 25/4
  with a factored cofactor on a sector about the vertical axis and of order 41/20 elsewhere, and weighted L^2 low
  spaces. The profile it produces is C^{1,alpha} on every compact subset of the punctured plane for every
  alpha < 1/20. This comes from the Sobolev embedding of order 41/20 into C^{1,alpha} on the cylinder, not from a
  Hoelder inverse. Near the vertical axis the factored component has at least five continuous derivatives.
- Compatibility with the x-axis example. The bulk order 41/20 is below 5/2 - 1/D (about 2.453), so the high space is
  compatible with the frozen-saddle example across the stable segment [0, x_P) of the x-axis (Prop F4, THEOREM for the
  frozen formula, V067). The exponent 1/20 is far below 1 - 1/D, the exponent attained by that example (it is locally
  C^{1,1-1/D}).
- Lipschitz velocity. The sufficient condition of section 0 is supplied by the high space:
  ||DW[g]||_inf + |c[g]| <= C_V ||g||_H (THEOREM, V073), which applies to the full high space through Lemma Emb
  (THEOREM, V177). C_V is finite and not computed.
- Is C^alpha(h_x) genuinely unnecessary? Derivative control beyond C^alpha of h and U[h] is necessary for a
  perturbative closure of the explicit semilinear map in every norm in which the explicit sequences of Lemmas N and N'
  stay bounded (THEOREM, V030). Its specific form C^alpha(h_x) is not needed as a norm: the
  established route imposes no Hoelder seminorm of h_x and obtains the Lipschitz velocity bound from the Sobolev high
  norm. That norm implies local C^alpha control of h_x for alpha < 1/20 by embedding. Necessity of a Lipschitz
  velocity is not claimed (V038).
- Admissible exponents. At 12:04Z the table of section 8 was unchanged except for one added row: the conditional profile of Theorem E,
  alpha < 1/20 on compact subsets of the punctured plane, by Sobolev embedding (V178).
- Origin (added 14:09Z and 14:12Z). The localized origin problem is now solved in C^alpha_2 for every alpha < 1,
  with the complete normalized coupling and the actual transport inside B_{delta/2} (S(e), V203 to V207), and with no
  derivative of h in the norm. The cubic coordinate J is not closable in that graph norm (V208), so this local
  inverse does not by itself give a normalized Hoelder theory, and the quadratic term is discontinuous at 0 from that
  graph norm to C^alpha_2 (Lemma N'', V211), so the perturbative (semilinear) fixed-point map about 0 does not close
  in it either; a quasilinear scheme, which moves U[h].grad into the transport, is not addressed by Lemma N''.
- Source (added 14:20Z). The actual variable source operator, unnormalized, is inverted on a
  neighbourhood of P in C^alpha_b intersected with L^2 for every alpha < 1 (3.1(iii), V213 to V215). With S(e) at the
  origin, both critical points now have local actual-coefficient Hoelder inverses, in different spaces and with the
  strain functional handled differently (bounded on C^alpha_2 at the origin, unbounded on C^alpha_b intersected with
  L^2 at the source). Patching them into a global inverse is OPEN.
- Global realization (3.4; added 14:58Z, updated 15:11Z to 15:34Z, 15:57Z and 16:01Z). Both cut-off local inverses map into the
  common target Y = E_2 intersected with L^2(w_gamma), gamma > 4k, which contains F0 (the uncut auxiliary inverses
  need not act on Y); the complete coupling is bounded and the full operator A_0 is closed on its maximal domain, on
  every such Y and on E_2 itself (V222, V224, V228; V241, V247). The specified cutoff parametrix error is not compact
  (V227; this does not exclude cancellation in a sum of patches), and A_0 is not even onto Y: T, L_ren and A_0 have
  infinite algebraic cokernel on E_2 and on every Y (THEOREM, V232, V234, V241, 3.4(e)): the global x^2 weight of
  the vertical seminorm is too weak at infinity. On the scaled far target Z the complete coupling is bounded, the full operator is
  closed for 2k - 1 < beta < k (THEOREM, V235, V244), and the exterior operator is invertible (THEOREM, V236, V242).
  Z is not a valid global target either (THEOREM, V243, V249: infinite algebraic cokernel, 3.4(g6)): ordinary far
  C^alpha permits
  transverse powers along the outgoing vertical axis. The target Z_2 with scaled quadratic control on every annulus
  carries the bounded coupling, the residual, the closed full operator and an actual exterior inverse (THEOREM, V245,
  V254). At a certified simple turning height on the vertical axis, T is not onto Z_2 for alpha > 1/2, and L_ren
  and A_0 are not onto Z_2 for alpha > 2/3 (THEOREM, V256, V262; alpha > 1/2 by V257, THEOREM,
  V265). Surjectivity for smaller
  alpha, a global inverse on Z_2 and the patching across the middle annuli are OPEN. The next candidate is the
  joint-cofactor target Z_cof of 3.4(g) (THEOREM, V261, V268): mapping, residual, closed domains and an
  exterior inverse, with the turning-height forcings excluded; its global inverse is OPEN, and the nonlinear map is
  not continuous in its graph topologies (THEOREM, V264, V271), so the nonlinear step needs a quasilinear scheme; T alone
  is not onto Z_2 or Z_cof for alpha > 1/A_s (THEOREM, V266, V272), which excludes a Neumann series around T but not an
  inverse of A_0.
- OPEN, and no longer on the critical path: a global Hoelder inverse of L, Hoelder estimates with numerical constants
  for the actual transport, and the Hoelder theory of the actual operator near the origin on a bounded domain or
  globally. Existence now reduces to
  hypotheses (I) and (S) of Theorem E, both stated in Hilbert norms.
- Labels. In section 9, CONFIRMED (Vnnn) is the verifier's verdict, and the statement then carries the label THEOREM.

# S2_CALPHA_THEORY.md: Hoelder estimates for h (Avenue II)

First version 2026-10-28T02:01Z (theory author), revised 2026-10-28T02:08Z after V022 to V025 and 2026-10-28T02:34Z after V028 to
V030, 02:54Z after V036 (C^4 hypothesis in S(d)), 03:08Z after V038 (Lipschitz velocity is sufficient, not shown necessary) and 04:46Z (C^{1,alpha} limit across the x-axis segment from Prop F4 of S2_L2_THEORY.md 6.2), and 12:04Z (section 10: status at the end of the run, after V178). Labels as in S2_L2_THEORY.md: THEOREM only after a verifier verdict, DERIVED
(proof written here, awaiting independent check), CONDITIONAL, NUMERICAL, OPEN, REFUTED. The verdict status of each
item is in section 9.

## 0. Summary of the answers

- Frozen origin saddle (section 2). Isotropic C^alpha has an inverse only for alpha < 1/D = 0.0469 (Proposition S(a)).
  This is sharp: for alpha > 1/D a smooth compactly supported forcing gives the bounded solution an exact |y|^{1/D}
  singularity along the whole incoming x-axis (S(b)). Anisotropic classes C^alpha_p work. In these classes the
  y-Hoelder seminorm is weighted by |x|^p, the order to which the data vanish on the outgoing y-axis. T_0^{-1} is
  bounded on C^alpha_p iff 1 + pA > D alpha, with explicit constants (S(c)). At p = 2 (the natural x^2 structure)
  this holds for every alpha < 1. The weighted sup version of Proposition N1 also holds: coercivity together with
  exclusion of x^2 y forces |x|^a weights with a > 2 (Proposition H0), so the y-axis jet is a coordinate here too.
- Coupling (section 1). U[h].grad rho_bar = -(rho_bar_y / 2) h + (Beurling-type principal value part). The local
  part damps where rho_bar_y > 0, in particular at the sources (rho_bar_y(P) = g = 29.75). The C^alpha norm of the
  principal value part is not its symbol supremum. No sharp Hoelder Garding inequality is available, so a Hoelder
  Lyapunov argument like Theorem R cannot be run with the same constants. Near the origin the coupling is small.
  Localized by a smooth cutoff chi_delta, it maps C^alpha_1 into C^alpha_1 with norm O(delta) (Proposition S(d),
  THEOREM, V028). So the frozen transport T_0 plus the localized coupling is invertible on the whole-plane class
  C^alpha_1 for alpha < (1 + A)/D = 0.5227 and delta small. This statement excludes the strain column and uses the
  frozen T_0, not the actual V. Above 0.5227 at the same alpha, an x-derivative of h must enter the norm.
- Source (section 3). The verifier-confirmed low-order theorem holds at the actual modal source rate mu < 1 (V029):
  the frozen coupled source inverse maps compact C^alpha input to C^alpha for every 0 < alpha < 1. The coupling is
  essential: without it the pure transport inverse at the source loses Hoelder regularity above 1/A (Remark 3.1).
- Infinity (section 3). In scale-invariant weighted Hoelder norms the window is 2k - 1 < gamma < k.
- Global C^alpha linear estimate: OPEN. No global Hoelder inverse is claimed.
- Nonlinear term (section 4). Lemma N is a rigorous obstruction (THEOREM in the repaired form of V030). For every
  0 < alpha < 1 and every space controlling
  the local C^alpha norms of h and U[h] near a regular axis point, h -> L^{-1} N(h) is unbounded on C^alpha-bounded
  sets. The sequence is explicit: two crossing plane waves of amplitude n^{-alpha} interact exactly into
  -n^{1-2alpha} sin(2ny), and the transport inverse does not regain y-derivatives where V is parallel to e_1.
  Lemma N' (THEOREM, V030, in a stronger form than the sketch) carries the failure over to the C^alpha graph norm:
  inputs with bounded graph norm have ||N||_{C^alpha} >= c n, and so do the solutions. Hence C^alpha(h_x) is
  not unnecessary for nonlinear closure. A sufficient condition for a quasilinear scheme is a Lipschitz transport
  velocity V + W[h]. Since DU[h] = Riesz^2(d_x h) exactly, this is the condition Riesz^2(d_x h) in L^infinity. It is
  implied by d_x h in C^epsilon (with decay); it is not equivalent to d_x h in C^alpha (verifier counterexample, V025).
  Necessity of a Lipschitz velocity is not claimed (V038 refuted the unrestricted necessity and equivalence wording of
  the closure document). Section 5 gives the compatible high/low formulation and its precise linear
  requirements (OPEN).
- First derivatives across the x-axis (S2_L2_THEORY.md 6.2, Prop F4; THEOREM for the frozen saddle, V067). For the frozen saddle, a smooth
  compactly supported source x^4 chi(x) psi(y) gives the exact solution -C x^4 sgn(y)|y|^{2 - 1/D} near the x-axis.
  So C^{1,alpha} across the stable manifold of the origin (the segment [0, x_P) of the x-axis, up to P) is attainable
  at most for alpha < 1 - 1/D = 0.9531, and this is the generic regularity there. A C^{1,eps} high norm (eps small) is
  compatible with it; a uniform C^{2,alpha} or H^s norm with s >= 5/2 - 1/D is not.

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
    C_c^infinity into C^alpha. Hence no isotropic C^alpha inverse of the frozen saddle exists above 1/D = 0.0469,
    whatever the norm on the data, unless the data satisfy the outgoing-axis condition M_F = 0.
(c) Anisotropic classes. If 1 + pA - D alpha > 0, then T_0^{-1} is bounded on C^alpha_p:
        ||h||_inf <= ||F||_inf,  [h]_x <= [F]_x / (1 + A alpha),  [h]_{y,p} <= [F]_{y,p} / (1 + pA - D alpha).
    The condition is sharp, including equality (V028). The test function first proposed here,
    F = |x|^p chi(x) psi(y), is not in C^alpha_p when 0 < p < alpha, because its x-Hoelder seminorm is infinite.
    The verifier's replacement is F = |x|^p sgn(y) |y|^alpha chi(x) chi(y/|x|^q), q = max(alpha - p, 0)/alpha, which
    belongs to C^alpha_p. For it the y-Hoelder quotient of T_0^{-1} F grows like int_0^T e^{-(1 + pA - D alpha)t} dt,
    which is unbounded in T when 1 + pA <= D alpha. (For 1 + pA < D alpha the original computation, valid when
    p >= alpha, shows T_0^{-1} F(x, y) ~ -C |x|^p y^{(1+pA)/D} for fixed small x != 0.)
    Thresholds: p = 0 gives alpha < 1/D = 0.047; p = 1 gives alpha < (1 + A)/D = 0.5227; p = 2 gives alpha < 1,
    because (1 + 2A)/D = 1. At p = 2 the threshold exponent is exactly 1 because x^2 y is the resonance. The
    forcing x^2 y chi(r) produces -(1/D) x^2 y log(1/|y|), the log solution of the jet row in Theorem O.
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
    (c[h]/3) G_bar, does not replace T_0 by the actual V, and gives no boundary realization on B_delta. The coupling
    does not map into C^alpha_p for p > 1 at the same alpha unless d_x U_1[h] is bounded, that is, unless d_x h is
    controlled (section 4). Above 0.5227 at the same alpha, an x-derivative of h must enter the norm.

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
For F = x^2 y chi(r): e^{-s} e^{-2As} e^{Ds} = 1, so T_0^{-1} F = -x^2 y |{s : |Phi_s X| in supp chi}| and the
measure is (1/D) log(1/|y|) + O(1).
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
a conjugacy with the extra mapping properties that would be needed is OPEN. So the Hoelder theory of the actual
transport near 0 is OPEN; only the frozen statements (a) to (d) are established.

Remark 2.2 (relation with Theorem O). The L^2 theory needs the factor |x|^{-2a} with a >= 5/2, an L^2 vanishing order of at least
2 on the y-axis (the endpoint a = 5/2 is admissible, V025). The sup theory needs a > 2 (Proposition H0). The
Hoelder seminorm theory needs only p > (D alpha - 1)/A in the y-Hoelder weight, which is below 2 for every alpha < 1,
but it does not see the x^2 y jet: J is not continuous on C^alpha_p.
A normalized C^alpha space for the S2 problem must combine a weighted sup part (a > 2, giving J as a coordinate) with
the seminorms of (c).

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
higher-order loss does not decide the low-order problem. General-mu sharpness, variable-coefficient patching, the
rank-one correction and global inversion are OPEN.

Remark 3.1 (the coupling is what saves the source; DERIVED). For the pure transport A s d_s + y d_y - 1 (g = 0), the
bounded inverse integrates along trajectories leaving P. For F = y chi(X) with chi = 1 near P, the solution is
h = -(y/A) log(1/|s|) + O(|y|) on the region |y|^A << |s| << 1. Its x-Hoelder quotient on dyadic scales
|s| ~ |y|^A is about |y|^{1 - A alpha}, so the C^alpha norm is infinite for alpha > 1/A = 0.0985. With g > A - 1 the
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
y(s) in [y_n, sqrt(2) y_n] on [0, s_0], so 2n y(s) in [pi/2, pi/sqrt(2)] and sin(2n y(s)) >= sin(pi/sqrt(2)) = 0.796.
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
constant: sin(pi/sqrt(2)) = 0.7957, so 0.796 is rounded upward; 0.79 is the correct lower constant. (4) Before
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
||L^{-1} N(h_1 + k_n)||_{X_gr} >= c n^{1 - alpha}. So perturbative closure fails in the C^alpha graph norm as well. This is
the usual derivative loss of quasilinear transport. The L^2 counterpart is the verified weak-graph discontinuity of N
in the diagnostic weighted H^1 norm (V019).

Answer to "is C^alpha(h_x) genuinely unnecessary?". For the linear theory at low order, yes: Proposition S(c), the
source theorem 3.1 and the far window all bound h in C^alpha (or C^alpha_p) by the forcing in the same class, without
h_x. For the nonlinear closure, no. Lemmas N and N' show that no perturbative scheme closes in C^alpha(h) or its graph
norm. The quasilinear scheme of section 5 uses a Lipschitz transport velocity V + W[h] (sufficient, not shown
necessary). Since DU[h] = Riesz^2(d_x h) exactly, this is the condition Riesz^2(d_x h) in L^infinity, for which
d_x h in C^epsilon is sufficient. The
precise loss is one derivative, transverse to V. The derivative that enters the velocity is d_x h only. The
contraction step (section 5) needs grad h in L^infinity, so both derivatives in the high norm. Only conormal
derivatives are needed across the axes: W_1 = 0 on {x = 0} and W_2 = 0 on {y = 0}, so
W.grad h = (W_1/x)(x h_x) + (W_2/y)(y h_y).

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
     (1 + g)/A = 3.03.
(Q3) Bilinear bound: ||W[d].grad h||_{X_lo} <= C ||d||_{X_lo} ||h||_{X_hi}. This needs grad h in L^infinity (with the
     conormal structure above) and U bounded on X_lo. It holds for standard weighted Hoelder or Sobolev pairs.
(Q4) Smallness: ||F_N(rho_bar)||_{Y_sigma} small and the constants of (Q1) to (Q3) certified.
Then the iterates are bounded in X_hi and contract in X_lo, and the limit solves F_N(rho_bar + h) = 0 in X_hi (by
weak-star compactness). This is a standard scheme and needs no Nash-Moser iteration, because the loss in (Q2) falls
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

Strain on the Hoelder classes C^alpha_p (THEOREM, V028). For h in C^alpha_p, oddness gives
|h(x, y)| <= [h]_{y,p} |x|^p |y|^alpha, and the near-origin strain integral over B_R is bounded by
[h]_{y,p} R^{p+alpha-1}/(pi (p + alpha - 1)) when p + alpha > 1. For p + alpha <= 1, c is unbounded on C^alpha_p:
for p + alpha < 1, h_e = e^{p+alpha} H(X/e) with a smooth annular class-P bump H, c[H] != 0, has bounded norm and
c[h_e] = e^{p+alpha-1} c[H]; at equality a degree-one angular function between radii e and 1 gives c ~ log(1/e). So a
Hoelder space carrying the rank-one term needs p + alpha > 1 or an added weighted sup condition near 0 (the cubic
sup norm of Proposition H0 suffices). The coupling class C^alpha_1 of (d) satisfies p + alpha > 1 for every alpha > 0.

## 7. What Avenue II establishes, and what it does not

Verified (THEOREM): Proposition H0 and S(a) to (c) (V028); S(d) in the smooth-cutoff form, with the whole-plane
inverse of T_0 + B_delta on C^alpha_1 (V028); the strain bound on C^alpha_p for p + alpha > 1 and its failure for
p + alpha <= 1 (V028); the source theorem 3.1 at mu = 1 (V013) and at the actual rate mu < 1 (V029); Lemma N and the
stronger Lemma N' (V030). DERIVED, not submitted as theorems: the plane-wave identity (4.2) (used inside V030); the
identity DU[h] = Riesz^2(d_x h); the quasilinear identity of section 5. REFUTED: the indicator form of S(d) and the
norm transfer of Remark 2.1. Not established: the Hoelder theory of the actual transport near 0; a global C^alpha
inverse of L; any C^alpha estimate with numerical constants; the high/low closure (Q1) to (Q4). No same-order global
C^alpha inverse is claimed.

## 8. Admissible alpha (summary)

| Piece | admissible alpha | space |
|---|---|---|
| frozen saddle, isotropic | 0 < alpha < 1/D = 0.0469 (sharp) | C^alpha_0 |
| frozen saddle, axis-weighted p | alpha < (1 + pA)/D (sharp); all alpha < 1 for p >= 2 | C^alpha_p |
| saddle plus localized coupling (frozen transport, no strain column) | alpha < (1 + A)/D = 0.5227 (verified) | C^alpha_1 |
| strain functional bounded | p + alpha > 1 (verified; fails for p + alpha <= 1) | C^alpha_p |
| frozen coupled source, actual rate mu < 1 | all 0 < alpha < 1 (verified, V029) | C^alpha_* compact input |
| pure transport source (no coupling) | alpha < 1/A = 0.0985 | (illustration) |
| infinity | all alpha, gamma in [2k - 1, k) | scaled C^alpha |
| nonlinear closure, perturbative | none (Lemma N, N') | any C^alpha-type |
| grad h across the x-axis segment [0, x_P), data even in x | alpha < 1 - 1/D = 0.9531 (sharp for the frozen saddle, Prop F4 of S2_L2_THEORY.md 6.2) | C^{1,alpha} |
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
- The C^{1,alpha} limit across the x-axis segment: Prop F4 of S2_L2_THEORY.md 6.2, THEOREM for the frozen saddle (V067);
  for the true operator OPEN.

## 10. Status at the end of the run (2026-10-28T12:04Z)

The answers of section 0 stand at their stated scope. What changed later in the run is the role of Hoelder regularity
in the conditional existence theorem that was established.

- Regularity of the conditional profile. Theorem E (CONDITIONAL THEOREM, V178; the accompanying S2_L2_THEORY.md and the
  final report, section 6.2 item 6) is proved in Hilbert spaces: a variable-order Sobolev high space, of order 25/4
  with a factored cofactor on a sector about the vertical axis and of order 41/20 elsewhere, and weighted L^2 low
  spaces. The profile it produces is C^{1,alpha} on every compact subset of the punctured plane for every
  alpha < 1/20. This comes from the Sobolev embedding of order 41/20 into C^{1,alpha} on the cylinder, not from a
  Hoelder inverse. Near the vertical axis the factored component has at least five continuous derivatives.
- Compatibility with the sharp x-axis limit. The bulk order 41/20 is below 5/2 - 1/D = 2.453, so the high space is
  compatible with the generic regularity across the stable segment [0, x_P) of the x-axis (Prop F4, THEOREM for the
  frozen saddle, V067). The exponent 1/20 is far below the frozen limit 1 - 1/D.
- Lipschitz velocity. The sufficient condition of section 0 is supplied by the high space:
  ||DW[g]||_inf + |c[g]| <= C_V ||g||_H (THEOREM, V073), which applies to the full high space through Lemma Emb
  (THEOREM, V177). C_V is finite and not computed.
- Is C^alpha(h_x) genuinely unnecessary? Derivative control beyond C^alpha of h and U[h] is necessary for a
  perturbative closure (Lemma N and N', THEOREM, V030). Its specific form C^alpha(h_x) is not needed as a norm: the
  established route imposes no Hoelder seminorm of h_x and obtains the Lipschitz velocity bound from the Sobolev high
  norm. That norm implies local C^alpha control of h_x for alpha < 1/20 by embedding. Necessity of a Lipschitz
  velocity is not claimed (V038).
- Admissible exponents. The table of section 8 is unchanged. One row is added: the conditional profile of Theorem E,
  alpha < 1/20 on compact subsets of the punctured plane, by Sobolev embedding (V178).
- OPEN, and no longer on the critical path: a global Hoelder inverse of L, Hoelder estimates with numerical constants
  for the actual transport, and the Hoelder theory of the actual operator near the origin. Existence now reduces to
  hypotheses (I) and (S) of Theorem E, both stated in Hilbert norms.
- Labels. In section 9, CONFIRMED (Vnnn) is the verifier's verdict, and the statement then carries the label THEOREM.

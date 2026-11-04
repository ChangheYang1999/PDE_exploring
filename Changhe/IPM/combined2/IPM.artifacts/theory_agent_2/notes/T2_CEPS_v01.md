# T2_CEPS_v01: the k-dependent weak constant Cbar of the AT-114 inverse on the reference ball (T2.4)

Version 1. Owner: the second theory agent. Written 2026-11-03T00:01Z. Plain-text mathematics as in T2_REV_v01. Paths are relative to the
combined2 root; files of this agent are given relative to theory_agent_2/. Requested by the coordinator 23:01Z item 6 and 23:19Z item 5
(after c_W at P-S2: C_eps_bar and Cbar). Built on theory_agent_1/research/qwg/QWG_v01.md (working draft, SHA256 1829c7b1... when
read at 2026-11-02T23:32Z; the theory auditor AT-150 to AT-152 on its snapshot ac379e61...). Definition CB was accepted by the first theory agent as
the shared definition (the first theory agent's team notes note 9, 2026-11-02T23:48Z), with the rate-domain qualification of note 10
(after the theory auditor AT-173); this note uses the rate form throughout.

## 1. Definitions and elementary facts

Setting: exactly that of AT-114 (the theory auditor research/sharp_full_garding/PROOF.md): 2 < q < 3, W = (1 + |X|^2/r0^2)^(sigma/2),
N(f) = ||J^q (W f)||_2, A_k h = (V + U[k]).grad h - h + U[h].grad rho, B_q(k), the reference ball
Kbar = {k real S1 : ||k||_2 <= Rbar, N(k) <= Mbar} (no ell constraint) and betaK = -sup over Kbar x R^2 of
lambda_max B_q(k). For real S1 Schwartz u put h = W^(-1) u, g = J^q u, G = ||g||_2 and
Q_k(u) = Re (J^q [W A_k W^(-1) u], g). At k = 0, A_0 = L and B_q(0) = N_q, so beta = -sup_X lambda_max N_q(X) >= betaK.

Definition CB (offered to the first theory agent at 2026-11-02T23:45Z). For a rate b > 0 and delta0 > 0,
    Cbar^opt(b, delta0; Kbar) := inf { C >= 0 : Q_k(u) <= -b G^2 + C ||h||^2 + (1 + delta0) N(k) ||grad h||_inf G
                                       for all k in Kbar and all real S1 Schwartz u },
with inf of the empty set = +infinity. C_eps_bar(eps; delta0) := Cbar^opt(betaK - eps, delta0; Kbar) for
0 < eps < betaK. "Cbar in (6)" is any number C >= Cbar^opt(b, delta0; Kbar) at the rate b = betaK - eps of (6), on one
reference ball containing every trial ball (AT-114, last paragraph).

Facts (CLAIMED; elementary, proofs below).
- (D1) Attainment. Cbar^opt = max(0, sup over k in Kbar, u != 0 of [Q_k(u) + b G^2 - (1 + delta0) N(k) ||grad h||_inf G]/||h||^2),
  and if it is finite it is itself admissible.
- (D2) Monotonicity. Cbar^opt is non-decreasing in b, non-decreasing in Kbar under inclusion (at fixed b), and
  non-increasing in delta0.
- (D3) k = 0 lower bound. Put C^opt(b) := Cbar^opt(b, delta0; {0}) (the k = 0 optimal constant at rate b; it does not
  depend on delta0 because N(0) = 0). Then Cbar^opt(b, delta0; Kbar) >= C^opt(b). When beta is the actual k = 0 margin and
  0 < b < beta, C^opt(b) = C_eps^opt(beta - b), the first theory agent's QWG_v01 section 1 constant (rate beta - eps); with b = betaK - eps
  this is AT-150's Cbar >= C_eps^opt(eps + beta - betaK). The slack form needs b < beta for the beta in use: with a chosen
  certified lower beta, betaK can exceed it (the theory auditor AT-173, which CONFIRMS the rate form and REFUTES betaK <= beta for an
  arbitrary certified lower beta). The rate form has no such restriction. More generally Cbar^opt(b, delta0; Kbar) >= sup
  over k in Kbar of the single-coefficient optimum C_k^opt(b, delta0).
- (D4) Subadditivity. If Q_k = Q^1_k + Q^2_k for every k in Kbar, Q^1_k(u) <= -b1 G^2 + C1 ||h||^2 + (1 + delta0) N(k) ||grad h||_inf G
  and Q^2_k(u) <= -b2 G^2 + C2 ||h||^2 on Kbar, then Cbar^opt(b1 + b2, delta0; Kbar) <= C1 + C2.
- (D5) Finiteness. Cbar^opt(b, delta0; Kbar) < infinity for every 0 < b < betaK and delta0 > 0 (AT-114 (1), a CONFIRMED
  implication under its retained hypotheses). Nothing here makes it explicit.
- (D6) Use in (6). AT-114 (2) and (6) hold with every admissible C in place of Cbar (their proofs use only (1)), so the
  best closure is obtained at C = Cbar^opt, and the AT-151 budget applies to Cbar^opt: the criterion
  N(F) + (b Cbar^opt)^(1/2) R <= Bcap must hold for the explicit route to close.

Proofs.
- (D1) For fixed (k, u) with u != 0 (so h != 0, W^(-1) > 0) the condition is C >= r(k, u), the displayed ratio; for
  u = 0 it reads 0 <= 0. The admissible set is [max(0, sup r), infinity), a closed half-line.
- (D2) Increasing b, or adding coefficients k, adds constraints or strengthens them; increasing delta0 weakens them.
- (D3) {0} is a subset of Kbar (||0||_2 = 0, N(0) = 0), so (D2) gives Cbar^opt(b, delta0; Kbar) >= Cbar^opt(b, delta0; {0}),
  and N(0) = 0 removes the tame term. At k = 0 the inequality is the first theory agent's at rate b (slack beta - b when b < beta). The sup
  over k is (D2) applied to {k}.
- (D4) Add the two inequalities. (D6) Read the AT-114 proof of (2): the Cauchy-Schwarz step uses (1) with its constant
  only through b x^2 <= D x + C L^2.

Remark on the parametrization. Parametrizing by the rate b, not by the slack eps, makes (D2) clean and lets the k = 0
constant of the first theory agent and the k-dependent constant be compared at equal b. betaK itself depends on Kbar; with eps fixed,
enlarging Kbar lowers betaK and the rate, so C_eps_bar(eps) is not monotone in Kbar in general.

## 2. Theorem CB-ZERO: at small Rbar the k-dependent weak constant is the k = 0 constant

Notation as in section 1; chi and Q_Lambda = 1 - chi(D/Lambda) as in AT-111 (chi real smooth radial, 0 <= chi <= 1,
1 on the unit ball, 0 outside radius 2). Fourier convention fhat(xi) = integral f(X) exp(-i X.xi) dX, so
||f||_2 = (2 pi)^(-1) ||fhat||_2. E(k, u) := Q_k(u) - Q_0(u) = Re (J^q [W (U[k].grad h)], g); E is linear in k because
A_k - A_0 = U[k].grad (the term U[h].grad rho does not depend on k).

Theorem CB-ZERO (CLAIMED; an implication from AT-112 and the definition of C^opt, plus the elementary Lemma LOW).
Let C_112 be the constant of AT-112 (1) (finite, depends on q, W and the cutoffs; not explicit). Put
    L(Lambda) := Rbar D_low(Lambda) + C_112 Mbar Lambda^(-(q-2)/4),
with D_low(Lambda) = D_1(Lambda) + D_2(Lambda) explicit (Lemma LOW). For every Lambda >= 1, rate b > 0 with
C^opt(b) < infinity, k in Kbar and real S1 Schwartz u,
    Q_k(u) <= -(b - L(Lambda)) G^2 + C^opt(b) ||h||^2 + (1 + C_112/Lambda) N(k) ||grad h||_inf G.
Hence, whenever b > L(Lambda),
    Cbar^opt(b - L(Lambda), C_112/Lambda; Kbar) <= C^opt(b),
and, in the first theory agent's slack notation with beta the actual k = 0 margin and b = beta - eps1,
    Cbar^opt(beta - eps1 - L(Lambda), C_112/Lambda; Kbar) <= C_eps^opt(eps1).
Proof. Split k = k_low + e, k_low = chi(D/Lambda) k, e = Q_Lambda k. Then Q_k(u) = Q_0(u) + E(k_low, u) + E(e, u).
Q_0(u) <= -b G^2 + C^opt(b) ||h||^2 by the definition of C^opt (the infimum is attained, D1). AT-112 (1) (stated for
every real k with finite N, no ball or ell constraint) gives |E(e, u)| <= (1 + C_112/Lambda) N(k) ||grad h||_inf G
+ C_112 N(k) Lambda^(-(q-2)/4) G^2 with no weak term, and N(k) <= Mbar. Lemma LOW gives |E(k_low, u)| <= Rbar D_low G^2,
since ||k_low||_2 <= ||k||_2 <= Rbar. Add. QED.

What it says. No compactness over Kbar, no matrix comparison and no k-dependent localization are needed: every
k-dependent cost goes into the rate (Rbar D_low and the high-frequency loss) and into the tame coefficient. The weak
constant is exactly the first theory agent's k = 0 constant. The price is the rate: CB-ZERO uses the k = 0 margin beta minus crude losses,
whereas AT-114 uses betaK, which keeps the principal part q Sym DU[k] - (U[k].grad log W) I of the perturbation
pointwise. With Rbar tiny (Rbar = R = ||F_*||_2/beta_0*, between 3.6e-5 and 3.2e-4 for the QWG_v01 section 2 inputs) the low loss Rbar D_low is
negligible for Lambda of order 1 to 3 (section 3); the high-frequency loss C_112 Mbar Lambda^(-(q-2)/4) is not small at
any moderate Lambda because (q-2)/4 = 1/40 at q = 21/10 (Lambda^(-1/40) = 0.94 at Lambda = 10). So CB-ZERO is
useful exactly when the high-frequency coefficient energy has a small explicit quadratic constant at moderate cut.
This isolates the one missing explicit estimate (section 4).

Lemma LOW (CLAIMED, elementary, explicit). Let Lambda >= 1, k real with ||k||_2 <= Rbar, a = U[k_low]. Then for real
Schwartz u (h = W^(-1) u, g = J^q u, G = ||g||_2)
    |E(k_low, u)| <= Rbar (D_1(Lambda) + D_2(Lambda)) G^2,
    S(Lambda) := (pi [(1 + 4 Lambda^2)^(q+1) - 1]/(q + 1))^(1/2),
    D_1(Lambda) := (2 pi)^(-1) q 2^((q-1)/2) S(Lambda),
    D_2(Lambda) := (2 pi)^(-3) 2^q S(Lambda) P,
    P := (2 pi)^2 sigma r0 2^(q/2 - 1) [pi/(2 r0^2) + 2^q Gamma((1+q)/2) Gamma((3+q)/2) r0^(-2-q)].
Proof.
- W (a.grad h) = a.grad u - phi u with phi = a.psi, psi = grad log W = sigma X/(r0^2 + |X|^2). So
  E(k_low, u) = Re (J^q (a.grad u), g) - Re (J^q (phi u), g).
- a is real, smooth, bounded with all derivatives bounded (Fourier support in |xi| <= 2 Lambda), and div a = 0. Hence
  Re (a.grad g, g) = -(1/2) integral (div a) |g|^2 = 0 and Re (J^q (a.grad u), g) = Re ([J^q, a.grad] u, g).
- ahat = m khat_low with |m| <= 1 (the symbol of U; |m|^2 = xi1^2/|xi|^2), so |ahat(z)| <= |khat(z)| 1_(|z| <= 2 Lambda)
  and integral <z>^q |ahat(z)| dz <= ||khat||_2 (integral over |z| <= 2 Lambda of <z>^(2q))^(1/2) = 2 pi Rbar S(Lambda).
- Commutator. ([J^q, a.grad] u)^(xi) = (2 pi)^(-2) integral ahat(z).i(xi - z) uhat(xi - z) [<xi>^q - <xi - z>^q] dz.
  With <x + y> <= 2^(1/2) <x> <y> and the mean value theorem, |<xi>^q - <xi - z>^q| <= q 2^((q-1)/2) |z| <z>^(q-1)
  <xi - z>^(q-1). So the integrand is at most q 2^((q-1)/2) [|z| <z>^(q-1) |ahat(z)|] [<eta>^q |uhat(eta)|],
  eta = xi - z, and Young (L1 * L2) gives ||[J^q, a.grad] u||_2 <= (2 pi)^(-2) q 2^((q-1)/2) (2 pi Rbar S) G
  = Rbar D_1 G, using |z| <z>^(q-1) <= <z>^q and ||<.>^q uhat||_2 = 2 pi G.
- Weight term. <xi>^q <= 2^(q/2) <z>^q <xi - z>^q gives ||J^q (phi u)||_2 <= (2 pi)^(-2) 2^(q/2) ||<.>^q phihat||_1 G, and
  |phihat| <= (2 pi)^(-2) |ahat| * |psihat| gives ||<.>^q phihat||_1 <= (2 pi)^(-2) 2^(q/2) (2 pi Rbar S) ||<.>^q psihat||_1.
  The Fourier transform of 1/(r0^2 + |X|^2) in R^2 is 2 pi K_0(r0 |xi|), so psihat_j = i sigma d_j (2 pi K_0(r0 |xi|)) and
  |psihat(xi)| = 2 pi sigma r0 K_1(r0 |xi|) (locally integrable, K_1(t) ~ 1/t). With (1 + r^2)^(q/2) <= 2^(q/2-1)(1 + r^q)
  (convexity, q >= 2) and integral_0^inf t^(mu-1) K_1(t) dt = 2^(mu-2) Gamma((mu-1)/2) Gamma((mu+1)/2) at mu = 2 and
  mu = 2 + q: ||<.>^q psihat||_1 <= P. Collect: ||J^q (phi u)||_2 <= Rbar D_2 G.
- Cauchy-Schwarz against g. QED.

Corollary CB-S (sandwich; CLAIMED, from D3 and CB-ZERO). For every Lambda >= 1 and b > L(Lambda),
    C^opt(b - L(Lambda)) <= Cbar^opt(b - L(Lambda), C_112/Lambda; Kbar) <= C^opt(b),
in slack notation C_eps^opt(eps1 + L(Lambda)) <= Cbar^opt(beta - eps1 - L(Lambda), C_112/Lambda; Kbar) <= C_eps^opt(eps1).
So the optimal k-dependent weak constant is fixed by the first theory agent's k = 0 function C^opt up to a shift L(Lambda) of the rate.
(The lower bound holds for every delta0, by D3; C^opt is non-decreasing in b.)

Corollary CB-B (no reference ball for the weak constant; CLAIMED). The constant C^opt(b) of CB-ZERO depends on
neither Rbar nor Mbar. Applied on the trial ball K (R, M) itself, with N(k) <= M, CB-ZERO gives AT-114 (1) with
    b(R, M) = b - R D_low(Lambda) - C_112 M Lambda^(-(q-2)/4),   Cbar = C^opt(b),   delta0 = C_112/Lambda,
and AT-114 (2) and (6) follow verbatim with this b (their proofs use only (1), D6). The AT-114 rule that Cbar must be
computed on one reference ball containing every trial ball is not needed for this constant; the M-dependence moves
into the rate b(R, M), which is explicit up to C_112.

## 3. Numbers (FLOAT evaluation of the closed forms of Lemma LOW; research/ceps/dlow.py, dlow.out)

The Bessel moment formula was checked by quadrature (mu = 2: pi/2; mu = 4.1: 5.250124). The bound P against direct
quadrature of ||<.>^q psihat||_1: P-S1 1968.2 against 1917.4, P-S2 390.29 against 383.76. Rbar = R = ||F_*||_2/beta_0*
for ||F_*||_2 = 1.006e-4 (quadratic part) and 5.91e-4 (complete F_*, the first theory agent QWG_v01 section 2) with beta_0* = 1.862 gives
Rbar = 5.4e-5 and 3.2e-4.

| tuple | Lambda | D_1 | D_2 | Rbar D_low at 5.4e-5 | at 3.2e-4 |
|---|---:|---:|---:|---:|---:|
| P-S1 (21/10, 1, 1/2) | 1 | 5.949 | 413.5 | 0.0227 | 0.134 |
| P-S1 | 2 | 39.78 | 2765 | 0.152 | 0.898 |
| P-S1 | 3 | 132.8 | 9232 | 0.506 | 3.00 |
| P-S2 (21/10, 7/5, 1) | 1 | 5.949 | 82.00 | 0.00475 | 0.0281 |
| P-S2 | 2 | 39.78 | 548.4 | 0.0318 | 0.188 |
| P-S2 | 3 | 132.8 | 1831 | 0.106 | 0.628 |

- The low part is cheap only at Lambda of order 1 (S(Lambda) grows like Lambda^(q+1)); D_2 (the weight term, two Peetre
  steps) dominates and can be sharpened; at P-S2 the weight term is five times smaller than at P-S1 (larger r0).
- At Lambda = 1 the high-frequency loss C_112 M and the tame coefficient 1 + C_112 are not small. With AT-112 as it
  stands, CB-ZERO is a structural statement, not a usable number.

## 4. The one missing estimate (OPEN) and why a small cut cannot be avoided cheaply (HEURISTIC orders)

Target HF-EXP. Explicit constants delta_hf, d_hf (and optionally a principal-retaining form) such that for Lambda of
order 1, all real k with N(k) < infinity and all real S1 Schwartz u,
    |E(Q_Lambda k, u)| <= (1 + delta_hf) N(k) ||grad h||_inf G + d_hf N(k) G^2,
or, keeping the principal part (B_q is affine in k),
    E(Q_Lambda k, u) <= integral (Rg)^T [q Sym DU[e] - (U[e].grad log W) I] (Rg) + d'_hf N(k) G^2 + (1 + delta_hf) N(k) ||grad h||_inf G.
With HF-EXP, the proof of CB-ZERO gives the weak constant Cbar = C^opt(b) at the explicit rate
b - Rbar D_low(Lambda) - d_hf M, tame coefficient 1 + delta_hf (or, in the second form, with the principal part bounded pointwise through
q ||Sym DU[e]||_inf, which carries the GN factor R^theta).
- Where AT-112 loses (the theory auditor sharp_tame_upper/PROOF.md (8) to (10), eta = (q-2)/2): the quadratic powers are -eta
  (||Da||_inf, principal-like, removed by the second form), -eta/2 (= mu^(-eta) at mu = Lambda^(1/2): the high-input
  part through the old KP-W constants), -1/2 - eta, -(1+eta)/2, -1/2. The binding term is the high-input one.
- The high-input loss is a C^(q-2) effect (HEURISTIC). In the paraproduct form J^q (f.v), f = W U[k], v = grad h, the
  high-high part R(f, v) has ||J^q R(f, v)||_2 <= N(k) (sum over 2^j > mu of ||Delta_j v||_inf^2)^(1/2) and
  ||Delta_j grad h||_inf ~ 2^(j(2-q)) G, so its size is of order N(k) mu^(-(q-2)) G^2 on inputs above mu, with no
  smallness from Rbar (sup norms of DU[k] carry only R^theta, theta = (q-2)/q = 0.048). A small quadratic constant
  d therefore forces mu >= (C M/d)^(1/(q-2)) = (C M/d)^10 at q = 21/10, and the low part then needs a cut above mu,
  where Rbar D_low grows like Lambda^(q+1) and any localization of the low compact family costs W(2 rho)^2 mu^(2q).
  This is why the AT-114 constant, made explicit along its own proof, is astronomically above the AT-151 budget
  (orders as in the first theory agent QWG_v01 section 6). For the bare remainder (after principal retention, with no tame term) the
  exponent q - 2 is sharp (the external referee t2-cbar1 packet example, section 5 below); for the full inequality (1), whose tame
  allowance has the same scale on those packets, whether the loss is intrinsic is OPEN.
- Consequence for planning (HEURISTIC). The usable explicit route is a moderate cut (Lambda of order 1) with an
  explicit, not small, quadratic constant d_hf and the M-dependent rate b(R, M) of CB-B. It is feasible only if d_hf M
  is well below the k = 0 rate b, roughly d_hf <= 1 at M = 0.2 to 0.4 (P-S1 actual margin beta = 0.7103192, QWG_v01
  section 2). The weak constant is then the first theory agent's C^opt(b), and the AT-151 budget applies to it unchanged.

## 5. Referee check: the external referee t2-cbar1 (collected; answer in an external referee answer, verification.txt)

Question scratch/an external referee answer (principal retention, the high-input loss, an explicit trade-off, the weight).
The answer is a claim; I checked the items below by hand and in scratch/ceps/referee_check.py (+ .out; exact sympy
identities and FLOAT arithmetic). No error found in the checked items.
- (a) Exact principal retention. With a = U[k], ell = grad log W, b = a.ell, P(a, g) = q integral (Rg)^T Sym Da (Rg)
  - integral b |Rg|^2: Q_k - Q_0 = E_W(a, u) and B_q(k) - B_q(0) = q Sym Da - b I, and the remainder
  F_W = E_W - P = Re([J^q, a.grad] u, g) - q integral (Rg)^T Sym Da (Rg) + integral b (|Rg|^2 - |g|^2) - Re([J^q, b] u, g)
  (div a = 0 and J^q(bu) = bg + [J^q, b]u). Checked. Retaining the whole principal part removes the matrix comparison
  exactly but gives no estimate of F_W; bounding P(a_high, g) separately costs q ||Da_high||_inf + ||ell||_inf ||a_high||_inf,
  with ||ell||_inf = sigma/(2 r0) (checked: 1 at P-S1, 7/10 at P-S2). Agrees with section 4 (the -eta term).
- (b) Bare-remainder obstruction (packet example). In the homogeneous unweighted form the trilinear symbol is
  (i m(p).r/2)[|s|^(2q) - |r|^(2q) - q(|s|^2 - |r|^2)|r|^(q-1)|s|^(q-1)], and the bracket is 2(|r||s|)^q [sinh(qz) - q sinh z]
  > 0 for |s| > |r| (z = log(|s|/|r|); checked symbolically, leading Taylor term (q^3 - q) z^3/3). The torus triad value
  (1/32)[13^q - 5^q - 8 q 65^((q-1)/2)] = 0.69269 at q = 21/10 (checked). Rescaled S1 Schwartz packets k_n, u_n with
  N(k_n) = M, G_n = 1 give F_W(k_n, u_n) >= c M n^(-(q-2)) at input frequency about sqrt5 n, for n large (threshold not
  numerical). I checked the scaling (k_n in the ball for large n, weight term smaller by n^(-2)) but not the sign
  bookkeeping of the four reflected packets in full. Consequence: for the bare remainder the exponent q - 2 is sharp, so
  section 4's high-input order is attained there. The packets have N(k_n) ||grad h_n||_inf G_n of the same order
  M n^(2-q), so they do not refute a sharp tame inequality with small quadratic constant.
- (c) Homogeneous explicit model. |F_q(k, u)| <= A_q K ||u||_2^(alpha/q) G^(2 - alpha/q) (alpha = q - 2, K = ||D^q k||_2,
  unweighted), and |F_q| <= D_q K mu^(-alpha) G^2 if uhat vanishes on |xi| < mu. At q = 21/10: T_q = 7.23316,
  L_q = 0.64453, A_q = 11.6091, D_q = 9.60539 (recomputed). Young with theta = alpha/(2q) = 1/42 gives the comparison
  weak constant (1/42)(41/42)^41 (A_q K)^42 d^(-41), prefactor 0.0088648 (recomputed): this is the precise form of the
  (C M)^(2q/(q-2)) d^(1 - 2q/(q-2)) order of section 4, and it is in ||u||_2, not ||h||_2 (the weighted version is not
  proved). Checked: the split |p| >= |r|/2 (with |s| <= 3|p|) and |p| < |r|/2 (Taylor, z <= |p|/|r|, third derivative
  <= 2 q^3 (3/2)^q); the factor 13/8.
- (d) Bounded optimal constant as d -> 0. Trivial: the extra slack d >= 0 only weakens the inequality. A d^(-41)
  divergence is a property of a construction, not of the optimal constant. Agree.
- (e) Weight issue (question 4). For centrally odd f (all of S1) and 1 <= sigma < 2, ||W U[f]||_2 <= B_sigma ||W f||_2 with
  B_sigma = 2^((sigma-1)/2) (1 + 2 sigma/(2 - sigma)^2)^(1/2), independent of r0; B_1 = sqrt3, B_(7/5) = 3.40329.
  Checked: the log-polar symbols (Hessian |z(z-1)|^2 + 2 m^2 |z-1|^2 + |z - m^2|^2, Laplacian z^2 - m^2, z = 1 - sigma + i tau),
  the identity N_m - D_m = 2 sigma [tau^2 + (2 sigma - 1) m^2 + (1 - sigma)^2] (sympy), the bounds bracket <= sigma^2 S
  (uses sigma >= 1 and (sigma - 1)^2 (m^2 - 1) >= 0) and D_m >= sigma^2 (2 - sigma)^2 S^2 (uses odd |m| >= 1), and the
  weight comparison 1 + s^(2 sigma) <= (1 + s^2)^sigma <= 2^(sigma-1)(1 + s^(2 sigma)). So W U[k_low] is in L^2 on S1, and my
  question 4 is settled. Lemma LOW does not need it (it works with the unweighted a = U[k_low] and phi = a.ell).
- (f) Unresolved by the referee: an explicit weighted principal-retaining inequality with the sharp tame coefficient;
  no constant below the AT-151 budget (1e4 to 1e6) is certified or excluded. This is HF-EXP of section 4.

Use in this note: (a) and (e) are adopted as CLAIMED (checked); (b) and (c) support the HEURISTIC orders of section 4
and are recorded as CLAIMED statements about the bare remainder only.

## 6. Status labels

| ID | statement | label |
|---|---|---|
| T2-CB-DEF | Definition CB and facts D1 to D6 | CLAIMED (elementary) |
| T2-CB-ZERO | Theorem CB-ZERO and Lemma LOW | CLAIMED (implication from AT-112 and the definition of C_eps^opt; Lemma LOW elementary) |
| T2-CB-S | sandwich C^opt(b - L) <= Cbar^opt(b - L, C_112/Lambda; Kbar) <= C^opt(b) | CLAIMED |
| T2-CB-B | ball-independent weak constant, rate b(R, M) | CLAIMED |
| T2-CB-TAB | section 3 table | FLOAT evaluation of explicit closed forms (upper bounds once the formulas are confirmed) |
| T2-HF-EXP | explicit high-frequency estimate at moderate cut | OPEN |
| T2-HF-LOSS | high-input loss of order N(k) mu^(-(q-2)) in the full inequality (1) | HEURISTIC |
| T2-referee-A | exact principal-retention identity (section 5 (a)) | CLAIMED (checked) |
| T2-referee-B | bare-remainder exponent q - 2 sharp (packets; not a bound for the full inequality) | CLAIMED (scaling checked, sign bookkeeping partly) |
| T2-referee-C | homogeneous unweighted A_q, D_q and the d^(-41) comparison cost | CLAIMED (constants recomputed, FLOAT) |
| T2-referee-E | odd weighted bound ||W U[f]||_2 <= B_sigma ||W f||_2, 1 <= sigma < 2 | CLAIMED (checked) |

## 7. Requests

- The first theory agent: thank you for notes 9 and 10 (Definition CB accepted; rate form after AT-173). Please quote CB-ZERO and CB-S
  in QWG_v02 and theory_v03 T2.4 in the rate form: your C^opt(b) is also the k-dependent weak constant, at the rate loss
  L(Lambda) and the tame coefficient 1 + C_112/Lambda. Section 5 (e) (odd weighted bound B_sigma) may be useful for your
  far-field work.
- The theory auditor: audit D1 to D6, Theorem CB-ZERO (the split, the use of AT-112 (1) with no weak term, the attained infimum) and
  Lemma LOW (constants D_1, D_2, P; the K_0/K_1 transform; the two Peetre steps). research/ceps/dlow.py is FLOAT.
- The theory auditor: also audit section 5 (e) (the external referee t2-cbar1 odd weighted bound) if it is to be used by the first theory agent.
- The coordinator: the k-dependent weak constant reduces to the k = 0 one (the first theory agent). The open explicit item for the AT-114
  closure is now HF-EXP (an explicit high-frequency coefficient estimate at moderate cut), not a compactness constant.

## 8. Files

- research/ceps/dlow.py, research/ceps/dlow.out (Lemma LOW numbers; FLOAT).
- scratch/ceps/plan.md (working notes), scratch/an external referee answer (referee question), an external referee answer and
  verification.txt (referee answer), scratch/ceps/referee_check.py (+ .out; checks of section 5).

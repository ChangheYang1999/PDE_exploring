# T2_QIDZO_v01: Lemma QID (the low-band form as a spatial integral with a zero-mean density) and Proposition ZO (the low-band constant has a zeroth-order lower limit under dilation), proofs for the theory auditor

Agent the second theory agent, written 2026-11-03 (file created 23:24Z); frozen 2026-11-03T23:24:25Z. Recipient: the theory auditor (the coordinator X7 item 5(d): "its proofs of Lemma QID and
Proposition ZO for the theory auditor"); cc the first theory agent, the coordinator. Status: both CLAIMED. Paths: notes/ relative to the agent directory, code/
and runs/ relative to research/h4/far009/ of agent the second theory agent.

Source: notes/T2_FAR_C2_PLAN_v01.md section 2 (SHA256 d9604af8f6abb707745cf37e42328a2403d919b6c08a7443b3703237c874ec9e).
This note restates both results with their full hypotheses and complete proofs. Changes against that source:
- the Fourier moments are written M_s here, not D_s, so they are not confused with the energies D_s = ||(-Delta)^(s/2) a||_2
  of Theorem CS-B;
- the scaling of those energies is added in Proposition ZO (c): D_1 is dilation invariant, so the consequence is stated
  for the energies with s > 1 only;
- Step 2 of the proof of Lemma QID (the Parseval identity for a triple product) is written out.
No statement of the source is strengthened. Nothing here changes Theorem CS-B, Corollary CS-W or the AE plan
(notes/T2_FAR_AE_PLAN_v01.md); Proposition ZO concerns bounds of A_low by size quantities of the coefficient alone,
and the AE plan bounds A_low for one explicit field.

## 1. Setting

- R^2, q real (the application uses q = 21/10; neither proof uses a property of q). f^(xi) = int f(x) e^(-i x.xi) dx, so
  int f conj(g) dx = (2 pi)^-2 int f^ conj(g^) d xi.
- <xi> = (1 + |xi|^2)^(1/2), w = xi/|xi|, w' = eta/|eta|, zeta = xi - eta, and (T2_FAR_v02 section 2.3)
      Ktil(xi, eta) = <xi><eta> |w - w'|^2 + (<xi>^q - <eta>^q)^2 (<xi><eta>)^(1 - q),
      S[k](u) = (2 pi)^-4 int int k(xi, eta) u^(eta) conj(u^(xi)) d xi d eta.
- Lambda^s is the Fourier multiplier <xi>^s, Lambda = Lambda^1, and R_j (j = 1, 2) the Riesz transform with symbol
  -i xi_j/|xi|.
- S1 is the class of real functions that are even in x_1 and odd in x_2 (T2_CWS2_v01 section 1; the parity class of
  the second numerics agent results/N2_BAND_PRICE_013_v02.md section 3.2).
- Band constant (T2_FAR_v02 section 2.3): for real a with a^ in L^1 and K' > 0, A_low(K'; a) is the supremum of
  S[-(1/2) a^ K](f)/||J^-1 f||^2, K = Ktil/(<xi><eta>), J = Lambda, over nonzero f in L^2 of class S1 with f^ = 0 a.e. on
  |xi| > K'. J and J^-1 keep reality, the class S1 and the Fourier support, and S[-(1/2) a^ K](J u) =
  S[-(1/2) a^ Ktil](u). So, with u = J^-1 f,
      A_low(K'; a) = sup { S[-(1/2) a^ Ktil](u)/||u||^2 : 0 != u in L^2, u of class S1, u^ = 0 a.e. on |xi| > K' }.   (1.1)
- osc(b) = sup b - inf b for real bounded b. SC(a) = sup_x max(0, (1/2)[(q^2 - 1) lambda_max Hess a(x) + Delta a(x)])
  (T2_FAR_v02 section 2.3). M_s(a) = int |a^(zeta)| |zeta|^s d zeta and D_s(a) = ||(-Delta)^(s/2) a||_2 for s > 0.

## 2. Lemma QID (CLAIMED)

Statement. Let a be real and bounded with a^ in L^1, and let u be real in L^2 with u^ = 0 a.e. outside a bounded set.
Put
    rho_u = sum_(j=1,2) (Lambda R_j u)^2 - (Lambda^(1+q) u)(Lambda^(1-q) u).
Then rho_u is in L^1, int rho_u dx = 0, and
    S[-(1/2) a^ Ktil](u) = int a rho_u dx.
In particular S[-(1/2) a^ Ktil](u) = int (a - c) rho_u dx for every real constant c.

Proof.
Step 1 (the factors). Let u^ vanish outside |xi| <= B. Then u^ is in L^1 (Cauchy-Schwarz on the disk). The symbols
p(xi) = <xi>^s and p_j(xi) = -i xi_j <xi>/|xi| (the symbol of Lambda R_j) are bounded on |xi| <= B, so P u := F^-1(p u^)
is in L^2 with (P u)^ in L^1 and L^2, and P u is bounded and continuous. P u is real: u real gives
u^(-xi) = conj(u^(xi)), and p(-xi) = conj(p(xi)) for both symbols (<xi>^s is even and real, p_j is odd and purely
imaginary), so (P u)^(-xi) = conj((P u)^(xi)).

Step 2 (Parseval for a triple product). Let g, h be in L^2 with g^, h^ in L^1 and L^2. Since a is bounded, a g is in
L^2, and since a^ is in L^1, (a g)^ = (2 pi)^-2 a^ * g^ (both sides are in L^2 by Young, L^1 * L^2 into L^2, and they agree
as distributions: a is the inverse transform of a^ almost everywhere, and the convolution theorem holds for a^ in L^1,
g^ in L^1). Parseval gives
    int a g conj(h) dx = (2 pi)^-2 int (a g)^ conj(h^) d xi = (2 pi)^-4 int int a^(xi - eta) g^(eta) conj(h^(xi)) d eta d xi,
and the double integral converges absolutely: int int |a^(xi - eta)| |g^(eta)| |h^(xi)| <= ||a^||_1 ||g^||_2 ||h^||_2
(Schur test with the kernel |a^(xi - eta)|).

Step 3 (kernels). For two of the multipliers of Step 1, with symbols p and p', Step 2 with g = P u and h = P' u (P' u is
real, so conj(P' u) = P' u) gives
    int a (P u)(P' u) dx = S[k](u),   k(xi, eta) = a^(xi - eta) p(eta) conj(p'(xi)).
- P = P' = Lambda R_j: p_j(eta) conj(p_j(xi)) = (-i eta_j <eta>/|eta|)(i xi_j <xi>/|xi|) = <xi><eta> xi_j eta_j/(|xi||eta|).
  The sum over j is <xi><eta> w.w'.
- P = Lambda^(1+q), P' = Lambda^(1-q): k = a^(xi - eta) <eta>^(1+q) <xi>^(1-q). Exchanging the roles of P and P' gives the
  same spatial integral with the kernel a^(xi - eta) <eta>^(1-q) <xi>^(1+q), so the form is S of the average,
  (1/2) a^(xi - eta) (<xi>^(1+q) <eta>^(1-q) + <xi>^(1-q) <eta>^(1+q)).
Hence int a rho_u dx = S[a^ k_0](u) with
    k_0(xi, eta) = <xi><eta> w.w' - (1/2)(<xi>^(1+q) <eta>^(1-q) + <xi>^(1-q) <eta>^(1+q)).

Step 4 (algebra). Off the null set {xi = 0} union {eta = 0}, |w - w'|^2 = 2 - 2 w.w', and
    (<xi>^q - <eta>^q)^2 (<xi><eta>)^(1-q) = <xi>^(1+q) <eta>^(1-q) + <xi>^(1-q) <eta>^(1+q) - 2 <xi><eta>.
Adding, Ktil = -2 <xi><eta> w.w' + <xi>^(1+q) <eta>^(1-q) + <xi>^(1-q) <eta>^(1+q) = -2 k_0. So
S[-(1/2) a^ Ktil](u) = S[a^ k_0](u) = int a rho_u dx.

Step 5 (mean zero). rho_u is a finite sum of products of L^2 functions, hence in L^1, and by Plancherel
    int rho_u dx = sum_j ||Lambda R_j u||^2 - <Lambda^(1+q) u, Lambda^(1-q) u>
                 = (2 pi)^-2 int |u^(xi)|^2 <xi>^2 (xi_1^2/|xi|^2 + xi_2^2/|xi|^2 - 1) d xi = 0.
The last statement follows since int c rho_u dx = 0. QED.

FLOAT check (not a proof): code/c1/qid_check.py (SHA256 53d1c030f1086eb3cd738c17d63ac32c2281c7575fb2955a490ff9954051112f)
compares both sides of the identity on the torus for random real a and u with Fourier modes |k| <= 6 (grid 64^2):
relative difference 1.22e-15, int rho_u = -4.5e-12 against int u^2 = 5058.71 (runs/qid_check_2032.log, SHA256
b296624df78ff1aea37beb2dc87f70e072c9732b13079bf267b0ef05394a7439).

## 3. Proposition ZO (CLAIMED)

Notation. For real u in L^2 with u^ = 0 a.e. outside a bounded set put rho^0_u = sum_j (R_j u)^2 - u^2 (it is in L^1 and
has integral 0 by the computation of Step 5 with <xi> replaced by 1), and for real bounded b and u != 0 put
Z(b, u) = int b rho^0_u dy/||u||^2.

Statement. Let q be real and K' > 0.
(a) For every real Schwartz function b and every nonzero u in L^2 of class S1 with u^ = 0 a.e. on |xi| > 1,
        liminf_(eps -> 0+) A_low(K'; b(eps .)) >= Z(b, u).
(b) There are a real radial Schwartz function b > 0 and u as in (a) with Z(b, u) > 0.
(c) For real Schwartz b and eps > 0: SC(b(eps .)) = eps^2 SC(b), M_s(b(eps .)) = eps^s M_s(b) and
    D_s(b(eps .)) = eps^(s-1) D_s(b). So SC, every M_s (s > 0) and every D_s with s > 1 tend to 0 as eps -> 0, while
    D_1 is constant.
(d) For every real bounded b and every real u in L^2 with u^ = 0 a.e. outside a bounded set,
    int b rho^0_u dy <= osc(b) ||u||^2.

Proof.
(a) Let 0 < eps <= min(1, K') and u_eps(x) = u(eps x). u_eps is real, of class S1 (dilation commutes with the coordinate
reflections), and u_eps^(xi) = eps^-2 u^(xi/eps) vanishes a.e. on |xi| > eps, hence on |xi| > K'. b(eps .) is real,
bounded, with Fourier transform eps^-2 b^(./eps) in L^1. By (1.1) and Lemma QID,
    A_low(K'; b(eps .)) >= int b(eps x) rho_(u_eps)(x) dx/||u_eps||^2.
For a multiplier P with symbol p, (P u_eps)(x) = (P_eps u)(eps x), where P_eps has the symbol p(eps zeta): the Fourier
transform of the right side is eps^-2 p(eps (xi/eps)) u^(xi/eps) = p(xi) u_eps^(xi). R_j has a symbol homogeneous of
degree 0, so R_j,eps = R_j; Lambda^s gives M^s_eps with the symbol <eps zeta>^s. Hence
rho_(u_eps)(x) = rho_eps(eps x), with
    rho_eps = sum_j (M^1_eps R_j u)^2 - (M^(1+q)_eps u)(M^(1-q)_eps u).
The substitution y = eps x and ||u_eps||^2 = eps^-2 ||u||^2 give
    int b(eps x) rho_(u_eps)(x) dx/||u_eps||^2 = int b rho_eps dy/||u||^2 =: Q_eps.
For |zeta| <= 1 and eps <= 1, the mean value theorem for t -> (1 + t)^(s/2) on [0, eps^2] gives
|<eps zeta>^s - 1| <= C_s eps^2 with C_s = (|s|/2) 2^(|s|/2). By Plancherel, ||M^s_eps v - v||_2 <= C_s eps^2 ||v||_2 for
every v whose Fourier transform vanishes outside the unit disk, which holds for u and for R_j u. With
||f g - f_0 g_0||_1 <= ||f - f_0||_2 ||g||_2 + ||f_0||_2 ||g - g_0||_2, rho_eps -> rho^0_u in L^1, and since b is bounded,
|Q_eps - Z(b, u)| <= ||b||_inf ||rho_eps - rho^0_u||_1/||u||^2 -> 0. So liminf A_low(K'; b(eps .)) >= lim Q_eps = Z(b, u).
(b) Let psi be smooth on R, psi >= 0, psi > 0 on [0, 1/4] and psi = 0 on [1, infinity), and let w be the function with
w^(xi) = psi(|xi|^2). w is real, radial and Schwartz. Put u = d_2 w, so u^(xi) = i xi_2 psi(|xi|^2): u is real, nonzero,
even in x_1 and odd in x_2 (class S1), and u^ vanishes outside the unit disk. u^, (R_1 u)^ and (R_2 u)^ are in L^1, so
u, R_1 u and R_2 u are bounded and continuous, and
- u(0) = 0, since u is odd in x_2;
- R_1 u(0) = (2 pi)^-2 int xi_1 xi_2 psi(|xi|^2)/|xi| d xi = 0, since the integrand is odd in xi_1;
- R_2 u(0) = (2 pi)^-2 int xi_2^2 psi(|xi|^2)/|xi| d xi > 0, since the integrand is >= 0 and positive on an open set.
So rho^0_u is bounded and continuous with rho^0_u(0) = (R_2 u(0))^2 > 0. For b_sigma(y) = exp(-|y|^2/sigma^2),
    sigma^-2 int b_sigma rho^0_u dy = int exp(-|z|^2) rho^0_u(sigma z) dz -> pi rho^0_u(0) > 0   (sigma -> 0+)
by dominated convergence. So Z(b_sigma, u) > 0 for every small enough sigma > 0, and b_sigma is real, radial,
Schwartz and positive.
(c) Hess(b(eps .))(x) = eps^2 (Hess b)(eps x) and Delta(b(eps .))(x) = eps^2 (Delta b)(eps x); the supremum over x is
unchanged by the dilation and max(0, .) is positively homogeneous, so SC(b(eps .)) = eps^2 SC(b). With
(b(eps .))^(zeta) = eps^-2 b^(zeta/eps) and zeta = eps v,
    M_s(b(eps .)) = int eps^-2 |b^(zeta/eps)| |zeta|^s d zeta = eps^s M_s(b),
    D_s(b(eps .))^2 = (2 pi)^-2 int |zeta|^(2s) eps^-4 |b^(zeta/eps)|^2 d zeta = eps^(2s-2) D_s(b)^2.
(d) int b rho^0_u = int b sum_j (R_j u)^2 - int b u^2 <= sup b sum_j ||R_j u||^2 - inf b ||u||^2 = osc(b) ||u||^2, since
both densities are >= 0 and sum_j ||R_j u||^2 = ||u||^2 (Plancherel). QED.

Consequence (CLAIMED, from (a) to (c)). Let Sigma be a finite subset of (0, infinity) and Sigma' a finite subset of
(1, infinity). There is no function Phi with Phi(x) -> 0 as x -> 0 such that
    A_low(K'; a) <= Phi(SC(a), (M_s(a))_(s in Sigma), (D_s(a))_(s in Sigma'))
for every real radial Schwartz function a: take b and u of (b); along a = b(eps .) every argument
tends to 0 by (c), while liminf A_low(K'; a) >= Z(b, u) > 0 by (a). So a slowly varying part of the coefficient is charged
by the low band at zeroth order, between the Z-type lower values of (a) and osc(b) of (d). This is the precise form of
the obstacle that the second numerics agent noted (results/N2_BAND_PRICE_013_v02.md sections 2 and 3.1) for a lemma that would charge the tail
a_t of route F-a through its derivatives alone, and it is why the C2 plan (notes/T2_FAR_C2_PLAN_v01.md) keeps the
certified tail charge OMF(a_t) as a separate zeroth-order term. It does not exclude a treatment that uses the sign or the
explicit form of the coefficient, such as the AT-707 band bound applied to one explicit field.

Relation to earlier audits. The theory auditor showed (AT459 to AT465, exchange v165 and v166) that the form without a frequency
restriction is invariant under a common dilation of coefficient and test, so positive-order moment and derivative budgets
cannot lower the unrestricted constant. Proposition ZO is the corresponding statement for the band |xi| <= K', where the
form is not dilation invariant (the weights <xi>^s) and only its zeroth-order limit survives.

## 4. Files

- notes/T2_FAR_C2_PLAN_v01.md d9604af8f6abb707745cf37e42328a2403d919b6c08a7443b3703237c874ec9e (source of both statements)
- code/c1/qid_check.py 53d1c030f1086eb3cd738c17d63ac32c2281c7575fb2955a490ff9954051112f (FLOAT check only)
- runs/qid_check_2032.log b296624df78ff1aea37beb2dc87f70e072c9732b13079bf267b0ef05394a7439

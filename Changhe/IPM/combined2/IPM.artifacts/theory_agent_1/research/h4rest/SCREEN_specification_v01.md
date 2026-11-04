# SCREEN_specification_v01: normalizations for the FLOAT screen of the H4 rest term at C2-N1-013 (the first theory agent)

Written 2026-11-04 in a work session for coordinator note 09:02Z item 2(b), which assigns core 44 (the first numerics agent) a FLOAT screen in
the normalizations of sections 4 and 5 of H4REST_PLAN_v01 and asks the first theory agent and the second theory agent to answer questions about them.
This file states those normalizations in advance. It adds no bound; the screen enters no certificate. The two
lemmas cited are elementary and CLAIMED (Lemma MOM of the second theory agent's T2_H4_v01, and the inversion bound of item 0).

## 0. Conventions

- Setting of T2_H4_v01 section 2: P-S1 (q = 21/10, sigma = 1, r0 = 1/2), self-similar variable X in R^2, V = cX + ubar
  with div ubar = 0, S = Sym D ubar (symmetric, traceless; the field of the cover bound ||Sym Du||_op <= 137/125),
  rhobar the background density. The background is that of C2-N1-013.
- Fourier transform f^(zeta) = int e^(-i X.zeta) f(X) dX. Moments are m_k(f) = (2 pi)^(-2) int |zeta|^k |f^(zeta)|
  d zeta, with the Euclidean norm for vectors and the operator norm for matrices.
- Inversion bound (CLAIMED, elementary): if P is a homogeneous polynomial of degree k with |P(zeta)| <= |zeta|^k, then
  |P(grad) f(X)| <= m_k(f) at every X. Examples: (e.grad)^k with e a unit vector, Delta (k = 2), Delta^2 (k = 4).
  So a sampled pointwise sup is a lower bound of the moment, up to the sampling error.
- Lemma MOM (T2_H4_v01, eps = 1): m_k(f) <= (4 pi)^(-1/2) || |D|^k (1 - Delta) f ||_2, with the Frobenius norm for
  matrices and || |D|^3 F ||_2 = ||grad Delta F||_2, || |D|^4 F ||_2 = ||Delta^2 F||_2. An L^2 norm by quadrature
  is an upper of the moment, up to the quadrature and truncation error; it is finite only if the derivatives decay.

## 1. The quantities (all FLOAT; report each with its resolution and a convergence check)

Each item gives the definition, then the pointwise lower (report the sampled sup and its location), then the L^2
upper (report the quadrature value and the truncation radius).
- u_3 = m_3(ubar). Lower: sup over X and unit e of |(e.grad)^3 ubar(X)|. Upper: (4 pi)^(-1/2)
  ||grad Delta (1 - Delta) ubar||_2.
- M2(S) = m_2(S). Lower: sup over X of the larger of ||Delta S(X)||_op and the max over e of ||(e.grad)^2 S(X)||_op.
  Upper: (4 pi)^(-1/2) ||Delta (1 - Delta) S||_2.
- M4(S) = m_4(S). Lower: sup over X of the larger of ||Delta^2 S(X)||_op and the max over e of
  ||(e.grad)^4 S(X)||_op. Upper: (4 pi)^(-1/2) ||Delta^2 (1 - Delta) S||_2.
- M_S = 3 M2(S) + 2 M4(S), the moment of Lemma TIS-FG. Lower and upper: 3 and 2 times those above.
- r_3 = m_3(grad rhobar) = m_4(rhobar). Lower: sup over X of the larger of |Delta^2 rhobar(X)| and the max over e of
  |(e.grad)^3 grad rhobar(X)|. Upper: (4 pi)^(-1/2) ||Delta^2 (1 - Delta) rhobar||_2.

M_S = (2 pi)^(-2) int |zeta|^2 (1 + 2 <zeta>^2) ||S^(zeta)||_op d zeta = 3 M2(S) + 2 M4(S) exactly. For a real
symmetric traceless 2 x 2 matrix, ||A||_op = (A_11^2 + A_12^2)^(1/2). If a quantity cannot be reached (for example
because ubar or rhobar does not decay and an L^2 norm diverges), state that instead of substituting another quantity
(coordinator 09:02Z item 2(b)); the sampled sup over the outer annuli of the integrand is then the useful record.

## 2. What each value decides (thresholds from H4REST_PLAN_v01; exact budget arithmetic, rounded)

- u_3, Lemma HI' route for the high part of T_IS + C_tr, at U = 8(2c - 1) and the plan of record (11/20, 72): the
  route can use the cut mu_r only if u_3 <= R mu_r^2/(phi x 10.67804022), phi = (1 + 5^(1/2))/2, with
  R = 0.000938706156 at the inner regional lower of the matrix rate and R = 0.006302110849 at the ceiling
  c + 1 - q. At mu_r = 72 this is u_3 <= 0.2817 and u_3 <= 1.891; at 100, 0.5433 and 3.648; at 200, 2.173 and 14.59
  (plan section 4). A lower above a value excludes that cut on this route; an upper below it shows only that the u_3
  term fits, with the tail term and the other pieces still to be paid from the same R.
- M_S, Lemma TIS-FG route (T_IS paid from the free gain (B) = 0.0127320502923 alone): needs M_S <= 0.0121257621831
  (= (B)/(q/2)). A lower above it excludes this route for the whole T_IS; an upper below it shows that T_IS fits in
  (B), which the other pieces may also need.
- r_3: no threshold yet. C_vs1 and C_vs3 have no written NE form (T2_H4_v01 section 5, NE-vs OPEN); the value
  orients that work only.

## 3. Requested output

For each quantity of section 1: the two FLOAT values (sampled sup and L^2 upper), the grid or quadrature, the
truncation radius, the location of the sup, a second resolution for convergence, and the label FLOAT. Nothing in the
screen is a certificate; a certified H4-REST needs certified moments (plan section 5).

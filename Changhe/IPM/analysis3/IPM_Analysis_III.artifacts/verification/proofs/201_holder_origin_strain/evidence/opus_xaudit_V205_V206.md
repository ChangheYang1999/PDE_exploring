# Cross-audit of V205 (proof 201) and V206 (proof 202)

Independent independent cross-audit, 2026-10-28. Pen-and-paper reading. One sympy check (under 1 s, nice -n 19) confirmed
symbolically: (d_x K1)(-Y) and (d_y K2)(-Y); the identity y(3x^2-y^2)/r^6 = sin(3theta)/r^3; the exact cancellation
(c(-x,y)+cX/3).grad(x^2 y)=0; alpha(L+1)+kappa=q0+p+alpha; the reduction of (8) to (a/(2delta))^(-(q0+alpha)) <= 1;
and the normalization algebra in the proof 202 modal paragraph. V203/V204 (proofs 199, 200) are taken as given.
No file other than this one was written.

## Verdicts

- **V205** (proofs/201_holder_origin_strain/PROOF.md): **PASS WITH REMARKS**. All remarks are cosmetic. Checked: the
  kernel Taylor bound outside 3r, the circular cancellation inside 3r with epsilon=r^(beta/alpha), the exponent
  min(p+alpha,2) with its log, and o(r^3) for the normalized coupling.
- **V206** (proofs/202_variable_origin_holder/PROOF.md): **PASS WITH REMARKS**. The core estimates have no gap. The
  remarks are cosmetic or precision issues, plus one dependency flag: the paragraph applying the theorem to the modal
  trial rests on topics 01, 04 and 33, which were not re-audited.

## What was checked in V205

- Kernels and contact term. Symbol of d_x^2 Gamma is xi^2/|xi|^2, so -xi^2/|xi|^2 = PV(x^2-y^2)/(2 pi r^4) - delta/2.
  This matches U2 = PV K2*h - h/2. K1 = -xy/(pi r^4) has symbol xi eta/|xi|^2 = m_1 of proof 199.
- Derivative candidate. (d_x K1)(-Y) = -y(3x^2-y^2)/(pi r^6) and (d_y K2)(-Y) = +y(3x^2-y^2)/(pi r^6), with
  y(3x^2-y^2)/r^6 = sin3theta/r^3. So DU(0) = diag(-c,c), and the off-diagonal entries vanish by parity. Absolute
  convergence holds near 0 iff beta>1, and at infinity for bounded h.
- Outer part (|Y|>=3r). The segment from -Y to X-Y stays at distance >= 2|Y|/3 from 0, so the Taylor bound
  C r^2 |Y|^(-4) holds. On |Y|>=1 the canonical subtracted kernel is used consistently, and U(0)=0 by parity. The
  radial integrals are correct for beta<2, beta=2 and beta>2.
- Inner part (|Y|<3r). (5) holds absolutely and needs beta>1. epsilon=r^(beta/alpha)<r, so the epsilon-disk lies in
  B_(2r). The circular cancellation uses C^alpha on B2, which holds since 4r<1/2. The annulus bound is
  log(4r/epsilon) = log4 + (beta/alpha - 1)|log r|. Every bound used lies inside B1, since 3r<=3/8.
- At beta=p+alpha=2 the first-order Taylor bound produces r^2 log(1/(3r)), so the log in (2) is needed for the
  estimate as written. The stated bound is correct for every beta in (1,3), which is the full E_p range.
- E_p hypotheses. |h| <= [h]_(y,p)|x|^p|y|^alpha <= ||h|| r^(p+alpha) holds globally, so L=[h]_(y,p). On B2,
  [h]_(C^alpha) <= C([h]_x + 2^p [h]_(y,p)).
- (3). U + cX/3 = c(-2x/3, 4y/3) + E. Contracting with grad(x^2 y) gives exactly 0. The remainder is
  O(|c| r^4 + M r^(gamma+2)(1+|log r|)), and gamma+2 >= 3+min(p+alpha-1,1) > 3. Hence the normalized coupling is
  o(r^3), as claimed.

## What was checked in V206

- Axis division. A = -int_0^1 d_x V1(sx,y) ds and D likewise are C^2 and even-even, with grad A(0)=0. This gives
  |A-A0| <= C r^2 and |grad A| <= C r, and after the cutoff the deviations are O(delta^2) with O(delta) derivatives.
- Smoothness and the transition annulus. beta_delta = D_delta/A_delta is globally C^2 (A_delta >= A0/2). In
  B_delta \ B_(delta/2), the cutoff derivative contributes (1/delta) O(delta^2) = O(delta) to grad beta_delta, and
  |y| <= delta there. Hence L = sup_(R^2)(beta_delta + y d_y beta_delta) is in [beta0, beta0 + C delta^2] and
  Lx = sup|y d_x beta_delta| <= C delta^2.
  - These are global sups, so the transition region needs no separate treatment.
  - The flow of W_delta is global and complete, so no "stay in the region" condition is needed.
  - L >= beta0 because d_y v = beta0 outside B_delta.
- Time direction. The forward integral R f = -int_0^inf e^(-q0 t) f(Phi_t) dt gives S R f = f with the correct
  sign.
  - Along forward orbits, the weight |x_t|^p = e^(-pt)|x|^p beats the y-Lipschitz growth e^(alpha L t).
  - kappa = q0+p-alpha L >= kappa0 - alpha C delta^2, where kappa0 = (1+pA0-alpha D0)/A0 > 0 by (1). Positivity
    for small delta is therefore guaranteed.
- Structural reason the method works. The time change makes x_t = e^(-t)x exact. The flow maps then have the form
  (x,y) -> (g(x), G(x,y)): a y-motion depending on x, never an x-shift depending on y. The latter is the mechanism of
  the refuted conjugacy transfer (S2_CALPHA_THEORY Remark 2.1, V028), so V206 does not conflict with that refutation.
- Delayed entry. For lambda >= a/2 and s < t0 = log^+(a/(2delta)), e^(-s)lambda > delta. The point is then outside
  {|x| <= delta}, which contains supp(beta_delta - beta0), whatever y is.
  - Growth of y can only delay or prevent entry into B_delta.
  - (7) is an upper bound that holds whether or not the trajectory ever enters.
  - d_lambda Y_t = 0 for t <= t0, and the variational integral gives (7).
  - The exponents combine exactly to e^(-(q0+p+alpha)t0), and (8) holds in both cases a <= 2delta and a > 2delta.
- Comparable and noncomparable split.
  - Comparable pairs (a/2 <= b <= a): the x step at fixed y gives [f]_x d^alpha/(q0+alpha); the y step at fixed
    x = e^(-t)b gives the (8) term.
  - Noncomparable pairs (a > 2b, including b=0) use |f| <= [f]_x|x|^alpha, which needs f(0,y)=0, and
    a^alpha + b^alpha <= (2^alpha+1)d^alpha < 3d^alpha.
  - Opposite-sign pairs reduce to these cases by evenness of Rf, since |a-(-b)| >= |a-b|.
  - (9) and (10) are correct for the sum norm: the sup, x and weighted-y parts are all controlled, and continuity
    follows.
- Parity and the axis condition. Y_t(-x,y) = Y_t(x,y) and Y_t(x,-y) = -Y_t(x,y), so Rf is even in x, odd in y and
  vanishes on x=0.
- Division by A. q_delta (V_delta.grad h) = W_delta.grad h holds as distributions for C^1 coefficients. Then
  S h = q T h + m h and T h = A(S h - m h). With the multiplier bounds this gives D_delta = D(S_delta) exactly.
  (11) checked: ||mh||_inf, [mh]_(y,p) <= C delta^2 ||h||, and [mh]_x <= C delta^2 [h]_x + C delta^(2-alpha) ||h||_inf.
- Maximal domain. R maps E_p into D(S). Uniqueness holds for bounded continuous distributional solutions, via flow
  boxes plus continuity; the only stationary point is 0, where h(0)=0 anyway. The graph is closed.
- Neumann series. L = A(S+E) with E = -m + qB bounded on E_p. (S+E) = (I+ER)S on D(S), so
  L^(-1) = R(I+ER)^(-1)q on the same domain D_delta. B is bounded, so it does not change the domain. All powers in
  (14) are positive, and C_R is bounded uniformly. The choice of p in [1,2) is valid because (D0 alpha - 1)/A0 < 2.
- Scope. These exclusions are all stated: original full-plane operator, disk boundary realization, closed cubic
  normalization, nonlinear existence, numerical delta_*, and (I),(S) still OPEN. No overclaim was found.

## Issues (numbered; none fatal)

### V205

1. **Location:** "partial_y K2(-Y)=y(3x^2-y^2)/(pi r^6), partial_x K1(-Y)=-y(3x^2-y^2)/(pi r^6)."
   - **Why it matters:** These are the derivatives evaluated at -Y, i.e. (d_y K2)(-Y). Differentiating Y -> K(-Y)
     instead flips both signs, and with them the sign of c. Read as (d K)(-Y), both formulas are correct and give
     DU(0) = diag(-c,c), consistent with D = int DK(-Y)h(Y)dY in (4) and with the normalization DW(0) =
     c diag(-2/3,4/3).
   - **Status:** Cosmetic. Repair: write (d_y K2)(-Y) and (d_x K1)(-Y).
2. **Location:** "For beta<2 this is O(M r^beta)" and "a finite constant C_(alpha,beta)".
   - **Why it matters:** The constant degenerates in three limits:
     - beta -> 2^- from (3r)^(beta-2)/(2-beta);
     - beta -> 1^+ from (5) and from |c| <= C/(beta-1);
     - alpha -> 0 from epsilon^alpha/alpha and beta/alpha.

     The statement allows all of these. Uniformity near beta=2 can be recovered from
     t^(beta-3) <= (3r)^(beta-2) t^(-1), which gives r^beta log(1/(3r)) and fits the log already in (2).
   - **Status:** Cosmetic.
3. **Location:** "|U(X)-c[h](-x,y)|<=C_(alpha,beta) M r^gamma(1+|log r|)" with gamma=min(beta,2).
   - **Why it matters:** The bound is correct but not sharp. By parity every second-order term
     int D^2K(-Y)[X,X]h(Y)dY over the reflection-symmetric region |Y|>=3r vanishes, since each integrand is odd in x
     or in y. So the outer part is actually O(r^min(beta,3)), and the cap at 2 and the outer log at beta=2 are
     artifacts of stopping the Taylor expansion at first order. The inner annulus still produces
     r^beta(1+|log r|) with this choice of epsilon, so the log as stated is consistent with the proof. Nothing
     downstream needs more than gamma>1.
   - **Status:** Cosmetic. No repair needed.
4. **Location:** "(U[h]+c[h]X/3).grad rho =O_(alpha,p,rho)(||h||_(E_p) r^(gamma+2)(1+|log r|)). (3)"
   - **Why it matters:** The restriction r <= 1/8 and r inside the C^4 disk of rho is implicit in (3). The o(r^3)
     claim follows because gamma+2 > 3.
   - **Status:** Cosmetic. Repair: restate the radius range.
5. **Location:** "Only proof 01's explicit distributional velocity kernels and proof 199's definition of E_p enter the
   proof."
   - **Why it matters:** evidence/check.json also lists proof 200 as a dependency. The proof itself only cites
     proof 200 for the identical integral.
   - **Status:** Cosmetic bookkeeping.

### V206

6. **Location:** "We prove a more general estimate using only q0>0, p>0, L>0, Lx<infinity, and the fact that
   v_delta-beta0 y is supported in B_delta."
   - **Why it matters:** The proof also uses four further facts, all true here:
     - (a) the x-component of W is exactly -x;
     - (b) L is a global upper bound for d_y v, used in (6) and in the propagator of (7);
     - (c) parity of v and f(0,y)=0, used for the noncomparable case and the sign reduction;
     - (d) q0+alpha>0.
   - **Status:** Cosmetic. Repair: list these hypotheses.
7. **Location:** "We may take L>0."
   - **Why it matters:** This is automatic, since d_y v = beta0 outside B_delta gives beta0 <= L <= beta0+C delta^2.
     That interval is also the precise answer to "what L is".
   - **Status:** Cosmetic.
8. **Location:** "Formula(5) solves S_delta R_delta f=f: this follows by differentiating the integral along a
   characteristic, or first testing the integral against a compactly supported smooth function and changing
   variables by the C1 flow."
   - **Why it matters:** The first route (pointwise derivative along orbits plus flow boxes) does not cover the
     stationary point 0. The second route, a global change of variables, does. Alternatively, the defect is a
     distribution of order <= 1 supported at {0}. Testing it with phi(X/epsilon) and using |W(X)| <= C|X| shows the
     defect is zero.
   - **Status:** Precision point, repairable as stated. The proof already names the valid route.
9. **Location:** "Topics199-201 prove, on exactly E_p, ||B_delta||<=C_B delta^(2-p)+C_c C_H delta^(3-p-alpha)"
   - **Why it matters:** The bound comes from proof 199 (C_B) and proof 200 (C_c, C_H), with the same chi and the
     constraint 0<delta<=min(delta0/4,1/4). Proof 201 is not needed for it. V206 inherits any defect found in the
     separate V203/V204 audit.
   - **Status:** Cosmetic; dependency flag.
10. **Location:** "Consequently ||mh||_(E_p)<=C_M delta^(2-alpha)||h||_(E_p)."
    - **Why it matters:** The bound is correct. The argument actually gives C delta^2 for the sup and weighted-y
      parts; only [mh]_x loses delta^(-alpha), through ||h||_inf [m]_alpha. The choice of identity, with the
      undifferenced h taken at a point of supp m where |y| <= delta, is essential and is stated correctly.
    - **Status:** Cosmetic. An optional sharpening is available.
11. **Location:** "This proves injectivity, surjectivity into the maximal domain and closedness."
    - **Why it matters:** The wording is off. L_delta is surjective onto E_p, and L_delta^(-1) maps E_p onto
      D_delta.
    - **Status:** Cosmetic.
12. **Location:** "There is delta_*>0, depending only on alpha,p,A0,D0, the stated local norms of V,rho, and chi"
    - **Why it matters:** delta_* also depends on delta0 and on the radius of the "fixed smaller disk" in the Taylor
      step. Loosely, these are covered by "local norms".
    - **Status:** Cosmetic.
13. **Location:** "Thus U, and hence V=ell X+U, are C3 locally. Axis parity and the exact scalar normalization give
    DV(0)=diag(-(2ell-1),4ell-1)".
    - **Why it matters:** This is a hypothesis check for the modal trial, not part of the theorem. The algebra is
      verified: DU[rho](0) = c diag(-1,1), and the cubic normalization 3 ell - c - 1 = 0 gives c = 3 ell - 1,
      A0 = 2 ell - 1 and D0 = 4 ell - 1 = 2A0+1. The other inputs were not re-audited: the C^(4,1) regularity, the
      sublinear modal tail behind "C3" and ell > 1/2 (topics 04, 33).
    - **Status:** Dependency, not a gap.
14. **Location:** "The theorem replaces the unproved conjugacy transfer with a direct estimate in the original E_p
    coordinates."
    - **Why it matters:** This is true only for the localized operator L_delta. Taken out of context, it could be
      read as rehabilitating the refuted transfer of S2_CALPHA Remark 2.1 for the actual full-plane transport. The
      surrounding scope paragraph excludes that reading.
    - **Status:** Cosmetic. Repair: add "for the localized operator L_delta".

## 5-line summary (for the team note)

V205 PASS WITH REMARKS: DU(0)=diag(-c,c) and U = c(-x,y) + O(r^min(p+alpha,2)(1+|log r|)) hold for every E_p input. The 3r Taylor split, the choice epsilon=r^(beta/alpha) and o(r^3) for the normalized coupling are all correct.
V205 remarks are cosmetic: the (dK)(-Y) notation, constant blow-up as beta->1+ or beta->2-, and a cap at 2 (log included) that is not sharp, since parity kills the second-order term.
V206 PASS WITH REMARKS: the time-changed flow has x_t = e^(-t)x exactly, kappa = q0+p-alpha L with L in [beta0, beta0+C delta^2], and delayed entry and (8) hold. The comparable/noncomparable split, the multiplier and domain identities, and the Neumann series are all correct on the same maximal domain.
V206 remarks are precision only: the full hypothesis list for the general estimate, the stationary point in S R f = f (covered by the global change of variables), and dependency flags on V203/V204 and on topics 04/33 for the modal trial.
Scope is stated correctly in both: localized operator only; no disk inverse, no full-plane actual inverse, no closed cubic J, no nonlinear closure, no numerical delta_*. No fatal or repairable gap was found.

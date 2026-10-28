# Independent audit of V245 (proof proof 228, scaled quadratic axis space Z2)

Audited file: verification/proofs/228_scaled_quadratic_axis_space/PROOF.md (217 lines).
Audit run: Wed Oct 28 15:44:54 UTC 2026 (date -u). Auditor: independent team, read-only except this file.

SHA256 of PROOF.md recomputed: dc9ffef502b399f2b914f4a8846d4c40a282a988ca81d6c920a2ddafbcd31d3e. MATCHES the
expected value and the value in evidence/check.json.

Dependency hashes (PROOF.md of each, recomputed with sha256sum against evidence/check.json): all 7 MATCH.
- 213_common_holder_patch_space 29c5fe9c...e1b0b MATCH
- 214_global_holder_coupling 77e47e53...c27bc1b MATCH
- 217_full_moving_tail_holder a4a9e82a...575477 MATCH
- 222_scaled_far_holder_realization 6fabe851...9b932d MATCH
- 223_scaled_exterior_inverse 30980d7f...6b0530 MATCH
- 35_nonlinear_closure_audit f6b46867...29a9a5 MATCH
- 117_far_residual_leading_term 20b9e69c...dc1851 MATCH
The manifest hashes only PROOF.md files; see finding 1 for the unhashed clarification files that the proof uses.

VERDICT: PASS WITH REMARKS

No gap or error invalidates a stated claim. Every assertion in (a), (b), (c) and every scope sentence was checked
and is proved as stated. The remarks below are clarifications, two literal typos, and one forward-looking warning
(finding 9) about a possible obstruction to global surjectivity on Z2 for alpha > 1/2 that lies outside the scope
of this proof.

## Findings

1. CLARIFICATION (Dependencies and scope; evidence/check.json). The argument uses, besides the hashed PROOF.md
   files: proof 222's AUDIT_CLARIFICATIONS.md and LOCAL_COMMUTATOR_CLARIFICATION.md (the diagonal coefficient times h
   in the differentiated commutator [chi,U], and the auxiliary gamma0 in (4k,2) for the compact input of the local
   E2 step), and proof 223's AUDIT_CLARIFICATIONS.md item 4 (C1 flow boxes turning the distributional identity into
   the orbit identity and back). The proof cites "proof 223's clarification" explicitly in the maximal-domain
   paragraph. These files are not hashed in the manifest. Proof 227 is cited only for the exclusion remark and is
   not a logical dependency, so its absence from the manifest is harmless. Fix: add the clarification files to the
   manifest, or note that they were audited with V242/V244.

2. CLARIFICATION (Annular comparisons, display (5); item 1 of the audit request). The scaling is correct: for
   h = R^beta H(X/R) with H vanishing quadratically on x=0, [h]_(y,2,alpha;A) = R^(beta-2-alpha)[H], so
   R^(2+alpha)[h]_(y,2,alpha;A) has the same order R^beta as the supremum and as R^alpha[h]_(x,alpha;A). Display (5)
   follows exactly as stated: for y != 0 the points (x,y), (x,-y) have the same radius, so both lie in A, and odd-y
   parity gives 2|h(x,y)| <= x^2 (2|y|)^alpha N R^(beta-2-alpha) <= 8^alpha N x^2 R^(beta-2). The seminorm is a
   two-point quantity with no segment condition, so the pair may straddle the inner disk (|x| < R); the definition
   allows this and the proof uses it consistently (distant pairs are always treated by (5), never by integration
   along a segment). Near the horizontal axis the same comparison gives the stronger bound
   N x^2 |y|^alpha R^(beta-2-alpha); at large radius near the vertical axis (5) gives the transverse quadratic
   vanishing that excludes proof 227. The derived ordinary scaled C^alpha bound (one coordinate at a time, the
   intermediate point at radius >= 7R/8 for pairs closer than R/8) and the enlarged-annulus comparison (for a pair
   on one vertical line, |r - r'| <= |y - y'|, so a radius ratio above two forces |y - y'| >= r_max/2) are correct.
   Hence Z2 -> Z is continuous and Z2 is Banach.

3. CLARIFICATION (Divided velocity bounds, display (6); item 2). Verified piece by piece. Middle piece: after
   rescaling X = R Z and dividing by R^beta, the cutoff input has global E2 norm <= C N; crossing pairs use
   |psi(x,y) - psi(x,y')| <= C min(1,|dy|/R) together with (5), so the factor x^2 is kept. Proof 214 display (4)
   holds for every E2 input (truncation argument in proof 214) and gives ||U1/x|| <= C M,
   [U1(x,.)/x]_alpha <= C M(1+|x|), [U2(x,.)]_alpha <= C M(1+x^2), all bounded on the fixed rescaled annulus. The
   canonical velocity is dilation invariant of order zero (kernel of degree -2 plus the local multiplier), and
   U1[h]/x scales by R^(beta-1), which gives exactly the last two lines of (6). The local multiplier part of U2 is
   covered because [h]_(y,alpha) <= x^2 [h]_(y,2,alpha) <= C N R^(beta-alpha). Inner piece: only the L1 mass
   C N R^(beta+2) (beta > -2) and separated kernel derivatives enter, so the local region and all inner annuli need
   no quadratic control; the horizontal segment from (0,y) to (x,y) stays at radius >= |y|, comparable to R in the
   near-axis regime. Outer piece: subtracted kernel O(R|Y|^-3) and beta < 1. The three-piece split therefore
   accounts for distant annuli and the local region. For the smallest annuli (j = 0,1) one uses (6) at R = 2 on a
   comparable annulus containing [1,4], with the inner cutoff shrunk accordingly and the middle piece controlled on
   B2 by ||chi h||E2; the proof's phrase "every fixed comparable-radius annulus" covers this.

4. CLARIFICATION (displays (7), (8); divided density coefficients). Identity (7) is exact:
   (U1 rho0_x + U2 rho0_y)/x^2 = (rho0_x/x)(U1/x) + (rho0_y/x^2) U2. Parities: rho0_x/x is even in x, odd in y;
   rho0_y vanishes to second order at x=0 because rho0(0,y)=0 and rho0_y is even in x. The far orders
   a1 = O(R^(k-2)), a2 = O(R^(k-3)) with one more derivative costing R^-1 are proof 214 display (10) (and 222). The
   product estimate gives the vertical cofactor seminorm C N R^(beta+k-3-alpha) from both the coefficient and the
   velocity differences, distant pairs by the supremum C N R^(beta+k-3) of the cofactor; multiplying by
   R^(2+alpha) yields (8). The weighted tail R^(beta+k-gamma/2) uses gamma > 4k > 2beta+2k. All four exponents in
   (2) are negative, as stated.

5. CLARIFICATION (F0 and M0 in Z2; item 3). F0: proof 117 gives F0/r^3 = r^(2k-4) S(theta) + O(r^(3k-5)), every
   fixed cylinder derivative included, and the exact factorization S = cos(theta)^2 sin(theta) B_S(theta) with B_S
   a finite cosine polynomial. So the leading angular factor vanishes to second order at theta = pi/2, as needed.
   The remainder also vanishes on x=0 (F0 does, and 3k-2 < p) and is even in x, so Taylor division in theta with
   two extra cylinder derivatives gives the cofactor F0/x^2 = O(r^(p-2)) with derivatives O(r^(p-3)), hence
   N_R(F0) <= C R^p. M0: proof 217 display (6) gives exactly |m0/x^2| <= C r^(2k-3)(1+log r),
   |d_y(m0/x^2)| <= C r^(2k-4)(1+log r), |d_x m0| <= C r^(2k-2)(1+log r), hence N_R(M0) <= C R^p(1+log R), and the
   pointwise bound gives the weighted tail for every gamma > 4k (proof 217's restriction gamma < 2 is not needed
   here). H0 is compact with local x^2 division. Closedness of the maximal T and A0 on D2 and the identity of the
   maximal full and transport domains follow by bounded perturbation, as stated. The J packets: on a fixed compact
   support the Z2 norm is bounded by a constant times the E2 norm, so proof 214's input and actual transport-image
   rates transfer; J is nonclosable on the A0 graph, as claimed.

6. CLARIFICATION (Time change, displays (9) to (13); item 5). Positivity of a = V1/x on the whole exterior: the
   error a - ell = U1[rho0]/x is O(r^(k-1)) uniformly in angle (near the vertical axis integrate d_x U1 along the
   horizontal segment at radius >= |y|, which is comparable to r; near the horizontal axis divide directly).
   Likewise b - ell = U2/y = O(r^(k-1)). Hence a >= ell/2 and b/a >= 1/2 for r >= R0/2 with R0 large, uniformly
   including both axes. W1 = V1/a = x identically (also on x = 0), which gives (12) exactly. W = X + O(r^k),
   DW = I + O(r^(k-1)), div W = 2 + O(r^(k-1)), q = k + O(r^(k-1)), Dq = O(r^(k-2)) need second derivatives of
   U[rho0] of order r^(k-2), available from the finite outer modal formulas (proof 117: termwise differentiation at
   every fixed order). Bounds (11) follow by Gronwall and Liouville with drift integral at most
   C r^(k-1) * 2/(1-k), uniform in R. For (13), the derivative of the exponent has integrand bounded by
   C (r e^s)^(k-2) e^s, integrable since k < 1. m_t is even in both coordinates because q is even-even and Psi_t
   commutes with both reflections. Note that a is NOT positive globally: a(0,y) = d_x V1(0,y) tends to -A as y -> 0.
   The device is intrinsically exterior (see finding 9).

7. CLARIFICATION (displays (14) to (17) and the maximal domain). Equivalence with proof 223: with
   tau(t) = int_0^t q(Psi_s X) ds one has Phi_tau(X) = Psi_t(X) (since V = aW), e^(-tau) = m_t, and
   d tau = dt/a, so (15) equals proof 223's -int_0^inf e^(-tau) f(Phi_tau X) d tau. The proof does not need this,
   since it proves (15) directly: the cocycle m_(t+s)(X) = m_s(X) m_t(Psi_s X) gives
   W.grad(Q_R f) = q Q_R f + f/a, and m_S h(Psi_S X) <= C e^((beta-k)S) r^beta -> 0 gives Q_R T_R h = h; I
   rechecked both. Pair estimates in (14): supremum, C N (r e^t)^beta. Close horizontal pair: images differ in both
   coordinates by <= C e^t |dx|; the ordinary scaled C^alpha bound from finding 2 suffices, and the vertical step of
   that decomposition is bounded by (e^t x')^2 s^(beta-2-alpha)|dy|^alpha <= s^(beta-alpha)|dy|^alpha, with
   s ~ r e^t, so there is no harmful mixing. Close vertical pair: by (12) both images have abscissa e^t x, the
   ordinate difference is <= C e^t |y - y'| along the vertical segment (which stays in r >= 3r_j/4 >= R0/2 for
   |dy| <= r_j/4), and the displayed computation gives x^2 r^(beta-2-alpha) e^(beta t)|dy|^alpha exactly. Distant
   pairs use (5) at the images with the lower radius bound c r e^t (needed because beta - 2 < 0); this holds. The
   multiplier m_t has ||m_t|| + R||Dm_t|| <= C e^(-kt), so (16) holds with 1/(k-beta). Weighted L2: change of
   variables on the injective image Psi_t(Omega_R), a subset of Omega_R, with w(Psi_t^-1 Z) <= C e^(gamma t) w(Z)
   and inverse Jacobian <= C e^(-2t); integrability of e^((gamma/2-1-k)t) is exactly gamma < 2+2k, and for
   gamma >= 2+2k the pointwise r^beta bound gives (17) with R-power <= beta - k < 0. Both regimes are uniform in
   R >= R0. Injectivity on the maximal domain, the absence of an inner trace, and continuity up to r = R hold as
   stated.

8. CLARIFICATION (Cutoff extension and (18)). E_R: F_R^(2) -> Z2 and P_R: Z2 -> F_R^(2) are uniformly bounded
   (crossing pairs into the zero collar use (5) at the exterior endpoint; chi E_R h = 0 for R >= 4 since
   5R/4 >= 5 > 4). V.grad eta_R = eta'(r/R)(X.V)/(rR) is even-even, O(1), with scale-R derivative bounds, so
   E_R maps D_R^(2) into D2. Since tau_(R/4) equals one on Omega_R, B_R = P_R tau_(R/4) C0 E_R and
   ||B_R|| <= C epsilon(R/4). The identities (T_R + B_R) Q_R (I + B_R Q_R)^(-1) = I and, for h in D_R^(2),
   T_R h + B_R h = (I + B_R Q_R) T_R h, give both inverse identities. The displayed transition discrepancy
   (eta_R - 1) T_R h + h V.grad eta_R is correct and vanishes for r >= 2R.

9. REMARK (possible surviving obstruction for global work; heuristic, outside the scope of proof 228; item 4).
   The proof 227 forcings (alpha < sigma < 1+alpha < 2) are excluded from Z2 by (5), as claimed. The forcings with
   sigma in [2, 2+alpha) do lie in Z2 and in D2, but give no contradiction: their characteristic integrals are of
   order x^sigma <= x^2 and the resulting x^sigma G(y) satisfies the local E2 bounds. The V232 strips
   x^2 phi(x) y^(-b) have Z2 vertical quotient of order R^(2-b-beta), so membership needs b >= 2 - beta, and then
   the characteristic size x^(k+b) is o(x^2); V234 lives entirely in the far field, where (b) gives a bounded
   inverse. I found no surviving obstruction of these three types. However, there is a different candidate
   mechanism located exactly where the time change of finding 6 fails. Along the outgoing axis let
   kappa(u) = d_x V1(0,u)/V2(0,u). It is about -A/(Du) near 0 and positive at large u, so it changes sign at some
   turning height u*. For orbits from (x,y0) with x small and y0 small, the abscissa at height s is approximately
   x Lambda(y0,s), Lambda(y,s) = exp(int_y^s kappa), which has an interior minimum at s = u*. Take
   f = x^2 psi(|x|/x0) sin(|x|/delta) g(y), with g odd, smooth, supported near +-u*, g(u*) != 0, and
   delta = x0^(2/alpha). Its Z2 norm is bounded uniformly as x0 -> 0 (supremum O(x0^2), horizontal seminorm
   O(x0^2 delta^-alpha), vertical cofactor quotient <= [g]_alpha). Stationary phase in s with parameter
   lambda ~ x0/delta suggests (Q f)/x^2 ~ c lambda^(-1/2) sin(phase(y)) near (x0/Lambda(y0,u*), y0), with phase
   derivative in y of order lambda. Then the local E2 vertical quotient of every T preimage (they all coincide with
   the characteristic integral on these orbits, by the identity used in proof 227) is about lambda^(alpha-1/2),
   unbounded when alpha > 1/2. By the open mapping argument of V234 this would make T: D2 -> Z2 non-surjective for
   alpha > 1/2. A tiny toy computation (nice -n 19, under a second) confirmed the lambda^(-1/2) amplitude and the
   lambda^(alpha-1/2) growth of the quotient for a model phase. None of this is proved: it needs a rigorous
   stationary-phase estimate along the actual orbits, and it says nothing yet about A0, because C0 is not small
   and the oscillatory coupling contribution has not been estimated. A degenerate turning point would give slower
   decay and only strengthen the effect. It does not affect any claim of proof 228. It does suggest checking the
   turning height u* before global surjectivity on Z2 is attempted for alpha > 1/2, and it shows that the exterior
   device of (b) cannot be globalized as it stands.

10. TYPO (Complete coupling, residual paragraph). "with differentiated cofactor order r^(p-2)" should say that
    the cofactor F0/x^2 is O(r^(p-2)) and its first derivatives are O(r^(p-3)). That is what gives
    R^(2+alpha)[F0]_(y,2,alpha) <= C R^p. The conclusion N_R(F0) <= C R^p is correct.

11. TYPO (Weighted L2 section, line after the composition bound). "proves the weighted bound in (15)" means the
    weighted bound for the operator Q_R defined by (15), namely ||Q_R f||L2(w_gamma) <= C||f||L2(w_gamma)/(k+1-gamma/2).
    Also, the letter a names a generic multiplier coefficient in the multiplication paragraph and V1/x in (9). This
    is harmless but could be renamed.

12. REMARK (Scope, theorem block and final section). Every scope sentence is accurate. The proof claims no global
    inverse, no Fredholm property, no closed cubic normalization, no nonlinear closure, no condition (I) and no
    profile. Condition (I) is not mentioned at all, which is consistent. The statements "excluded by (1)" (via (5))
    and "Their exclusion alone is not evidence of a global inverse" are correct. "No statement about a complete
    assembled error, injectivity on the whole plane or a complement inverse is made" is accurate. Given finding 9,
    the sentence calling Z2 "a candidate for further global work" is fair, but for alpha > 1/2 it should be read
    with that caveat.

## Proved scope

For the exact joined normalized trial rho0, every 0 < alpha < 1, 2k-1 < beta < k and gamma > 4k, proof 228
proves the following, with qualitative constants. The space Z2 (local E2 norm of chi h, plus annular norms with
growth beta made of the supremum, the scaled horizontal alpha-Hoelder seminorm and the scaled quadratic vertical
seminorm R^(2+alpha)[h]_(y,2,alpha), plus L2(w_gamma)) is a Banach space. It embeds continuously into proof 222's
Z, and each element satisfies |h| <= C||h|| x^2 r^(beta-2) at large radius. The strain c, the unnormalized
coupling U[.].grad rho0, Cren and the full coupling C0 = U[.].grad rho0 + c[.]M0 are bounded on Z2. The output
tails obey ||tau_R C0|| <= C{R^(k-1) + R^(beta+k-gamma/2) + (R^(p-beta) + R^(2k-gamma/2))(1+log R)} -> 0. F0, H0
and M0 lie in Z2. T and A0 = T + C0 are closed on the same maximal domain D2, and J is not closable on the A0
graph. On each large exterior Omega_R, with the exterior version of the Z2 norm and no inner trace, the actual
T_R = V.grad - 1 is a closed bijection from its maximal domain onto F_R^(2), with inverse
Q_R f = -int_0^inf m_t (f/a)(Psi_t X) dt along the positive time change W = V/(V1/x), for which x_t = e^t x
exactly. This inverse coincides with proof 223's and is bounded uniformly in R. The auxiliary operator
T_R + P_R C0 E_R is a closed bijection with uniformly bounded inverse, and it agrees with A0(E_R h) for r >= 2R,
with the explicit transition discrepancy (eta_R - 1)T_R h + h V.grad eta_R. The proof 227 fractional forcings are
not in Z2. Nothing is proved about a global inverse, surjectivity or Fredholm property on Z2, the middle-annulus
matching, cubic normalization, nonlinear closure, condition (I) or the existence of a profile.

## Checks performed

- Recomputed SHA256 of PROOF.md and of the 7 dependency PROOF.md files; all match check.json.
- Read topics 222 (with both clarification files), 223 (with clarifications), 227, 214 (with clarifications),
  217 (with clarifications), the relevant parts of 213 and 117, and the theory author's section 3.4 of S2_CALPHA_THEORY.md.
- Checked the dimensional scaling of the quadratic vertical seminorm and the derivation of (5), including near both
  axes, at large radius, and for pairs straddling the inner disk.
- Checked Z2 -> Z, completeness, the enlarged-annulus and dyadic-grid comparisons, and the cutoff and coefficient
  multiplier lemma, including crossing pairs.
- Checked (6) for each of the three input pieces, the rescaled use of proof 214 display (4), dilation homogeneity
  and the scaling of U1/x; checked (7), (8), the local E2 step through proof 222's commutator, and the weighted
  tails and exponents in (2).
- Checked F0 in Z2 through proof 117's factorization S = cos^2 sin B_S and the remainder division, M0 in Z2 through
  proof 217 display (6), H0, closedness of the maximal T and A0, and J nonclosability.
- Checked positivity of V1/x and V2/y on the exterior uniformly in angle, the exactness of x_t = e^t x, the bounds
  (10), (11), (13), the reparametrization identity with proof 223's formula, the cocycle and orbit identities,
  uniqueness, all three pair estimates in (14), the weighted L2 bound in both regimes, and uniformity in R.
- Checked E_R, P_R, E_R(D_R^(2)) in D2, the B_R bound, the Neumann inverse (18), and the discrepancy formula.
- Checked that the proof 227, V232 and V234 forcings are excluded or harmless in Z2, and the sigma in [2,2+alpha)
  forcings; identified the turning-height mechanism of finding 9 heuristically (one toy stationary-phase check
  under a second, nice -n 19; no other computation).
- Checked every scope sentence against what is proved.

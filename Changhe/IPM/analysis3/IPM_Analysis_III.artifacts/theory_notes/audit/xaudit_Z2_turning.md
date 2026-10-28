# Independent audit of Z2_turning_obstruction.md (turning-height obstruction on the target Z_2 of proof 228)

Audit time: Wed Oct 28 16:06:48 UTC 2026 (date -u; audit started 15:55:09 UTC). Auditor: independent team.

Audited file: theory-working-files/Z2_turning_obstruction.md (155 lines).
SHA256 recomputed: 14521dacc00feb7e3387ce3a3cc552a337b0809045af81cbcf18b87fc1e5190b. MATCHES the expected value.

Sources read (read-only): proof 228 PROOF.md (sha256 prefix dc9ffef502b399f2) and AUDIT_CLARIFICATIONS.md; proof 222
PROOF.md (6fabe851db30a53c) with AUDIT_CLARIFICATIONS.md and LOCAL_COMMUTATOR_CLARIFICATION.md; proof 223 PROOF.md
(30980d7ffb01e0df) with AUDIT_CLARIFICATIONS.md; proof 227 PROOF.md (a96237e8a3907bd5) with AUDIT_CLARIFICATIONS.md;
proof 217 PROOF.md (bounds (4) to (6)); work/audit/xaudit_V245.md (finding 9); artifacts/code/farres/axis_profile.json
(e92afdc367b2bd76) and axis_profile.py; the hypothesis (A) row of S2_NUMERICAL_CERTIFICATES.md.

VERDICT: PASS WITH REMARKS, conditional on (H*) exactly as the document states it.

Both parts of the Proposition are proved under (H*), but one step needs a small repair. Finding 4: the sign of b(0, y0) at
the chosen starting height does not follow from (H*). Any fixed y0 close to 0 removes the problem, and nothing else
changes. Two citations carry real weight and should be made explicit: the divided horizontal bound for M0 (finding
10) and the far variational bounds (finding 3). Remark 5 overstates its scope for part (ii) (finding 15). Remark 6 is an
unverified sketch (finding 16). I found no ERROR in the Proposition or its proof.

## Findings

1. CLARIFICATION (Step 2, the Z_2 norm of f; item 1). I checked every part of the norm and each one holds. f is smooth,
   even in x and odd in y. It vanishes on x = 0 because phi(0) = 0. The odd extension of g is smooth because
   supp g lies in (y* - delta, y* + delta), away from y = 0.
   - Supremum: |f| <= 16 s^2 ||phi|| ||g||.
   - Horizontal seminorm. f is C^1 in x on the whole line. The seminorm is a two-point quantity with no segment
     condition, so the mean value theorem along the full horizontal line covers every pair. This includes pairs that
     cross the edges of supp phi(./s) and pairs that cross x = 0. On the support, |d_x f| <= C(s + s^2/eps). This is
     at most C s^2/eps once eps <= s, which holds for small eps because eps/s = c_s^(-1) eps^(1 - alpha/2) -> 0. That
     implicit step should be stated. For |Dx| <= eps the difference is at most C s^2 eps^(-alpha) |Dx|^alpha. For
     |Dx| > eps it is at most 2||f|| <= C s^2 eps^(-alpha) |Dx|^alpha. Since s^2 eps^(-alpha) = c_s^2, the seminorm is
     bounded uniformly in eps.
   - Vertical seminorm. At fixed x the factor x^2 cos(2 pi x/eps) phi(x/s) is common to both points, so the quotient is
     at most ||phi||_inf [g_odd]_alpha. The constant 4 in the text is unexplained but harmless (finding 18).
   - Annular scaling. The support lies at radii between y* - delta and ((y* + delta)^2 + 16 s^2)^(1/2). That range
     meets at most three overlapping annuli A_j, all at a fixed scale R. So R^alpha, R^(2+alpha) and 2^(-j beta) are
     fixed constants.
   - Local factor. Rigorously only log y* in (0, 4.111) is known, so y* < 4 is possible and chi f need not vanish.
     It is still bounded. The horizontal part follows from the product rule. The vertical part uses
     |chi(x, y) - chi(x, y')| <= C |Dy|^alpha together with |f|/x^2 <= C.
   - The weighted L^2 part is trivially bounded.

   Hence ||f||_Z2 <= C_0 uniformly in eps. CONFIRMED.

2. CLARIFICATION (Step 1, orbit geometry, graph over height, critical point; item 2).
   - Proof 227 (1) to (3) is proved for y0 = 1/2. The same proof applies to any fixed y0 > 0, with constants uniform
     for y0 in a compact subinterval of (0, infinity) and under the O(1/mu) shifts used in Step 3.
   - The band is crossed only once. In the tube V2 >= v_min, so y_t increases while in the band, and after T_* the
     orbit stays above R > y* + 2 delta.
   - A cleaner derivation of the y0 derivative: d_{y0} xi(eta) = -x0 b(x0, y0) J(eta), where
     J = exp(int_{y0}^eta (b + xi b_x)). This gives d_{y0} log xi = -b(x0, y0) e^(O(x0^2)) = -b(0, y0) + O(x0^2),
     as claimed.
   - Critical point. Put F(eta) = b(xi(eta), eta). Since b_x = O(xi) by evenness, F' = b_eta(0, eta) + O(x0^2). So F
     has a unique zero eta_c = y* + O(x0^2) in the band, and xi''(eta_c) = xi b_eta(xi, eta_c) >= c x0.
   - The sign a_y(0, y*) > 0 is not needed: a nondegenerate maximum works equally well.
   - Regularity. The rescaled Xi solves Xi' = Xi b(s Xi, eta), whose right side is C^3 uniformly in s, so Xi is C^4
     with uniform bounds. The claimed C^3 is enough. V is C^5 near the axis away from the origin (proof 217's local
     regularity, proof 227 clarification 1), so "at least C^4" is correct.
   - The segment {0} x [1, 2y*] in the Smoothness paragraph should read {0} x [y0, 2y*] (see finding 4). It still
     stays away from the origin.

3. CLARIFICATION (Step 1, equal-time separation of the two orbits). The bounds |x_t - x'_t| <= C x_t Delta and
   |y_t - y'_t| <= C y_t Delta for all t are correct. The cited proof 227 (2) is a zero-order bound, though, and does
   not control y0 derivatives.
   - What is needed on r >= R0/2: D(V1/x) = O(r^(k-1-1)) (proof 228 (10): Dq = O(r^(k-2)) with a >= ell/2) and
     DV = ell I + O(r^(k-1)) (proof 223 (3)).
   - Then u = d_{y0} log x_t and v = d_{y0} log y_t satisfy |u'| + |v'| <= C r_t^(k-1)(|u| + |v|) after T_*.
     Gronwall with int r_s^(k-1) ds < infinity keeps u and v bounded.
   - On [0, T_*] they are bounded uniformly in small x0, because a is C^1 and the axis is invariant.

   The citation should be changed accordingly.

4. GAP (minor, repaired here; Step 1 and Step 3, the sign of b(0, y0); items 2 and 3).
   - The problem. The proof says b(0, y0) < 0 "because y0 < y*" for y0 in (y*/4, y*/2). (H*) only makes y* a simple
     zero. It does not say a(0, .) < 0 on (0, y*). The box bounds give a < 0 rigorously only for y <= 1, while
     y*/4 > 1 whenever y* > 4. Numerically y* = 9.15, so y0 lies in (2.29, 4.58), where the recomputed a is in
     [-8.69, -5.52]. The claim is numerically true but amounts to an extra hypothesis.
   - What is actually needed: a fixed y0 with 0 < y0 < y* - 2 delta and b(0, y0) != 0. The sign only fixes the
     direction in which the phase moves.
   - The repair needs no new input. a(0, 0) = 2 ell - D = -A < 0 exactly, and a(0, .) = 2 ell - d_y V2(0, .) is
     continuous because V is C^1. So fix y0 > 0 so small that a(0, y0) < 0. Under the box bound any y0 <= 1 also
     works.
   - The rest goes through unchanged. The near-axis geometry of proof 227 holds for any fixed y0 > 0. The start points
     lie in B2, where chi = 1, so (3) follows from the local E2 factor. The local velocity bounds near the start are
     covered in finding 11.

   With this repair the Proposition depends on (H*) alone.

5. CLARIFICATION (Step 3, the stationary-phase lower bound (1), uniformity and the choice of y0; item 3). Verified.
   - Expansion. The leading term c mu^(-1/2) cos(mu Xi(eta_c) + pi/4) has the right constant and the right sign of
     pi/4 for a minimum. The error is uniform in (x0, y0) over the compact parameter set: the phase is C^4, Xi'' >= c,
     |Xi'| >= c |eta - eta_c| on supp g, and the amplitude is C^2. There are no endpoint terms. In fact only a uniform
     o(mu^(-1/2)) error is needed.
   - Envelope. The dependence on eta_c drops out of d_{y0}[mu Xi(eta_c)] at the critical point, as stated.
   - Phase increment. Xi(eta_c) = 1 + O(s^2), because eta_c - y* = O(x0^2) and b(0, y*) = 0. Together with the
     O(mu) second y0 derivative, the phase moves by pi Xi(eta_c)(1 + O(x0^2)) + O(mu Delta^2) = pi + O(s^2) + O(1/mu)
     over Delta = pi/(mu |b(0, y0)|).
   - Lower bound. The cosine goes from 1 to -1 + o(1), and c(x0, y0 + Delta) = c(x0, y0) + O(Delta). Hence
     |I - I'| >= s^2 mu^(-1/2)(2 c_0 - o(1)) - C s^2 mu^(-1), which gives (1).
   - Choice of y0. x0 must be fixed first, from a base y0, and only then is y0 moved with x0 held fixed. The text
     allows this reading. The move changes Xi on the band by a factor 1 + O(1/mu), so phi(xi/s) = 1 is preserved.

6. CLARIFICATION (Step 4, the representation (2), the open mapping step and the endpoint; item 4). Verified.
   - Sign. d/dt[e^(-t) h(Phi_t X)] = e^(-t) (Th)(Phi_t X) and Th = f - G, which gives (2) with the stated signs.
   - Endpoint. |h(Phi_t X)| <= C K (1 + r_t)^beta, using the upper radial bound when beta >= 0 and the trivial bound
     when beta < 0. Multiplied by e^(-t) this tends to 0 because ell beta < 1.
   - Open mapping. B is closed, so D2 with the graph norm is a Banach space and B maps it boundedly onto Z_2. This
     gives preimages with a graph-norm bound, hence a Z_2-norm bound. No injectivity is needed. "No bounded inverse"
     and "every smaller domain" follow.
   - The characteristic identity along these near-axis orbits, including the initial segment in B2, is the flow-box
     argument of proof 223 clarification 4, extended in proof 227 clarification 2 (V != 0 along the orbit). The
     latter should be cited. Th = f - G is continuous because f and G lie in Z_2.

7. CLARIFICATION (Step 4, the bound (3) at the starting points; item 5). Verified.
   - Both points lie on one vertical line with the common abscissa x0 and are close together.
   - For r >= 1 they share an annulus A_j with j bounded, and R^(2+alpha) [h]_(y,2,alpha;A_j) <= 2^(j beta) ||h||.
     Inside B2 the local E2 factor applies, since chi = 1 there. Either way the constant is C K.
   - With x0 ~ s and Delta ~ eps/s this gives C K s^2 (eps/s)^alpha.
   - Part (i) then reads c_1 <= C K (eps/s)^(alpha - 1/2) with eps/s -> 0, which is false for small eps when
     alpha > 1/2. Correct.

8. CLARIFICATION (Step 5, the vertical step and the decomposition; item 6). Verified.
   - Vertical step. Q_t and P'_t share the abscissa x'_t <= C x_t. Their vertical separation is
     |y_t - y'_t| <= C y_t Delta, much smaller than r_t, so they lie in one annulus. ||G||_Z2 <= C K (C0 and C_ren
     are bounded on Z_2 by proof 228 (a)) gives [G]_(y,2,alpha) <= C K R^(beta-2-alpha). Using the lower radial bound
     for the negative power, the integrand is C K x0^2 Delta^alpha e^((ell beta - 1)t), which is integrable.
   - The identity U[h].grad rho0 = x a1 U1 + x^2 a2 U2 is exact (proof 228 (7)).
   - Horizontal step. Expanding both products into three terms each, with |U1| <= C K x R^(beta-1),
     |DU| <= C K R^(beta-alpha) delta^alpha, a1 = O(R^(k-2)), a2 = O(R^(k-3)) and Lipschitz constants one power
     lower, gives |G(P_t) - G(Q_t)| <= C K (x delta^alpha R^(beta+k-2-alpha) + x delta R^(beta+k-3)) plus the c[h]M
     term. This is slightly sharper than the displayed bound.

9. CLARIFICATION (Step 5, far power counting and the threshold; item 6).
   - The x delta^alpha term gives x0^(1+alpha) Delta^alpha e^(ell(beta-1)t), using ell k = 1. Correct.
   - The x delta term, written with R^(beta+k-2-alpha) as in the text, gives x0^2 Delta e^(ell(beta-alpha)t). That is
     not the stated O(x0^(1+alpha) Delta^alpha e^(ell(beta-1)t)), because delta_t grows like e^(ell t) and
     delta_t <= delta_t^alpha eventually fails. It is still integrable, since alpha > 1/2 > k > beta. With the
     sharper power R^(beta+k-3) it is x0^2 Delta e^(ell(beta-1)t). Either way its integral is at most
     C K x0^2 Delta <= C K x0^(1+alpha) Delta^alpha.
   - So (4) holds. The last step uses x0^2 Delta^alpha ~ s^(2-alpha) eps^alpha <= s eps^alpha.
   - Threshold: s^2 (eps/s)^(1/2) / (s eps^alpha) ~ eps^(1/2 - 3 alpha/4), which tends to infinity exactly when
     alpha > 2/3. CONFIRMED.

10. CLARIFICATION (Step 5, the c[h]M term; this citation is load-bearing).
    - What is needed. The bound |M(P_t) - M(Q_t)| <= C x_t delta_t r^(2k-3)(1 + log r) needs a horizontal bound
      carrying a factor x, for example |d_x(M0/x^2)| <= C r^(2k-4)(1 + log r), or
      |d_x M0| <= C |x| r^(2k-3)(1 + log r).
    - Why it matters. Proof 217's displayed (6) gives only |d_x m0| <= C r^(2k-2)(1 + log r), without the factor x.
      With that alone the term contributes C K x0 Delta ~ C K eps. Since eps / (s^2 (eps/s)^(1/2)) =
      eps^(1/2 - 3 alpha/4) tends to infinity exactly for alpha > 2/3, the undivided bound would destroy part (ii)
      on its whole stated range.
    - Where the divided bound comes from. It follows from the sentence just before proof 217 (6): the finitely many
      smooth angular factors divide by cos^2 theta with uniform angular derivative bounds, including fixed cylinder
      derivatives. On the bounded initial segment it follows from M0 being C^2 near the axis and even in x. H0 is
      compact, smooth off the origin, and even in x.
    - With the divided bound the term is C K x0^2 Delta int (1 + t) e^((1-ell)t) dt ~ C K s eps, which is
      o(s^2 (eps/s)^(1/2)).

    The proof should state this divided derivative explicitly.

11. CLARIFICATION (Step 5, local velocity bounds near the start). Proof 228 (6) is stated for R >= 2. The starting
    height is below 2 under the repair of finding 4, and could also be under the original choice if y* < 8, which the
    rigorous location (0, 4.111) allows. On the part of the initial segment in B2, the bounds |U1| <= C K |x| and
    |DU| <= C K delta^alpha come from two places: proof 222's commutator (chi U[h] = U[chi h] + W with W in C^(1,alpha)
    and W1/x bounded), and proof 214's directional estimate for chi h in E2 together with proof 222's fixed-disk C^alpha
    bound. These results are available, so nothing hidden is assumed, but they should be cited.

12. CLARIFICATION (Setting, the rigorous sign change from the box bounds; item 7).
    - Arithmetic, verified. For t <= 0: a <= -A + 0.100883 + 0.202073 = -9.8478 < 0. For t >= 0:
      a >= ell - 162.6455 e^(-(1-k)t), which is positive for t > ln(162.6455/ell)/(1-k) = 4.1105. So "t > 4.12" is
      safe, and a zero lies at log y* in (0, 4.111).
    - Continuity: a(0, y) = 2 ell - d_y V2(0, y) because div V = 2 ell, and this is continuous because V is C^1.
    - Status. In S2_NUMERICAL_CERTIFICATES.md these box bounds are a single-team CERTIFIED row for hypothesis (A).
      V072 verified its coverage and aggregation conditional on the exported cell enclosures, and the row is
      conditional on the exact normalization (V005). The phrase "conditional only on the V072 box certificate" should
      carry these qualifiers.
    - This existence statement is not a logical input of the Proposition, since (H*) itself posits the zero. Under
      the repair of finding 4 the box bounds are not used at all.

13. REMARK (numerical support for (H*), recomputed; item 7). I recomputed a = 2 ell - d - d' from axis_profile.json
    with non-uniform three-point central differences (single-threaded, nice -n 19, under a second).
    - Invalid rows. The rows at t = -6 and t = -5.5 are broken floating output (d = -4074.7 and -1.1e15). The
      document's range -4.8 < t correctly excludes them.
    - Sign change. Over the remaining samples (t from -4.84 to 12) there is exactly one sign change, between
      t = 2.2107 (a = -0.0195) and t = 2.2183 (a = +0.0351). Linear interpolation gives t* = 2.2134, y* = 9.147,
      da/dt = 7.19, so a_y = 0.79 > 0. This matches the document, which quotes the slope as 7.1.
    - Other values: a <= -9.87 on (-4.8, 0]; a in [-8.69, -5.52] for t in (0.83, 1.52), the numerical range of the
      document's y0; a >= 4.94 for t > 4.11.
    - Consistency with the box bounds. |d - D| e^(-2t) peaks at 0.100876 and max |d'| is 5.6008, against the
      certified 0.100883 and 5.6012. The finite-difference d' slightly exceeds the first certified constant
      (0.20261 against 0.202073) and exceeds the second at the sparse far row t = 10 (87.7 against 73.3113). Both are
      effects of coarse central differences on widely spaced rows. The asymptotic value of |d'| e^((1-k)t) implied by
      the profile is about 73.3, so the certified constant appears essentially sharp. Neither figure contradicts the
      box bounds.
    - This is not a certificate. With sample spacing up to 0.08 in t, a narrow double zero between samples cannot be
      ruled out from these data.

    The scratch script is work/audit/xaudit_Z2_turning_scratch.py.

14. REMARK ((H*) paragraph, degenerate zeros). The sentence "a degenerate zero of finite order with a sign change
    would only strengthen the conclusions" is not proved. An O(x0^2) perturbation of b can split a degenerate zero into
    several nearby simple zeros. A uniform lower bound for the resulting oscillatory integral is not supplied (a van
    der Corput estimate only gives an upper bound), and the y0-phase argument would need redoing. The Proposition does
    not use this sentence, which should be labeled heuristic.

15. REMARK (Remark 5, scope).
    - Part (i) does transfer. With G = 0, the forcing f has bounded E2 norm, (3) holds with the E2 vertical
      seminorm, and the endpoint vanishes because h is bounded. This assumes T is closed on those maximal domains
      (V241).
    - Part (ii) does not transfer verbatim. The vertical step of (4) uses the decay R^(beta-2-alpha) of the Z_2
      vertical seminorm of G. In E2 the only bound is ||G|| x_t^2 |y_t - y'_t|^alpha. Its integrand
      x0^2 Delta^alpha e^(((2+alpha)ell - 1)t) is not integrable, since ell is about 5.575. Proof 214's unscaled
      velocity Holder bounds do not restore the decay.
    - So "applies verbatim" should be restricted to T, or an additional far-field argument should be supplied. This
      does not affect non-surjectivity on E2 and Y, which is already a theorem (V232, V234, V241).
    - The Statement-block sentence that the far structure "plays no role except through the convergence of the orbit
      integrals" is accurate for Z_2. For part (ii) on E2, that convergence is exactly what fails.

16. REMARK (Remark 6). This is an unverified sketch, and it is correctly labeled "(sketch)".
    - Size of the claim. A_P is about 10.15 at the sources (team message board), so 1/A_P is about 0.099. If proved,
      Remark 6 would make T fail to be onto Z_2 for alpha > 0.099. That would supersede part (i) for T but would not
      touch L_ren or A0.
    - What I checked. In the frozen model, the horizontal Holder quotient of h near |s| ~ |y|^(A/mu) behaves like
      |y|^((1 - A alpha)/mu) (with a logarithm when mu = 1). This is consistent with a threshold of 1/A for mu <= 1.
    - Not checked: the transfer through the conjugacy of V214, the parity bookkeeping, and the claim that the coupling
      restores the local inverse. Remark 6 should not be counted as a result.
    - Remark 3(a) ("choose alpha <= 1/2 ... no inverse is known") should say that it concerns A0 and L_ren. For T
      alone, Remark 6 would lower the relevant threshold.

17. REMARK (Remarks 1 to 4).
    - Remark 1 is an accurate heuristic. The coherence length is mu^(-1/2) ~ (eps/s)^(1/2), against Delta ~ eps/s.
      Proof 228's time change uses a = V1/x >= ell/2 only in the exterior (V245 finding 6).
    - Remark 2 is correct only in the scaled form |D_x(U1/x)| <= C K R^(beta-1-alpha) delta^alpha along the whole
      orbit. In that form the horizontal-step contribution becomes C K (s^2 eps^alpha + s eps), which is
      o(s^2 (eps/s)^(1/2)) for alpha > 1/2, so the threshold drops to 1/2. The unscaled bound C delta^alpha would make
      the far integral diverge. The OPEN label is right.
    - Remark 3 is labeled heuristic. In (b), "i.e." is not an equivalence: h = x^2 S with S in C^alpha controls the
      x^(2-alpha)-weighted quotient only for pairs with |Dx| <= x. The (s/eps)^alpha computation is correct.
    - Remark 4 is correct.

18. TYPO.
    - (a) "phi even, phi = 1 on [1/2, 2], supported in [1/4, 4]" should read 1/2 <= |u| <= 2 and 1/4 <= |u| <= 4.
    - (b) "<= 4 [g]_(C^alpha)": the constant should be ||phi||_inf times the seminorm of the odd extension of g.
    - (c) "after moving y0 by at most 2 pi/(mu |b(0, y0)|)" needs a factor (1 + o(1)). The phase increment over Delta
      is pi Xi(eta_c)(1 + o(1)), with Xi(eta_c) = 1 + O(s^2).
    - (d) "da/dt = 7.1": recomputed as 7.19.
    - (e) "It concerns only the horizontal seminorm of Z_2": the mechanism is the mismatch between the unweighted
      horizontal seminorm and the x^2-weighted vertical seminorm.

## Proved scope

Assume (H*): the axis rate a(0, y) = d_x V1(0, y) = 2 ell - d - d' has a simple zero y* > 0. Numerically y* is about
9.15, with a single sign change; this is not certified. The setting is the exact joined normalized trial, every
p < beta < k and every gamma > 4k. With the one-line repair of finding 4, the document proves the following.

- (i) For 1/2 < alpha < 1, T is not onto Z_2(alpha, beta, gamma) from its maximal domain D2, nor from any smaller
  domain.
- (ii) For 2/3 < alpha < 1, neither L_ren nor A0 is onto Z_2.
- In both cases none of these operators has a bounded inverse Z_2 -> D2.

The mechanism combines the open mapping theorem, the smooth forcings x^2 cos(2 pi x/eps) phi(x/s) g(y) with
s ~ eps^(alpha/2) and bounded Z_2 norm, a stationary-phase lower bound at the turning height, and the x^2-weighted
vertical seminorm of the preimage at the starting points of near-axis orbits. The only inputs besides (H*) are topics
222, 223, 227 and 228, plus topics 214 and 217 for the local velocity bounds and the divided M0 bound. Separately, the
single-team box bounds give the rigorous fact that a(0, .) changes sign, with a zero at log y* in (0, 4.111).

Not proved:
- (H*) itself, and the extension to degenerate zeros;
- anything for L_ren and A0 with alpha <= 2/3, or for T with alpha <= 1/2 (apart from the unverified Remark 6);
- the transfer of part (ii) to E2 and Y claimed in Remark 5;
- the remedies of Remark 3;
- the dimension of the cokernel, the range of the actual residual, and any global inverse or existence statement.

Process: all sources were read only. The only files written are this report and the scratch script
xaudit_Z2_turning_scratch.py, both in theory-working-files/audit/. There was one
single-threaded Python run under nice -n 19, lasting under a second. No servers, no JavaScript tooling and no network
were used. No file outside work/audit was written or modified.

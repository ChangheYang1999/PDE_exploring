# Independent audit of V257 (proof proof 234, divided_velocity_full_holder)

Audited file (read only): verification/proofs/234_divided_velocity_full_holder/PROOF.md
(195 lines) and evidence/derivation.json. Audit finished Wed Oct 28 16:21 UTC 2026. Auditor: independent team.
Only this file was written. No computation was run.

## Audited SHA256

- PROOF.md: 1fb068b423e0e39c644f865d7ff018d9a151aeb440943628cfc6c916cc2bcb65 (matches the announcement; rechecked at
  the end, unchanged).
- The dependency hashes in derivation.json match the files on disk: proof 228 PROOF.md dc9ffef5..., proof 232 PROOF.md
  e9cb9c11..., proof 232 turn_certificate.json 0c0efde0....

VERDICT: PASS WITH REMARKS

The new content has no gap: lemma (1), the annular estimate (2) and the coupling difference (18). The lemma is
proved under its stated hypotheses. (2) follows on Z2 with constants uniform in R. (18) is correct term by term,
including c[h]M0, c[h]H0, and the a1, a2 factors. With (18), the T, Lren and A0 thresholds all drop to alpha>1/2.
Two inherited steps (findings 1 and 2) need the binding clarifications that proof 232 recorded after its independent audit
(V256 CONFIRMED, 16:19Z). Finding 1 is load-bearing in proof 234 for 2/3 <= alpha < 1.

## Findings

1. NEEDS CLARIFICATION (inherited, load-bearing). Location: line 161, "the exact M0 cofactor bound
   O(r^(2k-3)(1+log r)) with one more derivative costing r^(-1)".
   - What is needed. Both Cartesian derivatives of Q=M0/x^2 in the thin cone must satisfy
     |grad Q| <= C r^(2k-4)(1+log r). Proof 217 (6) displays only d_y(m0/x^2) and d_x m0.
   - Why it is load-bearing. With only |d_x m0| <= C r^(2k-2)(1+log r), the column difference is C N q delta. The
     ratio in (20) then gains the term q^(-1) lambda^(-1/2) = n^((3kappa-1)/2). That forces kappa<1/3, and with
     kappa>alpha/2 the A0 claim would hold only for 1/2<alpha<2/3.
   - The needed bound does hold: see proof 232 AUDIT_CLARIFICATIONS.md item 1 (proof 217 (5) cylinder derivatives plus
     smooth division by cos^2(theta)).
   - Fix: cite that item. Write the split Delta(x_t^2 Q) = Delta(x_t^2) Q + x_t^2 Delta Q. For H0 cite item 2.

2. NEEDS CLARIFICATION (inherited). Location: lines 173-179, the stationary-phase step ("exactly one nondegenerate
   critical point").
   - Uniform constants also need |phi'| >= b0 > 0 off a fixed neighborhood of s_c on the support of the amplitude.
   - Fix: cite proof 232 AUDIT_CLARIFICATIONS.md item 3 (compactness plus the uniform C1 convergence (11)).

3. NEEDS CLARIFICATION. Location: lines 5-9, the lemma hypotheses.
   (a) The value of g at x=0 "can be assigned arbitrarily", but K takes sup_x over all x, including x=0, so an
       arbitrary assignment could make K infinite. Only s^2|g_j(s)| enters the proof. Fix: take both suprema over
       x != 0.
   (b) "Assume h is continuous, so its canonical IPM velocity agrees with the usual order-zero multiplier" gives the
       wrong reason. For bounded, compactly supported h, the canonical singular integral of proof 214 and the L2
       multiplier differ at most by the far-subtraction constant. That constant vanishes for U1 by x-parity.
       Continuity is not used, and line 17 depends on this. Fix: state the parity reason and cite proof 214.

4. COSMETIC. Location: line 17, "The proof below also applies by approximation to bounded measurable g".
   - No approximation scheme is given, and the claim is never used. For measurable g, "uniformly C^alpha in y"
     needs an every-x or a.e.-x meaning.
   - Fix: drop the sentence, or label it as an unused remark.

5. NEEDS CLARIFICATION (minor). Location: line 125, "Smooth radial localization to that annulus preserves the divided
   vertical seminorm".
   - The lemma needs [g(Z_1,.)]_alpha on the ENTIRE vertical line. That includes:
     - pairs on the two vertical components of the support, across the hole;
     - pairs whose radii differ by more than a factor 2.
   - These pairs use proof 228 (5) at both endpoints, with |dZ_2| bounded below. Cutoff-crossing pairs use
     |psi(Z)-psi(Z')| <= C|dZ_2| together with (5).
   - For 2 <= R < 8, the inner annuli of the localized piece lie in B4, so the chi h E2 term is used there.
   - Fix: cite proof 228 lines 64 and 68 and add one sentence on these cases.

6. COSMETIC. Location: line 101, "equivalently (11) gives H in W^(2,infinity)". C1 is not equivalent to W^(2,infinity).
   Fix: replace "equivalently" with "moreover".

7. COSMETIC. Location: lines 161-165, (18). The letter C denotes both the coupling operator and a generic constant.
   Fix: rename the operator, e.g. Ccp in {C0, Cren}.

8. COSMETIC. Location: line 195, "the geometric series and stationary-phase argument above provide no contradiction at
   that endpoint". The geometric series converge for every 0<alpha<1. At alpha=1/2, the failure is only that (20)
   reduces to b <= C N. Fix: rephrase.

9. COSMETIC (status and scope). Location: line 38 and derivation.json.
   - "their separate independent audit is pending" is stale: V256 has been CONFIRMED with binding clarifications.
   - The manifest omits proof 232 AUDIT_CLARIFICATIONS.md and topics 214, 217 and 222, which the proof uses.
   - The exclusion list does not say that targets other than this Z2 (Z_sc, unscaled E2, Y) are not addressed, or
     that a degenerate turn is not covered.
   - Fix: update the status line, hash the clarification file, and add one scope sentence. Give the scope as
     1/2<alpha<1, 2k-1<beta<k, gamma>4k.

10. REMARK (no fix required). Location: lines 36, 131 and 157. The compact-annulus version of (2) is not needed. The
    initial radius is about 9.15 > 2, so (2) applies directly (proof 232 clarification 4).

## Checks confirmed (items 1-5 of the request)

1. Kernel and parity.
   - With hat convention f^(xi) = int f e^(-ix xi), e^(-|eta||x|)/(2|eta|) has transform (xi^2+eta^2)^(-1). The
     multiplier xi eta corresponds to -d_x d_y. Together these give (3) exactly, with sign(x-s).
   - d_x[sign(x-s) e^(-B|x-s|)] = 2 delta - B e^(-B|x-s|) gives (4).
   - d_x^2 e^(-B|x-s|) = B^2 e^(-B|x-s|) - 2B delta gives (11).
   - h even in x makes U1 odd in x, and F and H even in x. The convention matches IPM u1 = d_x d_y Delta^(-1) rho.
     The sign is irrelevant to the norms.
2. Blocks.
   - Littlewood-Paley in y (5): G_j <= C [g] 2^(-j alpha) for j>=0, using the zero-mean kernel and the y seminorm
     only.
   - The band kernel bound (6) holds. (9) holds via s^2 <= 2x^2 + 2(x-s)^2.
   - (10): |u_j| <= C G(x^2+lambda^-2), and the same bound times lambda for F. For |x| >= 1/lambda, (7) follows.
   - For |x| <= 1/lambda: |H''| <= C lambda G. H is C1 and even, so H'(0)=0. Also |D h_j(x)| <= C lambda G x^2
     (Bernstein), so |F(x)-F(0)| <= C lambda G x^2 and |F(0)| <= C G/lambda.
   - (13) holds a.e. and gives |q_j| <= C G/lambda and |d_x q_j| <= C lambda G |x|. Nowhere is h differentiated in x.
   - For lambda <= 1, (8) holds, with |H''| <= C lambda^3 G on the compact support.
   - y-Lipschitz: division by x keeps the y-frequency support, so Bernstein applies.
   - Summation: sum_j min(2^(-j alpha), d 2^(j(1-alpha))) <= C_alpha d^alpha, split at 2^j ~ 1/d. The j<0 blocks
     sum to C K. Convergence is uniform. Identification: sum h_j -> h in L2 (Plancherel) and U1 is L2-bounded.
3. Passage to Z2.
   - Scaling: g = H/Z_1^2 satisfies |g| <= C N by proof 228 (5), and [g(Z_1,.)]_alpha <= C N because
     R^(2-beta) R^(beta-2-alpha) R^alpha = 1. U1/x then scales by R^(beta-1), which gives (2).
   - Inner part: L1 mass C N R^(beta+2) (beta>-2), with kernels R^-2, R^-3, R^-4.
   - Outer part: subtracted kernel R|Y|^-3 against |Y|^beta, beta<1. U1(0,y)=0 by parity.
   - Near the axis, the segment from (0,y) to (x,y) is separated from both the inner and outer sources. Both
     derivatives of U1/x are <= C N R^(beta-2), which gives R^alpha[U1/x] <= C N R^(beta-1).
   - Coupling: W = (U.grad rho0)/x^2 satisfies |W| <= C N r^(beta+k-3). Each of the four product differences is
     <= C N r^(beta+k-3)(delta+delta^alpha), using separation O(r delta) and the full C^alpha of U1/x and U2.
   - Delta(x^2) W and x^2 Delta W are each <= C N q^2 r^(beta+k-1) delta^alpha, which is (17).
   - e^-t r_t^(beta+k-1) = e^(ell(beta-1)t), which is integrable.
   - The columns contribute C N q^2 delta, given finding 1. The exponent is 1-ell<0, and the factor (1+t) is
     harmless.
   - This gives (18).
4. Threshold chain.
   - The orbit identity gives h(q,y)-h(q,y') = -(I_f(y)-I_f(y')) + (I_C(y)-I_C(y')).
   - Hence b q^2 lambda^(-1/2) <= C N q^2 delta^alpha (h term) + C N q^2 delta^alpha (18), with
     delta ~ pi/(lambda|v_q'|).
   - So N >= c lambda^(alpha-1/2).
   - Bounded forcings require kappa >= alpha/2. lambda = n^(1-kappa) -> infinity requires kappa<1. Open mapping
     gives N <= K sup||f||.
   - The window (alpha/2,1) is nonempty for every alpha<1, so there is a contradiction iff alpha>1/2. For T the
     coupling term is absent.
   - Proof 232's extra ratio n^((1+kappa)/2-alpha) is gone because q^2 now cancels exactly.
5. Scope.
   - The only claim is non-surjectivity onto this Z2 for alpha>1/2, using the certified simple turn.
   - There is no endpoint claim, no F0-range claim, no infinite-cokernel claim and no existence claim. Finding 9
     covers the wording.

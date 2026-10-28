# Independent cross-audit of V228 (proof 217, full moving-tail linearization on the common Hoelder target)

Proof audited: verification/proofs/217_full_moving_tail_holder/PROOF.md

SHA256 (sha256sum, computed at audit time): a4a9e82afc9701235950f96fe4ddbe76c948d299aeb5498faf723a3169575477

This matches evidence/check.json and the V228 record in VERIFICATION_RECORD.md. The nine dependency hashes in check.json (topics 117, 167, 188, 190, 212, 213, 214, 215, 216) all match the current PROOF.md files.

Read: proof 217 PROOF.md and evidence/check.json; topics 213, 214, 212 (with AUDIT_CLARIFICATIONS.md), 215, 216, 167, 188, 190, 117 in full; proof 202 statement and setup; proof 59 and proof 35 sections 1 and 2; the V034 record and proof 31 lines on the far strain moment. No computation was run beyond hand arithmetic.

## Verdict

**PASS WITH REMARKS.** I found no mathematical gap. The local formula (3) is derived correctly, with the correct sign. The cubic cancellation and the divided bounds (4) follow from the proof 212 bracket and the parity of R_zeta. The far cancellation is exact: k r^k Theta minus k r^k Theta, using ell0 k = 1. The decay (5)-(6), the membership m0 in Y for 4k < gamma < 2, the tail (1), closedness, both counterexample transfers and the origin extension are all correct. The remarks concern points that are cited rather than proved (n'_0 >= 3, the sharp O(r^k(1+log r)) velocity of zeta), an overloaded cutoff symbol, steps left implicit, and an incomplete dependency list.

## Checks

### 1. Local formula (3) and the sign of the c[zeta] term: PASS

On r <= 1, chi_infinity = 0, so zeta and grad zeta vanish there. Hence L_fix zeta = U[zeta].grad rho0 on the disk where also chi0 = 1. There M0 = (X.grad rho0 + U[zeta].grad rho0)/n'_0 and H0 = X.grad rho0/3, so

m0 = X.grad rho0 (1/n'_0 - 1/3) + U[zeta].grad rho0/n'_0.

Since 1/n'_0 - 1/3 = (3 - n'_0)/(3 n'_0) = c[zeta]/(3 n'_0), this is exactly {U[zeta] + c[zeta]X/3}.grad rho0/n'_0. The plus sign is correct. It uses only n'_0 = 3 - c[zeta], which is the derivative of n(ell) = 3 ell - 1 - c[rho_ell], and not the sign of c[zeta]. I checked zeta = partial_ell rho_ell = -k^2 chi_infinity r^k log(r) Theta from partial_ell r^(1/ell) = -ell^(-2) r^(1/ell) log r at ell = 1/k. The identity n'_0 M0 = X.grad rho0 + L_fix zeta is the ell-derivative of F_ell(rho_ell) at ell0. This agrees with proof 59 (15), proof 167 (12)-(13) and proof 188.

The inequality n'_0 >= 3, equivalently c[zeta] <= 0, is cited in proof 217, not proved there. It is justified upstream. Proof 35 eq (2) gives c[zeta] = -k^2 c[KP] with c[KP] = (s3/pi) times the integral of chi_infinity r^(k-2) log r dr, which is nonnegative. The moment bounds 37.63077494715565 < s3/pi < 37.63077494715567 are certified in proof 31/V034. Proof 217 needs only n'_0 != 0, since it divides by a fixed nonzero constant (Finding 1).

### 2. Local bounds (4): PASS

Write U[zeta] = c(-x,y) + R_zeta with c = c[zeta]. Then U[zeta] + cX/3 = c(-2x/3, 4y/3) + R_zeta. With rho0_x = x a1 and rho0_y = x^2 a2,

n'_0 m0 = x^2 { c E + a1 R_zeta1/x + a2 R_zeta2 },   E = -(2/3)a1 + (4/3)y a2.

This is exactly proof 212 (18), with Z = R_zeta1/x and W = R_zeta2. With a1 = 2y + e1 and a2 = 1 + e2, the linear parts of E cancel: -(4/3)y + (4/3)y = 0. So E = -(2/3)e1 + (4/3)y e2 = O(r^3), with DE = O(r^2). On the leading cubic, c(-x,y).grad(x^2 y) = -c x^2 y and (cX/3).grad(x^2 y) = c x^2 y, so the strain and X/3 terms cancel exactly.

U[zeta] is smooth near 0 and has the IPM parities (U1 odd in x and even in y, U2 even in x and odd in y). Divergence is zero and the linear coefficient is c[zeta] (proof 167 (7)). The parities exclude constant and quadratic Taylor terms. Hence R_zeta = O(r^3), D R_zeta = O(r^2) and D^2 R_zeta = O(r). Taylor division gives R_zeta1/x = O(r^2) and partial_y(R_zeta1/x) = O(r). So a1 R_zeta1/x = O(r)O(r^2) = O(r^3) and a2 R_zeta2 = O(r^3). Their y derivatives are O(1)O(r^2) + O(r)O(r) = O(r^2) and O(r)O(r^3) + O(1)O(r^2) = O(r^2). This gives |m0/x^2| <= C r^3, |partial_y(m0/x^2)| <= C r^2 and |m0| <= C r^5.

The bound partial_x m0 = O(r^4) is not derived explicitly in the text, but it holds. Differentiate n'_0 m0 = c x^2 E + R_zeta.grad rho0. The first term gives 2xE + x^2 E_x = O(r^4). The second gives (partial_x R_zeta).grad rho0 + R_zeta.partial_x grad rho0 = O(r^2)O(r^2) + O(r^3)O(r) = O(r^4) (Finding 4). The Taylor input is correct. Parity excludes degrees 2 and 4, and h(0,y) = 0 excludes y and y^3. So the C^(4,1) density has Taylor polynomial x^2 y through degree 4, and rho0 - x^2 y = O(r^5).

### 3. Far cancellation and (5): PASS

Where chi_infinity = 1 and chi0 = 0:

- X.grad(r^k Theta) = r partial_r(r^k) Theta = k r^k Theta.
- (ell0 r partial_r - 1)(r^k log r) = ell0(k r^k log r + r^k) - r^k log r = r^k/k, using ell0 k = 1. Multiplying by -k^2 Theta gives -k r^k Theta.

The sum is exactly zero. In this region zeta equals -k^2 r^k log(r) Theta identically, so the linear zeta part ell0 X.grad zeta - zeta leaves no remainder. The cutoff transition annulus is compact and is treated in the compact-region step. The remaining linear term is X.grad R = partial_t R = O(r^(2k-1)) by proof 117. There R = O(r^(2k-1)) comes from the second exponent alpha_1 = 2k-4 of rho/r^3, with every fixed cylinder derivative.

L_fix as defined in line 15 contains U[rho0].grad zeta. With U[rho0] = O(r^k) and grad zeta = O(r^(k-1)(1+log r)), this term is O(r^(2k-1)(1+log r)). The term U[zeta].grad rho0 is O(r^k(1+log r)) O(r^(k-1)). The bounds U[rho0] = O(r^k) and grad rho0 = O(r^(k-1)) already include R, so the remark "products involving R are faster" is redundant but harmless. Hence n'_0 M0 = O(r^(2k-1)(1+log r)), with cylinder derivatives.

The bound U[zeta] = O(r^k(1+log r)) is stated ("The separated tail gives"), but proof 167 (7) displays only O(r^(q_*)) with q_* > k strictly. The sharp form is correct. Differentiate in q the homogeneous particular solution r^(q+1)P_q(theta) of proof 35 section 1, whose modal denominators q +/- n + 2 are nonresonant. Add the decaying exterior multipoles from the compact transition (proof 117: at least r^(-3) in U). See Finding 2.

Axis division at infinity: the termwise vanishing argument is right. V1, U1, rho0_x and zeta_x are odd in x. rho0, zeta, rho0_y and zeta_y are even in x and vanish on x = 0, hence are O(x^2). For each fixed r, m0(r,.) and its r partial_r derivatives lie in a fixed finite-dimensional space of trigonometric polynomials (finite modal trial, finite Theta, mode-preserving Green formula). Division by cos^2(theta) is a bounded linear map on the subspace that vanishes to second order at theta = +/-pi/2. This justifies "smooth division ... with uniform angular derivative bounds" and gives (6), with Cartesian derivatives costing r^(-1).

### 4. Membership m0 in Y: PASS

All four quantities m0, partial_x m0, m0/x^2 and partial_y(m0/x^2) are bounded. Near 0 they vanish by (4). At infinity they decay, since 2k-1, 2k-2, 2k-3 and 2k-4 are all negative (k is about 0.17936). On the compact region they are bounded because the trial is C6 across joins, so m0 is C5 there and the quotient by x^2 has bounded y derivative. Splitting differences at 1 gives [m0]_x and [m0/x^2]_y finite, and [m0]_(y,2) = sup|G(x,y) - G(x,y')|/|y-y'|^alpha with G = m0/x^2. The parities and m0(0,y) = 0 hold. The weight is w_gamma = (1+r^2)^(-gamma/2), comparable to r^(-gamma) at infinity. So |m0|^2 w_gamma r dr <= C r^(4k-2)(1+log r)^2 r^(1-gamma) dr = C r^(4k-1-gamma)(1+log r)^2 dr. This is integrable at infinity iff 4k-1-gamma < -1, that is gamma > 4k. At gamma = 4k the integral of r^(-1)(log r)^2 diverges, so the condition is exactly right. H0 is compact, with cofactor (a1 + y a2)/3 near 0, so H0 is in Y and therefore M0 is in Y.

### 5. Tail (1): PASS

beta_R vanishes on B_R. Substituting r = Rs,

integral_R^infinity r^(4k-1-gamma)(1+log r)^2 dr = R^(4k-gamma) integral_1^infinity s^(4k-1-gamma)(1+log R+log s)^2 ds <= C R^(4k-gamma)(1+log R)^2,

because the s-integrals with (log s)^j, j = 0,1,2, converge for gamma > 4k. The square root is C R^(2k-gamma/2)(1+log R), which is (7). For the E2 part, the supremum is C R^(2k-1)(1+log R). The x seminorm uses beta_R partial_x m0 + m0 partial_x beta_R = O(R^(2k-2)(1+log R)) and the supremum, split at 1. The weighted y seminorm is even smaller, O(R^(2k-3)(1+log R)). So ||beta_R m0||_E2 <= C R^(2k-1)(1+log R).

Exponent comparisons: (2k - gamma/2) - (2k-1) = 1 - gamma/2 > 0 iff gamma < 2, and (2k - gamma/2) - (k-1) = k + 1 - gamma/2 > k > 0. So for R >= 1 the weighted term dominates both the E2 part and the proof 214 tail O(R^(k-1)(1+log R)). beta_R H0 = 0 for large R. With ||c||_(Y*) <= 4/pi this gives (1). The exponent 2k - gamma/2 is negative iff gamma > 4k. For gamma in (4k, 2), about (0.7174, 2), it lies in (2k-1, 0).

### 6. Closedness and transfer of the counterexamples: PASS

c is bounded on Y by 4/pi (proof 213) and m0 is in Y, so c[.]m0 is bounded rank-one. Proof 214 gives L_ren closed on D_Y, with D_Y the maximal domain. A bounded perturbation keeps it closed, keeps the same maximal distributional domain (A0 h is in Y iff V.grad h is in Y) and gives equivalent graph norms. Also L_ren + c[.]m0 = V.grad - 1 + U[.].grad rho0 + c[.](H0 + m0), and H0 + m0 = M0, so the two displayed forms of A0 agree.

The packets k_eps have c[k_eps] = 0, so A0 k_eps = L_ren k_eps. Nonclosability of J transfers unchanged.

For proof 216, the packets h_n are supported in a fixed compact K away from the origin and the axes, have c[h_n] = 0 and satisfy ||h_n||_inf -> 0. The added commutator is c[chi h_n]m0 - c[h_n]chi m0 = c[chi h_n]m0. Since c[f] = (1/pi) integral sin(3 theta) r^(-3) f dX, it satisfies |c[f]| <= (1/pi)||f||_inf integral_K r^(-3) dX for f supported in K. So the added term is at most C||h_n||_inf ||m0||_Y -> 0. Graph boundedness transfers by equivalence of the graph norms. The argument is valid. A shorter route also exists (Finding 5).

### 7. Origin extension (2), (8): PASS

Take G = chi(X/delta) m0/x^2. Its support is in B_delta, |G| <= C delta^3, and |partial_y G| <= C delta^2 (the cutoff derivative C/delta times C delta^3, plus C delta^2). Then min(C delta^2 d, 2C delta^3) <= C delta^(3-alpha) d^alpha for every d, which gives [chi m0]_(y,2) <= C delta^(3-alpha) globally. The supremum O(delta^5) and x seminorm O(delta^(5-alpha)) are smaller. So (8) holds. With |c[h]| <= (4/pi)||h||_E2, ||D_delta||_(E2->E2) <= C delta^(3-alpha).

On supp chi(X/delta), which is in B_delta, chi0 = 1, so (2) minus proof 215's L_delta is exactly chi(X/delta)c[h](M0 - X.grad rho0/3) = c[h]chi(X/delta)m0 = D_delta h. Since L_delta = A_coeff(S_delta + E_delta) with q_delta = 1/A_coeff, we get (2) = A_coeff(S_delta + E_delta + q_delta D_delta). This is the correct form: the rank-one term must carry the reciprocal coefficient, and the proof says so and distinguishes A_delta,coeff from the operator. Then ||q_delta D_delta|| <= (q0 + C delta^2) C delta^(3-alpha) <= C delta^2, since 3 - alpha > 2 and delta <= 1. The maximal domain {S_delta h in E2} is unchanged by bounded perturbations. The Neumann formula S^(-1)(I + E'S^(-1))^(-1)q_delta gives a closed bijection with an inverse bound uniform in delta. On B_(delta/2), V_delta = V (proof 202) and the coupling cutoff is 1, so (2) matches the A0 expression there.

### 8. Scope and the H0/M0 membership statement: PASS

The statement disclaims a global inverse, injectivity, a closed cubic normalization and numerical constants (lines 26, 41, 146). The proof proves nothing beyond these limits.

H0 and M0 being in Y while excluded from the targets of proof 188 is consistent. E2 constrains h/x^2 only through a bounded y-Hoelder seminorm, so a nonzero cubic jet x^2 y times a cutoff is admissible. In Y_H and the proof 173 low targets, a vertical cofactor trace tending to 1 fails the weight a_H, comparable to exp(9t/5), and the exp(-t/2) scalar weight. Proof 213's remark that the raw X.grad rho0 is not in Y concerns growth like r^k at infinity, not the jet. H0 is cut off, and M0 decays by the far cancellation.

## Findings

1. (remark) n'_0 >= 3 is cited, not proved. The chain is proof 31/V034 (certified s3/pi of about 37.6308, positive) to proof 35 eq (2) (c[KP] >= 0 for a nonnegative cutoff) to proof 59 and topics 167, 188, 190. Proof 217 uses only n'_0 != 0. The sign in (3) does not depend on it.

2. (remark) The sharp far bound U[zeta] = O(r^k(1+log r)), with cylinder derivatives, is asserted, not derived. Proof 167 (7) displays only O(r^(q_*)) with q_* > k. The sharp form follows from the q-derivative of the nonresonant homogeneous modal solution (proof 35 section 1) plus the decaying exterior multipoles (proof 117). Without it, membership for every gamma > 4k would still follow, choosing q_* close to k. But the displayed rate R^(2k-gamma/2)(1+log R) in (1) uses the sharp form. A one-sentence derivation would close this.

3. (cosmetic) The symbol chi is overloaded. In (1), chi = 1 on B1 and is supported in B2. In (2), (8) and D_delta, chi(X/delta) must be proof 202's cutoff (1 on B_(1/2), supported in B1), as "support in B_delta", "chi0 = 1 on B_delta" and "On B_(delta/2)" presuppose. With the first chi, the difference from proof 215's L_delta would not be exactly rank-one (it would still be repairable via proof 212). Suggest a separate name.

4. (cosmetic) partial_x m0 = O(r^4) near 0 is stated without derivation; the listed division facts address only y derivatives. It follows in one line from n'_0 m0 = c x^2 E + R_zeta.grad rho0 (Check 2).

5. (remark) The proof 216 transfer is correct as written. More simply, [c[.]m0, chi]h = c[chi h]m0 - c[h]chi m0 is a bounded operator Y -> Y of rank at most two, hence compact, so noncompactness of [L_ren, chi] transfers for every admissible chi without using the packets.

6. (cosmetic) In the proof of (8), "pairs with one point outside the larger support box have separation comparable to delta" is not literally true for pairs that cross the boundary at close range. The following clause covers them. The global estimate min(C delta^2 d, 2C delta^3) <= C delta^(3-alpha) d^alpha for G = chi(X/delta)m0/x^2 makes the case split unnecessary.

7. (cosmetic) The dependency list omits proof 202 (V_delta and the cutoff, used explicitly), proof 201 (strain identity), proof 33 (C^(4,1) regularity) and topics 31/35/59 (n'_0 >= 3). The nine listed dependency hashes match.

8. (remark) The sentence "products involving R are faster" in the far section is redundant, because the bounds for U[rho0] and grad rho0 already include R. No error results.

## Scope summary (for quoting)

V228 (proof 217) was audited independently and passes with remarks; no gap was found. The exact moving-tail column m0 = M0 - H0 lies in Y = E2 intersect L2(w_gamma) for every 0 < alpha < 1 and 4k < gamma < 2. Two exact cancellations give this. At the origin, the strain bracket gives m0/x^2 = O(r^3). At infinity, k r^k Theta minus k r^k Theta cancel, leaving O(r^(2k-1)(1+log r)). Hence the full linearization A0 = L_ren + c[.]m0 is closed on the maximal domain D_Y. Its coupling output tail is O(R^(2k-gamma/2)(1+log R)), an upper bound only. J nonclosability and the noncompactness of the cutoff commutator carry over to the full A0 graph. The actual-origin auxiliary extension that includes the exact M0 column is a closed bijection on its maximal E2 domain, with an inverse bounded uniformly in delta and factorization error O(delta^2). The new column costs only O(delta^(3-alpha)). The inequality n'_0 >= 3 and the sharp O(r^k(1+log r)) velocity of zeta are cited from upstream topics rather than reproved. The result gives no global inverse, no injectivity, no closed cubic normalization, no numerical constants and no nonlinear statement. H0 and M0 belong to this Hoelder target only because E2 admits a cubic jet. Their exclusion from the stronger targets of proof 188 still holds.

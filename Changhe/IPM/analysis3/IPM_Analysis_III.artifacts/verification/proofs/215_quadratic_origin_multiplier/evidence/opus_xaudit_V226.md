# Independent audit of V226 (proof 215, quadratic origin multiplier)

Proof audited: verification/proofs/215_quadratic_origin_multiplier/PROOF.md

SHA256 (sha256sum, computed at audit time): e237998650ebf3759f91951c20fe0bf1bd81a30614405d3865f52f115e66b363

This matches the hash in evidence/check.json and in the V226 record. The four dependency hashes in check.json (topics 33, 202, 203, 212) also match the current PROOF.md files.

Read: proof 215 PROOF.md and evidence/check.json, proof 202 PROOF.md, proof 212 PROOF.md and AUDIT_CLARIFICATIONS.md, the p=2 section of proof 203, the V226 record, xaudit_V205_V206 remark 10, xaudit_V207_V208 A11 and xaudit_V219 remark 12. No computation was run. All checks below were done by hand.

## Verdict

**PASS WITH REMARKS.** I found no mathematical gap. The multiplier lemma (1), ||m_delta h||_(E_p) <= C delta^2 ||h||_(E_p) for every p>0 and 0<delta<=1, is correct. Its only inputs are sup|m| <= C0 delta^2, sup|Dm| <= C1 delta, support in B_delta, and the pointwise bound |h(x,y)| <= [h]_(y,p)|x|^p|y|^alpha. That pointwise bound comes from h(x,0)=0, that is from oddness in y, and the proof attributes it correctly. The supported-endpoint identity (5) handles every pair of points. This includes pairs with one point outside supp m and pairs at arbitrarily different |x|, because the Hoelder bound (4) for m holds globally on R^2. The source of the old delta^(2-alpha) loss in proof 202 (11) is identified correctly: that bound used ||h||_inf. The hypotheses hold for the actual multiplier m_delta = 1/A_delta - 1/A0 = -chi(X/delta)(A-A0)/(A0 A_delta). The factorization L_delta = A_delta(S_delta + E_delta) with E_delta = -m_delta + q_delta B_delta is exact. The bound ||E_delta|| <= C_E delta^2 follows from (1) and proof 212. The p=2 exponent kappa0 = beta0(1-alpha) is correct, as are the maximal-domain identity and the Neumann formula (2). The scope statements are accurate. The remarks are cosmetic or informational. One of them notes that the x-seminorm part needs even less than the proof uses.

## Checks

### 1. Product estimate in each component of the E_p norm: PASS

Put M = ||h||_(E_p). Let C4 = max(C1, 2C0) be the constant in (4).

(a) Bound (4). For any X, X' in R^2 with d = |X-X'|, m is C1 on the convex set R^2. For d <= delta the mean value inequality gives |m(X)-m(X')| <= C1 delta d = C1 delta d^(1-alpha) d^alpha <= C1 delta^(2-alpha) d^alpha. For d >= delta it gives |m(X)-m(X')| <= 2C0 delta^2 = 2C0 delta^(2-alpha) delta^alpha <= 2C0 delta^(2-alpha) d^alpha. So (4) holds for every pair in the plane, not only pairs on coordinate lines.

(b) Supremum. ||mh||_inf <= C0 delta^2 ||h||_inf. Correct.

(c) x-seminorm. Take A=(x,y), B=(x',y) with x != x'. If both product values vanish there is nothing to prove. Otherwise one of them, say at A, is nonzero, so m(A) != 0 and |A| <= delta. The identity (5),

m(A)h(A) - m(B)h(B) = m(B)(h(A)-h(B)) + (m(A)-m(B))h(A),

is exact; I expanded it by hand. The first term is at most C0 delta^2 [h]_x |x-x'|^alpha, using only the global sup of m at B, wherever B lies. In the second term, (4) gives |m(A)-m(B)| <= C4 delta^(2-alpha)|x-x'|^alpha. Bound (3) at A gives |h(A)| <= [h]_(y,p) delta^(p+alpha). The product is C4 delta^(2+p)[h]_(y,p)|x-x'|^alpha <= C4 delta^2 M |x-x'|^alpha, since p>0 and delta<=1. The case with B outside supp m is the case m(B)=0. Then the first term vanishes and the second term is exactly m(A)h(A). The estimate is unchanged. The case of very different |x|, for example |x| <= delta and |x'| >> 1, is covered because (4) is a global bound in d. No local Hoelder norm of h or of m is used. The case where both points lie in supp m is the same computation. The choice of A is a without-loss-of-generality step, since the difference quotient is symmetric in absolute value.

(d) Weighted y-seminorm. Take A=(x,y), B=(x,y') with x != 0 and m(A) != 0. The first term in (5) is at most C0 delta^2 [h]_(y,p)|x|^p|y-y'|^alpha. In the second term, (3) at A gives |h(A)| <= [h]_(y,p)|x|^p|y|^alpha <= [h]_(y,p)|x|^p delta^alpha, and (4) gives |m(A)-m(B)| <= C4 delta^(2-alpha)|y-y'|^alpha. The product is C4 delta^2 [h]_(y,p)|x|^p|y-y'|^alpha. Both points share the same x, so the weight |x|^p is common and no comparison of weights at different x arises. This step requires that (3) carries the weight |x|^p. It does.

(e) Membership. m is even in both variables and h is even in x and odd in y, so mh has the same parities. mh is bounded and continuous, and m(0,y)h(0,y) = 0. So mh lies in E_p.

Summing gives the explicit bound

||mh||_(E_p) <= C0 delta^2 ||h||_(E_p) + 2 C4 delta^2 [h]_(y,p) <= (C0 + 2 max(C1, 2C0)) delta^2 ||h||_(E_p),

for every p>0 and 0<delta<=1. This is (1). The constant does not depend on alpha or p (Remark 2).

### 2. The hypotheses for the actual multiplier: PASS

By proof 202, T_delta = V_delta.grad - 1 = -x A_delta partial_x + y D_delta partial_y - 1 = A_delta(W_delta - q_delta). With q_delta = 1/A_delta = q0 + m_delta this is A_delta(S_delta - m_delta). Thus m_delta = 1/A_delta - 1/A0 = -chi(X/delta)(A-A0)/(A0 A_delta), exactly as named in proof 215.

- Support. chi is supported in B1, so m_delta is supported in B_delta.
- Parity and regularity. A = -integral_0^1 partial_x V1(sx,y) ds is C2 when V is C3, and it is even in both variables. chi is reflection invariant. So m_delta is C2, in particular C1, and even in both variables.
- Supremum. Evenness in each variable gives DA(0) = 0, and A is C2. So |A-A0| <= C r^2 and |DA| <= C r on a fixed disk. For delta small enough that B_delta lies in that disk and A_delta >= A0/2, we get |m_delta| <= |A-A0|/(A0 A_delta) <= (2C/A0^2) delta^2.
- Derivative. Dm_delta = -DA_delta/A_delta^2. Also DA_delta = delta^(-1)(Dchi)(X/delta)(A-A0) + chi(X/delta)DA, and both terms are O(delta) on B_delta. So |Dm_delta| <= (4/A0^2) C delta.

The constants do not depend on delta. The same hypotheses hold for A_delta - A0, so multiplication by A_delta = A0 + (A_delta - A0) is bounded on E_2. It has the bounded inverse q_delta = q0 + m_delta.

### 3. The pointwise bound (3) on supp m: PASS

The bound |h(x,y)| <= [h]_(y,p)|x|^p|y|^alpha needs h(x,0) = 0. Then |h(x,y)| = |h(x,y) - h(x,0)| <= [h]_(y,p)|x|^p|y|^alpha. Oddness in y gives h(x,0) = -h(x,0) = 0, and the proof says "Oddness in y gives ...", which is the correct attribution. The condition h(0,y) = 0 alone does not give this bound. It gives the different bound |h(x,y)| <= [h]_x|x|^alpha, and it makes the weighted seminorm meaningful at x = 0. On supp m, which lies in B_delta, we have |x|, |y| <= delta, so |h| <= M delta^(p+alpha), as the auditor's remark stated. Since E_p and E_2 are defined with odd-y parity, which every input inherits, no extra hypothesis is needed. The parenthetical in the audit request, "from h(0,y)=0", is imprecise in this respect. The proof itself is not.

### 4. Factorization, inverse estimate and domains: PASS

- Algebra. L_delta = T_delta + B_delta = A_delta(S_delta - m_delta) + A_delta q_delta B_delta = A_delta(S_delta + E_delta), with E_delta = -m_delta + q_delta B_delta. The formula S_delta = -x partial_x + (D_delta/A_delta) y partial_y - q0 is proof 202's W_delta - q0. The variable transport coefficient beta_delta stays inside S_delta. No derivative of a coefficient error is treated as a bounded perturbation.
- Error size. ||m_delta|| <= C_M delta^2 by Check 1. ||q_delta|| <= q0 + C_M delta^2, since multiplication by a constant c has norm |c| on E_2. ||B_delta|| <= C_B delta^2 by proof 212 (1), which holds for the C^(4,1) background of proof 33. Hence ||E_delta|| <= C_M delta^2 + (q0 + C_M delta^2) C_B delta^2 <= C_E delta^2 for delta <= 1. This is (10).
- p=2 exponent. q0 + 2 = (1+2A0)/A0 = D0/A0 = beta0, so kappa0 = q0 + 2 - alpha beta0 = beta0(1-alpha) = (D0/A0)(1-alpha) > 0. This agrees with proof 203 and xaudit_V207_V208 A11. Proof 202's characteristic estimates (5)-(10) assume only q0>0, p>0, L>0 and Lx finite, plus the support property. With L <= beta0 + C delta^2 we get kappa >= kappa0/2 for small delta, and (10) of proof 202 gives a uniform C_R. The factor (2delta)^p in (8) and (9) of proof 202 is harmless at p=2.
- Domains. If S_delta h is in E_2, then T_delta h = A_delta(S_delta h - m_delta h) is in E_2. If T_delta h is in E_2, then S_delta h = q_delta T_delta h + m_delta h is in E_2. These identities hold distributionally, because A_delta is C2 and multiplies the first-order distribution S_delta h. So the maximal domains agree, and adding the bounded B_delta does not change them.
- Inverse. If C_E C_R delta^2 < 1, then I + E_delta S_delta^(-1) is invertible by a norm-convergent Neumann series. S_delta + E_delta = (I + E_delta S_delta^(-1))S_delta is a bijection from D(S_delta) onto E_2, and L_delta h = f is equivalent to (S_delta + E_delta)h = q_delta f. This gives L_delta^(-1) = S_delta^(-1)(I + E_delta S_delta^(-1))^(-1) q_delta and ||L_delta^(-1)|| <= C_R(q0 + C_M delta^2)/(1 - C_E C_R delta^2). This is (2). Closedness follows because L_delta has an everywhere-defined bounded inverse. It also follows from the closed graph of S_delta, a bounded perturbation, and the bounded invertible left factor A_delta.

### 5. Scope: PASS

The proof states that this is the explicitly localized whole-plane extension, equal to the actual operator only on B_(delta/2), and that it is not a full-plane inverse. It supplies no numerical C_E, C_R or delta0. It does not close the cubic trace or a nonlinear iteration. It claims sharpness neither of E_delta nor of (1). All of this is accurate. The V226 record restates the same limits. The only change from V206/V219 is the rate of the Neumann error, from O(delta^(2-alpha)) to O(delta^2). The qualitative conclusion, invertibility for small delta with uniformly bounded inverse, was already known.

## Remarks

1. Weaker input for the x-seminorm. The improvement of [mh]_x does not need the weighted seminorm or oddness in y. Using h(0,y) = 0, |h(A)| <= [h]_x|x_A|^alpha <= [h]_x delta^alpha on supp m, and the second term of (5) becomes C4 delta^2 [h]_x|x-x'|^alpha. The delta^(2-alpha) in proof 202 (11) came only from bounding h(A) by ||h||_inf, which ignores the vanishing on the axis. Only the y part genuinely needs (3), and with it the weight |x|^p. Informational.

2. Constant dependence. The statement says C depends on alpha, p, C0 and C1. In fact C = C0 + 2 max(C1, 2C0) works for every p>0 and every alpha in (0,1), provided 0<delta<=1. Cosmetic.

3. Wording of (4). "For two points on either coordinate line" undersells (4), which holds for any two points of R^2, since m is C1 on the whole plane. Cosmetic.

4. Notation in (2). The bound uses "q0 + C delta^2"; by (8) this should read q0 + C_M delta^2. Cosmetic.

5. Cutoff compatibility. Proof 212 is stated for a radial chi, while proof 202 allows any reflection-invariant chi. The combined theorem should fix a radial chi, which satisfies both. I saw no place where proof 212 uses radiality beyond reflection invariance and support in B1. Cosmetic.

6. Notation clash. Proof 212's sharpness section uses q_delta = delta/8 for a point coordinate, while topics202 and 215 use q_delta = 1/A_delta. This is harmless because the two uses never meet, but it would be cleaner to rename one of them. Cosmetic.

7. delta0 requirements. delta0 must be small enough that B_delta lies in the disk where A, D are C2 and rho is C^(4,1), that A_delta >= A0/2 and kappa >= kappa0/2, and that delta < 1/4 as in proof 212. The phrase "for sufficiently small delta" covers all of these qualitatively. Cosmetic.

8. Natural size, not claimed. The order delta^2 for ||m_delta||_(E_p -> E_p) is the natural one whenever sup|m_delta| is of exact order delta^2, which happens when the quadratic Taylor part of A is nonzero. A high-frequency x-oscillation test like the one in proof 212's sharpness section, placed near an off-axis point where |m_delta| is comparable to delta^2, gives [m h]_x of order delta^2 with ||h|| bounded. The proof explicitly disclaims sharpness, so this is informational only. Both pieces of E_delta are now O(delta^2), and the coupling piece is sharp by proof 212. Any cancellation between -m_delta and q0 B_delta would be an additional claim, and none is made.

9. Integrity. The proof hash and all four dependency hashes in evidence/check.json match the current files. "computation": "none" is accurate. Informational.

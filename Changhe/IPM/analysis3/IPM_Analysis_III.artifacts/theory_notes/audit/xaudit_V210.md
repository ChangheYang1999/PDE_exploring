# Cross-audit of V210: high-space and high-graph conformity of the 78 pure spline columns

Auditor: independent cross-audit, 2026-10-28T14:18Z.

Audited file: verification/proofs/206_pure_spline_high_domain/PROOF.md
SHA256 (computed with sha256sum): de26e2faee4f120c80d67c78fb48a93bf5f6b9a7f09369b57b80f51c73f81238
This is the hash bound in VERIFICATION_RECORD.md V210 and in evidence/final_certificate.json.

Also read: code/check.py, evidence/check.json, evidence/final_certificate.json, evidence/source/basis.py (docstring and q
parameter), section.py (q=3 default), the S1M4P metadata of proof 198, topics 76, 123, 126, 149, 150, 167 (statements), 173,
174 and 198 in full, CONVENTIONS.md, and section 3 and the V210 item of section 9 of S2_BASIS_CERTIFICATION.md (revision of
14:12Z, which already contains the theory author's qualification).

Replay: one exact rational replay in /tmp (under 1 second, nice 19). It parses the 42 coarse knots from check.json, checks
that the 26 interior knots are strictly increasing and distinct from the endpoints, and recomputes the one-sided derivative
jets of all 34 B-splines at t_- and t_+. It uses its own derivative recursion
B'_{i,k} = k/(t_{i+k}-t_i) B_{i,k-1} - k/(t_{i+k+1}-t_{i+1}) B_{i+1,k-1}, not the proof 198 or proof 04 code. Results agree with
check.json: the first nonzero left orders are 0..7 for i=0..7 and none for i>=8; the first nonzero right orders are 7..0 for
i=26..33 and none for i<=25. The thresholds give 6..27 (66 columns) and 7..26 (60 columns). Re-hashing gives check.json
63fff138... and check.py 2b198541..., which match final_certificate.json.

## Verdict

PASS WITH REMARKS. Equations (1) and (2) of the proof are correct: P intersect H_full is spanned by i=6..27, m=1..3
(66 columns), and P intersect D_H(A0) by i=7..26, m=1..3 (60 columns). All 78 columns are low-conforming. I found no
mathematical gap. The remarks concern wording that should be tightened, one provenance detail, and the C^6 qualification
in S2_BASIS_CERTIFICATION.md section 3. As now written by the theory author, that qualification is itself partly inaccurate
(Remark 5).

## Checks

1. Fractional jump threshold and the index cut-offs. CONFIRMED.
   Take a compactly supported piecewise smooth f in one variable that is C^(q-1) and whose q-th derivative has a nonzero
   jump. Then f is in H^s locally exactly for s < q + 1/2. The proof's Gagliardo argument is correct. Near a jump, the
   tau-seminorm of f^(q) is comparable to the double integral of (u+v)^(-1-2 tau) over (0,eps)^2. That integral is finite
   for tau < 1/2 and diverges logarithmically at tau = 1/2. The Lipschitz part of f^(q) is harmless.
   The reduction from two dimensions to one is also valid. For a fixed smooth angular test phi, set
   g(t) = integral f(t,theta) phi(theta) dtheta. Cauchy-Schwarz in the dual angular variable gives
   ||g||_{H^s(R)} <= C ||f||_{H^s} for s >= 0, and g inherits the jump integral J(theta) phi(theta) dtheta. That jump is
   nonzero for a suitable phi when J is nonzero on an open set.
   Jet orders: for a clamped degree-7 knot vector with simple interior knots, t_- has multiplicity 8-i among the local
   knots of b_i (i<=7), so b_i is C^(i-1) there and its first jump is in derivative i. At t_+ the multiplicity is i-25
   (i>=26) and the first jump order is 33-i. Each interior simple knot gives first jump order 7. My replay confirms all of
   these for the archived knots. So the effective first jump order of column i is q_i = min(i, 33-i, 7) for 4<=i<=29.
   Input order: every F_m vanishes quadratically at theta = pi/2 and 3 pi/2, so every h in P has zero vertical cofactor
   trace. Its scalar coordinate is therefore beta = 0, and only the X_s condition applies. That condition is H^(25/4) for
   the cofactor on the vertical sector, and order s(.) <= 25/4 elsewhere. Proof 123 states explicitly that b p w with w in
   H^sigma and zero axis trace lies in X_s.
   Hence membership holds iff 25/4 < q_i + 1/2, that is q_i >= 6, that is 6 <= i <= 27. The converse elimination is
   correct and in the right order. At t_- only b_4..b_7 are present. The 4th-derivative jump is a nonzero multiple of
   sum_m a_(4,m) F_m, which is excluded because sigma > 9/2. Then the 5th-derivative jump is excluded because
   sigma > 11/2. The reflected argument at t_+ removes 29 and then 28. Independence of F_1, F_2, F_3 on any open interval
   follows from analyticity and the distinct top frequencies.
   Graph order: the transport cofactor contains q b_i', whose first jump order is q_i - 1. Membership needs
   25/4 < q_i - 1/2, that is q_i >= 7, that is 7 <= i <= 26. This also holds at interior knots, where b_i' has
   6th-derivative jumps and lies in H^s for s < 13/2.
   Both cut-offs are exact. The low realization needs only continuity (C^1 for an H^1_loc image), so even the C^3 columns
   sp4 and sp29 pass there.

2. No cancellation of the fifth jump for i = 6 and 27. CONFIRMED.
   I re-derived formula (3) independently. With t = log r, V.grad = q d_t + vartheta d_theta, where q = V_r/r and
   vartheta = V_theta/r. Applying V.grad - 1 to e^(3t) p b F and dividing by e^(3t) p gives exactly (3).
   After (1), only b_6 and b_7 are present near t_-. The one-sided Leibniz rule, using b_6^(j)(t_-^+) = 0 for j <= 5, gives
   the jump of the fifth t-derivative of q b' F as q(t_-,theta) b_6^(6)(t_-^+) sum_m a_(6,m) F_m(theta). This holds
   whatever the join regularity of q at t_-.
   The remaining terms are b_6 and b_7 times coefficients in W^(7,infinity) (proof 126: q, vartheta and the divided angular
   coefficients are C^6 with bounded piecewise seventh derivative), plus q b_7' F. All of these are locally in H^6, in fact
   in H^s for all s < 13/2. So they cannot cancel the jump.
   Nonvanishing: on the vertical axis q equals d(t) = V_2(0,e^t)/e^t >= 5.5752 for all t (proof 76, from proof 68). By
   continuity q(t_-,.) is nonzero near pi/2. G is a nonzero trigonometric polynomial with isolated zeros. G vanishes on the
   axis itself, so the obstruction sits on an open sector next to the axis. That is enough, because X_s requires H^sigma
   on the whole sector, not only a trace condition.
   The coupling is genuinely bounded into the target. Proof 123 estimate (9) gives
   ||C_ren h/b||_{H^{s(.)}} + ||chi C_ren h/(b p)||_{H^sigma} <= C ||h||_{X_s} for every h in X_s, not only for h in the
   graph domain. The column m0 lies in Y_H (proof 167). Every Y_H element has vertical-sector cofactor in H^sigma: for
   E Gamma_H the cofactor is gamma/a_H, which is in H^sigma, and for X_s this holds by definition. So A0 h in Y_H would
   force the transport cofactor into H^sigma on the sector, which contradicts the fifth-derivative jump.
   The i=6 and i=27 contributions sit at disjoint endpoints and cannot interact. The resulting domain is consistent with
   the one used in topics 149 and 150: D_H(A0) = E B_H direct-sum D_s, with D_s = {h in X_s : T h in X_s}.
   The forward inclusion (i = 7..26) is sound. q b_i' and b_i times the W^(7,infinity) coefficients are in H^sigma, the
   trace is zero, the divided coefficient (p'/p) vartheta is regular, and the coupling is covered by the same bounded
   estimate.

3. Low conformity of all 78 columns. CONFIRMED.
   The low space of proof 198, w = |cos theta|^(-17/2) exp(mu(t)) with mu = -17t/2 for t < 0 and -5t/4 for t >= 0, is
   exactly setting (O) of proof 173 (a_w = 17/4, beta = 17/2, eta = 5/4).
   The columns have compact radial support and are at least C^3, so the transport image is bounded and compactly
   supported. The angular input is cos^4 Q_m (proof 185). The image keeps fourth-order vanishing at the vertical axis,
   because vartheta F_m' and (p'/p) vartheta F_m vanish quadratically at the cofactor level, and |cos|^8 against
   |cos|^(-17/2) is integrable. The coupling is bounded in the low space (topics 43 and 48).
   The claim is also consistent with the embedding of H_full into the low maximal domain (proof 173), since 66 is a subset
   of 78. Equations (1) and (2) do not affect the low input Gram, as the proof states.

4. Overreach. NONE IN THE PROOF; minor points in the surrounding text.
   The proof computes no high norm, Gram or singular value and says so twice. Its claims are restricted to P. The
   "full image membership" sketch for the forward inclusion (origin cofactor rate r^(2-9/5) = r^(1/5) with
   b = r^(24/5) at 0, and output O(r^(k-5/2)) after division by b = r^(-1/2) at infinity, with k < 5/2) is only
   supplementary. It is consistent with the parameters delta = 9/5 and gamma = -1/2 of proof 173, but the bounded-operator
   theorems of topics 123, 149, 150 and 167 carry the load.
   The verdict wording "A blanket C6 statement for the current basis at ALL radial joins is REFUTED" is a correct
   existential refutation. See Remark 5 for its completeness, and Remark 9 for one phrase in the theory author's section 9 summary.

5. The proposed qualification of the "C6 joins" wording. CORRECT FOR THE PURE COLUMNS, BUT INCOMPLETE; see Remark 5.
   For the pure columns, the statement "C^6 at interior simple knots, only C^3 at the zero-extension endpoints for sp4 and
   sp29" is true. It is backed by the 884 exact joins and the exact endpoint jets. The full statement is that the
   zero-extension end is C^(q_i - 1): C^3 for sp4/sp29, C^4 for sp5/sp28, C^5 for sp6/sp27, C^6 for sp7/sp26, and
   identically zero near that end for the others.

## Remarks

1. Multiplier regularity in the non-membership step. The jump lemma is stated for smooth multipliers ("Smooth positive
   multipliers do not change the first jump order"), but it is applied with q, vartheta and the divided coefficients,
   which are only W^(7,infinity) (proof 126). The sentence "The other transport terms are C5 there, so cannot cancel that
   fifth jump" is also slightly loose, since C^5 alone does not imply H^(11/2) membership. Both are fixed in one line.
   Write q = q(t_-,theta) + (t - t_-) Q with Q in W^(6,infinity). Then (t - t_-) Q b_6' F and the b-times-coefficient
   terms lie in H^6 locally. The leading piece q(t_-,theta) b_6'(t) F(theta) is a smooth angular function times a
   one-variable function whose first jump is at order 5, so it is not in H^(11/2) on the sector where q(t_-,.)G is
   nonzero. This is a wording gap, not a mathematical one.

2. Provenance. evidence/check.json records proof_sha256 2d544aaa..., which is an earlier revision of PROOF.md: the
   exact-result paragraph was added after the 13:59:10 run. final_certificate.json binds the audited de26e2fa..., and the
   check.json and check.py hashes match it. The computed data do not depend on the proof text, so this is acceptable. A
   future replay could record both hashes explicitly.

3. Structural, not coincidental, equality. The graph test q_i - 1/2 > 25/4 is the same inequality as q_i + 1/2 > 29/4.
   So the 60-column graph set is exactly what one would get by wrongly applying the scalar order 29/4 to the inputs. The
   proof is right to insist that the zero trace makes the input order 25/4. That distinction is exactly what makes the
   66-column input set differ from the graph set. Readers should not cite the 60-set as the H_full set.

4. Use of the 66 versus 60 subspaces. The theory author's section 9 sentence "A high-norm certificate on this section must use the
   60-column subspace" is correct for anything that involves A0 h in Y_H, such as output norms or graph-norm singular
   values. A pure H_full input Gram may use all 66 columns.

5. C^6 wording in S2_BASIS_CERTIFICATION.md section 3 (revision 14:12Z). The theory author inserted "This concerns that jet-joined
   basis." That sentence implies the C^6 claim is right for the jet-joined columns, which is not true at t_- and t_+.
   - The producer basis.py (default q=3 in section.py; the numerics S2_BASIS_CERTIFICATION 2.3 and
     S2_NUMERICAL_CERTIFICATES C6 both record q = 3 for the 169 conforming columns) joins the extended splines and the
     inner and outer power-law columns by matching only the q-jet. vander_solve imposes derivatives n = 0..q.
   - Its own docstring says "Every function is C^q at t_-, t_+ (exactly), C^6 at the coarse knots".
   - So the jet-joined basis is C^6 at interior coarse knots. The J column is C^6 at t_- and the cutoff chi is C^6.
     Elsewhere at t_- and t_+, only C^3 is guaranteed.
   - This is harmless for the H^1-type conformity of V014, which needs C^1 (the docstring requires q >= 2). It does mean
     the original section 3 sentence was already an over-statement for that basis, not only for the later pure section.
   Suggested wording: "C^6 at the interior coarse knots; at t_- and t_+ the jet-joined columns are matched to order q = 3
   (C^3), J excepted (C^6 at t_-); the zero-extended pure columns sp_i are C^(min(i,33-i)-1) at their ends, i.e. C^3,
   C^4, C^5 for i = 4, 5, 6 (and 29, 28, 27)." I did not check whether particular jet-joined columns happen to match
   beyond order 3. By construction they need not.

6. Scope with respect to the other columns of S1M4P. V210 classifies only the 78 pure columns. The remaining 91 columns of
   the 169-column S1M4P section (labels sp0+in, ..., out9, col_m 0..3) use cos(2 m theta) or m = 0. They therefore have
   nonzero vertical cofactor trace, so the scalar order 29/4 of B_H would apply to their axis coordinate, and they are
   only C^3 at t_- and t_+. Their high-space status is untouched by V210 and would need a separate argument. This is an
   observation, not a verified claim.

7. Notation. The letter q is used for the radial transport coefficient, for the jump order in the lemma and in
   check.py, and in the producer for the jet order (q=3). The proof stays unambiguous in context, but a different symbol
   for the jump order would help.

8. The proof's dependency list (50, 76, 123, 126, 140, 167, 173, 174, 198) is adequate. The load-bearing facts I traced
   are: proof 123 (9) for the coupling bound on all of X_s; proof 126 for the W^(7,infinity) coefficients and divided
   components; proof 76 for d >= 5.5752; proof 149 for the definition of D_s; proof 167 for m0 in Y_H; and topics 173 and
   174 for the exact spaces and A0. All match the uses in the proof.

9. In the theory author's section 9 summary, "b_i vanishes to exact order i at t_- and to order 33 - i at t_+" should be
   restricted to i <= 7, resp. i >= 26. For other i the spline vanishes identically near that end. The derived
   "C^(i-1) at the left end, C^(32-i) at the right end" is true for all i but sharp only in those ranges.

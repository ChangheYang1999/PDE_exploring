# Audit of the three axis-obstruction proofs

**Bottom line.** All three arguments are correct. I reconstructed each step by hand and found no counterexample. The defects are presentational: a quantifier-order slip in the third file, a symbol clash in the second, and a few under-stated steps. Corrections are given at the end of each section.

## 1. origin-fixed-source (dependency)

**Base asymptotics.** Near 0 we have w₀ = −Ax + O(x³), so (w₀′−A)/w₀ = 2/x + O(x). With the normalization this gives g₀ = x²h(x).

- The function h is even, analytic and positive. The reason is that d log(g₀/x²)/dx is odd analytic.
- Then m₀ = (A/x)(1+O(x²)) and W₀ = A^(β−2) x^(−β)(1+O(x²)).
- Also Q₀ ≈ (2x + 2A)/(2x⁶ + …), so Q₀ ~ A x^(−6) at worst. To leading order it is a Laurent series with odd and even powers starting at x^(−6). The claim "x^(−5) in steps of two" is slightly off when w₀″(0) is involved. For odd w₀, w₀″ = O(x), so Q₀ = O(x^(−5)) and the claim holds.
- Every power in Q₀W₀ and in Q(L)W₀ is shifted by the non-integer −β. So no x^(−1) term appears, there are no logarithms, and no finite-part constant arises. Confirmed.

**Layer p_N.**
- Each x-derivative of χ(log(r₀/x)) costs a factor x^(−1), uniformly in N.
- χ is flat at 0, so p_N is smooth after extension by zero.
- Bound (5) holds to every order, not only i ≤ 2.

**Bound (6).** log(1+p/w₀) = O(x^(6+β)/N). The integral ∫₀ˣ p/w₀² is also O(x^(6+β)/N). Derivatives follow the same pattern. Confirmed.

**Integrand difference.** The leading term is −p″/(2g₀³)·W₀ = −(A^(β−2)/2) p″ x^(−6−β).

The error terms, checked one by one:

| Error source | Size |
|---|---|
| δg′/(2g³)·W | x^(7+β)·x^(−6)·x^(−β)/N = x/N |
| Q₀·δW | x^(−5)·x^(−β)·x^(6+β)/N = x/N |
| O(x²) correction | x/N |
| Q(L) shift | x^(−β)/N |
| Quadratic terms | smaller still |

The key point is that every error is pointwise bounded by an integrable envelope that is independent of the log-length N of the support. The only O(1) contribution is the leading term, and it is exact. Confirmed.

**Constant.** (β−1)A^(1−β)/3 · (−A^(β−2)/2) = (1−β)/(6A).

- Integrating by parts twice gives (x^(−6−β))″ = (6+β)(7+β) x^(−8−β), with zero boundary terms because the support is compact and p is flat.
- With dt = −dx/x, ∫ p x^(−8−β) dx = (a/N)∫₀^(N+2) χ(t)χ(N+2−t) dt = (a/N)(N + 2∫₀¹χ).
- So κ_A and formula (8) are correct.

**Interior correction.**
- J′(0) = −∫f/w₀² < 0.
- I_N = O(1/N), because the integrand is x^(5+β)/N.
- The supports are disjoint, so the reciprocal differences add exactly. Hence g_N = g₀ on [c, L].
- The comparison on [c, L] uses λ^(−2), λ^(−3) and λ^(1−β), with the endpoint value subtracted first. This gives the envelope (L−x)^(β−1)/N. Confirmed.

**Verdict: correct.**

## 2. finite-observation-fibers (exact target via the intermediate value theorem)

**Uniformity in a ∈ [−M, M].**
- Every estimate is in |a|/N. The pointwise envelopes do not depend on N.
- The positivity and invertibility thresholds depend only on M/N.
- So the constant C_M and the threshold N₀(M) are legitimate.

**Inverse map.** One fixed inverse neighborhood of J serves all |a| ≤ M. The map a ↦ t_N(a) = J^(−1)(−I_N(a)) is smooth, since I_N is smooth in a on a fixed compact support where w₀ is bounded away from 0.

**Continuity in a at fixed N.** This is valid, and it is the crux of the argument.
- All w_(N,a) coincide with w₀ on (0, r₀e^(−(N+2))). That neighborhood is independent of a.
- They also coincide with w₀ on [c₀, L], so Q(L) is independent of a.
- Therefore B[w_(N,a)] − B[w₀] is an ordinary integral over a fixed compact subinterval of (0, L).
- On that interval the integrand is jointly continuous in (x, a), and its denominators w and g are bounded away from 0.
- So no global continuity of B is needed.

**IVT bookkeeping.** With error < 1/2:
- B(a₋) ≤ B₀ + D − 1 + 1/2 = b − 1/2.
- B(a₊) ≥ b + 1/2.

M is chosen after the target b, and N is chosen after M and ε. This order is consistent. The case a = 0 (no perturbation) is included and harmless.

**Observation consequence.** It is correct as stated, for exact local agreement on [δ, L] and near 0.

**Corrections.**
- The target b clashes with b, b₀ used for the support of f. Rename one of them.
- Formula (6) inherits the explicit factor 1 + (2/N)∫χ. This is fine, but state that it is absorbed into C_M/N using |a| ≤ M.

**Verdict: correct.**

## 3. critical-holder-origin (C^(7,β) and C^(8,β) estimates)

**Weighted lemma.**
- Case h ≥ x/2: the bound is (2^β + 3^β)e h^β.
- Case h < x/2: the bound is e·h·x^(β−1) ≤ e·h·(2h)^(β−1) ≤ e h^β, using x > 2h and β − 1 < 0.
- Pairs including x = 0 follow from the amplitude bound.
- Correct and uniform in the vanishing neighborhood.

**Derivative orders for w.**
- C^(7,β) needs |p^(7)| ≲ x^β/N and |p^(8)| ≲ x^(β−1)/N, so j ≤ 8 suffices. The stated j ≤ 9 is harmless.
- The orders j < 7 are bounded because the exponent 7 + β − j > 0.
- The f-term contributes |t_N|·‖f‖ = O_M(1/N). Confirmed.

**Derivative orders for g.** C^(8,β) needs (g−g₀)^(8) ≲ x^β/N and (g−g₀)^(9) ≲ x^(β−1)/N, so j ≤ 9 is required and is supplied.

- **σ = p/w₀.** Write w₀ = x·v with v(0) = −A ≠ 0. By Leibniz, p^(j−i)·x^(−1−i) gives x^(6+β−j). Confirmed for j ≤ 9; this needs p to order 9, which is available.
- **log(1+σ).** By Faà di Bruno, a term with q factors is bounded by N^(−q) x^(q(6+β)−j) ≤ N^(−1) x^(6+β−j), using x < 1. Here 1+σ is bounded below uniformly because |σ| ≲ M x^(6+β)/N.
- **Reciprocal difference.** −p/(w₀²(1+σ)) is of order x^(5+β−j) for j ≤ 8. Integrating it gives η^(j) ~ x^(6+β−j) for j ≤ 9.
- **e^η − 1.** It satisfies the same bounds.
- **Leibniz with g₀ = x²h.** Write the term as g₀^(i)·(e^η−1)^(j−i):
  - For i = 0 and i = 1, the powers are x²·x^(6+β−j) and x·x^(7+β−j). Both equal x^(8+β−j).
  - For i ≥ 2, g₀^(i) is bounded and the term is x^(6+β−j+i) ≤ x^(8+β−j).
  - So (4) holds on (0, r₀].
- **On [r₀, L].** The difference is (λ−1)g₀ before b₀, with an O(1/N) correction on [b₀, c₀], and zero after c₀. All C⁹ norms are O_M(1/N). Since x^(8+β−j) is bounded below there, (4) extends to the whole interval. The lemma with k = 8 applies.

**Uniformity in a.** As in file 2, all constants depend only on M. The bounds are uniform on [−M, M].

**Correction (quantifier order).** The last paragraph picks a_N and then says "choose N still larger". As written, this would change the family. Fix it as follows:
1. Choose N once, large enough that the error in (1) is < 1/2 and C_M/N < ε/2 in both (2) and (5).
2. Then apply the IVT at that N.

Since (2) and (5) are uniform in |a| ≤ M, the resulting a_N satisfies all the bounds.

**Minor nits.**
- The symbol f is used both for the lemma's generic function and for the fixed bump. Rename one.
- The scope sentence is accurate. No uniform analyticity is claimed, and none is supplied.

**Verdict: correct after the quantifier reordering.**

## Overall

| Proof | Verdict | Fix needed |
|---|---|---|
| 1. origin-fixed-source | Correct | None beyond the Q₀ Laurent remark |
| 2. finite-observation-fibers | Correct | Notational |
| 3. critical-holder-origin | Correct | Reorder the choice of N before applying the IVT |

The key mechanisms verify:
- an exact log-length cancellation giving a·κ_A;
- error envelopes that are integrable independently of N;
- exact causality of the normalized ODE combined with the reciprocal-integral constraint, which fixes the source germ;
- continuity in a at fixed N, coming from a common compact interval of difference.

No counterexample was found.

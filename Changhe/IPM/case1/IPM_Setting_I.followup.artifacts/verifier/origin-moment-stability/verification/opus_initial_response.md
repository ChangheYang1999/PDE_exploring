# Review of `verifier/origin-moment-stability/PROOF.md` (origin-moment stability and the Dini control)

## Verdict

The theorem is **correct as stated, up to one bookkeeping repair** in the source-correction part. I reconstructed every estimate. My answers to the three questions:

1. **Remainder in (2) over many decades.** The O(e) remainder does not fail when the support spans arbitrarily many logarithmic decades.
2. **Source correction.** The exact correction preserves the bound, with constants that must be allowed to depend on f, b and c.
3. **Dini criterion.** (5) and (6) follow with no extra endpoint assumptions.

## 1. Base structure and the finite part

- **Base expansions.** (w_0'−A)/w_0 is odd with simple-pole residue (−2A)/(−A) = 2. So g_0 = x²·(even analytic), and:
  - Q_0 = x⁻⁵·(even), since g_0' and w_0'' are odd.
  - W_0 = (−w_0)^(β−2) g_0^(1−β) = x^(−β)·(even).
- **Finite part is well defined.** The integrand (Q_0 − Q_0(L))W_0 has the powers x^(−5−β+2k) and x^(−β+2k). No x⁻¹ term occurs because β ∉ ℤ, so there is no logarithm.
- **Linearity of the finite part.** The finite part is linear. Both traces coincide near 0, and the only change there is the term −ΔQ(L)·W_0 = O(e x^(−β)), which is integrable. Hence the difference of finite parts equals an ordinary integral, as claimed.
- **Behaviour at L.** Q_0 is smooth at L because g_0(L) > 0. With W_0 ~ s^(β−2), the product is O(s^(β−1)), which is integrable.

## 2. Estimate (2) and its uniformity

**Density bounds (7)–(9).** These check out. With |v^(i)| ≤ e x^(7+β−i):
- v/w_0 = O(e x^(6+β)).
- The reciprocal difference is −v/(w_0(w_0+v)) = O(e x^(5+β)).
- The derivative of the reciprocal difference is O(e x^(4+β)).
- Hence η^(i) = O(e x^(6+β−i)), g_hat − g_0 = O(e x^(8+β)), and g_hat' − g_0' = O(e x^(7+β)).

Past the support, η is the constant −A·I. This is consistent with (9).

**The key size count.** The leading term is v''·g_0⁻³·W_0, of size e x^(5+β)·x⁻⁶·x^(−β) = **e/x**. This is the only piece that is not uniformly integrable: it grows like e times the number of decades. The proof keeps it *exactly* and converts it to κ_A M(v). Every other term is uniformly integrable:

| Term | Size |
|---|---|
| O(x²) correction of g_0⁻³W_0 | e x |
| δQ·W_0 (δg', denominator, w_0''·δ(g⁻³)) | e x^(1+β)·x^(−β) = e x |
| Q_0·δW, using δW = W_0·O(e x^(6+β)) = O(e x⁶) | e x |
| ΔQ(L)·W | e x^(−β) |
| Quadratic terms | e² x^(5+β) |

**Tail and constant.**
- On [r_0, L], formula (13) is exact: g = λg_0 and W_hat = λ^(1−β)W_0. After subtracting the values at L, the integrand difference is O(e(L−x)^(β−1)).
- The constant checks: ((β−1)/3)·A^(1−β)·(−A^(β−2)/2) = (1−β)/(6A).
- The two integrations by parts have no boundary terms and produce the factor (6+β)(7+β). This gives κ_A.

**Counterexample search.** Take v = ε x^(7+β) times a smooth cutoff spread over N decades. Then e ≍ ε, while M ≍ ε N, which is unbounded relative to e. Estimate (2) correctly isolates this growth in M. The remainder stays O(e) because all remaining terms carry at least x^(1−β)-type integrable weights. I found no failure.

## 3. Source correction (3)

- J'(0) = −∫ f/w_0² < 0, so the implicit function theorem gives a locally unique t with J(t) = −I and |t| ≤ Ce.
- The supports are disjoint, so the reciprocal differences add. Then η ≡ 0 on [c, L] by (7).
- The comparison with the uncorrected pair splits into three regions:
  - On [0, b] the two pairs coincide except for Q(L), contributing O(e)·∫W.
  - On [b, c] there is a C² change of size O(e).
  - On [c, L] the difference is base versus λg_0, bounded via (13).

All of this is correct.

**Necessary repair.** The constants in (3), and the decreased e_*, depend also on f, b and c. Examples are the lower bound on |J'(0)|, the C² norm of f, and inf |w_0| on [b, c]. The statement says C and e_* depend "only on the fixed base, A and r_0". This should be amended to include (f, b, c) for (3), and for the corrected case of (5). Uniqueness of t should also be stated as uniqueness within a fixed neighbourhood of 0.

## 4. Dini criterion (5) and (6)

- **Taylor step.** The Taylor formula for v^(i) with kernel (x−s)^(6−i)/(6−i)! is exact, because v vanishes near 0. Since ω_v is nondecreasing, the bound |v^(i)(x)| ≤ c_(i,β) ω_v(x) x^(7+β−i) follows.
- **Consequences.** This gives e(v) ≤ max_i c_(i,β)·ω_v(r_0) and |M| ≤ c_(0,β)∫ω_v dx/x. Then (5) follows from (2) and (3) under e ≤ e_*.
- **Sequences.** D_β(v_n) → 0 forces ω_{v_n}(r_0) → 0. So e(v_n) ≤ e_* holds eventually, and B[w_n] → B[w_0].
- **Endpoint assumptions.** None are needed. At 0, compact support gives vanishing derivatives. At r_0, ω only involves sup over (0, x].
- **Hölder bound (6).** Using v^(7)(0) = 0, we get ω_v(x) ≤ [v^(7)]_γ·x^(γ−β). Integrating gives exactly r_0^(γ−β)(1 + 1/(γ−β)), for β < γ ≤ 1.
- **Compatibility with the critical-Hölder case.** At γ = β, ω_v stays bounded but ∫ω_v/x need not be small. This matches the critical-Hölder cutoff remark.

## Summary of repairs

1. **Required:** in (3) and the corrected case of (5), allow C and e_* to depend on f, b and c, and state that t is locally unique.
2. **Optional:** record that the finite part has no log term because β ∉ ℤ.
3. **Optional:** note explicitly that M(v) is not O(e), so (2) alone does not give continuity in e; it is (5) that does.

With repair 1, the stated theorem is proved.

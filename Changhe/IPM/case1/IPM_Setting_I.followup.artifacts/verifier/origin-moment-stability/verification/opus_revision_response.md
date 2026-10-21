# Review of `verifier/origin-moment-stability/PROOF.md` (revised)

## Verdict

**Accept.** The revision resolves exactly the two issues from the previous review, and it changes nothing else:

1. **Constant dependence.** The constants for the source-corrected construction may now depend on f, b and c. This covers C and e_* in (3), and C in the corrected case of (5).
2. **Uniqueness of t.** Uniqueness is now stated in a fixed neighborhood of zero. This means a t-neighborhood fixed once f is chosen, and independent of v.

I rechecked every estimate independently and found no remaining mathematical gap. The JSON's claim that "no mathematical estimate or endpoint conclusion changed" is accurate.

## Independent reconstruction

### Base asymptotics, eq. (8)
- The ODE gives (log g)' = (w'−A)/w. With w_0 = −Ax(1+O(x²)) odd analytic, (w_0'−A)/w_0 − 2/x is odd analytic. Its integral is even and vanishes at 0, so g_0 = x²(1+O(x²)), and g_0 is even analytic.
- From this, m_0 = (A/x)(1+O(x²)) and W_0 = (−w_0)^(β−2) g_0^(1−β) = A^(β−2) x^(−β)(1+O(x²)).
- Q_0 = O(x^(−5)). Its numerator g_0'−w_0'' is odd and its denominator g_0³ is even.
- **The finite part is well defined with no log term.** The base integrand Q_0W_0 expands in powers x^(−5−β+2k). None of these equals x^(−1), because β ∉ ℤ. The Q_0(L)W_0 piece is O(x^(−β)), which is integrable.
- So the "no added constant" FP convention is unambiguous. A difference of finite parts equals the ordinary integral whenever the singular parts coincide.

### Formula (7) and estimates (9)
- (7) follows because ∫w'/w = log|w|. The normalization holds because v vanishes near 0, so η ≡ 0 there.
- With |v^(i)| ≤ e x^(7+β−i) and w_0 ≤ −cx on (0,r_0]:
  - v/w_0 = O(e x^(6+β)).
  - The reciprocal difference −v/(w_0(w_0+v)) = O(e x^(5+β)), and its derivative is O(e x^(4+β)).
- Hence η^(i) = O(e x^(6+β−i)) for i = 0, 1, 2.
- g−g_0 = g_0(e^η−1) = O(e x^(8+β)).
- g'−g_0' = g_0'(e^η−1) + g_0η'e^η = O(e x^(7+β)).
- All constants are uniform in the inner support radius.

### Tail, eqs. (10) and (13)
- On [r_0, L] we have v = 0, so η = −AI is constant and |I| ≤ C∫x^(5+β)e ≤ Ce. This gives exactly λg_0 and the λ-scalings in (13).
- G − G(L) and V − V(L) are O(L−x), since g_0(L) > 0.
- W_0 = O((L−x)^(β−2)), so the integrand difference is Ce(L−x)^(β−1).

### Expansion (11)
I decomposed Q̂−Q_0 as:
- −v''/(2ĝ³), plus
- (ĝ'−g_0')/(2ĝ³) = O(e x^(1+β)), plus
- (g_0'−w_0'')(ĝ^(−3)−g_0^(−3)) = O(x · x^(−6) · e x^(6+β)) = O(e x^(1+β)).

Swapping ĝ³ for g_0³ in the v'' term costs O(e² x^(5+2β)). For W, Ŵ/W_0 = (1+v/w_0)^(β−2)(ĝ/g_0)^(1−β) = 1 + O(e x^(6+β)), so Ŵ−W_0 = O(e x⁶). This needs only a mean-value bound, not differentiation; the conclusion is unaffected.

### Integrand difference (12)
Expanding fully, there is one extra term the text does not list: −Q_0(L)(Ŵ−W_0) = O(e x⁶). It is harmlessly covered by E. The remaining terms are as stated:
- (Q̂−Q_0)W_0
- Q_0(Ŵ−W_0) = O(e x)
- the cross term O(e² x^(5+β)), using v''/g_0³ = O(e x^(β−1))
- −(Q̂(L)−Q_0(L))Ŵ = O(e x^(−β))

### Main term
- The prefactor is (β−1)A^(1−β)/3 · (−A^(β−2)/2) = (1−β)/(6A).
- Two integrations by parts give (x^(−6−β))'' = (6+β)(7+β)x^(−8−β). This recovers κ_A.
- The leading term is genuinely only O(e·log) in size. It is kept exactly as M(v), not absorbed into C·e. That is the point of the theorem, and it is handled correctly.

### Source correction
- J'(t) = −∫f/(w_0+tf)² < 0 wherever w_0+tf < 0 on [b,c], so J is strictly decreasing there. Uniqueness therefore holds on the whole admissible t-interval, not just in some neighborhood; it is not fragile.
- The supports are disjoint, so I+J(t) = 0 is equivalent to η ≡ 0 on [c,L].
- |t| ≤ Ce, with C ~ 1/|J'(0)|, and negativity requires |t|·sup f < min_[b,c]|w_0|. Both depend on f, b, c. This is precisely what the revised statement now allows.
- The three-region comparison of corrected and uncorrected pairs is correct:
  - (0,b): only the Q(L) constants differ, by O(e), against integrable W.
  - [b,c]: smooth O(e) changes on a fixed compact interval.
  - [c,L]: the λ-tail bound applies.

### Dini part
- The Taylor formula is valid because all derivatives of v vanish at 0. It gives |v^(i)(x)| ≤ c_(i,β) ω_v(x) x^(7+β−i), where c_(i,β) is a finite Beta-integral constant.
- Hence e ≤ max_i c_(i,β) ω(r_0) and |M| ≤ c_0∫ω dx/x, which gives (5) under e ≤ e_*.
- D→0 forces ω(r_0)→0, so the hypothesis e ≤ e_* eventually holds.
- (6) checks: since v^(7)(0) = 0, ω(x) ≤ [v^(7)]_γ x^(γ−β), and integrating gives r_0^(γ−β)(1 + 1/(γ−β)).

### Counterexample search
- **Log-long cutoffs** with critical C^(7,β) norm → 0 but M ↛ 0 do not violate (5). Their ω_v is small pointwise, but ∫ω dx/x is not.
- **Any v with e ≤ e_*** keeps negativity and positivity of g.
- **Support placement:**
  - Placing v near the source would break the disjoint-support step, but it is excluded since r_0 < b.
  - Placing v near L is excluded by supp v ⊂ (0,r_0).

No counterexample to (2), (3), (5) or (6) arises within the stated class.

## Conclusion

The revised statement correctly records the f, b, c dependence of e_*, C and the t-neighborhood. This is exactly the dependence the inverse-function step requires, and the proof's arguments are unchanged and valid. I find no remaining mathematical gap in the stated scalar-trace result.

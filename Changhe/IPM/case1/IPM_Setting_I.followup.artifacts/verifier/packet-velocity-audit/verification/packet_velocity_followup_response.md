# Verdict on the full-vector velocity and constant-gauge proof

**Verdict: correct as stated.** I independently reconstructed all four priority items and found no counterexample and no sign error. My only remarks are minor sharpenings, listed at the end.

## 1. Full-vector signs

Write E = e^{istr^A}, z = t²r^q, f = (1+z)^{-b} and f₁ = (1+z)^{-b-1}.

**Divergence.**
- ∂_s of the (3) integrand is 2i c_F r^{2A-3} ∫ t²Φ E cos(yr) f₁.
- ∂_y of the (2) integrand is −2i c_F r^{q-1} ∫ t²Φ E cos(yr) f₁.
- Since q−1 = 2A−3, the divergence vanishes for every truncation.

**Curl.**
- ∂_s U₂ = 2c_F r^{q+A-2} sin(yr) ∫ t³Φ E f₁. Using r^{q+A-2}t³ = r^{A-2}·t·z, this is 2c_F r^{A-2} sin ∫ tΦ E z f₁.
- −∂_y U₁ = 2c_F r^{A-2} sin ∫ tΦ E f₁.
- Their sum is 2c_F r^{A-2} sin ∫ tΦ E f, because (z+1)f₁ = f.
- From (1), ∂_s v = 2i·i c_F r^{A-2} sin ∫ tΦ E f, which is exactly the negative of that sum.
- Hence ∂_sU₂ − ∂_yU₁ = −∂_s v. ✓

**Reality.** The constraint Φ(−t) = −Φ̄(t) gives Φ̄(t) = −Φ(−t).
- Conjugating the inner integral of (3) and substituting t → −t returns the same integral, so U₁ is real.
- The inner integral of (2) changes sign under the same operation, so it is imaginary, and U₂ (with its −2i prefactor) is real. ✓

**Parity.**
- U₁ is even in y because of cos(yr); U₂ is odd in y because of sin(yr).
- For Φ = iφ with φ real and even:
  - tΦ is odd, so only the −sin(str^A) part of E survives in U₁. The subtracted term ∫tΦf₁ = 0, so U₁ is odd in s.
  - t²Φ is even, so only cos(str^A) survives in U₂, which is therefore even in s.
  - v keeps only cos(str^A), so v is even in s.
- These parities kill both constant components, as claimed. ✓

## 2. Convergence for all A > 1

**Low frequency.**
- |E cos − 1| ≤ C(r^A + r²) on compact physical sets.
- In (3) this gives the weight r^{2A-3} + r^{A-1}. Both exponents exceed −1 exactly when A > 1.
- In (2), |sin(yr)| ≤ C r gives the weight r^{q-1}, and q − 1 > −1.

**High frequency.**
- f₁ ~ r^{-g-q}.
- This gives r^{A-3-g-q} = r^{-A-1-g} in (3) and r^{-2-g} in (2). Both are integrable at infinity.

The dominated-convergence and truncation argument for the distributional identities (4) is sound. It relies on the dependent locally uniform convergence of v.

## 3. Sublinear growth and uniqueness

**Growth estimates.** I re-derived the split integrals:
- S term: ∫₀¹ r^{A-3} min(1, Sr^A) dr ~ S^{(2-A)/A} for 1 < A < 2.
- Y term: ~ Y^{2-A} for 1 < A < 2.
- U₂: ~ Y^{1-q} for 0 < q < 1.
- Endpoints: each becomes logarithmic at its endpoint (A = 2 or q = 1) and bounded beyond it.
- Every exponent is below 1, since A > 1 and q > 0.

**Liouville step.**
- A difference H of two solutions satisfies ΔH = 0 componentwise.
- Mollifying preserves the growth bound.
- The interior gradient estimate gives |∇H_ε| ≲ R^{κ−1} → 0, so H is constant.

**Gauge.**
- The normalization H(0) = 0 fixes the constant.
- Alternatively, oddness of H₂ in y and oddness of H₁ in s fix it.
- The stream-function term λsy produces a linearly growing velocity and is correctly excluded. ✓

## 4. The A > 2 decay and the moment criterion

**Decay for A > 2.**
- Under ξ = t r^A, the frequency L¹ norm of U₁^dec is ∫ r^{A-3} ∫ |tΦ| f₁ dt dr, which is finite for A > 2.
- The analogous norm for U₂ is ∫ r^{q-2}, finite iff q > 1.
- Riemann–Lebesgue then gives decay at infinity.
- The difference between U₁^dec and (3) is the convergent constant 2c_F ∫ r^{A-3} ∫ tΦ f₁. ✓

**Moment criterion for 1 < A ≤ 2.**
- The origin integrand expands as Σ d_k m_k r^{A-3+kq}.
- The coefficients d_k are nonzero because b > 0, and the exponents are distinct.
- Let k be the smallest index with m_k ≠ 0 and A − 2 + kq ≤ 0. Its power (or a logarithm, in the equality case) dominates and cannot be cancelled by the higher terms.
- So condition (8) is both necessary and sufficient at the origin.
- At any other point, the bare integrand equals the anchored integrand plus the origin integrand. The anchored part converges, so the criterion is the same everywhere. ✓

**Counterexample.**
- Φ = tχ, with χ ≥ 0 smooth, even and supported away from 0, satisfies Φ(−t) = −Φ̄(t) and ∫Φ = 0.
- Its first moment is m₀ = ∫ t²χ dt > 0, so the bare first-velocity integral diverges for every 1 < A ≤ 2.
- In the imaginary-even subspace, tΦ is odd, so every m_k = 0 and the origin integral ∫tΦf₁ vanishes identically. ✓

## Minor corrections and sharpenings (none affect the conclusions)

1. **Wider decay range for U₂.** The L¹ decay argument for U₂ needs only q > 1, that is A > 3/2, not A > 2. The text's "in this range" is true but not sharp.
2. **Wording of the growth bound.** The phrase "chosen logarithmic majorant" is clearer as: for A = 2 or q = 1, any fixed κ ∈ (0, 1) works.
3. **Status of the s-parity gauge.** The alternative gauge via s-oddness of H₁ is available only in the centered imaginary-even case. The text implies this, but it should state it explicitly next to the uniqueness claim.
4. **Remaining dependency.** The distributional passage to (4), and hence the whole claim, still depends on the locally uniform convergence of the truncated v from ../packet-dyadic-audit. This review does not verify that dependency, so the OPEN status regarding it is appropriate.

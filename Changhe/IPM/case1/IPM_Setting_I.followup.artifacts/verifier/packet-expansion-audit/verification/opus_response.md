# Review: finite-part expansion of the frozen Fourier packets

**Verdict: accepted, with one small gap.** The gap is the smoothness of u_k away from the origin (claim 1). It is not explicitly proved, but it follows from an estimate already in the companion proof; the fix is given below. I found no counterexample, and every sign and factor checks out. I recomputed each step independently, as follows.

## 1. Expansion of the density

- **Rewriting the amplitude.** Since ξ²/η² = t²r^{2A−2} = t²r^q, we get (1+t²r^q)^{−b} = |t|^{−2b} r^{−qb} (1+z)^{−b}, with z = t^{−2}r^{−q}.
- **Power of r.** Using qb = g, the total power is r^{−A−2−g}. This equals r^{−Q−h}, because Q+h = A+2+g.
- **Binomial series.** The coefficients of (1+z)^{−b} are (−1)^k(b)_k/k!, which matches c_k.
- **Shifted exponents.** z^k = t^{−2k}r^{−qk} gives h_k = h+kq. Formula (11) is correct.

## 2. Pairing and Taylor expansion (5)

- **Jacobian.** dξdη = r^A dt dr, so the exponent is r^{−Q−H+A} = r^{−H−1}. Correct.
- **Coefficients.** The monomial ξ^aη^c contributes t^a r^{Aa+c}(±1)^c ∂^a∂^cφ(0)/(a!c!). The two η signs give a factor 2 for odd c and cancel even c. This gives exactly M_{k,a,c}.
- **Irrational A.** Every retained weight Aa+c ≤ H forces a+c ≤ H < L, so all retained terms lie in the degree-(L−1) Taylor polynomial.
- **Remainder.** The Taylor remainder is O(|X|^L) = O(r^L) on the fixed t-support. The dropped terms of degree below L have weight greater than H, and there are finitely many of them. So δ > 0 is correct, and no rationality of A is needed.

## 3. Equivalence of (6) and (7)

For λ < H, ∫_ε^1 r^{λ−H−1} dr = (1−ε^{λ−H})/(λ−H), and ∫_ε^1 r^{−1} dr = −log ε.

Substituting these into (6) and cancelling the constant terms leaves:

- −Σ C_λ ε^{λ−H}/(H−λ), and
- +C_H log ε.

This matches (7), including the sign of the logarithmic term.

## 4. Scaling identity (8)

- J_{φ_μ}(r) = J_φ(μr) and C_λ(φ_μ) = μ^λ C_λ(φ). Both verified.
- Substituting ρ = μr maps ε to ε' = με. The power subtractions become μ^H C_λ ε'^{λ−H}.
- The logarithm becomes μ^H C_H [log ε' − log μ]. This gives (8) exactly.

**Fourier side.** I checked directly that F(u∘δ_μ) pairs with φ as ⟨E_k, φ_μ⟩. The Jacobians μ^{−Q} and μ^{Q} cancel. Hence P_k = −F^{−1}Res_k.

## 5. Sign and Fourier factors in (3)

- **Functional.** Res(φ) = Σ M ∂^αφ(0) = ⟨Σ M (−1)^{|α|} ∂^αδ, φ⟩.
- **Inverse transform.** F^{−1}(∂^αδ) = c_F ⟨∂^αδ, e^{iX·ζ}⟩ = c_F (−iX)^α.
- **Product of signs.** (−1)^{|α|}(−i)^{|α|} = i^{|α|}, so P_k = −c_F Σ M i^{a+c} s^a y^c. This confirms (3).
- **Reality.** The symmetry Φ(−t) = −conj Φ(t) gives conj M = (−1)^{a+1} M. For odd c, conj i^{a+c} = (−1)^{a+1} i^{a+c}. The product is therefore real, so P_k is a real polynomial. Confirmed.

## 6. The obstruction cannot be cancelled

- Two extensions differ by Σ ∂^αδ. The inverse transform of this is a polynomial p.
- Requiring the corrected field to be homogeneous gives (9).
- In weight-H monomials the left side vanishes identically, while the right side is −μ^H log μ times the nonzero coefficients of P_k.
- So a nonzero resonant moment cannot be removed by any change of extension, resonant or not. The converse also holds: if all resonant moments vanish, (8) shows E_k is homogeneous.

## 7. Remainder estimate (4)

- **Size of the error.** Factoring z^K produces r^{−Q−h_K}.
- **Uniform smoothness.** z = 2^{−qn} t^{−2} u^{−q} is bounded uniformly with all derivatives, since |t| and u are bounded below.
- **Scaling of pieces.** Inverting 2^{−(Q+h_K)n} f(2^{−An}ξ, 2^{−n}η) gives 2^{−h_K n} G_n(2^{An}s, 2^n y).
- **Derivative bound.** An ordinary derivative of order (a,c) costs 2^{(Aa+c)n} ≤ 2^{ANn}, since A > 1 and a+c ≤ N. With h_K > AN the series converges uniformly. The condition is conservative but valid.
- **Low frequencies.** (1−χ_hi)E_k is supported in |η| ≤ 2 and |ξ| ≤ C·2^A, so it is compactly supported and its inverse transform is entire. The same holds for the exact packet's low-frequency part.
- **Decomposition.** χ_hi(V̂ − Σ_k density_k) = χ_hi · error_K. Confirmed.

## Correction needed

Claim 1 asserts that each u_k is smooth away from the origin, but the text never proves it. The remainder section only gives C^N bounds. Add:

> "Since (1) is exactly quasi-homogeneous, the dyadic pieces of χ_hi E_k are 2^{−h_k n}G(2^{An}s, 2^n y) for one fixed Schwartz G. They therefore satisfy the analogue of estimate (7) in the dyadic proof, and choosing N large gives uniform convergence of all derivatives on compact sets avoiding the origin. The compact-frequency part is entire."

With this sentence added, I accept the proof. I recommend changing its status from OPEN to accepted once the correction is recorded.

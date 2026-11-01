# Audit of the delta3/5 corollary and its numerical example

## Statement and dependencies

The four real roots of the degree-ten compatibility polynomial from200 give convergent tuned exterior series at delta3/5, c5/2. The independent proof is in200 and was admitted inV416. The corollary transcribes the same hypotheses: finite odd-sine leading data sin(theta)+b sin(3theta), exact first compatibility, all-index nonzero responses with a nonzero limit, and the rational tuning theorem. The latter supplies all weighted derivatives and, since h=3, a common pure potential without logarithms.

## Proof audit

The two-coefficient determinant argument is valid: irreducibility and degree at most ten would force a vanishing response to be proportional to the compatibility polynomial. The determinant of its constant and degree-ten coefficients would then vanish. The exact nonzero determinant certificate excludes this at every integer index and at infinity. Convergence of the response sequence to its nonzero limit bounds all sufficiently large indices away from zero; the remaining nonzero finite set has a positive minimum. The quoted offset cutoff39<40 at k7 is correct. The coarse inverse bound L5 is valid, although the later quantitative boxes use75/29.

## Numerical transcription correction

For the largest root, the third response is

    sigma_3 = -3.51470779422979918347146978744215140278028569e-5

with the directed enclosure retained in verification/checks.json. The corollary prints approximately-3.5147, missing the factor10^-5. This number is refuted; the proof and its determinant certificate are unaffected. The source excerpt is retained for review.

The phrase first parameter with an odd reduced numerator should mean an odd reduced numerator greater than one: delta1/3, already treated, has odd reduced numerator one. This is a description of the campaign order, not a new mathematical property.

## Scope

The numerical value and prose correction do not change the proved exterior convergence theorem. The statement does not imply a whole-plane stationary extension, a sharp radius, or convergence of the canonical logarithmic branch.

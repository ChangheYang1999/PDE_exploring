# Independent audit of the 122-case prime-congruence table

Status: CONFIRMED finite exact audit, completed2026-10-31T05:13:22Z. The all-prime mathematical theorem is already confirmed in topic31; this topic checks the numerical experiments' expanded table.

## Claim and exact conditions

For every prime p in [5,61] and every even integer a with 4 <= a < p and 1/4 < a/p < 3/4, start the pure stationary recursion at delta=a/p and f_1(theta)=sin(theta). At its first stream resonance n=p, let j=a/2-1 and let kappa be the coefficient of sin((2j-1)theta) in f_p. The table claims there are122 such pairs and that kappa is nonzero, its denominator is coprime to p, and

    kappa = (-1)^((a-4)/2) modulo p.

It also reports approximate floating values for kappa. These approximations are not exact certificates.

## Independent calculation and interpretation

Enumerate the pairs with integer inequalities p < 4a < 3p. Recompute f_1 through f_p using exact rational signed Laurent polynomials and Cartesian derivatives, with no import from the numerical implementation. Before p, solve the stream equation by dividing the independently differentiated density coefficients by their exact nonzero Poisson multipliers. Obtain each next density from the ordered Cartesian products, divided by (n-1)(c-1).

At n=p the stream mode2j resonates. The independently computed forcing is exactly -2j*kappa; this identity checks the compatibility coefficient and its normalization. Reduce the exact numerator and denominator of kappa modulo p, verifying that the denominator is a unit, then compare the residue with both the reported value and the proved formula. Retain the exact kappa and full terminal density for each completed pair, plus the source and implementation hashes.

The exact inductive recursion is the proof of each finite value. The theorem in topic31 separately explains the shared congruence for all primes; the finite table is not used to infer that theorem. All122 cases are complete in verification/summary.json. Every congruence, nonzero numerator, unit denominator and forcing normalization passed. Conversion of each exact value to a Python float agrees exactly with the reported float; this statement concerns rounded representations only. The five run segments took513.0709536732174,522.2298259837553,510.50323727494106,506.1579963895492 and200.33112711878493 seconds of actual wall time.

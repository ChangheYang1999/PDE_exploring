# A certified residual gap in the weighted fractional norm

## Statement and scope

Let F be the unnormalized density residual of the exact recovered state131, with c=4076476460239181/2251799813685248. Let N_s^w and its weights be exactly those of PROOF.md. For every0<s<=1/2,

    N_s^w(F)>2^-18.

The smooth residual belongs to this space: its tail degree is q=2/c-1=427123167131315/4076476460239181, which lies strictly between0 and1/5, and its differentiated symbol bounds follow from its finite regularized-power potential. The membership argument is in section10 of ROUGH_INVERSE_PROOF.md.

At the conditional theorem's s=2^-104 and eta=2^-78/24 this gives

    N_s^w(F)/eta >24*2^60=27670116110564327424.

Thus the accepted state does not meet this theorem's sufficient smallness test. This does not exclude nearby exact profiles or improved inverse constants, nor does it give a lower bound over a class of alternative references.

## Point certificate and independent recomputation

The code verification/state131_weighted_gap.py reads only its own exact source reconstruction and exact residual polynomials. It verifies the canonical and original-record hashes and the exact tail exponent. Three768-bit Arb evaluations at(0,1000) agree: fourth-order Cartesian potential jets, independently assembled seventh-order Cartesian potential jets, and the compactified polar residual polynomial. Each interval is finite, all overlap, and each proves the strict rational inequality

    F(0,1000)>1/8.

The common value begins0.1253022828320913051009248020472951799277285557515301503887744509668313550717315972244414277649542847. The rigorous balls, dependencies and exact rational comparisons are stored in verification/state131_weighted_gap.json. The fourth-order evaluator's consecutive-radial-index assumption is checked for every original group before use.

## Norm lower bound

V077 proves |g(X)|<=2^13 max(1,|X|)^(1/5)N_s^w(g). Since1000<4^5, evaluating this bound at(0,1000) gives

    1/8<F(0,1000)<2^15 N_s^w(F).

Therefore N_s^w(F)>2^-18. Division by the exact positive eta proves the displayed gap. No floating-point estimate enters this deduction.

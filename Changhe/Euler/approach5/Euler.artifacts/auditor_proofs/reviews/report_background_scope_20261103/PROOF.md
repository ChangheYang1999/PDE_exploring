# A bounded normalized velocity is uniformly sublinear

Status: the literal report nonimplication is REFUTED in A503. The bounded-background normalization theorem is unchanged.

## Exact claim and proof

Let U:R3->R3 be any bounded function, b,z0 any fixed vectors, and V(y)=U(y+z0)-b. Then

    |V(y)|<=||U||infinity+|b|,
    sup_(|y|>=R) |V(y)|/|y| <= (||U||infinity+|b|)/R -> 0.

Thus V is uniformly sublinear, with no equation or regularity assumption. In particular the profile normalized in A406 always has this property. If its required regularity and other hypotheses hold, the dynamical results requiring only uniform sublinearity apply. A406 alone does not prove that V tends pointwise or uniformly to zero at infinity.

The report's Section 6 says that the dynamical results use pointwise decay or uniform sublinearity, 'which the shifted profile need not have'. As a claim about uniform sublinearity this is false. It should say: 'The shifted velocity is bounded and therefore uniformly sublinear. Its uniform pointwise decay is not established by A406 alone, so results requiring that stronger decay retain their hypothesis.'

This is a scope clarification, not a counterexample to the pressure or background theorem. It does not extend the helicity-sign Liouville theorem without checking that theorem's complete decay dependencies. The existing configured-model report and A406 review are the collaboration basis. No computation.

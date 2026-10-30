# Scope audit of the transient-rate claim in theory_v02

## Exact claim being checked

The frozen theory_v02 source, lines347 to349, cites the audited far-field cap beta<=1+c-ca for a finite-prefactor semigroup bound on Y and concludes that transient routes of type(L) have to be posed in L2 or X_s, not in Y. Here (L) is a rate-one semigroup estimate with prefactor2. This conclusion does not follow from the cited cap.

## Complete argument

Fix c>0 and any 0<a<=1. Then beta_infinity=1+c-ca>=1. A hypothetical estimate ||S(t)||<=2 exp(-t) therefore has decay exponent1<=beta_infinity and violates no part of the cited necessary inequality. The inequality alone excludes rate1 only for a>1. At a=1, it permits the endpoint rate exactly. For0<a<1 it permits a strictly larger rate than1.

This verifies the scope error as a logical inference; it does not construct an actual semigroup with this bound for an IPM reference. Such a bound still needs its own domain and quantitative proof. The newer origin arguments, if accepted, may impose additional restrictions, but cannot retroactively make the stated inference from the far-field cap valid.

A correct replacement is: "The audited far-field cap rules out rate-one estimates in Y when a>1. For0<a<=1 the cap leaves such estimates open. The registered(L) hypothesis itself is posed in L2 and remains unverified for every candidate."

## Dependencies and verdict

The only dependency is the already audited inequality beta<=1+c-ca, together with the exact rate in(L). The overbroad exclusion of everyY transient route is REFUTED as an inference from that inequality. The registered L2 framework, its threshold and the actual open status of(L) are unchanged.

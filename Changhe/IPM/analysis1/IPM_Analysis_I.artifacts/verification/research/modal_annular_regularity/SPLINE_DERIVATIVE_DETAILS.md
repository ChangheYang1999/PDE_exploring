# Details of the spline derivative identity

Written 2026-10-21T20:17:02.266395+00:00 before the new checker. Read with PROOF.md.

For degree p>=2 set A=k_(i+p)-k_i, B=k_(i+p+1)-k_(i+1), C=k_(i+p-1)-k_i, D=k_(i+p)-k_(i+1), E=k_(i+p+1)-k_(i+2). Initially take positive denominators. In the differentiated Cox recurrence the coefficient of N_(i,p-2) is p(t-k_i)/(AC) and the coefficient of N_(i+2,p-2) is -p(k_(i+p+1)-t)/(BE). The coefficient of N_(i+1,p-2) is

 [(k_(i+p)-t)-(p-1)(t-k_i)]/(AD)
 +[-(t-k_(i+1))+(p-1)(k_(i+p+1)-t)]/(BD).

Subtract the proposed coefficient p(k_(i+p)-t)/(AD)-p(t-k_(i+1))/(BD). The difference is (p-1)(-A/A+B/B)/D=0. These three equalities prove the derivative formula by induction starting from the degree1 hats. They also supply the algebra omitted from the prose collection in PROOF.md.

Endpoint repetitions cause some lower-degree basis supports to collapse at the endpoint. On a fixed neighborhood of any strictly interior simple knot these collapsed basis functions are identically zero. The recurrence terms with zero denominator are omitted. The same identity then follows by perturbing the repeated endpoint knots to distinct nearby ordered knots: the collapsed supports stay outside this neighborhood, and every remaining rational recurrence term tends to its stated value. This uses only finitely many polynomial coefficients and nonzero denominators on the noncollapsed terms. It does not assume smoothness at the endpoint. The two outer endpoints are instead handled by the separate exact jet-matching construction.

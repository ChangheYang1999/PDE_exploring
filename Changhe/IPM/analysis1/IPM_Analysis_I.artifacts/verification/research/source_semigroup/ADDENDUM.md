# Review scope and arithmetic certificate design

The first core review saw only sections1-3 and identified the absence of the
decay and inverse derivation in that excerpt. Sections4-5 of the full PROOF.md
already contain that derivation; this is not a gap in the full manuscript.
Its detailed domain, conjugation, C4 regularity and core checks were accepted.
The notation infinity,F in E means the supremum of the Frobenius norm;
it is followed by addition of ||q||infinity. The common kappa is uniform over
the stated g box, not a claim of the same margin for arbitrary g.

For the independent scalar check, every parameter row is an abstract exact
rational illustration, not the derivative norms of a constructed coefficient
field. For each row, the positive base b0=1+R/d is rational and

 C=b0^(31/10),  K_A=C/a_s.

The primary audit evaluates these expressions with Arb512 and mpmath.iv180.
A different method bounds C entirely by integers. If b0^31=p/q in lowest
terms, B is a positive integer and

 n=floor( floor(p*2^(10B)/q)^(1/10) ),

then n^10<=p*2^(10B)/q<(n+1)^10. Consequently

 n/2^B<=C<(n+1)/2^B.

The code verifies both integer inequalities by cross multiplication against
p*2^(10B), so the intermediate flooring cannot create an unchecked endpoint.
When equality holds at the lower endpoint, C is exactly that dyadic and its
upper endpoint may also be set equal to it. Dividing these rational bounds
by positive a_s bounds K_A. We use B=1536 and check that the whole intervals
lie inside the saved primary enclosures. beta_s uses a separate Arb1536
square root of25/(231pi). These numerical illustrations do not establish
any actual E, R, coefficient norm or rank-one denominator.

The semigroup proof uses the already independently checked topic77 energy
and commutator inequalities. Its final verdict is pinned as a dependency;
no trial numerical data is needed for this auxiliary theorem.

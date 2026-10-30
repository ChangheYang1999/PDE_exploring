# Opposite H and E2 orderings for candidates007 and016

## Exact statement and notation

Let F007 and F016 be the complete canonical whole-plane residuals of
C1-N1-007-d2w-j7-e2bal and C1-N1-016-legqs25-quot013, with their exact
source identities bound in the accepted N4-252 and N4-410 certificates.
For each j use rho_j=-partial_y Delta chi_j,
u_j=(-chi_j,xyy,chi_j,xxy), and F_j=(cX+u_j).grad rho_j-rho_j,
with the common fixed c and the accepted generator convention. All
norms use Lebesgue measure on R2 and the Euclidean Hessian norm.
Define

 H(F)=sup{|int F phi|:phi in C_c^infty(R2), ||grad phi||2<=1},
 G0=||F||2, G1=||grad F||2, P2=||(1+4r^2)^(2/5)D2F||2,
 E2(F)^2=P2^2+2^14G1^2+2^18G0^2+(20/21)2^18H(F)^2.

The accepted complete-source certificates establish that all these
norms are finite. Then

 H(F007)-H(F016)>0.015873038675998,
 E2(F016)-E2(F007)>1.572166921614.

Thus the two actual norms give opposite strict orderings for these
same candidates. This statement compares norms of residuals. It does
not order distances from stationary solutions, approximation quality
under another norm, or the difficulty of a future inverse theorem.

## Complete informal proof

N4-252 provides an outward real ball enclosing a lower bound on
H(F007). For a printed ball [m +/- r], its exact rational endpoint
m-r is therefore also a lower bound. Both m and r in that accepted
record are finite decimals, so decode them as exact rationals.
N4-410 supplies a strict rational upper h16 for H(F016). Subtracting
h16 from the lower endpoint of the007 ball gives a positive exact
rational exceeding0.015873038675998. Hence the first strict inequality.
Its proof uses the complete upper for016, including the bounded
uncomputed angular tail; it does not compare two dual lower bounds.

N4-410 supplies E2(F016)>304196192960807/500000000000.
N4-252 supplies E2(F007)<606820219/1000000. Subtracting these gives
exactly1.572166921614. Strictness of both original bounds gives the
second strict inequality even though this displayed gap is exactly
the difference of their rational endpoints. The E2 weights in both
accepted proofs are identical. Its positive H contribution does not
force the same total ordering, since G0,G1 andP2 also contribute.

## Dependencies, verification and scope

Bind the exact252 and410 results, their complete direct input maps,
and this proof before the checker. Recheck every recorded pass flag,
parse the007 H lower ball by exact decimal arithmetic, and verify
its positive radius and lower endpoint. Recheck410's strict H upper
by exact squaring against its accepted square upper, and its strict
E2 lower against its accepted square lower. Recheck252's strict E2
upper against the upper endpoint of its E_upper ball. Then subtract
and verify both displayed gaps by exact rational inequalities. Hash
binding preserves identity; the previously accepted source proofs
are the premises establishing the actual norms. No new integration,
peer program, optimizer, inverse or stationary existence proof is
performed. The Opus domain reviews already accepted in404/408 are
part of410's proof dependencies; no additional model is claimed.

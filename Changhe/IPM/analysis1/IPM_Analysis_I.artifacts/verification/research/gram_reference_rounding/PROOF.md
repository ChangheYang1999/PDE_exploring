# Exact continuity of the newly encoded cutoff references

## Statement and scope fixed before arithmetic

Let a<b be finite logarithmic radii and P(z) a real polynomial. Define
f(t)=1 for t<a, f(t)=P(t-a) for a<t<b, and f(t)=0 for t>b.
Let h(x,y)=x^2 y f(log r), r=sqrt(x^2+y^2), with the natural extension
h=x^2y near the origin. Use the full-plane weak weighted H1 space X
from topic128, with the same positive k,L and norm weight. Then h lies
in X if and only if P(0)=1 and P(b-a)=0. In particular, any nonzero
upper value trace invalidates the claim that this encoded reference
is in X, however small that trace is.

Near the origin h is exactly x^2y, so its X energy is finite by the
radial exponent criterion a=3>2. At infinity h vanishes. On the two
finite boundary circles the weight is positive and bounded. Integration
by parts on the three open regions shows that the distributional gradient
is the piecewise classical gradient plus the jumps times circle measure
and the unit normal. Since x^2y is nonzero on open arcs of either circle,
a nonzero radial value jump is a nonzero measure singular to area and
cannot be a weak L2 gradient. If both jumps vanish, those measures cancel;
the remaining piecewise gradient is square integrable and proves membership.
This also proves that changing values only on the circles cannot repair a
jump. No derivative trace matching is necessary for X membership.

The intended ideal polynomial is
P(z)=1-S(z/(b-a)), where
S(s)=126s^5-420s^6+540s^7-315s^8+70s^9.
Exact differentiation shows S(0)=0, S(1)=1 and S^(j)(0)=S^(j)(1)=0
for j=1,...,4. Thus its ideal piecewise formula is C4.
Replacing its coefficients by rounded binary64 numbers is a different
polynomial. The exact endpoint tests must be redone on those numbers.

## Verification plan and dependencies

Freeze the current numerics src/c2_gram2.py and its complete step_pieces
function, STEP_COEF list and REFS construction. Bind M24 tmin and t0 to
the previously captured, pinned NPY scalar members of topic130. Evaluate
only the isolated frozen step function locally on these exact inputs;
record every returned finite coefficient in hexadecimal JSON. This is a
reproduction of the current source expression, not evidence that a future
numerics job used these exact bytes or generated these outputs.

Reconstruct endpoint derivatives through order4 by exact rational Horner
arithmetic. Independently decode all binary64 bits and sum differentiated
monomials directly. Verify the ideal identities separately. Compare every
exact result, recording successes and failures without forcing a desired
outcome. The claim concerns these three encoded reference functions only,
not the singular vectors, the numerical Gram spectra or the PDE. A
continuous reference alone would not make a nonconforming singular vector
an element of X. Topic130 supplies scalar provenance and topic128 the
already established local weak-gradient criterion; the argument is restated
above so its mathematical role is explicit.

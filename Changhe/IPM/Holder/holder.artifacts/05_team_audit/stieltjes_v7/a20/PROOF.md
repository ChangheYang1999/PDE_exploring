# A finite positive certificate for the diagonal norm at exponent 1/5

For real functions on R^2 let [f]_a=sup_(z!=w)|f(z)-f(w)|/|z-w|^a.
Define T_xx by the circular principal-value kernel
(z_1^2-z_2^2)/(2 pi |z|^4), and its extension modulo constants by
convergent increments. Let D_a be the operator seminorm of
R_1^2=T_xx-I/2, equivalently its supremum over smooth compactly supported
functions. Subject to the exact certificate checks recorded in the
adjacent accepted.json with verdict CONFIRMED, the following bound holds:

    D_(1/5) >= 3.9578692464.

Use the projection-cusp witness of
../../../11_lattice_pole_constraints/axis_projection_stieltjes/PROOF.md
with a=1/5, b=3/8, shift=-1/20 and K=1011/1000. Its explicit polygon,
projection profile and clamping operations are as stated there. The
independently checked profile certificate gives [P]_(1/5)<=1.010555855930,
which is less than K. The lattice construction therefore gives [f]_a<=1
and opposite pole values f(1/2,0)=-1/2 and f(-1/2,0)=1/2. Its exact
diagonal increment is

    1+4 integral_(X>0,Y>0) V(X,Y)(-d_Y f)dX,
    V(X,Y)=XY/[pi(((X-1/2)^2+Y^2)((X+1/2)^2+Y^2))].

The integral is positive. This identity accounts for the circular
principal values, the local identity term and the convergent increment
at infinity; its derivation is in the cited witness and monotone-axis
proofs. Their compact approximation argument transfers the witness
bound to smooth compactly supported inputs.

Write X=1/2+s d, s=+1 or -1. Take logarithmic ratio endpoints v in
[-6,3], meaning Y=d exp(v). On each sign, the logarithmic d interval
[-60,-18] is split into 2048 equal strips and the v interval into256
cells. The positive sign also uses log d in[-18,12] and the negative
sign uses[-18,log(1/2)], each with16384 strips and512 ratio cells.
Each logarithmic endpoint is the exact affine subdivision of the
stated interval endpoints. Exponentiation gives the d and Y/d endpoints;
the final negative d endpoint is exactly1/2. There
is no overlap of strip interiors. The omitted positive integral is
nonnegative, so completeness over the entire infinite quadrant is
unnecessary.

On every cell use the pointwise lower rules proved in ../PROOF.md:
direct enclosure, exact homogeneous profile difference, first- or
second-order mean-value bound, or complete subdivision. Multiplying
a nonnegative lower variation by the lower endpoint kernel and the
strip width gives a lower bound for the positive integral on that
cell. Interval endpoints are rounded outward. Eighteen chunk records
cover every selected strip exactly once. Independent exact rational
resummation yields the lower endpoint stored as exact_D_lower in
independent_audit.json; it exceeds3.9578692464 and is below3.9578692465.
This proves the displayed bound.

The audit verifies all parameters, strip coverage, profile hypotheses,
source identities, serialized endpoints and downward rounding. Three
selected chunks were independently replayed, covering mixed derivative
and subdivision rules, the direct rule, and the negative-side endpoint.
All their numerical fields must match. This is a selected replay, not
an assertion that every production cell was independently rerun.
The source hash was observed during production; a formal pre-launch
hash for this run was not supplied. That provenance limitation is
preserved in accepted.json. No finite-exponent sharpness is claimed.

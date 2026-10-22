# Finite tensor composition criterion for the flow certificate

Written 2026-10-21 before the new computation. Numerical application OPEN.
This result is separate from the full angular and radial queues. It will
validate only explicitly enumerated contemporary finite compositions.

## Statement and hypotheses

Let Q=12 and n=1,...,261. On 0<=sigma<=h and |eta|<=d suppose

 P_n(sigma)=sum_(j=0)^Q p_nj sigma^j+e_Pn(sigma),
 R_n(sigma)=sum_(j=0)^Q r_nj sigma^j+e_Rn(sigma),
 f_n(eta)=sum_(k=0)^2 f_nk eta^k+e_fn(eta),

where f is one of c,C,S, the absolute errors are bounded by nonnegative
E_Pn,E_Rn,E_fn, and every coefficient belongs to its supplied interval.
All intervals are finite exact dyadic midpoint-radius boxes. The functions
need not attain their coefficient and error bounds independently.
Dependencies are retained mathematically and enlarged to independent boxes
for the interval calculation. Membership in these input boxes is an
explicit premise; a composition test does not prove membership itself.

Take h,d>0, H_j>=h^j, and exact scalar interval enclosures of c_l and mu.
Set a=129/20, b=307/100. Define

 SP=sum_n c_n P_n, SC=sum_n C_n R_n, SS=sum_n S_n R_n,
 s=c_l-SP, v2=s+SC, v1=s-SS,
 T=-(1+c_l)-a SS+b SC+mu s.

Here mu may be any function of sigma with values in its scalar interval.
All products involving mu are interval products, so no derivative or
polynomial dependence of mu is assumed. If the complete independently
computed interval ranges below lie in the reported source ranges for
s,v2,v1,T, those source ranges enclose these four functions throughout
the stated rectangle. This is a finite sufficient criterion. Failure of
this test alone does not show the source range is false.

## Product coefficients and complete remainder

For intervals I=[l,u],J=[v,w], define I+J=[l+v,u+w] and
IJ=[min(lv,lw,uv,uw),max(lv,lw,uv,uw)]. These formulas follow by affine
extremization successively in each variable. Induction gives inclusion for
any finite arithmetic expression. Exact rational evaluation incurs no
rounding error. Directed arbitrary precision evaluation gives a second
inclusion if every endpoint operation is rounded outwards.

For each family f and corresponding radial model X=P or R, enclose
q_kj=sum_n f_nk x_nj by these interval operations. Put

 A_Xn=sum_j sup|x_nj| H_j,
 A_fn=sum_(k=0)^2 sup|f_nk| d^k,
 E_fX=sum_n [ E_fn A_Xn+(A_fn+E_fn) E_Xn ].

Writing (pol_f+e_f)(pol_X+e_X)-pol_f pol_X as
 e_f pol_X+pol_f e_X+e_f e_X proves this bound by the triangle inequality.
Thus sum f_n X_n is its tensor polynomial with coefficients q_kj and an
absolute error at most E_fX. All modes and all mixed errors are included.
Use errors E_SP+E_SC for v2, E_SP+E_SS for v1, and
 a E_SS+b E_SC+sup|mu| E_SP for T. The polynomial coefficients use the
same interval operations as the displayed definitions. The scalar term
-(1+c_l) introduces no additional analytic error: its full interval is
included in the constant coefficient.

## Tensor Bernstein bounds and two radial constructions

Write eta=d(2z-1), 0<=z<=1. Direct expansion shows the degree-two
Bernstein coefficients of q0+q1 eta+q2 eta^2 are

 q0-d q1+d^2 q2, q0-d^2 q2, q0+d q1+d^2 q2.

This identity holds coefficient by coefficient in sigma. Its three
Bernstein weights are nonnegative and sum to one. A common interval
containing the ranges of these three radial polynomials contains the
original tensor polynomial.

Choose a positive exact dyadic ell with 2ell>=h. On each of the two
radial intervals [a,a+ell], a=0 or ell, translation gives power
coefficients c_j=sum_(i=j)^Q binom(i,j) b_i a^(i-j). Scaling to [0,1]
and the binomial identity give Bernstein coefficients

 B_k=sum_(j=0)^k c_j ell^j binom(k,j)/binom(Q,j).

The Bernstein weights binom(Q,k)z^k(1-z)^(Q-k) are nonnegative and sum
to one, hence the minimum lower and maximum upper coefficient endpoints
bound the polynomial. Taking both subintervals and all three angular
coefficients gives a complete tensor bound on the original rectangle.
Finally enlarge it by the absolute analytic remainder on both sides.

A second construction converts the radial polynomial on [0,2ell] into
Bernstein coefficients. Repeated arithmetic means in the de Casteljau
triangle produce the Bernstein coefficients on [0,ell] and [ell,2ell].
For completeness, multiplying B_(Q,k)(z) by 1=(1-z)+z splits each
basis term into its two adjacent degree-Q+1 terms with the binomial
ratios; equivalently repeated affine interpolation of control points
evaluates the polynomial. Substituting z=w/2 or z=(1+w)/2 in this
identity gives the left and right edge entries of the triangle as the
subinterval coefficients. This proves the subdivision identity by
induction on Q. Outward interval means preserve inclusion. This second
calculation uses mpmath.iv; the first uses exact Fraction arithmetic and
direct translated power coefficients. The two resulting interval hulls
need not be equal, and each must be contained in the candidate source
range separately. Mere overlap does not pass the criterion.

## Evidence and limits

The new program will record exact candidate arrays, source hashes,
selected radial and angular identities, finite nonnegative radii and
remainders, two independently computed output ranges, exact comparison
results and runtime information. Every stored float is converted through
its exact integer ratio. It will use frozen topic93 radial arrays at
cells 0,4102,7808. Contemporary angular inputs will be reconstructed from
the frozen source and explicitly identified finite tree nodes. The
finite scalar, radial and angular membership dependencies will be stated
separately; no historical-run provenance is inferred from current replay.

This criterion bypasses a BLAS evaluation hypothesis for the particular
outputs which pass. It does not validate unseen cells, the full finite
outer region, adaptive coverage, field derivatives, the full finite-flow
aggregate, a global inverse, or either endpoint of PROMPT.md. Any future
claim about a physical field needs input membership and rectangle
coverage in addition to this composition criterion. Actual Opus5.5 will
review the proof and completed bounded experiment; unresolved criticisms
remain OPEN.

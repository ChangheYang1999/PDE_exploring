# A shorter analytic exterior region for the conic rate

2026-10-21. Written before this topic's computation. Proposed numerical
comparisons remain OPEN until the saved two-method computation, exact
audit and independent review pass. This is a result for the canonical
repaired modal trial, not a stationary solution or global inverse.

## Exact setting and inherited theorem

Put k=1615536043799051/9007199254740992, c_l=1/k,
omega=1-k>0, t_b=2289893859708677/281474976710656,
a=129/20, b=307/100, S=a+b=238/25, gamma=1129/1000.
Use U=(-psi_y,psi_x), -Delta psi=rho_x with the canonical sublinear
whole-plane inverse, V=c_l X+U, s=X.V/r^2, v1=V1/x, v2=V2/y.
The component quotients have their continuous axis extensions.
Define mu(r)=gamma+(S-gamma)/(1+(r/6)^4) and

 T=-(1+c_l)+a v1+b v2+(mu(r)-S)s.

Topic53, exterior_flow/PROOF.md, establishes for the canonical exact modal
trial, for every tau=log(r)-t_b>=1 and every angle in the closed quadrant,

 |s-c_l|<=P exp(-omega(tau-1)),
 |v1-c_l|,|v2-c_l|<=Q exp(-omega(tau-1)).

Here P and Q are respectively the exact rational joint_P_upper_exact and
joint_Q_upper_exact in its T_exact=1 row. Each is the larger of the Arb and
independent mpmath.iv upper endpoints. The theorem includes all261 modes,
all11 exterior exponent families, the degree-six correction and canonical
homogeneous transients. No new reconstruction of those inputs is claimed.
Its dependency verdict and every pinned input will be rechecked. Its
canonical moment and exact normalization premises remain explicit.

## Uniform estimate and proposed numerical conclusion

For tau>=5, set E=exp(-4omega), R=exp(t_b+5), P5=P E, Q5=Q E.
The elementary identity exp(-omega(tau-1))=
E exp(-omega(tau-5)) and omega>0 give |s-c_l|<=P5 and
|vi-c_l|<=Q5 throughout r>=R. Write s=c_l+ds and
vi=c_l+di. Substitution in T gives exactly

 T=-1+(mu(r)-1)c_l+a d1+b d2+(mu(r)-S)ds.

Since a,b,c_l>0 and gamma<=mu(r)<=mu(R)<=S,

 T <= -1+(mu(R)-1)c_l+S Q5+(S-gamma)P5 =: B5.

The coefficient mu(r)-S is nonpositive; taking its absolute value times
|ds| gives the positive error(S-mu(r))P5<=(S-gamma)P5. Thus this bound
never multiplies an interval by a sign assumed without proof. Mu decreases
because its denominator increases, and r>=R. Also s>=c_l-P5 and
vi>=c_l-Q5 on the same unbounded region.

The planned sufficient rational checks are

 20<R<510000, B5<-11/50, c_l-P5>557/100, c_l-Q5>557/100.

If they pass, then on every r>=R, including both axes,
T<-0.22, s>5.57, v1>5.57 and v2>5.57. They also hold on the public
region r>=510000, which is a subset. The off-box classification follows
from R>20 and the first-quadrant box with binary coordinates4.8,6.82,2.85:
it is contained in r<20, as follows by bounding both coordinates by7 and3.
The proof does not use a rounded radius to glue intervals. The remaining
finite exterior region is 0<=tau<=5, and the shared endpoint tau=5 is
included in both pieces. This strictly shortens the topic71 choice tau>=9.
It does not shorten the middle region or supply any missing finite coverage.

## Two independent scalar computations

Method A uses Arb512 and forms R=exp(t_b+5), E=exp(-4omega), mu directly,
and B5 in the displayed expression. It records exact rational interval
endpoints and verifies all required strict rational comparisons.

Method B uses exact Fraction interval arithmetic and a positive Taylor
series for the exponential. For rational x>0 and integer N with x<N+2,
let S_N=sum_(j=0)^N x^j/j! and t_(N+1)=x^(N+1)/(N+1)!.
The remaining positive terms have successive ratios at most x/(N+2)<1,
so

 S_N < exp(x) <= S_N+t_(N+1)/(1-x/(N+2)).

This follows by comparison with a geometric series, and supplies rational
outward endpoints without transcendental library calls. Use N=192 for
x=4omega and x=t_b+5, checking the ratio assumptions exactly. Invert the
first positive interval to enclose E. The second encloses R; integer
powers, positive reciprocals, sums and endpoint products then give mu(R),
P5,Q5 and a second enclosure of B5. For an independent factoring use

 B5 = (-1+(gamma-1)c_l)
       +c_l(S-gamma)/(1+(R/6)^4)
       +E(S Q+(S-gamma)P).

All interval operations use the extrema of rational endpoint products;
there is no rounding. Every endpoint, positivity fact, decay exponent and
strict public comparison is checked exactly. Both methods must pass the
public comparisons separately. Overlap is only a diagnostic. A saved-number
checker independent of both engines verifies the Taylor endpoint identities,
all inequalities and hashes. It is not a third transcendental computation.

## Scope and dependencies

This proof uses the accepted canonical exterior_flow theorem and its full
input dependencies. It introduces no new field, clipping, tail replacement
or additional large-mode truncation. It proves no finite angular coverage,
finite annulus range, global flow topology, transit or orbit cost, coercive
functional norm, inverse, nonlinear estimate, X3 distance or source
neighborhood. Neither decisive endpoint of PROMPT.md follows. Actual
Claude Opus5.5 reviews both this argument and the completed evidence, and
any unresolved mathematical objection leaves the numerical conclusion OPEN.

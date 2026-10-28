# Positive vertical-variation formula for axis witnesses

## Statement and notation

Use the real homogeneous Holder space and the centered circular principal
values of ../../01_setup/PROOF.md. Fix 0<alpha<1, a=1/2, x=(a,0), y=-x,
and R_1^2=T_xx-I/2. Suppose f has seminorm at most one, is odd under
X-reflection and even under Y-reflection, satisfies f(x)=-1/2, and for
every X>0 is nonincreasing as Y runs from zero to infinity. In particular
|f(X,Y)|<=2^(alpha-1) X^alpha by oddness and the Holder bound.

For each X>0 let m_X be the positive Lebesgue-Stieltjes measure on
(0,infinity) specified by

    m_X((u,v])=f(X,u)-f(X,v), 0<u<v.

The continuity of f makes the choice of open or closed endpoints immaterial.
Define

    V(X,Y)=2aXY/[pi((X^2-Y^2-a^2)^2+4X^2Y^2)], X,Y>0.

Then the exact fixed-axis increment is

    R_1^2 f(x)-R_1^2 f(y)
      =1+4 integral_0^infinity integral_0^infinity V(X,Y) dm_X(Y) dX.

The integral is finite and nonnegative. Consequently any finite sum of
rigorous lower bounds on disjoint vertical strips, retaining any disjoint
Y intervals within each strip, is a lower bound for D_alpha after adding
one. The Y intervals may depend measurably on X.

## Proof of the integral formula

The rational kernel calculation in ../axis_zero_set/PROOF.md gives

    nu(X,Y)=K_xx((X,Y)-x)-K_xx((X,Y)-y)=partial_Y V(X,Y).

For fixed X>0, X!=a, integrate by parts in Y. The function f(X,Y)+1/2 is
bounded as a function of Y. The boundary terms vanish because V(X,0)=0
and V(X,Y) tends to zero as Y tends to infinity. Ordinary integration by
parts for a continuous function of bounded variation therefore gives

    integral_0^infinity nu(X,Y)(f(X,Y)+1/2) dY
      =integral_0^infinity V(X,Y) dm_X(Y).

The left integrand is absolutely integrable over the first quadrant.
Near x this follows from |f(z)+1/2|<=|z-x|^alpha and nu=O(|z-x|^-2).
On bounded regions away from x it is continuous. At infinity,
|nu|=O(|z|^-3) and |f(z)+1/2|=O(1+|z|^alpha), giving a finite integral
because alpha<1. Thus Fubini applies on the left. Tonelli applies to the
nonnegative right side. Both integrated quantities are finite and equal.
Evenness in Y gives

    J0=integral_{X>0} nu(f+1/2)=2 integral V dm_X dX.

The half-plane principal-value mass is -1/2, as proved in
../axis_reduction/PROOF.md. Hence Jf=PV integral_{X>0} nu f=J0+1/4.
Oddness in X doubles Jf in the full-plane increment, and the local term
-I/2 contributes +1/2. The result is 2J0+1, proving the formula.
The compact smooth approximation theorem applies to this fixed increment.

## A direct certificate rule

Let I=[l,r] be an X interval with 0<l<r, and let 0<u(X)<v(X) be measurable.
Suppose numbers A,B>=0 obey for every X in I

    f(X,u(X))-f(X,v(X))>=A,
    V(X,Y)>=B for u(X)<=Y<=v(X).

Then this strip contributes at least (r-l)AB to the double integral.
This follows directly by integrating the positive Stieltjes measure.
Summing over disjoint strips and disjoint vertical intervals is safe.
Omitted pieces have the favorable sign. No quadrature error assertion is
needed beyond the proved enclosures A and B.

For fixed X!=a, V is unimodal in positive Y. Indeed the sign of its
Y derivative is the sign of

    (X^2-a^2)^2-2(X^2+a^2)Y^2-3Y^4,

which decreases strictly from a positive value to minus infinity.
At X=a, V is decreasing in Y. Therefore its minimum on a finite positive
Y interval occurs at an endpoint. This observation can tighten B.

## An explicit lattice family

Let b>0 and g be the axis signed-distance polygon of
../axis_clamped_layercake/PROOF.md. In H={X>0} put

    h(X)=2^(alpha-1)X^alpha,
    P(X,Y)=((|X-a|-|Y|)_+/sqrt(2))^alpha,
    F(X,Y)=min(g(X,Y)+t, -1/2+lambda P(X,Y)),
    f(X,Y)=max(-h(X),min(h(X),F(X,Y))).

Take t>=-1/2 and 0<=lambda<=1, and extend f evenly in Y and oddly in X.
This family satisfies every hypothesis of the theorem.

To prove admissibility, P is the alpha power of the distance to the closed
set {|Y|>=|X-a|}. Its seminorm is at most one. The signed-distance lemma
for g gives the same bound. Translations, multiplication by lambda,
minimum, maximum and the half-plane gluing lemma preserve the stated
bound. At x, g=P=0 and t>=-1/2, so F=-1/2 and the pole value is exact.

To prove monotonicity, work in Y>=0. P is nonincreasing in Y. In either
positive component of g, the distance to the boundary is the minimum of
X and the distances to the upper supporting lines; those line distances
are nonincreasing in Y. In the complement above the graph Y=B(X), the
absolute distance to the zero set is the minimum of X and the distances
to the closures of the two positive components. Each such component,
restricted to Y>=0 and filled down to Y=0, is downward closed. Its
Euclidean distance from (X,Y) is nondecreasing in Y above the upper graph:
a closest point may be taken with height at most Y, and lowering Y cannot
increase the least distance until the component is reached. Equivalently,
projection onto either convex component has nonnegative vertical residual
there. Thus g is nonincreasing in Y throughout H. Minimum and clamping
by constants in Y preserve monotonicity. This proves the claim.

The same positive formula may be used with other monotone local profiles,
but their global Holder bound must be proved separately. No numerical
value for the present family is claimed in this proof.

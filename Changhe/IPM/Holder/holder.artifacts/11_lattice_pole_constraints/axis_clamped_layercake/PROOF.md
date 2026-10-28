# Positive layer-cake formula for the clamped axis polygon witness

## Statement

Fix 0<alpha<1 and b>0. Work in the real homogeneous Holder space of
../../01_setup/PROOF.md, with the Euclidean seminorm, the centered circular
principal values, and R_1^2=T_xx-I/2. Put a=1/2, x=(a,0), y=-x,
H={X>0}, c=2^(alpha-1), and h(X,Y)=c X^alpha.

In H define the continuous piecewise linear function

    B(X)=a-X                         for 0<X<=a,
         X-a                         for a<=X<=a+b,
         (X-a+(sqrt(3)-1)b)/sqrt(3)   for X>=a+b.

Let Z consist of the vertical axis, the graphs Y=+-B(X) in H, and their
reflections into X<0. Give H\Z sign + when |Y|<B(X), sign - otherwise,
and reverse that sign under X-reflection. The values on Z are zero. Set

    g(z)=c sign(z) dist(z,Z)^alpha,
    f(z)=max(-h(z),min(h(z),g(z)-1/2)) for z in H,
    f(-z)=-f(z) for z in H, and f=0 on X=0.

Then [f]_alpha<=1, f(x)=-1/2 and f(y)=1/2. Define P(u,s) and N(u,s) by
the elementary boundary formulas below. Put U(t)=(t/c)^(1/alpha), t>=0.
The exact fixed-axis increment is

    R_1^2 f(x)-R_1^2 f(y)=1+2(J_plus+J_mid+J_minus),

where

    J_plus = integral_0^infinity P(U(t),U(t+1/2)) dt,
    J_mid  = integral_0^(1/2) P(U(t),U(1/2-t)) dt,
    J_minus= integral_0^infinity N(U(t+1/2),U(t)) dt.

Every integrand is nonnegative, and all three integrals converge. Thus
any lower enclosure obtained by integration on compact subintervals is
already a rigorous lower bound for D_alpha. There is no omitted-tail
penalty: omitted portions have the favorable sign.

The formula concerns this explicit admissible witness. It does not claim
that the axis direction or the saturated pole values are optimal for
D_alpha.

## Boundary functions

For X>0, Y>0 define

    V(X,Y)=-(a/pi) Im[1/((X+iY)^2-a^2)].

It is positive, since the imaginary part of the denominator is 2XY>0.
The increment kernel is

    nu(X,Y)=K_xx((X,Y)-x)-K_xx((X,Y)-y)=partial_Y V(X,Y).

For a line Y=mX+d define

    L(m,d;p,q)=integral_p^q V(X,mX+d) dX.

Only intervals on which X>0 and Y>=0 are used below. With z=X+i(mX+d),
an antiderivative is

    F(m,d;X)=-(1/(2pi)) Im[log((z-a)/(z+a))/(1+im)].

Use the logarithm whose argument lies in [0,pi] for points in the closed
upper half-plane. Its value at infinity is zero. Therefore
L=F(q)-F(p), including q=infinity. The integrals below never run through
a pole. At an endpoint with Y=0 and 0<X<a the logarithm has imaginary
part pi. This convention matters in a numerical implementation.

Write beta=(sqrt(3)-1)b, and for u,s>0 put

    v=max(u,s), w=a-sqrt(2)s,
    d1=-a-sqrt(2)s, d2=(beta-a-2s)/sqrt(3),
    k=(d2-d1)/(1-1/sqrt(3)),
    r=max(u,a+sqrt(2)s,a-beta+2s).

Define

    P(u,s)=2 [ 1_(v<w) L(-1,w;v,w)
                 +1_(r<k) L(1,d1;r,k)
                 +L(1/sqrt(3),d2;max(r,k),infinity) ].

For N assume u>=a+s, as holds at every argument in the theorem. Let

    l=a+b-s/sqrt(2), r=a+b-s/2,
    C(X)=b+sqrt(s^2-(X-a-b)^2), l<=X<=r,
    Q(p,q)=integral_p^q V(X,C(X)) dX.

Then

    N(u,s)=2 [ 1_(u<l) L(1,-a+sqrt(2)s;u,l)
                 +1_(max(u,l)<r) Q(max(u,l),r)
                 +L(1/sqrt(3),(beta-a+2s)/sqrt(3);
                    max(u,r),infinity) ].

All displayed line and arc integrals are integrals of the positive V
in the first quadrant. Endpoint cases s=0 are interpreted by limits;
they do not affect the t integrals.

For completeness, the circular arc also has an elementary primitive.
Put z_c=a+b+ib and z=X+iC(X). Along this arc

    dX=(1/2)[1-s^2/(z-z_c)^2] dz.

Define

    A(z)=log((z-a)/(z+a))/(2a),
    B_c(z)=-1/[(z_c^2-a^2)(z-z_c)]
           -2z_c log(z-z_c)/(z_c^2-a^2)^2
           +log(z-a)/[2a(a-z_c)^2]
           -log(z+a)/[2a(a+z_c)^2].

Then a primitive for Q is

    H(z)=-(a/(2pi)) Im[A(z)-s^2 B_c(z)].

Indeed A'=1/(z^2-a^2), and partial fractions give
B_c'=1/[(z-z_c)^2(z^2-a^2)]. All logarithms are continuous along the
upper arc; z-z_c has argument between 2pi/3 and 3pi/4.

## Admissibility and the geometric level sets

The signed-distance lemma gives [g]_alpha<=1. On H the functions h,-h
have seminorm at most c<=1. Minimum and maximum preserve this seminorm
bound. The half-plane gluing lemma in ../half_plane/PROOF.md then gives
[f]_alpha<=1 globally. Since g(x)=0 and h(x)=1/2, the stated pole values
follow. The function is even in Y and odd in X.

The set where g>c s^alpha has two components in H. Its inner component
is the eroded triangle

    X>s,  |Y|<a-X-sqrt(2)s.

Its outer component is the intersection of the eroded half-planes

    |Y|<X-a-sqrt(2)s,
    |Y|<(X-a+beta-2s)/sqrt(3).

These descriptions follow by subtracting s from the distances to the
boundary lines of the respective convex components. Intersecting with
X>u gives exactly the line intervals in P. Integration first in Y gives
twice V on their upper boundaries. Hence

    P(u,s)=integral_{X>u, g>c s^alpha} nu.

For the negative level set used in N, u>=a+s. Consequently all points
with X>u have distance greater than s from every piece of Z contained
in X<=a, and from the vertical axis. Only the outer upper or lower
polygon boundary matters. Above that boundary, distance greater than s
means lying above the upper boundary of its Euclidean s-neighborhood.
That boundary has a 45-degree parallel line, a radius-s arc about the
corner (a+b,b), and a 30-degree parallel ray. The joining abscissae are
l and r above. The small circle about the pole lies in X<=a and is
irrelevant in this restricted region. Integration from that boundary to
Y=infinity gives -V; reflection doubles it. Therefore

    N(u,s)=-integral_{X>u, g<-c s^alpha} nu.

The assumed inequality u>=a+s follows from
U(t+1/2)^alpha=U(t)^alpha+a^alpha and
(a+s)^alpha<=a^alpha+s^alpha.

## Layer cake and the nonzero half-plane mass

For the present nu, the centered principal-value mass of {X>u} is

    mu({X>u})=-1/2 for 0<=u<a, and 0 for u>a.

This is the half-plane flux calculation of ../axis_reduction/PROOF.md,
with the dividing line translated to X=u. The exceptional u=a is not
needed. In particular mu(H)=-1/2.

For t>0 the clamping identity gives

    {f>t}={h>t, g>t+1/2},
    {f<-t}={h>t, g<1/2-t}.

If 0<t<1/2, the second set is the complement of
{h>t, g>1/2-t} within {h>t}. Its mass is therefore
-1/2-P(U(t),U(1/2-t)). If t>1/2, its mass is
-N(U(t),U(t-1/2)). The first set always has mass
P(U(t),U(t+1/2)). Thus

    PV integral_H nu f=1/4+J_plus+J_mid+J_minus.

Here equality on level boundaries is harmless: the relevant boundaries
are curves of planar measure zero. The constant 1/4 is essential.

To justify exchanging levels and spatial integration, subtract the pole
value before applying Fubini. The integral of the absolute level-change
indicators at a point z equals |f(z)+1/2|. The product
|nu(z)| |f(z)+1/2| is integrable near x by the Holder bound, and at
infinity because |nu|=O(|z|^-3), f=O(|z|^alpha), alpha<1. There is no
other pole in H. This proves absolute Fubini for the subtracted formula;
the half-plane mass then restores the displayed 1/4. It also proves
convergence of the three positive integrals.

Finally the full-plane kernel integral is twice its half-plane value.
The local identity term is -(f(x)-f(y))/2=1/2. Substitution gives
1+2(J_plus+J_mid+J_minus). The approximation theorem in the setup note
transfers this lower bound to the original compact smooth test class.

## Numerical verification contract

The exploratory file ../../code/axis_clamp_layercake_float.py uses these
primitives and is not a certificate. A rigorous lower certificate may
partition compact t intervals, enclose each included boundary primitive
using outward ball arithmetic, and sum interval lower endpoints. It may
omit a nonnegative line or arc contribution when a branching condition
is unresolved on a cell. It may also omit any endpoint or tail interval.
Those omissions weaken the lower bound but cannot invalidate it. All
parameters, partition endpoints, precision, source hashes and resulting
lower roundings must be saved before a numerical claim is accepted.

# One-dimensional lower formula for the axis sector cusp

## Statement

Use the real homogeneous Holder seminorm, the increment-defined transforms,
and the normalization R_1^2=T_xx-I/2 of ../../01_setup/PROOF.md. Fix
0<alpha<1, b>=1/2, and -1/2<=t<=0. Put a=1/2, c=2^(alpha-1),
U(w)=(w/c)^(1/alpha), beta=(sqrt(3)-1)b. Let g be the signed-distance
axis polygon of ../axis_clamped_layercake/PROOF.md, with this b. In X>0 set

    h=c X^alpha,
    P=((|X-a|-|Y|)_+/sqrt(2))^alpha,
    f=clamp(min(g+t,-1/2+P), -h,h).

Extend evenly in Y and oddly in X. This is an admissible seminorm-one
witness with f(a,0)=-1/2. Define M_plus, M_minus and N below. Then

    R_1^2 f(a,0)-R_1^2 f(-a,0)=1+2(J_plus+J_mid+J_low),

where, writing q0=t+1/2,

    J_plus=int_0^infinity M_plus(U(|r+t|),U(r),(r+q0)^(1/alpha)) dr,
    J_mid =int_0^q0 M_minus(U(1/2-q),U(q0-q),q^(1/alpha)) dq,
    J_low =int_0^infinity N(U(r+1/2),U(r+q0)) dr.

All three integrands are nonnegative. At q0=0 take J_mid=0. Endpoint
values in the integrals are interpreted by limits. In particular any
rigorous lower enclosure on finite subintervals gives a lower bound for
D_alpha with no omitted-tail penalty.

## Boundary integrals

Use the positive V and its line and arc integrals L and Q from
../axis_clamped_layercake/PROOF.md. For M_plus(u,s,p), put

    v=max(u,s), w=a-sqrt(2)max(s,p),
    d1=-a-sqrt(2)max(s,p), d2=(beta-a-2s)/sqrt(3),
    k=(d2-d1)/(1-1/sqrt(3)),
    z=max(u,a+sqrt(2)max(s,p),a-beta+2s).

Then

    M_plus=2[1_(v<w)L(-1,w;v,w)
              +1_(z<k)L(1,d1;z,k)
              +L(1/sqrt(3),d2;max(z,k),infinity)].

For M_minus(u,s,p) used above, one has u>=s and u<=a. Put

    w=a-sqrt(2)p,
    d1=-a-sqrt(2)p, d2=(beta-a+2s)/sqrt(3),
    k=(d2-d1)/(1-1/sqrt(3)), z=max(u,a+sqrt(2)p).

Then

    M_minus=2[1_(u<w)L(-1,w;u,w)
               +1_(z<k)L(1,d1;z,k)
               +L(1/sqrt(3),d2;max(z,k),infinity)].

The function N(u,s) is the same line-arc-line formula as in the earlier
clamp proof. Its validity here requires only u>=a and u>=s, since b>=a:

    l=a+b-s/sqrt(2), R=a+b-s/2,
    N=2[1_(u<l)L(1,-a+sqrt(2)s;u,l)
          +1_(max(u,l)<R)Q(max(u,l),R)
          +L(1/sqrt(3),(beta-a+2s)/sqrt(3);max(u,R),infinity)].

This weaker domain condition for N is proved below and is not an implicit
extension of the hypothesis in the earlier proof.

## Proof

Admissibility and vertical monotonicity are proved for this family in
../monotone_axis/PROOF.md. In particular its exact increment is

    1+4 int_{X>0} int_{Y>0} V(X,Y)(-d_Y f) dX.

For fixed X, the push-forward of Lebesgue measure on levels between the
limiting values of the continuous monotone function Y->f(X,Y) gives its
Stieltjes variation. Thus the inner integral equals the integral of V
at the upper boundary of {Y:f(X,Y)>ell}, over all levels ell. Flat pieces
cause no ambiguity for almost every level. Since V is positive, Tonelli
permits the order of X and ell integration to be interchanged.

The lower limiting value is -h: for sufficiently large Y, dist((X,Y),Z)=X,
so g=-h and g+t<=-h. Clamping gives f=-h there. A level can contribute
only if X>U(|ell|). We now find its upper boundary.

If ell>=t, put s=U(ell-t), p=(ell+1/2)^(1/alpha), u=U(|ell|).
The conditions are g>c s^alpha and P>p^alpha. In the inner triangle these
are X>max(u,s) and Y<a-X-sqrt(2)max(s,p). In the outer component they are
Y<X-a-sqrt(2)max(s,p) and Y<(X-a+beta-2s)/sqrt(3), together with X>u.
Integrating V on these line segments and ray gives M_plus/2. The change
r=ell-t gives J_plus.

If -1/2<ell<t, put s=U(t-ell), p=(ell+1/2)^(1/alpha), u=U(-ell).
Here u>=s, because t<=0, and u<=a. The cusp condition is
Y<|X-a|-sqrt(2)p. On the inner part X<a this lies strictly below the
original upper triangle boundary, so the condition g>-c s^alpha is
automatic. On the outer part, the cusp lies below the 45-degree line.
Up to X=a+b it is again inside the positive component. Beyond that
corner the only further restriction is
Y<(X-a+beta+2s)/sqrt(3), from the distance to the 30-degree ray. Its
orthogonal projection lies beyond the corner whenever this restriction
is active. The reflected inner segment is contained in the outer
45-degree segment because b>=a; for X>=a it is no farther away than the
inner segment. Other reflected zero pieces are farther away. The axis
cannot remove the restriction because X>u>=s. This proves M_minus/2.
The change q=ell+1/2 gives J_mid.

Finally let ell<-1/2, w=-ell. The cusp bound is automatic. We need X>u=U(w)
and g>-c s^alpha with s=U(w+t). Since w>1/2 and t<=0, u>=a and u>=s.
For X>=a the inner segment is dominated by its reflection in the line
X=a, which is contained in the outer 45-degree segment when b>=a.
For Y>=0 the lower zero pieces are dominated by the upper pieces. The
axis is farther than s because X>u>=s. Thus the allowed vertical section
is exactly the Euclidean s-expansion of the outer positive wedge. Its
upper boundary is the 45-degree parallel line, the circular corner arc,
and the 30-degree parallel ray. The extra circular cap at the pole lies
to the left of X=a-s/sqrt(2), hence outside X>u>=a. This gives N/2.
Putting r=w-1/2 gives J_low.

Adding the three level ranges in the positive variation formula proves
the identity. It also proves convergence, since the full increment
exists by the Holder bound and alpha<1. At t=-1/2, min(g-1/2,-1/2+P)
is g-1/2: on positive components, c dist(Z)^alpha<=P, and on negative
components g<=0<=P. Thus this endpoint reproduces the earlier axis clamp,
providing a useful independent consistency check.

## Verification contract

A certificate must record exact alpha,b,t and exact transformed integration
endpoints, cover its chosen integration interval exactly, and enclose every
retained line or arc by outward arithmetic. Unresolved nonnegative components
may be discarded. The earlier explicit primitives apply without alteration.
No computed extremality or optimization claim is part of this theorem.

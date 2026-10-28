# An explicit gap in the axis-phase local angular bound

## Statement and notation

Let 0<alpha<1, x=(1,0), y=(0,0), R=1/2 and

    K(h)=(h_1^2-h_2^2)/(2 pi |h|^4).

For real functions on R^2 with Euclidean homogeneous Holder seminorm
[f]_alpha<=1, define

    L(f)=pv integral_(B(x,R)) K(z-x) f(z) dz
         -pv integral_(B(y,R)) K(z-y) f(z) dz.

Each principal value uses circular holes and subtracts the value at its
own pole. The angular mean of K is zero, and alpha>0 makes these local
integrals converge. Constants in f do not change L. Define

    a2(alpha)=2^(1+alpha/2)/(pi(alpha+2)),
    U(alpha)=2 a2(alpha) (1/2)^alpha/alpha,
    eta(alpha)=[log(10/9) sin(1/10)/pi]
               [(3/5)^alpha-(11/20)^alpha].

Then

    |L(f)| <= U(alpha)-eta(alpha),                         (1)
    eta(alpha)>0.

Thus (1) is an explicit quantitative form of the strict axis-phase gap.
It concerns only the two own-pole disks. It includes neither cross
kernels nor identity atoms, and does not replace a global operator bound.

## The original reflection plan

On a circle about a pole, divide each positive lobe of cos(2theta) into
two halves and reflect each half across the adjacent zero ray into the
negative lobe. The two reflected angular densities agree. Pairing each
positive value of f with its negative partner and using [f]_alpha<=1
gives the exact one-circle bound a2(alpha) r^alpha. Its radial integral
is a2(alpha) R^alpha/alpha. Apply this plan independently to K at x and
to -K at y. Its total cost is U(alpha).

We modify the plan only on radii 9/20<=r<=1/2 and angles 0<=u<=1/20.
All measures being modified have finite mass, since these radii stay
away from zero. The remaining singular pairing is unchanged and has
finite Holder cost. Therefore the argument can first be made with
circular holes and then passed to the limit.

## A four-point exchange

For such r,u write c=cos(u), s=sin(u), and set

    p=(1-r c, r s),    a=(1-r s, r c),
    b=(r s, r c),      q=(r c, r s).

The points p and a lie in the x disk, and b and q in the y disk. Their
angular positions about their respective poles are pi-u, pi/2+u,
pi/2-u and u. Thus p is a positive source for K at x, a a negative
source, b a positive source for -K at y, and q a negative source.
The original reflection plan contains the pairs p to a and b to q,
with the same positive mass

    dm=cos(2u) du dr/(2 pi r).

Their common distance is

    ell=sqrt(2) r (c-s).

Replace these two pairs by p to q and b to a. This leaves every positive
and negative marginal unchanged. The new distances are

    d1=1-2r c,    d2=1-2r s.

They are nonnegative because r<=1/2 and 0<=s,c<=1. Concavity of the
power gives

    d1^alpha+d2^alpha
       <=2[(d1+d2)/2]^alpha
       =2[1-r(c+s)]^alpha
       <=2(11/20)^alpha,                                  (2)

since c+s>=1 on [0,1/20] and r>=9/20.

On this interval, cos(u)>=1-u^2/2 and sin(u)<=u give

    c-s >= 759/800.

Since sqrt(2)>141/100,

    ell >= (9/20)(141/100)(759/800)
         =963171/1600000 > 3/5.                           (3)

Equations (2)-(3) show that the saving per unit paired mass is at least

    2[(3/5)^alpha-(11/20)^alpha].                          (4)

Reflect the same exchange in the horizontal axis. The upper and lower
patches are disjoint except at sets of angular measure zero, and have
the same cost and mass. The two exchanges can therefore be made at once.

## Integration and conclusion

The mass of each one of the upper patches is

    integral dm = [log(10/9) sin(1/10)]/(4 pi).

There are two reflected exchanges, and each has saving (4). Their total
saving is at least eta(alpha). The modified plan therefore has cost at
most U(alpha)-eta(alpha), proving the upper bound on L. Apply the same
inequality to -f for its absolute value. Since 3/5>11/20 and alpha>0,
eta(alpha)>0.

No numerical optimization is used in this proof. Decimal values in the
verification record are evaluations of the explicit eta formula only.
The dependency is the already verified exact angular reflection cost
in ../../../02_upper_bounds/PROOF.md. The exchange and all new inequalities are proved
above. No formalization is claimed.

Status at creation: OPEN pending independent lead cross-read.

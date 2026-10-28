# An explicit homogeneous tail for the axis lattice witness

## Statement and dependencies

Let 0<a<1, b>0, c real, and lambda>=0. Use the real homogeneous
Euclidean Holder seminorm and the normalized kernel

    K(z)=(z_1^2-z_2^2)/(2 pi |z|^4).

Let f be exactly the polygon-plus-projection lattice witness of
../PROOF.md, with poles0,e1 and midpoint m=e1/2. Thus on X>0,
with z=m+(X,Y),

    f(z)=max(-h,min(h,g(z)+c,-1/2+lambda P(z-e1))),
    h=2^(a-1) X^a,
    g=2^(a-1) sigma dist(z,Z0(b))^a,
    P(u)=(|u|^a+sign(u_1^2-u_2^2)
                     (|u_1^2-u_2^2|/|u|)^a)/2.

Set P(0)=0 and extend f oddly across X=0. Assume

    lambda [P]_a <= 1,             lambda(1+2^(-a)) >= 1.       (1)

The first condition is supplied by the existing profile certificates;
the second is a separate explicit scalar inequality. Define

    H=sqrt((b+1/2)^2+b^2),
    B=max(H^a+|c|,1/2+2^(-a)),
    a3(a)=(3*2^a/pi) integral_0^(pi/6) sin(3t) sin(t)^a dt.

For R>1/2, the absolutely convergent tail satisfies

    | integral_(|z-m|>R) (K(z-e1)-K(z)) f(z) dz
        - 2 a3(a) R^(a-1)/(1-a) | <= E(a,b,c,R),              (2)

where every constant is explicit:

    E = 2B/[R(1-1/(4R^2))^2]
          + R^(a-3)/[2(3-a)(1-1/(4R^2))^2].                  (3)

This is a tail replacement for an existing integral certificate. It
has no singular poles on its integration domain and changes neither
the principal-value convention nor the local identity contribution.
The final operator lower bound still uses the separate admissibility
proof, finite-region certificate and identity term of ../PROOF.md.

Status: the analytic theorem is confirmed in V130 after the complete
independent cross-read recorded in lead Note27. Numerical consequences
require their separate finite-region and outward-arithmetic checks;
this analytic proof alone does not certify a numerical lower bound.

## Geometry of the limiting cone

Work in w=z-m coordinates. Let Zinf be the union of the vertical line
and the four rays through0 in directions (+sqrt(3)/2,+/-1/2) and
(-sqrt(3)/2,+/-1/2). Equivalently it is the zero set of cos(3 theta).
Define

    v0(w)=sigma(m+w) dist(m+w,Z0(b)),
    vinf(w)=sign(cos(3 theta)) dist(w,Zinf).

Both are zero on their respective zero sets. The Hausdorff distance
between Z0(b)-m and Zinf is at most H. Indeed, corresponding infinite
rays are translates by vectors (+/-(b+1/2),+/-b), of length H. Every
finite segment of Z0(b)-m lies in the closed disk of radius H, and0
belongs to Zinf. The vertical lines coincide. Conversely every point
on a limiting ray is within H of its translated ray. Consequently

    |dist(m+w,Z0(b))-dist(w,Zinf)| <= H.                       (4)

We need a signed version of (4). It is immediate when the signs agree.
By reflection it suffices to consider X>0 and Y>=0. The positive
region for v0 lies below the graph Y=B0(X), where

    B0(X)=1/2-X                         (0<=X<=1/2),
           X-1/2                       (1/2<=X<=1/2+b),
           b+(X-1/2-b)/sqrt(3)          (X>=1/2+b).

The positive region for vinf lies below Y=X/sqrt(3). When the signs
are opposite, Y lies between these two heights. The distances to the
two zero sets are bounded by the vertical distances to these graph
points, so their sum is at most |B0(X)-X/sqrt(3)|. This difference is
linear on the first two intervals and constant on the third. Its
endpoint values are1/2, -1/(2sqrt(3)), and
b-(b+1/2)/sqrt(3). Their absolute values are at most H: the last is at
most max(b,(b+1/2)/sqrt(3))<=H. Thus in all cases

    |v0(w)-vinf(w)| <= H.                                      (5)

The scalar map p_a(t)=2^(a-1) sign(t)|t|^a has Holder seminorm at most
one. For opposite signs this is concavity,
2^(a-1)(s^a+t^a)<=(s+t)^a; for equal signs use
|s^a-t^a|<=|s-t|^a. Therefore the homogeneous function

    ginf(w)=p_a(vinf(w))

satisfies

    |g(m+w)-ginf(w)| <= H^a.                                  (6)

## The other branches and the uniform witness error

The cone has six equally spaced rays, so dist(w,Zinf)<=|w|/2 and
|ginf(w)|<=|w|^a/2. Because Zinf contains X=0, also
|ginf(w)|<=2^(a-1)X^a=h for X>0.

If ginf(w)>0 in this half-plane, then |theta|<pi/6. Hence
cos(2theta)>=1/2 and

    lambda P(w)>=lambda(1+2^(-a))|w|^a/2
                 >= |w|^a/2 >= ginf(w).                       (7)

If ginf(w)<=0, (7)'s final comparison follows just from P>=0.
Thus the limiting min/max expression is exactly ginf:

    max(-h,min(h,ginf(w),lambda P(w)))=ginf(w).                 (8)

From lambda[P]_a<=1 and z-e1=w-e1/2,

    |-1/2+lambda P(w-e1/2)-lambda P(w)|<=1/2+2^(-a).            (9)

The minimum and maximum maps are nonexpansive in the largest absolute
coordinate change. Equations(6),(8),(9) give

    |f(m+w)-ginf(w)|<=B.                                     (10)

The same estimate holds on X<0 by odd reflection, and on X=0 by
continuity. This bound is uniform on the entire plane.

## Exact dipole and integrable errors

Identifying w with a complex number, the complex kernel difference is

    (1/(2pi))[(w-1/2)^(-2)-(w+1/2)^(-2)]
        =1/[pi w^3(1-1/(4w^2))^2].                          (11)

Its real part is the required kernel difference. Put
D(w)=cos(3theta)/(pi |w|^3) and q_R=1/(4R^2)<1. For r=|w|>R,

    |K(w-e1/2)-K(w+e1/2)|<=1/[pi r^3(1-q_R)^2],
    |K(w-e1/2)-K(w+e1/2)-D(w)|
           <=1/[2pi r^5(1-q_R)^2].                           (12)

For the second inequality expand (1-q)^(-2), or use
sum_(n>=1)(n+1)|q|^n=(2|q|-|q|^2)/(1-|q|)^2
<=2|q|/(1-q_R)^2, with |q|=1/(4r^2).

Multiply the first bound by B and integrate in polar coordinates.
The result is2B/[R(1-q_R)^2]. Multiply the second bound by
|ginf|<=r^a/2 and integrate. The result is
R^(a-3)/[2(3-a)(1-q_R)^2]. These are precisely(3).

Finally, each of the twelve half-lobes of cos(3theta) contributes the
same positive angular integral. With t the angular distance from a
zero ray,

    integral_0^(2pi) cos(3theta) ginf(e^(i theta)) dtheta
        =12*2^(a-1) integral_0^(pi/6) sin(3t)sin(t)^a dt
        =2pi a3(a).

Since integral_R^infinity r^(a-2)dr=R^(a-1)/(1-a), the integral of
D(w)ginf(w) is2a3(a)R^(a-1)/(1-a). This proves(2).

## An independent positive series for numerical use

Substitute u=sin(t), then v=2u. The identity sin(3t)=3u-4u^3 gives

    a3(a)=(3/(4pi)) integral_0^1
                       (3v^(a+1)-v^(a+3))/sqrt(1-v^2/4) dv.

With c_k=binomial(2k,k)/4^k, expand the last square root. Thus

    a3(a)=(3/(4pi)) sum_(k>=0) c_k 4^(-k)
                        [3/(a+2+2k)-1/(a+4+2k)].             (13)

Every summand is positive. Since0<c_k<=1, omitting k>=N has error at
most

    3*4^(-N)/[pi(a+2+2N)].                                   (14)

This explicit bound follows by discarding the negative term and
summing the geometric series. It is valid for every N>=0. A separate
implementation can therefore compute the tail in outward ball
arithmetic without numerical quadrature or optimizer imports.

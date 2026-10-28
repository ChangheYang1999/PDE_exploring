# Explicit zero curves of the axis increment kernel

## Statement

Fix a>0, let z=X+iY, and exclude the poles z=+-a. For the kernel
K_xx(w)=Re(w^-2)/(2pi), put

    nu_a(z)=K_xx(z-a)-K_xx(z+a)
           =(2a/pi) Re[z/(z^2-a^2)^2].

In the closed first quadrant its zero set consists of the vertical axis
and exactly two branches meeting at the excluded pole (a,0):

    inner: z(theta)=a exp(i theta)/sqrt(1+2 sin theta),
           0<=theta<=pi/2,
    outer: z(theta)=a exp(i theta)/sqrt(1-2 sin theta),
           0<=theta<pi/6.

The inner endpoint on the vertical axis is (0,a/sqrt(3)). Its tangent
there is horizontal. The initial inner and outer tangent directions at
the pole are respectively 3pi/4 and pi/4. Reflection in the two axes
gives the entire zero set.

The outer branch can also be parametrized without a trigonometric
inverse. For r>=a,

    Y(r)=(r^2-a^2)/(2r),
    X(r)=sqrt((r^2+a^2)(3r^2-a^2))/(2r).

It has distance at most a^2/(sqrt(3)r) from the point r exp(i pi/6).
Consequently the Hausdorff distance between its part r>=R and the
30-degree radial ray r>=R is at most a^2/(sqrt(3)R), for every R>=a.

These formulas describe the exact zero set. They do not make an
arbitrary signed polyline distance an admissible Holder function.

## Derivation

Taking the real part after multiplication by the conjugate denominator
gives

    Re[z/(z^2-a^2)^2]
      = X[(X^2+Y^2)(X^2-3Y^2)-2a^2(X^2+Y^2)+a^4]
        / |z^2-a^2|^4.

For X>0 and z=r exp(i theta), the bracket is

    r^4(1-4 sin(theta)^2)-2a^2r^2+a^4
      = [r^2(1+2 sin theta)-a^2]
        [r^2(1-2 sin theta)-a^2].

In the first quadrant the first factor has its unique positive radial
root for every theta; the second does so only when theta<pi/6. This
proves completeness of the two branches. Differentiating at theta=0
gives a(-1+i) for the inner tangent and a(1+i) for the outer tangent.
At theta=pi/2 the derivative of the inner radial factor is zero, so
its tangent is the horizontal vector -a/sqrt(3).

On the outer branch, sin theta=(1-a^2/r^2)/2. Thus Y=r sin theta has
the displayed formula, and X=sqrt(r^2-Y^2) gives the other one. Since
cos t>=sqrt(3)/2 on [0,pi/6],

    0<=pi/6-theta
      <=(2/sqrt(3))(1/2-sin theta)=a^2/(sqrt(3)r^2).

The distance to r exp(i pi/6) is at most r times this angle. Pairing
points with equal r in both directions proves the Hausdorff bound.

## Certified polyline approximation

The inner branch gamma(theta) has |gamma''(theta)|<=7a. Indeed its
radial factor satisfies r<=a, |r'|<=a and |r''|<=4a, and
|gamma''|<=|r''|+2|r'|+r. On an angular subinterval of width h, its
linear interpolant therefore differs from it by at most 7a h^2/8.
This follows from the integral remainder for linear interpolation,
whose nonnegative scalar Green kernel has integral at most h^2/8.
The same parameter pairing proves a Hausdorff bound for the segment.

For the outer parametrization, |gamma''(r)|<=4a^2/r^3. To check this,
set u=a^2/r^2 and b(u)=sqrt(3+2u-u^2)/2, so X=rb(u). Then

    b'=(1-u)/(2sqrt(3+2u-u^2)),
    b''=-2/(3+2u-u^2)^(3/2),
    X''=(2u/r)(b'+2u b''),   Y''=-a^2/r^3.

For 0<=u<=1, the quadratic under the square root is at least 3.
Hence |X''|<=11a^2/(3sqrt(3)r^3), and
|gamma''|<=|X''|+|Y''|<4a^2/r^3. On [r0,r1] the chord therefore has
Hausdorff error at most a^2(r1-r0)^2/(2r0^3). These errors and the
explicit exterior-ray error give a completely specified Hausdorff
bound for a finite approximation of all zero curves.

If a closed approximation Z' has Hausdorff distance at most eta from
the true closed set Z, then |dist(z,Z')-dist(z,Z)|<=eta for every z.
This supplies certified pointwise bounds for the true signed-distance
witness when its sign is taken from the exact kernel. It is essential
to retain the distance error. Using the exact kernel sign with a
noncoincident polyline distance generally produces jumps at the true
zero curve, so that approximate function need not be Holder at all.
Alternatively, use component signs of the polyline's own complement;
that gives an admissible but different witness by the signed-distance
lemma.

## Scope and dependencies

This is exact planar geometry and a certified distance-approximation
lemma. It provides no finite-alpha operator value by itself. The
normalization of the increment kernel agrees with 01_setup/PROOF.md;
a=1/2 is the unit-pole-distance convention used in the team reports.

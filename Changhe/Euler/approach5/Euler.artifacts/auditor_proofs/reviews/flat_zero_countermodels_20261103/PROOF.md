# What flat zeros and transport alone do not imply

Status: CONFIRMED as A483 after the complete independent reconstruction and postwrite read. These are local countermodels to stronger geometric inferences, not counterexamples to Euler nonexistence. Read after in the team records, whose verification folder pins the complete source and focused configured-model review.

## 1. A genuine curl with an isolated transverse double zero

In a small Euclidean Cartesian box with coordinates (x,y,z), let b!=0, R any real constant, and

    F(x,z)=z/2-sinh(2z)cos(2x)/4,
    U=R grad F+(b-F)e_y.

Then U is analytic, div U=0 and U.curl U=0. Its vorticity is

    W=(F_z,0,-F_x).

On z=0, W=(sin^2 x,0,0). On the line x=z=0, U=b e_y, W=DW=0. In a sufficiently small box this line is the entire zero set of W, so the zero on the surface z=0 does not extend to a transverse surface of zeros. No nonconstant closed W orbit lies in the box.

Proof. The function F is independent of y and satisfies F_xx+F_zz=0. Direct curl and divergence give the formulas, and U.W=R F_x F_z-R F_z F_x=0. The Taylor expansion

    F=zx^2-z^3/3+terms of degree at least five

proves the flatness statements. More exactly,

    F_x=(sinh(2z)sin(2x))/2,
    F_z=(1-cosh(2z)cos(2x))/2.

If |x|<pi/4 and both derivatives vanish, F_x=0 implies z=0 or x=0. The second equation then forces respectively x=0 or z=0. Thus the vorticity zero set is precisely the indicated line.

Any nonconstant periodic orbit of a C1 autonomous vector field is, after taking its least period, a simple closed regular curve. Here Wy=0 and WF=0, so such an orbit would be a closed regular level curve F=k in an (x,z) plane. Its Jordan interior D lies within the planar rectangle, since the rectangle is convex. Green's identity, applied to F-k, gives

    integral_D |grad F|^2
      =integral_boundary_D (F-k)partial_n F
       -integral_D (F-k)Delta F=0.

Continuity then forces grad F=0 on the orbit, a contradiction.

This field fails the actual Euler vorticity equation for every c>0 and every omega. To see this without choosing pressure, put A=cI-omega J, B=A(x,y,z)+U and kappa=1+c. A necessary equation is

    R_v=(B.grad)W-(W.grad)B+kappa W=0.

On z=0 the x component is exactly

    (R_v)_x=(cx+omega y)sin(2x)+sin^2 x.

Indeed B_x=cx+omega y, partial_x B_x=c, partial_z W_x=0 and W=(sin^2 x,0,0) there. At y=0 this is (2c+1)x^2+O(x^4), nonzero for small nonzero x. Thus this construction proves only that actual curl, incompressibility and zero helicity do not propagate a surface double zero into a transverse zero sheet.

## 2. A quadrant transport model with no closed vortex orbits

Work on the abstract product cylinder S1_theta times (-epsilon,epsilon)_h times (-epsilon,epsilon)_z, with flat product metric and volume. Choose c in (0,1/2), d=3c, kappa=1+c, nu!=0, and real rho,s with s=d-rho and rho s<0. Choose an integer m>=4 large enough that

    r=(-kappa-(m-1)s)/rho>3.

For h>0,z>0 define

    phi=theta-(nu/rho)log h,
    Psi=h^r z^m sin^2 phi,
    W0=(partial_z Psi,0,-partial_theta Psi),
    B0=nu partial_theta+rho h partial_h+s z partial_z.

Extend Psi and W0 by zero when h<=0 or z<=0. Then W0 is C2, W0=DW0=0 on both coordinate cylinders, div W0=0, div B0=d and

    [B0,W0]=-kappa W0.

There is no nonconstant closed W0 orbit. Each of the two phase strips modulo2pi is a connected component of {W0!=0}, and its closure contains the entire central circle h=z=0.

Proof. Since -s/rho>0, r grows to infinity with m, so the choice is possible. Every derivative of W0 of order at most2 has a bounded trigonometric factor and a factor at least h^(r-2) in h and z^(m-3) in z, with the other coordinate powers nonnegative on compact boxes. These exponents are positive. The derivatives therefore extend continuously by zero across either axis, including their intersection. First derivatives vanish there as claimed. The mixed partial cancellation proves div W0=0.

B0 phi=0. The theta component of W0 has weight rho r+s(m-1), and the z component has scalar weight rho r+s m but the bracket subtracts s W0_z. Both weights therefore equal -kappa. This proves the bracket relation directly. The divergence of B0 is rho+s=d.

In a phase strip, W0_h=0 and W0_theta=m h^r z^(m-1)sin^2 phi>0. Along an orbit h is fixed, so theta stays in an interval of length pi between its two nodal boundaries. Uniqueness prevents a nonconstant orbit from crossing the zero set. Strict increase in theta within that interval rules out periodicity, even on S1. The map (theta,h,z) to (phi modulo2pi,h,z) is a diffeomorphism for h,z>0, so each strip is connected. For any prescribed theta on the central circle, choose a sequence h_n tending to zero for which phi modulo2pi stays in a fixed strip and choose z_n tending to zero. These points approach that theta on the central circle.

One may additionally set H=h and g=-rho h/a, a=1-2c, to get B0H=-ag and dH wedge dg=0. This does not prove g=U.B0, B0=Ay+U, div U=0 or curl U=W0 for any physical Euler velocity. The product-cylinder geometry also cannot simply be identified with a Euclidean tube. This example tests only the indicated transport and flatness relations.

## 3. Scope

The first construction retains actual Euclidean curl, divergence and zero helicity but violates Euler transport. The second retains exact transport, divergence of vorticity and the carrier, and flat quadrant geometry, but supplies no physical velocity. Neither excludes or constructs a full Euler flat periodic witness. The normal-form equations retain precisely the missing coupling B=Ay+U. No numerical experiment is used.

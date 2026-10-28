# A singular angular adjoint for the local central strain

## Statement and scope

Let A>0, D=2A+1 and C=A+D=3A+1. On the plane define

    B=diag(-A,D), T_0 h=BX dot grad h-h,
    b(theta)=-A cos^2 theta+D sin^2 theta,
    v(theta)=C sin theta cos theta,
    p=(4A+2)/C, q=(5A+1)/C.

Then 4/3<p<2, 1<q<5/3 and p+q=3. This topic constructs an exact local adjoint identity for the scalar

    c_R[h]=(1/pi) integral_(|X|<R) h(X) sin(3theta)/r^3 dX.

It is a frozen-transport statement. It does not replace T_0 by the full nonlocal linearization, establish an inverse, or eliminate a boundary flux.

For theta in (0,pi/2), put

    W(theta)=sin(theta)^(-p) cos(theta)^(-q),
    F(theta)=sin(3theta) sin(theta)^(p-1) cos(theta)^(q-1),
    omega_0(theta)=-(W(theta)/C) integral_0^theta F(s) ds. (1)

Extend omega_0 to the plane's angular circle with even-x, odd-y parity. Let

    H(theta)=cos^2(theta)sin(theta) omega_0(theta).

This H extends continuously to the axes, is bounded and nonpositive, and is integrable. The factor omega_0 itself is not locally integrable across x=0. Its use below is a pairing on the stated factor class, not an unqualified distribution represented by a locally integrable function.

Let R>0 and h=x^2 y f on the closed disk, where f is C1 with even-even parity. Then all integrals in

    c_R[h]=(1/pi) integral_(|X|<R) omega_0(theta) T_0 h/r^3 dX
       -(R^2/pi) integral_0^(2pi) b(theta)H(theta)f(R,theta)dtheta (2)

are absolutely convergent. In particular if f vanishes near the outer circle, the flux is zero. If

    F_0=T_0 h/(x^2 y)=BX dot grad f

is bounded, then

    |c_R[h]| <= K_A R^2 ||F_0||_(L-infinity(B_R))           (3)

for such zero-flux h, where the explicit sufficient constant is

    K_A = B(p/2,q/2) B(1-p/2,p/2)/(2 pi C).               (4)

Here B(a,b)=integral_0^1 t^(a-1)(1-t)^(b-1)dt is the Euler beta integral; every argument in (4) is positive. The same formula (2) gives a bound with its displayed boundary term for general f. No assumption J(h)=0 is needed.

## Derivation of the adjoint equation

For the Euclidean measure, the formal adjoint is

    T_0^* psi=-BX dot grad psi-(D-A+1)psi.

Substitute psi=r^(-3)omega(theta). The equation T_0^* psi=r^(-3)sin(3theta) becomes

    -v omega' + [3b-(D-A+1)]omega=sin(3theta).             (5)

Since

    3b-(D-A+1)=C[-p cos^2(theta)+q sin^2(theta)],
    W'/W=-p cot(theta)+q tan(theta),

W solves the homogeneous equation. Variation of constants gives

    (omega/W)'=-F/C.                                     (6)

Equation (1) is therefore an exact solution of (5), and all solutions on a quadrant differ by a constant multiple of W.

## The compatibility obstruction at the two axes

The complete integral in (6) is

    I=integral_0^(pi/2) F(theta)dtheta
      =(2-p)/2 B((p+1)/2,q/2)>0.                         (7)

Indeed sin(3theta)=3sin(theta)-4sin^3(theta). The two sine-cosine integrals are beta integrals with first arguments (p+1)/2 and (p+3)/2. Integration by parts in the beta integral gives B(a+1,b)=a B(a,b)/(a+b). Since p+q=3, their ratio is (p+1)/4, yielding (7).

Near theta=0,

    omega_0(theta)=-3 theta/[C(p+1)]+O(theta^3).

Near theta=pi/2, with t=pi/2-theta,

    omega_0(theta)=-(I/C)t^(-q)(1+O(t^2))+O(1).

A solution bounded at theta=0 must have the homogeneous coefficient zero in (1), so it is omega_0 and necessarily diverges at the other axis. A solution bounded at theta=pi/2 is instead

    omega_1=(W/C) integral_theta^(pi/2) F(s)ds,

which tends to -1/(Cq) at that endpoint and diverges like (I/C)theta^(-p) at theta=0. Thus no classical solution of (5) is bounded at both axes. A bounded homogeneous degree-minus-three adjoint for this strain kernel cannot be obtained by choosing a different integration constant.

The integrand F is positive before pi/3 and negative after pi/3. Its cumulative integral starts at zero, increases, and then decreases to the strictly positive value I. It is positive throughout (0,pi/2). Therefore omega_0<0 in that quadrant. Multiplication by cos^2(theta)sin(theta) gives

    H(theta)=O(theta^2) as theta->0,
    H(theta)=O((pi/2-theta)^(2-q)) as theta->pi/2.

Because 2-q>0, H extends continuously by zero at both ends. Reflection preserves the sign of H and its continuity. This proves the stated boundedness and integrability without pretending that omega_0 is an ordinary locally integrable kernel on all densities.

## Integration by parts on the factor class

First work on the annulus epsilon<r<R with angular distance greater than eta from every axis. The functions are smooth there, so ordinary integration by parts gives the volume pairing with T_0^*psi plus the flux of psi h BX. The outer radial flux is exactly the second term in (2), with positive sign before it is moved to the right side.

At a cut angular side near y=0, the flux density is proportional to

    v omega_0 cos^2(theta)sin(theta)f = O(theta^3).

Near x=0 it is O(t^(3-q)), which tends to zero since q<3. Boundedness of f, the finite radial interval and these positive exponents allow the angular cutoffs to be removed. The volume terms are absolutely integrable because both h and T_0h contain x^2y, with bounded C0 factors; the angular multiplier is H.

The inner radial flux has magnitude at most

    (epsilon^2/pi) ||f||_infinity integral |b H| dtheta,

so it vanishes as epsilon->0. Dominated convergence for the volume integrals now proves (2) on the full disk. C1 regularity suffices because the integration-by-parts formula can first be applied to smooth approximations of f converging in C1, with the same integrable dominating angular factors.

## Explicit bound

The absolute value of the cumulative integral in (1) is at most

    (1/2) B(p/2,q/2),

using |sin(3s)|<=1. Since p+q=3,

    |H(theta)| <= [B(p/2,q/2)/(2C)]
                     sin(theta)^(1-p) cos(theta)^(p-1).

Both endpoint exponents exceed -1. Integrating over all four quadrants gives

    integral_0^(2pi)|H|dtheta
       <= B(p/2,q/2) B(1-p/2,p/2)/C.                     (8)

The radial area integral is R^2/2. Applying (8) to the first term of (2) proves (3)-(4). This sufficient bound is not asserted sharp.

As an internal normalization check, multiply (5) by cos^2(theta)sin(theta) and integrate. The angular boundary terms vanish as above. The identity T_0(x^2y)=0 and v'=D-A-2b give

    integral b(theta)H(theta)dtheta=-pi/8.

Indeed the right side of (5), paired with cos^2(theta)sin(theta), integrates to pi/4. This also makes (2) exact for h=x^2 y times any smooth radial cutoff.

## Relevance and limitations

A bounded unweighted angular adjoint is obstructed by the positive compatibility integral (7). Nevertheless the admitted factor class supplies enough axis vanishing for the singular adjoint pairing. This distinguishes a direct c estimate from a gap controlling an entire radial moment. It is consistent with the quasimodes in topics 05 and 07, which have c=0 after correction.

For the full linearization one must insert

    T_0 h=Lh-(V-BX) dot grad h
              -(U[h]+c[h]X/3) dot grad rho.

Equation (2) remains an algebraic starting point only when every inserted factor pairing exists. Bounding those error pairings, the outer flux and their nonlocal dependence is additional work. The constant in (4) alone is not a local or global inverse bound for IPM.

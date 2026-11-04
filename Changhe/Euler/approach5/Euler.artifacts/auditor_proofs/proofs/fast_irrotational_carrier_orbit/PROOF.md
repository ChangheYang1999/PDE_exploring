# Arbitrarily fast periodic carrier orbits for exact irrotational local profiles

## Exact statement and scope

Let 0<c<1/2, omega be any nonzero real number, R>0 and L>0. Put A=cI-omega J, a=1-2c, B=Ay+U, and W=curl U. There are explicit smooth solutions of

    div U=0,
    (1-c)U+(B.grad)U+omega JU+grad P=0

on a neighborhood of the circle C={y1^2+y2^2=R^2,y3=0}, with W=0 there, for which C is a periodic carrier orbit and its backward-flow Lyapunov spectrum is (L,0,-3c-L). Its normalized angular probability is full-flow ergodic, nonstationary and has entropy zero for the time-one map.

One such profile is smooth on all of R3 but has cubic growth and incomplete backward trajectories. Another is smooth on R3 minus the origin and has U=O(|y|^-2) at infinity but has an irremovable singularity at the origin. Neither is a target counterexample, nor a counterexample to a bound proved using the complete global hypotheses of the campaign. They exclude only a bound on these exponents from local irrotational Euler identities alone.

At omega=0 the same constructions yield a circle of equilibria. The normalized circle measure is then not ergodic; point masses provide an equilibrium test instead.

## 1. Harmonic potentials solve the full local equation

Let phi be real C3 and harmonic on an open domain, and set

    U=grad phi, q=|grad phi|^2/2,
    P=-a phi-q-(Ay).grad phi.                         (1)

Then div U=0 and W=0. Symmetry of the Hessian gives

    (B.grad)U=D2 phi Ay+grad q,
    grad[(Ay).grad phi]=A^T grad phi+D2 phi Ay.

Substitution in momentum leaves [(1-c)I+omega J-aI-A^T]grad phi=0 because A^T=cI+omega J. Thus (1) verifies pressure and every momentum component directly. The reduced Bernoulli scalar is H=P+q+Ay.U=-a phi. For an axisymmetric phi, (Jy).grad phi=0 and the pressure is independent of omega.

## 2. Entire polynomial example

Write r^2=y1^2+y2^2 and z=y3. Define

    b=-c/2+L/4, d=-L/(8R^2),
    phi=b(r^2-2z^2)+d(r^4-8r^2 z^2+(8/3)z^4).       (2)

The Laplacian of the quadratic factor is 4-4=0. For the quartic factor, the three Laplacians are 16r^2, -8(4z^2+2r^2), and 32z^2, whose sum is zero. Thus (1) gives a polynomial exact Euler profile.

Away from the axis, any axisymmetric potential gives

    r'=cr+phi_r, theta'=-omega, z'=cz+phi_z.           (3)

Potential (2) is even in z, so z=0 is invariant. On this plane,

    r'=(L/2)r(1-r^2/R^2).

It vanishes at r=R and its radial derivative there is -L. The vertical derivative is

    c+phi_zz(R,0)=c-4b-16dR^2=3c+L.

The mixed radial-vertical derivatives vanish by evenness. Hence C has period 2pi/|omega| and forward transverse exponents -L and 3c+L.

Since d!=0, the velocity has nonzero cubic terms and fails sublinearity and decay. Under backward time on z=0, r'=Lr(r^2/R^2-1)/2. For every r0>R the integral from r0 to infinity of 2/[Lr(r^2/R^2-1)] is finite. This proves actual finite-time backward escape, not merely absence of a proven completeness bound.

## 3. Decaying example with a singular origin

Put s=|y| and

    M=(5c+L)R^3/2, Q=(3c+L)R^5/6,
    phi=M/s+Q(2z^2-r^2)/s^5, s>0.                   (4)

The first term is harmonic off the origin. The second equals Q partial_zz(1/s), hence is also harmonic. On z=0,

    phi=M/r-Q/r^3,
    r'=cr-M/r^2+3Q/r^4.

The chosen constants give M=cR^3+3Q/R^2, so r=R is stationary in the radial equation. Its derivative there is

    c+2M/R^3-12Q/R^5=3c-6Q/R^5=-L.

Direct expansion at z=0 gives phi_zz=-M/r^3+9Q/r^5, so c+phi_zz(R,0)=3c+L. Evenness again eliminates mixed transverse derivatives, and (3) yields the same circle and spectrum.

At infinity grad phi=O(s^-2) uniformly in direction. Near zero the quadrupole gradient is homogeneous of degree -4 and nonzero on an open set of directions because Q>0. Thus U is unbounded near zero and has divergent energy there. No continuous extension can satisfy the target C2 hypothesis.

Writing phi0=M/s and phi2=Q(2z^2-r^2)/s^5, homogeneity in (1) gives the explicit pressure

    P=(3c-1)phi0+(5c-1)phi2-q.

This pressure follows from momentum. No unrelated harmonic-pressure normalization is imposed. Global completeness on the punctured domain is not asserted.

## 4. Exact measure and Lyapunov calculation

On C the flow is theta(t)=theta(0)-omega t. The normalized angular measure is invariant under every real rotation. Any measurable set invariant modulo null sets under this full flow is invariant under every rotation, so has measure zero or one. Thus the full flow is ergodic, irrespective of rationality of omega/(2pi). The time-one rotation is an isometry, whose metric entropy is zero; no time-one ergodicity is assumed.

In the orthonormal radial, angular and vertical frame along C, the derivative of the forward flow is diag(exp(-Lt),1,exp((3c+L)t)). The frame itself rotates orthogonally, which does not change norms or exponents. Reversing time proves (L,0,-3c-L). These are exact constants, not numerical Floquet estimates.

In particular L can exceed 2(1-2c) or any larger prescribed bound. The Gamma_Z in A399 and A417 concerns the maximal compact core of an entire uniformly sublinear profile with nonzero vorticity. Both examples violate those global hypotheses, and their vorticity is identically zero. They do not realize that campaign core. They show that any automatic global bound must use more than local harmonicity, pressure Poisson, exact local momentum or the entropy of the circle measure.

## Verification

The submitted LIT87 proof was read in full and every formula above independently differentiated. No computation, numerical experiment or external existence theorem is needed. The exact submission is pinned in the team records. The proof is independent of the conditional coverage theorem; that theorem supplies only the context of the proposed bound being tested.

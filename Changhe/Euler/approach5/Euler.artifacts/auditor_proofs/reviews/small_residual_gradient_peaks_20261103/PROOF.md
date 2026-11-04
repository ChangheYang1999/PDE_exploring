# Small momentum residual with superpolynomial gradient peaks

Status: A806-A809 CONFIRMED. This is an explicit counterexample to an approximate-profile gradient inference. It is not an exact rotating Euler profile and does not settle the campaign conjecture.

## 1. Statement and smooth ingredients

Let Jx=(-x2,x1,0), A=cI-omega J and L=(1-c)I+omega J. There is a fixed constant C such that for every 0<epsilon<=1 there are smooth real U,P on R3, independent of c and omega, with the following properties for every 0<c<1 and omega in R:

    div U=0, U.curl U=0, U in L2,
    (1+|x|)^N U(x)->0 for every finite N>=0,
    P=partial_i partial_j Gamma*(U_i U_j)=Gamma*tr((DU)^2),
    -Delta P=tr((DU)^2), Gamma(x)=1/(4pi|x|),
    |P(x)|<=C epsilon^2(1+|x|)^(-3), DU,grad P in L3,
    |LU+DU(Ax+U)+grad P|<=C epsilon(1+|x|)^(-4).        (1)

The ordinary potential of the L1 source in(1) is absolutely convergent at every point. Nevertheless neither gradient has a polynomial pointwise growth bound. At z_n=(0,0,10^n), and at some y_n on the sphere |y_n-z_n|=2^(-5n^2/2)/2,

    DU(z_n)=epsilon 2^(3n^2/2)J,
    |grad P(y_n)|>=epsilon^2 2^(n^2/2)/3.               (2)

Writing the momentum residual as R, one has

    curl R(z_n)=2epsilon 2^(3n^2/2)e3.                  (3)

Thus the residual is never zero for these parameters. The constants in(1) do not depend on c,omega or epsilon. Constants for arbitrary rapid-decay weights may depend on N.

For a concrete cutoff put b(s)=exp(-1/s) for s>0 and zero otherwise, and

    chi(s)=b(4-s^2)/(b(4-s^2)+b(s^2-1)).

Its denominator is positive everywhere. It is even and smooth, equals1 on [-1,1] and zero outside[-2,2]. Define f(s)=s chi(s) for s>=0 and H(s)=integral_s^infinity t chi(t)^2 dt. Then H'=-f^2/s, with its smooth continuation at zero, and H(s)=H(0)-s^2/2 near zero. The radial function H(rho/ell) is therefore Cartesian smooth, including at rho=0.

## 2. One tube and its exact canonical pressure

For positive a,ell,L,R with ell<=L, put rho=sqrt(x1^2+x2^2), s=rho/ell, t=(x3-R)/L and

    U0=(a/ell)chi(s)chi(t)Jx=a f(s)chi(t)e_phi,
    P0=-a^2 chi(t)^2 H(s).                            (4)

Both are smooth and supported in rho<=2ell, |x3-R|<=2L. The velocity is divergence free. Its curl has only radial and axial components away from the axis, so its helicity vanishes there and, by continuity, everywhere. Its acceleration is

    DU0 U0=-a^2 f(s)^2 chi(t)^2/(ell s)e_rho.

The radial derivative of P0 cancels this exactly, leaving

    DU0 U0+grad P0=(partial_3 P0)e3,
    |partial_3 P0|<=C a^2/L.                          (5)

Let F=tr((DU0)^2). Divergence of the acceleration gives F, so

    -Delta P0=F-partial_3^2 P0.

Set v=partial_3^2 P0, q=Gamma*v and P_tube=P0+q. Then -Delta P_tube=F with the required sign. Compact support and integration by parts give

    q=(partial_3^2 Gamma)*P0,
    P_tube=Gamma*F=partial_i partial_j Gamma*(U0_i U0_j). (6)

Thus this is exactly the canonical pressure, without adding a harmonic term.

The source bounds are |v|<=C a^2/L^2 and ||v||1<=C a^2 ell^2/L. Split the Newtonian kernels at radius d. Their near integrals give

    ||q||infinity<=C(||v||infinity d^2+||v||1/d),
    ||grad q||infinity<=C(||v||infinity d+||v||1/d^2).

Taking d=(ell^2 L)^(1/3) yields

    ||q||infinity<=C a^2 ell^(4/3)L^(-4/3),
    ||grad q||infinity<=C a^2 ell^(2/3)L^(-5/3).        (7)

For the L3 estimate, the near part of grad Gamma has L1 norm at most Cd, while its far part has L3 norm at most C/d. The elementary convolution inequality therefore gives

    ||grad q||3<=C[d||v||3+d^(-1)||v||1]
                <=C a^2 ell^(4/3)L^(-4/3).             (8)

The last inequality uses the cylinder volume O(ell^2 L). These estimates use ordinary absolute kernels, not an unverified singular-integral cancellation.

## 3. Infinite sum and all convergence claims

Choose n>=1 and

    R_n=10^n, L_n=R_n/20,
    ell_n=2^(-5n^2/2), a_n=epsilon 2^(-n^2).            (9)

Their support cylinders have axial ranges[0.9R_n,1.1R_n], hence are disjoint and leave every compact set. Define U=sum U_n, P0=sum P0_n, q=sum q_n, P=P0+q using(4)-(6). U and P0 are locally finite smooth sums. On the nth support |x| is comparable to R_n. Since 10^(Nn)2^(-n^2)->0 for every N, they have rapid decay of every order, with amplitudes O(epsilon) and O(epsilon^2), respectively. Also

    ||U||2^2<=C sum a_n^2 ell_n^2 L_n<infinity.        (10)

Equations(7) imply uniform absolute convergence of q and grad q. On a fixed compact set, all sufficiently distant tubes satisfy |x-y|>=c0R_n. Differentiating the separated kernel in q_n=Gamma*v_n gives

    |D^j q_n(x)|<=C_j R_n^(-1-j) a_n^2 ell_n^2/L_n.

This is summable for every fixed derivative order, so q and P are globally smooth. Each individual q_n and grad q_n vanishes at infinity, and uniform summability gives the same for the sums.

The source has the explicit radial formula

    F_n=-(a_n^2/ell_n^2)chi(t)^2 (f(s)^2)'/s.

In particular ||F_n||1<=C a_n^2L_n, a summable bound. Disjoint supports imply tr((DU)^2)=sum F_n in L1. Its Newtonian integral converges absolutely at each x: the source is locally smooth and bounded near x, and outside a fixed ball the kernel is bounded and the source integrable. Equations(6) pass to the sum by absolute convergence. Alternatively the stresses U_i U_j of finite sums converge in L1 by(10); the associated convolution distributions converge after testing against any Schwartz function. This proves both canonical representations in(1) and the Poisson equation. There is no harmonic normalization freedom in this construction.

## 4. Uniform pressure and residual decay

Let r=|x| be large. If R_n<=r/3, the support is in |y|<=1.2R_n, so its distance from x is at least0.6r. Using the second representation of q in(6),

    |q_n(x)|<=C r^(-3)||P0_n||1,
    |grad q_n(x)|<=C r^(-4)||P0_n||1,
    ||P0_n||1<=C a_n^2 ell_n^2L_n.

The last masses sum to at most C epsilon^2. For R_n>r/3 use(7). Their terms are epsilon^2 times 2^(-b n^2)10^(d n), with b>0 and d fixed, so the resulting tail is O_N(epsilon^2 r^(-N)) for every fixed N. For example dominate it eventually by 10^(-(N+1)n), sum the geometric tail, and absorb the finitely many initial indices into the constant. Hence

    |q(x)|<=C epsilon^2(1+r)^(-3),
    |grad q(x)|<=C epsilon^2(1+r)^(-4).                (11)

Together with rapid decay of P0 this proves the pressure bound.

Axisymmetry gives the exact identity DU_n Jx=J U_n, so every omega term cancels from LU+DU Ax. On the nth support the remainder is the azimuthal vector

    T_n=a_n[(1-c)f(s)chi(t)+c s f'(s)chi(t)
                     +c(x3/L_n)f(s)chi'(t)]e_phi.      (12)

Here |x3/L_n|<=22; thus |T_n|<=C a_n uniformly for all0<c<1. Because the velocity supports are disjoint, their nonlinear accelerations have no cross terms. Equation(5) therefore gives the exact full residual

    R=sum_n[T_n+(partial_3 P0_n)e3]+grad q.             (13)

The sum is rapidly decaying of every order, bounded by C_N epsilon(1+r)^(-N) for epsilon<=1. Equation(11) proves the residual estimate in(1) with one fixed constant for the full c,omega range. Large individual nonlinear and pressure terms have been canceled algebraically, not estimated separately.

## 5. Total-pressure peaks and the nonzero residual

On B(z_n,ell_n), both cutoffs are1 and all other velocity tubes vanish. Thus U=(a_n/ell_n)Jx, DU=(a_n/ell_n)J, and

    Delta P=2(a_n/ell_n)^2.                            (14)

This is the total canonical pressure, including all other tubes. Integrating(14) over the ball of radius ell_n/2, its outward flux divided by sphere area is a_n^2/(3ell_n). Some point on the sphere therefore has gradient norm at least this large. Substitution of(9) gives precisely(2). Both gradients grow faster than every polynomial in |z_n| or |y_n|.

In the same ball equation(12) reduces to T_n=U, and partial_3P0_n=0. Equation(13) says R=U+grad q. Taking curl proves(3). This makes explicit why small momentum residual does not give small residual in the vorticity equation.

For a second direct check, choose s_* in(0,2) at a positive maximum of f. At rho=ell_n s_*,x3=R_n, one has f'(s_*)=0, and the azimuthal residual is (1-c)a_n f(s_*)>0. All pressures are axisymmetric, so pressure cannot cancel this component. The residual is thus nonzero for every omega and every0<c<1.

## 6. Both gradients are in L3

The cylinder volume and ell_n<=L_n give

    ||DU_n||3^3<=C a_n^3 L_n/ell_n,
    ||grad P0_n||3<=C a_n^2 L_n^(1/3)ell_n^(-1/3).

The first series equals a constant times epsilon^3 sum 10^n2^(-n^2/2); the second is a summable Gaussian-in-n sequence as well. Disjointness proves DU in L3. The triangle inequality proves grad P0 in L3. Equation(8) gives sum ||grad q_n||3<infinity; its L3 limit agrees distributionally with the smooth derivative already constructed. Thus grad P is in L3 despite(2).

## 7. Scope and verification

The construction verifies every item of LIT180 using exact calculus and convergent series. No numerical computation was needed. It extends the kinematic gradient-peak test by making the momentum residual small and decaying, uniformly in c and omega. It does not approximate the vorticity equation in a uniform first-derivative norm and cannot refute an exact-profile gradient or Liouville theorem.

The exact source was read in full and retained alongside this independent proof. Continuing collaboration is through the existing configured model agents; provider runtime is not independently attested.

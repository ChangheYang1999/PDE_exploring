# Cumulative source: logarithmic density and the failure of a pointwise limit

Status: confirmed in A3087 with the qualified C comparison and ordinary-measure refinement in A3088. The example is kinematic and fails full Euler; stronger full-profile conclusions remain OPEN in A3089.

## 1. Exact statements and notation

Let U be C1 and divergence-free on R3. Write E(r)=integral_(B_r)|U|^2, T(r)=integral_(partial B_r)|U|^2, N(r)=integral_(partial B_r)|U.e_r|^2, q=tr((DU)^2), S(r)=integral_(B_r)q, and A(r)=integral_0^r s S(s)ds. Surface integrals use area measure. Assume

    E(r)=L r^beta+O(r^(beta-1)), L>0, 0<beta<1.

For every fixed lambda>1 and 0<kappa<1-beta, define G={r in [R,lambda R]: A(r)<=-kappa E(r)}. There is a finite C, independent of sufficiently large R, such that

    integral_G dr/r >= [1-beta/(1-kappa)]log(lambda)-C/R.   (1)

Only E(r)/(L r^beta)->1 is needed for the same conclusion with an error o(1).

Conversely, for each L>0 and 0<beta<1 there is a smooth divergence-free U that decays uniformly, has the displayed energy asymptotic, and satisfies A(R_n)=L R_n^beta+O(R_n^(beta-1)) at R_n=10^n. At other unbounded radii A=-E. Its energy derivative also fails E'(r)~beta L r^(beta-1). No single-valued C1 pressure makes this example a full profile for any finite c and omega.

For full bounded C1/C1 profiles with Hb and 2/5<c<1/2, the confirmed A3053 energy law supplies the hypotheses of (1) with beta=5-2/c, L>0 whenever U is nonzero. The counterexample makes no assertion about a full-profile pointwise limit.

## 2. Radial identities and the density estimate

Local C1 convolution of a divergence-free U gives, on passing the divergence theorem to the limit,

    S(r)=integral_(partial B_r)((U.grad)U).e_r.

Put U(r theta)=u theta+V with V tangent to S2. Then div_S V=-r partial_r u-2u, and the radial acceleration is u partial_r u+r^-1 V.grad_S u-r^-1|V|^2. Integration by parts on S2, with the factor r^2 of surface area, gives

    S=N'-(T-N)/r, E'=T, 0<=N<=T.

Thus (rN-E)'=rS. Since E and rN are O(r^3) at0, integration gives A=rN-E with no constant. This is also the independently reconstructed identity in the cumulative-source review.

E is positive for all sufficiently large r. On the complement of G, rN/E>1-kappa. Therefore

    (1-kappa) integral_([R,lambda R] minus G) dr/r
      <=integral_R^(lambda R) N/E dr
      <=integral_R^(lambda R) E'/E dr
      =log(E(lambda R)/E(R)).

The assumed relative error is O(1/r), so the last expression is beta log(lambda)+O(1/R). Subtract from the total logarithmic measure log(lambda) to get (1). For relative o(1) use the same logarithm argument. This proof never differentiates the energy error. Its positive lower proportion requires the strict inequality kappa<1-beta.

## 3. Baseline with no accumulated energy offset

Let J(y1,y2,z)=(-y2,y1,0) and K0=8pi/3. For U_f=f(r)Jy, direct integration on the sphere gives T_f(r)=K0 r^4 f(r)^2, while N_f=0 and div U_f=0. Set b=sqrt(beta L/K0) and p=(beta-5)/2.

Choose a smooth cutoff taking values in [0,1], equal to0 for r<=7/4 and1 for r>=2. Multiplying b r^p by it gives a smooth exterior profile whose energy inside2 is less than beta L integral_(7/4)^2 r^(beta-1)dr<L 2^beta. Add a scalar smooth bump supported in (1/2,1), with positive amplitude chosen to supply exactly the missing energy. The two radial summands have disjoint supports, so their squared energies add. Call their sum f0. It is smooth, vanishes near0, equals b r^p for r>=2, and has total energy L 2^beta inside2.

Consequently U0=f0(r)Jy is globally smooth and divergence-free, and for every r>=2,

    E0(r)=L r^beta, T0(r)=beta L r^(beta-1), N0(r)=0.     (2)

The exact initial energy is essential. An uncancelled constant offset would exceed the required error r^(beta-1), which tends to zero.

## 4. Poloidal shells and exact compensation

Choose an even real phi in C_c^infinity((-1,1)) with phi(0)=1, hence phi'(0)=0. Let I0=integral phi^2, I1=integral (phi')^2 and Cphi=8I0+2I1. Choose nonnegative chi in C_c^infinity((2,3)) with integral1 and D=||chi||_infinity. Fix

    0<delta<min(1/4,beta/(4 Cphi D)).

For every integer n>=1, at R_n=10^n put ell_n=ceiling(R_n/delta), Lambda_n=ell_n(ell_n+1), and choose an L2-normalized real zonal spherical harmonic Y_n of degree ell_n about the vertical axis. Define

    a_n=sqrt(2L R_n^(beta+1))/Lambda_n,
    h_n(r)=a_n phi((r-R_n)/delta),
    W_n=(Lambda_n h_n/r^2)Y_n e_r+(h_n'/r)grad_S Y_n.     (3)

Since Delta_S Y_n=-Lambda_n Y_n, the two polar divergence terms are Lambda_n h_n'Y_n/r^2 and its negative. Thus W_n is divergence-free. The support is the shell |r-R_n|<delta; smooth compact support of phi makes extension by zero smooth. Orthogonality of radial and tangential components, and integral |grad_S Y_n|^2=Lambda_n, give

    N_n=Lambda_n^2 h_n^2/r^2,
    T_n=N_n+Lambda_n(h_n')^2.                            (4)

On its support r>=R_n/2 and Lambda_n>=R_n^2/delta^2. Therefore its positive total energy e_n satisfies

    e_n<=8L delta R_n^(beta-1) I0
          +2L delta R_n^(beta-1) I1
        =Cphi L delta R_n^(beta-1).                     (5)

On the later interval (R_n+2,R_n+3), (2) gives T0>=beta L R_n^(beta-1)/2. Hence e_n chi(r-R_n)<=T0/2. Define k_n=e_n chi(r-R_n)/T0(r) on this interval and zero elsewhere. Its extension is smooth, 0<=k_n<=1/2, and its support avoids every zero of T0. All these intervals and poloidal shells are disjoint. Set

    f=f0 sqrt(1-sum_n k_n), U=f(r)Jy+sum_n W_n.           (6)

The sums are locally finite, the square root is smooth and bounded away from zero, and U is globally smooth and divergence-free. Zonal Y_n has no azimuthal gradient, so W_n is pointwise orthogonal to Jy. Thus there are no energy cross terms:

    T=T0-sum_n e_n chi(r-R_n)+sum_n T_n, N=sum_n N_n.    (7)

Each complete added shell is followed by removal of exactly e_n. Consequently E-E0=0 outside [R_n-delta,R_n+3], and within this interval it lies between0 and e_n. These intervals are disjoint and r is comparable to R_n there. Equation (5) proves E=L r^beta+O(r^(beta-1)) without any residual constant from earlier shells.

At r=R_n, (3)-(4) give N=2L R_n^(beta-1), and phi'(0)=0 gives T_n=N_n. Equations (2) and (7) then give

    A(R_n)=R_n N(R_n)-E(R_n)
          =L R_n^beta+O(R_n^(beta-1)),
    E'(R_n)=(beta+2)L R_n^(beta-1).                     (8)

Between the modified intervals N=0 and E=E0, hence A=-E. This proves both infinite envelopes and the failure of the proposed derivative asymptotic.

## 5. Angular degree and uniform decay

For an L2-normalized degree-ell spherical harmonic, rotation invariance of the sum of squared values over an orthonormal basis, followed by integration, gives

    |Y|<=sqrt((2ell+1)/(4pi)).

Apply the same argument to the sum of squared gradient norms, whose integral is Lambda(2ell+1), to obtain

    |grad_S Y|<=sqrt(Lambda(2ell+1)/(4pi)).

The invariance holds because each rotation acts orthogonally on the eigenspace and is an isometry of the sphere. These estimates bound each individual term of the nonnegative sums.

Here ell_n<=2R_n/delta. The radial term in (3) is bounded by C Lambda_n a_n sqrt(ell_n)/R_n^2. The tangential term is bounded by C a_n sqrt(Lambda_n ell_n)/(delta R_n). Substitution of a_n and Lambda_n>=R_n^2/delta^2 bounds both by

    C_(L,delta,phi) R_n^((beta-2)/2).

This tends to zero, since beta<1. The toroidal term is at most |U0|, of order r^((beta-3)/2) outside2. Disjoint supports and local finiteness prove uniform decay of U. They prove only local smoothness of all derivatives; no global derivative bound is asserted.

## 6. Full Euler fails on an untouched annulus

There are arbitrarily large open annuli where U=b r^p Jy. Vector axisymmetry gives (Jy).grad U=JU, so both rotational terms in the full profile equation cancel. The angular component or torque identity requires

    partial_theta P=-rho^2 b r^p(1+c p), rho^2=y1^2+y2^2.

A complete horizontal circle lies inside the annulus at any fixed appropriate r and z. The right side is constant on it, while a single-valued C1 P integrates to zero around it. Thus 1+c p=0 is necessary. If this condition fails, no pressure exists.

If it holds, all linear terms in momentum cancel, because y.grad(b r^p Jy)=(p+1)U. Directly, (U.grad)U=-b^2 r^(2p)(y1,y2,0). Hence momentum would demand

    grad P=b^2 r^(2p)(y1,y2,0).

Its first component has z derivative 2p b^2 r^(2p-2)y1 z, whereas the z component has y1 derivative zero. This is nonzero at points with y1 z!=0, since p<0. The vector is not a distributional gradient. Thus no C1 pressure exists in this case either. This covers every finite c and omega. No numerical residual is used.

## 7. Euler application and source scope

For the full C1/C1 equation, -Delta P=q in distributions. Local convolution and the divergence theorem give S=-4pi r^2 pbar'(r) and A=-4pi integral_0^r s^3 pbar'(s)ds for the actual spherical pressure mean pbar. Hence radii in G satisfy

    integral_0^r s^3 pbar'(s)ds>=kappa E(r)/(4pi).

This is a bound for an accumulated quantity. It is not a sign for the pressure derivative at that radius, nor for the spherical integral of q. A3053 supplies the exact energy law for every nonzero bounded Hb target profile, so (1) applies for every finite omega. The kinematic example refutes only an inference from energy, smoothness, divergence freedom and decay. A stronger conclusion using full momentum remains open.

All seven LIT370 sections, its32manual checks, reading record, formal-source scope and the one-hunk derivative precision were read. The example and density bound were independently reconstructed above. No computation or formal build was needed. An existing configured model analytical comparison is requested; actual provider execution is independently unattested. No novelty or optimal density constant is claimed.


## 8. Complete C comparison and an ordinary-measure version

The complete C comparison dated 2026-11-04T07:58:02Z was read, including
all eight analytical items. Its main proof agrees with Sections 1-7.
Its scripts, revised execution after initial failures, numerical crossover
values and claimed numerical comparisons of constants are not certified.
The following two analytical remarks are checked here.

The same set G has a lower bound for its ordinary Lebesgue measure:

    |G|/[(lambda-1)R] >= 1-beta/(1-kappa)-C/R.           (9)

On the complement of G, 1-kappa<rN/E<=rE'/E. Therefore

    (1-kappa)|[R,lambda R] minus G|
      <=integral_R^(lambda R) rE'/E dr
      =[r log E(r)]_R^(lambda R)-integral_R^(lambda R)log E(r)dr.

Write log E=log L+beta log r+epsilon(r), where epsilon=O(1/r).
The first two terms contribute exactly beta(lambda-1)R. The endpoint
terms r epsilon(r) are O(1), and the integral of epsilon over this fixed
ratio interval is O(log lambda), also O(1) for fixed lambda. This proves
(9). If only E/(Lr^beta) tends to1, the same calculation gives an o(1)
error after division by R: on the interval the supremum of |epsilon|
tends to zero. Neither proof differentiates epsilon. The strict range
0<kappa<1-beta is essential for a positive proportion. This ordinary-measure
bound is confirmed without the numerical comparison of alternative constants.

The explicit shells can also use real spherical harmonics of any allowed
azimuthal order. For a degree-ell harmonic Y, the cross term with the
azimuthal baseline is pointwise

    (f Jy).W=f h' partial_phi Y.

It need not be zero pointwise, but its integral over every sphere is zero
by periodicity. Hence the formulas for T, E and N, their exact compensation,
and the positive A(R_n) values still hold. The harmonic supremum bounds
and the triangle inequality still give uniform decay. The untouched annuli
still rule out full momentum. Zonality in the original construction is a
sufficient convenient choice, not a necessary one.

For precision, an angular energy decomposition uses the rotating vector
frame, or equivalently the action U(y) -> R^(-1)U(Ry) of axial rotations.
Orthogonal real Fourier pairs in that frame have zero cross integrals in
E, T and N. Divergence commutes with this rotation action, so each real
mode pair is divergence-free and has its own identity A_m=rN_m-E_m.
Summing gives the full A. This is a quadratic energy decomposition, not
an identification of A_m with the linear scalar Fourier projection of q.

In a variant using only nonzero azimuthal orders for W_n, the zero vector
mode is the compensated toroidal baseline f(r)Jy. Its radial energy is
zero, so A_0=-E_0<0 at large radii; here E_0 denotes that zero-mode energy,
not the unmodified baseline energy of Section 3. The positive values of
A(R_n) come from the nonzero mode pairs. This confirms C's mode remark at
that precise convention. No specified scalar source mode or pressure mode
is thereby forced to carry every radius in G.

The pressure conclusion remains an inequality for the accumulated integral
in Section 7. The full-profile pointwise limits, eventual signs, and any
optimal density constant remain outside this confirmation. Existing
configured model collaboration uses working files; actual provider execution
is independently unattested.

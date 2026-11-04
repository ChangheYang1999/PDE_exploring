# Independent C1 pressure rigidity reconstruction

Status: CONFIRMED A3047, comparison A3048, extensions OPEN A3049. Pressure symmetry remains an additional hypothesis.

## 1. Exact theorem and elementary inputs

Fix 0<c<1/2 and any finite real omega. Set J(x1,x2,z)=(-x2,x1,0), A=cI-omega J and B=Ay+U. Let U belong to C1(R3;R3), let P belong to C1(R3), and assume the full equations

    (1-c)U+(B.grad)U+omega JU+grad P=0,   div U=0.

Suppose U is uniformly sublinear, meaning sup_(|y|>=L)|U(y)|/|y| tends to zero as L tends to infinity. Suppose R>0 and delta>0 satisfy

    B(y).y>=delta|y|^2 whenever |y|>=R.

If the actual P is invariant under every rotation about the vertical axis on D=B_R(0), then U=b e_z and P=-(1-c)b z+p0 for constants b,p0. The same conclusion holds if Gamma=(Jy).U vanishes on D. Uniform decay forces b=0. Global pressure symmetry is a special case, because uniform sublinearity gives the radial inequality at large R with delta=c/2.

The elementary inputs are C1 ODE flow and its Jacobian formula, the chain rule, Stokes' theorem with the approximation justification below, harmonic regularity and analyticity, and the harmonic gradient estimate. No earlier pending pressure theorem, pressure normalization, global vorticity integrability, derivative growth hypothesis or trajectory-limit classification is a premise.

## 2. Flow, ball and torque

For every epsilon>0 one has |U(y)|<=C_epsilon+epsilon|y|. Thus B is locally Lipschitz with linear growth. Gronwall controls each trajectory on every finite interval in both time directions; the local continuation theorem gives a complete C1 flow Phi_t. Since div B=3c,

    det D Phi_t(y)=exp(3ct).

The reverse field points strictly into the closed ball on its boundary. The first-exit argument therefore makes both D and its closure invariant for negative time. Every point enters D in finite negative time: if a backward trajectory stayed outside, the radial inequality would give |Phi_(-s)y|<=exp(-delta s)|y| for all s>=0, contradicting its radius being at least R. At the first boundary contact, strict inward motion gives entry into the open ball.

Differentiation of Gamma gives

    B.grad Gamma+(1-2c)Gamma=-(Jy).grad P.

Indeed B.grad Gamma=(JB).U+(Jy).(B.grad U), (JB).U=c Gamma-omega(J^2y).U, and (Jy).JU=-(J^2y).U; the two rotation terms cancel. If P is axisymmetric in D, then along each negative trajectory from D,

    Gamma(Phi_t y)=exp(-(1-2c)t)Gamma(y).

The left side stays bounded on the compact closed ball. Because 1-2c>0, Gamma vanishes. Conversely Gamma=0 on the open ball gives (Jy).grad P=0 there by the torque identity; integration along each axial circle yields pressure invariance.

## 3. C1 circulation gives continuous two-form transport

Define the C1 one-form alpha=U.dy and the C1 scalar G=|U|^2/2-P. The full momentum equation gives the coefficient identity

    (B.grad)U+(DB)^T U=(2c-1)U+grad G.                    (1)

Here (DB)^T U=cU+omega JU+grad(|U|^2/2). Thus (1) uses only continuous first derivatives and does not differentiate curl U.

For a closed piecewise C1 loop gamma, parametrize its transported image by Y(t,s)=Phi_t(gamma(s)). The variational equation is partial_t partial_s Y=DB(Y) partial_s Y. On each compact time interval all terms are continuous and bounded on the parametrized loop. Differentiating under the line integral, applying (1), and integrating grad G around the closed loop proves

    integral_(Phi_t gamma) alpha=exp((2c-1)t) integral_gamma alpha.  (2)

Put beta=d alpha, a continuous two-form. For a smooth oriented disk Sigma, Stokes and (2) give

    integral_Sigma Phi_t^* beta=exp((2c-1)t) integral_Sigma beta.

Stokes is valid on the C1 image disk as follows. Approximate its C1 parametrization on a compact parameter disk in C1 by smooth parametrizations. Apply Stokes to the pullback of the C1 form on each smooth parametrization. The boundary integrals converge by C1 convergence and continuity of alpha; the area integrals converge by C1 convergence and continuity of beta. Injectivity of the approximants is unnecessary for this parametrized identity. This proves the claimed identity without a C2 flow.

Now let Sigma shrink to a point in each coordinate two-plane. Divide its integral by its oriented area and use continuity of both integrands. Every component of the following pointwise identity is obtained:

    Phi_t^* beta=exp((2c-1)t) beta.                       (3)

Because D Phi_t is invertible, beta vanishes at one orbit point if and only if it vanishes at every finite-time point of that orbit.

## 4. Meridional Jacobian and the finite quotient integral

Inside D, Gamma=0 gives u_theta=0 away from the axis. The Cartesian horizontal velocity is parallel to the horizontal position; taking limits along different rays gives U_h(0,z)=0. Thus the axis is invariant while in D, and uniqueness prevents an off-axis trajectory in D from meeting it at finite time.

In cylindrical coordinates, write U=f(r,theta,z)e_r+g(r,theta,z)e_z. For negative trajectories from D,

    r'=cr+f,   z'=cz+g,   theta'=-omega.

Let q=partial_z f-partial_r g, so q=Omega.e_theta, with Omega=curl U continuous. Define xi=q/r off-axis. For fixed initial theta, the map of (r,z) has Jacobian J2. The last coordinate derivative row of the full map (r,z,theta) is (0,0,1). Since Cartesian volume has density r, the full Jacobian identity implies

    J2(t)=exp(3ct) r(0)/r(t)>0.                          (4)

A small meridional disk away from the axis is transported into the meridional half-plane of angle theta-omega t. On such a disk alpha=f dr+g dz and beta=-q dr wedge dz. Applying (3) to its two tangent directions and using (4) gives

    q(Phi_t y) J2(t)=exp((2c-1)t)q(y),
    xi(Phi_t y)=exp(-(1+c)t)xi(y),   t<=0.                (5)

No derivative of q or xi has been taken. For each fixed finite t, the disk can be chosen small enough to stay in the ball and away from the axis over that compact time interval. Negative invariance and off-axis uniqueness then justify (5) at every off-axis starting point and every t<=0.

Let M be the supremum of |Omega| on the closed ball. It is finite by C1 regularity. Then

    I=integral_D |xi| <= 2pi M integral_(-R)^R sqrt(R^2-z^2) dz < infinity.  (6)

This follows from |q|<=M and cancellation of 1/r against the cylindrical volume factor r. Values assigned on the axis do not matter. For any fixed t<0, Phi_t(D) is a subset of D. Change variables in its nonnegative integral, using (5) almost everywhere and det D Phi_t=exp(3ct), to obtain

    I >= integral_(Phi_t D)|xi|=exp((2c-1)t) I.           (7)

The multiplicative factor is strictly greater than one. Since I is finite, I=0. Continuity of q off the axis gives q=0 there. This is an integral contradiction on one ball; no pointwise bound on xi or global integrability has been assumed.

## 5. Cartesian C1 extension of each meridional slice

Put v(z)=U_z(0,z). The radial horizontal field has D_x U_h(0,z)=a(z)I2: a linear map preserving every horizontal line is scalar. Also partial_z U_h(0,z)=0. The original divergence condition gives 2a+v'=0. As r decreases to zero on any ray, q=0 implies

    D_x U_z(0,z).e_r = lim partial_r g = lim partial_z f=0.

Thus D_x U_z(0,z)=0. This axis information has been deduced after the integral argument, using only C1 regularity.

For fixed theta0, copy the corresponding meridional slice into every horizontal direction:

    V_theta0(r,phi,z)=f(r,theta0,z)e_r(phi)+g(r,theta0,z)e_z,
    V_theta0(0,z)=v(z)e_z.

The original C1 Taylor expansion at each axis point gives the first-order expansion of this field with derivative blocks a(z)I2, 0, 0, v'(z). In detail the horizontal error is o(sqrt(r^2+|z-z0|^2)) before and after replacing e_r(theta0) by e_r(phi); the vertical error has the same bound because its original horizontal derivative is zero.

Away from the axis its horizontal derivative block is

    (f/r)I2+(partial_r f-f/r)e_r(phi) tensor e_r(phi).

Both f/r and partial_r f tend to a(z). The other blocks tend to 0, 0 and v'(z). These limits hold locally uniformly in z by continuity of DU. Hence V_theta0 is C1 throughout D, with no singular derivative supported on the axis.

Its divergence vanishes off-axis because partial_r f+f/r+partial_z g=0. Its only possible curl component is q(r,theta0,z)e_phi=0. Continuity extends both identities to the axis. Consequently Delta V_theta0=0 distributionally, and harmonic regularity makes each Cartesian component smooth and harmonic in D.

## 6. Harmonic axis data recover the actual curl

An axisymmetric harmonic scalar h on D that vanishes on the axis must vanish identically. To prove this, expand near an interior axis point in a convergent Taylor series. Rotational invariance makes each horizontal homogeneous polynomial a multiple of r^(2n), with odd horizontal degrees zero. In a smaller neighborhood of absolute convergence one may write

    h(r,z)=sum_(n,m>=0) a_nm r^(2n)(z-z0)^m.

The axis data give a_0m=0. The harmonic equation gives

    4(n+1)^2 a_(n+1,m)+(m+2)(m+1)a_(n,m+2)=0.

Induction on n kills every coefficient. Thus h is zero near the axis point, and analyticity on the connected ball gives h=0 everywhere.

Apply this to the difference of the vertical components of V_theta0 and V_theta1. They share the same axis function v, so their vertical components agree on D. Therefore g is independent of theta. Integrate the original divergence equation radially at fixed z:

    r f(r,theta,z)=-integral_0^r s partial_z g(s,z) ds.

The lower boundary term is zero since f=O(r) at the axis. The right side is independent of theta, so f is also independent of theta. Now the actual U, not merely the auxiliary fields, is axisymmetric in D and has zero swirl and q=0. It follows that its full curl is zero there.

## 7. Global propagation and exact scope

For every point y choose a finite negative time with Phi_t y in D. Since beta vanishes at that orbit point, invertibility in (3) gives beta(y)=0. Thus div U=curl U=0 globally. Each component of U is entire harmonic. At any y0 the interior estimate gives

    |DU(y0)|<=C L^-1 sup_(B_L(y0))|U|.

Insert |U(y)|<=C_epsilon+epsilon|y|, send L to infinity and then epsilon to zero. This proves DU=0. The zero horizontal axis value in D leaves U=b e_z. Momentum gives grad P=-(1-c)b e_z. Uniform decay excludes b nonzero.

Every finite omega is included: it enters the carrier and angular motion but cancels from torque and the volume exponent. The proof requires 0<c for the sublinear large-ball trapping and c<1/2 for both torque damping and the strict inequality in (7). At c=1/2 the integral factor is one, so no endpoint claim follows. Pressure symmetry on an arbitrary small ball or only in the exterior is not proved sufficient, and pressure symmetry is not deduced from decay.

## 8. Source comparison and countertest

All eight sections of LIT364 at hash54e4b9cf, its verification and formal-source files, and all thirty manual author checks were read. The complete source is captured under verification. Its argument is independently reconstructed above; no computation or formal build is needed.

The LIT363 C1,alpha example has q/r proportional to r^(alpha-1), 0<alpha<1. This quotient is unbounded but integrable on each finite ball. It does not contradict (7): its axis carrier has B(0,0,z).(0,0,z)=(c-2a)z^2<0, so no ball satisfies the required radial inequality, and its velocity is not uniformly sublinear. Nonzero axial constants likewise remain permitted under sublinearity and are excluded only by decay.

Existing configured model comparison is requested, especially for the C1 Stokes passage, meridional Jacobian, strict integral exponent, extension across the axis and distinction between auxiliary and actual curl. Actual provider execution is independently unattested. No claim of novelty or of optimal weak regularity is made. The unrestricted rotating conjecture remains open.

## 9. Complete existing-agent comparison and disposition

The full C comparison dated 2026-11-04T07:11:50Z, items0-17 and its diagnostic description, was read. Items1-13 agree with the proof above. In particular, Stokes is passed through smooth parametrizations before shrinking disks; the transported two-form is continuous, not differentiated. The meridional volume factor contains r(0)/r(t). Its combination with circulation gives exponent -(1+c), and the finite L1 integral over the negatively invariant ball has factor exp((2c-1)t)>1 for every t<0. The axis is null for this integration. No bounded quotient is required.

The actual curl is killed only after harmonic axis-data uniqueness removes theta dependence. Neither the C2 axis ODE nor its exceptional stationary-point analysis enters this C1 proof. The growing C1,alpha countertest has an integrable quotient and satisfies its transport law, but fails the ball condition. These observations resolve the regularity issue without changing the extra pressure-symmetry hypothesis.

The described thirty-nine diagnostic checks and their retained failed run were not read or rerun by this agent; no verdict certifies them. The optional Legendre proof from an earlier comparison is also outside this reconstruction. The exact theorem in Section1 is ready for a designated verdict. No c=1/2 endpoint, arbitrary-small-ball result, automatic pressure symmetry or unrestricted rotating conclusion is asserted. Existing collaboration is with the configured model C agent, with actual provider execution independently unattested.

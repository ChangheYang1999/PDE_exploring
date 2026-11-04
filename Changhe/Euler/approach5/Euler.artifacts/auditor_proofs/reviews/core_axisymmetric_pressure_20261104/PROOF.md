# Independent review: pressure symmetry on an absorbing ball

Status: CONFIRMED A3033 at the exact scope below; existing C comparison qualified in A3034, stronger scope OPEN A3035. This is a conditional rigidity statement, with an additional pressure hypothesis. It does not settle the unrestricted rotating problem.

## 1. Exact statement and dependencies

Fix 0<c<1/2 and any finite real omega. Write J(x1,x2,z)=(-x2,x1,0). Let U in C2(R3;R3), P in C1(R3), with

    B=(cI-omega J)y+U,
    (1-c)U+(B.grad)U+omega JU+grad P=0,   div U=0.

Assume uniform sublinearity: sup_(|y|>=L) |U(y)|/|y| tends to zero as L tends to infinity. Suppose some R>0 and delta>0 satisfy

    B(y).y >= delta |y|^2 for |y|>=R,
    P is invariant under every axial rotation on the open ball B_R.

Then there are real constants b,p0 such that U=b e_z and P=-(1-c)b z+p0. In particular, decay of U at infinity forces U=0. One can replace pressure symmetry on B_R by Gamma=(Jy).U=0 on B_R.

Uniform sublinearity already provides the radial inequality for all sufficiently large R, with delta=c/2. The extra premise is symmetry on a ball this large, not on an arbitrary small ball. No velocity symmetry, pressure condition outside the ball, derivative bound at infinity or energy hypothesis is imposed.

The proof uses elementary complete-flow theory for a C1 vector field with linear growth, uniqueness for continuous linear systems, distributional div-curl identities, harmonic regularity and the harmonic interior gradient estimate. The local harmonic uniqueness fact is proved below. The separately submitted global pressure-symmetry theorem is not an input.

## 2. Complete flow and the local torque identity

For every epsilon>0, sublinearity gives |U(y)|<=C_epsilon+epsilon|y|. Thus B has linear growth and is locally Lipschitz. Gronwall bounds a trajectory on every finite time interval in either direction; local continuation gives a complete flow Phi_t.

On the sphere of radius R the vector field -B points strictly into the ball. The first-crossing argument implies backward invariance of the open ball and its closure. Every point outside the ball enters its interior in finite backward time. Indeed, while rho(t)=|Phi_t y|>=R,

    d log rho(t)/dt >= delta.

If that inequality held for all t<=0, integration from t to zero would give rho(t)<=rho(0) exp(delta t), contradicting rho(t)>=R. At a first contact with the sphere, strict inward motion for -B gives immediate entrance. In particular, all backward trajectories starting inside the ball stay in the compact closed ball.

The equation makes grad P a C1 function, so P is actually C2. Product differentiation gives

    B.grad Gamma=(JB).U+(Jy).(B.grad U),
    (JB).U=c Gamma-omega(J^2y).U,
    (Jy).JU=-(J^2y).U.

Taking the dot product of momentum with Jy therefore yields

    B.grad Gamma+(1-2c)Gamma=-partial_theta P.

Both rotation terms have cancelled. For a point in B_R, pressure symmetry makes Gamma(Phi_t y)=exp(-(1-2c)t)Gamma(y) for every t<=0. Gamma is bounded on the closed ball and 1-2c>0, so Gamma(y)=0. Conversely Gamma identically zero on the ball makes partial_theta P zero there. Each axial rotation stays in the ball, so this is equivalent to pressure invariance.

## 3. The axis derivative cannot be omitted

Write y=(x,z), x in R2. Gamma=0 says that U_h(x,z) is parallel to x for x nonzero. Continuity along different rays gives U_h(0,z)=0 for |z|<R. Its horizontal derivative maps each ray to itself, hence

    D_x U_h(0,z)=a(z)I2,   partial_z U_h(0,z)=0.

A linear map with every vector as an eigenvector is scalar, as follows by testing e1,e2,e1+e2. Put

    v(z)=U_z(0,z),  g(z)=D_x U_z(0,z),  beta(z)=cz+v(z).

The divergence condition gives 2a+v'=0, thus beta'=c-2a. Curling momentum gives, with Omega=curl U,

    Omega+B.grad Omega-(Omega.grad)U+omega JOmega=0.

On the axis Omega_z=0 and w=Omega_h=(g2,-g1). Since g.w=0, the vertical stretching component vanishes, while the horizontal component is a w. The axis equation is consequently

    beta w'+(1-a)w+omega J2 w=0.                 (1)

This is the actual vector equation on the axis. It is not inferred by dividing a cylindrical component by radius.

The axis is invariant while its trajectory lies in the ball. Backward invariance keeps each such trajectory in the segment [-R,R]. A nonstationary trajectory solves z'=beta(z) within a component of {beta!=0}, so it is monotone. Its backward limit z* exists, and beta(z*)=0, since otherwise its speed stays bounded below near the limit. The limit is interior: continuity and the radial inequality give beta(R)>=delta R and beta(-R)<=-delta R.

On the side from which z* is approached, beta(z)/(z-z*) is positive. Differentiability at the root therefore gives beta'(z*)>=0 and a(z*)<=c/2<1. Along the trajectory, skewness of J2 in (1) yields

    d|w|^2/dt=-2(1-a)|w|^2.

For sufficiently negative t, 1-a is bounded below by a positive number. A nonzero solution at any finite time would then grow exponentially backward, contradicting the bounded continuous w on the compact axis segment. Hence w=0 at each nonstationary point.

At a root of beta, equation (1) is a matrix equation with determinant (1-a)^2+omega^2. It gives w=0 except possibly when omega=0 and a=1. In that case beta'=c-2 is nonzero, making the root isolated. Nearby nonstationary points have w=0, so continuity resolves this exception too. Nonisolated roots cannot be exceptional. We have proved

    D_x U_z(0,z)=0 for |z|<R.

All the stated zero derivatives extend to the two endpoints by continuity. Only one-dimensional axis trajectories were shown to converge to points; no such claim has been made for general B-trajectories.

## 4. Damping of the divided meridional vorticity

For r=|x|>0 write U=f(r,theta,z)e_r+g0(r,theta,z)e_z. These components can still depend on theta. Set

    D=(cr+f)partial_r+(cz+g0)partial_z-omega partial_theta,
    q=partial_z f-partial_r g0,  xi=q/r.

The moving-frame rotation cancels omega JU, so momentum and divergence give

    Df+(1-c)f+P_r=0,   Dg0+(1-c)g0+P_z=0,
    f_r+f/r+g0_z=0.

Differentiate the first momentum equation in z and the second in r, then subtract. The two mixed pressure derivatives cancel, and the commutators give

    Dq+(1+f_r+g0_z)q=0,
    Dq+(1-f/r)q=0.

Since Dr=cr+f, division by r gives exactly

    Dxi=-(1+c)xi.                              (2)

There is no angular symmetry assumption in this calculation: the coefficient of partial_theta is the constant -omega.

The C2 bound on the closed ball and the axis identities from Section 3 give

    |f_z|+|g0_r|<=C r.

For the first term use f_z=e_r.partial_z U_h and its zero axis value; for the second use g0_r=e_r.D_x U_z and its zero axis value. Apply the mean value estimate along the horizontal segment from the axis to (x,z), which stays in the ball. Therefore xi is uniformly bounded on the punctured ball. A continuous extension of xi across the axis is not needed.

An off-axis trajectory cannot meet the invariant axis in finite time by uniqueness. Equivalently r'=(c+f/r)r, and f/r is bounded on the closed ball since U_h vanishes on the axis. For every off-axis point of B_R the entire backward trajectory thus remains off-axis inside B_R. Equation (2) gives xi(Phi_t y)=exp(-(1+c)t)xi(y). Its boundedness and 1+c>0 force xi=0. Hence q=0 throughout the punctured ball.

## 5. Harmonic uniqueness from axis values

Let h be an axisymmetric harmonic scalar on B_R, with h(0,0,z)=0 for all |z|<R. Harmonic regularity makes h analytic. In a small neighborhood of any axis point (0,0,z0), rotational invariance of its convergent Taylor series gives

    h(r,z)=sum_(n,m>=0) a_nm r^(2n)(z-z0)^m.

Indeed, each horizontal homogeneous coefficient polynomial must be invariant under every planar rotation. Odd degrees vanish and degree 2n is a multiple of (x1^2+x2^2)^n. Regrouping is legitimate inside a smaller neighborhood of absolute convergence.

Zero axis values give a_0m=0 for every m. Applying the Laplacian to the convergent series gives

    4(n+1)^2 a_(n+1,m)+(m+2)(m+1)a_(n,m+2)=0.

Induction on n kills every coefficient. Thus h vanishes in a neighborhood of an axis point and, by analytic continuation on the connected ball, on the whole ball. This statement requires axisymmetry; a general harmonic scalar can vanish on the axis without being zero.

## 6. The auxiliary slices have enough regularity

For each fixed theta0 define on B_R

    V_theta0(r,phi,z)=f(r,theta0,z)e_r(phi)+g0(r,theta0,z)e_z,
    V_theta0(0,0,z)=v(z)e_z.

This copies one meridional slice into an axisymmetric field; it does not assume that U itself is axisymmetric. The axis identities and continuity imply, uniformly on compact axis intervals,

    f/r -> a,  f_r -> a,  f_z -> 0,
    g0_r -> 0,  g0 -> v,  g0_z -> v'.

In particular, the horizontal derivative matrix is

    D_x(V_theta0)_h=(f/r)I2+(f_r-f/r)e_r tensor e_r,

which tends to a I2. All other first derivatives have the limits just displayed. Taylor expansion of the original C2 field also gives f=a(z)r+O(r^2) and g0=v(z)+O(r^2) locally uniformly in z; these yield differentiability at the axis with those limits. Hence V_theta0 is C1 throughout the ball. No C2 even-extension condition is being assumed.

Away from the axis, divergence of V_theta0 is f_r+f/r+g0_z=0 and its only possible curl component is q=0. Continuity of first derivatives extends these identities to the axis. Distributionally Delta V_theta0=grad div V_theta0-curl curl V_theta0=0, so every component is smooth and harmonic.

For theta0 and theta1, the difference of their vertical components is an axisymmetric harmonic scalar whose axis values are v-v=0. Section 5 makes it identically zero. Therefore g0(r,theta,z) is independent of theta. Divergence integrated at fixed z gives

    r f(r,theta,z)=-integral_0^r s partial_z g0(s,z) ds.

The boundary term at zero vanishes because f=O(r). This proves that f is also independent of theta. The original U is now axisymmetric on the ball, has no swirl, and has q=0. Its full actual curl therefore vanishes on B_R.

## 7. Global propagation and final constant

For any y, choose a finite negative time t0 with Phi_t0 y in B_R. The actual vorticity along [t0,0] solves

    d Omega(Phi_t y)/dt=[DU(Phi_t y)-I-omega J]Omega(Phi_t y).

The coefficients are continuous on this compact time interval. Zero initial data at t0 therefore give Omega(y)=0. Thus div U=curl U=0 on all of R3 and each component is entire harmonic.

At a fixed y0 the harmonic gradient estimate gives

    |DU(y0)|<=C L^-1 sup_(B_L(y0))|U|.

Uniform sublinearity makes the right side tend to zero: split the ball into a fixed compact part and its complement where |U(y)|<=epsilon|y|, let L tend to infinity, then epsilon tend to zero. Hence U is constant. Gamma=0 on the ball makes its horizontal components zero, so U=b e_z. Substitution in momentum gives grad P=-(1-c)b e_z, yielding the claimed pressure.

## 8. Scope and source record

The source reviewed is the eight-section LIT360 proof, captured with its exact hash in the team records. Its 34 author checks are retained as author checks. The reconstruction above uses no part of LIT359 as an unproved lemma and no mathematical computation.

Pressure symmetry on the absorbing ball remains additional. Neither decay alone, symmetry only at infinity, nor symmetry on an arbitrary smaller ball has been shown sufficient by this argument. Constants explain why the sublinear statement concludes axial constancy while the decaying statement concludes zero. The full rotating conjecture remains open.

## 9. Existing C comparison and exact scope

The full existing configured model C comparison dated 06:56:50Z has been read, including items 0-8 and its diagnostic paragraph. It agrees with all eight sections above. Its direct Taylor-coefficient verification supplies precisely the local harmonic uniqueness used here. The optional Legendre expansion is an alternative argument and is not used or newly certified. The distinction between auxiliary and actual curl is correct: the example u_r=z cos(theta), u_z=r cos(theta) has q=0 but a nonzero angular-derivative contribution to actual curl; it is only an off-axis control, not a globally C1 field or an Euler counterexample.

Its quantitative consequence is correct. For a decaying profile with M=sup|U|, every R>M/c obeys B.y>=(c-M/R)|y|^2 for |y|>=R. Hence a nonzero such profile must have Gamma not identically zero on every such ball. This requires both the decay hypothesis and the theorem proved above. It is not a derivation of pressure symmetry for a general profile.

Item 0 explicitly accepts the A3030 correction to the previous LIT359 comparison: a nonzero axial constant is allowed under uniform sublinearity; the nonzero angular-pressure-mode conclusion is restricted to decaying profiles. The C1 extension, strict boundary crossing and finite-time propagation checks agree. All interior gradient constants may be replaced by a universal C, so no choice of matrix norm affects the limit argument.

The named 21-check diagnostic script, its final log and its retained first-run log have not been read or rerun in this review. Their counts, classifications, hashes and success claims are not certified here. No computation is needed for the analytical proof. Existing configured model file collaboration has occurred; actual provider execution is independently unattested.

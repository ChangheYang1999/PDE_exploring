# A Hilbert-Schmidt formula for the signed energy remainder

## 1. Exact statement and conventions

Use the Fourier transform fhat(xi)=integral f(X) exp(-i X.xi) dX on R2 and its unitary form fhat/(2pi). Put R_j=partial_j(-Delta)^(-1/2), with symbol i u_j(xi), where u(xi)=xi/|xi| away from zero. All operator norms in this note are on scalar L2(R2), unless S1 is explicitly indicated. Hilbert-Schmidt norm is denoted HS. Values of u at zero do not affect any integral.

Let a,b be real C_0(R2) functions with weak first derivatives in L2. Define

    Q=-a R1 R2+b R1^2,
    P=R1 b R1-(R1 a R2+R2 a R1)/2,
    K=Sym Q-P.

Then K is self-adjoint and Hilbert-Schmidt, with

    K = (1/2)[R1,[R1,b]]-(1/2)[R1,[R2,a]],                 (1)
    ||K||_HS <= kappa (||grad a||_2^2+||grad b||_2^2)^(1/2),
    kappa = sqrt((4 log 2-1)/(8 pi)).                       (2)

For a=rho_x, b=rho_y, the last factor is exactly ||D^2 rho||_2 with all ordered derivatives. No L2 assumption on a or b is required in (2). In particular, the statement allows gradients of a sublinear far-field density, provided they vanish at infinity and have square-integrable first derivatives.

Sections 4 and 5 give an explicit finite-rank approximation for compact smooth coefficients, including frequency and partition errors. Combined with a spatial coefficient cutoff, it applies to the preceding C_0 coefficients. This is an alternative way to certify the compact remainder in ../signed_coupling/PROOF.md. It supplies no profile-specific positive inverse gap and no nonlinear theorem.

## 2. Double commutator and Fourier kernel

Expanding the double commutators and using R1 R2=R2 R1 gives (1): the b contribution is

    (b R1^2+R1^2 b)/2-R1 b R1,

and the a contribution is

    -(a R1 R2+R1 R2 a)/2+(R1 a R2+R2 a R1)/2.

These are exactly Sym Q-P. Each double commutator here is self-adjoint, because a first commutator of a skew-adjoint Riesz transform with real multiplication is self-adjoint, and commutation of a skew-adjoint operator with a self-adjoint operator is self-adjoint.

For compact smooth coefficients, the kernel in the unitary Fourier representation is

    k(xi,eta) = [-(du_1)^2 bhat(q)+du_1 du_2 ahat(q)]/(2(2pi)^2),
    q=xi-eta,  du=u(xi)-u(eta).                            (3)

Consequently

    |k(xi,eta)|^2 <= |du|^4 (|ahat(q)|^2+|bhat(q)|^2)/(4(2pi)^4). (4)

Indeed the coefficient vector (du_1 du_2,-du_1^2) has Euclidean norm |du_1| |du|<=|du|^2. This second multiplier difference is essential. The corresponding single-commutator bound would have |du|^2, whose integral over eta diverges logarithmically in dimension two.

## 3. An exact two-dimensional integral

For every q in R2,

    integral_R2 |u(eta+q)-u(eta)|^4 deta
        = I0 |q|^2,   I0=2pi(4 log 2-1).                  (5)

Rotation and scaling reduce the nonzero case to q=(1,0). Use elliptic coordinates with foci at0 and(-1,0):

    eta=((cosh(mu) cos(nu)-1)/2, sinh(mu) sin(nu)/2),
    mu>=0, 0<=nu<2pi.

These coordinates cover the plane once outside a set of measure zero. If r=|eta| and t=|eta+q|, then r+t=cosh(mu), |r-t|=|cos(nu)| and

    rt=(sinh(mu)^2+sin(nu)^2)/4,
    |u(eta+q)-u(eta)|^2=4 sin(nu)^2/(sinh(mu)^2+sin(nu)^2).

The Jacobian is (sinh(mu)^2+sin(nu)^2)/4. Thus the integral in (5) becomes

    4 integral_0^(2pi) integral_0^infinity
       sin(nu)^4/(sinh(mu)^2+sin(nu)^2) dmu dnu.

On 0<nu<pi/2, substitution z=tanh(mu) gives the inner integral

    (pi/2-nu)/(sin(nu) cos(nu)).

The four equal angular quadrants therefore give

    I0=16 integral_0^(pi/2) (pi/2-nu) sin(nu)^3/cos(nu) dnu
      =16 integral_0^(pi/2) theta (cot(theta)-sin(theta)cos(theta)) dtheta.

Integration by parts gives integral theta cot(theta)=(pi/2)log2 and integral theta sin(theta)cos(theta)=pi/8. The first identity follows from integral_0^(pi/2) log(sin(theta))=-(pi/2)log2, obtained by adding the sine and cosine integrals and substituting2theta. Boundary terms vanish. This proves (5), including the removable angular endpoints by monotone integration of the nonnegative integrand.

Integrate (4), use (5), then use Plancherel:

    ||K||_HS^2
      <= I0/(4(2pi)^4) integral |q|^2(|ahat|^2+|bhat|^2) dq
       = I0/(16pi^2) (||grad a||_2^2+||grad b||_2^2).

This is (2).

For general coefficients in the statement, let a_R=chi(X/R)a and b_R=chi(X/R)b, with a fixed smooth compact radial cutoff chi equal to1 on B1 and0 outside B2. The first-derivative errors tend to zero in L2. The derivative tails do so by integrability; the cutoff derivative error is bounded by a fixed constant times the supremum of |a| or |b| outside B_R, which tends to zero. Smooth approximation gives compact smooth coefficients with the same convergence and uniform convergence. Bound (2) makes their K operators Cauchy in HS. Uniform coefficient convergence identifies the operator limit with (1), since each double commutator has operator norm at most4 times the coefficient supremum. This proves (2) and the claimed identification without assuming an ordinary L2 Fourier transform of a or b.

## 4. Frequency truncation with explicit error

For this section assume a,b are compact smooth. Put

    A0=(||a||_2^2+||b||_2^2)^(1/2),
    A2=(||D^2 a||_2^2+||D^2 b||_2^2)^(1/2).

Let Pi be the Fourier projection to Omega={epsilon<=|xi|<=Lambda}, where0<epsilon<Lambda. Then

    ||K-Pi K Pi||_HS
       <= sqrt(2/pi) (epsilon^2 A0^2+Lambda^(-2) A2^2)^(1/2). (6)

For the low-frequency region |eta|<epsilon, use |du|<=2 to obtain integral |du|^4 deta<=16pi epsilon^2, for each q. The same bound applies to the region |xi|<epsilon by interchanging variables. Bound (4), Plancherel, and their union give a squared HS bound 2 epsilon^2 A0^2/pi.

For |eta|>Lambda and |q|<=Lambda/2, the segment eta+tq stays outside |eta|/2, and ||Du(z)||<=1/|z|. Hence |du|<=2|q|/|eta| and

    integral_(|eta|>Lambda) |du|^4 deta<=16pi |q|^4/Lambda^2.

For |q|>Lambda/2, use the full integral I0|q|^2<=4I0|q|^4/Lambda^2. Since I0<4pi (log2<3/4 suffices), this is bounded by the same16pi expression. The exchanged region |xi|>Lambda gives the same bound. Bound (4) and Plancherel now give a squared HS bound 2 A2^2/(pi Lambda^2). Adding the low and high union estimates proves (6). Overlaps only make this upper bound larger.

## 5. Finite matrix on the remaining annulus

Partition a square containing Omega into squares of side h. Let Omega_i be the nonempty intersections with Omega, and choose xi_i in each Omega_i. Discard cells of zero measure. In L2(Omega), define the orthonormal indicators e_i=1_(Omega_i)/sqrt(|Omega_i|). Let F be the finite-rank operator with kernel constant and equal to k(xi_i,xi_j) on Omega_i times Omega_j. Its matrix is

    F_ij=sqrt(|Omega_i| |Omega_j|) k(xi_i,xi_j).             (7)

This matrix is Hermitian when exact values are used, because K is self-adjoint. Define

    A=(||a||_1^2+||b||_1^2)^(1/2),
    X_A=(|||X| a||_1^2+|||X| b||_1^2)^(1/2).

Then

    ||Pi K Pi-F||_HS
       <= (sqrt(2)/pi) Lambda^2 h (2A/epsilon+X_A).        (8)

To prove the bound, use |u(x)-u(y)|<=2|x-y|/epsilon for x,y in Omega. On the ball |v|<=2, the vector polynomial v -> (v_1 v_2,-v_1^2) is Lipschitz with constant4. Also the vector Fourier coefficient is bounded by A and is Lipschitz with constant X_A. Formula (3) is therefore Lipschitz in either variable on Omega, with constant

    L=(2A/epsilon+X_A)/(2pi^2).

Moving each variable to its cell representative costs at most sqrt(2)h. The kernel error is at most2sqrt(2)h L. Multiplying by |Omega|<=pi Lambda^2 bounds its HS norm and proves (8). No path through the excluded low-frequency disk is needed for the global unit-vector bound.

A uniform certified kernel evaluation error delta_k in (7) adds at most pi Lambda^2 delta_k to the HS error. The cell areas and representative coordinates must also be exact or enclosed; their errors cannot be omitted. Symmetrizing an approximate matrix cannot increase its operator error relative to K. Compressing by the orthogonal S1 parity projection cannot increase the operator error on that subspace. The action on the orthogonal complement of the finite range is zero, so a bound for the largest eigenvalue of the resulting operator must include0.

## 6. Complete approximation recipe and scope

For a,b as in Section1, choose compact smooth a_R,b_R, and certify

    E1=(||grad(a-a_R)||_2^2+||grad(b-b_R)||_2^2)^(1/2).

Apply Sections4-5 to a_R,b_R. Combining (2), (6), (8) and the arithmetic error gives

    ||K-F|| <= kappa E1
       +sqrt(2/pi)(epsilon^2 A0^2+Lambda^(-2) A2^2)^(1/2)
       +(sqrt(2)/pi) Lambda^2 h(2A/epsilon+X_A)
       +pi Lambda^2 delta_k.                              (9)

Every norm on the right is an ordinary explicitly stated integral of the compact coefficient approximation or its cutoff error. Fourier values in the finite matrix require their own validated integration. There is no claim that the conservative bound (9) yields a small matrix for the case4 profile.

This theorem strengthens the qualitative compactness statement with a Hilbert-Schmidt norm and a different finite-rank error calculation. Together with a full-plane bound on theta and a certified matrix eigenvalue it can be inserted into the conditional L2 inverse criterion of ../signed_coupling/PROOF.md. It leaves the high-space inverse, strain trace, nonlinear estimates, and all candidate-specific numerical values unproved.

## Dependencies

The proof uses Plancherel, elementary Fourier multipliers, Hilbert-Schmidt kernel calculus, elementary elliptic coordinates and finite-dimensional spectral bounds. Each quantitative estimate is derived above. The ordinary single-commutator literature is recorded separately in source/LITERATURE.md only to distinguish the operators; no Schatten theorem from that literature is used as an input.

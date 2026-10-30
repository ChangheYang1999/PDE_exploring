# A signed principal part and a finite-rank remainder for the L2 coupling

## Statement, conventions and scope

Let R_j = partial_j (-Delta)^(-1/2), with Fourier symbol i xi_j / |xi| for the transform integral f(X) exp(-i X.xi) dX. Thus R_j is skew-adjoint on real L2, the R_j commute, and sum_j ||R_j h||_2^2 = ||h||_2^2. The density background rho is real and smooth, even in x and odd in y. Write a = rho_x and b = rho_y and assume a,b belong to C_0(R2), are bounded, and have bounded first derivatives. Here C_0 means uniformly vanishing at spatial infinity. Let

    Q = -a R_1 R_2 + b R_1^2.

This is exactly U[h].grad(rho), for U = (-R_1 R_2, R_1^2). The full operator Q is generally not compact. Its symmetric part nevertheless admits the following decomposition:

    Sym Q = P + K,
    P = R_1 b R_1 - (R_1 a R_2 + R_2 a R_1)/2,
    C = [R_1,b] R_1 - ([R_1,a] R_2 + [R_2,a] R_1)/2,
    K = -(C + C*)/2.                                      (1)

The operator K is compact and self-adjoint on L2, and

    <P h,h> = integral ( -b |R_1 h|^2 + a (R_1 h)(R_2 h) ). (2)

Define

    theta = ess sup_X (sqrt(a(X)^2+b(X)^2) - b(X))/2.

Then <P h,h> <= theta ||h||_2^2. Compactness of K is proved quantitatively below, with no appeal to a compactness theorem for singular integrals.

Consequently, suppose V = c X + U[rho] is smooth, globally Lipschitz, has at most linear growth and divergence 2c. Let K_F be a finite-rank self-adjoint approximation to K on the S1 subspace, with certified error ||K-K_F|| <= epsilon. If lambda_F bounds the largest eigenvalue of K_F as an operator on the entire S1 L2 space, and

    nu = c + 1 - theta - lambda_F - epsilon > 0,            (3)

then the maximal L2 realization of L = V.grad - 1 + Q has a semigroup of norm at most exp(-nu t) and is bijective from its generator domain onto S1 L2, with inverse norm at most 1/nu.

This is a conditional L2 inverse test, not a nonlinear existence theorem. It supplies neither a strain trace on L2 nor high-regularity control. It cannot by itself replace the high-space part of the baseline theorem. No values of theta, K_F or epsilon are certified for a numerical IPM profile here.

## 1. Exact decomposition and the sign retained

Expand the multiplications in P using R_j d = d R_j + [R_j,d]. Since R_1 R_2 = R_2 R_1, this gives P = Q+C. The adjoint identities R_j* = -R_j and real multiplication d*=d show P*=P. Taking symmetric parts proves (1).

For real h, moving each first R_j to the other side of the inner product gives (2). The pointwise matrix of this quadratic form on v=(R_1 h,R_2 h) is

    [ -b    a/2 ]
    [ a/2    0  ].

Its largest eigenvalue is (sqrt(a^2+b^2)-b)/2. Integrating and using ||v||_2=||h||_2 proves the theta bound. In particular, at the origin of a positive-slope S1 profile, a=0 and b=a_0>0, so this principal form is negative semidefinite. Replacing Q by its unsigned operator norm would discard precisely this information.

The remainder can alternatively be expressed using double commutators, but (1) is sufficient for both compactness and explicit error bounds. No estimate here treats Q itself as compact.

## 2. Quantitative finite-rank approximation of a commutator

We first take a real coefficient d in C_c^1(R2), supported in the disk B_R, and put

    M = ||d||_infinity,    L_d = ||grad d||_infinity.

Let T >= 2R, delta>0, and divide the square Omega=[-T,T]^2 into congruent squares of side h=2T/n, n a positive integer. There exists an explicit operator F of rank at most n^2 such that

    ||[R_j,d] - F||_(L2->L2)
       <= 2 L_d delta + 4 M R/T + 7 L_d T^2 h/delta^2.     (4)

Construction: choose a smooth radial function chi_delta equal to zero on r<=delta, equal to one on r>=2delta, taking values in [0,1], with derivative bounded by 2/delta. Set

    k_j(z) = -z_j/(2 pi |z|^3),
    H(x,y) = chi_delta(|x-y|) k_j(x-y) (d(y)-d(x)).

On each product of two partition cells, replace H(x,y) by its value at the two cell centers. Extend this piecewise constant kernel by zero when x or y is outside Omega. The integral operator with the resulting kernel is F. Its range consists of functions constant on each of the n^2 output cells, so its rank is at most n^2.

The Riesz kernel formula follows by differentiating the two-dimensional kernel 1/(2 pi |z|) of (-Delta)^(-1/2). The latter also follows directly by integrating the Gaussian heat kernel against t^(-1/2)/sqrt(pi). In the commutator the subtraction d(y)-d(x) cancels one power of the singularity, making the kernel locally integrable. The estimates below justify its extension from smooth compact inputs to L2.

### Near the diagonal

The discarded kernel has absolute value at most

    L_d /(2 pi |x-y|),   |x-y|<2delta.

Its integral in either variable is at most 2 L_d delta. The two-sided Schur estimate therefore bounds its L2 operator norm by 2 L_d delta.

### Outside the square

If x is outside Omega, then |x|>T and d(x)=0. The only nonzero inputs satisfy y in B_R. Since T>=2R,

    |x-y| >= |x|/2,
    |H(x,y)| <= 2M/(pi |x|^2).

Its squared Hilbert-Schmidt norm on this region is at most

    (4 M^2/pi^2) (pi R^2) integral_(|x|>T) |x|^(-4) dx
      = 4 M^2 R^2/T^2.

Thus deleting this output region costs at most 2MR/T. Deleting the input region outside Omega costs the same by transposition. The sum is at most 4MR/T. Their intersection has zero kernel; no additional region is omitted.

### Partition error on the square

For |z|>=delta one has |k_j(z)|<=1/(2pi |z|^2) and |grad k_j(z)|<=4/(2pi |z|^3). Since |d(y)-d(x)|<=L_d |x-y|, differentiation of H in either variable, including the cutoff derivative, gives

    |grad_x H|, |grad_y H| <= 7 L_d/(2pi delta^2).

This bound extends across |x-y|=delta because the cutoff is smooth and constant on the inner disk. Moving x and y to their cell centers changes H by at most 7 sqrt(2) L_d h/(2pi delta^2). The square has area 4T^2, so the Hilbert-Schmidt error is at most

    (14 sqrt(2)/pi) L_d T^2 h/delta^2
      < 7 L_d T^2 h/delta^2.

This proves (4). Taking delta small, T large, and then h small shows compactness with a finite, explicit error bound at every stage. This parameter order matters: the estimate does not assert that a modest matrix size suffices.

### Uniformly decaying coefficients

For d in C_0 with bounded first derivative, choose a smooth cutoff d_R that agrees with d on B_R and is supported in B_(2R). The trivial multiplier bound ||R_j||<=1 gives

    ||[R_j,d]-[R_j,d_R]|| <= 2 ||d-d_R||_infinity.          (5)

The right side tends to zero. Applying (4) to d_R therefore proves compactness and gives a certified approximation whenever the coefficient bounds, tail amplitude and sampled kernel values are certified. A bound on a finite box alone does not certify the tail term in (5).

## 3. Propagating commutator errors to the energy remainder

Suppose finite-rank approximations F_(1,b), F_(1,a), F_(2,a) to the indicated commutators have respective operator errors epsilon_(1,b), epsilon_(1,a), epsilon_(2,a). Set

    C_F = F_(1,b) R_1 - (F_(1,a) R_2 + F_(2,a) R_1)/2,
    K_F_raw = -(C_F+C_F*)/2.

These are finite-rank operators. Since each R_j has norm at most one,

    ||K-K_F_raw|| <= epsilon_(1,b)
                    + (epsilon_(1,a)+epsilon_(2,a))/2.    (6)

Let Pi be the orthogonal S1 parity projection. Replacing K_F_raw by Pi K_F_raw Pi preserves self-adjointness and does not increase the error on S1. It is legitimate to represent the resulting finite-rank operator in an orthonormal basis of its range and bound its eigenvalues with interval arithmetic. Its action on the orthogonal complement of its range is zero. Therefore lambda_F in (3) must be at least zero as well as at least the largest eigenvalue of that matrix. Using a negative matrix maximum as a negative bound on the whole infinite-dimensional space would be incorrect.

Any numerical error in constructing this matrix or orthonormalizing its range must be included in epsilon or in a validated eigenvalue enclosure. Formula (4) is not a substitute for that finite arithmetic certification.

## 4. L2 semigroup and inverse, including the domain

For smooth compact S1 h, integration by parts gives

    Re <(V.grad - 1)h,h> = -(c+1)||h||_2^2.

Combining this identity with (1)-(3) yields

    Re <Lh,h> <= -nu ||h||_2^2.                           (7)

The complete globally Lipschitz flow of V defines the strongly continuous transport group for V.grad-1 on L2. Its maximal distributional generator has the smooth compact core: spatial mollification and expanding cutoffs give graph approximation because DV is bounded and V grows at most linearly. The coefficient multiplications and Riesz transforms make Q bounded on L2, so bounded perturbation gives the same maximal domain for L. Smooth parity projection commutes with these constructions. Thus (7) extends in graph norm to the generator domain. Differentiating semigroup orbits there, integrating (7), and using density gives ||exp(tL)||<=exp(-nu t).

For each f in S1 L2, the Bochner integral

    h = -integral_0^infinity exp(tL) f dt

converges, belongs to the generator domain, and solves Lh=f, with ||h||_2<=||f||_2/nu. If Lh=0, its orbit is constant and also decays, so h=0. This establishes surjectivity and injectivity, not merely a formal energy inequality.

## Dependencies and open numerical tasks

All compactness and error estimates above are proved within this note. The only general functional-analytic ingredients are the Schur estimate, Hilbert-Schmidt bound, complete Lipschitz transport flow, bounded perturbation theorem and semigroup integration; their required hypotheses are stated where used. A profile-specific application must certify the full-plane theta bound, a uniform coefficient tail estimate, the commutator approximation and finite matrix, and the positive gap (3). A nonlinear use additionally requires a high space, a strain trace and compatible rough-transport estimates. These remain open here.

## 5. Relationship with the existing signed energy

The signed principal matrix above is the negative of the baseline matrix

    A = [[rho_y, -rho_x/2],[-rho_x/2,0]].

Thus the baseline condition B2 already certifies theta<=1/20 for its certified reference. This note does not claim that the baseline discarded the sign. Its different proposal is to certify the compact energy remainder by finite rank, potentially avoiding a compulsory Hdot^-1 term in the low norm. No such improvement has yet been certified.

There is a useful exact identity explaining the existing Hdot^-1 correction. For compact smooth h in S1, set phi=(-Delta)^(-1)h, p=phi_x and q=phi_y. Integration by parts gives

    integral b(phi_xx phi_yy - phi_xy^2)
      = integral [b_xy p q - (b_yy p^2+b_xx q^2)/2].

Therefore, with a=rho_x, b=rho_y,

    <Qh,h> = integral[-b(phi_xx^2+phi_xy^2)
                          +a phi_xy(phi_xx+phi_yy)]
                  + integral (grad phi)^T N (grad phi),
    N = (1/2) [[rho_yyy,-rho_xyy],[-rho_xyy,rho_xxy]].      (8)

The first integral is bounded by theta ||D^2 phi||_2^2=theta ||h||_2^2. If N<=C_N I, the second is bounded by C_N ||h||_H^2. The identity is justified first by cutoffs of phi and passage to the limit; compact S1 h has zero mean, so grad phi is square integrable and the boundary errors vanish. Bounded coefficient derivatives suffice for these passages.

Under the baseline bounds theta<=1/20, C_N<=1 and H energy decay19/5, choosing the energy ||h||_2^2+(20/21)||h||_H^2 gives decay at least11/4 for c>9/5. Indeed c+1-theta>=11/4 and (20/21)(19/5-11/4)=1. This reproduces the existing E0 coefficient and explains why merely sharpening theta is not a substantial new closure mechanism.

The diagnostic in `verification/principal_scan.json` samples theta for C1-BASE-S131. It is FLOAT, not a whole-plane upper bound. It is separate from B2's existing certificate and from the still-open finite-rank remainder calculation.

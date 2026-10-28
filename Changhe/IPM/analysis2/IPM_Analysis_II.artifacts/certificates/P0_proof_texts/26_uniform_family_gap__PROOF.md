# A uniform residual obstruction for the fixed finite N-B family

Status: CONFIRMED V106 by independent algebra and arithmetic, with lead review CORRECT at07:41Z. This is a lower bound for the unweighted Route U norm. No uniform weighted obstruction is asserted.

## 1. Exact statement, family and dependencies

Put c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma. Consider any real potential

    chi=sum_(0<=j<=5, 0<=m<=59, m<=k<=75) a_(j,m,k)
             r^(2k)(1+r^2)^((3+gamma-j delta)/2-k)cos(2m theta).

Set rho=-partial_y Delta chi, U=(-chi_xyy,chi_xxy) and F=(cX+U).D rho-rho. The function is smooth on the plane and has the density parity. Its subquadratic stream function is the canonical one by the uniqueness statement of topic01. Impose these exact affine constraints on the potential coefficients:

1. For each j=0,...,5, the leading cosine polynomial sum_(m,k) a_(j,m,k)cos(2m theta) is C_(j+1), the six stationary homogeneous potential profiles uniquely determined by the full leading angular profile of original state131. Topics05 and10 construct these profiles. Their exact rational coefficients are in 10_tail_splice/verification/state131_splice.json.
2. For j=0,1, the first descendant cosine polynomial sum_(m,k) a_(j,m,k)((3+gamma-j delta)/2-k)cos(2m theta) vanishes.

The center normalization may also be imposed but is not needed for this lower bound. Coefficients may be arbitrarily large. The exact A2, A3, A4, A5 and Mpen references satisfy these constraints whenever their separate canonical audits pass. The larger displayed index set is intentional and contains their supports.

Write e(theta)=sum_m e_m sin(m theta) for the residual coefficient at degree p_star=gamma-6delta=1-7delta. It is fixed by the six leading branches and is independent of every remaining coefficient. Only odd m=1,...,139 occur, and its full-circle L2 norm is greater than3081.27. Define

    a0=7delta/2-2,
    A={ell delta/2+k-2 : 1<=ell<=12, 0<=k<=154,
                                  ell delta/2+k-2>=a0}.

List the1852 distinct elements increasingly as a0,a1,...,a1851. Define

    D=(2a0+1)^(-1/2) product_(j=1)^1851 (a_j-a0)/(a_j+a0+1),
    C_D^2=sum_j a_j^2+sum_(i<j)(2a_i+1)(2a_j+1).

Then every potential in the family satisfies

    ||F||_(dot H^-1)^2 >= (pi/2) D^2
                      sum_m e_m^2/[m^2+(1+2C_D)^2].                 (1)

The384-bit evaluation and independent512-bit audit gives the right-hand square root greater than2.67750e-7. For the Route U norm N_s=E2(J^s .), s=2^-18, the established reverse comparison N_s(F)>=(1-34s)E2(F) and the negative component of E2 give

    N_s(F)>=(1-34s)sqrt((20/21)2^18)||F||_(dot H^-1)
           >0.00013376.                                          (2)

This exceeds210 times eta_U=1/1572864. Thus no member of this particular finite family can satisfy the existing Route U sufficient residual threshold, even with arbitrary real coefficients. This is neither a nonexistence theorem for IPM nor a lower bound for arbitrary reference families. Adding a branch, changing the leading profile or exponent, or increasing the degree changes the argument and its constants.

Numerical inequalities in this statement become certified only after the accompanying verification program and audit record pass. The norm definition and reverse comparison are in topics09 and13; no background matrix or coefficient assumption is used to compare norms.

## 2. Exact finite power representation

Put u=(1+r^2)^(-1), t=1-u. Topic11 derives, by repeated Cartesian differentiation expressed in polar variables,

    F_m(r)=sqrt(1-u)u^(-1/2) H_m(u),
    H_m(u)=sum_(ell=1)^12 u^(ell delta/2) P_(ell,m)(1-u).           (3)

Here every P is a real polynomial of degree at most153. To check this degree rather than assume it, a d-th derivative of one potential generator has, after its common radial factor is removed, powers t^(k-2+l), 0<=l<=d. At d=3 the degree is at most k+1<=76; at d=4 it is at most k+2<=77. Negative powers cancel for each generator separately because k>=m makes that generator smooth. Each generator has one fixed radial exponent, so its angular polynomial after differentiation is divisible by the power of t needed for origin regularity. This assertion is applied before summing distinct radial exponent classes. The nonlinear term multiplies a third derivative and a fourth derivative and therefore has degree at most153. The linear terms have degree at most77. The branch number of a single derivative is ell=j+1, while a nonlinear product adds two such branch numbers. Thus1<=ell<=12 contains every residual term. This reasoning allows zero polynomials and does not assume that all possible powers are actually attained.

The exact rational delta makes every ell delta/2+k in the displayed finite ranges distinct. The leading stationary conditions cancel the sectors with j=0,...,5 and q=0; the two descendant conditions cancel the sectors(j,q)=(0,1),(1,1). The relation between the exterior expansion and(3) is triangular within each fractional power class. These are exactly the eight exponents below lambda_star=7delta/2 in(3). Hence they vanish there too. The next exponent is lambda_star and its coefficient is e_m. Since no potential branch j=6 is present, that residual coefficient consists solely of the quadratic interactions of branches i+j=5, so it is fixed. Multiplication by1-u does not change it.

Set

    w_m(u)=(1-u)u^(-2)H_m(u).

This belongs to the real power space V=span{u^a:a in A} and its u^a0 coefficient is e_m. The additional factor1-u accounts for the degree154 in A. Since a0>-1/2, all powers in V are square integrable. No assertion that an arbitrary element of V is a nonlinear residual is required: using the larger linear space weakens a valid lower bound.

## 3. Distance of one power from a finite span

Let -1/2<a0<a1<...<an. In L2(0,1), the distance of u^a0 from span{u^a1,...,u^an} is

    D=(2a0+1)^(-1/2) product_(j=1)^n (a_j-a0)/(a_j+a0+1).          (4)

Distinct powers are linearly independent: setting u=exp(t) gives distinct exponentials, whose derivatives have a nonzero Vandermonde determinant at any interior t. Their Gram matrix is therefore positive definite. Let q be the orthogonal residual of u^a0. Its Mellin transform Q(z)=int_0^1 q(u)u^z du is rational, with simple poles at-a_j-1, zeros at a1,...,an, and residue1 at-a0-1. Its numerator has degree at most n, so these conditions give

    Q(z)=C product_(j=1)^n(z-a_j)/product_(j=0)^n(z+a_j+1),
    C=product_(j=1)^n(a0-a_j)/(a0+a_j+1).

The residue condition fixes this constant, including its sign. Orthogonality gives ||q||2^2=<q,u^a0>=Q(a0), which is the square of(4). Consequently every element of V whose u^a0 coefficient is e has norm at least|e|D. The minimizing orthogonal projection exists in this finite-dimensional space, so this is an exact distance formula.

## 4. A norm bound for dilation

The operator B=u partial_u preserves V. For f,g in V, integration by parts gives

    <Bf,g>+<f,Bg>=f(1)g(1)-<f,g>.                               (5)

The endpoint at zero vanishes because every exponent in u f g is positive. Gram-Schmidt in increasing exponent order gives orthonormal polynomials p_j in the powers, each in span{u^a0,...,u^aj}. Thus B has a triangular matrix with diagonal a_j. Taking f=g=p_j in(5) yields p_j(1)^2=2a_j+1. For i<j, Bp_i belongs to the earlier span and is orthogonal to p_j. Taking f=p_i,g=p_j in(5) therefore shows that the other triangular entry has square(2a_i+1)(2a_j+1). The Frobenius norm bounds the operator norm, proving

    ||Bw||2<=C_D||w||2.                                          (6)

This is not a spectral-radius estimate and does not assume that B is self-adjoint.

## 5. The actual homogeneous negative norm

For one sine mode m>=1, let s=log r and g_m(s)=r^2F_m(r). Writing the potential of -Delta in these variables gives

    ||F_m(r)sin(m theta)||_(dot H^-1)^2
        =pi <g_m,(-partial_s^2+m^2)^(-1)g_m>_L2(ds).              (7)

Indeed the radial Poisson equation becomes -phi_ss+m^2 phi=g_m and its Dirichlet energy is pi int(phi_s^2+m^2 phi^2)ds. The positive cylinder operator has inverse kernel exp(-m|s-t|)/(2m). For g_m in L2, this is the unique H1 cylinder solution, and hence realizes the homogeneous inverse in this angular sector. Approximation by smooth compactly supported cylinder functions justifies the pairing and identifies it with the completion of the full-plane Dirichlet space. There is no zero angular mode.

In the present finite family g_m belongs to H1(R). At r=0 the smooth odd residual is O(r), so g_m and its s derivative decay at least like r^3. At infinity F has a differentiable expansion beginning at p_star<-2, so g_m and its derivative decay exponentially in s. The same conclusion also follows directly from the formulas below and(6).

For a positive operator A=-partial_s^2+m^2, Cauchy-Schwarz gives

    <g,A^-1g> >= ||g||2^4/(||g'||2^2+m^2||g||2^2).               (8)

Using r^2=(1-u)/u and |ds|=du/[2u(1-u)], direct substitution gives

    ||g_m||2^2=(1/2)||w_m||2^2,
    ||g_m'||2^2=(1/2)||(-1+2u)w_m-2u(1-u)w_m'||2^2.             (9)

Since |2u-1|<=1 and |1-u|<=1, equations(4),(6),(9) imply

    ||g_m||2>=|e_m|D/sqrt(2),
    ||g_m'||2<=(1+2C_D)||g_m||2.

Equations(7)-(8) now prove(1) for each mode. Distinct sine modes are orthogonal in the Dirichlet energy, so their squared bounds add. This proves the stated full norm inequality.

## 6. Scope of the obstruction

This argument controls the actual unweighted negative norm, rather than merely the proxy ||rF||2. The factor C_D is essential for that passage. The degree bound and all eight cancellations are also essential.

The weighted norm L_R(F)=||(1+r^2/R^2)^(-11/10)F||_(dot H^-1) is not bounded below by a fixed multiple of the unweighted norm on arbitrary functions. Its multiplier changes the finite power space. Therefore(1)-(2) do not establish a coefficient-independent weighted gap. The previously certified weighted annular gaps remain statements about their particular exact candidates. A separate argument is required for a uniform weighted bound.

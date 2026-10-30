# Angular Gram audit of optimization quadrature

## Statement

Let the potential use only harmonics cos(2m theta), with 0<=m<=M. At each fixed positive radius the density residual F is a sine polynomial in positive odd frequencies n<=4M+3. Consequently its quotient F/(r sin theta) is a cosine polynomial in even frequencies 0,2,...,4M+2.

On the quadrant [0,pi/2], orthonormal bases for these spaces are

s_k(theta)=sqrt(4/pi) sin((2k+1)theta), 0<=k<=2M+1,
c_0=sqrt(2/pi), c_k(theta)=sqrt(4/pi)cos(2k theta), 1<=k<=2M+1.

For any positive angular quadrature with nodes theta_i and weights w_i, let G_kl=sum_i w_i b_k(theta_i)b_l(theta_i), for either basis. The exact angular squared integral of a polynomial with coefficient vector v is v^T v, while the quadrature gives v^T Gv. Thus

lambda_min(G)||v||^2 <= quadrature <= lambda_max(G)||v||^2.

A numerical computation of these eigenvalues is a floating screening test, not a validated quadrature error bound. It can nevertheless expose unresolved angular directions independently of any optimizer or candidate values. Candidate-specific energy errors may be much smaller than this worst-case error.

## Angular bandwidth proof

The Laplacian preserves each angular frequency, so rho=-partial_y Delta chi has odd frequencies at most2M+1. The stream function psi=chi_xy has even frequencies at most2M+2. The advection is the polar Jacobian (psi_r rho_theta-psi_theta rho_r)/r, whose angular frequencies are bounded by the sum4M+3. Linear radial transport preserves the density frequencies. S1 symmetry leaves only odd sine modes. Finally sin((2k+1)theta)/sin(theta)=1+2 sum_(j=1)^k cos(2j theta), proving the quotient bandwidth.

## Uniform midpoint comparison

The uniform midpoint nodes theta_i=(i+1/2)pi/(2N), i=0,...,N-1, and weights pi/(2N) give exact orthogonality for both bases whenever N>=2M+2. This is the finite geometric-series identity for the cosine sum, applied to products through twice the maximum frequency. It is not the polynomial exactness statement for Gauss-Legendre quadrature in theta. The latter rule integrates algebraic polynomials of degree2N-1 exactly, whereas these angular basis functions are trigonometric; its Gram matrix must be checked separately.

The code compares Gauss-Legendre and midpoint rules at several orders, records extreme eigenvalues and the most inaccurate mode pair, and hashes the implementation. NumPy eigensolutions are labeled FLOAT. A failure in this worst-case test is a reason to increase the rule or change it, not a proof that one particular candidate's reported loss is wrong.

## Candidate-specific radial slices

For an exact residual representation F(r,theta)=sum_(n odd) f_n(r)sin(n theta), first evaluate f_n(r) from the exact radial polynomials with Arb2048 at a finite list of rational radii. This retains the actual candidate's angular coefficients. The full-circle density integral is pi sum_n f_n^2. The quotient cosine coefficients are a_0=sum_n f_n/r and a_(2k)=2 sum_(n>2k)f_n/r, so its quadrant integral is (pi/2)a_0^2+(pi/4)sum_(k>=1)a_(2k)^2.

The slice script converts the validated coefficient midpoints to binary64 for the quadrature comparison. It compares the direct positive weighted sums against these exact-angular formulae. The resulting relative errors are FLOAT diagnostics; the stored Arb coefficient and norm intervals are valid enclosures but do not make the binary64 quadrature error a rigorous bound. A finite list of radii also does not certify the full radial objective.

## Validated witness for a specified floating rule

A further test freezes every binary64 quadrature node and weight as an exact rational number. It also rounds an approximate least-eigenvalue vector to rational coefficients. The sine polynomial with these coefficients is a fully specified mathematical function. Its exact squared integral on the quadrant is pi/4 times the sum of coefficient squares. Arb sine evaluation encloses its positive weighted quadrature sum for the frozen nodes. A strict upper bound on the ratio is a rigorous statement about that particular quadrature rule. It does not need validated Gauss root construction, since the nodes themselves are the exact input rationals, and it makes no claim about every possible implementation of Gauss-Legendre quadrature. This proves a potential failure on the complete allowed harmonic space; it does not prove that the polynomial is realized by an actual nonlinear candidate residual.

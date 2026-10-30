# Nonzero density tails in the exact candidate007

## Statement

Fix c=4076476460239181/2251799813685248, gamma=1/c and
delta=1-gamma. Let chi be the exact immutable candidate007 potential
with its2982 generators and canonical representation. For j=0,...,7
put e_j=1-(j+1)delta and d_j=3+e_j. Every branch has a uniform exterior
expansion, including one differentiated remainder,

    rho_j(r,theta)=r^e_j Theta_j(theta)+O(r^(e_j-2)),
    r partial_r rho_j=e_j r^e_j Theta_j(theta)+O(r^(e_j-2)),

where rho=-partial_y Delta chi. Each Theta_j is a finite sine polynomial.
The exact verification records all its coefficients and proves that
its first sine coefficient is nonzero for every j=0,...,7. In
particular the four nonintegrable unweighted density tails j=0,...,3
are all present. These are branch coefficients of the density; they
are not residual coefficients or numerical residual lower bounds.

## Exact endpoint and Fourier calculation

In a block(j,m), all generators have common factor

    H_m (1+r^2)^(p_j-m), H_m=Re(x+iy)^(2m), p_j=d_j/2,

with radial polynomial t^w or t^w P_n(2t-1), t=r^2/(1+r^2).
The Legendre recurrence

    (n+1)P_(n+1)(z)=(2n+1)zP_n(z)-nP_(n-1)(z)

and P_0(1)=P_1(1)=1 show inductively that every endpoint is1.
Thus A_(j,m), the leading potential amplitude, is the exact sum
of its generator coefficients. Independently, it is the sum over k
of the canonical coefficients A_(j,m,k). Both full maps are compared.
Since t=1+O(r^-2) and the factors are smooth powers, finite
differentiation of their Taylor expansion proves the two remainder
estimates above, uniformly in angle.

For an angular exponential exp(in theta), the Laplacian of
r^d exp(in theta) is(d^2-n^2)r^(d-2)exp(in theta). Also

    partial_y[r^k exp(in theta)]
      =i r^(k-1)[(n-k)exp(i(n+1)theta)
                        +(n+k)exp(i(n-1)theta)]/2.

Split each cosine amplitude into its positive and negative
frequencies. Apply these two formulas and the sign in
rho=-partial_y Delta chi. The resulting Fourier coefficients
are purely imaginary and opposite at n and-n. Convert them
back to real sine coefficients. This computes every frequency
without specializing to sine1. Only m=0 and1 can contribute to
sine1, giving the separate identity

    b_(j,1)=-A_(j,0)d_j^2(d_j-2)
                  +A_(j,1)(d_j^2-4)d_j/2.

The full Fourier value, this two-term value and T4-222's exact
canonical endpoint value must agree as rational numbers. Strict
rational enclosures are obtained by integer division, with an
extra unit on both sides, not by rounding printed decimals.

## Integrability thresholds and finite amplitude check

For E_a=L2(R2,(1+r^2)^(-a)dX), a nonzero pure angular tail r^e Theta
is in E_a outside a circle if and only if e<a-1. Indeed its positive
angular square integral multiplies the radial integral of
r^(2e+1-2a), up to factors bounded above and below by positive
constants. At equality the radial integral diverges logarithmically.
The retained exact inequalities show e_3>-1>e_4 and

    0<4gamma-2<3gamma-1<2gamma<1+gamma.

Consequently the count of nonintegrable branch tails is4,3,2,1,0
as a crosses these thresholds, with the lower count starting
strictly after the corresponding endpoint. The one differentiated
exterior remainder is O(r^(gamma-2)) and belongs to E_a for a>=0.

For rho_lambda(X)=lambda rho(X/lambda), the j-th amplitude change
is(lambda^((j+1)delta)-1)Theta_j. Its first four coefficient vectors
span four dimensions: set z=lambda^delta and choose z=2,3,4,5.
A relation among the columns z_i^k-1, k=1,...,4, would give a
degree-at-most4 polynomial vanishing at five distinct points
1,2,3,4,5. It must vanish identically. The checker also computes
this determinant by the full permutation expansion. This supplies
the exact numerical hypotheses for T4's finite amplitude chart.
The general chart theorem and the Opus discussion are separate.
No canonical velocity bound, inverse, optimization improvement or
existence result is inferred from these eight coefficients.

## Dependencies and verification

The immutable raw and canonical candidate hashes and their prior
exact identity are in basis_redundancy and family_tail_equality.
The own code uses the Legendre recurrence and the full Fourier
derivative formulas above, while the frozen peer uses canonical
endpoint sums and the specialized sine1 formula. All8 branches,
all360 amplitude blocks, all2982 generator endpoints, strict
thresholds and the4-by-4 determinant are checked exactly.
The source manifest freezes the peer proof/code/result.

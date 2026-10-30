# Independent audit of scaled potential generators

## Statement, hypotheses and scope

Let m,w,n,Q be nonnegative integers, p rational, and R a positive rational number. Set s=x^2+y^2, H_m=Re(x+iy)^(2m), a=p-m and B=w+Q+n. The generator is

    chi=H_m (1+s)^a [s/(R^2+s)]^w [R^2/(R^2+s)]^Q
         P_n((s-R^2)/(s+R^2)),                           (1)

where P_n(1)=1 is the ordinary Legendre polynomial. All statements below extend by finite linearity. They confirm the algebraic, origin, far-field and Cartesian-evaluation statements in the frozen N4 proof. They do not certify any future candidate's coefficients, residual norm, inverse estimate or existence.

The restriction R rational makes the series coefficients rational. Analytic statements remain valid for real R>0, but rational arithmetic then needs a representation of R or R^2.

## Origin and field normalization

The denominators in (1) are positive for s>=0, and (1+s)^a is smooth. At the origin the radial factor equals

    (-1)^n R^(-2w) s^w + O(s^(w+1)).

This follows from P_n(-1)=(-1)^n and direct evaluation of the remaining factors. Thus the first nonzero homogeneous polynomial in chi is (-1)^n R^(-2w) H_m s^w, with exact degree2(m+w). If m+w>=5, every derivative through order9 vanishes.

For rho=-partial_y Delta chi and U=(-chi_xyy,chi_xxy), the origin quantities rho_y(0)=-chi_xxyy(0)-chi_yyyy(0) and partial_y U2(0)=chi_xxyy(0) use only fourth derivatives. Such added generators therefore preserve both quantities exactly. This is a statement about the explicitly defined fields. Canonical inversion for an arbitrary growth exponent p is a separate issue; the campaign's admissible sublinear class supplies that dependency when needed.

## Far-field coefficients and convergence

Write chi=G(r)cos(2m theta), z=r^-2, and P_n(v)=sum c_k v^k. Direct substitution gives

    r^(-2p)G(r)=R^(2Q) z^Q (1+z)^a
       sum_(k=0)^n c_k (1-R^2 z)^k
                         (1+R^2 z)^(-w-Q-k).            (2)

This formula is an independent way to compute the coefficients. Each finite requested coefficient is a finite sum of rational binomial coefficients. Factoring out (1+R^2 z)^(-B) gives the N4 numerator

    A_n(v)=sum c_k (1-v)^k (1+v)^(n-k).

Both forms are identical. Their series converge absolutely for |z|<min(1,R^-2), so they give the actual generator for r>max(1,R). Since P_n(1)=1 and P_n'(1)=n(n+1)/2, logarithmic differentiation at zero, after removing z^Q, yields

    M_q=0 (q<Q), M_Q=R^(2Q),
    M_(Q+1)=R^(2Q)[a-R^2(w+Q+n(n+1))].                 (3)

The derivative value follows by substituting v=1 in (1-v^2)P_n''-2vP_n'+n(n+1)P_n=0. For R>1 and B>0, A_n(-1)=2^n c_n is nonzero. Thus z=-R^-2 is a pole of order B and is the nearest singularity; the convergence radius is exactly R^-2. Moving the scale R outward therefore moves the guaranteed far-field region outward.

For 0<=z<eta<min(1,R^-2), define

    C_eta=R^(2Q) eta^Q (1-eta)^(-|a|)
           sum_k |[v^k]A_n| (R^2 eta)^k
           (1-R^2 eta)^(-B).

For real a, |binom(a,j)|<= (|a|)_j/j!: each factor |a-l| is bounded by |a|+l. Therefore the absolute binomial series bounds |(1+zeta)^a| by (1-eta)^(-|a|) on |zeta|=eta. All remaining factors have the displayed polynomial and denominator bounds. Cauchy's formula gives |M_j|<=C_eta eta^-j. Summing the geometric tail proves

    |r^(-2p)G(r)-sum_(j=0)^K M_j z^j|
       <= C_eta (z/eta)^(K+1)/(1-z/eta).                (4)

This confirms N4's finite-prefix remainder statement. Residual tails require differentiated versions and coefficient summation; (4) for the potential alone is insufficient.

## Cartesian jets with only one irrational factor

Define the exact polynomial

    N(s)=s^w sum_k c_k (s-R^2)^k(s+R^2)^(n-k).

The radial factor in (1) is R^(2Q) N(s)(1+s)^a(R^2+s)^(-B). At a rational point (x0,y0), let s0=x0^2+y0^2. Its Taylor coefficient of h^l is the common positive factor

    Z=R^(2Q)(1+s0)^a(R^2+s0)^(-B)

times the exact rational number

    sum_(i+j+k=l) [h^i]N(s0+h)
           binom(-B,j)(R^2+s0)^(-j)
           binom(a,k)(1+s0)^(-k).                      (5)

Thus all Cartesian derivatives can be formed by exact rational arithmetic followed by a single positive real power. Substitute h=2x0 X+2y0 Y+X^2+Y^2 in the scalar polynomial through degree d and multiply by H_m(x0+X,y0+Y). The omitted scalar terms have total degree at least d+1 because h has no constant term. Multiplying the coefficient of X^iY^j by i!j! gives the derivative. Formula (5) is also valid at s0=0 because N is evaluated as a polynomial; no division by s0 occurs.

N4's implementation forms the same truncated algebra by a Legendre recurrence and repeated outward interval products. This alternative groups every rational coefficient exactly before evaluating Z, so it supplies an independent interval path rather than a comparison with a decimal approximation. Finite exact checks supplement the analytic proof; they do not replace it.

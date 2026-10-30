# Full weighted residual norms of a finite single-scale profile

## Statement and scope

Let c>1 be rational, delta=1-1/c, and let a finite smooth S1 potential determine the canonical density rho and stream function psi by rho=-partial_y Delta chi and psi=partial_xy chi. The velocity is u=(-psi_y,psi_x). Suppose their exact finite polar representations are

    rho=r sum_(j,n) z^b_j R_(j,n)(t) sin(n theta),
    psi=r^2 sum_(j,m) z^b_j S_(j,m)(t) sin(m theta),
    t=r^2/(1+r^2), z=1-t, b_j=(j+1)delta/2,

with rational polynomials, j>=0, positive odd n and positive even m. The potential construction and exact origin divisibility checks are the already audited polar identities in ../weighted_forcing_audit/PROOF.md. These are hypotheses here, not conclusions from point sampling.

Define the exact residual F=(cX+u).D rho-rho. For a rational real weight parameter a set w=(1+r^2)^(-a/2). The construction below gives its full weighted norm whenever the finite separated integrability checks hold:

    ||w F||_2^2=(pi/2) E_a,

where E_a is an explicitly computed rational number. The angular integral is over the full circle. No radial truncation, omitted tail or spatial quadrature enters this identity. It is a forcing norm and is not a correction radius or an existence theorem.

## Complete residual algebra

On r^d z^b P(t), the logarithmic radial derivative is r^d z^b T_(b,d)P, where

    T_(b,d)P=(d-2bt)P+2t(1-t)P'.

The linear term contributes c T_(b_j,1)R-R in exponent b_j at mode n. For a density term (i,n,R) and stream term (j,m,S), the nonlinear product is

    r z^(b_i+b_j) [n R T_(b_j,2)S sin(m theta)cos(n theta)
                    -m S T_(b_i,1)R cos(m theta)sin(n theta)].

The product-to-sum identities therefore give the coefficients

    [n R T_(b_j,2)S-m S T_(b_i,1)R]/2 at mode n+m,
    [-n R T_(b_j,2)S-m S T_(b_i,1)R]/2 at mode n-m.

A negative sine mode is folded with a minus sign. Equal exponents and angular modes are added exactly before integration. This reconstructs F pointwise from its defining differential equation, by algebraic identities, with no Fourier truncation of the products. Write the result as

    F=r sum_(ell,n) z^(ell delta/2) P_(ell,n)(t) sin(n theta).

Here ell=j+1 for a linear term and ell=i+j+2 for a product. All P are rational polynomials.

## Integrability and the exact moment

Replace every whole polynomial by Q_(ell,n)(z)=P_(ell,n)(1-z), and let v_(ell,n) be its exact vanishing order at z=0. Zero polynomials are discarded. A sufficient separated integrability check is

    a-3+ell delta+2v_(ell,n)>-1                         (1)

for every remaining component. Indeed the exponent of every cross term is the arithmetic mean of its two diagonal exponents, so (1) makes every monomial after its exact vanishing factors integrable. This permits expansion of the finite square and integration term by term. A failed separated check alone is not a divergence proof, because distinct components could cancel.

Angular orthogonality and r^3 dr=-(1-z)dz/(2z^3) give

    E_a=sum_n sum_(ell,k) integral_0^1
          z^(a-3+(ell+k)delta/2) (1-z)
          Q_(ell,n)(z)Q_(k,n)(z) dz.                   (2)

The ordered sum includes all branch cross terms. Equivalently use unordered pairs with multiplier two off the diagonal. Group every exact polynomial by the rational exponent e=(ell+k)delta/2-3:

    H_e(z)=sum (1-z)Q_(ell,n)(z)Q_(k,n)(z).

If H_e(z)=sum h_(e,v) z^v, formula(2) is

    E_a=sum_(e,v) h_(e,v)/(a+e+v+1).                    (3)

Every denominator with a nonzero coefficient is positive after the checks. Formula(3) is rational for rational inputs. An outward enclosure of pi and its square root yields an outward norm enclosure. Exact positivity of E_a is checked for a nonzero residual. Signed polynomial terms must not be discarded before summation.

Smoothness of the original profile ensures integrability at r=0. The formula also directly has bounded polynomials at z=1 and the factor1-z. Thus the only nontrivial endpoint check is r=infinity, which is precisely (1).

## A sharp membership test when a leading sector survives

Let q be the minimum of ell delta/2+v_(ell,n). Combine all leading coefficients attaining q at each angular mode, and let C(theta) be their finite sine sum. If C is not zero, the finite expansion gives

    F(r,theta)=r^(1-2q) [C(theta)+O(r^(-epsilon))]

uniformly in theta for some epsilon>0. This follows from z=r^-2(1+O(r^-2)) and from the positive gap to the next exponent in a finite sum. The squared angular norm tends to ||C||_L2(circle)^2>0 after factoring out r^(2-4q). Hence the radial weighted integral is finite exactly when

    a>2-2q.

At equality it diverges logarithmically. This proves an actual membership or nonmembership claim after exact leading-sector combination; it does not use the merely sufficient separated check. The code checks the nonzero leading angular vector for state131, and records q and the threshold.

## Verification status

The complete residual algebra is the same independently audited construction used for T4-032. Formula(3) is a specialization to the full radial interval and R=1. New numerical norms remain original T4 results pending independent reproduction. They do not verify the compact weighted inverse or the missing high resolvent estimate in the dyadic framework. All input, code and result hashes and the actual computation time are recorded in verification.

# Annular lower bounds for a regularized weighted forcing norm

## Statement and hypotheses

Fix exact rational c>1 and put delta=1-1/c. Let F be the residual of a finite smooth S1 generator potential, with exact real sine expansion

F(r,theta)=r sum_(ell,n) u^(ell delta/2) P_(ell,n)(1-u) sin(n theta),
u=(1+r^2)^(-1), n positive and odd.

The finite polynomials P have rational coefficients. No unweighted global integrability is assumed. Let a>0, R>0 and w_R(r)=(1+r^2/R^2)^(-a/2). For any 0<A<B<infinity,

||w_R F||_2 >= (1+B^2/R^2)^(-a/2) ||F||_(L2(A<r<B)).

The right side has the finite exact-power formula below. The inequality remains true with an infinite left side. If several disjoint annuli are used, their weighted lower bounds may instead be combined in squared norm.

## Exact annular integration

Angular orthogonality gives

||F||_(L2(A<r<B))^2
 = (pi/2) sum_n integral_(U_B)^(U_A) (1-u) u^(-3)
      [sum_ell u^(ell delta/2) P_(ell,n)(1-u)]^2 du,
U_A=(1+A^2)^(-1), U_B=(1+B^2)^(-1).

Expand the finite square, counting the diagonal once and each cross term twice. Collect equal exponents to write the integrand as a finite sum of u^b Q_b(u). If Q_b(u)=sum_k q_(b,k) u^k, each term contributes

q_(b,k) [U_A^(b+k+1)-U_B^(b+k+1)]/(b+k+1)

when b+k+1 is nonzero, and q_(b,k) log(U_A/U_B) otherwise. This formula holds for every real exponent because both endpoints are strictly positive. It does not extrapolate a leading asymptotic coefficient or require a guessed onset radius.

The weight w_R is positive and decreasing, so w_R(r)^2 >= w_R(B)^2 on the annulus. Multiply the unweighted annular integral by this constant and take the nonnegative square root to prove the statement. For disjoint annuli, integrate this pointwise bound on each annulus and sum before taking the square root.

## Verification and scope

All polynomial construction and differentiation use the exact coefficient representation audited in ../radial_fourier/PROOF.md. Rational coefficients are converted to outward Arb balls only for finite-power evaluation. The code checks that each annular integral is strictly positive before reporting its square root; an inconclusive interval is an arithmetic failure to resolve. The result is a lower bound for the specified weighted norm, not an upper bound or an inverse estimate.

In particular, a large forcing norm does not by itself prove that the actual linear correction is large, since a bounded inverse supplies only an upper estimate on its output. The calculation quantifies a cost of a proposed norm and normalization. It does not rule out a weighted nonlinear theory or an exact nearby solution in a different norm.

## Exterior lower bound when the weighted norm is finite

A second bound includes the entire exterior, which matters when the weighted decay exponent is close to its integrability endpoint. For r>=R and u=(1+r^2)^(-1),

w_R(r)^2 = R^(2a) u^a / [1+(R^2-1)u]^a.

If R>=1, the denominator inside brackets lies between1 and2, so

w_R(r)^2 >= (R^2/2)^a u^a.

Consequently

||w_R F||_2^2 >= (R^2/2)^a (pi/2)
  sum_n integral_0^((1+R^2)^(-1)) (1-u) u^(a-3)
  [sum_ell u^(ell delta/2) P_(ell,n)(1-u)]^2 du.

The exact finite-power antiderivative now has lower endpoint zero. Its validity requires that each actual diagonal exponent after extracting the exact polynomial order at zero be greater than -1. Cross exponents are averages of these diagonal exponents and then satisfy the same condition. If the check fails, this implementation returns no exterior bound; it does not infer divergence solely from a failed separated check. For the stated finite nonresonant family, exact extraction also identifies the leading exponent directly.

The comparison uses a pointwise lower weight on the same nonnegative squared field, before expansion. Therefore signed polynomial cross terms do not invalidate it. All terms must be included in the finite integral; taking only selected signed terms would be unsound. This exterior bound and overlapping annular bounds cannot be added, but their maximum is again a valid lower bound.

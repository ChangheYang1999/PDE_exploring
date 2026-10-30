# The two triangular halves of the radial Green integral

## Statement and normalization

For an integer n>=1 and R>0, let f(r)=sum_j e_j r^(a_j) for r>=R and f=0 for r<R, with finitely many real coefficients and exponents a_j<-2. Take the real plane source F(r,theta)=f(r)sin(n theta). The homogeneous negative Sobolev norm is defined by

||F||dotH^-1^2 = integral_R2 F(-Delta)^-1 F.

With full-circle angular measure this norm is

||F||dotH^-1^2
 = (pi/(2n)) integral_R^infinity integral_R^infinity
       (min(r,s)/max(r,s))^n f(r)f(s) r s dr ds
 = (pi/n) sum_(i,j) e_i e_j
       R^(a_i+a_j+4)/[(-a_i-a_j-4)(n-a_i-2)].             (1)

The ordered sum over i,j does not remove the factor two between the square and either one of its triangular halves.

This statement is exact for the displayed finite power source. Applying it to a finite asymptotic expansion of a different source requires a separate remainder estimate. It is not an exact norm certificate for an unbounded omitted remainder.

## Proof

The radial Green kernel for the nth sine mode of -Delta is (min(r,s)/max(r,s))^n/(2n). Its normalization follows either from the jump in r times its radial derivative at r=s, or by solving the radial equation with the regular solution r^n and the decaying solution r^-n. Full-circle orthogonality gives integral_0^(2pi) sin(n theta)^2 dtheta=pi, proving the first equality.

Absolute convergence follows by treating the finite sum termwise. On the triangle R<=s<=r, for outer exponent a and inner exponent b, Tonelli applied to the positive power integrand gives

I(a,b)
 = integral_R^infinity r^(a+1-n) integral_R^r s^(b+1+n) ds dr
 = integral_R^infinity s^(b+1+n) integral_s^infinity r^(a+1-n) dr ds
 = R^(a+b+4)/[(n-a-2)(-a-b-4)].                         (2)

Both denominators are positive because a,b<-2 and n>=1. Formula (2) is valid also when b+n+2=0. In that case evaluating the inner integral first would introduce a logarithm; the reversed order avoids an artificial division by zero.

The diagonal r=s has zero two-dimensional measure. The symmetric integrand has equal integrals on the two complementary triangles. Expanding f(r)f(s) on one triangle gives sum_(i,j) e_i e_j I(a_i,a_j); it still represents only that triangle, even though the sector indices are ordered. Multiplication by two proves the second equality in (1).

## Exact synthetic test

Choose R=1, n=1 and f=r^-4 outside the unit disk. Then I(-4,-4)=1/12, and (1) gives ||F||dotH^-1^2=pi/12.

An independent potential calculation gives the same result. The radial solution of -Delta(p(r)sin theta)=F is

p(r)=r/6 for r<=1,
p(r)=1/(2r)-1/(3r^2) for r>=1.

Its value and first derivative agree at r=1. It is regular at zero and decays at infinity, so there is no boundary measure at the joining circle. Direct differentiation verifies the equation in both regions. Finally,

integral F(-Delta)^-1 F
 = pi integral_1^infinity r^-4 [1/(2r)-1/(3r^2)] r dr
 = pi(1/6-1/12)=pi/12.

A formula using pi/(2n) times only I would instead give pi/24 and is false.

## Audited implementation and evidence

The frozen source `source/N1_ipm_hminus1.py` computes the ordered triangular sum `tot_oo` but multiplies it by pi/(2n). Its inner and cross terms already include the factor two. The fix to this isolated factor is pi/n for the outer term. Equation (2) is also a simpler and nonsingular replacement for its subtraction formula.

The frozen d2 v4 log separates inner, cross and outer squared contributions. Adding one more copy of its outer contribution is an arithmetic diagnostic of the identified error; it does not certify the remaining quadrature or asymptotic truncation. The code in `code/` checks the exact synthetic source, the removable singularity, the frozen file hashes, and this diagnostic against the separately computed full-plane d2 Green norm.

No protected source or other lane file is modified or executed. New implementation findings require the owning lane to confirm its correction before they are described as repaired.

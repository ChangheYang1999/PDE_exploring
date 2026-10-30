# Residual sector contracts with and without a homogeneous negative norm

## Statement

Fix c=4076476460239181/2251799813685248, gamma=1/c, and delta=1-gamma. Suppose a smooth S1 residual has the finite-generator asymptotic expansion

F(r,theta)=sum_(h,q>=0) r^(gamma-h delta-2q) E_(h,q)(theta)

associated with the rational radial potential class in ../candidate_audits/PROOF.md. The expansion converges locally uniformly with all derivatives for sufficiently large r, each E is a finite odd sine polynomial, and the generators are smooth at the origin. The leading transport sector E_(0,0) vanishes identically.

For this class, the integer energy

E_*(F)^2=||omega D²F||_2²+2^14||DF||_2²+2^18||F||_2²,
omega=(1+4r²)^(2/5),

and the additional quantity ||omega D³F||_2 are finite if and only if E_(1,0)=E_(2,0)=E_(3,0)=0. This condition is weaker than the requirement for a finite homogeneous H^-1 norm. For the latter all sectors with exponent at least -2 must vanish: E_(h,0) for h=1,...,5 and E_(0,1), E_(1,1), in addition to the automatic E_(0,0)=0.

This is a membership statement, not an inverse or nonlinear existence theorem. In particular the proposed no-H closure framework of lane T4 requires a separate independent theory audit and all of its background hypotheses.

## Proof

A nonzero homogeneous sector r^e E(theta) contributes a positive multiple of integral_R^infinity r^(2e+1)dr to the squared L2 norm. It is integrable precisely when e<-1. Different exponents cannot cancel the leading nonzero term in a convergent asymptotic expansion. Orthogonality of the finite sine harmonics makes its angular energy strictly positive. These statements also hold at the borderline, where the radial integral diverges logarithmically.

A derivative of order k is O(r^(e-k)), and multiplication by omega gives O(r^(e-k+4/5)). Thus the thresholds for DF, omega D²F and omega D³F are respectively e<0, e<1/5 and e<6/5. The strictest of the four E_* and third-derivative conditions is therefore e<-1. Smoothness handles every bounded region. Uniformly differentiable convergence of the generator expansion bounds the remainder and proves sufficiency.

The exact rational c gives gamma between0.5523 and0.5524 and delta between0.4476 and0.4477. For q=0, exponents with h=1,2,3 are at least -1, while the h=4 exponent is less than -1. For every q>=1 and h>=0, the exponent is at most gamma-2<-1. The automatic sector h=q=0 has coefficient(c gamma-1)rho_0=0. These observations prove the first equivalence.

For H^-1, use the modewise Green energy derived and independently audited in ../exact_negative_norm/PROOF.md. A nonzero sector r^e sin(n theta), n positive odd, has finite exterior negative energy exactly when e<-2. Its energy scales as integral r^(2e+3)dr, with logarithmic divergence at equality. For q=0 the offending nonautomatic indices are h=1,...,5, because gamma-5delta>-2 and gamma-6delta<-2. For q=1 they are h=0,1; for q>=2 there are none. The exponents cannot resonate within these finitely many indices, as follows by exact rational comparison. This proves the second contract.

## Numerical design consequence and scope

A candidate family targeting E_* membership needs exact cancellation of three leading stationary residual sectors. It need not enforce q=1 descendant cancellations merely for membership. A four-branch potential with exact stationary leading coefficients through branch3 and enough angular modes is therefore a possible design; the previously tested860-generator family lacks the necessary angular bandwidth. Whether such a family produces small residuals or satisfies the reference bounds is a numerical question. Retaining extra tail constraints may still help optimization or another framework, but they are not forced by E_* membership.

The comparison of fractional norms with integer energies and Q3 must be taken from a proved framework with its stated constants. This note does not replace that comparison or claim that a small E_* alone is a closure certificate.

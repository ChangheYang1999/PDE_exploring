# Exact residual membership with and without a negative norm

## Statement

Fix c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma. Consider the smooth finite-generator S1 class described in source/N4_PROOF.md: its residual has a convergent, termwise differentiable large-radius expansion

F(r,theta)=sum_(h,q>=0) r^(gamma-h delta-2q) E_(h,q)(theta),

with finitely many h, nonnegative integer q and finite odd sine polynomials E. Assume the leading transport cancellation E_(0,0)=0. The full-plane energy

E_*²=||omega D²F||_2²+2^14||DF||_2²+2^18||F||_2²,
omega=(1+4r²)^(2/5),

and ||omega D³F||_2 are finite exactly when E_(1,0), E_(2,0), E_(3,0) all vanish identically. Adding ||F||_(Hdot^-1) to the requirements instead requires E_(h,0)=0 for 1<=h<=5 and E_(0,1)=E_(1,1)=0. These are membership conditions only.

## Proof

A nonzero angular profile E at exponent e contributes positive angular mass times integral r^(2e+1)dr to L2. This integral converges exactly for e<-1. Among a finite collection of offending exponents, the largest nonzero one controls the tail because the uniformly convergent remainder is smaller by a positive power. Distinct angular modes cannot remove its positive angular L2 mass. Coefficients of equal exponents must be combined first.

Here none of the possibly offending exponents collide. For L2 they are q=0, 0<=h<=3. For Hdot^-1 they are q=0,0<=h<=5 and q=1,h=0,1. A collision between the two q rows would require an integer multiple of delta to equal2; direct comparison of delta with the relevant fractions excludes it. The rational value of delta is fixed, so no approximate cancellation is used.

The unweighted first derivative is O(r^(e-1)), the weighted second derivative O(r^(e-6/5)) and the weighted third derivative O(r^(e-11/5)). Their respective sufficient power thresholds are e<0, e<1/5 and e<6/5. Thus, once F is in L2, each is integrable in the stated differentiable finite-generator class. Smoothness gives integrability on bounded sets. Conversely, E_* includes the L2 component. This proves the first equivalence after listing the exponents.

The exact c gives 0.5523<gamma<0.5524 and 0.4476<delta<0.4477. Consequently gamma-h delta is at least -1 precisely for h=0,1,2,3, while every q>=1 gives exponent at most gamma-2<-1. Remove the automatic (0,0) sector to obtain the three claimed cancellations.

For the homogeneous negative norm, fix a positive odd sine frequency n. The radial Poisson equation for a forcing r^e sin(n theta) has a particular solution proportional to r^(e+2), except at e+2=+/-n, where a logarithmic factor occurs. Its gradient energy at infinity has radial scale integral r^(2e+3)dr, so the threshold is e<-2. At e=-2 the integral diverges logarithmically. At the resonances, direct solution with the logarithm gives the same strict membership threshold; none of the offending exponents listed here is resonant. The possible homogeneous harmonic additions do not cancel a nonzero forcing at another power. Equivalently, the independently audited modewise Green formula gives the same criterion. Since the profiles are centrally odd, there is no angular zero mode and hence no extra total-mass condition.

For q=0, gamma-h delta>=-2 holds for h=0,...,5; for q=1 it holds only for h=0,1; for q>=2 it never holds. Exact cancellation of these finitely many sectors leaves a positive decay gap below -2. The convergent expansion and its differentiated version then bound the remainder and its Poisson gradient, proving sufficiency. This establishes the negative-norm contract.

## Scope and dependencies

The argument uses the exact fixed exponent and differentiable convergent finite-generator expansion. It is not a statement about arbitrary formal asymptotic series. Fractional norm bounds require the separately proved interpolation comparison with E_* and the weighted third derivative. A membership certificate does not prove smallness, any inverse estimate, a background matrix bound or a nonlinear solution.

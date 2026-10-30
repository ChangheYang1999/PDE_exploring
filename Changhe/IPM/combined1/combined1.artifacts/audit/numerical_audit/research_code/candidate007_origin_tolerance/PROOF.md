# Exact axis Taylor coefficient of candidate007 and the uniform tolerance claim

## Statement

Let chi be the exact canonical potential of C1-N1-007-d2w-j7-e2bal, raw SHA256 ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21 and c=4076476460239181/2251799813685248. On the whole plane define rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy), F=(cX+u).grad rho-rho. Parity gives an analytic quotient R_f=F/y near the origin. Taylor coefficients have no factorial scaling. The finite exact computation below proves

 2.0899e-11 < [y^4] R_f(0,y) < 2.0900e-11,
 [1] R_f(0,y)=0.

In particular the saved candidate's five degree-two and degree-four Taylor equations do not all have absolute residual at most2e-13. This refutes the universal saved-candidate assertion in line54 of the frozen NUMERICS_FINAL_1702.md, not the independently accepted exact center or far-field equations. It also independently checks the already disclosed section1 coefficient. The optimizer's earlier floating projections need not equal the final exactly pivoted candidate. No tolerance statement about those earlier projections is inferred.

## Exact finite proof

Write z=x^2+y^2, gamma=1/c, lambda=1-gamma and p_j=(3+gamma-j lambda)/2. A saved Legendre generator has potential a H_m t^w P_n(2t-1)(1+z)^(p_j-m), where t=z/(1+z) and H_m=Re(x+iy)^(2m). Its shifted Legendre coefficients are integers (-1)^(n-h) binom(n,h) binom(n+h,h). Thus its degree-eight Taylor polynomial is the sum over h and ell>=0 with m+w+h+ell<=4 of

 a (-1)^(n-h) binom(n,h) binom(n+h,h)
   binom(p_j-m-w-h,ell) H_m z^(w+h+ell).

For a monomial generator use its one saved radial power. Rational binomial coefficients are obtained by the finite product recurrence. All discarded potential terms have even degree at least ten. Three derivatives give density and velocity terms of degree at least seven; their product in u.grad rho has degree at least seven because rho and u start at degree one. They cannot affect F through degree five. No infinite-series numerical remainder is needed for this finite jet.

For each term v H_m z^s put d=m+s. Its x^0 y^(2d) coefficient is (-1)^m v. Its x^2 y^(2d-2) coefficient is (-1)^m(s-m(2m-1))v. This follows by selecting either the x^2 coefficient of H_m or that of z^s. Aggregate these exact sums as A_d and B_(d-1), respectively, so chi(0,y)=sum A_d y^(2d), and [x^2]chi=sum B_d y^(2d). Only d<=4 is needed.

At x=0, parity gives rho_x=0 and u_x=0. If r_j=[y^j]rho(0,y) and v_j=[y^j]u_y(0,y), then for odd j=1,3,5,

 r_j=-(j+3)(j+2)(j+1) A_((j+3)/2)-2(j+1)B_((j+1)/2),
 v_j=2(j+1)B_((j+1)/2).

Hence for k=1,3,5 the exact residual coefficient is

 [y^k]F=(ck-1)r_k+sum_(p,q odd positive,p+q-1=k) v_p q r_q.

This axis computation is independent of the peer's general bivariate polynomial multiplication. The checker computes every A and B directly from all saved rational generator records, then all displayed r,v,F values. It verifies the zero constant and the two strict rational bounds. Since [y^4]R_f=[y^5]F, the coefficient exceeds2e-13, which contradicts an asserted upper tolerance of2e-13 for every saved candidate. The displayed floating approximations are not used in that contradiction.

## Evidence and scope

The proof precedes its checker. Freeze the raw-source identity, report, N1 referee proof/program/output as inert text and accepted N4-090 structural record. Register every input hash. The own implementation uses exact flint rationals and independent axis coefficient formulas, without importing or executing peer code. Read the peer's scope and equation convention before comparing. Store all exact A,B,r,v,F coefficients in JSON and verify source stability at the end. Whole-plane source identities and analytic parity are explicit premises. This finite statement supplies no exact stationary solution, no origin tolerance uniform in a basis, and no change to the existing sufficient-framework exclusions.

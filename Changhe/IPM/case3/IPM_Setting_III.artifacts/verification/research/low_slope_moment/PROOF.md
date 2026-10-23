# Consequences of a small third angular moment

Status: independent proof complete. Date: 2026-10-20.

## Statement and notation

For an exact smooth primary profile put a=rho_y(0)!=0, D=ell-1>0, A=2ell-1. Let

    rho3(r)=(1/pi) int_0^(2pi) rho(r cos theta,r sin theta) sin(3theta) dtheta,
    J=int_0^infty rho3(r) r^(-2) dr.

The canonical strain identity and exact center relation give J=a/4-D. Then:

1. If 0<a<=A-1, int_0^infty (rho3)_- r^(-2) dr >= (A-1)/4, where f_-=max(-f,0).
2. If a>0 and |J|<=epsilon a/4 with 0<=epsilon<1, then a>=2(A-1)/(1+epsilon).
3. If |J|<=kappa|a| with 0<=kappa<1/4, then a>0 and 4D/(1+4kappa)<=a<=4D/(1-4kappa).

These statements add moment hypotheses or a slope range; they do not exclude the full primary class.

## Convergence and proof

Smooth parity and the a y leading term imply rho3=O(r^3) near zero, because the first sine mode is orthogonal to sin(3theta). At infinity the stated sublinear bound gives rho3=O(r^gamma), gamma<1. Thus the radial integral defining J is absolutely convergent, as are its positive and negative parts. This is absolute convergence after angular projection; the original unregularized two-dimensional strain kernel need not be absolutely integrable near the origin.

For (1), a<=A-1=2D gives J=a/4-D<=-D/2. Writing J=Jplus-Jminus with both terms nonnegative gives Jminus>=-J>=D/2=(A-1)/4.

For (2), J>=-epsilon a/4 implies D<=a(1+epsilon)/4. Since 4D=2(A-1), this is the claimed lower bound.

For (3), if a<0 then |J|=D+|a|/4>kappa|a|, a contradiction. For a>0, |a/4-D|<=kappa a is equivalent to a(1/4-kappa)<=D<=a(1/4+kappa). Both factors are positive, so division proves the two bounds. The case kappa=0 is included and forces a=4D.

## Dependencies and scope

Only the independently established canonical strain identity, exact center relation, parity and the advertised growth bound are used. The quantities a,D,J and the inequalities are invariant under the remaining spatial scaling. This verifies the lead's LOWSLOPE2(a-c), with the angular normalization and radial absolute convergence explicitly fixed.

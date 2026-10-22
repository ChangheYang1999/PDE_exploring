# Canonical strain contribution at the trial source

Topic90. Written before computation. The intended conclusion is a scalar enclosure only; its numerical and provenance checks are pending.

Let rho_X be the exactly reconstructed original stored X3 and rho_T the exact normalized modal_v2 trial from topic15. Both have the canonical whole-plane velocity, the required parity and sufficient sublinear growth. Let sigma[f]=psi[f]_xy(0) denote raw canonical strain, with -Delta psi[f]=f_x and U[f]=(-psi[f]_y,psi[f]_x). The prompt functional is c[f]=sigma[f]/3. Fix the same exact dyadic k used by these two data sets. Topic15 proves sigma[rho_T]=3/k-1. The independently audited original-X3 scalar certificate gives

 3/k-1-sigma[rho_X] in [103009/10^13, 51507/5*10^12].

For clarity the intended decimal endpoints are 0.0000000103009 and 0.0000000103014; code uses these decimal strings as exact rationals. In the fractional notation above the second endpoint means 51507/(5*10^12). The full original scalar archive remains a dependency, and its lack of a second independent rigorous whole-integral summation remains disclosed.

The canonical inverse is linear: the difference of the two stream functions solves the difference Poisson equation, has the same parity and sublinear velocity, and hence agrees with the canonical inverse of the difference by its uniqueness theorem. Thus for h=rho_X-rho_T,

 sigma[h] in [-0.0000000103014,-0.0000000103009].

Let P=(p,0) be the exact equilibrium of the trial's V from topic89. That certificate gives

 a=4841405518533377/562949953421312 < p
 < b=4841405518533711/562949953421312.

With d0=0.0000000103009 and d1=0.0000000103014, all a,b,d0,d1 are positive. Multiplication is monotone in the positive rectangle, so

 -b*d1/3 <= p*sigma[h]/3 <= -a*d0/3.

Exact rational comparison, independently directed Arb multiplication and independently grouped mpmath.iv multiplication will check that this interval lies strictly inside

 [-0.0000000295309,-0.0000000295294].

This quantity is only the strain part of W[h]_1(P)=U_1[h](P)+p*sigma[h]/3. No bound on U_1[h](P) follows from it. In particular its absolute value exceeding 2.2e-8 does not put h outside a ball restricting the sum W[h]_1(P): cancellation is possible. Choosing the unconstrained velocity contribution to be the negative strain term illustrates the logical gap without asserting that the actual h realizes that choice. This calculation neither places X3 in the topic76 exclusion neighborhood nor excludes it from that neighborhood, and is no decisive endpoint.

Dependencies: canonical uniqueness and original scalar theorem in research/canonical_inverse; exact normalization in research/modal_repair; the actual root in research/source_instance. Recheck all their pinned data and conclusions before accepting this result. No new whole-plane integral is claimed.

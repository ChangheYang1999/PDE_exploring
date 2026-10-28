# A larger source neighborhood for zero exclusion

## Exact statement and certificate condition

Let rho be the normalized exact-join modal density from proof 04 and
V=ell X+U[rho]. Proof 15 proves a unique source P=(p,0) in the exact
axis bracket [p_-,p_+] recorded there, with

    DV(P)=diag(A_P,mu_P), A_P>10, mu_P>0.99999997745.

Set h=1/2 and

    Q=[p_- - h,p_+ + h] times [-h,h],
    R_Q=sqrt((h+p_+-p_-)^2+h^2).

Suppose a verified number M bounds the Frobenius norm of the third
derivative tensor of the stream function throughout Q. Since
U=(-psi_y,psi_x), it also bounds the Euclidean tensor norm of D^2V.
If

    M R_Q < 0.99999997745,                                (1)

then P is the only zero of V in Q. More strongly, the symmetric part
of DV throughout Q is bounded below by
(0.99999997745-M R_Q) times the identity.

This statement supplies a patch for a global nonzero-field certificate
that omits a small group of boxes near P. Every omitted box must be
proved to lie in Q. No global zero count follows without nonzero-field
bounds outside Q and appropriate treatment of the origin.

## Proof

The box Q is convex and contains P. The segment joining any X in Q to
P remains in Q and has length at most R_Q. Integrating D^2V along this
segment gives

    ||DV(X)-DV(P)||_op<=M |X-P|<=M R_Q.

The same estimate bounds the symmetric-part perturbation. Since the
smallest eigenvalue of DV(P) exceeds0.99999997745, (1) proves the
claimed positive lower bound for S(DV). For X distinct from P,

    (V(X)-V(P)).(X-P)
      =integral_0^1 (X-P)^T DV(P+t(X-P))(X-P)dt >0.

Thus V(X) cannot equal V(P)=0. This proves uniqueness throughout Q,
including its boundary, without an interval Newton iteration.

## Cover and independent computation

The positive-y half of Q lies in the polar rectangle

 log(p_- - h)<=t<=log(sqrt((p_+ + h)^2+h^2)),
 0<=theta<=atan(h/(p_- - h)).

Reflection across y=0 preserves the relevant tensor norm. The own-code
Green reconstruction and derivative expansion of proof 19 is reused
with this larger explicit rectangle. Its input is read directly from
the original NPZ, and its source bracket is the exact rational one
from proof 15. All radial spline spans meeting the rectangle and all
angular subdivisions must be covered. Each component of D^3psi is
enclosed on each box by a finite Taylor expansion and its analytic
remainder. The tensor norm bound is

    sqrt(|psi_xxx|^2+3|psi_xxy|^2
                         +3|psi_xyy|^2+|psi_yyy|^2).

The numerical output requires a separate audit of input identity,
coverage, outward aggregation and (1). Until that audit succeeds,
only the conditional statement above is established.

## Dependencies and current scope

Dependencies are the source bracket and rates of proof 15, the exact
modal density and its scalar normalization from proof 04, and the
explicit derivative/Green formulas of proof 19. No global (Z), inverse
or nonlinear result is asserted by this topic alone.

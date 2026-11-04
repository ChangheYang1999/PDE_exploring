# Exact Euler coupling in volume coordinates

## Statement

Let 0<c<1/2, omega be real, a=1-2c and kappa=1+c. Let V be a smooth three-manifold with volume form mu, and let B0,W0 be C1 vector fields satisfying

    div_mu B0=3c, div_mu W0=0, [B0,W0]=-kappa W0.

Let F:V->R3 be a C2 embedding and Q a C1 real function. Set alpha0=i_W0 i_B0 mu. Suppose

    F^*vol=mu,
    alpha0=a[sum_i (B0 F_i)dF_i+omega(F1 dF2-F2 dF1)]+dQ.   (1)

Then on the open image O=F(V), the fields B=F_*B0, W=F_*W0, U=B-(cI-omega J)y and

    H composed F=Q+(ac/2)|F|^2,
    P=H-|U|^2/2-((cI-omega J)y).U

satisfy curl U=W, div U=0 and the full rotating profile equation with a single-valued C1 pressure P.

Conversely, if a profile is conjugate to (B0,W0,mu) by such a volume-preserving C2 F, then (1) holds with Q=H composed F-(ac/2)|F|^2.

An embedding of a three-manifold without boundary into R3 has open image by the inverse-function theorem; if a domain with boundary is used, the statement concerns its interior. No existence of F or Q is asserted.

## Proof

The divergence and bracket hypotheses give, by Cartan's identity,

    d alpha0=(kappa-3c)i_W0 mu=a i_W0 mu.                  (2)

The sign can also be checked in Euclidean coordinates: curl(B cross W)=(W.grad)B-(B.grad)W-W div B=(kappa-3c)W.

Let beta=F^*(U.dy). Since B composed F has components B0 F_i,

    beta=sum_i(B0 F_i)dF_i-(c/2)d|F|^2
         +omega(F1 dF2-F2 dF1).

Thus (1) is exactly

    alpha0=a beta+d(H composed F).                       (3)

The right side has the classical derivative needed below: alpha0 and beta are C1, so the asserted first derivatives of H composed F are C1, upgrading H to C2 locally. Alternatively (3) can be differentiated distributionally first. Taking its exterior derivative and using (2) gives d beta=i_W0 mu. Volume preservation makes this equivalent to curl U=W on O. It also gives div B=3c, and hence div U=0.

Push (3) to O. It is the reduced Lamb identity

    a U+grad H=B cross W.

Insert W=curl U and H=P+|U|^2/2+((cI-omega J)y).U. The elementary identities

    (curl U) cross U=(U.grad)U-grad(|U|^2/2),
    (curl U) cross Ay=(Ay.grad)U-(DU)^T Ay,
    grad((Ay).U)=A^T U+(DU)^T Ay

with A=cI-omega J reduce the Lamb identity exactly to

    (1-c)U+(Ay+U).grad U+omega JU+grad P=0.

All functions are globally single-valued on O because F is injective and Q is a real function. This proves sufficiency. For necessity, start from this Lamb identity, pull it back by the given conjugacy and substitute the displayed beta. Rearranging gives (1) and the stated Q. No simple-connectivity assumption is needed: the globally defined Q explicitly carries the period condition.

## Scope

This confirms the precise equivalence in Theory Agent C C26. It is a reformulation of the coupled PDE and volume condition, not a solvability theorem, an elliptic estimate, or an assertion that an arbitrary bracket model admits such coordinates. The unrelated principal-symbol and construction comments in Remark5.7 are not part of this verdict.

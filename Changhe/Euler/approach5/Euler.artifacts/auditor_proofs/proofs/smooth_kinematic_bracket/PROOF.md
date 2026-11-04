# Smooth independent eigenfield with compactly supported velocity

## Statement

For every 0<c<1/2 and every finite real omega, there exist U,W in C-infinity(R3;R3) such that U is compactly supported, div U=div W=0, W is not identically zero, and, with B=(cI-omega J)y+U,

    [B,W]=-(1+c)W,       |W(y)|=O(|y|^(-1/c)).

The compact trapping handlebody and expanding Lorenz-type return quotient of A066 are preserved. The field W is nowhere zero near that handlebody. Globally W vanishes exactly on two smooth proper lines and is flat along them. The two new equilibria in the filling handles are nonhyperbolic.

The field W is independent of curl U and is not equal to it. No pressure satisfying the Euler momentum equation is constructed. This is a smooth counterexample to a decoupled kinematic exclusion, not an Euler profile counterexample. No mixing or transitivity classification of the trapping set is asserted.

## Inputs from A066

The complete construction and its differential-topology checks are in the team records. Set X=-B, a=1+c, d=3c and k=a-d=1-2c>0. The already confirmed A066 gives:

1. A smooth genus-two handlebody H with X strictly inward on its boundary, a positive smooth volume form mu satisfying L_X mu=-d mu, and a smooth nowhere-zero W0 near H with [X,W0]=aW0. The local return quotient is uniformly expanding.
2. Two disjoint annuli on the boundary, chosen in the cancelling 1/2-handle isotopy classes. Attaching two solid 2-handles along them and rounding the incoming corners gives a ball N.
3. A relative volume correction on N and a boundary flow-collar identification that send mu to Euclidean volume and make B equal to (cI-omega J)y near the boundary. The correction is the identity in that collar. Extending by the same linear field produces U compactly supported and divergence-free.

Only the fields inside the two filling handles change below. The attaching isotopy classes, original H, return maps and relative-volume argument are unchanged. No hyperbolicity of the added equilibria is required by any of these inputs.

## The new filling field and flux match

On D={u in R2: |u|<=1} times [-1,1], put r=|u| and choose any epsilon>0. Define

    X_u=epsilon r^2 u,
    X_v=-(d+4epsilon r^2)v,
    mu_D=kappa du_1 wedge du_2 wedge dv.

This polynomial field has divergence -d. It points out on r=1 and in on v=+1 and v=-1. It has one zero, at the origin, with derivative diag(0,0,-d). Its index is -1: the homotopy replacing epsilon r^2 u by epsilon(r^2+s)u has no other zero and, for s>0, determinant -epsilon^2 s^2 d<0 at the zero.

The outgoing side flux is kappa epsilon dtheta wedge dv. If M is the incoming flux of its attaching annulus, choose kappa=M/(4pi epsilon). The cumulative-coordinate area map from A066 identifies these positive flux forms and remains in the same attaching isotopy class. Extend this map along the two X flows. In flow coordinates both volume forms are exp(-dt)dt wedge nu and X=partial_t. Thus X and mu match on an open collar, to every derivative order. Equality with the old linear handle formula at the side is unnecessary; the collar coordinates identify the actual new flow. Use a short collar time less than 1/(2epsilon), so the new polynomial flow exists throughout it.

## Exact transport into the handle

For r>0, the flow and the exit data at r=1 are

    r(t)=r(1-2epsilon r^2 t)^(-1/2),
    v(t)=v exp(-dt)(1-2epsilon r^2 t)^2,
    tau=(r^(-2)-1)/(2epsilon),
    z=v r^4 exp(-d tau).

Let G_r(theta,z), G_theta(theta,z), G_v(theta,z) be the smooth side values transported from W0, in the orthonormal radial, angular and vertical frame. The unique transported field is

    W=exp(-a tau) (DF_tau)^(-1) G,

where the derivative is taken at fixed time and only then evaluated at tau. At exit its radial and angular diagonal entries are r^(-3) and r^(-1), its vertical entry is exp(-d tau)r^4, and its radial-to-vertical entry is -8epsilon tau v r^3 exp(-d tau). Inverting this triangular matrix gives

    W_r=exp(-a tau) r^3 G_r(theta,z),
    W_theta=exp(-a tau) r G_theta(theta,z),
    W_v=exp(-k tau) r^(-4) G_v(theta,z)
          +4v(1-r^2)exp(-a tau) G_r(theta,z).             (1)

The factor 4(1-r^2) follows from 8epsilon tau r^2=4(1-r^2). This computation also checks the full normal component, not only section-tangent transport.

## Smooth extension through the axis

For each finite Cartesian derivative order, every term obtained from (1) is a bounded smooth side-data derivative times a finite power of r or r^(-1), an angular trigonometric factor, a bounded power of v, and at least one of exp(-a tau), exp(-k tau). Derivatives of z introduce further powers of r^(-1) and the factor exp(-d tau); they remain bounded on a fixed enlarged v interval. Since a,k,d>0 and tau=(r^(-2)-1)/(2epsilon), these exponential factors dominate every inverse power of r.

Thus, uniformly for v in a compact interval, every derivative of W tends to zero faster than every power of r. Set W=0 on the axis. This defines a smooth flat extension: inductively, the difference quotient of any extended derivative at an axis point is bounded by C_N r^N divided by the displacement magnitude, and r is no larger than that magnitude. Taking N>1 makes the quotient tend to zero. Continuity and differentiability of every order follow. The bracket identity extends to the axis by continuity.

## Global matching, caps and corner rounding

Let O be the interior of H, which is forward invariant. Any point p whose forward X orbit enters O has a neighborhood on which one fixed time t has F_t(p) in O. Define there

    W(p)=exp(-at) (DF_t(p))^(-1) W0(F_t(p)).

The bracket law for W0 and the flow chain rule show that this is independent of the chosen later time. Hence it is smooth on the entire basin of O. It agrees with all collar and side formulas to every order, including (1).

Every handle point off its axis exits to O in finite time. The only points missing from this basin are the two axes and their backward continuations. At a cap-center point, or at a point further along such a continuation, choose a fixed forward time carrying it to the interior of the corresponding handle axis. The displayed fixed-time pullback transports the smooth flat extension there to a smooth flat extension near the original point. This proves regularity across caps and along the entire exceptional lines, not merely inside D.

For explicit corner control, use side-flow coordinates (t,theta,z), with t=0 at r=1. Near the upper cap, its equation is z=g(t), t<=0, where

    g(t)=(1-2epsilon t)^(-2)exp(dt),
    g'(t)/g(t)=d+4epsilon/(1-2epsilon t)>0.

The incoming defining functions are -t and z-g(t), with strictly negative X derivatives. A smooth minimum or maximum, as appropriate for the local union or intersection, is chosen with nonnegative partial derivatives summing to one. Its X derivative remains strictly negative. This rounds the corners by changing only the domain. The fields and volume form are already smooth on an enlarged collar and are unchanged. All rounded pieces still flow into O.

The two axes continue to infinity under the exterior flow and are smooth proper embedded lines. There are no further zeros of W, because all other points transport by an invertible derivative from the nowhere-zero W0. The flatness result is preserved by the smooth coordinate and volume corrections.

## Euclidean extension and divergence

Apply the unchanged relative-volume construction of A066. It gives a smooth Euclidean B, equal to (cI-omega J)y outside a ball. The exterior transport is

    y=R exp(cs) exp(-omega Js)theta,
    W(y)=exp(-s)exp(-omega Js)W(Rtheta),

so W is smooth and O(|y|^(-1/c)). It agrees with the interior on an open collar. The B flow is complete and every backward orbit is bounded.

The bracket law and constant div B imply, by transforming divergence under the flow,

    div W(Phi_s p)=exp(-(1+c)s)div W(p).

The left side remains bounded as s tends to minus infinity along its compact backward orbit. Therefore div W(p)=0 everywhere. This argument needs only C1 regularity of W, which has already been exceeded.

The set {W!=0} is nonempty, open and invariant. It has infinite volume, since the Jacobian of Phi_s is exp(3cs) and a finite positive invariant volume would contradict this factor. Since curl U is compactly supported, W cannot equal curl U.

## Verification and scope

The coordinator's independent model cross-check is in the team records. Its flow-collar, cap-continuation and rounding arguments have been checked above. The accompanying symbolic script is supplementary; this proof uses exact formulas and no numerical flatness test. The earlier A066 topology and relative-volume proof remain explicit dependencies.

This construction upgrades the independent eigenfield from arbitrary finite Cj to C-infinity. It does not give an analytic example, does not retain hyperbolicity at the two filling zeros, and does not resolve the Euler curl coupling.

## Repeated audit, 2026-11-02T21:25:03Z

The original 2-handle filling and the smooth replacement were read again together with the source construction. The return footprints have positive separation at equal target x, the flux identity is b K rho=L exp(-dT), and the stable-vector identity is D P(partial_y)=exp(-aT) partial_y. The increasing tube cross-sections are needed for strict inward lateral boundaries. The two attaching curves may be chosen as the standard disjoint cancelling curves for the abstract genus-two handlebody; subsequent annular flux reparametrizations are isotopic to those choices. The relative-volume correction is supported away from the outer collar and cannot disturb the prescribed exterior linear flow.

The polynomial smooth handle has eigenvalues (0,0,-d) for X at its added zero. Consequently the smooth example cannot be cited as an example with all equilibria hyperbolic. The finite-Cj linear-handle version has hyperbolic filling zeros, but does not assert one globally smooth W for that fixed linear filling. No new gap was found in the stated A066/A121 constructions. The return quotient is expanding, but transitivity, mixing and a classification of the full maximal invariant set are not included in this conclusion.

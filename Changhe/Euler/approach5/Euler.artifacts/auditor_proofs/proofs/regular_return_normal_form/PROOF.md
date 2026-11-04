# Exact local return data for a regular bracket eigenfield

## Statement and scope

Let 0<c<1/2, b=1+c, a=1-2c, d=3c=b-a. Let X be a C2 vector field and W a C1 field on an open three-dimensional region with Euclidean volume form m, satisfying

    div X=-d,    [X,W]=b W,    div W=0.

Assume X and W are nonzero and independent where the following sections and flow segments are used. Write Psi_t for the X flow. In the Euler application X=-B and W=curl U. The local result does not require that curl coupling.

At any periodic orbit of period T in this region, the transverse multipliers are exp(-bT) and exp(aT), both positive. On suitable local sections tangent to W and transverse to X, every positive-time return branch has coordinates

    P(u,v)=(F(u),F'(u)^(-b/a) v+G(u)),
    tau(u)=a^-1 log F'(u),    F'(u)>1.                 (1)

There is an exact smooth local seam construction for every pair of smooth F,G with F'>1. This is not a global regular-attractor construction.

## Periodic multipliers and the retained cat-map obstruction

The bracket equation gives

    D Psi_t W=exp(-bt) W composed with Psi_t.

At a point of period T, W is a transverse eigenvector of multiplier exp(-bT). The flow direction has multiplier one; constant divergence gives determinant exp(-dT). The remaining multiplier is exp((b-d)T)=exp(aT).

Positive time changes preserve the return map on a fixed transverse section. Smooth coordinate changes conjugate its derivative. A change of smooth positive section density multiplies its Jacobian by an endpoint ratio, which cancels around each periodic orbit. These operations therefore cannot change either periodic multiplier or their product.

For the toral map A0=[[2,1],[1,1]], the points p=(1/5,2/5) and q=(4/5,3/5) form a two-cycle modulo integers. The derivative over that cycle is A0^2=[[5,3],[3,2]], of determinant one. Any proposed return map agreeing with A0 near these points and retaining this orbit has periodic determinant one. It cannot satisfy the required exp(-dT)<1 after a time change, conjugacy or density correction. Retention of that particular orbit is an explicit hypothesis. A modification changing all relevant periodic derivatives is not excluded.

## Section coordinates and exact map

Put beta=i_W m and theta=i_W i_X m. Cartan's formula gives

    d theta=-a beta,
    Psi_t^* theta=exp(at)theta,
    Psi_t^* beta=exp(at)beta.

Theta annihilates exactly span(X,W). Sweep a short transverse curve by the local W flow to obtain a C1 section Sigma tangent to W and transverse to X. On Sigma the flux form sigma=(i_X m)|Sigma is nonzero. The W flow preserves its coefficient: it preserves m, and pushes X to X plus a multiple of W, which vanishes upon evaluation against the W tangent direction. Thus coordinates can be chosen with

    W=partial_v,    sigma=dv wedge du,    theta|Sigma=du.

This construction uses the C1 flow and the coefficient along the original transverse curve, so it does not require second derivatives of W or of the resulting section.

Let P(z)=Psi_tau(z) z map one such section to another. Differentiation gives

    DP W=exp(-b tau) W(Pz)+X(Pz) d tau(W).

The first two terms are tangent to the target section, whereas X is transverse. Hence d tau(W)=0 and DP W=exp(-b tau)W(Pz). Therefore tau=tau(u) and

    P(u,v)=(F(u),exp(-b tau(u))v+G(u)).

Pulling back the target flux form gives P^*sigma=exp(-d tau)sigma. Terms from differentiating the return time repeat X in the volume determinant and vanish. Consequently

    exp(-b tau)F'=exp(-d tau),

so F'=exp(a tau). This proves (1), including orientation and positivity. These are local branches; no global return section is assumed.

## Exact seam verification

Given smooth F,G with F'>1, put tau=a^-1 log F' and q=exp(-b tau). In coordinates (u,v,t), take

    X=partial_t,    B=-partial_t,
    W=exp(bt)partial_v,
    m=exp(-dt) dt wedge dv wedge du.

Then div_m B=d, div_m W=0 and [B,W]=-bW. The transition

    H(u,v,t)=(F(u),q(u)v+G(u),t-tau(u))

preserves B and W. For the volume form,

    H^*m=exp(-d(t-tau))qF' dt wedge dv wedge du=m,

because qF'=exp(-d tau); the other differentiated terms contain a repeated du. Thus the fields and the volume agree exactly across this local seam. The coordinate r=-exp(-dt)/d makes m=dr wedge dv wedge du locally, so the volume can be put in Euclidean form.

This does not produce compatible global domains, a knot-exterior embedding, the exterior dynamics, a global field W, or a compactly supported U. None of those missing steps is supplied by the local seam.

## Basin observation and dependencies

If a complete X flow has a compact regular attractor Lambda with W nowhere zero on it, then X,W stay nonzero and independent throughout its basin. Their zero sets are invariant. Parallelism W(x)=kX(x) would imply W(Psi_t x)=k exp(bt)X(Psi_t x), contradicting bounded W and a positive lower bound on |X| near Lambda unless k=0, which is also impossible.

Even div W=0 follows on this basin if only the bracket and constant divergence are initially given: taking exterior derivatives of Psi_t^*(i_W m)=exp(at)i_W m yields

    div W(Psi_t x)=exp(bt)div W(x).

The left side remains bounded near Lambda. This argument uses only C1 W. If the complete W flow is available, its commutation with Psi also makes the basin W-flow invariant. These observations do not extend a field across the basin boundary.

The proof independently reconstructs the completed regular_kinematic review in the coordinator agent. No DA existence or rigidity theorem, and no bibliographic assertion, is needed. The global realizability question remains open.

Audit written: 2026-11-02T20:43:26Z

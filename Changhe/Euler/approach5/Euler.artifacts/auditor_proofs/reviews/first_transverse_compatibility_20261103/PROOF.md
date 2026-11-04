# First normal compatibility and a separate rank obstruction

Status: CONFIRMED as a C2 characteristic identity and exact compatible scalar data, A749-A750. The separate rank corollary is included in the stronger C1 A751. No velocity realization of the scalar data is asserted.

## 1. Exact hypotheses

Use a genuine Euclidean circular collar with coordinates

    x=((R+h)cos(theta),-(R+h)sin(theta),z),
    r=R+h>0, metric=r^2 dtheta^2+dh^2+dz^2,
    oriented volume=r dtheta dh dz.

Let U be C2 and P be C1 on a neighborhood of S1 times I times{0}, with div U=0, U.curl U=0, and the rotating Euler profile equation. Put A=cI-omega J, B=Ax+U, W=curl U, kappa=1+c and a=1-2c. Here c>0 and omega is any finite real number. Assume the central traces

    U=u(h) partial_h, W=w(theta,h) partial_theta, u(h)!=0,

where u is C2, w is C1 and periodic in theta. Set

    b=cr+u, t=3c-b'-b/r,
    L=omega partial_theta+b partial_h,
    v(theta,h)=partial_z W^theta(theta,h,0).

Then v is continuous and, along every local central characteristic, obeys

    Lw+kappa w=0,
    Lv+(t+kappa)v=r w w_h.                           (1)

The second equation is a characteristic differential or integral identity. No C3 velocity, second spatial derivative of W, global completeness, decay or pressure normalization is assumed. The pressure equation upgrades P to C2, so all uses of the Lamb identity below are classical.

## 2. Proof at C2 regularity

For contravariant vector components, the coordinate curl is

    W^theta=(partial_h U^z-partial_z U^h)/r,
    W^h=(partial_z(r^2 U^theta)-partial_theta U^z)/r,
    W^z=(partial_theta U^h-partial_h(r^2 U^theta))/r.

The central traces give B=(omega,b,0), partial_z B^theta=0, partial_z B^h=-r w. The divergence of B is3c, so partial_z B^z=t. The surface z=0 is locally B-invariant by uniqueness of the C1 flow. Differentiating helicity once in z gives u partial_z W^h=0: the only other possible central term, r^2 partial_z U^theta W^theta, vanishes. Thus partial_z W^h=0. The divergence of W gives partial_z W^z=-w_theta. These formulas leave v free at this stage. The central theta component of [B,W]+kappa W=0 gives the first equation in(1).

Here is the low-regularity argument for differentiating the bracket law. For the local forward B flow Phi_s the exact Cauchy identity is

    W(Phi_s x)=exp(-kappa s)D Phi_s(x)W(x).

The C2 field B has a C2 flow in its initial point, and both first and second spatial derivatives of Phi_s are continuously differentiable in s. This follows directly by differentiating the flow integral equation once and twice; their right sides contain only continuous DB and D2B. Differentiating the displayed identity in x and solving for DW(Phi_s x) using the invertible D Phi_s proves that DW(Phi_s x) is C1 in s. With M=DB and D=DW in this coordinate chart, its equation is

    dD/ds=M D-D M-kappa D+(W.partial)M.             (2)

The Hessian term is continuous and uses symmetry of the second partial derivatives of B. This derivation uses no spatial derivative of DW. Coordinate vector components satisfy the ordinary bracket formula, so no additional connection term belongs in(2).

The entire theta row of M vanishes on z=0. In the theta-z entry of -DM, only the h and z columns contribute, giving r w w_h-t v. The theta-z entry of (W.partial)M is w partial_theta partial_z B^theta=0, since B is C2 and its central partial_z B^theta vanishes identically. Equation(2) therefore gives the second equation of(1).

Precisely, for theta_s'=omega and h_s'=b(h_s), let

    E(s)=exp(integral_0^s(t(h_q)+kappa)dq).

Then E(s)v(theta_s,h_s) equals its value at0 plus integral_0^s E(q)r(h_q)w(theta_q,h_q)w_h(theta_q,h_q)dq. This also establishes the equation across any local angular-chart overlap. No long-time characteristic assertion is needed.

## 3. Exact scalar data satisfying this one equation

Let2/5<c<1/2, -kappa<rho<=-2a, and omega!=0. Put

    p=-kappa/rho>1, beta=-omega/rho,
    u=-cr+rho h, b=rho h,
    phase=theta+beta log h, w=h^p f(phase), h>0,

where f is any nonzero C2 periodic function. On a sufficiently small interval about0, u is nonzero. Since L phase=0 and rho p=-kappa, the first equation of(1) holds. Now t=3c-rho-rho h/r. On writing v=r k the second equation becomes

    Lk+(kappa+3c-rho)k=w w_h.

The right side is h^(2p-1)[p f^2+beta f f'] and has L-eigenvalue rho(2p-1). Its total coefficient in this equation is

    rho(2p-1)+kappa+3c-rho=-a-2rho>=3a>0.

Consequently

    v=r w w_h/(-a-2rho)                              (3)

is an exact solution of this scalar equation. Extend w and v by zero to h<=0. Their sizes and first h derivatives have respective bounds O(h^p),O(h^(p-1)) and O(h^(2p-1)),O(h^(2p-2)); angular derivatives also vanish at h=0. Since p>1 and f is C2, both extended scalar functions are C1 and flat to first order there. Equations(1) hold through h=0, where the characteristic remains on h=0.

This is not a construction of a velocity realizing(w,v). The analytic LIT116 reconstruction fixed v=0 and therefore had first normal residual-r w w_h. Formula(3) proves only that this one scalar normal equation is solvable when v is allowed to vary. Other normal equations and the rank identity have not been imposed in this construction.

## 4. An additional restricted consequence of the rank identity

Assume now c>0, c!=1/2 and, in addition to Section1, the rank identity

    dH wedge dg=0 on the central vortical set,
    H=P+|U|^2/2+(Ax).U, g=U.B.                      (4)

This is a separate hypothesis. It is supplied for the appropriate global helicity-free class by A413, but is not inferred here from local helicity alone. The Lamb identity grad H=-aU+B cross W and the oriented metric give on z=0

    H_theta=0, H_h=-a u, H_z=-r b w,
    g=u b, g_h=u'b+u b',
    g_z=-r w(b+u).

The last identity uses the already proved partial_z U^theta=0, partial_z U^h=-r w, and the vanishing central U^z,B^z. The dh wedge dz coefficient in(4) is

    r w F(h),
    F(h)=b(u'b+u b')+a u(b+u).                     (5)

Hence w(theta,h) F(h)=0 at every point: at a vortical point this follows from(4), and otherwise w=0.

If b(h0)=0, the nonzero-velocity assumption gives u(h0)=-c(R+h0)!=0. Thus

    F(h0)=a u(h0)^2!=0.

By continuity F remains nonzero on a neighborhood of h0. Equation(5) forces w=0 throughout that central neighborhood. Therefore the exact circular central trace of Section1, with constant angular carrier speed and purely radial velocity u(h), cannot support vortical points accumulating on a root of b when the rank identity holds. In particular the nonzero log-phase traces in Section3 cannot satisfy this additional rank condition near h=0.

This is a restriction on a prescribed planar central cylinder and its velocity trace. No argument identifies a general curved stable cylinder or general Euler witness with this trace. It neither removes W2 nor contradicts the scalar solvability in Section3. It also does not assert that local helicity implies(4).

## 5. Sources and verification

The complete LIT117 source is retained in the team records with its hash and capture time. Sections1-3 independently derive all of its claims. Section4 is an additional exact argument proposed by this agent. A474 is used only to explain why the interval-kappa<rho<=-2a is of current interest; it is not used to prove(1)-(5). No computation is needed or used.

Focused file review is requested from the existing coordinator/theory collaboration configured for the primary model. That is configuration evidence, not provider attestation.

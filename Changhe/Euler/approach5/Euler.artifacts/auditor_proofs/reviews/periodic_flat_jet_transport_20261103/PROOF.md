# Vorticity jets along flat periodic connections

Status: CONFIRMED A888-A892 at the exact scopes below. The smooth conclusion is stronger than the submitted B51: both bounded W2 endpoints are flat to all orders, in either window. General C2 and smooth profile exclusions remain OPEN, A893.

## 1. Exact setting and conclusions

Fix 2/5<c<1/2 and omega in R. Put Jx=(-x2,x1,0), A=cI-omega J, a=1-2c and kappa=1+c. Let U in C2(R3;R3), P in C1(R3) solve

    div U=0,
    ((1-c)I+omega J)U+DU(Ax+U)+grad P=0,
    U.curl U=0, U(x)=o(|x|) uniformly as |x| tends to infinity.

Define B=Ax+U, Omega=curl U, H=P+|U|^2/2+(Ax).U and g=U.B. No pressure normalization or natural derivative bound is required here.

Use an actual W2 periodic witness and trace as confirmed in A820-A831. Explicitly, Gamma is a nonconstant periodic B orbit in the vortical closure, Omega=D Omega=0 and U!=0 on Gamma. Its constant covector rate is rho, and its Floquet exponents are 0,rho,3c-rho, with positive transverse multipliers. The upper window is rho>=2-c and the lower window rho<=-2a. A selected nonstationary trace z(t) is irrotational, lies in g=0 and a regular level H=H0, and carries the exact ambient law

    dH_(z(t)) D Phi_t(z(0))=exp(rho t)dH_(z(0)).

In the upper window z goes from an irrotational equilibrium q to Gamma. In the lower window it goes from Gamma to an equilibrium q or escapes forward. The bounded endpoint and its nonzero U are already confirmed inputs.

For an upper trace with D Omega(q)!=0, the C2 conclusion is the exact law

    D Omega(z(t))
      =C0 exp(-(rho+kappa)t) B(z(t)) tensor dH_(z(t)), C0!=0,
    log|D Omega(z(t))|/log dist(z(t),Gamma)
      ->(rho+kappa)/(rho-3c)>1.

For U in C-infinity the stronger conclusion is:

    every ambient derivative D^m Omega vanishes on
    W^s(Gamma) union W^u(Gamma), for every integer m>=0.

Consequently every bounded W2 endpoint q in either window has D^m Omega(q)=0 for all m. Every point of an escaping W2 trace has the same flatness. This does not imply vanishing in an open neighborhood.

The new general transport lemma proving the smooth statement is in Section 3. Its only inputs are the exact Cauchy identity, exponential approach to the compact periodic orbit and flatness there. A560 supplies this last input for smooth actual W2 witnesses. The full A560 argument in the team records was compared again. A522 supplies the positive nonflat endpoint structure used only for the more precise C2 rate.

## 2. The submitted upper-window first-jet law

If D Omega(q)!=0, A522 gives the first spectral family at q and a small regular box in which

    {Omega=0}={g=0}={H=H0}.

At a trace point sufficiently near q, D Omega therefore annihilates ker dH. Write D Omega=w tensor dH. The identity Omega.grad H=0 differentiated at an irrotational point shows w is tangent to the level.

Differentiate the Cauchy formula at any irrotational point x:

    D Omega(Phi_t x) D Phi_t(x)
       =exp(-kappa t) D Phi_t(x) D Omega(x).           (1)

The term D2 Phi_t multiplied by Omega(x) vanishes. Combining (1) with the exact covector law propagates the tensor factorization along the entire trace and gives

    w(Phi_t x)=exp(-(kappa+rho)t)D Phi_t(x)w(x).

This derivation only requires the initial regular level box. It does not require an unproved full annular neighborhood near Gamma.

Let nu be the level two-form obtained by contracting volume with grad H/|grad H|^2. Its pullback along the trace is exp((3c-rho)t)nu. Since D Phi_t B=B Phi_t,

    nu(B,w)(Phi_t x)=exp((-a-2rho)t)nu(B,w)(x).

As t tends to negative infinity, B tends to zero at q while w and nu remain bounded. Since -a-2rho<0, the equality forces nu(B,w)=0. Thus w is parallel to the nonzero trace vector B. Its transport gives w=C0 exp(-(kappa+rho)t)B. Continuity and D Omega(q)!=0 make C0 nonzero.

Near Gamma, |B| and |dH|=a|U| are bounded above and below by positive constants. Hence

    t^(-1)log|D Omega(z(t))| -> -(rho+kappa).

The scalar return map on the stable cylinder is s to exp((3c-rho)T)s+o(s), and return times tend to T. This gives t^(-1)log dist(z(t),Gamma)->3c-rho. Between returns the distance comparison follows from uniformly bounded invertible derivatives over one return interval. Division gives the asserted exponent. C2 regularity supplies only continuity of D Omega and is consistent with this decay.

## 3. A general all-order flatness propagation lemma

Here is the stronger argument. Let B and Z be smooth vector fields on a region containing a complete half-orbit, and suppose their flows obey

    Z(Phi_t x)=exp(-kappa t)D Phi_t(x)Z(x).             (2)

Let C be compact, with every ambient derivative of Z zero on C. Suppose, for one epsilon in {+1,-1},

    x_s=Phi_(epsilon s)x, s>=0,
    dist(x_s,C)<=C1 exp(-eta s), eta>0,

and the half-orbit has compact closure. Then every D^m Z is zero at every finite point of the same orbit wherever continuation exists.

Choose L bounding |DB| on the compact half-orbit closure. For F_s=D Phi_(epsilon s)(x), the variational equation and its inverse give

    |F_s|<=exp(Ls), |F_s^(-1)|<=exp(Ls).

Flatness on compact C and Taylor's theorem imply, for every pair of nonnegative integers m,N,

    |D^m Z(y)|<=C_(m,N) dist(y,C)^N

in a small compact neighborhood of C. A nearest point exists by compactness, and Taylor is applied on a fixed small ambient ball about that point. No smooth nearest-point projection is needed.

For m=0, pull back (2). The preceding bounds give

    |Z(x)|<=C_(0,N) C1^N
       exp((|kappa|+L-N eta)s).

Choose N eta>|kappa|+L and let s tend to infinity. Thus Z(x)=0. Starting at any other finite point of the same orbit proves its vanishing there too.

Inductively suppose all ambient derivatives of order less than m vanish along the orbit. Differentiate (2) m times in the initial point. Every chain-rule term containing a lower derivative of Z at either endpoint is zero. The only surviving terms are

    D^m Z(x_s)[F_s v1,...,F_s vm]
       =exp(-epsilon kappa s)
          F_s D^m Z(x)[v1,...,vm].                    (3)

All derivatives of the finite-time smooth flow exist. In particular terms involving higher derivatives of the flow have disappeared by the induction hypothesis; no bound for them is needed.

Pulling back (3) and using operator norms yields

    |D^m Z(x)|
       <=exp((|kappa|+(m+1)L)s)|D^m Z(x_s)|
       <=C_(m,N) C1^N
          exp((|kappa|+(m+1)L-N eta)s).

Choose N eta>|kappa|+(m+1)L. The limit gives D^m Z(x)=0. The same argument at every finite orbit point closes the induction. The use of |kappa| makes both time directions valid. No irrotational surface, rank condition, covector rate or analyticity is needed for this lemma.

## 4. Application to both W2 windows

For an actual smooth profile, Z=Omega obeys (2) exactly. A560 gives every ambient derivative of Omega zero on Gamma. Its transverse Taylor argument also covers ambient derivatives: all transverse coefficients vanish identically along the cycle, so their tangential derivatives vanish, and smooth coordinate chain rules give all ambient jets.

Every point of the global stable or unstable manifold of a hyperbolic periodic orbit approaches it exponentially in the corresponding time direction. This is also immediate from the local contracting return map, after a finite initial orbit segment. Its approaching half-orbit has compact closure, and |DB| is bounded there. Section 3 therefore applies in both directions.

The upper W2 trace lies in W^s(Gamma); the lower trace lies in W^u(Gamma). Thus Omega is flat to every order at each trace point, including traces without an independently established irrotational level neighborhood. If a trace converges at its other end to q, continuity of each D^m Omega makes every such derivative zero at q.

This proves more than the original nonflat-endpoint contradiction. It also repairs the parent source's proposed use of its tensor factorization after setting w(q)=0: that factorization was derived from the nonflat endpoint box and was not available merely from D Omega(q)=0. Section 3 gives the stronger vanishing conclusion directly. No claim that the endpoint is excluded follows.

## 5. The accompanying curvature identities

These identities have a separate local scope. On a regular invariant irrotational level piece with constant covector rate rho, put u=|U|, n=U/u, T=D n restricted to the tangent plane, mean curvature M_s=tr T/2 and Gaussian curvature K_s=det T. The convention is D n. From g=0,

    u=-Ax.n, B=(Ax)^tangent,
    (DU)^tangent=uT, n.DU n=-u tr T.

The covector equation gives B log u=rho-c+u tr T. Since div_surface B=2c+u tr T,

    div_(dA/u) B=3c-rho,
    u^2 tr T+T(B,B)+omega B.Jn+u(rho-c)=0.

The second formula follows by differentiating u=-Ax.n tangentially, obtaining grad_surface u=-omega Jn-TB. A positive-area compact domain in this piece cannot have its entire boundary tangent to B, by the weighted divergence theorem. This excludes a proposed filling disk, not an annular neighborhood.

On Gamma the same shape identity follows from D2H=-a DU, since Omega=D Omega=0. With flow-time derivatives, v=|B|, e1=B/v, e2=n cross e1, j=n.e3 and tau=e2 dot d_t e1, it gives

    2u M_s=c-rho+dot(u)/u,
    u T11=dot(v)/v-c, u T12=tau+omega j,
    u T22=2c-rho+dot(u)/u-dot(v)/v.

The determinant of these entries gives K_s. Their periodic averages are

    mean(u M_s)=(c-rho)/2,
    mean(u T11)=-c, mean(u T22)=2c-rho.

At an irrotational carrier equilibrium q with DB(q)^T U(q)=rho U(q), let u_q=|Aq| and j_q=-c q3/u_q. Its invariant tangent-plane eigenvalues lambda_minus,lambda_plus give

    M_s(q)=(c-rho)/(2u_q),
    K_s(q)=[lambda_minus lambda_plus-2c^2+c rho-omega^2 j_q^2]/u_q^2.

Indeed the tangent matrix is cI+u_q T-omega j_q J2; its determinant is the symmetric-part determinant plus omega^2 j_q^2. For the nonflat first family lambda_plus=rho+kappa, lambda_minus=-a-2rho, the numerator becomes

    -2rho^2+(c-3)rho+c-1-omega^2 j_q^2<0.

This negative endpoint curvature is consistent with its saddle structure. Pointwise eigenvalues of a projected moving tangent matrix on Gamma must not be identified with Floquet exponents.

## 6. Exact local irrotational upper-window model

Fix rho>=2-c, omega!=0 and R>0. Put m=rho/c-2>1 and b=R/sqrt(m). Near the ellipsoid r^2/R^2+z^2/b^2=1 define lambda by

    r^2/(R^2+lambda)+z^2/(b^2+lambda)=1.

The implicit derivative in lambda is strictly negative on this compact surface, so a smooth collar exists. Set

    F(lambda)=-(c R^2 b/2)
      integral_0^lambda ds/[(R^2+s)sqrt(b^2+s)],
    phi=F(lambda), U=grad phi,
    P=H0-a phi-|U|^2/2-(Ax).U.

To check harmonicity directly, put d1=d2=R^2+lambda, d3=b^2+lambda, D=sum x_i^2/d_i^2 and Q_d=sum 1/d_i. Implicit differentiation gives

    partial_i lambda=2x_i/(d_i D),
    |grad lambda|^2=4/D, Delta lambda=2Q_d/D.

The two additional summed second-derivative terms cancel. Since F''+(Q_d/2)F'=0, Delta phi=0. Thus div U=0 and Omega=0. For a gradient field,

    DU(Ax+U)=grad((Ax).U+|U|^2/2)-A^T U.

Substitution and A^T=cI+omega J verify the full profile equation exactly; H=H0-a phi.

On the ellipsoid F'(0)=-c/2, and if nu is its outward unit normal then U=-c(x.nu)nu. Rotation is tangent to the surface, so g=0 and B=(Ax)^tangent there. At the equatorial circle,

    U=-cR e_r, B=-omega R e_theta, period=2pi/|omega|,
    DU=diag(rho-c,-c,2c-rho)

in the cylindrical orthonormal frame. The entries follow from lambda_rr=2, lambda_zz=2m and F''(0)=c(2+m)/(4R^2). The cylindrical variational exponents are 0,rho,3c-rho. Also dot U=-omega JU and DB^T U=rho U+omega JU, so the covector law has rate rho on the circle. The level equation B_z=cz(1-1/(b^2D)) has negative derivative 3c-rho at the equator, verifying attraction within the level.

This is an exact local profile on a collar, which need not extend into the enclosed solid ellipsoid. It is irrotational everywhere in its domain and has no vortical closure or nonflat-endpoint connection. The covector ratio l defined there by dg=l dH is

    -a l|_surface
       =4F''(0)/D
       =rho/[1+m(m-1)z^2/R^2],

so the constant-rate condition on the whole invariant level fails away from the equator. The model tests attraction, embedding, strain and the local Euler equation only.

## 7. Verification and limits

The full B51 source section, the complete 456-line consultation answer, its complete standalone proof and verification record were read. Its algebra, confocal harmonicity and jet transport were checked analytically here. No new computation was needed. The consultation's failed Bedrock credential request is not counted as a successful model review.

The new all-order lemma was submitted through agent notes for continuing comparison with the existing configured model agents. Provider runtime remains unattested; no new client or agent is used. Exact source pins and hashes accompany this proof.

The C2 configuration remains unresolved. In the smooth class both endpoint types are now infinitely flat, which still gives no open irrotational neighborhood. The local ellipsoid model does not realize the full global configuration. Neither argument proves the requested general decay-only nonexistence theorem.

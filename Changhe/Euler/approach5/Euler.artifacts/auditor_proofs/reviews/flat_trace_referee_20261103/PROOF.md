# All-order trace flatness and the lower-window finite-regularity test

Status: CONFIRMED at the exact scopes below. Removing the level-germ hypothesis from the C3 conclusion is OPEN. This does not exclude a smooth witness with flat endpoints.

## 1. Setting

Fix 2/5<c<1/2 and omega in R. Let Jx=(-x2,x1,0), A=cI-omega J, a=1-2c and kappa=1+c. Let U in C2(R3;R3), P in C1(R3) satisfy

    div U=0,
    ((1-c)I+omega J)U+DU(Ax+U)+grad P=0,
    U.curl U=0,
    U(x)=o(|x|) uniformly at infinity.

Put B=Ax+U, Omega=curl U, H=P+|U|^2/2+(Ax).U and g=U.B. Let Phi_t be the B flow. It is complete because B has at most linear growth. Suppose Gamma is an actual W2 periodic witness as specified in A820-A831: a nonconstant periodic B orbit in the vortical closure, with Omega=D Omega=0 and U nonzero there, constant covector rate rho, and transverse Floquet exponents rho,3c-rho. The upper window is rho>=2-c; the lower window is rho<=-2a. A trace is an irrotational nonstationary B orbit in a regular level H=H0 and g=0, approaching Gamma forward in the upper window or backward in the lower window. Its covector law is

    dH_(Phi_t x) D Phi_t(x)=exp(rho t)dH_x.

Bounded opposite endpoints q have B(q)=Omega(q)=0 and U(q)!=0. These are prior W2 conclusions, not consequences asserted for arbitrary periodic orbits.

For smooth U, every ambient derivative of Omega vanishes on every trace and at every endpoint q. In fact the same conclusion holds on the entire global stable and unstable manifolds of Gamma. For C2 U, a lower-window trace with a nonflat endpoint and the additional level-germ hypothesis in Section 3 must have rho<-kappa. For C3 U, no such nonflat lower endpoint exists under that extra hypothesis.

## 2. All-order transport

A559-A560 give all ambient derivatives of Omega zero on Gamma in the smooth class. The Cauchy law is

    Omega(Phi_t x)=exp(-kappa t)D Phi_t(x)Omega(x).

Every point of either global stable or unstable manifold approaches the compact Gamma exponentially in one time direction. Write t=epsilon s, s>=0, epsilon in {1,-1}. The approaching half-orbit has compact closure; for some K and eta>0,

    |F_s|+|F_s^-1|<=2 exp(Ks),
    dist(Phi_(epsilon s)x,Gamma)<=C exp(-eta s),
    F_s=D Phi_(epsilon s)(x).

Taylor's theorem on a fixed compact tube about Gamma gives, for every m,N,

    |D^m Omega(y)|<=C_(m,N)dist(y,Gamma)^N.

For m=0, pull back the Cauchy law and take N eta>kappa+K. This proves Omega(x)=0 at every finite point of the orbit. Suppose all derivatives below order m vanish at all such points. Differentiate the Cauchy law m times. Every term involving a higher derivative of the flow multiplies a lower derivative of Omega at one endpoint and vanishes. The surviving identity is

    D^m Omega(Phi_t x)[D Phi_t v1,...,D Phi_t vm]
       =exp(-kappa t)D Phi_t D^m Omega(x)[v1,...,vm].

Thus

    |D^m Omega(x)|
       <=exp((kappa+(m+1)K)s)|D^m Omega(Phi_(epsilon s)x)|
       <=C exp((kappa+(m+1)K-N eta)s).

Choose N eta>kappa+(m+1)K and pass to infinity. This closes the induction at each finite orbit point. Continuity of each ambient derivative gives the same result at a finite endpoint q. No irrotational level germ, rank-one factorization or A522 box is needed. This is exactly the all-order argument already checked in A889-A890; B52 independently applies it to the trace set.

## 3. Lower-window tensor transport under an extra level germ

Assume a lower-window trace z(t) tends to Gamma as t tends to minus infinity and to q as t tends to plus infinity. Assume D Omega(q)!=0. In addition, at one trace point suppose Omega vanishes on a relatively open germ of the regular surface H=H0. Then D Omega annihilates ker dH there. Differentiating Omega.grad H=0 at that irrotational point also makes its image tangent to the level. Therefore

    D Omega=w tensor dH, with w tangent.

The differentiated Cauchy law, with the exact covector law, propagates this factorization and gives

    w(z(t))=exp(-(kappa+rho)t)D Phi_t w(z(0)).

Let nu be the level two-form obtained by contracting volume with grad H/|grad H|^2. Along this trace its pullback scales by exp((3c-rho)t). Consequently

    nu(B,w)(z(t))=exp((-a-2rho)t)nu(B,w)(z(0)).

Since rho<=-2a, -a-2rho>=3a>0. At q, B tends to zero while w and nu remain bounded, because dH(q)=-aU(q) is nonzero. The preceding identity forces nu(B,w)=0. On the nonstationary trace this means w is parallel to B. Transport now gives

    D Omega(z(t))=C0 exp(-(kappa+rho)t)B(z(t)) tensor dH_(z(t)).

The constant C0 is nonzero: otherwise D Omega vanishes on the whole trace and hence at q. Near Gamma, |B| and |dH| are bounded above and below by positive constants. Continuity of D Omega and its zero value on Gamma therefore force rho<-kappa. In particular rho=-kappa is excluded already for C2 U under the extra germ hypothesis.

Set r=-rho>kappa. The unstable return-map multiplier at Gamma is exp((3c+r)T). Backward convergence on the unstable cylinder and bounded distortion over one return period give

    log dist(z(t),Gamma)/t ->3c+r as t->-infinity.

Combining this with the exact tensor law gives

    log|D Omega(z(t))|/log dist(z(t),Gamma)
       ->(r-kappa)/(3c+r),

which lies strictly between zero and one. This is a logarithmic exponent; no fixed asymptotic prefactor is claimed.

## 4. The C3 contradiction and its limit

For C3 U, D Omega is C1. It vanishes on Gamma, so a compact-tube mean-value estimate gives

    |D Omega(y)|<=C dist(y,Gamma).

The exponent in Section 3 is less than one, contradicting this estimate. Thus the nonflat lower endpoint is impossible for C3 U under the regular irrotational level-germ hypothesis.

For C2 U, D Omega is only continuous. Its vanishing on Gamma does not give a linear distance bound, and the fractional exponent is consistent with this regularity. Moreover A522 supplies its separating level box only in the positive nonflat spectral family. It does not supply the extra germ at the lower-window endpoint. Removing that premise from this C3 argument remains OPEN. The smooth argument in Section 2 removes it by a different mechanism.

## 5. Referee exchange and scope

The completed w2flatend referee confirms the upper-window transport law, the local confocal collar model and curvature formulas at the scopes checked in A888-A892. The parent Theory Agent B source has applied the propagation repair and independently extended the referee's first-derivative argument to all orders in B52. This agrees with A889-A890. The model remains an irrotational collar, not a global vortical-closure witness. Curvature along the time-parametrized periodic curve requires the supplied c, omega and rho; the curve alone does not determine the transverse curvature.

The nested referee reported that its attempted model credential retrieval failed before invocation. That failed attempt is not counted as a model review. The existing Theory Agent B parent agent is configured for model and supplied its explicit checked argument; provider runtime has not been independently attested. No new model client, external posting, numerical experiment or formal build was used.

# Axisymmetric degenerate tails constrained by their pressure

Status: CONFIRMED as A549 after repeated complete independent postread and full source comparison. No computation was used by this agent. The actual-profile application retains all extra hypotheses.

## 1. Exact theorem

Let 1/3<c<1/2, omega in R, p=(1-c)/c in(1,2), a=1-2c and A=cI-omega J, where J(x1,x2,x3)=(-x2,x1,0). On D=R3 minus{0}, let V in C1(D;R3) and P2 in C1(D) be axisymmetric about the third axis and homogeneous of degrees -p and -2p, respectively. Vector axisymmetry means V(Rx)=RV(x) for every rotation R about that axis. Assume

    div V=0, W=curl V,
    Ax cross W=aV,
    -Delta P2=partial_i partial_j(V_i V_j),
    W.grad S=0, S=P2-|V|^2/2.                             (1)

The pressure equation is distributional on D. All other identities are classical. Then omega!=0 implies V=0.

At omega=0, every possible nonzero V satisfying(1) is purely azimuthal and has one strict swirl sign off the axis. In spherical coordinates r,theta,phi, put z=cos(theta), s=sin(theta), w=1-z^2. There are a C1 function F on(-1,1) with no zero there and a constant C<0 such that

    V=r^-p (F(z)/s)e_phi,
    S=C r^-2p |F(z)|^nu, nu=2p/(p-1)>2,
    F(z)=O(1-z^2) at both endpoints.                       (2)

This last conclusion is necessary, not an existence assertion. No finite order of a zero is assumed. The theorem is global on D; E=Ax cross W-aV vanishing only on a cone or sheet is insufficient.

## 2. Angular reduction, including the poles

Put t=omega/c. Taking the scalar product of Ax cross W=aV with Ax gives Ax.V=0. At radius1, Ax=c e_r-omega s e_phi. If F=sV_phi and H=sV_theta, then

    V=r^-p [tF e_r+(H/s)e_theta+(F/s)e_phi].               (3)

F and H are C1 on the open interval. At each pole, axisymmetry makes V parallel to the third axis; Ax.V=0 then forces V=0. Since V is C1 through that pole, its angular components have magnitude O(s). Thus

    F=O(w), H=O(w) at z=-1 and z=1.                       (4)

The divergence equation gives

    H'=kF, k=(2-p)t.                                      (5)

In particular H is C2 in the interior. Direct curl differentiation yields

    W_r=-r^(-p-1)F',
    W_theta=r^(-p-1)(p-1)F/s,
    W_phi=r^(-p-1)[-(p-1)H/s+t sF'].                       (6)

Equations(3),(5),(6) also recover Ax cross W=aV. Write

    P2=r^-2p u(z), S=r^-2p h(z),
    e(z)=|V|^2/2 at r=1=[t^2F^2+(F^2+H^2)/w]/2,
    u=e+h.

Using(6), the last equation in(1) is

    2pF'h-(p-1)Fh'=0.                                    (7)

On every connected component I of {F!=0}, solve this ordinary linear equation:

    h=C_I |F|^nu, nu=2p/(p-1)>2.                          (8)

C_I is finite and may differ between components; zero is permitted. No bound uniform over components will be needed.

## 3. The pressure equation with only C1 velocity

For a divergence-free C1 vector field, local smooth mollification gives

    partial_i partial_j(V_i V_j)=tr((DV)^2)

in distributions. The right side is continuous. In the orthonormal spherical frame, set M=r^(p+1)DV. Direct differentiation of(3) gives

    M=[ -ptF,       -tsF'-H/s,             -F/s;
        -pH/s,      (p-1)tF-zH/w,          -zF/w;
        -pF/s,      -F'-zF/w,              tF+zH/w ].       (9)

For example, the middle diagonal entry is -H'-zH/w+tF, which becomes (p-1)tF-zH/w by(5). This checks the geometric derivative terms that matter at a zero of F.

Separating radial and angular test functions in the pressure equation gives

    (w u')'+kappa0 u=-tr(M^2), kappa0=2p(2p-1).            (10)

On each compact interval in(-1,1), w>0. Since u is C1 and the right side is continuous, (10) makes w u' C1 and hence u C2 there. It does not make F C2. This distinction is used at the endpoint below.

## 4. A pressure constraint at an arbitrary interior endpoint

Let z0 be an interior endpoint of a nonempty component I of {F!=0}. Then F(z0)=0. Write d=F'(z0), H0=H(z0) and w0=1-z0^2>0. On I, formula(8) gives h->0 and h'->0, so continuity yields h(z0)=h'(z0)=0. Moreover

    F(z)=O(|z-z0|),
    h'(z)=O(|z-z0|^(nu-1)).

Since nu>2, the one-sided derivative of h' at z0 is zero. The constant in this estimate depends only on this one component I.

The derivative of F F' at z0 exists one-sidedly and equals d^2: divide F(z)F'(z) by z-z0 and use F(z)/(z-z0)->d and F'(z)->d. No second derivative of F is being taken. Since H'=kF and H is C2, differentiating the explicit expression for e' at z0 gives

    e(z0)=H0^2/(2w0),
    e'(z0)=z0 H0^2/w0^2,
    e''(z0)=(t^2+1/w0)d^2+kH0 d/w0
                  +H0^2(1/w0^2+4z0^2/w0^3).             (11)

Here e'' denotes the one-sided derivative of e' at z0. Because u=e+h is C2, its actual second derivative at z0 equals this value. Thus substituting into(10) is legitimate at C1 velocity regularity.

From(9), at F=0,

    tr(M^2)=2ptH0d+2pH0^2/w0+2z0^2H0^2/w0^2.

Using this and(11), equation(10) becomes

    (1+t^2w0)d^2+(p+2)tH0d
       +[(2p^2+p+1)/w0+4z0^2/w0^2]H0^2=0.              (12)

The first diagonal coefficient is positive. Four times the determinant of this quadratic form is

    4(2p^2+p+1)/w0+16z0^2/w0^2
                      +t^2[7p^2+16z0^2/w0]>0.           (13)

Indeed expanding the t^2 coefficient uses
4(2p^2+p+1)-(p+2)^2=7p^2. Therefore the form is positive definite for every real t, and

    H(z0)=0, F'(z0)=0.                                   (14)

The conclusion includes flat zeros and zeros of unprescribed order.

## 5. Integrated uniqueness excludes the component endpoint

A separate direct multiplication of(9), using only F',H', yields

    tr(M^2)=T'+R,
    T=2ptHF+zF^2/w,
    R=(2p-1)[2(p-1)t^2+1/w]F^2
         +[2p/w+2z^2/w^2]H^2+2kzFH/w.                   (15)

To check the decomposition, the derivative terms of tr(M^2) are 2ptHF'+2zFF'/w. Differentiating T adds 2ptkF^2+(1+z^2)F^2/w^2. The remaining t^2 coefficient is 2(2p-1)(p-1), and the remaining F^2/w coefficient is 2p-1, giving(15). Equation(10) is therefore

    (w u'+T)'=-kappa0 u-R.                               (16)

Suppose z0 is a left endpoint of I. On a sufficiently short interval inside I, the positive quadratic e dominates the higher-order term C_I|F|^nu. Thus for some b>0,

    u>=b(F^2+H^2)>=0.                                    (17)

All coefficients in(15) are bounded on this interval. It follows that |T|+|R|<=C u. By(14), u(z0)=u'(z0)=T(z0)=0. Integrating(16) from z0, with w bounded below, gives

    |u'(z)|<=C u(z)+C integral_(z0)^z u(q)dq.             (18)

Let Y(z)=u(z)+integral_(z0)^z u(q)dq. It is nonnegative, C1, has Y(z0)=0, and obeys Y'<=C'Y. Multiplication by exp(-C'(z-z0)) and integration show Y=0. Then(17) gives F=H=0 on a subinterval of I, a contradiction.

At a right endpoint use the reflected coordinate z0-z and integrate(16) backward. The absolute-value estimate(18) has the same form and gives the identical contradiction.

Hence a nonempty component of {F!=0} has no endpoint in(-1,1). Either F is identically zero there or it is everywhere nonzero with one fixed sign. In the first case(5) and(4) give H=0, and V=0. An accumulation of components cannot evade this argument: each proper component would already have an interior endpoint.

## 6. The pole constraint and zero-rotation residual class

Suppose V!=0, so F has one strict sign. Equation(4) makes F integrable and H(-1)=H(1)=0. Integrating(5) gives

    0=(2-p)t integral_(-1)^1 F(z)dz.

The integral is nonzero and 2-p>0. Thus t=0 and omega=0. This proves the asserted exclusion for every nonzero omega, without a uniform lower bound on |omega|.

When omega=0, equation(5) and the endpoint values make H=0. Hence V is the pure azimuthal field in(2). There is only one interval {F!=0}=(-1,1), so(8) has a single constant C. Its sign follows from the pressure equation, not from the first-integral ODE alone.

For clarity let

    R0=integral_(S2) V_r^2,
    T0=integral_(S2)|V_T|^2,
    P0=integral_(S2)P2.

Test the pressure equation against a smooth radial function chi supported in an annulus. The Hessian of chi has radial entry chi'' and tangential entries chi'/r, giving

    -P0 integral r^(2-2p)(chi''+2chi'/r)
       =R0 integral r^(2-2p)chi''
                   +T0 integral r^(1-2p)chi'.

Twice integrating the compactly supported radial test yields

    P0=[(2-2p)R0-T0]/(2p).

Here R0=0, and therefore

    integral_(S2)S=-(p+1)T0/(2p)<0.

Since integral |F|^nu is finite and positive, C<0. This does not assert a Poisson-compatible field of the residual form exists.

## 7. Application to an actual profile

Suppose a full C2/C1 profile in 2/5<c<1/2 has global U.curl U=0, uniform U->0 and DU=O(sqrt r). The confirmed natural-bound chain and A210 give its actual leading tail V. A533 gives V in C1alpha_loc(D) for every alpha<1. A530 gives its canonical P2, while A531 gives Wstar.grad(P2-|V|^2/2)=0.

Assume additionally that this actual V is axisymmetric and E=Ax cross Wstar-aV vanishes on all D. Twisted homogeneity then becomes ordinary homogeneity; the canonical pressure operator preserves axisymmetry and the required degree. All hypotheses of(1) hold. For omega!=0 the theorem gives V=0. The actual expansion becomes U=o(r^-p), so A053 gives U=0. At omega=0 the separately confirmed nonrotating Liouville theorem applies directly to the full decaying profile.

Thus this is a conditional nonexistence result for an axisymmetric, globally degenerate leading tail, allowing a non-axisymmetric full profile. Global zero helicity, derivative control, and global degeneracy of the leading tail are additional assumptions. An open zero cone obtained from A534 or a zero arc obtained from A536 does not meet the global hypothesis.

## 8. Verification and dependencies

The complete LIT141 source is retained in the verification folder. Equations(9),(12),(13),(15) were rederived by hand, independently of its exact symbolic check. Endpoint regularity uses only C1 velocity and the one-dimensional pressure equation. The uniqueness step is the explicit scalar Gronwall argument above. No external Liouville or weighted Harnack theorem enters the standalone result. The actual-profile application uses only the separately confirmed inputs listed in Section7.

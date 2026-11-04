# Angular compression can reverse the exit-cost sign

Status: LIT314 is CONFIRMED A2663-A2665 after complete independent and existing coordinator comparison. The precisely qualified full-completion cost window is CONFIRMED A2666; unrestricted consequences remain OPEN A2667. This is a local omega=0 carrier and a scalar noncompletion theorem, not a global Euler profile.

## 1. Exact claim and notation

Fix 0<c<1/2, set omega=0, X(x)=cx, L=(1-c)I, a=1-2c, b=2(1-c), eta=a/b, kappa=1-2eta=c/(1-c), and p=(1-c)/c. There is a smooth velocity V on a finite flowbox around a segment Gamma of the positive x3-axis through x0=(0,0,1), with

    div V=0, X.V=0, DV X=-LV.

It is flat on Gamma and nonzero off Gamma. On sigma(y)=(y1,y2,1), let r=|y|, t=log(1/r), f(r)=exp(-t^2). Its one-form is sigma*(V.dx)=f zeta, where for positive constants c1,c2,d,C,

    c1 f<=|V(sigma(y))|<=c2 f, zeta.e_theta>=d, |zeta|<=C.

Every forward trajectory of Y=(zeta2,-zeta1) exits a small punctured section disc through its outer circle in finite time. Nevertheless its signed divergence cost I on the ray theta=0 satisfies

    I(r,0)=-C0 t^4+O(t^3), C0>0.

Thus kappa log(1/f)+I and log(1/f)+I both tend to minus infinity there. Both actual ratios |curl V|/|V| and |curl V.X|/|V| belong to every section Lq with 0<q<2, but neither is bounded by B2+C*/r for B2 in L2 and a finite C* on any disc centered at zero.

There is no scalar S continuous at x0, zero on Gamma, C1 and strictly negative off Gamma, satisfying X.grad S=-bS and curl V.grad S=0 off Gamma. No pressure condition is required for this last conclusion. All claims are local, for omega=0 only, with constants allowed to depend on c and the construction.

## 2. Smooth oscillatory stream function

Take a nonnegative nonzero chi in C-infinity with compact support in (-1/4,1/4), bounded by one. Put Jchi=integral chi>0. Fix 0<epsilon<1/8 and choose an integer N large enough below. Let R=exp(-(N-1/2)), m_n=n^3, and define

    Psi(r)=integral_0^r f(s) ds,
    psi(r,theta)=Psi(r)+sum_(n>=N) epsilon r f(r) m_n^-1
                                      chi(t-n)cos(m_n theta).

The logarithmic annuli are disjoint, so the sum is locally finite off zero. Since r f'/f=2t, its polar derivatives on the nth annulus are

    psi_r/f=1+(epsilon/m_n)[(1+2t)chi-chi']cos(m_n theta),
    psi_theta/r=-epsilon f chi sin(m_n theta).

The first error is O(n^-2). Increase N so

    3f/4<=psi_r<=5f/4, |psi_theta|/r<=epsilon f.             (1)

At fixed Cartesian derivative order j, each oscillatory term has magnitude at most C_j f r^(1-j)(1+t)^(M_j). Angular derivatives cost n^3/r, radial derivatives cost r^-1 times a polynomial in t, and n=t+O(1) on the support. Each such bound is smaller than every prescribed power of r as r tends to zero. The base term has the same property, since Psi<=r f and Psi'=f. All derivatives extend continuously as zero at the center. The fundamental theorem of calculus along segments shows successively that these extensions are the derivatives of the extended function. Hence psi is smooth and flat, while its gradient is nonzero off zero by (1).

## 3. Exact lift and normalization

Write J2(u1,u2)=(-u2,u1) and set

    rho=(1+r^2)^((p-2)/2), q=rho^-1 J2 grad psi,
    M=I-y tensor y/(1+r^2), h=-y.q/[c(1+r^2)],
    v0=(Mq,-y.q/(1+r^2)),
    Phi(y,s)=exp(cs)(y1,y2,1),
    V(Phi(y,s))=exp(-(1-c)s)v0(y).                         (2)

The last formula is smooth on a finite flowbox and flat exactly on the central orbit, because |v0|^2=q.Mq and M has eigenvalues 1 and (1+r^2)^-1. The section dot product (y,1).v0 vanishes, so X.V=0 throughout the flowbox. Differentiation in s gives DV X=-(1-c)V.

The coordinate vector field in (2) has components exp(-s)(q,h), and the coordinate volume density is c exp(3cs). Therefore

    div V=exp(-s)[div q+(3c-1)h].

Since div(rho q)=div(J2 grad psi)=0,

    div q=-(p-2)y.q/(1+r^2)=(3c-1)y.q/[c(1+r^2)].

This cancels the h term exactly. There is no residual divergence correction.

The pulled-back covector is Mq. In polar components,

    zeta=rho^-1[(psi_r/f)e_theta
                  -psi_theta/(r f(1+r^2)) e_r],
    Y=rho^-1[(psi_r/f)e_r
                  +psi_theta/(r f(1+r^2)) e_theta].        (3)

Equation (1), bounded positive rho and positive-definite M give all normalization bounds in Section 1. In particular Y.e_r has a fixed positive lower bound. For each punctured point the trajectory remains in its compact annulus until it exits, and smooth ODE continuation plus increasing radius proves finite first exit. No global completeness is used.

## 4. Exact signed divergence cost on the invariant ray

At theta=0 the angular component in (3) vanishes, so the ray is invariant. Write d(r)=psi_r(r,0)/f(r); it lies between 3/4 and 5/4 and equals 1+O(n^-2) on the nth annulus. Polar divergence, divided by the radial speed, gives on the ray

    div Y/Y_r=(log Y_r)' +1/r
                     +psi_thetatheta/[r^2(1+r^2)psi_r].

Consequently

    I(r,0)=log[R Y_r(R)/(r Y_r(r))]
         +integral_r^R psi_thetatheta(s,0)
                             /[s^2(1+s^2)psi_r(s,0)] ds.   (4)

On the nth support psi_thetatheta=-epsilon n^3 s f(s)chi(log(1/s)-n). Changing variables u=log(1/s),

    I(r,0)=t+O(1)-epsilon sum_(n>=N) n^3
       integral_(N-1/2)^t chi(u-n)/[(1+exp(-2u))d(exp(-u))]du.

Each complete annulus contributes Jchi n^3+O(n). The sum of these errors is O(t^2), and the at most one incomplete annulus contributes O(t^3). The identity sum_(n<=t) n^3=t^4/4+O(t^3) now gives

    I(r,0)=-(epsilon Jchi/4)t^4+O(t^3).                    (5)

Changing the fixed outer radius only adds a constant to the ray cost. Thus (5) also holds inside any proposed completion germ.

## 5. Physical curl ratios and the failed endpoint bound

Two derivatives of psi give |Dq|<=C f(1+t^3)/r. The largest contribution is the second angular derivative divided by r^2, of order n^3 f/r; all mixed and radial contributions are bounded by this estimate. Differentiating (2) in physical coordinates on the section uses a smooth inverse flowbox and bounded coefficients. Thus, for W=curl V,

    |W|/|V|+|W.X|/|V|<=C(1+t^3)/r.                       (6)

The qth power is integrable against r dr dtheta for q<2, because its radial integral is bounded by a constant times integral (1+t^3)^q exp(-(2-q)t)dt.

To prove failure of the endpoint majorant, use the complete annular gaps outside every cutoff support. There q=rho^-1 f e_theta, and Mq=q. Derivatives tangent to sigma are physical x1,x2 derivatives, so the physical third curl component equals

    W3=(1/r)partial_r(r rho^-1 f)
       =rho^-1 f[(1+2t)/r-rho'/rho].                      (7)

For large t it is bounded below in magnitude by C^-1 t f/r. The carrier identities give X cross W=aV and hence

    W.X=[|X|^2 W3-a(V cross X)3]/X3,
    X3=c, |X|^2=c^2(1+r^2).

On these gaps |(V cross X)3|<=C r f. Therefore |W.X|>=C^-1 t f/r as well. Comparability with f proves a C^-1 t/r lower bound for each ratio on every small gap. The gaps have a fixed positive logarithmic length in each unit t interval. For any finite C*, the positive part of either ratio minus C*/r has squared integral bounded below by a positive multiple of integral t^2dt over all large gaps, which diverges. It cannot be dominated by the absolute value of an L2 function. These are actual physical curl ratios, not auxiliary planar derivatives.

## 6. The opposite cost direction itself obstructs a scalar

Suppose S has the properties in Section 1 and set H=-S>0 off Gamma. From X cross W=aV, X.grad H=-bH and W.grad H=0,

    a grad H cross V=bH W.

Because eta=a/b, curl(H^-eta V)=0. This uses C1 regularity only off the orbit. Pull back to the section and set F=f(H composed sigma)^-eta. Its closedness is div(FY)=0. Along the invariant ray to any fixed outer radius R' within the germ,

    log F(r,0)=log F(R',0)+I_R'(r,0),
    log H(sigma(r,0))=[-t^2-log F(R',0)-I_R'(r,0)]/eta.

By (5) the last expression tends to positive infinity. Thus H is unbounded as its argument approaches x0, contradicting continuity there. In fact local boundedness alone would suffice. The Poisson equation, pressure normalization and scalar flatness play no role.

## 7. Dependencies and precise conclusion

All formulas have been derived from the explicit stream function, the finite local lift, planar divergence and elementary exponential integrability. No numerical approximation, formal build or external literature result is needed. The positive-cost criterion of LIT311 is not refuted: its cost hypothesis fails here. The example refutes only an inference that angular definiteness, finite exits, flatness and subcritical curl-ratio bounds automatically supply that hypothesis. It also shows the criterion is not necessary for proving noncompletion, since the negative cost direction already forces scalar blow-up.

Neither nonzero omega nor a global decaying profile is constructed. The existing configured model coordinator comparison is completed below; actual provider runtime is independently unattested.


## 8. Complete existing coordinator comparison

The seven-section source, seven-section independent reconstruction, all nine substantive items of the existing coordinator comparison, its two wording points and its supplied check log have been read in full. The symbolic checks at two sample values of c are corroboration only; the proof of the lift for every 0<c<1/2 is the exact parameter identity in Section 3. The finite numerical cost samples are corroboration only; the asymptotic proof is the complete-annulus sum with its controlled incomplete-annulus remainder in Section 4. No numerical computation was rerun in this agent.

The source and comparison agree on the physical third curl component, the reconstruction of W.X, the positive logarithmic measure of the gaps, and the failure of each L2-plus-C/r majorant. The scalar contradiction requires neither a pressure equation nor scalar flatness. Both wording points are valid with the local omega=0 scope retained. The comparison does not establish a counterexample to LIT311, whose cost premise is absent here.

The comparison is by the existing agent configured as model. The actual provider runtime remains independently unattested. No new client or agent was used.

## 9. Precise scope of the proposed cost-window remark

Work on the specified section and exit domain of LIT311, with a positive f tending uniformly to zero, finite individual exits and a scalar completion that is continuous and zero at the center, strictly negative off the central orbit, and C1 there. Set Hf=log(1/f) and H=-S. The exact exit relation and positivity on the whole compact outer circle imply, for a bounded function C(y),

    eta log H0(y)=-Hf(y)-I(y)-C(y).

Continuity gives H0(y)->0 uniformly, so necessarily

    Hf(y)+I(y)->+infinity uniformly.                 (8)

This conclusion uses only scalar transport and closedness. To use the other side of the proposed window, additionally impose all the pressure, regularity and carrier hypotheses of the confirmed LIT311 or its C2 double-zero replacement. That full Poisson completion cannot satisfy the sufficient exclusion condition

    kappa Hf(y)+I(y)->+infinity uniformly.

Negating this limit means that there are a finite constant C0 and a sequence y_n->0 with

    kappa Hf(y_n)+I(y_n)<=C0.                       (9)

On this same sequence, (8) holds. The exact necessary window is therefore

    -Hf(y_n)+d_n <= I(y_n) <= -kappa Hf(y_n)+C0,
    d_n->+infinity.

For example one may take d_n=Hf(y_n)+I(y_n). This is a subsequence statement with an additive upper constant. It is not a pointwise bound on every trajectory, not a claim of strict separation of the ratios I/Hf from either endpoint, and not an existence theorem. The same fixed-domain versus germ restriction as LIT311 applies. For the explicit carrier here, (8) already fails along the invariant ray. For the previously excluded positive-cost carriers, the full Poisson condition fails by LIT311.

The upper restriction (9) must not be attributed to the scalar equations alone. To see the distinction exactly, use the radial base carrier in Sections 2-3 with no oscillatory summands. Then zeta=rho^-1 e_theta, Y=rho^-1 e_r, and F=rho/r obeys div(FY)=0. Define

    H0=(r f/rho)^(1/eta),
    H(Phi(y,s))=exp(-bs)H0(y).

For f=exp(-log(1/r)^2) this is positive off the orbit and extends smoothly and flatly by zero. The one-form H^-eta V.dx has no ds component and is independent of s: its scaling is exp((b eta-(1-c)+c)s)=1. Its section restriction is F zeta.dx=dtheta, which is closed on the punctured disc. Thus curl(H^-eta V)=0, hence W.grad H=0, and X.grad H=-bH holds by definition. This is a scalar-only completion despite the positive cost I=log[R rho(r)/(r rho(R))]. It is excluded as a Poisson completion, exactly as LIT311 asserts. This auxiliary observation corrects the scope of the wording, without changing any LIT314 conclusion.

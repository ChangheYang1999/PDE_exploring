# Leading hydrostatic near-axis layer and its limitations

Written independently on 2026-10-21 before the accompanying checks. The lead's two layer check programs and their output have not been read. This proof concerns a linear leading inner problem. It neither constructs a solution of the nonlinear hydrostatic equation nor changes the original IPM endpoint.

## Hypotheses, notation and exact claims

Let 0<p<1, c=1/p, D=c-1, K>0. Put

    alpha=(p+1)/2, h=alpha*p, q=h+p-1,
    s=p-1/alpha<0, A=c*(1-alpha),
    lambda=p*K/(2*alpha^2*A)>0, theta=z*d/dz.

An outer density f has degree p, is smooth off the origin and even in x, with positive-axis expansion

    f(x,y)=K*y^p+(Q/2)*x^2*y^(p-2)+O(x^4*y^(p-4)).

Its canonical hydrostatic velocity has V2=a*y^p+Cp*|x|^p+O(x^2*y^(p-2)), a=Q/[p(1-p)]. This formula is proved with its improper-integral scope in result211. Take an inner density correction u=y^q*b(z), z=x/y^alpha. Let the total nonsmooth outer velocity and this correction contribute y^h*v(z) to V2. The linear leading system is

    A*(theta-p-2)b+p*K*v=0,                              (1)
    b''+alpha^2*(theta-p)*(theta-s)v=0.                  (2)

On z>0 the functions

    B1=z^p * 2F2(-p/2,(1-p)/2; p/(p+1),2; -lambda/z^2),
    B2=z^s * 2F2(-p/2+1/(p+1),(1-p)/2+1/(p+1);
                 1+1/(p+1),2+1/(p+1); -lambda/z^2)

span the solutions without the third, z^(p+2), leading behavior at infinity. Write Oj for the coefficient of z in the small-z expansion of Bj. Then O2 is nonzero, and for every real Cp exactly one member of this span extends smoothly and evenly through0 and has leading coefficient p*K*Cp/D at infinity. It is

    b=(p*K*Cp/D)*(B1-(O1/O2)*B2),
    v=-A*(theta-p-2)b/(p*K).                            (3)

There is no arbitrary extra recessive summand in (3). Its coefficient is already fixed by choosing this combination.

These statements use the usual generalized hypergeometric functions with positive real z and positive lambda. Their asymptotics are justified below. They establish a leading formal matching mechanism only. The full canonical core and subsequent inner orders remain separate problems.

## Derivation and omitted powers

For a function y^q b(x/y^alpha), (cX.grad-1)u equals y^q[(cq-1)b+A*theta b]. Since cq-1=alpha-c=-A(p+2), the advection of u plus p*K*y^(p-1)*y^h*v gives (1). The inverse satisfies V2,yy=-g_xx. Two y derivatives of y^h v give y^(h-2)*(h-1-alpha*theta)*(h-alpha*theta)v. Also u_xx=y^(q-2alpha)b''=y^(h-2)b''. Thus (2) follows, including its sign. Eliminating v gives the especially simple exact ODE

    (theta-p)*(theta-s)*(theta-p-2)b=2*lambda*b''.       (4)

The scaling alpha is forced by q=h+p-1 and q-2alpha=h-2. The other relation h=alpha*p matches the fixed outer Cp term. No original full Laplace inverse has been replaced by a wall boundary condition here: this is the already stated hydrostatic limit, whose canonical boundary and tail conditions must still be checked.

For bounded z and smooth profiles b,v, the base velocity V2 is O(y^p), and the base V1 is O(x*y^(p-1)). Their transport of u is O(y^(q+p-1)). The x^2 term of f has y derivative O(y^(2p-2)), so its transport by y^h v has the same order. If the smooth axis term of the next outer density is already included, its derivative also contributes at this order. The inner V1 has size y^(h+alpha-1), as follows by integrating u_x on the whole tail. Its transport of f_x=O(y^(alpha+p-2)) again has order y^(q+p-1)). Finally both components of the inner self-transport have order y^(q+h-1). Relative to y^q these are y^(p-1) and y^(h-1); h<p, so self-transport is later. These are power counts after cancellation of the smooth outer hierarchy, not an error bound for an actual solution. Additional core-generated homogeneous terms, logarithms, or unmatched outer terms have not thereby been excluded.

## Hypergeometric equation and coefficients

Set t=z^(-2) and b=t^(-p/2)w(t). Then theta_z acting on b corresponds to p-2theta_t on w. Also b''=z^(-2)*theta_z*(theta_z-1)b. Substitution into (4) gives

    theta_t*(theta_t+b1-1)*(theta_t+1)w
      -X*(theta_t+a1)*(theta_t+a2)w=0,
    X=-lambda*t, a1=-p/2, a2=(1-p)/2, b1=p/(p+1).

The 2F2 power series solves this by its coefficient ratio, so both displayed Bj solve (4). The three Frobenius powers at t=0 give z^p,z^s,z^(p+2). The last can include a logarithmic lower-order term since the first and third indicial exponents differ by an integer. The two displayed series remain independent, since p-s=1/alpha is not an even integer for0<p<1. A solution with no third leading term is therefore in their span.

For general real parameters a2-a1=1/2, the algebraic terms of 2F2(a1,a2;b1,b2;-L), L>0, arise from the simple Mellin-Barnes poles at a1+n and a2+n. The leading residue at ai supplies

    Gamma(b1)*Gamma(b2)*Gamma(aj-ai)
    /[Gamma(aj)*Gamma(b1-ai)*Gamma(b2-ai)] * L^(-ai),
    j!=i.

This also follows by continuing the Mellin-Barnes integrand Gamma(a1+w)Gamma(a2+w)Gamma(-w)/[Gamma(b1+w)Gamma(b2+w)] and taking the residues at w=-ai, with the prefactor Gamma(b1)Gamma(b2)/[Gamma(a1)Gamma(a2)]. Its algebraic asymptotic series and exponentially small complementary term are the standard 2F2 expansion on the negative argument axis. Primary source: NIST DLMF16.11, especially16.11.2 and16.11.7; differential equation and resonant Frobenius interpretation: DLMF16.8.3 and16.8.6. The upper parameters here never differ by an integer, so these algebraic poles are simple. Cancellations against denominator poles are handled by the reciprocal gamma function, an entire function. The exponential term is a power of z times exp(-lambda/z^2) and is flat after even extension.

Multiplying the two residue terms by z^p yields respectively a constant and z. Thus

    O1=Gamma(b1)Gamma(2)Gamma(a1-a2)*lambda^(-a2)
       /[Gamma(a1)Gamma(b1-a2)Gamma(2-a2)].             (5)

For O2 use a1'=a1+1/(p+1), a2'=a2+1/(p+1), b1'=1+1/(p+1), b2'=2+1/(p+1). The prefactor z^s again turns the a2' term into z, giving the same formula with primes. Here a1'>0, b1'-a2'=(1+p)/2>0 and b2'-a2'=(3+p)/2>0. Its numerator is nonzero, so O2<0. In (5), the only possible zero is the reciprocal gamma factor at

    b1-a2=(p^2+2p-1)/[2(p+1)].

This quantity lies between -1/2 and1/2 and vanishes only at p=sqrt(2)-1. Hence exactly this value makes O1=0. The negative a1 in(-1/2,0) causes no additional zero.

The asymptotic expansions hold in a complex sector about positive real z of angle less than pi/4. Cauchy estimates on disks of radius proportional to z then allow differentiation of each fixed finite truncation, with an arbitrarily high power remainder. The even algebraic part and the flat part extend C-infinity to0. The odd part has nonzero one-sided first derivative and cannot extend evenly with a derivative. Therefore smooth even extension is equivalent to zero odd coefficient. The condition on the two-dimensional span is O1*C1+O2*C2=0 and O2!=0. Prescribing C1=p*K*Cp/D gives (3), uniquely. Any independently added flat solution would either change the prescribed infinity behavior or violate its exclusion of the third mode; it is not a remaining free parameter.

For completeness, Taylor coefficients cn of any smooth solution obey

    2*lambda*(n+2)*(n+1)c_(n+2)
        =(n-p)*(n-s)*(n-p-2)c_n.

For a nonzero even formal series its ratio grows linearly in n, so that series diverges as a series in z^2; it is an asymptotic Taylor series. The identically zero even series of a purely flat solution is an exception to an unqualified assertion that every even series diverges.

## Full-line inverse within the homogeneous inner model

The equation (2) loses two integration constants; checking it alone is insufficient. Assume b is the smooth even solution above, with differentiated infinity expansions inherited from Bj. For x>0, define u(x,y)=y^q b(x/y^alpha) for every y>0 for this calculation only. This expression need not be a physical smooth core. Nonetheless its canonical V2 integrals converge at both ends on each fixed x>0: as t->0, u_xx=O_x(t^(p-1))+O_x(t^p), so t*u_xx is integrable; as t->infinity it is O(t^(h-2)), and h<1.

The substitution w=z*tau^(-alpha), tau=t/y, gives the exact velocity coefficient

    I[b](z)=(1/alpha)*[z^p*int_z^infinity w^(-p-1)b''(w)dw
                      +z^s*int_0^z w^(-s-1)b''(w)dw]. (6)

Both integrals converge: near0 the second has exponent -s-1>-1, and at infinity the first has exponent -3 from the z^p asymptotic of b. The corresponding V2 has value0 at y=0 for x>0 and V2,y->0 at infinity. Its large-z expansion is

    I[b](z)=A_s*z^s+O(z^(p-2)),
    A_s=(1/alpha)*int_0^infinity w^(-s-1)b''(w)dw.      (7)

The integral in (7) also converges at infinity since p-s-3=1/alpha-3<-1. This z^s term is generated by the canonical inverse, not a freely added harmonic velocity. From (1), v has z^p coefficient Cp and a z^s term, but no faster term. The difference v-Cp*z^p-I[b] solves the homogeneous inverse equation, hence is C*z^p+E*z^s. The infinity expansion sets C=0. At z=0, v is bounded, Cp*z^p vanishes, and I[b] is bounded, while z^s diverges. Thus E=0. Consequently

    v=Cp*z^p+I[b]

holds exactly within this inner model. No additional independent condition on A_s or the flat coefficient is imposed by these canonical end conditions.

This is not a construction of the full nonlinear canonical field: u can be singular at y=0 or on the axis as y->0, and its use for all positive y was solely to establish the model inverse. A smooth physical core and overlap errors need separate construction. Cutting off u changes the inverse by terms whose sizes must be checked before asserting a matched solution.

## Fixed-line and moment repairs

Since h<p, the proposed bound g-G=O(x^2*y^(h-2)) for the total density is generally false. The leading outer density already has

    f(x,y)-f(0,y)=(Q/2)*x^2*y^(p-2)+O_x(y^(p-4)).

For Q!=0 this is not O(x^2*y^(h-2)). The inner difference alone is

    u(x,y)-u(0,y)=(b''(0)/2)*x^2*y^(h-2)+O_x(y^(h-2-2alpha)).

The corrected total bound is O(x^2*y^(p-2)), with the displayed smaller inner contribution, subject to bounds on remaining terms. This satisfies the curvature/growth estimates for gamma>=p. The formal example K*y^p+(Q/2)*x^2*y^(p-2), restricted to a cone about the positive axis, already disproves the stronger total-density estimate.

Similarly, smoothness of v implies y^h[v(x/y^alpha)-v(0)]=O_x(y^(h-2alpha))->0, which is a vanishing fixed-line velocity difference. It does not imply the existence of the renormalized moments used in3.77(a). If b''(0)!=0, the inner curvature on a fixed line is b''(0)*y^(h-2)+lower powers; after subtracting only Q*y^(p-2), the weighted integral contains int y^(h-1)dy, which diverges because h>0. The correct statement is that the leading model has the necessary vanishing velocity difference; equality of the moments follows only when those moments exist under the stated absolute hypotheses. Precisely such extra tails can violate the remainder hypotheses of3.77 without violating the leading model.

## First correction: a possible resonance, not a completed solvability calculation

Consider the linear homogeneous operator at a lower relative order beta, with density exponent q+beta and velocity exponent h+beta. Its two inverse roots and transport root are

    m=p+beta/alpha, n=m-1/alpha,
    t=p+2-beta/(1-alpha).

Elimination gives (theta-m)(theta-n)(theta-t)B=2*lambda*B''. The same transformation produces parameters

    a1=-m/2, a2=(1-m)/2,
    b1=1-1/(2alpha), b2=2-beta/[2alpha(1-alpha)].

The coefficient controlling the odd component of the n-branch contains the reciprocal gamma factor

    1/Gamma((1+m)/2).

At the first base-feedback order beta=p-1, m ranges from -2 to1 as p ranges from0 to1. It equals -1 exactly at

    p=sqrt(5)-2, c=sqrt(5)+2.

At this value the odd coefficient of the n-branch vanishes, while that of the m-branch is nonzero: for the latter, a1=1/2, a2=1, b1-1=-1/(p+1) is not an integer, and b2-1>0. Thus the free n-branch coefficient cannot in general cancel a prescribed odd mismatch at this correction order. An inhomogeneous matching problem can have a scalar compatibility condition there. This statement about the homogeneous connection map is proved by the same residue calculation, or at the resonant point by cancelling a common upper/lower parameter of the n-branch 2F2 to1F1. It does not show that the actual forcing violates a condition. The forcing, logarithmic terms if required, intervening core terms and their matching coefficients remain OPEN. It would be incorrect to infer arbitrary-order formal solvability from the leading two-plane count.

## Scope, dependencies and evidence

The leading system, its parameter algebra, connection coefficient zeros and model inverse have been independently derived. The total fixed-line bound and unqualified moment assertion need the repairs above. Primary sources were consulted through the read-only web tool: NIST DLMF16.8 and16.11. Attempts to download separate TeX equation files through Python received403; that failure is recorded in verification/sources/MANIFEST.json, not described as a successful retrieval. Numerical and symbolic checks will be stored alongside this proof. A later nonlinear solution, a full far-field expansion, a hydrostatic nonexistence result and either original-IPM decisive endpoint are all OPEN.


## Additional inverse error control and outer-completion caveat

The Gaussian inverse manufacture uses b(z)=exp(-z^2), so b''=(4z^2-2)exp(-z^2). Formula(6) is an explicit combination of upper/lower incomplete gamma integrals. A separate integral in physical t first encountered the expected slow convergence of the algebraic tail when h is close to1. To control this, set u=(y/t)^(1-h) in its upper tail. The exact transformed upper contribution is

    y^h/(1-h)*int_0^1 [4*z^2*u^(2alpha/(1-h))-2]
                     *exp(-z^2*u^(2alpha/(1-h))) du.

This removes the algebraic endpoint weight and retains an integral distinct from the incomplete gamma formula. The initial failed numerical tolerance is preserved, not hidden or treated as failure of the analytic inverse identity.

The leading inner power counts cannot, without additional outer information, assert that all errors are of relative order y^(p-1) or y^(h-1). Here is an explicit mathematical reason. Put d=2p-1 and choose a nonzero nonnegative smooth function F supported in1<s<2. Away from the origin define an outer correction H(x,t)=|x|^d F(t/|x|) for t>0, with the even-x/odd-y extension and a smooth radial cutoff at the origin. At large x the cutoff is absent. For y>2|x| the density and its local derivatives vanish, V1[H](x,y)=0, but the canonical vertical velocity is

    V2[H](x,y)=|x|^d*(d+1)*(d+2)*int_0^infinity s F(s) ds.

Indeed H_xx=|x|^(d-2)[d(d-1)F-2(d-1)s F'+s^2 F'']; integrating t H_xx and integrating by parts twice, with no boundary terms because F is compactly supported, gives the coefficient (d+1)(d+2). The tail is zero in this region. The cutoff ensures a smooth admissible function locally; its outer growth is sublinear since d<1. In inner variables with fixed z>0, this velocity is of order y^(alpha*d), a relative factor y^(alpha*(p-1)) compared to y^h. This factor decays more slowly than y^(p-1).

The example does not solve the outer transport equation and does not give freedom to change the uniquely specified f_d of a solution. Its purpose is precise: local inner smoothness and the leading trace alone do not control the first omitted inverse contribution. The full specified outer completion must be checked or subtracted, including its constants; the two powers in the lead's claim describe the listed local interactions only. The inverse's nonlocal dependence cannot be discarded in an error estimate. The first-feedback homogeneous resonance computed above is at beta=p-1 and remains a statement about that operator, not proof that no earlier corrections occur.

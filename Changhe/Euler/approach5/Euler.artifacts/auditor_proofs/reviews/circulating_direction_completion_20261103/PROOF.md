# Circulating direction and logarithmic variation exclude a negative scalar completion

Status: local conditional theorem CONFIRMED A2607-A2610, with complete comparison A2613. Unrestricted extensions remain OPEN A2614. The carrier and direction assumptions are not proved for all rotating Euler tails.

## 1. Exact theorem

Fix 0<c<1/2, omega in R, Jx=e3 cross x, A=cI-omega J, X=Ax, L=(1-c)I+omega J, a=1-2c, b=2(1-c) and eta=a/b in (0,1/2). Let sigma be a smooth transverse section on a disc D_R in R2, sigma(0)=x0!=0, and let Phi(y,s)=exp(sA)sigma(y) be a finite smooth flowbox. Write Gamma=Phi({0},s).

Suppose a smooth vector field V on this flowbox satisfies

    div V=0, X.V=0, DV X=-LV,

is infinitely flat on Gamma and nonzero off Gamma. Let W=curl V. Suppose a positive smooth radial f(r), r=|y|, is flat in value at zero, meaning f(r)=O(r^N) for every N>0, and suppose

    sigma^*(V.dx)=f(r) zeta(y),
    c1 f(r)<=|V(sigma(y))|<=c2 f(r),
    zeta.e_theta>=d0>0, |zeta|<=D0,
    |D zeta(y)|<=q(r),
    integral_r^R q(t)dt<=K0+K1 log(R/r).                 (1)

Here zeta is a smooth planar one-form on the punctured disc, e_theta=(-sin theta,cos theta), c1,c2,d0,D0 are positive finite constants, K0,K1 are finite nonnegative constants, and q is nonnegative and locally integrable. Derivative and coefficient norms are Euclidean in the fixed section. Take R inside the section domain so that the outer circle is smooth and all relevant fields extend to it.

There is no smooth scalar S near x0 with

    X.grad S=-bS, W.grad S=0,
    S<0 off Gamma, S=0 on Gamma,
    -Delta(S+|V|^2/2)=tr((DV)^2).                        (2)

No sign of tr((DV)^2) is assumed. No uniformity in omega of the constants is asserted. The proof implies scalar flatness from (1)-(2); it is not a separate hypothesis.

## 2. Closedness and the integrating factor

Assume (2) and put H=-S, E=|V|^2. Differentiating X.V=0 and using the carrier equation gives X cross W=aV. Also X.grad H=-bH and W.grad H=0. The triple-product formula therefore gives

    a grad H cross V
       =grad H cross(X cross W)
       =X(grad H.W)-W(grad H.X)=bH W.

It follows, with eta=a/b, that curl(H^(-eta)V)=0 wherever H>0. This is an exact identity of smooth one-forms off Gamma, so its pullback to the punctured section is closed. Define

    F=f H(sigma(y))^(-eta)>0, Y=(zeta2,-zeta1).

The closedness equation is div(FY)=0. The sign is checked directly: its left side is partial_1(F zeta2)-partial_2(F zeta1). Moreover

    Y.e_r=zeta.e_theta>=d0, |Y|<=D0,
    |div Y|<=sqrt(2)|D zeta|.                           (3)

A forward Y-orbit starting at radius r>0 reaches radius R in time at most (R-r)/d0. Indeed its radius is strictly increasing; while its radius stays in [r,R], smoothness and compact-annulus continuation prevent finite-time breakdown. If it failed to reach R by that time, integrating dr/dtau>=d0 would be a contradiction. This argument asserts no continuation through the centre.

Parameterize such a trajectory by its increasing radius. From div(FY)=0,

    d(log F)/dr=-(div Y)/(Y.e_r).

Its integral is bounded in absolute value by (sqrt(2)/d0)[K0+K1 log(R/r)]. On the outer circle the smooth positive F has a positive minimum and finite maximum. Thus, after absorbing powers of fixed R into the constant, for some C>=1 and K>=0,

    C^(-1) r^K<=F(y)<=C r^(-K).                         (4)

The orbit may wind arbitrarily often. Its angle does not affect this estimate because q bounds every angle at each radius.

## 3. Scalar flatness and dominance of energy

Solving for H and using (4) and the velocity comparison gives, on the section,

    H=(f/F)^(1/eta)<=C f^(1/eta) r^(-K/eta),
    E/H>=C^(-1)r^(K/eta) f^(2-1/eta).                   (5)

The first bound makes H flat in value. The exponent 2-1/eta is strictly negative. For the second bound, choose N so large that N(1/eta-2)>K/eta. The bound f(r)<=C_N r^N then forces its right side to infinity as r tends to zero, uniformly in angle. Hence E/H tends uniformly to infinity on the punctured section.

The carrier equation and skew-symmetry of J give X.grad E=-bE. Equation (2) gives the same scaling for H. Thus both scale by exp(-bs) and E/H is unchanged along the X-flow. On a compact time interval the flowbox and its inverse have bounded derivatives. In particular |y|<=C|x-x0| near x0. Formula (5) and bounded transport factors imply H(x)=O(|x-x0|^N) for every N, and E/H tends uniformly to infinity as x tends to x0 off Gamma. Smoothness of H makes every Taylor coefficient vanish at x0: a first nonzero homogeneous Taylor polynomial would contradict this value estimate on a ray.

## 4. The local tensor lemma, including the centre flux

Shrink to a Euclidean ball about x0 where E>=4H off Gamma. Let

    P=E/2-H, T=V tensor V+P I.

Then

    (E/4)I<=T<=(3E/2)I, div div T=0.                   (6)

The inequalities extend over Gamma by continuity. The differential equation follows by expanding div div(V tensor V)=tr((DV)^2) for div V=0 and using (2). The tensor is smooth and flat at x0 because V and H are flat there.

Translate x0 to the origin and let averages below be normalized surface averages over the unit sphere. Define

    A(r)=average n.T(rn)n,
    B(r)=average [tr T(rn)-n.T(rn)n].

The divergence theorem applied to div T on the entire ball gives integral_(sphere_r) n.div T=0. There is no puncture in this application, since T is smooth at the centre. To compute the average integrand, use

    div(Tn)=n.div T+[tr T-n.Tn]/r.

The average of div(Tn) is A'(r)+2A(r)/r, since the tangential divergence on the sphere integrates to zero. Therefore

    A'(r)=[B(r)-2A(r)]/r.                               (7)

If e(r) is the spherical average of E, (6) gives A>=e/4 and B<=3e, so B<=12A. Consequently (A(r)r^(-10))'<=0. For 0<r<r1 this yields

    A(r)>=(r/r1)^10 A(r1).

Flatness gives A(r)=O(r^N) for every N. Letting r tend to zero after choosing N>10 proves A(r1)=0. Since E is nonnegative and continuous, its zero spherical average forces E=0 on every sufficiently small sphere. Hence V=0 on a ball, contradicting nonzero V off Gamma. This proves the theorem without any assumed trace sign, boundary regularity of a zero set, or flux at infinity.

## 5. Application to specified smaller-amplitude envelope carriers

Use the independently checked carrier constructions of A2580-A2586 and A2588-A2595. Their section one-form is Mw, where M=g/j is a smooth positive definite matrix and

    w=f e_theta+p+q0 e_r,
    |p|<=C epsilon f, |q0|<=Crf, |D(q0 e_r)|<=Cf.        (8)

Here q0 is the whole radial Volterra correction. On a fixed compact disc let m0>0 be the minimum eigenvalue of M. First choose epsilon>0 small enough that |Mp|<=m0f/4, and then shrink the radius to give |Mq0 e_r|<=m0f/4. These choices precede the envelope lambda. Then zeta=Mw/f satisfies zeta.e_theta>=m0/2 and |zeta|<=D0. The velocity remains comparable to f.

The normalized radial correction obeys

    |D[(q0/f)e_r]|<=C[1+r f'/f],                       (9)

by (8) and the product rule. The envelope construction has r f'/f=Lambda(log(1/r)) with bounded first derivative of Lambda and at most linear growth; the logarithmic construction has r f'/f=log log(1/r)+1. Thus (9) is bounded by C/r after shrinking. The derivative of M e_theta is also O(1/r).

For a bump at rn=2^(-n) with radius elln, narrow-annulus comparison gives

    |D(p/f)|<=C[elln^(-1)+f'/f]
              <=C elln^(-1)

on its support. The last inequality follows from elln=rn/[100(1+Lambda_n)^2] and the bounded derivative of Lambda; it also holds for the cubic widths elln=rn^3/100 of the logarithmic construction. Off these supports p is zero. Therefore, with In=(rn-elln,rn+elln),

    |D zeta|<=C/r+C sum_n elln^(-1) 1_In(r).             (10)

The intervals are disjoint, and each contributes at most 2C to its radial integral. If In meets [r,R], rn>=r/1.01, so there are at most C0+C1 log(R/r) such intervals. Integrating (10) proves (1).

Reducing a fixed positive epsilon does not remove the dominant indefinite Hessian at sufficiently late bump centres, the metric cancellation, or the subcritical and envelope estimates. The choices of all constants before lambda remain in the same order. Thus these specified smaller-amplitude versions of LIT306-LIT308 retain both trace signs and, in the metric-adjusted case, unbounded strain-to-vorticity ratio, while admitting no scalar (2). No assertion is made that every unmodified amplitude meets the direction bound for every section metric.

## 6. Scope and comparison

This is a conditional obstruction using a definite angular component of the normalized section form and logarithmically bounded accumulated variation. It does not exclude carriers whose normalized form changes that angular sign or violates the variation bound. It does not prove unrestricted nonexistence of smooth decaying Euler profiles, nor construct or preclude completions with other scalar signs or zero sets.

All six sections of the submitted LIT309 source were read. The independent proof explicitly checks the weighted closedness sign, forward annulus exit, angularly uniform radial integration, uniform flowbox transfer, centre flux and monotonicity direction in the local tensor argument, and the normalized sparse-bump derivative. No numerical calculation or formal build is required. The existing coordinator comparison is complete.

The full eleven-item coordinator comparison, its four wording points and its concluding consistency check were read. All four source and independent proofs agree. The inverse-flowbox Lipschitz transfer and shrinking of the outer circle are explicit here; only a lower bound on F is needed. The sparse application retains a smaller fixed positive amplitude chosen before the envelope. The comparison is pinned in the team records. The existing configured model agent supplied this comparison through files; actual provider execution is independently unattested. No client or extra agent was started. No gap was found in the stated conditional theorem.

# Exact sector profiles with a nonzero harmonic pressure remainder


Audit completed 2026-11-03T18:12:23.335190+00:00; verdicts A1989-A1994 in the auditor's ledger (AUDIT_LEDGER.md). Exact positive statements are CONFIRMED; the excluded extensions remain OPEN.
Independent audit of LIT279. Verdicts are assigned in the auditor's ledger (AUDIT_LEDGER.md) after the complete argument is read. This result concerns an invariant open sector, not a profile smooth on all of R3.

## 1. Exact statement and notation

Fix 2/5<c<1/2 and an arbitrary finite real omega. Let a=1-2c, d=1-c, b=2d, Jx=e3 cross x, A=cI-omega J, X=Ax and L=dI+omega J. Thus a>0, b-a=1 and aI+A^T=L. Write F_t=exp(tA), R_t=exp(-omega tJ). Let D be an open subset of R3 minus{0}, invariant under F_t for every real t. Suppose f,Q are real smooth harmonic functions on D with X.grad f=-af and X.grad Q=-bQ.

Then

    V=-grad f/a, phi=-f/a+Q,
    U=grad phi, P=Q-|U|^2/2

solve div U=curl U=0 and LU+DU(X+U)+grad P=0 on D. Their natural tails are exactly V and P2=Q-|V|^2/2, so Q=P2+|V|^2/2 is the harmonic pressure remainder. For every such c,omega one can choose D,f,Q so that Q is nonzero, V is nowhere zero, and S=P2-|V|^2/2 satisfies

    (2/3)|S|<=|V|^2<=2|S|,
    grad(X.V) cross grad S!=0

throughout D. The exterior original velocity and its first derivative obey the natural upper bounds, the velocity obeys a matching lower bound, and its sector energy is infinite. No extension across the origin or missing directions is asserted.

## 2. Momentum and the two scalar degrees

For any harmonic phi, U=grad phi has zero divergence and curl. Direct differentiation with the transpose gives

    grad(a phi+X.grad phi)
      =(aI+A^T)U+D2phi X=LU+DU X.

Also DU U=grad(|U|^2/2). For the stated phi, the f terms cancel and

    a phi+X.grad phi=(a-b)Q=-Q.

Consequently LU+DU X+DU U+grad P=0 exactly. This check varies velocity and pressure together: adding Q to pressure alone would not preserve momentum. Taking divergence verifies the profile pressure Poisson equation on D. No pressure uniqueness or normalization on the whole space is needed.

Differentiate the scalar homogeneities. They give

    V(F_t x)=e^(-dt) R_t V(x),
    grad Q(F_t x)=e^(-(b+c)t) R_t grad Q(x).

Since b+c=d+1 and b=2d,

    e^(dt) R_t^(-1)U(F_t x)=V(x)+e^(-t)grad Q(x),
    e^(bt)P(F_t x)=Q(x)-|V(x)+e^(-t)grad Q(x)|^2/2.

These are identities of smooth functions of x, so differentiating them gives convergence in every local smooth norm as t tends to infinity. Furthermore X.V=f. Thus the rank scalar is f and the actual tail scalar is S=Q-|V|^2. The velocity potential is phi, which differs from f.

## 3. A globally single-valued branch on a spiral sector

Put sigma=omega/c. For n on a sufficiently small disk about e1 in S2 with compact closure in {n1>0}, let theta(n)=arg(n1+i n2), with the continuous choice theta(e1)=0. Define

    pi(x)=exp(sigma log|x| J)x/|x|,
    D={x!=0: pi(x) in O}, z=x1+i x2,
    ell(x)=log|z|+i[theta(pi(x))-sigma log|x|].

The map (r,n)->r exp(-sigma log r J)n identifies D with (0,infinity) times O. In particular it is open, avoids the vertical axis, and is invariant under all F_t. The identity exp ell=z makes ell locally a branch of log z. Its x3 derivative is zero locally, including where its explicit formula uses |x|: the local logarithm identity gives its derivatives without treating the lifted argument modulo 2pi. Since pi(F_t x)=pi(x),

    ell(F_t x)=ell(x)+(c-i omega)t.

Let lambda=-a/(c-i omega), mu=-b/(c-i omega), and choose

    f=Re(i exp(lambda ell)),
    Q=epsilon Re(exp(mu ell)).

These are smooth and locally real parts of holomorphic functions of z, hence harmonic in R3. The exact flow increment proves both required scalar degrees. For epsilon!=0, Q(e1)=epsilon, so the remainder is not zero. The holomorphic derivative of i exp(lambda ell) is i lambda exp((lambda-1)ell), which never vanishes. Therefore grad f and V never vanish on D.

## 4. Rank and ratio on a fixed angular disk

Write lambda=u+iv and E0=|lambda|^2/a^2. At e1 the two horizontal gradients at epsilon=0 are

    grad f=(-v,-u,0),
    grad(-|V|^2)=-2E0(u-1,-v,0).

Their cross product is -2E0(|lambda|^2-u)e3. Since u=-ac/(c^2+omega^2)<0, it is nonzero for every finite omega, including omega=0. Choose O smaller with compact closure where this cross product and E=|V|^2 both have strictly positive lower bounds in norm and value respectively.

The functions Q/epsilon and their first derivatives are bounded on that closure. A sufficiently small fixed nonzero epsilon therefore preserves nonzero grad f cross grad(Q-E) there and gives |Q|<=E/2. Hence S=Q-E<0 and E/2<=|S|<=3E/2, which is precisely (2/3)|S|<=E<=2|S|.

Both Q and E scale by e^(-bt). The gradients of f and S scale by a positive exponential times the same proper rotation. Their cross product therefore also scales by a nonzero exponential and a rotation. All inequalities and rank nonvanishing extend to the entire invariant D. The angular aperture stays fixed after the choices of O and epsilon. Neither the aperture nor epsilon is claimed uniform in omega.

## 5. Natural exterior bounds and infinite energy

The formulas of Section 2 and bounded angular derivatives imply, with p=d/c in (1,3/2), for r=|x|>=1 in this D,

    |U(x)|<=C r^(-p), |DU(x)|<=C r^(-p-1),
    |U(x)-V(x)|<=C r^(-p-1/c).

For example DV has flow factor e^(-(d+c)t)=e^(-t), while D2Q has factor e^(-(b+2c)t)=e^(-2t). Thus the derivative estimate respects the extra spatial derivative. Compact angular closure gives |V(x)|>=v r^(-p) for a v>0. Increase the exterior radius to make the correction at most half this bound. Then |U(x)|>=v0 r^(-p).

At each radius the angular cross-section is a rotation of O and has its fixed positive spherical area. Therefore the sector energy is at least

    v0^2 area(O) integral_R^infinity r^(2-2p) dr=infinity,

because 2-2p>-1. This is a direct lower bound; it does not insert a finite-energy assumption or integrate across an unproved side boundary.

## 6. Verdict scope and dependencies

The identities, branch, perturbation, bounds and energy calculation establish every stated sector conclusion. They refute the inference Q=0 from local full momentum, irrotationality, natural sector bounds, positive bounded tail ratio and a nonzero leading velocity. The solution omits the origin and a nonempty set of directions and provides no vortical support or matching jets. It is not a counterexample to the campaign conjecture. It does not remove the global or additional regularity hypotheses in LIT275, LIT277 or LIT280.

The proof uses elementary differentiation and local holomorphic calculus. The branch mechanism also appears in the independently confirmed LIT273, but is reconstructed here. All six sections of the pinned LIT279 source were read. The source and its actual-time hash manifest are in the team records. No numerical computation or formal build was used. The existing configured model agents receive findings through the agent notes; provider runtime identity remains independently unattested.

# Tail growth and negative-order integrability

## Exact numerical tail representation

The archived potential generators are

    chi_(j,m,k)=r^(2k)(1+r^2)^(p_j-k) cos(2m theta),
    2p_j=3+gamma-j(1-gamma), gamma=1/c_l,
    j=0,1,2,3; m=0,...,9; k=m,...,25.

The potential determines rho=-partial_y Delta chi and psi=partial_x partial_y chi. For r>1, the binomial expansion is absolutely convergent, together with every fixed finite number of derivatives, on r>=R>1. Thus the leading potential term in branch j is

    r^(3+gamma-j(1-gamma)) sum_m C_(j,m) cos(2m theta),
    C_(j,m)=sum_(k=m)^25 a_(j,m,k).

For a potential term C r^s cos(n theta), elementary polar differentiation gives density exponent s-3 and coefficients

    sin((n+1)theta): -C(s^2-n^2)(s-2-n)/2,
    sin((n-1)theta): +C(s^2-n^2)(s-2+n)/2.

The stream function has exponent s-2 and coefficients

    sin((n+2)theta): +C(s-n)(s-n-2)/4,
    sin((n-2)theta): -C(s+n)(s+n-2)/4.

Negative sine indices are folded using sin(-k theta)=-sin(k theta). These formulas include n=0 after both contributions are combined.

If rho=r^p F(theta) and psi=r^t P(theta), the nonlinear advection is

    U dot grad rho = r^(p+t-2)[-p P'(theta)F(theta)+t P(theta)F'(theta)].

Consequently the residual has leading candidate exponent 2gamma-1. The nominal r^gamma term vanishes identically because c_l gamma=1. Its coefficient at r^(2gamma-1) is E1, containing the linear branch-1 term and the branch-0 self-advection. Since the branch-1 density has sine modes only up to 19, its linear part cannot affect sine mode 39.

## Nonzero leading residual of the actual checkpoints

Put n=18, s=3+gamma and C=C_(0,9). The highest density and stream coefficients from branch 0 are

    A=-C(s^2-n^2)(s-2-n)/2,       B=C(s-n)(s-n-2)/4.

The sin(39 theta) coefficient of E1 is exactly

    e39=(19-gamma) A B/2.                                            (1)

For each supplied checkpoint 88 and 131 the independently reconstructed exact rational C is nonzero, 0<gamma<1, and (1) is strictly negative. The checks use exact rational arithmetic, not a floating-point threshold. Their complete inputs, coefficient tables and interval enclosures are in `verification/state088_tail.json` and `state131_tail.json`; the independent program is `verification/check_tail.py`.

For state131, rounded displays are

    c_l=1.810319210199998,
    2gamma-1=0.10477753797853508,
    e39=-7.698363346447813e-7,
    ||E1||_(L2(0,pi/2))=0.0910394455355629.

The corresponding state88 norm is 0.12112557210824139. The coefficient norms are enclosed by Arb with exact rational input. This certifies the stated finite computations subject to the arithmetic library, not the numerical profile's proximity to a true solution.

The remainder after E1 is uniformly lower order in theta because the finite family has a convergent differentiated binomial expansion. Since e39 != 0, E1 is nonzero in angular L2. Hence

    ||F(rho)(r,.)||_(L2(0,pi/2)) / r^(2gamma-1) -> ||E1|| > 0.

Both exponents are positive, so the unnormalized density residual grows. A forcing space imposing boundedness or decay on this residual cannot contain the actual background defect. Smallness of the archived normalized residual R_f=R_rho/y does not fix this incompatibility.

## A sharp tail obstruction for ordinary homogeneous H^-1

Consider a smooth function g on R^2 which is odd in y and even in x, and equals r^beta sin(m theta) for r>=2, where m is a positive odd integer and beta is real. Then

    g belongs to homogeneous H^-1(R^2) if and only if beta<-2.           (2)

Here membership means existence of a distributional potential Phi with -Delta Phi=g and grad Phi in L2, equivalently continuity on the homogeneous H^1 test space. Smooth modifications on a bounded set with the same odd symmetry do not change the conclusion.

For necessity, choose a smooth radial cutoff chi supported in 1<r<2 with integral chi(r)r^(beta+1)dr nonzero and take test functions phi_R=chi(r/R)sin(m theta), supported on disjoint dyadic annuli. Their gradient L2 norms are independent of R, while <g,phi_R> is a nonzero constant times R^(beta+2). If beta>-2, the dual norm is therefore infinite. At beta=-2, choose N such tests on disjoint annuli and add them. Pairing grows as N while the gradient norm grows as sqrt(N), again contradicting a bounded H^-1 norm.

For sufficiency, solve the polar radial ODE for this single angular mode. Away from resonances,

    Phi_tail=-r^(beta+2)sin(m theta)/((beta+2)^2-m^2).

Its gradient is O(r^(beta+1)), square integrable at infinity precisely when beta<-2. At the possible resonant exponent beta+2=-m, replace the particular solution by a constant times r^(-m)log(r)sin(m theta); its gradient is still square integrable since m>=1. A smooth radial continuation through the inner region leaves a compactly supported odd forcing error. Such an error has zero integral; its Newtonian potential has gradient O(r^-2) at infinity and a locally square-integrable gradient. Adding that correction proves sufficiency. The case beta+2=+m is outside beta<-2.

This proof extends to any fixed nonzero smooth angular profile with odd sine modes: necessity uses a test angular profile with nonzero pairing, and sufficiency follows by angular mode estimates when the angular regularity is sufficient. The single-mode statement (2) alone already disproves any proposed space admitting arbitrary leading tails under the incompatible weights below.

## Consequence for the weight in the prompt

Let w_s=(1+r^2/R0^2)^(-s/2), R0>0. A free leading perturbation h=r^gamma sin(m theta) at infinity gives w_s h asymptotic to R0^s r^(gamma-s)sin(m theta). The same annular proof and radial ODE show

    ||grad(-Delta)^(-1)(w_s h)||_2 < infinity  iff  s>2+gamma.

The limiting positive-matrix condition of the weighted energy in `../02_energy/PROOF.md` is s<2+gamma. There is no overlap. At equality the energy diverges logarithmically; the endpoint does not repair the problem.

For the first correction tail r^(2gamma-1)Theta_1, the lower integrability threshold is instead s>1+2gamma. Thus the heuristic window

    1+2gamma < s < 2+gamma

can apply only after the leading tail is fixed or explicitly extracted. It cannot include a freely varying leading angular profile. Exponent variation produces r^gamma log(r) terms, which also fail at or below the leading-tail threshold.

## Subtraction order and scope

The formal nonlinear hierarchy has p_n=n gamma-(n-1)=1-n(1-gamma). If the first N orders are extracted and the remainder really has a controlled first omitted power p_(N+1), ordinary H^-1 requires p_(N+1)<-2, equivalently (N+1)(1-gamma)>3. For state131 and state88 the smallest possible N is 6. This is a threshold calculation, not a proof that a six-order expansion exists, that its angular equations are solvable, or that its logarithmic terms are controlled. Each of those conditions remains separate.

The leading angular profile belongs to an infinite-dimensional function space. Treating all its variations as one scalar, or changing c_l while omitting derivatives of r^(p_n(c_l)), does not define the full tangent space.

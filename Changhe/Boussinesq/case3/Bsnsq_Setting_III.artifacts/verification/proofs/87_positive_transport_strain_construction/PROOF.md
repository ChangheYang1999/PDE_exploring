# Positive vorticity, exact temperature transport, and one strain identity

Date: 2026-10-20. Status: complete independent informal proof, independently re-derived by the lead and checked by the verifier; the additional lead referee audit was read in full and its justified precision fixes adopted at 2026-10-20T23:39:14.864539+00:00. This is a construction of nonprofiles. It establishes neither existence nor nonexistence for the coupled Boussinesq equations. The proof does not depend on the numerical signs in packet86.

## 1. Statement and notation

For every beta>2 there are smooth real fields Omega,Theta,Psi on the full plane such that, with nu=1/beta, c=1+beta/2, lambda=(beta-2)/2, V=(-Psi_y,Psi_x) and W=beta X+V:

1. Omega=-Delta Psi, and V is the canonical centered full-plane inverse, with V(0)=0. There is no added harmonic strain. Psi and Omega are odd in x, Theta is even in x, and no y-reflection is imposed.
2. Omega>0 on x>0. At the origin, Psi_xy=c, Omega=b0 x+O(r^3) with b0>0, and Theta=a0 x^2+O(r^3), where a0=beta b0/4. Also Theta=0 exactly on x=0 and Theta>0 off that axis.
3. W.grad Theta=(beta-2)Theta holds exactly everywhere. There is a fixed kappa>0 such that W(X).X>=kappa |X|^2. Thus every nonzero backward orbit tends to0 and every nonzero forward orbit escapes.
4. Omega=mu r^(-nu)cos(theta)+O(r^(-nu-2)), with mu>0. The velocity is sublinear, V=O(r^(1-nu)), and Theta=O(r^(1-2nu)), grad Theta=O(r^(-2nu)). The corresponding differentiated source and velocity bounds hold at every order.
5. With K=xy/r^4 and g=K_x, all the following integrals are ordinary absolutely convergent full-plane integrals, and the single strain identity holds:

       int Omega V.grad K - (1/2) int Theta V.grad g = pi c.       (S)

6. The vorticity equation W.grad Omega+Omega=Theta_x fails at every sufficiently large point of the positive horizontal ray. In particular these are not B2 profiles and are not members of the profile subclass G, despite satisfying its global-flow condition.

A positive spatial dilation can impose a0=1. The construction retains strictly positive vorticity and a nonzero slow tail after this normalization. The first angular mode makes the absolute integral for an uncentered vertical drift divergent. All inverse assertions here use the admissible centered relative law, not an absolute drift value or the fixed-center B1 condition.

Polar angle theta is measured from the positive x-axis. A dot over a radial cutoff denotes r d/dr, equivalently differentiation in log r.

## 2. Smooth cutoffs and the positive source

Fix smooth radial cutoffs eta,kappa0 with values in[0,1], satisfying

    eta=0 on r<=1, eta=1 on r>=2,
    kappa0=0 on r<=1/2, kappa0=1 on r>=1.

Choose a constant K0>=48 large enough that

    4 |12eta-4 dot eta-ddot eta| <= K0 kappa0                (1)

for all r. This is possible because the expression vanishes for r<=1 and is bounded on[1,2], while it equals12 for r>=2.

Fix a smooth nonincreasing cutoff chi(s), equal to1 for s<=0 and0 for s>=1. Choose a smooth nonnegative zeta, supported in[0,1], such that zeta>=|chi'|+|chi''|. For an explicit existence construction, let chi' be a negative normalized multiple of rho(s)=exp(-1/[s(1-s)]) on(0,1); a sufficiently large multiple of exp(-1/[2s(1-s)]) dominates both |chi'| and |chi''| and is smooth and flat at the endpoints.

Choose b_*>0 so small that

    4b_* <= lambda/8, K0 b_* <= lambda/8,
    b_* < 36c/K0^2.                                      (2)

Choose L>0 sufficiently large that, for

    J_L(t)=(4/L+1/L^2) zeta(t/L),

one has (c+4b_*) sup J_L<=lambda/8. Finally let R>2, to be increased later, and put

    chi_R(r)=chi(log(r/R)/L),
    J_R(r)=J_L(log(r/R)).

For b in[0,b_*] and small delta,mu>=0, define

    q(r)=K0 b kappa0(r) chi_R(r)+(c+4b)J_R(r)
         +delta r exp(-r^2)+mu r(1+r^2)^(-(1+nu)/2),
    Psi_2=(c/2)r^2 sin(2theta) chi_R(r),
    Psi_4=b r^2 sin(4theta) eta(r) chi_R(r).                (3)

Both angular stream functions are smooth: Psi_2=cxy near0, and Psi_4 vanishes near0. Their vorticities have the form q2(r)sin(2theta), q4(r)sin(4theta), where

    q2=-(c/2)(4 dot chi_R+ddot chi_R),
    q4=b[12eta chi_R-4 dot(eta chi_R)-ddot(eta chi_R)].     (4)

The supports of derivatives of eta and chi_R are disjoint. On the inner transition, (1) bounds4|q4| by K0 b kappa0 and q2=0. On the outer transition eta=kappa0=1, and

    2|q2|<=c J_R,
    4|q4|<=48b chi_R+4b J_R.

On the plateau2<=r<=R one has q2=0, q4=12b, and q=K0 b plus the two positive small additions. It follows everywhere that

    q(r)>=2|q2(r)|+4|q4(r)|
           +delta r exp(-r^2)+mu r(1+r^2)^(-(1+nu)/2).     (5)

Let Psi_1=p(r)cos(theta) be the centered canonical inverse of q(r)cos(theta), defined explicitly by

    p(r)=-(1/2)[r int_0^r q(s)ds-r^(-1)int_0^r s^2q(s)ds]. (6)

Set Psi=Psi_1+Psi_2+Psi_4 and Omega=-Delta Psi. Since |sin(2theta)|<=2|cos(theta)| and |sin(4theta)|<=4|cos(theta)|, (5) proves strict positivity of Omega on x>0 whenever delta+mu>0. Near the origin q=(delta+mu)r+O(r^3), so

    Psi_1=-(delta+mu)r^3 cos(theta)/8+O(r^5),
    Omega=(delta+mu)x+O(r^3), Psi_xy(0)=c.                 (7)

The angular cutoffs are absent there. Formula(6) has zero linear harmonic coefficient at the origin; it is exactly the centered, rather than freely strained, inverse. At infinity the compact angular modes vanish and

    p(r)=-mu r^(2-nu)/[(1-nu)(3-nu)]+C r+O(r^(-nu))+O(r^-1).

Thus the relative stream is subquadratic and the velocity sublinear. Uniqueness of this inverse follows from the harmonic difference: a smooth entire harmonic function of subquadratic growth has only constant and linear terms, which are removed by oddness/additive normalization and centering of the velocity. Equivalently (6) is the directly integrated regular mode1 Poisson equation with precisely that centering. The compact modes have their ordinary whole-plane inverses, since their displayed stream functions vanish outside a compact set. No wall or exterior multipole is used.

## 3. Uniform outward transport and exact temperature

Write h=p/r. Direct differentiation of(6) gives

    h'(r)=-r^(-3)int_0^r s^2q(s)ds, h(0)=0.              (8)

If 0<=q<=A, then |h'|<=A/3 and |p|<=A r^2/3. Each of the last two functions in q is bounded by its coefficient delta or mu. Restrict these coefficients so delta<=lambda/16 and mu<=lambda/16. Equations(2)-(3) then give A<=3lambda/8. Since the radial velocities of the three modes are p sin(theta)/r, -c r cos(2theta)chi_R and -4b r cos(4theta)eta chi_R,

    W_r/r >= beta-c-4b_*-A/3 >= 3lambda/4.               (9)

This estimate is uniform in R and in all the selected parameters. Completeness follows from linear growth; (9) gives both global backward convergence and forward escape directly.

The smooth even function Q1=lambda-W1/x extends across the axis and vanishes at0. Define, using the complete flow phi_t,

    u(X)=int_0^infinity Q1(phi_(-t)(X))dt,
    xi(X)=x exp(u(X)), a0=beta(delta+mu)/4,
    Theta(X)=a0 xi(X)^2.                                (10)

This is a smooth construction and W.grad xi=lambda xi. Here are the convergence details, also needed for parameter continuity below. At0, DW(0)=diag(lambda,beta+c), and near0 DW(X)=DW(0)+O(r), uniformly on the fixed compact parameter box. In fact Q1=-(delta+mu)y/4+O(r^3), so Q1=O(r); no quadratic vanishing is needed. In a fixed smaller neighborhood, the reversed flow is contracting. Its kth spatial derivative is bounded by C_k exp(-alpha t) for a fixed alpha>0: the first derivative follows from the positive symmetric part of DW, and the higher derivatives follow inductively from their contracting variational equation with products of at least two lower derivatives as forcing. Composition with Q1, which vanishes at0, gives an integrable bound of the same form for every derivative of the integrand. Outside that neighborhood, (9) supplies a finite uniformly bounded backward entrance time on each compact set. Splitting the integral at such an entrance time proves smoothness in X and continuous, indeed smooth, parameter dependence locally.

Changing variables in(10) yields W.grad u=Q1. Hence W.grad xi=lambda xi. Reflection makes u even and xi odd in x; xi has the sign of x, and Dxi(0)=(1,0). These observations prove exact temperature transport, positivity, axis vanishing, and all center identities in the statement.

At infinity V=O(r^(1-nu)) and DV=O(r^-nu), uniformly on any fixed compact parameter family after R,L are chosen. Use a large outward transverse circle. Along its outgoing trajectories r(t) is uniformly comparable to exp(beta t), because the integral of |V|/r is finite. The rescaled flow derivative satisfies Dphi_t=exp(beta t)M(t), with M and its inverse uniformly bounded, because the integral of |DV(phi_t)| is finite. Therefore Theta=O(r^(1-2nu)) and grad Theta=O(r^(-2nu)), by their exact transport laws. The same variational argument gives differentiated source/velocity bounds and a smooth angular escape map where needed. Apply the same transport bounds also to B=xi^2 itself, including delta=mu=0, where Theta=0: its section data are uniformly bounded on the fixed parameter box, B<=C r^2 near0 and B<=C r^(1-2nu) at infinity. Thus int |g| B is uniformly finite and int g Theta=a0 int g B=O(delta+mu). These bounds and local parameter continuity give moment continuity by dominated convergence. Near0 all four weighted integrands have absolute radial bound C dr. At infinity the bounds for K Omega, Omega V.grad K, g Theta and Theta V.grad g are respectively C r^(-1-nu), C r^(-1-2nu), C r^(-1-2nu) and C r^(-1-3nu), including the polar area element. All are integrable.

## 4. Exact angular moment reduction

Set N=int Omega V.grad K and I=int g Theta. Since temperature transport is exact, packet79, identity(2), gives

    int Theta V.grad g=2I.

Also the centered inverse gives int K Omega=pi c. Thus(S) is precisely

    D:=N-I-pi c=0.                                      (11)

Angular orthogonality leaves only the mode1 self-interaction and the interactions between modes2 and4 in N. Indeed the kernel has angular frequency2, so an interacting pair must have sum or difference of its frequencies equal to2. Among1,2,4 these are(1,1) and(2,4). For mode1 alone, direct angular integration gives

    N1=(pi/2)int_0^infinity q(r)[p'(r)-p(r)/r]r^-2 dr
       =-(3pi/2)int_0^infinity h'(r)^2 dr/r <=0.          (12)

To check the second equality, the mode1 Poisson equation reads q=-r h''-3h'. Substitute p'-p/r=r h', integrate h''h', and use h'(0)=h'(infinity)=0. The boundary limits follow from(7)-(8), including when mu>0, for which h'=O(r^-nu). All integrals are absolutely convergent.

For the remaining part N24, the plateau2<=r<=R has Psi_2=(c/2)r^2sin(2theta), Psi_4=b r^2sin(4theta), q2=0 and q4=12b. A direct trigonometric integration gives the contribution

    12pi c b int_2^R dr/r.

The inner transition has fixed radii. In the outer transition put r=R s; its log width is L, and the degree2 stream functions make its contribution independent of R. Consequently

    N24=12pi c b log R+O_(c,b,L)(1).                     (13)

This estimate is exact up to a bounded constant, not a numerical asymptotic inference.

First set delta=mu=0. On2<=r<=R the source q equals K0 b, so (8) gives

    h'(r)=-K0 b/3-C0/r^3,

where C0 depends on the fixed inner transition but not on R. Hence

    int_2^R h'(r)^2 dr/r=(K0^2 b^2/9)log R+O(1).

The inner part is bounded independently of R. For the outer part use r=R s in(8): the source is a fixed function of s on1<=s<=exp L and vanishes afterwards, while the inner integral contributes K0 b/3+O(R^-3). This gives a bounded integral over1<=s<infinity, since h'=O(s^-3) past the support. Combining with(12)-(13),

    N=pi[12cb-K0^2 b^2/6]log R+O_(c,b,L)(1),
                     when delta=mu=0.                  (14)

At b=b_* the coefficient is strictly positive by(2). Choose a finite R sufficiently large that N(b_*,0,0)>2pi c. At b=0, N=N1<=0. With delta=mu=0, a0=0 and Theta=0, so

    D(0,0,0)<0, D(b_*,0,0)>0.                          (15)

The zero-temperature parameter values in(15) are used only as limits to arrange these strict signs; they are not the final fields.

Fix this R. The construction and the moments depend continuously on b,delta,mu on the selected compact parameter box. In particular N is quadratic in the source coefficients, and I=a0 int g xi^2 tends to0 as delta+mu tends to0 by the uniform bounds from Section3. Choose strictly positive delta and mu sufficiently small that both strict signs in(15) persist and the bounds preceding(9) remain satisfied. Now keep delta,mu fixed. The intermediate value theorem supplies b in(0,b_*) with D=0. These final fields have strictly positive vorticity, a0>0, a nonzero slow tail mu>0, exact global temperature transport, and the single identity(S).

## 5. Why these fields do not solve the vorticity equation

This failure can be seen directly, without using the finite-angular-support exclusion. Outside r=R exp L only the first angular source and stream modes remain. On the positive horizontal ray, V1=0 and Omega_y=0, so

    W.grad Omega+Omega=beta r q'(r)+q(r).

For the algebraic tail term in(3), this expression is

    mu(beta+1)r(1+r^2)^(-(3+nu)/2),                     (16)

using beta nu=1. The Gaussian contribution is

    delta r exp(-r^2)[beta+1-2beta r^2].

Both are integrable in r at infinity. If the vorticity equation held, Theta_x(r,0) would be integrable and Theta(r,0) would have a finite limit.

Exact temperature transport instead gives Theta(r,0) tending to infinity. To justify the positive angular coefficient, let a run over a large transverse circle and form Z(a)=lim_(t->infinity) exp(-beta t)phi_t(a). The limits and first derivatives converge uniformly by the decay bounds in Section3; |Z| is bounded below by radial comparison. The area identity div W=2beta gives

    det(beta Z(a),Z'(a))=det(W(a),a')>0.

Thus the limiting angular map is a local orientation-preserving circle diffeomorphism. Its degree is1, by homotopy from the finite-time flow curves, so it is a global circle diffeomorphism. Reflection and axis invariance fix the two vertical directions and preserve the two open half-circles. The preimage of the positive horizontal direction therefore lies strictly in x>0, where the section temperature is positive. For completeness write (r,0)=phi_(t_r)(a_r), where a_r lies on the fixed transverse circle. Uniform convergence and the invertibility of the limiting angle map imply a_r->a_*, the preimage of the horizontal direction. The exact identity Theta(r,0)/r^(1-2nu)=Theta(a_r)/|exp(-beta t_r)phi_(t_r)(a_r)|^(1-2nu) then has limit Theta(a_*)/|Z(a_*)|^(1-2nu)>0. Thus exact transport and radial asymptotics yield

    Theta(r,0)=r^(1-2nu)[H0+o(1)], H0>0.

Since beta>2, this diverges. This contradicts the finite limit forced by(16). More precisely, (T) and the gradient bound give Theta_x(r,0)=(1-2nu)Theta(r,0)/r-V2 Theta_y/(beta r)=(1-2nu)H0 r^(-2nu)+o(r^(-2nu)). The vorticity side is O(r^(-2-nu)), so its residual is strictly negative at every sufficiently large point of the ray.

The normalization and drift assertions can also be checked directly. For l>0 set Psi_l(X)=l^2 Psi(X/l), V_l(X)=l V(X/l), Omega_l(X)=Omega(X/l), Theta_l(X)=l Theta(X/l). Then a0_l=a0/l, mu_l=mu l^nu>0; l=a0 normalizes the center jet. Every stated property, including (S), is invariant by substitution and the homogeneities of K and g. On the exterior first-mode tail the ordinary vertical origin-velocity integrand has angular integral (1/2)q(r)dr. Since q~mu r^-nu and nu<1, this positive integral diverges. The relative kernel remains integrable, as required.

## 6. Scope and dependencies

The construction invalidates any attempt to deduce a contradiction from positive vorticity, exact global temperature transport, the source-flow geometry, these center and tail conditions, and the single identity(S) alone. It does not say that all first-family homogeneous identities can hold together: packet69's completeness result ensures that some other one fails. It does not construct a profile or weaken the task's endpoint standard.

The proof uses the centered mode1 Poisson formula, smooth cutoff functions, elementary trigonometric orthogonality, the explicitly proved contracting-flow integral, the divergence theorem, the intermediate value theorem, and packet79's absolutely convergent temperature moment identity. No numerical sign, discretized inverse, unproved bound, external solver, or formal proof assistant result is used.

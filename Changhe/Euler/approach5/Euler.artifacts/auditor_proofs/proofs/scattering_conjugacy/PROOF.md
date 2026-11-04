# Scattering map for a bounded solenoidal perturbation

Audit A209. Written: 2026-11-02T21:59:03Z. Status: CONFIRMED.

## Statement and notation

Let U in C^1(R3;R3) be bounded and divergence free, let c>0 and omega be any finite real number, let J(x,y,z)=(-y,x,0), and set A=cI-omega J and B(x)=Ax+U(x). Write Phi_t for the complete B flow and M=sup|U|. Then

    S(x)=lim_(t->infinity) exp(-tA) Phi_t(x)

exists uniformly on R3, is continuous and proper, satisfies |S(x)-x|<=M/c, and intertwines Phi_s with exp(sA) for every real s. It is onto and pushes Lebesgue measure to Lebesgue measure. Its zero fibre is precisely the nonempty compact null set K of forward-bounded points; K is contained in {|x|<=M/c}.

If U tends uniformly to zero, then |S(x)-x|<=epsilon(|x|/2)/c for |x|>=2M/c, where epsilon(r)=sup_(|y|>=r)|U(y)|. If

    integral_1^infinity m(r) dr/r < infinity,
    m(r)=sup_(|y|>=r)||DU(y)||,

then S is a C^1 volume-preserving diffeomorphism R3 minus K onto R3 minus {0}. It satisfies DS B=A S and DS(x)->I uniformly at infinity. For R1>2M/c, delta0=(2/c) integral_(R1/2)^infinity m(r)dr/r, and |x|>R1, one has

    ||DS(x)-I|| <= exp(delta0)(2/c) integral_(|x|)^infinity m(r)dr/r.

## Proof

The field B has linear growth, so its local C^1 flow is complete. Since exp(tA) is exp(ct) times an orthogonal map,

    d_t[exp(-tA)Phi_t(x)]=exp(-tA)U(Phi_t(x)).

Integrating its norm gives both |h_t-id|<=M/c and ||h_t-h_s||_infinity<=M exp(-cs)/c for t>=s>=0. This proves uniform convergence and the integral formula for S. The identity h_t(Phi_s x)=exp(sA)h_(t+s)(x) gives equivariance.

For r(t)=|Phi_t x| away from zero, r'>=cr-M. Once r>M/c, it grows without bound and r(t)>=M/c+exp(ct)(r(0)-M/c). Consequently a bounded forward orbit remains in the closed M/c ball and has S=0. Conversely, an unbounded orbit eventually leaves that ball; the displayed lower bound and equivariance force S!=0. The bound |S-id|<=M/c makes S proper. For each z, x maps to z-(S(x)-x) continuously maps the ball of radius |z|+M/c to itself, so Brouwer's theorem gives S(x)=z.

Liouville's formula gives det D Phi_t=exp(3ct), hence det Dh_t=1. For compactly supported continuous f, all f composed with h_t and with S have support in one fixed ball, and converge uniformly. Thus integral f(S(x))dx=lim integral f(h_t(x))dx=integral f(x)dx. Equality of Radon measures proves S_*Leb=Leb, including |K|=0. Surjectivity supplies a point of K. If |x|>=2M/c, its orbit stays at radius at least |x|/2, giving the epsilon bound directly from the integral formula.

For the differentiable assertion put N_t=exp(-tA)D Phi_t. Its equation is N_t'=Q_t DU(Phi_t x)Q_t^T N_t, where Q_t=exp(omega tJ). Along exterior orbits r'>=cr/2, hence the integral of ||DU(Phi_t x)|| from any time s onward is at most (2/c) integral_(r(s))^infinity m(r)dr/r. This tail tends to zero uniformly for |x|>R1. Gronwall bounds N_t and N_t^-1 by exp(delta0), and makes N_t uniformly Cauchy there. Uniform convergence of maps and derivatives on this open exterior proves S is C^1, DS=lim N_t, det DS=1, and the stated derivative bound. Every point outside K eventually enters the exterior. Equivariance extends these facts to a neighbourhood of that point and gives DS B=A S.

It remains to prove global injectivity, not merely local invertibility. Suppose x!=x' outside K have S(x)=S(x'), and advance both to the exterior. Write D(t)=h_t(x)-h_t(x'). Then D(t)!=0 but D(t)->0. For sufficiently large t the straight segment between Phi_t(x) and Phi_t(x') lies at radius at least (R1/4)exp(ct): the first radius is at least (R1/2)exp(ct), while their separation is exp(ct)|D(t)|. Therefore

    |D'(t)|<=m((R1/4)exp(ct))|D(t)|.

The coefficient has finite time integral. Gronwall's lower bound keeps |D(t)| bounded away from zero, a contradiction. An onto injective C^1 local diffeomorphism has a C^1 inverse. This proves all claims.

## An autonomous example without Dini decay

The draft's nonautonomous linear illustration does not itself belong to this theorem's class. Here is an example that does. Take omega=0, a smooth compactly supported cutoff chi on R2 equal to one on [-2,2]^2, and psi(x,y)=cxy chi(x,y). Define U=(-partial_y psi,partial_x psi,0), independent of z. This is a bounded smooth divergence-free field on R3. For |a|<1 and z0!=0, the B orbit through (a,0,z0) is (a,0,exp(ct)z0). Its scattering limit is (0,0,z0). Thus different points outside K have the same S. Dini decay fails because DU is fixed and nonzero along the unbounded z-axis. The example is kinematic and is not a decaying Euler profile.

## Dependencies and scope

Only elementary ODE theory, the inverse function theorem, Brouwer's fixed-point theorem, Liouville's formula, and equality of Radon measures are used. This independently verifies Theory Agent A SCATTERING_TAIL Theorem S. No Euler equation, pressure normalization, vorticity transport, numerical computation, or restriction on omega is used. The statement does not assert differentiability on K.

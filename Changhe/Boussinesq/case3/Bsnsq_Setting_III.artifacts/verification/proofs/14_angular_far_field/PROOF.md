# Angular temperature limits and critical vorticity tails without velocity derivative decay

Status: independent reconstruction of the lead's referee F claims, read at 14:10 UTC on 2026-10-20. The arguments below confirm the three claims with explicit scope and add a beta=2 regularity observation. They do not exclude the entire prompt class.

## Hypotheses and notation

Let beta>=2. Let U, Theta, Omega be smooth on R^2 and solve

    div U=0, V=U-U(0), W=beta X+V,
    W.grad Theta=(beta-2)Theta,
    W.grad Omega+Omega=partial_x Theta.

Assume |V(X)|<=C(1+|X|)^(1-delta) for some delta in (0,1). Assume the B2 axis conditions W_1(0,y)=0, Theta(0,y)=0, and the nonzero temperature jet Theta=a0 x^2+O(|X|^3). Normalize a0>0 by the exact signed symmetry of all fields from research/07. No decay bound on DV is assumed. The curl relation is not used in this packet beyond any use made of it to establish the stated velocity bound.

Write m=1-2/beta, q=2/beta and kappa=2-q=m+1. Polar angles theta are measured from the positive x-axis. Put e(theta)=(cos theta,sin theta). Every assertion below concerns the original physical polar angle, not merely an unspecified scattering coordinate.

## 1. Uniform angular limit of temperature

There is a continuous 2pi-periodic function A such that

    r^(-m) Theta(r e(theta)) -> A(theta)

uniformly in theta. Moreover A(+-pi/2)=0, and A is positive at some angle strictly inside the right semicircle. In particular |Theta(X)|<=C'(1+|X|)^m.

Choose rho sufficiently large that w_r=W.e_r>=beta r/2 for r>=rho. The flow is complete because W is locally Lipschitz and has at most linear growth. A trajectory starting at rho e(sigma) meets each radius r>=rho exactly once. Write its arrival time s(r,sigma) and angle h_r(sigma), taking continuous lifts with h_r(sigma+2pi)=h_r(sigma)+2pi. Uniqueness makes h_r an orientation-preserving circle diffeomorphism for finite r: every point at radius r, followed backward, reaches rho in finite time while its radius decreases at a rate bounded below by beta r/2.

In radius parametrization,

    partial_r s = 1/(beta r)+O(r^(-1-delta)),
    partial_r h_r = w_theta/(r w_r)=O(r^(-1-delta)),

uniformly in sigma. Consequently tau_r=s-(1/beta)log(r/rho) and h_r converge uniformly to continuous tau_infinity and h_infinity.

The exact angular Jacobian can be obtained without differentiating V at infinity. The determinant of the two flow-coordinate tangent vectors, one in time and one in initial angle, is rho w_r(rho,sigma) exp(2 beta s), because div W=2 beta. On the arrival circle it is r w_r(r,h_r(sigma)) h_r'(sigma). Therefore

    h_r'(sigma)=rho w_r(rho,sigma) exp(2 beta s(r,sigma))
                /[r w_r(r,h_r(sigma))].

Since w_r(r,theta)/r -> beta uniformly, the derivatives converge uniformly to

    J_infinity(sigma)=w_r(rho,sigma)/(beta rho)
                      exp(2 beta tau_infinity(sigma)) > 0.

The limit function is continuous and bounded away from zero. Uniform convergence of functions and derivatives gives h_infinity in C^1 with derivative J_infinity. Its degree is one, so it is a circle diffeomorphism. The inverse maps converge uniformly as well.

The transport equation gives

    r^(-m) Theta(r e(h_r(sigma)))
      =rho^(-m) exp((beta-2)tau_r(sigma)) Theta(rho e(sigma)).

The right side converges uniformly. Composing with h_r inverse proves the asserted limit and continuity, with

    A(h_infinity(sigma))
      =rho^(-m) exp((beta-2)tau_infinity(sigma)) Theta(rho e(sigma)).

The invariant axis fixes the two axis angles throughout the flow, so its zero temperature gives A(+-pi/2)=0. To obtain a positive value, choose a bounded open patch D in x>0 with Theta>=a>0. Its images have area exp(2 beta t)|D|. They cannot all stay in B_rho. An escaping positive-temperature trajectory crosses the circle in the right half-plane and the displayed formula gives positive A at its limiting angle. The limiting angle is not an axis angle because A vanishes there. The uniform limit also gives the stated global temperature growth bound by adding the bounded interior.

For beta=2 there is a useful improvement. The exponential in the last formula equals one. Thus A=Theta(rho e(.)) composed with h_infinity inverse is C^1. Also

    partial_theta Theta(r e(h_r(sigma)))
      =partial_sigma Theta(rho e(sigma))/h_r'(sigma)

converges uniformly after inverse composition to A'. The radial transport identity gives partial_r Theta=O(r^(-1-delta)), because the angular derivative is uniformly bounded. It follows that

    r partial_x Theta(r e(theta)) -> -sin(theta) A'(theta)

uniformly in theta at beta=2. No statement of C^1 angular convergence is made here for beta>2.

## 2. Logarithmic divergence at the critical vorticity exponent

Under the same hypotheses, the mixed-Casimir theorem in research/09 gives

    M(R)=integral_(B_R) |Omega| >= c R^kappa

for all R>=R0, after enlarging R0. This implies

    integral_(B_R) |Omega|^beta >= c' log(R/R0)

for all sufficiently large R. This quantitative assertion does not require finite L^beta norm or bounded vorticity at infinity.

Indeed let w(X)=max(R0,|X|)^(-kappa), and J(R)=integral_(B_R)|Omega|w. Tonelli's theorem yields

    c log(R/R0) <= integral_R0^R M(t)t^(-kappa-1)dt <= J(R)/kappa.

The last inequality follows by interchanging integrals and dropping the negative outer-radius term. With beta'=beta/(beta-1), the identity kappa beta'=2 gives

    integral_(B_R) w^beta' = pi+2pi log(R/R0).

Holder's inequality now gives J(R)<=||Omega||_(L^beta(B_R)) [pi+2pi log(R/R0)]^(1/beta'). Raising to power beta and rearranging proves the claim. All integrals on finite balls are finite by smoothness.

## 3. A critical pointwise upper bound forces a unique weak angular tail

Add the hypothesis |Omega(X)|<=C(1+|X|)^(-q), q=2/beta. Then on compact subsets of R^2 minus the origin,

    R^q Omega(RX) -> |X|^(-q) B(arg X)

in the weak-* L^infinity sense as R tends to infinity. Here the angular distribution

    B=sin(theta) A'-m cos(theta) A

has an L^infinity representative. In the right semicircle it obeys

    integral_(A>0) B(theta) dtheta
      =-(m+1) integral_(-pi/2)^(pi/2) A_+(theta) cos(theta) dtheta < 0.

Consequently a constant c>0 exists such that for every sufficiently large R,

    integral_{R<|X|<2R, x>0} Omega_-(X) dX >= c R^kappa.

The derivative in the definition of B is initially distributional. The statement is not an unproved termwise differentiation of the temperature remainder.

For the proof define omega_R=R^q Omega(RX), theta_R=R^(-m)Theta(RX), w_R=W(RX)/R. On every compact annulus theta_R converges uniformly to Theta_infinity=|X|^m A(arg X), w_R converges uniformly to beta X, and omega_R is bounded in L^infinity. A diagonal weak-* subsequence gives a limit omega_* on the punctured plane with |omega_*|<=C|X|^(-q). The conservative vorticity equation passes to the limit as

    div(beta X omega_*)-(2 beta-1)omega_*=partial_x Theta_infinity,
    beta r partial_r omega_*+omega_*=-r^(-q) B(theta).

Pair with an arbitrary smooth angular test psi. The scalar distributional radial ODE has solution

    integral omega_*(r,theta) psi(theta)dtheta
      =r^(-q)<B,psi>+c_psi r^(-1/beta).

The global bound as r tends to infinity forces c_psi=0, since q>1/beta. It then bounds |<B,psi>| by C||psi||_L1. Hence B belongs to L^infinity and omega_*=r^(-q)B. All convergent subsequences have the same limit; compactness therefore gives convergence of the whole family on each compact annulus.

Where sin(theta)!=0 the identity defining B and continuity of A imply that A is locally Lipschitz. For smooth bounded F>=0 vanishing on nonpositive arguments, let G(t)=integral_0^t F. Integrate B F(A) separately on either side of theta=0. The chain rule for locally Lipschitz functions and integration by parts give

    integral_(-pi/2)^(pi/2) B F(A)
      =-integral_(-pi/2)^(pi/2) cos(theta)[G(A)+m A F(A)].

The boundary terms at the vertical angles vanish since A=0. The terms at +-eta around zero tend to zero since sin(eta)G(A(+-eta)) tends to zero. No differentiability at zero is presumed. Approximate the indicator of positive arguments by such functions 0<=F<=1 and use dominated convergence. This proves the stated strictly negative signed integral.

Choose one fixed such F for which the integral is negative. The weak-* limit can be tested against the L^1 weight 1_{1<r<2,x>0} F(A(theta)); it need not be smooth. Its limiting integral is negative. Since the weight lies between zero and one, the integral of (omega_R)_- over this half-annulus is bounded below by a positive constant for every large R. Rescaling proves the negative-mass claim.

At beta=2, Section 1 gives A in C^1 even without assuming a uniform pointwise omega tail. Thus the B determined above has the continuous representative sin(theta)A', with B(0)=B(pi)=0. Also the improper integrals of B/sin(theta) on the two parts of the right semicircle sum to A(pi/2)-A(-pi/2)=0. For beta>2, continuity of B is not established by the critical upper bound alone.

## Scope and dependencies

The full B2 class only imposes U=o(r); the power improvement used here is an extra hypothesis unless separately derived from a tail condition. Critical upper decay is another extra assumption only in Section 3. A slower homogeneous vorticity term of order r^(-1/beta) is not excluded. The angular data A=cos^2(theta), B=-cos(theta)[m cos^2(theta)+2 sin^2(theta)] satisfy the displayed limiting identities and parity but are not a constructed coupled whole-plane profile. Thus these results cannot authorize a full NO.

Dependencies: complete C^1 ODE flows, exact divergence Jacobian, uniform convergence of derivatives, the previously proved mixed-Casimir mass theorem, Holder and Tonelli, weak-* compactness on compact annuli, and the scalar distributional Euler ODE. No formal verification or interval computation is claimed.

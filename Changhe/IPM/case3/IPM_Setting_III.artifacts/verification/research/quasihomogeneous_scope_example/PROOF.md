# An exterior constant-coefficient density with three cusp directions at infinity

Independent proof, 2026-10-21 UTC, written before its supporting checker.
The frozen lead proposal is in verification/LEAD_PROPOSAL.frozen.md.
This is a test density for comparing restricted ansatz classes. It is not
a solution or a candidate for the IPM transport equation.

## Statement and conventions

There is a real C-infinity function rho on R^2, even in x and odd in y,
with rho_y(0) nonzero and

    |rho(X)|+(1+|X|)|grad rho(X)| <= C(1+|X|)^(2/3),

annihilated outside a compact set by a nonzero linear differential
operator P with constant real coefficients, such that rho has neither
finite angular support nor finite separation rank in any fixed invertible
linear coordinate system, even outside a disc. The same rank exclusion
holds for approximation by finitely many separated functions with
pointwise little-o error relative to R^(1/2) along every ray in the
chosen upper coordinate half-plane.

Its isotropic far field is the locally uniform limit

    R^(-1/2)rho(RX) -> F(X)
      = kappa [S(y)+S((x+y)/sqrt(2))+S((y-x)/sqrt(2))],
    S(t)=sign(t)|t|^(1/2),  kappa=1/(2sqrt(pi)).

In particular F(0,1)=kappa[1+2^(3/4)] is nonzero. The three distinct
nonzero cusp terms are essential to the simple rank proof below. We
choose their coefficients all equal to one. Allowing arbitrary
coefficients would require at least that all three are nonzero; a
nonzero y-axis amplitude also excludes their indicated cancellation.

The inverse Fourier convention is
f(X)=(2pi)^(-2) integral exp(i X dot Xi) fhat(Xi) dXi.
The first construction takes place in coordinates (s,t). Put

    Q=d_s^4-d_t^6,  q(xi,eta)=xi^4+eta^6.

No claim about the IPM stream, its center strain, or transport is part
of this construction.

## The odd tempered fundamental derivative

On frequency space minus zero define

    m(xi,eta)=(i eta)^3/(xi^4+eta^6).

It is even in xi, odd in eta, and purely imaginary. Its extension at
zero is fixed by odd pairing: in its distributional integral replace a
test function phi by [phi(xi,eta)-phi(xi,-eta)]/2. This integral is
absolutely convergent near zero. Indeed, under the frequency dilation

    delta_lambda(xi,eta)=(lambda^3 xi,lambda^2 eta),

m has degree -6 and volume has degree 5, while the odd test part
vanishes at least as eta, of degree 2. An annular decomposition then
has a summable factor lambda^(5-6+2)=lambda near zero. At infinity,
Schwartz decay makes the pairing converge. Thus this defines a
tempered distribution with exactly the stated anisotropic homogeneity.
There is no hidden choice of an even finite part in this definition.

Multiplication by q gives q m=(i eta)^3 as distributions. This follows
by applying the odd pairing to q phi, since q is even and the product
(i eta)^3 phi is locally integrable. Let H be the inverse Fourier
transform. Then

    QH=d_t^3 delta,  H(lambda^3 s,lambda^2 t)=lambda H(s,t).       (1)

The scaling follows either by change of variables in the odd pairing,
or by duality: the degree -6 and volume degree 5 give spatial degree 1.
The symmetries give real H, even in s and odd in t.

## Smoothness away from zero, without an unproved hypoellipticity step

Choose a smooth anisotropic annular partition
1=sum_j chi(delta_(2^(-j)) Xi) on Xi!=0, with chi even in xi and eta.
For example use differences of smooth radial cutoffs in
(xi^4+eta^6)^(1/12). The compactly supported annular function chi m is
smooth. Its inverse Fourier transform A is Schwartz, even in s and
odd in t. In the sense of distributions the inverse series is

    H(s,t)=sum_(j in Z) 2^(-j) A(2^(3j)s,2^(2j)t).                (2)

For negative j, oddness gives
|A(2^(3j)s,2^(2j)t)|<=C_K 2^(2j) on every compact K of (s,t);
the term in (2) is at most C_K 2^j. After a derivative
d_s^alpha d_t^beta with alpha+beta>=1, its prefactor is
2^(j(3alpha+2beta-1)), whose exponent is positive. The differentiated
Schwartz function is bounded on compact sets, so every differentiated
negative-j series converges uniformly there. For nonnegative j and
any compact K away from zero, the scaled point has magnitude at least
c_K 2^(2j). Arbitrarily high Schwartz decay beats the prefactor of
every derivative, so the positive-j series also converges uniformly
with every derivative on K. Consequently H is C-infinity off zero.
This proves the exact regularity needed here directly.

The odd distributional extension equals the sum used in (2): the
negative frequency shells pair with the odd test part and are
absolutely summable by the preceding degree count; the positive
frequency shells converge against Schwartz tests. No polynomial term
can appear from summing these specified distributions.

## An explicit integral, continuity, and the axis constant

For b>0, Fourier inversion of the one-dimensional quartic denominator
gives

    integral_R exp(i s xi)/(xi^4+b^4) dxi
      = pi/(sqrt(2)b^3) exp(-z)(cos z+sin z),
    z=b|s|/sqrt(2).                                             (3)

One can verify (3) without choosing a contour. The function on its
right solves (d_s^4+b^4)g=0 on s!=0, decays at both ends, is C^2
at zero, and has jump 2pi in its third derivative. Thus it solves
(d_s^4+b^4)g=2pi delta. Taking its Fourier transform gives the left
side with the displayed normalization.

Apply (3) with b=|eta|^(3/2), pair the odd eta frequencies, and put
E(z)=exp(-z)(cos z+sin z). The result is

    H(s,t)=1/(2pi sqrt(2)) integral_0^infinity
             sin(t eta) eta^(-3/2) E(|s|eta^(3/2)/sqrt(2)) d eta. (4)

The right side is an ordinary absolutely convergent integral: near
zero use |sin(t eta)|<=|t|eta, and at infinity eta^(-3/2) is
integrable while E is bounded. The same estimates, with t in any
bounded interval, provide an integrable dominating function. They
prove continuity for all (s,t), including zero, and identify this
function with the specified distribution by odd Fourier pairing.

At s=0, a change of variables shows that the integral equals
sign(t)|t|^(1/2) times integral_0^infinity sin u/u^(3/2) du.
Integration by parts gives twice the improper integral of
cos u/sqrt(u). The boundary terms vanish. The Abel regularization
of this last integral is

    Re integral_0^infinity exp(-(epsilon-i)u)u^(-1/2)du
       = sqrt(pi) Re(epsilon-i)^(-1/2) -> sqrt(pi/2).

Its Abel limit equals the improper oscillatory integral: integration
by parts bounds tails uniformly after one derivative of u^(-1/2).
This proves

    integral_0^infinity sin u/u^(3/2)du=sqrt(2pi),
    H(0,t)=kappa S(t),  kappa=1/(2sqrt(pi)).                     (5)

## Growth, smoothing, and isotropic asymptotics

Let d(s,t)=|s|^(1/3)+|t|^(1/2). It scales by lambda in (1).
The set d=1 is compact and avoids zero. Smoothness off zero and
anisotropic scaling therefore give

    |H|<=C d,  |H_s|<=C d^(-2),  |H_t|<=C d^(-1)              (6)

away from zero. The derivative bounds also show local integrability
of these derivatives: an anisotropic ball of radius epsilon has
volume proportional to epsilon^5. The continuous function H has
these as weak first derivatives, as is seen by removing such a ball
in integration by parts and using its scaling, or directly from
the convergent distributional construction.

For r=sqrt(s^2+t^2)>=1, d<=2r^(1/2), while d>=c r^(1/3).
Thus |H|<=C r^(1/2), |H_s|<=C r^(-2/3), and
|H_t|<=C r^(-1/3). In particular the isotropic first-derivative
growth exponent is 2/3, not just the density exponent 1/2.

Choose a real, nonnegative, radial mu in C_c^infinity(R^2) with
integral one, and define h=H*mu. It is smooth everywhere, even in
s and odd in t. Constant-coefficient differentiation commutes
with convolution and (1) gives

    Qh=d_t^3 mu.

The right side is compactly supported. For r greater than twice
the support radius of mu, every point in the convolution has
comparable isotropic radius, so (6) implies

    |h|+(1+r)|grad h|<=C(1+r)^(2/3).                            (7)

The same bound on bounded sets follows from smoothness.

Taking lambda=sqrt(R) in (1) gives the exact identity

    R^(-1/2)H(Rs,Rt)=H(R^(-1/2)s,t).

Continuity of H makes this tend to H(0,t), uniformly on compact
sets of (s,t). For the convolution the integrand becomes
H(R^(-1/2)s-R^(-3/2)z_s,t-R^(-1)z_t), with z in a fixed compact
set. It converges uniformly on such compact sets too. Therefore

    R^(-1/2)h(Rs,Rt) -> kappa S(t)                             (8)

locally uniformly, including across t=0.

## Three directions and the exterior equation

Use the three orthogonal coordinate systems

    (s0,t0)=(x,y),
    (s+,t+)=((x-y)/sqrt(2),(x+y)/sqrt(2)),
    (s-,t-)=((x+y)/sqrt(2),(y-x)/sqrt(2)).

Put h_j(X)=h(s_j,t_j). Under x -> -x the two rotated summands
are exchanged, because h is even in its first argument. Under
y -> -y they are exchanged with a minus sign, because h is odd
in its second argument. Thus their sum, as well as h0, is even
in x and odd in y.

Let zeta be a smooth radial compact cutoff equal to one near
zero. Choose a real c_* such that
c_*+d_y(h0+h++h-)(0)!=0, and set

    rho=h0+h++h-+c_* y zeta.

This makes the center slope nonzero and preserves parity. It
does not assert a relation between that slope and any IPM strain.
The growth bound follows from (7) and rotation invariance of the
Euclidean norm. For j=0,+,- let Q_j be Q written in that coordinate
system. Each Q_j h_j is compactly supported. The commuting
constant-coefficient operator

    P=Q0 Q+ Q-

therefore annihilates each h_j outside a compact set, as well as
the compact correction. Its symbol is a product of three nonzero
real polynomials, so P is nonzero. Equations (8) give exactly
the stated far field F and its nonzero y-axis value.

## Infinite rank in every linear coordinate system

The three lines t_j=0 are distinct. On each line away from their
common origin, exactly one term of F has a square-root cusp and
the other two terms are smooth. Each coefficient is nonzero, so
none of these cusps cancels. In particular the angular function
F(cos(theta),sin(theta)) is not C^1, hence cannot be a trigonometric
polynomial.

Now fix any invertible real linear change X=M(u,v). Write
t_j(M(u,v))=alpha_j u+beta_j v. The three covectors remain
nonproportional. At most one has alpha_j=0, and at most one has
beta_j=0. Thus at least one index j_* has both nonzero. Its cusp
in a section at v>0 occurs at

    u=tau_* v,  tau_*=-beta_(j_*)/alpha_(j_*) != 0.

The other possible cusp locations are tau_j v for those j with
alpha_j!=0. The distinct covectors give distinct tau_j. A term
with alpha_j=0 is constant in u on a fixed v>0 section.

For any integer L, choose distinct v1,...,vL>0 so that for every
n!=m and every j with alpha_j!=0,

    tau_* v_n != tau_j v_m.

Such a choice is possible recursively: each previous v forbids
only finitely many positive new values, both for a new distinguished
cusp and for an old distinguished cusp to coincide with a new one.
At u=tau_* v_n the n-th section has a nonzero square-root cusp,
while every other chosen section is smooth in a neighborhood.
Any vanishing linear combination of these sections must have
zero n-th coefficient. As this holds for every n, the L sections
are linearly independent. Arbitrarily large L proves infinite
separation rank on v>0.

For completeness, finite separation rank of rho in these exterior
coordinates, even up to the stated raywise error, would pass to F.
For arbitrary u0,...,uN and positive v0,...,vN, the matrix of the
separated approximation at (R u_i,R v_j), divided by R^(1/2), has
rank at most N once R is large enough to lie in the exterior.
Every entry tends to F(M(u_i,v_j)) by (8) and the error hypothesis.
Continuity of its determinant makes every (N+1)-minor of this
limiting kernel zero. If N+1 sections were independent, suitable
evaluation points u_i would make one such minor nonzero: prove
this elementary fact by induction, choosing a point where a
nonzero function remaining after elimination does not vanish.
This contradiction excludes finite rank without any regularity
assumption on the separated one-variable factors.

Similarly, fixed finite angular support of rho outside a disc
would put all rescaled angular traces in one finite-dimensional
trigonometric space. Uniform convergence of (8) on the circle
would put F in that closed space, contradicting its cusp.

## Scope and evidence

This proves noncontainment of the exterior constant-coefficient
ansatz class in either the finite-angular or finite-linear-rank
class. It does not prove that a general IPM profile exists.
Indeed the nonsmooth far field violates the smooth off-zero
far-field condition required of an exact profile in result121
and the lead's theorem3.23. No transport equation has been
verified for this density.

The proof uses only Fourier duality, the explicit one-dimensional
identity (3), a supplied annular decomposition, and finite-rank
linear algebra. A background literature search for quasi-elliptic
fundamental solutions was not used as a substitute for the
smoothness argument or as an input to a claimed theorem.
Independent exact symmetry, symbol, and rank checks, and numerical
checks of (4), will be recorded separately. They support this
proof and do not replace its all-scale arguments.

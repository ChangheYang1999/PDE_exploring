# The nonintegrable tails are forced by the leading angular profile

Status: proposed theorem, OPEN independent Opus review. The proof precedes
its application to the exact candidate. This is a necessary far-field
classification, not an existence theorem or a transport inverse.

## Statement and notation

Work in R2 with the S1 symmetry: a density is even in x and odd in y.
Let 0 < gamma < 1, c = 1/gamma, delta = 1-gamma, and

    N = floor(2/delta), e_j = 1-(j+1)delta, 0 <= j < N.

Thus e_j >= -1 exactly for these indices, and e_N < -1. An equality
at e_(N-1) = -1 is included. A tail r^e Theta(theta), with Theta not
identically zero, belongs to exterior L2 exactly when e < -1.

Let Theta_0,...,Theta_(N-1) be smooth real S1 functions on the circle,
so each is a rapidly convergent sum of sin(n theta) with n positive odd.
Let chi(r) be a smooth radial function, zero for r <= 1 and one for
r >= 2. Set

    R(X) = sum_(j=0)^(N-1) chi(r) r^(e_j) Theta_j(theta).

For each j let Psi_j be the unique smooth sine-even solution of

    [partial_theta^2+(e_j+1)^2] Psi_j
        = -e_j cos(theta) Theta_j + sin(theta) Theta_j'.       (1)

Here sine-even means a sum of sin(m theta) for positive even m; it
means odd in x and odd in y, not an even function of theta. Define

    B_(l,m) = -e_m Psi_l' Theta_m + (e_l+1) Psi_l Theta_m'.      (2)

The canonical smooth velocity U[R] is defined below. For h in the S1
subspace of L2(R2), define U[R+h] = U[R]+U[h], where U[h] is the bounded
Fourier multiplier with symbol

    (xi_1 xi_2/|xi|^2, -xi_1^2/|xi|^2).

Suppose rho=R+h solves, in distributions,

    c div(X rho) - (2c+1)rho + div(U[rho] rho) = 0.            (3)

Then necessarily, for j=1,...,N-1,

    Theta_j = 1/[j(c-1)] sum_(l+m=j-1) B_(l,m).              (4)

Conversely (4) implies that the residual of the smooth reference R
belongs to L2(R2). It does not imply that (3) has a solution.

For fixed gamma and Theta_0, equations (1) and (4) give unique smooth
Theta_1,...,Theta_(N-1). Each Theta_j is a homogeneous polynomial of
degree j+1 in Theta_0, with linear angular operators and differentiation
allowed in its coefficients. No bounded mapping claim in a finite
regularity norm is part of this statement.

In particular, if 1/2 < gamma < 3/5, then N=4. Once the entire leading
angular profile is fixed, an exact solution with this four-power
expansion modulo L2 has no freedom to choose its other three
nonintegrable angular profiles.

## Proof of the canonical velocity construction

The right side of (1) has only positive even sine frequencies. Since
0 <= e_j+1 < 2, none of the eigenvalues (e_j+1)^2-m^2, m=2,4,...,
is zero. Divide its Fourier coefficients by those eigenvalues. The
coefficients still decay faster than every power, proving existence,
smoothness and uniqueness in the specified angular space.

Put psi_j = r^(e_j+1) Psi_j(theta) on r>0. The polar Laplacian and
(1) give

    Delta psi_j = -partial_x [r^(e_j) Theta_j].

Our convention is grad-perp psi = (-partial_y psi, partial_x psi).
Consequently the homogeneous velocity outside the origin is

    u_j = r^(e_j)[-Psi_j' e_r+(e_j+1)Psi_j e_theta].           (5)

Let v = grad-perp sum_j chi psi_j. Both v and R are globally smooth.
The function

    g = curl(v) + partial_x R

is smooth, supported in 1<=r<=2, and odd in both x and y. In particular
its integral is zero. With G(X)=(1/(2pi))log|X|, put

    w = grad-perp(G*g), U[R] = v-w.                          (6)

The distributional identity Delta G=delta_0 follows by the flux of
its radial gradient across a circle. Convolution with the smooth compact
source makes w smooth. It follows directly that

    div U[R]=0, curl U[R]=-partial_x R.

The zero integral of g gives, outside twice its support,

    w(X) = integral [grad-perp G(X-Y)-grad-perp G(X)]g(Y)dY.

The kernel derivative is O(r^-2), uniformly along these segments, so
w=O(r^-2). Differentiating once gives grad w=O(r^-3). Therefore

    U[R] = sum_j u_j + O(r^-2).                              (7)

All estimates are uniform in angle. U[R] has the S1 velocity parities:
u1 is odd in x and even in y, while u2 is even in x and odd in y. Its
growth is O(r^gamma).

These conditions determine U[R] uniquely. The difference of two smooth
velocities with the same divergence and curl has harmonic components.
For a harmonic component d with growth O(r^gamma), the interior gradient
estimate on a radius L ball centered at a fixed point gives
|grad d| <= C L^(gamma-1) for large L. Letting L tend to infinity shows
that d is constant. Each constant is zero by the required parity.
The gradient estimate itself follows by differentiating the mean-value
or Poisson formula on a ball. This also shows why the sublinear growth
and parity specifications are needed.

The Fourier multiplier U on L2 has norm at most one and has the same
divergence, curl and parity identities. The construction is independent
of the choice of cutoff in its affine sense: if R and R_tilde use two
cutoffs with the same tails, R-R_tilde is smooth compactly supported.
The Fourier velocity of this difference is smooth and decays at
infinity. The difference U[R]-U[R_tilde]-U[R-R_tilde] has zero divergence
and curl and sublinear growth, so it vanishes by the same uniqueness
argument. Thus R+h and R_tilde+(h+R-R_tilde) have the same velocity.
All products in (3) are locally integrable, since its nonsmooth factors
are locally L2 and R,U[R] are smooth.

## Proof of the triangular equations

Outside r=2, (5) gives

    u_l dot grad(r^(e_m)Theta_m) = r^(e_l+e_m-1) B_(l,m)
                               = r^(e_(l+m+1)) B_(l,m).

Also c e_0-1=0, and c e_j-1=-j(c-1). Therefore the smooth residual is

    F[R] = (cX+U[R]) dot grad R-R
         = sum_(j=1)^(N-1) r^(e_j) E_j + L,
    E_j = -j(c-1)Theta_j+sum_(l+m=j-1) B_(l,m),              (8)

where L is smooth and square integrable. Indeed the omitted quadratic
terms have indices j>=N and hence e_j<=e_N<-1. The error in (7)
contributes O(r^(gamma-3)), which is square integrable because gamma<1.
The cutoff region is compact. More explicitly every error is a finite
sum of strictly lower powers than e_(N-1), plus this uniform bound.

If any E_j is nonzero, let j be its smallest such index. Equation (8)
then has a uniform leading term r^(e_j)E_j, with e_j>=-1. The residual
obstruction T4-202 at weight a=0 applies: its smooth background satisfies
|U[R]|=O(r^gamma) and |grad R|=O(r^(gamma-1)), while h and U[h] are in L2.
For completeness, test the correction equation against

    phi_L(X)=L^-1 eta(|X|/L) E_j(arg X),

where eta is smooth, nonnegative, nonzero and supported in (1,2).
The residual pairing is L^(e_j+1)(A+o(1)), A>0. Put
m_L=||h||_(L<r<2L), n_L=||U[h]||_(L<r<2L); both tend to zero. The
linear cX transport term and zeroth-order term are O(m_L). The
background velocity term is O(L^(gamma-1)m_L); the U[h] dot grad R
term is O(L^(gamma-1)n_L); the quadratic correction is O(L^-2 m_L n_L).
Dividing by L^(e_j+1), whose exponent is nonnegative, makes every
correction tend to zero. This contradicts the residual pairing. Thus
all E_j vanish, which is (4).

Conversely, when all E_j vanish, (8) is exactly the square integrable
remainder L. This proves the residual claim.

For uniqueness of the tails, compute Psi_0 linearly from Theta_0, then
use (4) at j=1 to determine Theta_1. Inductively its right side uses
only indices l,m<=j-1, already determined, and j(c-1)>0. Products and
angular derivatives preserve smoothness and S1 symmetry. If Theta_l
has degree l+1 in Theta_0 and Theta_m has degree m+1, each summand has
degree l+m+2=j+1. This proves the homogeneity and induction claims.

## Interpretation and scope

Under the dilation rho_lambda(X)=lambda rho(X/lambda), the leading
amplitude is multiplied by z=lambda^delta. Equations (4) force the
j-th profile to be multiplied by z^(j+1), exactly the dilation weights.
Fixing a nonzero leading profile removes this gauge. In the four-tail
class, fixing the other three profiles to their compatible values does
not discard an exact solution that otherwise has the same leading
profile and an L2 remainder. An incompatible set of lower profiles
instead excludes the entire affine L2 class, regardless of residual
size near the origin.

This assertion does not fix an arbitrary leading angular shape by
fixing a single scalar normalization. It does not cover logarithmic
terms, additional asymptotic powers outside the stated class, or
corrections outside L2. It proves no existence, inverse, quantitative
smallness condition or Sobolev mapping estimate. The canonical velocity
and the nonlocal correction in (6) are essential parts of the theorem.

## Exact candidate verification contract

The candidate application uses the frozen canonical potential JSON.
For each branch j and potential angular frequency n, let A_(j,n) be
its endpoint coefficient at t=1, and let d=e_j+3. A potential term
A r^d cos(n theta) contributes to the density endpoints by

    sin(n+1): -A(d^2-n^2)(d-2-n)/2,
    sin(n-1): +A(d^2-n^2)(d-2+n)/2,

and to stream endpoints by

    sin(n+2): +A(d-n)(d-n-2)/4,
    sin(n-2): -A(d+n)(d+n-2)/4.

Negative sine indices reverse the sign; the zero index vanishes.
These identities follow by differentiating the homogeneous potential,
with rho=-partial_y Delta potential and psi=partial_x partial_y potential.
The verifier forms (1) and (8) over exact rationals for j=0,...,3. It
stores the full endpoint data and zero checks in exact JSON. A separate
numerical lane must reproduce a candidate-specific conclusion before
it is called independently confirmed.

Dependencies: Fourier multiplier Plancherel bound, elementary polar
differentiation, the logarithmic Green function and its zero-mean
far-field estimate, the harmonic mean-value formula, and the annular
argument of T4-202 reproduced above. No external existence theorem.

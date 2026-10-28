# Independent original-data global coefficient enclosures

## Object, quantities and acceptance conditions

The input is the read-only original modal NPZ, with exact dyadic
coefficients, the exact C6 joins and the exact-real scalar repair of
proof 04. The stream function and velocity are the canonical ones.
Write ell=1/k, c=3ell-1, A=2ell-1, D=4ell-1, b0=1+ell,
and a=17/4. With t=log r, define

 q=V_r/r, v=V_theta/r, d(t)=q(t,pi/2),
 bplus=(|grad rho|-rho_y)/2,
 kappa=b0+(mu_a'/2)q+a tan(theta)v,
 m_a=kappa-bplus,
 m_R=b0+(mu_R'/2)q-bplus.

Here mu_a'=-17/2 on t<0 and -5/4 on t>0. The piecewise
mu_R' has knots 3/2,7/4,3,4,5,6,7,8,9,10 and values
(4,17,28,27,25,18,4,-10,-17,-19,-20)/16 in order.
Cells crossing a knot include both adjacent values.

The accompanying code independently reconstructs the modal Green
integrals from the original input. A global positive claim is accepted
only after every finite cell and both half-lines are covered, all
arithmetic outputs are finite, the relevant directed lower bounds are
positive, and the reconstruction and coverage audit succeeds. This
file states the enclosure argument; numerical conclusions are kept in
the separate evidence and verification entry after completion.

## Independent Green representation

Expand rho=r^3 sum_(j=0)^261 H_j(t) sin((2j+1)theta).
For n=1,...,261 put a_n=2n+4, b_n=2n-4 and

 I_n(t)=integral_(-infinity)^t exp(-a_n(t-s))H_(n-1)(s)ds,
 J_n(t)=integral_t^infinity exp(b_n(t-s))H_n(s)ds.

They satisfy I_n'=H_(n-1)-a_n I_n and J_n'=b_n J_n-H_n.
The stream function is

 psi=sum_n r^4 (J_n-I_n)/2 sin(2n theta).

This is the density-integrated Green formula of topics15 and19;
it can also be checked by differentiating the radial Poisson equation
and imposing its canonical endpoint conditions. Let S_n=(J_n-I_n)/2.
Then

 P_n=2n r^2 S_n, Q_n=r^2(4S_n+S_n'),
 q=ell-sum P_n cos(2n theta), v=sum Q_n sin(2n theta),
 rho_r=r^2 sum (3H_j+H_j') sin((2j+1)theta),
 rho_theta/r=r^2 sum (2j+1)H_j cos((2j+1)theta).

These expressions avoid importing the numerics team's exponential
polynomial or operator-image implementation.

## Finite cells

On each spline span the exact polynomial is reconstructed from the
original B-spline coefficients. Forward stable integration gives
I at the left endpoints and backward stable integration gives J at
the right endpoints. Each integral uses phi_p(z)=integral_0^1
exp(zu)u^p du, with its convergent Taylor series and explicit remainder
as in proof 56. The independent source-neighborhood code of proof 66
supplies the local Taylor jets and the exact polynomial-plus-exponential
remainder bounds for S and its derivatives.

The outer continuation is a finite sum of exp(lambda tau) times
polynomials, tau=t-t_plus. The I particular solution solves
(D+a_n)I=H_(n-1), the J particular solution solves
(D-b_n)J=-H_n, and the I homogeneous coefficient is fixed by its
reconstructed endpoint value. The positive denominators in the J
formula enforce its canonical infinity condition. Every nonzero
denominator in the I formula is checked exactly.

A finite interval is enclosed by shifting each exponential polynomial
to its midpoint, collecting its Taylor coefficients through degree N,
and bounding its omitted exponential series termwise. For a term
exp(lambda x) sum_(p<=P)c_p x^p on |x|<=h, the remainder is at most

 sum_p |c_p|h^p exp(|lambda|h)
                   (|lambda|h)^(N-p+1)/(N-p+1)!.

This follows directly from the exponential Taylor remainder. All
arithmetic, trigonometric interval values and matrix products use Arb.
For tan(theta)sin(2n theta), division by a vanishing cosine is avoided:
for low n use

 sin(theta) 2 sum_(j=1)^n (-1)^(n-j)sin((2j-1)theta),

and for higher n use its absolute bound2n. This holds on the entire
closed quadrant, including the vertical axis. Refining an angular cell
and taking the smallest certified child lower bound preserves coverage.

## Inner half-line

Put tau=t-t_minus=-w<=0. Each H_j is a constant plus powers
exp(lambda tau) times polynomials, with lambda>=0. All nonconstant
exponents are positive. Multiplication by r^2 changes every exponent
to lambda+2>0. The I particular polynomial has denominators
lambda+a_n>0 and is bounded termwise on the half-line.

For n>=2 the J homogeneous term has exponent b_n+2>0 after
multiplication by r^2. A monomial forcing exp(lambda tau)tau^p
has weighted convolution bounded by

 exp(-(b_n+2)w) integral_0^w exp((b_n-lambda)u)u^p du
 <= p!/(lambda+2)^(p+1).

A second valid bound, when b_n+2>0, is

 sup_(u>=0) exp(-(lambda+2)u)u^p /(b_n+2).

Both follow by writing the integrand as the product of the two
nonnegative decaying factors and extending one integral. They remain
valid at exact and near resonance, without dividing by lambda-b_n.
For n=1 the homogeneous contribution to both P_1 and Q_1 is exactly
c by normalization. Its particular solution has denominators
lambda+2>0 and is treated separately.

Thus obtain error bounds E_P=sum|P_n-c delta_(n1)| and
E_T=sum2n|Q_n-c delta_(n1)|, and G>=|grad rho|.
For every theta the limiting anisotropic expression is the constant
b0+aA. Consequently

 d>=D-E_P,
 m_a>=b0+aA-a E_P-a E_T-G,
 m_R>=b0-A/8-E_P/8-G.

These are uniform on the entire inner half-line. The last inequality
uses q>=-A-E_P and mu_R'=1/4 there.

## Outer half-line

Choose a finite outer cutoff tau=T after the exact continuation begins.
Every term in P,Q and the gradient has a strictly negative exponent
there. Shift to u=t-t_plus-T>=0 and bound each term
c_p exp(-sigma u)u^p by |c_p|p!/sigma^p. This follows from
exp(sigma u)>=(sigma u)^p/p! and includes p=0.
Let E_P=sum|P_n|, E_T=sum2n|Q_n| and G>=|grad rho|.
Both weights have radial derivative -5/4, so

 d>=ell-E_P,
 m_a>=b0-5ell/8-5E_P/8-a E_T-G,
 m_R>=b0-5ell/8-5E_P/8-G.

All upper bounds are computed outward and all lower bounds downward.
The half-line inequalities and the finite-cell cover together imply
the reported global claims, if and only if the acceptance checks pass.

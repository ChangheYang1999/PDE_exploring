# The exact potential quotient has no further density gauge

Status: new theorem, OPEN pending independent Opus review. This strengthens
T4-195/N4-158 only at the potential-to-density map. It says nothing about
the kernel of the stationary PDE linearization.

## Statement

Fix c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
and p_j=(3+gamma-j delta)/2. Let V be any finite real span of functions

    chi_(j,m,Q)(x,y) = H_m(x,y) (1+r^2)^(p_j-m) Q(t),
    H_m=Re(x+iy)^(2m), t=r^2/(1+r^2), r^2=x^2+y^2,

where j belongs to {0,...,7}, m is a nonnegative integer, and Q is an
ordinary real polynomial. Define rho[chi]=-partial_y Delta chi.
Then rho:V -> C^infinity(R^2) is injective.

Consequently the exact candidate007 potential span of dimension1922
also gives a density span of dimension1922. The coefficient-to-density
map has exactly1060 kernel dimensions, all accounted for by the
zero-potential relations of N4-158/T4-195. This is an exact finite-span
statement; no conclusion about norm conditioning or PDE invertibility
is included.

The same proof applies to any finite set of j>=0 for which p_j is not
an integer and p_j-p_k is not an integer for distinct labels j,k.

## 1. Decay after four derivatives

Every displayed generator is smooth and even in x and in y. At r>=1,
all its Cartesian derivatives of order k<=4 are O(r^(2p_j-k)).
To verify this, write Q(t) as a finite sum of monomials. A term is

    H_m r^(2w) (1+r^2)^(p_j-m-w),

a polynomial of degree2m+2w times a smooth radial power. Repeated
product and chain rules lower the exterior power by one per derivative.
This argument is valid for all real exponents p_j-m-w; its constants
may depend on the fixed generator.

Since j>=0 and delta>0, 2p_j<=d=3+gamma<4. Thus every chi in V obeys

    chi=O(r^d), D^4 chi=O(r^(d-4)), d<4.            (1)

## 2. A zero density forces a quadratic polynomial potential

Suppose rho[chi]=0. Then partial_y Delta chi=0, so Delta chi=f(x) for
a smooth function f. Differentiation in x gives

    f''(x)=partial_x^2 Delta chi(x,y).

Fix x and let |y| tend to infinity. Equation(1) makes the right side
tend to zero. Therefore f''=0. Evenness in x implies f is constant,
say f=K. Hence psi=chi-K r^2/4 is an entire harmonic function, even
in both coordinates and bounded in absolute value by C(1+r^d).

Here is the elementary polynomial conclusion without an unquoted
Liouville theorem. Each angular Fourier coefficient a_n(r) of psi
satisfies the radial harmonic equation

    a_n''+a_n'/r-n^2 a_n/r^2=0.

For n>=1 its solutions are A_n r^n+B_n r^-n. Smoothness at r=0 forces
B_n=0. The n=0 solutions are A_0+B_0 log r, and smoothness forces B_0=0.
The growth bound with d<4 forces A_n=0 for n>=4: indeed
|A_n| r^n=|a_n(r)|<=C'(1+r^d), and let r tend to infinity. Evenness in
y removes sine modes; evenness in x leaves only even cosine modes.
Thus psi=A+B r^2 cos(2theta), and

    chi=A+B(x^2-y^2)+K r^2/4.                     (2)

The angular Fourier equations hold by differentiating a smooth function
on every compact annulus. Fourier uniqueness on each circle completes
the argument. No growth estimate for the Fourier series is assumed.

## 3. No nonzero quadratic polynomial belongs to V

First separate the angular labels m by orthogonality. Fix m and put
u=(1+r^2)^-1. Its nonzero angular coefficient from branch j is

    r^(2m) u^(m-p_j) Q_j(1-u).

Divide by the common r^(2m) on r>0. Each nonzero polynomial Q_j(1-u)
has a first nonzero term b_j u^(k_j), with k_j a nonnegative integer.
The resulting leading exponent m-p_j+k_j has fractional part determined
by p_j. For different j these exponents cannot agree, since p_j-p_k is
not an integer.

For m=0, the angular coefficient of(2) is A+K r^2/4, a finite Laurent
polynomial in u with integer powers. For m=1 it is B r^2; after division
by r^2 it is constant. For m>=2 it is zero. Each target therefore has
only integer powers. No exponent of a nonzero branch can coincide with
a target exponent, since p_j is not an integer. A proposed equality
between branches and such a target has a unique least exponent among
its nonzero terms. Divide by that power and let u tend to zero; its
nonzero coefficient cannot vanish. Thus all branches and the target
are zero. In particular chi=0, proving injectivity.

All nonintegrality conditions hold exactly for j=0,...,7 and are checked
with rational arithmetic in verification/parameters.json. The numerical
dimension consequence uses the independently confirmed T4-195 rank.

## Scope

The result excludes a hidden harmonic or y-independent-density gauge
inside this particular finite function space after its polynomial
redundancy is removed. It does not exclude a true kernel of L on the
resulting density functions, a kernel created by finite sampling, or
poor conditioning. Constraints and the infinite-dimensional complement
still require their separate checks. No coefficient optimization,
server, external compute or formal proof-assistant build is used.

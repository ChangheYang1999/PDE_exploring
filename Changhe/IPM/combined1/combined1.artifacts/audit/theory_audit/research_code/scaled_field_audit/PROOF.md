# Independent audit of rational scaled Cartesian fields

## Statement and scope

Let c>1 be rational, gamma=1/c, delta=1-gamma and
p_j=(3+gamma-j delta)/2. The finite potential is an exact rational
combination of

    H_m(X) (1+|X|^2)^(p_j-m) t_R^w u_R^q P_n(2t_R-1),
    H_m=Re(x+i y)^(2m), t_R=|X|^2/(R^2+|X|^2),
    u_R=R^2/(R^2+|X|^2), R in {1,10,100},

where j,m,w,q,n are nonnegative integers. Mono has n=q=0; leg has
R=1,q=0; legq has R=1. The fields are rho=-chi_xxy-chi_yyy,
u1=-chi_xyy, u2=chi_xxy, rho_x=-chi_xxxy-chi_xyyy and
rho_y=-chi_xxyy-chi_yyyy. The residual is
F=(cx+u1)rho_x+(cy+u2)rho_y-rho.

The claim being audited is the algebraic field engine in N4-191, not
candidate010's full-plane moments. The proof below verifies the
representation and derivative recurrence. Independent Cartesian jets
check every derivative through order4 on the manufactured fixtures.

## Rational radial representation and its domain

Put S=1+r^2, t=r^2/S and v=1-t. Since H_m=r^(2m)cos(2m theta),
the radial amplitude after extracting S^p_j is

    A=t^(m+w)(R^2 v)^q P_n(2t/L-1)/L^(w+q),
    L=R^2-(R^2-1)t=1+(R^2-1)v.

If P_n(z)=sum a_k z^k, its common numerator is
sum a_k(2t-L)^k L^(n-k), with extra denominator L^n.
This proves the exact constructor formula, including n=0 and R=1.
Both allowed nonconstant factors 1+99v and1+9999v are positive on
[0,1]. A rational field stores P(t) divided by nonnegative integral
powers of those factors. Addition uses the componentwise maximum of
the powers, multiplication adds them, and differentiation gives

    (P/L^k)'=P'/L^k+k(R^2-1)P/L^(k+1).

The plus sign is necessary because L' is negative. Equality follows
by a common denominator. Division by t^k is allowed only when the
first k numerator coefficients vanish exactly. The denominator has
nonzero constant term, so that test is both necessary and sufficient.

## Cartesian recurrence

For a total derivative of order d represented by S^p r^(-d) A(t)
trig(n theta), its Euler radial derivative has numerator
2t(1-t)A'+(2pt-d)A. Use
partial_x=cos theta partial_r-sin theta r^(-1)partial_theta and
partial_y=sin theta partial_r+cos theta r^(-1)partial_theta.
Put C=t(1-t)A'+ptA. For x differentiation the n-1 and n+1
amplitudes are C+(n-d)A/2 and C-(n+d)A/2. For y differentiation
these amplitudes have respectively signs (+,-) on sine input and
(-,+) on cosine input, with the trigonometric kind exchanged.
Negative sine frequencies reverse sign; cosine frequencies do not;
sine frequency zero vanishes. These identities follow directly from
angle addition and remain true for n=0 because the equal folded
frequencies are added. Induction proves every stored derivative.
At r=0 this particular representation has removable factors; the
smooth original potential defines the value. The engine is evaluated
only at r>0, including points on either coordinate axis.

## Independent local Cartesian proof and implementation

At any rational X0 write X=X0+Z and work in the polynomial ring
Q[Z1,Z2] modulo monomials of total degree at least5. Let a(Z) be
any polynomial with positive constant a0. Then for real rational e,

    a(Z)^e=a0^e sum_(k=0)^4 binom(e,k)((a-a0)/a0)^k
                         modulo terms of degree at least5.

This follows from the ordinary Taylor series on a neighborhood of X0;
its omitted terms have degree at least5. For integral e all retained
coefficients, including a0^e, are rational. For the factor S^(p_j-m)
keep only S0^(p_j-m) as an outward Arb power; every other coefficient
is exact. Expand the shifted Legendre polynomial independently as

    P_n(2z-1)=sum_(k=0)^n (-1)^(n+k) C(n,k) C(n+k,k) z^k.

Thus each generator is assembled in Cartesian coordinates as a sum of
H_m S^(p_j-m) R^(2q) (r^2)^(w+k)(R^2+r^2)^(-w-q-k).
No radial differentiation or peer recurrence enters this calculation.
The coefficient of Z1^a Z2^b times a!b! gives chi_(a,b)(X0) exactly
up to the enclosing nonintegral S0 power. All fields then follow from
the displayed Cartesian differential definitions.

The peer engine is copied into this topic before execution. Compare
all15 derivatives through order4 and all6 physical fields at the
peer's three points and additional signed and axis points. Check
mixed derivative order by exact rational equality. New rational
arithmetic fixtures are checked against the quotient rule after
multiplying by the full denominator. Numerical agreement corroborates
the algebraic proof; it does not replace its domain assumptions.

## Dependencies and limits

Exact coefficients are in data/fixtures.json. Frozen N4 proof, code
and result are in source/. Hashes, precision, comparison flags and
real runtime belong in verification/. The trusted arithmetic base is
Python integers, python-flint exact rationals and Arb outward real
operations. No finite-difference approximation, mesh, quadrature,
server, JavaScript, cluster or Lean build is used. No inverse,
residual upper norm or existence statement follows from this audit.

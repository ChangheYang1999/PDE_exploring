# A universal velocity remainder cannot beat the single-mode lower bound

Status: independent T4 proof of the admissible single-mode test proposed
in the T2 theory worker's status file at09:55Z. Written before the checker. Independent
Opus comparison is requested before treating this result as AUDITED.

## 1. Statement, domain and exact test function

Fix -5<q<-3 and set a=-q>3. Use the canonical IPM velocity

    U[h]=(0,-h/2)+PV integral K(X-Y)h(Y)dY,
    K(Z)=(-z1 z2,(z1^2-z2^2)/2)/(pi |Z|^4).

Suppose a number E satisfies, for every real centrally odd C1 h with
finite weighted norm H_q and all |X|>=R0, where R0 is fixed,

    |U[h](X)+DK(X)M(h)| <= E H_q(h) |X|^q,                 (1)
    H_q(h)=max(sup (1+r)^(-q)|h|,
                    sup (1+r)^(1-q)|grad h|),
    M(h)=integral Y h(Y)dY.

Then necessarily

    E >= Etest(q) = (-q-1)/(2(-q)(-q-3)).                  (2)

This lower bound also applies if the domain in (1) is restricted to
S1 functions, since the test below is even in x and odd in y. It does
not apply to a proposed estimate restricted to stationary solutions
unless that estimate separately includes the test function. The test
is not asserted stationary and satisfies no imposed origin trace
hyperplane. Thus (2) concerns precisely the universal weighted C1
estimate used in T4-335, not every conceivable PDE-specific estimate.

Let

    h(x,y)=y(1+r)^(q-1)/a=f(r)sin(theta),
    f(r)=r(1+r)^(q-1)/a.

It is real, S1 and C1 on the plane. At the origin the additional
terms in grad[y(1+r)^(q-1)] are O(r), so the gradient is continuous.
Its weighted amplitude is at most1/a. Its weighted gradient has norm

    (1/a) sqrt([(1+q r)/(1+r)]^2 sin(theta)^2+cos(theta)^2).

Because |(1-a r)/(1+r)|<=a, this is at most1. At theta=pi/2 it tends
to1 as r tends to infinity. Hence H_q(h)=1 exactly. The first moment
converges absolutely and equals

    M(h)=(0,m),
    m=pi integral_0^infinity r^2 f(r)dr
     =6pi/[a^2(a-1)(a-2)(a-3)].                            (3)

The last identity is the elementary beta integral after t=r/(1+r).

## 2. Canonical velocity and its exact leading remainder

Solve Delta psi=h in the first sine mode using the whole-plane Green
formula

    psi(r,theta)=-sin(theta)/2 *
      [r^(-1) integral_0^r s^2 f(s)ds
                          +r integral_r^infinity f(s)ds]. (4)

This is regular at the origin and decays at infinity. It selects the
canonical Hessian velocity U=(psi_xy,-psi_xx). This can also be checked
by Fourier transform: Delta psi=h, and the decaying solution leaves
no polynomial harmonic term whose Hessian could alter U.

Since f(r)=r^q/a+O(r^(q-1)), rewrite the first integral as its total
integral minus the tail. The two tails in (4) give

    psi=-m sin(theta)/(2pi r)
       +r^(q+2)sin(theta)/[a(q+1)(q+3)]+O(r^(q+1)).         (5)

The error can be differentiated twice, with the expected loss of one
power for each radial derivative. This follows directly by
differentiating the integrals in (4) and the smooth expansion of f;
it is not obtained by differentiating an uncontrolled little-o term.
The angular dependence is a single sine and introduces no further
regularity issue.

The Hessian velocity of the first term in (5) is precisely
-DK(X)(0,m), including its sign. Let W be the Hessian velocity of
the second homogeneous term. Explicit Cartesian differentiation
using r^(q+2)sin(theta)=y r^(q+1) gives

    W/r^q = 1/[a(q+3)] *
       (cos(theta)[1+(q-1)sin(theta)^2],
       -sin(theta)[1+(q-1)cos(theta)^2]).                  (6)

Thus

    U[h]+DK M = W+O(r^(q-1))

uniformly in angle. At theta=pi/4 the Euclidean norm of (6) is
|q+1|/[2a|q+3|]=Etest(q). Divide (1) by r^q, use H_q=1, and let
r tend to infinity along that ray. This proves (2). The norm in
(6) has square proportional to
1+(q-1)(q+3)sin(theta)^2 cos(theta)^2, so that ray also maximizes
the homogeneous remainder for this test. No singular homogeneous
function is inserted into (1); the actual test is C1 at the origin.

## 3. Consequence for the existing endpoint closure test

Retain every hypothesis and definition of T4-380, especially its
uniform endpoint limit and finite H_q. Let H0 be a valid pointwise
lower bound, B the angular projection bound, g0 a positive reference
gradient lower bound, v0 an optional velocity lower bound, delta>0
and D=1-c(q-delta)>0. Set

    r0=[sqrt(2pi) H0 (v0+Etest g0)/(D B)]^(1/delta),
    alpha=-2q-2>0.

For every universal E admissible in (1), the square root of the CI
right-hand side is at most

    cap_crude=B r0^(q+1)/sqrt(alpha).                     (7)

This follows from380 and the monotonic decrease of that bound in E.
One may retain the radial shape of the same nonnegative error term,
which gives the sharper bound

    cap_delta=B r0^(q+1)
      *sqrt[1/alpha-2/(alpha+delta)+1/(alpha+2delta)]
     =B r0^(q+1)
      *sqrt[2delta^2/(alpha(alpha+delta)(alpha+2delta))].   (8)

Indeed the full positive part is no greater than
B[1-(r0/r)^delta]_+. Square, integrate against r^(2q+1) on
(0,infinity), substitute r=r0 s, and integrate the three powers.
The actual finite starting radius and other nonnegative errors only
reduce the integral. Formula (8) is also the delta-only integral
used as a diagnostic in the T2 theory worker's sharpE script; no numerical quadrature
or claim of equality for the full CI is involved.

Equations (7)-(8) bound this specific certificate, not the actual
solution distance. They do not exclude all small radii, establish
an upper H_q budget, or address a velocity estimate using additional
stationary-solution structure. They do show when even the best
universal E cannot make this CI reach a named target radius.

## 4. Verification and dependencies

The checker uses exact rational c, q, Etest and the accepted endpoint
coefficient maps. It recomputes the pointwise H0 and B rather than
rounding the peer values. It checks the Cartesian derivative and
Green coefficients symbolically, the beta integral at the exact
campaign exponent in Arb, and both cap expressions. Every target
radius is explicitly labeled in JSON; family ceilings and the actual
fixed sharpw radius are kept separate.

Dependencies are the canonical kernel convention, T4-335's endpoint
expansion and its finite-cutoff application, T4-375's gradient-limit
lemma, T4-380's pointwise minimization, and the original CI351. There
is no dependence on the proposed folded-kernel upper bound1.749109.

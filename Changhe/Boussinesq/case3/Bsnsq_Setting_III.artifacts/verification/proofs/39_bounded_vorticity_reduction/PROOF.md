# Decaying, bounded, and beta-two vorticity class reductions

Date:2026-10-20. Status: CONFIRMED by the independent verifier.
These are independently checked versions of the lead's D-prime and
D-double-prime extensions and its beta-two extension. No endpoint is
claimed.

## 1. Statement and notation

Let beta>=2 and let U,Omega,Theta be smooth on R2, with

    div U=0, partial_y U1-partial_x U2=Omega,
    V=U-U(0), W=beta X+V,
    W.grad Omega+Omega=Theta_x,
    W.grad Theta=(beta-2)Theta.                         (1)

Suppose U=o(r), uniformly as r=|X| tends to infinity. Then each of the
following hypotheses is sufficient for the conclusion below:

(i) Omega(X)->0 uniformly, without an assumed rate;
(ii) Omega is bounded;
(iii) beta=2, without any vorticity growth assumption.

Conclusion: for every eta>0,

    |Omega(X)|<=C_eta (1+r)^(-1/(beta+eta)),             (2)

Theta is polynomially bounded, and

    V(X)=int [K(X-Y)-K(-Y)] Omega(Y)dY,
    K(Z)=(Z2,-Z1)/(2 pi |Z|^2),                         (3)

where the integral converges absolutely. The implication from(i) is
included as a separate proof, although it is subsumed by(ii). If the
standing B2 parity, axis-zero temperature and nonzero center jet are
also present, the solution therefore belongs to class A. No moment
condition on the absolute vertical velocity is added.

## 2. Escape from a fixed circle

The smooth W has at most linear growth, so its flow exists at every
finite time. For any eps in(0,min(1,beta)), take R sufficiently large
that |V(X)|<=eps |X| outside B_R. Then the radial derivative along W
is between(beta-eps)r and(beta+eps)r. Every exterior point is a unique
point phi_t Z with Z in S_R, t>=0, and

    R e^((beta-eps)t)<=|phi_t Z|<=R e^((beta+eps)t).     (4)

All compact-circle initial values and derivatives are uniformly bounded.
The temperature equation gives

    Theta(phi_t Z)=e^((beta-2)t)Theta(Z),
    |Theta(X)|<=C_eps r^p, p=(beta-2)/(beta-eps)<1.      (5)

Writing w=|W(phi_t Z)|, the same radial estimates on any interval[s,t]
give

    C_eps^-1 e^((beta-eps)(t-s))<=w(t)/w(s)
                      <=C_eps e^((beta+eps)(t-s)).     (6)

These conclusions use no vorticity assumption.

## 3. Local strain estimate when vorticity is bounded

Let r=|X| and M_X=sup_{B(X,r/2)}|Omega|. Suppose M_X is uniformly
bounded for large r. We claim

    |DV(X)|<=o(1)+C M_X+C A_X/r,
    A_X=sup_{B(X,r/4)}|Theta|.                         (7)

The o(1) term is uniform at infinity and follows from U=o(r).
In particular DV is bounded under(ii), and tends to0 under(i), because
A_X/r tends to0 by(5).

To prove(7), choose chi' supported on B(X,r/2), equal to1 on
B(X,3r/8), with derivative bounds at scale r. Write
V=K*(chi' Omega)+H'. The convolution is bounded by C r M_X; H' is
harmonic in B(X,3r/8), and its gradient in B(X,r/4) is bounded by
o(1)+C M_X. The elementary near/far difference-kernel split gives

    |K*(chi' Omega)(P)-K*(chi' Omega)(Q)|
                 <=C M_X h[1+log(r/h)], h=|P-Q|<=r/2.

As M_X is bounded and h[1+log(r/h)]<=C r^(1/2)h^(1/2),

    |W(P)-W(Q)|<=C r^(1/2)|P-Q|^(1/2)                 (8)

on B(X,r/4), with C independent of X. No bound on DOmega is used.

For smooth f supported in this ball, |f|<=A and |W.grad f|<=C A,
use the identity

    W(X).grad(K*f)(X)=K*div(W f)(X)
          +int DK(X-Y)[W(X)-W(Y)]f(Y)dY.               (9)

The first term is bounded by C r A. The second is also C r A,
because(8) makes its singularity integrable:
r^(1/2)int_0^{r/4}rho^(-1/2)d rho<=C r. The delta terms in the
distributional derivative of K cancel in the commutator. Since
|W(X)|>=c r, this bounds the derivative of K*f in the W direction
by C A. A divergence-free matrix in the basis(e,e-perp), e=W/|W|,
has entries [[a,b],[c,-a]] and c-b=-f. Its full norm is therefore
bounded by its first-column norm plus C|f|. Consequently

    |D(K*f)(X)|<=C A.                                 (10)

Choose chi supported in B(X,r/4), equal to1 on B(X,r/8).
For f=chi Theta, the temperature equation and |W Dchi|<=C give
|W.grad f|<=C A_X, so(10) gives |D(K*(chi Theta))(X)|<=C A_X.
For f=chi Omega, instead use

    div(W f)=(2 beta-1)chi Omega+Omega W.grad chi+chi Theta_x.

The first two terms and the commutator in(9), divided by |W(X)|,
are bounded by C M_X. The last term is

    K*(chi Theta_x)=partial_x(K*(chi Theta))
                                  -K*((partial_x chi)Theta),

bounded by C A_X; divided by |W(X)| it is C A_X/r.
The same matrix argument gives
|D(K*(chi Omega))(X)|<=C M_X+C A_X/r. Finally
H=V-K*(chi Omega) is harmonic in B(X,r/8), bounded there by
o(r)+C r M_X, so |DH(X)|<=o(1)+C M_X. This proves(7).
All cutoffs are frozen at the evaluation point when taking derivatives.

## 4. Direct conclusion when Omega tends to zero

Under(i), (7) gives DV->0. Put q=grad Theta. Differentiating(1),

    q'=-(2 I+DV^T)q                                   (11)

along each orbit. For any small eps>0, choose the starting sphere
large enough that |DV|<=eps outside it. Then
|q(phi_t Z)|<=C e^((-2+eps)t). If eps<1, the first equation of(1)
implies

    e^t Omega(phi_t Z)=Omega(Z)+int_0^t e^sigma Theta_x(phi_sigma Z)d sigma,
    |Omega(phi_t Z)|<=C e^-t.                          (12)

Using the upper bound in(4) gives exponent-1/(beta+eps).
For any prescribed eta>0 choose eps<min(eta,1); the stronger exponent
implies(2), after enlarging the constant on the compact core.

## 5. Moving-frame argument for bounded Omega

Under(ii), (7) only gives bounded DV. This is enough because the
exact gradient system is triangular in the direction of W.
Write e=W/w, n=(-e2,e1), and N=DV in this oriented frame as
[[a,b],[c,-a]]. Then

    w'/w=beta+a, e'=c n, n'=-c e.

For p=q.e and ell=q.n, equation(11) becomes

    p'=-(2+a)p,
    ell'=(-2+a)ell-(b+c)p.                             (13)

The rotating-frame derivatives cancel the c ell term in the first
equation. In the second equation they supply the extra-c p term.
By(6),

    |int_s^t a|<=eps(t-s)+log C_eps.

Thus variation of constants gives

    |q(t)|<=C e^(-(2-eps)t)[1+int_0^t |DV(phi_sigma Z)|d sigma]
           <=C(1+t)e^(-(2-eps)t).                     (14)

For eps<1 this makes e^t Theta_x integrable over positive times,
uniformly over the compact starting sphere. Equations(12),(4) again
give(2). This independently verifies the lead's D-double-prime
conclusion; it does not assume pointwise small strain in advance.

## 6. Beta two without a vorticity bound

At beta=2, q.W=0 by(1), so p=0 on every exterior orbit. The second
of(13) reduces to ell'=(-2+a)ell. Since a=w'/w-beta,

    ell(t)=ell(0)e^(-(beta+2)t)w(t)/w(0).

By(6), |q(t)|<=C e^(-(2-eps)t). Equations(12),(4) then prove(2),
with no appeal to section3, no vorticity bound, and no strain bound.
Temperature is bounded by(5) and smoothness on the compact core.

## 7. Canonical inverse, dependencies and scope

Choose a decay exponent d in(0,1/beta). Formula(2) permits such a d.
The integral B in(3) converges near0 and X by smoothness and the
integrability of K, and at infinity by the difference-kernel bound
C_X|Y|^-2 times |Omega|<=C|Y|^-d. A split into |Y|<r/2,
r/2<=|Y|<=2r and |Y|>2r gives |B(X)|<=C(1+r^(1-d)). For the
subtracted kernel in the inner region use int_0^r(1+rho)^-d d rho;
for the ordinary kernel there use r^-1 int_0^r rho(1+rho)^-d d rho;
the middle and outer pieces obey the same bound by local kernel
integrability and the difference-kernel estimate.
Distributionally div B=0 and -curl B=Omega; smoothness follows locally
from elliptic regularity. V-B is therefore entire harmonic and
sublinear. The harmonic gradient estimate on expanding balls makes
its gradient zero. Since V(0)=B(0)=0, their difference vanishes.
This proves(3).

Dependencies: elementary flow estimates, local harmonic estimates,
the explicit Biot-Savart kernel and its distributional divergence/curl,
local elliptic regularity and the proved moving-frame equations.
The lead's auditL response was not taken on trust: each local estimate,
frame derivative and exponent conversion has been rederived here.
The lead also has a claimed averaged-Lp extension; that extension is
not asserted or checked in this packet. None of(i)-(iii) excludes the
resulting nontrivial class A. Smooth beta>=2 remains open.

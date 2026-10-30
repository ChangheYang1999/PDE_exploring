# Complete angular envelopes for scaled candidates

Written before implementation on 2026-10-29. The preparation record gives
its real timestamp and hash. This result compares like quantities in the
floating diagnostics and exact complete-plane weak tests.

## Statement and hypotheses

Let c>1 and let rho be a smooth real S1-symmetric reference on R2 with
canonical divergence-free velocity u. Assume u=O(r^gamma) and
grad rho=O(r^(gamma-1)) for gamma<1. Let

    F=(cX+u).grad rho-rho.

Suppose h belongs to real S1-symmetric L2(R2), U[h] is its canonical
velocity with ||U[h]||2<=||h||2, and

    F+div((cX+u)h)-(2c+1)h+U[h].grad rho+div(U[h]h)=0

holds in distributions. Assume the products are locally integrable.
For odd n>0 and integer K>=(n-1)/2, put

    t=r^2/(1+r^2), v=1-t,
    phi=r v^2 t^K sin(n theta),
    d_K(t)=(2K+1)-(2K+4)t,
    I=int F phi,
    A=||(2c+1)phi+cX.grad phi||2,
    Bbar^2=int |u|^2 v^4 t^(2K) (d_K(t)^2+n^2) dX,
    Cbar^2=int |grad rho|^2 r^2 v^4 t^(2K) dX.

For any proven H>=||grad phi||infinity, define Dbar=A+Bbar+Cbar. Then

    |I| <= Dbar ||h||2 + H ||h||2^2,
    ||h||2 >= 2|I|/(Dbar+sqrt(Dbar^2+4H|I|)).

The complete transport and density norms

    M=||(2c+1)phi+(cX+u).grad phi||2,
    C=||phi grad rho||2

satisfy M<=A+Bbar and C<=Cbar. Thus a smaller envelope-based necessary
bound than the complete M+C bound does not, by itself, exhibit numerical
integration error. All these statements concern one specified reference,
probe and fixed c, with no optimality or existence assertion.

## Weak argument and gradient bound

The numerator r^(2K+1) sin(n theta) is a homogeneous harmonic polynomial
of degree n times a nonnegative integer power of r^2. Hence phi is smooth
at the origin. At infinity phi=O(r^-3) and grad phi=O(r^-4). Radial cutoffs
therefore permit testing the displayed distributional equation. Terms
with cutoff derivatives tend to zero: linear coefficients multiplying h
are square integrable by the sublinear background bounds, and U[h]h is
integrable by Cauchy-Schwarz.

Integration by parts, divergence-free u and the identity div(cX)=2c give

    I=int h ((2c+1)phi+(cX+u).grad phi)
      -int phi U[h].grad rho + int h U[h].grad phi.

Signs do not affect the absolute bound. The two polar components of the
probe gradient are v^2 t^K d_K sin(n theta) and n v^2 t^K cos(n theta).
Their length is bounded by v^2 t^K sqrt(d_K^2+n^2). The pointwise bounds
|u.grad phi|<=|u| |grad phi| and |phi|<=r v^2 t^K prove the M and C
inequalities. Cauchy-Schwarz proves the quadratic inequality. Solving
it gives the stable root above.

One elementary admissible gradient cap, used to reproduce the old 007
calibration, is

    H0=max(2K+1,3) * 4 K^K/(K+2)^(K+2)  (K>0),
    H0=3  (K=0).

Indeed n<=2K+1, |d_K|<=max(2K+1,3), and the maximum of v^2 t^K is
4 K^K/(K+2)^(K+2). For new candidates we reuse the sharper global critical
point certificate from their full weak test. Its hash, n and K are
checked. A mesh maximum times 1.05 is not a general gradient certificate.
A particular saved mesh value can be validated as an upper bound only if
it exceeds a separately proven global bound for that same probe.

## Exact whole-plane radial reduction

Let delta=1-1/c and p_j=2-(j+1)delta/2. The exact rational scaled generator
class, differentiated in Cartesian coordinates, has representations

    u_i=r sum_(j,l) v^((j+1)delta/2) U_(i,j,l)(t) trig_l(theta),
    partial_i rho=sum_(j,l) v^((j+1)delta/2) R_(i,j,l)(t) trig_l(theta).

Each U and R is rational with denominator a product of positive factors
1+a v, where a is 99, 624, 2499 or 9999. These denominators have no zeros
on the integration interval. The stored derivative maps contain a common
t^2, which is divided out exactly before this representation is used.
The finite field expansions include every actual raw generator.

For each Cartesian component, square the coefficients at matching angular
frequencies and group by ell=j+j'+2. Distinct radial-branch pairs have
factor two. A constant cosine frequency has an additional factor two,
because its full angular square integral is 2pi rather than pi.
Cross terms between different frequencies vanish. Let W_ell^u and
W_ell^rho denote the resulting rational sums, already including these
factors. Since r dr=-dv/(2v^2),

    Bbar^2=(pi/2) sum_ell int_0^1
      v^(1+ell delta/2) (1-v)^(2K+1)
      [((2K+4)v-3)^2+n^2] W_ell^u(v) dv,

    Cbar^2=(pi/2) sum_ell int_0^1
      v^(1+ell delta/2) (1-v)^(2K+1) W_ell^rho(v) dv.

The radial Jacobian and both Cartesian components are included. This is
exact integration of the defined envelopes, rather than quadrature or an
angular truncation. For the finite candidates the smallest ell and all
endpoint exponents are checked, and each integral is convergent.

Set a=2K+2, L0=3c+1+2cK and L1=2c(K+2). The remaining exact norm is

    A^2=(pi/2) [L0^2-2L0 L1 a/(a+2)
          +L1^2 a(a+1)/((a+2)(a+3))]/[a(a+1)].

This is the beta integral of t^(2K+1)(1-t)(L0-L1 t)^2. Its angular factor
is pi for every positive n.

For each rational group, the existing factored-moment proof decomposes
the rational function by exact polynomial division and partial fractions
in v, retaining (1-v)^(2K+1) as a factor. Beta moments and positive-pole
moments are evaluated by outward Arb arithmetic, with independent scalar
calibrations and exact decomposition replay. Every coefficient, pole,
exponent and cancellation is retained. Positive complete energies and
relative accuracy above 150 bits are required.

## Verification and comparison protocol

Before new candidate use, the complete A, Bbar and Cbar of the accepted
007 probe (21,522) are reproduced against the old independent polynomial
construction. Its I and elementary H0 reproduce the old envelope root.
A manufactured constant cosine mode checks its factor two explicitly;
a sine zero mode is rejected. At rational physical points the converted
coefficient fields are compared with the complete Cartesian evaluator.

For 016 and 017, I, M, C and the global gradient certificate are taken
from the hash-bound complete weak computation at the same n and K.
Their original candidate and dependency hashes are checked. New A,
Bbar and Cbar are computed by the exact formulas above. The inequalities
M<=A+Bbar and C<=Cbar are checked on their containing intervals as a
further candidate-specific consistency test, not used as a substitute
for their analytic proof.

The saved N1 FLOAT JSON and current source text are copied and hashed.
Only the saved JSON data are read; no foreign Python code is executed.
Each saved raw candidate hash must equal the exact tested source hash.
Differences and relative differences compare its printed approximations
with the whole-plane exact-envelope quantities. These differences combine
coefficient rounding, finite radial range, quadrature and other evaluation
effects. They do not isolate a cause without additional controlled tests.
The N1 routine uses a different B bound and H bound from weak_tests2 even
when n=1. Source documentation saying otherwise needs that qualification.

New scaled-envelope calculations remain OPEN independent candidate-level
review. The regression test and exact arithmetic do not turn the original
FLOAT diagnostics into certified bounds, and no sampled maximum is
identified with a global one.

## Dependencies and scope

- ../angular_weak_probes/PROOF.md: polynomial version and old 007 envelope.
- ../joint_scaled_factored_weak/PROOF.md and code: exact rational fields.
- ../factored_pole_moments/PROOF.md: complete rational-pole integration.
- The individual 016/017 full weak proofs and hash-bound results.

All new code and outputs live in this topic's code/ and verification/
subfolders. The proof precedes implementation. Source copies are data
and review evidence only. There is no formal Lean development or new
axiom in this calculation. No upper residual norm, inverse estimate,
family-wide distance floor or exact stationary solution is claimed.

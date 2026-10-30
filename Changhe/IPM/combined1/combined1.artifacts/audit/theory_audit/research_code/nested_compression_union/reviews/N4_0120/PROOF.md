# Overlapping compression energies with commuting projections

## Statement

Let H be a real or complex Hilbert space and let K be a Hilbert-Schmidt
operator on H. Let P and Q be commuting orthogonal projections, and put
R = PQ. Then

    ||PKP||HS^2 + ||QKQ||HS^2 - ||RKR||HS^2 <= ||K||HS^2.       (1)

The left side is nonnegative. Finite rank and self-adjointness of K are
not needed for (1). For the numerical application, P and Q have finite
rank and K is self-adjoint.

Suppose further that H0 is a reducing subspace for K and the ranges of
P and Q lie in H0 perpendicular. If ||K||HS^2 <= C, the left side of (1)
can be subtracted from C to bound ||K restricted to H0||HS^2. Compression
energies from other mutually orthogonal reducing subspaces can also be
subtracted.

## Proof

The Hilbert-Schmidt operators on H form a Hilbert space, with the usual
trace inner product. The maps

    A(X) = PXP,     B(X) = QXQ

are orthogonal projections on that Hilbert space. Indeed, they are
idempotent, bounded, and self-adjoint in the Hilbert-Schmidt inner
product. For example, left and right multiplication by P are commuting
orthogonal projections, and their product is A.

Since P and Q commute, A and B commute, and

    AB(X) = RXR.

Thus E = A + B - AB is an orthogonal projection: self-adjointness is
immediate, and expansion using A^2=A, B^2=B, and AB=BA gives E^2=E.
Consequently

    0 <= <K,EK>HS <= ||K||HS^2.

For any orthogonal projection J, <K,JK>HS = ||JK||HS^2. Substitution of
A, B and AB gives (1) and its lower bound.

For the reducing-subspace statement, write K as the orthogonal direct
sum of its restrictions to H0 and H0 perpendicular. Apply (1) to the
second restriction. Hilbert-Schmidt squared norms add under this
orthogonal direct sum, proving the claimed subtraction. Apply the same
argument to further mutually orthogonal reducing subspaces to obtain
the last assertion.

## Application to the Poisson test spaces

Use the Poisson derivative tests specified in the parity audit proofs.
In the even-even parity class, let P project onto all tests with radial
index 0 through N-1 in each cosine harmonic 0,2,...,M. Let Q project
onto the radial harmonic-zero tests with indices 0 through d-1, where
d >= N.

Different angular harmonics are orthogonal in L2 of the plane. The
harmonic-zero part of the P space is contained in the Q space, and
every other harmonic in the P space is orthogonal to Q. On harmonic
zero the projections are nested and commute; on the other harmonics
at least one is zero. Hence P and Q commute. Their intersection is
exactly the harmonic-zero span of indices 0 through N-1.

If Tangular is the sum of three complementary parity compression
energies, and Tradial(k) is the harmonic-zero energy for k tests, then

    Tunion = Tangular + Tradial(d) - Tradial(N)

is a valid lower bound for the complementary squared Hilbert-Schmidt
energy. It is not necessarily the exact energy of the combined span:
the uncomputed cross entries between additional radial tests and the
nonradial tests are omitted, with nonnegative squared contributions.

Given a certified full squared bound kappa2, the target parity
restriction has operator norm at most sqrt(kappa2 - Tunion). If the
separate signed compression theorem has target energy Ttarget and a
nonnegative upper certificate q, its quadratic-form upper bound becomes
sqrt(kappa2 - Tunion - Ttarget + q^2), under that theorem's hypotheses.

## Dependencies and verification contract

The general proof uses only the Hilbert space of Hilbert-Schmidt
operators and commuting orthogonal projections. The Poisson application
uses the test definitions and Gram formulas in
../parity_budget_audit/PROOF.md and ../parity_angular_audit/PROOF.md.
The signed extension uses ../signed_compression_audit/PROOF.md.

For numerical use, every record must identify the same exact candidate
and operator convention. The common radial Gram and coupling entries
must agree exactly. The values Tradial(d), Tradial(N), and Tangular
must themselves have independent verified records. Arithmetic on
unreviewed component values does not independently certify them.

This is an independent review of T4's nested-compression lemma.
It supplies no candidate theta bound, low-generator domain theorem,
high-space inverse, or nonlinear closure.

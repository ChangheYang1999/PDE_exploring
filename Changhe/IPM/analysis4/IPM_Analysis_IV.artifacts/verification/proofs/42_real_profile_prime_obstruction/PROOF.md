# Prime obstructions for every finite real profile with a first harmonic

Status: CONFIRMED after the theory part's independent adversarial review, 2026-10-31T03:56:16Z. Exact hypotheses and limitations below remain in force.

## Statement

Fix a finite nonzero real sine polynomial

\[
 f_1(\theta)=\sum_{k=0}^{M}\alpha_{2k+1}\sin((2k+1)\theta),
 \qquad \alpha_1\ne0.
\]

There is a finite set S of primes, depending on this fixed coefficient vector, such that for every prime p>=5 outside S and every even integer 4<=a<p, the pure stationary stream recurrence at delta=a/p fails its first compatibility condition, at order p. In particular the incompatible rational parameters are dense in (0,1).

Combined with the first-pole and Baire argument of topic15, the pure far-field density series for this fixed profile has zero convergence radius on a dense residual set of irrational delta in every open interval in (0,1). Combined with the independently proved Brjuno convergence theorem, it has a positive radius for almost every delta. The residual divergent set therefore has measure zero. This statement concerns a fixed finite real leading profile; it makes no claim that all non-Brjuno parameters diverge.

## 1. The polynomial version of the prime congruence

Let X_1,X_3,...,X_(2M+1) be indeterminates, and generate the recurrence with these leading amplitudes. At delta=a/p the order-p compatibility coefficient is a homogeneous degree-p polynomial

\[
 K_{p,a}(X_1,X_3,\ldots,X_{2M+1})\in\mathbb Q[X_1,X_3,\ldots,X_{2M+1}].
\]

The induction in topic31 proves that its coefficients lie in Z_(p), the rationals with denominator prime to p. That proof works over the polynomial ring as well: all divisors used through order p depend only on a,p and the order or Fourier index, and are units after the displayed factors of p have cancelled.

The characteristic-p generating identity gives

\[
 F_p\equiv f_1^p[(-1)^{(p-1)/2}\cos(\theta)^{p-1}-1].
\]

By Frobenius, each leading amplitude enters as its p-th power. Every leading frequency at least three moves to absolute frequency at least 3p before multiplication by cos(theta)^(p-1), and so cannot reach the resonant frequency a-3<p. Only the first input frequency contributes. Thus the precise polynomial congruence is

\[
 \boxed{K_{p,a}(X)\equiv(-1)^{(a-4)/2}X_1^p\pmod p.}
 \tag{1}
\]

For numerical rational coefficients, the p-th power can be replaced by the coefficient itself modulo p; for indeterminates or extension fields it must be retained. This distinction is needed below.

## 2. Algebraic coefficient vectors

First suppose all alpha_k are algebraic numbers, not necessarily real. Let F be a number field containing them. Include alpha_1^(-1) among the generators. Each of these finitely many algebraic numbers satisfies a monic polynomial with rational coefficients. There is an integer D>=1 such that all those polynomial coefficients belong to Z[1/D]. Hence

\[
 S_0=\mathbb Z[1/D,\alpha_1,\alpha_3,\ldots,\alpha_{2M+1},\alpha_1^{-1}]
\]

is integral over Z[1/D].

For a prime p not dividing D, the ring S_0/p S_0 is nonzero. Otherwise p would be a unit in S_0, and 1/p would be integral over Z[1/D]. A monic relation for 1/p, multiplied by p to its degree and then by a power of D clearing all denominators, would imply that p divides a power of D, a contradiction.

The image of alpha_1 in this quotient is a unit because its inverse was included. Localize further at the rational denominators of K_(p,a), which are all prime to p; equivalently tensor with Z_(p). This does not kill the quotient, since each integer prime to p is already a unit modulo p. Equation (1) therefore says that the image of K_(p,a)(alpha) is a nonzero unit, with sign. Consequently K_(p,a)(alpha) cannot vanish in characteristic zero. The same D works for every admissible a. This proves the theorem for algebraic coefficient vectors.

## 3. Specialize arbitrary real coefficients to algebraic ones

Now let the alpha_k be arbitrary real numbers with alpha_1 nonzero. The ring

\[
 R=\mathbb Q[\alpha_1,\alpha_3,\ldots,\alpha_{2M+1},\alpha_1^{-1}]
\]

is a nonzero finitely generated Q-algebra. Choose a maximal ideal m of R. The finite-type Hilbert Nullstellensatz says that the residue field R/m is a finite extension of Q. This is the only external algebraic theorem used here; a precise reference is The Stacks Project, Theorem 10.34.1, tag 00FV.

Let beta_k be the images of alpha_k in this residue field. They are algebraic numbers, and beta_1 is nonzero because alpha_1 was inverted in R. Every polynomial identity over Q satisfied by the original coefficient vector is preserved by the quotient homomorphism. In particular,

\[
 K_{p,a}(\alpha)=0\quad\Longrightarrow\quad K_{p,a}(\beta)=0.
\]

Section2 provides a single finite exceptional set of primes for the fixed algebraic vector beta. Outside it, the right side is false for every even 4<=a<p. Therefore the left side is false as well. This proves the asserted finite exceptional set for the original real profile.

The specialization is used only to rule out zero polynomial values. It does not preserve order, approximate sizes or the Fourier profile itself. No bound on the size of K_(p,a)(alpha) is inferred.

## 4. Dense poles and divergent irrational parameters

For any open interval I in (0,1), arbitrarily large primes outside the finite exceptional set have an even a with a/p in I and 4<=a<p. The first resonance is n=p. Its nonzero compatibility coefficient produces a nonzero pole in the next density coefficient, as proved in topic15. For a finite sine polynomial, the angular factor multiplying that pole is nonzero by its highest-frequency coefficient.

The open sets where a coefficient root exceeds a specified bound at an arbitrarily large order are therefore dense. Their countable intersection over bounds and starting orders is a dense residual subset of the irrational parameter space, and on it the coefficient-root limsup is infinite. The Brjuno theorem supplies the separate almost-everywhere positive-radius conclusion. These two notions of a typical parameter give different answers.

## Dependencies and evidence

Dependencies: topic31's characteristic-p calculation; topic15's first-pole and Baire argument; the Brjuno convergence theorem; and the finite-type Hilbert Nullstellensatz. The specialization theorem is applied to a nonzero finite-type Q-algebra, not to an arbitrary infinitely generated ring. Finite Fourier support is essential to this particular argument.

External reference inspected on 2026-10-31: The Stacks Project, Theorem 10.34.1 (Hilbert Nullstellensatz), tag 00FV, specifically its assertion about residue fields of maximal ideals in finite-type algebras. Source identifier: `https://stacks.math.columbia.edu/tag/00FV`.

Independent finite verification: code/polynomial_prime_audit.py computes the Cartesian recurrence over Q[u] for sin(theta)+u sin(3theta)+u^2 sin(5theta), and for u sin(theta)+sin(3theta). All14 cases at seven admissible (p,a) pairs through p=13 satisfy the exact polynomial congruence: respectively the constant sign and the sign times u^p. Every preceding Poisson identity is checked exactly. The actual run took 5.877024149987847 seconds (the exact recorded value is in verification/polynomial_checks.json). These finite checks do not substitute for the all-prime proof.

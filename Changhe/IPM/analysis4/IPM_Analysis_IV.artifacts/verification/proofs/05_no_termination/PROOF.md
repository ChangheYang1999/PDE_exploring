# No nonzero finite termination with finite angular polynomials

## Statement

Fix c>1 and delta=1-1/c. Suppose

\[
\rho=\sum_{n=1}^N r^{1-n\delta}f_n(\theta),\qquad
\psi=\sum_{n=1}^N r^{2-n\delta}g_n(\theta),
\]

where each f_n is a real finite odd-frequency sine polynomial and each g_n is a real finite even-frequency sine polynomial. Assume f_N is nonzero, -Delta psi=partial_x rho, and the stationary equation

\[
(cX+u)\cdot\nabla\rho-\rho=0,\qquad u=(-\psi_y,\psi_x)
\]

holds on an exterior domain. Such a pair does not exist.

The statement permits free harmonic stream coefficients at resonant orders within the stated sums. It forbids a finite termination of the pure recursion with finite angular polynomials and no additional stream exponents beyond the density truncation. It does not address infinite series, logarithmic terms, or independently appended multipoles outside these sums.

## A homogeneous angular lemma

Let p<1. Let f be a nonzero finite sine polynomial with positive odd frequencies and g a finite sine polynomial with positive even frequencies, satisfying

\[
-(g''+(p+1)^2g)=p\cos\theta f-\sin\theta f'.
\]

Then

\[
\mathcal Q_p(f,g)=(p+1)gf'-pg'f
\]

is not identically zero.

To prove this, let M be the highest frequency of f and a its nonzero sine amplitude. The right-hand side of the Poisson equation has highest possible frequency M+1, whose coefficient is (p-M)a/2. This is nonzero because M>=1 and p<1. Therefore g has a nonzero coefficient at M+1. In particular p=-M-2 is impossible, since it would make that nonzero forcing resonant. The amplitude at M+1 is

\[
b=-\frac{a}{2(M+p+2)}.
\]

Every stream frequency above M+1, if present, must be harmonic. Since p<1, there is at most one such frequency, K=-p-1.

If there is no such higher harmonic, the highest frequency of g is K=M+1. The coefficient of sin((M+K)theta) in Q_p is

\[
\frac{ab}{2}\big[(p+1)M-pK\big]
=\frac{ab}{2}(M-p)
=-\frac{a^2(M-p)}{4(M+p+2)},
\]

which is nonzero. No lower pair of frequencies can reach M+K.

If a higher harmonic is present, let its nonzero amplitude be b and let K=-p-1>M+1. The same highest-frequency coefficient is

\[
\frac{ab}{2}\big[(p+1)M-pK\big]
=-\frac{abK}{2}(M+p).
\]

Here p=-K-1 and K>M+1 give M+p=M-K-1<0, so this coefficient is again nonzero. This proves the lemma in all cases.

## Application to the finite expansion

Distinct orders have distinct radial powers because delta>0. The stream Poisson equation therefore implies the homogeneous Poisson equation for each pair (f_n,g_n).

Let N be the final nonzero density order and assume both displayed sums end at N, as in the statement. The linear dilation term has orders at most N. The nonlinear velocity-density product has orders at most 2N, because p_i+p_j-1=p_(i+j). At order 2N only the pair (i,j)=(N,N) contributes. Thus stationarity forces

\[
(p_N+1)g_N f_N'-p_N g_N'f_N=0.
\]

But p_N=1-N delta<1 and f_N is nonzero, so the homogeneous lemma contradicts this identity. The finite expansion cannot be stationary.

## Dependencies and scope

The proof uses the angular Poisson equation, sine product identities, the ordering of finite Fourier support, and independence of distinct radial powers on an exterior interval. It has no convergence assumption and no numerical premise. It rules out a finite-polynomial termination as a shortcut to the requested convergent infinite series. It gives no lower bound on the growth of a nonterminating series and is not an infinite-series divergence theorem.

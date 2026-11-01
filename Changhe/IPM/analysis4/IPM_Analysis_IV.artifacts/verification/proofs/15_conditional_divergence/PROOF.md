# Conditional divergence from dense incompatible rational parameters

## Statement and scope

Fix a nonzero finite odd sine polynomial f_1, independent of delta, with highest frequency L. For each irrational 0<delta<1, define the unique pure density and stream recursion of topic 01, and write F_n(delta)=||f_n(delta)||_0 for its sine coefficient l1 norm. Let I be a nonempty open subinterval of (0,1).

At a rational delta_*, let n_0 be the first stream resonance, let j_0=n_0 delta_*/2-1, and let kappa(delta_*) be the coefficient of sin((2j_0-1)theta) in f_{n_0}(delta_*). This coefficient is well defined by the density-stream recursion before the first stream resonance. An earlier potential resonance does not invalidate this algebraic definition.

Assume explicitly:

(H) The rational delta_* in I with kappa(delta_*) nonzero are dense in I.

Then the set

\[
G=\{\delta\in I\setminus\mathbb Q:
       \limsup_{n\to\infty}F_n(\delta)^{1/n}=\infty\}
\]

is a dense G_delta subset of I. At every delta in G, the pure density series has zero radius in z=r^(-delta), and its terms are unbounded in angular supremum norm at every fixed r>0. Thus it cannot converge uniformly in angle there.

This is a proved conditional theorem. Hypothesis (H) is OPEN. A finite collection of exact nonzero compatibility coefficients does not prove (H). By the Brjuno convergence theorem, G is disjoint from the Brjuno parameter set and therefore has measure zero. No unconditional divergence parameter for this nonlinear recursion is supplied by this theorem alone.

## The first pole and its nonzero residue

At each fixed order the pure recursion is a finite combination of rational functions of delta. Every f_n for n<=n_0 is regular at delta_*, because it uses only streams of lower order. In g_{n_0}, precisely the resonant Fourier multiplier may have a pole:

\[
g_{n_0}(\delta)=S(\delta)\sin(2j_0\theta)
                   +\widetilde g(\delta),\qquad
S(\delta)=-\frac{a_{n_0,j_0-1}(\delta)}
                    {2(2j_0+2-n_0\delta)}.
\]

Here the remainder is regular, and

\[
\operatorname*{Res}_{\delta=\delta_*}S
 =\frac{\kappa}{2n_0}.
\]

At density order n_0+1, the only ordered pair that uses this stream is (i,j)=(n_0,1). The other pair involving order n_0 uses its regular density and is harmless. Since P_{n_0}(delta_*)=-2j_0 and p_1(delta_*)=gamma_*=1-delta_*, direct substitution gives

\[
\operatorname*{Res}_{\delta=\delta_*} f_{n_0+1}
=-\frac{\kappa j_0}{n_0^2(c_*-1)}
\left[\sin(2j_0\theta) f_1'
       +\gamma_*\cos(2j_0\theta)f_1\right].
\tag{1}
\]

Write a_L for the nonzero highest sine coefficient of f_1. The coefficient of sin((L+2j_0)theta) in the bracket is

\[
\frac{L+\gamma_*}{2}a_L\ne0.
\]

This follows from the two sine-cosine product identities; no lower input frequency can reach this sum frequency. Hence (1) is a nonzero simple pole when kappa is nonzero. In particular F_{n_0+1}(delta) tends to infinity as delta tends to delta_* through irrationals.

This highest-frequency argument also verifies that nonlinear cancellation cannot remove the pole at this first density order. It makes no assertion about cancellations at later resonances.

## The Baire argument

For positive integers M,N define

\[
U_{M,N}=\{\delta\in I\setminus\mathbb Q:
          F_n(\delta)>M^n\text{ for some }n\ge N\}.
\]

Every U_{M,N} is relatively open, because each finite coefficient is continuous at every irrational delta. It is relatively dense under (H): every nonempty open J contained in I contains infinitely many incompatible rationals, with unbounded reduced denominators. Their first resonance orders are at least those denominators. Choose one with n_0>=N and use its nonzero pole to find nearby irrational parameters in U_{M,N}.

The space I minus the rationals is a dense G_delta subspace of the real line and admits a complete compatible metric. Baire's theorem implies that the countable intersection of the U_{M,N} is dense in this space. The intersection is exactly G. Since the irrational subspace itself is G_delta in I, G is a dense G_delta in I as well.

The support estimate deg f_n<=n(L+1)-1 makes the coefficient norm and angular supremum norm comparable by a factor growing only polynomially in n. For example, each sine coefficient has magnitude at most 2||f_n||_infinity, and there are at most n(L+1) of them. Thus

\[
F_n\le2n(L+1)\|f_n\|_\infty.
\]

Taking n-th roots transfers the infinite limsup to the supremum norm. Multiplication by the fixed geometric factor r^{1-n delta} cannot make the terms tend to zero; in fact their norms are unbounded. This proves the assertion.

## Dependencies and audit record

The proof uses the independently verified recurrence, its linear support bound, elementary rational-function algebra and the Baire category theorem. It confirms theory Lemma 10.1 and Theorem C with their stated open hypothesis. The source statement is retained in `sources/lead_conditional_divergence.md`. The nearby rational pole is an exact finite-order fact; it is not inferred from a floating growth fit.

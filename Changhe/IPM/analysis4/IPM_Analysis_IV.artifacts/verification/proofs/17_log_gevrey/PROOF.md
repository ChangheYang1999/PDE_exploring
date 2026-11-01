# Rational logarithmic degree and Gevrey bounds

## Exact statement

Let 0<delta=a/b<1 be rational in lowest terms, c=1/(1-delta), p_n=1-n delta and P_n=2-n delta. Put t=log r. Let f_1 be a finite odd sine polynomial with highest frequency L, B=L+1 and F=||f_1||_0. Use the formal logarithmic density and stream recursion of topic 10, prescribing the constant term of every resonant stream coefficient to be zero.

Set

\[
q_0=\frac{2b}{\gcd(a,2)},\quad h=\frac a{\gcd(a,2)},\quad
\epsilon=\begin{cases}1&h=1,\\0&h\ge2,\end{cases}
\]

\[
d_n=\max\{0,\lfloor(n-1)/q_0\rfloor-\epsilon\},\qquad
e_n=\max\{0,\lfloor n/q_0\rfloor-\epsilon\}.
\]

Write the order-n coefficients as F_n(t,theta),G_n(t,theta), and define, with s=4b,

\[
\|H\|_{!,s}=\sum_{k\ge0}k!s^k\|[t^k]H\|_0,
\qquad C=\frac{56bB}{c-1}.
\]

Then

\[
\deg_t F_n\le d_n,\qquad \deg_t G_n\le e_n,
\]

\[
\|F_n\|_{!,s}\le\frac{d_n!}{n}F(8CF)^{n-1},\qquad
\|G_n\|_{!,s}\le4b\frac{d_n!}{n}F(8CF)^{n-1}.
\tag{1}
\]

This is a proved Gevrey upper bound of order 1/q_0 in the order index. It does not prove ordinary convergence or divergence of the canonical infinite logarithmic series. Potential reconstruction exists formally by topic 10, but (1) asserts a norm bound only for density and stream.

For an analytic odd sine profile with F=||f_1||_{sigma_0}<infinity, sigma_0>0, replace C by

\[
C_{\rm an}=\frac{(32+48\sigma_0)b e^{\sigma_0}}{c-1}.
\]

Then every sigma<sigma_0 satisfies

\[
\|F_n\|_{!,s,\sigma}
\le\frac{d_n!}{n}F
 \left(\frac{8C_{\rm an}F}{\sigma_0-\sigma}\right)^{n-1}.
\tag{2}
\]

The stream bound has the additional factor 4b exp(sigma_0). No estimate at the original strip boundary is asserted.

## Operators and degree count

Let D=partial_t and lambda_n=(n-1)(c-1). Direct differentiation gives

\[
(\lambda_n-cD)F_n
=\sum_{i+j=n}\left[(P_i+D)G_i\,\partial_\theta F_j
              -\partial_\theta G_i\,(p_j+D)F_j\right].
\tag{3}
\]

For stream frequency q=2j the factored Poisson inverse is

\[
B_{n,j}=-\tfrac12(D+P_n+q)^{-1}A_{n,j-1}
        -\tfrac12(D+P_n-q)^{-1}A_{n,j}.
\tag{4}
\]

A nonzero scalar shift has the finite polynomial inverse

\[
(D+v)^{-1}H=\sum_{k\ge0}(-1)^k v^{-k-1}D^kH.
\]

At P_n=-q the first inverse becomes integration from zero. Subtract the constant of the resulting coefficient to enforce B_{n,j}(0)=0. This changes only a free harmonic stream term. Density inversion is the finite sum lambda_n^{-1} sum_k(cD/lambda_n)^k, so it preserves log degree.

The stream resonances are n=q_0 m with hm>=2. Therefore a resonant inverse increases degree by at most one; all other operations preserve or add degrees. For i+j=n,

\[
e_i+d_j\le d_n.
\]

For epsilon=0 this is the elementary floor inequality. For epsilon=1, use max(0,x-1)+max(0,y-1)<=max(0,x+y-1) for nonnegative integers x,y. At each true resonance e_n=d_n+1, and otherwise e_n=d_n. Induction proves the degree bounds. Their values are upper bounds, and can fail to be attained when a resonant projection vanishes.

## Polynomial norms and inverses

The factorial weights give

\[
\|DH\|_{!,s}\le s^{-1}\|H\|_{!,s},\qquad
\|\int_0^tH\|_{!,s}=s\|H\|_{!,s}.
\]

Every nonzero P_n+q has magnitude at least 1/b, and q-P_n>=n delta>=1/b. Thus

\[
\|(D+v)^{-1}\|\le\frac1{|v|-1/s}\le\frac{4b}{3}<2b.
\]

In (4), each input sine coefficient enters at most two output modes. The half-integral at a resonance costs 2b. The other, nonresonant output costs at most b under the looser inverse bound. For the input in the second resonant channel, subtracting its constant costs at most another copy of that channel's norm. These bounds give the uniform column-sum estimate

\[
\|G_n\|_{!,s}\le4b\|F_n\|_{!,s}.
\tag{5}
\]

No factor counting the total number of Fourier modes is present.

For polynomials U,V of degrees at most e,d,

\[
\|UV\|_{!,s}\le {e+d\choose e}\|U\|_{!,s}\|V\|_{!,s}.
\]

Indeed the contribution of degrees k,l is multiplied by binomial(k+l,k), which increases in both indices. Set u_n=||F_n||_{!,s}/d_n! and v_n=||G_n||_{!,s}/e_n!. Since e_i+d_j<=d_n, products have normalized constant at most one, and (5) implies v_n<=4b u_n.

The density inverse obeys

\[
\|(\lambda_n-cD)^{-1}\|
\le\frac1{\lambda_n}\frac1{1-c/(s\lambda_n)}
\le\frac2{(n-1)(c-1)},
\]

because c/(s lambda_n)=1/(4a(n-1))<=1/4 for n>=2.

## Scalar majorant

The angular supports remain deg F_n<=Bn-1 and deg G_n<=Bn. The four multipliers in (3) have norm bounds 4i, Bi, Bj and 3j, respectively. Combining them with (5), the normalized product estimate and the density inverse yields

\[
u_n\le\frac C{n-1}\sum_{i+j=n}ij\,u_i u_j.
\]

Put x_n=n u_n. Then x_1=F and x_n<=2C sum_{i+j=n}x_i x_j. The Catalan recursion gives x_n<=F(8CF)^{n-1}. This proves (1).

In particular the coefficient at the maximal allowed degree d_n satisfies

\[
\|[t^{d_n}]F_n\|_0\le\frac F{n s^{d_n}}(8CF)^{n-1}.
\]

This exponential bound concerns that specified degree. It does not assert the same bound for the actual highest nonzero coefficient when its degree is lower than d_n.

## Analytic angular data

Fourier shifts cost at most exp(sigma_0). The stream inverse and its angular derivative satisfy, in each smaller strip,

\[
\|G_n\|_{!,s,\sigma}\le4b e^{\sigma_0}\|F_n\|_{!,s,\sigma},
\]

\[
\|\partial_\theta G_n\|_{!,s,\sigma}
\le8bn e^{\sigma_0}\|F_n\|_{!,s,\sigma},\qquad
\|(P_n+D)G_n\|_{!,s,\sigma}
\le16bn e^{\sigma_0}\|F_n\|_{!,s,\sigma}.
\]

For the first derivative multiplier use q/|P_n+q|<=1+b|P_n|<=4bn away from resonance. The second obeys q/(q-P_n)<=1+2/(n delta)<=3bn. At a resonance q=n delta-2<n, so the half-integral costs at most 2bn. Constant subtraction is bounded as in (5). This proves the stated derivative constants.

Define u_n as the supremum of (sigma_0-sigma)^{n-1}||F_n||_{!,s,sigma}/d_n!. The Wiener strip estimate, optimized at an increment (sigma_0-sigma)/j, gives

\[
\|\partial_\theta F_j\|_{!,s,\sigma}
\le j d_j!u_j(\sigma_0-\sigma)^{-j}.
\]

For j=1 take the limit from inside the original strip. Inserting these bounds in (3) gives the same scalar inequality with C_an: the two nonlinear terms contribute 32 and 48 sigma_0 after density inversion. The Catalan argument proves (2).

## Why the bound does not establish convergence

For a fixed nonzero scalar v,

\[
[(D+v)^{-1}t^K]_{t^0}=(-1)^K K!/v^{K+1}.
\]

Uniformly separated nonzero divisors alone therefore do not bound the ordinary polynomial coefficient norm exponentially. The constrained nonlinear inputs may have further cancellations, so this observation also does not prove IPM divergence.

A separate linear example shows why a general Fuchsian label is insufficient. For a positive integer q and eta>0,

\[
(z\partial_z-qw\partial_w+\eta-1)U
=\frac z{1-z^q w\log z}
\]

has a convergent right-hand log expansion in a fixed sector near zero. A formal solution sum_k z^{qk+1}w^k u_k(log z) requires u_k'+eta u_k=t^k. Its unique polynomial solution is

\[
u_k(t)=(-1)^k k!\eta^{-k-1}
       \sum_{j=0}^k\frac{(-\eta t)^j}{j!}.
\]

At every fixed real t the sum tends to exp(-eta t), which is nonzero. Thus this formal solution diverges at every fixed positive z and nonzero w. This example is not an IPM solution.

## Dependencies and provenance

This audit independently checks the proof contributed by the theory part's rational-log review. The source is retained in `sources/rational_log_source.md`. Algebra and original-potential formal existence are proved independently in topic 10, with exact Cartesian verification through the first resonances. The present argument adds sharper universal degree bounds and the coefficient-norm estimate. No claim of convergence of a rational-parameter logarithmic IPM expansion is made.

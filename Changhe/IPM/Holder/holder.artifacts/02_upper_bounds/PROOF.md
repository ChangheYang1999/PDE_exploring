# An explicit bound from angular reflection

Status: independently proved; numerical values still require separate evaluation. The theorem uses the kernel and homogeneous-space convention in `../01_setup/PROOF.md`.

## Theorem

Let $0<\alpha<1$ and define, for $n=1,2,3$,

$$a_n(\alpha)=\frac n\pi\int_0^{\pi/(2n)}\sin(nt)(2\sin t)^\alpha\,dt.$$

In particular,

$$a_2(\alpha)=\frac{2^{1+\alpha/2}}{\pi(\alpha+2)}.$$

Set

$$b_\alpha=\min\left\{\frac{a_3(\alpha)+a_1(\alpha)}2,\frac{2^{\alpha+1}}{3\pi}\right\},\qquad
B_\alpha=\frac{2a_3(\alpha)}{1-\alpha}+b_\alpha,\qquad
s_\alpha=\frac{(1-\alpha)B_\alpha}{2a_2(\alpha)},$$

and

$$F(\alpha)=\frac{2a_2(\alpha)s_\alpha^\alpha}{\alpha(1-\alpha)}.$$

For every real $f\in\dot C^\alpha(\mathbb R^2)$, with operators defined modulo constants as in the setup proof,

$$[T_{xx}f]_\alpha\le F(\alpha)[f]_\alpha,\qquad
[T_{xy}f]_\alpha\le F(\alpha)[f]_\alpha,$$

$$[R_1^2f]_\alpha\le\bigl(F(\alpha)+\tfrac12\bigr)[f]_\alpha.$$

The integrals defining $a_n$ are finite positive elementary definite integrals and specify every constant. This is an upper bound, not a claim that $F(\alpha)$ is the exact finite-alpha operator norm. The same upper bounds hold for complex inputs with the modulus seminorm. For this extension, apply the real theorem to $\operatorname{Re}(e^{i\phi}f)$ and choose the phase to realize the modulus of each fixed output increment. This avoids any need for a complex-valued McShane extension.

## Exact angular lemma

For $r>0$ and any phase $\gamma$, define

$$\mathcal A_{n,r,\gamma}(f)=\frac1{2\pi}\int_0^{2\pi}
\cos(n\theta-\gamma)f(r\cos\theta,r\sin\theta)\,d\theta.$$

Then

$$|\mathcal A_{n,r,\gamma}(f)|\le a_n(\alpha)r^\alpha[f]_\alpha.$$

The constant is exact for this angular functional on real global alpha-Hölder functions.

A rotation removes $\gamma$. Split each positive lobe of $\cos(n\theta)$ into two halves, and reflect each half across its adjacent zero ray into the neighboring negative half-lobe. There are $2n$ such positive half-lobes. If $t\in[0,\pi/(2n)]$ is the angular distance to that zero ray, both densities have magnitude $\sin(nt)$, and the paired points are separated by the chord $2r\sin t$. The integral over a positive half-lobe and its reflected partner is bounded by

$$\frac{[f]_\alpha r^\alpha}{2\pi}
\int_0^{\pi/(2n)}\sin(nt)(2\sin t)^\alpha\,dt.$$

Adding the $2n$ disjoint pairs proves the bound.

For exactness, let $Z_n$ be the union of zero lines of $\cos(n\theta)$ and define

$$u_n(z)=\operatorname{sign}(\cos(n\arg z))\operatorname{dist}(z,Z_n),\qquad u_n(0)=0.$$

The function $u_n$ is 1-Lipschitz. Points with the same sign use the 1-Lipschitz property of distance to a closed set. If the signs differ, the joining segment crosses $Z_n$, so the sum of the two distances to $Z_n$ is no greater than the segment length.

The scalar function $p_\alpha(s)=2^{\alpha-1}\operatorname{sign}(s)|s|^\alpha$ has alpha-Hölder seminorm at most 1. For inputs of the same sign this follows from $|a^\alpha-b^\alpha|\le|a-b|^\alpha$ and $2^{\alpha-1}\le1$. For opposite signs, concavity gives $2^{\alpha-1}(a^\alpha+b^\alpha)\le(a+b)^\alpha$. Thus $f=p_\alpha\circ u_n$ has $[f]_\alpha\le1$. On every reflected pair its value difference is exactly $(2r\sin t)^\alpha$, so the angular bound is attained. The same pair also shows that $[f]_\alpha=1$.

For $n=2$, substitute $v=\sin t$ to obtain

$$\int_0^{\pi/4}\sin(2t)(2\sin t)^\alpha\,dt
=\frac{2^{\alpha/2}}{\alpha+2},$$

which gives the displayed formula for $a_2$.

## Near and far decomposition

First take $f\in C_c^\infty$ and let $R>0$. Define

$$N_Rf(x)=\int_{|z|<R}K_{xx}(z)(f(x-z)-f(x))\,dz,$$

$$H_Rf(x)=\int_{|z|\ge R}K_{xx}(z)f(x-z)\,dz.$$

The first integral converges absolutely. The second is finite for compactly supported $f$ at each fixed $x$. Angular cancellation gives $T_{xx}f=N_Rf+H_Rf$. The angular lemma yields

$$|N_Rf(x)|\le\frac{a_2(\alpha)}\alpha R^\alpha[f]_\alpha.$$

To bound the far increment, let $e=(\cos\beta,\sin\beta)$ be a unit vector. Direct differentiation gives

$$\partial_eK_{xx}(r,\theta)=-\frac{\cos(3\theta-\beta)}{\pi r^3}.$$

The distributional derivative of the truncated kernel is

$$\partial_e(\mathbf1_{|z|\ge R}K_{xx})
=\mathbf1_{|z|>R}\partial_eK_{xx}
+\delta(|z|-R)(e\cdot z/|z|)K_{xx}.$$

The positive sign of the inner-sphere term follows by differentiating $\mathbf1_{r\ge R}$. It can also be checked by integration by parts on the exterior domain. The bulk term, after convolution with $f$, has absolute value at most

$$2a_3(\alpha)[f]_\alpha\int_R^\infty r^{\alpha-2}\,dr
=\frac{2a_3(\alpha)}{1-\alpha}R^{\alpha-1}[f]_\alpha.$$

For the sphere term, the identity

$$\cos2\theta\cos(\theta-\beta)
=\tfrac12\cos(3\theta-\beta)+\tfrac12\cos(\theta+\beta)$$

and the angular lemma imply the bound

$$\frac{a_3(\alpha)+a_1(\alpha)}2R^{\alpha-1}[f]_\alpha.$$

There is a second bound for the sphere term. Its density is odd under $\theta\mapsto\theta+\pi$, so antipodal pairing gives the angular norm bound

$$2^{\alpha-1}\frac1{2\pi}\int_0^{2\pi}
|\cos2\theta\cos(\theta-\beta)|\,d\theta.$$

The integral has maximum $8/3$. Here is a direct verification. Denote it by $I(\beta)$. Symmetry reduces to $0\le\beta\le\pi/4$. Differentiating the periodic function $|\cos t|$ twice in distributions gives $(d^2/dt^2+1)|\cos t|=2\sum_{k\in\mathbb Z}\delta_{\pi/2+k\pi}$. Therefore $I''+I=4\cos2\beta$ on this interval. Direct integration gives $I(0)=4(2\sqrt2-1)/3$, and symmetry gives $I'(0)=0$. Solving this scalar equation yields

$$I(\beta)=\frac{8\sqrt2\cos\beta-4\cos2\beta}{3}.$$

Its derivative is $(8/3)\sin\beta(2\cos\beta-\sqrt2)$, which is nonnegative on the interval. Hence $I(\beta)\le I(\pi/4)=8/3$. The sphere term is consequently bounded by $2^{\alpha+1}/(3\pi)$ as well as by the earlier harmonic bound. Taking their minimum gives $b_\alpha$.

All angular densities in this calculation have zero mean. Thus constants in $f$ contribute nothing. The bound is uniform in $x$ and in the direction $e$, and proves

$$|\partial_eH_Rf(x)|\le B_\alpha R^{\alpha-1}[f]_\alpha.$$

No derivative of $f$ is bounded by its Hölder seminorm in this argument. The derivative falls on the truncated kernel, including its sphere contribution.

For $h=|x-y|>0$, integrate this derivative along the segment from $x$ to $y$ and use the two near-field estimates:

$$|T_{xx}f(x)-T_{xx}f(y)|
\le[f]_\alpha\left(\frac{2a_2(\alpha)}\alpha R^\alpha
+B_\alpha hR^{\alpha-1}\right).$$

Choose $R=sh$. Dividing by $h^\alpha$ gives

$$[T_{xx}f]_\alpha\le[f]_\alpha\inf_{s>0}
\left(\frac{2a_2(\alpha)}\alpha s^\alpha+B_\alpha s^{\alpha-1}\right).$$

The expression tends to infinity at both endpoints $s\downarrow0$ and $s\to\infty$. Its derivative has the sign of $2a_2(\alpha)s-(1-\alpha)B_\alpha$, so its unique minimizer is $s=s_\alpha$. Substitution gives $F(\alpha)$.

The rotation identity in the setup proof gives the same bound for $T_{xy}$. Adding the local term gives the $R_1^2$ bound.

## Passing to the full homogeneous space

There is no need to assert seminorm density of smooth compactly supported functions. The following weaker approximation suffices and also shows equality of the sharp norm on test functions and on the full quotient space.

Normalize $f(0)=0$ and put $H=[f]_\alpha$. For $M>0$, prescribe $f$ on the closed ball $\overline B_M$ and prescribe zero on $\mathbb R^2\setminus B_{2M}$. These data are $H$-Lipschitz in the metric $d_\alpha(x,y)=|x-y|^\alpha$. For a cross pair, $|f(x)|\le HM^\alpha\le H|x-y|^\alpha$. The other pairs use the original seminorm or the zero data.

The McShane formula

$$f_M(z)=\inf_{a\in\overline B_M\,\cup\,(\mathbb R^2\setminus B_{2M})}
\{g_M(a)+H|z-a|^\alpha\}$$

extends these data with $[f_M]_\alpha\le H$. To verify this directly, the triangle inequality for $d_\alpha$ implies $f_M(z)-f_M(w)\le H|z-w|^\alpha$; interchange $z,w$ for the reverse bound. Compatibility implies equality with every prescribed value. Thus $f_M$ is compactly supported, equals $f$ on $B_M$, and satisfies $f_M(0)=0$ and $|f_M(z)|\le H|z|^\alpha$.

Convolve with a nonnegative smooth compactly supported approximate identity. This keeps the seminorm at most $H$, produces smooth compactly supported functions, and converges locally uniformly to $f$ as first the smoothing radius tends to zero and then $M\to\infty$. The normalized functions have the uniform growth bound $H|z|^\alpha$ after subtracting their value at zero.

The increment integral in the setup proof converges along this approximation. Near either singularity, uniform Hölder control gives the integrable majorant proportional to $r^{\alpha-2}$. Away from the singularities use local uniform convergence. At infinity use the uniform growth bound and the kernel-difference majorant proportional to $r^{\alpha-3}$, whose area integral converges for $\alpha<1$. Therefore each fixed output increment is a limit of test-function output increments, and the proved bound passes to $f$. Taking suprema also proves equality of the two sharp operator norms.

## Small-alpha consequence

For each fixed $n$, dominated convergence gives $a_n(\alpha)\to1/\pi$ as $\alpha\downarrow0$. More precisely $a_n(\alpha)=1/\pi+O(\alpha)$: differentiating under the integral is justified by the integrability near zero of $t|\log t|$. Thus $B_\alpha=8/(3\pi)+O(\alpha)$, $s_\alpha=4/3+O(\alpha)$, and

$$F(\alpha)=\frac2{\pi\alpha}+O(1).$$

The lower construction in `../03_lower_bounds/PROOF.md` supplies the matching coefficient. The $O(1)$ statement here describes the expansion of the fully explicit function $F$; it is not used in place of the finite-alpha theorem.

## Remaining losses

The two near values, the bulk and sphere terms, and the two harmonics in the sphere term were bounded separately. These are possible sources of finite-alpha improvement. The exact angular lemma itself has no loss on the unrestricted real Hölder class.

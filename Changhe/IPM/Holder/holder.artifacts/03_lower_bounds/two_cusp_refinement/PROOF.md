# Retaining the full cusp integral and its angular moments

Status: independently proved refinement of the compact two-cusp lower bound. All operators use the normalization and homogeneous Hölder seminorm in `../../01_setup/PROOF.md`.

## Theorem

For $0<\alpha<1$, put $q=\sqrt2-1$ and

$$P=\frac1{15}+\frac14\log\frac{15}{16}>0.$$

Define

$$S_\alpha=\frac2\pi\int_0^{\pi/4}\sin2t
\left[\frac{b(t)^\alpha}{\alpha}
+\int_0^{b(t)}\frac{w^\alpha}{1-w}\,dw\right]dt,
\qquad b(t)=\frac{\sin t}{1+\sin t}.$$

Then, for the real homogeneous seminorm operator constants and also for their smooth compact test-function suprema,

$$C_\alpha\ge L_2(\alpha),\qquad D_\alpha\ge L_2(\alpha),\qquad
L_2(\alpha)=2S_\alpha-\frac{2q^\alpha}{\pi}P.$$

An equivalent positive series specifies $S_\alpha$ without a nested integral:

$$S_\alpha=\frac4\pi\sum_{n=0}^\infty
\frac{q^{\alpha+n+2}}{\alpha+n+2}
\sum_{k=0}^n\frac{(n-k+1)(n-k+2)}{2(\alpha+k)}.$$

Its small-alpha expansion is

$$L_2(\alpha)=\frac2{\pi\alpha}
-\frac{1+\log2+2P}{\pi}+O(\alpha).$$

This improves the earlier cusp bound, especially at small alpha, while the degree-three homogeneous family is stronger near alpha = 1.

## Input and self contribution

Let $e=(1,0)$, $\rho=1/2$, and

$$s(z)=(|z_1|-|z_2|)/\sqrt2,\quad
\nu(z)=\operatorname{sign}(s(z))\min\{|s(z)|,(\rho-|z|)_+\},$$

$$g(z)=2^{\alpha-1}\operatorname{sign}(\nu(z))|\nu(z)|^\alpha,
\qquad f(z)=g(z)-g(z-e).$$

The two support disks have disjoint interiors. Their signed-distance pieces together form a globally 1-Lipschitz function before applying the scalar signed power. For equal signs this follows from the distance-to-zero-set inequality; for opposite signs the segment crosses that zero set. The scalar inequality $2^{\alpha-1}(a^\alpha+b^\alpha)\le(a+b)^\alpha$ proves $[f]_\alpha\le1$, and reflection across a zero line proves equality. Also $f(0)=f(e)=0$.

Set $S=\int K_{xx}(z)g(z)dz$ and $E=\int K_{xx}(e-z)g(z)dz$. The increments at the two centers are $2(S-E)$ in absolute value. The local term in $R_1^2$ contributes zero to this input increment.

Use the eight equal angular sectors and let $t$ be distance to the nearest diagonal ray. On one sector the angular density is $\sin2t$, and the unsigned distance is $\min(r\sin t,\rho-r)$. The two branches meet at $r=\rho/(1+\sin t)$. Therefore

$$S=\frac{2^{\alpha+1}}\pi\int_0^{\pi/4}\sin2t
\int_0^\rho \min(r\sin t,\rho-r)^\alpha\,\frac{dr}{r}\,dt.$$

Evaluate the first radial branch and substitute $w=1-r/\rho$ in the second. Since $2^\alpha\rho^\alpha=1$, the result is exactly $S=S_\alpha$ in the statement.

For the series, substitute $v=\sin t$, then $b=v/(1+v)$, so $\sin2t\,dt=2b(1-b)^{-3}db$ and $0\le b\le q$. Expand $(1-b)^{-3}$ and $(1-w)^{-1}$. All terms are positive, so monotone convergence justifies the interchange and gives the displayed series.

## Cross contribution and cancellation of moments

On the support disk, the complex kernel has the uniformly convergent expansion

$$K_{xx}(e-z)=\frac1{2\pi}\operatorname{Re}\sum_{m=0}^\infty(m+1)z^m.$$

The function $g$ is even under each coordinate reflection and changes sign under exchanging the coordinates. Thus only the angular modes $m=4k+2$, $k\ge0$, survive integration. On every circle,

$$\left|\int_0^{2\pi}g(r,\theta)\cos(m\theta)\,d\theta\right|
\le4\|g\|_\infty\le2q^\alpha.$$

The last inequality uses $|\nu|\le q/2$. Integrating in radius and summing the absolute values yields

$$|E|\le\frac{q^\alpha}\pi
\sum_{k=0}^\infty\frac{4k+3}{4k+4}\rho^{4k+4}
=\frac{q^\alpha}\pi P.$$

Indeed, with $t=\rho^4=1/16$, the series is $t/(1-t)+(1/4)\log(1-t)$. Its positivity also follows from the positive series. Consequently the center increment is at least $2S_\alpha-2q^\alpha P/\pi$, as asserted. Positive mollification preserves the input seminorm and converges in these output increments, proving the same lower bound for smooth compact inputs.

## Expansion and a certificate tail

In the integral for $S_\alpha$, the constant term after subtracting $1/\alpha$ is

$$\log b-\log(1-b)=\log\sin t.$$

The needed logarithmic integrals are finite, including second logarithmic moments, so termwise expansion has an $O(\alpha)$ remainder. Since

$$\int_0^{\pi/4}\sin2t\,dt=\frac12,
\qquad
\int_0^{\pi/4}\sin2t\log\sin t\,dt=-\frac{1+\log2}{4},$$

the stated expansion follows.

For certification, let the outer series stop before $n=N$. Its omitted sum is nonnegative and at most

$$\frac4{\pi\alpha}\,
\frac{\binom{N+3}{3}\,q^{\alpha+N+2}}{\alpha+N+2}
\left(1-q\frac{N+4}{N+1}\right)^{-1},$$

provided $q(N+4)/(N+1)<1$. To verify this, bound every $(\alpha+k)^{-1}$ by $\alpha^{-1}$, sum the triangular coefficients to $\binom{n+3}{3}$, and bound the ratio of successive resulting terms by $q(N+4)/(N+1)$. This gives a rigorous geometric tail. The certificate code uses this bound with exact rational input alpha and Arb arithmetic.

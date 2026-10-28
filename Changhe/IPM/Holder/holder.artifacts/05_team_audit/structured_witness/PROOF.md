# Audit of the numerical team's polygonal signed-distance witness

Status: the input and the explicit tail enclosure below are proved. No numerical value of the full integral is certified by this note. The source being audited is `numerics_code/structured_lb.py` and the note headed 01:25, read at the actual time recorded in the verifier log.

## Statement and admissibility

Fix $a>0$, $m=(1/2,0)$, and the closed set $Z_a$ consisting of the horizontal axis, the vertical segments from $(0,0)$ to $(0,a)$ and from $(1,0)$ to $(1,a)$, the rays from these upper endpoints in directions $2\pi/3$ and $\pi/3$, respectively, and the point reflections of these four pieces through $m$.

In the upper half-plane, assign sign $-1$ between the two polygonal curves and $+1$ outside. Extend the sign by oddness through $m$. For $0<\alpha<1$, set

$$f_a(z)=2^{\alpha-1}\sigma(z)\operatorname{dist}(z,Z_a)^\alpha.$$

The sign is constant on each connected component of the complement. The signed distance $v_a=\sigma\operatorname{dist}(\cdot,Z_a)$ is 1-Lipschitz: on equal-sign pairs this is the usual distance-function estimate; on opposite-sign pairs the connecting segment crosses $Z_a$, so the sum of the two distances is at most the length of the segment. The signed-power inequality then gives $[f_a]_\alpha\le1$.

Both center values vanish. Thus the absolutely convergent increment

$$I(\alpha,a)=\int_{\mathbb R^2}[K_{xy}(z-e_1)-K_{xy}(z)]f_a(z)\,dz$$

gives $C_\alpha\ge|I(\alpha,a)|$ and $D_\alpha\ge|I(\alpha,a)|$. For the second assertion, rotate the input and the increment so that the $T_{xy}$ output becomes a $T_{xx}$ output; the two input values remain zero, so the local term contributes zero. Compact approximation gives the same statement for the smooth compact test-function suprema.

## Comparison with the homogeneous far profile

Let $Z_\infty$ be the three lines through $m$ at angles $0,\pi/3,2\pi/3$. Let $v_\infty$ be their signed distance with the sign of $\sin3\theta$ about $m$, and put $f_\infty=2^{\alpha-1}\operatorname{sign}(v_\infty)|v_\infty|^\alpha$. Set

$$M=\sqrt{a^2+1/4}.$$

The Hausdorff distance between $Z_a$ and $Z_\infty$ is at most $M$: corresponding rays differ by a translation of length $M$, every finite segment lies within distance $M$ of $m$, and the horizontal axes coincide. Hence the unsigned distance functions differ by at most $M$.

For opposite signs, consider the upper half-plane and write $z=(x,y)$. The right boundaries of the middle components are

$$x_a(y)=1+\frac{(y-a)_+}{\sqrt3},\qquad
x_\infty(y)=\frac12+\frac y{\sqrt3}.$$

Their horizontal separation is at most $H=\max(1/2,|1/2-a/\sqrt3|)\le M$. Opposite signs force the point to lie between corresponding boundaries. Its distances to the two zero sets then sum to at most that horizontal separation. The left boundaries and lower half-plane follow by symmetry. Thus the signed functions satisfy

$$|v_a-v_\infty|\le M,
\qquad |f_a-f_\infty|\le M^\alpha.$$

Also $|f_\infty(z)|\le|z-m|^\alpha/2$, because the nearest line is at angular distance at most $\pi/6$.

## Explicit tail enclosure

Let $R>1/2$, $q_R=1/(4R^2)$, and

$$E_R=\frac14\frac{2-q_R}{(1-q_R)^2}.$$

Write $a_3(\alpha)=\frac3\pi\int_0^{\pi/6}\sin(3t)(2\sin t)^\alpha dt$. Then

$$\left|\int_{|z-m|>R}[K_{xy}(z-e_1)-K_{xy}(z)]f_a(z)dz
-\frac{2a_3(\alpha)}{1-\alpha}R^{\alpha-1}\right|
\le\frac{4M^\alpha}{\pi R}
+E_R\left[\frac{R^{\alpha-3}}{3-\alpha}
+\frac{2M^\alpha}{3R^3}\right].$$

To prove it, write $w=z-m$ and use the complex kernel $K_{xx}+iK_{xy}=1/(2\pi\overline w^2)$. Its exact increment is

$$\frac1{2\pi}\left[\frac1{(\overline w-1/2)^2}-\frac1{(\overline w+1/2)^2}\right]
=\frac1{\pi\overline w^3}\left(1-\frac1{4\overline w^2}\right)^{-2}.$$

The imaginary part of the leading term is $\sin3\theta/(\pi r^3)$. Its integral against $f_\infty$ is exactly $2a_3R^{\alpha-1}/(1-\alpha)$ by the angular lemma. Replacing $f_\infty$ by $f_a$ in that leading term costs at most $4M^\alpha/(\pi R)$.

For the remainder, the convergent geometric derivative series gives

$$\left|\left(1-\frac1{4\overline w^2}\right)^{-2}-1\right|
\le\frac{2q-q^2}{(1-q)^2}\le\frac{E_R}{r^2},
\qquad q=\frac1{4r^2},\quad r\ge R.$$

Use $|f_a|\le r^\alpha/2+M^\alpha$ and integrate the absolute complex-kernel bound in polar coordinates. This produces exactly the remaining two terms.

This tail is a rigorous replacement for the prototype's leading-term-only tail estimate. In particular, the prototype tail is not an exact integral, but the missing error can be bounded explicitly and made small by increasing $R$.

## Local singular disks

For $0<\delta\le\min(a/2,1/2)$, the zero set in either center disk has the same nearest-distance geometry as the two perpendicular lines through that center. Rays beyond the bends are at distance at least $a-\delta\ge\delta$, and the opposite vertical segment is at distance at least $1-\delta\ge\delta$. Hence the own-kernel contribution in each disk is exactly

$$\frac{a_2(\alpha)}\alpha\delta^\alpha,
\qquad a_2(\alpha)=\frac{2^{1+\alpha/2}}{\pi(\alpha+2)}.$$

The other kernel is smooth there. A sufficient absolute error bound for that cross contribution in each disk is

$$\frac{2^{\alpha/2-1}\delta^{\alpha+2}}{(\alpha+2)(1-\delta)^2}.$$

Indeed, its magnitude is at most $[2\pi(1-\delta)^2]^{-1}$, while $|f_a|\le2^{\alpha/2-1}r^\alpha$ locally. The two omitted cross contributions in the prototype therefore have an explicitly bounded total error. For its tiny inner radius this error is negligible, but it must still be included in a rigorous certificate.

# A compact two-cusp lower bound

Status: independently proved. This construction gives a matching small-alpha coefficient and an explicit finite-alpha lower bound for both scalar operators.

## Theorem

Let $0<\alpha<1$, let $C_\alpha=\|T_{xx}\|=\|T_{xy}\|$ and $D_\alpha=\|R_1^2\|$ in the homogeneous Hölder seminorm convention of `../01_setup/PROOF.md`, and put $q=\sqrt2-1$. Then

$$C_\alpha\ge L(\alpha),\qquad D_\alpha\ge L(\alpha),$$

where

$$L(\alpha)=q^\alpha\left(\frac4{\pi\alpha(\alpha+2)}-\frac14\right).$$

Together with `../02_upper_bounds/PROOF.md`, this proves

$$\lim_{\alpha\downarrow0}\alpha C_\alpha
=\lim_{\alpha\downarrow0}\alpha D_\alpha=\frac2\pi,$$

and in fact $C_\alpha=2/(\pi\alpha)+O(1)$ and $D_\alpha=2/(\pi\alpha)+O(1)$. The lower bound applies already to the supremum over real $C_c^\infty$ inputs.

## The signed distance construction

Write $e=(1,0)$, $\rho=1/2$, and

$$s(z)=\frac{|z_1|-|z_2|}{\sqrt2},\qquad
\nu(z)=\operatorname{sign}(s(z))\min\{|s(z)|,(\rho-|z|)_+\}.$$

Thus $\nu$ vanishes outside the radius-$\rho$ ball, on its boundary, and on the two diagonal lines. Inside the ball, $|\nu|$ is the distance to the union of those lines and the exterior of the ball. Define

$$u(z)=\nu(z)-\nu(z-e),\qquad
f(z)=2^{\alpha-1}\operatorname{sign}(u(z))|u(z)|^\alpha.$$

The interiors of the two balls are disjoint. Their boundaries meet only at $e/2$, where both terms vanish. The function $u$ is 1-Lipschitz. To see this without estimating the two summands separately, let $Z$ be its zero set. On every connected component of $\mathbb R^2\setminus Z$, its sign is constant and $|u(z)|=\operatorname{dist}(z,Z)$. For equal signs, use the 1-Lipschitz property of distance to a closed set. For opposite signs, the segment between the points meets $Z$, and the sum of the two distances is no larger than the segment length. This also covers a zero endpoint.

The scalar signed-power inequality proved in the angular lemma gives $[f]_\alpha\le1$. It is exactly 1: choose two points reflected across a diagonal line, sufficiently close to that line and away from both the center and circle boundary. Their distances to $Z$ are equal, their signs are opposite, and the signed-power inequality is an equality. The function is real, compactly supported, and alpha-Hölder. Both center values vanish: $f(0)=f(e)=0$.

Let

$$g(z)=2^{\alpha-1}\operatorname{sign}(\nu(z))|\nu(z)|^\alpha.$$

Because the ball interiors are disjoint, $f(z)=g(z)-g(z-e)$. The function $g$ is even under $z\mapsto-z$ and changes sign under interchange of its coordinates. In particular $\int g(z)\,dz=0$.

## Self and cross contributions

The principal values at the two centers converge absolutely after the center value is subtracted. Define

$$S=\int K_{xx}(z)g(z)\,dz,\qquad
E=\int K_{xx}(e-z)g(z)\,dz.$$

Evenness of $K_{xx}$ and $g$ gives

$$T_{xx}f(0)=S-E,\qquad T_{xx}f(e)=E-S.$$

The signs of $K_{xx}(z)$ and $g(z)$ agree. Thus every self-integrand contribution is nonnegative.

For $r\le r_0=\rho/(1+1/\sqrt2)=1/(2+\sqrt2)$, the inequality $|s(z)|\le r/\sqrt2\le\rho-r$ implies $\nu(z)=s(z)$. On this whole inner ball, $g$ is the exact angular extremizer from the upper-bound proof. Therefore

$$S\ge\frac{a_2(\alpha)}\alpha r_0^\alpha.$$

The global maximum of $|\nu|$ is at most $\rho/(1+\sqrt2)=q/2$. Indeed,

$$|\nu(z)|\le\min\{r/\sqrt2,\rho-r\},$$

and the two linear bounds intersect at $r=r_0$. Consequently

$$\|g\|_\infty\le2^{\alpha-1}(q/2)^\alpha=\frac12q^\alpha.$$

On the translated disk $e-B_\rho$, the first coordinate is at least $1/2$, while the absolute second coordinate is at most $1/2$. Hence $K_{xx}$ is nonnegative there. Also $|e-z|\ge1/2$, so

$$0\le K_{xx}(e-z)\le\frac2\pi\qquad(z\in B_\rho).$$

Using $\int g=0$, subtract the midpoint $1/\pi$ of this interval:

$$|E|=\left|\int_{B_\rho}\left(K_{xx}(e-z)-\frac1\pi\right)g(z)\,dz\right|
\le\frac1\pi\,\pi\rho^2\,\|g\|_\infty
\le\frac18q^\alpha.$$

The evaluation points have distance 1, so

$$[T_{xx}f]_\alpha\ge|T_{xx}f(0)-T_{xx}f(e)|
\ge2S-2|E|
\ge\frac{2a_2(\alpha)}\alpha r_0^\alpha-\frac14q^\alpha.$$

Finally $2^{\alpha/2}r_0^\alpha=q^\alpha$, which gives the stated $L(\alpha)$.

Since $f(0)=f(e)=0$, the local term $-f/2$ makes no change to this particular output increment. The identical lower bound therefore holds for $D_\alpha$, without subtracting another $1/2$.

## Smooth test functions and asymptotics

Convolve $f$ with nonnegative compactly supported smooth approximate identities. These functions are in $C_c^\infty$ and have seminorm at most 1. Their $T_{xx}$ increments at 0 and $e$ converge to the displayed increment by the local Hölder majorant and compact support. Their center-value difference tends to $f(0)-f(e)=0$, so the same conclusion holds for $R_1^2$. This proves the lower bounds for the test-function suprema as well as for the homogeneous extensions.

The explicit formula has expansion

$$L(\alpha)=\frac2{\pi\alpha}
+\frac{2\log q-1}{\pi}-\frac14+O(\alpha).$$

The explicit upper bound has the same leading term and a bounded remainder. The two inequalities prove both limits and both $O(1)$ claims. No assertion is made that the finite-alpha lower bound is optimal.

## Dependencies and scope

The proof uses the exact angular lemma, the verified principal-value convention, elementary signed-distance estimates, and smoothing by a positive approximate identity. It is a real-valued construction. No numerical quadrature or unverified bibliographical statement enters the theorem.

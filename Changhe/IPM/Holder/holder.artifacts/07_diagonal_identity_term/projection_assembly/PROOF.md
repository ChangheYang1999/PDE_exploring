# Assembly of the projection-cusp witness

## Conditional statement

Use the real homogeneous Hölder space and the operators of `../../01_setup/PROOF.md`. Write

$$g_\alpha(u)=\frac12\left(|u|^\alpha+\operatorname{sgn}(u_1u_2)\left(\frac{2|u_1u_2|}{|u|}\right)^\alpha\right),\qquad g_\alpha(0)=0.$$

Assume that, for all sufficiently small positive $\alpha$,

$$[g_\alpha]_\alpha\le1+\varepsilon_\alpha,\qquad \varepsilon_\alpha=o(\alpha).\tag{A}$$

This is the local-profile hypothesis. It is proved with epsilon_alpha=2 alpha^2 for 0<alpha<=1/4 in `../local_projection_profile/PROOF.md` (V043). The argument below is stated conditionally to isolate the assembly mechanism.

Let $x=(1/2,0)$ and, on the right half-plane, let $\Gamma$ be the graph $X=b(Y)$, where

$$b(Y)^2=\frac{1/4-Y^2+2\sqrt{Y^4+Y^2/4+1/16}}3.$$

Let $s(z)$ be signed distance to $\Gamma$, positive to its right, and put $V(z)=(s(z),Y)$. Let $\rho=\alpha$ and define

$$F_\alpha(z)=-\frac12+\frac12\min(|V(z)|,\rho)^\alpha
+\frac12\operatorname{sgn}(s(z)Y)\left(\frac{2|s(z)Y|}{|V(z)|}\right)^\alpha.$$

At $V=0$ the last term is zero. Set $h(z)=(2X)^\alpha/2$ for $X>0$, clamp $F_\alpha$ to $[-h,h]$, and extend the resulting function oddly under $z\mapsto-z$, with value zero on $X=0$. Denote the result by $f_\alpha$.

Then, under (A),

$$[f_\alpha]_\alpha\le1+\varepsilon_\alpha+O(\alpha\rho^3)=1+o(\alpha).$$

The constant in the geometric error is independent of sufficiently small $\alpha$. This is a conditional regularity theorem for an explicit witness. By itself it does not assert the value of the sharp operator constant or its second asymptotic term.

## The frozen planar profile

For $u\in\mathbb R^2$ write $S(u)=2u_1u_2/|u|$, with $S(0)=0$. Its gradient away from the origin is

$$\nabla S(u)=\left(\frac{2u_2^3}{|u|^3},\frac{2u_1^3}{|u|^3}\right),\qquad |\nabla S|\le2.$$

Continuity at the origin and integration along line segments show that $S$ is 2-Lipschitz. The scalar signed power satisfies

$$\left|\operatorname{sgn}(a)|a|^\alpha-\operatorname{sgn}(b)|b|^\alpha\right|
\le2^{1-\alpha}|a-b|^\alpha.$$

Therefore the function

$$H_{\alpha,\rho}(u)=\frac12\rho^\alpha+\frac12\operatorname{sgn}(S(u))|S(u)|^\alpha$$

has Hölder seminorm at most one. Crucially, the planar frozen profile is exactly

$$G_{\alpha,\rho}(u)=\min\{g_\alpha(u),H_{\alpha,\rho}(u)\}.$$

The minimum of two functions with Hölder seminorm at most $L$ has seminorm at most $L$. Thus (A) implies

$$[G_{\alpha,\rho}]_\alpha\le1+\varepsilon_\alpha.$$

This directly controls planar pairs on opposite sides of the freezing radius. There is no triangle-inequality loss at the interface.

## The outer profile in the curved geometry

Let $Z=\Gamma\cup\{Y=0\}$ and let

$$\Pi(z)=\frac{2|s(z)Y|}{\sqrt{s(z)^2+Y^2}},\qquad \sigma(z)=\operatorname{sgn}(s(z)Y).$$

The map $V$ is globally $\sqrt2$-Lipschitz since each coordinate is 1-Lipschitz. Hence the signed function $S(V(z))=\sigma(z)\Pi(z)$ is $2\sqrt2$-Lipschitz. Also

$$\Pi(z)\le2\min\{|s(z)|,|Y|\}=2\operatorname{dist}(z,Z).$$

The outer profile

$$H(z)=-\frac12+\frac12\rho^\alpha+\frac12\sigma(z)\Pi(z)^\alpha$$

has $[H]_\alpha\le1$ for $0<\alpha\le2/3$. For equal signs the bound is $\tfrac12(2\sqrt2)^\alpha\le1$. For opposite signs the joining segment crosses $Z$, so, with $d_p=\operatorname{dist}(p,Z)$,

$$|H(p)-H(q)|\le2^{\alpha-1}(d_p^\alpha+d_q^\alpha)
\le(d_p+d_q)^\alpha\le|p-q|^\alpha.$$

The same reasoning includes points of $Z$ by continuity.

## Local distortion

The graph satisfies $b(Y)=1/2+O(Y^4)$ and $b'(Y)=O(Y^3)$. In a fixed neighborhood of $x$, signed distance is smooth and its unit normal differs from the horizontal direction by $O(|z-x|^3)$. Consequently, on $B(x,20\rho)$,

$$\operatorname{Lip}(V)\le1+C\rho^3$$

for a fixed $C$ and sufficiently small $\rho$. Indeed the two rows of $DV$ are the unit vector $\nabla s$ and $(0,1)$, whose inner product is $O(\rho^3)$; the largest eigenvalue of their Gram matrix is $1+O(\rho^3)$. The ball is convex, so the derivative bound gives the stated Lipschitz bound.

Moreover, $|V(p)|\le\rho$ implies $|p-x|\le2\rho$ for sufficiently small $\rho$. To see this, $|Y_p|\le\rho$ and a nearest point $(b(t),t)$ on $\Gamma$ has $|t-Y_p|\le\rho$, hence $|t|\le2\rho$. It follows that $|X_p-1/2|\le\rho+O(\rho^4)$ and initially $|p-x|\le2\rho$. The local expansion of signed distance gives the sharper equivalence if needed.

For two points in $B(x,20\rho)$,

$$F_\alpha=-\frac12+G_{\alpha,\rho}\circ V$$

therefore has seminorm at most

$$(1+\varepsilon_\alpha)(1+C\rho^3)^\alpha
=1+\varepsilon_\alpha+O(\alpha\rho^3).$$

## Mixed pairs outside the local ball

It remains to compare $p$ with $|V(p)|<\rho$ to $q$ with $|q-x|\ge20\rho$. Put $R=|q-x|$. The previous implication shows $|V(q)|>\rho$, so $F_\alpha(q)=H(q)$, while $F_\alpha(p)\le H(p)$.

If $F_\alpha(p)\ge F_\alpha(q)$, then

$$F_\alpha(p)-F_\alpha(q)\le H(p)-H(q)\le|p-q|^\alpha.$$

For the reverse inequality use $g_\alpha\ge0$, hence $F_\alpha(p)\ge-1/2$, and $\Pi(q)\le2\operatorname{dist}(q,Z)\le2R$. Since $|p-q|\ge R-2\rho$,

$$\frac{F_\alpha(q)-F_\alpha(p)}{|p-q|^\alpha}
\le\frac12\left[\left(\frac{\rho}{R-2\rho}\right)^\alpha+
\left(\frac{2R}{R-2\rho}\right)^\alpha\right]
\le\frac12\left(18^{-\alpha}+(20/9)^\alpha\right).$$

Both terms in the middle expression decrease with $R/\rho\ge20$. The final expression is at most one for $0\le\alpha\le1/2$: it is convex in $\alpha$, equals one at zero, and at $1/2$ equals

$$\frac12\left(\frac1{3\sqrt2}+\frac{2\sqrt5}3\right)<1.$$

This controls every remaining mixed pair. Pairs with both points outside the freezing set are controlled by $H$.

## Clamp and extension

On the right half-plane $[h]_\alpha\le2^{\alpha-1}\le1$. Taking a minimum with $h$ and a maximum with $-h$ preserves the larger Hölder bound. Across $X=0$, the odd extension satisfies

$$|f_\alpha(p)-f_\alpha(q)|\le\frac12(2X_p)^\alpha+\frac12(2|X_q|)^\alpha
\le(X_p+|X_q|)^\alpha\le|p-q|^\alpha.$$

Reflection treats pairs in the left half-plane. This completes the conditional assembly proof.

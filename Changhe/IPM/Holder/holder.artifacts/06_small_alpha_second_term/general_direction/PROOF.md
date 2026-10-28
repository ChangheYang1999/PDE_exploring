# Existence and exact variational formula for the second term

Status: proved. The finite-dimensional maximization in the formula is not evaluated here.

## Statement and notation

Work with the real homogeneous Hölder seminorm on the plane and the singular-integral extension modulo constants defined in `../../01_setup/PROOF.md`. For $0<\alpha<1$, let $C_\alpha$ be the common seminorm operator norm of $T_{xx}$ and $T_{xy}$. Put $x=(1/2,0)$, $y=-x$, and, for $b\in\mathbb R$, define

$$K_b(z)=\frac{\cos(2\arg z-2b)}{2\pi|z|^2},\qquad
\nu_b(w)=K_b(x-w)-K_b(y-w).$$

Let $H=\{w_1>0\}$ and

$$J(b)=\int_{H\setminus B(x,1/2)}|\nu_b(w)|\,dw
+\int_{B(x,1/2)}\bigl(|\nu_b(w)|-|K_b(x-w)|\bigr)\,dw.$$

Both integrals converge absolutely. Then

$$C_\alpha=\frac2{\pi\alpha}+C_0+o(1),\qquad
C_0=-\frac{1+\log2}{\pi}+\max_{0\le b\le\pi/4}J(b).$$

For each fixed $b$, the norm of the unit increment functional

$$V(\alpha,b)=\sup_{[f]_\alpha\le1}\left|(T_bf)(x)-(T_bf)(y)\right|$$

has the expansion

$$V(\alpha,b)=\frac2{\pi\alpha}-\frac{1+\log2}{\pi}+J(b)+o(1).$$

The maximum exists. The independently evaluated diagonal value in `../diagonal/PROOF.md` yields

$$C_0\ge\frac12+\frac{\log2-1}{\pi}.$$

This last inequality is not asserted to be equality. The theorem does not determine a second term for $D_\alpha=\|R_1^2\|$.

Dependencies: the setup, the exact angular estimate in `../../02_upper_bounds/PROOF.md`, and the signed-distance Hölder lemma. This is an independent completion of the lead's `notes/c0_theorem.md`; in particular the local lower-bound error is proved below without an unproved logarithmic-distance assertion.

## Increment decomposition and finite part

The complex kernel is $k(z)=1/(2\pi\overline z^2)$. Its increment satisfies

$$|\nu_b(w)|\le\left|k(x-w)-k(y-w)\right|
=\frac{|w|}{\pi|w-x|^2|w-y|^2}.$$

Thus the increment is $O(|w|^{-3})$ at infinity, uniformly in $b$. On $B(x,1/2)$ the absolute value of the difference $|\nu_b|-|K_b(x-\cdot)|$ is bounded by $|K_b(y-\cdot)|\le2/\pi$. These facts prove the asserted absolute convergence and, by dominated convergence, continuity of $J$ in $b$.

Fix $0<\rho<1/2$. The increment acting on $f$ equals the sum of the two local, center-subtracted kernel integrals and the action of the density

$$\mu_{b,\rho}(w)=K_b(x-w)\mathbf1_{|x-w|\ge\rho}
-K_b(y-w)\mathbf1_{|y-w|\ge\rho}.$$

This density is integrable, odd under $w\mapsto-w$, and has the same uniform cubic decay at infinity. Every term in the decomposition is absolutely convergent for $[f]_\alpha<\infty$, after using the basepoint normalization from the setup. Circular cancellation justifies changing the local cutoff radius.

The circular finite part is

$$W(b)=\lim_{\rho\downarrow0}\left[
\frac2\pi\log\rho+\frac12\int_{\mathbb R^2\setminus(B(x,\rho)\cup B(y,\rho))}|\nu_b|\right]
=J(b)-\frac{2\log2}{\pi}.$$

Indeed, the half-plane $H$ contains the entire disk $B(x,\rho)$ and the absolute increment is centrally even. Subtract the own kernel in $B(x,1/2)$, and use its exact annular absolute mass $2\log((1/2)/\rho)/\pi$. The remaining integral over $B(x,\rho)$ is bounded in magnitude by a constant times $\rho^2$, uniformly in $b$.

## Uniform upper bound

The two local integrals are bounded by

$$\frac{2a_2(\alpha)\rho^\alpha}{\alpha},\qquad
a_2(\alpha)=\frac{2^{1+\alpha/2}}{\pi(\alpha+2)}.$$

Since $\mu_{b,\rho}$ is odd, antipodal pairing gives

$$\left|\int\mu_{b,\rho}f\right|
\le2^{\alpha-1}\int |\mu_{b,\rho}(w)|\,|w|^\alpha\,dw.$$

For fixed $\rho$, the latter expression converges as $\alpha\downarrow0$ to $\frac12\|\mu_{b,\rho}\|_1$, uniformly in $b$. To see uniformity directly, bound $|\mu_{b,\rho}|$ by a single integrable density with cubic decay and multiply it by $\max(1,(2|w|)^{1/2})$. The supremum over $b$ of the error is then bounded by an integral to which dominated convergence applies.

The contribution of $\mu_{b,\rho}$ inside the two disks is at most $\rho^2/(2(1-\rho)^2)$ after multiplication by $1/2$. Moreover,

$$\frac{2a_2(\alpha)\rho^\alpha}{\alpha}
=\frac2{\pi\alpha}+\frac{\log2-1}{\pi}+\frac2\pi\log\rho+O_\rho(\alpha).$$

Combining these statements and the finite-part formula proves a bound uniform in $b$:

$$\limsup_{\alpha\downarrow0}
\left(V(\alpha,b)-\frac2{\pi\alpha}\right)
\le\frac{\log2-1}{\pi}+W(b),$$

where uniformity means that the supremum of the positive error over $b$ tends to zero. One first fixes $\rho$, takes $\alpha\downarrow0$, and then takes $\rho\downarrow0$.

## Local geometry for the matching lower bound

Fix $b$. Let $Z_b$ be the closure of the zero set of $\nu_b$, including the poles. Give its complement the sign of $\nu_b$, and let $v_b$ be the resulting signed distance. The segment-crossing argument proves that $v_b$ is 1-Lipschitz. Define

$$f_{\alpha,b}=2^{\alpha-1}\operatorname{sign}(v_b)|v_b|^\alpha.$$

Then $[f_{\alpha,b}]_\alpha\le1$, both pole values vanish, and

$$V(\alpha,b)\ge\int\nu_b f_{\alpha,b}
=2^{\alpha-1}\int|\nu_b|\,\operatorname{dist}(w,Z_b)^\alpha\,dw.$$

The zero set has area zero: away from the poles it is the zero set of a nonzero real-analytic rational function, whose numerator is a nonzero polynomial. Consequently the integrand outside fixed pole disks converges almost everywhere to $|\nu_b|/2$. It is dominated there by an integrable function, since the distance to $Z_b$ is at most the distance to a pole and $\alpha\le1/2$.

It remains to control the disks without losing a constant term. In coordinates $w=x+r(\cos\theta,\sin\theta)$, the zero equation is

$$\frac{\cos(2\theta-2b)}{2\pi}-r^2K_b(y-x-r(\cos\theta,\sin\theta))=0.$$

The second term is smooth for $r<1/2$. At $r=0$ the four angular roots are simple, and the first radial derivative of the second term vanishes. The implicit function theorem and uniform angular separation from zero outside neighborhoods of these roots show that, for sufficiently small $r$, these are exactly four arcs with angular displacement $O(r^2)$ from the two perpendicular zero lines of the own kernel. In a radius-$2r$ disk their displacement is therefore $O(r^3)$.

Let $v_0$ be signed distance to these two lines, with the sign of the own kernel. Nearest points can be sought in the radius-$2r$ disk because the pole belongs to both zero sets. The ordinary distance comparison and the fact that opposite signs occur only between corresponding arcs imply

$$|v_b(w)-v_0(w)|\le A_b r^3.$$

For completeness, in an angular neighborhood of each zero ray the two curves are graphs over that ray with transverse separation bounded by $A_b r^3$. When the signs differ, the point lies between these graphs, so the sum of its two unsigned distances is bounded by their transverse separation. Outside these neighborhoods the signs agree and the Hausdorff distance bound applies directly.

Write $v_0=r\psi(\theta)$ and $\epsilon=A_b r^2$. Thus $v_b/r=\psi+O(\epsilon)$. The angular own-kernel weight is bounded by $2|\psi|$. On $|\psi|\ge2\epsilon$, the signed-power mean value theorem gives

$$|\psi|\left|\operatorname{sign}(v_b)|v_b/r|^\alpha
-\operatorname{sign}(\psi)|\psi|^\alpha\right|
\le A'_b\alpha\epsilon,$$

uniformly for $0<\alpha\le1/2$. On $|\psi|<2\epsilon$, the angular set has measure $O(\epsilon)$, its kernel weight is $O(\epsilon)$, and the powers remain bounded. Its integrated contribution is $O(\epsilon^2)$. The total weighted angular error is therefore

$$O_b(\alpha r^2+r^4).$$

Radial integration against $r^{\alpha-1}$ bounds the local difference from the exact angular extremizer by

$$O_b(\alpha\rho^{\alpha+2}+\rho^{\alpha+4}).$$

The smooth other-pole kernel contributes $O(\rho^{\alpha+2})$. The same argument applies at $y$, with the reversed sign. Hence

$$\limsup_{\alpha\downarrow0}
\left|\int_{B(x,\rho)\cup B(y,\rho)}\nu_b f_{\alpha,b}
-\frac{2a_2(\alpha)\rho^\alpha}{\alpha}\right|=O_b(\rho^2).$$

Taking the outside limit, then sending $\rho\downarrow0$, proves the fixed-$b$ lower bound with second term $(\log2-1)/\pi+W(b)$.

## Passing to the full operator norm

Translation, dilation, and rotation give $C_\alpha=\sup_b V(\alpha,b)$. Reflection in the horizontal axis sends $b$ to $-b$, and increasing $b$ by $\pi/2$ reverses the kernel sign. Therefore $b$ can be restricted to $[0,\pi/4]$. The uniform upper estimate gives the upper limit bounded by the maximum of the stated continuous function. Fixing any maximizing $b$ in the lower construction gives the reverse limit. No uniform lower estimate or exchange of a supremum with a merely pointwise limit is used.

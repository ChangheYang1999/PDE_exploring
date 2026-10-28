# Audit of the corrected polar-cell certificate

Status: the corrected algorithm is valid under its stated parameter range and the mesh choices used in the reported runs. The old sliver formula was false; this audit concerns the corrected source snapshot, not its previous version.

## Claim and dependencies

For the polygonal signed-distance function in `../structured_witness/PROOF.md`, the corrected `certify_lb.py` encloses the increment integral by summing exact local terms, interval cell contributions, and explicit omitted-region bounds. Its real Hölder seminorm is at most one and both evaluation values vanish, so every certified lower endpoint bounds both $C_\alpha$ and $D_\alpha$. Operator and space definitions are those of `../../01_setup/PROOF.md`.

The independent layer-cake proof in `../structured_layercake/PROOF.md` recomputes this integral through a different one-dimensional formula. Its certificate already proves $C_{1/2},D_{1/2}\ge2.0877423954$, independently validating the weaker numerical lower bounds previously reported by the numerical team.

## First-order cells

Let $Q$ be a cell, $c$ its exact centroid, and $r_Q$ a radius containing it. If $k$ is the increment density and $f$ the witness, then

$$|k(z)f(z)-k(c)f(c)|\le\sup_Q|k|\,|f(z)-f(c)|+|f(c)|\sup_{[c,z]}|\nabla k|\,|z-c|.$$

The global Hölder bound supplies $|f(z)-f(c)|\le r_Q^\alpha$. If the ball avoids $Z$, the mean value estimate for $2^{\alpha-1}d^\alpha$ gives the alternate bound $2^{\alpha-1}\alpha(d(c)-r_Q)^{\alpha-1}r_Q$. Taking the smaller is valid. When a sign decision at the centroid is uncertain, the code encloses both signs.

## Second-order cells and the distance Hessian

Every piece used to form $Z$ is a closed convex line, segment, or ray. For distance $d_C$ to such a piece, the squared-distance function has gradient $z-P_Cz$, which is 1-Lipschitz by the firm nonexpansiveness of the convex projection. Away from $C$, $d_C$ is continuously differentiable with unit gradient. At almost every point,

$$0\le D^2d_C\le I/d_C.$$

This can be derived by differentiating the squared-distance function, or directly from its piecewise linear and circular formulas here. Hence, for $0<\alpha<1$,

$$\|D^2(d_C^\alpha)\|\le\alpha(2-\alpha)d_C^{\alpha-2}.$$

The displayed estimate uses the triangle inequality and is safe; it need not be sharp. The gradient is locally Lipschitz, so the almost-everywhere Hessian bound implies the usual Taylor remainder along line segments even across a transition between endpoint and interior projection.

If one piece is nearest at $c$ and its distance is separated from all other piece distances by more than $2r_Q$, it stays uniquely nearest throughout the ball. This follows from the 1-Lipschitz property of each distance. The code's sorted tentative winner is accepted only after this certified gap test; a floating-point sort by itself is not used as evidence. Thus $d_Z=d_C$ throughout that ball and the preceding Hessian estimate applies.

For $g=kf$,

$$\|D^2g\|\le\sup|f|\sup\|D^2k\|+2\sup|\nabla k|\sup|\nabla f|+\sup|k|\sup\|D^2f\|.$$

Integrating the Taylor expansion at the exact centroid removes its linear term. The remainder is at most half this bound times $\int_Q|z-c|^2\,dz$. Both the centroid and this second moment are evaluated by exact polar-sector formulas with outward interval arithmetic. An interval enclosing the centroid encloses the value at that exact point.

## Kernel and geometric bounds

For $K=xy/(\pi|z|^4)$, complex differentiation gives $|K|\le1/(2\pi r^2)$, $|\nabla K|\le1/(\pi r^3)$, and $\|D^2K\|\le3/(\pi r^4)$. For the increment at unit-separated poles, the corresponding far bounds are $1/(\pi d^3)$, $3/(\pi d^4)$, and $12/(\pi d^5)$, where $d$ is the distance to the segment joining the poles, bounded below by distance to the midpoint minus $1/2$.

For a sector about one pole with inner radius $r_1$ and angular half-width $h\le\pi/2$, its convex hull lies in a half-plane whose distance to that pole is $r_1\cos h$. The corrected code uses this lower bound for all Taylor segments. The enclosing-ball distance to the other pole remains valid. Thus the earlier claim that $r_1$ bounds the distance of the whole enclosing ball is no longer needed.

The midpoint sectors are either inside the two radius-$1/2$ disks, outside them, or cut by their boundaries. The test is the exact polar condition $r\le|\cos\theta|$ for their union. Ambiguous cells are subdivided; at the final level the entire cell area times a valid supremum bounds the integral over its remaining subset. There is no need to approximate that subset's area.

## Omitted regions and exact local contribution

Within radius $\min(a,1)/2$ of a pole, the nearest zero pieces are exactly its two perpendicular local lines. The own-kernel integral is therefore $a_2(\alpha)r^\alpha/\alpha$. The cross kernel is smooth and is bounded by its distance from the other pole. The outer tail uses $|f(z)|\le2^{\alpha-1}|z-m|^\alpha$ and the far kernel estimate, giving the explicit bound in the source.

For the small midpoint sliver outside both disks, at radius $r<1$ the angular measure is exactly $4\arcsin r$. Therefore, with $C=2^{\alpha-1}$,

$$\left|\int_{\text{sliver},\ |z-m|<\rho}kf\right|
\le\frac{16C}{\pi}\int_0^\rho r^{\alpha+1}\arcsin r\,dr
\le\frac{16C\rho^{\alpha+3}}{\pi(\alpha+3)\sqrt{1-\rho^2}}.$$

This is the corrected expression in the source. The old area upper bound $4\rho^3/3$ was too small.

## Arithmetic and scope

Arb operations are outward-enclosing. Worker midpoint and radius strings are parsed as enclosures, and the radius is used as an upper magnitude, so serialization is safe. Exact decimal grid endpoints are shared by adjacent cells; their use does not create gaps. This audit validates the corrected implementation's mathematical estimates. It does not retroactively turn an old erroneous source snapshot into a valid certificate. Concrete reported numbers are independently checked by the separate layer-cake integral.

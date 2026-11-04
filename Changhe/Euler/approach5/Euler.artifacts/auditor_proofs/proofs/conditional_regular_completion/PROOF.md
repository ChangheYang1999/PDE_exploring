# Exact exterior completion conditional on a smooth regular plug

## Statement

Let 0<c<1/2, b=1+c, a=1-2c, d=3c=b-a, and A=cI-omega J for any fixed finite real omega. Let N be a compact connected oriented smooth three-manifold diffeomorphic to the exterior of a knot in S3. Suppose it has a smooth positive volume form m and smooth fields B,W satisfying

    div_m B=d, div_m W=0, [B,W]=-bW.

Assume B is strictly outward on its boundary, B and W are nonzero and independent throughout N, and the maximal backward invariant set Lambda in N is a transitive hyperbolic attractor of -B with W spanning its stable line. Finally assume there is a smooth meridian E in the boundary whose tangent is everywhere transverse to span(B,W).

Then these fields admit a smooth completion, after a time-preserving spatial conjugacy of N, to R3 with standard volume such that B=Ay+U, U is compactly supported and divergence free, W is smooth and divergence free, and [B,W]=-bW. There is one added zero p of B with spectrum {b,-a/2,-a/2}. Its one-dimensional B-unstable manifold is a proper line ell, W is nonzero on ell, and the backward basin of Lambda is R3 minus ell. On the exterior |D^jW|=O(r^(-1/c-j)) for every fixed j.

This is a conditional construction. It does not provide N or E. It does not assert W=curl U. The regular kinematic realization problem and the Euler problem remain open.

## Exact collar at the meridian

Write theta=i_W i_-B m. Parametrize the meridian by e(u), with u periodic, and use the map

    F(r,u,z)=flow_W^z(flow_B^r(e(u))).

Transversality gives an embedded coordinate neighborhood for uniformly small r,z. The bracket identity gives

    W=partial_z, B=partial_r+b z partial_z.

The W-divergence equation makes the coordinate volume density independent of z. The B-divergence equation then gives

    m=h(u) exp(-ar) dr du dz, theta=h(u)exp(-ar)du.

Orient u so h>0. Reparametrization with period 2pi makes h a positive constant h0. A short W-saturated annulus r=0 can be made part of the actual boundary: it projects diffeomorphically to the old boundary along B, and replacing the boundary by this nearby graph preserves outward transversality. The modification is confined to a collar disjoint from Lambda.

All collar extensions can be made exactly. On an arbitrary outgoing boundary, let s be B-time, sigma=i_Bm on the boundary, and write W=w(q)partial_s+V(q) there. Extend by

    B=partial_s, m=exp(ds)ds sigma,
    W=exp(-bs)(w partial_s+V).

Its divergence is exp(-bs)(div_sigma V-a w), which is zero because the original boundary data satisfy that equation. These formulas also agree with the original fields on the inner flow collar, so no derivative mismatch is introduced.

## The two-handle and its dynamics

Put R0^2=2h0/a and use

    R=R0 exp(-ar/2), x=R cos u, y=-R sin u.

Then m=dx dy dz exactly and

    B=-(a/2)(x partial_x+y partial_y)+b z partial_z,
    W=partial_z.

Attach the full handle {x^2+y^2<=R0^2, |z|<=epsilon} by its lateral annulus. The coordinates match on an open collar. The displayed fields and volume extend over its center without a singularity, satisfy all three differential identities, and introduce only the zero p at its center. In backward time the radius increases as exp(at/2) and |z| decreases as exp(-bt). Every off-axis handle point therefore enters N in finite backward time; the axis tends to p.

B points out of the caps and into the handle across its attaching side. At the two exposed corners, the coordinates r and |z|-epsilon both increase under B. A monotone rounded corner thus remains strictly outward. Only the domain boundary changes, so no field identity is perturbed. The small rounding region follows the same transit orbits.

Meridional handle attachment changes the knot exterior into a ball M. Indeed the omitted part of its complementary solid torus is a thick disk complement, hence an embedded ball in S3. That known ball is ambiently isotopic to a small coordinate ball: shrink its parametrized embedding within itself, then straighten in a chart, extending the smooth embedding isotopy to an ambient isotopy. Its complement is consequently a ball as well. No claim that arbitrary orbital equivalence fixes the knot slope is used: the hypothesis specifies a meridian.

## Matching the Euclidean exterior

Let V=integral_M m and choose R* by 4pi R*^3/3=V. The outgoing flux form sigma=i_Bm on the sphere boundary of M has total dV. On the Euclidean sphere of radius R*, the field Ay has flux form cR* dS and the same total dV, since Jy is tangent to the sphere.

There is an orientation-preserving boundary diffeomorphism h matching these two forms. For completeness, after any sphere parametrization their difference is a smooth two-form of integral zero, hence equals d eta. This follows, for example, by solving the mean-zero scalar Laplace equation on S2 by spherical harmonics. For the convex path sigma_t of positive forms, the equation i_(Y_t)sigma_t=-eta has a smooth solution Y_t. Its flow pulls sigma_t back to sigma_0 and provides the required h. This proves the volume-form fact needed here.

On an open flow collar prescribe

    j(flow_B^s q)=exp(As)h(q).

It sends B to Ay and pulls Euclidean volume back to exp(ds)ds sigma=m. Extend it to a ball diffeomorphism using a collar isotopy: interpolate the two outward transverse collar fields, use their flows to interpolate the collar parametrizations, and extend the isotopy generator by a cutoff. All interpolated fields remain outward in a common sufficiently thin collar.

One final interior volume correction is legitimate. The forms m and j*vol agree near the boundary and have equal total integral. Their compactly supported difference has a compactly supported primitive on the interior ball. An explicit proof in R3 is obtained by integrating the density first in x and subtracting eta1(x) times its x-integral, then in y with the corresponding subtraction, and finally in z; the final primitive is compactly supported because the total density integral is zero. Apply the same convex-path Moser equation with this primitive. Its vector field vanishes in a boundary collar, so the resulting diffeomorphism leaves the prescribed collar map unchanged. Composing j with it matches volume everywhere.

Transport B,W by this corrected j. Extend B=Ay outside the sphere and set

    W(exp(As)y0)=exp(-bs)exp(As)W(y0), s>=0.

Each exterior point has unique coordinates (s,y0), because its radius is R*exp(cs). These expressions agree with the inner collar, preserve the bracket equation, and preserve div W=0 by the preceding intrinsic collar calculation. Thus U=B-Ay is smooth, compactly supported and divergence free. The formula reduces to

    W(exp(As)y0)=exp(-s)exp(-omega Js)W(y0).

It proves all derivative bounds and makes W bounded. Both B and W have complete flows.

## Basin and exceptional line

The two axial B-orbits exit the handle caps, then the outgoing collar, then tend to infinity in the exact linear exterior. They cannot meet each other. Together with p they form one smooth proper line ell, also a W-trajectory; W is already nonzero and smooth across its central segment and remains so by transport. There is no limiting extension across that line to justify.

Every other exterior point enters M in finite backward time. The collar and handle formulas then put it in N in finite additional backward time, so its limit lies in Lambda. No time change was used on N. Thus the regular dynamics on Lambda and its stable W-line are preserved. Conversely points on ell tend to p rather than Lambda. This gives the stated basin.

The forward nonescaping set on the adjusted plug boundary is exactly E. Removing E leaves an annulus mapped by first forward exit to the large sphere minus its two axial points. This is compatible with the necessary topology A162, but establishing a transverse meridian for a proposed plug is still a separate requirement.

## Scope audit

The construction in the coordinator's regular_construct response has the asserted conditional content. Smoothness of W, not merely C1, is an explicit input of this version. The unconstructed plug must satisfy the exact differential identities before attachment. A train-track combinatorial model, interval packing or an orbit-equivalence classification does not supply that input. No global regular example or obstruction follows from this completion alone.

# Audit of the two-dimensional projection-cusp certificate

## Statement and scope

Implementation correction V103: the old source snapshot has three reproducible interval defects. The analytic rules below are conditional on valid input enclosures. See repairs/PROOF.md for the counterexamples and the repaired source snapshot. This proof does not unconditionally endorse the old implementation.

Fix 0<alpha<1, b>0, a real c, and lambda>=0 with lambda [P]_alpha<=1. Let
Z0(b) be the axis polygon defined in ../../11_lattice_pole_constraints/axis_clamped_layercake/PROOF.md,
translated so that the poles are (0,0) and e1=(1,0). On H={x>1/2}, put

    g=2^(alpha-1) sigma dist(.,Z0(b))^alpha,
    P(w)=1/2 [|w|^alpha+sgn(w1^2-w2^2)(|w1^2-w2^2|/|w|)^alpha],
    h=2^(alpha-1)(x-1/2)^alpha,
    f=clamp(min(g+c,-1/2+lambda P(.-e1)),-h,h).

Set P(0)=0. Extend f by odd reflection across x=1/2. The polygon and P
are even in y, so f is also odd under point reflection through (1/2,0).
The lattice lemma gives [f]_alpha<=1 and f(e1)=-1/2, f(0)=1/2.
At e1, g=P=0 and min(c,-1/2)<=-1/2, so clamping gives this pole value
for every real c. No sign restriction on c is needed.

Let K(w)=(w1^2-w2^2)/(2 pi |w|^4), k(z)=K(z-e1)-K(z), with circular
principal values at the poles. Then the quantity D_alpha is at least
|I0|+1/2, where I0=pv integral k f. This bound uses the choice between
T_xx-I/2 and T_xx+I/2, whose norms are equal. It does not require that
I0 be positive.

The cell rules in the archived code enclose I0 provided all tasks finish,
the domain decomposition and parameter restrictions below hold, and the
external seminorm condition lambda[P]_alpha<=1 has been verified. This
method audit is not a certification of an unfinished run or of an
unverified value of lambda.

## Stable kernel and differential bounds

Write A=x^2+y^2, B=(x-1)^2+y^2, and u=1-2x. Algebra gives

    k(x,y)=u [A(3y^2-x^2)-u(x^2-y^2)]/(2 pi A^2 B^2).

It is the exact difference of the two kernels. It avoids the subtraction
of nearly equal floating values at large radii. Direct differentiation
of the real part of (2 pi z^2)^(-1) gives

    |K|<=1/(2 pi r^2), |grad K|=1/(pi r^3),
    ||Hess K||_op=3/(pi r^4).

For k, the sums of these bounds at the two poles are valid. If every
point is at distance at least d>1/2 from their midpoint, integrating
one more derivative along the segment between the poles also gives

    |k|<=1/[pi(d-1/2)^3],
    |grad k|<=3/[pi(d-1/2)^4],
    ||Hess k||_op<=12/[pi(d-1/2)^5].

The implementation takes the smaller of two valid bounds.

## The smooth profile branch

On a ball avoiding both the origin and w1=+-w2 write P=r^alpha Phi(theta),
Phi=(1+q)/2, q=s(s cos(2theta))^alpha, where s is the constant sign of
cos(2theta). With C=s cos(2theta)>0,

    q'=-2 alpha sin(2theta) C^(alpha-1),
    q''=s [4 alpha(alpha-1)sin(2theta)^2 C^(alpha-2)-4 alpha C^alpha].

In the orthonormal polar frame the gradient has components
r^(alpha-1)(alpha Phi,Phi'). The Hessian has entries

    r^(alpha-2) [ alpha(alpha-1)Phi, (alpha-1)Phi';
                 (alpha-1)Phi', alpha Phi+Phi'' ].

Thus the implemented gradient norm and Hessian Frobenius norm are
upper bounds for the required Euclidean and operator norms. If the
ball has center of radius rho and radius rQ<rho, its radial range is
[rho-rQ,rho+rQ] and its angular deviation is at most asin(rQ/rho).
Replacing theta by theta+pi does not change P or these bounds. The
implementation chooses between these two angular representations to
avoid an artificial atan2 branch cut. If the angle enclosure reaches
a diagonal, it declines to use smoothness. Balls reaching the origin
are treated in the same conservative way.

On a smooth signed-distance branch, the nearest polygon piece must be
unique throughout the ball. A gap exceeding 2rQ between the nearest
piece and every competitor at the center proves this. Distance to one
closed segment, ray or line is C^(1,1) away from the piece, including
projection transitions at its endpoints. With Dmin=dist(center,Z)-rQ>0,

    |grad g|<=2^(alpha-1) alpha Dmin^(alpha-1),
    ||Hess g||_op<=2^(alpha-1) alpha Dmin^(alpha-2)

almost everywhere. The second-order integral remainder remains valid
for this C^(1,1) regularity. The same reasoning applies to +-h.

The min and clamp branches are chosen only after their center values,
plus or minus a uniform variation bound, are strictly separated. When
smoothness is unavailable the variation rQ^alpha follows from the
external seminorm bound. This prevents a second-order rule from being
used across a branch interface. If the ball reaches the reflection
axis, only the global Holder rule is used.

## Cell integration and domain coverage

For a polar cell Q let zc be its exact centroid, rQ an upper bound for
max_Q|z-zc|, area=|Q|, and M2 an upper bound for integral_Q|z-zc|^2.
The archived cell_geom_ang computes these from the exact polar-sector
formulas, with outward rounding. On a full cell, the first-order error
for kf is bounded by

    area [sup|k| rQ^alpha+|f(zc)| sup|grad k| rQ].

For a certified smooth branch, a Hessian bound H for kf gives error
H M2/2. The linear term integrates to zero at the centroid. If the
latter error is smaller, the code uses it. Near e1 the integrand is
K(z-e1)(f(z)+1/2)-K(z)f(z); the same rules apply separately to the two
products. This removes the artificial singular error caused by the
constant pole value. That constant integrates to zero over each full
centered annulus, so the sum still represents the principal value.
Reflection doubles the e1-disk contribution to account for the 0 disk.

The two open disks of radius 1/2 are disjoint. In midpoint polar
coordinates z=(1/2,0)+rho(cos(theta),sin(theta)), their complement is
rho>=|cos(theta)|. A cell entirely within the disks is omitted; a cell
entirely outside is integrated. If it straddles the boundary at the
last refinement level, the absolute integral on the exterior portion
is bounded by the full-cell area times an upper bound of |kf|. Its
contribution is enclosed symmetrically about zero. Distances to both
poles are at least 1/2 on that exterior portion, even if the enclosing
ball reaches a pole.

Require 0<rho_min<1/2, 0<rho_m<1 and rho_max>1, positive mesh sizes,
and angular cell widths below pi. The three omitted regions have
absolute bounds

    E_inner=rho_min^alpha/alpha
              +rho_min^2(1/2+rho_min^alpha)/[2(1-rho_min)^2],
    E_sliver=16*2^(alpha-1)*rho_m^(alpha+3)
              /[pi(alpha+3)sqrt(1-rho_m^2)],
    E_tail=2^alpha [R/(R-1/2)]^3 R^(alpha-1)/(1-alpha), R=rho_max.

The first uses |f(z)-f(e1)|<=|z-e1|^alpha and the regular cross-kernel
bound. The second uses |k|<=4/pi on the disk complement and its angular
measure 4 asin(rho)<=4rho/sqrt(1-rho_m^2). The last uses the dipole
bound and |f(z)|<=2^(alpha-1)|z-(1/2,0)|^alpha. Therefore

    I0 in 2*(near+[-E_inner,E_inner])+rest
              +[-E_sliver,E_sliver]+[-E_tail,E_tail].

Shared radial endpoints are represented by identical strings and
shared angular endpoints by the same expressions. Inexact choices of
mesh locations do not impair coverage. Tasks must cover each radial
interval once and all angular cells once. The numeric inputs in the
runs being audited satisfy the restrictions above; the script does
not itself enforce all of them for arbitrary command-line input.

## Evidence and remaining checks

The source snapshot and SHA256 manifest are in sources/ and
verification/. The mathematical audit was completed on 2026-10-28.
Independent finite-point and derivative diagnostics, and each final
reported enclosure, are separate checks recorded in the verifier's dated record (not included).
No finite diagnostic replaces the branch or domain arguments above.

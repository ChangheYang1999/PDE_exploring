# Local-circle transport with the diagonal identity term

## Theorem and exact convention

Let 0<alpha<1, p>0, 0<delta<R=1/2, and let m be a positive integer.
The operators and the real homogeneous Holder seminorm on R^2 are those
of ../../01_setup/PROOF.md. Put x=(1/2,0), y=-x and

    T_phi=cos(phi)T_xx+sin(phi)T_xy,
    phi_j=j*pi/(2m), 0<=j<=2m,
    eta=(1/2)(2*delta)^p,
    q=sec(pi/(4m)).

For each j, let L_j be any rigorous transport upper bound for the regular
local measure defined below on delta<=r<=R, and let M_j,E_j be rigorous
upper bounds for the middle and exterior parts of the same kernel
increment. Then

    D_alpha <= S_alpha(delta)+eta
               +q*max_j(L_j+M_j+E_j)+(q-1)*(1/2-eta),

where

    S_alpha(delta)=2*a_2(alpha)*delta^alpha/alpha
                  +(1+2*delta)^alpha*delta^2/(2*(1-delta)^2),
    a_2(alpha)=2^(1+alpha/2)/(pi*(alpha+2)).

The result also bounds the original compact smooth test supremum. This is
a theorem for any feasible plans and any stated parameters. Concrete
numerical bounds require outward arithmetic and complete coverage checks.

## Exact measure and the identity allocation

Write z_r(theta)=1/2+r*exp(i*theta). The paired local-circle decomposition
in ../paired_local_circles/PROOF.md gives the two local disks' increment as

    integral_0^R integral_0^(2*pi)
      w_(r,phi)(theta)[f(z_r(theta))-f(-z_r(theta))] dtheta dr/r,

    w_(r,phi)(theta)=[cos(2*theta-phi)
       -r^2*Re(exp(i*phi)/(1+r*exp(i*theta))^2)]/(2*pi).

Let lambda(r)=(p/2)(2r)^p. Its integral against dr/r from zero to R is
1/2. Therefore the exact identity contribution -(f(x)-f(y))/2 can be
inserted by replacing each circle measure by

    mu_(r,phi)=w_(r,phi)(theta)dtheta at z_r(theta)
              -w_(r,phi)(theta)dtheta at -z_r(theta)
              -lambda(r)delta_x+lambda(r)delta_y.

This measure has zero total mass and is antisymmetric under z -> -z.
On 0<r<delta the circle part costs at most S_alpha(delta), by the previous
local theorem, and the atomic part costs at most eta since |x-y|=1.
These bounds include the small disks' smooth cross-kernel contributions.

## A completely finite feasible plan on each radial interval

Fix a<=r<=b. Use the certified signed angular masses from the previous
local theorem: if a cell has one sign throughout this radial interval,
extract a constant mass of that sign whose magnitude is no larger than
its actual mass; otherwise extract zero. Let V be a uniform upper bound
for the right circle's total variation and let A be the sum of absolute
extracted right-circle masses. Include their negatives at the opposite
circle. Also extract atomic masses -c at x and +c at y, where
0<=c<=lambda(a). All extracted masses sum to zero. A nonnegative transport
plan with these exact marginals is feasible for every r in the interval.

For same-circle cells with circular index separation k among n equal
angular cells, the integrated cost is at most

    [2*sin(pi*min(k+1,n/2)/n)]^alpha * (b^alpha-a^alpha)/alpha.

For opposite-circle cells, an upper bound for distance is the maximum of
|1+a(u+v)| and |1+b(u+v)| over the two angular arcs. The squared distance
is convex in r, so these endpoints suffice. Raise that bound to alpha and
multiply by log(b/a).

An arc and its own center have integrated cost (b^alpha-a^alpha)/alpha.
An arc and the opposite center use the maximum of |1+a*u| and |1+b*u|
over the arc, raised to alpha and multiplied by log(b/a). Between the two
centers the integrated cost is log(b/a).

Multiply each such integrated cost by its transported mass and sum. The
remaining circle variation is antisymmetric and costs at most

    (V-A)*(1+2b)^alpha*log(b/a),

by pairing every residual point with its negative. The remaining atomic
mass can be integrated exactly and costs at most

    (1/2)[(2b)^p-(2a)^p]-c*log(b/a).

Both residual terms are nonnegative. This proves the finite-plan bound
without any assertion that the selected plan is optimal. Integer mass
quantization gives exact marginal checks. All distances, powers,
integrals and residuals can be enclosed with outward interval arithmetic.
Summing a partition of [delta,R] defines L_j.

## The full phase interval and interpolation correction

It is enough to consider phi in [0,pi]: reflection in the horizontal axis
changes phi to -phi, preserves the pole pair and the identity term, and
is an isometry of the seminorm. The regular increment functional has the
form

    F_phi=cos(phi)A+sin(phi)B-(1/2-eta)I,

where I(f)=f(x)-f(y) has norm one. On two adjacent phases, there are
nonnegative interpolation coefficients c,d satisfying

    (cos(phi),sin(phi))
        =c(cos(phi_j),sin(phi_j))+d(cos(phi_(j+1)),sin(phi_(j+1))),
    1<=c+d<=q.

Consequently

    F_phi=cF_(phi_j)+dF_(phi_(j+1))
                 +(c+d-1)(1/2-eta)I.

Taking norms gives the correction (q-1)(1/2-eta). Omitting this term or
using only [0,pi/2] would not prove the stated D bound.

The middle and exterior regions contain no allocated identity atoms.
Their phase costs at pi-phi may reuse those at phi: reflect the measure
in the horizontal axis and reverse its sign. This transformation preserves
all distances and feasible transport costs. Thus existing [0,pi/2] phase
tables supply M_j,E_j for the whole interval by index reflection.

Finally add the uniform small-disk bound and use the rotational conjugacy
of T_phi-I/2 to R_1^2. The setup's approximation theorem transfers the
inequality between homogeneous functions modulo constants and compact
smooth tests. All integrals at infinity are those already controlled by
the middle and exterior proofs.

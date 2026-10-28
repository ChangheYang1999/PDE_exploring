# Lattice witnesses on components of a closed cut set

## Statement

Use the operators, real homogeneous Holder space and compact-test
approximation theorem in ../../01_setup/PROOF.md. Let 0<alpha<1 and let
Z be a nonempty closed subset of R^2. Define

    h_Z(z)=2^(alpha-1) dist(z,Z)^alpha.

On each connected component O of R^2 minus Z, choose a real function F_O
with Holder seminorm at most one on O. The constant formal choices
F_O=+infinity or F_O=-infinity are also allowed and mean f=+h_Z or -h_Z
there. For finite F_O set

    f(z)=max(-h_Z(z),min(h_Z(z),F_O(z))) on O,
    f(z)=0 on Z.

Then f is continuous and [f]_alpha<=1. Put x=(1/2,0), y=-x. If

    dist(x,Z)>=1/2, dist(y,Z)>=1/2,
    F_{O_x}(x)<=-1/2, F_{O_y}(y)>=1/2,

where the formal constant choices are interpreted in the usual order,
then f(x)=-1/2 and f(y)=1/2. For every real phi,

    D_alpha >= |pv integral_R2 [K_phi(z-x)-K_phi(z-y)]f(z) dz|+1/2,

where K_phi=cos(phi)K_xx+sin(phi)K_xy and the principal value removes
centered disks about both poles. The value integral must be separately
evaluated and certified before any numerical lower bound is claimed.

## Complete proof

The distance to a nonempty closed set is1-Lipschitz, and the alpha power
of any nonnegative1-Lipschitz function has Holder seminorm at most one.
Thus [h_Z]_alpha<=2^(alpha-1)<=1. Minimum and maximum preserve the bound
one on any common domain, by comparing both input values at two points
and then interchanging the points. The clamp therefore has seminorm at
most one on each component. It also satisfies |f|<=h_Z.

If p and q belong to different components, their connecting segment
meets Z; otherwise that segment would connect the two points inside the
complement. Pick w in Z on this segment. Then

    dist(p,Z)+dist(q,Z)<=|p-w|+|w-q|=|p-q|.

Concavity of t^alpha gives

    |f(p)-f(q)|<=2^(alpha-1)(dist(p,Z)^alpha+dist(q,Z)^alpha)
                 <=(dist(p,Z)+dist(q,Z))^alpha<=|p-q|^alpha.

If one point belongs to Z, the same result follows from
|f(p)|<=2^(alpha-1)dist(p,Z)^alpha. Together with the within-component
bound this proves the global seminorm estimate and continuity, including
at every point of Z. This argument also covers the formal constant
choices, whose clamps are simply +/-h_Z.

The distance assumptions give h_Z(x),h_Z(y)>=1/2. The input constraints
therefore imply f(x)<=-1/2 and f(y)>=1/2. At this step equality does not
follow from the clamp alone when h_Z is larger than1/2. Instead the
already proved global bound and |x-y|=1 give

    1<=f(y)-f(x)<=1.

This forces both pole values to be exactly the stated numbers.

Fix z0 in Z. Since dist(z,Z)<=|z-z0|, f grows at most as a fixed multiple
of (1+|z|)^alpha. The kernel difference decays as |z|^-3, so its product
with f is absolutely integrable at infinity for alpha<1. At a pole,
subtract the value of f at that pole from its singular kernel term.
The resulting absolute integral converges for alpha>0, and the removed
constant has zero integral on every centered annulus. This defines the
stated principal value and identifies it with the increment Lambda_phi(f)
of T_phi.

Both T_phi-I/2 and T_phi+I/2 have norm D_alpha: the first is a rotation
conjugate of R_1^2, and the second is the negative of T_{phi+pi}-I/2.
Their increments on f are Lambda_phi(f)+1/2 and Lambda_phi(f)-1/2.
The larger absolute value is |Lambda_phi(f)|+1/2. The seminorm bound on f
proves the result. The fixed-increment approximation theorem in the
setup yields the same lower bound from real compact smooth tests.

## Scope and dependencies

No boundedness, regularity or finite-component assumption on Z is needed.
Nonemptiness makes the distance finite and supplies the growth bound.
This generalizes the half-plane construction. It does not prove that a
particular cut set or family F_O improves a previous numerical result.
The only dependencies are the setup theorem and elementary distance,
power and lattice inequalities proved above. The construction was
proposed in the addendum to the lead's Note12 and independently audited
here. Source and dated verdict are stored in verification/.

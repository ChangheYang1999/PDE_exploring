# Exactly which local phases attain the summed angular bound

## Statement and conventions

For 0<alpha<1 let x=(1,0), y=(0,0), R=1/2 and

    K_phi(h)=cos(2 arg(h)-phi)/(2 pi |h|^2),
    L_phi(f)=pv integral_(B(x,R)) K_phi(z-x) f(z) dz
             -pv integral_(B(y,R)) K_phi(z-y) f(z) dz,
    U(alpha)=2 a2(alpha) R^alpha/alpha,
    a2(alpha)=2^(1+alpha/2)/(pi(alpha+2)).

The principal values have circular holes at the two poles. Equivalently,
subtract f(x) and f(y) in their respective integrals. The norm is over
real functions on R^2 with Euclidean homogeneous Holder seminorm at
most one, modulo constants. Then

    ||L_phi|| <= U(alpha),
    ||L_phi|| = U(alpha) if and only if cos(phi)=0.          (1)

In particular the inequality is strict at every sampled phase
0, pi/4 and 11pi/32, and is an equality at pi/2. The strict gaps at the
first three phases are not numerically identified by this theorem.
The statement concerns only the own-pole local functional, without cross
kernels and without identity atoms.

## Reduction and attainment

Reflection in the horizontal axis conjugates L_phi to L_(-phi), and
L_(phi+pi)=-L_phi. Their norms agree. It is therefore enough to consider
0<=phi<=pi/2. The exact angular reflection lemma gives the upper bound U.

Normalize f(0)=0. The Holder unit ball is compact in local uniform
convergence: its members have |f(z)|<=|z|^alpha and share a common
modulus of continuity on every compact disk. For any epsilon>0 the
functional with both radius-epsilon pole disks removed is continuous
on this ball. The norm of the omitted part is at most
2a2 epsilon^alpha/alpha, uniformly in f. Thus L_phi is continuous and
attains its norm, after changing the sign of f if needed.

## The four forced values

Suppose 0<=phi<pi/2 and L_phi(f)=U. The two nonnegative radial deficits
in the one-circle angular bound have zero integral. Their continuity
for positive radii implies equality in both circle bounds for every
0<r<1/2. In the angular reflection proof, every paired Holder deficit
has nonnegative integrand. Continuity forces equality at any pair with
positive angular density, and also at the half-lobe endpoint by a
one-sided limit.

The directions pi and zero are inside the positive angular lobes,
since cos(phi)>0. Their reflections across the adjacent zero rays give

    p=x-r e1,                  q=y+r e1,
    a=x+r(-sin(phi),cos(phi)),
    b=y+r(sin(phi),-cos(phi)).

For p the zero ray has angle3pi/4+phi/2, and its reflected direction is
pi/2+phi. For q the zero ray has anglephi/2-pi/4, and its reflected
direction is phi-pi/2. These are the relevant half-lobe reflections
throughout 0<=phi<pi/2. At phi=0 use the endpoint limit just described.

The x-pole kernel is positive at p and negative at a. The y-pole
functional has the opposite sign, hence is positive at b and negative
at q. Set

    d_phi=sqrt(2-2sin(phi))>0.

The forced equalities are

    f(p)-f(a)=(r d_phi)^alpha,
    f(b)-f(q)=(r d_phi)^alpha.

On the other hand,

    |p-q|=1-2r,
    |a-b|=sqrt(1-4r sin(phi)+4r^2).

The Holder bounds between the cross-disk pairs therefore imply

    (1-4r sin(phi)+4r^2)^(alpha/2)
        >= f(b)-f(a)
        >=2(r d_phi)^alpha-(1-2r)^alpha.                  (2)

Let r increase to1/2. The left side tends to d_phi^alpha and the
right side to2^(1-alpha)d_phi^alpha. Since d_phi>0 and alpha<1, (2)
is impossible. Attainment of the local norm now proves strictness.

## The phase pi/2

Let Z be the union of the horizontal axis and the two vertical lines
through x and y. Set

    sigma(z)=sign(z2) sign(z1(z1-1)),
    f(z)=2^(alpha-1) sigma(z) dist(z,Z)^alpha

off Z, and f=0 on Z. The sign is constant on each component of the
complement. The segment joining points with opposite signs crosses Z;
concavity gives 2^(alpha-1)(a^alpha+b^alpha)<=(a+b)^alpha. For points
with the same sign use the one-Lipschitz property of distance and
|a^alpha-b^alpha|<=|a-b|^alpha. Thus [f]_alpha<=1.

Inside B(x,1/2), the nearest vertical line is z1=1 and the sign is that
of (z1-1)z2. Inside B(y,1/2), the nearest vertical line is z1=0 and the
sign is minus that of z1 z2. The two restrictions are precisely the
positive and negative exact angular reflection profiles for sin(2theta).
Each radial integral attains a2 R^alpha/alpha. This proves equality
at phi=pi/2, and the reduction proves all of (1).

## Dependencies and status

Dependencies are the exact one-circle reflection lemma in
../../../02_upper_bounds/PROOF.md, elementary compactness, and the
signed-distance proof included above. No computation or literature
formula is used. The phase-zero quantitative refinement in the sibling
quantitative_gap directory is separate.

Status at creation: OPEN pending independent lead cross-read.

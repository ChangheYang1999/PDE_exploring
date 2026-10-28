# Real and complex inputs for the Beurling transform

## Statement and conventions

Fix 0<alpha<1. For a complex-valued function on R^2=C use the Euclidean
modulus seminorm

    [f]_alpha=sup_(z!=w) |f(z)-f(w)|/|z-w|^alpha.

The homogeneous space is taken modulo complex constants. Write

    S=T_xx+i T_xy,
    K_S(z)=1/(2pi conjugate(z)^2),
    B f=-(1/pi) pv integral_C f(w)/(z-w)^2 dA(w).

Principal values are circular. For inputs that grow at infinity, the
operators are defined by convergent increments modulo constants, as in
../01_setup/PROOF.md, using the complex modulus for estimates. Define

    M_alpha=||S||_(complex dot C^alpha -> complex dot C^alpha),
    B_alpha^complex=||B||_(complex dot C^alpha -> complex dot C^alpha),
    B_alpha^real=||B||_(real dot C^alpha -> complex dot C^alpha).

The same constants result from suprema over compact smooth inputs of
the indicated scalar type. Then B_alpha^complex=2 M_alpha and
B_alpha^real=2 C_alpha. The individual real-kernel operators T_xx,T_xy
and R_1^2 have the same norms on real and on complex inputs, namely
C_alpha,C_alpha,D_alpha.

For every 0<alpha<1 the following explicit bounds hold:

    16^(-alpha)(1/alpha-1/18) <= M_alpha <= A(alpha),        (1)

    A(alpha)=2^(-3alpha/2)/alpha+(3/2)^alpha/18
               +2 log(6)+16*2^alpha/[9(1-alpha)].

Consequently

    lim_(alpha->0+) alpha M_alpha=1,
    lim_(alpha->0+) alpha B_alpha^complex=2,
    lim_(alpha->0+) B_alpha^complex/B_alpha^real=pi/2.      (2)

The final limit uses the independently proved sharp real-input
asymptotic alpha C_alpha -> 2/pi. Thus equality of the real-input and
complex-input Beurling norms is false. In particular, the certified
C_(1/10)<=6.87717 and (1) imply

    B_(1/10)^real <=13.75434 <179/12 <B_(1/10)^complex.     (3)

Bound (1) is only intended to prove the sharp small-alpha coefficient
and the scalar-type distinction. It is not offered as an optimized
finite-exponent Beurling upper bound.

## Complexification of an individual real-kernel operator

Let T be any of T_xx,T_xy,R_1^2. For each complex f and each fixed output
increment choose a real phase gamma making that increment real and
nonnegative after multiplication by exp(-i gamma). Since T has real
kernel and real local term,

    |Tf(x)-Tf(y)|
      = T Re(exp(-i gamma)f)(x)-T Re(exp(-i gamma)f)(y).

The projected real input has seminorm at most [f]_alpha. The real
operator bound therefore proves the same complex operator bound. The
opposite norm inequality follows by restricting to real inputs.

This argument applies to each real-kernel operator separately. It does
not apply to S or B, whose kernels are complex. Instead the exact
identity

    S f=-(1/2) conjugate(B conjugate(f))

gives B_alpha^complex=2 M_alpha. On real inputs the output phase
projection of S is cos(gamma)T_xx+sin(gamma)T_xy. Each such scalar
operator is rotation-conjugate to T_xx. Taking the suprema over phases,
inputs and evaluation pairs yields B_alpha^real=2 C_alpha.

## The upper estimate

By translation and dilation it suffices to bound the increment between
x=(1/2,0) and y=-x. Set delta=1/4. Fix the representative f(0)=0 and
assume [f]_alpha<=1. Decompose the plane into the two radius-delta pole
disks, their complement inside B(0,1), and the exterior of B(0,1).

On a circle of radius r about either pole, the own-kernel angular
functional is

    I(r)=(1/(2pi)) integral_0^(2pi)
                   exp(2i theta) f(p+r exp(i theta)) dtheta.

Rotation of theta by pi/2 reverses exp(2i theta). Hence

    I(r)=(1/(4pi)) integral_0^(2pi) exp(2i theta)
          [f(p+r exp(i theta))-f(p+r exp(i(theta+pi/2)))] dtheta,
    |I(r)| <= (1/2)(sqrt(2)r)^alpha.

The constant value f(p) cancels exactly. Integrating dr/r on
(0,delta) and adding the two disks costs at most

    (sqrt(2)delta)^alpha/alpha=2^(-3alpha/2)/alpha.         (4)

The two smooth other-pole terms combine by central reflection into

    - integral_(B(x,delta)) K_S(z-y)[f(z)-f(-z)] dA(z).

On this disk |z-y|>=1-delta and |2z|<=1+2delta. Its absolute value is
at most

    delta^2(1+2delta)^alpha/[2(1-delta)^2]
      =(3/2)^alpha/18.                                   (5)

For the remaining region inside B(0,1), the normalization gives |f|<=1.
Bound the absolute increment kernel by the sum of its two kernels.
For each pole the region lies in the annulus delta<=|z-p|<=3/2.
Since |K_S(z-p)|=1/(2pi|z-p|^2), the total cost is at most

    2 log((3/2)/delta)=2 log(6).                           (6)

Finally, in complex notation the increment kernel is the conjugate of
G(z)=z/[pi(z^2-1/4)^2]. It is odd under z->-z, and

    |G(z)|<=r/[pi(r^2-1/4)^2], r=|z|.

Central reflection replaces f by (f(z)-f(-z))/2 on the exterior.
Since this difference has magnitude at most (2r)^alpha, the tail is
bounded by

    2^alpha integral_1^infinity r^(alpha+2)/(r^2-1/4)^2 dr
      <=16*2^alpha/[9(1-alpha)].                         (7)

All tail integrals converge for alpha<1. The local bounds prove the
principal-value convergence for alpha>0. Summing (4)-(7) proves the
upper estimate in (1). In particular limsup alpha M_alpha<=1.

## A compact complex cusp with a controlled seminorm

Fix rho=1/4 and define the nonnegative radial tent

    t(z)=max(0,min(|z|,rho-|z|)).

It is 1-Lipschitz, is supported in the closed radius-rho disk, and obeys
t(z)<=|z|. Set

    F(z)=(1/2)t(z)^alpha exp(-2i arg z), z!=0,
    F(0)=0.

This compactly supported function is continuous. We prove

    [F]_alpha<=2^alpha.                                  (8)

Take two points at distance d, and put T=max(t(z),t(w)). If T=0 there
is nothing to prove. If d>=T/2, the triangle inequality gives
|F(z)-F(w)|<=T^alpha<=2^alpha d^alpha.

Suppose d<T/2. Along the segment joining the two points, the tent is
at least T-d>0, so the segment avoids the origin and the boundary of
the support. The tent is piecewise smooth there. The differential norm
of exp(-2i arg z) is 2/|z|. Since t<=|z|, the product rule gives almost
everywhere along the segment

    ||DF|| <= (1/2)(alpha+2)t^(alpha-1)
             <=(1/2)(alpha+2)(T-d)^(alpha-1).

The function is locally Lipschitz on that segment, including a possible
crossing of the tent's middle circle, so integration of this bound gives

    |F(z)-F(w)|/d^alpha
      <=(1+alpha/2)(d/(T-d))^(1-alpha)
      <=1+alpha/2 <=2^alpha.

The last inequality follows from exp(alpha log2)>=1+alpha log2 and
log2>1/2. This proves (8) without an angular discretization or an
unproved estimate for a complex extension.

## The two-pole lower bound

Set

    f(z)=F(z-x)-F(z-y).

The two support disks are disjoint. In one support disk, or when one
point is outside both disks, the global bound (8) for that summand
applies. For points in different disks, their distance is at least
1-2rho=1/2, whereas

    |f(z)-f(w)| <= (rho/2)^alpha=(1/8)^alpha.

That quotient is at most (1/4)^alpha<=2^alpha. Points outside both
disks have zero values. Thus [f]_alpha<=2^alpha.

At its own pole, the phase of F cancels the phase of K_S. The two own
contributions to Sf(x)-Sf(y) therefore have positive real sum

    integral_0^rho t(r)^alpha dr/r
      >=integral_0^(rho/2) r^(alpha-1) dr
      =(rho/2)^alpha/alpha.                              (9)

Each other-pole kernel has magnitude at most
1/[2pi(1-rho)^2] on a support disk. Also |F|<=(1/2)(rho/2)^alpha.
The sum of the absolute cross contributions is consequently at most

    rho^2(rho/2)^alpha/[2(1-rho)^2]
       =(rho/2)^alpha/18.                                (10)

The reverse triangle inequality, (9) and (10), followed by division by
the upper bound 2^alpha for [f]_alpha, proves

    M_alpha >=(rho/4)^alpha(1/alpha-1/18)
              =16^(-alpha)(1/alpha-1/18).

The lower expression is positive throughout 0<alpha<1. This proves
liminf alpha M_alpha>=1 and hence (2).

To check the entirely rational comparison in (3), at alpha=1/10 the
complex Beurling lower bound is (179/9)2^(-2/5). Since
2^(-2/5)>3/4, equivalently 4<(4/3)^5=1024/243, this exceeds179/12.
The cited scalar upper endpoint gives B^real<=2*6.87717=13.75434,
which is smaller than179/12.

## Compact smooth inputs and the homogeneous extension

For the lower bound it already suffices to mollify the compact Holder
function f above with a nonnegative compactly supported smooth kernel
of integral one. Convolution does not increase its complex modulus
seminorm. The smooth transforms converge at the fixed increment: near
each pole subtract the corresponding point value and dominate by a
constant times r^(alpha-2); away from the poles use uniform convergence
and the common compact support. This proves the same lower bound for
the original compact-smooth test supremum.

For completeness, compact-smooth and homogeneous operator norms agree
also for complex inputs. Normalize a homogeneous input by f(0)=0. The
metric projection P_M of C onto its closed radius-M disk is
1-Lipschitz. Indeed, in polar coordinates squared distances are
(r-s)^2+2rs(1-cos(theta)); replacing r,s by min(r,M),min(s,M) decreases
both terms. Thus v_M=P_M(f) has seminorm at most [f], magnitude at most
M, and equals f on each fixed compact set for large M.

Choose a real cutoff chi_N, equal to one on B(0,N), zero outside
B(0,2N), with 0<=chi_N<=1 and Lipschitz constant1/N. Its seminorm is at
most N^(-alpha). Then

    [chi_N v_M]_alpha <=[f]_alpha+M N^(-alpha).

Take M->infinity and N->infinity with M N^(-alpha)->0, and mollify on a
scale tending to zero. This produces compact smooth inputs converging
locally to f, with seminorm limsup at most [f]. Their normalization at
zero and uniform seminorm control also give the uniform growth bound
needed for the kernel-difference tail. Dominated convergence on each
local-subtracted pole region and on the absolutely convergent tail
proves convergence of every fixed operator increment. This establishes
equality of the norms. No density in the full homogeneous seminorm is
asserted.

## Dependencies and scope

Dependencies are the verified kernel and rotation identities, the
small-alpha scalar theorem alpha C_alpha->2/pi, and the scalar upper
certificate C_(1/10)<=6.87717. The cusp and complex upper estimate are
proved here. No claim about a full sup-plus-Holder norm, the endpoint
alpha=1, or an exact finite-alpha complex Beurling norm is made. The
new asymptotic is an independent derivation, not an attribution to
unseen literature.

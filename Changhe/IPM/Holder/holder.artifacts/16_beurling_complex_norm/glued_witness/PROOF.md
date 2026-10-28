# Gluing the two flowers to an exterior third angular mode

## Statement and normalization

Fix 0<a<1. Let S=T_xx+i T_xy have kernel
K_S(z)=1/(2 pi conjugate(z)^2). Its norm M_a acts on complex-valued
homogeneous Holder space with seminorm

    [f]_a=sup_(z!=w) |f(z)-f(w)|/|z-w|^a,

where both moduli are Euclidean. Singular integrals use circular
principal values at each pole; growing inputs define increments modulo
constants by the convergent kernel difference. Put

    Q2=2/sqrt(2-a) ((1-a)/(2-a))^((1-a)/2),
    Q3=6/(3-a) (3(1-a)/(4(3-a)))^((1-a)/2),
    b2=2^(a-1)/Q2,   b3=2^(a-1)/Q3,
    A_a=2^(-a)/a+integral_0^(1/2) t^a/(1-t) dt.

Then

    M_a >= A_a/Q2 + 2 b3 B(a+1,1-a)
         = A_a/Q2 + 2^a a pi/[Q3 sin(pi a)].             (1)

In particular,

    liminf_(a->0+) (M_a-1/a) >= 1-(log2)/2.             (2)

The lower bound also holds for the supremum starting with compact
smooth inputs. It may be maximized with the homogeneous cubic lower
bound (a+3)/(2(1-a)Q3). No sharp finite-exponent value or matching
second term is asserted.

Dependencies: the exact angular-mode norms in
../exact_angular_modes/PROOF.md and the two-flower calculation in
../compact_flower/PROOF.md. The norm-preserving gluing and exterior
calculation are proved here.

## The normalized inner witness

Put x=1/2, y=-1/2, R=1/2 and

    tau(r)=max(0,min(r,R-r)),
    F(z)=b2 tau(|z|)^a exp(-2i arg z),   F(0)=0,
    f_in(z)=F(z-x)-F(z-y).

The cited flower proof gives [f_in]_a=1 and

    S f_in(x)-S f_in(y)=A_a/Q2.                        (3)

Each flower is supported on its own radius1/2 disk. These disks have
disjoint interiors and lie inside the closed unit disk. If z is in
one of them, set u=tau(|z-x|) or tau(|z-y|), respectively. Then

    |f_in(z)|=b2 u^a,  0<=u<=1-|z|.                   (4)

For example, in the x disk, |z|<=1/2+|z-x| gives
1-|z|>=1/2-|z-x|>=u. The same argument holds in the y disk.

## The normalized exterior witness and gluing

Define

    f_out(z)=b3 (|z|-1)_+^a exp(-3i arg z),

with value zero on |z|<=1. The radial map

    Psi(z)=(|z|-1)_+ z/|z|

is one-Lipschitz: its radial scalar is one-Lipschitz and is between
zero and |z|, so the squared-distance identity from the flower proof
applies. The exact seminorm of r^a exp(-3i theta) is 1/b3. Therefore
[f_out]_a<=1.

Let f=f_in+f_out. For pairs of points in the same support, or with
one point outside both supports, the separate norm bounds apply.
Consider the only remaining case: z is in an inner disk and |w|>1.
Put v=|w|-1. By (4),

    |z-w|>=|w|-|z|>=u+v.

The exact Qn maxima satisfy Q2,Q3>=1, so b2,b3<=2^(a-1).
Concavity now gives

    |f(z)-f(w)| <= b2 u^a+b3 v^a
                <=2^(a-1)(u^a+v^a)
                <=(u+v)^a<=|z-w|^a.

Thus [f]_a<=1. A maximizing pair in one inner disk still attains one,
so [f]_a=1. No estimate of the sum of the two seminorms is used.

## Exact exterior increment

The exterior witness vanishes in neighborhoods of x,y, so there are
no local singularities. At infinity its growth is O(r^a), and the
kernel difference is O(r^-3); hence the increment converges absolutely.
For z=r exp(i theta) with r>=1, the difference kernel is

    nu_S(z)=conjugate(z)/[pi(conjugate(z)^2-1/4)^2]
           =sum_(k>=0) (k+1) exp(i(2k+3)theta)
                         /[pi 4^k r^(2k+3)].

The expansion is uniformly absolutely convergent in its angular and
geometric factor. Multiplication by exp(-3i theta) and angular
integration leaves exactly k=0. It follows that

    S f_out(x)-S f_out(y)
      =2 b3 integral_1^infinity (r-1)^a/r^2 dr
      =2 b3 B(a+1,1-a).                               (5)

For the beta integral, substitute t=(r-1)/r. Euler's reflection formula
then gives B(a+1,1-a)=a pi/sin(pi a). The two increments (3),(5) are
positive real numbers. Adding them and using [f]_a=1 proves (1).

## Compact smooth approximation

For L>1 replace the exterior radial scalar (r-1)_+ by

    tau_L(r)=max(0,min(r-1,2L-1-r)).

It is one-Lipschitz, between zero and r, equals r-1 for 1<=r<=L,
and is at most (r-1)_+. The exterior seminorm and the cross-support
argument remain unchanged. The new glued function is compactly
supported and has seminorm one. As L tends to infinity, its exterior
increments converge by domination with (r-1)^a/r^2. Finally convolve
with positive smooth approximate identities. Seminorms do not increase,
and the fixed transform increments converge by the local Holder
cancellation and integrable tail. Thus compact smooth inputs approach
the same lower bound.

## The small-exponent conclusion

The flower proof gives A_a/Q2=1/a-(log2)/2+O(a). From the explicit
formula, b3 tends to1/2; also B(a+1,1-a) tends to1. Hence the added
term tends to1, proving (2). All limits are within0<a<1. No assertion
at the endpoint a=0 is made.

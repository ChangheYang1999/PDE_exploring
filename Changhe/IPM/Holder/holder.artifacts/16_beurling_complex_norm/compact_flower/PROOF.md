# A compact complex witness with zero cross interaction

## Statement and definitions

Let 0<a<1 and let M_a be the complex-input homogeneous Holder norm of
S=T_xx+i T_xy, whose kernel is K_S(z)=1/(2 pi conjugate(z)^2). The
seminorm is [f]_a=sup|f(z)-f(w)|/|z-w|^a, with Euclidean distance and
complex modulus. Define

    Q_a=2/sqrt(2-a) * ((1-a)/(2-a))^((1-a)/2),
    J_a=integral_0^(1/2) t^a/(1-t) dt
       =sum_(k>=0) 2^(-a-k-1)/(a+k+1).

Then

    M_a >= [2^(-a)/a+J_a]/Q_a.                          (1)

This explicit lower bound comes from a compactly supported Holder
function with exactly known seminorm. Mollification gives the same
lower bound for the supremum over compact smooth inputs. In particular,

    liminf_(a->0+) (M_a-1/a) >= -(log 2)/2.              (2)

No matching second-term upper bound is asserted. The only dependency is
the exact angular-mode seminorm in ../exact_angular_modes/PROOF.md.

## The radial contraction

For R>0 put tau_R(r)=max(0,min(r,R-r)), r>=0, and
Psi_R(z)=tau_R(|z|)z/|z| for z!=0, Psi_R(0)=0. The scalar function
tau_R is one-Lipschitz and 0<=tau_R(r)<=r. If z=r exp(i theta) and
w=s exp(i phi), then

    |Psi_R(z)-Psi_R(w)|^2
       =(tau_R(r)-tau_R(s))^2
          +2 tau_R(r)tau_R(s)(1-cos(theta-phi))
       <=(r-s)^2+2rs(1-cos(theta-phi))=|z-w|^2.

Thus Psi_R is one-Lipschitz. The flower

    F_R(z)=1/2 tau_R(|z|)^a exp(-2i arg z), F_R(0)=0,

is one half of F_(a,-2) composed with Psi_R. Its Holder seminorm is
at most A_a=2^(-a)Q_a. It is exactly A_a: a maximizing equal-radius
pair from the angular-mode theorem can be placed in 0<|z|<R/2, where
Psi_R is the identity.

## Two centers and the exact input seminorm

Choose x=1/2, y=-1/2 on the real axis, put R=1/2, and define

    f(z)=F_R(z-x)-F_R(z-y).

The interiors of the two support disks are disjoint. If two points
lie in the same disk, or one lies outside both disks, the A_a estimate
follows from the one-flower seminorm. Suppose instead z lies in the
x disk and w in the y disk. Put r=|z-x|, s=|w-y|. Then

    |z-w|>=1-r-s=(R-r)+(R-s)>=tau_R(r)+tau_R(s).

Concavity gives

    |f(z)-f(w)|<=1/2(tau_R(r)^a+tau_R(s)^a)
                 <=2^(-a)|z-w|^a<=A_a |z-w|^a,

because Q_a>=1. The lower bound A_a is attained inside either one
disk. Therefore [f]_a=A_a exactly. Tangency of the closed disks is
harmless because both flowers vanish at the tangent point.

## Vanishing of the cross terms

Each flower vanishes at its own center, so its own-kernel integral
converges absolutely there. Polar integration gives

    S(F_R(. - x))(x)=1/2 integral_0^R tau_R(r)^a dr/r.

At the other center the kernel is smooth on the support disk. For a
nonzero real d with |d|=1 and |u|<=R=1/2,

    1/(conjugate(d-u))^2
       =d^(-2) sum_(k>=0)(k+1)(conjugate(u)/d)^k.

The series converges absolutely and uniformly on the disk. Multiplying
by tau_R(r)^a exp(-2i theta) gives angular modes -(k+2), all nonzero.
Every angular integral is zero, so

    S(F_R(. - x))(y)=S(F_R(. - y))(x)=0.

Consequently

    Sf(x)-Sf(y)=integral_0^R tau_R(r)^a dr/r
       =R^a[2^(-a)/a+J_a].                             (3)

The output increment distance is one. Dividing (3) by
A_a=2^(-a)Q_a and taking R=1/2 gives (1).

## Smooth approximation and the small-exponent expansion

Convolve the compact Holder input f with positive smooth approximate
identities. The resulting functions remain compactly supported, their
seminorms are at most A_a, and their transform increments converge to
(3). This follows either from the convergent increment formula or from
commutation with convolution and continuity of Sf, already guaranteed
by the complex upper bound. Thus no density in the full seminorm is
needed.

The positive series for J_a follows by expanding 1/(1-t) and monotone
convergence. After terms k=0,...,N-1 its tail is at most

    2^(-a-N)/(a+N+1).

In a neighborhood of a=0 the defining integral and its first two
parameter derivatives are dominated by integrable powers of |log t|.
Therefore J_a=log 2+O(a), while 2^(-a)/a=1/a-log 2+O(a). The explicit
Q_a formula, or differentiation at its maximizing angle, gives
Q_a=1+(log 2)a/2+O(a^2). Substitution proves (2).

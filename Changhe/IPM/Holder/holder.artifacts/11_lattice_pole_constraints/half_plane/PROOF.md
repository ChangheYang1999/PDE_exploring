# Half-plane lattice witnesses with prescribed pole values

## Statement and conventions

Let 0<alpha<1 and use the real homogeneous Holder space, increment-defined
singular integrals and compact-test equivalence proved in
../../01_setup/PROOF.md. Its seminorm is

    [f]_alpha = sup_{p != q} |f(p)-f(q)|/|p-q|^alpha.

Put x=(1/2,0), y=-x, H={(X,Y):X>0}, and h(X,Y)=(2X)^alpha/2 on H.
Suppose F:H->R satisfies [F]_{alpha,H}<=1 and F(x)<=-1/2. Define

    f(z)=max(-h(z),min(h(z),F(z))) for z in H,
    f(z)=-f(-z) for z in -H,
    f(0,Y)=0.

Then f is continuous, [f]_alpha<=1, f(x)=-1/2, and f(y)=1/2.
For every real phi define

    K_phi(z)=[cos(phi)(z_1^2-z_2^2)+2sin(phi)z_1z_2]/(2pi|z|^4),
    nu_phi(z)=K_phi(z-x)-K_phi(z-y),
    J_phi = pv integral_H nu_phi(z) f(z) dz.

The principal value deletes a Euclidean disk centered at x. The integral
is absolutely convergent at infinity and after the constant f(x) is
subtracted from the singular K_phi(z-x) term near x. With
D_alpha=||R_1^2|| on this space and R_1^2=T_xx-I/2, one has

    D_alpha >= 2|J_phi|+1/2.

This is a theorem for every admissible F, not a certified numerical
improvement. Evaluating J_phi remains a separate task.

## Proof of the Holder bound

For nonnegative s,t, |s^alpha-t^alpha|<=|s-t|^alpha. Hence
[h]_{alpha,H}<=2^(alpha-1)<=1. The minimum or maximum of two real
functions with seminorm at most one has seminorm at most one: each input
value at p is bounded by its value at q plus |p-q|^alpha; taking the same
minimum or maximum on both sides proves one direction, and interchanging
p,q proves the other. Thus the displayed clamp has seminorm at most one
on H and obeys |f(X,Y)|<=2^(alpha-1)X^alpha.

For p in H and q in -H, concavity of the power gives

    |f(p)-f(q)| <= 2^(alpha-1)(X_p^alpha+|X_q|^alpha)
                  <= (X_p+|X_q|)^alpha <= |p-q|^alpha.

On -H the bound follows by central reflection. For q on the line X=0,
|f(p)|<=2^(alpha-1)|X_p|^alpha<=|p-q|^alpha. These inequalities prove the
global bound and continuity across the line. At x, h=1/2 and F<=-1/2,
so the clamp is -1/2. Central oddness gives the other pole value.

## Convergence, symmetry and the identity term

The clamp gives |f(z)|<=2^(alpha-1)|z|^alpha. The kernel difference
nu_phi is O(|z|^-3) at infinity by differentiating the explicit kernel;
its product with f is therefore integrable there since alpha<1.
Choose any r0<1/2. In B(x,r0), the singular integral is represented by

    integral_{B(x,r0)} K_phi(z-x)(f(z)-f(x)) dz,

plus the smooth K_phi(z-y) contribution. The first integral converges
absolutely since alpha>0. The removed constant integrates to zero on
every centered annulus because K_phi has zero angular mean. Thus the
stated principal value exists. The same argument applies at y in -H.

K_phi is even, hence nu_phi(-z)=-nu_phi(z). As f is also centrally odd,
the full increment Lambda_phi(f)=pv integral_R2 nu_phi f equals 2J_phi.
The operator T_phi with kernel K_phi is a rotation conjugate of T_xx.
Consequently T_phi-I/2 is a rotation conjugate of R_1^2 and has norm
D_alpha. The operator T_phi+I/2 also has norm D_alpha: it is the negative
of T_{phi+pi}-I/2, and phi+pi is an allowed rotation phase.

Since f(x)-f(y)=-1, the two corresponding increments are
Lambda_phi(f)+1/2 and Lambda_phi(f)-1/2. Their larger absolute value is
|Lambda_phi(f)|+1/2=2|J_phi|+1/2. Their seminorm bounds and [f]<=1 prove
the lower bound. Compact smooth approximation of this fixed increment,
as established in the setup proof, gives the same lower bound when the
operator norm is initially defined only on real C_c^infinity tests.

## Candidate family and scope

If g is any real function on H with [g]_{alpha,H}<=1 and g(x)=0, then
F=lambda*g-t is admissible for 0<=lambda<=1 and t>=1/2. The polygonal
signed-distance witnesses provide such g. The theorem also permits
other functions and all phases; it makes no claim that a particular
phase or choice of lambda,t is optimal. A bare integral without the
principal-value prescription would be ambiguous at x and should not
be used in the statement.

## Dependencies and verification

Only the setup theorem, the elementary Holder power inequality, the
lattice inequality proved above and rotation invariance are used. The
lead proposed this construction in Note12 at2026-10-28T05:01Z. Its
statement was independently checked in the independent verifier. The dated
verification record and source snapshot are in verification/.

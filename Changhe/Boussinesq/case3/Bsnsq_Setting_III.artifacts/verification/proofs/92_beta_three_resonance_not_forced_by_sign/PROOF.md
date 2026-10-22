# Positive leading angular data do not force the beta-three logarithm

Written 2026-10-21T00:09:27.133385+00:00. Complete informal calculation written before the independent Cartesian check. This is a statement about leading angular data and the finite transport recursion. These data are not exact B2 profiles, and no existence conclusion follows.

## 1. Exact statement

At beta=3 put s=m=1/3, k0=5/3 and k1=4/3. For real parameters a>0, h>|d|, define on the punctured plane

    omega0=r^-1/3 a cos(theta),
    theta0=r^1/3 cos(theta)^2 [h+d sin(theta)],
    Psi0=-(9a/16)r^5/3 cos(theta),   u0=(-Psi0_y,Psi0_x).

The canonical homogeneous inverse of omega0 is u0. The fields are smooth off zero, odd/even in x as required, omega0 is strictly positive on x>0, and theta0 is strictly positive off the vertical axis and vanishes quadratically on that axis. Define the formal finite recursion below. Its identification with actual profile tail coefficients uses packets90-91; this calculation rechecks the displayed recursion and does not reprove that asymptotic theorem,

    omega1=u0.grad omega0-partial_x theta0,
    theta1=u0.grad theta0,
    u1=K_rel omega1,
    omega2=(u0.grad omega1+u1.grad omega0-partial_x theta1)/2.

The first cosine coefficient of r omega2 is exactly

    alpha=-3a(27a^2-41d)/320.                            (1)

The coefficient is independent of h. For any a>0, choosing d=27a^2/41 and any h>d gives alpha=0. In particular a=h=1 and d=27/41 satisfy every stated positivity, parity and smoothness property, with alpha=0. With a=h=1, d=0 gives alpha=-81/320 and d=4/5 gives alpha=87/1600. Thus these leading angular sign conditions alone force neither a nonzero resonance nor a prescribed sign. Whether the cancellation can occur for an exact global profile is OPEN. The center conditions and global transport equations have not been imposed on these data.

## 2. Leading inverse and exact second coefficients

For a source r^-1/3 a cos(theta), solving -(f''+(5/3)^2 f)=a cos(theta) gives f=p cos(theta), p=-9a/16. This is the unique periodic angular inverse because5/3 is not an integer. Its relative whole-plane inverse converges absolutely at the subtraction point since1/3<1, at the evaluation singularity off0, and at infinity by the relative kernel cancellation. The homogeneous stream supplies its negative curl and divergence, and the homogeneous growth and centering give equality, as in packet03.

Write c=cos(theta), t=sin(theta), A1=r^2/3 omega1 and H1=theta1. Direct polar differentiation with u0_r=-r^2/3 f' and u0_theta=(5/3)r^2/3 f gives

    A1=k0 f(a c)' + s f'(a c) - m c H0 + t H0',
    H1=k0 f H0' - m f' H0,
    H0=c^2(h+d t).

Using elementary angle identities and Q=9a^2/16-d/3, these expressions are

    A1=Q sin(2theta) -(3h/4)cos(theta)+(5h/12)cos(3theta)
                                                    +(d/3)sin(4theta),
    H1=p[-3h c^2 t -3d c^2 t^2 +(5d/3)c^4].           (2)

The first equation can be checked before converting to Fourier form: its advective part is(9a^2/8)c t, and its temperature part is

    -(h/3)c^3-2h c t^2 +(2d/3)c^3 t-2d c t^3.

The second stream is r^4/3 g(theta), where solving -(g''+k1^2 g)=A1 term by term gives

    g=(9Q/20)sin(2theta)+(27h/28)cos(theta)
                           +(3h/52)cos(3theta)+(3d/128)sin(4theta). (3)

Its relative inverse converges by the same argument with source degree-2/3. Neither inverse admits a free harmonic strain.

## 3. Extraction of the resonance

Packet90's direct polar identity, which also follows immediately by differentiating the fields above, is

    2 r omega2 = k0 f A1' + 2s f' A1
                         + k1 g(a c)' + s g'(a c) + t H1'.       (4)

The coefficient multiplying c H1 is absent because m-s=0. Only the sin(2theta) terms of A1 and g can contribute to the first cosine through the first four terms in(4). Products with cos(theta) and sin(theta) change angular frequency by one; the other cosine modes contribute sine modes, and the sin(4theta) terms contribute cosine modes3 or5. Their first-cosine contributions, using(2)-(3), are respectively

    (k0-s)p Q=(4/3)p Q,
    (-k1/2+s)a(9Q/20)=-3aQ/20.

Their sum is -9aQ/10. For the last term, the d-dependent even part of H1 is

    p d[1/4+(5/6)cos(2theta)+(7/12)cos(4theta)].

The h-dependent odd part has a derivative even in theta, so multiplication by t yields an odd function with no cosine coefficient. The first cosine coefficient of t H1' is therefore -5p d/6=15a d/32. Dividing the sum in(4) by2 yields

    alpha=(-9aQ/10+15a d/32)/2
          =-81a^3/320+123a d/320,

which proves(1) and all three exact examples.

## 4. Scope and relation to the logarithmic theorem

For an exact class A beta3 profile, packet91 proves a logarithmic velocity and fourth scalar corrections when alpha!=0. The examples here show why that theorem must remain conditional when only leading positivity and symmetry are used. They do not refute a possible additional constraint from the global PDE, center relations, inverse self-consistency at finite radii, or source geometry. No solution is constructed by assigning omega1 and omega2 through a finite recursion. The leading fields are singular at zero and are used only as exterior homogeneous coefficients. All claimed equalities are elementary finite Fourier identities with the canonical homogeneous inverse. No formal proof assistant or numerical certification is involved.

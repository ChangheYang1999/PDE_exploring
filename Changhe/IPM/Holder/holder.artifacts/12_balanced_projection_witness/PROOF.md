# A continuous projection witness with a radial bias

## Proved statement and open step

Let 0<alpha<=2/3, a>0, x=(1/2,0), y=-x. Put
b(Y)=1/2+(|Y|-a)_+/sqrt(3), and let Gamma be the union of the two
piecewise linear graphs X=+/-b(Y). Let s(z) be signed distance to Gamma,
negative in the strip |X|<b(Y) and positive outside. Define

    P(z)=2|s(z)Y|/sqrt(s(z)^2+Y^2),
    Psi(z)=(1/2)sgn(s(z)Y) P(z)^alpha,
    h(z)=(1/2)(|z-x|^alpha-|z-y|^alpha),
    f(z)=h(z)+Psi(z).

Set P=0 at x,y. These formulas define continuous real functions on R^2.
For the Euclidean homogeneous Holder seminorm,

    [Psi]_alpha <= 1,    [h]_alpha <= 1,    [f]_alpha <= 2.

The function f is centrally odd and f(x)=-1/2, f(y)=1/2. It grows no
faster than a constant times |z|^alpha, so its singular-integral increments
exist under the normalized operator definition of ../01_setup/PROOF.md.

If an independent argument proves [f]_alpha<=K, with any positive K,
then the exact rotated diagonal lower bound is

    D_alpha >= (sqrt(J^2+[alpha/(2(alpha+2))]^2)+1/2)/K,
    J = integral_R2 (K_xy(z-x)-K_xy(z-y)) Psi(z) dz.

The principal values and convergence are understood as below. The universal
choice K=2 is proved here. A sharper bound for this particular f is an OPEN
step, and a numerical estimate of K does not certify the displayed lower
bound with that numerical K. No claim of improvement over earlier bounds
is made in this file.

## Complete proof of the stated bounds

Signed distance to Gamma is1-Lipschitz. For points on the same side this
is the ordinary distance inequality. For opposite sides the connecting
segment crosses Gamma, and the sum of the two distances to Gamma is at
most the segment length. Hence z -> (s(z),Y) is sqrt(2)-Lipschitz.
The function d(u,v)=2|uv|/sqrt(u^2+v^2) is2-Lipschitz on each quadrant:
its gradient there has components2v^3/r^3 and2u^3/r^3 up to signs, so its
length is at most2. Continuity and subdivision of a segment at the axes
give the same global Lipschitz constant. Thus P is2sqrt(2)-Lipschitz.

Write Z=Gamma union {Y=0}. Since
P(z)<=2min(|s(z)|,|Y|)=2dist(z,Z), opposite signs of sY give

    |Psi(p)-Psi(q)|
      <= 2^(alpha-1)(dist(p,Z)^alpha+dist(q,Z)^alpha)
      <= (dist(p,Z)+dist(q,Z))^alpha <= |p-q|^alpha.

The middle inequality is concavity of t^alpha, and the last one follows
because the segment crosses Z. For equal signs,

    |Psi(p)-Psi(q)| <= (1/2)|P(p)-P(q)|^alpha
                     <= 2^(3alpha/2-1)|p-q|^alpha <= |p-q|^alpha.

This includes zero values by continuity. Each distance power in h has
seminorm at most one, so [h]<=1 by the triangle inequality, and [f]<=2.
The function s is even in X and Y, so Psi is even in X and odd in Y.
The function h is odd in X and even in Y. Their sum is centrally odd.
At the poles Psi vanishes and the stated values follow from |x-y|=1.

For the lower bound, use the normalized kernel
K_phi=cos(phi)K_xx+sin(phi)K_xy and T_phi its operator. Parity makes the
cross pairings vanish: the K_xy increment applied to h and the K_xx
increment applied to Psi are zero. Solving the radial Poisson equation,

    (-Delta)^(-1)|z|^alpha = -|z|^(alpha+2)/(alpha+2)^2

up to irrelevant harmonic normalization gives

    T_xx |z|^alpha = -alpha |z|^alpha cos(2theta)/(2(alpha+2)).

This formula follows by differentiating explicitly and adding |z|^alpha/2.
The homogeneous increment definition gives the same result; the difference
of two translated powers has sufficient decay for this calculation.
Consequently (T_xx h)(x)-(T_xx h)(y)=alpha/(2(alpha+2)). Thus

    ((T_phi-I/2)f)(x)-((T_phi-I/2)f)(y)
       = cos(phi)alpha/(2(alpha+2))+sin(phi)J+1/2.

Maximizing over phi gives the claimed expression. Every T_phi-I/2 is a
rotation conjugate of R_1^2. Divide by the proven or independently supplied
K, and use the compact approximation theorem in the setup if compact smooth
test functions are desired. Locally the Holder differences remove the
principal-value singularities. At infinity the kernel difference is
O(|z|^-3), while f=O(|z|^alpha), so the integral converges for alpha<1.

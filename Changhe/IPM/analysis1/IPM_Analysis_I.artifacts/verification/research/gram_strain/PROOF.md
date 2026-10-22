# Canonical strain in the diagnostic H1m space

## Statement and definitions

Fix L>0 and 0<k<1/2. Write r=|(x,y)| and

    m(r)=(r/L)^3(1+r^2/L^2)^((k-3)/2),
    w(r)=m(r)^(-2)(1+r^2/L^2)^(-3/2).

Let X consist of locally integrable real functions modulo equality almost
everywhere, with locally square integrable weak gradient and finite norm

    ||h||_X^2=integral_R2 [h^2+r^2|grad h|^2]w(r) dX.

Define the linear functional

    Sigma(h)=(1/pi) integral_R2 h(r,theta) sin(3theta)/r^3 dX.       (1)

The integral converges absolutely for every h in X. Its zeroth-order
Cauchy-Schwarz bound is C0=1/[L^2 sqrt(pi(1-2k))]. Using the angular
derivative gives the stronger bound

    |Sigma(h)| <= Cang ||h||_X,
    Cang=1/[L^2 sqrt(10pi(1-2k))].                              (2)

Cang is an upper bound, not a claimed sharp X-dual norm. For a density h
with the regularity and canonical hypotheses stated below, Sigma(h)
equals psi[h]_xy(0) for -Delta psi[h]=h_x and U[h]=(-psi_y,psi_x).
Thus the prompt's speed variation c[h]=Sigma(h)/3 has bound Cang/3.
The lead's raw-strain convention uses Sigma, without that division.

Let D={h in X:h=x^2 y a_h near0 with a_h continuous near0}, and let
j(h)=a_h(0). For every real s and every h in D with Sigma(h)=s, every
real c is attainable by a sequence h_epsilon in D such that

    Sigma(h_epsilon)=s, j(h_epsilon)=c,
    ||h_epsilon-h||_X ->0.                                    (3)

Consequently, fixing the bounded strain functional does not restore
continuity of the central density coefficient. This is a function-space
statement, not a near-kernel or nonlinear IPM assertion.

## Absolute integrability and the bound

Algebra gives

    1/w=(r/L)^6(1+r^2/L^2)^(k-3/2).

Since integral_0^(2pi) sin^2(3theta) dtheta=pi,

    integral_R2 sin^2(3theta)/(r^6 w) dX
      =pi L^(-6) integral_0^infinity r(1+r^2/L^2)^(k-3/2) dr
      =pi/[L^4(1-2k)].                                       (4)

For the last equality put z=1+r^2/L^2, so r dr=L^2 dz/2.
The exponent k-3/2 is strictly less than -1. The primitive
z^(k-1/2)/(k-1/2) tends to0 at infinity. Cauchy-Schwarz applied to
|h| sqrt(w) and |sin(3theta)|/(r^3 sqrt(w)) proves absolute
convergence of(1) and the bound C0 using just the h^2 term of X.

For almost every r>0, let

    h3(r)=(1/pi) integral_0^(2pi) h(r,theta)sin(3theta) dtheta.

Local H1 on compact annuli implies the angular weak integration-by-parts
identity

    integral h_theta cos(3theta) dtheta=3pi h3(r).

For completeness, approximate on each compact annulus by smooth functions
in H1, use Fubini to extract a subsequence converging in angular H1 for
almost every radius, and pass the smooth identity to the limit. A countable
exhaustion gives the identity for almost every positive r. The weight is
bounded above and below on such annuli, so the local argument applies to X.
Cauchy-Schwarz on the circle now gives

    integral h^2 dtheta >= pi h3^2,
    integral h_theta^2 dtheta >= 9pi h3^2.

In polar coordinates r^2|grad h|^2=(r h_r)^2+h_theta^2. Hence

    ||h||_X^2 >=10pi integral_0^infinity h3(r)^2 w(r) r dr.

By absolute convergence Sigma(h)=integral_0^infinity h3(r)r^(-2) dr.
A second Cauchy-Schwarz inequality, with radial dual integral

    integral_0^infinity 1/(r^5 w(r)) dr=1/[L^4(1-2k)],

proves(2). No radial derivative has been used to improve the constant.
The condition k<1/2 is used in this dual integral. No assertion about
boundedness or unboundedness of the full X-dual at other k is made here.

## Identification with the canonical central strain

For this identification assume h is C2 locally, even in x and odd in y,
with |h|+r|grad h|=O(r^3) near0 and O(r^gamma) at infinity for some
gamma<1. Assume its canonical Poisson solution exists, is C2 near0,
and has sublinear velocity, excluding the added xy harmonic strain.
These are hypotheses for the identification, not an existence theorem
for the inverse on every member of X.

Let f1(r)=(1/pi) integral h_x(r,theta)sin(2theta) dtheta. Its canonical
mode is

    psi1(r)=[r^(-2) integral_0^r u^3 f1(u)du
                 +r^2 integral_r^infinity f1(u)/u du]/4.       (5)

Direct differentiation proves
-(psi1''+psi1'/r-4psi1/r^2)=f1. The alternative homogeneous modes r^-2
and r^2 are excluded respectively by regularity at0 and sublinear
velocity. Since f1=O(r^2) at0 and O(r^(gamma-1)) at infinity, all
integrals converge. Dividing(5) by r^2 and taking r down to0 gives
one quarter of integral f1/r. The C2 quadratic Taylor projection of
psi onto sin(2theta) has coefficient psi_xy(0)/2, because
r^2 sin(2theta)=2xy. Therefore

    psi_xy(0)=(1/2) integral_0^infinity f1(r)/r dr
              =(1/pi) integral_R2 h_x xy/r^4 dX.

Integrating by parts on epsilon<r<R yields

    -(partial_x(xy/r^4))=y(3x^2-y^2)/r^6
                           =sin(3theta)/r^3.

The boundary integrals are O(epsilon^2) and O(R^(gamma-1)), so both
vanish. This proves the sign and normalization in(1). It also avoids
assuming any convergence of an infinitely differentiated angular series.
The sign agrees with topic80's canonical correction; it is independently
derived here. A finite annulus requires its boundary term and cannot use
this whole-plane identity unchanged.

## Central variation at exactly fixed strain

Put p=x^2y and b_epsilon=p(1-r^2/epsilon^2)_+^6 for0<epsilon<=L.
This is C5, compactly supported, has the required density parity, and
j(b_epsilon)=1. A direct norm calculation is included to avoid using
unproved small-support scaling. With chi(t)=(1-t^2)^6 on[0,1],

    ||b_epsilon||_X^2=(pi/8)L^6 epsilon^2 integral_0^1
       t(1+(epsilon t/L)^2)^(3/2-k)
       [15chi^2+6t chi chi'+t^2 chi'^2]dt.

The bracket is 6chi^2+(3chi+t chi')^2. The positive weight is at most
2^(3/2-k)<3. Direct polynomial integration gives

    integral t chi^2 dt=1/26,
    integral t^2 chi chi' dt=-1/26,
    integral t^3 chi'^2 dt=12/143,

so the bracket integral is123/286. Since pi<4,

    ||b_epsilon||_X^2 <=(369pi/2288)L^6 epsilon^2
                       < L^6 epsilon^2.                     (6)

The angular identity cos^2(theta)sin(theta)=(sin(theta)+sin(3theta))/4
and(1) give the exact strain

    Sigma(b_epsilon)=(1/4) integral_0^epsilon
               r(1-r^2/epsilon^2)^6 dr=epsilon^2/56.           (7)

Let g=b_L-b_(L/2). Then j(g)=0, Sigma(g)=3L^2/224 and
||g||_X<(3/2)L^4 by(6). Set

    q_epsilon=b_epsilon-[4epsilon^2/(3L^2)]g.

Equations(6),(7) give

    j(q_epsilon)=1, Sigma(q_epsilon)=0,
    ||q_epsilon||_X < L^3 epsilon+2L^2 epsilon^2
                     <=3L^3 epsilon.

For any h as in(3), choose h_epsilon=h+(c-j(h))q_epsilon. This proves
all three assertions in(3), including exact preservation of Sigma.
Each central level set is thus dense within the inherited topology on
D intersect {Sigma=s}. This does not assert density of D in all X.
The strain level {Sigma=s} itself is closed in X, by(2). There is no
conflict between these two statements. The exact PDE, fixed tail, and
other domain conditions are not imposed by this construction.

## Verification and scope

This proof precedes the computation. Two independent exact calculations
will check the angular moments, kernel derivative, power integral and
central compensation. The constants for L=8614738245908811/1125899906842624
and k=1615536043799051/9007199254740992 will be enclosed by Arb balls and
independently by exact rational Machin bounds and integer square roots.
These are explicit parameters, not a new uncertainty enclosure for X3.
No actual SVD, velocity mapping on all X, full inverse, nonlinear estimate
or decisive endpoint is established.

# Moment interpolation under a weighted tail budget

## Statement

Let q<-3, d=-q-3>0, theta=d/(d+2), and let h be a real measurable
function on R2 with ||h||2<=beta and |h(X)|<=H(1+|X|)^q almost everywhere,
where beta,H are finite and nonnegative. Then the first moment is
absolutely integrable and

    |integral y h| <= Csplit(d) beta^theta H^(1-theta),
    Csplit(d)=(d+2)/(2d) pi^(theta/2) 4^(1-theta).                 (1)

In particular (1) applies to the S1 weighted C1 class Hq(h)<=H used in
T4-359. On a set with uniform Hq bound M, the moment functional is
Holder continuous in L2 with exponent theta, with difference estimate
Csplit ||h1-h2||2^theta (2M)^(1-theta). For every real prescribed
moment m, beta>0 and h with that moment,

    H >= [|m|/(Csplit beta^theta)]^(1/(1-theta)).                (2)

At qstar=1/c-4, c=4076476460239181/2251799813685248, d=delta=1-1/c.
This independently verifies the review of T4-359 R2, and extends its q range.
The proof uses only the amplitude bound; no derivative bound or S1
parity is needed for (1). The exponent is optimal on bounded Hq sets,
including smooth compact S1 functions with exact interior screening.
No claim of an optimal constant for the weighted C1 class is made.

## Complete proof

For any a>0, Cauchy-Schwarz on the disk and direct polar integration
outside it give

    integral |y h| <= (sqrt(pi)/2) beta a^2 + (4H/d) a^(-d).      (3)

Indeed integral_(r<a) y^2=pi a^4/4. Outside the disk, q<0 gives
(1+r)^q<=r^q, and integral |sin(theta)| dtheta=4, leaving
4H integral_a^infty r^(q+2)dr=4H a^(-d)/d. Both are finite, proving
absolute integrability. If beta=0 or H=0 then h=0 almost everywhere.
Otherwise the right side of (3) tends to infinity at both endpoints.
Its derivative vanishes at the unique point

    a^(d+2)=4H/(sqrt(pi) beta).

Substitution gives (1), and rearrangement gives (2). Apply (1) to a
difference, with amplitude bound2M, for Holder continuity.

For exponent optimality use the nonzero smooth normalized annular f
from the audited T4-359, and h_R=R^(-d-3)f(X/R), R>=1. Its first
moment is R^-d, its L2 norm is ||f||2 R^(-d-2), and its Hq norm is
bounded above and below by positive constants independent of R.
Its velocity vanishes on r<R. An estimate with any exponent
alpha>theta and uniform constant on this bounded set would require
R^-d<=C R^(-alpha(d+2)), impossible as R tends to infinity. This
proves exponent optimality with the exact weighted C1 hypothesis.

## Endpoint projection and reference scope

For the repaired references007,013,014, let A and P be the exact
angular maps in the frozen endpoint data. The coefficient of the
residual change from an annular moment m is (m/pi)P at exponent
qstar. Hilbert-space orthogonality gives its unique minimizing moment

    mstar=-pi <A,P>/||P||2^2,

because P is nonzero. Exact rational scalar products verify each
projection coefficient; Arb encloses mstar and the residual norm.
This accepts the algebraic part of the review of T4-359 R3. Its numerical
bump costs are FLOAT and are not certified here. In particular R3(c)
compares the drift contribution in the annulus with a pure exterior
endpoint term. The full annular residual change has three additional
terms in T4-359(7). Their possible cancellation requires control before
one calls the entire annular change larger at every R. That stronger
quantitative assertion remains OPEN. It is not needed for (1) or359.

For a higher odd angular density eta_n(r)sin(n theta) supported in
1<r<2, its Newton potential on r<1 is

    -r^n sin(n theta)/(2n) integral_1^2 s^(1-n)eta_n(s)ds.

This follows by solving a''+a'/r-n^2 a/r^2=eta_n with a regular at0
and decaying at infinity: a=-(r^-n integral_0^r s^(n+1)eta_n ds
+r^n integral_r^infty s^(1-n)eta_n ds)/(2n). Inside the annulus the
integrals reduce as asserted. Mode1 yields a linear potential, hence
zero velocity. For each n>=3 its velocity is homogeneous of degree
n-2 and vanishes exactly when the displayed radial moment vanishes.
Different n have different polynomial degrees, so they cannot cancel
identically on the interior disk. These are reference facts, not an
inverse or existence theorem. The dipole shift does not change the
orthogonal endpoint projection or any weighted consequence for the
same stationary correction under a changed reference decomposition.

## Verification

The complete argument precedes computation. The exact checker verifies
the optimizer identities and scaling relation, reconstructs the three
endpoint scalar products from rational Fourier maps, and independently
encloses the moment coefficients and interpolation constants in Arb.
The all-radius estimate is the analytic proof (3), not a sample test.

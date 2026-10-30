# Complete weak distances for new immutable polynomial candidates

## Exact reference and hypotheses

The first application is C1-N1-014-pairB-from007, whose immutable raw
coefficient JSON has SHA256
8dfc33c3dc5f8265e802831a500d757e2da09bc26890c457c0d3603afc3cb746.
All generator coefficients are exact rationals. The exact independent
conversion, origin and sector checks in candidate_audits must succeed
before this computation. The exact c is
4076476460239181/2251799813685248. Set gamma=1/c and delta=1-gamma.
The canonical potential chi gives rho=-partial_y Delta chi and
u=(-chi_xyy,chi_xxy). Its exact tail constraints imply F in L2(R2),
where F=(cX+u).grad rho-rho. Its reference fields are smooth S1 fields
with sublinear growth O(r^gamma). Source hashes identify the reference.

Let h be real, S1-symmetric and in L2(R2), and suppose rho+h solves
(cX+U[rho+h]).grad(rho+h)-(rho+h)=0 in distributions at this same c.
Require the canonical velocity decomposition U[rho+h]=u+U[h],
divergence-free U[h], the contraction ||U[h]||2<=||h||2 and locally
integrable weak products. These hypotheses and the exact reference
membership are conditions of the following necessary distance.

Use n=21, K=522, t=r2/(1+r2), v=1-t, and

    phi=r v2 t^K sin(n theta),
    I=int F phi,
    M=(2c+1)phi+(cX+u).grad phi,
    Cx=phi rho_x, Cy=phi rho_y,
    D=||M||2+sqrt(||Cx||2^2+||Cy||2^2),
    Hbar=4156114212970569/100000000000000000000.

After verifying Hbar>||grad phi||infinity, the conclusion is

    ||h||2 >= 2|I|/[D+sqrt(D2+4 Hbar |I|)].                 (1)

The program returns outward containing balls and a strictly smaller
positive rational floor. Its new candidate-level result remains OPEN
until an independent computation accepts it. This statement does not
prove existence, an inverse estimate or a floor for all possible
coefficients in the generator family. The all-c extension needs the
separately audited common-leading-tail chart theorem.

The n21,K522 probe was included among014's102 optimization rows. It is
therefore an optimization design probe for014, not held out from its
optimization. Exact certification on the frozen output remains a valid
necessary test. For013 it was held out of the first-mode objective.

## Standalone weak proof

Subtract the equations and first test with a smooth compact cutoff of
phi. Both background and correction velocities are divergence-free.
Integration by parts gives

    I=int h M-int phi U[h].grad rho+int h U[h].grad phi.

At the origin, r^(2K+1)sin(n theta) is a homogeneous harmonic polynomial
times (r2)^((2K+1-n)/2), with nonnegative integral exponent. Thus phi
is smooth. At infinity phi=O(r^-3), grad phi=O(r^-4); the reference
fields grow sublinearly. Cauchy-Schwarz shows that the three products
converge and their escaping-annulus cutoff errors vanish. Consequently

    |I| <= [||M||2+||phi grad rho||2]||h||2
                                    +||grad phi||infinity ||h||2^2.

Use the contraction for U[h] and solve this positive quadratic to obtain
(1). Integration of the reference transport separately gives
I=-int rho M. This supplies a pairing calculation without constructing
F. The sign in that identity follows from div(cX+u)=2c.

## Exact construction and all-plane integration

Keep the common t^K outside the polynomial arrays. Differentiation gives

    phi_r=v2 t^K G sin(n theta),
    phi_theta/r=n v2 t^K cos(n theta),
    G=(2K+1)-(2K+4)t.

The phi_x sine amplitudes at n-1,n+1 are (G+n)/2,(G-n)/2;
the phi_y cosine amplitudes are (G+n)/2,(n-G)/2. Multiply by every
Cartesian velocity mode, using exact trigonometric product formulas,
and add the linear M term. Multiplication of phi by each Cartesian
density derivative gives Cx,Cy. Every field is

    r v2 t^K sum_(ell,kind,m) v^(ell delta/2) P(t) trig(m theta),

with exact rational polynomial P. Test the factored constructor against
the independently audited ordinary polynomial constructor at K3,n7.
At three Cartesian points compare M,Cx,Cy against directly differentiated
phi and independently evaluated background fields. These checks are
performed for the current candidate, not inherited numerical values.

Angular orthogonality gives pi for every nonzero sine or cosine mode.
Square each vector component separately and retain all radial branch
cross terms within that angular frequency, with factor2 off diagonal.
A product of branches ell,j contributes

    (pi/2) int_0^1 v^(1+(ell+j)delta/2)
                           (1-v)^(2K+1) P(1-v)Q(1-v) dv.

All exponents are greater than-1. Gamma-based Beta recurrences integrate
the finite polynomial exactly up to outward Arb rounding. The same
complete products are constructed separately in t and v. Starting with
B(b+1,m+1), successive moments use factors(b+k+1)/(b+m+k+2)
or(m+k+1)/(b+m+k+2), respectively. Require endpoint intervals to overlap
and complete positive energies to have more than150 relative bits.
No angular mesh or finite radial cutoff is used.

The direct I uses the exact complete sine-n projection of F, formed
from the full Cartesian velocity and density-derivative product. Its
moments are(pi/2)B integrals with exponent ell delta/2-1 and powerK+1.
The second I uses -rho M. Require overlap and more than150 relative
bits. The already confirmed013 factored computation calibrates the
shared constructor and full moments; no014 value is accepted by that
calibration alone.

## Complete finite gradient maximum

At each radius, the angular maximum of |grad phi| is the larger of
|v2(1-v)^K[-3+(2K+4)v]| and n v2(1-v)^K. The angular amplitude reaches
its maximum at v=2/(K+2). Both radial endpoints vanish. The radial
amplitude derivative, divided by v(1-v)^(K-1), is

    -6+(9K+18)v-(2K+4)(K+3)v2.

Check this identity exactly, enclose its two roots and verify they
both belong to(0,1). The absolute radial amplitude can attain a positive
maximum only at these critical points or endpoints. Evaluate both roots
and the angular critical point with outward arithmetic and verify all
three amplitudes are strictly below the exact Hbar. This certificate
depends only on the probe, so it must agree with the independently
confirmed013 gradient certificate even though the reference changed.

## Data and verification evidence

The manifest binds exact candidate JSON, its structural audit, this
proof, every executed module and the confirmed013 reference record.
Only own copied sources are executed. Code and JSON evidence are kept
alongside this standalone proof. No Lean or Lake build is run. The
proof was checked before this new candidate implementation. A result
is a conditional necessary distance with its explicit weak solution
hypotheses, and its independent audit status is recorded separately.

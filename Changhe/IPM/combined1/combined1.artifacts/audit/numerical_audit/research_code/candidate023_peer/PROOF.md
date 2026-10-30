# Candidate 023: independent acceptance of point, origin and full prefix

Written 2026-10-29T12:03:52.194962+00:00, before the comparison checker. All new comparison results are OPEN until the checker finishes.


# Candidate 023 point certificate: independent acceptance

## Exact statement

Fix c=4076476460239181/2251799813685248 and the exact candidate
C1-N1-023-legqs25p100-quot013, raw SHA256
 d67bdd9ff05917736e686af5f834a2e12afede891098ccf8f9de8a6e2d7a71df.
Set F=(cX+u).grad rho-rho with the canonical velocity u=U[rho].
At X=(1/10,73/100), the positive gaps calculated below exclude a fixed-c
stationary correction h in each of the following H^(2+s)(R2) balls.
The Sobolev norm has multiplier (1+|xi|^2)^((2+s)/2), the Fourier
normalization is Plancherel, and the canonical velocity multiplier has
absolute operator norm at most one. Require the stationary difference
equation, canonical velocity decomposition, and the point embeddings
specified below. No result about another space, inverse or exact profile
is inferred.

| Registered ball | s | radius |
|---|---|---|
|A2-Db|1/262144|1/65536|
|FW-T-TB-rebal-v1|1/65536|3/32768|
|FW-T-TB-sharp-v1|1/8192|43/50000|
|T4-019-no-H|1/131072|1/16384|
|FW-T-T4L2-sharp-v1|1/7744|147/200000|
|FW-T-T4L2-sharpw-v1|1/5184|1351/1000000|

The same point excludes the original graded family under its audited
universal embedding bounds b0,b1 below. Those bounds are hypotheses of
this application; the existing graded-family proof supplies them.

## Complete point argument

For h with H^(2+s) norm at most r and s>0, Fourier Cauchy-Schwarz in R2
gives ||h||infinity, ||U[h]||infinity <= C0 r and
||grad h||infinity <= C1 r, with the directionally sharp gradient bound

 C0=(4pi(1+s))^(-1/2), C1=(8pi s(1+s))^(-1/2).

For the gradient, take the supremum over unit output directions after
using the identical isotropic multiplier integral in each direction.
These integrals converge because s>0. Subtract the reference stationary
residual from the exact equation:

 -F=(cX+u).grad h+U[h].grad rho-h+U[h].grad h.

The triangle inequality at the fixed point yields

 |F| <= r[C1|cX+u|+C0(1+|grad rho|)]+C0 C1 r^2.       (1)

The right side is increasing for r>=0. A positive gap excludes that
closed ball. Its positive quadratic root is evaluated with the stable
expression 2|F|/(D+sqrt(D^2+4C0C1|F|)), where
D=C1|cX+u|+C0(1+|grad rho|).
For the original graded geometry, its audited top-margin estimate gives
C0 r<b0 and C1 r<b1 with

 b0=50/(651 sqrt(28248) sqrt(4pi)), b1=25/(217 sqrt(8pi)).

Therefore |F| is bounded by b1|cX+u|+b0(1+|grad rho|)+b0b1 if any such
correction exists. A positive gap excludes precisely that family under
its defining hypotheses. The frozen T4 graded proof and the prior own
generator and graded-point proofs give the family derivation.

## Independent field evaluation

Our N4-337 field calculation differentiates the exact raw potential by
Cartesian jets. T4-417 independently sums exact radial Taylor jets at
t0=r^2/(1+r^2), differentiates the polar Laplacian and the stream function,
and encloses the fractional positive prefactor with Arb. Its complete
local derivation is frozen in source/candidate023_point/PROOF.md. The following identities
explain why radius 25 introduces no global integration in this point test.
For a legqs generator, D=R^2(1-t)+t and

 V(t)=sum_(k=0)^N (-1)^(N+k) binom(N,k)binom(N+k,k)
       R^(2Q)t^(m+w+k)(1-t)^Q D^(-w-Q-k).

Here R=25 and D>0. Taylor derivatives through degree4 suffice: the density
and velocity use at most three derivatives of the potential, and the
density gradient at most four. Every local Taylor coefficient apart from
the single positive fractional power is rational. T4 includes all radial
prefactor derivatives and updates angular sine and cosine with the old
pair in the addition recurrence. Its frozen proof's polar identities
follow by direct differentiation and have been checked before this
acceptance. No peer code is executed by this checker.

## Verification and scope

Bind every peer result dependency by SHA256, retaining byte-identical own
files when available. Compare all eight fields from the two independent
paths, recompute their residual identity and all six exact parameter rows,
(1), the positive roots, and the graded upper bound and gap with outward
Arb arithmetic. Compare the signed local diagnostic
(|grad rho|-rho_y)/2, which is not a global background bound. The global
radius 25 rational-moment integrator and the exact asymptotic sector flags
need their separate independent reviews. Point agreement does not certify
them. Positive gaps are strict mathematical inequalities, not a proxy
optimization loss. The result retains containing balls and all hashes.


# Candidate 023 exact origin normalization: independent acceptance

## Statement and hypotheses

Fix c=4076476460239181/2251799813685248 and the exact rational potential
of C1-N1-023-legqs25p100-quot013, raw SHA256
d67bdd9ff05917736e686af5f834a2e12afede891098ccf8f9de8a6e2d7a71df.
Set gamma=1/c, delta=1-gamma, rho=-partial_y Delta chi and
u=(-partial_xyy chi,partial_xxy chi). The existing canonical-potential
identification is assumed; this local calculation does not reprove it.
The exact claim is c+partial_y u2(0)=1 and partial_y rho(0)>0.
Its exact slope and an outward decimal interval are stored in the result.
It asserts no stationary solution, global bound or inverse.

## Complete local argument

Write z=x^2+y^2, H_m=Re((x+iy)^(2m)) and
p_j=(3+gamma-j delta)/2. A generator is
H_m (1+z)^(p_j-m) t_R^w u_R^Q P_N(2t_R-1),
where t_R=z/(R^2+z), u_R=R^2/(R^2+z), R>0 and w,Q,N>=0.
The mono case has N=Q=0 and R=1; the ordinary Legendre case has Q=0,R=1.
Let A_N(Z)=(1+Z)^N P_N((1-Z)/(1+Z)). The Legendre recurrence constructs
this finite polynomial exactly. The radial coefficient after H_m is

 (-1)^N R^(-2w) z^w (1+z)^(p_j-m)
 A_N(z/R^2) (1+z/R^2)^(-w-Q-N).

This identity follows by P_N(-x)=(-1)^N P_N(x). All factors are analytic
at zero, so finite Taylor convolution gives exact coefficients. Only
the coefficient of z^(2-m) can affect fourth derivatives. Terms with
m+w>2 vanish to order at least six. Sum the remaining exact coefficients
into B_m for m=0,1,2. Since H_0=1, H_1=x^2-y^2 and
H_2=x^4-6x^2y^2+y^4, the homogeneous quartic part is

 (B0+B1+B2)x^4+(2B0-6B2)x^2y^2+(B0-B1+B2)y^4.

If its coefficients are A40,A22,A04, direct differentiation gives
partial_y u2(0)=4A22 and partial_y rho(0)=-4A22-24A04.
Every higher Taylor term has zero fourth derivative at zero; lower terms
also have zero fourth derivative. These exact finite identities prove
the normalization and slope claim once the rational checks pass.

## Independent path and verification

N4 reconstructs the local coefficients by the homogenized Legendre
recurrence above. T4-418 instead expands the shifted Legendre polynomial
as sum_k (-1)^(N+k) binom(N,k) binom(N+k,k) t_R^k, then convolves its
two binomial series. Both derivations are exact, with no differentiation
step size or quadrature. Read and freeze T4's full proof, code and input
hashes without executing its code. Recompute the own origin coefficients
and all three quartic coefficients, compare all four exact fields with
both independent records, count every contributing raw generator and
summand, and check the strict slope interval with outward Arb arithmetic.
The input is exact JSON; no numeral table is manually transcribed.
The local generator proof is ../generator_sector_audit/PROOF.md. Every
executed local dependency and frozen peer source is bound by SHA256.


# Complete exact residual-sector comparison for candidate 023

## Statement, hypotheses, and scope

The reference is the function defined by the immutable rational generator file
for C1-N1-023-legqs25p100-quot013, SHA256
d67bdd9ff05917736e686af5f834a2e12afede891098ccf8f9de8a6e2d7a71df.
Let c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma.
The potential chi defines rho=-partial_y Delta chi, psi=partial_x partial_y chi,
and U=(-partial_y psi,partial_x psi). The residual is
F=c X.grad rho-rho+U.grad rho. The coefficient functions in this proof
are finite Fourier sine or cosine polynomials on the full circle.

We independently compare all density, stream, and residual coefficients for
the sixteen labels (K,L), K>=1,L>=0, whose exponent
 e(K,L)=1-K delta-2L
is at least -7/2. The proposed conclusion is exactly eleven zero residual
sectors and five nonzero sectors in decreasing exponent order:
 (4,1), (9,0), (5,1), (1,2), (10,0).
The first four L=0 density and stream profiles must equal those of the
separately audited candidate 007. This statement concerns asymptotic
coefficients only. It implies no residual upper norm, existence theorem,
background bound, inverse estimate, or optimality of a finite basis.

## Independent expansion and differentiated remainder

Write z=r^-2. A generator with branch j, angular degree 2m, and rational
positive scale R has potential
 r^(2m) cos(2m theta) (1+r^2)^(p_j-m)
 t_R^w u_R^Q P_n(2t_R-1),
where p_j=(3+gamma-j delta)/2, t_R=r^2/(R^2+r^2), and
u_R=R^2/(R^2+r^2). Mono and unscaled Legendre terms are the stated special
cases. The independent expansion uses the homogeneous polynomial
 A_n(z)=(1+z)^n P_n((1-z)/(1+z)).
Its radial factor after extracting r^(2p_j) is
 R^(2Q) z^Q (1+z)^(p_j-m) A_n(R^2 z)
 (1+R^2 z)^(-w-Q-n).
This follows by substituting t_R=1/(1+R^2 z). The finite polynomial A_n
is obtained from the Legendre recurrence. Convolution of its coefficients
with the two generalized binomial series gives each exact rational Taylor
coefficient. This differs from the peer's expansion of P_n(2t-1) into
powers of t before convolution. Both series are analytic near z=0;
finite differentiation preserves the required asymptotic remainder order.
All new scaled terms have Q=4 and therefore make zero direct contribution
to the field coefficients with L<=2. Optimized unscaled coefficients can
nevertheless change those coefficients.

For every computed homogeneous potential r^d C(theta), differentiate in
Cartesian directions using the polar formulas
 partial_x=cos(theta) partial_r-sin(theta) r^-1 partial_theta,
 partial_y=sin(theta) partial_r+cos(theta) r^-1 partial_theta.
Trigonometric product identities give finite exact coefficient maps for
rho, psi, their derivatives, and U. For density exponent a=d-3, form the
linear residual (c a-1)rho. Add every product U_i.grad rho_j at its exact
rational exponent, using complete Fourier products. Verify separately
 Delta psi=-partial_x rho
for every sector. This checks the stream sign and the homogeneous-degree
shift independently of the nonlinear residual assembly.

## Completeness and equality checks

The local code uses j=K-1 and q=L. It computes q<=2 and j<=9 for the
residual, while retaining every generator branch required in products.
The first omitted radial exponent is gamma-6 and the first omitted
branch exponent is gamma-10 delta. Both are strictly less than -7/2.
Nonlinear sector labels add positive K and nonnegative L, so a factor
outside this range cannot contribute to a retained exponent. Filtering
by exact rational comparison gives all sixteen labels, with distinct
exponents. The thirteen labels common to the earlier rectangular audit
are compared again. The three additional labels (9,0),(1,2),(10,0) are
recomputed in exact arithmetic, not inferred from the publisher's FLOAT
norm table.

At each retained label compare all three complete angular coefficient
maps with the independently derived peer maps. Equality of finite maps
proves equality of the corresponding Fourier polynomials. A nonzero
coefficient proves a nonzero sector. Orthogonality gives the exact
full-circle squared norm pi times the sum of squared sine coefficients;
Arb arithmetic encloses its square root and compares it with the peer's
outward interval. The leading nonzero sector is established because its
exponent is above the complete omitted bound. Recompute the first four
leading density and stream maps from the independently frozen raw 007
input and compare them exactly. This completes the stated argument when
all exact checks succeed.

## Dependencies and evidence

The raw-generator algebra and its analytic remainder argument are in
../generator_sector_audit/PROOF.md and PROOF_CANDIDATES.md; its local
implementation is generator_sector_audit/code/direct.py, using the
Legendre recurrence in multiscale_generators/code/moments.py and Cartesian
homogeneous differentiation in sector_audit/code/sectors_flint.py.
The peer proof and code are frozen under source/ and are read as text only.
The result binds the raw snapshot, all local dependencies, and every
frozen peer file by SHA256. Hashes identify data; the mathematical proof
and exact checks justify claims. No foreign code is executed.

## Stored evidence and compression

The actual basis has 1922 unscaled and 504 scaled generators at positive
radii25 and100. Peer sources are frozen before checking. Already frozen
identical local inputs may be reused by content hash. Large new exact
JSON inputs may be stored in gzip form. The manifest records both stored
and decoded hashes; mathematical checks consume the exact decoded JSON.
Compression changes storage, not a coefficient or claimed interval.
All sixteen new peer maps are compared with a fresh own raw-generator
expansion, including the three rows previously compared only to a FLOAT
publisher norm by T4. Peer code is inspected as text and never executed.

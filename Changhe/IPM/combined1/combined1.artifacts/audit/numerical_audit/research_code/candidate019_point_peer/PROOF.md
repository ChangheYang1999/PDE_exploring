# Candidate 019 point certificate: independent acceptance

## Exact statement

Fix c=4076476460239181/2251799813685248 and the exact candidate
C1-N1-019-legqs50-cont12, raw SHA256
 ca0fffafe2aa7ea3c6049e0b5a83651113451087027b0783800c046ae170d419.
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

Our N4-279 field calculation differentiates the exact raw potential by
Cartesian jets. T4-353 independently sums exact radial Taylor jets at
t0=r^2/(1+r^2), differentiates the polar Laplacian and the stream function,
and encloses the fractional positive prefactor with Arb. Its complete
local derivation is frozen in source/candidate019_point/PROOF.md. The following identities
explain why radius 50 introduces no global integration in this point test.
For a legqs generator, D=R^2(1-t)+t and

 V(t)=sum_(k=0)^N (-1)^(N+k) binom(N,k)binom(N+k,k)
       R^(2Q)t^(m+w+k)(1-t)^Q D^(-w-Q-k).

Here R=50 and D>0. Taylor derivatives through degree4 suffice: the density
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
radius 50 rational-moment integrator and the exact asymptotic sector flags
need their separate independent reviews. Point agreement does not certify
them. Positive gaps are strict mathematical inequalities, not a proxy
optimization loss. The result retains containing balls and all hashes.

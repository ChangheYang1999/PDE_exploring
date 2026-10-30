# Complete candidate007 forcing norm after the negative-norm audit

## Statement, conventions and dependencies

The exact reference is C1-N1-007-d2w-j7-e2bal at
c=4076476460239181/2251799813685248, raw SHA256
ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21.
Its canonical whole-plane residual is F=(cX+U[rho]).grad rho-rho.
Use standard spatial L2 norms, the ordered Cartesian derivative tensors,
omega=(1+4|X|^2)^(2/5), J=(1-Delta)^(1/2), and Lambda=(-Delta)^(1/2).
Put G0=||F||2, G1=||grad F||2, P2=||omega D^2F||2,
Q3=||omega D^3F||2 and H=||Lambda^-1 F||2. The definition and variational
normalization of H are proved in ../negative_norm007_peer/PROOF.md.
All five quantities are finite, by the full-plane certificates139,153,
166 and249. The Hessian and third tensor include multiplicities1,2,1
and1,3,3,1 respectively. Set

 E^2=P2^2+2^14 G1^2+2^18 G0^2+2^18(20/21)H^2,
 N_s(F)=E_2(J^s F),

where E_2 uses precisely that same four-component expression. For
0<s<1/34 the containing intervals in verification/result.json enclose E
and N_s(F), using the comparisons proved below. The four exact s values
and sufficient thresholds checked are

| Framework | s | sufficient forcing threshold |
|---|---|---|
|FW-A2-Db|1/262144|1/1572864|
|FW-A2-Da|1/268435456|1/2684354560|
|FW-T-TB-rebal-v1|1/65536|3/327680|
|FW-T-TB-sharp-v1|1/8192|5289/50000000|

The first two definitions and thresholds are in the frozen Analysis II
proof/report. The rebalanced fraction is in theory_v01 Section FW-T-TB-rebal-v1 and the original
T2-R1 source; the sharp threshold is in the frozen current theory registry,
which carries its audited antecedents. The inequalities checked here do
not require the background inverse assumptions. A norm above a sufficient
threshold fails that smallness condition. It alone does not exclude a
stationary correction or disprove a different existence theorem.

## Norm comparison proof

For a smooth f with finite E=E_2(f), Q=||omega D^3 f||2, define the
Hilbert-valued function

 Tf=(omega D^2f,128Df,512f,512sqrt(20/21)Lambda^-1 f).

Then ||Tf||2=E. Write B=16384 and b0=20/21. The global Lipschitz bound
||grad omega||infinity<=2 and the inequality |a+b|^2<=2|a|^2+2|b|^2 give
||D(omega D^2 f)||2^2 <= 2Q^2+8||D^2 f||2^2.
The derivatives of the other entries have squared norms
B||D^2f||2^2,16B||Df||2^2 and16B b0||f||2^2. The last identity uses
sum_i |xi_i|^2/|xi|^2=1. Since omega>=1 and each component contributes
to E^2, adding these inequalities gives

 ||Tf||H1^2 <= 2Q^2+(B+25+b0)E^2 < 2Q^2+16410E^2.       (1)

For0<s<=1/2 the Bessel-kernel commutator gives
||[J^s,omega]v||2<=34s||v||2. To see its scope, use the positive kernel
of J^s-I, insert |omega(x)-omega(x-z)|<=2|z|, and apply the kernel's
first-moment bound17s and Young's inequality. The source proof supplies
the exact kernel and its finite moment; this is an operator bound, not a
sampled weight estimate. The same proof applies to a finite tensor.
All unweighted entries of T commute with J^s. Thus

 | ||T J^s f||2-||J^s Tf||2 | <=34s||D^2f||2<=34sE.

Fourier Holder interpolation and (1) imply

 N_s(f)<=E^(1-s)(2Q^2+16410E^2)^(s/2)+34sE.              (2)

Conversely ||Tf||2<=||J^s Tf||2 because the Bessel multiplier is at least
one. The preceding commutator gives E<=N_s(f)+34sE, so

 N_s(f)>=(1-34s)E.                                     (3)

These arguments hold first on the smooth core and then by completion.
They also apply to the smooth reference residual with the finite complete
certified E,Q. This is the source Analysis II Section8 proof written with
all four components, not a new inverse estimate. E=0 forces f=0 and is
trivial; every input here is positive. The statement does not identify E
with N_s even when s is small.

## Outward assembly and independent comparison

The accepted own G0,G1,P2,Q3 intervals and the independently confirmed249
H interval are bound by SHA256. The N3 registered H endpoints must equal
the frozen H result used in249. Their positive lower and upper balls,
not only their midpoint decimals, enter the assembly. E is monotone in
all components. For0<s<1/34, (3) is increasing in E; the right side of
(2) is increasing in E,Q since all exponents are positive. Substitute the
lower component endpoints for (3) and upper endpoints for (2), using Arb
at512bits. The narrower own tensor-weight intervals can give a stricter
containing result than the independent peer's approximation.

Every printed N3 E2 and N_s interval is checked by strict containment of
the own lower and upper comparison expressions, rather than overlap
alone. Four exact threshold ratios are recomputed; the peer's display of
a threshold as binary64 decimal is read only as an approximate label.
Every reported rational floor/ceiling is verified with a strict whole-ball
inequality. Components' energy shares divide their nonnegative weighted
squares by the complete E^2; interval division preserves inclusion.
A share describes this quadratic norm and does not identify a difficult
operator direction. No full field integration is repeated. No peer code
is executed. Fine digits in the own Green norm beyond the coarse249
acceptance are not used to narrow this certificate.

## Prepublication threshold repair

The first arithmetic comparison used the N3 code's printed decimal
9.1553e-6 as the rebalanced divisor. The source theorem instead states
3/327680=0.0000091552734375 exactly. The printed decimal exceeds it by
17/640000000000. The old ratio is still a conservative lower bound for
the ratio to the exact smaller threshold, and every E2/N_s enclosure is
unchanged. It was incorrect to call that decimal the exact registered
threshold. The current checker uses3/327680, retains the old comparison
as development evidence, and verifies the ordering rationally. This
arithmetic correction does not assert that a slightly larger threshold
could not be proved by other estimates.

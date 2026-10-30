# Audit of the present two-weight remainder at campaign radii

## Statement and scope

Assume the canonical S1 stationary setting, finite H=H_q(h)>0,
reference hypotheses and endpoint expansion of T4-335, with
c=4076476460239181/2251799813685248, q=1/c-4, delta=1-1/c,
and D=1-c(q-delta)=5c-1. The exact endpoint angular data A,P,
Theta0 for each of007,013,014 are the copied JSON data. Let

 B=dist_L2(0,2pi)(A,span(P))/(4c)>0,
 g0=Theta0'(0)>0,
 Phi=|q(AP'-A'P)|/[4c sqrt(q^2P^2+P'^2)]

at the exact rational angle in parameters.json. By T4-380, H>=Phi.
Let beta be one of the four exact targets in that file and put

 alpha=-2q-2,
 r_beta=[B/(beta sqrt(alpha))]^(1/(-q-1)),
 Kcrit=D B r_beta^delta/[sqrt(2pi) g0],
 Sigma=1/2+2^(3-q)+2^(1-q)+2^(2-q)/(q+5).

Use specifically the uniform velocity remainder in T4-410 (7)-(9),
with R0>=2, L0=2R0, amplitude A410 and J(R) as defined there.
Assume its input list contains the positive delta-term from T4-335:
C_delta=H(V+E G)/D>0, with G>=g0 and V,E>=0. Hence its admissible
epsilon obeys0<epsilon<=delta. The hypothesis of positivity is
explicit: it follows from the existing positive E and G, or from
positive V for these references. No lower bound on the actual
velocity of a stationary correction is assumed.

For every L0<=R<=r_beta,

 J(R)/H >= Sigma (5/r_beta)^delta = j_min.              (1)

For all three references and all four targets, the finite checker
proves j_min Phi>Kcrit. Consequently the uniform constant furnished
by (9), even after discarding its nonnegative limiting coefficient
and cutoff harmonic error, cannot certify the specified beta with
the registered CI test. This is a restriction of that error majorant
and its current tail input. It is not nonexistence, an upper bound
on actual solution distance, or a restriction on every possible
use of a radius-dependent remainder or a sharper kernel estimate.

## Proof of the main obstruction

Write a=q-epsilon. In T4-410, A410>=H(1+L0)^epsilon.
The bracket in J is at least C_a+L_a. Because -5<a<q<-3,
2^(3-a),2^(1-a),2^(2-a)/(a+5) each exceed their value at q,
and the two other omitted terms of C_a are positive. Therefore
C_a+L_a>=Sigma. The base (1+L0)/R is at least5/r_beta.
Since5/r_beta<1 and epsilon<=delta, its epsilon power is at
least(5/r_beta)^delta. This remains true when the first base
exceeds1: its epsilon power then exceeds1. This proves(1).

For completeness, the necessary cutoff condition needs no assumption
R<=r_grad. A constant absolute velocity bound Cvel gives the
nonnegative CI summand (HV+Cvel G)r^-delta/D. Put

 r_grad=[sqrt(2pi)(HV+Cvel G)/(D B)]^(1/delta).

The CI integrand vanishes below r_grad and is at most B^2 r^(2q+1)
elsewhere. If its starting radius is R, its square-root value is
at most B max(R,r_grad)^(q+1)/sqrt(alpha). Reaching beta requires
both R<=r_beta and r_grad<=r_beta, thus Cvel<=Kcrit, after dropping
HV and using G>=g0. But (9) furnishes Cvel>=J(R)>=Phi j_min>Kcrit.
This is the contradiction for the chosen sufficient majorant.
The same proof covers a CI starting later than the velocity validity
radius, by taking the best available J at the later radius.

## Conditional structural variant and scope repair

If additionally L0<=R<=r_grad and the same C_delta defines
r_grad^delta=sqrt(2pi)C_delta/B, then

 A410>=2^-a C_delta L0^(epsilon-delta),
 J(R)>=2^-a(C_a+L_a) C_delta R^-delta
       >=2^-q Sigma B/sqrt(2pi).                         (2)

Indeed L0^(epsilon-delta)>=R^(epsilon-delta). The checker verifies
all numerical ratios in T2's conditional table. This variant is
valid only with the displayed same-coefficient and R<=r_grad
conditions. A general CI may start at R>r_grad; T2's statement that
R<=r_grad is necessary is too strong. The main obstruction above
uses only the actual necessary R<=r_beta and survives this repair.

T2's FLOAT searches for a better epsilon, heuristic inner multipole
estimate and illustrative kernel-loss factors are not accepted as
certificates here. T1 independently reviews the full T4-410 theorem.
The present audit rederives its campaign consequence and each claimed
directed numerical bound from exact endpoint data.

## Arithmetic evidence and dependencies

Reconstruct the full-circle projection exactly by sine orthogonality:
B^2=pi[sum A_n^2-(sum A_n P_n)^2/(sum P_n^2)]/(16c^2).
Evaluate Phi at the stored rational angle using outward Arb arithmetic.
No floating optimizer enters the accepted bounds. Recompute Sigma,
r_beta,Kcrit,j_min, the epsilon=1/4 variant, and every directed
non-FLOAT table entry, and compare with copied T2_result.json.
Dependencies are T4-335 (audited350), CI351, endpoint380 and the
explicit majorant of410. The raw input, proof and checker hashes,
real execution time and all comparisons are stored in verification.

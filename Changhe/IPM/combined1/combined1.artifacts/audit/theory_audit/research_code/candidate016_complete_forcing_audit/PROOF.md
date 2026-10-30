# Complete candidate016 components and five actual weighted forcing comparisons

Written 2026-10-29T15:17:21.322120+00:00. This finite audit accepts completed N4-392/393 arithmetic under
the prior independent moment and exact differentiation certificates. It does
not execute peer code or repeat a candidate integral.

## Exact statement

Let rho016 be the canonical real S1 profile with immutable raw hash
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42,
c=4076476460239181/2251799813685248 and
delta=1824676646553933/4076476460239181. On R2 put
F=(cX+U[rho016]).grad rho016-rho016, using the accepted canonical velocity.
Use Lebesgue norms, the unitary Fourier transform, J=(1-Delta)^(1/2),
Lambda=(-Delta)^(1/2), and omega=(1+4|X|^2)^(2/5). Define

 G0=||F||2, G1=||DF||2, P2=||omega D2F||2, R=||rF||2,
 H=||Lambda^(-1)F||2,
 E_w(F)^2=P2^2+w1 G1^2+w2 G0^2, E_*=E_(16384,262144),
 E2(F)^2=E_*^2+(262144*20/21)H^2,
 N_s(F)=E2(J^sF), X_(s,w)(F)=E_w(J^sF).

D2 is the full ordered Cartesian Hessian. Assume the source-bound complete
component balls and moment groups in source/production.json.gz are valid,
with exact differentiation and positive-pole moment soundness established
by their accepted N3/N4 dependencies. Their finite arithmetic and binding
will be independently checked here. The exact four component endpoints
are in data/components.json. All ten framework parameter rows, including
their strictly positive thresholds, are in data/parameters.json. The
accepted commutator estimates described below and their domain hypotheses
are also premises. Then the directed bounds in verification/result.json
prove ten failures of those named sufficient forcing tests and the five
same-parameter strict inequalities X_(s,w)(F007)<X_(s,w)(F016). Candidate007
has immutable raw hash
ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21.
Its accepted upper bounds are source/baseline007.json, previously audited
in T4-238. Both profiles use the same real S1 and norm conventions.

The five conservative gaps are respectively sharp30.172542254537,
sharpw18.235303194523, bL[7/5]18.306105182355,
bL[1]18.513960661750 and trans30.726383186740. These are lower bounds
for the actual differences at the identical source parameters. No actual
E2 ordering, stationary-correction distance ordering, other-candidate
ranking, inverse estimate, dyadic exclusion or existence follows.

## Complete angular and radial accounting

An exact derivative of order d has radial factor R_d and a finite sum
of ell branches with angular sine or cosine mode n. Distinct modes and
kinds are orthogonal. Each nonzero sine or cosine square integrates to
pi, and the constant cosine square integrates to2pi. The full ordered
d-th derivative tensor gives partial_x^a partial_y^(d-a) multiplicity
binomial(d,a). Thus d=2 uses1,2,1. Expand every ordered pair within each
same angular mode, then combine exactly by ell_sum. The unweighted pair
count counts terms, not multiplicities. The metadata supports14960 pairs
at d=0,30176 at d=1 and45648 at d=2. The saved numerator hashes identify
the representation; they do not independently reconstruct its coefficients.

Put t=r^2/(1+r^2), v=1-t. The accepted radial representation has
R_d=r v^(d/2) for even d, and v^((d-1)/2) for odd d. Since
r dr=dt/(2v^2), the complete branch group has exponent
b=d-3+ell_sum*delta/2+q, with extra t when d is even, where q is its
exact factored v-zero order. The R norm adds t/v. The P2 norm adds
omega^2=(1+3t)^(4/5)v^(-4/5). Therefore its b has another -4/5,
and R has another -1. Every exact saved exponent is checked against this
formula and must exceed-1 after cancellation. All remaining denominator
factors1+a v are strictly positive. This is an ordinary absolutely
convergent integral. No analytically continued divergent piece is used.

For P2 set z=(3t-3/2)/(5/2), so |z|<=3/5, and let W be the degree56
binomial polynomial for(1+z)^(4/5). The coefficient ratio after degree57
is at most3/5 in absolute value on this interval. Consequently

 epsilon=|binomial(4/5,57)|(3/5)^57/(2/5)

is a uniform absolute remainder bound. Multiply W-epsilon <=
(1+z)^(4/5) <= W+epsilon by the complete nonnegative squared Hessian
density. If S is its radial integral with v^(-4/5) and T includes W,
then

 P2^2 in (pi/2)(5/2)^(4/5)[T-epsilon S,T+epsilon S].

Individual branch groups may have either sign. Summing their accepted
outward moment balls is legitimate because the weight inequality was
proved for their total nonnegative density. S>0 and both square
endpoints must be proved positive before square roots. Unweighted norm
squares are pi*S/2. The checker independently recomputes epsilon exactly,
sums all31 groups for each component, verifies exponent formulas and
all reconstruction flags, and compares the new interval to the accepted
strict rational component endpoints. Saved point comparisons and minimum
accuracy bits are checked as recorded metadata. They do not substitute
for full exact differentiation or moment soundness.

## Lower comparisons and domains

F is odd in y, so its angular mean vanishes. For a compact smooth test
phi, its odd part preserves the F pairing and cannot increase its
gradient norm. Circle Poincare gives ||phi_odd/r||2<=||grad phi||2.
Hence |int F phi|<=R||grad phi||2, proving H<=R by homogeneous Sobolev
duality. In particular all components of E2(F) are finite and

 E_*<=E2(F)<=sqrt(E_*^2+(262144*20/21)R^2).

Define the Hilbert direct-sum operator
T f=(omega D2f,128 Df,512 f,512 sqrt(20/21)Lambda^(-1)f).
Its norm is E2(f). All blocks except the first commute with J^s.
The accepted AnalysisII estimate ||[J^s,omega]v||2<=34s||v||2,
0<s<1/34, applied entrywise gives
||J^s TF-TJ^sF||2<=34s||D2F||2<=34s E2(F).
The Euclidean tensor sum adds no factor2. If E2(J^sF) is finite, the
distribution identity proves J^sTF is L2 and hence TF is in its
operator domain. Plancherel gives ||J^sTF||2>=||TF||2. Therefore
N_s(F)>=(1-34s)E2(F)>=(1-34s)E_*. If the fractional norm is infinite,
the lower estimate is automatic. Removing the final block gives the
legacy X3 lower estimate. The five general XSW norms use the accepted
T2-R3/T4-042 coefficient48/25 and replace middle block factors by
sqrt(w1),sqrt(w2), giving
X_(s,w)(F)>=(1-(48/25)s)E_w(F).
Every registered coefficient is positive. We invoke these established
commutator theorems with their original domain assumptions, without
asserting a new fractional regularity or upper-bound theorem.

All positive sums, square roots and divisions by positive thresholds
are monotone. Component floors therefore give forcing floors. A floor
above its registered threshold refutes that sufficient test, and no
necessity for profile existence is asserted. An accepted baseline007
upper bound below the corresponding016 lower bound orders the actual
XSW norms. Exact agreement of s,w1,w2,Cw and threshold is checked first.
Two lower bounds alone would not justify such an ordering.

## Strict endpoints and a conditional dual target

The peer's corrected formatter extracts exact dyadic endpoint mantissas
and exponents, scales in rational arithmetic, takes integer floor or ceil,
then moves one extra decimal unit outward. Thus even a grid-aligned
endpoint has strict rational margins. This checker verifies every saved
margin against independent interval arithmetic and exact rational gaps.
It retains the earlier formatter failure as development evidence.

The dual theorem independently audited in T4-466 would also imply
H016^2 >= (376/1000)^2+(371/1000)^2 if distinct modes1 and3 each have
an independently certified absolute quotient at least those exact
values. Together with E_*>547861145896494/10^12 and an accepted same-E2
upper E2(F007)<606820219/10^6, this would imply E2(F016)>E2(F007)
provided the exact squared gap checked here is positive. This paragraph
is a sufficient conditional target only. The new016 dual values are
OPEN until reproduced; this audit does not accept them or order E2.
The baseline E2 source is bound for this conditional test, without
repeating its underlying negative-norm calculation.

## Verification, dependencies and scope

The manifest freezes compact primary evidence and all exact scalar data.
external_bindings.json records the read-only rehash of the62 N4 assembly
inputs, the component and production source graphs, and the baseline
negative-norm assembly graph. The checksum check is identity evidence,
not a proof of those external algorithms. This audit executes only its
own finite checker. The accepted moment integrals and their symbolic
soundness remain explicit premises. N4-347's provenance qualification
is retained: copied peer modules were imported by the production fixture;
the field and norm routines were N4's own. Agreement is against saved
40-digit containing peer balls, not an independent recreation of every
historical1024-bit endpoint. No Q3 or fractional upper bound for016 is
provided. All test failures and actual comparisons are scoped above.

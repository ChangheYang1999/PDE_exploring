# N4 numerical audit handoff

Final summary frozen 2026-10-29T18:51:00.332283+00:00. The claim ledger runs through N4-440. Later report repairs and acceptances go in FINAL_AUDIT_ADDENDA.md; this summary stays unchanged for collection. This handoff
replaces the chronological working summary, retained unchanged in
[maintenance/AUDIT_SUMMARY_before_final_rewrite.md](maintenance/AUDIT_SUMMARY_before_final_rewrite.md).
The append-only [VERDICT_LEDGER.md](VERDICT_LEDGER.md) governs individual
verdicts. [research/README.md](research/README.md) gives the reading order
and standalone proofs; [REPRODUCE.md](REPRODUCE.md) records commands,
precisions, source hashes, failed attempts and expected results.
[the N4 next-audit plan](the N4 next-audit plan) gives proposed priorities beyond this run.

No a posteriori existence proof has closed. The accepted results exclude
the specified scalar correction balls and original graded boxes around
the 24 exact references 002 through 026, excluding the controlled FLOAT
comparison 011. They do not exclude every stationary IPM profile. The
newest trials 027 and 028 have no new PDE certificate from this lane.

Candidate 007 remains the extensively certified comparison reference.
Candidate 016 has a smaller verified homogeneous negative norm, but a
larger verified E2 norm. Both comparisons use complete bounds on the
same norms. They neither rank distances to solutions nor establish a
better reference for every proof framework. Candidate 017 has accepted
weak exclusions and a complete background cover. Its proposed complete
H and E2 bounds remain conditional on source integrals that this lane
has not reproduced.

## Exact objects and the weak exclusion

All norms use real functions and Lebesgue measure on R2. For the named
fixed-c references, put

    c0 = 4076476460239181/2251799813685248,
    rho = -partial_y Delta chi,
    u = (-chi_xyy, chi_xxy),
    F = (c0 X+u).grad rho-rho.

The potential chi is the immutable exact rational snapshot, not its
binary64 conversion. For h in L2(R2), let U[h] be the Fourier multiplier
with symbol (xi1 xi2/|xi|^2, -xi1^2/|xi|^2). Its value at zero does not
affect the L2 operator. The correction class in the accepted common
exclusion consists of distributional solutions of

    F + div((c0 X+u)h) - (2c0+1)h
      + U[h].grad rho + div(h U[h]) = 0.

Here U is an L2 contraction, h U[h] is locally integrable, and the exact
reference fields are smooth with the proved sublinear far field. This
formulation requires no point trace of an arbitrary L2 correction.
S1-normalized corrections with the required traces are a subset.

For a retained smooth probe phi, complete integral certificates give
I=|int F phi|, an upper D for
||(c0 X+u).grad phi+(2c0+1)phi||2+||phi grad rho||2, and an upper Hphi
for ||grad phi||infinity. Testing with radial cutoffs gives

    I <= D ||h||2 + Hphi ||h||2^2.

The cutoff limits, whole-plane moment formulas and global gradient
bounds are proved in the linked result folders. The finite composition
[N4-390](audit record h18_coverage_peer, proof) checks, for each of the
24 references, the strict rational inequality

    I_lower - D_upper/1000 - Hphi_upper/1000000 > 0.

Thus every such correction has ||h||2>1/1000. The eight registered
scalar tuples have L2 radius ceilings below 3793/10^9. The original
graded top-margin geometry has ceiling
50/(651 sqrt(28248)), whose square is exactly 625/2992882662 and is
less than (0.000457)^2. These are smaller than 1/1000. The trans/statL
conclusions retain the original top margin. The uniform weight extensions
in [N4-395](audit record weight_uniform_budget_peer, proof) retain their
specified floors and constants. They are not statements about arbitrary
new weights, an improved inverse, a different chart, or every dyadic scheme.

For reference 001, a separate annular argument is stronger:
[N4-397](audit record candidate001_affine_peer, proof) excludes its entire
affine class rho+L2 for every real c and every constant background
velocity. It imposes no symmetry or smallness on h. Non-L2 corrections,
other tails and linear velocity backgrounds are outside that theorem.

The following strict distance floors are all accepted. Their exact
source links and 2023 direct dependency comparisons were checked in
[N4-387](audit/numerical_audit/research_code/final_table_trace/DISTANCE_PROOF.md), with subsequent
safe report displays checked in N4-411. Each row uses its named probe;
no maximum over every possible probe is claimed.

| Reference suffix | Strict lower bound on ||h||2 | Principal audit |
|---|---:|---|
| 007 | 0.004769166867 | N4-157 |
| 008 | 0.036323397462385412 | N4-238 |
| 009 | 0.016967603956 | N4-183 |
| 010 | 0.022479506978 | N4-215 |
| 012 | 0.018641021007 | N4-188 |
| 013 | 0.00199234339 | N4-204 |
| 014 | 0.00198301351067 | N4-224 |
| 015 | 0.003033479200692324 | N4-383 |
| 016 | 0.001470360924123708 | N4-253 |
| 017 | 0.00167183069831928 | N4-267 |
| 018 | 0.00165582579205606 | N4-276 |
| 019 | 0.001661806967193251 | N4-290 |
| 020 | 0.001855374677442712 | N4-299 |
| 021 | 0.001864696854799172 | N4-320 |
| 022 | 0.00135251075726327 | N4-334 |
| 023 | 0.002634958245163687 | N4-350 |
| 024 | 0.001556067368832641 | N4-359 |
| 025 | 0.002065801265578052 | N4-371 |
| 026 | 0.001355907204057457 | N4-379 |

The deterministic inequality remains valid when a probe appeared in an
optimizer objective. In particular, 014's displayed (21,522) probe was
an objective row. The later 25-probe register and each analytic-span
check have their own source-bound scope. Statistical blindness and a
necessary mathematical inequality are different claims.

## Complete residual norms

Define

    H(F) = sup {|int F phi| : phi in C_c^infinity(R2), ||grad phi||2 <= 1},
    G0 = ||F||2, G1 = ||grad F||2,
    P2 = ||(1+4|X|^2)^(2/5) D2 F||2,
    E2(F)^2 = P2^2 + 2^14 G1^2 + 2^18 G0^2
                         + (20/21) 2^18 H(F)^2.

D2 is the ordered Cartesian Hessian with its Euclidean tensor norm.
Every bound below covers the entire plane.

| Exact reference | H(F), strict containing interval | E2(F), strict containing interval |
|---|---:|---:|
|007| (0.635524375, 0.635532270) | (606.818151, 606.820219) |
|016| (0.616733500, 0.617897369) | (628.580088, 628.865389) |

The 007 bounds are accepted in N4-249/252. Its full G0, G1, P2 and Q3
certificates also support four two-sided fractional forcing intervals.
The exact rebalanced threshold is 3/327680; a nearest decimal is not
substituted for it. The finer own H expansion from N4-156 retains its
separate independent-review status. The coarser accepted interval above
is sufficient for every comparison here.

The 016 G0, rF, G1 and P2 components are independently accepted in
[N4-392](audit record candidate016_scaled_norm_peer, proof). Sixteen full
dual and divergence-free trials at odd frequencies 1 through 31 were
reconstructed from the exact residual in N4-416. The calculation retains
2130 radial integral groups with 4096-bit arithmetic and 650-digit
containing exports. Distinct frequencies are combined orthogonally;
two trials at the same frequency are selected by a maximum, never added.

The full source has 160 odd angular modes, through frequency 319.
The uncomputed modes in the complete upper bound are retained by the
positive-coefficient Hardy formula in
[N4-431](audit record candidate016_multimode_complete_bounds, proof).
It uses the accepted complete ||rF||2, 32 individual Hardy integrals
through frequency 63, and minimum omitted frequency 65. All 128 omitted
modes retain a positive tail bound. N4-430 replays 920 Hardy integral
groups; N4-431 passes 4,446 checks with 361 input bindings. The earlier
prefix31 and prefix47 bounds remain valid. T4-486 independently checks
the trial energies and exported groups; T4-488 and N4-421 reconcile the
earlier containing endpoints, recording a positive upper-square
difference below 10^(-500). T4-498 accepts the prefix47 refinement.
T4-502 accepts the final prefix63 replay at 8192 bits.
[N4-433](audit record final_peer_acceptance, proof) verifies all 32 exact
interval comparisons and reconciles both complete upper squares.

The sharper exact endpoints in those records prove

    E2(016) - E2(007) > 21.759869526341,
    H(007) - H(016) > 0.017627007636152781.

[N4-393](audit record candidate016_full_forcing, proof) separately compares
all five registered X_(s,w) norms at identical parameters and proves
X_(s,w)(007)<X_(s,w)(016). All ten specified sufficient scalar forcing
tests fail for 016. These are failures of sufficient forcing hypotheses;
the correction-distance exclusions have their independent weak proof.

For the fixed sharpw norm at s=1/5184 and w=(2^15,2^20),
[N4-415](audit record sharpw_fixed_norm_optimum, proof) checks the exact
maximum allowed by the stated sufficient radius estimate:

    eta* = 40722836401/193491763200000,
    r* = 201799/149299200.

The accepted 007 forcing lower bound exceeds eta* by a factor greater
than 3594606. This optimizes one sufficient estimate in one fixed norm,
not the inverse constant or the tolerance across different spaces.

## Candidate 017 and background margins

[N4-426](audit record candidate017_final_reciprocal, proof) accepts the
independent T4-495 replay of all 16 dual floors and both completed
residual-mode endpoints. It directly rehashes all 16 mode files and
22 group files. The complete H upper bound and E2 remain open.

[N4-425](audit record candidate017_dual_residual_replay, proof) completes
all 16 proposed dual trials and residual trials only for frequencies 1
and 3. The source-specific calculation used 1,339 complete moment groups
and passed 5,704 checks at 17:42:23Z. It establishes

    H(017) > 0.614419598760047422137134027058.

The standalone proof gives the exact trial functions, endpoint assumptions
and residual-square identity. Only two individual modes have independently
reproduced residual enclosures. This lower bound needs no unverified
complete Hardy norm for 017.

[N4-432](audit record candidate017_opus_residual_review, proof) accepts
the main residual-identity and gradient-completion arguments of both
Opus lanes, T1 R1-053 and T2's independent review. Every one of the
2,174 exact potential generators is smooth at the origin; the residual
is odd in y and O(r), which supplies local integrability for each angular
projection. Exact manufactured examples and all 16 saved T1 endpoint
extracts agree. T2's first review omitted n from an auxiliary cross bound;
the correct expression is n sqrt(Qn(a+d)). An exact n=3 example refutes
the old expression. This correction changes no residual identity or
accepted candidate endpoint. N4-433 and T4-503 accept the corrected
18:14Z review; the literal repair and source-origin request are closed.

[N4-413](audit record candidate017_conditional_totals, proof) confirms the
finite arithmetic that would follow from the proposed full source
bounds: H in (0.6144195987,0.6165956396), E2 in
(605.4068697,605.9589546), and E2(007)-E2(017)>0.8591. Those are
conditional numerical implications. Fourteen residual trials and
158 of the 160 complete Hardy-mode inputs remain unreproduced, together
with the complete G0/G1/P2 source premises. Therefore the actual 017 upper bounds and actual E2 ordering
are not certified here. Agreement of a FLOAT proxy with these intervals
would not discharge any missing premise.

The complete background cover for 017 is independently accepted in
[N4-329](audit record candidate017_complete_cover_peer, proof). With

    theta = sup_X (|grad rho(X)|-rho_y(X))/2,

it proves theta<=2/25 and, using the accepted structured commutator
upper kappa<0.729080538628955349, the low-space rate
c0+1-theta-kappa>2.00123867. The 247-leaf rational Bernstein cover includes
the origin, angular edges and the limiting infinite-radius edge.
For 007, the accepted full-plane bounds similarly give theta<=2/25,
kappa<0.72816468018232542729 and rate>2.00215453001767. These background
estimates do not supply the separate high inverse or nonlinear closure.

N4-273/304 independently locate the 016/017 background-norm discrepancy:
more than 99.998 percent of the omitted squared kappa lies outside the
saved finite radial mesh. The small remaining annulus discrepancy does
not isolate quadrature error from rounding or endpoint effects.

The separately registered origin-inverse dyadic test fails for 015,
016 and 017 on all seven cells, with strict minimum ratios respectively
1.242922259074, 1.253908386497 and 1.221854480167 (N4-382,355,389).
These conclusions retain all realization, partition, input, plateau
and absorption hypotheses in their standalone proofs. They are not
unconditional nonexistence results or full residual upper norms.

## What the numerical audit changed

Exact far-field identities matter even when pointwise errors are tiny.
Rounding the saved 007 coefficients to binary64 changes 421 coefficients
and introduces a nonzero forbidden sector. That rounded mathematical
residual is not unweighted L2, whereas the exact rational snapshot has
the accepted cancellations. The stationary recurrence through order 16
has an independent 3060-coefficient check. Neither a finite recurrence
nor the last retained asymptotic term bounds an omitted remainder.
N4-220/221 explicitly detect the nonzero omitted term in the saved finite
first-mode tail model and compare the complete pairings.

Angular resolution is another distinct issue. Ideal midpoint exactness
is proved for the finite angular bandwidth, with separate requirements
for rotation-invariant norms and individual derivative components.
This does not bound floating arithmetic or radial quadrature. MID8
reverses some saved 007 weak-pairing signs; the accepted MID24/MID32
finite comparisons concern that frozen test list only. The negative-norm
Green split also had a factor-two error in its outer-outer term; N4-067
provided an exact counterexample and N1 corrected the implementation.

The 2982 original 007 coordinates have potential rank 1922 and 1060
zero-potential directions. The 421 linear tail/center constraints have
rank 421; adding the five nonlinear Taylor differentials gives rank 426.
Thus 1496 is the physical homogeneous differential dimension, not a
claim that the saved candidate satisfies all nonlinear Taylor equations.
N4-419 independently proves

    2.0899e-11 < [y^4](F/y)(0,y) < 2.0900e-11,

while the constant coefficient is exactly zero. The universal saved
Taylor tolerance of 2e-13 was refuted. Exact coordinate reduction removes
representation redundancy; it does not certify a PDE inverse or improved
conditioning. Positive damping and finite optimizer trials likewise do
not bracket the undamped solution or prove a minimum over a function span.

N4-420 verifies all 600 printed values/factors in eight final-report
25-probe comparisons. It also identifies six errors of scope, stage or
provenance, including the full 013 first-mode reduction range and the
023 final-versus-12-step range. The exact serialized-decimal comparisons
are evidence about the saved FLOAT data, not PDE bounds. The full findings
and wording repairs remain in the ledger and team notes. N4-422
identified two remaining literal defects: the 09:13 hash attribution and
the largest-four probe label. N4-424 accepts both repairs in the 17:36
report after exact ranking within each mode and across the full register.
N4-423 accepts T4-490 and T4-492 after a complete exact Cartesian jet and
finite ratio replay. All five saved 007 Taylor coefficient magnitudes
exceed 2e-13.

[N4-429](audit record final_threshold_displays, proof) checks the repaired
007 threshold quotients using exact 1/163840 and 3/327680. The resulting
integer floors are 84699685 and 66246337. The old X3 display 84699902
is refuted as the quotient of the same saved lower comparison by its
exact threshold. This is a transcription finding, not an upper bound
on the unknown actual norm; it changes no candidate verdict.

## Verification limits and handoff

Every accepted claim retains exact JSON inputs, standalone proof, code,
precision and an immutable result. The full source formulas, endpoint
convergence and outward moments are mathematical premises. File hashes
alone do not prove imported data. The final [selected integrity index](the N4 evidence index v03)
was frozen at18:30:07 UTC and checked at18:30:11. N4-435 accepts49 roots
and7497 direct local bindings, with1924 input files and no errors. The245
external provenance edges are listed but not rehashed. This finite byte
audit does not check unlisted transitive inputs or promote a mathematical
condition. Its result SHA256 is
1151786f8b4a324273c5914311301f9bbfae7ea68f00329bfd8c0628ca9e570d.

The 016 production fixture initializes copied peer modules, as disclosed
in N4-347. Its actual field, derivative and norm routines are independent
own code. Later trial, report and composition checks explicitly record
when no peer program was executed. The 017 proposed residual vectors
carry a historical code hash different from the current copied source;
that execution provenance is unobserved. Their mathematical values can
still be checked independently from the exact vectors and formulas.

Failed schema assumptions, outward-export repairs and earlier incorrect
wording are retained with real timestamps. They are not rewritten into
successful runs. The last source-integration worker completed frequency 63 at
18:07:23Z and its guard stopped it at 18:07:25Z. All computation in this
lane is local on CPU57 at nice19,
with one busy worker and one library thread. No JavaScript/TypeScript,
server, cluster, remote compute, GPU, Lean/Lake build, commit, push or
online posting is used. Source and peer lanes remain read-only.

The loop began at 2026-10-28T20:31:41Z; exact shift boundaries are in
[session log](session log). Pauses and wall time are separated
from computational claims. Team stop is 2026-10-29T19:30:31Z, followed
by the coordinator's report hour. No padded 24-hour runtime is claimed.

Opus collaboration has continued through the existing T1, T2 and
coordinator files, with independent T4 comparisons and follow-ups on
rounding, endpoint cancellation and formula scope. Their configured
model is us.anthropic.claude-opus-5-5; this lane cannot inspect a returned
provider model identifier and makes no stronger identity claim.

## Final enclosure width

N4-434 confirms R1-054's exact width decomposition from the accepted
016 records. With the low-mode bounds fixed, the modes1 through31
contribute between68.25% and68.35% of the final squared enclosure width.
Further Hardy modes can remove at most the remaining term in this
construction. That low-mode gap combines the dual lower-trial error,
the solenoidal upper-trial error and interval widths. The decomposition
does not attribute it to the dual lower trial alone. The standalone
[proof](audit record candidate016_width_decomposition, proof) gives two
exact Hilbert-space examples that separate these errors. No accepted
016 endpoint changes.

## Final report audit

The coordinator's frozen report and matrix v175 received a finite numerical
audit in N4-437: 3278 checks and 1258 local bindings, covering all 108 primary
candidate/status labels, selected distances, factors and complete norm
displays. [the N4 final numerical audit](the N4 final numerical audit)
gives the exact scope and line-numbered repairs. It does not claim a fresh
recomputation of every historical table number.

N4-438 refutes the attribution of 72/14/14 percent to the squared sharpw
norm in two report passages. Those shares belong to the unregularized
comparison E_star with weights 2^14 and 2^18. The actual fractional sharpw
G0 contribution exceeds one quarter. T4-509 independently confirms this;
N4-440 checks both propagations and all twelve original share endpoints.
The fractional P2 and G1 shares remain uncomputed.

N4-439 requests a second literal repair: the table heading should say
"residual value or bound", because some entries are nearest-rounded
summaries rather than directed bounds. Its 342 checks confirm the
reported elementary 007 lower bounds, complete background cover and four
N_s intervals, five matched 007/016 norm orderings, and three dyadic
minimum floors. The accepted d2 G0 and 016 rF upper endpoints both lie
below the corresponding nearest-rounded displays. Explicit strict lower
bounds still require directed rounding.

Neither repair changes an accepted norm, ratio or candidate verdict.
N4-436 also confirms that the final N1 report differs from the previously
audited version only in its header: all 600 saved FLOAT probe displays
are unchanged. The 49-root integrity index remains the immutable H22
index through N4-435; these later finite audits are separate additions.

# Two-fold non-axisymmetric self-similar profiles of 3D Euler with 0.4 < c_l < 0.5: final report

Report version: final, 2026-10-23, written at the end of the run (T_end 08:24:15 UTC).

## Summary

**Final status.** Primary target (an exact, smooth, globally decaying, genuinely two-fold profile with
0.4 < c_l < 0.5): **RIGOROUS OBSTRUCTION UNDER EXPLICIT ASSUMPTIONS**. Numerical search: **NO ACCEPTABLE CANDIDATE
FOUND IN THIS SEARCH**. The task's minimum of 96 hours of measured active numerical time was **not met**.

- *Proved result.* Theorem L2 (section 3): for 0 < c_l < 1/2, every C^2 solution of the stationary profile equations
  on R^3 with U = o(|y|) uniformly has zero vorticity and constant velocity, and U = 0 if U decays. This covers the
  whole primary class, with or without the constant axial recentering, and every positive c_l <= 2/5, with no assumption on
  the stagnation set, symmetry, axis vorticity or tail beyond global decay. It does not cover c_l >= 1/2, non-C^2
  profiles, velocities that are not uniformly sublinear, other ansatzes (anisotropic, discretely self-similar,
  rotating, multi-center) or approximate solutions. It is a written proof, not a machine-checked one. An independent
  verifier and an external referee (a second model) each wrote a complete proof; these were cross-audited and then
  reviewed line by line, in a hostile review (no counterexample; two presentation gaps repaired) and for scope.
- *Best numerical evidence.* 77 independently evaluated checkpoint files at fixed c_l in {0.41, 0.43, 0.45, 0.47,
  0.49} and the control 0.50 have resolved n = 2 content and none is affine, but their worst-region relative momentum
  RMS is 0.129 to 0.333, against the screening goal 10^-3. The best primary state (second representation, fixed input
  c_l = 0.43) fails worst on 1 < R < 2 with 0.148, and at R = 4096 its residual is 59 times the nonlinear terms.
  These are approximate states, not profiles.
- *Endpoints not reached.* No strong or preliminary candidate. No exponent resolved below 1/2: every c_l was a fixed
  input and no free-exponent refit was run. No constraint-removal, refinement or whole-space certification study.
  No progress snapshot at 24, 48, 72 or 96 active hours.
- *Exact remaining gap.* Within the hypotheses of L2 the primary question is settled, by an informal proof. Open:
  whether an exact smooth decaying m = 2 profile exists at c_l = 1/2 or for some c_l > 1/2, where the argument of L2
  fails (section 3.3); only a short c_l = 0.50 calibration was run and nothing above 1/2. Also open: a computed
  residual floor for approximate solutions below 1/2 (one exists under uniform bounds, value unknown, section 3.5).
- *End of run.* T0 = 2026-10-23 06:13:20 UTC (start of the run, with no code, checkpoint or ledger in place);
  T_end = 2026-10-23 08:24:15 UTC; elapsed 2 h 10 min 55 s. Training stopped at 07:47 UTC under the task's rule that
  a proved, independently checked obstruction covering the whole search class supersedes further blind search.
- *Measured active time.* From the campaign ledger, the union of non-overlapping credited training intervals lies
  between 0.999 and 1.180 hours (between 1.144 and 1.326 hours with the independent validation intervals), 1.0 % to
  1.4 % of the required 96 hours. The 96-hour minimum was not met (section 5).
- *Continuation.* The resume command in the accompanying artifacts restarts the c_l = 0.50 queue (section 9).

This is the first published report for this case. The independent verifier validated sections 0 to 9 in their
pre-publication form (33 report-level checks, 124 table comparisons, none refuted). Publication added this summary
and the end-of-run record and matched the artifact list to the accompanying artifacts; no
result or number changed, and these edits were not audited again.

## 0. Final status

Evidence base. The numerical evidence is the final frozen snapshot of 2026-10-23 07:57 UTC, taken after all
training had stopped (07:47 UTC) and all independent validation had finished (training ledger of 64 records, SHA256
prefix 9f9477b05b19cafb; validation ledger, SHA256 prefix f596f809df539d3a; independent checkpoint table of 77
evaluated checkpoint files, SHA256 prefix 9f6b5d16fae9af40). Only results checked by the independent verification
code and audits are reported as results. The code, configurations, selected checkpoints, ledgers, proofs, audits and
validation evidence are in the accompanying artifacts.

**Primary target: RIGOROUS OBSTRUCTION UNDER EXPLICIT ASSUMPTIONS.** Theorem L2 (section 3) rules out every nonzero
exact C^2, globally decaying, time-independent self-similar profile of the 3D Euler equations on R^3 with
0 < c_l < 1/2. This includes the task's entire primary target: smooth, globally decaying, genuinely two-fold (m = 2)
profiles with 2/5 < c_l < 1/2 in the prescribed isotropic single-scale ansatz centered on the z-axis, together with
the permitted constant axial recentering. It also covers c_l = 2/5 and every 0 < c_l < 2/5. The theorem makes no
assumption on the stagnation set, the symmetry, the vorticity on the axis, paired off-axis peaks or the tail beyond
global decay; uniform sublinear growth U = o(|y|) already forces U to be constant. It does not exclude the
c_l = 1/2 calibration or candidates with c_l > 1/2. It gives no numerical residual threshold, and it is not a general
obstruction to Euler or Navier-Stokes blowup by other mechanisms (anisotropic, discretely self-similar, rotating or
multi-center profiles, or profiles that are not C^2). The proof is written mathematics, not a machine-checked proof.
It is supported by two independent complete proofs, a line-by-line review, a hostile review by an external referee
(a second model) that found no counterexample (its two presentation gaps were repaired) and a separate scope
review (section 3.6).

**Numerical search: NO ACCEPTABLE CANDIDATE FOUND IN THIS SEARCH.** All 77 independently evaluated checkpoint files,
at fixed c_l in {0.41, 0.43, 0.45, 0.47, 0.49} and the control c_l = 0.50, fail the independent regional momentum
screen (the task's initial screening goal 10^-3) by more than two orders of magnitude: their worst-region relative
momentum RMS is between 0.129 and 0.333, and at least 0.148 strictly inside 0.4 < c_l < 0.5. These are approximate
states, not exact profiles. By L2 there is no nonzero exact decaying profile in the primary range for them to
approximate. A positive lower bound on the residual of approximate solutions holds only within classes with uniform
derivative and tail bounds, and its value is not known (section 3.5).

**Measured active numerical time: the required 96 hours were NOT completed.** The ledgers do not record the exact
boundaries of eligible numerical work, so only enclosures of recorded intervals are available. In the final ledgers
the union of credited elapsed training intervals lies between 0.999 and 1.180 hours, and the union including the 108
closed independent validation intervals lies between 1.144 and 1.326 hours. These intervals include some ineligible
time (checkpoint I/O, short pauses) and omit some eligible work, so they are not exact measures of eligible activity
(section 5). All training and validation intervals in the frozen ledgers lie between about 06:12 UTC, when the
campaign started with no code, checkpoint or ledger in any work directory, and 07:57 UTC on 2026-10-23, so no measure
of the active numerical time recorded in the frozen evidence can exceed 1.8 hours. A few short numerical runs took
place outside the frozen ledgers, after training stopped (checkpoint exports and software tests of revised training
code, section 5); they receive no active-time credit. Proof work, literature reading and report writing are not
counted. The campaign closes early under the task's rule that "a rigorous mathematical obstruction covering the whole
explicitly specified search class, if truly proved and independently checked, supersedes further blind numerical
work". It does not close because the numerical milestones were completed: most of them were not (section 8). The
secondary questions (c_l = 1/2, c_l > 1/2) remain open. Section 9 describes how the numerical queue is resumed.

### Answers to the required questions

1. *Did we obtain a genuinely non-axisymmetric m = 2 candidate?* No. Trained states have a resolved n = 2 signal
   (n = 2 fraction of sampled core ring energy 0.35 to 0.69 across states, and 0.66 of the physical-volume velocity
   energy on R < 1 for the selected checkpoint) and are not affine, but every one fails the momentum equation by
   13 % to 33 % relative RMS in its worst region. In the primary range no nonzero exact decaying profile of this kind
   exists (Theorem L2).
2. *Is c_l numerically resolved below 1/2?* No. Every run used a fixed input c_l, and a fixed input is never reported
   as a resolved exponent. No free-exponent refit was run. In the primary range there is no nonzero exact decaying
   profile, and so no exponent to resolve.
3. *Does the candidate survive removal of artificial nondegeneracy constraints and refinement?* This was not tested,
   and no acceptable candidate was found. No additional anti-axisymmetry penalty was used. A soft sampled amplitude
   penalty was retained: the 16-norm of |U| over 2048 fixed core points was pushed toward 1 with weight 1. It
   discourages collapse to zero but does not exclude zero or fix the true maximum of |U|. The representation imposes
   the exact m = 2 symmetry, exact incompressibility, algebraic envelopes and the pressure gauge P -> 0 at infinity.
   No refinement series was run (section 8).
4. *What is the worst validated region?* For 71 of the 77 evaluated checkpoint files it is the physical shell
   1 < R < 2. The other six fail worst on 0.25 < R < 1: two files of an early state (75 steps) and four late pilot
   files (steps 4624 to 5726). The selected checkpoint (section 6) has relative momentum RMS 0.148 on 1 < R < 2 and
   relative pressure-Poisson RMS between 0.62 and 0.87 on every shell beyond R = 2.
5. *Is the tail credible?* No. At R = 4096 the ratio of the momentum residual to the nonlinear terms is 3.0 x 10^4 to
   2.5 x 10^6 for the first representation, and 1.5 to 108 in the primary range and 0.80 to 1.17 at c_l = 0.50 for the
   second. The diagnostic tail screen of the independent validation is 10^-2; it is our choice, not a threshold set by
   the task.
6. *What prevents a stronger conclusion?* For the primary target the question is settled by L2 within its stated
   hypotheses. The limits are that the proof is informal and that its hypotheses (C^2 on all of R^3, uniform
   sublinear growth or global decay, the stationary isotropic single-center ansatz) define the class it covers. For
   the secondary questions (c_l = 1/2, c_l > 1/2) only a short calibration was run at c_l = 0.50, with no acceptable
   state, and nothing above 1/2 was run. The recorded numerical activity is about one hour, far below the planned 96
   hours, and no refinement, free-exponent, alternative-seed, alternative-optimizer or whole-space certification step
   was carried out.

## 1. Problem and conventions

With tau = T - t, the similarity ansatz u = tau^(c_l - 1) U(y), p = tau^(2c_l - 2) P(y), y = (x - x_*)/tau^(c_l),
gives the profile equations

    (1 - c_l) U + (c_l y + U)·grad U + grad P = 0,   div U = 0   on R^3,

with the two-fold symmetry U(Qy) = Q U(y), P(Qy) = P(y), Q = diag(-1, -1, 1). A constant axial drift C e_3 in the
transport term is equivalent to a shift of the center along e_3 and is removed in the canonical frame. The natural
far-field degree of U is d = 1 - 1/c_l, which lies in (-3/2, -1) for 2/5 < c_l < 1/2. A nonzero natural degree-d
leading tail is not square-integrable at infinity, and U in L^2(R^3) is not required. If an exact profile had a
nonzero leading tail U(R theta) = R^d a_inf(theta) + o(R^d), formal matching would give the blowup-time limit
|x - x_*|^d a_inf((x - x_*)/|x - x_*|) away from x_*. For a nonzero smooth angular coefficient a_inf this is locally
square-integrable near x_* if and only if c_l > 2/5. This scaling calculation does not construct a blowup solution.
"Genuinely m = 2" means a resolved
nonzero n = 2 cylindrical Fourier component relative to the error. The equations document in the accompanying
artifacts contains the conventions, derivations, gauges, axis regularity conditions, tail expansions and the list of
false solutions. Its check log records 33 passing symbolic checks, and an independent audit examined the equations
claim by claim.

## 2. Sources and what was borrowed

The method follows Ganeshram-Duruisseaux-Anandkumar (arXiv:2609.10867 v2) and Wang-Liu-Li-Anandkumar-Hou
(arXiv:2506.19243 v1): direct residual minimization of the stationary profile equations in FP64, symmetry by output
symmetrization, constraints against the trivial solution, wide-range sampling, staged optimization and separate
validation by region. The axisymmetry, the exponent 1/2, the local outgoing property at stagnation points and the
source-specific parities and boundary conditions were not borrowed. Optimizers: the configured pipeline is Adam
stages followed by standard L-BFGS. Only Adam steps were executed in any run. SS-eSOAP
(arXiv:2608.29448) and SS-Broyden are neither implemented nor claimed. The restrictions of Constantin-Ignatova-Vicol
(arXiv:2602.17570 v3) were checked against their hypotheses; none of them excludes the m = 2 class with
0.4 < c_l < 0.5 under the task's assumptions alone. Theorem L2 below is a separate proof. Versions, hashes and the
borrowed-versus-changed table are in the source notes in the accompanying artifacts.

## 3. Theory

Notation: c = c_l, V = c y + U, A = grad V = cI + grad U, S the symmetric part of grad U, Omega = curl U,
N_V = {V = 0}, lambda_max(S) the largest eigenvalue of S, E = {p in N_V : lambda_max(S(p)) >= 1}.

### 3.1 Statement

**Theorem L2.** Let 0 < c < 1/2. Let U and P be C^2 on R^3 and solve the profile equations, with U(y) = o(|y|)
uniformly as |y| -> infinity. Then Omega = 0 and U is constant. If U -> 0 at infinity, U = 0 and P is constant.

Nonzero constants U = b with P = -(1 - c) b·y are exact sublinear solutions, so "constant" cannot be improved to
"zero" without decay. Theorem L1 is the earlier version of the result. It assumes in addition that N_V is countable,
and L2 supersedes it.

### 3.2 Proof outline

1. Trapping. Sublinearity gives V·y >= c|y|^2/2 outside a ball, so the flow dY/ds = V(Y) is global and every
   backward trajectory stays in one compact ball.
2. Bernoulli Lyapunov function. H = |V|^2/2 + P + c(c - 1)|y|^2/2 satisfies grad H = -[(1 - 2c) I + Omega x] V, hence
   dH/ds = -(1 - 2c)|V|^2 along trajectories. Every backward limit set alpha(a) is therefore a nonempty, compact,
   connected, invariant subset of N_V on which H is constant.
3. Vorticity transport. Along trajectories Omega' = (grad U - I) Omega, so
   d|Omega|^2/ds <= 2(lambda_max(S) - 1)|Omega|^2. If alpha(a) avoids E, then lambda_max(S) <= 1 - eta near alpha(a),
   and integrating backward gives Omega(a) = 0. Hence every point with Omega != 0 has a backward limit set meeting E.
4. Spectrum on E. At p in E, A(p) has rank at least 2, a positive eigenvalue and an eigenvalue with negative real
   part. If Omega(p) != 0, then grad U Omega = Omega at the zero, so A has the eigenvalue 1 + c, and its other two
   eigenvalues have sum 2c - 1 < 0. If Omega(p) = 0, grad U is symmetric and trace-free with largest eigenvalue >= 1,
   so A has an eigenvalue >= 1 + c and one <= c - 1/2 < 0.
5. Backward limit sets meeting E are single points. Near p in E, N_V is an isolated point or a closed subset of a C^2
   arc (implicit function theorem). If alpha(a) contains p but is not {p}, connectedness forces it to contain a
   nondegenerate arc J of equilibria close to p. At a point q of J close to p, A(q) has simple real eigenvalues
   lambda_s < 0 = lambda_0 < lambda_u. Since the bracket in step 2 is invertible at zeros, the Hessian of H at q has
   the kernel of A(q) and is nondegenerate transversally. This gives |H - h|^(1/2) <= C|grad H| near q, where h is
   the value of H on J, and with |grad H| <= C'|V| it bounds the remaining backward path length after a late return
   near q by a constant times |H - h|^(1/2). The orbit is then trapped near q and converges to one point,
   contradicting J being contained in alpha(a). A second, independent argument uses variation of constants in
   coordinates that flatten J.
6. Null graphs. For each p in E, because A(p) has an eigenvalue with negative real part, there is a neighborhood B_p
   such that the points whose backward orbits stay in B_p lie on a Lipschitz graph over a subspace of dimension at
   most 2, a Lebesgue null set. This is a weighted contraction estimate in an adapted direct-sum norm; no
   hyperbolicity is assumed.
7. Conclusion. E is compact and is covered by finitely many such neighborhoods. Every a with Omega(a) != 0 converges
   backward to a point of E, so for some integer n the point Y(a, -n) lies on one of finitely many null graphs. Hence
   {Omega != 0} is contained in a countable union of images of null sets under C^1 diffeomorphisms, which is a null
   set. It is also open, so it is empty. Then U is divergence-free and curl-free, hence harmonic, and o(|y|), hence
   constant by the Liouville theorem.

### 3.3 Where c < 1/2 is used, and what happens at c >= 1/2

The hypothesis c < 1/2 enters three times: 1 - 2c > 0 makes H a strict Lyapunov function and the bracket in step 2
invertible; the eigenvalue sum 2c - 1 is negative at vortical zeros; and c - 1/2 < 0 at irrotational points of E. At
c = 1/2, H is conserved along trajectories and backward limit sets need not lie in N_V (an exact rotating affine
example has circles as backward limit sets). For c > 1/2, vortical stagnation arcs can attract backward
trajectories (an exact stagnation-line affine example does so), and irrotational exceptional zeros can have rank
one. This argument therefore gives no obstruction for c >= 1/2. It does not show that exact profiles exist there.

### 3.4 Scope

L2 covers exact, time-independent solutions on all of R^3, with or without the constant axial drift, that are C^2
everywhere and uniformly sublinear. The following are not needed: an assumption on the stagnation set (isolated
points, curves, surfaces or Cantor-like sets), axis vorticity, any symmetry (the m = 2 symmetry is not used), the
angular tail structure, an algebraic decay rate (any global decay implies sublinearity), analyticity at infinity, or
finite total energy. The theorem does not apply to the following:

- profiles that fail to be C^2 at some point;
- velocities that are not o(|y|), for example nonconstant affine backgrounds;
- fields for which only decay along individual rays is known, so that uniform sublinearity U = o(|y|) is not
  established (raywise decay alone does not verify the growth hypothesis);
- time-dependent, discretely self-similar, rotating, anisotropic or multi-center ansatzes;
- approximate solutions.

### 3.5 Approximate solutions: a positive but uncomputed residual floor

Fix 0 < c < 1/2, d = 1 - 1/c and K >= 1. Let F(c, K) be the set of divergence-free U in C^3(R^3) such that

- |D^j U(y)| <= K (1 + |y|^2)^((d - j)/2) for j = 0, 1, 2;
- the sup norm of D^3 U is at most K;
- the sup norm of D^2 U equals 1 (a scale gauge).

Then there is eps_0(c, K) > 0 such that the sup norm of the momentum residual is at least eps_0 for every U in F(c, K)
and every C^1 pressure P. The proof is by compactness and contradiction with L2. The constant is not computed. The
bound on D^3 U is one sufficient form of control on D^2 U; some uniform control of this kind is necessary, because
rescaled compactly supported fields have residual tending to zero while D^3 U blows up. The consequence for numerics
is limited. A sequence of normalized fields at fixed c < 1/2 whose whole-space momentum residual tends to zero in the
sup norm must leave every such class. A decreasing training or holdout loss proves nothing by itself: it is a sampled
relative quantity, and it may decrease toward a positive floor. Without uniform control, L2 implies no floor at all:
U = eps W, with W smooth, compactly supported and divergence-free and P = 0, has residual tending to zero and the
trivial limit.

### 3.6 Review evidence and relation to the literature

- The independent verification produced a complete proof, using variation of constants for the capture step. An
  external referee (a second model) wrote a second complete proof, using the Bernoulli Hessian. The two proofs were
  cross-audited line by line.
- A further line-by-line review covered both proofs and the reconciled written proof. Repairs from this review: the
  choice of chart in the topological step, and the choice of q near p so that the saddle spectrum persists.
- A hostile review by the external referee tested the proof against exact solution families: rotating strain,
  stagnation lines, rank-one affine fields, shears, Beltrami fields, periodic fields, two-dimensional three-component
  fields and singular axial fields. Its verdict was "proof correct with repairable gaps", with no counterexample and
  no missing hypothesis. Both gaps were repaired: an explicit adapted norm in the null-graph estimate, and an explicit
  first-exit argument in the optional second capture argument. The independent verification checked both repairs.
- A scope review by the external referee compared the hypotheses with the task specification and confirmed the
  coverage stated in section 0, including the recentering and c_l = 2/5.

Closest checked predecessor: Constantin-Ignatova-Vicol, Theorem 3.9. It assumes a finite stagnation set and the local
outgoing property at every stagnation point; L2 needs neither. Chae (2007) needs small-p integrability of the
vorticity, Chae-Shvydkoy (2013) and Bronzi-Shvydkoy (2015) need L^p-type assumptions, and Chae-Wolf (2023) treats
c_l <= 2/5 (only its abstract was accessible). None of these covers 2/5 < c_l < 1/2 under the hypotheses of L2. This
was a bounded literature search, not a novelty claim. The full proofs, the audits and the dated audit log are in the
accompanying artifacts.

## 4. Numerical method

The velocity is the curl of a vector potential A, so div U = 0 holds analytically. The learned vector-potential and
pressure corrections are FP64 tanh networks, symmetrized by F(y) -> [F(y) + Q F(Qy)]/2 for the vector output and
p(y) -> [p(y) + p(Qy)]/2 for the scalar pressure, so the m = 2 symmetry is exact; no additional parity is imposed.
The corrections are added to the smooth, divergence-free seed

    M = [[a, b, 0], [g, -1 - a, 0], [0, 0, 1]],   chi(y) = (1 + |y|^2)^(-1/(2 c_l)),
    A_seed(y) = -(chi(y)/3) [y x (M y)],   U_seed = curl A_seed,   P_seed(y) = -(chi(y)^2/2) y·[(M + M^2) y],

with (a, b, g) = (0.2, -0.4, 0.7) at initialization; these three parameters are trainable. The seed is an
initialization, not an exact profile. Two representations were run.

- First representation: unbounded logarithmic radial input and one envelope. It was later proved to force the learned
  leading far field to an axisymmetric swirl when all first-layer radial weights are nonzero, and it is kept only as
  a controlled baseline.
- Second representation: bounded inputs and two algebraic envelopes per field, building in the velocity degrees d and
  2d - 1.

Loss: region-stratified mean squares of the momentum residual over a core ball, logarithmic shells out to a maximal
radius (3000 in the main sweep), an axis tube and an origin ball, normalized by the linear-term scale R^d in the first
stage. Later stages move the normalization toward the nonlinear scale R^(2d - 1); only the pilot reached the second
stage (normalization R^(d + (d - 1)/2)). This loss is an optimization objective; it is not a physical-volume norm.
The scale gauge is a soft penalty (weight 1) that pushes a smooth-maximum surrogate of |U|, the 16-norm of |U| over
2048 fixed core points, toward 1; it does not fix the true maximum of |U|. The pressure gauge is P -> 0 at infinity.

Configured: fixed c_l in {0.41, 0.43, 0.45, 0.47, 0.49, 0.50}, the seed above and two other seed matrices
((a, b, g) = (-0.9, 0.8, -0.3) and (0.6, 0.5, 0.5)), and an off-axis paired-blob family. Executed: only the seed
above, at all six exponents (table in section 5). The other seed matrices and the blob family were queued and not
started.

## 5. Campaign execution and resource use

Hardware: NVIDIA A100-SXM4-80GB GPUs in FP64 for training; the runner assigned workers to two devices (the ledger
records the model and the arithmetic, not the device index). Independent validation ran on CPU with one thread. A
supervised, detached runner keeps a directory queue of experiments, writes atomic checkpoints (model, optimizer,
scalars, random-generator and sampler state) every 10 minutes and appends one ledger record per checkpoint interval.

Experiments executed (the seed of section 4 for every run; steps are Adam steps; every run stopped in its first or
second Adam stage):

| Experiment | Representation | c_l | Steps reached | Status when training stopped |
|---|---|---|---|---|
| pilot | first, width 64 | 0.45 | 5726 (second Adam stage) | stopped at 07:47 UTC |
| first-representation runs | first, width 96 | 0.41, 0.43, 0.47, 0.49 | 847 to 920 | held after the tail defect was proved |
| first-representation control | first, width 96 | 0.50 | 4402 | stopped at 07:47 UTC |
| second-representation runs | second, width 96 | 0.41, 0.43, 0.45, 0.50 | 7643, 6565, 7071, 7763 | stopped at 07:47 UTC |
| second-representation runs | second, width 96 | 0.47, 0.49 | 1271, 1399 | requeued at 07:10 UTC, not resumed |

Active-time accounting. The task asks for the non-overlapping union of active intervals across workers. The trainer
did not record exact boundaries of eligible numerical work. The enclosures below concern the elapsed intervals it
credited, not all eligible work.

- Early ledger records give rounded wall endpoints and an active-second count. Each is enclosed by a conservatively
  enlarged interval, and per-worker lower bounds are combined by a union-minus-missing-measure argument.
- Later records give credited chunks with millisecond endpoints, which are padded by 0.502 ms.
- The bounds are bounds on the union of elapsed intervals that the trainer credited. Credited chunks run between
  accepted optimizer step ends, so they include checkpoint I/O and short pauses. First steps and some long validation
  intervals are not credited.
- The figures are therefore not a certificate of eligible numerical activity in either direction. They also assume an
  ordered clock and the audited logging protocol.
- The independent validation intervals are closed wall intervals of validation tasks. They are not CPU time, and
  idle watcher time is excluded.

| Snapshot (UTC) | Training ledger records | Training union, hours | Training and validation union, hours |
|---|---|---|---|
| 2026-10-23 07:23 | 45 | 0.563 to 0.743 | not computed |
| 2026-10-23 07:32 | 51 | 0.731 to 0.911 | 0.775 to 0.956 |
| 2026-10-23 07:57 (final) | 64 | 0.999 to 1.180 | 1.144 to 1.326 |

The final row uses the frozen ledgers: 38 early records, 26 chunk records and 108 closed validation intervals. One
validation interval without a recorded end is excluded. In this row lower bounds are rounded down and upper
bounds up.

The sum of credited seconds over training workers, about 7.4 hours, counts concurrent work repeatedly and is not
the requested measure. The interim value "0.22 to 0.23 h" (16 records, 06:50 UTC) was not a valid enclosure: the
displayed endpoints were floored and did not contain every credited chunk. The corrected enclosure of the 22-record
ledger a few minutes later is 0.256 to 0.404 hours.

**The required minimum of 96 hours of measured active numerical time was not reached.** No 24, 48, 72 or 96 hour
progress snapshot exists, because those active-time milestones were never reached; none has been fabricated. Training
was stopped at 07:47 UTC on 2026-10-23, and the last independent validation process recorded in the frozen evidence
exited at 07:57 UTC. The campaign started at about 06:12 UTC on the same day with no code, checkpoint or ledger in any
work directory, and every training and validation interval in the frozen ledgers lies between these times. For the
frozen evidence, this wall-clock window, less than 1.8 hours long, bounds every measure of active numerical time,
independently of the ledger enclosures above.

Numerical runs outside the frozen ledgers. After training stopped, the last checkpoints of the second-representation
runs at c_l = 0.45 and 0.50 were exported with trainer-side audit files between 07:50 and 07:52 UTC. After the
evidence freeze, two short software tests of revised training code were run: an independent resume test of the
stage-transition repair (section 7) from 08:00:14 to 08:00:28 UTC in one CPU thread, and, according to the notes
kept with the training code, a 12-step test of the revised interval recording at about 08:09 UTC that wrote to a
separate test ledger. None of these runs was appended to a campaign ledger, none receives active-time credit, and
none is evidence about a profile.

## 6. Numerical results (independently validated)

Independent validation recomputes all residuals from the saved parameters with a separately written evaluator. It uses
explicit potential derivatives and fourth- and sixth-order finite differences in physical coordinates, with both
Cartesian and direct cylindrical differentiation. It samples 256 points in each uniform physical-volume shell, 1331
points on a core Cartesian grid, 129 points on the axis and 96 points on each far-field sphere. Grid and axis
statistics use their own diagnostic sample measures and are not volume norms. A relative RMS is the RMS of the
residual magnitude over the sample of a region, divided by the sum over the terms of that equation of the RMS
magnitude of each term. For the momentum equation the terms are (1 - c_l) U, c_l (y·grad) U, (U·grad) U and grad P
(the drift term is zero). Absolute values are in the units set by the scale gauge of section 4. The evaluator passed
32 calibration tests and nine synthetic decoder tests. On matched points it reproduces the trainer's saved metrics to
about 3 x 10^-13 relative (first representation) and 3 x 10^-8 relative (second representation). Quantiles and maxima
are sampled values, not rigorous supremum bounds.

Best evaluated state per representation and exponent (smallest worst-region relative momentum RMS among all 77
evaluated checkpoint files):

| Representation | c_l | Saved step | Worst relative momentum RMS (region) | Residual / nonlinear terms at R = 4096 |
|---|---|---|---|---|
| first (pilot, width 64) | 0.45 | 5726 | 0.172 (0.25 < R < 1) | 3.6 x 10^4 |
| first | 0.41 | 500 | 0.225 (1 < R < 2) | 2.5 x 10^6 |
| first | 0.43 | 500 | 0.210 (1 < R < 2) | 1.0 x 10^6 |
| first | 0.47 | 500 | 0.185 (1 < R < 2) | 1.8 x 10^5 |
| first | 0.49 | 500 | 0.186 (1 < R < 2) | 9.2 x 10^4 |
| first | 0.50 (control) | 4402 | 0.158 (1 < R < 2) | 3.0 x 10^4 |
| second | 0.41 | 6000 | 0.186 (1 < R < 2) | 99 |
| second | 0.43 | 6565 | 0.148 (1 < R < 2) | 59 |
| second | 0.45 | 4476 | 0.185 (1 < R < 2) | 20 |
| second | 0.47 | 1271 | 0.180 (1 < R < 2) | 4.5 |
| second | 0.49 | 1399 | 0.181 (1 < R < 2) | 1.5 |
| second | 0.50 (control) | 6667 | 0.129 (1 < R < 2) | 1.1 |

At each exponent the best second-representation state has a far-field imbalance three to five orders of magnitude
below the best first-representation state. In the three second-representation runs with several evaluated checkpoints
in the primary range the tail ratio increased from each evaluated checkpoint to the next: from 44 (step 500) to 108
(step 7643) at c_l = 0.41, from 5.8 (step 75) to 59 (step 6565) at c_l = 0.43, and from 7.5 (step 500) to 28
(step 7071) at c_l = 0.45. No state comes near the screens (the task's initial momentum screening goal 10^-3 and our
diagnostic tail screen 10^-2). The c_l = 0.50 controls reach somewhat lower residuals than the primary exponents. Step
counts and costs differ between runs and no matched-budget comparison was designed, so this is a descriptive sampled
comparison. It is not evidence for or against an exact profile at c_l = 1/2.

**Selected checkpoint.** It minimizes the worst sampled momentum defect among evaluated states strictly inside
0.4 < c_l < 0.5: the second representation at c_l = 0.43, saved step 6565 (the last step of that run), SHA256
prefix 0b690cfd0b74062c. A second file of the same saved state, prefix 572dc35c3762ab7d, gives the same values.
Residuals by region (sampled values; q99.9 is the 99.9 % sample quantile):

| Region | Momentum rel. RMS | Momentum abs. RMS | Momentum abs. q99.9 | Momentum sampled max | Vorticity rel. RMS | Pressure-Poisson rel. RMS | Divergence rel. RMS |
|---|---|---|---|---|---|---|---|
| R < 0.25 | 0.010 | 0.0042 | 0.0084 | 0.0084 | 0.100 | 0.016 | 1.6 x 10^-10 |
| 0.25 < R < 1 | 0.099 | 0.025 | 0.27 | 0.31 | 0.41 | 0.38 | 4.1 x 10^-11 |
| 1 < R < 2 | 0.148 | 0.015 | 0.18 | 0.23 | 0.56 | 0.83 | 7.3 x 10^-11 |
| 2 < R < 4 | 0.029 | 6.6 x 10^-4 | 2.3 x 10^-3 | 2.4 x 10^-3 | 0.036 | 0.62 | 1.5 x 10^-10 |
| 4 < R < 8 | 0.022 | 1.9 x 10^-4 | 7.2 x 10^-4 | 7.8 x 10^-4 | 0.020 | 0.84 | 1.1 x 10^-10 |
| 8 < R < 16 | 0.012 | 4.0 x 10^-5 | 2.2 x 10^-4 | 2.4 x 10^-4 | 0.0059 | 0.87 | 2.2 x 10^-10 |
| 16 < R < 32 | 0.0038 | 5.0 x 10^-6 | 2.0 x 10^-5 | 2.0 x 10^-5 | 0.0018 | 0.81 | 7.7 x 10^-11 |
| 32 < R < 64 | 0.0011 | 5.7 x 10^-7 | 2.1 x 10^-6 | 2.2 x 10^-6 | 3.8 x 10^-4 | 0.83 | 8.5 x 10^-11 |
| core grid | 0.091 | 0.016 | 0.18 | 0.19 | 0.42 | 0.32 | 1.1 x 10^-10 |
| axis | 0.016 | 0.0015 | 0.0074 | 0.0076 | 0.11 | 0.021 | 2.9 x 10^-10 |

Further independent checks of this checkpoint:

- Momentum: no region meets the screen of 10^-3; the outermost shell, at 1.1 x 10^-3, comes closest.
- Vorticity equation: worst relative RMS 0.56, on 1 < R < 2.
- Pressure-Poisson consistency: relative RMS 0.62 to 0.87 on every shell beyond R = 2, worst 0.87 on 8 < R < 16.
- Divergence: relative RMS below 3 x 10^-10 in every sampled region. The curl construction makes the divergence
  vanish analytically; the sampled value is finite-difference and roundoff error.
- Symmetry and structure: the Q-symmetry defect is exactly 0, and the core affine-fit remainder is 0.70. The
  defects of the x and y mirror reflections are 0.36 and those of the z reflection and of the full inversion are
  0.46 (relative), so the state has none of these additional symmetries.
- Angular content: the n = 2 fraction of the physical-volume velocity energy is 0.66 on R < 1 and 0.68 on
  8 < R < 16, and the n = 2 fraction of the vorticity energy is 0.34 on R < 1. The 32- and 64-angle core velocity
  energies differ by 4 x 10^-5 in absolute energy units (about 6 x 10^-4 relative).
- Three-dimensional variation: the smallest normalized eigenvalue of the core derivative Gram matrix is 0.081.
- Axis Taylor structure: consistent on the axis (horizontal axis velocity 0, off-block Jacobian RMS 2 x 10^-20).
- Coordinate cross-check: Cartesian and cylindrical momentum residuals differ by RMS 1.9 x 10^-13 on the tested
  points. In a derivative-step sweep over fourth- and sixth-order differences with steps 0.004 to 0.001, the momentum
  residual differs from the sixth-order, step 0.001 value by at most 1.5 x 10^-7 RMS. Together these support the
  sampled momentum defects; they are not a certified error bound for every derivative or point.
- Peak-vorticity identity: refined local vorticity extrema give stretching ratios -0.32 and -0.23, where an exact
  interior maximum requires 1.
- Stagnation points: a multistart search found 3 zeros of V from 31 starts, one on the axis and a Q-symmetric pair
  near |y| = 0.97. This is not a complete root count.
- Far field: from R = 8 to R = 4096 the residual falls from 1.8 % to 2 x 10^-7 of the full term sum, while its
  ratio to the nonlinear terms grows from 3.1 to 59, and the residual divided by R^(2d - 1) grows from 0.19 to 4.2.
  The built-in tail degree d makes the linear terms cancel at leading order, and they balance to high relative
  accuracy; the remaining residual is large compared with the nonlinear terms, so the far field does not balance at
  the nonlinear scale.

**Whole-space consistency.** This was checked on two early checkpoints by Newton and Biot-Savart quadrature through
radius 256, at three targets and two resolutions:

- Pressure: the gradient mismatch RMS is 0.021 for the first-representation pilot at step 500, and 0.020 to 0.021 for
  the second representation at c_l = 0.45, step 500. The mismatch persists under refinement in both cases, so both
  fail the finite-quadrature pressure comparison.
- Velocity: the Biot-Savart mismatch decreases under refinement, from 7 x 10^-4 to 6 x 10^-5 and from 5 x 10^-3 to
  3 x 10^-4.
- No analytic bound on the exterior or quadrature error is available, and the comparison was not repeated on the
  selected checkpoint.

**Training versus holdout.** For one checkpoint (second representation, c_l = 0.45, saved step 4476) the final
training batch was reconstructed exactly by replaying the sampler; the replayed generator state matched the saved one
byte for byte. At the same parameters, the relative momentum RMS on R < 1 is 0.103 on the 100 training points and
0.216 on the 61 holdout points (ratio 2.09); on 1 < R < 3 it is 0.073 versus 0.115 (ratio 1.59); outside R = 3 the two
agree within about 6 %. This is one finite last-batch comparison, not a statistic over training or a generalization
bound. Both sets fail the momentum screen in the inner regions. The holdout set was also used by the trainer for
checkpoint selection; the independent validation points above are separate.

## 7. Rejected artifacts and negative results

- The task seed is not a profile. Its worst relative momentum RMS is 0.347, on 1 < R < 2. Its far-field expansion
  contains a velocity correction of degree d - 2, whose residual decays more slowly than the nonlinear scale
  R^(2d - 1) when c_l < 1/2. Tail diagnostics are therefore reported at the nonlinear scale.
- The first representation's unbounded logarithmic radial input forces the learned leading far field to an
  axisymmetric swirl when all first-layer radial weights are nonzero (proved). The second representation removes
  this generic saturation, but exact balance still requires a combined degree d - 2 coefficient to cancel.
- A nonzero divergence-free homogeneous leading velocity tail of degree d in (-3/2, -1), smooth away from the origin,
  cannot be irrotational.
- Exact solutions outside the target were screened on every branch: the affine family U = M y (trace-free M with
  M + M^2 symmetric), whose residual is exactly zero, and the constant solutions with linear pressure, which do not
  decay. Collapse to affine, axisymmetric, four-fold, two-dimensional or zero fields was also screened. Across all
  77 evaluated checkpoint files the core affine-fit remainder is at least 0.328, the vector non-axisymmetric energy
  fraction of the sampled core is 0.37 to 0.76, n = 2 carries at least 85 % of the non-axisymmetric ring energy, and
  the smallest normalized derivative-variation fraction is at least 0.072. None of these collapses occurred.
- An early claim that a residual floor follows from isolated numerical stagnation points was false and is withdrawn
  (counterexample U = eps W, section 3.5).
- Runtime defects found by the independent audit and repaired during the run:
  - overlapping sampling weights in the validation norm (earlier trainer-side metrics use a different weighted
    measure from the later ones);
  - a doubled drift factor in a denominator, dormant because C = 0 in all runs;
  - L-BFGS history kept across resampling;
  - an aliased in-memory NaN rollback.

  Not repaired when training stopped: exact resume immediately after a stage transition (an executed counterexample
  with the training code as revised during the run gives a maximum parameter difference of 0.004), full NaN recovery
  of the optimizer, sampler and counters, and instrumentation of exact eligible activity (section 5).

  After training stopped, the stage-transition case was repaired in a revision of the training code (SHA256
  prefix 61c6f9e23750908e): an independent repetition of the same interrupted run agrees bitwise with the
  uninterrupted run in the model parameters, and the optimizer, sampler and random states and the counters also agree.
  The revision current at this report version (SHA256 prefix 2f6dbd5ecb0f18f8) differs from it only in how work
  intervals are recorded and in a test-only option for a separate ledger; the repetition was made on the earlier
  revision. Exact resume for every history and configuration, in particular from checkpoints written during the
  campaign, full NaN recovery and exact instrumentation of eligible activity remain unresolved. The repair changes no
  evaluated checkpoint and no independent evaluation.

## 8. Work not performed, and why the campaign ends here

The primary objective, a nonzero exact smooth globally decaying m = 2 profile with 0.4 < c_l < 0.5, is excluded by an
independently checked proof, and the task's section 13 rule lets such an obstruction supersede further blind search
in the primary class. We chose to end the campaign at that obstruction, leaving extended calibration at c_l = 1/2 and
any search above 1/2 unfinished. This decision does not resolve those secondary questions, complete the numerical
deliverables or satisfy the 96-hour minimum. The following planned work was not performed:

- free-exponent refits and a trainable-c_l branch;
- a training versus holdout comparison beyond the single reconstructed batch above;
- refinement series in capacity, sampling, domain size and tail model;
- the other configured seed matrices and the off-axis paired-blob representation;
- an executed L-BFGS stage (configured, not reached), and SS-eSOAP or SS-Broyden (not implemented);
- whole-space pressure and Biot-Savart certification with exterior bounds;
- the viscous-defect diagnostic for a credible candidate (no acceptable candidate was found);
- any search with c_l > 1/2;
- more than a short calibration at c_l = 1/2.

The open secondary questions are not decided by L2: whether an exact smooth decaying m = 2 profile exists at
c_l = 1/2 or for some c_l > 1/2. Also open are numerical acceptance thresholds for approximate profiles, stability,
and any construction of blowup from finite-energy data.

## 9. Reproducibility and continuation

The accompanying artifacts contain:

- the equations document (version 1.5, with the symbolic check script and log);
- the source notes;
- the theory notes with the full proofs of L1, L2 and the floor statement, the dated audit log, the independent
  proofs and audits, and the referee reviews;
- the training code and its 17 unit tests;
- the independent evaluator and its calibration tests;
- the experiment configurations;
- the best evaluated checkpoint for each representation and exponent (12 files, including the selected one); all 77
  evaluated checkpoint files are identified by SHA256 in the checkpoint table;
- the independent checkpoint table and one evaluation file per checkpoint;
- the training campaign ledger and the validation ledger, with the frozen copies used for this report;
- the active-time enclosure script;
- the launch, status, stop and resume scripts.

Exact resume is demonstrated only for tested cases: with the training code as revised during the run, an Adam stage
with per-step resampling and a resume inside a resampling block; with the post-stop revision, also an interruption
immediately after a stage transition (section 7). Exact resume in general, in particular from checkpoints written
during the campaign or after configuration edits, is not established.

Missing deliverables: progress snapshots at 24, 48, 72 and 96 active hours (never reached), and refinement and
free-exponent studies (not run).

Continuation. The resume script in the accompanying artifacts returns stopped queue
entries without a hold marker to the pending queue and restarts the supervised runner. After training stopped, the 25
primary-range entries (fixed c_l between 0.41 and 0.49, including the two requeued second-representation runs at 0.47
and 0.49 and every never-started primary entry) were moved to an archive directory of the queue. The script therefore
restarts only c_l = 0.50 entries: the two stopped runs with checkpoints, one in each representation, and the
never-started second-representation runs with the two other seed matrices and with the paired-blob family. Started
runs load their last atomic checkpoints, subject to the resume limitations above; archived entries can be moved back
to the pending queue unchanged, but their run directories are not in the artifacts, so they would restart from
their configurations. The queue contains no experiment with c_l > 1/2 and no free-exponent run; such
experiments must first be added as new configurations. The continuation notes in the accompanying artifacts list them.

# NUM_REPORT (numerics lane e1-num): method, configurations, results, verdict

Updated: 2026-10-23 08:05Z (shift 1, campaign stopped). Credited elapsed numerical time (union over workers): between 0.999 h and
1.180 h (STATE.json; verifier's independent reconstruction agrees). This bounds what the trainer credited between accepted optimizer
steps (including checkpoint I/O and pauses under 30 s); the eligible compute time is not recoverable exactly from the ledger. The 96-hour requirement was NOT
completed; the campaign closed early under PROMPT section 13 (see below).

## Current verdict
Numerics: NO ACCEPTABLE CANDIDATE FOUND IN THIS SEARCH. No trained checkpoint approaches the screening thresholds (independently
evaluated worst regional relative momentum residuals are 0.17-0.33, verifier's table); nothing here is evidence for or against
existence of a profile. All exponents in run names are fixed inputs.
Theory (lead and verifier, not this lane): RIGOROUS OBSTRUCTION UNDER EXPLICIT ASSUMPTIONS. Theorem L2 (lead THEORY_NOTES.md section 7,
independent proof by the verifier, hostile referee and scope audits clean as of 07:38Z): for 0 < c_l < 1/2, a C^2 solution of the
profile equations on R^3 with U = o(|y|) has zero vorticity and is constant; decaying implies U = 0. This covers the entire primary
exact-profile class of the prompt (0.4 < c_l < 0.5, any stagnation set, any angular structure); it does not decide c_l = 1/2 or
c_l > 1/2. On the lead's instruction (NOTES_FOR_TEAM.md 07:38Z) the numerical queue was stopped gracefully at 07:47:05Z: all six
workers checkpointed and exited, the ledger was frozen (64 records, SHA256 9f9477b05b19cafb4b8cd911b06c188db5ab1eb22933ae1510703fd3647505ff),
and the queue entries were kept (NEXT_STEPS.md has the continuation queue for the open secondary questions).

What this lane observed in the excluded class before the stop (trainer-internal holdout diagnostics, NOT evidence; the verifier's
independent evaluations are in e1-ver/CHECKPOINT_TABLE.tsv): in every v2 run at c_l in {0.41, 0.43, 0.45} (and at the 0.5 control) the
absolute core residual decreased during Adam stage 0 while the relative core residual eps_m(R<1) rose from ~0.15-0.20 to ~0.20-0.29,
because the velocity terms near the origin weakened (denominator 1.3-1.5 -> 0.8-0.9) while the vorticity maximum sharpened
(max |Omega| 2.7 -> 3.8 at 0.5, -> 5.5 at 0.41) and moved outward to an off-axis Q-pair at r ~ 0.9; the nonlinear-scale tail residual
stayed O(1) (that stage normalizes by the linear scale). Stagnation sets had three zeros (origin with one contracting direction; an
off-axis Q-pair with lambda_max(S) ~ 1-1.9). The stretching ratio at the vorticity maximum was far from 1 (-0.5 to 0.06). These
runs were stopped in stage 0 or 1 of a 4-stage curriculum; no run reached the nonlinear-scale or L-BFGS stages. They are archived
as a record of approximate optimization in a class that L2 excludes, not as a test of L2 (L2 says nothing about optimizer behavior
on approximate states, and a decreasing loss is not evidence either way).

## 1. Problem solved by the code
Stationary profile system (PROMPT.md section 3, EQUATIONS.md 1.1), canonical frame C = 0:
    (1 - c_l) U + (c_l y + U).grad U + grad P = 0,   div U = 0  on R^3,
with U(Qy) = Q U(y), P(Qy) = P(y), Q = diag(-1,-1,1) (m = 2), U decaying like R^d, d = 1 - 1/c_l, and P -> 0 at infinity.
c_l is a fixed input in every experiment named `..._clNNN` (NNN = 100 c_l). A fixed c_l is never reported as found.

## 2. Method (project/euler_ss, project/train.py)
- Unknowns: a smooth vector potential A and the pressure P, both tanh MLPs in FP64; U = curl A (divergence exactly zero).
- Hard m = 2 symmetry by projection S[N](y) = [N(y) + Q N(Qy)]/2 (vector) and [p(y) + p(Qy)]/2 (scalar); curl commutes
  with the proper rotation Q, so U is Q-equivariant (tested).
- Seed base (PROMPT.md section 9) plus learned corrections: A = A_seed + sum_k env_k S[N_A^k], P = P_seed + sum_k env'_k S[N_P^k].
  v1 representation: one term, envelope rho^(d+1) (rho^2 = 1 + R^2), features (y/rho, log(1+R^2)/3). The verifier proved
  that with the unbounded log feature the learned leading tail degenerates to an axisymmetric swirl (e1-ver
  research/radial-feature-tails/PROOF.md); v1 is therefore only a core-focused baseline / negative result for the tail.
  v2 representation ('tail2', EQUATIONS.md 5.4 R-tail): bounded analytic features xi = y/rho, |xi|^2, and two envelope terms
  per field, degrees d+1 and 2d for A (U degrees d and 2d-1), 2d and 3d-1 for P. Non-integer subleading powers are
  supplied by the envelopes, not by the network.
- Loss: sum over sampling regions (core ball R<4, log shells 4<R<R_max, axis tube r<0.2, origin ball R<0.5) of the mean
  of |R_m|^2 / T(y)^2, with T = rho^q, q = d + T_lambda (d-1): T_lambda = 0 normalizes by the linear-term scale R^d,
  T_lambda = 1 by the nonlinear scale R^(2d-1). Staged curriculum T_lambda 0 -> 0.5 -> 1. One scale gauge: smooth max of
  |U| over 2048 fixed core points = 1 (soft). Pressure gauge P(inf) = 0 (built in). No anti-axisymmetry penalty by default.
- Optimizer: Adam (cosine lr decay) stages, then L-BFGS (strong Wolfe, fixed collocation set re-drawn every 10 outer
  steps). No SS-eSOAP/SS-Broyden is implemented or claimed.
- Derivatives: nested forward-mode AD (torch.func.jacfwd) in physical coordinates; checked against finite differences to
  third order and against the exact affine family (zero residual for all four residuals) in tests/test_physics.py (15 tests).
- Validation inside training (never used for training): fixed holdout sets per region with physical-volume importance
  weights; eps_m(D) and eps_nl(D) = ||R_m||/(||U.grad U|| + ||grad P||) on shells D1..D6; vorticity, affine-fit remainder,
  non-axisymmetry (group average over 16 rotations), ring Fourier content (n = 0,2,4,>=6, odd), parity defects
  (inversion, z-reflection), hard-symmetry defect, 3D dependence, tail slope, stagnation set of V with eig(grad V), eig(S),
  |Omega| and isolation distance (EQUATIONS.md 7.3(h), 9.3).
- Infrastructure: detached supervised runner (project/runner.py; bin/launch.sh, status.sh, stop.sh, resume.sh, hold.sh),
  directory queue, atomic checkpoints every 10 min (model, optimizer, scalars, RNG, sampler state), per-worker active-time
  accounting with 30 s gap cap (pauses are not counted), CAMPAIGN_LEDGER.jsonl (one record per checkpoint interval),
  non-overlapping union computed by project/ledger.py. Exact-resume test: bitwise identical (tests/RESUME_TEST.md).

## 3. Experiments (final state at the 07:47Z stop; trainer-internal numbers in project/reports/snapshot_shift1_stop.md)
| id | representation | seed (a,b,c_M) | c_l | status | note |
|---|---|---|---|---|---|
| pilot_cl045_M1 | v1, width 64 | (0.2,-0.4,0.7) | 0.45 | stopped, stage 1 step ~5700 | FP64 pilot / smoke test; exact-resume test |
| v1_M1_cl050 | v1, width 96 | M1 | 0.50 | stopped, stage 0 step ~4300 | baseline with the flawed v1 tail (negative result) |
| v1_M1_cl049/047/043/041 | v1 | M1 | 0.49..0.41 | held at step 847-920 | stopped once the tail flaw was proved; checkpoints kept |
| v2_M1_cl050 | v2 (n_tail 2), width 96 | M1 | 0.50 | stopped, stage 0 step ~7600 | c_l = 1/2 control (not excluded by L2); open |
| v2_M1_cl045, cl041, cl043 | v2 | M1 | 0.45, 0.41, 0.43 | stopped, stage 0 steps 6400-7500 | excluded class; archived |
| v2_M1_cl047, cl049 | v2 | M1 | 0.47, 0.49 | stopped at step 1271 / 1399 | trained before the 07:12Z restart, not relaunched; in queue/stopped |
| v1_M1_cl045, v2_{Z0,M3}_cl*, v2b_BL_cl* (18 entries) | v2 / blobs | Z0=(0.6,0.5,0.5), M3=(-0.9,0.8,-0.3), blob pairs | 6 values | pending, never started | configs in configs/ |

Total: 12 experiment ids trained (all appear in the ledger), 18 queued but never started.

## 4. Results
No candidate. Independently evaluated (verifier, physical-volume shells, sixth-order finite differences) worst regional relative
momentum residuals of all saved checkpoints lie between 0.17 and 0.33 (shell 1 < R < 2 in every case), three to four orders of
magnitude above the screening target 1e-3; the v1 runs' outer nonlinear tail ratios are 1e4-1e6 (tail representation flaw), the
v2 runs' 0.8-50 (tail not yet trained at the nonlinear scale). Trainer-internal holdout diagnostics for every run are tabulated
in project/reports/snapshot_shift1_stop.md and are not evidence. Infrastructure results that are verified: exact resume (Adam and
L-BFGS mid-block, bitwise), derivative agreement AD vs finite differences (1e-8..1e-6 at steps 1e-5) and hand-derived vs torch.func
forward propagation (values 1e-12, derivatives 1e-11/1e-10, parameter gradients 1e-9), Cartesian vs cylindrical finite-difference residual agreement (1.6e-10 relative), exact affine family
zero residual for all four residuals, verifier's matched-point reproduction of the trainer's eps_m within 3e-8 relative.

## 4b. Published checkpoint records (project/artifacts/candidates, each with ckpt.pt, weights.npz, manifest.json, audit.json)
Audits by this lane's evaluate.py on fresh uniform-volume shells (same code family as the trainer, so not independent of it;
the verifier's evaluations are the independent ones):
| record | step | c_l (fixed) | worst eps_m (region) | eps_m, eps_omega, eps_P on 1<R<2 | worst eps_nl (region) | stretch at |Omega| max | zeros of V | label |
|---|---|---|---|---|---|---|---|---|
| v2_M1_cl050 | 7763 | 0.50 | 0.086 (0.25<R<1) | 0.067, 0.19, 0.68 | 1.14 (64<R<256) | -0.28 | 3 | c_l = 1/2 control, mid-training, not a candidate |
| v2_M1_cl045 | 7071 | 0.45 | 0.115 (0.25<R<1) | 0.080, 0.21, 0.75 | 18.6 (1024<R<4096) | -0.32 | 3 | excluded class, mid-training, negative record |
Both have the Cartesian-vs-cylindrical finite-difference residual agreement at 1e-8..1e-7 relative, tail slopes equal to d to 1e-3,
n = 2 ring energy fraction 0.62-0.63, group-average non-axisymmetry 0.70-0.72, inversion parity released (defect 0.24-0.26).

## 5. Negative results and failure modes recorded so far
- Representation v1 (unbounded log radial feature): learned leading tail is forced to an angular constant (proof by the
  verifier); replaced by v2. The v1 runs are kept as a controlled comparison of core behavior.
- The prompt's seed itself fails the momentum screen (relative momentum 0.35 on 1<R<2, verifier) and has a degree d-2
  tail correction that cannot balance at the nonlinear scale for c_l < 1/2 (verifier seed-family proof); it is an
  initializer only.

## 6. Theoretical constraint shaping the search (from the lead and verifier; not established by this lane)
Claim L1 (lead THEORY_NOTES.md; CONFIRMED by the verifier's independent proof and by an independent referee as of
2026-10-23 06:51Z): for 0 < c_l < 1/2, a C^2 solution with U = o(|y|), U -> 0, whose stagnation set N_V = {c_l y + U = 0} is
countable, has zero vorticity. It does not cover uncountable stagnation sets, so the search continues. L1 does NOT predict a
residual floor for a numerical sequence (counterexample: U = eps W, W compactly supported divergence-free, P = 0: one
nondegenerate zero of V, residual -> 0, limit U = 0). What this lane therefore logs for every branch whose relative residual
keeps decreasing at fixed c_l < 1/2: (a) nontriviality normalization (max |U| gauge, |Omega| and grad U at the origin, max
|Omega|, vorticity energy in the core) and whether it drifts to zero; (b) compactness (core radius, position of the vorticity
maximum, tail slopes, fraction of energy beyond R = 20; max |D^2 U|, |D^3 U| on the core in evaluate.py); (c) stagnation
structure (zeros of V with eig(grad V), eig(S), lambda_max(S), isolation distances, clustering along curves/surfaces). L1 implies
that an improving sequence at c_l < 1/2 must show normalization collapse, loss of compactness, or zeros of V becoming
non-isolated. The c_l = 0.50 control is not constrained by L1.

## 7. Measurement and reproducibility fixes (which runs predate them)
Applied 2026-10-23 07:12Z (runner restart; every worker resumed from its checkpoint with the new code):
- Ledger: each record since 07:12Z carries the credited elapsed pieces between accepted optimizer steps ("chunks", closed at
  gaps > 30 s or at checkpoints; they include checkpoint I/O and pauses under 30 s, omit the first step after a restart, and have
  1 ms rounded endpoints); the 38 legacy records written before 07:12Z carry only wall intervals and credited seconds. ledger.py
  reports lower and upper bounds of the credited union; the verifier's independent reconstruction of the final 64-record ledger
  gives 0.999 h to 1.180 h. Eligible numerical time remains unresolved beyond these bounds.
- Validation physical-volume norms use only the disjoint core ball + log shells (axis tube and origin ball reported separately).
  eps_m values logged before 07:12Z used summed overlapping weights and are a different weighted measure (not comparable at
  the 10% level; the verifier measured 0.19 vs 0.22 on one pilot checkpoint).
- Removed a double |C| factor in the eps_m denominator (dormant: all runs have C = 0).
- L-BFGS: quasi-Newton history reset whenever the collocation set is re-drawn; the current batch is checkpointed so a resume
  inside a resampling block is exact (tested bitwise). No run had reached an L-BFGS stage before the fix.
- NaN rollback reloads the atomic disk checkpoint (the earlier in-memory copy aliased live parameters; never triggered).
- Training derivatives now use the hand-derived forward propagation (euler_ss/fastderiv.py; tested against torch.func: values
  to 1e-12, first derivatives 1e-11, second derivatives 1e-10, parameter gradients 1e-9, all relative to the largest entry);
  validation keeps the torch.func path as an in-run cross-check. Known remaining lifecycle defects (verifier's
  RUNTIME_REPAIR_AUDIT.md): resume across a stage transition and the optimizer part of the NaN rollback; see section 8.

## 8. Known defects at the stop (not repaired because no further training is allowed)
- Stage-transition resume (verifier RUNTIME_REPAIR_AUDIT.md): a resume whose checkpoint was written at a stage boundary may not
  reproduce a continuous run bitwise (optimizer re-creation order); exact resume is demonstrated within a stage (Adam) and
  inside an L-BFGS resampling block.
- NaN rollback reloads the model and the Adam state from disk, but not the sampler/RNG state; never triggered in any run.
- Eligible active time: the ledger credits elapsed intervals between accepted steps (with checkpoint I/O and short pauses); the
  prompt's "active numerical experiment time" is bounded, not measured exactly.

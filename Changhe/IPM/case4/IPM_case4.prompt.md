# IPM Case 4 — Read-Only Handoff, Isolated 860-Generator Expansion, and ≥48-Hour Research Campaign

You are Codex working on a new, more powerful scientific-computing machine. **This is a standalone research assignment.** Do not assume access to previous conversations. The repository describes an existing numerical approximation to a whole-plane stationary self-similar IPM profile, not a proven PDE solution.

## 0. Non-negotiable filesystem boundary

The supplied reference repository is:

`Changhe/IPM/case4/IPM_StageXIII_GitHub_handoff`

The instruction file being read is:

`Changhe/IPM/case4/IPM_case4.prompt.md`

These may be relative paths: resolve them to their real absolute locations before proceeding. Treat **the entire `Changhe/IPM/case4` source tree, including this prompt and the handoff repository, as READ-ONLY**.

**NEVER execute research programs inside the handoff directory or elsewhere in the protected `case4` tree. NEVER edit, install into, create files in, write caches/logs/checkpoints under, or run Git commands that mutate this protected tree.** Reading text and computing read-only checksums is allowed. Do not run `verify_repository.py`, tests, import Python modules, execute notebooks, install an editable package, or start the optimizer while the original directory is the working directory or is being used as a writable dependency. Do not point a program's output, cache, Python bytecode, temporary directory, or checkpoint directory there. Do not update or push its Git metadata. Do not use symlinks that lead from the working copy back to the protected source.

**First read and understand the handoff as documentation only. Then make an independent physical copy at an entirely different path, outside `Changhe/IPM/case4`. ALL installation, execution, code modification, experiments, new documentation, logs, and results happen exclusively in that independent working copy or its separate experiment/output directories.** You have permission to refactor, replace, and extend code freely *within the new copy*, subject to scientific validation. No change may be written back to the original.

Choose a suitably spacious destination from actual host resources, preferably `/scratch/$USER/ipm_case4_860` or another stable work/scratch volume. If `/scratch` is unavailable, choose an absolute directory outside the protected Git source. Record `SOURCE_REALPATH`, `WORK_REALPATH`, and `OUTPUT_REALPATH`, and verify the latter two are not contained in, symlinked into, or otherwise writing to the protected tree. Copy all 217 handoff files (or the actual number found) including hidden configuration files and full accepted-state restart dependencies; verify file count and checksums. Audit symlinks and absolute path references. Original files may be read, but must never be modified. Record a before/after integrity check of the protected source with results saved ONLY under the working directory.

If the copy is incomplete, a dependency resolves back to the original, or protection cannot be guaranteed, **do not run anything**; repair the isolated copy or report the blocker.

## 1. Read and reconstruct what the project has actually achieved

From the read-only reference, first study:

- `README.md`
- `docs/MATHEMATICS.md`
- `docs/STATUS.md`
- `docs/CODE_GUIDE.md`
- `docs/NEXT_RESEARCH_PLAN_860.md`
- `docs/BASIS_860_SPEC.md`
- `docs/NEW_SERVER_CODEX_PROMPT.md`
- `docs/DEPLOY_LINUX.md`, `docs/RESTART.md`, `docs/HANDOFF_VALIDATION.md`
- The actual production, validation, restart, and basis source code in `research/`; follow imports to their real implementations.

Before any execution, write a **brief but mathematically explicit understanding report in the new work directory**: governing PDE, potential representation, parity, physical parameters and gauge, 181-dimensional method, objective, center elimination, C5 conditions, independent acceptance policy, numerical limitations, current checkpoint, intended 860-generator expansion, and what remains scientifically open. Distinguish documented statements from independently verified code behavior. Do not spend time narrating Stage I–XII history.

### PDE and numerical invariants

The whole-plane stationary IPM system is

\[
(c_lX+U)\cdot\nabla\rho=\rho,\quad
U=(-\psi_y,\psi_x),\quad-\Delta\psi=\rho_x.
\]

Density is even in `x`, odd in `y`, with `rho=y*f` and `rho_y(0)=a_0 != 0`. The potential formulation is

\[
\psi=\partial_{xy}\chi,\qquad \rho=-\partial_y\Delta\chi,
\]

so the Poisson identity is automatic. The physical density residual is `R_rho=(c_l X+U)·∇rho-rho=y R_f`; use the exact analytical axis extensions from the implementation. The canonical whole-plane Poisson inverse contains no independent harmonic strain.

Under spatial dilation `rho_s(X)=s rho(X/s)` and `U_s(X)=s U(X/s)`, **both** `c_l` and physical `a_0` remain unchanged. Both must remain free; only the legitimate spatial-dilation gauge may be fixed.

Preserve as the primary comparable objective

\[
J_{\mathrm{abs}}=\frac{1}{\pi a_{\mathrm{ref}}^2}
\int_{0}^{\pi/2}\int_0^\infty |R_f(r,\theta)|^2\frac{dr}{r}\,d\theta,
\qquad a_{\mathrm{ref}}=23.95065822465609.
\]

The reference amplitude is **not** a constraint setting the physical `a_0`. The current solver uses analytic center elimination, five Taylor compatibility conditions, whole-log-radius three-block positive quadrature, full `c_l` derivatives, SVD/Gauss–Newton trust region, independent whole-axis trial evaluation, and durable accepted/rejected records. Learn their exact implementation from source.

### Authoritative baseline

The implemented basis has **186 potential generators and 181 feasible variables**, including the free `c_l` parameter; physical `a_0` is free. The 860 basis has **NOT** yet been implemented in the baseline.

Authoritative state: `research/campaign/global181_v3/snapshots/accepted_00000278.json`.

Expected SHA-256:

`812d34466c078e2ce643c49671299f4359f764fe2e1d925426762ba962d6e955`

Independently assessed values:

- `c_l = 1.8089923602744993`
- `a_0 = 14.767729990606481`
- `J_abs = 4.2683726070948805e-9`
- Sampled fixed-grid `E_f = max |R_f|/a_ref = 1.23849639744e-4`
- Sampled fixed-grid `E_rho = max |R_rho|/(r*a_ref) = 7.16582921424e-5`
- Maximum of five remaining Taylor defects `4.88829345686e-14`.

Source-machine independent integration, canonical Green inverse, origin, clean-path reproduction, and derivative checks were reported. Seven selected derivative directions at three step sizes showed feasible descent, **not stationarity**. Some origin-region residuals worsened. For accepted278, the *unnormalized* density residual has a nonzero leading far-field coefficient,

\[
R_\rho(r,\theta)\sim r^{0.105587864228\ldots}\mathcal E_1(\theta),
\qquad\|\mathcal E_1\|_{L^2(0,\pi/2)}\approx0.440353421495.
\]

Thus the original residual grows at infinity despite a small quotient/integrated loss. There is **no established exact PDE solution, continuum supremum certificate, basis convergence, or stationary optimizer**.

## 2. Qualify the isolated machine and reproduce accepted278 BEFORE any new basis work

After the independent copy is made and its links are audited, change into the **working copy**. Install dependencies in a new environment entirely outside the original tree. Examine real CPU cores, NUMA topology, usable RAM, disk, scratch quotas, BLAS/LAPACK/threading, numerical precision, and available GPUs (do not assume GPU is needed). Monitor CPU, memory, disk and temperatures if sensors exist. Use all useful multicore CPU resources without oversubscription; plan safe resource limits for long jobs.

Run `python3 -B tools/verify_repository.py` **in the copy**, followed by the relocation/`inspect`, `restart-audit`, `smoke`, `objective`, and `replay` tests following the local `docs/DEPLOY_LINUX.md` and `docs/RESTART.md`, with fresh output paths. Independently reconstruct `accepted278`, its complete restart chain and mesh epoch, the fields, `c_l`, `a_0`, `J_abs`, origin/Taylor constraints, Poisson inverse, relative/absolute residuals, and the actual production Jacobian.

Numerically qualify the destination's BLAS, SVD, Jacobian and integration policy against the reference results. Diagnose discrepancies rather than weakening the old replay/acceptance thresholds merely to make Linux pass. Produce `LINUX_QUALIFICATION.md` with commands, numeric tolerances, PASS/FAIL/PENDING, host information and root-path isolation proof. **No optimization or 860 implementation before this initial reproduction passes, apart from justified diagnostic fixes confined to the copy.** Do not run a separate long 181D continuation.

## 3. Implement the complete 860-generator potential family in the independent copy

Define

\[
\gamma=1/c_l,\quad\lambda=1-\gamma,\quad p_j=(3+\gamma-j\lambda)/2,
\]

\[
\boxed{\chi_{m,k,j}(r,\theta)=r^{2k}(1+r^2)^{p_j-k}\cos(2m\theta),}
\quad 0\le m\le9,\quad m\le k\le25,\quad 0\le j\le3.
\]

There are exactly `4*sum(m=0..9)(26-m)=860` raw potential generators. **860 is not automatically the dimension of the feasible optimization variables.** Recompute constraint ranks, five-Taylor feasible-chart dimensions, free `c_l`, `a_0`, and gauge treatment from the implemented equations.

Each basis function is smooth at the origin because `r^(2k)cos(2m theta)=r^(2(k-m)) Re(x+iy)^(2m)`; evaluate regular Cartesian derivatives stably, especially on the axes. Preserve full analytic derivative dependence on `c_l` in radial exponents. Modes with `k>=max(m,5)` vanish to sufficiently high order to preserve the existing low-order center jets when used as corrections; handle lower-`k` modes through the legitimate chart, not by assuming they are unconstrained.

**Exact old-to-new embedding is a hard gate.** The former 186 functions (core radial-offset powers and shifted-Legendre global functions) are analytically contained in the 860 span. Derive a symbolic/algebraic coefficient map from the *actual old source*, not a loose least-squares fit. Do not append 860 functions onto 186 and create exact dependencies. Build a versioned 860 representation and deterministic conversion of accepted278; prove/test generator identities and verify fields and derivatives, including several `c_l` values and derivative directions, center constraints, Poisson relation, objective, and independently sampled residuals. Save an immutable **860-dimensional seed reproducing accepted278** in a new campaign root.

For far-field analysis, the exact tail-moment formula is

\[
C_{m,j,q}=\sum_{k=m}^{25}a_{m,k,j}\binom{p_j-k}{q},\qquad q\ge0.
\]

It allows separate treatment of leading moments, inverse-even radial corrections, and interior-shape nullspace directions. Confirm coefficient ordering, scaling, numerical rank and conditioning. Preserve the original source/accepted278 in the copy as a separately immutable baseline, even though all *new* code in the working directory may be modified/reorganized freely.

### Important deliberate far-field limitation

With `alpha_j=gamma-j*lambda` and asymptotic fields `rho~sum_j r^alpha_j F_j(theta)`, `psi~sum_j r^(alpha_j+1) Phi_j(theta)`, the Poisson and transport identities are

\[
-\Phi_j''-(\alpha_j+1)^2\Phi_j=\alpha_j\cos\theta\,F_j-\sin\theta\,F_j',
\]

\[
\mathcal E_N=-N(c_l-1)F_N+\sum_{i+j=N-1}\left[(\alpha_i+1)\Phi_iF_j'-\alpha_j\Phi_i'F_j\right].
\]

A uniform `m<=9` cutoff makes `F_1` support at most odd harmonic 19, while nonlinear forcing from leading `F_0` can reach harmonic 39. **We deliberately accept this approximation in the first experiment. Do NOT impose `E_1=E_2=E_3=0` as new hard constraints, add penalties for them to the primary objective, or automatically enlarge the angular cutoff to `(9,19,29,39)`.** Monitor representable and omitted Fourier-mode residuals separately, and record the unnormalized far-field power/coefficient. The previously quoted `0.145222%` unresolved fraction was measured for historical `accepted165`, NOT accepted278; remeasure it if useful.

## 4. Qualify and optimize the enlarged problem

Keep `J_abs`, `a_ref`, true physical symmetries, center elimination, five Taylor conditions, canonical inverse, legitimate dilation gauge and freedom in `c_l,a_0` mathematically unchanged for the primary campaign. You may **freely change/refactor/optimize code in the isolated working copy**, including switching numerical algorithms or CPU/GPU implementations, so long as you demonstrate equivalence of the physical formulation and independent acceptance tests. If you experiment with a changed objective or far-field constraints, isolate it in a separately named exploratory branch and do not call its results directly comparable to the fixed-objective 860 campaign.

Map the analytic center/C5 feasible chart to the new coefficient ordering and rederive the *actual* feasible dimension. Construct and independently validate the analytic Jacobian, including the `c_l` exponent derivatives and near-null directions. Compare finite differences at multiple step sizes for parameters, new radial/angle directions, and the gauge. Benchmark Jacobian assembly, SVD/QR/iterative linear solves, full-axis quadrature, memory and CPU scaling. For 860 generators, a naive dense SVD may become expensive; you may use chunked Jacobians, stable QR or JVP/VJP-based matrix-free iterative solvers **only after independently qualifying them against trusted small or medium problems and the old trust-region semantics**. Do not use unchecked normal equations or discard genuinely positive singular directions solely to make code faster.

Start from the exactly embedded accepted278 state. Run a small pilot, checking equality at zero step, predicted versus actual reduction, physical parameter changes, independent integration uncertainty, Taylor overlap, source hashes and restart behavior. Only after these gates pass begin a resource-guarded, durable high-dimensional optimization. Record every accepted/rejected step, configuration, mesh refinement, CPU/RAM metrics, errors and reason for stop. Run independent 32-region/far-field/near-origin assessments at significant improvements and at end. Preserve the accepted seed and every accepted checkpoint, separate from unaccepted lower-loss diagnostic trials.

### Minimum research duration and genuinely long optimization — REQUIRED

**Commit to at least 48 hours of genuine wall-clock research and/or running scientifically useful computation after beginning the isolated campaign**, unless an unavoidable hardware/safety/correctness failure prevents further work. This is a minimum effort/campaign duration, not a target at which an unfinished calculation should be killed. Do not fake the requirement by sleeping, waiting idly, reprinting logs, or counting work performed previously on the Mac. Record UTC start/end timestamps, optimizer uptime, research/check durations, substantive operations and interrupted intervals; clearly distinguish elapsed wall time, active investigator time, and active solver time. If a platform/session limit prevents reaching 48 hours, document the true duration and preserve a resumable job; never assert 48 hours were completed when they were not.

At the start, benchmark at least a few representative 860 evaluations and model/trust-region steps before assigning a runtime estimate. After the pilot and an initial stable sequence of real steps, publish a **rough ETA** grounded in the observed runtime distribution: seconds/minutes per evaluation and accepted/trial step, acceptance rate, realistic cost of independent checks, current throughput and configured next checkpoint/iteration/time budget. Give a **range in hours or days** with assumptions; explicitly distinguish *time to finish a specified compute budget* from *time to convergence*, which is generally unknown. Refresh this estimate when performance or acceptance rates change. Never invent a convergence deadline.

**If the optimizer needs far longer than 48 hours, you may end the interactive Codex research session only after the initial 48-hour genuine campaign has been met and the optimizer is demonstrably stable and durably running in the independent working area.** In that case, leave it continuing as a properly detached, supervised and restartable process (for example with an available job scheduler, systemd user service or tmux), not an unverified background promise. Before handing off, check that the PID/job actually exists, its working directory and output paths are outside the protected source, its log and recent checkpoint update, resource limits and disk budget are safe, and the automatic restart/monitoring procedure is documented. Report to the user: current accepted state, best measured loss, actual elapsed and active compute time, approximate **time needed for the planned budget**, credible uncertainty, monitoring commands and safe stop/restart instructions. If no persistent execution mechanism exists, do not claim the run will continue: checkpoint and report the blocker instead.

If 860 implementation/qualification uses most of the 48 hours and the optimizer has only just started, report that honestly, give a benchmark-based ETA, and keep the durable run operating when possible. Do not skip correctness gates to reach a time target. If a major correctness blocker arises, investigate it scientifically within the time budget rather than letting an invalid optimizer run.

## 5. Reports, checkpoints, and terminal handoff

Store **all** new materials outside protected `Changhe/IPM/case4`. Produce at least:

- `START_HERE_NEW_RUN.md`: verified original handoff understanding, new-machine paths, and what happened in this run.
- `LINUX_QUALIFICATION.md`: source isolation, new environment, exact replay and arithmetic checks.
- `BASIS_860_IMPLEMENTATION.md`: formulas, ordering, constraint dimension, old-to-new algebraic embedding and actual source/function map.
- `EMBEDDING_TESTS.md`: `accepted278` reproduction in the new representation, objective, Jacobian and full-axis independent checks.
- `OPTIMIZATION_860_LOG.md`: chronological trials, decisions, rejects, time accounting and compute resources.
- `RESULTS_860.md`: best accepted result, full comparison against accepted278, independent maxima, origin and far-field Fourier measurements, and caveats.
- `RUNBOOK_860.md`: exact runnable commands to verify, benchmark, monitor, stop safely and resume.
- Machine-readable environment, coefficient ordering, checkpoint hashes, file manifest, benchmark profiles and ETA estimates.

The final user-facing report must say plainly:

1. Where the original READ-ONLY handoff is and where the completely independent working copy and outputs are.
2. Whether source protection was independently checked before/after and whether **any** operation wrote into `Changhe/IPM/case4` (expected: none).
3. Whether Linux qualification and accepted278 reconstruction passed, with exact numerical differences.
4. Whether all 186 old generators were embedded algebraically into the 860 span, and the true number of feasible variables.
5. Whether the 860 seed reproduces the baseline physical fields and `J_abs` within qualified tolerances.
6. How many hours of **verified actual research/compute** were performed, measured separately from wall-clock elapsed.
7. What 860 optimization was actually run, its best accepted `J_abs`, `(c_l,a_0)`, independent maxima, Taylor constraints and far-field `E_1/E_2/E_3`.
8. Whether the unnormalized density residual still grows, and what its leading coefficient and unresolved angular modes are.
9. If a long run is left active: verified PID/job ID, logs/checkpoints, resource use, **approximate ETA in hours/days based on throughput**, plus monitor and safe-stop/restart commands. State clearly that time-to-convergence cannot be guaranteed.
10. Whether a stationary optimizer or a genuine exact PDE profile is supported by actual evidence (default: NO until proved), and the best next step.

**Execute the task; do not merely write another proposal. Priority: read source without execution → copy outside case4 → verify copy and Linux → reproduce accepted278 → implement/verify 860 basis → resource-guarded optimization ≥48h useful work → if longer, leave a VERIFIED stable process and provide a realistic ETA.**

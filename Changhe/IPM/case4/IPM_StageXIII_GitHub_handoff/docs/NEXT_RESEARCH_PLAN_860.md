# Next research plan: a validated 860-generator expansion

Decision recorded 2026-10-23. **This is a future Linux implementation and research plan, not an implemented basis or a completed optimization.** The shipped production state still has 186 potential generators and 181 feasible variables. Its complete accepted278 restart remains intact. Read [the basis specification](BASIS_860_SPEC.md), [the standalone receiving-Codex prompt](NEW_SERVER_CODEX_PROMPT.md), [current status](STATUS.md), and [Linux qualification commands](DEPLOY_LINUX.md).

The agreed priority replaces the earlier suggestion of a long 181D continuation: **qualify Linux and reproduce accepted278 first, then go directly to implementing and validating the 860-generator extension.** Do not insert a prolonged 181D optimization campaign between those tasks. The existing 181D restart remains a reproducible baseline and recovery capability, not the next scientific campaign.

## Mathematical contract and baseline

On the whole plane, preserve

\[
(c_lX+U)\cdot\nabla\rho=\rho,\quad U=(-\psi_y,\psi_x),\quad-\Delta\psi=\rho_x,
\qquad \psi=\chi_{xy},\quad\rho=-\partial_y\Delta\chi=yf.
\]

Density is even in x and odd in y; use the canonical full-plane inverse, analytic center elimination and the five Taylor compatibility equations in [MATHEMATICS.md](MATHEMATICS.md). Both \(c_l\) and physical \(a_0=\rho_y(0)\ne0\) remain free. Keep exactly

\[
J_{\rm abs}=\frac{1}{\pi a_{\rm ref}^2}
\int_0^{\pi/2}\int_0^\infty |R_f|^2\,\frac{dr}{r}\,d\theta,
\qquad a_{\rm ref}=23.95065822465609,
\]

\[
R_f=(c_lx-\psi_y)f_x+(c_ly+\psi_x)f_y+
(c_l-1+\psi_x/y)f,\qquad R_\rho=yR_f.
\]

The reference amplitude is fixed solely in the objective. It is not a physical-amplitude constraint. Relative residuals remain secondary diagnostics.

The immutable starting profile is
`research/campaign/global181_v3/snapshots/accepted_00000278.json`, SHA-256
`812d34466c078e2ce643c49671299f4359f764fe2e1d925426762ba962d6e955`.
Its independently assessed values are \(c_l=1.8089923602744993\),
\(a_0=14.767729990606481\), \(J_{\rm abs}=4.2683726070948805\times10^{-9}\),
frozen sampled \(E_f=1.23849639744\times10^{-4}\),
\(E_\rho=7.16582921424\times10^{-5}\), and maximum C5 defect
\(4.88829345686\times10^{-14}\). Sampled maxima are not continuous supremum bounds.
A verified feasible descent direction exists; stationarity, basis convergence and an exact PDE solution have not been established.

## Milestone 1 — qualify the actual Linux environment

Before changing numerical code:

- Verify the repository, candidate and complete restart closure with `tools/verify_repository.py`, `tools/prepare_assets.py`, and the `inspect` / `restart-audit` actions. Use fresh independent writable work and result directories.
- Discover native CPU architecture, allocated physical/logical cores, CPU affinity or scheduler allocation, RAM and available RAM, cgroup limits, disk and installed Python/NumPy/SciPy/BLAS/LAPACK. A GPU is optional; there is no GPU implementation or A100 requirement.
- Follow [DEPLOY_LINUX.md](DEPLOY_LINUX.md): guarded smoke, a fresh adaptive whole-axis integral, two distinct native production residual replays, full provider/derivative qualification, and an independent current-only residual/Green-inverse assessment. Reproduce origin and C5 data, physical fields, frozen/refined sampled maxima, radial bands and far-field diagnostics. Bind every receipt to the actual environment, source, thread policy, mesh and resource session.
- Preserve the unchanged saved-vector replay limit `64*eps*max(norm(fresh),norm(saved),1e-300)`. If native arithmetic fails it, retain the failure and investigate a separately reviewed, same-endpoint numerical-epoch qualification; never overwrite the saved vector or loosen a tolerance to label migration successful.

**Go:** baseline scientific comparisons and destination arithmetic/resource gates pass with documented tolerances and numerical error diagnostics. **Stop:** unresolved hash, replay, derivative, integration or inverse failures. A source-Mac PASS is never a Linux PASS. Do not spend a long 181D campaign trying to qualify the environment.

## Milestone 2 — implement the exact extension, separately

Use a new versioned numerical module and new immutable basis manifest. Do not mutate the shipped `research/` production source bytes or accepted278. With
\(\gamma=1/c_l\), \(\lambda=1-\gamma\), \(p_j=(3+\gamma-j\lambda)/2\), implement

\[
\chi_{m,k,j}=r^{2k}(1+r^2)^{p_j-k}\cos(2m\theta),
\quad j=0,1,2,3,\quad m=0,\ldots,9,\quad k=m,\ldots,25.
\]

There are \(4\sum_{m=0}^{9}(26-m)=860\) generators. This is **not** a verified feasible-variable count. Replace the 186-generator coordinates by the exact analytical embedding; do not append 860 to the old 186. The old integer offsets and shifted-Legendre polynomials have finite expansions in \(t=r^2/(1+r^2)\), and the old fractional offsets belong to branches j=1,2,3. Derive and store the complete sparse coefficient map, unique order, normalization and source provenance; see [BASIS_860_SPEC.md](BASIS_860_SPEC.md). An undocumented least-squares projection is not an embedding.

Verify Cartesian smoothness, parity, exact dependencies and numerical rank/conditioning, all \(c_l\)-dependent exponents and moment derivatives, and the old-to-new map and its \(c_l\) derivative. The analytical embedding coefficients are independent of \(c_l\); testing their zero derivative does not replace the nonzero derivatives of the generators, analytic center or chart. Audit exceptional parameter values as well as generic current \(c_l\): branch collisions at \(c_l=3\), and potential-only polynomial/harmonic nulls when exponents take special values, must be distinguished from ordinary ill-conditioning. Test every old generator identity and meaningful mixed combinations, not just a single checkpoint value. Use high precision where cancellation makes binary64 comparisons misleading.

**Go:** generator identities and their physical/parameter derivatives pass independent tests with stated absolute/relative scales and cancellation diagnostics. **Stop:** an unresolved identity, ordering, rank or derivative defect. Do not silently remove weak directions or count every generator as a feasible coordinate.

## Milestone 3 — embed accepted278 and establish a feasible chart/gauge

Embed the saved profile analytically without a fit. Before any optimizer update, independently compare old and new representations of \(\chi\), \(\rho\), \(\psi\), \(U\), f and its smooth-axis quotients, residuals, Taylor jets, the canonical Green inverse, whole-axis loss, frozen/refined maxima and far-field coefficients. Include strict origin/axis, transition, overlap and very large-radius tests; carry the integrator's uncertainty rather than hiding a discrepancy behind a broad relative tolerance. Preserve \(c_l\) and physical \(a_0\) to the documented numerical accuracy.

Construct an enlarged chart with the same analytic-center and C5 equations, derivative semantics and feasibility checks. At the origin, directions with \(k\ge\max(m,5)\) have potential degree at least 10 and preserve the existing low Taylor data; lower-order directions still need actual constraint elimination/retraction. Audit the full constraint rank and resulting tangent dimension. Retain complete dependence on \(c_l\), including exponent/logarithm terms, coefficient maps, center elimination and chart response.

Treat spatial gauge honestly. Exact dilation is
\(\chi_L(X)=L^4\chi(X/L)\),
\(\rho_L(X)=L\rho(X/L)\),
\(\psi_L(X)=L^2\psi(X/L)\), and \(f_L(X)=f(X/L)\).
Both \(c_l\) and \(a_0\) are invariant, so neither can fix spatial scale. A fixed finite span built with \(1+r^2\) is not generally closed under arbitrary L. Document how the new representation handles an explicit length/dilation action and a genuine spatial-width gauge, or any resulting finite-span limitation; test the exact action at shifted coordinates, not by refitting. A width gauge needs a well-defined nondegenerate width observable, its derivatives and preservation of physical parameter freedom. Do not fabricate a null vector or fix \(c_l\), \(a_0\), or the loss-reference amplitude as a substitute.

**Go:** the embedded incumbent is physically unchanged within independently documented accuracy and all center/chart/gauge/rank checks pass. **Stop:** apparent improvement caused only by projection error, altered normalization, changed profile, relaxed constraints or truncated integration. This creates a new versioned enlarged-state format; the old 181D checkpoint is not automatically an exact enlarged optimizer restart.

## Milestone 4 — qualify the enlarged residual, Jacobian and integration

Keep the positive frozen-epoch residual-vector convention and the same whole-plane functional. Verify the enlarged evaluator, tail bounds/envelopes, near-origin high-precision algebra, adaptive interval expansion, radial and angular refinement, and independent stateless whole-axis integration. Do not describe a fixed truncated or finite quadrature as exactly scale invariant. Check exact spatial dilations separately, including 2, 16, 256 and 1024, with controlled domain/tail errors.

Validate full analytic Jacobian assembly and selected independent feasible finite differences, with multiple step sizes and explicit accuracy/error budgets. Include \(c_l\), physical \(a_0\), low-origin directions, all fractional branches/tail moments, weak singular directions and random mixed directions. Test the retraction and the derivative of every transformed coefficient/map. Directional agreement is not a stationarity certificate or a claim of independently differencing every column.

Measure memory before scaling to large node counts: record shapes, cache/workspace multiplicity and SVD storage. Exploit allocated multicore CPU and RAM with measured block/thread configurations and fixed-input reproducibility tests. Dense SVD remains the correctness reference; any alternate backend must match meaningful steps, original-matrix predicted decrease, feasibility and trust-region/KKT diagnostics, including weak directions. Do not replace SVD with unchecked normal equations or blindly allocate dense AD tensors. Do not infer RAM needs from an unrelated Boussinesq/GPU experiment. Require bounded sessions, exclusive locks, memory/disk/time floors, checkpoint grace and fresh telemetry; sampled RSS is not a hard allocation cap.

**Go:** derivatives, quadrature, tails, physical checks and backend/resource qualifications pass before a research trial. **Stop:** cancellation, loss of constraint rank, unresolved quadrature error or resource risk; refine the implementation or immutable epoch and requalify, rather than weakening acceptance.

## Milestone 5 — guarded pilot, then a substantive 860-generator campaign

Only on the qualified Linux machine, run a short resource-aware pilot from the embedded accepted278. Checkpoint complete proposals before validation; accept only feasible steps with positive training decrease, the established gain criterion and a **fresh independent per-trial whole-axis integral** whose uncertainty is small relative to predicted decrease. Keep strict source/mesh/counter binding, saved residuals, coordinate maps, full chart/gauge state, trust radius, accepted/rejected outcomes and atomic complete checkpoints. Test interruption/restart from a completed enlarged checkpoint before extending the run. No old 181D detached driver may silently start the enlarged experiment.

If pilot replay, resource and acceptance checks pass, proceed to a substantive high-dimensional campaign with an explicit new budget. This is the next scientific optimization, not a long 181D continuation. The first campaign retains the same \(J_{\rm abs}\) with **no hard \(\mathcal E_1=\mathcal E_2=\mathcal E_3=0\) constraints and no added far-field penalty**. Do not modify the current objective weights or fix \(c_l\) or physical \(a_0\).

At accepted checkpoints report independently: whole-axis loss and error diagnostics; frozen and refined sampled quotient/density maxima and locations; identical radial/near-origin/transition bands; relative diagnostics on the same points; physical parameters and stability; C5 and higher Taylor coefficients; Fourier coefficients, absolute angular norms and scale-invariant diagnostics for \(\mathcal E_1,\mathcal E_2,\mathcal E_3\), including unresolved modes. Never silently project away an angular error.

## Far-field limitation and scientific outcomes

The uniform cutoff m≤9 can produce leading density harmonics through 19 and stream harmonics through 20, hence nonlinear \(\mathcal E_1\) through 39 while F1 can represent only harmonics through 19. It is not generically closed. With \(\alpha_j=\gamma-j\lambda\),

\[
\mathcal E_1=-(c_l-1)F_1+(\gamma+1)\Phi_0F_0'-\gamma\Phi_0'F_0.
\]

A nonzero coefficient leaves \(R_\rho\sim r^{2\gamma-1}\mathcal E_1\) under the formal differentiable-expansion/remainder assumptions. At accepted278, \(2\gamma-1=0.105587864228\ldots>0\), with reported coefficient L2 norm about 0.440353421495. Small integrated or quotient loss does not guarantee uniform density-residual decay. The earlier missing-harmonic fraction **0.145222% applies to accepted165 only**, not accepted278 and not a prediction for the enlarged experiment. Compute it afresh.

Measure the inverse-even \(r^{-2q}\) correction lattice as well as fractional layers; do not demand that every radial binomial moment vanish. Use the supported earlier audit for possible resonance/logarithm and canonical multipole qualifications, without asserting an asymptotic theorem. A later branch-dependent cutoff \(M_j=(9,19,29,39)\) is a possible measured-error response, not this first campaign's implementation target.

A successful first experiment demonstrates trustworthy independent loss reduction in the enlarged space, documented regional/parameter behavior, correct constraints, reproducible restarts and honest asymptotic diagnostics. Loss decrease with worse regional maxima or nondecaying density residual is a mixed outcome and must be reported as such. Little progress, rank/conditioning failure, or an angular closure bottleneck is also informative: retain evidence and decide whether to improve arithmetic, charts, integration or angular closure. None of these outcomes establishes a PDE solution, stationarity or basis convergence by itself. Consider still larger spaces only after this evidence, with fresh cross-dimension comparisons.

No basis implementation or optimization is authorized on the original Mac by this documentation update. After cloning on Linux, give the receiving Codex the complete [NEW_SERVER_CODEX_PROMPT.md](NEW_SERVER_CODEX_PROMPT.md), or instruct it to read and execute that file.

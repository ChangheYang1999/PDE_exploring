# Receiving Linux Codex task: qualify accepted278, then implement and optimize the 860-generator extension

Read this complete file and execute the task on the destination Linux compute server. It is standalone research authorization for the ordered work below. First confirm the host is the intended Linux server. **Do not optimize on the source Mac Pro.** Discover the actual resources; do not assume a particular CPU, GPU, RAM capacity or cluster allocation. Do not push to GitHub automatically.

## Mission and immutable baseline

This checkout is a compact, self-contained handoff of the current whole-plane stationary self-similar incompressible porous medium (IPM) computation. All paths below are relative to the checkout unless explicitly introduced as fresh destination paths. Read `README.md`, `docs/MATHEMATICS.md`, `docs/CODE_GUIDE.md`, `docs/STATUS.md`, `docs/DEPLOY_LINUX.md`, `docs/RESTART.md`, `docs/HANDOFF_VALIDATION.md`, `docs/BASIS_860_SPEC.md` and `docs/NEXT_RESEARCH_PLAN_860.md`; inspect the actual implementation and manifests before coding. A documentation proposal is not implemented numerical functionality.

The agreed next research is **Linux qualification and independent reproduction of accepted278, immediately followed by a versioned 860-generator exact extension and enlarged-space optimization**. Do not insert a prolonged 181-dimensional continuation campaign. Existing 181D resume commands document the preserved baseline recovery protocol; they are not the next campaign to launch.

Preserve the checkout's production scientific bytes, accepted snapshots, epoch/source bindings and audit evidence. Make all new implementation, numerical epochs, output and resource sessions in separately versioned modules and fresh writable workspaces. Never overwrite the incumbent or relabel diagnostic trials as accepted. No source-Mac path, environment, wheel, live synchronization folder or optional bulk archive may be a runtime dependency. The separate original 5.29 GB archival release is out of scope. Do not bulk-import research history.

## Mathematical problem, objective and current numerical facts

On all of \(\mathbb R^2\), solve

\[
(c_lX+U)\cdot\nabla\rho=\rho,\qquad
U=(-\psi_y,\psi_x),\qquad-\Delta\psi=\rho_x.
\]

Density is even in x and odd in y, \(\rho=yf\), with smooth even f and physical \(a_0=\rho_y(0)\ne0\). The smooth even potential representation is \(\psi=\chi_{xy}\), \(\rho=-\partial_y\Delta\chi\); it imposes local Poisson identically. Retain the canonical whole-plane Poisson inverse, regular origin, stipulated subquadratic stream-function growth, analytic center elimination and five Taylor compatibility equations. Do not introduce a freely chosen harmonic correction or finite exterior boundary condition.

Use exactly the existing absolute loss, with fixed reference amplitude:

\[
R_f=(c_lx-\psi_y)f_x+(c_ly+\psi_x)f_y+
(c_l-1+\psi_x/y)f,\qquad R_\rho=yR_f,
\]
\[
J_{\rm abs}=\frac1{\pi a_{\rm ref}^2}
\int_0^{\pi/2}\int_0^\infty |R_f|^2\frac{dr}{r}\,d\theta,
\qquad a_{\rm ref}=23.95065822465609.
\]

Use smooth analytic axis limits. Relative residuals remain secondary diagnostics. Both \(c_l\) and physical \(a_0\) remain free; \(a_{\rm ref}\) is not a constraint on \(a_0\). Under exact spatial dilation L,
\(f_L(X)=f(X/L)\), \(\rho_L=L\rho(X/L)\), \(\psi_L=L^2\psi(X/L)\), so \(R_{f,L}(X)=R_f(X/L)\), and the continuous integral is invariant when finite. Both cl and a0 are dilation invariants. Finite quadrature is an approximation, not exactly invariant. Do not simulate dilation by refitting a finite basis or call fixing cl/a0 a spatial gauge.

The authoritative incumbent is
`research/campaign/global181_v3/snapshots/accepted_00000278.json`, SHA-256:

```text
812d34466c078e2ce643c49671299f4359f764fe2e1d925426762ba962d6e955
```

Its current implementation has **186 potential generators / 181 feasible variables**: 19 implicit core-chart variables including cl, plus 162 Global coefficients. **No 860-generator implementation or enlarged restart exists yet.** Independently assessed values are:

| Quantity | accepted278 |
|---|---:|
| cl | 1.8089923602744993 |
| Physical a0 | 14.767729990606481 |
| Whole-axis J_abs | 4.2683726070948805e-9 |
| Frozen sampled E_f = max \|R_f\|/a_ref | 1.23849639744e-4 |
| Frozen sampled E_rho = max \|R_rho\|/(r a_ref) | 7.16582921424e-5 |
| Maximum five-Taylor defect | 4.88829345686e-14 |

Sampled maxima are not continuum supremum bounds. Independent integration, reconstructed canonical inverse and clean relocated replay passed on the source Mac, **not on this Linux server**. The derivative audit evaluated all 181 analytic feasible columns and independent finite differences along seven selected directions at three step sizes; it found verified feasible descent, not stationarity. Its lower-loss diagnostic trial points were not promoted. No exact PDE solution, basis convergence or stationary endpoint is established. Some origin/transition residual bands worsened. The original density residual has a nonzero leading coefficient, reported angular L2 norm about 0.440353421495, and grows like \(r^{2/c_l-1}=r^{0.105587864228\ldots}\), despite a small integrated quotient loss. Extreme-radius binary64 cancellation requires high-precision controls.

## Gate 1: qualify Linux and independently reproduce the baseline before numerical changes

Inventory architecture, OS, Python, CPU allocation/cores, RAM, cgroup/container limits, free disk and BLAS/LAPACK/thread behavior. Install native dependencies from `environment/requirements.lock.txt`; the source reference is Python 3.9.6, NumPy 1.23.5, SciPy 1.9.3, psutil 6.0.0 and threadpoolctl 3.6.0 on Intel macOS. Do not copy its venv or incompatible wheels. Record any interpreter/package change and qualify it explicitly.

Start with these existing, nonoptimizing entry points, using absolute fresh output paths:

```sh
python3 -B tools/verify_repository.py
python3 -B tools/prepare_assets.py
python3 -B tools/portable.py inspect --output /absolute/fresh/checks/inspect.json
python3 -B tools/portable.py restart-audit --output /absolute/fresh/checks/restart.json
```

Then follow the **actual guarded commands** in `docs/DEPLOY_LINUX.md`: initialize a fresh native resource baseline with `research/hardware/guard.py`; run `tools/portable.py smoke`, `objective`, and two separate `replay` processes; perform the complete unchanged `stage13_model_benchmark_v3.py` provider/derivative qualification in a writable research copy; bind real passing evidence with `tools/make_qualification.py`. Use `tools/entrypoint.py` for supported unchanged workers. Run the current-only independent residual assessment with `--labels stage13_v3_accepted278`, including frozen holdouts, origin/Taylor checks, physical fields and canonical Green inverse. Read the shipped `verification/` results as references, not fresh Linux receipts. Document objective, fields, maxima/locations, regional values, Taylor defects, inverse errors, integration/tail errors and all discrepancies.

The actual unchanged residual replay limit is
`norm(r_fresh-r_saved) <= 64*eps*max(norm(r_fresh),norm(r_saved),1e-300)`.
Preserve source/parent/epoch checks. A different BLAS may fail this strict test. Preserve and report the failure; do not widen tolerances, overwrite the saved residual, fabricate qualification, or call a warm start an exact restart. Any necessary same-endpoint numerical-epoch transition must be explicitly documented and independently qualified before release. A blocking gate failure stops progression to optimization.

After passing baseline gates, **proceed directly to the enlargement**. Retain complete accepted278 recovery evidence, but do not launch its long 181D continuation merely because a resume command exists.

## Gate 2: implement the proposed 860 generators as an exact replacement of coordinates

Let \(\gamma=1/c_l\), \(\lambda=1-\gamma\), \(p_j=(3+\gamma-j\lambda)/2\), \(R=1+r^2\), \(t=r^2/R\), \(H_m=\operatorname{Re}(x+iy)^{2m}\). Implement, in new versioned modules,

\[
\chi_{m,k,j}=r^{2k}R^{p_j-k}\cos(2m\theta)
=H_mR^{p_j-m}t^{k-m},
\quad j=0,1,2,3,\quad m=0,\ldots,9,\quad k=m,\ldots,25.
\]

The count is \(4\sum_{m=0}^9(26-m)=860\) **generators**, not an already verified feasible dimension. Define and save one unique coefficient order and manifest. Audit functional rank, numerical conditioning, center constraints, C5 rank and any genuine dilation-gauge implementation before reporting the feasible dimension. Distinct radial branches can become exactly dependent at special cl values (including cl=3); audit exponent collisions throughout the admitted parameter range, not just at accepted278. Do not append these 860 to the old 186, silently drop weak directions, or treat all coefficients as unconstrained.

Every generator is origin-smooth because \(r^{2k}\cos(2m\theta)=r^{2(k-m)}H_m\) for k>=m. Corrections with \(k\ge\max(m,5)\) have potential degree at least 10 and leave f and psi_x/y through degree four unchanged. Lower-k coefficients need explicit center/C5 participation. Preserve analytic center elimination and the five equations specified in `docs/MATHEMATICS.md`; do not freeze physical a0 or cl to obtain rank.

Prove and implement the **analytic exact embedding** of every old generator, using the saved current ordering in `research/absolute_fields.py` and `research/inputs/global.json`:

- Old integer-offset core: \(H_mR^{p_0-m-\sigma}=R^{p_0}t^m(1-t)^\sigma\cos(2m\theta)\), \(\sigma=0,1,2\). Expand \((1-t)^\sigma\) finitely into k=m,...,m+sigma in j=0.
- Old fractional core offset \(\sigma=j\lambda/2\), j=1,2,3: exactly the new `(m,k=m,j)` generator.
- Old Global generator: \(R^{p_0}t^{\max(m,5)}\sqrt{2n+1}P_n(2t-1)\cos(2m\theta)\). Use
  \[
  P_n(2t-1)=\sum_{h=0}^n(-1)^{n-h}\binom nh\binom{n+h}h t^h,
  \]
  assigning to k=max(m,5)+h, j=0. Actual modes are m=0,...,8 and n=0,...,17 with `(3,0)` omitted, then `(9,0)` appended; all map within k<=25. Use the exact implemented normalization and coefficient order, including any binary normalization discrepancy requiring explicit error accounting.

Reconstruct analytic c0 before embedding accepted278. No least-squares projection, fitting or new optimization may substitute for this map. Verify identities symbolically/algebraically and numerically at multiple cl values and in cl-dependent derivatives, including the center chain. In every new exponent \(p_j'=-(j+1)/(2c_l^2)\); differentiate powers, logarithms, moments, physical operators, center/implicit constraints, explicit transport and all cl dependence. Large monomial expansion coefficients may cause cancellation: use stable evaluation and high-precision reference controls rather than assuming a formally exact map is numerically harmless.

Define the potential tail moments
\[
C_{m,j,q}=\sum_{k=m}^{25}a_{m,k,j}\binom{p_j-k}{q},
\quad C_{m,j,0}=\sum_k a_{m,k,j},\quad
C_{m,j,1}=\sum_k(p_j-k)a_{m,k,j}.
\]
For \(b=3+\gamma-j\lambda-2q\), \(C(\theta)=\sum_m C_{m,j,q}\cos(2m\theta)\), \(D=(b^2+\partial_\theta^2)C\), the physical coefficient maps are
\[
F=-[(b-2)\sin\theta D+\cos\theta D'],
\quad\Phi=\tfrac12\sin(2\theta)[b(b-2)C-C'']+(b-1)\cos(2\theta)C'.
\]
Density and stream powers are b-3 and b-2. Differentiate these maps completely. Do not require all inverse-even moments to vanish.

Before releasing an enlarged epoch, demonstrate that the embedded accepted278 retains cl, physical a0, full-plane fields, center/C5 data, independent whole-axis objective, frozen/refined sampled maxima and radial bands within documented, justified numerical error. Include exact axes, strict origin series/overlap tests, distant radii, canonical inverse and high-precision cancellation controls. Record generator/source/map hashes. The embedded enlarged starting state is a **new versioned numerical epoch**, not the original 181D optimizer state with an invented exact restart label.

## Gate 3: new feasible chart, complete derivatives, integration and resources

Construct the enlarged feasible chart with the existing analytic-center and C5 semantics. Audit constraint/tangent rank and scaling. A spatial gauge must concern the exact action \(\chi_L(X)=L^4\chi(X/L)\); distinguish it from parameter normalization and finite-space nonclosure under dilation. Use an explicit length/width action with a nondegenerate, differentiated width gauge, or document and resolve any finite-space limitation before the campaign. Keep cl and a0 free. Establish meaningful independent derivatives in selected directions including cl, physical-amplitude variation, low-order origin coefficients, leading/subleading tail moments, new high-angular coefficients and weak singular directions. Use multiple finite-difference step sizes, independent stateless evaluations, training/refined rules, adjoint/linear controls where useful and high precision near cancellation. Do not call a few sampled directional checks a complete stationarity certificate.

Preserve the residual-vector convention \(r_i=\sqrt{2w_i/(\pi a_{\rm ref}^2)}R_f(X_i)\), \(J=\tfrac12r^Tr\), and positive frozen per-epoch quadrature. Revalidate whole-log-radius integration with independent near-origin Taylor orders, high-precision overlap, adaptive interval expansion, radial and angular refinement and far-tail estimates. Each physical trial needs fresh independent whole-axis acceptance validation. A fixed truncated integral is not exactly scale invariant, and refinement diagnostics are not rigorous integral enclosures.

Discover and use destination multicore CPU/RAM efficiently. Benchmark actual residual, Jacobian and full thin-SVD work; scope BLAS/OpenMP threads and prevent oversubscription. Use blocking/caching or validated alternatives if justified, recording arithmetic/provider effects. Keep the full-SVD trust-region method as the reference. Do not replace it with unchecked normal equations, silently truncate weak positive singular values, blindly allocate dense AD tensors, infer memory from unrelated Boussinesq/GPU work, or require an A100. A GPU is optional only after independent validation of any new implementation.

Use fresh supervisor sessions, exclusive locks, actual available-memory/cgroup/disk limits, explicit wall budgets and safe stop policies. Complete checkpoints must contain coefficients/order, chart/gauge, tangent/scales, meshes/epoch, source/environment hashes, trust radius, accepted/rejected/trial/event counters, independent validation and atomic proposal/outcome/commit state. Preserve rejected-trial records and resource ledgers. Never reset counters, reuse an incomplete Jacobian batch or overwrite original accepted278. Exercise recovery from a complete checkpoint before extending the campaign.

## Far-field diagnostics: retain them without changing the first enlarged campaign

Assuming differentiated formal expansions, set \(\alpha_j=\gamma-j\lambda\), \(\rho\sim\sum_jr^{\alpha_j}F_j\), \(\psi\sim\sum_jr^{\alpha_j+1}\Phi_j\). The necessary angular relations are
\[
-\Phi_j''-(\alpha_j+1)^2\Phi_j=
\alpha_j\cos\theta F_j-\sin\theta F_j',
\quad F_j(0)=0,\ F_j'(\pi/2)=0,\ \Phi_j(0)=\Phi_j(\pi/2)=0,
\]
\[
\mathcal E_N=-N(c_l-1)F_N+
\sum_{i+j=N-1}[(\alpha_i+1)\Phi_iF_j'-\alpha_j\Phi_i'F_j],
\]
so \(\mathcal E_1=-(c_l-1)F_1+(\gamma+1)\Phi_0F_0'-\gamma\Phi_0'F_0\).
These are conditional formal coefficient identities, not a theorem that every exact profile has this expansion.

The uniform m<=9 family permits F_j only through odd density harmonic 19 and Phi_j through even harmonic 20. Nonlinear E1 can reach odd harmonic 39 and is generically not fully cancellable by that F1. Quantify **all** generated Fourier modes and unresolved high-mode norms for E1,E2,E3 without silently projecting them away. Raw angular norms depend on dilation; also report, where denominators are nonzero, \(a_{\rm ref}^N\|\mathcal E_N\|/\|F_0\|^{N+1}\) and term-sum normalized diagnostics. The old finding that the beyond-19 E1 remainder was about **0.145222%** of its norm concerned **accepted165**, not accepted278; accepted64 was another distinct audit input. It is motivation only, not a current prediction. Recompute for the embedded and new accepted states.

**First 860 campaign: do not impose E1=E2=E3=0, add a far-field penalty, change objective weights, or switch to relative loss.** Measure the defects while minimizing the unchanged J_abs. Even tiny unresolved E1 retains a growing density-residual term at current cl; small J_abs does not imply uniform density-residual decay. Under explicitly controlled differentiated remainders and branches, complete E1 cancellation would leave the next fractional power \(3\gamma-2<0\), but projected cancellation is insufficient.

The compactified family also has inverse-even corrections with exponents \(\gamma-j\lambda-2q\). Resonances \(\alpha+1=\pm2n\) can require logarithms; canonical exterior stream multipoles are determined by the whole source, not free additions, and first interact at density-residual power \(\gamma-4\), below the first three fractional corrections. Do not infer a full asymptotic theorem or demand all radial moments vanish. A later cutoff progression `M_j=(9,19,29,39)` could address angular closure, with corresponding regular radial support; **it is not the first enlargement to implement**.

## Gate 4: pilot, then substantive enlarged optimization and reporting

Once Gates 1–3 genuinely pass on Linux, this task authorizes a guarded, bounded pilot in the enlarged feasible space and then a substantive high-dimensional campaign with explicit resource/time budgets. Do not run a long 181D detour. Do not launch if embedding, C5/rank, derivatives, independent integration, recovery or resource gates fail; report the concrete blocker and preserve evidence.

Independently verify every accepted physical update. Before increasing a pilot budget, inspect complete accepted/rejected records, predicted/actual decrease, feasible lift, weak-direction behavior, integration agreement, parameters and resource use. Checkpoint safely at every accepted state and trial outcome; recover only from complete independently validated state. Stop on uncontrolled errors, exhausted policy or numerical gate failures; a budget stop is not convergence.

Produce reproducible source/manifests/tests, a baseline Linux qualification report, analytic embedding proof and numerical comparison, enlarged chart/rank/derivative/integration/restart reports, benchmark/resource policy and exact new campaign commands. Report improvement separately for whole-axis J_abs, frozen/refined sampled maxima and locations, radial bands, cl/a0, higher origin Taylor terms, C5 defects and all-angular E1/E2/E3 including unresolved modes. Record failures and error estimates; make no claim of stationarity, continuum maxima, uniform far-field decay, PDE existence or dimension convergence without corresponding evidence. Consider still larger angular/radial spaces only if measured outcomes justify them.

The source map is: `research/absolute_fields.py` and `research/base/spectral_basis.py` (current generators/fields); `research/inputs/global.json` (exact old Global order); `research/absolute_chart*.py` (analytic center/C5 chart); `research/stage13_model_v3.py` and its imported providers (cached residual/Jacobian); `research/whole_axis_mesh.py` and `research/stage13_integration_v*.py` (quadrature/independent integral); `research/stage13_solver.py` (full SVD); `research/stage13_campaign_v3.py` (acceptance/commits/recovery); `research/verification/scripts/` (independent assessments). Existing `tools/` entry points operate the baseline; **design, implement and document the future 860 entry points rather than inventing commands for an API that is not yet present**.

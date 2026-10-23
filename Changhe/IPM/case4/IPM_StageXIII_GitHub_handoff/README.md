# Whole-plane self-similar IPM: current 181-variable research state

This repository transfers one current accepted numerical state and the production code needed to reconstruct, verify and resume it. It is a research approximation, **not an exact stationary PDE solution**. Start with this page, then [the mathematics](docs/MATHEMATICS.md), [the code guide](docs/CODE_GUIDE.md) and [the numerical status](docs/STATUS.md).

## Problem and method

We seek a smooth stationary self-similar profile on the entire plane satisfying

\[
(c_l X+U)\cdot\nabla\rho=\rho,\qquad
U=(-\psi_y,\psi_x),\qquad-\Delta\psi=\rho_x.
\]

Density is even in x and odd in y, with \(\rho=yf\). The Poisson inverse is the canonical whole-plane inverse, rather than an independently chosen harmonic correction. A scalar potential \(\chi\) represents \(\psi=\chi_{xy}\) and \(\rho=-\partial_y\Delta\chi\). Analytic center elimination and five numerical Taylor compatibility equations are maintained throughout optimization.

The current approximation uses **186 fixed potential generators and 181 feasible optimization variables**: a 19-dimensional implicit chart for the 24 raw core parameters, plus all 162 Global coefficients. **Both \(c_l\) and the physical \(a_0=\rho_y(0)\) remain free.** There is no active 860-function basis.

The primary objective is the absolute, continuously scale-invariant loss

\[
J_{\rm abs}=\frac{1}{\pi a_{\rm ref}^2}
\int_0^{\pi/2}\int_0^\infty |R_f|^2\,\frac{dr}{r}\,d\theta,
\quad a_{\rm ref}=23.95065822465609,
\]

with fixed reference amplitude, not the changing \(a_0\). Production uses a frozen positive three-block whole-log-radius quadrature, an analytic Jacobian with complete \(c_l\) dependence, and a full thin-SVD Gauss–Newton trust-region method. Every physical trial needs a fresh independent whole-axis integral check before acceptance. Relative residuals are secondary diagnostics.

## Best accepted result and its limits

The authoritative accepted candidate is `research/campaign/global181_v3/snapshots/accepted_00000278.json`, SHA-256:

```text
812d34466c078e2ce643c49671299f4359f764fe2e1d925426762ba962d6e955
```

| Quantity | Independently assessed value |
|---|---:|
| \(c_l\) | 1.8089923602744993 |
| Physical \(a_0\) | 14.767729990606481 |
| \(J_{\rm abs}\) | 4.26837260709488e-9 |
| Sampled frozen-grid \(E_f=|R_f|/a_{\rm ref}\) maximum | 1.23849639744e-4 |
| Sampled frozen-grid \(E_\rho=|R_\rho|/(ra_{\rm ref})\) maximum | 7.16582921424e-5 |
| Maximum five-Taylor defect | 4.88829345686e-14 |

Independent integration, physical residuals, Taylor algebra and canonical Green inverse checks passed on the source environment. The endpoint derivative audit computed all 181 analytic columns and finite differences along **seven selected directions at three step sizes**, finding verified feasible descent. It did not certify stationarity or complete 181 independent finite-difference directions. Lower-loss diagnostic trial points were **not promoted** to accepted checkpoints.

Some near-origin regions worsened. The original density residual has a nonzero leading far-field term proportional to \(r^{0.105587864228\ldots}\); it therefore grows even while the quotient residual decays. No continuum supremum bound, basis convergence, exact PDE solution or stationary endpoint has been established. The production campaign stopped normally on its time budget; budget exhaustion is not convergence. See [STATUS.md](docs/STATUS.md) for exact scope.

## Next research: 860-generator expansion

**860 is planned and unimplemented. The verified baseline remains accepted278 in the current 181-dimensional feasible space.** The agreed next campaign is:

1. Qualify the native Linux environment and reproduce accepted278, its independent whole-axis loss, physical fields, center/five Taylor conditions, canonical Green inverse and residual diagnostics before changing numerical code.
2. Go directly to a versioned **860-generator exact extension** of the current 186-generator span, embedding the same physical profile analytically. Do not run a separate prolonged 181D continuation first.
3. Validate the embedding, full `c_l` derivatives, enlarged center/C5 chart, genuine spatial gauge, quadrature and resource policy; then run guarded pilot updates and a substantive enlarged campaign with the same `J_abs`. Both `c_l` and physical `a_0` remain free.
4. Track independent regional maxima, higher origin errors and far-field Fourier defects alongside the loss. The uniform angular cutoff is not nonlinearly closed: **do not impose hard `E_1=E_2=E_3=0` constraints or a new far-field penalty in this first campaign**.

Read the authoritative [next research plan](docs/NEXT_RESEARCH_PLAN_860.md), [exact basis and embedding specification](docs/BASIS_860_SPEC.md), and [standalone receiving Codex prompt](docs/NEW_SERVER_CODEX_PROMPT.md). After cloning on Linux, send that prompt's complete text to the receiving Codex, or ask Codex to read the file and execute it. Existing 181D resume commands are preserved as recovery references; they are not the default next research action.

No optimization is launched by repository construction or read-only validation. The exact Linux installation, relocated checks and qualification commands are in [DEPLOY_LINUX.md](docs/DEPLOY_LINUX.md); complete restart semantics are in [RESTART.md](docs/RESTART.md). Package pins are in `environment/requirements.lock.txt`. The repository contains no virtual environment, platform-specific wheel or GPU implementation.

Read-only entry points, after native installation and asset preparation, are:

```sh
python3 -B tools/portable.py inspect --output /absolute/fresh/checks/inspect.json
python3 -B tools/portable.py restart-audit --output /absolute/fresh/checks/restart.json
```

The guarded `smoke`, `objective` and `replay` actions check progressively more: fixed-point reconstruction, fresh whole-axis integration, and the actual cached residual against the saved vector at the original64-epsilon criterion. They launch no optimization. Follow the deployment guide to create the required resource session and use fresh output paths.

## Where to read the implementation

All paths in this table are relative to `research/`; the files retain the production bytes. Versioned filenames in the import closure are required implementation dependencies, not an invitation to select another solver.

| Component | Exact implementation entry |
|---|---|
| Potential basis, normalization and mode order | `absolute_fields.py:26–39`; `base/spectral_basis.py:58–160`; `inputs/global.json` |
| Analytic center elimination | `absolute_fields.py:42–100`; `absolute_chart.py:21–26` |
| Physical fields and complete raw Jacobian | `absolute_fields.py:111–205`; `absolute_fields_v2.py:16–52` |
| Origin Decimal algebra and independent point checks | `highprecision_origin.py:73–233`; `field_tests.py:16–38` |
| Five-Taylor feasible chart | `absolute_chart_v2.py:15–70`; `absolute_chart.py:119–153` |
| Weighted residual vector and mesh semantics | `absolute_model.py:27–161`; `whole_axis_mesh.py:22–68` |
| Selected production cache/arithmetic | `stage13_model_v3.py:61–107`; `stage13_model.py:24–161`; `stage13_stable_exp.py:19–91` |
| Independent whole-axis trial integration | `stage13_integration_v3.py:49–186`; `stage13_integration_v2.py:81–165,246–308` |
| Full-SVD trust-region solver | `stage13_solver.py:67–292` |
| Feasible step, acceptance and durable restart | `stage13_campaign_v3.py:145–247,329–372,436–560` |
| Independent residual and derivative assessments | `verification/scripts/independent_residual_assessment.py`; `verification/scripts/stationarity_assessment.py` |

[CODE_GUIDE.md](docs/CODE_GUIDE.md) explains the call graph, data shapes, numerical safeguards and restart semantics; [MATHEMATICS.md](docs/MATHEMATICS.md) states the actual formulas and assumptions. All files required for accepted-state restart are included in the main repository. A separate optional artifact retains bulk derivative-audit arrays; it is not required to reconstruct or resume the candidate. **A candidate JSON alone reconstructs a profile but does not constitute an exact optimizer restart.**

## Handoff boundary

The separate 5.29 GB archival release remains unchanged. This staging repository focuses on the current method and accepted endpoint; it does not retell the earlier research stages. Original absolute paths inside immutable provenance are handled by the explicit relocation adapter, without editing numerical inputs or creating old-path symlinks. Clean relocated tests report what was run and what remains destination-specific. No GitHub push is performed automatically.

Repository contents and clean relocation results are recorded in [HANDOFF_VALIDATION.md](docs/HANDOFF_VALIDATION.md). See [GITHUB.md](docs/GITHUB.md) for the explicit create/commit/push commands and [ARTIFACTS.md](docs/ARTIFACTS.md) for the optional evidence package.

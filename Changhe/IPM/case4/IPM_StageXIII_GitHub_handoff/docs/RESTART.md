# Complete accepted-state restart

The resume target is **accepted_00000278**, with **181 feasible variables**. The
physical state has `c_l = 1.8089923602744993`, `a_0 = 14.767729990606481`, and
independently integrated `J_abs = 4.2683726070948805e-9`. Both `c_l` and physical
`a_0` remain free through the existing feasible chart. This handoff neither fits
new coefficients nor changes the solver.

**Priority clarification (2026-10-23):** this document preserves the exact
**181D** continuation capability and its dependency closure. The agreed next
campaign is [Linux baseline reproduction followed directly by a versioned
860-generator expansion](NEXT_RESEARCH_PLAN_860.md), without a prolonged 181D
continuation. No enlarged restart, basis implementation or feasible dimension
is supplied. [BASIS_860_SPEC.md](BASIS_860_SPEC.md) defines the exact physical
embedding contract; that future coordinate change creates a new bound campaign
with parent provenance, rather than reusing the old 181D map/scales/counters as
if its dimensions were unchanged.

Use [DEPLOY_LINUX.md](DEPLOY_LINUX.md) for executable installation, validation,
qualification and guarded resume commands. Never execute the archived worker
directly: the relocation adapter resolves its immutable original path bindings
without rewriting scientific source or checkpoint JSON bytes.

## State that is retained

All files listed in [restart_plan.json](../metadata/restart_plan.json) are
included under `research/` with their original relative names and bytes. That
schema-specific list records each SHA-256, byte count and the exact runtime
check that requires it. Its original-source discovery closure is **138 files,
8,381,432 bytes**; additional independent-validation inputs are inventoried
separately by the repository-wide manifest.

| Retained component | Why the unchanged runtime requires it |
| --- | --- |
| `campaign/global181_v3/state.json` | Parameters, counters, trust radius, integration anchor, validation, coordinate scaling and source identities. |
| `campaign/global181_v3/snapshots/accepted_00000278.json` and `.npz` | Complete coefficient/basis manifest and saved residual/parameter arrays. The candidate SHA-256 is `812d34466c078e2ce643c49671299f4359f764fe2e1d925426762ba962d6e955`. |
| `campaign/global181_v3/coordinate_map.npz` | All 181 positive column scales and initial core tangent; no weak directions are removed. |
| `campaign/global181_v3/commits/event_00000318.json` | Final authoritative post-state against which recovery compares the incumbent. |
| `campaign/global181_v3/parent_continuation.json` and explicitly bound predecessor records | The existing recovery gate hashes these records, their seven commits, source map, candidate, coordinate map and saved arrays. They are compatibility data, not a research-history collection. |
| Qualified `epoch.json`, training/refined meshes and explicitly dereferenced proof JSON files | Immutable quadrature and provider-release gate; mesh arrays total 1,104,765 bytes. |
| All 51 hash-bound current numerical source files, required solver test source and 42 base Python files | The unchanged resume and integration gates verify these source bytes. Some compatibility-named modules remain imported or hash-bound; deleting them would invalidate the actual implementation. |
| `workspace.json`, fixed `inputs/candidates.json`, `provenance/base_manifest.json`, solver test result | Required source/input identity maps, positive fixed `a_ref`, and solver gate. |
| `provenance/stage13_numerical_sources_v2.json` and portable `hardware/` modules | Production private-source namespace identity, native supervisor and worker bootstrap. |
| `campaign/global181_v3/numerical_calls.jsonl` | Preserves cumulative call accounting when the next slice finishes. |
| `campaign/global181_v3/solver_benchmark.json` | Existing completion sentinel avoids rerunning the initial solver benchmark during resume. |

At handoff the state records accepted **278**, rejected **39**, trials **317**,
events **318**, cumulative accepted **284**, cumulative trials **324**, and trust
radius **0.0346351387852478**. The extra event is an initialization transition;
it is not an additional optimization trial. Counts and radius are not reset.

## Deliberate omissions

The unchanged `stage13_campaign_v3.recover` reads the greatest existing V3
`event_*.json` and compares its `post_state` with `state.json`; it does **not**
traverse earlier V3 commits. Consequently this compact handoff retains the exact
final commit only, while preserving the original event counter **318**. It does
not claim that the omitted 317 earlier V3 commit files are locally present.
Future commits still use `events + 1`; the original accepted/trial counters and
immutable incumbent are preserved. Every one of the seven explicitly hash-bound
predecessor commits is retained because the actual parent gate traverses them.

The old 128,973,160-byte `solver_benchmark.npz` matrix is unnecessary for either
reconstruction or unchanged recovery. Its JSON report is retained; the report's
matrix path is provenance and is not dereferenced on resume. Old candidate
snapshots, rejected-trial arrays, bulk guard telemetry and earlier-stage
reference outputs are also omitted unless an actual import or hash check
requires them. Original file references inside retained provenance JSON are
not a promise that all historical artifacts are shipped. Runtime reads outside
the included tree fail rather than falling back to a source-machine directory.

No large optional artifact is needed for **this accepted-state restart**. A
separate optional verification artifact, if supplied with the release, contains
additional independent-audit evidence arrays and is not required to reconstruct
the candidate or run its current production solver.

## Recovery gates on the new server

1. Verify every repository manifest hash and copy `research/` into a new writable
   workspace. Preserve the immutable checkout and initial incumbent.
2. Run the relocation structural preflight. It invokes the actual source,
   predecessor, integration and solver proof gates; it must report missing files
   as a failure.
3. Reproduce candidate fields, five Taylor conditions, independent whole-axis
   integral and physical residual diagnostics in the new native environment.
   Record Python, NumPy, SciPy, BLAS, architecture, threads and resources.
4. Run the provider/derivative qualification described in the Linux runbook.
   Original-host proof JSON is a dependency and provenance, not evidence that a
   different Linux/BLAS environment has passed fresh tests.
5. Require the unchanged endpoint residual replay tolerance:
   `norm(r_fresh-r_saved) <= 64*eps*max(norm(r_fresh),norm(r_saved),1e-300)`.
   The recovery gate deliberately refuses a new host if this strict test fails.
   Do not weaken it, overwrite the saved NPZ or relabel a warm start as exact
   resume. A different arithmetic provider needs a separately reviewed
   qualification/requalification path.
6. For the agreed next research, stop before launching the old optimizer and
   proceed directly to the 860 implementation/embedding gates. The exact 181D
   slice API below is retained for a separately requested recovery exercise;
   it is not required to reproduce accepted278 and does not resume an enlarged
   state. No outer driver or optimization is automatically started by this handoff.

The raw worker's required argument meanings are:

```text
stage13_campaign_v3.py
  --label global181_v3
  --start <workspace>/campaign/global181/snapshots/accepted_00000006.json
  --epoch <workspace>/integration_epochs/epoch0004_v3_w4_released_iofix/epoch.json
  --parent-campaign <workspace>/campaign/global181
  --resume --workers 4 --block-size 1024 --expected-extra 162 --seconds 300
```

`--start` remains the saved parent template because the existing resume API
uses it to bind the chain; **the actual resumed coefficients and residual come
from accepted278 through the saved state**, not from that template. These raw
arguments are consumed by the guarded relocation wrapper in the Linux runbook;
they are not a command to run without that wrapper.

## Implementation references

- `research/stage13_campaign_v3.py:110`: explicit predecessor hash gate.
- `research/stage13_campaign_v3.py:261`: solver and integration source gate.
- `research/stage13_campaign_v3.py:329`: authoritative checkpoint recovery and
  strict endpoint replay; appends a continuation record only after replay passes.
- `research/stage13_campaign_v3.py:436`: bounded loop, safe complete snapshots,
  immutable commits and checkpoint stop behavior.
- `research/stage13_integration_v3.py:50`: immutable mesh loading.
- `research/stage13_integration_v3.py:70`: exact finite qualification-reference
  closure. Nested unused provenance paths are not recursively loaded.
- `tools/build_restart_plan.py`: standard-library-only source packaging audit;
  never imports the numerical model or launches a trial.

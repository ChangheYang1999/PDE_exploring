# Compact handoff inventory and validation

Prepared 2026-10-23. Entry point: [README.md](../README.md). The main Git payload
is approximately **18 MB**, including the complete accepted278 restart state.
There are no files near GitHub's ordinary 100 MB file limit. Exact per-file
sizes and SHA-256 values are in `metadata/repository_manifest.json` (the manifest
does not hash itself). Run `python3 -B tools/verify_repository.py` to check them.
Git's local object storage and ignored runtime products are separate from that
payload; neither a virtual environment nor verification logs are pushed.

## Essential inventory

| Contents | Location and purpose |
|---|---|
| Current mathematical problem, actual basis, center/Taylor algebra and scale-invariant loss | `docs/MATHEMATICS.md` |
| AI-readable production call graph, Jacobian, full-SVD solver and cache | `docs/CODE_GUIDE.md` |
| Scientific status, independently verified descent, origin/far-field defects and priorities | `docs/STATUS.md` |
| Linux installation, guarded checks, qualification and explicit resume commands | `docs/DEPLOY_LINUX.md` |
| Exact continuation closure and counters/maps/epoch semantics | `docs/RESTART.md`, `metadata/restart_plan.json` |
| Production scientific implementation and current verification workers | `research/` (original source bytes; 103 Python files including dependency closure) |
| Authoritative accepted profile and numerical state | `research/campaign/global181_v3/snapshots/accepted_00000278.{json,npz}`, `state.json`, final commit, fixed coordinate map, epoch/meshes and required parent bindings |
| Saved exact basis manifest | `research/inputs/global.json` |
| Independent frozen-grid inputs | `research/inputs/absolute_assessment_{design.json,coordinates.npz}` and `materials/assessment_grids_stage12.json.gz` |
| Native environment pins and fresh resource-policy templates | `environment/` |
| Relocation, verification, asset restoration and explicit execution adapters | `tools/` |
| Current scientific results and new relocation receipts | `verification/` |
| Origin/hash correspondence to unchanged scientific files | `metadata/source_copies.json` |

The schema-derived minimal recovery closure is **138 files / 8,381,432 bytes**.
Additional main-repository files provide independent verification, frozen grids,
source explanations and portable deployment. Only the last authoritative V3
commit is shipped. Earlier V3 iterates, old campaign logs, redundant snapshots,
Mac environments and the unused 129 MB solver benchmark matrix are omitted.
The small parent and provider-proof files retained by hash are compulsory
unchanged-recovery dependencies, not a history narrative or alternative method.

## Clean relocated verification: PASS

Tests ran from `/Users/caltech/research/IPM_stage13_github_clean_20261023`, outside
the original research tree, using a newly created native Python 3.9.6 virtual
environment. Packages were installed from the pinned dependency specification.
The path adapter denied original research reads at CPython's open/listdir/scandir
audit boundary; no original research reads occurred. The selected system Python
runtime is allowed. This is not a native-code system-call sandbox.

| Check | Outcome |
|---|---|
| `pip check`, exact compressed-input restoration and structural restart audit | PASS |
| 13 physical sample points, finite-rule reconstruction and high-precision Taylor algebra | PASS |
| Actual frozen production source, immutable-parent and epoch gates | PASS |
| Two separate native four-thread complete production residual replays | Both bitwise identical; norm difference 0, unchanged limit 1.31300493779e-18 |
| Fresh adaptive independent whole-axis absolute loss | 4.2683726070948805e-9; difference from reference 0 |
| Whole-axis numerical error diagnostic | 2.87591220263e-19; accuracy gate PASS (not a rigorous bound) |
| Maximum five-Taylor defect | 4.88829345686e-14 |
| Plan-only resume without installed site packages | PASS; no numerical imports required |
| Unguarded or unqualified execution rejection | PASS |
| Exact copied scientific files | 156 hash comparisons; no mismatches |
| Document links, adapter syntax and credential-pattern scan | PASS |

The four guarded numerical checks used 305.436 total wall seconds, with peak
sampled worker-family RSS 1,875.137 MiB. All four supervisor results passed with
no resource stops. Source and destination measurements, BLAS identities, exact
argument vectors, guard results and test outputs are retained under
`verification/relocation/`. Full runtime logs remain in the ignored clean test
workspace. Initial packaging checks exposed a missing dynamic import/bootstrap
and overly broad runtime-directory exclusion; both were corrected before these
final relocated tests. No tolerances or scientific source bytes were changed.

**These are macOS relocation tests, not Linux qualification.** Full new-host
derivative/provider qualification is explicitly required before any Linux
optimization. The previously completed current-candidate derivative and residual
audits are preserved; they were not rerun as a new optimization campaign here.
The production solver's strict replay may fail under a different BLAS. Preserve
that failure and use a separately reviewed numerical-epoch transition if needed;
do not widen the tolerance or silently replace residuals.

## Separate optional evidence and preservation

The original full derivative-audit arrays/probes are an optional
**683,566,328-byte** archive, outside this repository. They are not needed to
reconstruct, independently recompute or resume the candidate. See
[ARTIFACTS.md](ARTIFACTS.md) for its 141-file inventory, SHA-256 and commands.

The original **5,294,393,108-byte** archival release was independently rehashed.
Its SHA-256 remains
`3eefc02a1063d2d69ae04caad319008091eb11ae944ea8876af86209b9743e36`;
its nanosecond modification time is unchanged. The proof is
`verification/archival_preservation.json`.

No optimization, candidate promotion, solver modification, basis expansion,
automatic detached process, Git commit, GitHub repository creation or push was
performed. The local repository is initialized on `main`; follow
[GITHUB.md](GITHUB.md) to publish it deliberately.

## Documentation-only 860-plan update — 2026-10-23

The historical PASS statements above are unchanged. The README, current-status
and baseline code/deployment/restart guides now distinguish the preserved 181D
accepted278 from the **planned, unimplemented** 860-generator extension. The
authoritative next sequence is Linux qualification and accepted278 reproduction,
then direct versioned 860 development and validation, without a prolonged 181D
detour. The first enlarged campaign retains the original absolute loss; it adds
neither hard E1/E2/E3 matching nor a far-field penalty.

New documents are [the ordered plan](NEXT_RESEARCH_PLAN_860.md),
[the basis/embedding specification](BASIS_860_SPEC.md), and
[the standalone Linux Codex prompt](NEW_SERVER_CODEX_PROMPT.md). A small
[portable derivation extract](reference/FAR_FIELD_DERIVATION_EXTRACT.md) and
`metadata/farfield_derivation_provenance.json` retain the earlier mathematical
work, separating accepted64/165 evidence from current accepted278. No audit
arrays or optional bulk archives were added.

New checks passed: repository checksums after inventory refresh; documentation
links and Git whitespace; exact 860 count/unique proposed ordering and old-mode
embedding index support; all 13 source-provenance hashes; preservation of the
current numeric status table; and 191 existing scientific/runtime/input/evidence
file hashes. These are documentation and integrity checks, not a new basis
implementation, physical embedding test or enlarged-chart validation.

`git diff --check` passes for the new working-tree changes. The pre-existing
initial staged import reports three blank-line-at-EOF warnings in frozen
`research/base/engine/{fit_impl.py,stage6_engine.py,stage8.py}`. Their original
bytes and the pre-existing index were preserved; these are not new document
whitespace defects. The exact warnings are retained in the new checks receipt.

A fresh minimal copy under the staging repository's ignored
`runs/documentation_860_20261023/relocated_checkout/` passed standard-library-only
manifest verification, exact compressed-asset restoration, `inspect` and
`restart-audit`, with no original research reads. Tests and command receipts are
in `verification/documentation_860_20261023/`. The first attempt to write a
relocated receipt outside the allowed copy was correctly rejected by the
unchanged source-root audit hook; final checks wrote inside the copy and then
copied their receipts. No hook or tolerance was changed.

This update reran no PDE numerical evaluation or optimizer and makes no Linux
PASS claim. Production source bytes, snapshots, prior audit evidence and the
5.29 GB archival release remain unchanged. All new writes stay inside the
handoff staging repository. The pre-existing Git index was preserved; review
the working-tree edits and new files before `git add`, commit or push. No GitHub
operation or process start/stop/duplication was performed.

After cloning on Linux, send the receiving Codex the complete text of
`docs/NEW_SERVER_CODEX_PROMPT.md`, or ask it to read that file and execute it.

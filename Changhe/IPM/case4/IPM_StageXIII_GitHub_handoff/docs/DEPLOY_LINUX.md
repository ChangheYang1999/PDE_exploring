# Deploy, validate, and resume on Linux

Start with [README.md](../README.md), [CODE_GUIDE.md](CODE_GUIDE.md), and
[RESTART.md](RESTART.md). The shipped candidate is accepted278; the campaign
stopped at its time budget. This repository contains the current implementation
and exact recovery closure, not a fresh optimization run. Neither `c_l` nor the
physical center amplitude `a_0` is frozen by this handoff.

**Research order updated 2026-10-23:** complete the baseline qualification and
accepted278 reproduction below, then proceed directly to
[NEXT_RESEARCH_PLAN_860.md](NEXT_RESEARCH_PLAN_860.md) and
[BASIS_860_SPEC.md](BASIS_860_SPEC.md). There is no implemented 860 worker or
enlarged checkpoint yet. Do not insert a prolonged 181D continuation between
baseline reproduction and the new versioned implementation. The standalone
instructions for the receiving AI are [NEW_SERVER_CODEX_PROMPT.md](NEW_SERVER_CODEX_PROMPT.md).

## Native environment and preparation

Use a native CPython environment and the pinned dependencies. The measured
source environment is Python 3.9.6, NumPy 1.23.5, SciPy 1.9.3, psutil 6.0.0,
threadpoolctl 3.6.0, Intel x86_64 macOS. Linux/ARM and a different BLAS require
fresh qualification; a Mac PASS is not a Linux PASS. Do not copy the Mac venv or
install wheels for another architecture. Python 3.9 is the reference version;
if using another supported interpreter, record it and treat the environment
change as requiring the same full validation.

The following commands assume a native `python3.9` has already been installed.
Choose fresh directories and substitute the checkout location:

```sh
export REPO=/absolute/path/to/IPM-current
export PY="$HOME/venvs/ipm-current/bin/python"
python3.9 -m venv "$HOME/venvs/ipm-current"
"$PY" -m pip install --only-binary=:all: -r "$REPO/environment/requirements.lock.txt"
"$PY" -m pip check
"$PY" -B "$REPO/tools/verify_repository.py"
"$PY" -B "$REPO/tools/prepare_assets.py"
export CHECKS="$HOME/ipm_checks/server_01"
mkdir -p "$CHECKS"
"$PY" -B "$REPO/tools/portable.py" inspect --output "$CHECKS/inspect.json"
"$PY" -B "$REPO/tools/portable.py" restart-audit --output "$CHECKS/restart.json"
```

`prepare_assets.py` restores the exact compressed independent-grid JSON, with
its original SHA-256, into the ignored runtime location. It does not generate a
new grid. The standard-library inspect and restart audit perform no numerical
experiments. They bind the latest candidate, all frozen source hashes, exact
NPZ/chart/epoch/parent files, last authoritative event, and qualification proof
files used by unchanged recovery. The audit deliberately does not claim to
have executed `recover()` or to have qualified the new machine.

## Fresh resource baseline and numerical verification

Review `environment/smoke_policy.json` against the server's available RAM, disk,
CPU allocation, container/cgroup limits, and cluster rules. Write any chosen
policy to `$CHECKS`; never alter saved historical baselines. The example uses
one BLAS thread for the ordinary independent checks. `--workers 4` in production
selects scoped BLAS concurrency; it does not request four Python processes.
The guard's RSS is sampled, not a kernel-enforced allocation guarantee.

```sh
export SESSION="$CHECKS/session"
export GUARD="$REPO/research/hardware/guard.py"
"$PY" -B "$GUARD" init --session-dir "$SESSION" --disk-path "$CHECKS" \
  --policy "$REPO/environment/smoke_policy.json"
"$PY" -B "$GUARD" run --session-dir "$SESSION" --cwd "$CHECKS" \
  --lock-file "$CHECKS/verification.lock" --label value_smoke \
  -- "$PY" -B "$REPO/tools/portable.py" smoke --output "$CHECKS/smoke.json"
"$PY" -B "$GUARD" run --session-dir "$SESSION" --cwd "$CHECKS" \
  --lock-file "$CHECKS/verification.lock" --label whole_axis_objective \
  -- "$PY" -B "$REPO/tools/portable.py" objective --output "$CHECKS/objective.json"
"$PY" -B "$GUARD" run --session-dir "$SESSION" --cwd "$CHECKS" \
  --lock-file "$CHECKS/verification.lock" --label strict_replay_01 \
  -- "$PY" -B "$REPO/tools/portable.py" replay --output "$CHECKS/replay_01.json"
"$PY" -B "$GUARD" run --session-dir "$SESSION" --cwd "$CHECKS" \
  --lock-file "$CHECKS/verification.lock" --label strict_replay_02 \
  -- "$PY" -B "$REPO/tools/portable.py" replay --output "$CHECKS/replay_02.json"
```

These commands launch no optimization, chart trial, finite-difference probes,
or new accepted candidates. The ordinary smoke checks 13 fixed physical
locations, a 288-node positive finite rule, the five Taylor conditions using
independent high-precision algebra, and the saved residual norm. Its finite
rule value is **not** the whole-axis `J_abs`. The objective action additionally
calls the unchanged adaptive independent integrator: origin order comparisons,
85-digit overlap, interval expansion, radial/angular refinement, and infinity
envelope. It uses `target_abs=1e-16`, the integrator's accuracy gate, and the
unchanged epoch comparison limit `2.5e-15`. Error estimates are numerical, not
rigorous interval bounds.

Each replay executes the actual production source/parent/epoch gates and one
fresh cached four-thread residual evaluation. It compares the complete vector
to accepted278's NPZ using the unchanged norm limit
`64*eps*max(norm(fresh),norm(saved),1e-300)`. It calls neither `recover()` nor a
Jacobian and writes no continuation journal. The two guard calls are separate
native processes. A strict replay failure blocks exact resumption. Preserve
the failed evidence; do not widen the tolerance or replace the saved residual.
An explicit same-endpoint numerical epoch transition, with independently
reviewed qualification, is the existing solver's alternative; this handoff
does not fabricate or automatically release such a transition.

## Complete destination derivative/provider qualification

Before any research trial, make a separate writable copy of the prepared
scientific directory. The unchanged benchmark below evaluates the complete
raw Jacobian, all added coefficient finite differences, the feasible chart,
the full `c_l` dependence, adjoint controls, and the actual cached provider at
thread settings 1/4/8. It may take substantial time and memory. It tests
unaccepted perturbations but does not run an optimizer. This command has not
been executed on the destination by packaging this repository.

```sh
export WORK="$HOME/ipm_work/current181_01"
mkdir -p "$WORK"
rsync -a "$REPO/research/" "$WORK/"
export CANDIDATE="$WORK/campaign/global181_v3/snapshots/accepted_00000278.json"
export MESH="$WORK/integration_epochs/epoch0002_v2_w4/meshes/training.npz"
```

Create a fresh qualification session with a policy appropriate for this
benchmark. `environment/production_policy.example.json` is a template to review,
not a portable assertion about the server's resources:

```sh
export QUAL_SESSION="$CHECKS/qualification_session"
cp "$REPO/environment/production_policy.example.json" "$CHECKS/qualification_policy.json"
"$PY" -B "$GUARD" init --session-dir "$QUAL_SESSION" --disk-path "$WORK" \
  --policy "$CHECKS/qualification_policy.json"
"$PY" -B "$GUARD" run --session-dir "$QUAL_SESSION" --cwd "$WORK" \
  --lock-file "$CHECKS/verification.lock" --label complete_model_derivatives \
  -- "$PY" -B "$REPO/tools/entrypoint.py" --workspace "$WORK" \
     --worker stage13_model_benchmark_v3.py --execute -- \
     --candidate "$CANDIDATE" --mesh "$MESH" \
     --output "$WORK/results/new_host_model_benchmark" --workers 1 4 8 --block-size 1024
"$PY" -B "$REPO/tools/make_qualification.py" \
  --objective "$CHECKS/objective.json" \
  --replay "$CHECKS/replay_01.json" --replay "$CHECKS/replay_02.json" \
  --benchmark "$WORK/results/new_host_model_benchmark/checks.json" \
  --output "$CHECKS/NEW_HOST_QUALIFICATION.json"
```

The qualification builder requires real passing current-candidate outputs,
distinct successful native replay runs, complete derivative/provider checks,
matching host/architecture/interpreter and frozen sources, plus fresh
supervisor baseline/result hashes. It records an attestation binding these
files; it cannot replace missing tests. The historical epoch proof files remain
necessary exact recovery inputs, but are not relabeled as fresh Linux tests.

For a full fresh independent residual/maxima/canonical-inverse assessment of
the handed-off current candidate, use the shipped evaluator with its explicit
current-only label. This is more work than the smoke; choose a suitable
supervisor time budget first:

```sh
"$PY" -B "$GUARD" run --session-dir "$QUAL_SESSION" --cwd "$WORK" \
  --lock-file "$CHECKS/verification.lock" --label independent_current_assessment \
  -- "$PY" -B "$REPO/tools/entrypoint.py" --workspace "$WORK" \
     --worker verification/scripts/independent_residual_assessment.py --execute -- \
     --output "$WORK/results/independent_current_assessment" \
     --labels stage13_v3_accepted278
```

The evaluator preserves frozen holdouts, denser refinements, origin checks,
distant radial bands, independent integration and canonical Poisson inverse
tests. Its maxima are sampled, not continuous supremum certificates. The other
three labels appearing in the unchanged evaluator's source are unused by this
command; their obsolete checkpoint payloads are not required. Complete
stationarity diagnostics can later be explicitly dispatched through
`verification/scripts/stationarity_assessment.py`; they do not substitute for
the already verified descent finding. These workers operate the baseline;
the agreed versioned expansion has its own implementation and acceptance gates
in [NEXT_RESEARCH_PLAN_860.md](NEXT_RESEARCH_PLAN_860.md).

## Reference only: existing 181D exact resume API

The following commands document the preserved current restart API. They are
**not the next campaign in the agreed 860 plan**. Baseline qualification and
read-only replay above do not require an optimization slice. Use an 181D slice
only if separately requested; otherwise move directly to the new basis and
embedding gates after reproducing accepted278. No command for starting an 860
campaign exists yet.

First create a plan. No numerical modules, optimization, detached driver, or
time-budget extension are launched by this command:

```sh
"$PY" -B "$REPO/tools/entrypoint.py" --workspace "$WORK" \
  --worker stage13_campaign_v3.py --plan-output "$CHECKS/resume_plan.json" -- \
  --label global181_v3 \
  --start "$WORK/campaign/global181/snapshots/accepted_00000006.json" \
  --epoch "$WORK/integration_epochs/epoch0004_v3_w4_released_iofix/epoch.json" \
  --parent-campaign "$WORK/campaign/global181" --resume \
  --workers 4 --block-size 1024 --expected-extra 162 --seconds 3300
```

`--start` here is the immutable seed required by the unchanged recovery
protocol. With `--resume`, the actual `p`, 162 coefficients, radius, column
scales, counters and validation state come from the complete accepted278
continuation state; this does **not** restart from accepted6. See
[RESTART.md](RESTART.md). There is no weak singular-direction truncation and
no replacement fixed-domain relative objective.

Only if an 181D recovery slice is separately requested, after every check passes
and a new research budget is chosen, execute it under a **new** session. The example grants
3300 worker seconds; a full iteration/checkpoint can finish beyond that value.
It does not revive the exhausted historical detached driver:

```sh
export RUN_SESSION="$CHECKS/research_session"
"$PY" -B "$GUARD" init --session-dir "$RUN_SESSION" --disk-path "$WORK" \
  --policy "$CHECKS/qualification_policy.json"
"$PY" -B "$GUARD" run --session-dir "$RUN_SESSION" --cwd "$WORK" \
  --lock-file "$CHECKS/verification.lock" --label resumed181_slice01 \
  -- "$PY" -B "$REPO/tools/entrypoint.py" --workspace "$WORK" \
     --worker stage13_campaign_v3.py --execute --allow-research \
     --qualification "$CHECKS/NEW_HOST_QUALIFICATION.json" -- \
     --label global181_v3 \
     --start "$WORK/campaign/global181/snapshots/accepted_00000006.json" \
     --epoch "$WORK/integration_epochs/epoch0004_v3_w4_released_iofix/epoch.json" \
     --parent-campaign "$WORK/campaign/global181" --resume \
     --workers 4 --block-size 1024 --expected-extra 162 --seconds 3300
```

The wrapper verifies host-bound evidence and exact source bytes. The unchanged
solver then performs its own recovery gates and strict residual replay before
any step. Future slices use the same workspace and `--resume`; keep all newly
written commits, complete checkpoints, rejected proposals, and resource ledgers.
Do not delete state, reconstruct it from the coefficient-only JSON, reset
counters, or silently reuse partial Jacobian batches.

The agreed next research uses the qualified baseline as an exact physical seed
for the versioned 860 expansion, then validates the enlarged chart, derivatives
and independent integration before pilot updates. Track the whole-plane loss,
regional maxima, origin terms and far-field defects independently. The existing
descent finding remains distinct from any later stationarity claim. An enlarged
space does not itself establish basis convergence, an exact PDE solution or a
continuous supremum bound.

## Relocation mechanism

`tools/runtime.py` translates old absolute path strings only after JSON
decoding and never edits frozen scientific files, coefficients, arrays, or
hashes. Unused historical provenance roots map to absent directories. Its
CPython audit hook denies original research reads/listing; the relocated
checkout/workspace and selected interpreter runtime are explicit exceptions.
This is a relocation test, not a sandbox for native extension system calls.
Do not run the original Mac-only `launch.py` or detached outer driver.

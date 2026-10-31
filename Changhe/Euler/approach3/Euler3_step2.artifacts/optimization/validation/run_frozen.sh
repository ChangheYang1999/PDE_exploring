#!/bin/bash
# Frozen-copy launcher for the (l) work (lead 10:58:47Z item 1): the run imports only a copy of its sources made at launch (validation helpers and the
# production src/ package), with a sha256 manifest written before the computation; data directories (starts, status) are read through symlinks; the
# accepted scope file and the same-function records the run needs are copied in. Outputs land in the run directory's validation/ and are then copied
# into the main validation/ directory by hand with their hashes (never overwriting).
# v12 2026-10-29T18:1xZ: + record_63a.py (6.3 (a) record v1) in the copied list; its outputs land in <copy>/validation/records_63a/ (v11 kept as run_frozen.sh.v11_pre_record63a).
# v11 2026-10-29T16:3xZ (V374): add-on and pre-input records COPIED into the copy; LINKED_INPUTS.txt lists the remaining symlinks (gate records) with their launch-time hashes (v10 kept as run_frozen.sh.v10_pre_copy_inputs).
# v9 2026-10-29T16:0xZ: + links to gauge_row_dd_inputs_*.sha256 (verifier 16:00:50Z; v8 kept as run_frozen.sh.v8_pre_sha_links).
# v8 2026-10-29T15:5xZ: + links to g1_step_addon_*.json and gauge_row_dd_inputs_* (v7 kept as run_frozen.sh.v7_pre_addon_links).
# v7 2026-10-29T15:4xZ: + scripts/worker_d6.py and scripts/ledger.py copied and hashed (jc_eval_state.py imports the worker); v6 kept as run_frozen.sh.v6_pre_worker.
# v6 2026-10-29T14:4xZ: + g3_direction_capture.py in the copied list (v5 kept as run_frozen.sh.v5_pre_capture).
# Usage: validation/run_frozen.sh <run name> <gpu index or cpu> <script relative to validation/> [args...]
set -u
MAIN=RUN_ROOT/numerics/degree6_free_parameters_48h; PY=python3
NAME=$1; GPU=$2; SCRIPT=$3; shift 3
RUN=$MAIN/runs_l/$NAME; [ -e "$RUN" ] && { echo "run dir exists: $RUN"; exit 1; }
mkdir -p "$RUN/validation" "$RUN/src" "$RUN/scripts"
for f in worker_d6.py ledger.py; do [ -f "$MAIN/scripts/$f" ] && cp "$MAIN/scripts/$f" "$RUN/scripts/"; done   # v7 (15:4xZ): the production worker (gpu_v1p1) for jc_eval_state.py, hashed in the manifest
cp -r $MAIN/src/. "$RUN/src/"; find "$RUN/src" -name '__pycache__' -prune -exec rm -rf {} + 2>/dev/null
for f in dd_chain.py dd_tables.py dd_elementary.py dd_pressure.py l_eval.py l_power.py l_trig_qual.py l_screen.py gates.py record_63a.py g1_coverage_check.py g8_controls.py segment_report.py jac_cost.py g24_complete.py g3_addon.py g1_step_addon.py g5c_allm_capture.py g3_direction_capture.py gauge_row_diag.py gauge_row_dd.py jc_eval_state.py s11_closure_diag.py g8_controls_cases.py __init__.py; do [ -f "$MAIN/validation/$f" ] && cp "$MAIN/validation/$f" "$RUN/validation/"; done
[ -f "$MAIN/validation/l_scope.json" ] && cp "$MAIN/validation/l_scope.json" "$RUN/validation/"
for f in $MAIN/validation/dd_chain_check_*.json; do [ -f "$f" ] && case "$f" in *SMOKE*) ;; *) cp "$f" "$RUN/validation/";; esac; done
ln -s $MAIN/starts "$RUN/starts"; ln -s $MAIN/status "$RUN/status"; mkdir -p "$RUN/validation/logs"
for f in $MAIN/validation/gates_gpu_v1_*.json; do [ -f "$f" ] && ln -s "$f" "$RUN/validation/$(basename $f)"; done   # immutable gate records (threshold inputs), linked not copied
for f in $MAIN/validation/g1_step_addon_*.json $MAIN/validation/gauge_row_dd_inputs_*.json $MAIN/validation/gauge_row_dd_inputs_*.npz $MAIN/validation/gauge_row_dd_inputs_*.sha256; do [ -f "$f" ] && cp "$f" "$RUN/validation/$(basename $f)"; done   # v11 (16:3xZ, V374): the (k) add-on records and the (n)(5) pre-input records are COPIED (immutable in the copy), no longer linked
# v11: the large gate records above are symlinks (7 MB each); their launch-time hashes are in the manifest, and LINKED_INPUTS.txt names them so that no manifest entry is described as frozen when it is a link
( cd "$RUN" && for l in $(find validation -maxdepth 1 -type l); do echo "$(sha256sum "$l" | cut -d' ' -f1)  $l  -> $(readlink "$l")  (symlink: hashed at launch; the target is a registered record that must not change)"; done > "$RUN/LINKED_INPUTS.txt" )
( cd "$RUN" && find src validation scripts -type f -name '*.py' | sort | xargs sha256sum > "$RUN/SOURCES_SHA256.txt"; sha256sum validation/*.json >> "$RUN/SOURCES_SHA256.txt" 2>/dev/null )
echo "$(date -u +%FT%TZ) frozen copy for $NAME: $(wc -l < $RUN/SOURCES_SHA256.txt) files hashed; launching $SCRIPT $*" | tee -a "$RUN/launch.log"
if [ "$GPU" = "cpu" ]; then CVD=""; DEV=cpu; else CVD=$GPU; DEV=cuda:0; fi
cd "$RUN" && CUDA_VISIBLE_DEVICES=$CVD OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 10 taskset -c 31-34 $PY -u validation/$SCRIPT "$@" > "$RUN/validation/logs/${SCRIPT%.py}.log" 2>&1; rc=$?
echo "$(date -u +%FT%TZ) exit $rc" | tee -a "$RUN/launch.log"; exit $rc

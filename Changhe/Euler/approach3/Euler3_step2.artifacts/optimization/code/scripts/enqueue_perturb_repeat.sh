#!/bin/bash
# P1 perturbation repeat (lead 04:15:58Z item 2 (3); SPEC 7.4 (e)): (1) scripts/perturb_start_free.py v1.1 on the P1 s4 segment-end state file starts/P1s4_end_base_state.pt
# (--size 1e-3 non-axisymmetric coefficient perturbation, --param-perturb 1e-3 in z_c and z_w, recorded seed) on the given GPU through the busy guard (VALIDATION; blocking,
# about 10 min; manual ledger row written); (2) a FRESH FREE start from that file (enqueue_d6.py, worker keep path at the file's own parameters), max_iter 240, 7200 s, the
# production configuration of P1 s5 (release_queue COMMON stamps), label FREE, moved to queue/staged for the slot governor (one GPU alone). Fresh entry (not resume): the
# damping starts from lam0; the record states this (lead item 2 (3)). v2 (V628): an existing output is consumed only if its sidecar binds the exact provenance (tool v1.1, source path and sha256, output sha256, seed, size 1e-3, param perturbation 1e-3, guards true, usable true).
# v5 (06:2xZ; V659): the job note names the two registered comparisons (7.4 (e) against P1 s4; path reproducibility against P1 s5). v4 (05:4xZ): the perturbation runs directly inside the held launcher lock (no nested l_launch_v6). v3 (V633): the sidecar seed must be the exact integer (type int, equal; 7.5 or True refused).
# Usage: bash scripts/enqueue_perturb_repeat.sh <gpu for the perturbation> <target gpu for the job> <exclusive 0|1> [seed=7]
set -u; cd "$(dirname "$0")/.."; D=$(pwd); PY=python3; export CUDA_VISIBLE_DEVICES=
PGPU=$1; GPU=$2; EXCL=$3; SEED=${4:-7}
SRC=starts/P1s4_end_base_state.pt; SH=$(sha256sum $SRC | cut -c1-16); [ "$SH" = "60df5e72844f8689" ] || { echo "REFUSED: base file sha256 $SH differs from the registered 60df5e72844f8689"; exit 3; }
OUT=starts/P1s4_pert_1e-3_pp1e-3_s${SEED}.pt
if [ ! -f "$OUT" ]; then
  T0=$(date -u +%FT%TZ)
  # v4 (05:4xZ): this script runs UNDER scripts/enqueue_under_lock.sh, which already holds the launcher lock and has checked busy <= 3; the perturbation is launched directly
  # (foreground, one computation) instead of through validation/l_launch_v6.sh, whose flock on the same lock file would never be granted (nested-lock stall of 05:42Z to 05:47Z).
  (cd $D && CUDA_VISIBLE_DEVICES=$PGPU OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 10 taskset -c 31-34 $PY scripts/perturb_start_free.py $SRC $OUT --size 1e-3 --seed $SEED --param-perturb 1e-3 --device cuda:0 > validation/logs/perturb_P1s4_s${SEED}.out 2>&1)
  T1=$(date -u +%FT%TZ)
  $PY - "$T0" "$T1" "$PGPU" "$OUT" <<'PYEOF'
import json, sys, datetime as dt
t0, t1, gpu, out = sys.argv[1:5]; f = lambda s: dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
row = dict(kind="gpu_use", what=f"perturb_start_free.py {out} (P1 perturbation repeat start, 7.4 (e))", label="VALIDATION", gpu=int(gpu), start=t0, end=t1, hours=round((f(t1) - f(t0)).total_seconds() / 3600.0, 4), note="hand-launched through the busy guard; perturbation generation, no optimizer step")
open("status/gpu_hours_manual.jsonl", "a").write(json.dumps(row) + "\n"); print("ledger row:", row)
PYEOF
fi
[ -f "$OUT" ] || { echo "REFUSED: the perturbed start $OUT was not written (see validation/logs/perturb_P1s4_s${SEED}.out)"; exit 4; }
[ -f "$OUT.UNUSABLE" ] && { echo "REFUSED: $OUT is marked UNUSABLE: $(head -3 $OUT.UNUSABLE)"; exit 4; }
# v2 (V628): the sidecar must bind the exact provenance of the file before it is consumed: tool, source path and sha256, output sha256, seed, both perturbation sizes, usable
SRCSHA=$(sha256sum $SRC | cut -d' ' -f1); OUTSHA=$(sha256sum $OUT | cut -d' ' -f1)
$PY - "$OUT.json" "$SRC" "$SRCSHA" "$OUTSHA" "$SEED" "$OUT" <<'PYEOF' || { echo "REFUSED: the sidecar $OUT.json does not bind the requested provenance (see the assertion above); the file is not consumed"; exit 4; }
import json, sys, os
d = json.load(open(sys.argv[1])); src, srcsha, outsha, seed, out = sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]), sys.argv[6]
assert d.get("usable") is True, "usable is not true"
assert d.get("tool") == "scripts/perturb_start_free.py v1.1", f"tool {d.get('tool')!r}"
assert os.path.abspath(d.get("source", "")) == os.path.abspath(src), f"source {d.get('source')!r}"
assert d.get("source_sha256") == srcsha, "source sha256 mismatch"
assert d.get("out_sha256") == outsha, "output sha256 mismatch (the file differs from the one the sidecar describes)"
assert os.path.abspath(d.get("out", "")) == os.path.abspath(out), f"out {d.get('out')!r}"
assert type(d.get("seed")) is int and d.get("seed") == seed, f"seed {d.get('seed')!r} is not the integer {seed}"      # v3 (V633): exact integer seed, no int() coercion, bool excluded
assert float(d.get("size_requested")) == 1e-3, f"size_requested {d.get('size_requested')!r}"
assert float(d.get("param_perturb")) == 1e-3, f"param_perturb {d.get('param_perturb')!r}"
assert d.get("size_guard_ok") is True and d.get("m0_unchanged_bitwise") is True and d.get("E_l1_unchanged_bitwise") is True, "a perturbation guard is not true"
print("provenance bound:", out, outsha[:16], "seed", seed)
PYEOF
read CL OM < <($PY -c "import torch; S=torch.load('$OUT', map_location='cpu', weights_only=False); print(repr(float(S['z'][-2])), repr(float(S['z'][-1])))")
eval "$(grep '^COMMON=' scripts/release_queue.sh)"; EXTRA="{$COMMON}"
TAG=f3_P1s4_pert_s${SEED}
$PY scripts/enqueue_d6.py --start $OUT --label FREE --tag $TAG --c_l $CL --omega $OM --param_init keep_coefficients --max_iter 240 --time_limit 7200 --priority 29 --extra "$EXTRA" --note "lead 2026-10-30T04:15:58Z item 2 (3); SPEC 7.4 (e) perturbation repeat of the P1 s4 segment-end state: starts/P1s4_end_base_state.pt (60df5e72844f8689..., bytes-equal to the P1 s4 checkpoint) perturbed OFFLINE by scripts/perturb_start_free.py v1.1 (coefficient perturbation of relative size 1e-3 on m != 0 modes, parameter perturbation 1e-3 in z_c and z_w, seed $SEED; file $OUT sha256 $(sha256sum $OUT | cut -c1-16), record $OUT.json); FRESH FREE start at the file's own parameters ($CL, $OM) (fresh entry, damping from lam0: not a resume), max_iter 240, 7200 s, the P1 s5 production configuration; two named comparisons (lead 04:50:45Z item 4; V630): (a) SPEC 7.4 (e) return test against the perturbed origin P1 s4 (parameters within the 1 per cent half-widths of the P1 s4 sensitivity record and O1 within 1 per cent of the P1 s4 value 1.5616e-7; a continuing descent fails the O1 part and is reported as such), (b) path reproducibility against P1 s5 at equal optimizer time and at equal accepted iterations (fresh entry from a perturbed file against a resume); 7.4 (e) met only if (a) passes; branch identity by the registered rule" || exit 1
F=$(ls queue/pending/${TAG}_*.json | head -1); [ -f "$F" ] || { echo "no pending file for $TAG"; exit 1; }
$PY - "$F" "$GPU" "$EXCL" <<'PYEOF'
import json, sys, os, shutil
p = sys.argv[1]; j = json.load(open(p)); j["objective"] = "O1"; j["exclusive"] = None; j["gpus_allowed"] = None; j["placement"] = "governor"
j["target"] = dict(gpu=int(sys.argv[2]), exclusive=(sys.argv[3] == "1"))
j["record_label_job"] = "full release under the post-result timing rule 3.6 (m)"; j["g1_label_job"] = "G1 under post-result rules 3.6 (j), (k), (l), (n)"
j["lineage_history"] = "SPEC 7.4 (e) perturbation repeat of the P1 segment-4 end state (fresh FREE start from an offline perturbed file) under the full release of 2026-10-29T16:40:13Z; Phase III item started early (lead 04:15:58Z); not a continuation of the P1 lineage"
j["note"] = (j.get("note") or "") + "; placement by the slot governor (SPEC 3.6 (h) (1)); objective O1; launched under the FULL RELEASE of 2026-10-29T16:40:13Z (status/FULL_RELEASE_ACK)"
json.dump(j, open(p, "w"), indent=1); dst = p.replace("/pending/", "/staged/"); os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.move(p, dst); print("staged", dst)
PYEOF

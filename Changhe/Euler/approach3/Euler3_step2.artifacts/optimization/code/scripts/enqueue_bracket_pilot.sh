#!/bin/bash
# FREE bracket pilot (lead 03:13:16Z item 4; deliverable B): a saved field at a moved parameter (family F2, breadth, not a lineage continuation): the P1 s4
# segment-end coefficients kept (worker standard keep path, param_init_mode keep_coefficients) at (c_l, omega) = (c_l of the base, 1.80), i.e. log omega
# +0.246 above the P1 s4 end; FREE, 60 it / 1800 s, the production configuration (release_queue COMMON stamps, v1.25 labels), same exclusion rules; no automatic
# promotion. Base file: starts/P1s4_end_base_state.pt (sha256 60df5e72844f8689...; bytes-equal to the P1 s4 checkpoint z_full; starts/P1s4_end_base_state.json).
# Usage: bash scripts/enqueue_bracket_pilot.sh <gpu> <exclusive 0|1> [omega=1.80] [tag=f2_P1s4_om1p80]
set -u; cd "$(dirname "$0")/.."; PY=python3; export CUDA_VISIBLE_DEVICES=
GPU=$1; EXCL=$2; OM=${3:-1.80}; TAG=${4:-f2_P1s4_om1p80}
ST=starts/P1s4_end_base_state.pt; SH=$(sha256sum $ST | cut -c1-16); [ "$SH" = "60df5e72844f8689" ] || { echo "REFUSED: base file sha256 $SH differs from the registered 60df5e72844f8689"; exit 3; }
CL=$($PY -c "import torch; S=torch.load('$ST', map_location='cpu', weights_only=False); print(repr(float(S['z'][-2])))")
eval "$(grep '^COMMON=' scripts/release_queue.sh)"; EXTRA="{$COMMON}"
$PY scripts/enqueue_d6.py --start $ST --label FREE --tag $TAG --c_l $CL --omega $OM --param_init keep_coefficients --max_iter 60 --time_limit 1800 --priority 24 --extra "$EXTRA" --note "lead 2026-10-30T03:13:16Z item 4: FREE bracket pilot (family F2: a saved field at a moved parameter; breadth, not a lineage continuation): the P1 s4 segment-end coefficients (starts/P1s4_end_base_state.pt, sha256 60df5e72844f8689..., bytes-equal to runs/cont1_s4_S01 checkpoint_segment_end.pt z_full) kept at (c_l, omega) = ($CL, $OM) = log omega +0.246 above the P1 s4 end (1.4068972); purpose (deliverable B): P1 and F2 rose in omega from below; a start above the trend tests whether omega falls back toward 1.3 to 1.5 or keeps rising; pilot 60 it / 1800 s; its end record reports the core a_max ratios against its own start and against P1_start_v10 (6.3 (g) growth relative to S01); no automatic promotion (lead decides at 05:30Z)" || exit 1
F=$(ls queue/pending/${TAG}_*.json | head -1); [ -f "$F" ] || { echo "no pending file for $TAG"; exit 1; }
$PY - "$F" "$GPU" "$EXCL" <<'PYEOF'
import json, sys, os, shutil
p = sys.argv[1]; j = json.load(open(p)); j["objective"] = "O1"; j["exclusive"] = None; j["gpus_allowed"] = None; j["placement"] = "governor"
j["target"] = dict(gpu=int(sys.argv[2]), exclusive=(sys.argv[3] == "1"))
j["record_label_job"] = "full release under the post-result timing rule 3.6 (m)"; j["g1_label_job"] = "G1 under post-result rules 3.6 (j), (k), (l), (n)"
j["lineage_history"] = "bracket pilot started under the full release of 2026-10-29T16:40:13Z from the P1 s4 segment-end state (a saved field at a moved parameter, F2 family); not a continuation of the P1 lineage"
j["note"] = (j.get("note") or "") + "; placement by the slot governor (SPEC 3.6 (h) (1)); objective O1; launched under the FULL RELEASE of 2026-10-29T16:40:13Z (status/FULL_RELEASE_ACK)"
json.dump(j, open(p, "w"), indent=1); dst = p.replace("/pending/", "/staged/"); os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.move(p, dst); print("staged", dst)
PYEOF

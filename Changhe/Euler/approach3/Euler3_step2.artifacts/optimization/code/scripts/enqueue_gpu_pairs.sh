#!/bin/bash
# SPEC v1.13 3.6 (f) (lead 05:02Z item 5): at the PROVISIONAL RELEASE, P1 S01 on GPU 4 and P2 S09 on GPU 5; FREE and FIXED-CONTROL of a pair run together on
# the same GPU or each alone on its own GPU (SPEC v1.14 3.6 (h) (1): both members of a pair under the same sharing condition; alone when a GPU would otherwise
# idle). Placement by the PLACE variable: four fields tag:gpu:excl for P1 FREE, P1 FIXED, P2 FREE, P2 FIXED, e.g. PLACE="4:1 5:1 6:0 6:0" (default) puts P1's
# members alone on GPUs 4 and 5 (exclusive) and P2's members together on GPU 6 (non-exclusive; 2 x 26.2 GB + 8 GB < 80 GB). enqueue_d6.py is unchanged:
# the job files' "exclusive" and "gpus_allowed" are set after enqueue. Segment 1: max_iter 120, time limit 3600 s.
# Usage: [PLACE="4:1 5:1 6:0 6:0"] scripts/enqueue_gpu_pairs.sh [max_iter=120] [time_limit_s=3600] [segment_tag=s1]
# Configuration: snapshot gpu_v1, dd_fp64jac (module default), lagged Jacobian off, complete gradient every 4 accepted steps (R5; lagJ off => at every step),
# SPEC v1.13 labels, records "pre-verifier". Supervisor: configs/supervisor_gpu456.json with slots_per_gpu 2.
cd "$(dirname "$0")/.."; PY=python3
MI=${1:-120}; TL=${2:-3600}; SEG=${3:-s1}
# v4 2026-10-29T09:5xZ: new jobs carry spec_version v1.19 (lead 09:53:37Z item 2); segment-2 continuations keep their segment-1 cfg
# v3 2026-10-29T08:5xZ (PROVISIONAL RELEASE note 08:50Z): PLACE defaults to "flex": no gpus_allowed, exclusive null, "placement": "governor" in the job file; the
# slot governor places each pair when it starts (two clear GPUs: alone; one clear GPU: together) and every record carries "G1 under post-result rules 3.6 (j), (k)".
# v2 2026-10-29T08:36Z: labels SPEC v1.18 (binding), production worker gpu_v1p1 (snapshot gpu_v1 + worker cd35acf01f770dfb, SPEC 3.6 (i)), G1 label per pair
# (lead 07:41Z item 5: records that rest on the post-result G1 rules carry 'G1 under post-result rules 3.6 (j), (k)'); job objective set to O1 after enqueue
# (enqueue_d6.py labels every job with --extra 'variant'; the extra keys here are solver settings and labels, the objective is O1 with closure_lambda 1e-3, all5far).
COMMON='"lag_jacobian": false, "precision_mode": "dd_fp64jac", "complete_gradient_every": 4, "spec_version": "v1.19", "spec_sha256": "e5251d44ef7531ab687fc5fbb3dfa3561d31ba50eb52cd813094140f4dd6c1ee", "release_battery": "GPU (v1.13 to v1.19)", "snapshot": "gpu_v1p1", "record_label": "pre-verifier"'
EXTRA1="{$COMMON, \"g1_label\": \"G1 under post-result rules 3.6 (j), (k) (release-wide label, lead 08:50Z item 1; S01_own itself passes the registered G1 rule)\"}"
EXTRA2="{$COMMON, \"g1_label\": \"G1 under post-result rules 3.6 (j), (k) (S09_own rests on both post-result rules; lead 08:50Z item 1)\"}"
NOTE="SPEC v1.18 3.6 (f)/(h)/(i) pair, segment $SEG, GPU, pre-verifier, worker gpu_v1p1 (snapshot gpu_v1 + worker cd35acf01f770dfb)"
export CUDA_VISIBLE_DEVICES=
PLACE=${PLACE:-flex}
if [ "$PLACE" = "flex" ]; then read -r P1F P1C P2F P2C <<< "x:g x:g x:g x:g"; else read -r P1F P1C P2F P2C <<< "$PLACE"; fi
$PY scripts/enqueue_d6.py --start starts/S01_nest6_cl0.45_om1.0_p0.pt --label FREE          --tag p1_${SEG}_S01  --max_iter $MI --time_limit $TL --priority 30 $( [ "${P1F%%:*}" != "x" ] && echo --gpus ${P1F%%:*} ) --extra "$EXTRA1" --note "$NOTE"
$PY scripts/enqueue_d6.py --start starts/S01_nest6_cl0.45_om1.0_p0.pt --label FIXED-CONTROL --fixed --tag p1c_${SEG}_S01 --max_iter $MI --time_limit $TL --priority 29 $( [ "${P1C%%:*}" != "x" ] && echo --gpus ${P1C%%:*} ) --extra "$EXTRA1" --note "$NOTE"
$PY scripts/enqueue_d6.py --start starts/S09_d6w_cl0.45_om0.3_R1.pt  --label FREE          --tag p2_${SEG}_S09  --max_iter $MI --time_limit $TL --priority 28 $( [ "${P2F%%:*}" != "x" ] && echo --gpus ${P2F%%:*} ) --extra "$EXTRA2" --note "$NOTE"
$PY scripts/enqueue_d6.py --start starts/S09_d6w_cl0.45_om0.3_R1.pt  --label FIXED-CONTROL --fixed --tag p2c_${SEG}_S09 --max_iter $MI --time_limit $TL --priority 27 $( [ "${P2C%%:*}" != "x" ] && echo --gpus ${P2C%%:*} ) --extra "$EXTRA2" --note "$NOTE"
set_excl() { $PY - "$1" "$2" <<'PYEOF'
import json, sys; p, mode = sys.argv[1], sys.argv[2]; j = json.load(open(p)); j["objective"] = "O1"  # the --extra keys are solver settings and labels; closure_lambda 1e-3, nl_denominator all5far unchanged
if mode == "g":
    j["exclusive"] = None; j["gpus_allowed"] = None; j["placement"] = "governor"
    j["note"] += "; placement by the slot governor when the pair starts: alone on two clear GPUs or together on one clear GPU, both members started together (SPEC 3.6 (h) (1); lead 08:50Z item 4); objective O1"
else:
    ex = mode == "1"; j["exclusive"] = ex
    j["note"] += ("; alone on its GPU (exclusive)" if ex else "; shares its GPU with its pair partner (non-exclusive)") + " (SPEC v1.14 3.6 (h) (1)); objective O1"
json.dump(j, open(p, "w"), indent=1); print("placement", mode, "exclusive", j["exclusive"], "gpus_allowed", j["gpus_allowed"], p)
PYEOF
}
set_excl "$(ls queue/pending/p1_${SEG}_S01_*.json | head -1)" "${P1F##*:}"; set_excl "$(ls queue/pending/p1c_${SEG}_S01_*.json | head -1)" "${P1C##*:}"
set_excl "$(ls queue/pending/p2_${SEG}_S09_*.json | head -1)" "${P2F##*:}"; set_excl "$(ls queue/pending/p2c_${SEG}_S09_*.json | head -1)" "${P2C##*:}"
echo "enqueued P1 S01 and P2 S09 pairs (placement $PLACE), segment $SEG: max_iter $MI, time limit $TL s; start the governor and the supervisor: bash scripts/start_production_gpu456.sh"

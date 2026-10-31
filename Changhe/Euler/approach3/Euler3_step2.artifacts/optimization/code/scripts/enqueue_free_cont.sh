#!/bin/bash
# Generic FREE continuation of an ended segment (lead 04:15:58Z items (5), (6) and the F2 m4 rule; worker resume path through scripts/enqueue_segment2.sh: cfg unchanged
# except max_iter = end + INC and time_limit TL), the full-release job labels and a CORRECT lineage_history passed by the caller (enqueue_continuation_v122.sh carries the
# P1/P2 wording, which is false for the pilot-promoted lineages F1 and F2 and for P3), then moved to queue/staged for the slot governor. Tag must not match ^p[0-9].
# Usage: bash scripts/enqueue_free_cont.sh <ended run dir> <tag> <target gpu> <exclusive 0|1> <time_limit s> <iterations> "<lineage_history text>"
set -u; cd "$(dirname "$0")/.."; PY=python3; export CUDA_VISIBLE_DEVICES=
RUN=$1; TAG=$2; GPU=$3; EXCL=$4; TL=$5; INC=$6; LIN=$7
case "$TAG" in p[0-9]*) echo "REFUSED: tag $TAG matches the governor's pair regex"; exit 2;; esac
bash scripts/enqueue_segment2.sh "$RUN" "$TAG" "$GPU" "$EXCL" "$INC" "$TL" || exit 1
F=$(ls queue/pending/${TAG}_*.json | head -1); [ -f "$F" ] || { echo "no pending file for $TAG"; exit 1; }
LIN="$LIN" $PY - "$F" <<'PYEOF'
import json, sys, os, shutil, hashlib
p = sys.argv[1]; j = json.load(open(p)); c = j["config"]
j["label"] = "FREE"; j["objective"] = "O1"; j["placement"] = "governor"; j["exclusive"] = None; j["gpus_allowed"] = None
j["spec_version_job"] = "v1.25"; j["spec_sha256_job"] = "acd5406d92973592c2b45e7c5f3a484e5e80234ba8d2f4e271b509076c941e64"
j["record_label_job"] = "full release under the post-result timing rule 3.6 (m)"; j["g1_label_job"] = "G1 under post-result rules 3.6 (j), (k), (l), (n)"
j["release_note_job"] = "lead 2026-10-29T16:40:13Z FULL RELEASE (labels at the job level; cfg unchanged except max_iter and the time limit)"
j["lineage_history"] = os.environ["LIN"]
j["jc_record"] = "by EVAL after the segment end (validation/jc_eval_state.py v5, V370; 3.6 (o)); cfg unchanged by the worker's continuation rule (a)"
j["note"] = (j.get("note") or "") + "; FREE continuation (scripts/enqueue_free_cont.sh); not a pair member; cfg identical to the previous segment except max_iter and time_limit (worker rule (a)); job-level labels 'full release under the post-result timing rule 3.6 (m)' and 'G1 under post-result rules 3.6 (j), (k), (l), (n)'"
json.dump(j, open(p, "w"), indent=1)
dst = p.replace("/pending/", "/staged/"); shutil.move(p, dst)
print("staged", dst, "job", j["job_id"], "max_iter", c["max_iter"], "time", c["time_limit_per_start"], "target", j.get("target"), "config_sha256", hashlib.sha256(json.dumps(c, sort_keys=True).encode()).hexdigest()[:16])
PYEOF

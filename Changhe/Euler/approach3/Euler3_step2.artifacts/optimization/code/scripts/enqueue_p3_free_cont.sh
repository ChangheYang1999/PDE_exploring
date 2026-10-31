#!/bin/bash
# P3 FREE-only continuation (lead 02:11:51Z item 3 and 02:40:47Z item 6: the idle-slot fallback before the 08:30Z selection: a P3 FREE continuation of 3600 s,
# NOT a pair; no P3 FIXED-CONTROL before 08:30Z). Through scripts/enqueue_segment2.sh (worker resume path from the segment-2 end checkpoint; cfg unchanged except
# max_iter = end + 120 and time_limit 3600 s), then the job-level labels of the full release and a P3-specific lineage_history (enqueue_continuation_v122.sh carries
# the P1/P2 lineage text, which would be false for P3), then moved to queue/staged for the slot governor. The tag must not match the governor's pair regex ^p[0-9].
# Usage: bash scripts/enqueue_p3_free_cont.sh <previous P3 FREE run dir> <tag> <target gpu> <exclusive 0|1> [time_limit=3600] [iterations=120]
set -u; cd "$(dirname "$0")/.."; PY=python3; export CUDA_VISIBLE_DEVICES=
RUN2=$1; TAG=$2; GPU=$3; EXCL=$4; TL=${5:-3600}; INC=${6:-120}
case "$TAG" in p[0-9]*) echo "REFUSED: tag $TAG matches the governor's pair regex"; exit 2;; esac
bash scripts/enqueue_segment2.sh "$RUN2" "$TAG" "$GPU" "$EXCL" "$INC" "$TL" || exit 1
F=$(ls queue/pending/${TAG}_*.json | head -1); [ -f "$F" ] || { echo "no pending file for $TAG"; exit 1; }
$PY - "$F" <<'PYEOF'
import json, sys, os, shutil, hashlib
p = sys.argv[1]; j = json.load(open(p)); c = j["config"]
j["label"] = "FREE"; j["objective"] = "O1"; j["placement"] = "governor"; j["exclusive"] = None; j["gpus_allowed"] = None
j["spec_version_job"] = "v1.25"; j["spec_sha256_job"] = "acd5406d92973592c2b45e7c5f3a484e5e80234ba8d2f4e271b509076c941e64"
j["record_label_job"] = "full release under the post-result timing rule 3.6 (m)"; j["g1_label_job"] = "G1 under post-result rules 3.6 (j), (k), (l), (n)"
j["release_note_job"] = "lead 2026-10-29T16:40:13Z FULL RELEASE (labels at the job level; cfg unchanged except max_iter and the time limit)"
j["lineage_history"] = "P3 (S20_own, all-m class) FREE member: pair segments 1 and 2 (3600 s each, matched with the FIXED-CONTROL member) under the full release of 2026-10-29T16:40:13Z; this segment is a FREE-ONLY continuation (not a pair member; the FIXED-CONTROL member is not continued before the 08:30Z selection), ordered by the lead 2026-10-30T02:11:51Z item 3 as the idle-slot fallback"
j["jc_record"] = "by EVAL after the segment end (validation/jc_eval_state.py v5, V370; 3.6 (o)); cfg unchanged by the worker's continuation rule (a)"
j["note"] = (j.get("note") or "") + "; P3 FREE-only continuation of 3600 s (lead 02:11:51Z item 3); not a pair member (tag outside the pair regex); cfg identical to the previous segment except max_iter and time_limit (worker rule (a)); job-level labels 'full release under the post-result timing rule 3.6 (m)' and 'G1 under post-result rules 3.6 (j), (k), (l), (n)'"
json.dump(j, open(p, "w"), indent=1)
dst = p.replace("/pending/", "/staged/"); shutil.move(p, dst)
print("staged", dst, "job", j["job_id"], "max_iter", c["max_iter"], "time", c["time_limit_per_start"], "target", j.get("target"), "config_sha256", hashlib.sha256(json.dumps(c, sort_keys=True).encode()).hexdigest()[:16])
PYEOF

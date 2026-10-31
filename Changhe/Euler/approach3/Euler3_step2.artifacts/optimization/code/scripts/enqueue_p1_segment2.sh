#!/bin/bash
# Segment 2 of a pair (lead 08:50Z item 4, 08:53Z item 2, 09:02Z item 2, 09:39:59Z item 3): both members enqueued in ONE command from their
# segment-1 run directories, unplaced with target = the segment-1 arrangement (scripts/enqueue_segment2.sh v2), then moved into queue/staged so that the
# slot governor grants the pair as a whole (close, acknowledgment, placement into the files, move into pending, exposure). WORKLOG lines with times.
# Usage: scripts/enqueue_p1_segment2.sh <FREE run dir> <FIXED run dir> <pair tag p1|p2> <gpu> <excl 0|1> [inc=240] [tl=7200]
cd "$(dirname "$0")/.."; RF=$1; RC=$2; P=$3; GPU=$4; EX=$5; INC=${6:-240}; TL=${7:-7200}
[ -f "$RF/checkpoint_segment_end.pt" ] && [ -f "$RC/checkpoint_segment_end.pt" ] || { echo "both segment-1 end checkpoints are needed: $RF $RC"; exit 1; }
START=$(basename "$RF" | sed -E 's/^p[0-9]+_s1_([A-Za-z0-9]+)_.*/\1/')
T0=$(date -u +%FT%TZ)
bash scripts/enqueue_segment2.sh "$RF" ${P}_s2_${START} $GPU $EX $INC $TL || exit 1
bash scripts/enqueue_segment2.sh "$RC" ${P}c_s2_${START} $GPU $EX $INC $TL || exit 1
mkdir -p queue/staged
for f in queue/pending/${P}_s2_${START}_*.json queue/pending/${P}c_s2_${START}_*.json; do mv -v "$f" queue/staged/; done
T1=$(date -u +%FT%TZ)
echo "- $T1: ${P} segment 2 enqueued at $T0 from $RF and $RC (max_iter = end it + $INC, time limit $TL s; target GPU $GPU exclusive $EX = the segment-1 arrangement; unplaced), both files moved to queue/staged at $T1 (one command; the governor grants the pair as a whole)." >> ../WORKLOG.md
ls queue/staged

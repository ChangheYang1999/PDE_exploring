#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# Detached launcher for the g2_v4 evidence chain (lead NOTES 06:45Z item 4: independent steps as separate guarded sessions inside the 12-core allotment).
# Dependencies: t3 reads t26.json (T3.6 (ii) band maxima) and t0t1's seed_check; the supplement reads the replay reference file written by t3.
# Core assignments (lane affinity 78-89): s1 cores 78-81 (t0t1, t26, t3; 4 workers), s2 cores 82-85 (t2, t27h; 4 workers), s3 cores 86-89 (t27hx; 4 workers),
# then s4 cores 78-89 (supplement; 8 workers, its T3.4b configurations go up to 8 workers / 8 threads) after all three have ended.
# Every step is launched by bin/run_g2_steps_v3.sh (fail closed; verdicts bound to the new run dir). Usage: setsid nohup bash bin/launch_g2_v4.sh <tag> > outputs/g2/launch_<tag>.log 2>&1 &
set -u
LANE=$IPM_ARTIFACT_ROOT; TAG=${1:-g2_v4}; POL=$LANE/outputs/g2_policy_v2.json; R=$LANE/bin/run_g2_steps_v3.sh; L=$LANE/outputs/g2
stamp() { date -u +%FT%TZ; }
echo "$(stamp) launcher start tag=$TAG pid=$$ affinity=$(taskset -cp $$ | sed 's/.*: //')"
taskset -c 78-81 bash $R $TAG s1 4 $POL t0t1 t26 t3 > $L/launch_${TAG}_s1.log 2>&1 & P1=$!
taskset -c 82-85 bash $R $TAG s2 4 $POL t2 t27h   > $L/launch_${TAG}_s2.log 2>&1 & P2=$!
taskset -c 86-89 bash $R $TAG s3 4 $POL t27hx     > $L/launch_${TAG}_s3.log 2>&1 & P3=$!
echo "$(stamp) sessions started: s1 pid $P1 (cores 78-81: t0t1 t26 t3), s2 pid $P2 (cores 82-85: t2 t27h), s3 pid $P3 (cores 86-89: t27hx)"
wait $P1; R1=$?; echo "$(stamp) s1 ended exit=$R1"
wait $P2; R2=$?; echo "$(stamp) s2 ended exit=$R2"
wait $P3; R3=$?; echo "$(stamp) s3 ended exit=$R3"
R4=skipped
if [ $R1 = 0 ]; then
  echo "$(stamp) s4 start (cores 78-89, 8 workers): supplement"
  taskset -c 78-89 bash $R $TAG s4 8 $POL supplement > $L/launch_${TAG}_s4.log 2>&1; R4=$?; echo "$(stamp) s4 ended exit=$R4"
else
  echo "$(stamp) s4 (supplement) not started: s1 exit $R1 (the supplement needs the replay reference written by t3)"
fi
echo "$(stamp) launcher end: s1=$R1 s2=$R2 s3=$R3 s4=$R4 (0 = every step of that session succeeded under runner v3)"

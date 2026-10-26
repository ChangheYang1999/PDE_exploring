#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# Resume of the g2_v4 chain after the t3 RSS stop (08:07:48Z): t3 now in a new session (s7, cores 78-81, 4 workers, policy v3), then, after t3 succeeds and
# the other sessions (g2_v4 s2: t27h; g2_v6 s1: t27hx2) have ended, the supplement in session s8 on cores 78-89 with 8 workers. Runner v5 (strict verdict).
set -u
LANE=$IPM_ARTIFACT_ROOT; POL=$LANE/outputs/g2_policy_v3.json; R=$LANE/bin/run_g2_steps_v5.sh; L=$LANE/outputs/g2
stamp() { date -u +%FT%TZ; }
echo "$(stamp) resume launcher start pid $$ affinity $(taskset -cp $$ | sed 's/.*: //')"
taskset -c 78-81 bash $R g2_v4 s7 4 $POL t3 > $L/launch_g2_v4_s7.log 2>&1; R5=$?; echo "$(stamp) s7 (t3) ended exit=$R5"
if [ $R5 != 0 ]; then echo "$(stamp) t3 did not succeed; supplement not started"; exit 1; fi
while pgrep -f "tests/g2_t27h.py|tests/g2_t27hx2.py" > /dev/null; do sleep 30; done
echo "$(stamp) other sessions ended; s6 (supplement) start on cores 78-89, 8 workers"
taskset -c 78-89 bash $R g2_v4 s8 8 $POL supplement > $L/launch_g2_v4_s8.log 2>&1; R6=$?; echo "$(stamp) s8 (supplement) ended exit=$R6"
echo "$(stamp) resume launcher end: s7=$R5 s8=$R6"

#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# G3 bench launch (lead 13:19Z item 4, 15:05Z: ONE step, policy outputs/g3_bench_policy.json, G3_BENCH_WORKERS="4 8 12", session s2, nice 15, detached;
# only after the lead's release on the strict T4 read; never overlapping T4). Usage: bash outputs/g3/tools/launch_bench.sh
LANE=$IPM_ARTIFACT_ROOT; cd $LANE || exit 1
if pgrep -f 'tests/g3_t4|run_g3_steps|bench860' | grep -v $$ > /dev/null; then echo "refuse: a T4/runner/bench process is running"; pgrep -af 'tests/g3_t4|run_g3_steps|bench860' | grep -v pgrep; exit 2; fi
[ -d outputs/g3/session_g3_v1_s2 ] && { echo "refuse: session s2 exists (choose a new suffix)"; exit 3; }
[ -f outputs/g3_bench_policy.json ] || { echo "refuse: policy missing"; exit 4; }
python3 -c "import json; d=json.load(open('outputs/g3_bench_policy.json')); assert d['max_seconds']==36000 and d['max_family_rss_mib']==163840, d" || exit 4
echo "[$(date -u +%FT%TZ)] launching bench: G3_BENCH_WORKERS=\"4 8 12\" setsid nohup nice -n 15 bash bin/run_g3_steps.sh g3_v1 s2 8 $LANE/outputs/g3_bench_policy.json bench"
G3_BENCH_WORKERS="4 8 12" setsid nohup nice -n 15 bash bin/run_g3_steps.sh g3_v1 s2 8 $LANE/outputs/g3_bench_policy.json bench > outputs/g3/launch_g3_v1_bench.log 2>&1 < /dev/null &
sleep 15; cat outputs/g3/launch_g3_v1_bench.log | cut -c1-200
BP=$(pgrep -f 'bench860.py .*bench.json' | head -1)
if [ -n "$BP" ]; then setsid nohup nice -n 19 bash outputs/g3/tools/rss_sampler.sh $BP outputs/g3/g3_v1/bench_parent_rss.jsonl 10 > /dev/null 2>&1 < /dev/null & echo "parent RSS sampler on bench parent $BP -> outputs/g3/g3_v1/bench_parent_rss.jsonl"; else echo "WARNING: bench parent pid not found for the sampler"; fi
ps -o pid,ppid,ni,psr,pcpu,rss,etime,args -p $(pgrep -d, -f 'run_g3_steps|guard.py run|bench860') 2>/dev/null | cut -c1-150

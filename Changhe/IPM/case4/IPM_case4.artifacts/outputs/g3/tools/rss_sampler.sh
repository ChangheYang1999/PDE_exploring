#!/bin/bash
# Lightweight parent/children RSS sampler (lead 13:34Z: report the parent's own RSS beside the guard's family sum). Usage: rss_sampler.sh <pid> <out.jsonl> [interval_s]
# Each line: utc, parent VmRSS MiB, VmHWM MiB (peak), number of live descendants, sum and max of their RSS MiB. Ends when the pid is gone.
PID=$1; OUT=$2; IV=${3:-10}
while kill -0 $PID 2>/dev/null; do
  P=$(awk '/VmRSS/{r=$2}/VmHWM/{h=$2}END{printf "%.1f %.1f", r/1024, h/1024}' /proc/$PID/status 2>/dev/null)
  C=$(ps --ppid $PID -o pid= 2>/dev/null | tr -d ' ')
  D=$(for c in $C; do pgrep -P $c; echo $c; done | sort -u)
  S=$(for d in $D; do awk '/VmRSS/{print $2}' /proc/$d/status 2>/dev/null; done | awk '{s+=$1; if($1>m)m=$1; n++}END{printf "%d %.1f %.1f", n, s/1024, m/1024}')
  echo "{\"utc\": \"$(date -u +%FT%TZ)\", \"pid\": $PID, \"parent_rss_mib\": ${P% *}, \"parent_peak_rss_mib\": ${P#* }, \"descendants\": ${S%% *}, \"descendants_rss_sum_mib\": $(echo $S | awk '{print $2}'), \"descendant_rss_max_mib\": ${S##* }}" >> $OUT
  sleep $IV
done
echo "{\"utc\": \"$(date -u +%FT%TZ)\", \"pid\": $PID, \"ended\": true}" >> $OUT

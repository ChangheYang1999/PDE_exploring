#!/bin/bash
# v5 (01:2xZ; V556): the no-id fallback accepts only an UNAMBIGUOUS new active file (exactly one file of the prefix that did not exist before the enqueue); otherwise the lock is held as unresolved; the worker match uses the admitted-computation predicate of queue_guard_lib v2. v4 (8071c2d9) kept as .v4_8071c2d9.
# Enqueue a job without exceeding four busy computations. v4 (01:1xZ; V547): the exact job id is taken from the enqueue command's own output ("enqueued/staged
# <path>.json"), its state is looked up in EVERY queue directory, the worker is matched by its exact run-directory argv token (no substring), and the lock is held
# until that worker is visible or the job is in a terminal directory (failed, cancelled, done) with no active copy; a job whose file disappears without a terminal
# copy is treated as UNRESOLVED (lock held, warning every 60 s) until it reappears or an operator intervenes; an enqueue that returns no id and leaves no file of the
# prefix in any state releases with "nothing to reserve". v3 (9f72d692) kept as .v3_9f72d692. Lock: validation/.l_launch.lock (shared with the launchers).
# Usage: bash scripts/enqueue_under_lock.sh <job id prefix (tag)> <enqueue command ...>
set -u; cd RUN_ROOT/numerics/degree6_free_parameters_48h; PREFIX=$1; shift; LOCK=validation/.l_launch.lock; . scripts/queue_guard_lib.sh
exec 9>"$LOCK"; flock -x 9
t=0; while [ "$(busy)" -gt 3 ]; do sleep 20; t=$((t+20)); [ $t -ge 7200 ] && { echo "enqueue_under_lock: gave up waiting for a slot after $t s (busy $(busy)); nothing enqueued"; flock -u 9; exit 1; }; done
echo "$(date -u +%FT%TZ) enqueue_under_lock: busy $(busy) <= 3 after $t s; enqueuing: $*"
BEFORE_IDS=$(for d in staged pending granted running failed cancelled done; do for f in queue/$d/${PREFIX}_*.json; do [ -e "$f" ] && basename "$f" .json; done; done)
OUT=$("$@" 2>&1); rc=$?; echo "$OUT"
JID=$(id_from_output "$OUT")
if [ -z "$JID" ]; then
  # v5 (V556): no fallback to an older active file of the same prefix: the admitted id must be unambiguous: exactly ONE active file of the prefix that did not exist before the enqueue
  NEW=""; for d in staged pending granted running; do for f in queue/$d/${PREFIX}_*.json; do [ -e "$f" ] || continue; b=$(basename "$f" .json); echo "$BEFORE_IDS" | grep -qx "$b" || NEW="$NEW $b"; done; done
  NEW=$(echo $NEW | tr ' ' '\n' | sort -u); cnt=$(echo "$NEW" | grep -c . )
  if [ "$cnt" = "1" ]; then JID=$NEW; echo "$(date -u +%FT%TZ) enqueue_under_lock: no id in the output; exactly one new active file $JID (accepted as the admitted id)"
  elif [ "$cnt" = "0" ] && [ $rc -ne 0 ]; then echo "$(date -u +%FT%TZ) enqueue_under_lock: the enqueue failed (exit $rc), printed no id and created no active file: nothing to reserve; lock released"; flock -u 9; exec 9>&-; exit $rc
  else echo "$(date -u +%FT%TZ) enqueue_under_lock: WARNING ambiguous admission (enqueue exit $rc; new active files: $(echo $NEW)); the lock is HELD until an operator resolves it (stop this guard after cancelling or identifying the job)"; while true; do sleep 60; echo "$(date -u +%FT%TZ) enqueue_under_lock: WARNING unresolved admission for prefix ${PREFIX}; lock held"; done; fi
fi
echo "$(date -u +%FT%TZ) enqueue_under_lock: admitted job $JID (enqueue exit $rc); holding the lock until its worker is visible (states now:$(job_states $JID))"
t=0; state="pending"
while true; do
  st=$(job_states $JID)
  if worker_visible "$JID"; then state="visible"; break; fi
  case "$st" in *failed*|*cancelled*|*done*) case "$st" in *staged*|*pending*|*granted*|*running*) ;; *) state="terminal_without_worker:$st"; break;; esac;; esac
  [ -z "$st" ] && [ $((t % 60)) -eq 0 ] && echo "$(date -u +%FT%TZ) enqueue_under_lock: WARNING $JID has no file in any queue state (transient or lost); lock held"
  sleep 5; t=$((t+5)); [ $t -ge 900 ] && [ $((t % 60)) -eq 0 ] && echo "$(date -u +%FT%TZ) enqueue_under_lock: WARNING $JID not acknowledged after $t s (states:$st); lock still held"
done
echo "$(date -u +%FT%TZ) enqueue_under_lock: $JID state ${state} after $t s (busy $(busy)); lock released"
flock -u 9; exec 9>&-; exit $rc

#!/bin/bash
# Move every PENDING exclusive job file to queue/hold so that the supervisor cannot place an exclusive job on a GPU that is about to host a
# heavy ad hoc evaluation (the supervisor does not check GPU memory; it reads queue/pending at every poll). Reversible: scripts/release_hold.sh.
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT; mkdir -p queue/hold
n=0
for f in queue/pending/*.json; do
  [ -e "$f" ] || continue
  if .venv/bin/python -c "import json,sys; d=json.load(open('$f')); sys.exit(0 if d.get('exclusive') else 1)"; then mv "$f" queue/hold/; n=$((n+1)); fi
done
echo "$(date -u +%FT%TZ) held $n exclusive pending jobs in queue/hold" | tee -a status/hold.log

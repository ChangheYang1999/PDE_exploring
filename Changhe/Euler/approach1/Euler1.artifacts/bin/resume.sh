#!/bin/bash
# RESUME after any interruption: clears STOP and starts the runner, which requeues interrupted experiments;
# each worker resumes from its last atomic checkpoint (model, optimizer, scalars, RNG, sampler state).
P=$(cd "$(dirname "$0")/.." && pwd)
rm -f "$P/STOP"
for f in "$P"/queue/stopped/*.json; do [ -e "$f" ] && { id=$(basename "$f" .json); [ -e "$P/runs/$id/STOP" ] && { echo "keeping held $id"; continue; }; mv "$f" "$P/queue/pending/"; }; done
exec "$P/bin/launch.sh"

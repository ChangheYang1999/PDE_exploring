#!/bin/bash
# Hold (pause and park) one experiment: its worker checkpoints and exits; the entry goes to queue/stopped/.
P=$(cd "$(dirname "$0")/.." && pwd); for id in "$@"; do mkdir -p "$P/runs/$id"; touch "$P/runs/$id/STOP"; echo "hold $id"; done

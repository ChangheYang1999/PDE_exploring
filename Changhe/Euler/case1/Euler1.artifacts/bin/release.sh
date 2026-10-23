#!/bin/bash
# Release held experiments back to the pending queue (they resume from their last checkpoint).
P=$(cd "$(dirname "$0")/.." && pwd); for id in "$@"; do rm -f "$P/runs/$id/STOP"; [ -f "$P/queue/stopped/$id.json" ] && mv "$P/queue/stopped/$id.json" "$P/queue/pending/"; echo "released $id"; done

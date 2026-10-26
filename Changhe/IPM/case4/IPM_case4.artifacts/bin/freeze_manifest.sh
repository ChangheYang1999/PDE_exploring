#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# Record a frozen-code manifest before a gate run. Usage: freeze_manifest.sh <tag>
# Hashes: work/research860/**, bin/*, outputs/dev_policy.json, outputs/manifests/environment.json, and the frozen 181D
# closure (every file named in work/research/campaign/global181_v3/state.json source_sha256, recomputed).
set -eu
LANE=$IPM_ARTIFACT_ROOT; TAG=$1; OUT=$LANE/outputs/manifests/code_manifest_$TAG.json
[ -e "$OUT" ] && { echo "manifest $OUT exists; choose a new tag"; exit 1; }
cd $LANE
{
  echo "{"; echo "\"tag\": \"$TAG\", \"utc\": \"$(date -u +%FT%TZ)\", \"lane\": \"$LANE\","
  echo "\"files\": ["
  first=1
  for f in $(find work/research860 bin outputs/dev_policy.json outputs/manifests/environment.json -type f ! -name '*.pyc' 2>/dev/null | sort); do
    h=$(sha256sum "$f" | cut -d' ' -f1); b=$(stat -c %s "$f")
    [ $first = 1 ] || echo ","; first=0
    printf '  {"path": "%s", "bytes": %s, "sha256": "%s"}' "$f" "$b" "$h"
  done
  echo; echo "],"
  echo "\"frozen_181_closure\": ["
  first=1
  for f in $(python3 -c "import json;print('\n'.join(sorted(json.load(open('work/research/campaign/global181_v3/state.json'))['source_sha256'])))"); do
    h=$(sha256sum "work/research/$f" | cut -d' ' -f1)
    [ $first = 1 ] || echo ","; first=0
    printf '  {"path": "work/research/%s", "sha256": "%s"}' "$f" "$h"
  done
  echo; echo "],"
  echo "\"accepted278_sha256\": \"$(sha256sum work/research/campaign/global181_v3/snapshots/accepted_00000278.json | cut -d' ' -f1)\""
  echo "}"
} > "$OUT.partial" && mv "$OUT.partial" "$OUT"
echo "manifest: $OUT sha256 $(sha256sum "$OUT" | cut -d' ' -f1)"

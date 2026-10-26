#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# Frozen-code manifest, version 3 (new file): version 2 plus the guard and runtime files the campaign imports or runs under (lead G3 request:
# work/tools/runtime.py, work/research/hardware/guard.py, policy.py, worker_bootstrap.py) and the campaign policies/kappa file.
# Version 2 text: also hashes the loaded handoff files outside the state.json closure (base/basis_tests.py,
# base/engine/ipm_portable.py, base/engine/taylor_jet.py, base/spectral_basis.py), the pending-edit copies and the policies.
# Usage: freeze_manifest_v3.sh <tag> [base-tag]   (base-tag: a previous manifest this one supplements)
set -eu
LANE=$IPM_ARTIFACT_ROOT; TAG=$1; BASE=${2:-}; OUT=$LANE/outputs/manifests/code_manifest_$TAG.json
[ -e "$OUT" ] && { echo "manifest $OUT exists; choose a new tag"; exit 1; }
cd $LANE
{
  echo "{"; echo "\"tag\": \"$TAG\", \"utc\": \"$(date -u +%FT%TZ)\", \"lane\": \"$LANE\", \"base_manifest_tag\": \"$BASE\","
  [ -n "$BASE" ] && echo "\"base_manifest_sha256\": \"$(sha256sum outputs/manifests/code_manifest_$BASE.json | cut -d' ' -f1)\","
  echo "\"files\": ["
  first=1
  for f in $(find work/research860 bin work/tools/runtime.py work/research/hardware/guard.py work/research/hardware/policy.py work/research/hardware/worker_bootstrap.py work/research/farfield_asymptotic_audit_20261022_0836/coefficients_audit.py outputs/dev_policy.json outputs/g2_policy.json outputs/g2_policy_v2.json outputs/manifests/environment.json outputs/g2/pending_edits outputs/g2/post_chain_edits.md outputs/campaign860/campaign_policy.json outputs/campaign860/campaign_policy_v2.json outputs/campaign860/kappa_calibration.json outputs/campaign860/kappa_calibration_typed.json -type f ! -name '*.pyc' 2>/dev/null | sort); do
    h=$(sha256sum "$f" | cut -d' ' -f1); b=$(stat -c %s "$f"); [ $first = 1 ] || echo ","; first=0
    printf '  {"path": "%s", "bytes": %s, "sha256": "%s"}' "$f" "$b" "$h"
  done
  echo; echo "],"
  echo "\"frozen_181_closure\": ["
  first=1
  for f in $(python3 -c "import json;print('\n'.join(sorted(json.load(open('work/research/campaign/global181_v3/state.json'))['source_sha256'])))") base/basis_tests.py base/engine/ipm_portable.py base/engine/taylor_jet.py base/spectral_basis.py base/stage12_common.py base/stage12_chart.py base/c5_chart.py; do
    [ -f "work/research/$f" ] || continue
    h=$(sha256sum "work/research/$f" | cut -d' ' -f1); [ $first = 1 ] || echo ","; first=0
    printf '  {"path": "work/research/%s", "sha256": "%s"}' "$f" "$h"
  done
  echo; echo "],"
  echo "\"accepted278_sha256\": \"$(sha256sum work/research/campaign/global181_v3/snapshots/accepted_00000278.json | cut -d' ' -f1)\","
  echo "\"sealed_seed_json_sha256\": \"$(sha256sum outputs/campaign860/seed/seed_860.json | cut -d' ' -f1)\""
  echo "}"
} > "$OUT.partial" && mv "$OUT.partial" "$OUT"
echo "manifest: $OUT sha256 $(sha256sum "$OUT" | cut -d' ' -f1)"

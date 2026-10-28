#!/bin/bash
# make_artifacts_v2.sh (2026-10-27, shift 14): make_artifacts.sh plus the section 8 test records (validation and resume test) under artifacts/section8/.
# Identical to scripts/make_artifacts.sh except the two 'section8' lines marked below; the v1 file is unchanged. Run only after the lead's dated word.
set -e
ROOT=$(cd "$(dirname "$0")/.." && pwd); A=$ROOT/../artifacts
bash $ROOT/scripts/make_artifacts.sh
mkdir -p $A/section8/validation $A/section8/resume_test                                                                # section8 (v2)
cp $ROOT/runs/section8_validation/RECORD.md $ROOT/runs/section8_validation/MODULE_HASHES.sha256 $ROOT/runs/section8_validation/IMPORTED_LANE_MODULES.txt $ROOT/runs/section8_validation/PREFLIGHT.txt $ROOT/runs/section8_validation/compare_vt_nest10_v2.py $ROOT/runs/section8_validation/vt_nest10_full/*.md $ROOT/runs/section8_validation/vt_nest10_full/*.json $ROOT/runs/section8_validation/vt_nest10_full/*.sha256 $ROOT/runs/section8_validation/vt_nest10_full/*.txt $ROOT/runs/section8_validation/vt_nest10_full/stdout.log $A/section8/validation/ 2>/dev/null || true   # section8 (v2)
cp $ROOT/runs/resume_test_rs_record_20261027/* $A/section8/resume_test/ 2>/dev/null || true                            # section8 (v2)
(cd $A && find . -type f ! -name MANIFEST.sha256 -print0 | sort -z | xargs -0 sha256sum > MANIFEST.sha256)
du -sh $A | cut -f1; echo "artifacts (v2, with section8) written $(date -u +%Y-%m-%dT%H:%M:%SZ)"

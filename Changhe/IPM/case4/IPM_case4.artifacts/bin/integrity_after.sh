#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# Read-only protected-tree comparison (the shift 1 commands): sha256 of every file and stat of every entry of the handoff
# repository, plus sha256 of the two other case4 files; compared byte for byte with the before-records. Writes only under
# the lane's outputs/integrity/. Usage: bin/integrity_after.sh
set -u
LANE=$IPM_ARTIFACT_ROOT
SRC=${IPM_SOURCE_REALPATH:?set IPM_SOURCE_REALPATH to the protected handoff}
CASE4=$(dirname -- "${IPM_SOURCE_REALPATH:?set IPM_SOURCE_REALPATH to the protected handoff}")
OUT=$LANE/outputs/integrity
TS=$(date -u +%Y%m%dT%H%M%SZ)
(cd $SRC && find . -type f | sort | xargs -d '\n' sha256sum) > $OUT/source_after_$TS.sha256
(cd $SRC && find . | sort | xargs -d '\n' stat -c "%n %s %Y %A") > $OUT/source_after_$TS.stat
(cd $CASE4 && sha256sum IPM_case4.prompt.md .DS_Store) > $OUT/case4_other_after_$TS.sha256
R=IDENTICAL
cmp -s $OUT/source_before.sha256 $OUT/source_after_$TS.sha256 || R=DIFFERENT
cmp -s $OUT/source_before.stat $OUT/source_after_$TS.stat || R=DIFFERENT
cmp -s $OUT/case4_other_before.sha256 $OUT/case4_other_after_$TS.sha256 || R=DIFFERENT
echo "$TS protected tree vs before-records: $R ($(wc -l < $OUT/source_after_$TS.sha256) files, $(wc -l < $OUT/source_after_$TS.stat) entries; sha256 $(sha256sum $OUT/source_after_$TS.sha256 | cut -c1-16) / $(sha256sum $OUT/source_after_$TS.stat | cut -c1-16) / $(sha256sum $OUT/case4_other_after_$TS.sha256 | cut -c1-16))"
[ $R = IDENTICAL ] || { echo "DIFFERENCES:"; diff $OUT/source_before.sha256 $OUT/source_after_$TS.sha256 | head -20; diff $OUT/source_before.stat $OUT/source_after_$TS.stat | head -20; diff $OUT/case4_other_before.sha256 $OUT/case4_other_after_$TS.sha256; }
grep -q "812d34466c078e2ce643c49671299f4359f764fe2e1d925426762ba962d6e955  ./research/campaign/global181_v3/snapshots/accepted_00000278.json" $OUT/source_after_$TS.sha256 && echo "accepted278 sha256 unchanged" || echo "accepted278 line NOT found as expected"

#!/bin/bash
# make_artifacts_v4.sh (2026-10-27, numerics shift 15; v3 b6a8cd0b with one wording change asked by lead d128 RC: "of the 89 rows"): make_artifacts.sh (v1, unchanged) plus the section 8 test records under artifacts/section8/.
# Written for lead d128 QX item 8 (a) to (e). v2 (scripts/make_artifacts_v2.sh, 906e2ac9) is left unchanged and does not run.
# Run only after the lead's dated word, CPU only, before 2026-10-28T06:00:00Z.
# (a) no '2>/dev/null || true' on the section8 lines: with set -e a missing file stops the script;
# (b) the files are listed explicitly (VAL_FILES, RES_FILES);
# (c) artifacts/section8 is removed before the copy (it holds generated copies only);
# (d) after the copy, section8/COPY_CHECK.sha256 compares each copy's sha256 with its source; any mismatch exits 3;
# (e) one README line for section8 with the scope wording of the lead's VT review (QY, 2026-10-27T19:17:17Z).
set -e
ROOT=$(cd "$(dirname "$0")/.." && pwd); A=$ROOT/../artifacts
bash $ROOT/scripts/make_artifacts.sh
rm -rf $A/section8                                                                                                    # (c)
mkdir -p $A/section8/validation $A/section8/resume_test
V=$ROOT/runs/section8_validation
VAL_FILES="$V/RECORD.md $V/RECORD_CORRECTIONS_20261027.md $V/MODULE_HASHES.sha256 $V/IMPORTED_LANE_MODULES.txt $V/IMPORTED_LANE_MODULES_dynamic.txt $V/import_closure_stderr.txt $V/PREFLIGHT.txt $V/PREP_STAMP $V/compare_vt_nest10.py $V/compare_vt_nest10_v1_to_v2.diff $V/compare_vt_nest10_v2.py $V/vt_nest10_full/LAUNCH.txt $V/vt_nest10_full/stdout.log $V/vt_nest10_full/validate_full_nest10.json $V/vt_nest10_full/VT5_inputs.sha256 $V/vt_nest10_full/VT5_run.txt $V/vt_nest10_full/VT5_compare_v2.md $V/vt_nest10_full/VT5_compare_v2.json"   # (b)
R=$ROOT/runs/resume_test_rs_record_20261027
RES_FILES="$R/RECORD.md $R/LEDGER_ROWS_ADDED.jsonl $R/RESULT_FILES.sha256 $R/resume_test_preflight.txt $R/resume_test_rs_20261027T174857Z.log"   # (b)
for f in $VAL_FILES; do cp "$f" $A/section8/validation/; done                                                         # (a)
for f in $RES_FILES; do cp "$f" $A/section8/resume_test/; done                                                        # (a)
CHK=$A/section8/COPY_CHECK.sha256; : > $CHK; BAD=0                                                                    # (d)
for f in $VAL_FILES; do s=$(sha256sum "$f" | cut -d' ' -f1); c=$(sha256sum $A/section8/validation/$(basename "$f") | cut -d' ' -f1); if [ "$s" = "$c" ]; then v=MATCH; else v=MISMATCH; BAD=1; fi; echo "$v source $s copy $c section8/validation/$(basename "$f") <- runs/section8_validation/${f#$V/}" >> $CHK; done
for f in $RES_FILES; do s=$(sha256sum "$f" | cut -d' ' -f1); c=$(sha256sum $A/section8/resume_test/$(basename "$f") | cut -d' ' -f1); if [ "$s" = "$c" ]; then v=MATCH; else v=MISMATCH; BAD=1; fi; echo "$v source $s copy $c section8/resume_test/$(basename "$f") <- runs/resume_test_rs_record_20261027/$(basename "$f")" >> $CHK; done
echo "copy check written $(date -u +%Y-%m-%dT%H:%M:%SZ): $(grep -c '^MATCH' $CHK) MATCH, $(grep -c '^MISMATCH' $CHK) MISMATCH" >> $CHK
if [ "$BAD" != 0 ]; then echo "COPY MISMATCH, see $CHK"; exit 3; fi
cat >> $A/README.md <<EOR
- section8/: the section 8 test records. validation/: the single-command validation of the saved nest10 state (c_l 0.45, omega 1, omega/c_l 20/9, R_0 = 0.3), ACCEPTED by the lead (d128 QY, 2026-10-27T19:17:17Z) as a reproduction of the saved nest10 diagnostics from a clean process: the command released as VT-1 ran once on GPU 0 with unchanged code and no training, 2026-10-27 16:45:11Z to 18:42:07Z (7016 s), exit 0; of the 89 rows 81 agree within 1e-6 relative (57 identical, 21 to rounding, 3 close; they include the holdout rho_u^max 0.04195 and 0.04145), 7 differ (rho_u_bal on both grids by about 5 per cent, cause OPEN and not cited; three Gram shell lists with 21 against 23 shells; two rounding-floor closure quantities) and 1 is definitional; the VT's new sections are unreviewed numbers and are not cited; this is not new evidence about the state, whose label stays C provisional; RECORD_CORRECTIONS_20261027.md lists the lead's corrections VC1 to VC13 to RECORD.md. resume_test/: the interruption-and-resume test of the deployed worker v2.4 on a disposable job (lead QP, a software resume test only). COPY_CHECK.sha256: each copy's sha256 against its source.
EOR
(cd $A && find . -type f ! -name MANIFEST.sha256 -print0 | sort -z | xargs -0 sha256sum > MANIFEST.sha256)
du -sh $A | cut -f1; echo "artifacts (v4, with section8) written $(date -u +%Y-%m-%dT%H:%M:%SZ)"

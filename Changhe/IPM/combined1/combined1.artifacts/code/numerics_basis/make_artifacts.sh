#!/bin/bash
# Package the code, scripts and small data that reproduce every number reported by lane c1-n1 into artifacts/ (under 20 MB).
# Exact coefficient files (*_exact.json, 81 MB in total) are NOT copied: every snapshotted candidate's exact JSON is immutable in
# candidates/<ID>/ (sha256 in each SHA256SUMS); unsnapshotted trial files stay in numerics/optimization/candD2/.
set -e
L=RUN_ROOT/numerics_N1N2; A=$L/artifacts; cd $L
rm -rf $A/code $A/data; mkdir -p $A/code/lib $A/code/optimization $A/code/far_field $A/data/candD2 $A/data/heldout $A/data/far_field $A/data/reports
cp numerics/lib/*.py $A/code/lib/
cp numerics/optimization/*.py numerics/optimization/*.sh $A/code/optimization/ 2>/dev/null || true
cp numerics/far_field/*.py $A/code/far_field/ 2>/dev/null || true
cp numerics/check_ids.py numerics/check_certified.py $A/code/
cp numerics/optimization/heldout/*.md $A/data/heldout/
# small results: weak tests, diagnostics, per-step logs, sector tables, cell proxies (each under 3 MB)
for f in numerics/optimization/candD2/*_weaktests3.json numerics/optimization/candD2/*_weaktests2.json numerics/optimization/candD2/*_diag2.json \
         numerics/optimization/candD2/*_weaktests.json numerics/optimization/candD2/*_na_cells.json numerics/optimization/candD2/*_sectors.json \
         numerics/optimization/candD2/*_weaktests3c_n47.json numerics/optimization/candD2/*.log numerics/optimization/candD2/table_v11.md; do
  [ -f "$f" ] && [ $(stat -c %s "$f") -lt 3000000 ] && cp "$f" $A/data/candD2/; done
for f in numerics/far_field/*.json; do [ -f "$f" ] && [ $(stat -c %s "$f") -lt 3000000 ] && cp "$f" $A/data/far_field/; done
cp numerics/perprobe_*.txt numerics/perprobe_*.md numerics/v1*_status.md numerics/status026.txt numerics/v12_nacells.md $A/data/reports/ 2>/dev/null || true
cp numerics/NUMERICS_v*_published.md $A/data/reports/ 2>/dev/null || true
cp NUMERICS_FINAL.md $A/data/reports/NUMERICS_FINAL_copy.md
# run logs of the GPU phase (optimizer FINAL lines, step records)
mkdir -p $A/data/logs; for f in numerics/optimization/logs/*.out; do [ $(stat -c %s "$f") -lt 2000000 ] && cp "$f" $A/data/logs/; done
cd $A && find code data -type f | sort | xargs sha256sum > SHA256SUMS
du -sh $A; find $A -type f | wc -l

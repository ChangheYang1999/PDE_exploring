#!/bin/bash
# Assemble the c1-n3 artifacts folder: code, queue files, small result records (no caches, no polynomial records). Run from the lane root.
LANE=RUN_ROOT/numerics_N3; cd $LANE
A=artifacts
rm -rf $A/results $A/logs; mkdir -p $A/code $A/results $A/logs
cp certification/*.py certification/*.sh certification/jobs_core5*.txt $A/code/ 2>/dev/null
for f in certification/results/*.json; do
  case "$f" in *Fpoly*|*polynomials*|*_cache*) continue;; esac
  [ $(stat -c %s "$f") -lt 10000000 ] && cp "$f" $A/results/
done
# compact summaries of the large Hdot^-1 records (per-mode bounds and totals only)
for f in certification/results/*_hminus1.json; do
  python3 - "$f" "$A/results/$(basename ${f%.json})_summary.json" <<'PYEOF'
import json, sys
d = json.load(open(sys.argv[1]))
keep = {k: d.get(k) for k in ('name', 'canonical_sha256', 'source_sha256', 'input_sha256', 'kmax', 'small', 'max_mode', 'method', 'H_lower', 'H_upper', 'fixes', 'reruns', 'code_sha256', 'utc', 'elapsed_seconds') if k in d}
keep['tail'] = {k: v for k, v in (d.get('tail') or {}).items() if k != 'modes'} | {'n_modes': len((d.get('tail') or {}).get('modes', []))}
keep['rows'] = [{k: r.get(k) for k in ('n', 'status', 'mode_norm_LB', 'mode_norm_UB', 'mode_norm_UB_galerkin', 'hardy_direct_UB', 'mode_n_hardy_UB', 'ub_source', 'basis_size', 'classes', 'elapsed') if k in r} for r in d.get('rows', [])]
json.dump(keep, open(sys.argv[2], 'w'), indent=1)
PYEOF
done
rm -f $A/results/*_hminus1.json
# compact the exact-rational records: strings longer than 2000 characters (10^4-digit rationals) are replaced in the ARTIFACT COPY by
# {"sha256": ..., "chars": n}; the lane's certification/results keeps the full records and the code regenerates every value.
for f in $A/results/*.json; do
  case "$f" in *_hdual*) continue;; esac   # the duality / residual records keep their full replay certificates (exact rationals)
  [ $(stat -c %s "$f") -gt 300000 ] && python3 - "$f" <<'PYEOF2'
import json, sys, hashlib
def compact(x):
    if isinstance(x, dict): return {k: compact(v) for k, v in x.items()}
    if isinstance(x, list): return [compact(v) for v in x]
    if isinstance(x, str) and len(x) > LIM: return {'sha256': hashlib.sha256(x.encode()).hexdigest(), 'chars': len(x), 'head': x[:40], 'note': 'long string elided in the artifact copy; full value in the lane record'}
    return x
import os
p = sys.argv[1]; LIM = 2000 if os.path.getsize(p) < 1500000 else 120   # very large records: keep only the first 40 characters of long ball strings
d = json.load(open(p)); d['_artifact_note'] = f'compacted copy: strings over {LIM} characters replaced by sha256 markers with a 40-character head'
json.dump(compact(d), open(p, 'w'), indent=1)
PYEOF2
done
# compress what is still large so that the folder stays under 20 MB
for f in $A/results/*.json; do [ $(stat -c %s "$f") -gt 1000000 ] && gzip -f "$f"; done
cp certification/results/*.log $A/logs/ 2>/dev/null
cp logs/*.out $A/logs/ 2>/dev/null
cp NOTES_FOR_TEAM.md WORKLOG.md RUN_STATUS.md $A/ 2>/dev/null
mkdir -p $A/notes $A/astra $A/t4_probes; cp notes/*.md $A/notes/; cp source_copy/t4_probes/*.json $A/t4_probes/
for d in astra/*/; do [ -f $d/answer.md ] && { mkdir -p $A/$d; cp $d/answer.md $d/question.md $A/$d/ 2>/dev/null; }; done
( cd $A && find . -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS )
du -sh $A

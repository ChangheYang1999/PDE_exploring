"""Check complete, nonoverlapping independent compact-region replay."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
import hashlib,json
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'09_uniform_comparison/lead_certificate'
OUT=BASE/'verification/recomputed'
ctx.prec=256

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    source=ROOT/'code/reproduce_uniform_upper_chunks.py'
    expected={name:sha(BASE/'data'/name) for name in ['upper_n384.json','upper_n384_b.json']}
    files=sorted(OUT.glob('upper_r*_*.json'),key=lambda p:json.loads(p.read_text())['row_start'])
    original={}
    for name in expected:
        d=json.loads((BASE/'data'/name).read_text())
        for row in d['rows']:
            a=Fraction(row['alpha']);assert a not in original;original[a]=row
    alphas=sorted(original);sums={a:[arb(0) for _ in range(17)] for a in alphas};coverage=[];hashes={}
    for p in files:
        d=json.loads(p.read_text());assert d['source_sha256']==sha(source)
        assert d['input_sha256']==expected
        assert d['cells_per_axis']==384 and d['phase_intervals']==16
        assert [Fraction(r['alpha']) for r in d['rows']]==alphas
        coverage.extend(range(d['row_start'],d['row_stop']));hashes[str(p.relative_to(ROOT))]=sha(p)
        for row in d['rows']:
            a=Fraction(row['alpha']);assert len(row['regular_grid_endpoints'])==17
            for j,(lo,hi) in enumerate(row['regular_grid_endpoints']):
                lower,upper=arb(lo),arb(hi);assert lower<=upper
                sums[a][j]+=lower.union(upper)
    assert coverage==list(range(384)),f'incomplete or duplicate coverage: {len(coverage)} rows, ends {coverage[-1:]}'
    records=[];failures=[]
    for a in alphas:
        for j,value in enumerate(sums[a]):
            old=arb(original[a]['regular_grid'][j])
            contained=bool(old.contains(value));overlap=bool(old.overlaps(value))
            rec=dict(alpha=str(a),phase=j,original=original[a]['regular_grid'][j],new_lower=value.lower().str(70,more=True),new_upper=value.upper().str(70,more=True),original_contains_replay=contained,overlap=overlap)
            records.append(rec)
            if not contained:failures.append(rec)
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),rows_recomputed=384,exponents=len(alphas),phase_records=len(records),all_original_contain_replay=not failures,failures=failures,records=records,source_sha256=sha(source),input_sha256=expected,chunk_sha256=hashes,comparison_sha256=sha(Path(__file__)))
    (OUT/'all_upper_comparison.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['records','failures','chunk_sha256']},indent=2))
    print('Failed containments:',len(failures))
    assert not failures
if __name__=='__main__':main()

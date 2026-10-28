"""Independent endpoint recombination of the local-circle C certificate."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,hashlib
import mpmath as mp
from flint import arb,ctx
ctx.prec=256;mp.mp.dps=90
ROOT=Path(__file__).resolve().parents[1]
def endpoint(text):
    q=arb(text).upper().fmpq()
    return mp.mpf(str(q.numerator))/mp.mpf(str(q.denominator))
def main():
    finalname='data/local_circle_composite_a50.json'
    final=json.loads((ROOT/finalname).read_text());m=final['phase_intervals']
    chunks=[p for p in final['input_hashes'] if p.startswith('data/local_circle_chunks/')]
    for name,digest in final['input_hashes'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
    counts=[[0]*(m+1) for _ in range(final['radial_cells'])];local=[mp.mpf(0) for _ in range(m+1)]
    for name in chunks:
        c=json.loads((ROOT/name).read_text())
        for i in range(c['row_start'],c['row_stop']):
            for j in range(c['phase_start'],c['phase_stop']):counts[i][j]+=1
        for j,value in c['partial_phase_intervals'].items():local[int(j)]+=endpoint(value)
    assert all(v==1 for row in counts for v in row)
    row=final['rows'][0];alpha=mp.mpf(1)/2;delta=mp.mpf(1)/64
    middle=json.loads((ROOT/'data/middle_circle_certificate_n512.json').read_text())
    exterior=json.loads((ROOT/'data/far_circle_certificate_fine.json').read_text())
    mr=next(x for x in middle['rows'] if Fraction(x['alpha'])==Fraction(1,2))
    er=next(x for x in exterior['rows'] if Fraction(x['alpha'])==Fraction(1,2))
    vals=[local[j]+endpoint(mr['middle_phase_intervals'][j])+endpoint(er['far_phase_intervals'][j]) for j in range(m+1)]
    a2=mp.power(2,1+alpha/2)/(mp.pi*(alpha+2))
    small=2*a2*delta**alpha/alpha+(1+2*delta)**alpha*delta**2/(2*(1-delta)**2)
    value=small+max(vals)/mp.cos(mp.pi/(4*m))
    assert value<mp.mpf(row['safe_upper_C'])
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_decimal_digits=90,independent_upper=mp.nstr(value,80),small_disks=mp.nstr(small,70),maximizing_phase_index=max(range(m+1),key=lambda j:vals[j]),safe_upper_C=row['safe_upper_C'],status='Independent endpoint recomputation and exact coverage check passed',input_hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in [finalname,'code/check_local_composite.py']})
    (ROOT/'data/local_circle_composite_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

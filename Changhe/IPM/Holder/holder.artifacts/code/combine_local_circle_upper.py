"""Exact coverage merger and composite C upper bound for paired local circles."""
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
from fractions import Fraction
from certify_far_circles import upper_decimal
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[1];ctx.prec=192

def main():
    p=argparse.ArgumentParser();p.add_argument('--chunks',nargs='+',required=True);p.add_argument('--out',required=True);args=p.parse_args()
    chunks=[json.loads((ROOT/x).read_text()) for x in args.chunks];first=chunks[0]
    keys=['alpha','precision_bits','angles_per_circle','radial_cells','phase_intervals','delta','integer_unit','source_hashes']
    for c in chunks:
        for k in keys:assert c[k]==first[k],(k,c[k],first[k])
    for source,h in first['source_hashes'].items():assert hashlib.sha256((ROOT/source).read_bytes()).hexdigest()==h
    nr=first['radial_cells'];m=first['phase_intervals'];coverage=[[0]*(m+1) for _ in range(nr)];totals=[arb(0) for _ in range(m+1)]
    for c in chunks:
        assert set(map(int,c['partial_phase_intervals']))==set(range(c['phase_start'],c['phase_stop']))
        for row in range(c['row_start'],c['row_stop']):
            for j in range(c['phase_start'],c['phase_stop']):coverage[row][j]+=1
        for j,s in c['partial_phase_intervals'].items():totals[int(j)]+=arb(s)
    assert all(v==1 for row in coverage for v in row)
    alpha=arb(first['alpha']);delta=arb(first['delta']);a2=2**(1+alpha/2)/(arb.pi()*(alpha+2))
    small=2*a2*delta**alpha/alpha+(1+2*delta)**alpha*delta**2/(2*(1-delta)**2)
    for c in chunks:assert small.overlaps(arb(c['small_disk_upper']))
    midname='data/middle_circle_certificate_n512.json';farname='data/far_circle_certificate_fine.json'
    mid=json.loads((ROOT/midname).read_text());far=json.loads((ROOT/farname).read_text())
    assert mid['phase_intervals']==far['phase_intervals']==m
    mr=next(r for r in mid['rows'] if Fraction(r['alpha'])==Fraction(first['alpha']))
    fr=next(r for r in far['rows'] if Fraction(r['alpha'])==Fraction(first['alpha']))
    values=[a+arb(b)+arb(c) for a,b,c in zip(totals,mr['middle_phase_intervals'],fr['far_phase_intervals'])]
    assert len(values)==m+1
    mx=values[0]
    for v in values[1:]:mx=arb.max(mx,v)
    upper=small+mx/(arb.pi()/(4*m)).cos()
    row=dict(alpha=first['alpha'],local_phase_intervals=[v.str(45,more=True) for v in totals],middle_plus_local_plus_far=[v.str(45,more=True) for v in values],small_disk_upper=small.str(45,more=True),upper_C=upper.str(45,more=True),safe_upper_C=upper_decimal(upper))
    paths=args.chunks+[midname,farname,'code/combine_local_circle_upper.py']
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,phase_intervals=m,angles_per_circle=first['angles_per_circle'],radial_cells=nr,delta=first['delta'],rows=[row],input_hashes={x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in paths},status='Paired local, middle and exterior circle C upper bound; requires independent audit verdict')
    (ROOT/args.out).write_text(json.dumps(out,indent=2)+'\n');print(row['alpha'],row['safe_upper_C'])
if __name__=='__main__':main()

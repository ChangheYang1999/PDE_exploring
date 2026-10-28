"""Check exact grid coverage and merge interval integrals from row chunks."""
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
import argparse,json,hashlib
ctx.prec=192
ROOT=Path(__file__).resolve().parents[1]
def main():
    p=argparse.ArgumentParser();p.add_argument('chunks',nargs='+');p.add_argument('--out',required=True);a=p.parse_args()
    objects=[json.loads((ROOT/path).read_text()) for path in a.chunks]
    objects.sort(key=lambda z:z['row_start']);first=objects[0]
    n=first['cells_per_axis'];m=first['phase_intervals'];index=0
    for obj in objects:
        for key in ['cells_per_axis','phase_intervals','precision_bits','source_sha256','input_sha256']:
            assert obj[key]==first[key],key
        assert obj['row_start']==index
        index=obj['row_stop']
        assert [r['alpha'] for r in obj['rows']]==[r['alpha'] for r in first['rows']]
        assert all(len(r['regular_grid'])==m+1 for r in obj['rows'])
    assert index==n
    base=json.loads((ROOT/'data/explicit_bounds_intervals.json').read_text())['rows']
    assert hashlib.sha256((ROOT/'data/explicit_bounds_intervals.json').read_bytes()).hexdigest()==first['input_sha256']
    rows=[]
    for k,r in enumerate(first['rows']):
        values=[sum((arb(obj['rows'][k]['regular_grid'][j]) for obj in objects),arb(0)) for j in range(m+1)]
        alpha=arb(r['alpha']);assert r['alpha']==base[k]['alpha']
        a2=arb(base[k]['intervals']['a2']);near=2*a2*arb(2)**(-alpha)/alpha
        rows.append(dict(alpha=r['alpha'],regular_grid=[v.str(40,more=True) for v in values],near=near.str(40,more=True)))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,cells_per_axis=n,phase_intervals=m,version=2,
             rows=rows,method='Exact partition into row chunks of corrected reflection quadrature',
             input_sha256={path:hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in a.chunks},
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             status='Full regular integrals, with exact grid coverage verified. Add exterior and near contributions for an operator upper bound.')
    (ROOT/a.out).write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()

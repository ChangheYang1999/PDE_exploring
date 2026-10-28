"""Check complete partition coverage and combine positive layer-cake certificates."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import argparse,hashlib,json
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'11_lattice_pole_constraints/axis_clamped_layercake/verification';ctx.prec=256

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def lower(v,n=10):
 k=int((arb(v.lower())*10**n).floor().unique_fmpz());assert k>=0
 return f'{k//10**n}.{k%10**n:0{n}d}'
def main():
 p=argparse.ArgumentParser();p.add_argument('label');p.add_argument('--cells',type=int,default=131072);args=p.parse_args()
 files=sorted(BASE.glob(f'{args.label}_*_{args.cells}.json'));assert files
 parts={};sources={};params=None;inputs=[]
 for path in files:
  d=json.loads(path.read_text());inputs.append(path)
  key=(Q(d['alpha']),Q(d['b']));params=key if params is None else params;assert params==key
  assert d['cells']==args.cells and d['precision_bits']>=256
  for name,h in d['source_hashes'].items():
   src=ROOT/name;assert sha(src)==h,(name,'source changed');sources[name]=h
  parts.setdefault(d['part'],[]).append(d)
 assert set(parts)=={'plus','mid','minus'}
 totals={};intervals={}
 for name,chunks in parts.items():
  coverage=[0]*args.cells;total=arb(0)
  bounds={(Q(d['left']),Q(d['right'])) for d in chunks};assert len(bounds)==1
  for d in chunks:
   assert 0<=d['start']<d['stop']<=args.cells
   for i in range(d['start'],d['stop']):coverage[i]+=1
   value=arb(d['included_integral_enclosure']);assert value.lower()>0
   assert value.contains(arb(d['safe_integral_lower_10_places']))
   # Printed radii can widen the saved ball. Use its own lower endpoint.
   total+=value
  assert coverage==[1]*args.cells
  totals[name]=total;intervals[name]=[str(x) for x in bounds.pop()]
 result=1+2*sum(totals.values(),arb(0));safe=lower(result)
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=str(params[0]),b=str(params[1]),transformed_intervals=intervals,cells_per_part=args.cells,parts={k:dict(included_integral_enclosure=v.str(55,more=True),safe_lower_10_places=lower(v)) for k,v in totals.items()},included_D_enclosure=result.str(55,more=True),safe_D_lower_10_places=safe,source_hashes={**sources,**{str(x.relative_to(ROOT)):sha(x) for x in inputs+[Path(__file__)]}},verdict='CONFIRMED lower bound under the standalone analytic proof; no upper bound for this witness is asserted.')
 target=BASE/f'{args.label}_combined_{args.cells}.json';target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['alpha','b','included_D_enclosure','safe_D_lower_10_places']},indent=2))
if __name__=='__main__':main()

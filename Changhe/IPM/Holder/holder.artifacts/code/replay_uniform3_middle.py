"""Independent fixed-plan group replay using the previously audited geometry."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import argparse,json,hashlib,time
from flint import arb,ctx
from certify_middle_chunks import bin_data
from certify_far_circles import cell_measures
from middle_circle_plan import best_plan,edge_kind
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'09_uniform_comparison/pass3';ctx.prec=160

def main():
 p=argparse.ArgumentParser();p.add_argument('--start',type=int,required=True);p.add_argument('--stop',type=int,required=True);args=p.parse_args()
 prototype=json.loads((BASE/'data/mid/n512_0.json').read_text());n=prototype['angles_per_half'];nr=prototype['radial_cells'];m=prototype['phase_intervals'];unit=prototype['integer_unit']
 assert n==nr==512 and m==16 and unit==2**44 and 0<=args.start<args.stop<=nr
 groups=[(g.split(':')[0],g.split(':')[1].split(',')) for g in prototype['groups'].split(';')]
 pairs=[(ref,text) for ref,texts in groups for text in texts];sums={p:[arb(0) for _ in range(m+1)] for p in pairs};pi=arb.pi();started=time.monotonic()
 for row in range(args.start,args.stop):
  lo,hi,rmax,values,M1,M2=bin_data(row,nr,n)
  bases=([2*rmax*(hi*(k+1)/n).sin() for k in range(n)],[2*rmax*(lo*max(0,k-1)/n).cos() for k in range(n)])
  alltexts=set([r for r,_ in groups]+[t for _,t in pairs]);costs={text:([b**arb(text) for b in bases[0]],[b**arb(text) for b in bases[1]]) for text in alltexts}
  for j in range(m+1):
   phase=pi*j/(2*m);masses,tv=cell_measures(values,phase.cos(),phase.sin(),M1,M2,arb(2)/n,unit)
   remainder=tv-arb(sum(abs(v) for v in masses[:n]))/unit;assert remainder>=0
   for ref,texts in groups:
    c0,c1=costs[ref];plan,info=best_plan(masses,[float(c.mid()) for c in c0],[float(c.mid()) for c in c1],tries=prototype['plan_trials'])
    marg=[0]*len(masses);aggregated={}
    for (i,k),mass in plan.items():
     assert mass>=0 and masses[i]>0 and masses[k]<0
     marg[i]+=mass;marg[k]-=mass;key=edge_kind(i,k,n);aggregated[key]=aggregated.get(key,0)+mass
    assert marg==masses
    for text in texts:
     c0,c1=costs[text];value=sum((arb(mass)*(c0[k] if same else c1[k]) for (same,k),mass in aggregated.items()),arb(0))/unit
     value+=remainder*(2*rmax)**arb(text);sums[(ref,text)][j]+=value*(hi-lo)
  if row%4==0:print(row,args.stop,round(time.monotonic()-started,2),flush=True)
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),row_start=args.start,row_stop=args.stop,precision_bits=ctx.prec,groups=prototype['groups'],angles_per_half=n,radial_cells=nr,phase_intervals=m,rows=[dict(plan_reference_alpha=ref,alpha=text,middle_phase_intervals=[v.str(48,more=True) for v in sums[(ref,text)]]) for ref,text in pairs],elapsed_seconds=time.monotonic()-started)
 result['source_hashes']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),ROOT/'code/certify_middle_chunks.py',ROOT/'code/certify_far_circles.py',ROOT/'code/middle_circle_plan.py',ROOT/'code/circle_transport_plan.py']}
 q=BASE/f'verification/mid/replay_{args.start}_{args.stop}.json';q.write_text(json.dumps(result,indent=2)+'\n');print(q,flush=True)
if __name__=='__main__':main()

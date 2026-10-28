"""Merge complete diagonal local transport certificates with audited outer parts."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from flint import arb,ctx
from certify_far_circles import upper_decimal
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[1];ctx.prec=224

def main():
 p=argparse.ArgumentParser();p.add_argument('--chunks',nargs='+',required=True);p.add_argument('--out',required=True);a=p.parse_args()
 ds=[json.loads((ROOT/x).read_text()) for x in a.chunks];d=ds[0]
 keys=['alpha','power','precision_bits','angles_per_circle','radial_cells','phase_half_intervals','delta','integer_unit','source_hashes']
 for e in ds:
  for k in keys:assert e[k]==d[k],k
 for src,h in d['source_hashes'].items():assert hashlib.sha256((ROOT/src).read_bytes()).hexdigest()==h,src
 nr=d['radial_cells'];m=d['phase_half_intervals'];coverage=[[0]*(2*m+1) for _ in range(nr)];local=[arb(0) for _ in range(2*m+1)]
 for e in ds:
  assert set(map(int,e['partial_phase_intervals']))==set(range(e['phase_start'],e['phase_stop']))
  for r in range(e['row_start'],e['row_stop']):
   for j in range(e['phase_start'],e['phase_stop']):coverage[r][j]+=1
  for j,v in e['partial_phase_intervals'].items():local[int(j)]+=arb(v)
 assert all(v==1 for row in coverage for v in row)
 alpha=arb(d['alpha']);delta=arb(d['delta']);power=arb(d['power']);pi=arb.pi()
 a2=2**(1+alpha/2)/(pi*(alpha+2));small=2*a2*delta**alpha/alpha+(1+2*delta)**alpha*delta**2/(2*(1-delta)**2);eta=(2*delta)**power/2
 for e in ds:assert small.overlaps(arb(e['small_disk_upper'])) and eta.overlaps(arb(e['small_identity_mass']))
 paths=['data/middle_circle_certificate_n512.json','data/far_circle_certificate_fine.json']
 mid,far=[json.loads((ROOT/x).read_text()) for x in paths]
 assert mid['phase_intervals']==far['phase_intervals']==m
 mr=next(r for r in mid['rows'] if Fraction(r['alpha'])==Fraction(d['alpha']));fr=next(r for r in far['rows'] if Fraction(r['alpha'])==Fraction(d['alpha']))
 vals=[local[j]+arb(mr['middle_phase_intervals'][min(j,2*m-j)])+arb(fr['far_phase_intervals'][min(j,2*m-j)]) for j in range(2*m+1)]
 mx=vals[0]
 for v in vals[1:]:mx=arb.max(mx,v)
 sec=1/(pi/(4*m)).cos();upper=small+eta+sec*mx+(sec-1)*(arb(1)/2-eta)
 row=dict(alpha=d['alpha'],local_phase_intervals=[v.str(45,more=True) for v in local],regular_phase_intervals=[v.str(45,more=True) for v in vals],small_disk_upper=small.str(45,more=True),small_identity_mass=eta.str(45,more=True),phase_identity_correction=((sec-1)*(arb(1)/2-eta)).str(45,more=True),upper_D=upper.str(45,more=True),safe_upper_D=upper_decimal(upper),max_phase_index=max(range(2*m+1),key=lambda j:float(vals[j].mid())))
 paths+=a.chunks+['code/combine_local_diagonal.py']
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,phase_half_intervals=m,angles_per_circle=d['angles_per_circle'],radial_cells=nr,delta=d['delta'],power=d['power'],rows=[row],input_hashes={x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in paths},status='Complete local diagonal certificate. Independent mathematical and arithmetic audit required.')
 (ROOT/a.out).write_text(json.dumps(out,indent=2)+'\n');print(row['alpha'],row['safe_upper_D'],'phase',row['max_phase_index'])
if __name__=='__main__':main()

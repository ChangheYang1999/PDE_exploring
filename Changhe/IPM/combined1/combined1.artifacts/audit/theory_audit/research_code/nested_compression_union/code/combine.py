from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
from flint import fmpq as Q,arb,ctx
start=time.monotonic();ctx.prec=1024;sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parents[1];parent=base.parent
angular=Path(sys.argv[1]).resolve();radial=Path(sys.argv[2]).resolve()
signed=Path(sys.argv[3]).resolve() if len(sys.argv)>3 else None
A=json.loads(angular.read_text());R=json.loads(radial.read_text())
assert A['candidate']==R['candidate'] and R['dimension']>=A['N']
N=A['N'];d=R['dimension']
def ar(x):return arb(x.numerator)/x.denominator
def canonical_sha(obj):
 return next(v for k,v in obj['inputs'].items() if k.endswith('_canonical.json'))
assert canonical_sha(A)==canonical_sha(R)
E=A['blocks']['++'];inds=[i for i,l in enumerate(E['labels']) if l[0]=='cos' and l[1]==0]
assert len(inds)==N
checks=0
for i in inds:
 for j in inds:
  n,m=E['labels'][i][2],E['labels'][j][2]
  for key in ['G_over_pi','B_over_pi']:
   assert Q(E[key][i][j])==Q(R[key][n][m]);checks+=1
rows={r['dimension']:r for r in R['rows']};assert N in rows and d in rows
low=Q(rows[N]['captured_HS_energy_exact']);high=Q(rows[d]['captured_HS_energy_exact'])
old=Q(A['total_captured_exact']);union=old+high-low;assert high>=low and union>=old
kappa=arb(A['full_kappa']);assert kappa.overlaps(arb(R['full_kappa']))
c=Q(4076476460239181,2251799813685248)
remainder=kappa*kappa-ar(union);assert remainder>0
bound=remainder.sqrt()
inputs=[angular,radial,Path(__file__),base/'PROOF.md']
out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':A['candidate'],'precision_bits':ctx.prec,'angular_N':N,'angular_M':A['M'],'radial_dimension':d,'common_matrix_entries_checked':checks,'angular_energy':ar(old).str(90),'radial_common_energy':ar(low).str(90),'radial_extended_energy':ar(high).str(90),'union_energy_exact':str(union),'union_energy':ar(union).str(90),'S1_absolute_upper':bound.str(90),'theta_budget_for_beta2':(ar(c-1)-bound).str(90)}
if signed is not None:
 S=json.loads(signed.read_text());assert S['candidate']==A['candidate'] and canonical_sha(S)==canonical_sha(A)
 target=Q(S['target_HS_exact']);q=Q(S['certified_q']);ss=kappa*kappa-ar(union)-ar(target)+ar(q*q);assert ss>0
 sb=ss.sqrt();out.update({'signed_target_energy':ar(target).str(90),'signed_q':str(q),'S1_signed_upper':sb.str(90),'signed_theta_budget_for_beta2':(ar(c-1)-sb).str(90)})
 inputs.append(signed)
out['inputs']={str(p.relative_to(parent)):sha256(p.read_bytes()).hexdigest() for p in inputs}
out['status']='New union and signed theorems and nonradial arithmetic pending independent review'
out['elapsed_seconds']=time.monotonic()-start
suffix='_signed' if signed is not None else ''
path=base/'verification'/f"{A['candidate']}_n{N}_m{A['M']}_d{d}{suffix}.json";assert not path.exists()
path.write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k not in ['inputs','union_energy_exact']})

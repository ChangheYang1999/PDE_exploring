"""P357 finite width consistency; no convergence or independent-PDE claim."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time
r=Path('research/357_lower_width_formal_extension');v=r/'verification';start=datetime.now(timezone.utc);tick=time.monotonic();checks=[]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,t,d=None):checks.append(dict(name=n,passed=bool(t),detail=d))
f=json.loads((v/'freeze.json').read_text());ck('proof_hash',sha(r/'PROOF.md')==f['proof_sha256']);ck('proof_prepared_before_run',f['prepared_utc']<f['run_started_utc']);ck('freeze_before_audit',f['frozen_utc']<start.isoformat())
for x in f['inputs']:ck('hash_'+x['copy'],sha(x['copy'])==x['sha256']);ck('size_'+x['copy'],Path(x['copy']).stat().st_size==x['bytes'])
a=json.loads((v/'n11w300.json').read_text());b=json.loads((v/'n12w200.json').read_text());af=json.loads((v/'n11w300_coefficients.json').read_text());bf=json.loads((v/'n12w200_coefficients.json').read_text());N=b['records'][-1]['n'];M=min(a['records'][-1]['n'],N)
ck('width300_completed11',a['records'][-1]['n']==11 and a['parameters']['width']==300);ck('width200_requested12',b['parameters']['width']==200 and b['parameters']['order']==12);ck('not_claiming_unfinished_order',N<=12 and (b['status']!='COMPLETE' or N==12));ck('same_parameters',Q(a['parameters']['C'])==Q(b['parameters']['C'])==1 and Q(a['parameters']['k'])==Q(b['parameters']['k'])==-1)
ck('same_source_hash',a['code_sha256']==b['code_sha256']==sha(v/'solve_nonlinear_formal_jets.py'));ck('same_arithmetic_hash',a['arithmetic_sha256']==b['arithmetic_sha256']==sha(v/'check_all_order_fraction_jets.py'))
for tag,d,fields in [('width300',a,af),('width200',b,bf)]:
 nmax=d['records'][-1]['n'];ck(tag+'_stages_contiguous',[x['n']for x in d['records']]==list(range(2,nmax+1)));ck(tag+'_all_internal',d['passed']==d['total']==len(d['checks']) and all(x['passed']for x in d['checks']));ck(tag+'_internal_count',d['total']==(3*nmax*nmax+27*nmax-20)//2)
 ck(tag+'_checkpoint_time',d['started_utc']<=d['checkpoint_utc']<=f['frozen_utc'])
 for label,lo,hi in [('theta',1,nmax+1),('omega',0,nmax),('v',0,nmax+1)]:
  ck(tag+'_'+label+'_indices',set(map(int,fields[label]))==set(range(lo,hi+1)))
  for idx,e in fields[label].items():ck(tag+'_'+label+idx+'_precision',all(0<=int(k)<e['known_high']for k in e['coefficients']))
 for rec in d['records']:
  for label,idx,key in [('theta',rec['n'],'theta_leading'),('omega',rec['n']-1,'omega_leading')]:
   e=fields[label][str(idx)]['coefficients'];lead=min(map(int,e));ck(tag+f'_n{rec["n"]}_{key}',lead==rec[key][0] and Q(e[str(lead)])==Q(rec[key][1]))
  ck(tag+f'_n{rec["n"]}_residue_precision',min(rec['residue_known_high'])>-1)
 for item in d['checks']:
  e=item.get('detail')
  if isinstance(e,dict)and 'tested_high'in e:ck(tag+'_nonvacuous_'+item['name'],e['tested_high']-e.get('tested_low',0)>=20 and e['tested_high']<=e['known_high']and not e['first_nonzero'])
for n in range(2,M+1):
 x=next(r for r in a['records']if r['n']==n);y=next(r for r in b['records']if r['n']==n)
 for key in ['E','F','fixed_residue_T','fixed_residue_O']:ck(f'n{n}_{key}',Q(x[key])==Q(y[key]))
counts=[]
for label,hi in [('theta',M),('omega',M-1),('v',M)]:
 for idx,x in af[label].items():
  if int(idx)>hi:continue
  y=bf[label][idx];h=min(x['known_high'],y['known_high']);ck(label+idx+'_nonvacuous',h>=20);bad=[];nonzero=0
  for j in range(h):
   left=Q(x['coefficients'].get(str(j),'0'));right=Q(y['coefficients'].get(str(j),'0'));nonzero+=left!=0
   if left!=right:bad.append(j)
  ck(label+idx+'_agreement',not bad,dict(powers=h,nonzero=nonzero,bad=bad[:5]));counts.append(dict(field=label,index=int(idx),powers=h,nonzero=nonzero,zeros=h-nonzero))
for n in range(2,N+1):
 wants={f'n{n}_Eplus_thermal_negative':Q(-12,5*(2*n+1)),f'n{n}_Eplus_vorticity_negative':Q(-(2*n+5),385*(2*n+1)),f'n{n}_Fplus_thermal_negative':Q(0),f'n{n}_Fplus_vorticity_negative':Q(9,10*n)}
 for name,w in wants.items():
  found=[x for x in b['checks']if x['name']==name];ck(name+'_independent_matrix_value',len(found)==1 and Q(found[0]['detail']['actual'])==Q(found[0]['detail']['expected'])==w)
ranges=[x['detail']['tested_count']for x in b['checks']if isinstance(x.get('detail'),dict)and'tested_count'in x['detail']]
end=datetime.now(timezone.utc);out=dict(started_utc=start.isoformat(),ended_utc=end.isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(c['passed']for c in checks),total=len(checks),completed_order=N,requested_order=12,saved_status=b['status'],compared_final_order=M,compared_powers=sum(x['powers']for x in counts),compared_nonzero=sum(x['nonzero']for x in counts),compared_zeros=sum(x['zeros']for x in counts),minimum_shared_powers=min(x['powers']for x in counts),minimum_new_internal_powers=min(ranges),new_internal_controls=b['total'],proof_sha256=sha(r/'PROOF.md'),code_sha256=sha(__file__),counts=counts,checks=checks,scope='Shared recurrence and Fraction arithmetic; finite two-width consistency, not an independent PDE implementation or a proof of convergence, profile or endpoint.')
(v/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:x for k,x in out.items()if k not in ['checks','counts']},indent=2));print('FAILED',[x for x in checks if not x['passed']]);raise SystemExit(0 if all(x['passed']for x in checks)else 1)

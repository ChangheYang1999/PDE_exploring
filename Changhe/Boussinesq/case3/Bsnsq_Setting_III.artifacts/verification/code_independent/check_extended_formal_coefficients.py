"""Exact frozen checkpoint audit; own implementations only."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time
r=Path('research/354_extended_formal_coefficients');v=r/'verification';start=datetime.now(timezone.utc);tick=time.monotonic();checks=[]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,t,d=None):checks.append(dict(name=n,passed=bool(t),detail=d))
def load(tag,tail=''):return json.loads((v/(tag+tail+'.json')).read_text())
f=json.loads((v/'freeze.json').read_text());ck('proof_hash',sha(r/'PROOF.md')==f['proof_sha256']);ck('proof_before',f.get('revised_utc',f['prepared_utc'])<start.isoformat())
for a in f['inputs']:ck('hash_'+a['copy'],sha(a['copy'])==a['sha256']);ck('size_'+a['copy'],Path(a['copy']).stat().st_size==a['bytes'])
old=load('n10w190');new=load('v5_n16w300_C1kminus1');a=load('n10w190','_coefficients');b=load('v5_n16w300_C1kminus1','_coefficients');N=new['records'][-1]['n'];M=min(10,N)
ck('old_complete',old['status']=='COMPLETE' and old['records'][-1]['n']==10);ck('new_saved_status',new['status']=='RUNNING');ck('requested_order_not_completed',new['parameters']['order']==16 and N<16);ck('stage11_completed',N==11);ck('new_width',new['parameters']['width']==300);ck('old_width',old['parameters']['width']==190)
ck('same_parameters',Q(new['parameters']['C'])==Q(old['parameters']['C'])==1 and Q(new['parameters']['k'])==Q(old['parameters']['k'])==-1)
ck('new_solver_hash',new['code_sha256']==sha(v/'solve_nonlinear_formal_jets.py'));ck('old_solver_hash',old['code_sha256']==sha(v/'solver_v1_readonly.py'));ck('same_arithmetic',new['arithmetic_sha256']==old['arithmetic_sha256']==sha(v/'check_all_order_fraction_jets.py'))
for tag,d,fields in [('old',old,a),('new',new,b)]:
 nmax=d['records'][-1]['n'];ck(tag+'_contiguous_stages',[q['n']for q in d['records']]==list(range(2,nmax+1)));ck(tag+'_all_internal_checks',d['passed']==d['total']==len(d['checks']) and all(c['passed']for c in d['checks']));ck(tag+'_time_order',d['started_utc']<=d['checkpoint_utc']<=f['frozen_utc'])
 for label,minn,maxn in [('theta',1,nmax+1),('omega',0,nmax),('v',0,nmax+1)]:
  ck(tag+'_'+label+'_indices',set(map(int,fields[label]))==set(range(minn,maxn+1)))
  for idx,entry in fields[label].items():
   ck(tag+'_'+label+'_'+idx+'_coefficient_precision',all(0<=int(e)<entry['known_high']for e in entry['coefficients']))
 for rec in d['records']:
  for label,idx,key in [('theta',rec['n'],'theta_leading'),('omega',rec['n']-1,'omega_leading')]:
   entry=fields[label][str(idx)]['coefficients'];first=min(map(int,entry));ck(tag+f'_n{rec["n"]}_{key}_matches_dump',first==rec[key][0] and Q(entry[str(first)])==Q(rec[key][1]))
 for c in d['checks']:
  detail=c.get('detail')
  if isinstance(detail,dict) and 'tested_high'in detail:
   lo=detail.get('tested_low',0);hi=detail['tested_high'];ck(tag+'_nonvacuous_'+c['name'],hi-lo>=20 and hi<=detail['known_high'] and not detail['first_nonzero'])
 for rec in d['records']:ck(tag+f'_n{rec["n"]}_residue_precision',min(rec['residue_known_high'])>-1)
for n in range(2,M+1):
 x=next(d for d in old['records']if d['n']==n);y=next(d for d in new['records']if d['n']==n)
 for key in ['E','F','fixed_residue_T','fixed_residue_O']:ck(f'n{n}_{key}_width_agreement',Q(x[key])==Q(y[key]))
powers=0
for field,maxn in [('theta',M),('omega',M-1),('v',M)]:
 for idx,x in a[field].items():
  if int(idx)>maxn:continue
  y=b[field][idx];h=min(x['known_high'],y['known_high']);ck(field+'_'+idx+'_comparison_range',h>=20);bad=[]
  for j in range(h):
   if Q(x['coefficients'].get(str(j),'0'))!=Q(y['coefficients'].get(str(j),'0')):bad.append(j)
  powers+=h;ck(field+'_'+idx+'_exact_agreement',not bad,dict(powers=h,bad_indices=bad[:5]))
negative=[c for c in new['checks']if c['name'].endswith('_negative')];ck('four_negative_checks_per_stage',len(negative)==4*(N-1))
for n in range(2,N+1):
 wants={f'n{n}_Eplus_thermal_negative':Q(-12,5*(2*n+1)),f'n{n}_Eplus_vorticity_negative':Q(-(2*n+5),385*(2*n+1)),f'n{n}_Fplus_thermal_negative':Q(0),f'n{n}_Fplus_vorticity_negative':Q(9,10*n)}
 for name,want in wants.items():
  found=[c for c in negative if c['name']==name];ck(name+'_independent_value',len(found)==1 and Q(found[0]['detail']['actual'])==Q(found[0]['detail']['expected'])==want)
counts={}
for key,test in [('thermal',lambda n:'_full_T'in n),('vorticity',lambda n:'_full_V'in n),('poisson_definitional',lambda n:'poisson_update_consistency'in n),('negative',lambda n:n.endswith('_negative')),('analytic_jets',lambda n:'analytic_jets'in n),('residue',lambda n:'residue'in n)]:counts[key]=sum(test(c['name'])for c in new['checks'])
counts['base_J_integrand']=sum(c['name']=='base_J_analytic_integrand'for c in new['checks'])
ranges=[c['detail']['tested_count']for c in new['checks']if isinstance(c.get('detail'),dict) and 'tested_count'in c['detail']]
ck('new_range_count',len(ranges)==counts['thermal']+counts['vorticity']+counts['poisson_definitional']);ck('new_internal320',new['total']==320)
ratios=[]
for rec in new['records']:
 row={'n':rec['n']}
 for key in ['E','F']:
  val=Q(rec[key]);row[key+'_numerator_digits']=len(str(abs(val.numerator)));row[key+'_denominator_digits']=len(str(val.denominator));row[key+'_approx']=float(val)
 ratios.append(row)
end=datetime.now(timezone.utc);out=dict(started_utc=start.isoformat(),ended_utc=end.isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(c['passed']for c in checks),total=len(checks),completed_order=N,requested_order=16,compared_final_order=M,compared_coefficients=powers,internal_counts=counts,minimum_new_run_tested_powers=min(ranges),shared_range_min=min(c['detail']['powers']for c in checks if c['name'].endswith('_exact_agreement')),proof_sha256=sha(r/'PROOF.md'),code_sha256=sha(__file__),checks=checks,coefficient_size_diagnostic=ratios,scope='Exact finite width and checkpoint consistency only; shared arithmetic and recurrence. No convergence or global profile.')
(v/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:x for k,x in out.items()if k not in ['checks','coefficient_size_diagnostic']},indent=2));print('failed',[c for c in checks if not c['passed']])

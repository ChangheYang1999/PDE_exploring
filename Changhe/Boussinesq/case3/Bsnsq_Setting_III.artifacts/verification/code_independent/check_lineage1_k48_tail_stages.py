"""Separate exact witness consumer and finite stage comparison for P262."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,re,time
import numpy as np
R=Path('research/262_lineage1_k48_regional/verification');t0=time.monotonic();started=datetime.now(timezone.utc).isoformat();checks=[]
def check(name,ok,detail=None):checks.append({'name':name,'passed':bool(ok),'detail':detail})
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def prod(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def power(z,n):
 if n<0:
  d=z[0]**2+z[1]**2;z=(z[0]/d,-z[1]/d);n=-n
 out=(Q(1),Q(0))
 while n:
  if n&1:out=prod(out,z)
  z=prod(z,z);n//=2
 return out
def evaluate(poly,x,y,derivative=False):
 out=(Q(0),Q(0))
 for n,c in poly.items():
  n=int(n);v=tuple(map(Q,c))
  if derivative:v=(-n*v[1],n*v[0])
  v=prod(v,power((x,y),n));out=(out[0]+v[0],out[1]+v[1])
 return out
manifest=json.loads((R/'manifest.json').read_text());known={s['sha256']:s for s in manifest['states']}
tail=json.loads((R/'exact_native_tail.json').read_text())
for s in tail['states']:
 src=known[s['archive_sha256']];check('archive',h(R/src['snapshot'])==s['archive_sha256'],src['label'])
 beta=Q(s['beta_exact']);check('exponent_order',1-3/beta>Q(2,3)-2/beta>0>1-4/beta,str(beta))
 for key,w in s['exact_witnesses'].items():
  x,y=Q(w['cos_theta']),Q(w['sin_theta']);check('unit_witness',x*x+y*y==1,[src['label'],key]);val=evaluate(s['coefficients'][key],x,y)
  check('exact_nonzero_witness',val[1]==0 and val[0]==Q(w['exact_value']) and val[0]!=0,[src['label'],key,float(val[0])])
 for axis in s['source_axes']:
  y=Q(axis['sin_theta']);v=evaluate(s['coefficients']['PS0'],Q(0),y);dv=evaluate(s['coefficients']['PS0'],Q(0),y,True)
  check('source_simple_axis_zero',v==(0,0) and dv[1]==0 and dv[0]==Q(axis['PS_derivative']) and dv[0]!=0,[src['label'],str(y),float(dv[0])])


for src in manifest['supporting_inputs']:
 check('supporting_input_hash',h(R/src['snapshot'])==src['sha256'],src['snapshot'])
records=[]
for p in sorted(R.glob('*.npz')):
 if p.name.endswith(('_transport.npz','_self.npz')): continue
 with np.load(p,allow_pickle=False) as z:
  a={k:z[k].item() for k in ['beta','lam','K','Nt','a0','strain_mismatch','obj','converged','inner_f']}
  a.update(file=p.name,sha256=h(p),source_sha256=hashlib.sha256(z['cG_f'].tobytes()).hexdigest(),source_geometry={k:z[k].item()for k in z.files if k.startswith('seed_') and z[k].shape==()})
  records.append(a)
check('same_fixed_source',len({a['source_sha256']for a in records})==1 and all(a['source_geometry']==records[0]['source_geometry']for a in records))
log=(R/'blamB48ext.log').read_text();stages=[]
for line in log.splitlines():
 if line.startswith('  secant '):
  match=re.search(r'secant (\d+): beta=([\d.]+) lambda=([\d.]+) m=([+\deE.-]+).*iters=(\d+)',line)
  if match: stages.append({'secant':int(match[1]),'beta':float(match[2]),'lambda_rounded':float(match[3]),'m_rounded':float(match[4]),'iterations':int(match[5])})
check('completed_logged_stages',[(a['beta'],a['secant'],a['iterations'])for a in stages]==[(3.076,0,11),(3.092,0,33),(3.092,1,20)])
check('only_first_outer_stage_accepted',len(re.findall(r'# stage beta=3\.076:.*ok=True',log))==1 and '# stage beta=3.092:' not in log)
with np.load(R/'blamB48ext_start.npz',allow_pickle=False) as a,np.load(R/'blamB48ext_beta3.076.npz',allow_pickle=False) as b,np.load(R/'blamB48ext_beta3.076_sec0.npz',allow_pickle=False) as c,np.load(R/'blamB40ext_beta3.076.npz',allow_pickle=False) as old:
 changes={k:{'max_abs':float(np.max(abs(a[k]-b[k]))),'bitwise_equal':bool(np.array_equal(a[k],b[k]))}for k in ['cF','cG','cG_f']}
 check('inherited_lambda',a['lam'].item()==b['lam'].item()==old['lam'].item())
 check('vorticity_reoptimized',changes['cG']['max_abs']>1)
 check('temperature_reoptimized',changes['cF']['max_abs']>.7)
 check('source_preserved',changes['cG_f']['bitwise_equal'])
 check('accepted_state_equals_secant_data',all(np.array_equal(b[k],c[k])for k in ['cF','cG','cG_f','beta','lam']))
 check('old_objective_reproduced_in_start',a['obj'].item()==old['obj'].item())
 objective={'K40':old['obj'].item(),'K48':b['obj'].item(),'ratio_K48_over_K40':float(b['obj']/old['obj'])}
 check('lower_discrete_objective',objective['K48']<objective['K40'])
 check('center_a0_unchanged_nonzero',b['a0'].item()==1.011258)
center=json.loads((R/'center_certificates/checks.json').read_text());check('exact_center_consumer_passed',center['all_passed'])
c=center['checks'][0]['inverse'];saved=next(a for a in records if a['file']=='blamB48ext_beta3.076.npz')
mdiff=c['forced']['m']-saved['strain_mismatch'];check('center_saved_vs_exact',abs(mdiff)<2e-7,mdiff)
check('center_self_defect_positive',c['self']['ratioF']>1e-6 and c['self']['RF']<0)
c2=json.loads((R/'inverse_constant_certificates/summary.json').read_text())['rows'][0]
check('C2_nonzero_negative',Q(c2['C2_enclosure'][0])<Q(c2['C2_enclosure'][1])<0,c2['C2_enclosure_float'])
certcheck=json.loads((R/'inverse_constant_certificates/blamB48ext_beta3p076_certificate.check.json').read_text())
check('inverse_certificate_consumer_passed',certcheck['verdict']=='CONFIRMED_NEGATIVE',list(certcheck))
out={'started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t0,'passed':sum(c['passed']for c in checks),'total':len(checks),'checks':checks,'records':records,'stages':stages,'inherited_start_comparison':changes,'objective_comparison':objective,'center':c,'saved_center_m_difference':mdiff,'C2':c2,'script_sha256':h(__file__),'scope':'Frozen first-lineage K48 beta3.076 finite stage comparison, exact center/tail certificate consumers. beta3.092 was incomplete at freeze; no root, fold, continuum limit or B2 profile inferred.'}
(R/'tail_stage_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(out['passed'],out['total']);print([a for a in checks if not a['passed']])

"""Separate exact witness consumer and backward stage comparison for P280."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,re,time
import numpy as np
R=Path('research/280_backward_k48_beta3062/verification');t0=time.monotonic();started=datetime.now(timezone.utc).isoformat();checks=[]
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
log=(R/'blamB48ext2.log').read_text();stages=[]
for line in log.splitlines():
 if line.startswith('  secant '):
  match=re.search(r'secant (\d+): beta=([\d.]+) lambda=([\d.]+) m=([+\deE.-]+).*iters=(\d+)',line)
  if match and float(match[2])==3.062: stages.append({'secant':int(match[1]),'beta':float(match[2]),'lambda_rounded':float(match[3]),'m_rounded':float(match[4]),'iterations':int(match[5])})
check('completed_logged_stages',[(a['beta'],a['secant'],a['iterations'])for a in stages]==[(3.062,0,20),(3.062,1,19),(3.062,2,19),(3.062,3,8)])
check('target_logged_stage_accepted',len(re.findall(r'# stage beta=3\.062:.*ok=True',log))==1)
with np.load(R/'blamB48ext2_beta3.076.npz',allow_pickle=False) as a,np.load(R/'blamB48ext2_beta3.062.npz',allow_pickle=False) as b,np.load(R/'blamB48ext2_beta3.062_sec3.npz',allow_pickle=False) as c,np.load(R/'blamB40ext_beta3.062.npz',allow_pickle=False) as old, np.load(R/'blamB32_beta3.062.npz',allow_pickle=False) as k32, np.load(R/'blamB48ext_beta3.092.npz',allow_pickle=False) as upper:
 changes={k:{'max_abs':float(np.max(abs(a[k]-b[k]))),'bitwise_equal':bool(np.array_equal(a[k],b[k]))}for k in ['cF','cG','cG_f']}
 check('lambda_reoptimized',a['lam'].item()!=b['lam'].item())
 check('vorticity_reoptimized',changes['cG']['max_abs']>0)
 check('temperature_reoptimized',changes['cF']['max_abs']>0)
 check('source_preserved',changes['cG_f']['bitwise_equal'])
 check('accepted_state_equals_secant3_data',all(np.array_equal(b[k],c[k])for k in ['cF','cG','cG_f','beta','lam']))
 objective={'K32':k32['obj'].item(),'K40':old['obj'].item(),'K48':b['obj'].item(),'ratio_K48_over_K40':float(b['obj']/old['obj']),'ratio_K48_over_K32':float(b['obj']/k32['obj'])}
 lambda_comparison={'K32':k32['lam'].item(),'K40':old['lam'].item(),'K48':b['lam'].item(),'K48_minus_K40':float(b['lam']-old['lam']),'K48_minus_K32':float(b['lam']-k32['lam']),'restart_beta3076':a['lam'].item(),'upper_beta3092':upper['lam'].item()}
 check('lower_discrete_objective',objective['K48']<objective['K40']<objective['K32'])
 check('lambda_K40_agreement_below_1e6',abs(lambda_comparison['K48_minus_K40'])<1e-6)
 check('lambda_K32_agreement_below_1e6',abs(lambda_comparison['K48_minus_K32'])<1e-6)
 check('center_a0_unchanged_nonzero',b['a0'].item()==1.011258)
 check('sampled_middle_K48_lambda_strictly_lower',a['lam'].item()<min(b['lam'].item(),upper['lam'].item()))
 check('objective_accept_factor_set_1e9','--accept_factor 1e9' in (R/'b48ext2.sh').read_text())
 check('accepted_inner_and_outer_flags',all(b[k].item()==1 for k in ['converged','inner_converged','continuation_accepted']))
 check('accept_factor_not_a_small_objective_bound',b['obj'].item()>1)
center=json.loads((R/'center_certificates/checks.json').read_text());check('exact_center_consumer_passed',center['all_passed'])
c=center['checks'][0]['inverse'];saved=next(a for a in records if a['file']=='blamB48ext2_beta3.062.npz')
mdiff=c['forced']['m']-saved['strain_mismatch'];check('center_saved_vs_exact',abs(mdiff)<2e-7,mdiff)
check('center_self_defect_nonzero',c['self']['ratioF']>0 and c['self']['RF']!=0)
c2=json.loads((R/'inverse_constant_certificates/summary.json').read_text())['rows'][0]
check('C2_nonzero_negative',Q(c2['C2_enclosure'][0])<Q(c2['C2_enclosure'][1])<0,c2['C2_enclosure_float'])
certcheck=json.loads((R/'inverse_constant_certificates/blamB48ext2_beta3p062_certificate.check.json').read_text())
check('inverse_certificate_consumer_passed',certcheck['verdict']=='CONFIRMED_NEGATIVE',list(certcheck))
out={'started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t0,'passed':sum(c['passed']for c in checks),'total':len(checks),'checks':checks,'records':records,'stages':stages,'previous_stage_comparison':changes,'objective_comparison':objective,'lambda_comparison':lambda_comparison,'center':c,'saved_center_m_difference':mdiff,'C2':c2,'script_sha256':h(__file__),'scope':'Frozen backward first-lineage K48 beta3.062 accepted stage and four secants, exact center/tail certificate consumers. No exact root, derivative, fold, continuum limit or B2 profile inferred.'}
(R/'tail_stage_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(out['passed'],out['total']);print([a for a in checks if not a['passed']])

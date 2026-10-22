"""Execute selected frozen producer expressions on all saved replay operands."""
from pathlib import Path
from datetime import datetime,timezone
import ast,json,hashlib,sys,math,time,copy
import numpy as np
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];S=B/'research/localized_forcing/source/src';sys.path.insert(0,str(S))
from midrad import MR,U,succ
from cert_resid import TMArr,mag
start=time.monotonic()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
audit=json.loads((D/'evidence/audit.json').read_text());pins=dict(audit['pins']);assert len(pins)==165
for p,h in pins.items():
 # The large inherited Green NPZ is streamed to avoid a duplicate allocation.
 digest=hashlib.sha256()
 with (B/p).open('rb') as f:
  for c in iter(lambda:f.read(1048576),b''):digest.update(c)
 assert digest.hexdigest()==h,p
source=ast.parse((S/'cert_forcing.py').read_text());main=next(n for n in source.body if isinstance(n,ast.FunctionDef) and n.name=='main');records=[]
def assign(name):
 ns=[n for n in ast.walk(main) if isinstance(n,ast.Assign) and any(ast.unparse(t)==name for t in n.targets)];assert len(ns)==1,(name,len(ns))
 records.append({'target':name,'expression':ast.unparse(ns[0].value),'line':ns[0].lineno});return ns[0]
def expr(node,ns):return eval(compile(ast.Expression(body=copy.deepcopy(node)),'selected_frozen_expression','eval'),ns)
r2assign=assign('r2');supsassign=assign('epsSup');wqassign=assign('wq');fpassign=assign('fpow')
append={name:[n for n in ast.walk(main) if isinstance(n,ast.Call) and ast.unparse(n.func)==name+'.append'] for name in ['fpow','remfac']}
for k,nodes in append.items():assert len(nodes)==1;records.append({'append':k,'expression':ast.unparse(nodes[0].args[0]),'line':nodes[0].lineno})
ns={'np':np,'MR':MR,'succ':succ,'U':U,'mag':mag,'factorial':math.factorial,'Nmax':522,'Qp':8,'NDER':4}
with np.load(D/'evidence/factors.npz',allow_pickle=False) as z:
 ns['w_up']=float(z['w']);ns['twoN1']=z['nu'].copy();saved_fac=z['remfac'].copy();saved_wq=float(z['wq']);saved_fpm=z['fpow_mid'].copy();saved_fpr=z['fpow_rad'].copy()
ns['fpow']=expr(fpassign.value,ns)
for m in range(1,14):ns['fpow'].append(expr(append['fpow'][0].args[0],ns))
assert np.array_equal(np.stack([p.m for p in ns['fpow']]),saved_fpm) and np.array_equal(np.stack([p.r for p in ns['fpow']]),saved_fpr)
ns['wq']=expr(wqassign.value,ns);assert ns['wq']==saved_wq
fac=[]
for j in range(5):ns['j']=j;fac.append(expr(append['remfac'][0].args[0],ns))
assert np.array_equal(np.stack(fac),saved_fac);ns['A']={'remfac':fac}
mode_count=0;reduction_count=0
for ci in range(4096,4109):
 with np.load(D/'evidence'/f'cell_{ci}.npz',allow_pickle=False) as z:
  ns['eps']=[TMArr(MR(z['coef_mid'][i],z['coef_rad'][i]),z['rem'][i]) for i in range(5)];ns['hpow1']=z['hpow'];saved_sup=z['epsSup'];saved_r2=z['r2_native'];pairs=z['pairs']
  ns['epsSup']=expr(supsassign.value,ns);assert np.array_equal(np.stack(ns['epsSup']),saved_sup);mode_count+=saved_sup.size
  for pos,(i,j) in enumerate(pairs):
   ns['i']=int(i);ns['j']=int(j);value=expr(r2assign.value,ns);assert value==saved_r2[pos],(ci,i,j,value,saved_r2[pos]);reduction_count+=1
assert mode_count==33995 and reduction_count==195
for f in ['ADDENDUM.md','code/source_binding.py','evidence/audit.json']:
 p=D/f;pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-start,'status':'PASS_SELECTED_FROZEN_EXPRESSION_REPLAY','original_audit_pins':165,'source_expressions':records,'frequency_midpoint_radius_entries':2*14*523,'factor_entries':5*523,'epsSup_entries':mode_count,'r2_entries':reduction_count,'pins':dict(sorted(pins.items())),'scope':'Selected frozen expressions on saved contemporary inputs only, no complete pipeline execution or historic attestation.'}
(D/'evidence/source_binding.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(pins),'pins',out['seconds'],'seconds')

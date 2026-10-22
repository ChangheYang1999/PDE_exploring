"""Cross-engine endpoint comparisons, frozen dependencies, and replay dimensions."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,ast,sys
import numpy as np
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];P=B/'research/localized_forcing'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 return h.hexdigest()
def read(p):return json.loads(p.read_text())
def ff(x):return F.from_float(float(x))
prior=read(P/'evidence/verdict.json');assert prior['status']=='CONFIRMED_FINITE_COMPONENTS_PHYSICAL_FORCING_OPEN';pins=dict(prior['files']);assert len(pins)==139
for path,h in pins.items():assert sha(B/path)==h,path
reg=read(D/'evidence/regeneration.json');a=read(D/'evidence/arb.json');e=read(D/'evidence/exact_iv.json');geo=read(P/'evidence/geometry_arb.json')
assert reg['status']=='REGENERATED_INPUTS_REQUIRING_TWO_ENGINE_AUDIT'
assert a['status']=='PASS_REGENERATED_ANGULAR_REDUCTION_ARB' and e['status']=='PASS_REGENERATED_ANGULAR_REDUCTION_EXACT_IV'
for obj in [reg,a,e]:
 for p,h in obj['pins'].items():
  assert sha(B/p)==h,p
  if p in pins:assert pins[p]==h,p
  pins[p]=h
for key,val in [('radial_mode_checks',33995),('coefficient_entries',441935),('factor_checks',2615),('power_checks',351),('reduction_checks',195),('subnormal_threshold_checks',195)]:assert a[key]==e[key]==val
assert reg['cell_count']==13 and reg['radial_models']==65 and reg['per_mode_sups']==33995 and reg['reductions']==195 and reg['n']==523
assert reg['Qs']==12 and reg['Qp']==8 and e['factor_iv_checks']==2615
assert len(a['rows'])==len(e['rows'])==195
pairs=[(i,j) for i in range(5) for j in range(5-i)];seen=[];row_checks=0
for aa,ee in zip(a['rows'],e['rows']):
 key=tuple(aa[x] for x in ['ci','i','j']);assert key==tuple(ee[x] for x in ['ci','i','j']);seen.append(key)
 s=F(ee['S_exact']);r=F(ee['r2_exact']);slack=F(ee['slack_exact']);rel=F(ee['relative_slack_exact']);raw=F(ee['native_sum'])
 assert 0<F(aa['S']['lower'])<=s<=F(aa['S']['upper'])<=r
 assert r==F(aa['r2']) and slack==r-s>0 and rel==slack/r>0
 assert 0<F(aa['relative_slack']['lower'])<=rel<=F(aa['relative_slack']['upper'])
 assert raw==F(aa['native_sum'])>F(523,2**1021);row_checks+=4
assert seen==[(ci,i,j) for ci in range(4096,4109) for i,j in pairs]
for stem in ['min_model_relative_slack','min_r2_relative_slack','min_factor_relative_slack']:
 x=F(e[stem+'_exact']);assert 0<F(a[stem]['lower'])<=x<=F(a[stem]['upper'])
assert F(e['min_model_relative_slack_exact'])>F(1816684,10**21)
assert F(e['min_r2_relative_slack_exact'])>F(5827561,10**20)
assert F(e['min_native_sum_exact'])>F(2,10**21) and F(e['max_native_sum_exact'])<F(61,10**10)
# Bind regenerated radial powers and common angular half-width to the finite geometry.
with np.load(D/'evidence/factors.npz',allow_pickle=False) as z:
 assert ff(z['w'])==ff(geo['w_up']);assert z['fpow_mid'].shape==z['fpow_rad'].shape==(14,523)
 assert np.array_equal(z['nu'],2*np.arange(523)+1)
for ci,g in zip(range(4096,4109),geo['cells']):
 assert ci==g['ci']
 with np.load(D/'evidence'/f'cell_{ci}.npz',allow_pickle=False) as z:
  assert ff(z['h'])==ff(g['h_up'])
  for key in ['h','hpow','coef_mid','coef_rad','rem','epsSup','sum_native','r2_native']:
   assert z[key].dtype==np.dtype('float64') and np.isfinite(z[key]).all()
# Formula matches verify the source read in review. They are not historic execution records.
tree=ast.parse((D/'code/regenerate.py').read_text());matches=[]
def assignment(target,expression):
 ns=[n for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(ast.unparse(t)==target for t in n.targets)]
 assert len(ns)==1,(target,len(ns));assert ast.dump(ns[0].value)==ast.dump(ast.parse(expression,mode='eval').body),(target,ast.unparse(ns[0].value))
 matches.append({'target':target,'expression':expression,'line':ns[0].lineno})
for target,expr in [('eps','C._last_eps'),('epsSup','[e.sup(cell.hpow) for e in eps]'),('wq','succ(w**(Qp+1)*(1+2*(Qp+1)*U)/math.factorial(Qp+1))'),('remfac','[succ(mag(fpow[j+Qp+1])*wq*(1+2*U)) for j in range(NDER+1)]'),('shat','(epsSup[i]*remfac[j]).sum()'),('rr','succ(shat*succ(1+(Nmax+2)*U))')]:assignment(target,expr)
assert read(D/'evidence/proof_first.json')['sha256']==sha(D/'PROOF.md')
for f in ['PROOF.md','NUMERICAL_RESULT.md','code/regenerate.py','code/arb_check.py','code/exact_check.py','code/audit.py','evidence/proof_first.json','evidence/regeneration.json','evidence/arb.json','evidence/exact_iv.json']:
 p=D/f;pins[str(p.relative_to(B))]=sha(p)
p=P/'evidence/verdict.json';pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_REGENERATED_FINITE_ARITHMETIC_REQUIRES_MODEL_REVIEW','prior_pins':139,'endpoint_tests':row_checks+3,'source_assignment_checks':matches,'counts':{k:a[k] for k in ['radial_mode_checks','coefficient_entries','factor_checks','power_checks','reduction_checks','subnormal_threshold_checks']},'min_model_relative_slack_gt':'1816684/10^21','min_r2_relative_slack_gt':'5827561/10^20','pins':dict(sorted(pins.items())),'scope':'Contemporary frozen-source replay only. Exact sums bypass generic kernel hypotheses for these finite outputs only. Inherited radial models and complete physical forcing OPEN.'}
(D/'evidence/audit.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(pins),'pins',row_checks+3,'endpoint tests')

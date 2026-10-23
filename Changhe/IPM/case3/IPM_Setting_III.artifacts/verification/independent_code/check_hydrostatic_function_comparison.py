from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,math
import numpy as np
R=Path('research/hydrostatic_function_space_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[]
def ck(n,v,e=None):checks.append(dict(name=n,passed=bool(v),evidence=e))
g=json.loads((V/'CHECKS.json').read_text());ck('independent186 gate',g['status']=='PASS'and g['count']==186 and all(c['passed']for c in g['checks']));ck('gate proof',g['proof_sha256']==sha(R/'PROOF.md'));ck('gate driver',g['driver_sha256']==sha('independent_code/audit_hydrostatic_function_space.py'));ck('gate inputs',g['input_sha256']==sha(V/'INPUTS.json'))
for p,h in g['code_sha256'].items():ck('module '+p,sha(Path('independent_code')/p)==h)
for item in json.loads((V/'INPUTS.json').read_text())['files']:ck('source '+Path(item['path']).name,sha(item['path'])==item['sha256'])
for c,suffix in [(2,'c2'),(3,'c3_hsG')]:
 text=(V/f'producer_hs_cauchy_{suffix}.txt').read_text().split('scale of',1)[0];printed=[]
 for line in text.splitlines():
  m=re.match(r'^\d+x\d+\s*->\s*\d+x\d+\s+(.*)$',line)
  if m:printed.append(re.findall(r'[+-]?\d+\.\d+e[+-]\d+',m[1]))
 pairs=[r for r in g['pairs']if r['c']==c];ck('printed pair count'+str(c),len(printed)==len(pairs))
 for pair,tokens in zip(pairs,printed):
  label=pair['old']+'->'+pair['new'];ck(label+' fifteen tokens',len(tokens)==15);k=0
  for region in ['inner','subunit','annulus','far','outer']:
   for key in ['field','pointwise_relative','gradient']:
    tok=tokens[k];k+=1;mant,exponent=tok.lower().split('e');decimals=len(mant.split('.')[1]);halfunit=.5*10**(int(exponent)-decimals);val=pair['from_intended_radius_masks'][region][key]['value'];ck(label+' published rounding '+region+' '+key,abs(val-float(tok))<=halfunit,dict(printed=tok,independent=val,half_last_unit=halfunit))
  with np.load(V/(pair['old']+'_independent.npz'),allow_pickle=False)as f:a=f['jet'].copy();X=f['X'].copy();Y=f['Y'].copy()
  with np.load(V/(pair['new']+'_independent.npz'),allow_pickle=False)as f:b=f['jet'].copy();ck(label+' stored coordinates',np.array_equal(X,f['X'])and np.array_equal(Y,f['Y']))
  rad=np.hypot(X,Y);dh=np.abs(a[:,0]-b[:,0]);dg=np.linalg.norm(a[:,1:3]-b[:,1:3],axis=1)
  for region,row in pair['from_export_coordinates'].items():
   for key,nu,de in [('field',dh,(1+rad)**(1/c)),('gradient',dg,(1+rad)**(1/c-1)),('pointwise_relative',dh,np.abs(b[:,0]))]:
    q=row[key];j=q['index'];ck(label+' witness '+region+' '+key,q['x']==X[j]and q['y']==Y[j]and abs(q['numerator']-nu[j])<1e-12*(1+abs(nu[j]))and abs(q['denominator']-de[j])<1e-12*(1+abs(de[j]))and abs(q['value']-nu[j]/de[j])<1e-12*(1+abs(q['value'])))
summary=[]
for p in g['pairs']:
 data=p['from_intended_radius_masks'];summary.append(dict(old=p['old'],new=p['new'],c=p['c'],nominal={region:{k:v[k]['value']for k in ['field','gradient','sum_norm','pointwise_relative']}for region,v in data.items()},independent_grid={region:{k:v[k]['value']for k in ['field','gradient','sum_norm','pointwise_relative']}for region,v in p['independent_grid'].items()},last_gradient_fraction_by_region={region:v['gradient']['value']/v['gradient_scale']for region,v in data.items()},coordinate_boundary_gradient_annulus=p['from_export_coordinates']['annulus']['gradient']['value']))
c2=[p for p in summary if p['c']==2];c3=[p for p in summary if p['c']==3]
for key in ['field','gradient','sum_norm','pointwise_relative']:
 for region in ['annulus','far','outer']:ck('c2 decreasing finite differences '+region+' '+key,all(a['nominal'][region][key]>b['nominal'][region][key]for a,b in zip(c2,c2[1:])))
ck('c3 last annulus gradient remains large',c3[-1]['nominal']['annulus']['gradient']>.3);ck('c3 outer gradient remains large',c3[-1]['nominal']['outer']['gradient']>.7)
ratios={key:[b['nominal']['annulus'][key]/a['nominal']['annulus'][key]for a,b in zip(c2,c2[1:])]for key in ['field','gradient','sum_norm','pointwise_relative']}
out=dict(status='PASS'if all(x['passed']for x in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,summary=summary,c2_annulus_reduction_ratios=ratios,proof_sha256=sha(R/'COMPARISON_PROOF.md'),main_gate_sha256=sha(V/'CHECKS.json'),driver_sha256=sha(__file__))
(V/'COMPARISON.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count']);print([c for c in checks if not c['passed']]);print(ratios);raise SystemExit(out['status']!='PASS')

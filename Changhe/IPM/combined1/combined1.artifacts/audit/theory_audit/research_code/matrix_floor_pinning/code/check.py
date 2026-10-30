from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from hashlib import sha256
import json,time
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[1]
H=lambda p:sha256(p.read_bytes()).hexdigest()
def ar(q):return arb(q.numerator)/q.denominator
start=time.monotonic();ctx.prec=512
points=json.loads((BASE/'data/point_caps.json').read_text());points={r['name']:r for r in points['rows']}
rates=json.loads((BASE/'data/gram_rates.json').read_text())
audit=json.loads((BASE/'source/audit.json').read_text());assert audit['all_pass'] and all(r['pass'] for r in audit['checks'])
rows=[]
for kind,pname,low in [('B1','B4',Q(972875,10**6)),('B2','B5',Q(293619,500000)),('B3','B6',Q(-307719,250000))]:
 p=BASE/'source'/f'{kind}_global.json';r=BASE/'source'/f'{kind}_global.recheck.json'
 a=json.loads(p.read_text());b=json.loads(r.read_text())
 assert a['kind']==b['kind']==kind and Q(a['target'])==Q(b['target'])==low
 assert a['status']=='COMPLETE' and not a['failed'] and not a['pending_paths']
 assert b['all_pass'] and b['primary_sha256']==H(p) and len(a['accepted'])==b['leaves']
 assert a['source_sha256']==b['polynomials_sha256']==audit['polynomials_sha256']
 aa=next(x for x in audit['rows'] if x['kind']==kind)
 assert aa['primary_sha256']==H(p) and aa['recheck_sha256']==H(r) and Q(aa['target'])==low
 boxes=[];area=Q(0);paths=set()
 for row in a['accepted']:
  t0,t1=map(Q,row['t']);z0,z1=map(Q,row['z'])
  assert 0<=t0<t1<=1 and -1<=z0<z1<=1
  assert arb(row['lower_numerator_after_target'])>0
  boxes.append((t0,t1,z0,z1));area+=(t1-t0)*(z1-z0);paths.add(row['path'])
 assert area==2 and len(paths)==len(boxes)
 for i,x in enumerate(boxes):
  for y in boxes[i+1:]:assert min(x[1],y[1])<=max(x[0],y[0]) or min(x[3],y[3])<=max(x[2],y[2])
 assert {x['path'] for x in b['direct_restriction_rows']}==paths
 assert all(x['pass'] and arb(x['lower'])>0 for x in b['direct_restriction_rows'])
 cap=Q(points[pname]['strict_upper_cap']);assert arb(points[pname]['lambda_min'])<ar(cap)
 rows.append({'matrix':kind,'global_lower':str(low),'strict_upper_cap':str(cap),'width':str(cap-low),'leaves':len(boxes),'certificate_sha256':H(p),'recheck_sha256':H(r)})
ceilings=[]
for name,Cp,published in [('sharp',401,Q('0.000076219')),('sharpw',397,Q('0.00021035'))]:
 row=next(r for r in rates['floor_sensitivity'] if r['name']==name and r['floor']=='packet caps quoted')
 base=next(r for r in rates['floor_sensitivity'] if r['name']==name and r['floor']=='A2')
 mu=ar(Q(row['certificate']['nonpositive_upper']));mu0=ar(Q(base['certificate']['positive_lower']))
 eta=mu**2*mu.sqrt()/(10*arb(5*Cp).sqrt());eta0=mu0**2*mu0.sqrt()/(10*arb(5*Cp).sqrt())
 ratio=eta/ar(published);ratio0=eta/eta0
 cap=Q(11,5) if name=='sharp' else Q(181,100)
 assert ratio<ar(cap)
 ceilings.append({'weights':name,'mu_ceiling':mu.str(80),'eta_upper_expression':eta.str(80),'published_eta':str(published),'ratio_to_published':ratio.str(80),'ratio_to_optimized_baseline_Gram_lower':ratio0.str(80),'safe_ratio_ceiling':str(cap),'ratio_expression_exceeds_1_8':bool(ratio>arb(9)/5)})
 print(name,'eta upper',eta.str(25),'published ratio',ratio.str(25),'optimized ratio',ratio0.str(25),flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':H(BASE/'PROOF.md'),'code_sha256':H(Path(__file__)),'source_audit_sha256':H(BASE/'source/audit.json'),'source_audit_checks':len(audit['checks']),'point_data_sha256':H(BASE/'data/point_caps.json'),'gram_data_sha256':H(BASE/'data/gram_rates.json'),'matrix_intervals':rows,'threshold_ceilings':ceilings,'elapsed_seconds':time.monotonic()-start,'scope':'P96 global theorem inherited, certificate integrity and coverage checked; no full polynomial recomputation.'}
(BASE/'verification/results.json').write_text(json.dumps(out,indent=2)+'\n');print('all checks passed; seconds',out['elapsed_seconds'],flush=True)

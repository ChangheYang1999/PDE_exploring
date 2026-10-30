from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=768;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((B/'data/manifest.json').read_text());assert sha(B/'PROOF.md')==m['proof_sha256']
for k,h in m['inputs'].items():assert sha(B/k)==h,k
p=json.loads((B/'source/peer_result.json').read_text());o=json.loads((B/'source/original_result.json').read_text())
assert p['inputs']['PROOF']==sha(B/'source/original_PROOF.md') and p['inputs']['result']==sha(B/'source/original_result.json')
assert p['deps']['t4_375_review_results_sha256']==sha(B/'source/peer_375_result.json')
assert p['deps']['t4_410_review_results_sha256']==sha(B/'source/peer_410_result.json')
assert len(p['A'])==7 and all(p['A'].values());checks=7;numeric=0
C=lambda x:arb(Q(str(x)).numerator)/Q(str(x)).denominator
def parse(s):
 v,e=s.strip('[]').split('+/-');return arb(v.strip(),e.strip())
c=Q(4076476460239181,2251799813685248);q=1/c-4;d=1-1/c;D=5*c-1;al=-2*q-2;S=2*d*d/(al*(al+d)*(al+2*d));pi=arb.pi()
betas={'sharpw_rounded_ceiling':Q(28496,10**10),'TB_sharp_rounded_ceiling':Q(3793,10**9),'original_graded_ceiling':Q(25,54684),'fixed_sharpw_ball':Q(1351,1024000000)}
Elow=(-q-1)/(2*(-q)*(-q-3));assert C(Elow)>C(p['B']['E_lower_lower']);checks+=1
rows=[]
for row in o['rows']:
 n=row['candidate'];pr=p['B'][n];assert all(pr['checks'].values());numeric+=len(pr['checks'])
 bound=parse(row['B']);Phi=parse(row['H_point']);H=C(row['H0_integer']);g=C(row['g0_exact']);v0=C(row['v0_exact'])
 assert Phi.overlaps(parse(pr['Phi'])) and bound.overlaps(parse(pr['B']));checks+=2
 versions={}
 for vl,v in [('V_zero',C(0)),('V_lead',v0)]:
  rr=pr['versions'][vl];assert all(rr['checks'].values());numeric+=len(rr['checks'])
  orig=row['versions'][vl]
  assert parse(orig['radius'])>C(rr['r0_lower']) and parse(orig['cap'])<C(rr['cap_upper']) and parse(orig['crude_cap'])<C(rr['crude_cap_upper']);checks+=3
  th={}
  for key,beta in betas.items():
   a=rr['thresholds'][key];crit=C(D)*bound/((2*pi).sqrt()*Phi*g)*(bound*C(S).sqrt()/C(beta))**C(d/(-q-1))-v/g
   crude=C(D)*bound/((2*pi).sqrt()*Phi*g)*(bound/(C(beta)*C(al).sqrt()))**C(d/(-q-1))-v/g
   assert parse(orig['thresholds'][key]['retained_shape'])<C(a['retained_upper_H0']);assert parse(orig['thresholds'][key]['crude_cutoff'])<C(a['crude_upper_H0']);checks+=2
   assert crit<C(a['retained_upper_Phi']) and crude<C(a['crude_upper_Phi']) and crude<C(Elow);checks+=3
   for e in ['583/1000','93/250']:assert crit-C(e)<C(a[f'room_{e}_upper']);checks+=1
   if vl=='V_zero':assert C(a['T4-410 J/H lower'])/crit>C(a['J/H over retained threshold, lower']);checks+=1
   th[key]={'retained_Phi':crit.str(40),'room_0.372':(crit-C('93/250')).str(40)}
  versions[vl]=th
 rows.append({'candidate':n,'versions':versions})
assert numeric==204
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'precision_bits':ctx.prec,'own_checks':checks,'peer_numeric_checks':numeric,'rows':rows,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'foreign_code_executed':False,'verdict':'CONFIRMED full414 theorem and arithmetic, now independently AUDITED; radius-dependent extension handled separately'}
(B/'verification/result.json').write_text(json.dumps(r,indent=2)+'\n');print('PASS',checks,numeric,r['utc'],r['elapsed_s'])

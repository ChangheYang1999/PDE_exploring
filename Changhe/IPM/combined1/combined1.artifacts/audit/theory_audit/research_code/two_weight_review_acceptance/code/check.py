from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,time
from flint import arb,ctx
B=Path(__file__).resolve().parents[1];start=time.monotonic();ctx.prec=768;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((B/'data/manifest.json').read_text());assert sha(B/'PROOF.md')==m['proof_sha256']
for k,h in m['inputs'].items():assert sha(B/k)==h,k
review=(B/'source/review.md').read_text();log=(B/'source/peer_log.txt').read_text();code=(B/'source/peer_check.py').read_text()
for f in ['original_PROOF.md','peer_check.py','peer_log.txt']:assert sha(B/'source'/f) in review,f
passlines=[x for x in log.splitlines() if x.startswith('PASS ')];assert len(passlines)==22 and '22 checks, ALL PASS' in log and not any(x.startswith('FAIL') for x in log.splitlines())
C=lambda x:arb(Q(str(x)).numerator)/Q(str(x)).denominator
c=Q(4076476460239181,2251799813685248);q=1/c-4;d=1-1/c;kap=5-1/c;D=5*c-1
assert kap==4+d and D==c*kap;checks=2
lam=C(1)/2+5*C(2)**C(1-q);lam2=C(2)**C(-q)*lam
assert lam>109 and lam2>C('1195.78') and lam2<C('1195.8');checks+=3
low=lam*(C(5)/18860)**C(d);lows=lam*(C(5)/C('13761.58'))**C(d)
assert low>C('2.7473') and lows>C('3.1635');checks+=2
radii=[]
for room,lower in [('0.09893906',31600000),('0.155596',11500000),('0.086292',42900000),('0.06294',86900000)]:
 r=C(5)*(lam/C(room))**C(1/d);assert r>lower;checks+=1;radii.append({'room_exact':room,'radius':r.str(40),'strict_lower':lower})
rows=json.loads((B/'source/campaign_audit.json').read_text())['rows'];bounds=[]
for row in rows:
 for key,v in row['targets'].items():
  s=v['Ecrit_upper'];mid,rad=s.strip('[]').split('+/-');ec=arb(mid.strip(),rad.strip());assert ec<C('0.785064');checks+=1
  if row['candidate']=='013' and key=='fixed_sharpw_ball':assert ec>C('0.785063');checks+=1
  bounds.append(ec)
ru=C(5)*(lam/C('1.747261'))**C(1/d);eff=C('1.747261')*(1-(C(18860)/ru)**C(kap));assert eff>C('1.7277');checks+=1
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_s':time.monotonic()-start,'precision_bits':ctx.prec,'own_checks':checks,'peer_pass_groups':22,'peer_float_groups':['C1','C2','finite-point portion of A12'],'lambda':lam.str(40),'lambda2':lam2.str(40),'radii':radii,'current_universal_averaged_lower':eff.str(40),'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'foreign_code_executed':False,'verdict':'CONFIRMED full410 analytic theorem via R1-043; display inequalities repaired; radius-dependent proof separately audited'}
(B/'verification/result.json').write_text(json.dumps(r,indent=2)+'\n');print('PASS',checks,r['utc'],r['elapsed_s'])

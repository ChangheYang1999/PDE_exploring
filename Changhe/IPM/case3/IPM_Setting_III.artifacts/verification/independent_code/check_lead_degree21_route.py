"""Result288: own pairwise inner determinants and modular gcd certificates."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,traceback,resource
from math import gcd
from exact_degree21 import *
from modular_gcd_certificate_285 import certify
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3))
R=Path('research/lead_degree21_resultant_route_audit');V=R/'verification';D=Path('research/degree21_grouped_moment_obstruction/verification');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat();checks=[];jobs=[];rows=[];start=utc()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def save(status):
 out=dict(status=status,started_utc=start,updated_utc=utc(),count=len(checks),checks=checks,jobs=jobs,cases=rows,proof_sha256=sha(R/'PROOF.md'),review_proof_sha256=sha(R/'REVIEW_RESOLUTION_PROOF.md'),scope='Reconstruction and gcd arithmetic only until OUTER_CHECKS passes.',driver_sha256=sha(__file__),library_sha256=sha('independent_code/exact_degree21.py'),coefficient_sha256=sha(V/'COEFFICIENTS.json'),parent_reconstruction_sha256=sha(D/'RECONSTRUCTION.json'),parent_outer_sha256=sha(D/'OUTER_CHECKS.json'),parent_branches_sha256=sha(D/'BRANCH_CHECKS.json'),gcd_module_sha256=sha('independent_code/modular_gcd_certificate_285.py'))
 (V/'RECONSTRUCTION.json').write_text(json.dumps(out,indent=2)+'\n')
def strip(p,allowed):
 removed=[]
 for f in allowed:
  f=prim(f);power=0
  while p:
   q,r=divmod(p,f)
   if r:break
   ck('exact allowed factor removal',q*f==p);p=q;power+=1
  if power:removed.append(dict(polynomial=encode(f),exponent=power))
 return prim(p),removed
save('RUNNING')
try:
 ck('raw resultant manufacture',resultant(2*(y-1),3*(y-2),1)==-6)
 for factor in [h,h-21,h-x,(h-21)*x-(h-17)*h,(h-21)*x-(h-19)*h]:
  quotient,removed=strip(factor**3*(x*x+2*h*h+3),[factor]);ck('factor stripping manufacture',quotient==prim(x*x+2*h*h+3) and len(removed)==1 and removed[0]['exponent']==3)
 rec=json.loads((D/'RECONSTRUCTION.json').read_text());outer=json.loads((D/'OUTER_CHECKS.json').read_text());branches=json.loads((D/'BRANCH_CHECKS.json').read_text())
 for label,d in [('parent reconstruction',rec),('parent outer',outer),('parent branches',branches)]:ck(label+' PASS',d['status']=='PASS'and all(c['passed']for c in d['checks']))
 ck('parent library',rec['library_sha256']==sha('independent_code/exact_degree21.py'));data=json.loads((V/'COEFFICIENTS.json').read_text());ck('data gate',data['status']=='PASS'and all(c['passed']for c in data['checks']));ck('decoder binding',data['driver_sha256']==sha('independent_code/decode_lead_degree21_coefficients.py'))
 for filename,digest in data['source_sha256'].items():ck('source '+filename,sha(V/filename)==digest)
 for index,kind in [(13,'V'),(11,'VI')]:
  source=json.loads((D/'external'/f'certificate_{index:02d}.json').read_text());r=source['certificate']['regular'];pol=[prim(decode(r[k]))for k in ['N0','F1','F2']];ck(kind+' moment degrees',[degree(p,1)for p in pol]==([2,2,3]if kind=='V'else[3,4,4]));pairs=[];row=dict(kind=kind,source_sha256=sha(D/'external'/f'certificate_{index:02d}.json'),inner=[])
  for i,j in [(0,1),(0,2),(1,2)]:
   matrix=sylv(pol[i],pol[j],1);raw,divs,swaps=bareiss(matrix)
   if kind=='VI':p,removed=strip(raw,[h,h-21,h-x,(h-21)*x-(h-17)*h,(h-21)*x-(h-19)*h])
   else:p=prim(raw);removed=[]
   ck(kind+f' nonzero inner {i}{j}',bool(p) and degree(p,1)<=0);pairs.append(p);row['inner'].append(dict(pair=[i,j],polynomial=encode(p),raw_integer_content=str(raw.content()),removed=removed,divisions=divs,swaps=swaps));print('INNER',kind,i,j,tuple(map(int,p.degrees())),utc(),flush=True)
  if kind=='V':
   H,J=[decode(data['typeV'][k])for k in ['H','J']];core=prim(divexact(decode(r['common_resultant']),(h-21)**12));ck('V same90core',core==decode(data['typeV']['core']));target=prim((h-21)**106*core);ck('V core shift positive',all(c>0 for c in shifted(univ(core),23)));ck('V degrees316370',[degree(H,2),degree(J,2)]==[316,370]);new=[(pairs[0],pairs[1],H,'V pairwise H'),(pairs[0],pairs[2],J,'V pairwise J')]
  else:
   parent=next(j for j in rec['jobs']if j['name']=='11 VI outer H');ck('VI first input matches285',pairs[0]==decode(parent['f']));ck('VI second input matches285',pairs[1]==decode(parent['g']));H=decode(parent['resultant']);J=decode(data['typeVI']['J']);core=prim(decode(r['common_resultant']));target=prim(h**182*(h-21)**120*core);ck('VI core shift positive',all(c>0 for c in shifted(univ(core),23)));ck('VI degrees9461222',[degree(H,2),degree(J,2)]==[946,1222]);new=[(pairs[0],pairs[2],J,'VI pairwise J')]
  cert=certify(H,J,target)
  for key in ['exact_divisions_verified','identity_verified','leading_degrees_preserved']:ck(kind+' gcd '+key,cert[key])
  row['gcd_certificate']=cert;row['gcd']=encode(target);row['core_degree']=degree(core,2);rows.append(row)
  for f,g,target,name in new:jobs.append(dict(name=name,var=0,f=encode(f),g=encode(g),resultant=encode(target)))
  save('RUNNING')
 # Integer contents under the explicit raw-Sylvester convention.
 source=json.loads((D/'external/certificate_11.json').read_text())
 for branch in source['certificate']['zero_branches']:
  zero=branch['zero_weight'];expected,exponent={4:(128,4),2:(50176,8)}[zero];pol=[prim(decode(z))for z in branch['equations']];rr=[resultant(pol[0],pol[k],1)for k in [1,2]];content=gcd(int(rr[0].content()),int(rr[1].content()));ck('VI zero'+str(zero)+' raw gcd content',content==expected,content)
  goal=prim((h-21)**exponent);cert=certify(prim(rr[0]),prim(rr[1]),goal);ck('VI zero'+str(zero)+' primitive gcd',cert['identity_verified']and cert['exact_divisions_verified']and cert['leading_degrees_preserved']);rows.append(dict(zero_weight=zero,gcd_content=content,gcd=encode(goal)))
 ck('three new outer identities',len(jobs)==3);save('PASS_PENDING_OUTER');print('PASS_PENDING_OUTER',len(checks),utc(),flush=True)
except Exception:
 save('FAIL');(V/'reconstruction_traceback.txt').write_text(traceback.format_exc());raise

from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json
r=Path('research/stationarity_inference_audit');v=r/'verification';checks=[];bindings={}
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p);d=sha(p);ck('binding '+str(p),h is None or d==h);bindings[str(p)]=d
for name,count,status in [('CHECKS.json',34,'PASS_EXACT_LOGICAL_COUNTEREXAMPLE'),('ACCEPTANCE_CHECKS.json',28,'PASS_EXACT_ACCEPTANCE_COUNTEREXAMPLE')]:
 p=v/name;bind(p);a=json.loads(p.read_text());ck('complete '+name,a['count']==count==len(a['checks'])and a['status']==status and all(z['passed']for z in a['checks']))
 for p,h in a['bindings'].items():bind(p,h)
e=F(77,10000);K=8192;q=e*e/(1+e*e);alpha=F(1,10000)
ck('strict projection coefficient gap',0<q<alpha<1)
ck('positive supporting hyperplane coefficients',alpha-q>0 and K*q>0)
for k in range(16):
 l=F(1,2**k);u=-e*l;a=(e+u)**2+(1+K*u*u)**2;z=a-e*e-1
 ck('exact polynomial rederivation '+str(k),z==e*e*l*(-2+(1+2*K)*l)+K*K*e**4*l**4)
 ck('exact sign '+str(k),z>0 if k<=13 else z<0)
 ck('Cauchy support '+str(k),(e*(e+u)+1+K*u*u)/(1+e*e)==1-q*l+K*q*l*l)
 ck('all sample strict fixed-rule rejection '+str(k),a>(1+e*e)*(1-alpha*l)**2)
# Concrete disproof of the withdrawn half-slope lower bound.
l=F(1,16);h2=1-2*q*l+q*l*l
ck('false half-slope bound disproved exactly',h2<(1-q*l/2)**2)
ck('correct supporting bound',h2>=(1-q*l)**2)
reviews=[]
for name in ['opus_design','opus_followup']:
 p=v/name;m=json.loads((p/'metadata.json').read_text());a=json.loads((p/'response.json').read_text());ck('actual model '+name,m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']==a['model']=='claude-opus-5-5');ck('completed review '+name,m['stop_reason']==a['stop_reason']=='end_turn'and m['answer_nonempty']);bind(p/'request.txt',m['request_sha256']);ck('response text '+name,'\n\n'.join(z.get('text','')for z in a['content']if z['type']=='text').strip()==(p/'answer.md').read_text().strip())
 for f in ['metadata.json','response.json','answer.md']:bind(p/f)
 reviews.append(m)
for p in [Path(__file__),'independent_code/opus_review_308.py',r/'REVIEW_RESOLUTION_PROOF.md',r/'FINAL_REVIEW_RESOLUTION.md',r/'CLOSURE_PROOF.md',r/'RESULTS.md']:bind(p)
ck('scope explicit',all(s in(r/'RESULTS.md').read_text()for s in ['CONFIRMED','REFUTED','OPEN','UNRESOLVED','at least as strict as plain decrease']))
for p,h in list(bindings.items()):ck('stable '+p,sha(p)==h)
out=dict(status='PASS_LOGICAL_COUNTEREXAMPLE_AND_ACCEPTANCE_LEMMA',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,reviews=reviews,scope='Refutes the inference, not an independently evaluated producer gradient. Actual mechanism OPEN. Primary full-plane IPM UNRESOLVED.')
(v/'FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks),out['utc'])

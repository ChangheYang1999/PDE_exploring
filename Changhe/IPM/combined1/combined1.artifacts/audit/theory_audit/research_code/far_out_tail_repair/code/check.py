"""Exact campaign specialization of the analytic scaling theorem."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,time
B=Path(__file__).resolve().parents[1]; start=time.monotonic()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
c=Q(4076476460239181,2251799813685248);gamma=1/c;delta=1-gamma
q=4*gamma-5;e9=1-9*delta;cross=q+gamma-1;quad=2*q-1
assert -3<q<-1 and quad<cross<e9<-3
exponents={'L2':q+1,'mixed_residual':q+gamma,'quadratic_residual':2*q,
           'graded_hessian':q+Q(6,5),'sharp_hessian':q+Q(3,5)}
assert all(e<0 for e in exponents.values())
rows=[]
for name in ['007','013','014']:
 p=B/f'data/{name}_tail_repair.json';data=json.loads(p.read_text());mom=data['moment_checks']
 assert len(mom)==40 and all(Q(x['A1']) for x in mom)
 rows.append({'candidate':name,'source_sha256':sha(p),'nonzero_potential_modes':40,
              'exact_A1_values':{str(x['m']):x['A1'] for x in mom}})
out={'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':sha(B/'PROOF.md'),
     'code_sha256':sha(Path(__file__)),'q_exact':str(q),'first_remaining_exponent':str(e9),
     'mixed_tail_exponent':str(cross),'quadratic_tail_exponent':str(quad),
     'norm_scaling_exponents':{k:str(v) for k,v in exponents.items()},'all_scaling_exponents_negative':True,
     'rows':rows,'elapsed_seconds':time.monotonic()-start,
     'status':'Exact campaign specialization passes; analytic theorem OPEN independent Opus review.'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))

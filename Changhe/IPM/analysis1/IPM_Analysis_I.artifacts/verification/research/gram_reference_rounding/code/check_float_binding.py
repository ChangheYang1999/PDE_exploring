from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import ast,hashlib,json
B=Path(__file__).resolve().parents[3];D=B/'research/gram_reference_rounding'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def check(v,s):
 if not v:raise ValueError(s)
def hx(s):
 a,e=s.split('p');sign=-1 if a.startswith('-') else 1;a=a.lstrip('+-')[2:];p,q=a.split('.');return sign*Q(int(p+q,16),16**len(q))*Q(2)**int(e)
def rn(q):
 if q==0:return q
 sign=-1 if q<0 else 1;q=abs(q);e=q.numerator.bit_length()-q.denominator.bit_length()
 if q<Q(2)**e:e-=1
 check(-1022<=e<=1023,'normal finite result');s=q*Q(2)**(52-e);n,r=divmod(s.numerator,s.denominator)
 if 2*r>s.denominator or (2*r==s.denominator and n%2):n+=1
 return sign*Q(n)*Q(2)**(e-52)
a=json.loads((D/'evidence/compute.json').read_text());tree=ast.parse((D/'sources/c2_gram2.py').read_text());v=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='STEP_COEF' for t in n.targets));c=ast.literal_eval(v.value);check(all(x==int(x) for x in c),'integer seed coefficients');c=list(map(int,c));checks=0
for r in a['records']:
 w=rn(hx(r['b_hex'])-hx(r['a_hex']));check(w==hx(r['w_hex']),'rounded subtraction')
 for j,cc in enumerate(c):
  power=rn(w**j);q=rn(Q(cc)/power);check(q==hx(r['coefficients_hex'][j]),'exact nearest-even coefficient '+r['name']+str(j));checks+=1
pins={str(p.relative_to(B)):sha(p) for p in [D/'evidence/compute.json',D/'sources/c2_gram2.py',D/'REVIEW_RESOLUTIONS.md',Path(__file__)]}
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_RATIONAL_POWERS_AND_NEAREST_EVEN_SOURCE_COEFFICIENT_REPRODUCTION','rounded_coefficients_checked':checks,'rounded_widths_checked':3,'files':pins,'scope':'Independent exact-rational reproduction of these locally returned floating coefficients. No historical/future source execution claim.'}
with (D/'evidence/float_binding.json').open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
print(out['utc'],out['status'],checks)

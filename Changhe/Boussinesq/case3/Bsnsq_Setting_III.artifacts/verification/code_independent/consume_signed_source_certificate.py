"""Separate certificate consumer. No import of the certificate producer."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
v=Path('research/238_signed_source_axis_equilibria/verification')
c=json.loads((v/'certificate.json').read_text());checks=[]
def add(n,p):checks.append({'name':n,'pass':bool(p)})
def bounds(z):
 a,b=F(z['lower']),F(z['upper']);add('ordered rational enclosure',a<=b);return a,b
for k,r in enumerate(c['intervals']):
 l,rgt=bounds(r['phi_left']),bounds(r['phi_right']);d=bounds(r['phi_prime_over_bracket']);h=bounds(r['horizontal_eigenvalue'])
 add('endpoint signs '+str(k),l[1]<0<rgt[0] if k==0 else rgt[1]<0<l[0])
 add('derivative strict bounds '+str(k),2<d[0]<=d[1]<3 if k==0 else -4<d[0]<=d[1]<-2)
 add('trace six '+str(k),h==(6-d[1],6-d[0]))
 add('horizontal positive '+str(k),h[0]>0)
 lo,hi=(F('2.31431'),F('2.31500')) if k==0 else (F('-3.06298'),F('-3.00549'))
 add('outward rounded printed enclosure '+str(k),lo<=d[0]<=d[1]<=hi)
add('proof provenance',hashlib.sha256((v/'PROOF_before_status_closure.md').read_bytes()).hexdigest()==c['proof_sha256'])
add('input provenance',hashlib.sha256((v/'input.json').read_bytes()).hexdigest()==c['input_sha256'])
add('producer provenance',hashlib.sha256(Path('code_independent/certify_signed_source_equilibria.py').read_bytes()).hexdigest()==c['code_sha256'])
add('positive normalization',bounds(c['normalization_A'])[0]>0)
out={'checked_utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'all_passed':all(q['pass'] for q in checks),'certificate_sha256':hashlib.sha256((v/'certificate.json').read_bytes()).hexdigest(),'limitation':'Reparses exact stored bounds and provenance; does not independently regenerate exponential enclosures.'}
(v/'certificate_consumer.json').write_text(json.dumps(out,indent=2)+'\n')
print(sum(q['pass'] for q in checks),len(checks),out['checked_utc'])
assert out['all_passed']

from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
TOP=Path(__file__).resolve().parents[1];LANE=TOP.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
prior=LANE/'proofs/181_scalar_radius_necessary_test/evidence/check.json'
data=json.loads(prior.read_text())
assert data['verdict']=='PASS'
k=F(data['k']);S=F(data['S_upper']);B=F(data['universal_N4_upper'])
assert k==F(1615536043799051,9007199254740992)
coefficient=F(4,3)-1/(1-k)
assert coefficient>0 and B==3/k-12+S*coefficient
assert 0<B<F(181,20)
theta=1/B-k/3;middle=F(20,181)-k/3;coarse=F(50,453)-k/3
assert theta>middle>F(507,10000)
assert F(5058,100000)<coarse<F(506,10000)
out={'date':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED','k_exact':str(k),'N4_upper_exact':str(B),
     'relative_threshold_lower_exact':str(theta),'reported_safe_threshold':'507/10000',
     'threshold_decimal_for_orientation':float(theta),'coarser_threshold_exact':str(coarse),
     'coarse_is_less_than_00506':True,'arithmetic':'exact rational',
     'scope':'Conditional necessary test; no actual relative norm upper bound and no nonexistence conclusion',
     'proof_sha256':sha(TOP/'PROOF.md'),'code_sha256':sha(Path(__file__)),
     'scalar_certificate_sha256':sha(prior),'scalar_proof_sha256':sha(LANE/'proofs/181_scalar_radius_necessary_test/PROOF.md')}
(TOP/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

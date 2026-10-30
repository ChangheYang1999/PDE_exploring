from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,time
P=Path(__file__).resolve().parents[1]; start=time.monotonic()
c=Q(4076476460239181,2251799813685248); g=1/c; d=1-g; q=4*g-5; qs=g-4; q2=1-9*d
exponents={'q':q,'q+2':q+2,'q+1':q+1,'qstar':qs,'q2':q2,'q-2':q-2,'q+gamma-3':q+g-3,'2q-3':2*q-3,'gap_q2_to_next':q2-(q+g-1)}
assert -3<q<-2 and qs<q2<-3
assert all(x<qs for x in [q-2,q+g-3,2*q-3])
assert q2-(q+g-1)==2-4*d>0
for s in [Q(1,100),Q(1,2),Q(1)]:assert q+1+s<0
files={str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted((P/'source').iterdir())}
assert files['source/t4_314_review.py']=='9e6f7b8cf51d07b2e99c3e4a33eb9bab4fc020bb49b2be503b227c928bc79bd4'
assert files['source/t4_314_review_results.json']=='adeb26ae64ad2accb2d340248393971a8e95dccf27279a9e8019e84ffe2d498a'
out={'completed_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':files,'exponents':{k:str(v) for k,v in exponents.items()},'all_checks':True,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED exact specialization; analytic proof in PROOF.md; peer quadrature remains FLOAT'}
(P/'verification/result.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

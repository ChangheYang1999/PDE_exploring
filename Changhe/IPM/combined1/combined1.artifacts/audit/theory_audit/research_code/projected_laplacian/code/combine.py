from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as Q
import json,time
from flint import arb,ctx
start=time.monotonic();ctx.prec=1024
base=Path(__file__).resolve().parents[1]
def ar(x):return arb(x.numerator)/x.denominator
files={n:base/f'verification/candidate007_mode{n}.json' for n in range(1,16,2)}
data={n:json.loads(p.read_text()) for n,p in files.items()}
for n,d in data.items():assert d['angular_modes']==[n]
norms={n:{Q(r['a']):arb(r['projected_norm']) for r in d['rows']} for n,d in data.items()}
c=Q(4076476460239181,2251799813685248);A=1+1/c
rows=[]
for a in norms[1]:
 n2=(norms[1][a]**2+norms[3][a]**2).sqrt()
 n8=sum((norms[n][a]**2 for n in norms),arb(0)).sqrt()
 rows.append({'a':str(a),'modes_1_3_norm':n2.str(85),'modes_1_to_15_norm':n8.str(85)})
cells=[]
for l,h,eval_h in [(Q(4,5),Q(1),Q(1)),(Q(1),Q(5,4),Q(5,4)),(Q(5,4),Q(3,2),Q(3,2)),(Q(3,2),A,Q(7,4))]:
 n=(norms[1][eval_h]**2+norms[3][eval_h]**2).sqrt()
 lower=arb(5)**ar((l-2)/2)*n;upper=(8*arb.pi()).sqrt()*ar((1+c-c*l)**2/(1+l));ratio=lower/upper
 assert ratio>1
 cells.append({'left':str(l),'right':str(h),'norm_evaluation_at':str(eval_h),'lower':lower.str(85),'upper':upper.str(85),'ratio':ratio.str(85),'passed':True})
out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'candidate':'C1-N1-007-d2w-j7-e2bal','inputs':{str(p.relative_to(base)):sha256(p.read_bytes()).hexdigest() for p in files.values()},'proof_sha256':sha256((base/'COVER.md').read_bytes()).hexdigest(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows,'cells':cells,'all_passed':True,'elapsed_seconds':time.monotonic()-start,'status':'New numerical values pending independent reproduction'}
p=base/'verification/combined_cover.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
for r in cells:print(r['left'],r['right'],'ratio',r['ratio'])

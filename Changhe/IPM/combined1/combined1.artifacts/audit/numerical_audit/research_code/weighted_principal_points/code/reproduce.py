"""Independent rational axis evaluation of weighted principal witnesses."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import sys,json,time
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from radial import Radial,q,ar
ctx.prec=1024;start=time.monotonic()
src=ROOT/'research/baseline/data/state131_independent.json'
target=ROOT/'research/weighted_principal_points/peer_data/T4_points.json'
model=Radial(src);peer=json.loads(target.read_text());assert str(model.c)==peer['c']
rows=[]
for row in peer['rows']:
 a,R=q(row['a']),q(row['R']);x,y=map(q,row['point']);assert y==0
 v=model.evaluate(str(x),str(y));assert v['rho_x'].is_zero() and v['u2'].is_zero()
 b=ar(a)*(ar(model.c*x*x)+ar(x)*v['u1'])/ar(R*R+x*x)
 theta=(abs(v['rho_y'])-v['rho_y'])/2;lam=b+theta;gap=lam-ar(model.c+1)
 values={'rho_y':v['rho_y'],'U1':v['u1'],'weight_drift':b,'theta_X':theta,'lambda':lam,'excess_over_c_plus_one':gap}
 checks={k:v.overlaps(arb(row[k])) for k,v in values.items()};assert all(checks.values()) and gap>0
 rows.append({'a':str(a),'R':str(R),'point':row['point'],**{k:v.str(80) for k,v in values.items()},'overlaps':checks,'strict_positive_gap':True})
 print(a,R,x,gap.str(30),flush=True)
def sha(p):return sha256(p.read_bytes()).hexdigest()
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':'state131','precision_bits':ctx.prec,
 'source_sha256':sha(src),'peer_sha256':sha(target),'code_sha256':sha(Path(__file__)),
 'proof_sha256':sha(ROOT/'research/weighted_principal_points/PROOF.md'),'rows':rows,'elapsed_seconds':time.monotonic()-start}
(ROOT/'research/weighted_principal_points/verification/state131_1024.json').write_text(json.dumps(out,indent=2)+'\n')
print('elapsed_seconds',out['elapsed_seconds'],flush=True)

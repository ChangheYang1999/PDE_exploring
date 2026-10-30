from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import time
from flint import arb, ctx
base=Path(__file__).resolve().parents[1]
ctx.prec=512
start=time.monotonic()
s=arb(1)/131072
radius=arb(1)/16384
nu=radius/s.sqrt()
As=arb(127)/50+arb(653)/5*s
Bs=arb(9)/5*(1+44*s)
m1=arb(9)/10-4290*s-arb(13)/10*nu
q=6+1360*s
alpha=m1-s*q
m2=arb(1)/2-4708*s-(As+Bs)*nu
u1=arb(347)/5+5440*s+Bs*nu
v1=10+34816*s
k1=u1+s*v1
G1=(arb(1)/128+q/256)/alpha
G0=arb(1)/256+s*G1
G2=(1+k1*G1+v1/256)/m2+(40/m2).sqrt()*G1
KX=(G2*G2+16384*G1*G1+262144*G0*G0).sqrt()
cs=1/(4*arb.pi()*s*(1+s)).sqrt()
contraction=2*cs*radius
assert alpha>arb('0.83849') and m2>arb('0.36814')
assert KX<arb('11.490384') and KX<12
assert contraction<arb('0.012467')
assert cs*radius<arb('0.006234')
keys=('nu','As','Bs','m1','q','alpha','m2','u1','v1','k1','G1','G0','G2','KX','cs','contraction')
values=locals().copy()
out={'utc':datetime.now(timezone.utc).isoformat(), 'precision_bits':ctx.prec,
     's':'1/131072','radius':'1/16384','eta':'1/196608',
     'low_semigroup_hypothesis':{'M':'2','beta':'1'},
     'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'proof_sha256':sha256((base/'PROOF.md').read_bytes()).hexdigest(),
     'values':{key:values[key].str(90) for key in keys},
     'all_assertions_pass':True,'elapsed_seconds':time.monotonic()-start}
(base/'verification/constants_512.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

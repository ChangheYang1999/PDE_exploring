from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,time
from flint import arb,ctx
start=time.monotonic();ctx.prec=1024
base=Path(__file__).resolve().parents[1]
def load(p):return json.loads((base/p).read_text())
def digest(p):return sha256((base/p).read_bytes()).hexdigest()
def aq(s):
 q=Q(s);return arb(q.numerator)/q.denominator
own=load('data/own_point.json');peer=load('source/N4_result.json')
assert own['canonical_sha256']==peer['canonical_sha256']
f={k:arb(v) for k,v in own['fields'].items()}
c=aq(Q(4076476460239181,2251799813685248));x,y=map(aq,own['point'])
V=((c*x+f['u1'])**2+(c*y+f['u2'])**2).sqrt()
D=(f['rho_x']**2+f['rho_y']**2).sqrt();F=abs(f['residual'])
assert V.overlaps(f['velocity_norm']) and D.overlaps(f['gradient_norm'])
n=aq(Q(50,651))/arb(28248).sqrt();nu=aq(Q(25,217))
assert Q(1,2)-14124*Q(1,28248)==0
b0=n/(4*arb.pi()).sqrt();b1=nu/(8*arb.pi()).sqrt()
upper=b1*V+b0*(1+D)+b0*b1;gap=F-upper
assert gap>aq('0.0858095924457140')
values={'n_uniform_upper':n,'nu_uniform_upper':nu,'C0n_uniform_upper':b0,'C1n_uniform_upper':b1,'uniform_point_upper':upper,'uniform_positive_gap':gap}
assert upper.overlaps(arb(peer['uniform_graded_upper']))
assert gap.overlaps(arb(peer['uniform_graded_gap']))
cases=[('FW-T-T4L2-sharp-v1',Q(1,7744),aq(Q(147,200000))),('FW-T-T4L2-sharpw-v1',Q(1,5184),aq(Q(1351,1000000))),('FW-T-TB-graded-v1-box-i',Q(5,262144),(aq('0.0002022')**2+2*aq('0.0000003347')**2+aq('0.00000001899')**2).sqrt()),('FW-T-TB-graded-v1-box-ii',Q(1,50000),(aq(Q(1,5000))**2+2*aq(Q(1,3000000))**2+aq(Q(1,50000000))**2).sqrt()),('FW-T-TB-gradedL2-v1-instance',Q(5,262144),(aq('0.0002023')**2+2*aq('0.000000332')**2+aq('0.0000000184')**2).sqrt())]
rows=[]
for label,s,nr in cases:
 C0=1/(4*arb.pi()*aq(1+s)).sqrt();C1=1/(8*arb.pi()*aq(s*(1+s))).sqrt()
 bound=nr*(C1*V+C0*(1+D))+nr**2*C0*C1;gg=F-bound
 assert gg>0
 target=next((v for v in peer['sharp_boxes'] if v['framework']==label),None)
 if target is not None:
  assert nr.overlaps(aq(target['radius'])) and bound.overlaps(arb(target['point_upper'])) and gg.overlaps(arb(target['gap']))
 rows.append({'framework':label,'s':str(s),'radius':nr.str(95),'upper':bound.str(95),'gap':gg.str(95)})
out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'inputs':{p:digest(p) for p in ['PROOF.md','code/check.py','data/own_point.json','source/N4_result.json']},'all_8_available_peer_comparisons_agree':True,'uniform_values':{k:v.str(95) for k,v in values.items()},'finite_boxes':rows,'elapsed_seconds':time.monotonic()-start}
p=base/'verification/results.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print('uniform gap',gap.str(45));print('all8available peer comparisons agree; seconds',out['elapsed_seconds'])

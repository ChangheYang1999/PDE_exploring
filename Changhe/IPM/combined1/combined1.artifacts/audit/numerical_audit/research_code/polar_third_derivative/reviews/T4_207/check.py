"""Independent symbolic identity and complete retained Q3 record audit."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json,sys,time
import sympy as s
from fractions import Fraction as Q
from flint import arb,ctx
sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parents[1];source=base/'source'
start=time.monotonic();ctx.prec=2048
hashof=lambda p:sha256(p.read_bytes()).hexdigest()
snapshot=json.loads((source/'SNAPSHOT_MANIFEST.json').read_text())
for name,rec in snapshot['files'].items():assert hashof(source/name)==rec['sha256']
r,n=s.symbols('r n',nonzero=True,real=True);h=s.symbols('h0:4',real=True)
def dr(e):return s.diff(e,r)+sum(s.diff(e,h[j])*h[j+1] for j in range(3))
def raising(e,m):return s.expand(dr(e)-m*e/r)
ap=raising(raising(raising(h[0],n),n+1),n+2)
am=raising(raising(raising(h[0],-n),-n+1),-n+2)
j=h[2]+h[1]/r-n*n*h[0]/r**2
bp,bm=raising(j,n),raising(j,-n)
a=h[3];b=n*(h[2]/r-2*h[1]/r**2+2*h[0]/r**3)
c=h[2]/r-(1+n*n)*h[1]/r**2+2*n*n*h[0]/r**3
d=3*n*h[1]/r**2-n*(n*n+2)*h[0]/r**3
identity=s.expand(ap*ap+am*am+3*bp*bp+3*bm*bm-8*(a*a+3*b*b+3*c*c+d*d))
assert identity==0
# The exact polynomial connection identities hold for arbitrary d and P.
t,power=s.symbols('t d',real=True);coeff=s.symbols('p0:7');p=sum(coeff[k]*t**k for k in range(7))
def td(f,d):return (1-2*d*t)*f+2*t*(1-t)*s.diff(f,t)
tp=td(p,power);aa=-2*power*tp+2*(1-t)*s.diff(tp,t)
bb=n*(-2*power*p+2*(1-t)*s.diff(p,t));cc=(tp-n*n*p)/t
assert s.cancel(td(bb,power+1)-n*aa+2*bb)==0
assert s.cancel(td(cc,power+1)-aa+cc+n*bb)==0
# Degree112 weight, independent exact coefficient construction.
w=[Q(1)]
for k in range(1,114):
 value=Q(1)
 for j in range(k):value*= (Q(4,5)-j)*Q(-3,4)/(j+1)
 w.append(value)
assert all(v<0 for v in w[1:]);epsilon=4*abs(w[113])
assert all(abs(w[k+1]/w[k])<Q(3,4) for k in range(1,113))
full=json.loads((source/'N4_full.json').read_text());manifest=json.loads((source/'N4_manifest.json').read_text())
assert full['complete'] and not full['missing_modes']
assert full['manifest_sha256']==hashof(source/'N4_manifest.json')
assert full['code_sha256']==hashof(source/'N4_check.py')
assert full['completed_modes']==manifest['modes']==list(range(1,320,2))
assert manifest['components']==1360 and manifest['weight_degree']==112
can=json.loads((source/'canonical007.json').read_text());peer=json.loads((source/'N3_norms.json').read_text())
entries={tuple(k):Q(v) for k,v in zip(can['order'],can['coefficients']) if Q(v)}
serial='\n'.join(','.join(map(str,k))+':'+str(v) for k,v in sorted(entries.items()))+'\n'
semantic=sha256(serial.encode()).hexdigest()
assert semantic==can['canonical_serialization_sha256']==peer['canonical_sha256']
assert can['source_sha256']==peer['source_sha256']
assert hashof(source/'N3_code.py')==peer['code_sha256']
cl=Q(can['cl']);delta=1-1/cl
assert cl==Q(peer['cl'])==Q(4076476460239181,2251799813685248)
lo=arb(0);hi=arb(0);identities=0;endpoint_count=0
for k in manifest['modes']:
 path=source/f'modes/mode_{k:03d}.json';rec=json.loads(path.read_text())
 assert hashof(path)==full['mode_sha256'][str(k)]
 assert rec['mode']==k and rec['manifest_sha256']==full['manifest_sha256']
 for e in rec['endpoints']:
  assert Q(e['diagonal_exponent'])==e['ell']*delta+2*e['q']-Q(4,5)>-1
  endpoint_count+=1
 l,u=arb(rec['energy_lower_ball']),arb(rec['energy_upper_ball'])
 assert l>0 and u>l and min(l.rel_accuracy_bits(),u.rel_accuracy_bits())>150
 assert l.sqrt().overlaps(arb(rec['norm_lower_ball'])) and u.sqrt().overlaps(arb(rec['norm_upper_ball']))
 lo+=l;hi+=u;identities+=rec['symmetry_identities']
lo=lo.sqrt();hi=hi.sqrt()
assert identities==full['symmetry_identities']==2720
assert lo.overlaps(arb(full['norm_lower_ball'])) and hi.overlaps(arb(full['norm_upper_ball']))
other=peer['norms']['Q3'];pl,pu=arb(other['norm_lower_ball']),arb(other['norm_upper_ball'])
assert other['status']=='FINITE' and pl<pu and lo<pu and hi>pl
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'symbolic_complex_tensor_identity':True,'symbolic_degree6_connection_identities':True,'weight_degree':112,'weight_epsilon':str(epsilon),'modes':len(manifest['modes']),'symmetry_identities':identities,'exact_endpoint_checks':endpoint_count,'canonical_semantic_sha256':semantic,'source_sha256':can['source_sha256'],'norm_lower_ball':lo.str(90),'norm_upper_ball':hi.str(90),'N3_overlap':True,'proof_sha256':hashof(base/'PROOF.md'),'code_sha256':hashof(Path(__file__)),'snapshot_manifest_sha256':hashof(source/'SNAPSHOT_MANIFEST.json'),'scope':'General method and complete retained record CONFIRMED; full field arithmetic paths are N3 and N4, not regenerated here.'}
with (base/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k!='weight_epsilon'},indent=2))

from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict
import hashlib, importlib.util, json, time, sys
from flint import fmpq as Q, arb, arb_poly, ctx
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('t4_high',ROOT.parent/'high_power_weak_probe/code/check.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
f=h.f
ctx.prec=2048;sys.set_int_max_str_digits(0);start=time.monotonic()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
peer=json.loads((ROOT/'source/N4_result.json').read_text())
own_path=ROOT.parent/'high_power_weak_probe/verification/013_n21_k522.json'
own=json.loads(own_path.read_text())
source=ROOT.parent/'new_successor_weak/data/013/canonical.json'
assert own['source_sha256']==sha(source)
build=json.loads((ROOT.parent/'new_successor_weak/verification/013_build.json').read_text())
assert build['source_sha256']==peer['generator_sha256']
c,delta,rho,stream=f.fields(json.loads(source.read_text()))
N,K=21,522;T=f.T
Qp=(2*K+1)-(2*K+4)*T;A0=(2*c+1)+c*Qp
Ds={(j,n):f.td(S,(j+1)*delta/2,2) for (j,n),S in stream.items()}
Dr={(j,n):f.td(R,(j+1)*delta/2,1) for (j,n),R in rho.items()}
U={};G={}
for (j,n),S in stream.items():
 for (k,m),V in stream.items():
  if n==m:U[j+k]=U.get(j+k,f.ZERO)+n*n*S*V+Ds[j,n]*Ds[k,m]
for (j,n),R in rho.items():
 for (k,m),V in rho.items():
  if n==m:G[j+k]=G.get(j+k,f.ZERO)+Dr[j,n]*Dr[k,m]+n*n*R*V
ints=lambda p,b:h.integ(h.ap(p),b,2*K)
aa=arb.pi()/2*ints(A0*A0,Q(1))
bb=arb.pi()/2*sum((ints(p*(Qp*Qp+N*N),1+(j+2)*delta/2) for j,p in U.items()),arb(0))
cc=arb.pi()/2*sum((ints(p,1+(j+2)*delta/2) for j,p in G.items()),arb(0))
assert all(z>0 and z.rel_accuracy_bits()>150 for z in (aa,bb,cc))
A,B,C=aa.sqrt(),bb.sqrt(),cc.sqrt();D=A+B+C
I=arb(own['pairing']);H=Q(max(2*K+1,3))*Q(4*K**K,(K+2)**(K+2))
assert H==Q(peer['H_upper_exact'])
radius=2*abs(I)/(D+(D*D+4*f.ar(H)*abs(I)).sqrt())
vals={'pairing':I,'A':A,'B_upper':B,'C_upper':C,'D_upper':D,'L2_radius_lower':radius}
checks={k:z.overlaps(arb(peer[k])) for k,z in vals.items()}
assert all(checks.values()),checks
floor=Q(peer['strict_lower_exact']);assert f.ar(floor)<radius
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,
     'precision_bits':ctx.prec,'all_enclosures_overlap':checks,'exact_H_match':True,
     'strict_floor':str(floor),'source_raw_sha256':peer['generator_sha256'],
     'own_pairing_sha256':sha(own_path),'source_sha256':sha(source),
     'peer_result_sha256':sha(ROOT/'source/N4_result.json'),'proof_sha256':sha(ROOT/'PROOF.md'),
     'code_sha256':sha(__file__),'values':{k:z.str(100) for k,z in vals.items()},
     'status':'CONFIRMED N4-200 from independent polar assembly'}
(ROOT/'verification/result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['utc','elapsed_seconds','all_enclosures_overlap','strict_floor','status']},indent=2),flush=True)

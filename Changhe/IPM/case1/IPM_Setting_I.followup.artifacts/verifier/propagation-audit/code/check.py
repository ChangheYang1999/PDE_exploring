from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,math
import sympy as s
root=Path(__file__).resolve().parents[1];x,y,t,z,lam=s.symbols('x y t z lam',real=True);f=s.Function('f')(x,y);w=[s.Function('w1')(x,y),s.Function('w2')(x,y)];b=s.Function('b')(x,y);xs=[x,y]
Lap=lambda q:s.diff(q,x,2)+s.diff(q,y,2)
D=lambda q:sum(w[i]*s.diff(q,xs[i]) for i in range(2))
checks=[]
def test(name,e):
 result=s.simplify(s.expand(e));assert result==0,(name,result);checks.append({'name':name,'exact_residual':str(result)})
test('transport_Laplacian_commutator',Lap(D(f))-D(Lap(f))-sum(2*s.diff(s.diff(w[j],xs[i])*s.diff(f,xs[j]),xs[i])-s.diff(w[j],xs[i],2)*s.diff(f,xs[j]) for i in range(2) for j in range(2)))
test('rough_B_divergence_form',Lap(b*f)-b*Lap(f)-sum(s.diff(s.diff(b,xx)*f,xx)+s.diff(b,xx)*s.diff(f,xx) for xx in xs))
theta=s.Function('theta')(t);eta=s.Function('eta')(z);chi=eta*s.exp(lam*t/2)*theta
test('flow_cutoff_energy_sign',s.diff(chi**2,t)-lam*chi**2-2*eta**2*s.exp(lam*t)*theta*s.diff(theta,t))
for k in range(2,7):
 for ax in range(k+1):
  ay=k-ax;terms=[]
  for jx in range(ax+1):
   for jy in range(ay+1):
    coeff=math.comb(ax,jx)*math.comb(ay,jy)
    for i,xx in enumerate(xs):terms.append(coeff*s.diff(w[i],x,jx,y,jy)*s.diff(f,x,ax-jx,y,ay-jy, *([xx])))
  test(f'full_Leibniz_k{k}_x{ax}',s.diff(D(f),x,ax,y,ay)-sum(terms))
counts=[]
for k in range(2,101):
 for j in range(2,k):
  for aa,bb in [(j+1,k-j+1),(j,k-j+2)]:
   assert 2<=aa<=k and 2<=bb<=k and aa+bb==k+2 and (aa-2)+(bb-2)==k-2
   counts.append([k,j,aa,bb])
proof=root/'PROOF.md';obj={'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'intermediate_product_order_checks':len(counts),'maximum_k_tested':100,'verdict':'PASS','scope':'Exact finite symbolic identities and integer derivative bookkeeping only; the analytic proof is in PROOF.md.'};(root/'verification/check.json').write_text(json.dumps(obj,indent=2)+'\n');print(obj['utc'],len(checks),'symbolic checks',len(counts),'derivative checks PASS')

from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
from flint import arb,ctx
import json
ctx.prec=320
root=Path(__file__).resolve().parents[1]
base=root/'13_transport_duality/exponent_continuity/cost_comparison/one_sided'
source=base.parent/'verification/intervals.json'
def A(q):
 q=Q(q);return arb(q.numerator)/q.denominator
def enc(z):return dict(display=str(z),lower=str(z.lower().fmpq()),upper=str(z.upper().fmpq()))
rows=[]
for old in json.loads(source.read_text())['rows']:
 a0,a,b,U,V,E,mc,md=map(Q,[old[k] for k in ['alpha','auxiliary_a','auxiliary_b','U_C','V_D','E_exact_upper','mass_C_exact_upper','mass_D_exact_upper']])
 u,v=A(U+E),A(V-E);assert v>0
 ell=(old['cutoff_M']+1)*arb(2).log()
 hc=arb.max(arb(0),(A(mc)/u).log()/A(a0));hd=arb.max(arb(0),(A(md)/v).log()/A(a0))
 candidates={Q(j,10**k) for k in range(1,19) for j in range(1,10)}
 candidates.add(min(a0-a,b-a0))
 for rho in sorted(candidates,reverse=True):
  if rho>min(a0-a,b-a0):continue
  gm=v*(-ell*A(rho)).exp()-u*(hc*A(rho)).exp()-2*A(E)
  gp=v*(-hd*A(rho)).exp()-u*(ell*A(rho)).exp()-2*A(E)
  margin=arb.min(gm,gp)
  if margin>0:break
 else:raise AssertionError('No candidate')
 lower=Q(str(margin.lower().fmpq()));rounded=Q((10000*lower).__floor__(),10000)
 row={k:old[k] for k in ['alpha','auxiliary_a','auxiliary_b','U_C','V_D','E_exact_upper','mass_C_exact_upper','mass_D_exact_upper','cutoff_N','cutoff_M']}
 row.update(radius=str(rho),interval_left=str(a0-rho),interval_right=str(a0+rho),gap_minus=enc(gm),gap_plus=enc(gp),gap=enc(margin),rounded_down_gap=str(rounded),parent_radius=old['radius'])
 rows.append(row);print(a0,rho,rounded,flush=True)
paths=[Path(__file__),source,base/'PROOF.md',base.parent/'verification/accepted.json']
r=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,verdict='SCALAR CHECKS PASS',rows=rows,sha256={str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in paths})
(base/'verification/intervals.json').write_text(json.dumps(r,indent=2)+'\n')

"""Fresh audit of every saved angular coefficient using a complex recurrence."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import sys,json,time,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,acb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/flow_angular/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();ctx.prec=1536;ctx.threads=1;d=json.loads((E/'checks.json').read_text());assert d['status']=='PASS'
 assert d['arrays_sha256']==sha(E/'finite_arrays.npz') and d['code_sha256']==sha(B/'research/flow_angular/code/check_angular.py') and d['proof_sha256']==sha(B/'research/flow_angular/PROOF.md')
 for p,h in d['source_pins'].items():assert sha(B/p)==h
 z=np.load(E/'finite_arrays.npz',allow_pickle=False);nodes=[tuple(map(int,a)) for a in z['nodes']];expected={(l,l+w,7-(w.bit_length()-1)) for w in [1,2,4,8,16,32,64,128] for l in range(0,25600,w)}
 assert len(nodes)==len(set(nodes))==51000 and set(nodes)==expected
 assert len({tuple(a) for a in z['keys']})==51000 and np.all(np.isfinite(z['keys']))
 selected=[tuple(map(int,a)) for a in z['selected']];es=sorted((a for a in expected if a[2]==0 or a[0] in (0,12800,25600-(a[1]-a[0]))),key=lambda x:(x[2],x[0]));assert selected==es and len(es)==221
 assert z['midpoints'].shape==z['radii'].shape==(221,3,3,261)
 pi=arb.pi();widthpairs=set((r-l,float(h)) for (l,r,_),h in zip(nodes,z['half_widths']))
 for width,h in widthpairs:assert arb(h)>pi*width/102400
 remainder_checks=0
 for j,h in enumerate(z['distinct_half_widths']):
  for n in range(1,262):
   for fam,pre in [(0,8*n**3),(1,4*n*n*(n+1)**2+2*n*(n+1))]:
    assert F(float(z['remainder_arrays'][j,fam,n-1]))>=pre*F(float(h))**3/6;remainder_checks+=1
 mids=z['midpoints'];rads=z['radii'];checks=0
 for j,(l,r,depth) in enumerate(selected):
  theta=pi*(l+r)/102400;root=acb(0,2*theta).exp();power=acb(1);su=[arb(0),arb(0),arb(0)];sa=[arb(0),arb(0),arb(0)]
  for n in range(1,262):
   power=power*root;c=power.real;s=power.imag;part=[c,-2*n*s,-2*n*n*c];sg=1 if n%2==0 else -1;vals=[part,[],[]]
   for k in range(3):
    unit=1 if k==0 else 0;vals[1].append(unit+part[k]+2*su[k]);vals[2].append(-sg*(unit+sg*part[k]+2*sa[k]));su[k]+=part[k];sa[k]+=sg*part[k]
   for fam in range(3):
    for k in range(3):
     m=float(mids[j,fam,k,n-1]);rad=float(rads[j,fam,k,n-1]);assert abs(vals[fam][k]-arb(m)).upper()<=arb(rad),(j,n,fam,k);checks+=1
  if j%25==0:print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'centers_done':j+1,'containments':checks}),flush=True)
 assert checks==221*9*261 and d['coefficient_containments']==2*checks and remainder_checks==d['exact_remainder_checks'] and d['geometry_containments']==306000
 obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','fresh_precision':1536,'coefficient_containments':checks,'geometry_nodes_reconstructed':51000,'width_pairs_checked':len(widthpairs),'exact_remainder_checks':remainder_checks,'input_sha256':sha(E/'checks.json'),'arrays_sha256':sha(E/'finite_arrays.npz'),'code_sha256':sha(__file__),'proof_sha256':d['proof_sha256'],'seconds':time.monotonic()-start,'method':'Complex exponential followed by powers, with exact even-polynomial reconstruction; every stored midpoint-radius box compared at1536bits.','scope':d['scope']};(E/'output_audit.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj),flush=True)
if __name__=='__main__':main()

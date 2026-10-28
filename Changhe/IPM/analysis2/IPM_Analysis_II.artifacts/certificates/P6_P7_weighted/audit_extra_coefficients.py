"""Reconstruct exact polynomials, audit every certificate leaf, compare Cartesian jets."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, hashlib, time
from flint import arb, ctx
import extra_coefficients as ec
import sharp_coefficients as sc
from sharp_coefficients import A
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(sc.BASE/'source_audit'))
import field_eval as fe
fe.ORDER=7; fe.INDICES=[(i,j) for i in range(8) for j in range(8-i)]
ctx.prec=384; start=time.monotonic()
pfile=HERE/'extra_coefficient_polynomials.json'; raw=json.loads(pfile.read_text())
dfile=HERE/'extra_coefficient_certificate.json'; d=json.loads(dfile.read_text())
assert d['status']=='COMPLETE' and not d['failed'] and not d['pending']
s,delta,P,kinds=ec.construct()
saved={(k.rsplit('_',1)[0],int(k.rsplit('_',1)[1])):{(i,j):Q(v) for i,j,v in vals} for k,vals in raw['polynomials'].items()}
assert saved==P and kinds==raw['kinds'] and delta==Q(raw['delta'])
assert raw['source_sha256']==d['source_sha256']==s['canonical_serialization_sha256']
assert {k:Q(v) for k,v in d['targets'].items()}==ec.TARGETS
B=sc.make_blocks(P,d['nt'],d['nz']); Lt,Rt=sc.cc.split_matrices(d['nt']); Lz,Rz=sc.cc.split_matrices(d['nz'])
paths={v['path']:v for v in d['accepted']}; assert len(paths)==len(d['accepted'])
maxima={k:arb(0) for k in ec.TARGETS}; count=0
print('exact reconstruction PASS',time.monotonic()-start,flush=True)
def visit(path,b,tl,th,zl,zh):
 global count
 if path in paths:
  row=paths[path]; assert list(map(Q,row['t']))==[tl,th] and list(map(Q,row['z']))==[zl,zh]
  assert not any(p!=path and p.startswith(path) for p in paths)
  vals=ec.bound(b,tl,th,zl,zh,delta,kinds)
  for k,tar in ec.TARGETS.items():
   assert vals[k].is_finite() and vals[k]<=A(tar),(path,k,vals[k],tar)
   maxima[k]=maxima[k].max(vals[k])
  count+=1
  if count%100==0: print('leaves',count,'seconds',time.monotonic()-start,flush=True)
  return
 kids={p[len(path)] for p in paths if p.startswith(path)}; assert kids in ({'t','T'},{'z','Z'})
 axis='t' if kids=={'t','T'} else 'z'; left,right=sc.cc.split(b,axis,Lt if axis=='t' else Lz,Rt if axis=='t' else Rz)
 if axis=='t':
  m=(tl+th)/2; visit(path+'t',left,tl,m,zl,zh); visit(path+'T',right,m,th,zl,zh)
 else:
  m=(zl+zh)/2; visit(path+'z',left,tl,th,zl,m); visit(path+'Z',right,tl,th,m,zh)
visit('',B,Q(0),Q(1),Q(-1),Q(1)); assert count==len(paths)
pot=fe.State(131,384); points=[]
for xs,ys in [('0','1/10'),('1','0'),('1/2','1/2'),('1','2'),('3','1'),('60','80'),('0','1000')]:
 qx,qy=Q(xs),Q(ys); qq=qx*qx+qy*qy
 x,y=A(qx),A(qy); q=A(qq); t=A(qq/(1+qq)); z=A((qx*qx-qy*qy)/qq); w=(1-t)**(A(delta)/2)
 angular={'sin':y/q.sqrt(),'cos':x/q.sqrt(),'sin2':2*x*y/q,'one':arb(1)}
 vals={}
 for label,kind in kinds.items():
  val=sum((w**(j+1)*sum((A(v)*t**i*z**k for (i,k),v in P[label,j].items()),arb(0)) for j in range(4)),arb(0))*angular[kind]
  val*=t.sqrt()*(1-t)**A(Q(3,2)) if label.startswith('r4') else 1-t
  vals[label]=val
 jet=pot.evaluate(x,y,include_potential_jet=True)['potential_derivatives']; direct={}
 for i in range(5): direct[f'r4_{i}']=-jet[i+2,5-i]-jet[i,7-i]
 for i in range(4): direct[f'u3_0_{i}']=-jet[i+1,5-i]; direct[f'u3_1_{i}']=jet[i+2,4-i]
 checks={k:vals[k].is_finite() and v.is_finite() and vals[k].overlaps(v) for k,v in direct.items()}
 assert all(checks.values()),(xs,ys,[(k,vals[k],direct[k]) for k,v in checks.items() if not v])
 points.append({'point':[xs,ys],'checks':checks}); print('Cartesian',xs,ys,'PASS',flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'verdict':'CONFIRMED','source_sha256':s['canonical_serialization_sha256'],'certificate_sha256':hashlib.sha256(dfile.read_bytes()).hexdigest(),'polynomial_sha256':hashlib.sha256(pfile.read_bytes()).hexdigest(),'precision_bits':ctx.prec,'leaves':count,'targets':d['targets'],'maxima':{k:v.str(55) for k,v in maxima.items()},'points':points,'elapsed_seconds':time.monotonic()-start}
(HERE/'extra_coefficient_audit.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2),flush=True)

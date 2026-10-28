"""Recompute every matrix-certificate leaf and compare independent Cartesian values."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,sys,time
from flint import arb,ctx
import certify_matrix as cm
from compact_matrix import evaluate,A
from point_fields import Potential
HERE=Path(__file__).resolve().parent

def run(name):
 ctx.prec=384;start=time.monotonic()
 s=json.loads((HERE/f'{name}_audit.json').read_text())
 d=json.loads((HERE/f'{name}_matrix_certificate.json').read_text())
 raw=json.loads((HERE/f'{name}_matrix_polynomials.json').read_text())
 assert d['status']=='COMPLETE' and not d['failed'] and not d['pending']
 assert d['source_sha256']==raw['source_sha256']==s['source_sha256']
 assert d['canonical_sha256']==raw['canonical_sha256']==s['canonical_sha256']
 assert Q(d['target'])==Q(19,5)
 delta,P=cm.construct(s)
 saved={(key.rsplit('_',1)[0],int(key.rsplit('_',1)[1])):{(i,j):Q(v) for i,j,v in val} for key,val in raw['polynomials'].items()}
 assert saved==P and Q(raw['delta'])==delta
 paths={x['path']:x for x in d['accepted']};assert len(paths)==len(d['accepted'])
 B=cm.initial(P,d['nt'],d['nz']);Lt,Rt=cm.split_matrices(d['nt']);Lz,Rz=cm.split_matrices(d['nz'])
 lows=[];base=2*A(s['cl'])+1
 def visit(path,b,tl,th,zl,zh):
  if path in paths:
   row=paths[path];assert list(map(Q,row['t']))==[tl,th] and list(map(Q,row['z']))==[zl,zh]
   assert not any(p!=path and p.startswith(path) for p in paths)
   low,_=cm.bounds(b,tl,th,zl,zh,delta,base,True)
   assert low>=A(Q(19,5)) and arb(row['lower'])>=A(Q(19,5))
   lows.append(low)
   if len(lows)%200==0:print(name,'audited leaves',len(lows),'seconds',time.monotonic()-start,flush=True)
   return 1
  kids={p[len(path)] for p in paths if p.startswith(path)}
  assert kids in ({'t','T'},{'z','Z'})
  axis='t' if kids=={'t','T'} else 'z'
  left,right=cm.split(b,axis,Lt if axis=='t' else Lz,Rt if axis=='t' else Rz)
  if axis=='t':
   mid=(tl+th)/2
   return visit(path+'t',left,tl,mid,zl,zh)+visit(path+'T',right,mid,th,zl,zh)
  mid=(zl+zh)/2
  return visit(path+'z',left,tl,th,zl,mid)+visit(path+'Z',right,tl,th,mid,zh)
 n=visit('',B,Q(0),Q(1),Q(-1),Q(1));assert n==len(paths)
 worst=lows[0]
 for low in lows:worst=worst.min(low)
 origin={}
 for label in ('chi22','chi04','chi31'):
  co={}
  for j in range(4):
   for (i,k),v in P[label,j].items():
    if i==0:co[k]=co.get(k,Q(0))+v
  co={k:v for k,v in co.items() if v};assert all(k==0 for k in co)
  origin[label]=co.get(0,Q(0))
 assert origin['chi22']==1-Q(s['cl']) and origin['chi31']==0
 points=[];pot=Potential(s)
 for xs,ys in [('0','1/10'),('1/2','1/2'),('1','2'),('3','1'),('0','10'),('60','80'),('0','1000')]:
  qx,qy=Q(xs),Q(ys);qq=qx*qx+qy*qy
  x,y=A(qx),A(qy);t=A(qq/(1+qq));z=A((qx*qx-qy*qy)/qq)
  f=evaluate(P,delta,t,z);cart=pot.fields(xs,ys)
  aa=base-2*f['chi22']-f['chi04'];bb=base+f['chi22'];cc=f['chi31']
  mm=(aa+bb-((aa-bb)**2+4*cc**2).sqrt())/2
  assert mm.is_finite() and cart['M_min'].is_finite()
  assert mm.overlaps(cart['M_min'])
  assert all(v.is_finite() for v in f.values())
  assert f['chi22'].overlaps(cart['strain_DU22'])
  assert (-f['chi22']-f['chi04']).overlaps(cart['rho_y'])
  points.append({'x':xs,'y':ys,'M_min':mm.str(50),'Cartesian_comparison':'PASS'})
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'verdict':'CONFIRMED','name':name,'source_sha256':s['source_sha256'],'canonical_sha256':s['canonical_sha256'],'certificate_sha256':hashlib.sha256((HERE/f'{name}_matrix_certificate.json').read_bytes()).hexdigest(),'precision_bits':ctx.prec,'leaf_count':n,'minimum_recomputed':worst.str(55),'coverage':'complete exact binary partition','origin_strain':str(origin['chi22']),'points':points,'elapsed_seconds':time.monotonic()-start}
 (HERE/f'{name}_matrix_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':run(sys.argv[1])

"""Independent finite quotient grids and scalar MP checks of two frozen iterates."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
import argparse, json, hashlib, math
import numpy as np
import mpmath as mp
from q_checkpoint_reader import QCheckpoint
from q_high_precision_density import MPQDensity

ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('--tag',required=True);args=ap.parse_args()
q=QCheckpoint(args.snapshot);out=Path('evidence/low_slope_quotient')/args.tag;out.mkdir(parents=True,exist_ok=True)
proof=Path('research/low_slope_state_audit/PROOF.md')
a=sum((F(float(v))*(-1)**k for k,v in enumerate(q.coeff[0])),F(0));assert a
result=dict(started_utc=datetime.now(timezone.utc).isoformat(),source=args.snapshot,source_sha256=q.meta['sha256'],metadata=q.meta,a_exact=str(a),a=float(a),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),rows=[])
sets=[('producer_declared_set',np.exp(np.linspace(np.log(1e-4),np.log(1e6),400)),(np.arange(128)+.5)*math.pi/256),('independent_offset_and_axes',10**np.unique(np.r_[np.linspace(-16.037,8.029,653),[-100.,-50.,-30.,-20.,20.,50.,100.,250.]]),np.unique(np.r_[0.,math.pi/2,(np.arange(257)+.3141592653589793)/257*math.pi/2,np.geomspace(1e-10,.01,17),math.pi/2-np.geomspace(1e-10,.01,17)]))]
points=[]
for label,r,theta in sets:
 t,s,w=q.coordinates(r)
 radial=np.stack([w*s**j*q.polynomial(j,t)/float(a) for j in range(q.M)],axis=1)
 angles=np.cos(2*np.arange(q.M)[:,None]*theta[None,:])
 values=radial@angles
 assert np.all(np.isfinite(values))
 extrema={}
 for name,func in [('max',np.argmax),('min',np.argmin)]:
  i,j=np.unravel_index(func(values),values.shape);th=float(theta[j]);radius=float(r[i]);x=0. if th==math.pi/2 else radius*math.cos(th);y=0. if th==0 else radius*math.sin(th)
  extrema[name]=dict(q=float(values[i,j]),r=radius,theta=th,x=x,y=y,radial_index=int(i),angular_index=int(j));points.append((x,y))
 row=dict(label=label,radii=len(r),angles=len(theta),points=values.size,radius_range=[float(r[0]),float(r[-1])],angle_range=[float(theta[0]),float(theta[-1])],extrema=extrema,count_above_one=int(np.count_nonzero(values>1)),count_below_zero=int(np.count_nonzero(values<0)))
 result['rows'].append(row);print(json.dumps(row),flush=True)
points=list(dict.fromkeys(points));result['MP']=[]
for digits in (80,120):
 with mp.workdps(digits):
  den=mp.mpf(a.numerator)/a.denominator;m=MPQDensity(q.coeff,q.L,q.kappa,q.cl);row=dict(digits=digits,points=[])
  for x,y in points:
   xx,yy=mp.mpf(x),mp.mpf(y);r=mp.sqrt(xx*xx+yy*yy);theta=mp.atan2(yy,xx);s,w=m.coords(r);t=2*s-1 if s<mp.mpf('.5') else 1-2*w
   val=w/den*mp.fsum(s**j*m.clenshaw(cc,t)[0]*mp.cos(2*j*theta) for j,cc in enumerate(m.coeff))
   row['points'].append(dict(x=x,y=y,q=mp.nstr(val,digits-10)))
  result['MP'].append(row)
with mp.workdps(135):
 result['precision_differences']=[mp.nstr(abs(mp.mpf(a['q'])-mp.mpf(b['q']))/(1+abs(mp.mpf(b['q']))),30) for a,b in zip(result['MP'][0]['points'],result['MP'][1]['points'])]
result.update(status='COMPUTED',finished_utc=datetime.now(timezone.utc).isoformat(),scope='Two finite grids. Producer geometry only is repeated, evaluator is independent. MP checks at selected extrema are not interval bounds. q=1 at the origin; no sampled strict upper bound below 1 extends globally. A violation is a witness about this saved iterate, not a theorem about profiles.')
(out/'diagnostic.json').write_text(json.dumps(result,indent=2)+'\n');(out/'points.json').write_text(json.dumps(points,indent=2)+'\n')

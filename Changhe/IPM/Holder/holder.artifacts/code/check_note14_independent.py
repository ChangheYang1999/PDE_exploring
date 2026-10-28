"""Independent point and Cartesian-derivative diagnostics for the archived num code.
Run after the current single-threaded certificate queue finishes. These finite
checks are diagnostics; the complete mathematical method proof is separate.
"""
from pathlib import Path
import sys, json, random, hashlib
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'05_team_audit/note14_certificate/sources'
sys.path.insert(0,str(SRC))
import certify_note14 as C
from flint import arb,ctx
import mpmath as mp
ctx.prec=160;mp.mp.dps=80
rng=random.Random(202610280645)

def ab(v): return arb(mp.nstr(v,85))
def profile(x,y,a):
 r=mp.sqrt(x*x+y*y)
 if not r:return mp.mpf(0)
 D=x*x-y*y
 return (r**a+mp.sign(D)*(abs(D)/r)**a)/2

def derivatives(x,y,a):
 # Cartesian logarithmic differentiation, independent of the polar source.
 r2=x*x+y*y;r=mp.sqrt(r2);D=x*x-y*y
 v=mp.matrix([x,y]);d=mp.matrix([2*x,-2*y]);I=mp.eye(2)
 H_D=mp.matrix([[2,0],[0,-2]])
 A=r**a;B=mp.sign(D)*abs(D)**a*r**(-a)
 L=a*(d/D-v/r2)
 H_L=a*(H_D/D-(d*d.T)/(D*D)-I/r2+2*(v*v.T)/(r2*r2))
 grad=(a*r**(a-2)*v+B*L)/2
 hess=(a*r**(a-2)*I+a*(a-2)*r**(a-4)*(v*v.T)+B*(H_L+L*L.T))/2
 return mp.sqrt(sum(t*t for t in grad)),mp.sqrt(sum(hess[i,j]**2 for i in range(2) for j in range(2)))

def seg(x,y,A,B,ray=False):
 vx,vy=B[0]-A[0],B[1]-A[1]
 t=((x-A[0])*vx+(y-A[1])*vy)/(vx*vx+vy*vy)
 t=max(mp.mpf(0),t) if ray else min(mp.mpf(1),max(mp.mpf(0),t))
 return mp.hypot(x-A[0]-t*vx,y-A[1]-t*vy)

def f_independent(x,y,a,b,c,lam):
 if x==mp.mpf('.5'):return mp.mpf(0)
 sign=1 if x>mp.mpf('.5') else -1
 if sign<0:x=1-x
 dists=[abs(x-mp.mpf('.5'))]
 for pole,direction in [(mp.mpf(1),1),(mp.mpf(0),-1)]:
  for s in [-1,1]:
   dists.append(seg(x,y,(pole,0),(mp.mpf('.5'),mp.mpf(s)/2)))
   end=(pole+direction*b,s*b)
   dists.append(seg(x,y,(pole,0),end))
   dists.append(seg(x,y,end,(end[0]+direction*mp.sqrt(3),end[1]+s),True))
 D=min(dists);w=x-1
 boundary=-w if w<=0 else w if w<=b else b+(w-b)/mp.sqrt(3)
 sigma=mp.sign(boundary-abs(y))
 g=2**(a-1)*sigma*D**a
 h=2**(a-1)*(x-mp.mpf('.5'))**a
 return sign*max(-h,min(h,g+c,-mp.mpf('.5')+lam*profile(x-1,y,a)))

rows=[]
for aq,lamq in [('1/2','1000/1021'),('3/4','50/53'),('9/10','10/11')]:
 an,ad=map(int,aq.split('/'));ln,ld=map(int,lamq.split('/'))
 a=mp.mpf(an)/ad;lam=mp.mpf(ln)/ld;b=mp.mpf(3)/4
 cq='-3/10' if aq=='3/4' else '-3/20';cn,cd=map(int,cq.split('/'));c=mp.mpf(cn)/cd
 C.setup(aq,'3/4',cq,lamq)
 points=0;derivative_points=0;balls=0;declined=0
 for i in range(500):
  scale=mp.mpf(2)**rng.randrange(-20,21)
  x=mp.mpf(rng.randrange(-1024,1025))/1024*scale
  y=mp.mpf(rng.randrange(-1024,1025))/1024*scale
  fi=f_independent(x,y,a,b,c,lam)
  fi_ball=C.witness(ab(x),ab(y),arb(0))['f']
  assert fi_ball.overlaps(ab(fi)),('witness',aq,i,mp.nstr(x),mp.nstr(y),str(fi_ball),mp.nstr(fi))
  pv=C.P_val(ab(x),ab(y));assert pv.overlaps(ab(profile(x,y,a))),('profile',aq,i)
  points+=1
 for i in range(180):
  scale=mp.mpf(2)**rng.randrange(-20,21)
  x=mp.mpf(rng.randrange(-1024,1025))/1024*scale
  y=mp.mpf(rng.randrange(-1024,1025))/1024*scale
  radius=scale*mp.mpf(rng.randrange(1,31))/1024
  bounds=C.P_bounds(ab(x),ab(y),ab(radius))
  if bounds is None:declined+=1;continue
  balls+=1
  for j in range(13):
   rho=radius if j else mp.mpf(0)
   theta=2*mp.pi*j/12
   xx=x+rho*mp.cos(theta);yy=y+rho*mp.sin(theta)
   grad,hess=derivatives(xx,yy,a)
   assert ab(grad)<bounds[0] or ab(grad).overlaps(bounds[0]),('gradient',aq,i,j)
   assert ab(hess)<bounds[1] or ab(hess).overlaps(bounds[1]),('Hessian',aq,i,j)
   derivative_points+=1
 rows.append(dict(alpha=aq,b='3/4',shift=cq,lambda_q=lamq,point_values=points,accepted_balls=balls,declined_balls=declined,derivative_points=derivative_points))
 print(rows[-1],flush=True)
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=160,independent_decimal_digits=80,checks=rows,source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in SRC.glob('*.py')},verdict='PASS: finite diagnostics only; full mathematical justification is PROOF.md')
(ROOT/'05_team_audit/note14_certificate/verification/independent_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')

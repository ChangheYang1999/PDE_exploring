"""Positive derivative-density lower certificate for the projection lattice witness."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import argparse,json,hashlib,time
from flint import arb,ctx
ctx.prec=192;A=arb(1)/2;RT3=arb(3).sqrt();PI=arb.pi();ROOT=Path(__file__).resolve().parents[1]
def aa(v):
 q=F(v);return arb(q.numerator)/q.denominator
def lo(v):return arb(v.lower())
def hi(v):return arb(v.upper())
def positive(v):return arb.max(arb(0),v)
def piece(X,Y,x0,y0,dx,dy,ray=False):
 t=((X-x0)*dx+(Y-y0)*dy)/(dx*dx+dy*dy);tc=positive(t) if ray else arb.min(arb(1),positive(t));rx=X-x0-tc*dx;ry=Y-y0-tc*dy
 if t>=0 and (ray or t<=1):dist=abs((X-x0)*dy-(Y-y0)*dx)/(dx*dx+dy*dy).sqrt()
 else:dist=(rx*rx+ry*ry).sqrt()
 return dist,ry
def density(d,v,sign,alpha,b,shift,K):
 X=positive(A+sign*d);Y=d*v;c=2**(alpha-1);h=c*X**alpha
 pieces=[(X,arb(0)),piece(X,Y,arb(0),A,A,-A),piece(X,Y,A,arb(0),b,b),piece(X,Y,A+b,b,RT3,arb(1),True)]
 dist=pieces[0][0]
 for q in pieces[1:]:dist=arb.min(dist,q[0])
 B=arb.max(A-X,arb.min(X-A,(X-A+(RT3-1)*b)/RT3));power=c*positive(dist)**alpha
 if Y<B:sg=1;g=power
 elif Y>B:sg=-1;g=-power
 else:sg=0;g=(-hi(power)).union(hi(power))
 r=(1+v*v).sqrt();E=(1-v*v)/r;P=d**alpha*positive((r**alpha+positive(E)**alpha-positive(-E)**alpha)/2)
 fg=g+shift;fp=-A+P/K
 if fp<fg:selected=fp;branch='profile'
 elif fg<fp:selected=fg;branch='distance'
 else:return arb(0),'minimum'
 if not (selected>-h and selected<h):return arb(0),'clamp'
 if branch=='profile':
  qmax=hi(abs(1-v*v));r2max=hi(1+v*v);bracket=lo(v*v+3)*qmax**(alpha-1)-r2max**alpha
  rate=d**(alpha-1)*alpha*lo(v)*r2max**((-alpha-2)/2)*positive(lo(bracket))/(2*K)
 else:
  if sg==0:return arb(0),'sign'
  chosen=None
  for i,(di,ry) in enumerate(pieces):
   if all(di<other[0] for j,other in enumerate(pieces) if j!=i):chosen=i;break
  if chosen is None:return arb(0),'nearest'
  if chosen==0:return arb(0),'axis'
  di,ry=pieces[chosen]
  if not di>0:return arb(0),'distancezero'
  rate=positive(lo(-sg*c*alpha*ry*di**(alpha-2)))
 pref=2*A*X*d*v*v/(PI*(1+v*v)*((X+A)**2+d*d*v*v))
 val=positive(lo(pref*rate));assert val.is_finite();return val,branch

def safe(v):
 k=int((lo(v)*10**10).floor().unique_fmpz());return f'{k//10**10}.{k%10**10:010d}'
def main():
 p=argparse.ArgumentParser();p.add_argument('--alpha',required=True);p.add_argument('--b',required=True);p.add_argument('--shift',required=True);p.add_argument('--K',required=True);p.add_argument('--sign',type=int,choices=[-1,1],required=True);p.add_argument('--nx',type=int,default=2048);p.add_argument('--ny',type=int,default=512);p.add_argument('--start',type=int,default=0);p.add_argument('--stop',type=int);p.add_argument('--left',default='-18');p.add_argument('--right',default='24');p.add_argument('--vleft',default='-12');p.add_argument('--vright',default='14');p.add_argument('--out',required=True);args=p.parse_args()
 alpha,b,t,K=map(aa,[args.alpha,args.b,args.shift,args.K]);assert 0<alpha<1 and b>0 and t>=-A and K>=1
 stop=args.stop if args.stop is not None else args.nx;assert 0<=args.start<stop<=args.nx
 left=aa(args.left);right=A.log() if args.sign==-1 else aa(args.right);vl=aa(args.vleft);vr=aa(args.vright);du=(right-left)/args.nx;dv=(vr-vl)/args.ny;assert du>0 and dv>0
 ve=[(vl+j*dv).exp() for j in range(args.ny+1)];vc=[ve[j].union(ve[j+1]) for j in range(args.ny)]
 total=arb(0);counts={};started=time.monotonic()
 for i in range(args.start,stop):
  d=(left+i*du).exp().union((left+(i+1)*du).exp());row=arb(0)
  for v in vc:
   val,key=density(d,v,args.sign,alpha,b,t,K);row+=val;counts[key]=counts.get(key,0)+1
  total+=row*du*dv
  if i%32==0:print(i,stop,round(time.monotonic()-started,2),safe(1+4*total),flush=True)
 paths=[Path(__file__),ROOT/'11_lattice_pole_constraints/axis_projection_density/PROOF.md',ROOT/'11_lattice_pole_constraints/axis_projection_stieltjes/PROOF.md',ROOT/'11_lattice_pole_constraints/monotone_axis/PROOF.md',ROOT/'07_diagonal_identity_term/full_range_profile/PROOF.md']
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=str(F(args.alpha)),b=str(F(args.b)),shift=str(F(args.shift)),K=str(F(args.K)),sign=args.sign,nx=args.nx,ny=args.ny,start=args.start,stop=stop,left=args.left,right='log(1/2)' if args.sign==-1 else args.right,vleft=args.vleft,vright=args.vright,precision_bits=ctx.prec,cell_counts=counts,integral_lower_enclosure=total.str(55,more=True),safe_partial_D_lower=safe(1+4*total),elapsed_seconds=time.monotonic()-started,source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},status='Positive density lower sum; separately certified profile factor required.')
 target=ROOT/args.out;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

"""Outward positive Stieltjes lower sums for a normalized projection cusp."""
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
def distance(X,Y,x0,y0,dx,dy,ray=False):
 t=((X-x0)*dx+(Y-y0)*dy)/(dx*dx+dy*dy)
 if t>=0 and (ray or t<=1):return abs((X-x0)*dy-(Y-y0)*dx)/(dx*dx+dy*dy).sqrt()
 t=positive(t) if ray else arb.min(arb(1),positive(t))
 return ((X-x0-t*dx)**2+(Y-y0-t*dy)**2).sqrt()
def witness(drad,v,sign,alpha,b,shift,K):
 X=positive(A+sign*drad);Y=drad*v
 d=arb.min(X,distance(X,Y,arb(0),A,A,-A))
 d=arb.min(d,distance(X,Y,A,arb(0),b,b))
 d=arb.min(d,distance(X,Y,A+b,b,RT3,arb(1),True))
 B=arb.max(A-X,arb.min(X-A,(X-A+(RT3-1)*b)/RT3));c=2**(alpha-1);h=c*X**alpha;power=c*positive(d)**alpha
 if Y<B:g=power
 elif Y>B:g=-power
 else:g=(-hi(power)).union(hi(power))
 r=(1+v*v).sqrt();E=(1-v*v)/r
 P=drad**alpha*positive((r**alpha+positive(E)**alpha-positive(-E)**alpha)/2)
 return arb.max(-h,arb.min(h,arb.min(g+shift,-A+P/K)))
def V(X,Y):
 return 2*A*X*Y/(PI*(((X-A)**2+Y*Y)*((X+A)**2+Y*Y)))
def safe(v):
 k=int((lo(v)*10**10).floor().unique_fmpz());return f'{k//10**10}.{k%10**10:010d}'
def main():
 p=argparse.ArgumentParser();p.add_argument('--alpha',required=True);p.add_argument('--b',required=True);p.add_argument('--shift',required=True);p.add_argument('--K',required=True);p.add_argument('--sign',type=int,choices=[-1,1],required=True);p.add_argument('--nx',type=int,default=4096);p.add_argument('--ny',type=int,default=512);p.add_argument('--start',type=int,default=0);p.add_argument('--stop',type=int);p.add_argument('--left',default='-18');p.add_argument('--right',default='24');p.add_argument('--vleft',default='-12');p.add_argument('--vright',default='14');p.add_argument('--out',required=True);args=p.parse_args()
 alpha,b,t,K=map(aa,[args.alpha,args.b,args.shift,args.K]);assert 0<alpha<1 and b>0 and t>=-A and K>=1
 stop=args.stop if args.stop is not None else args.nx;assert 0<=args.start<stop<=args.nx
 left=aa(args.left);right=A.log() if args.sign==-1 else aa(args.right);vl=aa(args.vleft);vr=aa(args.vright)
 assert left<right and vl<vr;du=(right-left)/args.nx;dv=(vr-vl)/args.ny;ve=[(vl+j*dv).exp() for j in range(args.ny+1)]
 total=arb(0);positive_cells=0;started=time.monotonic()
 for i in range(args.start,stop):
  dl=(left+i*du).exp();dr=(left+(i+1)*du).exp();d=dl.union(dr);X=A+args.sign*d
  X=positive(X);width=positive(lo(dr-dl));vals=[witness(d,v,args.sign,alpha,b,t,K) for v in ve];vv=[V(X,d*v) for v in ve];row=arb(0)
  for j in range(args.ny):
   mass=positive(lo(vals[j]-vals[j+1]));kernel=positive(arb.min(lo(vv[j]),lo(vv[j+1])))
   if mass>0 and kernel>0:positive_cells+=1;row+=mass*kernel
  assert row.is_finite() and row>=0;total+=row*width
  if i%32==0:print(i,stop,round(time.monotonic()-started,2),safe(1+4*total),flush=True)
 paths=[Path(__file__),ROOT/'11_lattice_pole_constraints/axis_projection_stieltjes/PROOF.md',ROOT/'11_lattice_pole_constraints/monotone_axis/PROOF.md',ROOT/'07_diagonal_identity_term/full_range_profile/PROOF.md']
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=str(F(args.alpha)),b=str(F(args.b)),shift=str(F(args.shift)),K=str(F(args.K)),sign=args.sign,nx=args.nx,ny=args.ny,start=args.start,stop=stop,left=args.left,right='log(1/2)' if args.sign==-1 else args.right,vleft=args.vleft,vright=args.vright,precision_bits=ctx.prec,positive_cells=positive_cells,integral_lower_enclosure=total.str(55,more=True),safe_partial_D_lower=safe(1+4*total),elapsed_seconds=time.monotonic()-started,source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},status='Partial positive lower sum; K must have a separately verified global profile certificate.')
 out=ROOT/args.out;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()

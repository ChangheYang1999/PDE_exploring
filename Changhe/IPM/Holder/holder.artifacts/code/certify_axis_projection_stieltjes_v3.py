"""Positive Stieltjes sums with a correlated profile difference.
The complete proof is axis_projection_stieltjes/coupled_profile/PROOF.md.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import argparse,json,hashlib,time
from flint import arb,ctx
import certify_axis_projection_stieltjes_v2 as old
ctx.prec=192;A=arb(1)/2;RT3=arb(3).sqrt();ROOT=Path(__file__).resolve().parents[1]
aa=old.aa;lo=old.lo;hi=old.hi;positive=old.positive;safe=old.safe

def power_nonnegative(x,e):
 assert x.is_finite() and e>0
 if x>0:return x**e
 up=hi(x);assert up>=0
 return arb(0).union(up**e) if up>0 else arb(0)

def distance(X,Y,x0,y0,dx,dy,ray=False):
 t=((X-x0)*dx+(Y-y0)*dy)/(dx*dx+dy*dy)
 if t>=0 and (ray or t<=1):return abs((X-x0)*dy-(Y-y0)*dx)/(dx*dx+dy*dy).sqrt()
 t=positive(t) if ray else arb.min(arb(1),positive(t))
 u=X-x0-t*dx;v=Y-y0-t*dy
 return power_nonnegative(u*u+v*v,A)

def V(X,Y):
 u=X-A;v=X+A
 return 2*A*X*Y/(arb.pi()*((u*u+Y*Y)*(v*v+Y*Y)))

def profile(v,alpha):
 r=(1+v*v).sqrt();E=(1-v*v)/r
 return positive((r**alpha+power_nonnegative(positive(E),alpha)-power_nonnegative(positive(-E),alpha))/2)

def polygon(X,Y,alpha,b):
 d=arb.min(X,distance(X,Y,arb(0),A,A,-A))
 d=arb.min(d,distance(X,Y,A,arb(0),b,b))
 d=arb.min(d,distance(X,Y,A+b,b,RT3,arb(1),True))
 B=arb.max(A-X,arb.min(X-A,(X-A+(RT3-1)*b)/RT3))
 power=2**(alpha-1)*power_nonnegative(d,alpha)
 if Y<B:return power
 if Y>B:return -power
 return (-hi(power)).union(hi(power))

def data(d,ve,pe,sign,alpha,b,shift,K):
 X=positive(A+sign*d);h=2**(alpha-1)*power_nonnegative(X,alpha);factor=d**alpha/K
 gs=[polygon(X,d*v,alpha,b)+shift for v in ve]
 ps=[-A+factor*p for p in pe]
 fs=[arb.max(-h,arb.min(h,arb.min(g,p))) for g,p in zip(gs,ps)]
 return X,h,factor,gs,ps,fs

def mass_lower(j,h,factor,gs,ps,fs,pe):
 assert fs[j].is_finite() and fs[j+1].is_finite()
 basic=positive(lo(fs[j]-fs[j+1]));improved=basic
 if ps[j]<=gs[j]:
  delta=factor*(pe[j]-pe[j+1])
  val=lo(delta)
  for q in [ps[j]+h,h-ps[j+1],2*h]:val=arb.min(val,lo(q))
  improved=arb.max(basic,positive(val))
 assert improved.is_finite() and basic.is_finite()
 return positive(lo(improved)),positive(lo(basic))

def main():
 p=argparse.ArgumentParser();p.add_argument('--alpha',required=True);p.add_argument('--b',required=True);p.add_argument('--shift',required=True);p.add_argument('--K',required=True);p.add_argument('--sign',type=int,choices=[-1,1],required=True);p.add_argument('--nx',type=int,default=4096);p.add_argument('--ny',type=int,default=128);p.add_argument('--start',type=int,default=0);p.add_argument('--stop',type=int);p.add_argument('--left',default='-18');p.add_argument('--right',default='24');p.add_argument('--vleft',default='-12');p.add_argument('--vright',default='14');p.add_argument('--out',required=True);args=p.parse_args()
 alpha,b,t,K=map(aa,[args.alpha,args.b,args.shift,args.K]);assert 0<alpha<1 and b>0 and t>=-A and K>=1
 stop=args.stop if args.stop is not None else args.nx;assert 0<=args.start<stop<=args.nx and args.ny>0
 left=aa(args.left);right=A.log() if args.sign==-1 else aa(args.right);vl=aa(args.vleft);vr=aa(args.vright)
 assert left<right and vl<vr;du=(right-left)/args.nx;dv=(vr-vl)/args.ny;ve=[(vl+j*dv).exp() for j in range(args.ny+1)];pe=[profile(v,alpha) for v in ve]
 total=arb(0);basic_total=arb(0);positive_cells=0;improved_cells=0;started=time.monotonic()
 for i in range(args.start,stop):
  dl=(left+i*du).exp();dr=(left+(i+1)*du).exp();d=dl.union(dr);width=positive(lo(dr-dl))
  X,h,factor,gs,ps,fs=data(d,ve,pe,args.sign,alpha,b,t,K);vv=[V(X,d*v) for v in ve];row=arb(0);basic_row=arb(0)
  for j in range(args.ny):
   mass,basic=mass_lower(j,h,factor,gs,ps,fs,pe);kernel=positive(arb.min(lo(vv[j]),lo(vv[j+1])))
   if mass>0 and kernel>0:positive_cells+=1;row+=mass*kernel
   if mass>basic and kernel>0:improved_cells+=1
   basic_row+=basic*kernel
  assert row.is_finite() and row>=0 and basic_row.is_finite();total+=row*width;basic_total+=basic_row*width
  if i%64==0:print(i,stop,round(time.monotonic()-started,2),safe(1+4*total),flush=True)
 paths=[Path(__file__),ROOT/'code/certify_axis_projection_stieltjes_v2.py',ROOT/'11_lattice_pole_constraints/axis_projection_stieltjes/coupled_profile/PROOF.md',ROOT/'11_lattice_pole_constraints/axis_projection_stieltjes/PROOF.md',ROOT/'11_lattice_pole_constraints/monotone_axis/PROOF.md',ROOT/'07_diagonal_identity_term/full_range_profile/PROOF.md']
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=str(F(args.alpha)),b=str(F(args.b)),shift=str(F(args.shift)),K=str(F(args.K)),sign=args.sign,nx=args.nx,ny=args.ny,start=args.start,stop=stop,left=args.left,right='log(1/2)' if args.sign==-1 else args.right,vleft=args.vleft,vright=args.vright,precision_bits=ctx.prec,positive_cells=positive_cells,improved_cells=improved_cells,integral_lower_enclosure=total.str(55,more=True),basic_integral_lower_enclosure=basic_total.str(55,more=True),safe_partial_D_lower=safe(1+4*total),elapsed_seconds=time.monotonic()-started,source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},status='Partial positive lower sum with correlated profile; K requires a separately verified global certificate.')
 out=ROOT/args.out;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()

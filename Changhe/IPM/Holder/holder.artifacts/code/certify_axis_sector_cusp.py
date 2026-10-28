"""Outward positive one-dimensional lower certificate for the axis sector cusp."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import argparse,json,hashlib,time
from flint import arb,ctx
from certify_axis_clamp_layercake import aa,line,include_test,negative_mass_magnitude,SKIP,A,RT2,RT3,safe_lower
ROOT=Path(__file__).resolve().parents[1];ctx.prec=256

def pos(u,s,p,b):
 w=A-RT2*arb.max(s,p);v=arb.max(u,s);ans=arb(0)
 if include_test(v,w,'triangle'):ans+=line(arb(-1),w,v,w,hi_zero=True)
 d1=-A-RT2*arb.max(s,p);d2=((RT3-1)*b-A-2*s)/RT3;k=(d2-d1)/(1-1/RT3)
 z=arb.max(u,arb.max(A+RT2*arb.max(s,p),A-(RT3-1)*b+2*s))
 if include_test(z,k,'positive_first'):ans+=line(arb(1),d1,z,k)
 ans+=line(1/RT3,d2,arb.max(z,k));return arb.max(arb(0),2*ans)

def mid(u,s,p,b):
 w=A-RT2*p;ans=arb(0)
 if include_test(u,w,'triangle'):ans+=line(arb(-1),w,u,w,hi_zero=True)
 d1=-A-RT2*p;d2=((RT3-1)*b-A+2*s)/RT3;k=(d2-d1)/(1-1/RT3);z=arb.max(u,A+RT2*p)
 if include_test(z,k,'positive_first'):ans+=line(arb(1),d1,z,k)
 ans+=line(1/RT3,d2,arb.max(z,k));return arb.max(arb(0),2*ans)

def main():
 p=argparse.ArgumentParser();p.add_argument('--alpha',required=True);p.add_argument('--b',required=True);p.add_argument('--shift',required=True)
 p.add_argument('--part',choices=['plus','mid','low'],required=True);p.add_argument('--cells',type=int,default=131072);p.add_argument('--start',type=int,default=0);p.add_argument('--stop',type=int);p.add_argument('--left');p.add_argument('--right');p.add_argument('--out',required=True);args=p.parse_args()
 alpha,b,t=map(aa,[args.alpha,args.b,args.shift]);assert 0<alpha<1 and b>=A and -A<t<=0
 stop=args.stop or args.cells;assert 0<=args.start<stop<=args.cells;q0=t+A;c=2**(alpha-1);power=1/alpha
 left=Q(args.left or ('1/100000000' if args.part=='mid' else '-24'));right=Q(args.right or ('28' if args.part=='mid' else '40'));step=(right-left)/args.cells;assert step>0
 def U(x):return (x/c)**power
 total=arb(0);started=time.monotonic()
 for i in range(args.start,stop):
  x=aa(left+i*step).union(aa(left+(i+1)*step))
  if args.part=='mid':
   ee=(-x).exp();q=q0*ee;val=mid(U(A-q),U(q0-q),q**power,b)*q
  else:
   r=x.exp()
   if args.part=='plus':val=pos(U(abs(r+t)),U(r),(r+q0)**power,b)*r
   else:val=negative_mass_magnitude(U(r+A),U(r+q0),b)*r
  assert val.is_finite() and val>=0,(i,val);total+=val*aa(step)
  if i%2048==0:print(i,stop,round(time.monotonic()-started,3),flush=True)
 paths=[Path(__file__),ROOT/'code/certify_axis_clamp_layercake.py',ROOT/'11_lattice_pole_constraints/axis_sector_cusp/PROOF.md',ROOT/'11_lattice_pole_constraints/monotone_axis/PROOF.md',ROOT/'11_lattice_pole_constraints/axis_clamped_layercake/PROOF.md']
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=str(Q(args.alpha)),b=str(Q(args.b)),shift=str(Q(args.shift)),part=args.part,cells=args.cells,start=args.start,stop=stop,left=str(left),right=str(right),precision_bits=ctx.prec,included_integral_enclosure=total.str(55,more=True),safe_integral_lower_10_places=safe_lower(total),skipped_components=SKIP,elapsed_seconds=time.monotonic()-started,source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},status='Rigorous partial lower bound under the analytic proof; upper endpoint does not bound the full witness value.')
 target=ROOT/args.out;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['part','included_integral_enclosure','safe_integral_lower_10_places','elapsed_seconds']},indent=2))
if __name__=='__main__':main()

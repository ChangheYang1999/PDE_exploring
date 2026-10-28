"""Exact rational interval covering of every projection-profile pair class."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import argparse,json,time,hashlib
from flint import arb,ctx
ctx.prec=192;PI=arb.pi();ROOT=Path(__file__).resolve().parents[1]
def A(x):return arb(x.numerator)/x.denominator if isinstance(x,F) else arb(x)
def up(x):return arb(x.upper())
def low(x):return arb(x.lower())
def pos(x):return arb.max(arb(0),x)
def distance_lower(ul,uh,delta):
 ct=delta.cos();st=delta.sin()
 if uh<ct:d=(uh-ct)**2+st**2
 elif ul>ct:d=(ul-ct)**2+st**2
 else:d=st**2
 simple=(1-uh)**2+4*ul*(delta/2).sin()**2
 return arb.max(pos(low(d)),pos(low(simple)))
def sin_power(lo,hi,alpha):
 si=(2*PI*lo.union(hi)).sin();l=low(si);h=up(si)
 l=arb(0) if l<0 else l;h=arb(1) if h>1 else h
 return low(l**alpha),up(h**alpha)
def bound(box,alpha,mode):
 ul,uh,al,ah,bl,bh=map(A,box);u=ul.union(uh);R=u**alpha
 if mode=='opposite':
  delta=PI*(al+bl)
  if delta>=PI/2:return arb(1)
  k=1/(1-alpha)
  ans=arb.min(up((1-u)**(-alpha)),up(((1+R**k)/2)**(1/k)+(1-R)/(2*(1-u)**alpha)))
  _,sa=sin_power(al,ah,alpha);_,sb=sin_power(bl,bh,alpha)
  numerator=arb.min(arb(1),up((1+sa-ul**alpha*(1-sb))/2))
 else:
  delta=PI*arb.max(arb(0),arb.max(al-bh,bl-ah))
  dhi=PI*arb.max(abs(al-bh),abs(ah-bl));dmax=((1-ul)**2+4*uh*(dhi/2).sin()**2).sqrt()
  ans=up(2**(alpha-1)+alpha/2*(dmax/ul)**(1-alpha))
  edge=PI*arb.min(arb.min(al,bl),arb.min(arb(1)/2-ah,arb(1)/2-bh))
  if edge>0:
   rt2=arb(2).sqrt();grad=alpha/2*((ul/rt2)**(alpha-1)+2*(rt2*ul*edge.sin())**(alpha-1))
   ans=arb.min(ans,up(grad*dmax**(1-alpha)))
  sa0,sa1=sin_power(al,ah,alpha);sb0,sb1=sin_power(bl,bh,alpha)
  difference=arb.max(up(sa1-ul**alpha*sb0),up(uh**alpha*sb1-sa0))
  numerator=arb.min(up(1-ul**alpha/2),up((1-ul**alpha+difference)/2))
 ds=distance_lower(ul,uh,delta)
 if ds>0:ans=arb.min(ans,up(numerator/ds**(alpha/2)))
 return ans

def main():
 p=argparse.ArgumentParser();p.add_argument('--alpha',required=True);p.add_argument('--target',required=True);p.add_argument('--mode',choices=['same','opposite'],required=True);p.add_argument('--epsilon',default='1/100000000');p.add_argument('--max-boxes',type=int,default=8000000);p.add_argument('--out',required=True);args=p.parse_args()
 alpha=A(F(args.alpha));target=A(F(args.target));assert 0<alpha<1 and target>1;eps=F(args.epsilon);e=A(eps);assert 0<e<arb(1)/2
 endpoint_left=(1-e)**(-alpha);k=1/(1-alpha);R0=(1-e)**alpha;c=alpha*(1-e)**(alpha-1)
 endpoint_right=1+(k-1)*c*c*e*e/(8*R0**arb.max(arb(1),k-1))+c/2*e**(1-alpha)
 assert endpoint_left<target
 if args.mode=='opposite':assert endpoint_right<target
 hi=1-eps if args.mode=='opposite' else F(1)
 stack=[((eps,hi,F(0),F(1,2),F(0),F(1,2)),0)];checked=accepted=0;maxdepth=0;worst=arb(0);started=time.monotonic()
 while stack:
  box,depth=stack.pop();v=bound(box,alpha,args.mode);checked+=1
  if v<=target:accepted+=1;maxdepth=max(depth,maxdepth);worst=arb.max(worst,v)
  else:
   assert checked<args.max_boxes,('box limit',checked,len(stack),box,v)
   widths=[box[1]-box[0],2*(box[3]-box[2]),2*(box[5]-box[4])];d=max(range(3),key=lambda j:widths[j]);m=(box[2*d]+box[2*d+1])/2
   left=list(box);right=list(box);left[2*d+1]=m;right[2*d]=m;stack.extend([(tuple(left),depth+1),(tuple(right),depth+1)])
  if checked%20000==0:print(checked,accepted,len(stack),round(time.monotonic()-started,2),flush=True)
 assert checked==2*accepted-1
 paths=[Path(__file__),ROOT/'07_diagonal_identity_term/full_range_profile/local_gradient/PROOF.md',ROOT/'07_diagonal_identity_term/full_range_profile/PROOF.md',ROOT/'07_diagonal_identity_term/local_projection_profile/PROOF.md']
 result=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=str(F(args.alpha)),target=str(F(args.target)),mode=args.mode,epsilon=str(eps),precision_bits=ctx.prec,checked_boxes=checked,accepted_boxes=accepted,maxdepth=maxdepth,largest_accepted_bound=worst.str(50,more=True),left_endpoint=endpoint_left.str(50,more=True),right_endpoint=None if args.mode=='same' else endpoint_right.str(50,more=True),elapsed_seconds=time.monotonic()-started,source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},status='Complete exact rational covering of this pair class; both classes are required for a profile seminorm bound.')
 out=ROOT/args.out;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(out,flush=True)
if __name__=='__main__':main()

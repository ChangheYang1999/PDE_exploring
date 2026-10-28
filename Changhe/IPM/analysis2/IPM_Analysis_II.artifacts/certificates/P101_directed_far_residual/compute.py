"""Directed Bernstein/monomial cover, including the point at infinity."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
from functools import lru_cache
import json,sys,time,argparse
from flint import arb,arb_mat,ctx
sys.set_int_max_str_digits(0)
here=Path(__file__).parent

def A(v):
 q=F(v);return arb(q.numerator)/q.denominator

@lru_cache(None)
def T(n,lo,hi):
 lo,hi=F(lo),F(hi)
 return arb_mat([[A(sum((F(comb(k,l)*comb(i,l),comb(n,l))*lo**(k-l)*(hi-lo)**l for l in range(min(k,i)+1)),F(0))) for k in range(n+1)] for i in range(n+1)])

def halves(n):
 L=arb_mat([[A(F(comb(i,k),2**i)) if k<=i else arb(0) for k in range(n+1)] for i in range(n+1)])
 R=arb_mat([[A(F(comb(n-i,k-i),2**(n-i))) if k>=i else arb(0) for k in range(n+1)] for i in range(n+1)])
 return L,R

def radial(lo,hi,exponents,R):
 vals=[]
 for a in exponents:
  if not a:vals.append(arb(1));continue
  low=A(lo)**A(a)/A(R)**A(a) if lo else arb(0);high=A(hi)**A(a)/A(R)**A(a)
  vals.append(low.union(high))
 return arb_mat([vals])

def bound(B,tlo,thi,zlo,zhi,exponents,R):
 vals=(radial(tlo,thi,exponents,R)*B).entries();lo=hi=vals[0]
 for v in vals[1:]:lo=lo.min(v);hi=hi.max(v)
 # Multiplying the whole signed range is safe; its magnitude times the upper
 # angular factor also covers the absolute residual.
 return abs(lo).max(abs(hi))*((1-A(zlo))/2).sqrt()

def main(args):
 ctx.prec=384;start=time.monotonic();src=here/'sectors.json';d=json.loads(src.read_text());target=F(args.target);eps=F(d['epsilon_upper_rational']);rows=d['rows'];n=max(int(k) for r in rows for k in r['P']);P=arb_mat(len(rows),n+1)
 for j,row in enumerate(rows):
  for k,v in row['P'].items():P[j,int(k)]=A(v)
 B=P*T(n,'-1','1').transpose();exponents=list(map(lambda r:F(r['a']),rows));R=d['R'];L,H=halves(n);stack=[(B,F(0),F(1),F(-1),F(1),'',None)];good=[];bad=[];processed=0;prior=0
 dest=here/f"bound_{args.label}.json"
 if args.resume:
  old=json.loads(dest.read_text());assert old['status']=='INCOMPLETE' and old['source_sha256']==sha256(src.read_bytes()).hexdigest();assert F(old['target'])==target;good=old['accepted'];bad=old['failed'];processed=old['processed'];prior=old.get('cumulative_seconds',old['seconds']);stack=[]
  for path in old['pending_paths']:
   tl,th,zl,zh=F(0),F(1),F(-1),F(1);bb=B
   for letter in path:
    if letter=='t':th=(tl+th)/2
    elif letter=='T':tl=(tl+th)/2
    elif letter=='z':zh=(zl+zh)/2;bb=bb*L.transpose()
    else:zl=(zl+zh)/2;bb=bb*H.transpose()
   stack.append((bb,tl,th,zl,zh,path,None))
 while stack and time.monotonic()-start<args.seconds:
  bb,tl,th,zl,zh,path,cached=stack.pop();processed+=1;upper=bound(bb,tl,th,zl,zh,exponents,R) if cached is None else cached
  if upper+A(eps)<=A(target):good.append({'path':path,'t':[str(tl),str(th)],'z':[str(zl),str(zh)],'upper':upper.str(90)})
  elif len(path)>=55:bad.append(path)
  else:
   tm=(tl+th)/2;zm=(zl+zh)/2
   children=[[(bb,tl,tm,zl,zh,path+'t'),(bb,tm,th,zl,zh,path+'T')],[(bb*L.transpose(),tl,th,zl,zm,path+'z'),(bb*H.transpose(),tl,th,zm,zh,path+'Z')]];choices=[]
   for group in children:
    upp=[bound(x[0],x[1],x[2],x[3],x[4],exponents,R) for x in group];score=sum(max(float(v+A(eps)-A(target)),0) for v in upp);choices.append((score,[x+(v,) for x,v in zip(group,upp)]))
   stack.extend(reversed(min(choices,key=lambda x:x[0])[1]))
  if processed%100==0:print(processed,'processed',len(good),'accepted',len(stack),'pending',time.monotonic()-start,flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPLETE' if not stack and not bad else 'INCOMPLETE','target':str(target),'epsilon_upper_rational':str(eps),'R':R,'accepted':good,'failed':bad,'pending_paths':[x[5] for x in stack],'processed':processed,'source_sha256':sha256(src.read_bytes()).hexdigest(),'precision_bits':ctx.prec,'seconds':time.monotonic()-start,'cumulative_seconds':prior+time.monotonic()-start}
 dest.write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(good),'leaves',len(stack),'pending',out['seconds'],flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--target',default='0.244');ap.add_argument('--label',default='0244');ap.add_argument('--seconds',type=int,default=480);ap.add_argument('--resume',action='store_true');main(ap.parse_args())

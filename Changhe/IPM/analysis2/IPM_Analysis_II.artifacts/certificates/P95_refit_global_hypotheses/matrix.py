from pathlib import Path
from fractions import Fraction as F
from math import comb
from functools import lru_cache
from datetime import datetime,timezone
from hashlib import sha256
import sys,json,time,argparse
from flint import arb,arb_mat,ctx
sys.set_int_max_str_digits(0)
root=Path(__file__).resolve().parents[3];here=Path(__file__).parent

def aa(v):
 q=F(v);return arb(q.numerator)/q.denominator

def linear(P,a,b):
 D={}
 for (i,j),v in P.items():
  D[i,j]=D.get((i,j),F(0))+a*v
  D[i+1,j]=D.get((i+1,j),F(0))+b*v
 return {key:v for key,v in D.items() if v}

def plus(*terms):
 D={}
 for factor,P in terms:
  for k,v in P.items():D[k]=D.get(k,F(0))+factor*v
 return {key:v for key,v in D.items() if v}

@lru_cache(None)
def trans(n,low,high):
 lo,hi=F(low),F(high);T=arb_mat([[aa(comb(k,i)*lo**(k-i)*(hi-lo)**i) if i<=k else arb(0) for k in range(n+1)] for i in range(n+1)])
 G=arb_mat([[aa(F(comb(i,k),comb(n,k))) if k<=i else arb(0) for k in range(n+1)] for i in range(n+1)])
 return G*T

def halves(n):
 L=arb_mat([[aa(F(comb(i,k),2**i)) if k<=i else arb(0) for k in range(n+1)] for i in range(n+1)])
 R=arb_mat([[aa(F(comb(n-i,k-i),2**(n-i))) if k>=i else arb(0) for k in range(n+1)] for i in range(n+1)])
 return L,R

def prepare(d,kind):
 c=F(d['cl']);P={(label,j):{(i,k):F(v) for i,k,v in d['polynomials'][f'{label}_{j}']} for label in ['chi22','chi04','chi31','chi13','e'] for j in range(6)}
 S={}
 if kind=='M':scalar={(0,0):2*c+1-F(19,5)}
 elif kind=='M1':scalar={(0,0):F(1,2),(1,0):-c/5}
 else:scalar={(0,0):F(1,2)-c,(1,0):F(3,2)+c/5}
 for lab in ['a','b','q']:S[lab,0]=scalar if lab!='q' else {}
 for j in range(6):
  p22,p04,p31,p13,e=(P[label,j] for label in ['chi22','chi04','chi31','chi13','e'])
  if kind=='M':a=plus((-2,p22),(-1,p04));b=p22;q=p31
  elif kind=='M1':a=plus((-1,p04),(1,linear(e,0,-F(1,5))));b=plus((-1,p22),(1,linear(e,0,-F(1,5))));q=p13
  else:
   a=plus((1,linear(plus((1,p22),(-1,p04)),1,3)),(1,linear(e,0,F(16,5))))
   b=plus((-2,linear(p22,1,3)),(1,linear(e,0,F(16,5))))
   q=linear(plus((-F(1,2),p31),(F(3,2),p13)),1,3)
  for lab,p in [('a',a),('b',b),('q',q)]:S[lab,j+1]=p
 nt=max(i for p in S.values() for i,k in p);nz=max(k for p in S.values() for i,k in p)
 T=trans(nt,'0','1');Z=trans(nz,'-1','1').transpose();B={}
 for key,p in S.items():
  mat=arb_mat(nt+1,nz+1)
  for (i,k),v in p.items():mat[i,k]=aa(v)
  B[key]=T*mat*Z
 return S,B,nt,nz

def bound(B,tl,th,zl,zh,delta):
 wl=(1-aa(th))**aa(delta/2);wh=(1-aa(tl))**aa(delta/2)
 W=arb_mat([[sum((aa(F(comb(n,k)*comb(i,k),comb(6,k)))*wl**(n-k)*(wh-wl)**k for k in range(min(n,i)+1)),arb(0)) for n in range(7)] for i in range(7)])
 rr={}
 for label in ['a','b','q']:
  vals=(W*arb_mat([B[label,j].entries() for j in range(7)])).entries();lo=vals[0];hi=vals[0]
  for v in vals[1:]:lo=lo.min(v);hi=hi.max(v)
  rr[label]=(lo.lower(),hi.upper())
 al,bl=rr['a'][0],rr['b'][0];lo,hi=rr['q'];si=arb(1) if zl<=0<=zh else (1-aa(min(abs(zl),abs(zh)))**2).sqrt();C=abs(lo).max(abs(hi))*si
 low=((al+bl-((al-bl)**2+4*C*C).sqrt())/2).max(al.min(bl)-C)
 return low

def split(B,axis,L,R):
 if axis=='t':return {k:L*v for k,v in B.items()},{k:R*v for k,v in B.items()}
 return {k:v*L.transpose() for k,v in B.items()},{k:v*R.transpose() for k,v in B.items()}

def run(args):
 ctx.prec=512;start=time.monotonic();src=here/f'{args.name}.polynomials.json';d=json.loads(src.read_text());S,B,nt,nz=prepare(d,args.kind);delta=F(d['delta'])
 print('prepared',nt,nz,'seconds',time.monotonic()-start,flush=True)
 Lt,Rt=halves(nt);Lz,Rz=halves(nz);stack=[(B,F(0),F(1),F(-1),F(1),'',None)];good=[];bad=[];n=0;worst=arb(10)
 previous_seconds=0;previous_hash=None
 if args.resume:
  prior=here/f'{args.name}.{args.kind}.json';previous_hash=sha256(prior.read_bytes()).hexdigest();old=json.loads(prior.read_text())
  assert old['status']=='INCOMPLETE' and old['input_sha256']==sha256(src.read_bytes()).hexdigest()
  good=old['accepted'];bad=old['failed'];n=old['processed'];previous_seconds=old.get('cumulative_seconds',old['seconds']);stack=[]
  for row in good:worst=worst.min(arb(row['lower_numerator_after_target']))
  for path in old['pending_paths']:
   bb=B;tl,th,zl,zh=F(0),F(1),F(-1),F(1)
   for letter in path:
    axis=letter.lower();ll,rr=split(bb,axis,Lt if axis=='t' else Lz,Rt if axis=='t' else Rz)
    bb=ll if letter.islower() else rr
    if axis=='t':
     mid=(tl+th)/2
     if letter.islower():th=mid
     else:tl=mid
    else:
     mid=(zl+zh)/2
     if letter.islower():zh=mid
     else:zl=mid
   stack.append((bb,tl,th,zl,zh,path,None))
  print('resumed',n,'accepted',len(good),'pending',len(stack),'seconds',time.monotonic()-start,flush=True)
 while stack and time.monotonic()-start<args.seconds:
  B,tl,th,zl,zh,path,cached=stack.pop();n+=1;low=cached if cached is not None else bound(B,tl,th,zl,zh,delta)
  if low>=0:
   good.append({'path':path,'t':[str(tl),str(th)],'z':[str(zl),str(zh)],'lower_numerator_after_target':low.str(70)});worst=worst.min(low)
  elif len(path)>=60:bad.append({'path':path,'lower':low.str(70)})
  else:
   choices=[]
   for axis in ['t','z']:
    l,r=split(B,axis,Lt if axis=='t' else Lz,Rt if axis=='t' else Rz)
    if axis=='t':mid=(tl+th)/2;nodes=[(l,tl,mid,zl,zh,path+'t'),(r,mid,th,zl,zh,path+'T')]
    else:mid=(zl+zh)/2;nodes=[(l,tl,th,zl,mid,path+'z'),(r,tl,th,mid,zh,path+'Z')]
    lows=[bound(v[0],v[1],v[2],v[3],v[4],delta) for v in nodes]
    score=sum(min(float(v),0.0) for v in lows);choices.append((score,[node+(ll,) for node,ll in zip(nodes,lows)]))
   stack.extend(reversed(max(choices,key=lambda x:x[0])[1]))
  if n%10==0:print('processed',n,'accepted',len(good),'pending',len(stack),'depth',len(path),'seconds',time.monotonic()-start,flush=True)
 status='COMPLETE' if not stack and not bad else 'INCOMPLETE'
 out={'utc':datetime.now(timezone.utc).isoformat(),'name':args.name,'kind':args.kind,'status':status,'accepted':good,'failed':bad,'pending_paths':[v[5] for v in stack],'processed':n,'worst':worst.str(80),'precision_bits':ctx.prec,'degrees':[nt,nz],'seconds':time.monotonic()-start,'cumulative_seconds':previous_seconds+time.monotonic()-start,'previous_result_sha256':previous_hash,'input_sha256':sha256(src.read_bytes()).hexdigest(),'proof_sha256':sha256((here.parent/'PROOF.md').read_bytes()).hexdigest()}
 (here/f'{args.name}.{args.kind}.json').write_text(json.dumps(out,indent=2)+'\n');print(status,len(good),len(stack),out['seconds'],flush=True)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--name',default='nb_d2_exact');ap.add_argument('--kind',choices=['M','M1','M2'],default='M');ap.add_argument('--seconds',type=int,default=90);ap.add_argument('--resume',action='store_true');run(ap.parse_args())

from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
from math import comb
from functools import lru_cache
import sys,json,time,argparse
from flint import arb,arb_mat,ctx
root=Path(__file__).resolve().parents[3];here=Path(__file__).parent
sys.path.insert(0,str(root/'research/95_refit_global_hypotheses/verification'))
from matrix import aa,linear,plus,trans,halves,split

def prepare(d,kind,target,tl,th):
 c=F(d['cl']);P={(l,j):{(i,k):F(v) for i,k,v in d['polynomials'][f'{l}_{j}']} for l in ['chi22','chi04','chi31','chi13','e'] for j in range(4)};S={}
 if kind=='M':scalar={(0,0):2*c+1-target}
 elif kind=='B1':scalar={(0,0):1-target}
 elif kind=='B2':scalar={(0,0):1-c-target,(1,0):3+c/5-3*target}
 elif kind=='B3':scalar={(0,0):1-2*c-target,(1,0):3-F(14,5)*c-3*target}
 elif kind in ['symDU','A']:scalar={(0,0):target}
 else:scalar={(0,0):-target}
 for l in ['a','b','q']:S[l,0]=scalar if l!='q' else {}
 for j in range(4):
  p22,p04,p31,p13,e=(P[l,j] for l in ['chi22','chi04','chi31','chi13','e'])
  if kind=='M':a=plus((-2,p22),(-1,p04));b=p22;q=p31
  elif kind=='B1':a=plus((-1,p04));b=plus((-1,p22));q=p13
  elif kind in ['B2','B3']:
   k=2 if kind=='B2' else 3
   a=plus((1,linear(plus((k-1,p22),(-1,p04)),1,3)),(1,linear(e,0,F(16,5))))
   b=linear(plus((-k,p22)),1,3);b=plus((1,b),(1,linear(e,0,F(16,5))))
   q=linear(plus((F(1-k,2),p31),(F(k+1,2),p13)),1,3)
  elif kind=='symDU':a=p22;b=plus((-1,p22));q=plus((F(1,2),p13),(-F(1,2),p31))
  elif kind=='A':a=plus((-1,p22),(-1,p04));b={};q=plus((F(1,2),p31),(F(1,2),p13))
  else:a=plus((-1,p22),(-1,p04));b=a;q={}
  for l,p in [('a',a),('b',b),('q',q)]:
   idx=j if kind=='rho_scaled' else j+1
   S[l,idx]=plus((1,S.get((l,idx),{})),(1,p))
 for l in ['a','b','q']:
  for j in range(5):S.setdefault((l,j),{})
 nt=max(i for p in S.values() for i,k in p);nz=max(k for p in S.values() for i,k in p);B={}
 T=trans(nt,str(tl),str(th));Z=trans(nz,'-1','1').transpose()
 for key,p in S.items():
  M=arb_mat(nt+1,nz+1)
  for (i,k),v in p.items():M[i,k]=aa(v)
  B[key]=T*M*Z
 return S,B,nt,nz

def bound(B,tl,th,zl,zh,delta):
 wl=(1-aa(th))**aa(delta/2);wh=(1-aa(tl))**aa(delta/2)
 W=arb_mat([[sum((aa(F(comb(n,k)*comb(i,k),comb(4,k)))*wl**(n-k)*(wh-wl)**k for k in range(min(n,i)+1)),arb(0)) for n in range(5)] for i in range(5)])
 out={}
 for l in ['a','b','q']:
  vals=(W*arb_mat([B[l,j].entries() for j in range(5)])).entries();lo=vals[0];hi=vals[0]
  for v in vals[1:]:lo=lo.min(v);hi=hi.max(v)
  out[l]=lo.lower(),hi.upper()
 a,b=out['a'][0],out['b'][0];lo,hi=out['q'];sine=arb(1) if zl<=0<=zh else (1-aa(min(abs(zl),abs(zh)))**2).sqrt();C=abs(lo).max(abs(hi))*sine
 return ((a+b-((a-b)**2+4*C*C).sqrt())/2).max(a.min(b)-C)

def main(args):
 ctx.prec=384;start=time.monotonic();source=root/'research/96_original_auxiliary_recomputation/verification/polynomials.json';d=json.loads(source.read_text());target=F(args.target);tl=F(args.t_min);th=F(args.t_max);S,B,nt,nz=prepare(d,args.kind,target,tl,th);delta=F(d['delta']);L,R=halves(nt);Lz,Rz=halves(nz)
 stack=[(B,tl,th,F(-1),F(1),'',None)];good=[];failed=[];n=0;worst=arb(100)
 while stack and time.monotonic()-start<args.seconds:
  B,tl,th,zl,zh,path,cached=stack.pop();n+=1;low=bound(B,tl,th,zl,zh,delta) if cached is None else cached
  if low>=0:good.append({'path':path,'t':[str(tl),str(th)],'z':[str(zl),str(zh)],'lower_numerator_after_target':low.str(70)});worst=worst.min(low)
  elif len(path)>48:failed.append(path)
  else:
   choices=[]
   for axis in ['t','z']:
    ll,rr=split(B,axis,L if axis=='t' else Lz,R if axis=='t' else Rz)
    if axis=='t':mid=(tl+th)/2;nodes=[(ll,tl,mid,zl,zh,path+'t'),(rr,mid,th,zl,zh,path+'T')]
    else:mid=(zl+zh)/2;nodes=[(ll,tl,th,zl,mid,path+'z'),(rr,tl,th,mid,zh,path+'Z')]
    bounds=[bound(v[0],v[1],v[2],v[3],v[4],delta) for v in nodes];score=sum(min(float(v),0) for v in bounds);choices.append((score,[v+(b,) for v,b in zip(nodes,bounds)]))
   stack.extend(reversed(max(choices,key=lambda v:v[0])[1]))
  if n%100==0:print(args.kind,n,len(good),len(stack),time.monotonic()-start,flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'kind':args.kind,'target':args.target,'root_t':[args.t_min,args.t_max],'status':'COMPLETE' if not stack and not failed else 'INCOMPLETE','accepted':good,'failed':failed,'pending_paths':[v[5] for v in stack],'processed':n,'worst':worst.str(80),'precision_bits':ctx.prec,'degrees':[nt,nz],'source_sha256':sha256(source.read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
 (here/f'{args.kind}_{args.label}.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],args.kind,len(good),len(stack),out['seconds'],flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--kind',choices=['M','B1','B2','B3','symDU','A','rho_y','rho_scaled'],required=True);ap.add_argument('--target',required=True);ap.add_argument('--t-min',default='0');ap.add_argument('--t-max',default='1');ap.add_argument('--label',default='global');ap.add_argument('--seconds',type=int,default=90);main(ap.parse_args())

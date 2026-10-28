"""Complete directed covers for the three original-state decay quantities."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import json,sys,time,argparse
from flint import arb,arb_mat,ctx
here=Path(__file__).parent;root=here.parents[2];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(root/'research/95_refit_global_hypotheses/verification'))
from norms_correlated import prepare
from correlated import ranges
from matrix import aa,halves,split
TARGETS={'Drho':F('19.94465'),'Du':F('1.85619'),'u':F('0.97743')}
def bounds(B,labels,kind,a,b,c,d,delta):
 wl=(1-aa(b))**aa(delta/2);wh=(1-aa(a))**aa(delta/2)
 W=arb_mat([[sum((aa(F(comb(n,k)*comb(i,k),comb(5,k)))*wl**(n-k)*(wh-wl)**k for k in range(min(n,i)+1)),arb(0)) for n in range(6)] for i in range(6)])
 values={}
 for label in labels:
  vals=(W*arb_mat([B[label,j].entries() for j in range(6)])).entries();upper=arb(0)
  for v in vals:upper=upper.max(abs(v))
  values[label]=upper
 corr=ranges(B,labels,range(6),delta,a,b)
 if corr:
  for label,(lo,hi) in corr.items():values[label]=values[label].min(abs(lo).max(abs(hi)))
 sq=lambda l:values[l]**2
 s2=arb(1) if c<=0<=d else 1-aa(min(abs(c),abs(d)))**2
 if kind=='u':raw=(1+aa(d))/2*sq('u1')+(1-aa(c))/2*sq('u2')
 elif kind=='Drho':raw=sq('ry')+s2*sq('rx')
 else:raw=2*sq('d22')+s2*(sq('d13')+sq('d31'))
 peak=F(2,5)/delta;x=min(max(peak,a),b)
 f=aa(x)**aa(F(2,5))*(1-aa(x))**aa(delta-F(2,5))
 return f*raw/aa(TARGETS[kind]**2)
def main(args):
 ctx.prec=448;start=time.monotonic();source=here/'polynomials.json';d=json.loads(source.read_text());kind0='u' if args.kind=='u' else 'fourth';B,nt,nz,labels=prepare(d,{'polynomials':{}},kind0);delta=F(d['delta']);Lt,Rt=halves(nt);Lz,Rz=halves(nz);stack=[(B,F(0),F(1),F(-1),F(1),'',None)];good=[];bad=[];count=0;dest=here/f'{args.kind}.json';prior=0
 if args.resume:
  old=json.loads(dest.read_text());assert old['status']=='INCOMPLETE' and old['polynomials_sha256']==sha256(source.read_bytes()).hexdigest();good=old['accepted'];bad=old['failed'];count=old['processed'];prior=old.get('cumulative_seconds',old['seconds']);stack=[]
  for path in old['pending_paths']:
   bb=B;a,b,c,e=F(0),F(1),F(-1),F(1)
   for ch in path:
    axis=ch.lower();l,r=split(bb,axis,Lt if axis=='t' else Lz,Rt if axis=='t' else Rz);bb=l if ch.islower() else r
    if ch=='t':b=(a+b)/2
    elif ch=='T':a=(a+b)/2
    elif ch=='z':e=(c+e)/2
    else:assert ch=='Z';c=(c+e)/2
   stack.append((bb,a,b,c,e,path,None))
 while stack and time.monotonic()-start<args.seconds:
  bb,a,b,c,e,path,cached=stack.pop();count+=1;upper=bounds(bb,labels,args.kind,a,b,c,e,delta) if cached is None else cached
  if upper<=1:good.append({'path':path,'t':[str(a),str(b)],'z':[str(c),str(e)],'ratio_upper':upper.str(85)})
  elif len(path)>=60:bad.append(path)
  else:
   choices=[]
   for axis in ['t','z']:
    ll,rr=split(bb,axis,Lt if axis=='t' else Lz,Rt if axis=='t' else Rz)
    if axis=='t':mid=(a+b)/2;nodes=[(ll,a,mid,c,e,path+'t'),(rr,mid,b,c,e,path+'T')]
    else:mid=(c+e)/2;nodes=[(ll,a,b,c,mid,path+'z'),(rr,a,b,mid,e,path+'Z')]
    vals=[bounds(x[0],labels,args.kind,x[1],x[2],x[3],x[4],delta) for x in nodes];score=sum(max(float(v)-1,0) for v in vals);choices.append((score,[x+(v,) for x,v in zip(nodes,vals)]))
   stack.extend(reversed(min(choices,key=lambda x:x[0])[1]))
  if count%100==0:print(args.kind,count,len(good),len(stack),time.monotonic()-start,flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'kind':args.kind,'target':str(TARGETS[args.kind]),'decay_exponent':'2/5','status':'COMPLETE' if not stack and not bad else 'INCOMPLETE','accepted':good,'failed':bad,'pending_paths':[x[5] for x in stack],'processed':count,'polynomials_sha256':sha256(source.read_bytes()).hexdigest(),'precision_bits':ctx.prec,'seconds':time.monotonic()-start,'cumulative_seconds':prior+time.monotonic()-start};dest.write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],args.kind,out['status'],len(good),'leaves',len(stack),'pending',out['seconds'],flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--kind',choices=list(TARGETS),required=True);ap.add_argument('--seconds',type=int,default=480);ap.add_argument('--resume',action='store_true');main(ap.parse_args())

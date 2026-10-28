from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
from math import comb
import json,sys,time,argparse
sys.set_int_max_str_digits(0)
from flint import arb,arb_mat,ctx
from matrix import aa,trans,halves,split,plus
here=Path(__file__).parent

def prepare(d,ext,kind):
 P={}
 for obj in [d,ext]:
  for key,rows in obj['polynomials'].items():P[key]={(i,k):F(v) for i,k,v in rows}
 if kind=='fourth':
  terms={'d22':[(1,'chi22')],'d13':[(1,'chi13')],'d31':[(1,'chi31')],'ry':[(-1,'chi22'),(-1,'chi04')],'rx':[(-1,'chi31'),(-1,'chi13')]}
 elif kind=='D2u':terms={l:[(1,l)] for l in ['chi41','chi32','chi23','chi14']}
 elif kind=='D2rho':terms={'ryy':[(-1,'chi23'),(-1,'chi05')],'rxy':[(-1,'chi32'),(-1,'chi14')],'rxx':[(-1,'chi41'),(-1,'chi23')]}
 else:terms={l:[(1,l)] for l in ['u1','u2']}
 S={(label,j):plus(*[(v,P[f'{key}_{j}']) for v,key in ts]) for label,ts in terms.items() for j in range(6)}
 nt=max(i for p in S.values() for i,k in p);nz=max(k for p in S.values() for i,k in p);T=trans(nt,'0','1');Z=trans(nz,'-1','1').transpose();B={}
 for key,p in S.items():
  m=arb_mat(nt+1,nz+1)
  for (i,k),v in p.items():m[i,k]=aa(v)
  B[key]=T*m*Z
 return B,nt,nz,list(terms)
def bound(B,labels,kind,tl,th,zl,zh,delta):
 wl=(1-aa(th))**aa(delta/2);wh=(1-aa(tl))**aa(delta/2)
 W=arb_mat([[sum((aa(F(comb(n,k)*comb(i,k),comb(5,k)))*wl**(n-k)*(wh-wl)**k for k in range(min(n,i)+1)),arb(0)) for n in range(6)] for i in range(6)])
 values={}
 for l in labels:
  vals=(W*arb_mat([B[l,j].entries() for j in range(6)])).entries();up=abs(vals[0])
  for x in vals[1:]:up=up.max(abs(x))
  values[l]=up
 from correlated import ranges
 rr=ranges(B,labels,range(6),delta,tl,th)
 if rr is not None:
  for label,(lo,hi) in rr.items():values[label]=values[label].min(abs(lo).max(abs(hi)))
 sx=(1+aa(zh))/2;sy=(1-aa(zl))/2;s2=arb(1) if zl<=0<=zh else 1-aa(min(abs(zl),abs(zh)))**2
 def sq(l):return values[l]**2
 t=aa(th);w2=wh**2
 if kind=='fourth':
  du=2*sq('d22')+s2*(sq('d13')+sq('d31'));dr=sq('ry')+s2*sq('rx')
  ratios={'Du_fixed':w2*du/aa(F(14,5)**2),'Drho_fixed':w2*dr/256,'Du_decay':du/484,'Drho_decay_half':dr/8649}
 elif kind=='D2u':
  raw=sy*(sq('chi41')+3*sq('chi23'))+sx*(3*sq('chi32')+sq('chi14'))
  ratios={'D2u_fixed':t*w2*raw/9,'D2u_decay':t*t*raw/3136}
 elif kind=='D2rho':
  raw=sy*(sq('rxx')+sq('ryy'))+2*sx*sq('rxy');peak=F(1,4) if tl<=F(1,2)<=th else max(tl*(1-tl),th*(1-th))
  ratios={'D2rho_fixed':aa(peak)*w2*raw/9,'D2rho_weighted':t*w2*raw/64,'D2rho_decay_half':t*t*raw/8649}
 else:ratios={'u_decay':(sx*sq('u1')+sy*sq('u2'))/484}
 upper=arb(0)
 for v in ratios.values():upper=upper.max(v)
 return upper,ratios

def run(args):
 ctx.prec=512;start=time.monotonic();p=here/f'{args.name}.polynomials.json';e=here/f'{args.name}.derivatives.json';d=json.loads(p.read_text());ext=json.loads(e.read_text());assert d['source_sha256']==ext['source_sha256'];delta=F(d['delta']);assert delta>F(4,9);B,nt,nz,labels=prepare(d,ext,args.kind);Lt,Rt=halves(nt);Lz,Rz=halves(nz);good=[];bad=[];stack=[(B,F(0),F(1),F(-1),F(1),'',None)];processed=0;previous_seconds=0;previous_hash=None
 print(args.kind,'prepared',nt,nz,time.monotonic()-start,flush=True)
 output=here/f'{args.name}.{args.kind}.correlated.json'
 if args.resume:
  prior=json.loads(output.read_text());assert prior['status']=='INCOMPLETE' and prior['source_sha256']==sha256(p.read_bytes()).hexdigest() and prior['derivatives_sha256']==sha256(e.read_bytes()).hexdigest();previous_hash=sha256(output.read_bytes()).hexdigest();previous_seconds=prior.get('cumulative_seconds',prior['seconds']);good=prior['accepted'];bad=prior['failed'];processed=prior['processed'];stack=[]
  for path in prior['pending_paths']:
   bb=B;tl,th,zl,zh=F(0),F(1),F(-1),F(1)
   for letter in path:
    axis=letter.lower();ll,rr=split(bb,axis,Lt if axis=='t' else Lz,Rt if axis=='t' else Rz);bb=ll if letter.islower() else rr
    if axis=='t':
     mid=(tl+th)/2
     if letter=='t':th=mid
     else:tl=mid
    else:
     mid=(zl+zh)/2
     if letter=='z':zh=mid
     else:zl=mid
   stack.append((bb,tl,th,zl,zh,path,None))
 while stack and time.monotonic()-start<args.seconds:
  B,tl,th,zl,zh,path,cached=stack.pop();processed+=1;upper,ratios=bound(B,labels,args.kind,tl,th,zl,zh,delta) if cached is None else cached
  if upper<=1:good.append({'path':path,'t':[str(tl),str(th)],'z':[str(zl),str(zh)],'ratios':{k:v.str(75) for k,v in ratios.items()}})
  elif len(path)>=60:bad.append(path)
  else:
   choices=[]
   for axis in ['t','z']:
    ll,rr=split(B,axis,Lt if axis=='t' else Lz,Rt if axis=='t' else Rz)
    if axis=='t':mid=(tl+th)/2;nodes=[(ll,tl,mid,zl,zh,path+'t'),(rr,mid,th,zl,zh,path+'T')]
    else:mid=(zl+zh)/2;nodes=[(ll,tl,th,zl,mid,path+'z'),(rr,tl,th,mid,zh,path+'Z')]
    bs=[bound(n[0],labels,args.kind,n[1],n[2],n[3],n[4],delta) for n in nodes];score=sum(max(float(v[0])-1,0) for v in bs);choices.append((score,[n+(b,) for n,b in zip(nodes,bs)]))
   stack.extend(reversed(min(choices,key=lambda x:x[0])[1]))
  if processed%20==0:print(args.kind,processed,len(good),len(stack),time.monotonic()-start,flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'kind':args.kind,'name':args.name,'status':'COMPLETE' if not stack and not bad else 'INCOMPLETE','accepted':good,'failed':bad,'pending_paths':[x[5] for x in stack],'processed':processed,'degrees':[nt,nz],'seconds':time.monotonic()-start,'cumulative_seconds':previous_seconds+time.monotonic()-start,'previous_result_sha256':previous_hash,'source_sha256':sha256(p.read_bytes()).hexdigest(),'derivatives_sha256':sha256(e.read_bytes()).hexdigest(),'precision_bits':ctx.prec,'radial_enclosure':'Taylor degree4 or independent branch variable'}
 output.write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],args.kind,len(good),len(stack),out['seconds'],flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--name',default='nb_d2_exact');ap.add_argument('--kind',choices=['fourth','D2u','D2rho','u'],required=True);ap.add_argument('--seconds',type=int,default=480);ap.add_argument('--resume',action='store_true');run(ap.parse_args())

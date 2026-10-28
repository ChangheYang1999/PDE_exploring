"""Independent exact high principal-matrix certificate, state131."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sys,json,time,argparse
from flint import arb,arb_mat,ctx
BASE=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(BASE/'02_energy'/'verification'))
from compact_matrix import A,add,derivative,chebyshev,encode
import compact_certificate as cc
cc.NT=30;cc.NZ=12

def construct(state=131):
 d=json.loads((BASE/'source_audit'/f'state{state:03d}_exact.json').read_text());gamma=1/Q(d['exact_parameters']['cl']);delta=1-gamma
 P={}
 for branch in range(4):
  p=(3+gamma-branch*delta)/2
  for label,axes in [('chi22','xxyy'),('chi04','yyyy'),('chi31','xxxy'),('chi13','xyyy'),('rad','')]:
   trig={}
   for (j,m,k),a in zip(d['canonical_order'],d['canonical_coefficients']):
    if j!=branch:continue
    if label!='rad':
     T={('c',2*m,0):Q(a)}
     for di,axis in enumerate(axes):T=derivative(T,p,k,di,axis)
     for (kind,n,l),v in T.items():add(trig,kind,n,k-2+l,v)
    else:
     for axes3,sgn in [('xyy',-1),('xxy',1)]:
      T={('c',2*m,0):Q(a)}
      for di,axis in enumerate(axes3):T=derivative(T,p,k,di,axis)
      for (kind,n,l),v in T.items():
       if axes3=='xyy':
        assert kind=='c'
        add(trig,'c',n+1,k-1+l,-v/2);add(trig,'c',n-1,k-1+l,-v/2)
       else:
        assert kind=='s'
        add(trig,'c',n-1,k-1+l,v/2);add(trig,'c',n+1,k-1+l,-v/2)
   assert all(l>=0 for kind,n,l in trig)
   po={}
   for (kind,n,l),v in trig.items():
    assert n%2==0
    assert kind==('s' if label in ['chi31','chi13'] else 'c')
    C=chebyshev(n//2-1,'U') if kind=='s' else chebyshev(n//2)
    for zdeg,b in enumerate(C):po[l,zdeg]=po.get((l,zdeg),Q(0))+v*b
   P[label,branch]={key:v for key,v in po.items() if v}
 return d,delta,P

def mul_linear(P,a,b):
 out={}
 for (i,j),v in P.items():
  out[i,j]=out.get((i,j),Q(0))+a*v
  out[i+1,j]=out.get((i+1,j),Q(0))+b*v
 return out

def combine(*terms):
 out={}
 for scale,P in terms:
  for key,v in P.items():out[key]=out.get(key,Q(0))+scale*v
 return {key:v for key,v in out.items() if v}

def load(P,c,k,rad,sig,target=Q(1,2)):
 rr=rad*rad;tau=k-1-sig;b=1+(1-k)*c
 scalar={(0,0):(b-target)*rr,(1,0):(b-target)*(1-rr)+tau*c}
 tt=cc.transforms(cc.NT);tz=cc.transforms(cc.NZ,Q(-1),Q(1)).transpose()
 B={}
 for j in range(4):
  polys={
   'a':combine((Q(1),mul_linear(combine((k-1,P['chi22',j]),(-1,P['chi04',j])),rr,1-rr)),(tau,P['rad',j])),
   'b':combine((-k,mul_linear(P['chi22',j],rr,1-rr)),(tau,P['rad',j])),
   'c':mul_linear(combine(((1-k)/2,P['chi31',j]),((1+k)/2,P['chi13',j])),rr,1-rr)}
  for label,po in polys.items():
   mat=arb_mat(cc.NT+1,cc.NZ+1)
   for (i,z),v in po.items():mat[i,z]=A(v)
   B[label,j]=tt*mat*tz
 smat=arb_mat(cc.NT+1,cc.NZ+1)
 for (i,z),v in scalar.items():smat[i,z]=A(v)
 B['scalar',0]=tt*smat*tz
 return B

def bound(B,tl,th,zl,zh,delta):
 wl=(1-A(th))**(A(delta)/2);wu=(1-A(tl))**(A(delta)/2);W=cc.wcoeff(wl,wu)
 ranges={}
 for label in ['a','b','c']:
  mat=W*arb_mat([B[label,j].entries() for j in range(4)])
  if label!='c':
   scal=B['scalar',0].entries()
   vals=[mat[i,n]+scal[n] for i in range(5) for n in range(len(scal))]
  else:vals=mat.entries()
  ranges[label]=cc.hull(vals)
 al,ah=ranges['a'];bl,bh=ranges['b'];cl,ch=ranges['c']
 si=arb(1) if zl<=0<=zh else (1-A(min(abs(zl),abs(zh)))**2).sqrt()
 off=abs(cl).max(abs(ch))*si
 low=(al+bl-((al-bl)**2+4*off**2).sqrt())/2
 return low.max(al.min(bl)-off)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--k',default='2');ap.add_argument('--radius',default='1/2');ap.add_argument('--sigma',default='1/5');ap.add_argument('--seconds',type=int,default=480);ap.add_argument('--adaptive',action='store_true');ap.add_argument('--target',default='1/2');ap.add_argument('--tag',default='');args=ap.parse_args()
 ctx.prec=320;start=time.monotonic();k=Q(args.k);rad=Q(args.radius);sig=Q(args.sigma)
 pfile=Path(__file__).with_name('state131_high_symbol_polynomials.json')
 if pfile.exists():
  raw=json.loads(pfile.read_text());d=json.loads((BASE/'source_audit'/'state131_exact.json').read_text());delta=Q(raw['delta']);P={(key.rsplit('_',1)[0],int(key.rsplit('_',1)[1])):{(i,j):Q(v) for i,j,v in vals} for key,vals in raw['polynomials'].items()}
  assert raw['input_sha256']==d['canonical_serialization_sha256']
 else:
  d,delta,P=construct();pfile.write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'input_sha256':d['canonical_serialization_sha256'],'delta':str(delta),'polynomials':{f'{label}_{j}':encode(po) for (label,j),po in P.items()}},indent=2)+'\n')
 B=load(P,Q(d['exact_parameters']['cl']),k,rad,sig,Q(args.target));Lt,Rt=cc.split_matrices(cc.NT);Lz,Rz=cc.split_matrices(cc.NZ)
 stack=[(B,Q(0),Q(1),Q(-1),Q(1),'',0,0)];accepted=[];failed=[];processed=0;worst=arb(100)
 while stack and time.monotonic()-start<args.seconds:
  b,tl,th,zl,zh,path,dt,dz=stack.pop();processed+=1;low=bound(b,tl,th,zl,zh,delta)
  if low>=0:
   accepted.append({'path':path,'t':[str(tl),str(th)],'z':[str(zl),str(zh)],'lower_numerator_after_target':low.str(50)});worst=worst.min(low)
  elif dt+dz>=80:failed.append({'path':path,'lower':low.str(50)})
  else:
   axis='t' if dt<=dz+2 else 'z'
   if args.adaptive:
    tlb,trb=cc.split(b,'t',Lt,Rt);zlb,zrb=cc.split(b,'z',Lz,Rz);tm=(tl+th)/2;zm=(zl+zh)/2
    tscore=min(float(bound(tlb,tl,tm,zl,zh,delta).mid()),float(bound(trb,tm,th,zl,zh,delta).mid()))
    zscore=min(float(bound(zlb,tl,th,zl,zm,delta).mid()),float(bound(zrb,tl,th,zm,zh,delta).mid()))
    axis='t' if tscore>=zscore else 'z'
   if axis=='t':
    left,right=cc.split(b,axis,Lt,Rt);tm=(tl+th)/2
    stack.extend([(right,tm,th,zl,zh,path+'T',dt+1,dz),(left,tl,tm,zl,zh,path+'t',dt+1,dz)])
   else:
    left,right=cc.split(b,axis,Lz,Rz);zm=(zl+zh)/2
    stack.extend([(right,tl,th,zm,zh,path+'Z',dt,dz+1),(left,tl,th,zl,zm,path+'z',dt,dz+1)])
  if processed%100==0:print('k',k,'cells',processed,'accepted',len(accepted),'failed',len(failed),'pending',len(stack),'sec',round(time.monotonic()-start,2),flush=True)
 status='COMPLETE' if not stack and not failed else 'INCOMPLETE'
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'status':status,'state':131,'input_sha256':d['canonical_serialization_sha256'],'k':str(k),'radius':str(rad),'sigma':str(sig),'target':str(Q(args.target)),'precision_bits':ctx.prec,'processed':processed,'pending':len(stack),'accepted':accepted,'failed':failed,'pending_paths':[x[5] for x in stack],'worst_numerator_after_target':worst.str(50),'elapsed_seconds':time.monotonic()-start}
 dest=Path(__file__).with_name('state131_high_symbol_k'+str(k).replace('/','_')+('_adaptive' if args.adaptive else '')+args.tag+'.json');dest.write_text(json.dumps(out,indent=2)+'\n')
 print(status,k,len(accepted),len(failed),len(stack),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

"""Whole-plane radial-scale weak probes in the exact finite-power class."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,sys,time
from flint import fmpq as Q,fmpq_poly,arb,arb_poly,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
from radial import Radial,ar,pshift
from pipeline import load,source,DATA
U=fmpq_poly([1,-1]);T=fmpq_poly([0,1]);AU=arb_poly([1,-1]);X=arb_poly([0,1])
def digest(p):return sha256(p.read_bytes()).hexdigest()
def ap(poly):return arb_poly([ar(v) for v in poly])
def integral(poly,b):
 assert b>-1,str(b)
 return sum((v/ar(b+j+1) for j,v in enumerate(poly)),arb(0))
def supremum(a,b):return Q(a**a*b**b,(a+b)**(a+b)) if a else Q(1)
def groups(model,labels):
 result={}
 for label in labels:
  fields,a,kind=model.fields[label];by_n={}
  for (j,n),poly in fields.items():by_n.setdefault(n,[]).append((j,ap(pshift(poly,2)(U))))
  for n,rows in by_n.items():
   for i,(j,P) in enumerate(rows):
    for ii in range(i,len(rows)):
     jj,PP=rows[ii];b=Q(5)-model.p[j]-model.p[jj]
     factor=(2 if kind=='c' and n==0 else 1)*(1 if i==ii else 2)
     result[b]=result.get(b,arb_poly([]))+factor*P*PP
 return result

def run(name,ks,bits):
 start=time.monotonic();ctx.prec=bits;path=source(name);model=Radial(path)
 D=load(name,0)[0,0];F=[]
 for (ell,kind,n),poly in D.items():
  assert kind=='s'
  if n==1:F.append((ell,ap(poly(U))))
 del D
 bg=groups(model,['u1','u2']);cg=groups(model,['rho_x','rho_y'])
 print('prepared',name,'seconds',time.monotonic()-start,flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,'precision_bits':bits,
      'source_sha256':digest(path),'residual_sha256':digest(DATA/f'{name}_D0.json.gz'),
      'code_sha256':digest(Path(__file__)),'proof_sha256':digest(ROOT/'research/localized_weak_probe/PROOF.md'),
      'scope':'Necessary L2 correction size at fixed c; divergence-form solutions; no gradient cap. N4-ORIGIN.','probes':[]}
 for k in ks:
  startk=time.monotonic();W=AU**(2*k+1);weight=1+2*k*X+4*AU
  B2=arb.pi()/2*sum((integral(P*W*weight*weight,b) for b,P in bg.items()),arb(0))
  C2=arb.pi()/2*sum((integral(P*W,b) for b,P in cg.items()),arb(0))
  aa=Q(2*k+2);bb=Q(2);l0=3*model.c+1+2*model.c*k;l1=2*model.c*(k+2)
  A2=arb.pi()/2*ar((l0*l0-2*l0*l1*aa/(aa+bb)+l1*l1*aa*(aa+1)/((aa+bb)*(aa+bb+1)))/(aa*(aa+1)))
  assert A2>0 and B2>0 and C2>0,(k,A2,B2,C2)
  pair=arb.pi()/2*sum((integral(P*AU**(k+1),ell*model.delta/2-1) for ell,P in F),arb(0))
  A,B,C=[v.sqrt() for v in [A2,B2,C2]];linear=A+B+C
  H=Q(1) if k==0 else supremum(k,2)+2*k*supremum(k,3)+4*supremum(k+1,2)
  I=abs(pair);assert I>0,(k,pair)
  lower=2*I/(linear+(linear*linear+4*ar(H)*I).sqrt())
  row={'k':k,'p':2,'pairing':pair.str(80),'A':A.str(80),'B_weighted':B.str(80),'C':C.str(80),
       'D':linear.str(80),'gradient_sup_upper_exact':str(H),'L2_radius_lower':lower.str(80),
       'elapsed_seconds':time.monotonic()-startk}
  out['probes'].append(row);out['total_elapsed_seconds']=time.monotonic()-start
  (ROOT/f'research/localized_weak_probe/verification/{name}_{bits}.json').write_text(json.dumps(out,indent=2)+'\n')
  print('k',k,'pair',pair.str(15),'D',linear.str(15),'L2 lower',lower.str(18),'seconds',row['elapsed_seconds'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('candidate');p.add_argument('--k',nargs='+',type=int,default=[0,1,2,4,8,16,32,64,128]);p.add_argument('--bits',type=int,default=2048)
 args=p.parse_args();assert all(k>=0 for k in args.k);run(args.candidate,args.k,args.bits)

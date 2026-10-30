"""Exact compact-annular weak probes, with arbitrary rational radii."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,sys,time
from flint import fmpq as Q,fmpq_poly,arb,arb_poly,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
sys.path.insert(0,str(ROOT/'research/localized_weak_probe/code'))
from radial import Radial,ar
from pipeline import load,source,DATA
from evaluate import groups
S=fmpq_poly([0,1]);U=fmpq_poly([1,-1]);AU=arb_poly([1,-1])
QPOL=(S-1)**2*(4-S)**2
WPOL=QPOL**2+(QPOL+2*S*QPOL.derivative())**2

def sha(p):return sha256(p.read_bytes()).hexdigest()
def ap(P):return arb_poly([ar(v) for v in P])
def integral(P,b,lo,hi):
 e=b+1;pvlo=lo**ar(e);pvhi=hi**ar(e);ans=arb(0)
 for j,v in enumerate(P):
  ex=e+j
  ans+=v*((pvhi-pvlo)/ar(ex) if ex else (hi/lo).log())
  pvlo*=lo;pvhi*=hi
 return ans

def exact_integral(P,a,b):
 return sum((v*(b**(k+1)-a**(k+1))/Q(k+1) for k,v in enumerate(P)),Q(0))

def prepared_terms(group,weight):
 return [(k,v,b-4-k,P*AU**(k+1)) for b,P in group.items() for k,v in enumerate(weight) if v]

def run(name,rs,bits):
 ctx.prec=bits;start=time.monotonic();path=source(name);model=Radial(path)
 drift=(3*model.c+1)*QPOL+2*model.c*S*QPOL.derivative()
 A2=arb.pi()/2*ar(exact_integral(S*drift**2,Q(1),Q(4)));assert A2>0
 A=A2.sqrt();bg=prepared_terms(groups(model,['u1','u2']),WPOL)
 cg=prepared_terms(groups(model,['rho_x','rho_y']),QPOL**2)
 D=load(name,0)[0,0];ff=[]
 for (ell,kind,n),P in D.items():
  assert kind=='s'
  if n==1:
   shifted=ap(P(U))
   ff.extend((k,v,ell*model.delta/2-3-k,shifted*AU**(k+1)) for k,v in enumerate(QPOL) if v)
 del D
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,'precision_bits':bits,
  'source_sha256':sha(path),'residual_sha256':sha(DATA/f'{name}_D0.json.gz'),
  'code_sha256':sha(Path(__file__)),'proof_sha256':sha(ROOT/'research/annular_weak_probe/PROOF.md'),
  'grouping_code_sha256':sha(ROOT/'research/localized_weak_probe/code/evaluate.py'),
  'scope':'Necessary global L2 correction size at fixed c from compact C1 annular tests; no gradient cap. N4-ORIGIN.',
  'probes':[]}
 print('prepared',name,'seconds',time.monotonic()-start,flush=True)
 for rstr in rs:
  sk=time.monotonic();R=Q(rstr);assert R>0
  lo=ar(1/(1+4*R*R));hi=ar(1/(1+R*R));assert hi>lo>0
  factors={k:ar(R**(-2*k)) for k in range(9)}
  def terms_integral(terms):
   return sum((ar(v)*factors[k]*integral(P,b,lo,hi) for k,v,b,P in terms),arb(0))
  pair=arb.pi()/ar(2*R*R)*terms_integral(ff)
  B2=arb.pi()/ar(2*R**4)*terms_integral(bg)
  C2=arb.pi()/ar(2*R**4)*terms_integral(cg)
  assert B2>0 and C2>0,(R,B2,C2)
  B,C=B2.sqrt(),C2.sqrt();linear=A+B+C;H=Q(108)/(R*R);I=abs(pair);assert I>0
  lower=2*I/(linear+(linear*linear+4*ar(H)*I).sqrt())
  out['probes'].append({'R_exact':str(R),'pairing':pair.str(80),'A':A.str(80),'B':B.str(80),'C':C.str(80),
    'D':linear.str(80),'gradient_sup_upper_exact':str(H),'L2_radius_lower':lower.str(80),'elapsed_seconds':time.monotonic()-sk})
  out['total_elapsed_seconds']=time.monotonic()-start
  dest=ROOT/f'research/annular_weak_probe/verification/{name}_{bits}.json'
  dest.write_text(json.dumps(out,indent=2)+'\n')
  print('R',R,'pair',pair.str(14),'D',linear.str(14),'L2 lower',lower.str(20),'seconds',time.monotonic()-sk,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('candidate');p.add_argument('--R',nargs='+',default=['1','2','4','8','16','32','64','128','256','512','1024','4096','16384']);p.add_argument('--bits',type=int,default=2048)
 a=p.parse_args();run(a.candidate,a.R,a.bits)

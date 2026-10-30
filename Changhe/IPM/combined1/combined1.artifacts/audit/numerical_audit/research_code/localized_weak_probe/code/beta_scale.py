"""Localized weak probes at large k using beta recurrences."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,sys,time
from flint import fmpq as Q,arb,arb_poly,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from evaluate import groups,ap,U,Radial,ar,load,source,DATA

def sha(p):return sha256(p.read_bytes()).hexdigest()
def integral(P,b,M):
 assert b>-1 and M>=0
 value=ar(b+1).gamma()*arb(M+1).gamma()/ar(b+M+2).gamma()
 result=arb(0)
 for j,p in enumerate(P):
  result+=p*value
  value*=ar((b+j+1)/(b+j+M+2))
 return result

def supremum(a,b):
 return (ar(Q(a,a+b))**a)*(ar(Q(b,a+b))**b) if a else arb(1)

def run(name,ks,bits):
 ctx.prec=bits;start=time.monotonic();path=source(name);model=Radial(path)
 bg=groups(model,['u1','u2']);cg=groups(model,['rho_x','rho_y'])
 D=load(name,0)[0,0];F=[]
 for (ell,kind,n),P in D.items():
  assert kind=='s'
  if n==1:F.append((ell,ap(P(U))))
 del D
 refpath=ROOT/f'research/localized_weak_probe/verification/{name}_2048.json'
 refs={v['k']:v for v in json.loads(refpath.read_text())['probes']} if refpath.exists() else {}
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,'precision_bits':bits,
 'source_sha256':sha(path),'residual_sha256':sha(DATA/f'{name}_D0.json.gz'),'code_sha256':sha(Path(__file__)),
 'proof_sha256':sha(ROOT/'research/localized_weak_probe/BETA_EVALUATION.md'),
 'direct_power_reference_sha256':sha(refpath) if refpath.exists() else None,'probes':[],
 'scope':'Finite prescribed integer k; same necessary L2 correction bound; gamma-beta integral evaluation. N4-ORIGIN.'}
 print('prepared',name,'seconds',time.monotonic()-start,flush=True)
 for k in ks:
  sk=time.monotonic();weight=arb_poly([5,2*k-4])
  B2=arb.pi()/2*sum((integral(P*weight*weight,b,2*k+1) for b,P in bg.items()),arb(0))
  C2=arb.pi()/2*sum((integral(P,b,2*k+1) for b,P in cg.items()),arb(0))
  aa=Q(2*k+2);l0=3*model.c+1+2*model.c*k;l1=2*model.c*(k+2)
  A2=arb.pi()/2*ar((l0*l0-2*l0*l1*aa/(aa+2)+l1*l1*aa*(aa+1)/((aa+2)*(aa+3)))/(aa*(aa+1)))
  assert A2>0 and B2>0 and C2>0,(k,A2,B2,C2)
  pair=arb.pi()/2*sum((integral(P,ell*model.delta/2-1,k+1) for ell,P in F),arb(0))
  A,B,C=[v.sqrt() for v in [A2,B2,C2]];linear=A+B+C
  H=arb(1) if k==0 else supremum(k,2)+2*k*supremum(k,3)+4*supremum(k+1,2)
  I=abs(pair);assert I>0
  lower=2*I/(linear+(linear*linear+4*H*I).sqrt())
  vals={'pairing':pair,'A':A,'B_weighted':B,'C':C,'D':linear,'L2_radius_lower':lower}
  comparisons={}
  if k in refs:
   comparisons={key:v.overlaps(arb(refs[k][key])) for key,v in vals.items()}
   comparisons['H']=H.overlaps(ar(Q(refs[k]['gradient_sup_upper_exact'])))
   assert all(comparisons.values()),(k,comparisons)
  row={'k':k,'p':2,**{key:v.str(80) for key,v in vals.items()},'gradient_sup_upper_ball':H.str(80),
       'direct_power_comparisons':comparisons,'elapsed_seconds':time.monotonic()-sk}
  out['probes'].append(row);out['total_elapsed_seconds']=time.monotonic()-start
  dest=ROOT/f'research/localized_weak_probe/verification/{name}_beta_{bits}.json'
  dest.write_text(json.dumps(out,indent=2)+'\n')
  print('k',k,'pair',pair.str(14),'D',linear.str(14),'L2 lower',lower.str(22),'comparisons',len(comparisons),'seconds',time.monotonic()-sk,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('candidate');p.add_argument('--k',nargs='+',type=int,default=[0,128,256,512,1024,2048,4096,8192,16384,65536,262144,1048576,16777216,268435456]);p.add_argument('--bits',type=int,default=2048)
 a=p.parse_args();assert all(k>=0 for k in a.k);run(a.candidate,a.k,a.bits)

from pathlib import Path
from datetime import datetime,timezone
from math import factorial
import sys,json,hashlib,time
import numpy as np
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'inner-cutoff/code'));sys.path.insert(0,str(ROOT.parent/'exact-data/code'))
from hessian import binary,tensor_coefficients
from nodal_input import export,load

def bessel(n,z,K=64):
 if n<0:return ((-1)**(-n))*bessel(-n,z,K)
 t=(z/2)**n/factorial(n);total=arb(0)
 for a in range(K):
  total+=t;t*=-z*z/(4*(a+1)*(n+a+1))
 ratio=arb(9)/(4*(K+1)*(n+K+1));assert ratio<1 and abs(z)<3
 remainder=t.abs_upper()/(1-ratio)
 return total+arb(0,remainder)

def angular_weights(M,beta,K=64):
 cache={(l,j):bessel(j,l*beta,K) for l in (1,2,3) for j in range(-M-3,M)}
 def I(m,l):
  if l==0:return arb(1 if m==0 else 0)+(beta/2 if m==1 else 0)
  if m==0:return arb(0)
  return arb(m)/(2*l)*(cache[l,m-l]-cache[l,-m-l])
 return [(I(m,0)+I(m,1)-I(m,2)-I(m,3))/4 for m in range(M)]

def moment(co,L,cl,beta,K=64):
 weights=angular_weights(len(co[0]),beta,K)
 c=sum((co[n][m]*weights[m]/(1-n*n) for n in range(0,len(co),2) for m in range(len(weights))),arb(0))*L*L/(1-1/cl)
 return c

def tests():
 ctx.prec=192
 ws=angular_weights(14,arb(0));expected=[arb(1)/4,arb(1)/8,-arb(1)/8,-arb(1)/8]+[arb(0)]*10
 assert all((a-b).contains(0) for a,b in zip(ws,expected))
 for n in range(-8,9):
  for z in [arb(0),arb('0.9'),arb('-0.9'),arb('2.7')]:
   assert (bessel(n,z)-z.bessel_j(n)).contains(0)
 # Independent nonzero-warp floating angular integration.
 from scipy.integrate import quad
 import math
 beta=.9;ww=angular_weights(12,binary(beta))
 for m,w in enumerate(ww):
  def f(s):
   t=s+beta*math.sin(2*s)/2
   return (4/math.pi)*math.cos(t)**2*math.sin(t)*math.sin(3*t)*math.cos(2*m*s)*(1+beta*math.cos(2*s))
  q,e=quad(f,0,math.pi/2,epsabs=2e-13,epsrel=2e-13,limit=100);assert abs(float(w)-q)<1e-12
 c=moment([[arb(1)]],arb(2),arb(6),arb('.9'));assert (c-arb(6)/5).contains(0)
 print('MANUFACTURED_FULL_PLANE_CENTER_MOMENT_PASS',flush=True)

if __name__=='__main__':
 tests()
 if '--test' in sys.argv:raise SystemExit
 files=['grid-states/data/dnB_n96m40S.npz','ritz-resolution/data/dnSB_n120m48.npz','domain-states/data/dnB_n96m40SL4.npz','fixed-cl-correction/data/n96m40S_radius0.05.npz','fixed-cl-correction/data/n120m48_S_radius0.05.npz']
 out={'date_start':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'scope':'Exact binary ideal-node field, rigorous full-plane center strain only; not a full residual or profile certificate.','rows':[]}
 for rel in files:
  src=ROOT.parent/rel;target=ROOT/'data'/(src.stem+'.json');export(src,target);o,b,p,jhash=load(target);print('START',rel,datetime.now(timezone.utc).isoformat(),flush=True);t=time.monotonic();co=tensor_coefficients(b);L=binary(p['L']);cl=binary(p['c_l']);beta=binary(p['beta']);assert L>0 and cl>1 and abs(beta)<1 and o['N']>0 and o['M']>0;assert all(x==1 for x in b[0])
  c64=moment(co,L,cl,beta,64);c96=moment(co,L,cl,beta,96);assert (c64-c96).contains(0);defect=3*cl-1-c96
  row={'source':rel,'source_sha256':o['source_sha256'],'source_md5':hashlib.md5(src.read_bytes()).hexdigest(),'exact_json':str(target.relative_to(ROOT)),'json_sha256':jhash,'N':o['N'],'M':o['M'],'c64':c64.str(40),'c96':c96.str(40),'c_midpoint_float':float(c96.mid()),'self_consistency_ball':defect.str(40),'self_consistency_contains_zero':defect.contains(0),'self_consistency_midpoint_float':float(defect.mid()),'seconds':time.monotonic()-t}
  out['rows'].append(row);(ROOT/'verification/certificates.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(row),flush=True)
 out['complete']=True;out['date_end']=datetime.now(timezone.utc).isoformat();out['dependencies']=[{'file':str(p.relative_to(ROOT.parent.parent)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [Path(__file__),ROOT/'PROOF.md',ROOT.parent/'inner-cutoff/code/hessian.py',ROOT.parent/'exact-data/code/nodal_input.py']];(ROOT/'verification/certificates.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['date_end'],flush=True)

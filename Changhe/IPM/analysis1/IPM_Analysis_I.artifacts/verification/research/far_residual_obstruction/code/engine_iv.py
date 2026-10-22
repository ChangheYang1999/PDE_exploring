"""Raw NPZ Laurent multiplication and direct radial/tangential iv180 products.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[key]='1'
import json,hashlib,sys,time
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/far_residual_obstruction';E=D/'evidence'
P=Path('numerics/data/trial_v2_h0.008.npz')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()
def a(q):q=Q(q);return iv.mpf(q.numerator)/q.denominator
def rf(p):
 sg,m,e,bc=p;assert bc>=0
 return Q(-int(m) if sg else int(m))*Q(2)**int(e)
def box(x):
 lo,hi=map(rf,x._mpi_);assert lo<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'display':str(x)}
def mul(x,y):
 out={}
 for i,q in x.items():
  for j,r in y.items():out[i+j]=out.get(i+j,Q(0))+q*r
 return {i:q for i,q in out.items() if q}
def run():
 st=time.monotonic();iv.dps=180
 assert sha(P)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 with np.load(P,allow_pickle=False) as raw:
  assert raw['Aout'].shape==(260,10);A=raw['Aout'].copy();k=Q(float(raw['k']));t=Q(float(raw['knots'][-1]));bo=Q(float(raw['bo']))
 assert 0<k<Q(1,2) and bo>120;aa=k+1;beta=2*k-1
 # Laurent coefficients of 2i*cos(theta)^2*sin(theta), built as three products.
 base=mul(mul({1:Q(1,2),-1:Q(1,2)},{1:Q(1,2),-1:Q(1,2)}),{1:Q(1),-1:Q(-1)})
 series=[]
 for col in (0,1):
  f={}
  for m in range(260):
   q=Q(float(A[m,col]))/2
   for freq in (2*m,-2*m):f[freq]=f.get(freq,Q(0))+q
  series.append(mul(base,f))
 zd=base;ds=[];bs=[];zs=[]
 for j in range(262):
  nu=2*j+1;ds.append(series[0].get(nu,Q(0)));bs.append(series[1].get(nu,Q(0)));zs.append(zd.get(nu,Q(0)))
  for f in series+[zd]:assert f.get(-nu,Q(0))==-f.get(nu,Q(0))
 assert len(series[0])==len(series[1])==522 and ds[-1]==bs[-1]==zs[-1]==0
 norm=B/'research/modal_repair/evidence/independent_gauss_iv.json';nr=json.loads(norm.read_text());zb=nr['values']['A00_correction'];lo,hi=[Q(zb[key]) for key in ('lower_exact_dyadic','upper_exact_dyadic')];assert lo<=hi
 z=iv.mpf([a(lo).a,a(hi).b]);dens=[a(q)+a(s)*z for q,s in zip(ds,zs)];product=iv.mpf(0);witness=[]
 for n in range(1,262):
  m=2*n;den=m*m-aa*aa;assert den>0
  F=(a(aa-m)*dens[n-1]+a(aa+m)*dens[n])/2
  # Direct Green factors: qplus=F/(m-aa), qminus=F/(m+aa).
  qp=F/a(m-aa);qm=F/a(m+aa);v=-(qp+qm)/2;w=(qp-qm)/2
  radial=a(k)*v*(dens[n]-dens[n-1])/2
  angular=w*((m-1)*dens[n-1]-(m+1)*dens[n])/2
  product+=radial+angular
  if n in (1,2,3,64,260,261):witness.append({'n':n,'v':box(v),'w':box(w),'product':box(radial+angular)})
 radial_scale=iv.exp(a(t));linear=radial_scale**3*a(beta/k-1)*a(bs[0]);nonlinear=radial_scale**5*product;e0=linear+nonlinear;physical=e0/(radial_scale**a(beta))
 theta=(radial_scale**a(3-k))*sum((dens[j]*iv.sin((2*j+1)*iv.pi/4) for j in range(261)),iv.mpf(0))
 exact={'k':str(k),'tplus':str(t),'beta':str(beta),'b0':str(bs[0]),'z_bracket':list(map(str,(lo,hi))),'sine_affine':[[str(ds[j]),str(zs[j]),str(bs[j])] for j in range(262)]}
 files={str(p.relative_to(B)):sha(p) for p in (norm,D/'PROOF.md',Path(__file__))}
 out={'utc':utc(),'status':'COMPUTED_REQUIRES_OUTPUT_AUDIT','method':'Independent NPZ dyadics, Laurent multiplication, direct Green denominators and radial/tangential frequency-one products with iv180','dps':180,'source_archive':{'path':str(P),'sha256':sha(P)},'files':files,'exact':exact,'values':{key:box(x) for key,x in {'e0':e0,'E0':physical,'Theta_pi4':theta,'linear_term':linear,'quadratic_term':nonlinear,'z':z}.items()},'counts':{'input_outer_coefficients':520,'sine_modes':261,'poisson_modes':261,'antisymmetry_checks':786,'positive_denominators':261},'witnesses':witness,'seconds':time.monotonic()-st}
 (E/'iv.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('utc','status','seconds')}));print(json.dumps({k:x['display'] for k,x in out['values'].items()}))
if __name__=='__main__':run()

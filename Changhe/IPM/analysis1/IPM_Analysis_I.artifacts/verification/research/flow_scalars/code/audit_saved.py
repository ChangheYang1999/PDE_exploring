"""Fresh exact-data audit of saved scalar arrays. Does not import the source or producer."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,time,math
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
from collections import Counter
import numpy as np
from flint import arb,fmpq,ctx
assert not sys.flags.optimize
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/flow_scalars/evidence'
ctx.prec=1536;ctx.threads=1

def digest(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for block in iter(lambda:f.read(2**20),b''):h.update(block)
 return h.hexdigest()
def rational(x):return Fraction(float(x))
def ball(x):
 x=Fraction(x);return arb(fmpq(x.numerator,x.denominator))
def endpoint(x):
 m,e=x.man_exp();return Fraction(int(m))*Fraction(2)**int(e)
def contain(lo,x,hi):return lo<=endpoint(x.lower())<=endpoint(x.upper())<=hi
def mu(r):return ball(Fraction(1129,1000))+ball(Fraction(8391,1000))/(1+r**4/1296)

def main():
 tic=time.monotonic();report=json.loads((OUT/'checks.json').read_text());assert report['status']=='PASS_FINITE_RECONSTRUCTED_SCALARS_ONLY'
 assert digest(OUT/'scalar_arrays.npz')==report['array_sha256']
 for p,h in report['files'].items():assert digest(p)==h,p
 counts=Counter();stored=np.load(OUT/'scalar_arrays.npz');values={key:stored[key] for key in stored.files};stored.close()
 part=json.loads((ROOT/'research/middle_residual/evidence/partition_exact.json').read_text());pp=[]
 for span in part['spans']:
  left,right=map(Fraction,(span['a_exact'],span['b_exact']));n=span['count'];assert span['first_cell']==len(pp)
  step=(right-left)/n;assert step>0
  pp += [left+j*step for j in range(n)]
 pp.append(Fraction(part['spans'][-1]['b_exact']));assert len(pp)==7810
 for name,n in [('middle',7809),('outer',8948),('inner',2632)]:
  file=ROOT.parent/'ipmA-num/data'/('cert_green.npz' if name=='middle' else 'cert_'+name+'_green.npz')
  d=np.load(file);a=values[name];assert a.shape==(n,36) and np.isfinite(a).all()
  if name=='middle':grid=pp;tm,rr=d['tb'],d['tb_rad'];offset=Fraction(0)
  else:
   offset=rational(d['t0' if name=='outer' else 'tmin']);assert rational(d['t0_rad' if name=='outer' else 'tmin_rad'])==0
   assert offset==(pp[-1] if name=='outer' else pp[0])
   span=Fraction(17 if name=='outer' else 5);first=offset if name=='outer' else offset-5
   grid=[first+span*j/n for j in range(n+1)];tm,rr=d['tau'],d['tau_rad']
  for i,t in enumerate(grid):assert offset+rational(tm[i])-rational(rr[i])<=t<=offset+rational(tm[i])+rational(rr[i]);counts['exact_partition_contains']+=1
  for i,line in enumerate(a):
   h,em,er,im,ir,rlo,rhi,mm,mr=map(rational,line[:9]);assert 0<grid[i+1]-grid[i]<=h<Fraction(1,522)
   assert min(rlo,em-er)>0 and min(er,ir,mr)>=0;counts['width_hypothesis']+=1
   source_left=offset+rational(tm[i])-rational(rr[i]);source_right=offset+rational(tm[i])+rational(rr[i])
   for t in (source_left,source_right):assert contain(em-er,ball(t).exp(),em+er),(name,i,'exp');counts['fresh_exponential_contains']+=1
   assert rlo<=endpoint(ball(grid[i]).exp().lower())
   assert endpoint(ball(grid[i+1]).exp().upper())<=rhi;counts['fresh_radial_endpoint_contains']+=2
   for r in (rlo,rhi):assert contain(mm-mr,mu(ball(r)),mm+mr),(name,i,'mu');counts['fresh_mu_endpoint_contains']+=1
   for end in (em-er,em+er):assert contain(im-ir,1/ball(end),im+ir),(name,i,'inv');counts['fresh_reciprocal_endpoint_contains']+=1
   # Iterative fmpq multiplication, distinct from Fraction exponentiation in the producer.
   hf=fmpq(h.numerator,h.denominator);power=fmpq(1)
   for j,x in enumerate(line[9:]):
    xq=rational(x);assert fmpq(xq.numerator,xq.denominator)>=power,(name,i,'power',j)
    power*=hf;counts['fresh_rational_power_upper']+=1
   counts['cells']+=1
  d.close()
  print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'fresh_region_complete':name,'cells':n,'seconds':time.monotonic()-tic}),flush=True)
 for c in report['constants']:
  m=Fraction(float.fromhex(c['mid_hex']));r=Fraction(float.fromhex(c['rad_hex']));q=Fraction(c['exact'])
  assert contain(m-r,ball(q),m+r),(c['name'],'constant');counts['fresh_constant_contains']+=1
 assert counts['cells']==19389 and counts['fresh_constant_contains']==444
 for p,h in report['files'].items():assert digest(p)==h,p
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FRESH_ALL_SCALARS','method':'Independent rational partition; iterative fmpq powers; fresh Arb1536 exponential, reciprocal and rational-mu enclosures; no source MR or producer import.','counts':dict(counts),'producer_checks_sha256':digest(OUT/'checks.json'),'array_sha256':digest(OUT/'scalar_arrays.npz'),'self_sha256':digest(__file__),'seconds':time.monotonic()-tic}
 (OUT/'saved_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()

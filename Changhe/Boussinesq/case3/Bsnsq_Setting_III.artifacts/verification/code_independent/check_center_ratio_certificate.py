"""Separate integer checker for163. No imports from the generator or NUM lane."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import argparse,json,hashlib,time
import numpy as np

def rational(obj):return F(int(obj['numerator']),int(obj['denominator']))
def binary(v):return F.from_float(float(v))
def check(file):
 d=json.loads(Path(file).read_text());p=Path(d['archive']);assert hashlib.sha256(p.read_bytes()).hexdigest()==d['archive_sha256'];strains=[]
 with np.load(p,allow_pickle=False) as z:
  assert str(z['source_mode'])=='fixed_velocity_block' and float(z['eps'])==1
  for tag,arr,seed in [('self_block','cG',False),('seed_block','cG_f',True)]:
   c=d[tag];get=lambda k:z['seed_'+k].item() if seed and 'seed_'+k in z else z[k].item();degree=int(get('deg'));nt=int(get('Nt'));K=int(get('K'));grade=float(get('grade'));L=float(get('L'));b=float(z['beta_seed' if seed else 'beta_basis']);knots=[0.]*degree+list(np.linspace(0.,1.,nt+1)**grade)+[1.]*degree
   assert c['degree']==degree and c['Nt']==nt and c['K']==K and c['grade_hex']==grade.hex() and c['L_hex']==L.hex() and c['b_hex']==b.hex();assert c['knots_hex']==[float(v).hex() for v in knots]
   nb=len(knots)-degree-1;coeff=z[arr].reshape(K,nb)
   for n in range(K):
    for j in range(nb):assert c['active_coefficients_hex'][n][j]==float(0 if j<n//2 else coeff[n,j]).hex()
   total=F(0)
   for n,sign in [(1,-1),(3,1)]:
    if n<K:
     for j in range(n//2,nb):total+=sign*binary(coeff[n,j])*(binary(knots[j+degree+1])-binary(knots[j]))
   strain=binary(b)*binary(L)*total/(4*(degree+1));assert strain==rational(c['strain']);strains.append(strain)
  bb=binary(z['beta']);lam=binary(z['lam']);av=binary(z['cF'].ravel()[0]);qv=binary(z['cG'].ravel()[0]);param={'beta':bb,'lambda':lam,'a':av,'q':qv}
  assert all(rational(d['parameters'][k])==v for k,v in param.items())
  result={}
  for kind,cc in [('self',strains[0]),('forced',strains[0]+lam*strains[1])]:
   A=bb-cc;ft=[2*A*av,-(bb-2)*av];gt=[A*qv,qv,-2*av];nf=sum(abs(v) for v in ft);ng=sum(abs(v) for v in gt);assert nf>0 and ng>0;rf=sum(ft);rg=sum(gt)
   expected={'c':cc,'A':A,'m':cc-1-bb/2,'RF':rf,'RG':rg,'NF':nf,'NG':ng,'ratioF':abs(rf)/nf,'ratioG':abs(rg)/ng};node=d['inverse'][kind]
   for k,v in expected.items():
    assert rational(node['values'][k])==v;lo=rational(node['bounds'][k]['lo']);hi=rational(node['bounds'][k]['hi']);assert lo<=v<=hi and hi-lo==F(1,10**node['bounds'][k]['digits'])
   assert F(0)<=expected['ratioF']<=1 and F(0)<=expected['ratioG']<=1
   result[kind]={k:float(v) for k,v in expected.items()}
  # This corpus claim is asserted only after verifying all formulas and raw arrays.
  assert rational(d['inverse']['self']['bounds']['ratioF']['lo'])>F(3,5)
 return {'certificate':str(file),'sha256':d['archive_sha256'],'beta':float(bb),'lambda':float(lam),'inverse':result,'verdict':'CONFIRMED exact self thermal normalized supremum >3/5; REFUTED as literal B2 profile'}

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('certificates',nargs='+');a=p.parse_args();utc=datetime.now(timezone.utc).isoformat();start=time.monotonic();rows=[check(f) for f in a.certificates];d={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'all_passed':True,'checks':rows};Path(a.output).write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2))
if __name__=='__main__':main()

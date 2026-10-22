"""Separate integer checker. Reads archives and certificates, no generator imports."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import argparse,hashlib,json,time
import numpy as np

def num(v):return Fraction(int(v['numerator']),int(v['denominator']))
def binary(v):return Fraction.from_float(float(v))
def check(path):
 cert=json.loads(Path(path).read_text()); archive=Path(cert['archive'])
 assert hashlib.sha256(archive.read_bytes()).hexdigest()==cert['archive_sha256']
 with np.load(archive,allow_pickle=False) as z:
  assert str(z['source_mode'])=='fixed_velocity_block' and float(z['eps'])==1.
  strains=[]
  for seed,tag,array in [(False,'self_block','cG'),(True,'seed_block','cG_f')]:
   b=cert[tag];get=lambda k: z['seed_'+k].item() if seed and 'seed_'+k in z else z[k].item()
   degree=int(get('deg'));K=int(get('K'));nt=int(get('Nt'));grade=float(get('grade'));L=float(get('L'));bb=float(z['beta_seed' if seed else 'beta_basis'])
   assert b['degree']==degree and b['K']==K and b['Nt']==nt and b['grade_hex']==grade.hex() and b['L_hex']==L.hex() and b['b_hex']==bb.hex()
   # Freeze the independent Python reader's binary knot recipe, not ideal powers.
   internal=np.linspace(0.,1.,nt+1)**grade;knots=[0.]*degree+list(internal)+[1.]*degree
   assert [float(v).hex() for v in knots]==b['knots_hex']
   nb=len(knots)-degree-1; raw=z[array].reshape(K,nb)
   for n in range(K):
    for j in range(nb):assert b['active_coefficients_hex'][n][j]==float(0 if j<n//2 else raw[n,j]).hex()
   # Integer sum using the two angular moment weights, then common radial factor.
   total=Fraction(0)
   for n,weight in [(1,-1),(3,1)]:
    if n>=K:continue
    for j in range(n//2,nb):
     total+=weight*binary(raw[n,j])*(binary(knots[j+degree+1])-binary(knots[j]))
   result=binary(bb)*binary(L)*total/Fraction(4*(degree+1))
   assert result==num(b['strain']);strains.append(result)
  beta=binary(z['beta']);lam=binary(z['lam']);a=binary(z['cF'].ravel()[0]);g=binary(z['cG'].ravel()[0]);cm=strains[0]+lam*strains[1];m=cm-1-beta/2
  assert cert['beta_hex']==float(beta).hex() and cert['lambda_hex']==float(lam).hex() and cert['a0_hex']==float(z['a0']).hex()
  expected={'m_self':strains[0]-1-beta/2,'RF_self_center':-2*(strains[0]-1-beta/2)*a,'RG_self_center':(beta-strains[0]+1)*g-2*a,'c_self':strains[0],'c_seed':strains[1],'c_mixed':cm,'m':m,'a':a,'q':g,'RF_center':-2*m*a,'RG_center':(beta-cm+1)*g-2*a,'G_compatibility_error':g-4*a/beta,'a0_metadata_error':a-binary(z['a0'])}
  for k,v in expected.items():
   assert num(cert['values'][k])==v
   lo=num(cert['bounds'][k]['lo']);hi=num(cert['bounds'][k]['hi']);assert lo<=v<=hi and hi-lo==Fraction(1,10**cert['bounds'][k]['digits'])
  assert num(cert['bounds']['m_self']['hi'])<0 and num(cert['bounds']['m']['hi'])<0 and num(cert['bounds']['a']['lo'])>0
 return {'certificate':str(path),'archive_sha256':cert['archive_sha256'],'verdict':'PASS: literal field fails center thermal equation','m_bounds':cert['bounds']['m']['display'],'beta':float(beta)}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('certificates',nargs='+');a=ap.parse_args();start=time.monotonic();utc=datetime.now(timezone.utc).isoformat();results=[check(p) for p in a.certificates]
 output={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'all_passed':True,'checks':results}
 Path(a.output).write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(output,indent=2))
if __name__=='__main__':main()

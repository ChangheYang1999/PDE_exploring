"""Independent Arb and mpmath.iv enclosures of the face-estimate constants."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,math
from flint import arb,ctx
from mpmath import iv
from importlib.metadata import version
ctx.prec=256;iv.dps=160
BASE=Path(__file__).resolve().parents[1];E=BASE/'evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aq(x):x=F(x);return arb(x.numerator)/x.denominator
def iq(x):x=F(x);return iv.mpf(x.numerator)/x.denominator
def arbq(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ie(x):
 out=[]
 for s,m,e,bc in x._mpi_:
  assert bc>=0,'nonfinite interval endpoint'
  out.append((-1 if s else 1)*F(int(m))*F(2)**int(e))
 return out
def enclose(x,y):
 assert x.is_finite()
 lo,hi=arbq(x.lower()),arbq(x.upper());a,b=ie(y);assert lo<=a<=b<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'arb_display':str(x),'iv_display':str(y)}
def run():
 libraries={k:version(k) for k in ('python-flint','mpmath')};assert libraries=={'python-flint':'0.9.0','mpmath':'1.3.0'}
 inp=E/'inputs.json';cases=[]
 for row in json.loads(inp.read_bytes())['cases']:
  N=row['N'];b=F(row['b_exact']);assert F(N)-F(1,2)<b<F(N)+F(1,2)
  ab=aq(b);bb=iq(b);two=arb(2);itwo=iv.mpf(2);fac=math.factorial
  # Primary formula as stated in the theorem.
  SA=two**aq(2*b-2*N-1)*fac(2*N+1)/aq((2*N+1-2*b)*fac(N)**2)
  SK=two**aq(-2*b-1)/aq(2*b+1)
  C=two**aq(abs(b))+SA.sqrt()+SK.sqrt();Cp=C;scalars={'S_A':SA,'S_K':SK}
  # Independent reconstruction of each double integral in its integration order.
  # integral_0^infty z^p exp(-a z) dz=Gamma(p+1)/a^(p+1).
  def moment(p,a):return iv.gamma(iq(p+1))/iq(a)**iq(p+1)
  sA=iq(F(1,4*fac(N)**2))*2*2*itwo**iq(-(2*N+1-2*b))/iq(2*N+1-2*b)*moment(2*N+1,1)
  sK=iq(F(1,4))*2*2*itwo**iq(-(2*b+1))/iq(2*b+1)*moment(1,1)
  c=itwo**iq(abs(b))+iv.sqrt(sA)+iv.sqrt(sK);cp=c;other={'S_A':sA,'S_K':sK}
  for j in range(N):
   SB=two**aq(-2*b-1)*fac(2*j+1)/aq((2*b-2*j-1)*fac(j)**2)
   SC=3*two**aq(2*abs(b)-1)*fac(2*j+1)/fac(j)**2
   trace=(aq(2*b+1).gamma()).sqrt()*two**aq(-b-1)/fac(j)
   ext=trace*(aq(F(2)/(2*b-2*j-1))).sqrt()
   sB=iq(F(1,4*fac(j)**2))*2*2*itwo**iq(2*j+1-2*b)/iq(2*b-2*j-1)*moment(2*j+1,2)
   sC=iq(F(3,4*fac(j)**2))*itwo**iq(2*abs(b))*2*moment(2*j+1,1)
   tr=iv.sqrt(2*moment(2*b,2))/(2*fac(j))
   ex=tr*iv.sqrt(iq(F(2)/(2*b-2*j-1)))
   C+=SB.sqrt()+SC.sqrt();Cp+=SB.sqrt()+SC.sqrt()+ext
   c+=iv.sqrt(sB)+iv.sqrt(sC);cp+=iv.sqrt(sB)+iv.sqrt(sC)+ex
   for name,x,y in [('S_B',SB,sB),('S_C',SC,sC),('trace',trace,tr),('extension',ext,ex)]:scalars[f'{name}_{j}']=x;other[f'{name}_{j}']=y
  scalars.update(C=C,C_prime=Cp);other.update(C=c,C_prime=cp)
  values={key:enclose(v,other[key]) for key,v in scalars.items()}
  cases.append({**row,'values':values})
 decimal_bounds={('3','13/5'):('78.798713938733','82.260031194549'),('3','17/5'):('151.060134903140','156.124040371967'),('0','-1/4'):('2.863906001713','2.863906001713')}
 for row in cases:
  for key,bound in zip(('C','C_prime'),decimal_bounds[(str(row['N']),row['b_exact'])]):assert F(row['values'][key]['upper_exact'])<F(bound)
 result={'library_versions':libraries,'rounded_decimal_checks':6,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':sha(__file__),'input_sha256':sha(inp),'proof_sha256':sha(BASE/'PROOF.md'),'method':'Arb256 closed constants versus mpmath.iv160 independently assembled weighted double integrals and Cauchy-Schwarz integrals','cases':cases,'scope':'Arithmetic constants only; operator theorem and domain limitations are in PROOF.md.'}
 (E/'constants_audit.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'status':'PASS','utc':result['utc'],'cases':[{'N':r['N'],'b':r['b_exact'],'C':r['values']['C']['arb_display'],'C_prime':r['values']['C_prime']['arb_display']} for r in cases]},indent=2))
if __name__=='__main__':run()

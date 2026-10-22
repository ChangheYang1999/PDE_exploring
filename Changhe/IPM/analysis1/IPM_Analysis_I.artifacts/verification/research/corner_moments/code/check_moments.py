"""Independent exact sparse algebra and Arb/iv corner moment constants."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
from mpmath import iv
if sys.flags.optimize:raise RuntimeError('Assertions must be active')
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/corner_moments/evidence'
ctx.prec=512;ctx.threads=1;iv.dps=180

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def exact(x):
 assert x.is_finite() and x.rad()==0;m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ae(x):assert x.is_finite();return exact(x.lower()),exact(x.upper())
def ie(x):
 ans=[]
 for s,m,e,bc in x._mpi_:
  assert bc>=0;ans.append((-1 if s else 1)*F(int(m))*F(2)**int(e))
 assert ans[0]<=ans[1];return tuple(ans)
def out(x,method):
 a,b=ae(x) if method=='arb' else ie(x);return {'lower_exact':str(a),'upper_exact':str(b),'display':str(x)}
def beta_arb(p,q):return aa(p).gamma()*aa(q).gamma()/aa(p+q).gamma()
def beta_iv(p,q):return iv.gamma(iq(p))*iv.gamma(iq(q))/iv.gamma(iq(p+q))
def polyadd(p,q):
 ans=p.copy()
 for k,v in q.items():ans[k]=ans.get(k,F(0))+v
 return {k:v for k,v in ans.items() if v}
def scale(p,c):return {k:c*v for k,v in p.items() if c*v}
def mul(p,q):
 ans={}
 for (i,j),v in p.items():
  for (l,m),w in q.items():ans[(i+l,j+m)]=ans.get((i+l,j+m),F(0))+v*w
 return {k:v for k,v in ans.items() if v}
def diff(p,axis):
 ans={}
 for ex,v in p.items():
  if ex[axis]:ne=list(ex);ne[axis]-=1;ans[tuple(ne)]=v*ex[axis]
 return ans
def couple(rho,u1,u2):return polyadd(mul(diff(rho,0),u1),mul(diff(rho,1),u2))
def velocity(k):
 real={};imag={}
 for j in range(k+1):
  if j%2==0:real[(k-j,j)]=F((-1)**(j//2)*math.comb(k,j))
  else:imag[(k-j,j)]=F(-(-1)**((j-1)//2)*math.comb(k,j))
 return real,imag

def main():
 a,b,gamma=F(129,20),F(307,100),F(1129,1000);A=a+b;results=[];algebra=[]
 for k in [1,3,5,7]:
  n=k+2;prev=[1];current=[0,2]
  for j in range(2,n):
   nxt=[0]+[2*v for v in current];nxt[:len(prev)]=[x-y for x,y in zip(nxt,prev)]
   prev,current=current,nxt
  assert all(current[j]==0 for j in range(1,len(current),2));u=current[::2];sq=[0]*(2*len(u)-1)
  for i,v in enumerate(u):
   for j,w in enumerate(u):sq[i+j]+=v*w
  ja=sum((2*v*beta_arb(a+j+F(1,2),b+F(3,2)) for j,v in enumerate(sq)),arb(0))
  ji=iv.mpf(0)
  for r in range((n-1)//2+1):
   for s in range((n-1)//2+1):ji+=2*(-1)**(r+s)*math.comb(n,2*r+1)*math.comb(n,2*s+1)*beta_iv(a+n-r-s-F(1,2),b+r+s+F(3,2))
  al,au=ae(ja);il,iu=ie(ji);assert 0<al<=au and 0<il<=iu and max(al,il)<=min(au,iu)
  crude=2*beta_arb(a+F(1,2),b+F(1,2));assert ae(crude)[0]>=au
  p,q=2*(A-k-1),2*(k+1-gamma);assert p>0 and q>0
  radial_a=beta_arb(p,q);radial_i=beta_iv(p,q)
  # Coefficients for every parity-allowed l,j and both components.
  coeffs=[]
  for l in range(k+1):
   j=k-l;component=1 if l%2 else 2;factor_a=aa((k+1)*math.comb(k,l))/ (2*arb.pi());factor_i=iq((k+1)*math.comb(k,l))/(2*iv.pi)
   composite_a=factor_a*(ja*radial_a).sqrt();composite_i=factor_i*iv.sqrt(ji*radial_i)
   square_a=factor_a*(ja*aa(2)**aa(A-k-1)/aa(2*(A-k-1))).sqrt();square_i=factor_i*iv.sqrt(ji*iv.power(iq(2),iq(A-k-1))/iq(2*(A-k-1)))
   for x,y in [(composite_a,composite_i),(square_a,square_i)]:
    x0,x1=ae(x);y0,y1=ie(y);assert x0>0 and y0>0 and max(x0,y0)<=min(x1,y1)
   coeffs.append({'i':component,'l':l,'j':j,'binomial':math.comb(k,l),'composite_arb':out(composite_a,'arb'),'composite_iv':out(composite_i,'iv'),'unit_square_upper_arb':out(square_a,'arb'),'unit_square_upper_iv':out(square_i,'iv')})
  results.append({'degree':k,'angular_frequency':n,'chebyshev_even_coefficients':u,'squared_coefficients':sq,'J_arb':out(ja,'arb'),'J_iv':out(ji,'iv'),'radial_beta_arguments_exact':[str(p),str(q)],'coefficients':coeffs})
  u1,u2=velocity(k);G=couple({(2,1):F(1)},u1,u2);rem={ex:v for ex,v in G.items() if ex[0]>=6 and ex[1]>=3};expected={(6,3):F(-7)} if k==7 else {};assert rem==expected
  algebra.append({'velocity_degree':k,'G':{str(ex):str(v) for ex,v in sorted(G.items())},'rectangle_remainder':{str(ex):str(v) for ex,v in rem.items()}})
 # c=1, d1=-1 plus cX/3, and density alpha00/alpha20/alpha02 basis terms.
 u1,u2=velocity(1)
 w1=polyadd(scale(u1,F(-1)),{(1,0):F(1,3)});w2=polyadd(scale(u2,F(-1)),{(0,1):F(1,3)})
 assert w1=={(1,0):F(-2,3)} and w2=={(0,1):F(4,3)}
 assert couple({(2,1):F(1)},w1,w2)=={}
 assert couple({(4,1):F(1)},w1,w2).get((4,1))==F(-4,3)
 assert couple({(2,3):F(1)},w1,w2).get((4,1),0)==0
 u1,u2=velocity(3);assert couple({(2,1):F(1)},u1,u2)[(4,1)]==-1
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_ALGEBRA_AND_TWO_INTERVAL_CONSTANTS','source_sha256':sha(Path(__file__)),'proof_sha256':sha(BASE/'research/corner_moments/PROOF.md'),'parameters_exact':{'a':str(a),'b':str(b),'A':str(A),'gamma':str(gamma)},'methods':'Arb512 Chebyshev square and beta gamma evaluation; independent iv180 direct imaginary-binomial square and beta gamma evaluation. Sparse exact bivariate algebra without sympy.','moment_coefficients_checked':sum(len(r['coefficients']) for r in results),'norm_interval_overlaps':2*sum(len(r['coefficients']) for r in results),'angular_interval_overlaps':4,'coupling_identities':algebra,'J_zero':True,'K_alpha00_d3_exact':'-1','K_c_alpha20_exact':'-4/3','unbounded_growth_power_exact':str(A-8),'results':results,'scope':'Moment norm constants and exact local polynomial identities. No verification of lead D1/T2 or full variable-coefficient coupling bound.'}
 tmp=E/'checks.json.tmp';tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,E/'checks.json')
 print(json.dumps({k:v for k,v in result.items() if k not in ['results','coupling_identities']}),flush=True)
if __name__=='__main__':main()

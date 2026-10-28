"""Exact original residual sectors and directed omitted-tail bound."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import json,sys,time
from flint import arb,ctx
here=Path(__file__).parent;root=here.parents[2];sys.set_int_max_str_digits(0)
sys.path.insert(0,str(root/'research/05_tails/verification'))
sys.path.insert(0,str(root/'research/02_energy/verification'))
from check_tail import density_stream,advection,add_sine
from farfield_matrix_certificate import differentiate,binomial

def A(v):
 q=F(v);return arb(q.numerator)/q.denominator

def add(p,i,v):
 p[i]=p.get(i,F(0))+v
 if not p[i]:del p[i]

def odd_poly(n):
 assert n%2==1 and n>0
 # U_(n-1)(x)=sum_j (-1)^j binom(n-1-j,j)(2x)^(n-1-2j).
 m=n-1;out={}
 for j in range(m//2+1):
  power=(m-2*j)//2;fac=F((-1)**j*comb(m-j,j)*2**(m-2*j),2**power)
  for k in range(power+1):add(out,k,fac*comb(power,k))
 return out

def main():
 ctx.prec=512;start=time.monotonic();source=root/'research/source_audit/state131_exact.json';d=json.loads(source.read_text());c=F(d['exact_parameters']['cl']);g=1/c;delta=1-g;pp=[(3+g-j*delta)/2 for j in range(4)];order=[tuple(v) for v in d['canonical_order']];coeff=list(map(F,d['canonical_coefficients']));Q=10;R=300
 assert all(abs(pp[j]-k)<26 for j,m,k in order)
 absj=[sum((abs(v) for v,(jj,m,k) in zip(coeff,order) if jj==j),F(0)) for j in range(4)];den={};psi={};power={};caps={3:[],4:[]}
 for j in range(4):
  for q in range(Q+1):
   C={}
   for v,(jj,m,k) in zip(coeff,order):
    if jj==j:add(C,2*m,v*binomial(pp[j]-k,q))
   p=g-j*delta-2*q;power[j,q]=p;den[j,q],psi[j,q]=density_stream(C,p+3)
   deriv={(0,0):{('c',n):v for n,v in C.items()}}
   for dd in range(1,5):
    for nx in range(dd+1):
     ny=dd-nx
     deriv[nx,ny]=differentiate(deriv[nx-1,ny] if nx else deriv[nx,ny-1],p+4-dd,'x' if nx else 'y')
    if dd in caps:caps[dd].append((j,q,max(sum(map(abs,deriv[nx,dd-nx].values()),F(0)) for nx in range(dd+1))))
 E={}
 for key,f in den.items():E[key]={n:(c*power[key]-1)*v for n,v in f.items() if (c*power[key]-1)*v}
 for (i,qi),p in psi.items():
  for (j,qj),f in den.items():
   row=E.setdefault((i+j+1,qi+qj),{})
   for n,v in advection(p,f,power[i,qi]+1,power[j,qj]).items():add_sine(row,n,v)
 E={k:{n:v for n,v in p.items() if v} for k,p in E.items() if any(p.values())};assert (0,0) not in E
 oldpath=root/'research/05_tails/verification/state131_residual_truncated_sectors.json';old=json.loads(oldpath.read_text());assert old['Q']==Q and old['input_sha256']==d['canonical_serialization_sha256']
 assert {str(k):{str(n):str(v) for n,v in p.items()} for k,p in E.items()}==old['coefficients']
 rows=[]
 for (h,q),sin in sorted(E.items()):
  exponent=(h-1)*delta+2*q;assert exponent>=0
  P={}
  for n,v in sin.items():
   for k,x in odd_poly(n).items():add(P,k,v*x)
  rows.append({'h':h,'q':q,'a':str(exponent),'P':{str(k):str(v) for k,v in P.items()}})
 q0=Q+1;M={};T={};rat={}
 for dd in [3,4]:
  M[dd]=sum((A(v)*A(R)**A(-j*delta-2*q) for j,q,v in caps[dd]),arb(0));rat[dd]=A(F(q0+26,q0+1)*F(2*q0+34,2*q0+32)**dd)/R**2;assert rat[dd]<1
  T[dd]=A(comb(q0+25,q0)*(2*q0+32)**dd)*A(R)**(-2*q0)*sum((A(v)*A(R)**A(-j*delta) for j,v in enumerate(absj)),arb(0))/(1-rat[dd])
 eps=A(R)**A(delta)*(2*arb(2).sqrt()*A(c)*T[4]+2*T[3])+4*(T[3]*M[4]+M[3]*T[4]+T[3]*T[4])
 upper=F(1)
 while A(upper/2)>=eps:upper/=2
 assert A(upper)>=eps
 out={'utc':datetime.now(timezone.utc).isoformat(),'all_pass':True,'cl':str(c),'delta':str(delta),'R':R,'Q':Q,'rows':rows,'source_sha256':sha256(source.read_bytes()).hexdigest(),'canonical_sha256':d['canonical_serialization_sha256'],'prior_sectors_sha256':sha256(oldpath.read_bytes()).hexdigest(),'potential_caps':{str(dd):[[j,q,str(v)] for j,q,v in caps[dd]] for dd in caps},'absolute_branch_coefficients':list(map(str,absj)),'tail_M':{str(k):v.str(100) for k,v in M.items()},'tail_T':{str(k):v.str(100) for k,v in T.items()},'tail_ratio':{str(k):v.str(100) for k,v in rat.items()},'epsilon':eps.str(100),'epsilon_upper_rational':str(upper),'precision_bits':ctx.prec,'seconds':time.monotonic()-start}
 (here/'sectors.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],len(rows),'sectors PASS; epsilon',eps,'seconds',out['seconds'],flush=True)
if __name__=='__main__':main()

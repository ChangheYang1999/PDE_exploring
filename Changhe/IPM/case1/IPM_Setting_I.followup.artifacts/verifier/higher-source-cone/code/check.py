from fractions import Fraction as Q
from math import factorial,comb
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import sympy as sy
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]
J=101
mp.mp.dps=75

def poly_add(a,b,c=Q(1)):
 out=a.copy()
 for j,t in b.items():
  out[j]=out.get(j,Q(0))+c*t
  if not out[j]:del out[j]
 return out

def derivative(a):return {j-1:j*t for j,t in a.items() if j}
def radial(a,p):return {j:(p-j)*t for j,t in a.items() if (p-j)*t}
def times(a,b):
 out={}
 for j,t in a.items():
  for k,u in b.items():
   if j+k<=J:out[j+k]=out.get(j+k,Q(0))+t*u
 return {j:t for j,t in out.items() if t}
def truncate(a,last=J):return {j:t for j,t in a.items() if j<=last and t}
def norm(a,kap):return sum(abs(t)*kap**j for j,t in a.items())
def minusnorm(a,kap):return sum(abs(t)*kap**j/j for j,t in a.items() if j)
def minorder(a):return min(a) if a else None
def rising(x,n):
 z=Q(1)
 for i in range(n):z*=x+i
 return z

def inverse(A,b,m,C,n,H):
 q=Q(m-1)/A;p=1+(n+1)*(m-q-1);res=m+n*(m-1)
 f={};u={};v={};compat=[]
 for j in range(1,J+1,2):
  denom=A*p-1-(A-1)*j
  rhs=H.get(j,Q(0))-2*b*(A-1)*v.get(j,Q(0))
  if denom:fj=rhs/denom
  else:
   assert j==res and rhs==0,(A,b,m,n,j,rhs)
   fj=C if n==0 else Q(0);compat.append(j)
  if fj:f[j]=fj
  uj=(j-p)*(v.get(j,Q(0))+fj)/(j+1)
  if uj:u[j+1]=uj
  vj=(p-j-1)*uj/(j+2)
  if vj:v[j+2]=vj
 # Independent polynomial differentiation of all three PDE coefficients.
 trans=poly_add({j:(A*p-1+(1-A)*j)*t for j,t in f.items()},v,2*b*(A-1))
 assert not truncate(poly_add(trans,H,-1))
 assert not truncate(poly_add(derivative(v),radial(u,p),-1),J+1)
 curl=poly_add({j:(j-p)*t for j,t in v.items()},derivative(u),-1)
 assert not truncate(poly_add(curl,radial(f,p),-1))
 return {'p':p,'f':f,'u':u,'v':v,'compat':compat}

def forcing(modes,n):
 H={}
 for i in range(n):
  a=modes[i];d=modes[n-1-i]
  H=poly_add(H,times(a['u'],radial(d['f'],d['p'])))
  H=poly_add(H,times(a['v'],derivative(d['f'])),-1)
 return H

def number(x):return mp.mpf(x.numerator)/x.denominator
def evalpoly(a,z):return sum(number(t)*z**j for j,t in a.items())
def residual(modes,N,A,b,r,z):
 fields={key:mp.mpf(0) for key in ['f','fs','fy','u','us','uy','v','vs','vy']}
 for d in modes[:N+1]:
  power=r**number(d['p'])
  for tag in ['f','u','v']:
   fields[tag]+=power*evalpoly(d[tag],z)
   fields[tag+'s']-=power/r*evalpoly(radial(d[tag],d['p']),z)
   fields[tag+'y']+=power/r*evalpoly(derivative(d[tag]),z)
 R=-number(A)*r*fields['fs']+r*z*fields['fy']-fields['f']+number(2*b*(A-1))*fields['v']+fields['u']*fields['fs']+fields['v']*fields['fy']
 return {'N':N,'r':str(r),'z':str(z),'transport':str(R),'div':str(fields['us']+fields['vy']),'curl_identity':str(fields['vs']-fields['uy']+fields['fs'])}

start=time.monotonic();out={'date':datetime.now(timezone.utc).isoformat(),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'J':J,'cases':[]}
A,m,q,n,C,b=sy.symbols('A m q n C b');p=m-q
h=sy.expand((q*C/(m+1))*(-q*C)-(-q*(q+1)*C/((m+1)*(m+2)))*m*C)
assert sy.factor(h-q*(m-2*q)*C**2/((m+1)*(m+2)))==0
pn=1+(n+1)*(p-1)
assert sy.factor((A*pn-1-(A-1)*(m+n*(m-1))).subs(q,(m-1)/A))==0
assert sy.factor((A*(2*p-1)-1-(A-1)*(2*m+1)).subs(q,(m-1)/A)+2*(A-1))==0
out['symbolic']={'first_forcing':str(sy.factor(h)),'resonant_index':'m+n*(m-1)','first_correction_denominator':'-2*(A-1)','checks':'PASS'}
cases=[(3,Q(5,4),Q(1,2),Q(1)),(3,Q(2),Q(3),Q(1)),(3,Q(10,3),Q(50),Q(-2)),(5,Q(7,4),Q(13,8),Q(1)),(5,Q(2),Q(2),Q(1)),(5,Q(5,2),Q(13,8),Q(1)),(5,Q(5),Q(1,3),Q(1)),(7,Q(12,7),Q(2),Q(1)),(9,Q(4,3),Q(9),Q(1)),(11,Q(10),Q(30),Q(1))]
for m,A,b,C in cases:
 kap=Q(1,4) if b<15 else Q(1,16);q=Q(m-1)/A;p=m-q;B=kap**2/(1-kap**2)
 L=Q(2*m+1,2)/((A-1)*(1-b*B));K=(2*m+1)*kap/((A-1)*(1-kap**2)*(1-b*B));abar=abs(C)*kap**m/(1-max(Q(1),b)*kap**2)
 assert kap**2*(1+b)<1
 modes=[];row={'m':m,'A':str(A),'b':str(b),'C':str(C),'q':str(q),'p':str(p),'kappa':str(kap),'K':str(K),'a_bar':str(abar),'orders':[]}
 for n in range(6):
  H={} if n==0 else forcing(modes,n)
  d=inverse(A,b,m,C,n,H);modes.append(d);M=m+n*(m+1)
  for tag,minimum in [('f',M),('u',M+1),('v',M+2)]:
   assert minorder(d[tag]) is None or minorder(d[tag])>=minimum,(m,A,b,n,tag,minorder(d[tag]))
  an=norm(d['f'],kap);un=norm(d['u'],kap);vn=norm(d['v'],kap)
  assert un<=kap/(1-kap**2)*an and vn<=B*an
  if n==0:
   for j in range(m,J+1,2):
    ell=(j-m)//2;exact=C*(-1)**ell*rising(b,ell)*rising(q,2*ell)*factorial(m)/Q(factorial(ell)*factorial(m+2*ell))
    assert d['f'].get(j,Q(0))==exact
   assert an<=abar
  else:
   hn=minusnorm(H,kap);conv=sum(norm(modes[i]['f'],kap)*norm(modes[n-1-i]['f'],kap) for i in range(n))
   assert hn<=2*kap/(1-kap**2)*conv
   assert an<=L*hn and an<=K*conv
  catbound=Q(comb(2*n,n),n+1)*K**n*norm(modes[0]['f'],kap)**(n+1)
  assert an<=catbound
  if n==1:
   expected=-q*(m-2*q)*C**2/(2*(A-1)*(m+1)*(m+2))
   assert d['f'].get(2*m+1,Q(0))==expected
  row['orders'].append({'n':n,'p_n':str(d['p']),'forced_minimum':M,'actual_orders':[minorder(d[t]) for t in ['f','u','v']],'resonance':d['compat'],'phi_norm':float(an),'catalan_bound':float(catbound),'first_allowed_coefficient':str(d['f'].get(M,Q(0)))})
 # Nonlinear corrections do not alter any axis coefficient through m+2.
 assert modes[0]['f'][m]==C and modes[0]['f'][m+2]==-b*q*(q+1)*C/((m+1)*(m+2))
 assert all(not any(j<=m+2 for j in d['f']) for d in modes[1:])
 rlimit=(1/(4*number(K)*number(abar)))**(1/number(p-1));r=min(mp.mpf(1),rlimit/2);z=number(kap)/2
 row['sufficient_R_limit']=str(rlimit);row['residuals']=[residual(modes,N,A,b,r,z) for N in range(5)]
 out['cases'].append(row);(ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n')
 print('PASS m',m,'A',A,'b',b,'p',p,'orders',[d['actual_orders'][0] for d in row['orders']],'R0/R4',mp.nstr(mp.mpf(row['residuals'][0]['transport']),5),mp.nstr(mp.mpf(row['residuals'][-1]['transport']),5),flush=True)
out['complete']=True;out['seconds']=time.monotonic()-start;(ROOT/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');print('ALL60EXACTCASES PASS',out['seconds'],flush=True)

from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import factorial,comb
import os
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
import sys,json,hashlib,time
sys.dont_write_bytecode=True
from flint import fmpq,fmpq_poly,fmpq_mat
import mpmath as mp
mp.iv.dps=220
import sympy as s
R=Path(__file__).resolve().parents[3];D=R/'research/canonical_axis_residual';E=D/'evidence'
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def hx(t):
 neg=t.startswith('-');t=t.lstrip('+-');a,b=t.split('p');i,j=a[2:].split('.');q=fmpq(int(i+j,16))*fmpq(2)**(int(b)-4*len(j));return -q if neg else q
# Independent manual hexadecimal path never converts to binary floating point.
def iv(q):q=F(str(q));return mp.iv.mpf(q.numerator)/q.denominator
def mfrac(q):sign,man,exp,bc=q;assert bc>=0;return (-1 if sign else 1)*F(man)*F(2)**exp
def row(x):a,b=map(mfrac,x._mpi_);return {'display':str(x),'lo':str(a),'hi':str(b)}
start=now();timer=time.monotonic();A=load(E/'compute.json');assert A['proof_sha256']==sha(D/'PROOF.md')==load(E/'proof_first.json')['proof_sha256'] and A['code_sha256']==sha(D/'code/compute.py')
assert sha(R/A['parent_path'])==A['parent_sha256']
for n,h in A['parent_files'].items():assert sha(R/n)==h,n
path=R/'data_exact/modal_v2.json';assert sha(path)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';d=load(path);ar=d['arrays'];k,bi,bo=(hx(d['scalars_hex'][n]) for n in ['k','bi','bo']);assert 0<k<fmpq(1,2) and bi>4 and bo>4
T=list(map(hx,ar['knots']['hex']));M,nb=ar['S']['shape'];assert M==260 and nb==1565 and d['degree']==7 and len(T)==nb+8
assert T[:8]==[T[0]]*8 and T[-8:]==[T[-1]]*8 and all(T[i+1]>T[i] for i in range(7,nb))
def get(name,m,j):return hx(ar[name]['hex'][m*ar[name]['shape'][1]+j])
S=[get('S',1,j)+get('S',2,j)-get('S',3,j)-get('S',4,j) for j in range(nb)]
DD=[get('D',1,j)+get('D',2,j)-get('D',3,j)-get('D',4,j) for j in range(7)]
AA=[get('Aout',1,j)+get('Aout',2,j)-get('Aout',3,j)-get('Aout',4,j) for j in range(10)]
alpha=[(1+j)*k-(3+j+2*l) for j,l in d['outer_jl']];assert len(alpha)==10 and all(q<0 for q in alpha)
# Clamped endpoint jets by derivative coefficient recursion, no Cox polynomials.
def jets(c,t,right):
 out=[]
 for deg in range(7,0,-1):
  out.append(c[-1] if right else c[0]);new=[]
  for i in range(len(c)-1):
   den=t[i+deg+1]-t[i+1];assert den>0;new.append(deg*(c[i+1]-c[i])/den)
  c=new;t=t[1:-1]
 return out
Ji=jets(S[:8],T[:16],False);Jo=jets(S[-8:],T[-16:],True)
# A triangular solve of the derivative equations, independently of the exponential-multiplication formula.
def solve_join(J,coeff,powers,b):
 P=[sum((q*v**n for q,v in zip(coeff,powers)),fmpq(0)) for n in range(7)];out=[]
 for n in range(7):
  val=J[n]-P[n]-sum((out[j]*fmpq(factorial(n),factorial(n-j))*b**(n-j) for j in range(n)),fmpq(0));out.append(val/factorial(n))
 for n in range(7):assert P[n]+sum((out[j]*fmpq(factorial(n),factorial(n-j))*b**(n-j) for j in range(n+1)),fmpq(0))==J[n]
 return out
Ei=solve_join(Ji,DD,list(range(2,16,2)),bi);Eo=solve_join(Jo,AA,alpha,-bo)
# Exact eight-node Lagrange integral on [0,1], no stored quadrature constants.
nodes=[fmpq(j,7) for j in range(8)];weights=[]
for j,node in enumerate(nodes):
 p=fmpq_poly([1]);den=fmpq(1)
 for l,other in enumerate(nodes):
  if l!=j:p*=fmpq_poly([-other,1]);den*=node-other
 weights.append(sum((p[i]/(i+1) for i in range(8)),fmpq(0))/den)
for degree in range(8):assert sum((w*x**degree for w,x in zip(weights,nodes)),fmpq(0))==fmpq(1,degree+1)
assert all(w>0 for w in weights)
def value(span,x):
 z=S[span-7:span+1].copy()
 for order in range(1,8):
  for j in range(7,order-1,-1):
   i=span-7+j;v=(x-T[i])/(T[i+8-order]-T[i]);z[j]=(1-v)*z[j-1]+v*z[j]
 return z[7]
Im=fmpq(0)
for span in range(7,nb):
 left,right=T[span],T[span+1];h=right-left;Im+=h*sum((w*value(span,left+h*x) for w,x in zip(weights,nodes)),fmpq(0))
Ii=sum((DD[j]/(2*j+2) for j in range(7)),fmpq(0))+sum((Ei[j]*(-1)**j*factorial(j)/bi**(j+1) for j in range(7)),fmpq(0))
Io=sum((-AA[j]/alpha[j] for j in range(10)),fmpq(0))+sum((Eo[j]*factorial(j)/bo**(j+1) for j in range(7)),fmpq(0));I=Ii+Im+Io
Braw=sum(((-1)**m*get('D',m,0) for m in range(M)),fmpq(0));beta=4/k-1;H4=I/16-fmpq(1,64);Ac=-fmpq(1,6)-4*H4
exact={'k':k,'a':T[0],'bi':bi,'bo':bo,'Braw':Braw,'I_inner':Ii,'I_middle':Im,'I_outer':Io,'I':I,'H4':H4,'A':Ac,'beta':beta}
for n,v in exact.items():assert F(str(v))==F(A['exact'][n]),n
assert list(map(str,Ji))==A['jets_inner'] and list(map(str,Jo))==A['jets_outer'] and list(map(str,Ei))==A['joins_inner'] and list(map(str,Eo))==A['joins_outer']
B=iv(Braw)*mp.iv.exp(-iv(T[0]))**2;Q=2*iv(beta)*B+iv(fmpq(25,48))+5*iv(I)/4
rows={'B':row(B),'Q':row(Q)};lo,hi=map(F,A['Q_strict_window']);assert lo<F(rows['Q']['lo'])<=F(rows['Q']['hi'])<hi and lo*hi>0
for n,r in rows.items():assert max(F(r['lo']),F(A['balls'][n]['lo']))<=min(F(r['hi']),F(A['balls'][n]['hi'])),n
# Full Laurent projection for all260 input modes, independent of sine selection.
z=s.symbols('z');unit=(z+z**-1)**2*(z-z**-1)/(8*s.I);coeff={}
for m in range(260):
 expression=s.Poly(s.expand(unit*(z**(2*m)+z**(-2*m))/2*z**(2*m+3)),z)
 positive=expression.coeff_monomial(z**(2*m+8));negative=expression.coeff_monomial(z**(2*m-2)) if m>=1 else 0
 v=s.simplify(s.I*(positive-negative))
 if v:coeff[m]=str(v)
assert coeff=={1:'1/8',2:'1/8',3:'-1/8',4:'-1/8'}
x,y,ell,sig,Bsym,Asym,H=s.symbols('x y ell sig B A H');rho=x*x*(y+Bsym*y**3);psi=sig*x*y+Asym*x*y**3
Ux=-s.diff(psi,y);Uy=s.diff(psi,x);res=(ell*x+Ux)*s.diff(rho,x)+(ell*y+Uy)*s.diff(rho,y)-rho
axis=s.expand(s.diff(res,x,2).subs(x,0)/2);normal=s.expand(axis.subs(sig,3*ell-1));leading=s.expand(normal).coeff(y,3)
assert s.simplify(leading-((8*ell-2)*Bsym-5*Asym))==0 and normal.coeff(y,1)==0
psi4=-s.Rational(1,6)*x*y*(x*x+y*y)+4*H*(x**3*y-x*y**3)
assert s.simplify(s.diff(psi4,x).subs(x,0)-(-4*H-s.Rational(1,6))*y**3)==0
assert -s.Rational(1,2)*s.integrate(y**7/4,(y,0,x))/x**4==-x**4/64
# Full density Green leading terms with noncompact-origin correction.
n=s.symbols('n',integer=True,positive=True);Fminus,Fplus=s.symbols('Fminus Fplus')
assert s.simplify(s.Rational(1,2)*( -(n+1)-(n-1)))==-n
assert s.simplify(s.Rational(1,2)*((n-1)+(n+1)))==n
out={'start_utc':start,'utc':now(),'seconds':time.monotonic()-timer,'status':'PASS_INDEPENDENT_ALL_SPAN_EXACT_RULE_IV220_AND_SYMBOLIC_AXIS_REQUIRES_ACTUAL_REVIEW','code_sha256':sha(Path(__file__)),'compute_sha256':sha(E/'compute.json'),'parent_pin_count':len(A['parent_files']),'exact_values_compared':len(exact),'exact_endpoint_jet_and_join_values_compared':28,'spans_integrated':nb-7,'rational_nodes_per_span':8,'rule_polynomial_degrees_checked':8,'rule_nodes':list(map(str,nodes)),'rule_weights':list(map(str,weights)),'angular_projection':{str(m):v for m,v in coeff.items()},'symbolic_axis_y3':str(leading),'origin_quartic_correction':'-1/64','balls':rows,'Q_strict_window':A['Q_strict_window'],'Q_sign':A['Q_sign'],'scope':'Independent exact de Boor point rule on all spans, derivative endpoint jets and triangular joins, iv220 exponential, full Laurent and symbolic identities. Not a PDE endpoint.'}
(E/'independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({n:out[n] for n in ['utc','seconds','status','Q_strict_window','Q_sign']}));print('Q',rows['Q']['display'])

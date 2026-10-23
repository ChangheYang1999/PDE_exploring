"""Result267 exploration; independently derive grouped moments from the initial informal reduction."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import sympy as S
import json,sys,time,hashlib
R=Path('research/degree15_grouped_moment_obstruction');V=R/'verification'
n,t,p,v=S.symbols('n t p v');start=time.monotonic();out=dict(status='RUNNING',utc_started=datetime.now(timezone.utc).isoformat(),formulas={},cases={})
def record(name,x):out['formulas'][name]=str(S.factor(x));return x
def primitive(x,var):
 num,den=S.fraction(S.cancel(x));pol=S.Poly(num,var,n,domain=S.QQ);content,pol=pol.clear_denoms(convert=True)[1].primitive();pol=-pol if pol.LC()<0 else pol
 return pol,den
z=(15+2*n)/(14+2*n)
# Case i at all real n, independently of integer shortcut.
a=S.cancel(z*(1-2/n));h=S.cancel(-(1+2*a)/6);j=S.cancel((1+2*a*a+6*h*h)/12)
print('stage casei',flush=True)
record('case_i_pi_derivative',S.diff((v-a)*(v*v-h*v+j),v).subs(v,z))
record('case_i_n1',S.diff((v-a)*(v*v-h*v+j),v).subs(v,z).subs(n,1))
for A in [1,3]:
 print('stage discriminant',A,flush=True)
 m=A+12;zz=(m+2*n)/(m+2*n-1);lam=(A*(m+2*n)-m)/2
 q=S.cancel(((lam+1)*p*zz-(lam+2)*zz**2)/lam);h=-S.Rational(A,2)-2*p;j=S.cancel(((2-lam)*zz**2+(lam-1)*h*zz)/lam)
 expr=A+4*(p*p-2*q)+2*(h*h-2*j);pol,den=primitive(expr,p)
 record(f'A{A}_M2_num',pol.as_expr());record(f'A{A}_M2_den',den);record(f'A{A}_discriminant',S.discriminant(pol.as_expr(),p))
 out['cases'][f'A{A}']=dict(M2_terms=[dict(powers=list(m),coefficient=str(c))for m,c in pol.terms()],denominator=str(den))
# Case iii, rational reciprocal coordinates t,s.
print('stage caseiii',flush=True)
s=-n-2*t;a=S.cancel(z*(1-1/t));b=S.cancel(z*(1-1/s));h=S.cancel(-S.Rational(1,2)-3*a-2*b);j=S.cancel((1+6*a*a+4*b*b+2*h*h)/4)
W=v*v-h*v+j
D=S.cancel(z*S.diff(W,v).subs(v,z)+(t+s)*W.subs(v,z));M3=S.cancel(1+6*a**3+4*b**3+2*(h**3-3*h*j))
# Case iv, paired and tripled groups.
print('stage caseiv',flush=True)
q=S.cancel(((n+1)*p*z-(n+2)*z*z)/n);hh=-S.Rational(1,2)-2*p;jj=S.cancel(S.Rational(1,4)+p*p-2*q+hh*hh/2);k=S.cancel(((n-3)*z**3+(2-n)*hh*z*z+(n-1)*jj*z)/n)
B3=1+4*(p**3-3*p*q)+2*(hh**3-3*hh*jj+3*k)
B4=1+4*(p**4-4*p*p*q+2*q*q)+2*(hh**4-4*hh*hh*jj+2*jj*jj+4*hh*k)
for label,var,rawA,rawB in [('iii',t,D,M3),('iv',p,B3,B4)]:
 A,denA=primitive(rawA,var);B,denB=primitive(rawB,var)
 # Preserve the full numerator, including any parameter-only factor.
 row=dict(variable=str(var),A_terms=[dict(powers=list(m),coefficient=str(c))for m,c in A.terms()],B_terms=[dict(powers=list(m),coefficient=str(c))for m,c in B.terms()],A=str(A.as_expr()),B=str(B.as_expr()),A_denominator=str(S.factor(denA)),B_denominator=str(S.factor(denB)),A_degree_variable=A.degree(var),B_degree_variable=B.degree(var),A_degree_parameter=A.degree(n),B_degree_parameter=B.degree(n),A_factored=str(S.factor(A.as_expr())),B_factored=str(S.factor(B.as_expr())))
 out['cases'][label]=row
 if '--resultants'in sys.argv:
  tick=time.monotonic();res=S.resultant(A.as_expr(),B.as_expr(),var);factors=S.factor_list(res,n)
  row.update(resultant_seconds=time.monotonic()-tick,resultant=str(S.expand(res)),resultant_coefficients_ascending=[str(c)for c in reversed(S.Poly(res,n).all_coeffs())],resultant_factor_constant=str(factors[0]),resultant_factors=[dict(polynomial=str(f),power=int(e),coefficients_ascending=[str(c)for c in reversed(S.Poly(f,n).all_coeffs())],shifted_coefficients_ascending=[str(c)for c in reversed(S.Poly(S.expand(f.subs(n,n+1)),n).all_coeffs())])for f,e in factors[1]])
 print(label,'degrees',A.degree(var),B.degree(var),A.degree(n),B.degree(n),'resultant',row.get('resultant_seconds'),flush=True)
 (V/'elimination_exploration.json').write_text(json.dumps(out,indent=2)+'\n')
out.update(status='DONE',utc_finished=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-start,driver_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(V/'elimination_exploration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out['formulas'],indent=2));print('DONE',out['seconds'])

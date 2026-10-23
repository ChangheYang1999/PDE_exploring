"""Independent discovery for result275; not the exact certificate verifier."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as S
import json,hashlib,time
R=Path('research/degree17_grouped_moment_obstruction');V=R/'verification'
n,x=S.symbols('n x');D=17+2*n;tau=(D-1)/D
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def terms(p):
 return [dict(powers=list(k),coefficient=str(v))for k,v in S.Poly(p,x,n,domain=S.QQ).terms()]
def powers(coeff,K):
 L=len(coeff)-1;out=[S.Integer(L)]
 for k in range(1,K+1):
  if k<=L:v=-sum(coeff[j]*out[k-j]for j in range(1,k))-k*coeff[k]
  else:v=-sum(coeff[j]*out[k-j]for j in range(1,L+1))
  out.append(S.cancel(v))
 return out
def row(eq):
 num,den=S.fraction(S.cancel(eq));p=S.Poly(num,x,n,domain=S.QQ);den0,p=p.clear_denoms();content,p=p.primitive()
 if p.LC()<0:p=-p;content=-content
 return dict(numerator_terms=terms(num),denominator_terms=terms(den),primitive_terms=terms(p.as_expr()),primitive_content=str(content/den0))
def univariate(p):return [str(v)for v in reversed(S.Poly(p,n).all_coeffs())]
def sign_cert(p):
 c,ff=S.factor_list(p,n);factors=[]
 for f,k in ff:
  coeff=univariate(f);shift=univariate(S.expand(f.subs(n,n+1)))
  factors.append(dict(coefficients_ascending=coeff,power=int(k),shifted_coefficients_ascending=shift,shift_all_positive=all(S.Rational(v)>0 for v in shift)))
 return dict(constant=str(c),factors=factors,coefficients_ascending=univariate(p))
cases=[('q22a','two',(5,4,2,2)),('q22b','two',(1,6,2,2)),('q23a','two',(1,2,4,3)),('q23b','two',(3,4,2,3)),('q24','two',(1,4,2,4)),('s112a','three',(1,8,4,2,2)),('s112b','three',(1,6,2,4,2)),('s112c','three',(3,6,4,2,2)),('s113','three',(1,6,4,2,3))]
out=dict(started_utc=datetime.now(timezone.utc).isoformat(),initial_proof_sha256=sha(R/'INITIAL_REDUCTION.md'),driver_sha256=sha(__file__),cases={})
for name,kind,par in cases:
 start=time.monotonic();print('START',name,datetime.now(timezone.utc).isoformat(),flush=True)
 if kind=='two':
  A,a,b,L=par;T=A*D-17;lam=T/S.Integer(a-b);c=S.cancel(((lam+1)*x-(lam+2))/lam);u=powers([1,-x,c],L+1);cw=[S.Integer(1)];sw=[S.Integer(L)]
  for k in range(1,L):
   sw.append(S.cancel(-(A*tau**k+a*u[k])/b));cw.append(S.cancel(-(sw[k]+sum(cw[j]*sw[k-j]for j in range(1,k)))/k))
  cw.append(S.cancel(sum((L-j)*cw[j]for j in range(L))/lam-sum(cw)));w=powers(cw,L+1)
  eq=[A*tau**k+a*u[k]+b*w[k]for k in [L,L+1]]
 else:
  A,a,b,w,L=par;T=A*D-17;s=S.cancel((-T-(a-w)*x)/(b-w));alpha=1-1/x;beta=1-1/s;co=[S.Integer(1)];ss=[S.Integer(L)]
  for k in range(1,L+1):
   ss.append(S.cancel(-(A*tau**k+a*alpha**k+b*beta**k)/w));co.append(S.cancel(-(ss[k]+sum(co[j]*ss[k-j]for j in range(1,k)))/k))
  ps=powers(co,L+1);eq=[A*tau**(L+1)+a*alpha**(L+1)+b*beta**(L+1)+w*ps[L+1],sum((L-j)*co[j]for j in range(L))+(x+s)*sum(co)]
 rr=[row(e)for e in eq];pp=[sum(S.Rational(t['coefficient'])*x**t['powers'][0]*n**t['powers'][1]for t in r['primitive_terms'])for r in rr]
 data=dict(kind=kind,parameters=par,equations=rr,degrees=[(S.degree(p,x),S.degree(p,n))for p in pp])
 if name.startswith('q22'):
  pol=S.Poly(pp[0],x);assert pol.degree()==2;disc=S.expand(pol.nth(1)**2-4*pol.nth(2)*pol.nth(0));data['discriminant']=sign_cert(disc)
 else:
  res=S.resultant(pp[0],pp[1],x);data['resultant']=sign_cert(res);data['degree_bound']=int(data['degrees'][1][0]*data['degrees'][0][1]+data['degrees'][0][0]*data['degrees'][1][1])
 data['degrees']=[[int(v)for v in p]for p in data['degrees']];data['wall_seconds']=time.monotonic()-start;out['cases'][name]=data
 (V/'certificate_partial.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',name,data['degrees'],data['wall_seconds'],flush=True)
out['finished_utc']=datetime.now(timezone.utc).isoformat();(V/'certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE ALL',out['finished_utc'],flush=True)

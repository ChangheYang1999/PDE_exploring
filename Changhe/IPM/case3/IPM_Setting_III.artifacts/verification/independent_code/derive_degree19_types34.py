"""Result282 independent discovery in normalized q=v/z, not a certificate checker."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time,resource
import sympy as S
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3))
R=Path('research/degree19_grouped_moment_obstruction');V=R/'verification'
x,y,t,n=S.symbols('x y t n');D=19+2*n;tau=(D-1)/D
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def terms(p,variables):
 return [dict(powers=list(k),coefficient=str(v))for k,v in S.Poly(p,*variables,domain=S.QQ).terms()]
def row(eq,variables):
 num,den=S.fraction(S.cancel(eq));pol=S.Poly(num,*variables,domain=S.QQ);d,pol=pol.clear_denoms();c,pol=pol.primitive()
 if pol.LC()<0:pol=-pol;c=-c
 return dict(numerator_terms=terms(num,variables),denominator_terms=terms(den,variables),primitive_terms=terms(pol.as_expr(),variables),primitive_content=str(c/d))
def expr(data,variables):
 return sum(S.Rational(r['coefficient'])*S.prod(v**p for v,p in zip(variables,r['powers']))for r in data)
def ps(co,K):
 L=len(co)-1;out=[S.Integer(L)]
 for j in range(1,K+1):
  if j<=L:a=-sum(co[k]*out[j-k]for k in range(1,j))-j*co[j]
  else:a=-sum(co[k]*out[j-k]for k in range(1,L+1))
  out.append(S.cancel(a))
 return out
def ucoeff(p):return [str(a)for a in reversed(S.Poly(p,n).all_coeffs())]
def sign(p):
 c,ff=S.factor_list(p,n);fs=[]
 for f,k in ff:
  shift=ucoeff(S.expand(f.subs(n,n+1)));fs.append(dict(coefficients_ascending=ucoeff(f),power=int(k),shifted_coefficients_ascending=shift,shift_all_positive=all(S.Rational(a)>0 for a in shift)))
 return dict(constant=str(c),factors=fs,coefficients_ascending=ucoeff(p))
def pair_result(equations,var,label):
 print('RESULTANT START',label,datetime.now(timezone.utc).isoformat(),flush=True)
 rr=[row(e,(var,n))for e in equations];pp=[expr(r['primitive_terms'],(var,n))for r in rr];deg=[[int(S.degree(p,v))for v in(var,n)]for p in pp];bound=deg[1][0]*deg[0][1]+deg[0][0]*deg[1][1]
 # The installed resultant returned the opposite sign for the linear/cubic
 # pivot. Use the defining linear-factor formula here; the independent
 # checker still verifies the full Sylvester determinant identity.
 if deg[0][0]==1:
  aa=S.Poly(pp[0],var).nth(1);bb=S.Poly(pp[0],var).nth(0)
  res=S.cancel(aa**deg[1][0]*pp[1].subs(var,-bb/aa))
 else:res=S.resultant(*pp,var)
 sc=sign(res);print('RESULTANT DONE',label,deg,len(sc['coefficients_ascending'])-1,all(f['shift_all_positive']for f in sc['factors']),flush=True)
 return dict(equations=rr,degrees=deg,degree_bound=bound,resultant=sc)
out=dict(started_utc=datetime.now(timezone.utc).isoformat(),driver_sha256=sha(__file__),initial_proof_sha256=sha(R/'INITIAL_REDUCTION.md'),cases={})
def save():
 (V/'types_III_IV_partial.json').write_text(json.dumps(out,indent=2)+'\n')
print('TYPE III START',datetime.now(timezone.utc).isoformat(),flush=True)
u3=((n+3)-(n+2)*x+(n+1)*y)/n;uc=[1,-x,y,-u3];pu=ps(uc,5)
w1=S.cancel(-(tau+4*pu[1])/2);c1=-w1;w2=S.cancel(-(tau**2+4*pu[2])/2);c2=S.cancel(-(w2+c1*w1)/2);c3=S.cancel((3+2*c1+c2)/n-1-c1-c2);wc=[1,c1,c2,c3];pw=ps(wc,5);mom=[S.cancel(tau**k+4*pu[k]+2*pw[k])for k in range(1,6)]
r3=row(mom[2],(x,y,n));p3=expr(r3['primitive_terms'],(x,y,n));poly=S.Poly(p3,y);assert poly.degree()==1;C1=poly.nth(1);C0=poly.nth(0)
data=dict(moment3=r3,C1_terms=terms(C1,(x,n)),C0_terms=terms(C0,(x,n)),pivot_branch=pair_result([C1,C0],x,'III pivot'))
out['cases']['III']=data;save()
data['generic']=pair_result([e.subs(y,-C0/C1)for e in mom[3:]],x,'III generic');save()
print('TYPE IV START',datetime.now(timezone.utc).isoformat(),flush=True)
alpha=1-1/t;L1=-n-2*t;L2=n+t;v=S.cancel(-(tau+6*alpha+4*x)/2);c=S.cancel((2-x)/L1-1+x);k=S.cancel((2-v)/L2-1+v);pu=ps([1,-x,c],4);pw=ps([1,-v,k],4);mom=[S.cancel(tau**j+6*alpha**j+4*pu[j]+2*pw[j])for j in range(1,5)]
p2=S.Poly(mom[1],x);assert p2.degree()==2 and p2.nth(2)==12;B=p2.nth(1);C=p2.nth(0)
def remainder(eq):
 p=S.Poly(eq,x);r0=0;r1=0;power=[S.Integer(1),S.Integer(0)]
 for j in range(p.degree()+1):
  r0+=p.nth(j)*power[0];r1+=p.nth(j)*power[1]
  power=[S.cancel(-C*power[1]/12),S.cancel(power[0]-B*power[1]/12)]
 return S.cancel(r1),S.cancel(r0)
r1,r0=remainder(mom[2]);r3,r2=remainder(mom[3]);N1=S.cancel(r1*r2-r0*r3);N2=S.cancel(12*r0**2-B*r0*r1+C*r1**2)
data=dict(moments=[row(e,(x,t,n))for e in mom[1:]],B=row(B,(t,n)),C=row(C,(t,n)),remainders=[row(e,(t,n))for e in [r1,r0,r3,r2]],generic=pair_result([N1,N2],t,'IV generic'),branches={});out['cases']['IV']=data;save()
for branch in ('L1zero','L2zero'):
 if branch=='L1zero':
  tt=-n/2;aa=1+2/n;xx=S.Integer(2);vv=S.cancel(-(tau+6*aa+4*xx)/2);kk=S.cancel((2-vv)/(n/2)-1+vv);cc=S.cancel((tau**2+6*aa**2+4*xx**2+2*vv**2-4*kk)/8)
 else:
  tt=-n;aa=1+1/n;vv=S.Integer(2);xx=S.cancel(-(tau+6*aa+2*vv)/4);cc=S.cancel((2-xx)/n-1+xx);kk=S.cancel((tau**2+6*aa**2+4*xx**2-8*cc+2*vv**2)/4)
 up=ps([1,-xx,cc],4);wp=ps([1,-vv,kk],4);mm=[S.cancel(tau**j+6*aa**j+4*up[j]+2*wp[j])for j in range(1,5)];rr=[row(e,(n,))for e in mm[2:]]
 data['branches'][branch]=dict(values={k:row(v,(n,))for k,v in [('t',tt),('alpha',aa),('x',xx),('v',vv),('c',cc),('k',kk)]},moments=rr,sign_certificates=[sign(expr(r['primitive_terms'],(n,)))for r in rr]);save();print('BRANCH DONE',branch,flush=True)
special=[]
for nn in (1,2):
 z=S.Rational(19+2*nn,18+2*nn);v1=z*(1-S.Rational(3,nn));b1=-(1+2*v1)/8;b2=(1+2*v1**2+8*b1**2)/16;pi=z*z-b1*z+b2+(z-v1)*(2*z-b1);special.append(dict(n=nn,z=str(z),v1=str(v1),pair_sum=str(b1),pair_product=str(b2),pi_prime=str(pi)))
out['special_e2']=special;out['finished_utc']=datetime.now(timezone.utc).isoformat();save();(V/'types_III_IV_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE ALL',out['finished_utc'],flush=True)

from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json,hashlib
R=Path('research/e2_integer_divisor_audit');V=R/'verification';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(a,b,e=None):checks.append(dict(name=a,passed=bool(b),evidence=e))
def zero(a,b):ck(a,s.cancel(b)==0)
n,v,mu,k,t,D,h,d,N,g=s.symbols('n nu mu k t D h d N g')
A=n*n*(2*v+2*n+2*k+1);B=4*n*(k*k+3*n*k+2*n*(n+v));C=4*(4*n-v)*k**3+4*n*(14*n+3*v)*k*k+64*n*n*(n+v)*k+24*n*n*(n+v)**2
u=-k/n;ss=-(t+2*v*u)/(2*(v+n+k));jj=t*t/(4*(v+n+k))+v*u*u/(2*(v+n+k))+ss*ss/2
zero('direct node derivative equals Q',8*(v+n+k)**2*n*n*(3-2*(ss+u)+jj+u*ss)-(C+B*t+A*t*t))
Qexpanded=4*(4*n-v)*k**3+4*n*(14*n+3*v+t)*k*k+2*n*n*(32*n+32*v+t*t+6*t)*k+n*n*(24*(n+v)**2+(2*n+2*v+1)*t*t+8*(n+v)*t)
zero('positive power expansion',Qexpanded-C-B*t-A*t*t)
zero('C discriminant',s.discriminant(C,v)-16*k*k*(k+n)**2*(k*k-8*n*k-8*n*n))
ck('C leading',s.Poly(C,v).LC()==24*n*n)
F=s.expand(D*D*C+D*(D-1)*B+(D-1)**2*A);DD=6*v+6*n+4*k+1
zero('3A identity',3*A-n*n*(DD+2*k+2))
R9=2*n*n*D**4+(-2*k**3+6*n*k*k+16*n*n*k+n*n)*D**3+2*(4*k**4+18*n*k**3+k**3+18*n*n*k*k+3*n*k*k+3*n*n*k-3*n*n)*D*D-n*(12*k*k+24*k*n-n)*D+2*n*n*(k+1)
zero('second divisibility identity',3*F.subs(v,(D-6*n-4*k-1)/6)-R9)
K=n*(25*n-12)+2*N*h
zero('second congruence substitution',2*N*h-n*(12*(h*d-1)**2+24*n*(h*d-1)-n)-(K-12*n*h*h*d*d-24*n*h*(n-1)*d))
source=(V/'source_question.md').read_text();line=next(t for t in source.splitlines()if t.startswith('num = '));P=s.sympify(line[6:],locals={'n':n,'nu':v,'mu':mu})
zero('every original polynomial coefficient',4*P.subs(mu,v+n+k)-F.subs(D,DD))
rr=(1+2*v+4*mu+2*n)/(2*v+4*mu+2*n);aa=rr*(1-(mu-v)/n);SS=-(1+2*v*aa)/(2*mu);JJ=(1+2*v*aa*aa+2*mu*SS*SS)/(4*mu);EE=3*rr*rr-2*(SS+aa)*rr+JJ+aa*SS
zero('direct original clearing identity',8*mu*mu*n*n*(2*mu+n+v)**2*EE-P)
zero('boundary identity',P.subs(mu,n+v)-27*n*n*(n+v)**2*(2*n+2*v+1)*(4*n+4*v+1))
terms=[dict(powers=list(ex),coefficient=int(co))for ex,co in s.Poly(P,n,v,mu).terms()]
(V/'original_polynomial.json').write_text(json.dumps(dict(variables=['n','nu','mu'],terms=terms,source_sha256=sha(V/'source_question.md')),indent=2)+'\n')
(V/'polynomial_terms.tsv').write_text(''.join(' '.join(map(str,[x['coefficient'],*x['powers']]))+'\n'for x in terms))
ck('degree at most6',max(sum(t['powers'])for t in terms)==6)
ck('machine upper bound128',24*1000*250000**2*26000000<2**127)
ck('sieve bound',s.Rational(51,2)*1000**2-12*1000<26000000)
for nn in [1,2,3,4,5,8,10,16,25,32,60,64,100,128,256,500,512,800,1000]:
 gs=[x for x in s.divisors(nn*nn)if x%2 and x>4]
 ck('positive K bound '+str(nn),all(0<nn*(25*nn-12)+2*(nn*nn//gg)*hh<26*nn*nn for gg in gs for hh in {1,(gg-1)//4}))
 if nn&(nn-1)==0:ck('power of two no g '+str(nn),not gs)
for x in json.loads((V/'INPUTS.json').read_text())['files']:ck('input '+x['file'],sha(V/x['file'])==x['sha256'])
j=dict(status='PASS'if all(x['passed']for x in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,proof_sha256=sha(R/'PROOF.md'),driver_sha256=sha(__file__),input_sha256=sha(V/'INPUTS.json'),polynomial_sha256=sha(V/'original_polynomial.json'),terms_sha256=sha(V/'polynomial_terms.tsv'),scope='Exact identities and arithmetic proof only; finite enumeration not yet performed')
(V/'ALGEBRA_CHECKS.json').write_text(json.dumps(j,indent=2)+'\n');print(j['status'],j['count']);print([x for x in checks if not x['passed']]);raise SystemExit(j['status']!='PASS')

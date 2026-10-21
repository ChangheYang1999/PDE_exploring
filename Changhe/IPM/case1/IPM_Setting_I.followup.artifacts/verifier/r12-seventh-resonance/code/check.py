"""Own exact axis reconstruction at A=2, no imported lane code."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
import sympy as s
start=time.time();x,y=s.symbols('x y');R=s.Rational
out=Path(__file__).resolve().parents[1]/'verification'
def norm(e):return s.factor(s.cancel(e))
w=-2*x*(4-x*x)/(4+x*x);g=4*x*x/(4+x*x);h=3-s.diff(w,x)
G={1:g,3:R(64,3)*x*x/(x*x+4)**3,5:x*x*(11*x**6+88*x**4-1872*x*x+9984)/(90*(x*x+4)**5)}
a={0:w};b={1:h};F={};H={};checks={}
for j in [3,5,7]:
 a[j-1]=norm((s.diff(b[j-2],x)+s.diff(G[j-2],x))/(j-1));b[j]=norm(-s.diff(a[j-1],x)/j)
 F[j]=norm(-sum(a[k]*s.diff(G[j-k],x)+(j-k)*b[k+1]*G[j-k] for k in range(2,j,2)))
 H[j]=x**(2*j+R(j-1,2))*(1+x*x/4)**(-j)*(1-x*x/4)**(-R(j-1,2))
 checks['homogeneous_'+str(j)]=str(norm(w*s.diff(H[j],x)+(j*h-1)*H[j]))
 if j in G:checks['transport_'+str(j)]=str(norm(w*s.diff(G[j],x)+(j*h-1)*G[j]-F[j]))
checks['transport_1']=str(norm(w*s.diff(g,x)+(h-1)*g))
I=norm(-F[7]/(w*H[7]));print('F7',F[7],flush=True);print('integrand',I,flush=True)
terms={}
for t in s.Add.make_args(s.expand(I)):
 c,e=t.as_coeff_exponent(x)
 if c.has(x) or not e.is_integer:raise ValueError('Not a Laurent polynomial',t)
 terms[int(e)]=terms.get(int(e),s.S.Zero)+c
if terms.get(-1,0)!=0:raise ValueError('log term, handle explicitly')
primitive=sum(c*x**(e+1)/(e+1) for e,c in terms.items());B=norm(primitive.subs(x,2));G[7]=norm(H[7]*(B-primitive))
checks['primitive']=str(norm(s.diff(primitive,x)-I));checks['transport_7']=str(norm(w*s.diff(G[7],x)+(7*h-1)*G[7]-F[7]))
checks['source_7']=str(s.limit(G[7]/H[7],x,2,dir='-'))
checks['source_3']=str(s.limit(G[3]/H[3],x,2,dir='-'));checks['source_5']=str(s.limit(G[5]/H[5],x,2,dir='-'))
checks['first_order_divergence']=str(norm(s.diff(w,x)+h-3))
assert all(v=='0' for v in checks.values()),checks
result={'date':datetime.now(timezone.utc).isoformat(),'source_md5':hashlib.md5(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'F7':str(F[7]),'negative_integrand':str(I),'Laurent_coefficients':{str(e):str(c) for e,c in sorted(terms.items())},'primitive':str(primitive),'B7':str(B),'B7_decimal':str(s.N(B,35)),'G7_selected':str(G[7]),'G7_center17':str(s.expand(s.series(G[7],x,0,18).removeO()).coeff(x,17)),'axis_coefficients':{'a'+str(j):str(v) for j,v in a.items()}|{'b'+str(j):str(v) for j,v in b.items()},'seconds':time.time()-start}
(out/'check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)

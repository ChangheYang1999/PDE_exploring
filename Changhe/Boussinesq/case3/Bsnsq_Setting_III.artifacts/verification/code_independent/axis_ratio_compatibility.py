"""P242: independent physical-x jet derivation and exact formal-series elimination.
No numerical-lane imports or execution. Lead polynomial data are comparisons only.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,os,resource,time
os.environ.setdefault('SYMPY_GROUND_TYPES','flint')
import sympy as s
from sympy.polys.fields import field
from sympy.polys.rings import ring
ROOT=Path('research/242_two_axis_ratios_beta_gt2/verification')
beta,A0,B0,D0,c2,c4=s.symbols('beta A0 B0 D0 c2 c4')
a,A,a1,a2,a3=s.symbols('a A a1 a2 a3')
JETS=(a,A,a1,a2,a3)
PARAM=(beta,A0,B0,D0,c2,c4)
ALL=PARAM+JETS
utc=lambda:datetime.now(timezone.utc).isoformat()
def write(name,data):
 (ROOT/name).write_text(json.dumps(data,indent=2)+'\n')
def polydata(expr,variables):
 p=s.Poly(s.expand(expr),*variables,domain=s.QQ)
 return {'variables':[str(v)for v in variables],'terms':[[list(m),str(c)]for m,c in p.terms()]}
def restore(p):
 vv=s.symbols(' '.join(p['variables']),seq=True)
 return sum((s.Rational(c)*s.prod(x**e for x,e in zip(vv,m))for m,c in p['terms']),s.S.Zero)
def rationaldata(expr,variables):
 n,d=s.fraction(s.cancel(expr));return {'numerator':polydata(n,variables),'denominator':polydata(d,variables)}
def checks_doc():return {'started_utc':utc(),'checks':[]}
def ck(out,name,truth,**data):
 out['checks'].append({'name':name,'pass':bool(truth),**data})
 if not truth:raise AssertionError(name)
def finish_checks(name,out,start):
 out.update(ended_utc=utc(),elapsed_seconds=time.monotonic()-start,passed=sum(q['pass']for q in out['checks']),total=len(out['checks']),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 write(name,out);print(name,out['passed'],out['elapsed_seconds'],flush=True)
def derive():
 start=time.monotonic();out=checks_doc()
 dy=lambda f:s.diff(f,a)*a1+s.diff(f,A)*a+s.diff(f,a1)*a2+s.diff(f,a2)*a3
 alpha=(beta-2)/2;L=(3*beta+2)/2
 H=A0/a**2;B=B0/a**4;D=D0/a**6
 phi=L*A/a;w=2*beta-dy(phi)
 d2=3*alpha*B0/(2*A0);d4=10*alpha*D0/(3*A0)-5*alpha*B0**2/(2*A0**2)
 p=(c2+d2*A)/a**3;q=(c4+d4*A)/a**5
 b=-dy(dy(phi))-2*p;e=-dy(dy(p))/3-4*q
 ck(out,'temperature x2 identity',s.cancel(phi*dy(H)+2*w*H-(beta-2)*H)==0)
 ck(out,'temperature x4 identity',s.cancel(w*B-dy(p)*H/3+phi*dy(B)/4+p*dy(H)/2-(beta-2)*B/4)==0)
 ck(out,'temperature x6 identity',s.cancel(w*D-dy(p)*B/3-dy(q)*H/5+phi*dy(D)/6+p*dy(B)/4+q*dy(H)/2-(beta-2)*D/6)==0)
 R1=s.cancel(phi*dy(b)+(1+w)*b-H)
 R3=s.cancel(phi*dy(e)+(1+3*w)*e-dy(p)*b/3+p*dy(b)-B)
 N1=s.cancel(4*A0*a**5*R1);N3=s.cancel(12*A0**2*a**7*R3)
 ck(out,'cleared first equation is polynomial',s.denom(N1)==1)
 ck(out,'cleared third equation is polynomial',s.denom(N3)==1)
 write('physical_equations.json',{'N1':polydata(N1,ALL),'N3':polydata(N3,ALL),'normalization':['N1=4*A0*a^5*R1','N3=12*A0^2*a^7*R3'],'derivation':'physical x jets; no imported lead equations'})
 ck(out,'origin coefficient Y0',s.expand(N1.subs({a:1,A:0,a1:s.Symbol('r1')})-A0*(beta*(3*beta+2)*s.Symbol('r1')-4*(A0+beta*c2)))==0)
 weights=(0,1,-1,-2,-3);P=s.Poly(N1,*JETS)
 minimum=min(sum(e*w0 for e,w0 in zip(m,weights))for m,c in P.terms())
 ck(out,'all first-equation monomial weights at least minus1',minimum>=-1,minimum=minimum)
 principal=sum((c*s.prod(v**e for v,e in zip(JETS,m)) for m,c in P.terms()if sum(e*w0 for e,w0 in zip(m,weights))==-1 and sum(m[2:])==1),s.S.Zero)
 principal=s.expand(principal.subs(a,1))
 expected=A0*((3*beta+2)**2*A**2*a3+(3*beta+2)*(7*beta+4)*A*a2+beta*(3*beta+2)*a1)
 ck(out,'principal linear Euler operator exact',s.expand(principal-expected)==0)
 m=s.symbols('m',integer=True,positive=True)
 eigen=s.expand((3*beta+2)**2*m*(m-1)*(m-2)+(3*beta+2)*(7*beta+4)*m*(m-1)+beta*(3*beta+2)*m)
 target=(3*beta+2)*m**2*((3*beta+2)*m-2*beta-2)
 ck(out,'general symbolic recursion coefficient',s.expand(eigen-target)==0)
 ck(out,'constant solution at B0=0 and A0+beta*c2=0',s.cancel(N1.subs({a:1,a1:0,a2:0,a3:0,B0:0,c2:-A0/beta}))==0)
 y,z1,z2,z3,z4,z5=s.symbols('y z1 z2 z3 z4 z5')
 trans=s.cancel(y*(N1/A0).subs({B0:0,a:z1,A:y*z4,a1:z2/y,a2:z3/y**2,a3:z5/y**3}))
 ck(out,'Fuchsian transformed equation polynomial',s.denom(trans)==1)
 ck(out,'Fuchsian leading coefficient',s.expand(s.diff(trans,z5)-(3*beta+2)**2*z1**2*z4**2)==0)
 ck(out,'Fuchsian equilibrium identity',s.cancel(trans.subs({z1:1,z2:0,z3:0,z4:1,z5:0,c2:-A0/beta}))==0)
 write('fuchsian_equation.json',polydata(trans,(beta,A0,c2,y,z1,z2,z3,z4,z5)))
 finish_checks('derivation_checks.json',out,start)
 return N1,N3

class Jet:
 """Finite formal power series with exact ring coefficients."""
 def __init__(self,coeff,n,R):self.n=n;self.R=R;self.c=(list(coeff)+[R.zero]*(n+1))[:n+1]
 def asjet(self,v):return v if isinstance(v,Jet) else Jet([self.R(v)],self.n,self.R)
 def __add__(self,v):
  v=self.asjet(v);return Jet([x+y for x,y in zip(self.c,v.c)],self.n,self.R)
 __radd__=__add__
 def __neg__(self):return Jet([-v for v in self.c],self.n,self.R)
 def __sub__(self,v):return self+-self.asjet(v)
 def __mul__(self,v):
  v=self.asjet(v);d=[self.R.zero]*(self.n+1)
  for i,x in enumerate(self.c):
   if not x:continue
   for j,y in enumerate(v.c[:self.n+1-i]):
    if y:d[i+j]+=x*y
  return Jet(d,self.n,self.R)
 __rmul__=__mul__
 def __pow__(self,k):
  r=Jet([self.R.one],self.n,self.R);v=self
  while k:
   if k&1:r=r*v
   k>>=1
   if k:v=v*v
  return r

def chart(which,N1,N3,order=8):
 start=time.monotonic();out=checks_doc();out['chart']=which
 t,u=s.symbols('t u')
 if which==0:
  K,bb=field('beta',s.QQ);R,uu,cc,dd,zz=ring('u c4 D0 z',K);choice={A0:beta,c2:s.Integer(-1)};r1=R.zero
 else:
  K,bb,tt=field('beta t',s.QQ);R,uu,cc,dd,zz=ring('u c4 D0 z',K);choice={A0:beta*(3*beta+2-4*t)/4,c2:t};r1=R.one
 def compile_polynomial(poly):
  terms=[]
  for powers,coef in s.Poly(poly,*JETS).terms():
   cf=s.expand(coef.subs(choice).subs(B0,u));terms.append((powers,R.from_expr(cf)))
  return terms
 P1=compile_polynomial(N1);P3=compile_polynomial(N3)
 def evaluate(terms,coeff,n):
  coeff=(list(coeff)+[R.zero]*(n+4))[:n+4]
  deriv=lambda c:[(i+1)*c[i+1]for i in range(len(c)-1)]
  integ=[R.zero]+[coeff[i]*K(s.Rational(1,i+1))for i in range(n)]
  derivative1=deriv(coeff);derivative2=deriv(derivative1);derivative3=deriv(derivative2)
  variables=[Jet(c,n,R)for c in [coeff,integ,derivative1,derivative2,derivative3]]
  # Independent generic series algebra, compiled only from own physical equations.
  cached={(i,0):Jet([R.one],n,R)for i in range(5)}
  total=Jet([],n,R)
  for powers,coef in terms:
   term=Jet([coef],n,R)
   for i,k in enumerate(powers):
    if not k:continue
    if (i,k)not in cached:cached[i,k]=variables[i]**k
    term=term*cached[i,k]
   total=total+term
  return total.c
 def samezero(name,polynomial):ck(out,name,polynomial==R.zero)
 def base_scalar(polynomial):
  ck(out,'divisor independent of u,c4,D0,z '+str(len(out['checks'])),len(polynomial.terms())==1 and polynomial.terms()[0][0]==(0,0,0,0))
  return polynomial.terms()[0][1]
 rs=[R.one,r1];divisors=[]
 for n in range(1,order+1):
  e=evaluate(P1,rs+[zz],n)[n];slope=e.diff(zz);samezero('triangular linearity '+str(n),slope.diff(zz))
  c=base_scalar(slope);expected=K.from_expr(s.expand((A0*(3*beta+2)*(n+1)**2*((3*beta+2)*(n+1)-2*beta-2)).subs(choice)))
  ck(out,'exact general recursion multiplier '+str(n),c==expected)
  rs.append(-(e-slope*zz)*(1/c));divisors.append(c.as_expr())
  print('CHART',which,'r',n+1,'elapsed',round(time.monotonic()-start,3),utc(),flush=True)
 samezero('origin equation',evaluate(P1,rs,0)[0])
 third=evaluate(P3,rs,order-2)
 slope4=third[0].diff(cc);k4=base_scalar(slope4);samezero('c4 linearity',slope4.diff(cc));v4=-(third[0]-slope4*cc)*(1/k4)
 e1=third[1].compose(cc,v4);slope6=e1.diff(dd);k6=base_scalar(slope6);samezero('D0 linearity',slope6.diff(dd));v6=-(e1-slope6*dd)*(1/k6)
 reduced=[v.compose(cc,v4).compose(dd,v6)for v in third[2:]]
 for i,v in enumerate(reduced):
  for vv in [cc,dd,zz]:samezero('eliminated variable '+str(i)+' '+str(vv),v.diff(vv))
 def pack_ring(v):
  return [{'powers':list(m),'numerator':[[list(mm),str(co)]for mm,co in cf.numer.terms()],'denominator':[[list(mm),str(co)]for mm,co in cf.denom.terms()]}for m,cf in v.terms()]
 data={'chart':which,'field_variables':list(K.symbols),'ring_variables':['u','c4','D0','z'],'r':[pack_ring(v)for v in rs],'c4':pack_ring(v4),'D0':pack_ring(v6),'reduced':[pack_ring(v)for v in reduced],'source_equations_sha256':hashlib.sha256((ROOT/'physical_equations.json').read_bytes()).hexdigest()}
 data['field_variables']=[str(x)for x in data['field_variables']]
 write(f'chart{which}_raw.json',data)
 # Sparse JSON certificates can be read without executing a pickle.
 common_variables=(beta,t,u) if which else (beta,u)
 expanded={'chart':which,'reduced':[],'divisors':[str(s.factor(v))for v in divisors+[k4.as_expr(),k6.as_expr()]]}
 for i,v in enumerate(reduced):
  expanded['reduced'].append(rationaldata(v.as_expr(),common_variables));print('PACK',which,i,round(time.monotonic()-start,2),flush=True)
 write(f'chart{which}_reduced.json',expanded)
 finish_checks(f'chart{which}_checks.json',out,start)

if __name__=='__main__':
 resource.setrlimit(resource.RLIMIT_AS,(12*1024**3,12*1024**3))
 parser=argparse.ArgumentParser();parser.add_argument('--derive',action='store_true');parser.add_argument('--charts',default='');args=parser.parse_args()
 if args.derive:N1,N3=derive()
 else:
  e=json.loads((ROOT/'physical_equations.json').read_text());N1,N3=restore(e['N1']),restore(e['N3'])
 for which in args.charts.split(','):
  if which:chart(int(which),N1,N3)

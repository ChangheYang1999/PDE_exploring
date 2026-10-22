"""Independent Hamilton differentiation, rational rates and Arb/iv symmetric-matrix checks."""
import os
for v in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[v]='1'
import sys,json,hashlib,time,itertools
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as s,flint,mpmath
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/transition_scale/evidence';ctx.prec=512;ctx.threads=1;iv.dps=180;t0=time.monotonic();count=0
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
x,y,xi,eta=s.symbols('x y xi eta',real=True);aa=s.Function('a')(x,y);v=s.Function('v')(x,y);w=s.Function('w')(x,y);phi=s.Function('phi')(x);b,sigma,c0=s.symbols('b sigma c0',real=True)
p=v*xi+w*eta;Q=xi*xi+aa*aa*eta*eta
H=lambda f:s.diff(p,xi)*s.diff(f,x)+s.diff(p,eta)*s.diff(f,y)-s.diff(p,x)*s.diff(f,xi)-s.diff(p,y)*s.diff(f,eta)
def zero(z):
 global count
 assert s.simplify(s.expand(z))==0;count+=1
va=(v*s.diff(aa,x)+w*s.diff(aa,y))/aa
zero(-H(phi-b*s.log(aa)+sigma*s.log(Q)/2)-(-v*s.diff(phi,x)+b*va+sigma*(s.diff(v,x)*xi**2+(s.diff(w,x)+aa**2*s.diff(v,y))*xi*eta+aa**2*(s.diff(w,y)-va)*eta**2)/Q))
bf=s.Function('b')(x);zero(-H(phi-bf*s.log(aa))+v*s.diff(phi,x)-bf*va-v*s.diff(bf,x)*s.log(aa))
lam=s.Function('lam')(x);wx=s.Function('w')(x);mu=s.Function('mu')(x);A=s.sqrt(y*y+lam*lam);va2=(wx*s.diff(A,x)+mu*y*s.diff(A,y))/A
zero(va2-(wx*lam*s.diff(lam,x)+mu*y*y)/(lam*lam+y*y))
beta=-c0-wx*s.diff(phi,x)+b*va2+sigma*(s.diff(wx,x)*xi**2+s.diff(mu,x)*y*xi*eta+A*A*(mu-va2)*eta**2)/(xi*xi+A*A*eta*eta)
zero(beta.subs({y:0,xi:0})-(-c0-wx*s.diff(phi,x)+sigma*mu+(b-sigma)*wx*s.diff(lam,x)/lam))
tau=s.symbols('tau',real=True);S=s.Matrix([[s.diff(wx,x),s.diff(mu,x)/2],[s.diff(mu,x)/2,0]]);vv=s.Matrix([xi,tau]);ray=(vv.T*S*vv)[0]/(xi*xi+tau*tau)
zero(ray.subs(tau,-wx*xi/mu)-(s.diff(wx,x)-wx*s.diff(mu,x)/mu)/(1+(wx/mu)**2))
gx,gy,z=s.symbols('gx gy z',real=True);couple=s.Matrix([[-gy,gx/2],[gx/2,0]]);cp=couple.charpoly();cg=cp.gen;zero(cp.as_expr()-(cg*cg+gy*cg-gx*gx/4))
G=s.symbols('G',positive=True);zero((s.sqrt(gx*gx+G*G)-G)/2-gx*gx/(2*(s.sqrt(gx*gx+G*G)+G)))
# Exact coupling limit in physical frequencies, with bounded constant gradients.
q=(gx*xi*eta-gy*xi*xi)/(xi*xi+eta*eta);assert s.limit(q.subs(eta,tau/y),y,0)==0
cut=s.Function('theta')(y/lam);zero(wx*s.diff(cut,x)+mu*y*s.diff(cut,y)-s.Subs(s.Derivative(s.Function('theta')(z),z),z,y/lam)*(mu*y/lam-y*wx*s.diff(lam,x)/lam**2))
# Rational corner minima: separate Sympy and Fraction calculations, no rounded inputs.
sig=F(13,4);bb=F(307,100);corners=[]
for ap,mup in itertools.product([F(10),F(51,5)],[F(99,100),F(101,100)]):
 value=(sig-F(1,2))*ap+(bb-F(1,2))*mup-1
 sym=(s.Rational(13,4)-s.Rational(1,2))*s.Rational(ap.numerator,ap.denominator)+(s.Rational(307,100)-s.Rational(1,2))*s.Rational(mup.numerator,mup.denominator)-1
 assert str(value)==str(sym);corners.append({'A':str(ap),'mu':str(mup),'rate':str(value)})
assert min(F(r['rate']) for r in corners)==F(290443,10000)
collapse=[]
for n,nu in itertools.product(range(17),[1,2]):
 xq=F(1,2**n);rate=sig-F(3,2)+(sig-bb)*nu/xq
 assert rate>0;collapse.append({'x':str(xq),'nu':nu,'rate':str(rate)})
assert collapse[-1]['rate']==str(F(7,4)+F(9,50)*2*2**16)
# Separate validated radicals for representative symmetric matrices, plus rational Rayleigh direction checks.
def ar(q):q=F(q);return arb(q.numerator)/q.denominator
def ii(q):q=F(q);return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def ae(v):
 assert v.is_finite();out=[]
 for t in [v.lower(),v.upper()]:
  assert t.rad()==0;n,e=t.man_exp();out.append(F(int(n))*F(2)**int(e))
 return out
def ie(v):return [(-1 if sg else 1)*F(int(n))*F(2)**int(e) for sg,n,e,bc in v._mpi_]
pack=lambda e:{'lower_exact':str(e[0]),'upper_exact':str(e[1])}
matrices=[];rays=0
for m11,m12,m22 in [(F(10),F(1,3),F(0)),(F(-10),F(3,7),F(0)),(F(51,5),F(-5,2),F(99,100)),(F(-1),F(7,3),F(2))]:
 # Arb: characteristic discriminant. iv: trace and traceless part of the matrix.
 tr=m11+m22;det=m11*m22-m12*m12
 av=(ar(tr)+(ar(tr*tr)-4*ar(det)).sqrt())/2
 vv=ii(tr)/2+iv.sqrt(ii((m11-m22)/2)**2+ii(m12)**2)
 ea,ei=ae(av),ie(vv);assert max(ea[0],ei[0])<=min(ea[1],ei[1]);lo=min(ea[0],ei[0]);hi=max(ea[1],ei[1])
 for u,t in itertools.product(range(-4,5),repeat=2):
  if u==t==0:continue
  rayq=(m11*u*u+2*m12*u*t+m22*t*t)/F(u*u+t*t);assert rayq<=hi;rays+=1
 matrices.append({'entries':[str(m11),str(m12),str(m22)],'lambda_arb':pack(ea),'lambda_iv':pack(ei)})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','proof_sha256':sha(B/'research/transition_scale/PROOF.md'),'code_sha256':sha(__file__),'symbolic_identities':count,'coupling_limit_zero':True,'source_corners':corners,'source_minimum_exact':'290443/10000','collapse_examples':collapse,'matrix_checks':matrices,'rational_rayleigh_checks':rays,'runtime':{'python':sys.version,'sympy':s.__version__,'python_flint':flint.__version__,'mpmath':mpmath.__version__,'arb_bits':ctx.prec,'iv_dps':iv.dps},'seconds':time.monotonic()-t0,'scope':'Hamilton identities and conditional symbol-negativity obstructions. No global operator calculus, inverse or candidate enclosures.'}
(E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':'PASS','symbolic_identities':count,'source_minimum_exact':out['source_minimum_exact'],'rational_rayleigh_checks':rays,'seconds':out['seconds']}))

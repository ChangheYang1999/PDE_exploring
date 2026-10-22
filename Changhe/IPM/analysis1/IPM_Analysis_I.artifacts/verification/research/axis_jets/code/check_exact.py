"""Exact jet reconstruction, rational endpoint model and norm counterexamples."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
import sys,json,hashlib,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as s
import flint,mpmath
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/axis_jets/evidence';ctx.prec=512;ctx.threads=1;iv.dps=180
start=time.monotonic();checks={}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def zero(expr):assert s.cancel(s.expand(expr))==0
x,y,A,c,m,ap,delta,L=s.symbols('x y A c m ap delta L',nonzero=True)
w,mu,b,h3=[s.Function(k)(x) for k in ['w','mu','b','h3']]
w2,v3=s.Function('w2')(x),s.Function('v3')(x)
V1=w+w2*y**2;V2=mu*y+v3*y**3;h=b*y+h3*y**3
transport=s.expand(V1*s.diff(h,x)+V2*s.diff(h,y)-h)
zero(transport.coeff(y,1)-(w*s.diff(b,x)+(mu-1)*b));checks['trace_equation']=1
# A separate coefficient product, with arbitrary lower and higher jet data.
z=s.symbols('z');gg,ggp,uu,vv,cs=s.symbols('g gp u v cs');rho=y*(gg+ggp*z)+y**3*s.Symbol('g3')
Wh1=uu+cs*(L+z)/3+s.Symbol('u2')*y**2;Wh2=(vv+cs/3)*y+s.Symbol('v3')*y**3
row=s.diff(Wh1*s.diff(rho,z)+Wh2*s.diff(rho,y),y).subs({y:0,z:0})
zero(row-(ggp*uu+gg*vv+cs*(gg+L*ggp)/3));checks['coupled_P_row']=1
zero((-2*(2*c-1)+(4*c-1)-1)*x**2*y)
zero((-2*cs*x/3)*s.diff(x**2*y,x)+(4*cs*y/3)*s.diff(x**2*y,y));checks['center_cancellations']=2
checks['taylor_denominators']=0
for n in range(9):
 val=s.expand(ap*x*s.diff(x**n,x)+m*x**n)
 zero(val-(m+n*ap)*x**n);checks['taylor_denominators']+=1
zero((ap*delta+m).subs(delta,-m/ap));checks['homogeneous_exponent']=1
wr=A*x*(x*x-1)/(1+x*x);Hr=x*x/(1+x*x);mur=A-s.diff(wr,x)
zero(wr*s.diff(Hr,x)+mur*Hr);zero(s.diff(wr,x).subs(x,0)+A);zero(s.diff(wr,x).subs(x,1)-A)
zero(mur-2*A*(1-x*x)/(1+x*x)**2);checks['rational_model']=4
v=x**4*(1-x*x);integrand=s.cancel(v/(-wr*Hr));zero(integrand-x*(1+x*x)**2/A)
primitive=s.integrate(integrand,(x,0,x));br=s.cancel(-Hr*primitive)
zero(wr*s.diff(br,x)+mur*br-v);zero(s.limit(br/x**2,x,0));zero(s.limit(-br/x**2,x,1)-s.Rational(7,12)/A)
z=s.symbols('z',nonnegative=True);phi=(z/2+z*z/2+z**3/6)/(1+z)
zero(s.diff(phi,z)-(2*z**3+6*z*z+6*z+3)/(6*(1+z)**2));checks['kernel_constant']=5
# Logarithmic divergence from a positive exact comparison, no quadrature.
t=s.symbols('t',positive=True);lg=s.log(s.E/t)
zero(s.diff(s.log(lg),t)+1/(t*lg));zero(s.limit((-wr*Hr)/(1-x),x,1)-A/2);checks['non_Dini_counterexample']=2
# Scalar examples refuting a norm-independent lower bound.
examples=[]
for eps in [F(1,7),F(2,9),F(5)]:
 for mm in [F(-1,50000000),F(2),F(-3,7)]:
  inverse=eps/abs(mm);evalX=1/eps;correct=1/(abs(mm)*evalX);assert inverse==correct
  assert (inverse<1/abs(mm))==(eps<1)
  examples.append({'epsilon':str(eps),'m':str(mm),'inverse_norm':str(inverse),'evaluation_X_norm':str(evalX)})
checks['evaluation_scaling_examples']=len(examples)
# Exact l1 operator norms of scalar block matrices, independently inverted.
blocks=[]
for ar,aj,bb in [(2,3,-5),(-3,7,2),(7,-2,0),(1,1,4)]:
 M=s.Matrix([[ar,bb],[0,aj]]);inv=M.inv();cols=[sum(abs(inv[i,j]) for i in range(2)) for j in range(2)]
 norm=max(cols);bound=max(s.Rational(1,abs(ar)),(1+s.Rational(abs(bb),abs(ar)))/abs(aj));assert norm==bound
 blocks.append({'matrix':str(M),'inverse_norm':str(norm),'formula':str(bound)})
checks['block_norms']=len(blocks)
# Illustrative model constant using the same exact k as the modal normalization.
src=B/'data_exact/modal_v2.json';assert sha(src)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
d=json.loads(src.read_text());kh=d['scalars_hex']['k'];ka=F.from_float(float.fromhex(kh));sign=-1 if kh.startswith('-') else 1;mant,exp=kh.lstrip('+-').split('p');a0,a1=mant[2:].split('.')
kb=sign*F(int(a0+a1,16),16**len(a1))*F(2)**int(exp);assert ka==kb
Aval=2/ka-1;exact=F(7,12)/Aval
arbA=2/(arb(ka.numerator)/ka.denominator)-1
bv=((arb(2)**3-1)/6)/(2*arbA)
ivA=iv.mpf(Aval.numerator)/iv.mpf(Aval.denominator)
qv=(iv.mpf(1)/2+iv.mpf(2)/4+iv.mpf(1)/6)/(2*ivA)
def ae(z):
 assert z.is_finite()
 def cv(v):assert v.rad()==0;n,e=v.man_exp();return F(int(n))*F(2)**int(e)
 return cv(z.lower()),cv(z.upper())
def ie(z):
 ret=[]
 for sign,n,e,bc in z._mpi_:assert bc>=0;ret.append((-1 if sign else 1)*F(int(n))*F(2)**int(e))
 return tuple(ret)
rows=[]
for method,value in [('arb',bv),('iv',qv)]:
 lo,hi=ae(value) if method=='arb' else ie(value);assert lo<=exact<=hi
 rows.append({'method':method,'lower_exact':str(lo),'upper_exact':str(hi)})
checks['exact_constant_containments']=2
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/axis_jets/PROOF.md'),'input_sha256':sha(src),'checks':checks,'evaluation_examples':examples,'block_examples':blocks,'model_constant':{'k_exact':str(ka),'A_exact':str(Aval),'M_exact':str(exact),'enclosures':rows},'runtime':{'python':sys.version,'sympy':s.__version__,'python_flint':flint.__version__,'mpmath':mpmath.__version__,'arb_bits':ctx.prec,'iv_dps':iv.dps},'seconds':time.monotonic()-start,'scope':'Exact identity checks and an illustrative rational flow, not a numerical profile inverse. Dini and functional-analytic assertions are proved in PROOF.md.'}
(E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'seconds':out['seconds']}))

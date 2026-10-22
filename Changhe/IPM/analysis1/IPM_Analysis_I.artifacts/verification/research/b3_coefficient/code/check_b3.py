"""Exact cubic-axis algebra; independent positive quadrature for cutoff constants."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import sys,json,hashlib,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as s
import flint,mpmath
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/b3_coefficient/evidence';ctx.prec=512;ctx.threads=1;iv.dps=180;start=time.monotonic();checks={}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def zero(e):assert s.cancel(s.expand(e))==0
x=s.symbols('x',positive=True);y,c,A,p=s.symbols('y c A p');w,w2,v1,v3,G1,G3=[s.Function(k)(x) for k in ['w','w2','v1','v3','G1','G3']]
V1=w+w2*y**2;V2=v1*y+v3*y**3;rho=G1*y+G3*y**3
DIV=s.expand(s.diff(V1,x)+s.diff(V2,y));CURL=s.expand(s.diff(V2,x)-s.diff(V1,y)+s.diff(rho,x))
zero(DIV.coeff(y,0)-s.diff(w,x)-v1);zero(DIV.coeff(y,2)-s.diff(w2,x)-3*v3)
zero(CURL.coeff(y,1)-s.diff(v1,x)+2*w2-s.diff(G1,x));checks['axis_divergence_curl']=3
fluxx=s.expand(V1*rho);fluxy=s.expand(V2*rho)
zero(fluxx.coeff(y,1)-w*G1);zero(fluxx.coeff(y,3)-w*G3-w2*G1)
zero(fluxy.coeff(y,2)-v1*G1);zero(fluxy.coeff(y,4)-v1*G3-v3*G1);checks['Peano_flux_coefficients']=4
sub={s.diff(w,x):2*c-v1,s.diff(w2,x):-3*v3}
for j,G,expected in [(1,G1,w*s.diff(G1,x)+(v1-1)*G1),(3,G3,w*s.diff(G3,x)+(3*v1-1)*G3+w2*s.diff(G1,x)+v3*G1)]:
 eq=s.diff(fluxx.coeff(y,j),x)+(j+1)*fluxy.coeff(y,j+1)-(2*c+1)*G
 zero(eq.subs(sub)-expected)
checks['axis_equations']=2
zero((3*(4*c-1)-1)/(2*c-1)-(6+2/(2*c-1)));checks['p_identity']=1
# A literal counterexample to the printed sign, and the corrected identity.
pr=s.Rational(31,5);q=-pr/x+x;Hp=x**(-pr)*s.exp(x*x/2);Hm=x**(-pr)*s.exp(-x*x/2)
zero(s.diff(Hp,x)/Hp-q);zero(s.diff(Hm,x)/Hm-q+2*x);checks['integrating_factor_sign']=2
# Derive E from a general w=-Ax F, with p=6+2/A.
FF=s.Function('F')(x);ww=-A*x*FF;vv=A+1-s.diff(ww,x);qq=(3*vv-1)/ww
Eprime=3*s.diff(FF,x)/FF-(p-3)*(FF-1)/(x*FF)
zero((Eprime+qq+p/x).subs(p,6+2/A));checks['regular_E_formula']=1
# Rational reconstruction model, independent from the first-trace expression.
wm=A*x*(x*x-1)/(1+x*x);vm=A+1-s.diff(wm,x);gm=x*x/(1+x*x)
zero(wm*s.diff(gm,x)+(vm-1)*gm)
w2m=(s.diff(gm,x)-s.diff(wm,x,2))/2;v3m=-s.diff(w2m,x)/3;fm=s.cancel(-(w2m*s.diff(gm,x)+v3m*gm))
zero(2*w2m-s.diff(gm,x)+s.diff(wm,x,2));zero(s.diff(w2m,x)+3*v3m)
zero(s.limit(fm/x**2,x,0)-(10*A-s.Rational(5,3)))
Ep=(6-p)*s.log(1-x*x)-3*s.log(1+x*x)
zero((s.diff(Ep,x)+(3*vm-1)/wm+p/x).subs(p,6+2/A));checks['rational_reconstruction']=5
# Finite-part signs on Q=x2-2x4+3x6+5x8, with a nonzero exact remainder.
qj={2:s.Integer(1),4:s.Integer(-2),6:s.Integer(3),8:s.Integer(5)};Q=sum(v*x**j for j,v in qj.items())
BB=-sum(v/(j-pr) for j,v in qj.items());GG=x**pr*sum(v*(x**(j-pr)-1)/(j-pr) for j,v in qj.items())
zero(s.diff(GG,x)-pr*GG/x-Q/x)
zero(GG-sum(qj[j]*x**j/(j-pr) for j in [2,4,6])-BB*x**pr-5*x**8/(8-pr))
delta=s.symbols('delta',positive=True);Phi=-sum(qj[j]/(j-pr) for j in [2,4,6])-5*(1-delta**(8-pr))/(8-pr)
zero(BB-Phi+5*delta**(8-pr)/(8-pr));checks['finite_part_signs']=3
# Exact scaling and log moments used in the metric and counterexample.
eps=s.symbols('eps',positive=True);zero(eps**pr*eps**(-pr-1)*eps-1)
assert all(pr-j>0 for j in range(7));checks['small_support_scaling']=8
u,aa=s.symbols('u aa',positive=True)
zero(s.diff(-s.exp(-aa*u)/aa,u)-s.exp(-aa*u))
zero(s.diff(-s.exp(-aa*u)*(aa*u+1)/aa**2,u)-u*s.exp(-aa*u))
assert s.limit(s.exp(-aa*u)*(aa*u+1),u,s.oo)==0;checks['metric_integrals']=3
# Independent exact source parsing, no numeric fitting.
src=B/'data_exact/modal_v2.json';assert sha(src)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';data=json.loads(src.read_text());kh=data['scalars_hex']['k']
k1=F.from_float(float.fromhex(kh));man,ex=kh.split('p');whole,frac=man[2:].split('.');k2=F(int(whole+frac,16),16**len(frac))*F(2)**int(ex);assert k1==k2
Aval=2/k1-1;pv=6+2/Aval;assert 6<pv<7

def ar(q):q=F(q);return arb(q.numerator)/q.denominator
def ii(q):q=F(q);return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def ae(z):
 assert z.is_finite()
 def cv(t):assert t.rad()==0;n,e=t.man_exp();return F(int(n))*F(2)**int(e)
 return cv(z.lower()),cv(z.upper())
def ie(z):
 ret=[]
 for sign,n,e,bc in z._mpi_:assert bc>=0;ret.append((-1 if sign else 1)*F(int(n))*F(2)**int(e))
 return tuple(ret)
def pack(z,method):lo,hi=ae(z) if method=='arb' else ie(z);return {'lower_exact':str(lo),'upper_exact':str(hi)}
def ceil4(q):
 step=F(1)
 while q>=step*10000:step*=10
 while q<step*1000:step/=10
 return (q//step+1)*step
# Secondary method: x=delta*u^16, midpoint quadrature of u^beta.
# beta>2, 0<=f''<=beta(beta-1), so error is in [0,beta(beta-1)/(24N²)].
N=8192;beta=16*(8-pv)-1;assert beta>2
sm=iv.mpf(0)
for j in range(N):sm+=iv.exp(ii(beta)*iv.ln(ii(F(2*j+1,2*N))))/N
err=ii(beta*(beta-1)/F(24*N*N));quadrature=sm+iv.mpf([0,ie(err)[1].numerator])/ie(err)[1].denominator
# Above creates exactly [0,error_upper] using integer endpoint then division.
quad_exact=F(1)/(beta+1);assert ie(quadrature)[0]<=quad_exact<=ie(quadrature)[1]
rows=[]
for delt in [F(1,2),F(1)]:
 primary=ar(delt)**ar(8-pv)/ar(8-pv)
 secondary=16*iv.exp(ii(8-pv)*iv.ln(ii(delt)))*quadrature
 al,ah=ae(primary);il,ih=ie(secondary);assert il<=al<=ah<=ih
 pub=ceil4(max(ah,ih));assert max(ah,ih)<pub
 rows.append({'delta_exact':str(delt),'arb':pack(primary,'arb'),'iv':pack(secondary,'iv'),'public_strict_upper_exact':str(pub)})
# Independent finite-part illustrative constant from the subtracted polynomial and the quadrature.
coeff={2:F(1),4:F(-2),6:F(3)};Bexact=-sum(v/(j-pv) for j,v in {**coeff,8:F(5)}.items())
Ba=-sum(ar(v)/ar(j-pv) for j,v in {**coeff,8:F(5)}.items())
Bi=-sum(ii(v/(j-pv)) for j,v in coeff.items())-5*16*quadrature
assert ae(Ba)[0]<=Bexact<=ae(Ba)[1] and ie(Bi)[0]<=Bexact<=ie(Bi)[1]
checks['quadrature_antiderivative_comparison']=1;checks['cutoff_containments']=2;checks['finite_part_constant_containments']=2
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/b3_coefficient/PROOF.md'),'input_sha256':sha(src),'checks':checks,'parameters':{'k_exact':str(k1),'A_exact':str(Aval),'p_exact':str(pv)},'quadrature':{'cells':N,'substitution_power':16,'beta_exact':str(beta),'midpoint_sum':pack(sm,'iv'),'error_upper_exact':str(ie(err)[1]),'enclosure':pack(quadrature,'iv'),'exact_integral':str(quad_exact),'proof':'For beta>2 the second derivative is between0 and beta(beta-1). Convex midpoint sums are lower bounds; composite midpoint error <=beta(beta-1)/(24N²).'},'cutoff_constants':rows,'illustrative_finite_part':{'Q':'x²-2x4+3x6+5x8','L_exact':'1','exact_B3':str(Bexact),'arb':pack(Ba,'arb'),'iv':pack(Bi,'iv')},'runtime':{'python':sys.version,'sympy':s.__version__,'python_flint':flint.__version__,'mpmath':mpmath.__version__,'arb_bits':ctx.prec,'iv_dps':iv.dps},'seconds':time.monotonic()-start,'scope':'Conditional analytic B3 audit and cutoff illustrations only. The polynomial Q is an example, not the numerical profile. No exclusion or uniform class constants.'}
(E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'seconds':out['seconds'],'cutoff_upper':[x['public_strict_upper_exact'] for x in rows]}))
if __name__=='__main__':pass

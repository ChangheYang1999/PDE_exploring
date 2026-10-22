"""Exact fixed-extension algebra; Arb moments versus positive-series iv and midpoint quadrature."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
import sys,json,hashlib,time,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as s,flint,mpmath
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/jet_extension/evidence';t0=time.monotonic();ctx.prec=512;ctx.threads=1;iv.dps=180
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
u,z,x,k=s.symbols('u z x k',real=True);a=s.symbols('a',positive=True);chi=1-10*u**3+15*u**4-6*u**5;ns=0
def zero(v):
 global ns
 assert s.simplify(v)==0;ns+=1
zero(s.diff(chi,u)+30*u*u*(1-u)**2)
for j in range(3):assert s.diff(chi,u,j).subs(u,0)==(1 if j==0 else 0) and s.diff(chi,u,j).subs(u,1)==0
q=s.expand(2*s.diff(chi,u)+(1+u)*s.diff(chi,u,2));zero(q+60*u*(1-u)*(1-3*u*u))
Q=-30*u*u+20*u**3+45*u**4-36*u**5;zero(s.diff(Q,u)-q);root=1/s.sqrt(3);CS=s.simplify(Q.subs(u,1)-2*Q.subs(u,root));zero(CS-(9-16/(3*s.sqrt(3))))
M0=1+s.integrate(chi,(u,0,1));M1=s.Rational(1,2)+s.integrate((1+u)*chi,(u,0,1));assert M0==s.Rational(3,2) and M1==s.Rational(8,7)
bern=[-60,-20,200,-120];zero(s.diff(q,u)-sum(bern[j]*s.binomial(3,j)*u**j*(1-u)**(3-j) for j in range(4)));assert max(map(abs,bern))==200
p=z/(s.pi*(x*x+z*z));zero(-z*s.diff(p,x)-2*x*z*z/(s.pi*(x*x+z*z)**2));zero(s.diff(p,x,2)+s.diff(p,z,2))
# Multiplier divergence and strain signs.
I=s.symbols('I');Bsym=-s.I*k*I;Psym=k*k*I;zero(-s.I*k*Bsym+Psym)
# Two integration by parts endpoint rows: [zchi]=0 and [chi+zchi']=-1.
assert (chi+(1+u)*s.diff(chi,u)).subs(u,0)==1 and (chi+(1+u)*s.diff(chi,u)).subs(u,1)==0
# Exact Laplace identity for this polynomial cutoff, with independently formed polynomials.
inner=z;outer=s.expand(z*chi.subs(u,z-1));qz=s.expand(q.subs(u,z-1))
def smom(n,lo,hi):
 tail=lambda t:s.exp(-a*t)*sum((a*t)**j/s.factorial(j) for j in range(n+1))
 return s.factorial(n)/a**(n+1)*(tail(lo)-tail(hi))
Ic=smom(1,0,1)+sum(outer.coeff(z,n)*smom(n,1,2) for n in range(7));Jc=sum(qz.coeff(z,n)*smom(n,1,2) for n in range(5));zero(a*a*Ic-1-Jc)
# Finite-interval Volterra sign and fixed-point algebra in the linear illustration.
A,nu,Fc=s.symbols('A nu Fc',positive=True);xx=s.symbols('xx',positive=True);bb=(xx**2-xx**(2+nu))*Fc/(A*nu);zero(-A*xx*s.diff(bb,xx)+2*A*bb-Fc*xx**(2+nu));assert bb.subs(xx,1)==0
# Independent numeric methods.
def ar(q):q=F(q);return arb(q.numerator)/q.denominator
def ii(q):q=F(q);return iv.mpf(q.numerator)/iv.mpf(q.denominator)
def ae(v):
 assert v.is_finite();out=[]
 for t in [v.lower(),v.upper()]:
  assert t.rad()==0;n,e=t.man_exp();out.append(F(int(n))*F(2)**int(e))
 return out
def ie(v):return [(-1 if sg else 1)*F(int(n))*F(2)**int(e) for sg,n,e,bc in v._mpi_]
def pack(e):return {'lower_exact':str(e[0]),'upper_exact':str(e[1])}
N=8192;den=2*N;sumint=0;ivsum=iv.mpf(0)
for j in range(N):
 t=2*j+1
 # q numerator with denominator den^4, exact grid and exact absolute value.
 qnum=-60*t*den**3+60*t*t*den**2+180*t**3*den-180*t**4;sumint+=abs(qnum)
 v=ii(F(t,den));ivsum+=abs(-60*v*(1-v)*(1-3*v*v))/N
midsum=F(sumint,N*den**4);midends=ie(ivsum);assert midends[0]<=midsum<=midends[1]
err=F(200,4*N);Csiv=ivsum+iv.mpf([ii(-err).a,ii(err).b]);Csa=9-16/(3*arb(3).sqrt());csa,csi=ae(Csa),ie(Csiv);assert csi[0]<=csa[0]<=csa[1]<=csi[1]
constants={'C_B':(3/arb.pi(),2*ii(F(3,2))/iv.pi,F(955,1000)),'C_S':(Csa,Csiv,F(593,100)),'D_B':(8*arb(2).sqrt()/7,iv.sqrt(2*ii(F(8,7))**2),F(1617,1000))};exports={}
for key,(va,vi,pub) in constants.items():
 ea,ei=ae(va),ie(vi);assert max(ea[0],ei[0])<=min(ea[1],ei[1]);assert 0<min(ea[0],ei[0]) and max(ea[1],ei[1])<pub
 exports[key]={'arb':pack(ea),'iv':pack(ei),'public_strict_upper':str(pub)}
# Positive shifted exponential expansion for I(a). Exact moments have their own formula.
order=160;moments=[]
for n in range(order+1):
 left=sum((F(math.comb(n,j),(j+1)*(j+2)) for j in range(n+1)),F());right=F(20,n+4)-F(40,n+5)+F(27,n+6)-F(6,n+7);mn=left+right;assert left>0 and right>0;moments.append(mn)
assert moments[0]==F(8,7)
# Check the shifted moment formula for low n directly from both original pieces.
for n in range(9):
 exact=s.integrate(z*(2-z)**n,(z,0,1))+s.integrate((1+u)*chi*(1-u)**n,(u,0,1));assert F(str(exact))==moments[n]
def amom(n,lo,hi,av):
 def tail(t):
  at=av*t;return (-at).exp()*sum((at**j/math.factorial(j) for j in range(n+1)),arb(0))
 return math.factorial(n)/av**(n+1)*(tail(lo)-tail(hi))
co=[F(str(outer.coeff(z,n))) for n in range(7)];freq=[]
for aq in [F(1,2),F(1),F(4),F(16)]:
 av=ar(aq);Ia=amom(1,0,1,av)+sum((ar(c)*amom(n,1,2,av) for n,c in enumerate(co)),arb(0))
 sm=iv.mpf(0);power=F(1)
 for n,mn in enumerate(moments):
  if n:power*=aq/n
  sm+=ii(power*mn)
 lower=iv.exp(-2*ii(aq))*sm;rem=F(8,7)*(2*aq)**(order+1)/math.factorial(order+1);Ii=lower+iv.mpf([0,ii(rem).b]);ea,ei=ae(Ia),ie(Ii)
 assert max(ea[0],ei[0])<=min(ea[1],ei[1]) and 0<ei[0] and aq*aq*ei[1]<1
 freq.append({'a':str(aq),'I_arb_moments':pack(ea),'I_iv_positive_series':pack(ei),'series_order':order,'remainder_upper_exact':str(rem),'P_arb':pack(ae(av*av*Ia)),'S_arb':pack(ae(1-av*av*Ia))})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','proof_sha256':sha(B/'research/jet_extension/PROOF.md'),'code_sha256':sha(__file__),'symbolic_identities':ns,'cutoff':{'delta':'1','support_radius':'2','M0':'3/2','M1':'8/7','q_coefficients':[str(q.coeff(u,j)) for j in range(5)],'qprime_bernstein':bern,'outer_zchi_coefficients':[str(c) for c in co]},'quadrature':{'N':N,'midpoint_exact':str(midsum),'midpoint_iv':pack(midends),'lipschitz':'200','error_exact':str(err)},'constant_exports':exports,'frequency_checks':freq,'positive_moments_exact':[str(q) for q in moments],'runtime':{'python':sys.version,'sympy':s.__version__,'python_flint':flint.__version__,'mpmath':mpmath.__version__,'arb_bits':ctx.prec,'iv_dps':iv.dps},'seconds':time.monotonic()-t0,'scope':'Illustrative fixed C2 cutoff, canonical trace identities and conditional inverse algebra. No candidate-specific inverse constants.'}
(E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':'PASS','symbolic_identities':ns,'constant_upper':{k:v['public_strict_upper'] for k,v in exports.items()},'frequency_checks':len(freq),'seconds':out['seconds']}))

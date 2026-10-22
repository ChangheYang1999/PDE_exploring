"""Second modal scalar enclosure: exact derivative splines, de Boor, Gauss, mpmath.iv.

No stable-moment or Cox-polynomial code is imported. Gauss error is bounded
by derivative-spline convex hulls and the exact Gaussian remainder constant.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import json,math,hashlib,time,resource
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import mpmath as mp
from flint import arb,ctx,fmpq,fmpq_poly
BASE=Path(__file__).resolve().parents[3];mp.iv.dps=85;mp.mp.dps=95;ctx.prec=384;ctx.threads=1
resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=time.monotonic()
def utc():return datetime.now(timezone.utc).isoformat()
def emit(**kw):print(json.dumps({'utc':utc(),**kw}),flush=True)
def iv(v):
 if isinstance(v,F):return mp.iv.mpf(v.numerator)/v.denominator
 return mp.iv.mpf(v)
def dyadic(v):
 m,e=v.man_exp();return F(int(m))*F(2)**int(e)
def mpi_frac(t):
 sign,man,exponent,bc=t
 assert bc>=0
 return (-1 if sign else 1)*F(man)*F(2)**exponent

def row(v):
 lo,hi=(mpi_frac(t) for t in v._mpi_)
 return {'lower_exact_dyadic':str(lo),'upper_exact_dyadic':str(hi),'display':str(v),'width_upper':str(iv(hi-lo))}
def exact(v):return F.from_float(float.fromhex(v))
path=BASE/'data_exact/modal_v2.json';raw=path.read_bytes();sha=hashlib.sha256(raw).hexdigest();assert sha=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
d=json.loads(raw);ar=d['arrays'];sc={k:exact(v) for k,v in d['scalars_hex'].items()};k,L,bi,bo=(sc[v] for v in ('k','L','bi','bo'));assert L>0 and 0<k<F(1,2) and bi>4 and bo>4-2*k
M,nb=ar['S']['shape'];knots=[exact(v) for v in ar['knots']['hex']];assert len(knots)==nb+8
assert knots[:8]==[knots[0]]*8 and knots[-8:]==[knots[-1]]*8 and all(knots[i]<knots[i+1] for i in range(7,nb))
def get(name,m,j):return exact(ar[name]['hex'][m*ar[name]['shape'][1]+j])
assert all(ar[name]['shape']==[M,n] for name,n in [('S',nb),('D',7),('Ei',7),('Eo',7),('Aout',len(d['outer_jl']))])
alpha=[k-3-j*(1-k)-2*l for j,l in d['outer_jl']];assert alpha[0]==k-3 and all(v<-2 for v in alpha)
w=[F(1,4),F(1,8),-F(1,8),-F(1,8)]
S=[sum((w[m]*get('S',m,j) for m in range(4)),F(0)) for j in range(nb)]
def derivative(c,t,p):
 out=[]
 for i in range(len(c)-1):
  den=t[i+p+1]-t[i+1];assert den>0
  out.append(p*(c[i+1]-c[i])/den)
 return out,t[1:-1]
# Global derivative coefficients give rigorous per-cell convex-hull bounds.
cs=[S];ts=[knots]
for j in range(7):
 c,t=derivative(cs[-1],ts[-1],7-j);cs.append(c);ts.append(t)
# All exact endpoint jets, using the clamped derivative-coefficient formula.
def endpoint(c,t,right):
 vals=[]
 for p in range(7,0,-1):
  vals.append(c[-1] if right else c[0]);c,t=derivative(c,t,p)
 return vals
Ei=[];Eo=[]
for m in range(M):
 ji=endpoint([get('S',m,j) for j in range(8)],knots[:16],False)
 jo=endpoint([get('S',m,j) for j in range(nb-8,nb)],knots[-16:],True)
 def corr(jet,power,b):return [sum(((-b)**(i-j)*(jet[j]-power[j])/math.factorial(j)/math.factorial(i-j) for j in range(i+1)),F(0)) for i in range(7)]
 pi=[sum((get('D',m,j)*(2*j+2)**n for j in range(7)),F(int(m==0 and n==0))) for n in range(7)]
 po=[sum((get('Aout',m,j)*alpha[j]**n for j in range(len(alpha))),F(0)) for n in range(7)]
 Ei.append(corr(ji,pi,bi));Eo.append(corr(jo,po,-bo))
Di=[sum((w[m]*get('D',m,j) for m in range(4)),F(0)) for j in range(7)]
Ao=[sum((w[m]*get('Aout',m,j) for m in range(4)),F(0)) for j in range(len(alpha))]
eip=[sum((w[m]*Ei[m][j] for m in range(4)),F(0)) for j in range(7)]
eop=[sum((w[m]*Eo[m][j] for m in range(4)),F(0)) for j in range(7)]
inner=iv(F(1,8)+sum((Di[j]/(2*j+4)+eip[j]*(-1)**j*math.factorial(j)/(2+bi)**(j+1) for j in range(7)),F(0)))*mp.iv.exp(2*iv(knots[0]))
outer=iv(sum((Ao[j]/(-2-alpha[j]) for j in range(len(alpha))),F(0))+sum((eop[j]*math.factorial(j)/(bo-2)**(j+1) for j in range(7)),F(0)))*mp.iv.exp(2*iv(knots[-1]))
# Independent exact sign checks for every Gaussian root and derivative weight.
n=12;P0=fmpq_poly([1]);P1=fmpq_poly([0,1])
for j in range(1,n):P0,P1=P1,((2*j+1)*fmpq_poly([0,1])*P1-j*P0)/(j+1)
def q(v):return fmpq(v.numerator,v.denominator)
dP=P1.derivative();nodes=[];weights=[];previous=None
for j in range(n):
 x=arb.legendre_p_root(n,j);lo,hi=dyadic(x.lower()),dyadic(x.upper());assert -1<lo<hi<1 and P1(q(lo))*P1(q(hi))<0
 if previous is not None:assert hi<previous
 previous=lo
 # Pass exactly enclosing dyadic endpoints to a different interval engine.
 xx=mp.iv.mpf([iv(lo).a,iv(hi).b]);dp=iv(0)
 for a in reversed(list(dP.coeffs())):dp=dp*xx+iv(F(str(a)))
 ww=2/((1-xx**2)*dp**2)
 nodes.append(xx);weights.append(ww)
ki=[iv(v) for v in knots];si=[iv(v) for v in S]
def deboor(span,x):
 z=[si[i] for i in range(span-7,span+1)]
 for order in range(1,8):
  for j in range(7,order-1,-1):
   index=span-7+j;v=(x-ki[index])/(ki[index+8-order]-ki[index]);z[j]=(1-v)*z[j-1]+v*z[j]
 return z[7]
constant=F(math.factorial(n)**4,(2*n+1)*math.factorial(2*n)**3)
mid=iv(0);err=iv(0)
emit(stage='start',method='mpmath.iv Gauss12 plus exact derivative-spline remainder',cells=nb-7)
for count,span in enumerate(range(7,nb),1):
 a,b=knots[span],knots[span+1];h=b-a;center=(a+b)/2
 val=iv(0)
 for node,weight in zip(nodes,weights):
  t=iv(center)+iv(h/2)*node;val+=weight*mp.iv.exp(2*t)*deboor(span,t)
 mid+=iv(h/2)*val
 derivative_bound=sum((math.comb(2*n,j)*2**(2*n-j)*max(abs(v) for v in cs[j][span-7:span-j+1]) for j in range(8)),F(0))
 err+=iv(constant*h**(2*n+1)*derivative_bound)*mp.iv.exp(2*iv(b))
 if count%100==0:emit(stage='cells',done=count,total=nb-7,seconds=time.monotonic()-start)
error_hi=mpi_frac(err._mpi_[1]);mid+=mp.iv.mpf([-iv(error_hi).b,iv(error_hi).b])
c0=inner+mid+outer;target=3/iv(k)-1
slope=mp.iv.exp(2*iv(knots[-1]))*iv(F(1,4)/(-alpha[0]-2)*((alpha[0]+bo)/(bo-2))**7)
z=(target-c0)/slope
Rm,Rp=(mp.iv.exp(iv(knots[v])) for v in (0,-1));Wm=(1+(Rm/iv(L))**2)**iv((k-3)/2);Wp=(1+(Rp/iv(L))**2)**iv((k-3)/2)
Dij=[sum((abs(Ei[m][j]-get('Ei',m,j)) for m in range(M)),F(0)) for j in range(7)];Doj=[sum((abs(Eo[m][j]-get('Eo',m,j)) for m in range(M)),F(0)) for j in range(7)]
def ep(j,b):return iv(1) if j==0 else iv(F(j)/b)**j*mp.iv.exp(-j)
join=sum((iv(Dij[j])*ep(j,bi) for j in range(7)),iv(0))/Wm+sum((iv(Doj[j])*ep(j,bo-3+k) for j in range(7)),iv(0))/Wp
scalarcost=abs(z)/Wp
comparisons={};old=json.loads((BASE/'research/modal_repair/evidence/scalar_result.json').read_text())
vals={'c_before_scalar_repair':c0,'normalization_slope':slope,'A00_correction':z,'exact_joins_cost_in_factor_norm':join,'scalar_correction_cost_in_factor_norm':scalarcost,'total_exactification_cost_common_endpoints':join+scalarcost}
for name,v in vals.items():
 oldball=arb(old[name]['lower']).union(arb(old[name]['upper']));alo,ahi=dyadic(oldball.lower()),dyadic(oldball.upper());lo,hi=(mpi_frac(t) for t in v._mpi_);assert max(alo,lo)<=min(ahi,hi),name
 comparisons[name]='OVERLAP with independently reconstructed interval'
out={'utc':utc(),'input_sha256':sha,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'method':'Exact derivative B-spline coefficients, de Boor interval values, Gauss12 and full24th-derivative remainder in mpmath.iv; no Cox-polynomial or exponential-moment implementation reused','gaussian_roots_exact_sign_checks':n,'cells':nb-7,'digits':85,'quadrature_error':row(err),'inner_integral':row(inner),'middle_integral':row(mid),'outer_integral':row(outer),'values':{name:row(v) for name,v in vals.items()},'comparisons':comparisons,'seconds':time.monotonic()-start,'status':'PASS independent arithmetic and formula reproduction; not a PDE residual certificate'}
(BASE/'research/modal_repair/evidence/independent_gauss_iv.json').write_text(json.dumps(out,indent=2)+'\n');emit(stage='done',seconds=out['seconds'],c0=str(c0),z=str(z),cost=str(join+scalarcost))

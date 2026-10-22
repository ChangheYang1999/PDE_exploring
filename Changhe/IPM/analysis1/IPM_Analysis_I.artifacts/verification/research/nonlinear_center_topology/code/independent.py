"""Independent Fraction radial matching solve; no SymPy or primary polynomial reuse."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from datetime import datetime,timezone
import hashlib,json,sys
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'research/nonlinear_center_topology'
def check(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def rr(v):v=F(v);return str(v.numerator)+'/'+str(v.denominator)
def clean(p):return {i:v for i,v in p.items() if v}
def add(p,q):
 z=dict(p)
 for i,v in q.items():z[i]=z.get(i,F(0))+v
 return clean(z)
def scale(p,q):return clean({i:v*q for i,v in p.items()})
def dr(p):return clean({i-1:i*v for i,v in p.items() if i})
def val(p,r):return sum((v*r**i for i,v in p.items()),F(0))
def jet(p,j,r):
 for i in range(j):p=dr(p)
 return val(p,r)
def gauss(a,b):
 a=[list(map(F,row))+[F(c)] for row,c in zip(a,b)];n=len(b)
 for j in range(n):
  i=next(i for i in range(j,n) if a[i][j]);a[j],a[i]=a[i],a[j];c=a[j][j];a[j]=[v/c for v in a[j]]
  for i in range(n):
   if i!=j:
    c=a[i][j];a[i]=[v-c*w for v,w in zip(a[i],a[j])]
 return [a[i][-1] for i in range(n)]
def lap(p,n):return clean({i-2:(n*n-i*i)*v for i,v in p.items()})
def part(f,n):
 check(all((i+2)**2!=n*n for i in f),'no resonance in source');return {i+2:v/F(n*n-(i+2)**2) for i,v in f.items()}
rows=[];jetchecks=0;P_H={}
for n in (2,4):
 f=clean({2*j+2:F((-1)**j*comb(6,j))*(1+F(j,2) if n==2 else F(j,4)) for j in range(7)})
 f0={i:F(4,3)*v*(1-F(2)**(-i)) for i,v in f.items()};f1={i:-F(4,3)*v*F(2)**(-i) for i,v in f.items()};p0=part(f0,n);p1=part(f1,n)
 A=[[1,-1,-1,0],[n,-n,n,0],[0,F(2)**n,F(2)**(-n),-F(2)**(-n)],[0,n*F(2)**(n-1),-n*F(2)**(-n-1),n*F(2)**(-n-1)]]
 rhs=[val(p1,F(1))-val(p0,F(1)),jet(p1,1,F(1))-jet(p0,1,F(1)),-val(p1,F(2)),-jet(p1,1,F(2))]
 a,b,c,d=gauss(A,rhs);ps=[add(p0,{n:a}),add(p1,{n:b,-n:c}),{-n:d}]
 for p,q in zip(ps,[f0,f1,{}]):check(lap(p,n)==clean(q),'ODE coefficients')
 jets=[]
 for rad,lo,hi in ((1,0,1),(2,1,2)):
  row=[]
  for j in range(7):
   q=jet(ps[lo],j,F(rad));check(q==jet(ps[hi],j,F(rad)),'all boundary jets');row.append(rr(q));jetchecks+=1
  jets.append({'radius':rad,'jets':row})
 rows.append({'mode':n,'source_by_piece':[{str(i):rr(v) for i,v in clean(p).items()} for p in [f0,f1,{}]],'stream_by_piece':[{str(i):rr(v) for i,v in p.items()} for p in ps],'matching_jets':jets})
 p=part(f,n);h=-(n*val(p,F(1))+jet(p,1,F(1)))/(2*n);P_H[n]=add(p,{n:h})
check(rows[0]['stream_by_piece'][0].get('2','0/1')=='0/1','zero inner strain')
# Cartesian absolute sums reconstructed from binomial dictionaries.
def mul2(p,q):
 z={}
 for (a,b),v in p.items():
  for (c,d),u in q.items():z[a+c,b+d]=z.get((a+c,b+d),F(0))+v*u
 return clean(z)
def der2(p,j):
 z={}
 for m,v in p.items():
  if m[j]:i=list(m);i[j]-=1;z[tuple(i)]=m[j]*v
 return clean(z)
def powR(j):return {(2*i,2*(j-i)):F(comb(j,i)) for i in range(j+1)}
def sincart(n):return {(n-j,j):F((-1)**((j-1)//2)*comb(n,j)) for j in range(1,n+1,2)}
H={};psi={}
for j in range(7):H=add(H,scale(mul2({(2,1):F(1)},powR(j)),F((-1)**j*comb(6,j))))
for n,p in P_H.items():
 for degree,v in p.items():check(degree>=n and (degree-n)%2==0,'Cartesian source powers');psi=add(psi,scale(mul2(powR((degree-n)//2),sincart(n)),v))
U=[scale(der2(psi,1),F(-1)),der2(psi,0)];S1=sum((sum(map(abs,der2(H,j).values()),F(0)) for j in range(2)),F(0));S2=sum((sum(map(abs,der2(der2(H,j),k).values()),F(0)) for j in range(2) for k in range(2)),F(0));CH=sum((sum(map(abs,der2(u,j).values()),F(0)) for u in U for j in range(2)),F(0));CU=8*CH/3;B1=5*S1/3;B2=5*S2/3;AQ=CU*B1;BQ=CU*(B1+B2);C2=4*(AQ*AQ+BQ*BQ)
const={k:rr(v) for k,v in [('S1',S1),('S2',S2),('C_H',CH),('C_U',CU),('B1',B1),('B2',B2),('A_Q',AQ),('B_Q',BQ),('quadratic_norm_squared_over_pi_Cw',C2)]}
# Full radial density derivatives, independent of the trivial angular axis zeros.
a0={2*j+3:F((-1)**j*comb(6,j))*(F(4,3)-F(1,3)*F(4)**(-j)) for j in range(7)};a1={2*j+3:-F((-1)**j*comb(6,j),3)*F(4)**(-j) for j in range(7)};density_jets=0
for radius,p,q in ((1,a0,a1),(2,a1,{})):
 for j in range(6):check(jet(p,j,F(radius))==jet(q,j,F(radius)),'C5 density joins');density_jets+=1
check(a0[3]==1,'density central factor')
# Direct integrated sin3 moment: radial rho coefficient divided by r^2, factor 1/4.
def integral_moment(p,a,b):return sum((v*(b**(i-1)-a**(i-1))/F(i-1) for i,v in p.items()),F(0))/4
check(integral_moment(a0,F(0),F(1))+integral_moment(a1,F(1),F(2))==0,'independent strain moment')
# Independent scaling accounting by contributions, rather than copied exponents.
scale_b=3;scale_u=scale_b;scale_grad=scale_b-1;scale_q=scale_u+scale_grad;scale_qg=scale_q-1;radial_measure=2;weight=-6
exponents={'b':scale_b,'Ub':scale_u,'grad_b':scale_grad,'Q':scale_q,'grad_Q':scale_qg,'X_Q_squared':2*scale_q+weight+radial_measure,'X_b_squared':2*scale_b+weight+radial_measure,'rho_dilation_stream':1+1,'rho_dilation_source':1-1,'rho_dilation_velocity':1,'rho_dilation_strain':1-1}
ctx.prec=512;ctx.threads=1;iv.dps=180
v=(arb(C2.numerator)/C2.denominator).sqrt();w=(iv.mpf(C2.numerator)/C2.denominator)**iv.mpf('0.5')
def aq(x):
 check(x.rad()==0,'exact arb endpoint');m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def iq(t):
 sign,m,e,bc=t;return (-1 if sign else 1)*F(int(m))*F(2)**int(e)
av=[aq(v.lower()),aq(v.upper())];bv=[iq(w._mpi_[0]),iq(w._mpi_[1])];check(max(av[0],bv[0])<=min(av[1],bv[1]),'independent square root overlap')
ceiling=6800000000;check(all(0<a<=b<F(ceiling) for a,b in [av,bv]),'outward compact constant ceiling')
primary=json.loads((D/'evidence/compute.json').read_text());check(primary['radial_modes']==rows,'all piecewise modes');check(primary['unit_constants']==const,'all independently derived constants');check(primary['scaling_exponents']==exponents,'all scaling powers')
pins={}
for n,h in primary['files'].items():check(sha(ROOT/n)==h,'inherited pins');pins[n]=h
for p in [D/'evidence/compute.json',Path(__file__)]:pins[str(p.relative_to(ROOT))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_RADIAL_MATCHING_BINOMIAL_CONSTANTS_AND_SCALING','matching_jet_checks':jetchecks,'density_join_jets':density_jets,'radial_modes':rows,'unit_constants':const,'scaling_exponents':exponents,'normalized_quadratic_constant_arb_exact':[rr(q) for q in av],'normalized_quadratic_constant_iv_exact':[rr(q) for q in bv],'normalized_quadratic_constant_strict_upper':str(ceiling),'files':pins,'scope':'Specific compact family and conditional nonlinear topology theorem only. No stationary profile or exact solution set distance asserted.'}
p=D/'evidence/independent.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['utc','status','matching_jet_checks','density_join_jets','normalized_quadratic_constant_strict_upper']}))

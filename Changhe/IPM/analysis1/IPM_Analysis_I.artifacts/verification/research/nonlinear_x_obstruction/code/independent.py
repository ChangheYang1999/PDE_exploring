"""Independent rational ODE solution, Cartesian convolution and slice moments."""
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial
from datetime import datetime,timezone
import hashlib,json,sys
from flint import arb,ctx
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/nonlinear_x_obstruction'
def check(v,t):
 if not v:raise ValueError(t)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def rr(v):v=F(v);return str(v.numerator)+'/'+str(v.denominator)
def clean(p):return {m:c for m,c in p.items() if c}
def add(p,q):
 out=dict(p)
 for m,c in q.items():out[m]=out.get(m,F(0))+c
 return clean(out)
def sc(p,a):return clean({m:a*c for m,c in p.items()})
def mul(p,q):
 out={}
 for (i,j),c in p.items():
  for (k,l),d in q.items():out[i+k,j+l]=out.get((i+k,j+l),F(0))+c*d
 return clean(out)
def der(p,axis):
 out={}
 for m,c in p.items():
  if m[axis]:n=list(m);n[axis]-=1;out[tuple(n)]=m[axis]*c
 return clean(out)
def Rpow(j):return {(2*i,2*(j-i)):F(comb(j,i)) for i in range(j+1)}
def sinpoly(n):return {(n-i,i):F((-1)**((i-1)//2)*comb(n,i)) for i in range(1,n+1,2)}
H={};psi={};rows=[]
for j in range(7):H=add(H,sc(mul({(2,1):F(1)},Rpow(j)),F((-1)**j*comb(6,j))))
for n in [2,4]:
 source=clean({2*j+2:F((-1)**j*comb(6,j))*(1+F(j,2) if n==2 else F(j,4)) for j in range(7)})
 part={i+2:c/F(n*n-(i+2)**2) for i,c in source.items()};v=sum(part.values(),F(0));dv=sum((i*c for i,c in part.items()),F(0));a=-(n*v+dv)/(2*n);inside=add(part,{n:a});outside=v+a
 check(sum(inside.values(),F(0))==outside and sum((i*c for i,c in inside.items()),F(0))==-n*outside,'two boundary matching equations')
 check(clean({i-2:(n*n-i*i)*c for i,c in inside.items()})==source,'radial ODE')
 for degree,c in inside.items():psi=add(psi,sc(mul(Rpow((degree-n)//2),sinpoly(n)),c))
 rows.append({'mode':n,'inner':{str(i):rr(c) for i,c in inside.items()},'exterior':rr(outside)})
U1=sc(der(psi,1),F(-1));U2=der(psi,0);Q=add(mul(U1,der(H,0)),mul(U2,der(H,1)));Qx=der(Q,0);Qy=der(Q,1);E=add(mul(Qx,Qx),mul(Qy,Qy));check(Q.get((2,1))==F(-1,56) and all(sum(m)>=3 for m in Q),'independent cubic')
# Horizontal slice integration using half-integer Gamma recurrences, not polar factorial formula.
def hg(q):
 v=F(1)
 for j in range(q):v*=F(2*j+1,2)
 return v
moment=F(0);count=0
for (i,j),c in E.items():
 if i%2 or j%2:continue
 a,b=i//2,j//2;beta_over_pi=hg(a)*hg(b+1)/factorial(a+b+1);unit=F(2,2*b+1)*F(1,2)**(2*(a+b)+2)*beta_over_pi;moment+=c*unit;count+=1
check(moment>0,'positive exact slice integral')
# Derivatives of numerator/R^m by the exact quotient-rule polynomial recurrence.
Rp={(2,0):F(1),(0,2):F(1)}
def rational_derivative(p,m,axis):
 coord={(1,0) if axis==0 else (0,1):F(1)}
 return add(mul(der(p,axis),Rp),sc(mul(p,coord),-2*m)),m+1
p2={(1,1):F(-1,2016)};p4={(3,1):F(-1,3360),(1,3):F(1,3360)};diagonal=[]
for p,m in [(p2,2),(p4,4)]:
 for ax in [0,1]:p,m=rational_derivative(p,m,ax)
 diagonal.append((p,m))
check(sum(diagonal[0][0].values(),F(0))/F(2)**diagonal[0][1]==F(-1,2688),'diagonal mode2 coefficient');check(sum(diagonal[1][0].values(),F(0))==0,'mode4 diagonal cancellation')
strain_cases=[]
for n in [2,3,7,100]:
 epsilon=F(1,n*n);amplitude=F(1,n);total=F(0)
 for sx in [-1,1]:
  for sy in [-1,1]:
   x=-4*sx/epsilon;y=-4*sy/epsilon;v=F(0)
   for p,m in diagonal:v+=sum((c*x**i*y**j for (i,j),c in p.items()),F(0))/(x*x+y*y)**m
   total+=amplitude/epsilon*v
 check(total==-amplitude*epsilon**3/172032,'exact translated signed strain')
 check(total+amplitude*epsilon**3/172032==0,'exact compensator')
 strain_cases.append({'n':n,'epsilon':rr(epsilon),'amplitude':rr(amplitude),'packet_strain':rr(total),'corrected_strain':'0/1'})
# Interval representation of the positive unit disk energy, separately from its exact rational proof.
ctx.prec=512;ctx.threads=1;iv.dps=180
av=arb.pi()*(arb(moment.numerator)/moment.denominator);bv=iv.pi*(iv.mpf(moment.numerator)/moment.denominator)
def aq(x):
 check(x.rad()==0,'exact Arb endpoint');m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def iq(x):sign,m,e,bc=x;return (-1 if sign else 1)*F(int(m))*F(2)**int(e)
aint=[aq(av.lower()),aq(av.upper())];bint=[iq(bv._mpi_[0]),iq(bv._mpi_[1])];check(0<min(aint+bint) and max(aint[0],bint[0])<=min(aint[1],bint[1]),'positive overlapping unit energy intervals')
primary=json.loads((D/'evidence/compute.json').read_text());check(primary['radial_modes']==rows,'independent radial modes');check(F(primary['gradient_energy_over_pi'])==moment,'independent slice versus disk energy');check(primary['gradient_energy_polynomial_terms_integrated']==count,'energy terms')
def coeffs(p):return [{'powers':list(m),'coefficient':rr(c)} for m,c in sorted(p.items(),reverse=True)]
coefficient_checks=0
for name,p in [('H',H),('psi',psi),('U1',U1),('U2',U2),('Q_H',Q),('Q_x',Qx),('Q_y',Qy)]:check(primary['cartesian'][name]==coeffs(p),'all Cartesian coefficients '+name);coefficient_checks+=len(p)
pins={}
for name,h in primary['files'].items():check(sha(B/name)==h,'primary pin');pins[name]=h
for pth in [D/'evidence/compute.json',Path(__file__)]:pins[str(pth.relative_to(B))]=sha(pth)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_ODE_CONVOLUTION_SLICE_ENERGY_AND_SIGNED_STRAIN','cartesian_coefficients_compared':coefficient_checks,'energy_terms':count,'gradient_energy_over_pi':rr(moment),'gradient_energy_arb_exact':[rr(q) for q in aint],'gradient_energy_iv_exact':[rr(q) for q in bint],'display_only_energy':float(moment)*3.141592653589793,'strain_cases':strain_cases,'files':pins,'scope':'Finite arithmetic and explicit concentration sequence only. No claim about graph norms, stronger SPEC spaces, small linear residuals or PDE endpoints.'}
op=D/'evidence/independent.json';check(not op.exists(),'immutable');op.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['utc','status','cartesian_coefficients_compared','energy_terms','gradient_energy_over_pi','display_only_energy']}))

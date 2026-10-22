"""Arb512 and exact Cartesian-polynomial checks of the standalone theorem."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from datetime import datetime,timezone
import json,hashlib,sys
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_strain'
def check(x,s):
 if not x:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as h:return hashlib.file_digest(h,'sha256').hexdigest()
def A(x):x=F(x);return arb(x.numerator)/x.denominator
def qarf(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def box(x):check(x.is_finite(),'finite ball');return qarf(x.lower()),qarf(x.upper())
def add(a,b):
 c=a.copy()
 for n,x in b.items():c[n]=c.get(n,F(0))+x
 return {n:x for n,x in c.items() if x}
def mul(a,b):
 c={}
 for n,x in a.items():
  for m,y in b.items():t=tuple(i+j for i,j in zip(n,m));c[t]=c.get(t,F(0))+x*y
 return {n:x for n,x in c.items() if x}
def scale(v,a):return {n:v*x for n,x in a.items() if v*x}
def deriv(a,j):
 c={}
 for n,x in a.items():
  if n[j]:m=list(n);m[j]-=1;c[tuple(m)]=x*n[j]
 return c
R={(2,0):F(1),(0,2):F(1)};xy={(1,1):F(1)};kernel=add(scale(-1,mul(deriv(xy,0),R)),scale(2,mul(xy,deriv(R,0))))
check(kernel=={(2,1):F(3),(0,3):F(-1)},'canonical kernel numerator')
# sin even moments /pi, via integration-by-parts recurrence.
def smoment(j):
 a=F(2)
 for n in range(1,j+1):a*=F(2*n-1,2*n)
 return a
sin3sq=9*smoment(1)-24*smoment(2)+16*smoment(3)
p_sin3=3*smoment(1)-7*smoment(2)+4*smoment(3)
p2=smoment(1)-2*smoment(2)+smoment(3)
check((sin3sq,p_sin3,p2)==(F(1),F(1,4),F(1,8)),'Cartesian angular integrals')
chi=[F((-1)**j*comb(6,j)) for j in range(7)];chi2=[sum((chi[j]*chi[n-j] for j in range(7) if 0<=n-j<7),F(0)) for n in range(13)]
d=[(j+1)*chi[j+1] for j in range(6)];d2=[sum((d[j]*d[n-j] for j in range(6) if 0<=n-j<6),F(0)) for n in range(11)]
rad=[sum((x/F(2*j+2) for j,x in enumerate(chi2)),F(0)),sum((j*x/F(2*j+2) for j,x in enumerate(chi2)),F(0)),sum((4*x/F(2*j+6) for j,x in enumerate(d2)),F(0))]
check(rad==[F(1,26),-F(1,26),F(12,143)],'expanded bump radial integrals');total=15*rad[0]+6*rad[1]+rad[2];check(total==F(123,286) and 3*total/8*4<1,'bump energy bound using pi<4')
bump_sigma=p_sin3*sum((x/F(2*j+2) for j,x in enumerate(chi)),F(0));g_sigma=bump_sigma*(1-F(1,4));cancel=bump_sigma/g_sigma
check((bump_sigma,g_sigma,cancel)==(F(1,56),F(3,224),F(4,3)),'exact fixed strain compensation')
# Formal Green formula differentiation, with A'=r^3 f,B'=-r^-1 f.
def gd(poly):
 out={}
 for (p,t),c in poly.items():
  if p:out[(p-1,t)]=out.get((p-1,t),F(0))+p*c
  if t=='A':key=(p+3,'f');v=c
  elif t=='B':key=(p-1,'f');v=-c
  elif t=='f':key=(p,'fp');v=c
  else:raise ValueError('unsupported derivative symbol')
  out[key]=out.get(key,F(0))+v
 return {k:v for k,v in out.items() if v}
def shift(p,n):return {(r+n,t):v for (r,t),v in p.items()}
psi={(-2,'A'):F(1,4),(2,'B'):F(1,4)};dp=gd(psi);dd=gd(dp);ode=scale(-1,add(add(dd,shift(dp,-1)),scale(-4,shift(psi,-2))));check(ode=={(0,'f'):F(1)},'Green ODE exact cancellation')
k=F(1615536043799051,9007199254740992);L=F(8614738245908811,1125899906842624);check(0<k<F(1,2) and L>0,'dual domain')
source=B/'research/global_residual_assembly/evidence/primary_assembly_v2.json';src=json.loads(source.read_text());check(F(src['k_exact'])==k and F(src['L_exact'])==L,'explicit parameter agreement only')
radial_dual=1/(L**4*(1-2*k));check(radial_dual==1/(2*L**4*(F(1,2)-k)),'power primitive exact factor')
ctx.prec=512;ctx.threads=1
C0=1/(A(L)**2*(arb.pi()*A(1-2*k)).sqrt());Ca=1/(A(L)**2*(10*arb.pi()*A(1-2*k)).sqrt());vals={n:box(v) for n,v in [('C0',C0),('Cang',Ca),('speed_variation',Ca/3),('speed_cost_lower_factor',3/Ca)]}
public={}
for n,(lo,hi) in vals.items():
 check(0<lo<=hi,'positive bounds');scale10=10**12;floorlo=(lo.numerator*scale10)//lo.denominator;ceilhi=-((-hi.numerator*scale10)//hi.denominator)
 public[n]={'strict_lower_exact':str(F(floorlo,scale10)),'strict_upper_exact':str(F(ceilhi,scale10)),'lower_decimal':f'{floorlo//scale10}.{floorlo%scale10:012d}','upper_decimal':f'{ceilhi//scale10}.{ceilhi%scale10:012d}'};check(F(floorlo,scale10)<lo<=hi<F(ceilhi,scale10),'strict display enclosure')
inputs=[D/'PROOF.md',D/'evidence/proof_first.json',Path(__file__),source]
check(json.loads((D/'evidence/proof_first.json').read_text())['proof_sha256']==sha(D/'PROOF.md'),'proof before computation')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ARBITRARY_PRECISION_BALLS_CARTESIAN_POLYNOMIALS_AND_GREEN_IDENTITY','k_exact':str(k),'L_exact':str(L),'kernel_numerator':{str(n):str(v) for n,v in kernel.items()},'angular_over_pi':{'sin3_squared':str(sin3sq),'p_times_sin3':str(p_sin3),'p_squared':str(p2)},'radial_bump_integrals':list(map(str,rad)),'bump_energy_radial':str(total),'bump_sigma_over_epsilon_squared':str(bump_sigma),'g_sigma_over_L_squared':str(g_sigma),'compensation_over_epsilon_squared_L_inverse_squared':str(cancel),'radial_dual_exact':str(radial_dual),'formal_Green_ODE':{str(n):str(v) for n,v in ode.items()},'arb512':{n:list(map(str,v)) for n,v in vals.items()},'public':public,'files':{str(p.relative_to(B)):sha(p) for p in inputs},'scope':'Analytic theorem arithmetic and explicit parameter constants, no X3 uncertainty membership or PDE estimate.'}
p=D/'evidence/compute.json';check(not p.exists(),'immutable output');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'public':public,'sha256':sha(p)}))

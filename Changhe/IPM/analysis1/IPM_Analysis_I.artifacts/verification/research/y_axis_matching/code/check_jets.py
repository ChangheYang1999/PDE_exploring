"""Exact jet algebra, conditional scalar models, and independent trace integrals."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[name]='1'
import sys,json,math,hashlib,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as sp
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/y_axis_matching/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(z):z=F(z);return arb(fmpq(z.numerator,z.denominator))
def ii(z):z=F(z);return iv.mpf(z.numerator)/z.denominator
def dyad(m,e):return F(int(m))*F(2)**int(e)
def ends(z):
 if isinstance(z,arb):return tuple(dyad(*v.man_exp()) for v in (z.lower(),z.upper()))
 return tuple((-1 if sign else 1)*dyad(man,ex) for sign,man,ex,bc in z._mpi_)
def rec(z):
 l,u=ends(z);assert l<=u;return {'lower_exact':str(l),'upper_exact':str(u),'display':[float(l),float(u)]}
def beta(a,b):return F(math.factorial(a-1)*math.factorial(b-1),math.factorial(a+b-1))
def trace_arb(kap):
 kap=aa(kap);e=(-kap).exp();return kap*sum(((-1)**j*math.comb(8,j)*math.factorial(2+2*j)/kap**(3+2*j)*(1-e*sum((kap**q/math.factorial(q) for q in range(3+2*j)),arb(0))) for j in range(9)),arb(0))
def trace_iv(kap,N=180):
 kk=F(kap);assert kk<N+2
 def term(q):return kk**q/F(math.factorial(q))*sum((math.comb(8,m)*beta(3+m,9+q) for m in range(9)),F(0))
 lo=sum((term(q) for q in range(N+1)),F(0));tail=term(N+1)/(1-kk/F(N+2));s=iv.mpf([ii(lo).a,ii(lo+tail).b]);return ii(kk)*iv.exp(-ii(kk))*s

def main():
 start=time.monotonic();ctx.prec=512;ctx.threads=1;iv.dps=180
 x,y=sp.symbols('x y',real=True);kap=sp.symbols('kappa',positive=True);ell=sp.symbols('ell');a2,a4,BB,r2,r4,u,w,v,z=[sp.Function(s)(y) for s in ['a2','a4','B','r2','r4','u','w','v','z']]
 us={0:BB,1:-sp.diff(BB,y),2:-a2-sp.diff(BB,y,2)/2,3:sp.diff(a2,y)/3+sp.diff(BB,y,3)/6,4:-a4+sp.diff(a2,y,2)/12+sp.diff(BB,y,4)/24};us[5]=-sp.diff(us[4],y)/5
 hp=x*x*a2+x**4*a4;Up1=x*us[1]+x**3*us[3]+x**5*us[5];Up2=us[0]+x*x*us[2]+x**4*us[4]
 ids={}
 def ident(name,expr):
  q=sp.simplify(expr);assert q==0,(name,q);ids[name]=str(q)
 for j in [0,2]:ident('laplace_velocity_'+str(j),sp.expand(sp.diff(Up2,x,2)+sp.diff(Up2,y,2)+sp.diff(hp,x,2)).coeff(x,j))
 for j in [0,2,4]:ident('divergence_'+str(j),sp.expand(sp.diff(Up1,x)+sp.diff(Up2,y)).coeff(x,j))
 rho=x*x*r2+x**4*r4;V1=x*u+x**3*w;V2=v+x*x*z
 expression=V1*sp.diff(hp,x)+V2*sp.diff(hp,y)-hp+Up1*sp.diff(rho,x)+Up2*sp.diff(rho,y)+ell/3*(x*sp.diff(rho,x)+y*sp.diff(rho,y))
 row2=v*sp.diff(a2,y)+(2*u-1)*a2+2*r2*us[1]+sp.diff(r2,y)*BB+ell/3*(2*r2+y*sp.diff(r2,y))
 row4=v*sp.diff(a4,y)+(4*u-1)*a4+2*w*a2+z*sp.diff(a2,y)+4*r4*us[1]+2*r2*us[3]+sp.diff(r4,y)*BB+sp.diff(r2,y)*us[2]+ell/3*(4*r4+y*sp.diff(r4,y))
 ident('full_row2',sp.expand(expression).coeff(x,2)-row2);ident('full_row4',sp.expand(expression).coeff(x,4)-row4)
 cl,er,b,J=sp.symbols('cl er b J');center=(cl-er)*x*sp.diff(b*x*x*y,x)+(cl+er)*y*sp.diff(b*x*x*y,y)-b*x*x*y-ell*x*sp.diff(J*x*x*y,x)+ell*y*sp.diff(J*x*x*y,y)+ell/3*3*J*x*x*y
 ident('cubic_unconstrained',center/(x*x*y)-(b*(3*cl-er-1)+J*(-ell+ell)))
 ident('cubic_constraint',center.subs(cl,(1+er)/3));ident('row1_coupling_at_center',-2*ell+ell+ell)
 gp=sp.exp(-kap*x)/(2*kap);gm=sp.exp(kap*x)/(2*kap)
 ident('Green_right',-sp.diff(gp,x,2)+kap*kap*gp);ident('Green_left',-sp.diff(gm,x,2)+kap*kap*gm)
 ident('Green_derivative_jump',sp.diff(gp,x).subs(x,0)-sp.diff(gm,x).subs(x,0)+1)
 pp,H,S,FF=sp.symbols('p H S F');HH=sp.Function('H')(y);SS=sp.Function('S')(y);uu=sp.Function('u')(y);vv=sp.Function('v')(y);j=sp.symbols('j')
 ident('matching_derivative',(vv*sp.diff(SS,y)+(2*j*uu-1)*SS)/(vv*HH)-sp.diff(SS/HH,y).subs(sp.diff(HH,y),(1-2*j*uu)*HH/vv))
 A=2*cl-1;D=4*cl-1;k=1/cl;vvmod=y*(D+cl*y*y)/(1+y*y);uumod=(-A+cl*y*y)/(1+y*y)
 manufactured=y/(1+y*y)**3
 for jv in [1,2]:
  pj=(2*jv*A+1)/D;qj=k-2*jv;logder=pj/y+(qj-pj)*cl*y/(D+cl*y*y)
  ident('model_homogeneous_'+str(jv),vvmod*logder+2*jv*uumod-1)
  force=vvmod*sp.diff(manufactured,y)+(2*jv*uumod-1)*manufactured
  ident('manufactured_linear_coefficient_'+str(jv),sp.limit(force/y,y,0)-D*(1-pj))
  ident('far_jet_exponent_'+str(jv),4*jv+1-2*sp.Symbol('gamma')+2*qj-(2*k+1-2*sp.Symbol('gamma')))
 sigma=sp.symbols('sigma');ident('Fourier_energy_rate',D*(2*sigma+1)/2-D*(1+pp)-D*(sigma-sp.Rational(1,2)-pp))
 ident('p1',(2*A+1)/D-1);ident('p2',(4*A+1)/D-(2-1/D))
 # Exact positive-series beta ratio for the independent trace lane.
 q,m=sp.symbols('q m',integer=True,nonnegative=True);ident('beta_ratio',(q+9)/(q+m+12)-sp.cancel(sp.gamma(3+m)*sp.gamma(10+q)/sp.gamma(13+m+q)/(sp.gamma(3+m)*sp.gamma(9+q)/sp.gamma(12+m+q))))
 raw=B/'data_exact/modal_v2.json';assert sha(raw)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 kr=F.from_float(float.fromhex(json.loads(raw.read_text())['scalars_hex']['k']));assert kr==F(1615536043799051,9007199254740992)
 cr=1/kr;Ar=2*cr-1;Dr=4*cr-1;gam=F(1129,1000);s=F(153,50);pr2=(4*Ar+1)/Dr
 exact={'k':kr,'c_l':cr,'A':Ar,'D':Dr,'p1':F(1),'p2':pr2,'p2_Sobolev_threshold':pr2+F(1,2),'s':s,'gamma':gam,'far_Hardy_margin':1+kr-gam,'jet1_rate':Dr*(s-F(3,2)),'jet2_rate':Dr*(s-F(1,2)-pr2),'local_matching_power':3-pr2}
 assert F(5,3)<pr2<2 and gam<1+kr and s>pr2+F(1,2) and exact['jet2_rate']>0
 values={};trace={};bare={}
 for method,conv in [('arb',aa),('iv',ii)]:
  values[method]={name:rec(conv(val)) for name,val in exact.items()};trace[method]={};bare[method]={}
  for kk in [1,4,16]:
   tr=trace_arb(kk) if method=='arb' else trace_iv(kk);l,up=ends(tr);assert l>0 and up<F(2,kk*kk);trace[method][str(kk)]=rec(tr)
  for dd in [F(1,10),F(1,100),F(1,1000)]:
   d=conv(dd);factor=-(1+d*d)**(-3)*(1+conv(cr/Dr)*d*d)**conv((pr2-kr+4)/2);integ=factor*d**conv(1-pr2)
   assert ends(factor)[1]<0 and ends(integ)[1]<0
   bare[method][str(dd)]={'scaled':rec(factor),'integral':rec(integ)}
 def overlap(a,b):assert max(F(a['lower_exact']),F(b['lower_exact']))<=min(F(a['upper_exact']),F(b['upper_exact']))
 for n in values['arb']:overlap(values['arb'][n],values['iv'][n])
 for n in trace['arb']:overlap(trace['arb'][n],trace['iv'][n])
 for d in bare['arb']:
  for n in bare['arb'][d]:overlap(bare['arb'][d][n],bare['iv'][d][n])
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','code_sha256':sha(__file__),'proof_sha256':sha(B/'research/y_axis_matching/PROOF.md'),'data_sha256':sha(raw),'exact_identities':ids,'exact_parameters':{n:str(v) for n,v in exact.items()},'values':values,'trace_integrals':trace,'bare_matching_example':bare,'method':'Exact symbolic coefficient extraction and rational model; Arb512 finite antiderivative trace moments versus iv180 positive Beta/exponential series with geometric remainder.','seconds':time.monotonic()-start,'scope':'Exact jets and conditional diagonal matching only; no coupled index or inverse.'}
 (E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');summary={k:v for k,v in out.items() if k not in ['values','trace_integrals','bare_matching_example']};summary['checks_sha256']=sha(E/'checks.json');summary['values_display']={method:{n:v['display'] for n,v in row.items()} for method,row in values.items()};summary['trace_display']={method:{n:v['display'] for n,v in row.items()} for method,row in trace.items()};summary['bare_display']={method:{d:{n:v['display'] for n,v in row.items()} for d,row in tab.items()} for method,tab in bare.items()};(E/'review_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'seconds':out['seconds'],'identities':len(ids),'p2':values['arb']['p2']['display'],'trace':summary['trace_display']['arb']}),flush=True)
if __name__=='__main__':main()

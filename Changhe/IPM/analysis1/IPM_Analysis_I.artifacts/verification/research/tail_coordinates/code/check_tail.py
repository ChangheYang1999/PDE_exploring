"""Exact tail/block identities and independently enclosed trace and strain data."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import sys,json,hashlib,time,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as sp
from flint import arb,ctx,fmpq,arb_mat
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/tail_coordinates/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(z):z=F(z);return arb(fmpq(z.numerator,z.denominator))
def ii(z):z=F(z);return iv.mpf(z.numerator)/z.denominator
def dyad(m,e):return F(int(m))*F(2)**int(e)
def ends(z):
 if isinstance(z,arb):return tuple(dyad(*v.man_exp()) for v in (z.lower(),z.upper()))
 return tuple((-1 if s else 1)*dyad(m,e) for s,m,e,b in z._mpi_)
def rec(z):l,u=ends(z);assert l<=u;return {'lower_exact':str(l),'upper_exact':str(u),'display':[float(l),float(u)]}
def beta(a,b):return F(math.factorial(a-1)*math.factorial(b-1),math.factorial(a+b-1))
def machin(N=190):
 assert N%2==0
 def arctan(q):
  lo=sum(((-1)**j*F(1,(2*j+1)*q**(2*j+1)) for j in range(N)),F());return lo,lo+F(1,(2*N+1)*q**(2*N+1))
 l,u=arctan(5);a,b=arctan(239);return iv.mpf([ii(16*l-4*b).a,ii(16*u-4*a).b])
def interval_positive(lo,tail):return iv.mpf([ii(lo).a,ii(lo+tail).b])
def inv_fraction(mat):
 n=len(mat);a=[[F(v) for v in row]+[F(i==j) for j in range(n)] for i,row in enumerate(mat)]
 for c in range(n):
  p=next(i for i in range(c,n) if a[i][c]);a[c],a[p]=a[p],a[c];pivot=a[c][c];a[c]=[v/pivot for v in a[c]]
  for i in range(n):
   if i!=c:
    v=a[i][c];a[i]=[x-v*y for x,y in zip(a[i],a[c])]
 return [r[n:] for r in a]
def inv_iv(mat):
 n=len(mat);a=[[ii(v) for v in row]+[ii(i==j) for j in range(n)] for i,row in enumerate(mat)]
 for c in range(n):
  assert not(ends(a[c][c])[0]<=0<=ends(a[c][c])[1]);p=a[c][c];a[c]=[v/p for v in a[c]]
  for i in range(n):
   if i!=c:
    v=a[i][c];a[i]=[x-v*y for x,y in zip(a[i],a[c])]
 return [r[n:] for r in a]
def trace_arb(nu,N,coeff):
 q=aa(nu)
 def J(n,lo,hi):
  def top(z):
   zz=aa(z);return (-q*zz).exp()*sum(((q*zz)**m/math.factorial(m) for m in range(n+1)),arb(0))
  return aa(math.factorial(n))*q**(-n-1)*(top(lo)-top(hi))
 return q*(J(N,0,F(1,2))+sum((aa(v)*J(N+n,F(1,2),1) for n,v in enumerate(coeff)),arb(0)))
def trace_iv(nu,N,Q=160):
 lam=F(nu,2);assert lam<Q+2
 def term(q,side):
  w=beta(N+1,q+1) if side==0 else sum((math.comb(N,l)*math.comb(15,m)*beta(l+m+1,16-m+q) for l in range(N+1) for m in range(8)),F())
  return lam**q/F(math.factorial(q))*w
 vals=[]
 for side in [0,1]:
  lo=sum((term(q,side) for q in range(Q+1)),F());tail=term(Q+1,side)/(1-lam/F(Q+2));vals.append(interval_positive(lo,tail))
 return ii(F(nu,2**(N+1)))*(iv.exp(-ii(lam))*vals[0]+iv.exp(-ii(nu))*vals[1])
def main():
 start=time.monotonic();ctx.prec=512;ctx.threads=1;iv.dps=180;ids={}
 def ident(name,expr):
  z=sp.simplify(expr);assert z==0,(name,z);ids[name]=str(z)
 z,k,theta2,theta4,Ly=sp.symbols('z k theta2 theta4 Ly');a,g=sp.symbols('a gamma');f=theta2*z*z*(1+z*z)**(k/2-1)+theta4*z**4*(1+z*z)**(k/2-2)
 sf=sp.series(f,z,0,7).removeO().expand();lf=sp.series(f*(Ly+sp.log(1+z*z)/2),z,0,7).removeO().expand()
 ident('tail_x2',sf.coeff(z,2)-theta2);ident('tail_x4',sf.coeff(z,4)-theta4-(k-2)*theta2/2)
 ident('log_tail_x2',lf.coeff(z,2)-Ly*theta2);ident('log_tail_x4',lf.coeff(z,4)-(theta4+(k-2)*theta2/2)*Ly-theta2/2)
 tt=sp.series(sp.sqrt(1-z*z)*z*z*(1+(3-k)*z*z/2),z,0,7).removeO().expand();ident('angular_fourth',tt.coeff(z,4)-(2-k)/2)
 pp=(k-3)/2;sf1=sp.series(z*z*(1+z*z)**pp*(1-pp*z*z/(1+z*z)),z,0,9).removeO().expand()
 ident('counterexample_cartesian_fourth',sf1.coeff(z,4));ident('counterexample_sixth',sf1.coeff(z,6)+(k-3)*(k-5)/8)
 be=sp.symbols('beta');ident('corner_radial_power',-2*a+2*(a-g)+1+2*be-(2*be+1-2*g));ident('transport_energy',-(2-2*g)/(2*k)-1+(1-(g-1)/k))
 ell,er,ee,rhoE,transport,vel=sp.symbols('ell er e rhoE transport vel');ww=(rhoE-k*ee)/3;ident('scalar_extract',transport+vel+ell*rhoE/3-(transport+vel+ell*ww)-k*ell*ee/3)
 cq,ct=sp.symbols('ellq ellt');ident('log_scalar',(1/k)*ee+cq*rhoE/3-(1/k+k*cq/3)*ee-cq*ww);ident('tail_scalar',ct*rhoE/3-k*ct*ee/3-ct*ww)
 rr,C0=sp.symbols('r C0',positive=True);rem=k*C0/(1-k)*rr**(2*k-1);ident('far_integrated_forcing',(rr*sp.diff(rem,rr)/k-rem)+C0*rr**(2*k-1));ident('far_radial_bound',k*k/(1-k)+k-k/(1-k))
 eta=sp.symbols('eta',positive=True);ident('u2_cancel',-1-(sp.I*eta)**2*2/eta**2/2);ident('u3_cancel',sp.I*eta/3+(sp.I*eta)**3*2/eta**2/6);ident('u4_fourth_cancel',-1+(sp.I*eta)**4*24/eta**4/24);ident('u4_second_cancel',-eta**2/12+(sp.I*eta)**4*2/eta**2/24)
 x,y=sp.symbols('x y',real=True);logr=sp.log(x*x+y*y)/2;ident('kernel_halfplane',-sp.diff(logr,x,2,y).subs({x:-x,y:-y},simultaneous=True)-2*y*(3*x*x-y*y)/(x*x+y*y)**3)
 bracket=9-36/(a+2)+60/((a+2)*(a+3));ident('angular_beta_recurrence',bracket-3*(3*a*a+3*a+2)/((a+2)*(a+3)))
 t=sp.symbols('t');chi=sum(sp.binomial(15,m)*t**m*(1-t)**(15-m) for m in range(8));norm=F(math.factorial(15),math.factorial(7)**2)
 ident('C7_cutoff_derivative',sp.diff(chi,t)+sp.Rational(norm.numerator,norm.denominator)*t**7*(1-t)**7)
 for v in range(1,8):ident('cutoff_join0_'+str(v),sp.diff(chi,t,v).subs(t,0));ident('cutoff_join1_'+str(v),sp.diff(chi,t,v).subs(t,1))
 assert chi.subs(t,0)==1 and chi.subs(t,1)==0
 cpoly=sp.Poly(sp.expand(chi.subs(t,2*x-1)),x);coeff=[F(cpoly.nth(j)) for j in range(16)]
 # The finite blocks are independent examples, never PDE discretizations.
 mat=[[F(2),F(1),F(-1)],[F(3),F(-2),F(7)],[F(5),F(4),F(6)]];TT=sp.Matrix([sp.Rational(3,4),sp.Rational(11,2)]);bb=sp.Matrix([sp.Rational(-5,2),10]);ell0=sp.Matrix([[22,-3]])
 ident('T_annihilator',(ell0*TT)[0]);ident('tau_pairing',(ell0*bb)[0]+85);ident('block_determinant',sp.Matrix(mat).det()+85)
 hinv=inv_fraction([[F(9,20),F(1,5)],[F(1,10),F(3,10)]]);CH=max(sum(abs(x) for x in row) for row in hinv);assert CH==F(110,23)
 CB=[F(1,13),F(1,17)];BC=[F(1,7),F(-1,11)];S=F(2)-sum(CB[i]*hinv[i][j]*BC[j] for i in range(2) for j in range(2));assert S>0
 border=[[F(9,20),F(1,5),BC[0]],[F(1,10),F(3,10),BC[1]],[CB[0],CB[1],F(2)]]
 mats={'tail_block':mat,'border':border};exact_inv={n:inv_fraction(M) for n,M in mats.items()}
 for n,M in mats.items():
  sinv=sp.Matrix(M).inv();assert exact_inv[n]==[[F(sinv[i,j]) for j in range(3)] for i in range(3)]
 raw=B/'data_exact/modal_v2.json';assert sha(raw)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 kr=F.from_float(float.fromhex(json.loads(raw.read_text())['scalars_hex']['k']));assert kr==F(1615536043799051,9007199254740992);gam=F(1129,1000);br=2-gam
 beta_rad=F(6)/(br*(br+1)*(br+2)*(br+3));beta_ang_pi=F(math.factorial(12),2*4**6*math.factorial(6)*math.factorial(7));ell2_pi=2*beta_rad*beta_ang_pi*F(16,3)
 exact={'k':kr,'gamma':gam,'a':F(6),'tail_power':2*kr-1,'zeroth_far_margin':gam-2*kr,'radial_tail_divergence_power':2*kr+1-2*gam,'tail_x4_angular':(2-kr)/2,'tail_x6_cartesian':-(kr-3)*(kr-5)/8,'transport_gap':1-(gam-1)/kr,'strain_squared_times_pi':ell2_pi,'flat_trace_squared_constant':F(math.factorial(12),2**13),'closure_theta':F(4,27),'closure_bound':CH,'border_S':S,'border_bound':CH+(1+CH*max(map(abs,BC)))/S*(1+sum(map(abs,CB))*CH),'border_actual_inverse_norm':max(sum(map(abs,r)) for r in exact_inv['border'])}
 assert exact['zeroth_far_margin']>0 and exact['radial_tail_divergence_power']>-1 and exact['transport_gap']>0 and exact['border_bound']>exact['border_actual_inverse_norm']
 vals={};traces={};inverse={}
 for method,conv in [('arb',aa),('iv',ii)]:
  now={n:conv(v) for n,v in exact.items()};pi=arb.pi() if method=='arb' else machin()
  if method=='arb':
   rad=aa(4).gamma()*aa(br).gamma()/aa(4+br).gamma();ang=aa(F(3,2)).gamma()*aa(F(13,2)).gamma()/aa(8).gamma();sq=2*rad*ang*aa(F(16,3))/pi**2
  else:sq=conv(ell2_pi)/pi
  now['strain_constant']=sq.sqrt() if method=='arb' else iv.sqrt(sq);now['strain_squared']=sq
  vals[method]={n:rec(v) for n,v in now.items()};traces[method]={};inverse[method]={}
  for N in [2,4]:
   for nu in [4,16,64]:
    tr=trace_arb(nu,N,coeff) if method=='arb' else trace_iv(nu,N);mainterm=conv(F(math.factorial(N),nu**N));q=conv(F(nu,2));expq=(-q).exp() if method=='arb' else iv.exp(-q);err=mainterm*expq*sum((q**i/math.factorial(i) for i in range(N+1)),conv(0));gap=mainterm-tr
    assert ends(tr)[0]>0 and ends(gap)[0]>0 and ends(err-gap)[0]>0
    traces[method][f'{N}:{nu}']={n:rec(v) for n,v in {'multiplier':tr,'leading':mainterm,'tail_error_bound':err,'relative_gap':gap/mainterm}.items()}
  for n,M in mats.items():
   vv=arb_mat([[conv(v) for v in row] for row in M]).inv() if method=='arb' else inv_iv(M)
   inverse[method][n]=[[rec(vv[i,j] if method=='arb' else vv[i][j]) for j in range(3)] for i in range(3)]
 def overlap(o,p):assert max(F(o['lower_exact']),F(p['lower_exact']))<=min(F(o['upper_exact']),F(p['upper_exact']))
 for n in vals['arb']:overlap(vals['arb'][n],vals['iv'][n])
 for n,row in traces['arb'].items():
  for f in row:overlap(row[f],traces['iv'][n][f])
 for n in mats:
  for i in range(3):
   for j in range(3):
    overlap(inverse['arb'][n][i][j],inverse['iv'][n][i][j]);r=exact_inv[n][i][j]
    for method in ['arb','iv']:assert F(inverse[method][n][i][j]['lower_exact'])<=r<=F(inverse[method][n][i][j]['upper_exact'])
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','code_sha256':sha(__file__),'proof_sha256':sha(B/'research/tail_coordinates/PROOF.md'),'data_sha256':sha(raw),'exact_identities':ids,'exact_parameters':{n:str(v) for n,v in exact.items()},'cutoff_coefficients':[str(v) for v in coeff],'matrix_inputs':{n:[[str(v) for v in row] for row in M] for n,M in mats.items()},'exact_inverse':{n:[[str(v) for v in row] for row in M] for n,M in exact_inv.items()},'values':vals,'trace_integrals':traces,'matrix_inverses':inverse,'method':'Exact symbolic series/kernel/cutoff identities and Fraction Gauss-Jordan versus Sympy inversion; Arb512 Gamma and expanded polynomial antiderivatives versus iv180 exact factorial/Machin constant and positive Beta series with geometric tails; Arb matrix inversion versus iv elimination.','seconds':time.monotonic()-start,'scope':'Elementary tail and conditional block algebra; illustrative matrices, no PDE operator enclosure.'}
 (E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');summary={k:v for k,v in out.items() if k not in ['values','trace_integrals','matrix_inverses','cutoff_coefficients','exact_inverse']};summary['checks_sha256']=sha(E/'checks.json');summary['values_display']={m:{n:v['display'] for n,v in row.items()} for m,row in vals.items()};summary['trace_display']={m:{n:{f:v['display'] for f,v in row.items()} for n,row in tab.items()} for m,tab in traces.items()};(E/'review_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'seconds':out['seconds'],'identities':len(ids),'strain':vals['arb']['strain_constant']['display'],'closure_bound':str(CH)}),flush=True)
if __name__=='__main__':main()

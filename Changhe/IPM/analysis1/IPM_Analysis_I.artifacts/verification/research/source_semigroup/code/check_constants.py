"""Exact symbolic identities and two interval engines for auxiliary inverse bounds."""
import os
for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sys,json,hashlib,itertools,time
import sympy as sp
from flint import arb,fmpq,ctx
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_semigroup';E=D/'evidence';ctx.prec=512;ctx.threads=1;iv.dps=180
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aq(q):q=Q(q);return arb(fmpq(q.numerator,q.denominator))
def iq(q):q=Q(q);return iv.mpf(q.numerator)/q.denominator
def ep(x):m,e=x.man_exp();return Q(int(m))*Q(2)**int(e)
def ends(z):
 if isinstance(z,arb):return ep(z.lower()),ep(z.upper())
 def f(v):sg,m,e,bc=v;return (-1 if sg else 1)*Q(int(m))*Q(2)**int(e)
 return tuple(f(v) for v in z._mpi_)
def pack(vals):return {'lower_exact':str(vals[0]),'upper_exact':str(vals[1]),'mid_approx':float(sum(vals)/2)}
def main():
 start=time.monotonic();sv=Q(31,10);kap=Q(1687,500);ids={}
 def check(name,expr):assert sp.simplify(expr)==0,(name,expr);ids[name]=str(expr)
 x,y,A,mu,s=sp.symbols('x y A mu s',real=True);f=sp.Function('f')(x,y);j=(1+x*x+y*y)**(s/2)
 L=lambda h:-sp.diff(A*x*h,x)-sp.diff(mu*y*h,y)
 check('linear_positive_conjugation',j*L(f)-L(j*f)-s*(A*x*x+mu*y*y)/(1+x*x+y*y)*j*f)
 check('leading_tensor_L2_margin',(1+x*x+y*y)**2-(x*x+y*y)**2-(1+2*x*x+2*y*y))
 check('strain_symbol_square_margin',(x*x+y*y)**3-y*y*x**4-(x**6+2*x**4*y*y+3*x*x*y**4+y**6))
 tt,aa,dd,RR,z0,y0=sp.symbols('tt aa dd RR z0 y0',positive=True)
 z=sp.exp(-aa*tt/s)*(z0+RR/dd*y0*(1-sp.exp(-dd*tt/s)))
 check('comparison_ODE',sp.diff(z,tt)+aa*z/s-RR*y0*sp.exp(-(aa+dd)*tt/s)/s)
 e,v,q=sp.symbols('e v q',real=True)
 check('gap_cancellation',1+(A+mu)/2-e/2-q-(sp.Rational(1687,500)-e/2-sp.Rational(31,10)*v-q)-(1+(A+mu)/2-sp.Rational(1687,500)+sp.Rational(31,10)*v))
 a,b,c,d,l1,l2,r1,r2=sp.symbols('a b c d l1 l2 r1 r2');mat=sp.Matrix([[a,b],[c,d]]);ell=sp.Matrix([l1,l2]);row=sp.Matrix([[r1,r2]]);ainv=mat.inv();den=1+(row*ainv*ell)[0]
 check('rankone_determinant',(mat+ell*row).det()-mat.det()*den)
 candidate=ainv-ainv*ell*row*ainv/den
 for i in range(2):
  for k in range(2):check('rankone_inverse_'+str(i)+str(k),((mat+ell*row)*candidate-sp.eye(2))[i,k])
 rows=[];count=0
 for av,mv,ev,frac,rv in itertools.product([Q(10),Q(51,5)],[Q(99,100),Q(101,100)],[Q(0),kap/4,kap/2],[Q(0),Q(1,2)],[Q(0),Q(1),Q(10),Q(100)]):
  dw=frac*ev/sv;gap=1+(av+mv)/2-kap+sv*dw;decay=kap-ev;base=1+rv/gap
  assert gap>=Q(3121,1000) and decay>=kap/2 and ev>=sv*dw;count+=3
  vals={}
  for name,cv,powf in [('arb512',aq,lambda a,b:a**b),('iv180',iq,iv.power)]:
   val=powf(cv(base),cv(sv));vals[name]={'C':ends(val),'K_A':ends(val/cv(decay))}
  hull={key:pack((min(vals[n][key][0] for n in vals),max(vals[n][key][1] for n in vals))) for key in ['C','K_A']}
  rows.append({'A':str(av),'mu':str(mv),'E':str(ev),'Dw':str(dw),'R':str(rv),'gap':str(gap),'a_s':str(decay),'base':str(base),'bounds':hull})
 beta=[]
 for cv,pi,sqrt in [(aq,arb.pi(),lambda x:x.sqrt()),(iq,iv.pi,iv.sqrt)]:beta.append(ends(1/(2*sqrt(pi*(cv(sv)-1)*(cv(sv)-2)))))
 beta_bound=pack((min(z[0] for z in beta),max(z[1] for z in beta)))
 paths=[Path(__file__),D/'PROOF.md',D/'ADDENDUM.md',E/'proof_first.json',B/'research/source_local_estimate/evidence/verdict.json',B/'research/source_local_estimate/PROOF.md',B/'research/source_local_estimate/ADDENDUM.md'];pins={str(p.relative_to(B)):sha(p) for p in paths}
 dep=json.loads((B/'research/source_local_estimate/evidence/verdict.json').read_text());assert dep['status']=='CONFIRMED_CONDITIONAL_LOCAL_SOURCE_ESTIMATE'
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_AUXILIARY_INVERSE_FORMULAS','symbolic_identities':ids,'rows':rows,'beta_s':beta_bound,'counts':{'symbolic_identities':len(ids),'illustrative_rows':len(rows),'exact_illustrative_inequalities':count,'primary_engine_scalar_enclosures':len(rows)*4+2},'scope':'Abstract exact rational scalar illustrations only; no actual coefficient norms, E or R supplied.','files':pins,'seconds':time.monotonic()-start}
 (E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['rows','symbolic_identities','files']},indent=2))
if __name__=='__main__':main()

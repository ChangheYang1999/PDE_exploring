"""Direct radial identities and scalar moments by cancellation-aware Arb/iv recurrence."""
import os
for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import sys,json,hashlib,time
import sympy as sp
from flint import arb,fmpq,ctx
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];D=B/'research/radial_defect';E=D/'evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aq(q):q=Q(q);return arb(fmpq(q.numerator,q.denominator))
def iq(q):q=Q(q);return iv.mpf(q.numerator)/q.denominator
def ep(x):m,e=x.man_exp();return Q(int(m))*Q(2)**int(e)
def ends(z):
 if isinstance(z,arb):return ep(z.lower()),ep(z.upper())
 def val(v):sg,m,e,bc=v;return (-1 if sg else 1)*Q(int(m))*Q(2)**int(e)
 return tuple(val(v) for v in z._mpi_)
def pack(allends):return {'lower_exact':str(min(x[0] for x in allends)),'upper_exact':str(max(x[1] for x in allends))}
def main():
 start=time.monotonic();inp=json.loads((E/'test_inputs.json').read_text());ids={};t,l,lam=sp.symbols('t l lam',real=True,nonzero=True);A=sp.Function('A')(t);BB=sp.Function('B')(t);f=sp.Function('f')(t)
 sub={sp.diff(A,t):-l*A+sp.exp(2*t)*f,sp.diff(BB,t):l*BB-sp.exp(2*t)*f}
 def check(name,e):assert sp.simplify(e)==0,(name,e);ids[name]='0'
 P=(A+BB)*sp.exp(-2*t)/2;R=(BB-A)*sp.exp(-2*t)/2
 check('P_equation',sp.diff(P,t).subs(sub)+2*P-l*R)
 check('R_equation',sp.diff(R,t).subs(sub)-l*P+2*R+f)
 check('plus_equation',sp.diff(P+R,t).subs(sub)-(l-2)*(P+R)+f)
 check('minus_equation',sp.diff(P-R,t).subs(sub)+(l+2)*(P-R)-f)
 check('canonical_radial_derivative',sp.exp(-t)*sp.diff((A+BB)/(2*l),t).subs(sub)-(BB-A)*sp.exp(-t)/2)
 q=sp.Function('q')(t);p=sp.Function('p')(t);g=sp.Function('g')(t)
 check('variation_of_constants',sp.diff(sp.exp(-lam*t)*(q-p),t).subs(sp.diff(q,t),lam*q+g)-sp.exp(-lam*t)*(g+lam*p-sp.diff(p,t)))
 J=(sp.exp(lam*t)-1)/lam
 for j in range(4):
  if j:J=(j*J-t**j)/lam
  check('moment_ode_'+str(j),sp.diff(J,t)-lam*J-t**j);check('moment_zero_'+str(j),J.subs(t,0))
 gamma,c0,c1,c2=sp.symbols('gamma c0 c1 c2');cs=[c0,c1,c2];force=sp.exp(gamma*t)*(c0+c1*t+c2*t*t)
 for j in range(6):check('forcing_coefficient_'+str(j),sp.diff(force,t,j).subs(t,0)/sp.factorial(j)-sum(cs[k]*gamma**(j-k)/sp.factorial(j-k) for k in range(min(j,2)+1)))
 rows=[];enginecount=0;ineq=0
 for n in inp['mode_indices']:
  for branch,lv in [('+',2*n-2),('-',-2*n-2)]:
   for hs in inp['cell_widths']:
    h=Q(hs);vals={}
    for name,cv,exp in [('arb512',aq,lambda x:x.exp()),('iv180',iq,iv.exp)]:
     hv=cv(h);M=exp(cv(max(lv,0))*hv);js={}
     if lv==0:
      for j in inp['moment_orders']:js[j]=hv**(j+1)/(j+1)
     else:
      jj=(exp(cv(lv)*hv)-1)/lv
      if 0 in inp['moment_orders']:js[0]=jj
      for j in range(1,max(inp['moment_orders'])+1):
       jj=(j*jj-hv**j)/lv
       if j in inp['moment_orders']:js[j]=jj
     vals[name]={'M':ends(M),'J':{j:ends(v) for j,v in js.items()}};enginecount+=1+len(js)
     for j,v in js.items():
      lo,hi=ends(v);assert lo>0;ineq+=1
      if lv!=0:assert hi<=ends(M*hv**(j+1)/(j+1))[0];ineq+=1
      else:assert lo<=h**(j+1)/(j+1)<=hi;ineq+=1
    rows.append({'n':n,'branch':branch,'lambda':str(lv),'h':str(h),'M':pack([z['M'] for z in vals.values()]),'J':{str(j):pack([z['J'][j] for z in vals.values()]) for j in inp['moment_orders']}})
 paths=[Path(__file__),D/'PROOF.md',E/'proof_first.json',E/'test_inputs.json']
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_RADIAL_DEFECT_IDENTITIES_AND_MOMENTS','counts':{'symbolic_identities':len(ids),'parameter_rows':len(rows),'moment_cases':len(rows)*len(inp['moment_orders']),'primary_engine_enclosures':enginecount,'primary_inequalities':ineq},'rows':rows,'identities':ids,'scope':'Illustrative scalar arithmetic only; actual allcell flow audit OPEN.','files':{str(p.relative_to(B)):sha(p) for p in paths},'seconds':time.monotonic()-start}
 (E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['rows','identities','files']},indent=2))
if __name__=='__main__':main()

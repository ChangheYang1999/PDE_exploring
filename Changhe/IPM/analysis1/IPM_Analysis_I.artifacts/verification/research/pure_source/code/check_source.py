"""Pure-source identities and independent intervals for a smooth-forcing example."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import sys,json,hashlib,math,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as sp
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/pure_source/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def ii(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def dyad(m,e):return F(int(m))*F(2)**int(e)
def ends(q):
 if isinstance(q,arb):return tuple(dyad(*v.man_exp()) for v in (q.lower(),q.upper()))
 return tuple((-1 if s else 1)*dyad(m,e) for s,m,e,b in q._mpi_)
def rec(q):l,u=ends(q);assert l<=u;return {'lower_exact':str(l),'upper_exact':str(u),'display':[float(l),float(u)]}
def log_ratio(z,N):
 z=F(z);assert 0<z<1;lo=2*sum((z**(2*n+1)/F(2*n+1) for n in range(N)),F());tail=2*z**(2*N+1)/((2*N+1)*(1-z*z));return iv.mpf([ii(lo).a,ii(lo+tail).b])
def exp_series(x,N=180):
 lo,up=ends(x);assert 0<=lo<=up<N+2
 total=ii(1);term=ii(1)
 for n in range(1,N+1):term=term*x/n;total+=term
 tail=up**(N+1)/F(math.factorial(N+1))/(1-up/F(N+2));return total+iv.mpf([0,ii(tail).b])
def main():
 start=time.monotonic();ctx.prec=512;ctx.threads=1;iv.dps=180;ids={}
 def ident(n,e):
  v=sp.simplify(e);assert v==0,(n,v);ids[n]=str(v)
 s,y,A,u=sp.symbols('s y A u',positive=True);Q=sp.Function('Q');z=y*s**(-1/A);h=-y/A*Q(z);QP=sp.diff(Q(u),u).subs(u,z)
 ident('source_s_derivative',sp.diff(h,s)-s**(1/A-1)*z*z*QP/A**2);ident('source_y_derivative',sp.diff(h,y)+(Q(z)+z*QP)/A)
 ident('source_homogeneous_equation',A*s*sp.diff(h,s)+y*sp.diff(h,y)-h)
 ident('derivative_square_measure',2*(1/A-1)+1/A-(3/A-2));ident('derivative_L1_measure',1/A-1+1/A-(2/A-1));ident('boundary_L1_power',1/A+1/A-2/A)
 a=sp.symbols('a',positive=True);ident('CS_weight_integral',sp.integrate(u**(-4),(u,a,2))-(a**(-3)-sp.Rational(1,8))/3)
 eps,delta=sp.symbols('epsilon delta',positive=True);rad=(eps**(3/A-1)-delta**(3/A-1))/(1-3/A);ident('truncated_radial_derivative',sp.diff(rad,delta)-delta**(3/A-2))
 x,L=sp.symbols('x L',real=True);cl=(A+1)/2;psi=(A*L-(A-cl)*x)*y;v1=cl*x-sp.diff(psi,y);v2=cl*y+sp.diff(psi,x)
 ident('positive_source_patch',v1-A*(x-L));ident('positive_source_vertical',v2-y);ident('source_divergence',sp.diff(v1,x)+sp.diff(v2,y)-2*cl)
 mu,g=sp.symbols('mu g');grad=sp.Matrix([0,g]);ident('C1_y_eigenvalue',(sp.diag(A,mu).T*grad-grad)[1]-g*(mu-1));ident('C1_x_eigenvalue',(sp.diag(A,mu).T*grad-grad)[0])
 t=sp.symbols('t',real=True);ph=sp.Function('phi');ps=sp.Function('psi');ident('characteristic_cancellation',sp.exp(-t)*sp.exp(t)*y*ph(sp.exp(A*t)*s)*ps(sp.exp(t)*y)-y*ph(sp.exp(A*t)*s)*ps(sp.exp(t)*y))
 ident('pure_transport_resonance',A*s*sp.diff(y*sp.log(y),s)+y*sp.diff(y*sp.log(y),y)-y*sp.log(y)-y)
 raw=B/'data_exact/modal_v2.json';assert sha(raw)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';k=F.from_float(float.fromhex(json.loads(raw.read_text())['scalars_hex']['k']));assert k==F(1615536043799051,9007199254740992)
 ar=2/k-1;beta=1-3/ar;exact={'k':k,'c_l':1/k,'A':ar,'jump':-1/ar,'radial_exponent':3/ar-2,'divergence_power':beta,'boundary_vanishing_power':2/ar,'delta':F(1,2),'sigma':F(153,50)}
 assert ar>3 and exact['radial_exponent']<-1 and beta>0 and exact['sigma']>2
 vals={}
 for method,conv in [('arb',aa),('iv',ii)]:
  now={n:conv(v) for n,v in exact.items()}
  if method=='arb':
   l2=aa(2).log();l10=aa(10).log();p2=aa(2)**aa(3/ar);ang=3/(p2-aa(F(1,8)));pref=ang/aa(ar)**4;da=aa(F(1,2))**aa(-beta)
   now.update({'log2':l2,'log10':l10,'angular_CS_lower':ang,'norm_prefactor_lower':pref,'axis_cutoff_a':aa(2)**aa(-1/ar)})
   for m in [1,2,3]:now['annulus_lower_'+str(m)]=pref*(aa(F(1,10**m))**aa(-beta)-da)/aa(beta)
  else:
   l2=log_ratio(F(1,3),200);l10=l2+log_ratio(F(2,3),600);p2=exp_series(ii(3/ar)*l2);ang=3/(p2-ii(F(1,8)));pref=ang/ii(ar)**4;da=exp_series(ii(beta)*l2)
   now.update({'log2':l2,'log10':l10,'angular_CS_lower':ang,'norm_prefactor_lower':pref,'axis_cutoff_a':1/exp_series(ii(1/ar)*l2)})
   for m in [1,2,3]:now['annulus_lower_'+str(m)]=pref*(exp_series(ii(m*beta)*l10)-da)/ii(beta)
  assert ends(now['angular_CS_lower'])[0]>0 and ends(now['annulus_lower_1'])[0]>0
  assert ends(now['annulus_lower_1'])[1]<ends(now['annulus_lower_2'])[0]<ends(now['annulus_lower_2'])[1]<ends(now['annulus_lower_3'])[0]
  vals[method]={n:rec(v) for n,v in now.items()}
 for n in vals['arb']:assert max(F(vals['arb'][n]['lower_exact']),F(vals['iv'][n]['lower_exact']))<=min(F(vals['arb'][n]['upper_exact']),F(vals['iv'][n]['upper_exact']))
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','code_sha256':sha(__file__),'proof_sha256':sha(B/'research/pure_source/PROOF.md'),'data_sha256':sha(raw),'exact_identities':ids,'exact_parameters':{n:str(v) for n,v in exact.items()},'values':vals,'method':'Symbolic source/characteristic/distributional exponent identities; Arb512 powers and logarithms versus iv180 positive atanh log2/log5 series and positive exponential series with explicit tails.','seconds':time.monotonic()-start,'scope':'Smooth-forcing pure-transport counterexample only; numerical values are lower bounds from CS, not a profile norm.'}
 (E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');summary={k:v for k,v in out.items() if k!='values'};summary['checks_sha256']=sha(E/'checks.json');summary['values_display']={m:{n:v['display'] for n,v in row.items()} for m,row in vals.items()};(E/'review_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'seconds':out['seconds'],'identities':len(ids),'jump':vals['arb']['jump']['display'],'annulus_lower3':vals['arb']['annulus_lower_3']['display']}),flush=True)
if __name__=='__main__':main()

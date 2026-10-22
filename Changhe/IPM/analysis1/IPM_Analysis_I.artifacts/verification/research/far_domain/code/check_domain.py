"""Exact far-domain identities and illustrative constants; no profile existence input."""
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
B=Path(__file__).resolve().parents[3];E=B/'research/far_domain/evidence'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def ii(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def dyad(m,e):return F(int(m))*F(2)**int(e)
def bounds(q):
 if isinstance(q,arb):return tuple(dyad(*v.man_exp()) for v in (q.lower(),q.upper()))
 return tuple((-1 if sign else 1)*dyad(man,ex) for sign,man,ex,bc in q._mpi_)
def rec(q):
 l,u=bounds(q);assert l<=u;return {'lower_exact':str(l),'upper_exact':str(u),'display':[float(l),float(u)]}
def machin(N=190):
 def atan(q):
  s=sum(((-1)**j*F(1,(2*j+1)*q**(2*j+1)) for j in range(N)),F(0));term=F(1,(2*N+1)*q**(2*N+1));return s,s+term # N even: next term positive
 l5,u5=atan(5);l2,u2=atan(239);return iv.mpf([ii(16*l5-4*u2).a,ii(16*u5-4*l2).b])
def exp_positive(z,N=160):
 z=F(z);assert 0<z<N+2;terms=[z**j/F(math.factorial(j)) for j in range(N+1)];lo=sum(terms,F(0));tail=z**(N+1)/F(math.factorial(N+1))/(1-z/F(N+2));return iv.mpf([ii(lo).a,ii(lo+tail).b])
def main():
 start=time.monotonic();ctx.prec=512;ctx.threads=1;iv.dps=180
 x,y=sp.symbols('x y',real=True);cl,g,eps,a,b,t=sp.symbols('cl gamma eps a b t',real=True)
 z=sp.log(x*x+y*y)/2;ker=sp.diff(z,x,2,y);target=2*y*(3*x*x-y*y)/(x*x+y*y)**3
 identities={}
 def ident(name,expr):
  val=sp.simplify(expr);assert val==0,(name,val);identities[name]=str(val)
 ident('kernel_log_xxy',ker-target)
 ident('kernel_at_negative_point',-ker.subs({x:-x,y:-y},simultaneous=True)/2-y*(3*x*x-y*y)/(x*x+y*y)**3)
 ident('strain_positive_square',y*(3*x*x-y*y)*y*(3*x*x-y*y)-y*y*(3*x*x-y*y)**2)
 ident('flow_mass_exponent',2+2*cl-2*g*(cl+eps)-2*(1+cl-g*(cl+eps)))
 R=sp.Function('R');vv=sp.exp(-(g-1)*t)*R(t)
 ident('Hardy_E',sp.diff(vv,t)+(g-1)*vv-sp.exp(-(g-1)*t)*sp.diff(R(t),t))
 ident('Hardy_K',sp.diff(vv,t)-(2-g)*vv-sp.exp(-(g-1)*t)*(sp.diff(R(t),t)-R(t)))
 ident('Hardy_boundary_exponent',-(2-g)*t-(g-1)*t+t)
 rr,lam=sp.symbols('r lambda',positive=True);ident('cubic_scaling',sp.diff(lam**(-1)*(lam*x)**2*(lam*y),lam).subs(lam,1)-2*x*x*y)
 ident('kernel_homogeneity',target.subs({x:lam*x,y:lam*y},simultaneous=True)-lam**(-3)*target)
 ident('velocity_kernel_homogeneity',(-x*y/(x*x+y*y)**2).subs({x:lam*x,y:lam*y},simultaneous=True)-lam**(-2)*(-x*y/(x*x+y*y)**2))
 ident('tail_square_radial_exponent',2*(a-3)-2*g+1-(2*a-5-2*g))
 ident('jet_weight_power',4*b+1-2*g-((4*b+1)-2*g))
 # Exact box lower bound for chi supported on four reflected squares.
 assert F(3)*F(5,4)**2-F(7,4)**2==F(13,8)
 assert 2*F(7,4)**2==F(49,8)
 assert F(5,4)**2*F(13,8)**2/F(49,8)**3==F(4225,235298)
 assert 4*(F(7,4)-F(5,4))**2==1
 rawpath=B/'data_exact/modal_v2.json';assert sha(rawpath)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 raw=json.loads(rawpath.read_text());k=F.from_float(float.fromhex(raw['scalars_hex']['k']));assert k==F(1615536043799051,9007199254740992)
 gamma=F(1129,1000);epsilon=F(1,10);c=1/k
 exact={'k':k,'gamma':gamma,'c_l':c,'epsilon':epsilon,'far_threshold_margin':1+k-gamma,'flow_growth_rate':1+c-gamma*(c+epsilon),'transport_rate':1-c*(gamma-1),'Hardy_E_constant':1/(gamma-1),'Hardy_K_constant':1/(2-gamma),'kernel_safe_constant_rational':F(4)}
 assert exact['far_threshold_margin']>0 and exact['flow_growth_rate']>0 and 1<gamma<1+k<2
 vals={}
 for method,q,pi,expz in [('arb',aa,arb.pi(),aa(F(32,3)).exp()),('iv',ii,machin(),exp_positive(F(32,3)))]:
  now={name:q(value) for name,value in exact.items()}
  now.update({'explicit_strain_lower':q(F(4225,235298))/pi/expz,'velocity_tail_constant':q(4)/pi,'component_vector_constant':q(2)*q(2)**q(F(1,2))/pi})
  assert bounds(now['explicit_strain_lower'])[0]>F('0.000000133')
  assert bounds(now['velocity_tail_constant'])[1]<F('1.274')
  assert bounds(now['component_vector_constant'])[1]<bounds(now['velocity_tail_constant'])[0]
  vals[method]={name:rec(value) for name,value in now.items()}
 for name in vals['arb']:
  l,u=map(F,[vals['arb'][name]['lower_exact'],vals['arb'][name]['upper_exact']]);v,w=map(F,[vals['iv'][name]['lower_exact'],vals['iv'][name]['upper_exact']]);assert max(l,v)<=min(u,w)
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','code_sha256':sha(__file__),'proof_sha256':sha(B/'research/far_domain/PROOF.md'),'data_sha256':sha(rawpath),'exact_identities':identities,'exact_parameters':{k:str(v) for k,v in exact.items()},'values':vals,'methods':'Sympy exact differentiation plus rational inequalities; Arb512 exp/pi versus iv180 rational positive-exp series and exact alternating Machin pi. Constants are illustrative conditional-theorem parameters, not bounds on an unknown solution.','strict_strain_lower':'0.000000133','seconds':time.monotonic()-start,'scope':'Conditional far-domain obstruction only. No profile or full inverse asserted.'}
 (E/'checks.json').write_text(json.dumps(result,indent=2)+'\n');summary={k:v for k,v in result.items() if k!='values'};summary['values_display']={k:{n:r['display'] for n,r in v.items()} for k,v in vals.items()};summary['checks_sha256']=sha(E/'checks.json');(E/'review_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({'utc':result['utc'],'status':result['status'],'seconds':result['seconds'],'identities':len(identities),'strain_lower_display':vals['arb']['explicit_strain_lower']['display']}),flush=True)
if __name__=='__main__':main()

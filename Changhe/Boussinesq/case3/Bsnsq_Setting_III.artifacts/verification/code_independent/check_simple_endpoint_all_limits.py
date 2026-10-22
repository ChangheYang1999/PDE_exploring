"""P299 independently differentiate analytic ansatz and audit singular-system algebra."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import sympy as S
V=Path('research/299_simple_endpoint_all_limits/verification')
t0=time.monotonic();start=datetime.now(timezone.utc).isoformat();checks=[]
def ck(name,ok,detail=None):checks.append(dict(name=name,passed=bool(ok),detail=detail))
def zero(name,expr):
 v=S.factor(S.cancel(expr));ck(name,v==0,str(v))
s,beta=S.symbols('s beta',positive=True)
C=S.symbols('C',real=True,nonzero=True);ell=S.symbols('ell',real=True)
c=3*beta+2;a=4*beta+3
z,x,G,H,VV=S.symbols('z x G H V')
X=S.Matrix([z,x,G,H,VV])
for q in (0,1):
 for eps in (-1,1):
  tag=f'q{q}_eps{eps}_';delta=S.Rational(1+2*q,2)
  h0=-C/a;w0=eps*ell*C*(beta-2+q*c)/(4*(1+2*q))
  g=C+G;h=h0+H;w=w0+VV
  f=S.Matrix([-eps*s**4*h-2*eps*s**(5-q)*w,z-x,(2*z-3*x)*g/(c+x),((z-3*x-a)*h-g)/(c+x),delta*w+S.Rational(3,2)*w*(2*z-3*x)/(c+x)-eps*ell*g*(beta-2+q*(c+x))/8])
  subs0={j:0 for j in X};at0={**subs0,s:0}
  for j,value in enumerate(f.subs(at0)):zero(tag+'initial_balance_'+str(j),value)
  def ds(v):return S.diff(v,s)+sum(S.diff(v,u)*fu/s for u,fu in zip(X,f))
  def dy(v):return -eps*ds(v)
  B=s*(c+x);b=eps*B;T=s**3*g;eta=s**3*h;v=s**(4-q)*w;D=ell*s**(6-q)*g**2
  zero(tag+'Bprime',ds(B)-(c+z))
  zero(tag+'curl',eta+dy(dy(b))+2*v)
  zero(tag+'thermal',b*dy(T)+(3*beta+2-2*dy(b))*T)
  zero(tag+'eta',b*dy(eta)+(2*beta+1-dy(b))*eta-T)
  zero(tag+'fourth',b*dy(D)+(7*beta+2-4*dy(b))*D-8*dy(v)*T+12*v*dy(T))
  zero(tag+'ratio',D/T**2-ell*s**(-q))
  zero(tag+'slope_at_endpoint',dy(b).subs(at0)+c)
  A0=f.jacobian(X).subs(at0)
  for row in range(5):
   for col in range(row+1,5):zero(tag+f'triangular_{row}_{col}',A0[row,col])
  for j,d in enumerate([0,-1,0,-a/c,delta]):zero(tag+'diagonal_'+str(j),A0[j,j]-d)
  ck(tag+'zero_eigenspace_dimension_one',A0.rank()==4)
  lam=S.symbols('lambda');zero(tag+'charpoly',A0.charpoly(lam).as_expr()-lam**2*(lam+1)*(lam+a/c)*(lam-delta))
  f0=f.subs(subs0)
  for j in range(5):
   for k in range(4):zero(tag+f'initial_forcing_order4_{j}_{k}',S.diff(f0[j],s,k).subs(s,0))
  zero(tag+'initial_forcing_exact_z',f0[0]+eps*s**4*h0+2*eps*s**(5-q)*w0)
  for j in range(1,5):zero(tag+'other_initial_forcing_'+str(j),f0[j])
  ck(tag+'kernel_boundary_exponent',2-delta>0,str(2-delta))
  ck(tag+'zero_image_integrable',3-delta>-1,str(3-delta))
  ck(tag+'Lipschitz_first_integrable',2-delta>-1,str(2-delta))
  ck(tag+'Lipschitz_second_integrable',3-delta>-1,str(3-delta))
  for k in range(1,8):
   zero(tag+f'coefficient_matrix_det_{k}',(k*S.eye(5)-A0).det()-k**2*(k+1)*(k+a/c)*(k-delta))
   ck(tag+f'no_integer_resonance_{k}',S.Rational(k)!=delta)
  # A fourth-order correction is forced by (4 I-A) X4 = [z-forcing4,0,...].
  # This checks leading analytic departures without invoking any solver lane code.
  rhs=S.Matrix([S.diff(f0[j],s,4).subs(s,0)/24 for j in range(5)])
  X4=(4*S.eye(5)-A0).inv()*rhs
  for j in range(5):zero(tag+'first_coefficient_'+str(j),((4*S.eye(5)-A0)*X4-rhs)[j])
  ck(tag+'signed_powers_analytic',all(k>=0 and isinstance(k,int)for k in [1,3,3,4-q,6-q]))
  if q==0:zero(tag+'constant_limit_exact',D/T**2-ell)
  else:zero(tag+'pole_coefficient_exact',s*D/T**2-ell)
freeze=json.loads((V/'freeze.json').read_text());ck('proof_precedes_controls',freeze['proof_written_utc']<start);ck('proof_unchanged',hashlib.sha256((V.parent/'PROOF.md').read_bytes()).hexdigest()==freeze['proof_sha256'])
end=datetime.now(timezone.utc).isoformat();d=dict(started_utc=start,ended_utc=end,elapsed_seconds=time.monotonic()-t0,passed=sum(x['passed']for x in checks),total=len(checks),checks=checks,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(V/'checks.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({k:v for k,v in d.items()if k!='checks'},indent=2));print('FAILURES',json.dumps([x for x in checks if not x['passed']],indent=2))

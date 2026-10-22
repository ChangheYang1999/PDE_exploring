"""Exact finite-regularity controls for packet123's smooth extension proof.

No sampling is used for the product-rule norm bounds. These piecewise polynomial
controls are only C^11 or better, not the C-infinity extension in the theorem.
The coefficients and widths are exported as exact rational JSON data.
"""
from pathlib import Path
from datetime import datetime,timezone
from time import monotonic
from math import factorial,comb
import hashlib,json
import sympy as s
root=Path('research/123_whole_axis_flat_realization/verification');root.mkdir(parents=True,exist_ok=True)
u=s.Symbol('u');x,y=s.symbols('x y');t0=monotonic()
started_utc=datetime.now(timezone.utc).isoformat()
K=12
# Increasing beta-distribution step, with 12 vanishing endpoint derivatives.
density=u**K*(1-u)**K
norm=s.integrate(density,(u,0,1))
step=s.Poly(s.integrate(density,u)/norm,u)
assert step.eval(0)==0 and step.eval(1)==1
assert s.Poly(s.diff(step.as_expr(),u)-density/norm,u).is_zero
for k in range(1,K+1):assert step.diff((u,k)).eval(0)==step.diff((u,k)).eval(1)==0

def serial(p):return [{'power':int(a[0]),'coefficient':str(v)}for a,v in p.terms()]
def deserialize(rows):return s.Poly.from_dict({(r['power'],):s.Rational(r['coefficient'])for r in rows},u)
def l1(p):return sum(abs(z)for z in p.all_coeffs())
# On each unit interval exactly two partition members add to one.
eta_left=step;eta_right=s.Poly(1-step.as_expr(),u)
assert (eta_left+eta_right)==s.Poly(1,u)
# Even x cutoff: 1 through |x|<=1, 1-step(|x|-1) on 1..2, 0 outside.
cutbounds=[s.Integer(1)]+[l1(step.diff((u,k)))for k in range(1,11)]
a1=s.Rational(1,10);eta_star=s.Rational(1,100)
rows=[]
for n in [5,7,9,11]:
 for j in range(0,5):
  # q_ref control weight 1/(1+y^2), exact minimum on the closed cell.
  mj=s.Rational(1,1+max((j-1)**2,(j+1)**2))
  tau=eta_star*s.Rational(1,2**abs(j))*mj;target=s.Rational(1,2**n)*tau
  amplitude=s.Integer(10)**(20*n)
  pieces=[]
  for left,eta in [(j-1,eta_left),(j,eta_right)]:
   # d_n(y)=A*(y-1)_+^12: zero on the full central interval, C^11.
   dn=s.Poly(amplitude*(u+left-1)**12,u)if left>=1 else s.Poly(0,u)
   pieces.append((left,eta*dn))
   assert eta_left*dn+eta_right*dn==dn
  ybounds=[max(l1(p.diff((u,b)))for _,p in pieces)for b in range(n)]
  estimates=[]
  for a in range(n):
   Xbound=sum(s.Integer(comb(a,i))*s.Rational(factorial(n),factorial(n-i))*2**(n-i)*cutbounds[a-i]for i in range(a+1))
   for b in range(n-a):estimates.append((a,b,Xbound*ybounds[b]))
  B=max(z[2]for z in estimates)
  eps=min(s.Integer(1),a1/2,target/(1+B))
  assert eps>0
  bound=max(c*eps**(n-a)for a,b,c in estimates)
  assert bound<=target
  rows.append({'n':n,'j':j,'amplitude':str(amplitude),'weight_minimum':str(mj),'tau':str(tau),'target':str(target),
   'epsilon':str(eps),'bound':str(bound),'largest_derivative_order':n-1,
   'pieces':[{'left':left,'eta_times_dn':serial(p)}for left,p in pieces],
   'product_rule_constants':[{'dx':a,'dy':b,'constant':str(c)}for a,b,c in estimates]})
 # Uncut local correction has the exact prescribed x jet, no g1/g3 changes.
 D=s.Function('D')(y)
 local=x**n*D
 assert all(s.diff(local,x,k).subs(x,0)==0 for k in range(n))
 assert s.diff(local,x,n).subs(x,0)==factorial(n)*D
 lap=s.diff(local,x,2)+s.diff(local,y,2)
 assert s.expand(lap/x-(n*(n-1)*x**(n-3)*D+x**(n-1)*s.diff(D,y,2)))==0
certificate={'k':K,'scope':'exact finite C^11 piecewise polynomial controls only; C-infinity existence is the informal proof',
 'step':serial(step),'a1':str(a1),'eta_star':str(eta_star),'rows':rows}
path=root/'weighted_localization_certificate.json';path.write_text(json.dumps(certificate,indent=2)+'\n')
# Reload exact data and recompute every bound rather than trusting serialized claims.
loaded=json.loads(path.read_text());assert deserialize(loaded['step'])==step
for r in loaded['rows']:
 n=r['n'];eps=s.Rational(r['epsilon']);target=s.Rational(r['target']);outbound=s.Integer(0)
 ps=[deserialize(z['eta_times_dn'])for z in r['pieces']]
 for a in range(n):
  xb=sum(s.Integer(comb(a,i))*s.Rational(factorial(n),factorial(n-i))*2**(n-i)*cutbounds[a-i]for i in range(a+1))
  for b in range(n-a):
   c=xb*max(l1(p.diff((u,b)))for p in ps)
   outbound=max(outbound,c*eps**(n-a))
 assert outbound==s.Rational(r['bound']) and outbound<=target
out={'started_utc':started_utc,
 'ended_utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','elapsed_seconds':monotonic()-t0,
 'cells':len(rows),'degrees':[5,7,9,11],'all_exact_product_rule_bounds':True,
 'partition_identity_exact':True,'zero_central_interval':True,'jet_and_laplacian_identities_exact':True,
 'maximum_amplitude_decimal_exponent':220,
 'certificate':str(path),'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':certificate['scope']}
(root/'weighted_localization_tests.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)

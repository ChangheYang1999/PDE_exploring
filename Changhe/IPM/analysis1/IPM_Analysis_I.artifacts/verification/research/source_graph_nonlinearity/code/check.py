from common import *
from fractions import Fraction as F
from math import factorial
from collections import defaultdict
import copy
import sympy as sp
from flint import fmpq

def add(A,C):
 out=defaultdict(F,A)
 for ij,v in C.items():out[ij]+=v
 return {ij:v for ij,v in out.items() if v}
def mul(A,C):
 out=defaultdict(F)
 for (i,j),v in A.items():
  for (k,l),w in C.items():out[i+k,j+l]+=v*w
 return {ij:v for ij,v in out.items() if v}
def deriv(A,axis):
 out={}
 for ij,v in A.items():
  if ij[axis]:
   pos=list(ij);pos[axis]-=1;out[tuple(pos)]=v*ij[axis]
 return out
def qderiv(A,m,axis):
 rr={(2,0):F(1),(0,2):F(1)};v={(1,0) if axis==0 else (0,1):F(-2*m)}
 return add(mul(deriv(A,axis),rr),mul(A,v)),m+1
def decode(rows):return {tuple(x['powers']):F(x['coefficient']) for x in rows}
def qsym(A):return sum(sp.Rational(v.numerator,v.denominator)*x**i*y**j for (i,j),v in A.items())
def moment(i,j):
 if i%2 or j%2:return F(0)
 i//=2;j//=2
 return F(factorial(2*i)*factorial(2*j),4**(i+j)*factorial(i)*factorial(j)*factorial(i+j+1))*F(1,2)**(2*i+2*j+2)
def fm(v):return fmpq(v.numerator,v.denominator)
cache={}
def altmoment(i,j):
 if i%2 or j%2:return fmpq(0)
 i//=2;j//=2
 if (i,j) not in cache:
  z=fmpq(1)
  for u in range(1,i+1):z*=fmpq(2*u-1,2*u+2)
  for u in range(1,j+1):z*=fmpq(2*u-1,2*(i+u+1))
  cache[i,j]=z/fmpq(2)**(2*i+2*j+2)
 return cache[i,j]

if __name__=='__main__':
 start=now();pins,parents,pr=base();counts={};x,y,t,p,e,a=sp.symbols('x y t p e a',nonzero=True);rr=x*x+y*y
 numerators=[{(1,1):F(1)},{(3,1):F(1),(1,3):F(-1)}];powers=[2,4];wanted=[-3/t**4,-5/t**6];weights=[F(-1,2016),F(-1,3360)];axis=[];ncoef=0
 for A,m,target in zip(numerators,powers,wanted):
  symbolic=sp.cancel(sp.diff(qsym(A)/rr**m,x,y).subs({x:t,y:0}));need(sp.cancel(symbolic-target)==0,'fresh symbolic axis identity')
  M,q=qderiv(A,m,0);M,q=qderiv(M,q,1);ncoef+=len(M)
  need(sp.cancel(sp.diff(qsym(A)/rr**m,x,y)-qsym(M)/rr**q)==0,'all full quotient numerator coefficients agree')
  independent=sum(sp.Rational(v.numerator,v.denominator)*t**i for (i,j),v in M.items() if j==0)/t**(2*q)
  need(sp.cancel(independent-target)==0,'fraction quotient-rule full axis identity');axis.append({'numerator':{str(k):str(v) for k,v in sorted(M.items())},'denominator_power':q,'axis':str(symbolic)})
 counts.update(symbolic_axis_derivatives=2,quotient_axis_derivatives=2,all_axis_polynomial_coefficients=ncoef)
 unit=sum(sp.Rational(w.numerator,w.denominator)*z for w,z in zip(weights,wanted));sigma=2*a/e*unit.subs(t,p/e);expected=a*(e**3/p**4+e**5/p**6)/336;need(sp.cancel(sigma-expected)==0,'exact two-packet scale and strain')
 counts['two_packet_scale_identity']=1
 bracket=load(B/parents['89']['path'])['source_bracket'];lo,hi=map(F,bracket);need(F(4)<lo<hi,'certified bracket p>4');counts['bracket_order_inequalities']=2
 cases=[]
 for nv in [2,3,7,100]:
  ev=F(1,nv*nv);av=F(1,nv)
  for pv in [F(5),lo,hi]:
   direct=sum(av/ev*(F(1,672)*(F(sign)*pv/ev)**-4+F(1,672)*(F(sign)*pv/ev)**-6) for sign in [-1,1])
   explicit=av/F(336)*(ev**3/pv**4+ev**5/pv**6);need(direct==explicit and direct>0,'two signed rational translated packets')
   cases.append({'n':nv,'p_test_value':str(pv),'sigma':str(explicit)})
 counts['rational_translated_cases']=len(cases)
 need(F(-56,3)*(F(1,56)-F(4,56))==1,'Sigma g');need(F(-56,3)*(1-1)==0,'J g');need(F(-56,3)*(-6+F(6,4))==84,'g leading radial coefficient');counts['normalization_identities']=3
 saved=load(B/'research/nonlinear_x_obstruction/evidence/compute.json');other=load(B/'research/nonlinear_x_obstruction/evidence/independent.json');Q=decode(saved['cartesian']['Q_H']);dx=decode(saved['cartesian']['Q_x']);dy=decode(saved['cartesian']['Q_y']);need(deriv(Q,0)==dx and deriv(Q,1)==dy,'all inherited gradient coefficients rederived');need(Q[(2,1)]==F(-1,56),'nonzero cubic coefficient')
 counts['inherited_gradient_coefficients']=len(dx)+len(dy)
 energy_poly=add(mul(dx,dx),mul(dy,dy));even={ij:z for ij,z in energy_poly.items() if ij[0]%2==0 and ij[1]%2==0};energy=sum(v*moment(*ij) for ij,v in even.items());need(energy>0,'strict exact energy positive')
 alt=fmpq(0);pairs=0
 for A in [dx,dy]:
  for (i,j),v in A.items():
   for (k,l),z in A.items():alt+=fm(v)*fm(z)*altmoment(i+k,j+l);pairs+=1
 need(alt==fm(energy) and energy==F(saved['gradient_energy_over_pi'])==F(other['gradient_energy_over_pi']),'two fresh exact energy sums agree with accepted identity')
 counts.update(fresh_aggregate_energy_terms=len(even),fresh_unaggregated_energy_pairs=pairs)
 alpha,k=sp.symbols('alpha k');powers_out=[sp.expand(2*(2+alpha)-6+1),sp.expand(2*k-2*k-3+1),sp.expand(2*(k-4)-2*k-3+1),2*(-4)+1,2*5-6+1];need(powers_out==[2*alpha-1,-2,-10,-7,5],'all squared radial integrability powers');counts['integrability_identities']=5
 guards=reject=0
 for label,z in load(D/'parents.json').items():
  v=load(B/z['path']);parent_gate(v,z);guards+=1
  for field in ['status','files']:
   bad=copy.deepcopy(v)
   if field=='status':bad[field]='OPEN'
   else:bad[field].pop(next(iter(bad[field])))
   try:parent_gate(bad,z)
   except ValueError:reject+=1
   else:raise ValueError('malformed parent accepted')
   guards+=1
 counts.update(parent_guard_cases=guards,parent_guard_rejections=reject)
 need(counts==EXPECTED_COUNTS,'all expected concrete counts '+str(counts))
 rehash(pins)
 out={'start_utc':start,'utc':now(),'status':'PASS_SOURCE_GRAPH_NONLINEARITY_FINITE_CHECKS_REQUIRES_ACTUAL_REVIEW','counts':counts,'parents':parents,'proof_review':pr,'source_bracket':bracket,'axis_quotient_derivatives':axis,'unit_axis_strain':'(t^-4+t^-6)/672','two_packet_strain':'a*(epsilon^3/p^4+epsilon^5/p^6)/336','translated_rational_test_cases':cases,'energy_over_pi':str(energy),'radial_squared_integrand_exponents':[str(v) for v in powers_out],'files':dict(sorted(pins.items())),'scope':'Only the specified weak X graph norm at a noncentral equilibrium. All global estimates are analytic; no numerical value of the graph constant is claimed. The exact canonical trial application reuses accepted source and regularity results. No stronger SPEC norm, inverse or PDE endpoint.'}
 write(E/'checks.json',out);print(json.dumps({k:out[k] for k in ['start_utc','utc','status','counts']}),flush=True)

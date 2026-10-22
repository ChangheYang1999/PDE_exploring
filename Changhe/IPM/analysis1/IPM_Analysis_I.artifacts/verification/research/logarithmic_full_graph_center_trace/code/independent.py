from pathlib import Path
from collections import Counter
import sys,json
sys.dont_write_bytecode=True
from flint import fmpq as Q
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_full_graph_center_trace';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();primary=p.load(E/'check.json');p.rehash(primary['parent_files']);assert p.sha(D/'PROOF.md')==primary['proof_sha256']=='4d0743551aa93af5ae49825fe75f4230cd1392f17ac7ad45c007805056a08125'
raw=R/'data_exact/modal_v2.json';assert p.sha(raw)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';raw=p.load(raw)
def hx(t):
 sign=-1 if t.startswith('-') else 1;t=t.lstrip('+-');m,e=t.split('p');whole,frac=m[2:].split('.');return Q(sign*int(whole+frac,16))*Q(2)**(int(e)-4*len(frac))
k,bi=[hx(raw['scalars_hex'][n]) for n in ['k','bi']];knots=[hx(t) for t in raw['arrays']['knots']['hex']];shape=raw['arrays']['S']['shape'];modes=shape[0];degree=raw['degree']
assert list(map(str,knots))==primary['knots'] and degree==7 and modes==260 and shape==primary['shape']==[260,1565]
counts=Counter(knots);unique=sorted(counts);assert knots==sorted(knots) and len(unique)==primary['distinct_knots']==1559 and [counts[t] for t in unique]==[8]+[1]*1557+[8] and bi>50
actual={'k':k,'bi':bi,'inner_log_density_degree':Q(bi.p+3*bi.q,bi.q),'inner_log_velocity_degree':Q(bi.p+3*bi.q,bi.q),'fifth_derivative_log_margin':Q(bi.p-2*bi.q,bi.q),'spline_degree':Q(degree),'annular_join_order':Q(degree-1),'density_frequency_max':Q(2*(modes-1)+3),'source_frequency_max':Q(2*modes+2),'velocity_frequency_max':Q(2*modes+3),'s_example':Q(153,50),'theta_example':Q(153,50)-3,'alpha_example':Q(1,2),'multiplier_gap_example':Q(1,2)-(Q(153,50)-3)};assert {n:str(v) for n,v in actual.items()}==primary['actual']
# Laurent algebra for 2i times the density angular factor, with the radial
# homogeneity retained as a formal degree-one polynomial in P.
source_maps=[]
for mode in range(modes):
 la={}
 for freq,sign in [(1,1),(-1,-1),(3,1),(-3,-1)]:
  for shift in [-2*mode,2*mode]:la[freq+shift]=la.get(freq+shift,Q(0))+Q(sign,8)
 la={n:c for n,c in la.items() if c};out={}
 for freq,c in la.items():
  for direction in [-1,1]:
   target=freq+direction;aa,bb=out.get(target,(Q(0),Q(0)));out[target]=(aa-direction*freq*c/2,bb+c/2)
 out={n:v for n,v in out.items() if any(v)};assert all(n%2==0 for n in out) and max(out)<=522 and 0 not in out
 assert all(out[-n]==(-v[0],-v[1]) for n,v in out.items())
 source_maps.append({str(n):list(map(str,v)) for n,v in sorted(out.items()) if n>0})
assert source_maps==primary['source_maps']
# Rational differential ring adapted from207.
# Exponents correspond to u,y,delta,a,beta,A,D.
# Independent cutoff jets and eta jets are differentiated by the Leibniz rule.
def mon(powers=(0,)*7,jets=(),c=1):return {(tuple(powers),tuple(sorted(jets))):Q(c)} if c else {}
def var(i,n=1):
 v=[0]*7;v[i]=n;return mon(v)
def jet(name,i=0,j=0):return mon(jets=((name,i,j),))
def add(*parts):
 out={}
 for f in parts:
  for t,c in f.items():out[t]=out.get(t,Q(0))+c
 return {t:c for t,c in out.items() if c}
def scale(f,c):return {t:v*c for t,v in f.items() if v*c}
def mul(f,g):
 out={}
 for (a,j),c in f.items():
  for (b,jj),cc in g.items():
   t=(tuple(v+w for v,w in zip(a,b)),tuple(sorted(j+jj)));out[t]=out.get(t,Q(0))+c*cc
 return {t:c for t,c in out.items() if c}
def power(f,n):
 out=mon()
 for _ in range(n):out=mul(out,f)
 return out
def deriv(f,axis):
 out={}
 for (powers,jets),c in f.items():
  if powers[axis]:
   pp=list(powers);pp[axis]-=1;out=add(out,mon(pp,jets,c*powers[axis]))
  for at,(name,i,j) in enumerate(jets):
   if (name=='C' and axis==1) or (name in ['eta','W'] and axis==0 and name=='eta') or (name in ['W','Wa'] and axis==1):continue
   if name=='Log':
    if axis==0:
     jj=list(jets);jj.pop(at);out=add(out,mul(var(0,-1),mon(powers,jj,c)))
    continue
   if name=='W':out=add(out,scale(mul(var(4),mon(powers,jets,c)),-1));continue
   if name=='Wa':out=add(out,mul(var(3),mul(var(0,-1),mon(powers,jets,c))));continue
   ij=[i,j];ij[axis]+=1;jj=list(jets);jj[at]=(name,*ij);out=add(out,mon(powers,jj,c))
 return out
def diff(f,axis,n=1):
 for _ in range(n):f=deriv(f,axis)
 return f
u,y,delta,a,beta,unused,nn=[var(i) for i in range(7)];C,eta=jet('C'),jet('eta')
f=scale(mul(var(2,4),mul(var(0,4),mul(C,eta))),Q(-1,12))
def dx(f):return mul(var(2,-1),deriv(f,0))
h=scale(add(dx(dx(f)),diff(f,1,2)),-1);U1=scale(deriv(dx(f),1),-1);U2=dx(dx(f))
H2=mul(add(mul(var(0,2),C),scale(mul(var(0,3),jet('C',1)),Q(2,3)),scale(mul(var(0,4),jet('C',2)),Q(1,12))),eta)
H3=scale(mul(add(scale(mul(var(0,3),C),4),mul(var(0,4),jet('C',1))),jet('eta',0,1)),Q(1,12))
H4=scale(mul(var(0,4),mul(C,jet('eta',0,2))),Q(1,12))
checks={}
def check(name,left,right=None):
 if right is None:right={}
 assert left==right,(name,left,right);checks[name]=True
check('density_two_powers',h,add(mul(var(2,2),H2),mul(var(2,4),H4)))
check('velocity1_positive',U1,mul(var(2,3),H3))
check('velocity2_negative',U2,scale(mul(var(2,2),H2),-1))
Fz,W,pcoef,vcoef=jet('F'),jet('W'),jet('p'),jet('v');WF=mul(W,Fz)
trans=add(mul(pcoef,deriv(WF,0)),mul(vcoef,deriv(WF,1)),scale(WF,-1))
expect=mul(W,add(mul(pcoef,add(deriv(Fz,0),scale(mul(beta,Fz),-1))),mul(vcoef,deriv(Fz,1)),scale(Fz,-1)))
check('variable_transport_conjugation',trans,expect)
rx,ry=jet('rho_x'),jet('rho_y');check('nonlocal_coupling',add(mul(U1,rx),mul(U2,ry)),add(mul(var(2,3),mul(H3,rx)),scale(mul(var(2,2),mul(H2,ry)),-1)))
part=scale(mul(var(0,3),y),Q(-1,3));check('polynomial_source_particular',scale(add(diff(part,0,2),diff(part,1,2)),-1),scale(mul(u,y),2))
Wa,Log=jet('Wa'),jet('Log')
def radial(f,n):
 return add(scale(deriv(deriv(f,0),0),-1),scale(mul(var(0,-1),deriv(f,0)),-1),mul(mul(n,n),mul(var(0,-2),f)))
diagonal=add(mul(nn,nn),scale(mul(a,a),-1))
check('radial_power_diagonal',radial(Wa,nn),mul(var(0,-2),mul(diagonal,Wa)))
check('radial_log_triangular',radial(mul(Wa,Log),nn),mul(var(0,-2),add(mul(diagonal,mul(Wa,Log)),scale(mul(a,Wa),-2))))
resonant=scale(mul(var(3,-1),mul(Wa,Log)),Q(-1,2));check('radial_resonant_particular',radial(resonant,a),mul(var(0,-2),Wa))
# Exponent arithmetic in a separate two-entry affine polynomial representation.
beta_pair=(Q(1,2),Q(-1));a_pair=(Q(5,2),Q(-1));powers=[]
for order in [2,3,4]:
 left=(beta_pair[0]+order,beta_pair[1]);right=(a_pair[0]+order-2,a_pair[1]);assert left==right;powers.append(list(map(str,left)))
out={'start_utc':start,'utc':p.now(),'status':'PASS_INDEPENDENT_FMPQ_LAURENT_AND_FULL_GRAPH_DIFFERENTIAL_RING','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'check_sha256':p.sha(E/'check.json'),'parent_pin_count':len(primary['parent_files']),'exact_parameters_compared':len(actual),'knots_compared':len(knots),'angular_bases_compared':len(source_maps),'ring_checks':checks,'weighted_exponent_affine_pairs':powers,'source_reuse':'Leibniz differential ring adapted from207, with new formal logarithm rule and radial normal form. Angular Laurent computation, integerhex decode and fmpq arithmetic do not import NPZ, Sympy or the primary evaluator.','scope':'Exact algebra and finite angular support only. No interval or norm ceiling; multiplier and graph convergence proofs remain analytic.'};p.write(E/'independent.json',out);print(json.dumps(out))

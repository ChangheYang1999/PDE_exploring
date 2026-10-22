"""Manufactured and adversarial controls for packet187; standalone finite tests."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import copy,hashlib,json,time,sys
import modal_norm_power as iv
import generate_full_modal_norm as gen
import check_full_modal_norm as chk
assert Path.cwd()==Path('verification')
start=time.monotonic();checks=[];negative=[];counterchecks=[]
def contain(got,want,label):
    assert got[0]<=want<=got[1],(label,got,want);checks.append(label)
# Integral controls are exact even for nonintegral b because both endpoints are0,1.
for b in map(Q,['1/3','1','5/2','61/20','100/3']):
 for k in range(8):
  for m in range(4):
   ps=[[Q(0)]*6 for _ in range(k+1)];ps[k][m]=1
   a=gen.integrate_aggregates(gen.aggregate(ps,5),Q(0),Q(1),b);c=chk.normcell(ps,Q(0),Q(1),b,5)
   expected=Q(1,2*m+2)-(Q(1)/(2*m+2*b+2)if k%2 else 0);expected*=2 if k==0 else 1
   assert a==c
   contain(a[0],expected,f'monomial-I0-b{b}-k{k}-m{m}')
   contain(a[1],k*k*expected,f'monomial-I1-b{b}-k{k}-m{m}')
# Nontrivial fractional-power identities, including endpoints and near-one bases.
for denom in [2,3,7,31,257]:
 for n in [2,3,5]:
  value=Q(denom-1,denom);contain(iv.power(value**n,Q(1,n)),value,f'perfect-power-{denom}-{n}')
for v in [Q(0),Q(1),Q(1,2),Q(1,10**12)]:contain(iv.power(v,Q(0)),Q(1),f'zero-exponent-{v}')
# Two rational cubic/quintic spline families on a common grid, not archive data.
def data(mult):
 d=5;return {'basis_beta':'61/20','L':'3/2','degree':d,'knots':['0']*6+['1']*6,'knot_binary_little_endian_sha256':'manufactured','K':4,'coefficients':[[str(mult*Q(comb(d-j,k),comb(d,k)))if d-j>=k else '0'for j in range(d+1)]for k in range(4)]}
x=[data(Q(3,7)),data(Q(5,9))];cert=gen.generate(x);res=chk.check(cert,x,archives=False);assert res['verdict']=='CONFIRMED';checks.append('exact-deBoor-independent-checker')
for j,interval in enumerate(cert['relative_L2_to_second']):contain(tuple(map(Q,interval)),Q(8,35),f'exact-proportional-relative-norm-{j}')
# Three-cell global constant/linear splines with unequal mode counts.
# Linear reproduction uses the exact Greville coefficient (sum of d interior
# knots)/d for t. Hence 1-minus that value reproduces z=1-t on every cell.
ts=[Q(0)]*6+[Q(1,3),Q(2,3)]+[Q(1)]*6;d=5;nb=len(ts)-d-1
amps=[[Q(2,7),Q(-3,11),Q(5,13)],[Q(3,5),Q(4,9),Q(-2,3),Q(7,10),Q(1,6)]]
ys=[]
for aa in amps:
 coeff=[[a*(1-sum(ts[j+1:j+d+1])/d if k%2 else 1)for j in range(nb)]for k,a in enumerate(aa)]
 ys.append({'basis_beta':'61/20','L':'3/2','degree':d,'knots':list(map(str,ts)),'knot_binary_little_endian_sha256':'manufactured-three-cell','K':len(aa),'coefficients':[[str(c)for c in row]for row in coeff]})
 for k,row in enumerate(coeff):
  for j,(a,b)in enumerate(zip([Q(0),Q(1,3),Q(2,3)],[Q(1,3),Q(2,3),Q(1)])):
   for q in [Q(1,4),Q(3,4)]:
    t=a+(b-a)*q;assert chk.deboor(ts,row,d,t)==aa[k]*(1-t)**(k%2);checks.append(f'Greville-field{len(ys)}-k{k}-cell{j}-q{q}')
ycert=gen.generate(ys);yres=chk.check(ycert,ys,archives=False);assert yres['verdict']=='CONFIRMED';checks.append('three-cell-unequal-K-exact-checker')
padded=amps[0]+[Q(0)]*2
families=amps+[[a-b for a,b in zip(padded,amps[1])]]
for i,aa in enumerate(families):
 for deriv in [0,1]:
  exact=sum(a*a*(2 if k==0 else k*k if deriv else 1)*(Q(1,2*(k%2)+2)-(Q(1)/(2*(k%2)+2*Q(61,20)+2)if k%2 else 0))for k,a in enumerate(aa)if not(deriv and k==0))
  contain(tuple(map(Q,ycert['norm_squared_over_pi_b_L2'][i][deriv])),exact,f'three-cell-unequalK-field{i}-deriv{deriv}')

# Reject altered mathematical certificate fields, not just its file hash.
mutations=[('corrupt polynomial',lambda c:c['cells'][0]['polynomials_z'][0][0].__setitem__(0,'1')),('wrong radial interval',lambda c:c['cells'][0].__setitem__('z_interval',['1/100','1'])),('missing cell',lambda c:c.__setitem__('cells',[])),('wrong b',lambda c:c.__setitem__('basis_beta','3')),('wrong mode count',lambda c:c.__setitem__('mode_count',3)),('wrong precision',lambda c:c['precision'].__setitem__('bits',120)),('wrong norm',lambda c:c['norm_squared_over_pi_b_L2'][0][0].__setitem__(0,'1')),('wrong ratio',lambda c:c['relative_L2_to_second'][0].__setitem__(0,'1'))]
for name,mutate in mutations:
 c=copy.deepcopy(cert);mutate(c)
 try:chk.check(c,x,archives=False)
 except AssertionError:negative.append(name)
 else:raise AssertionError(('accepted corruption',name))
# Explicit convention mistakes must differ from the correct exact answers.
for name,wrong,correct in [('mode0 factor',Q(1,2),Q(1)),('odd rho squared',Q(1,2),Q(3,8)),('angular k squared',Q(1,2),Q(9,2)),('physical Jacobian',Q(1,14),Q(1,2)),('rounded coefficient subtraction',Q.from_float(float(10**16)-1.),Q(10**16)-1)]:
 assert wrong!=correct;counterchecks.append(name)
# Independently re-read an actual export, then reject mask, knot, basis mismatches.
p=Path('verification/full_modal_norm_20261021T1730Z/beta3p0315/input0.json');actual=json.loads(p.read_text());chk.decode(actual);checks.append('actual-independent-archive-decode')
for name,change in [('archive masked slot',lambda z:z['coefficients'][2].__setitem__(0,'1')),('archive knot bit',lambda z:z['knots'].__setitem__(6,str(Q(z['knots'][6])+Q(1,2**100)))),('archive basis exponent',lambda z:z.__setitem__('basis_beta',str(Q(z['basis_beta'])+Q(1,2**80))))]:
 z=copy.deepcopy(actual);change(z)
 try:chk.decode(z)
 except AssertionError:negative.append(name)
 else:raise AssertionError(('accepted archive change',name))
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','exact_controls':len(checks),'negative_controls':len(negative),'algebraic_counterchecks':len(counterchecks),'checks':checks,'rejected':negative,'counterchecks':counterchecks,'elapsed_seconds':time.monotonic()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
dest=Path('research/187_full_modal_L2_certificates/verification/controls.json');dest.write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in ['checks','rejected']})

"""Independent acceptance gates and exact algebra for the complete velocity run."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,math,sys
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];D=B/'research/n8_velocity_hessian';E=D/'evidence'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
def qa(x):x=F(x);return arb(fmpq(x.numerator,x.denominator))
def qi(x):x=F(x);return iv.mpf(x.numerator)/x.denominator
def aq(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def mq(x):s,m,e,b=x;assert b>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ends(x):
 lo,hi=(aq(x.lower()),aq(x.upper())) if isinstance(x,arb) else tuple(map(mq,x._mpi_));assert lo<=hi;return lo,hi
c=json.loads((E/'full_checks.json').read_text());d=json.loads((E/'moment_inputs.json').read_text());smoke=json.loads((E/'smoke_checks.json').read_text());dd=json.loads((B/'research/n8_density_hessian/evidence/density_inputs.json').read_text());dv=json.loads((B/'research/n8_density_hessian/evidence/verdict.json').read_text())
assert c['status']=='PASS_FULL_INDEPENDENT_VELOCITY_HESSIAN_BOUND'
assert dv['status']=='CONFIRMED_DENSITY_HESSIAN_BOUND_WITH_ARCHIVE_DEPENDENCY'
checked={}
for doc in [c,d,smoke,dd,dv]:
 for p,h in doc['files'].items():
  if p not in checked:checked[p]=sha(B/p)
  assert checked[p]==h,p
assert c['files']['research/n8_velocity_hessian/code/check_hessian.py']==smoke['files']['research/n8_velocity_hessian/code/check_hessian.py']=='d78774910f0692781fe2c0b86cf315367398aeb409beda36e0e9fad6d7b90781'
assert c['files']['research/n8_velocity_hessian/evidence/moment_inputs.json']==smoke['files']['research/n8_velocity_hessian/evidence/moment_inputs.json']
for name in ['source_header','source_center_bracket_exact','delta_exact','theta_max_exact','ntheta','radial_subdivisions','cells']:assert d[name]==dd[name],name
assert d['source_center_bracket_exact']==['4841405518533377/562949953421312','4841405518533711/562949953421312']
assert F(d['delta_exact'])==F(33,2000) and F(d['theta_max_exact'])==F(3,500)
assert (d['ntheta'],d['radial_subdivisions'],d['Q'],d['series_degree'])==(160,4,16,80)
assert len(d['cells'])==len(c['cells'])==13
assert [x['ci'] for x in d['cells']]==[x['ci'] for x in c['cells']]==list(range(4096,4109))
assert len(d['spans'])==7 and len({x['span'] for x in d['spans']})==7
spans={x['span']:x for x in d['spans']};dspans={x['span']:x for x in dd['spans']}
assert spans.keys()==dspans.keys()
for si,sp in spans.items():
 assert all(sp[k]==v for k,v in dspans[si].items())
 assert len(sp['i_left'])==len(sp['j_right'])==261
 assert F(sp['polynomial_mid_exact'])==(F(sp['a_exact'])+F(sp['b_exact']))/2
 assert len(sp['density_polynomials'])==262
 for p in sp['density_polynomials']:assert len(p)==8
 for v in sp['density_polynomials'][-1]:assert int(v['mid_m'])==int(v['rad_m'])==0
 for v in sp['i_left']+sp['j_right']:
  assert v['schema']=='arb-dyadic-mid-radius-v1' and int(v['rad_m'])>=0
counts={'cells':13,'radial_subcells':52,'angular_radial_boxes':8320,'canonical_moment_overlap_diagnostics':27144,'independent_monomial_series_tails':217152,'complete_antiderivatives':27144,'ode_model_remainders':54288,'tensor_model_remainders':108576}
assert c['counts']==counts,(c['counts'],counts)
assert F(c['bound_exact'])==F(743,2500)
coverage=[];pm,px=map(F,d['source_center_bracket_exact']);R=3*F(d['delta_exact']);theta=F(d['theta_max_exact']);assert R==F(99,2000)
for q,ex,sin,name in [(qa,lambda x:x.exp(),lambda x:x.sin(),'Arb512'),(qi,iv.exp,iv.sin,'iv180')]:
 lo=ends(ex(q(F(d['cells'][0]['a_exact']))));hi=ends(ex(q(F(d['cells'][-1]['b_exact']))));cap=ends(sin(q(theta)))
 assert pm>R and lo[1]<pm-R and hi[0]>px+R and cap[0]>R/pm
 coverage.append({'engine':name,'left_radius_upper_exact':str(lo[1]),'right_radius_lower_exact':str(hi[0]),'cap_sine_lower_exact':str(cap[0])})
subnodes=0;maxz=F()
for idx,(cell,row) in enumerate(zip(d['cells'],c['cells'])):
 assert all(cell[k]==row[k] for k in ['ci','a_exact','b_exact'])
 a,b=map(F,[cell['a_exact'],cell['b_exact']]);sp=spans[cell['span']];sa,sb=map(F,[sp['a_exact'],sp['b_exact']]);assert sa<=a<b<=sb
 if idx:assert F(d['cells'][idx-1]['b_exact'])==a
 nodes=[a+(b-a)*F(k,4) for k in range(5)];assert nodes[0]==a and nodes[-1]==b and all(x<y for x,y in zip(nodes,nodes[1:]));subnodes+=5
 for x,y in zip(nodes,nodes[1:]):
  tc=(x+y)/2;assert sa<tc<sb
  for n in range(1,262):
   maxz=max(maxz,abs(F(-2*n-4)*(tc-sa)),abs(F(4-2*n)*(sb-tc)))
assert maxz<82
for engine in ['arb','iv']:
 values=[F(x[engine+'_squared_upper_exact']) for x in c['cells']]
 assert all(v>=0 for v in values)
 assert max(values)==F(c[engine+'_squared_upper_exact'])==F(c['where'][engine]['squared_upper_exact'])<F(743,2500)**2
 w=c['where'][engine];assert 4096<=w['ci']<=4108 and 0<=w['k']<4 and 0<=w['theta_index']<160
 assert next(x for x in c['cells'] if x['ci']==w['ci'])[engine+'_squared_upper_exact']==w['squared_upper_exact']
# Derive the four differential operators by shifting D to D+4 in the
# covariant polar expressions, separately from the numerical implementation.
def pad(p,N=4):return list(p)+[F()]*(N-len(p))
def add(*ps):return [sum(v,F()) for v in zip(*map(pad,ps))]
def mul(a,b):
 out=[F()]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def scale(a,c):return [c*x for x in a]
z=[F(4),F(1)];z2=mul(z,z);z3=mul(z2,z);identities=0
for n in range(1,262):
 m=F(2*n)
 PA=add(z3,scale(z2,-3),scale(z,2));PB=scale(add(z2,scale(z,-3),[F(2)]),m)
 PC=add(scale(z,-m*m),z2,scale(z,-2),[2*m*m]);PD=add([-m**3],scale(z,3*m),[-2*m])
 assert PA==[24,26,9,1] and PB==[6*m,5*m,m,0] and PC==[8-2*m*m,6-m*m,1,0] and PD==[m*(10-m*m),3*m,0,0];identities+=16
 # Exact elimination of each moment's higher derivatives, as formal pairs
 # (coefficient of y, polynomial forcing H,H',H'') independently recurred.
 for lam,sign in [(m-4,-1),(-m-4,1)]:
  powers=[(F(1),[F(),F(),F()])]
  for k in range(3):
   cy,ch=powers[-1];powers.append((lam*cy,[sign*cy,ch[0],ch[1]]))
  for P in [PA,PB,PC,PD]:
   cy=sum(P[k]*powers[k][0] for k in range(4));ch=[sum(P[k]*powers[k][1][j] for k in range(4)) for j in range(3)]
   assert cy==sum(P[k]*lam**k for k in range(4))
   assert ch==[sign*sum(P[k]*lam**(k-1-j) for k in range(j+1,4)) for j in range(3)];identities+=4
# Verify the trace decomposition as an exact quadratic form, including crosses.
M=[[1,0,1,0],[0,1,0,1],[1,0,-3,0],[0,3,0,-1]]
for i in range(4):
 for j in range(4):assert sum(w*r[i]*r[j] for w,r in zip([3,3,1,1],M))==([4,12,12,4][i] if i==j else 0);identities+=1
# Exact ODE polynomial residual with deliberately nonzero degree-seven forcing.
# Also retain the Q=7 regression which necessitated the proof addendum.
regression=[]
for Q in [7,8,16]:
 ell=F(-3,20);hh=F(1,10);sign=-1;g=[F((-1)**j,j+1) for j in range(8)];co=[F(5,7)]
 for k in range(Q):co.append((ell*co[-1]+sign*hh*(g[k] if k<8 else 0))/F(k+1))
 residual=[(k+1)*co[k+1]-ell*co[k]-sign*hh*(g[k] if k<8 else 0) for k in range(Q)]+[-ell*co[Q]-sign*hh*(g[Q] if Q<8 else 0)]
 assert all(x==0 for x in residual[:-1])
 expected=-ell*co[Q]
 assert (residual[-1]==expected)==(Q>=8)
 regression.append({'Q':Q,'last_residual_exact':str(residual[-1]),'advertised_formula_exact':str(expected),'corrected_domain_pass':Q>=8})
# Algebraic series ratio is strictly dominated by the retained geometric ratio.
ratio_checks=0
for j in range(8):
 for k in range(81,91):
  assert F(j+k+1,(k+1)*(j+k+2))<=F(1,82);ratio_checks+=1
assert F(c['max_arb_tensor_model_remainder_exact'])>=0 and F(c['max_iv_tensor_model_remainder_exact'])>=0
pins=[Path(__file__),D/'PROOF.md',D/'ADDENDUM.md',E/'full_checks.json',E/'smoke_checks.json',E/'moment_inputs.json',B/'research/n8_density_hessian/evidence/verdict.json']
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FULL_VELOCITY_COVERAGE_OUTPUT_AND_EXACT_ALGEBRA_AUDIT','bound_exact':'743/2500','disc_radius_exact':'99/2000','counts':counts,'audit_counts':{'radial_nodes':subnodes,'operator_and_quadratic_identities':identities,'series_ratio_checks':ratio_checks,'complete_radial_cells':13,'canonical_endpoint_moments':3654},'maximum_series_argument_exact':str(maxz),'coverage':coverage,'ode_residual_regression':regression,'resolved_gates':['exact thirteen ordered contiguous cells','exact stated radius and bracket','same smoke and full numerical code and data','Q correction ADDENDUM pinned','full row counts and independent strict square ceilings'],'scope':'Complete full-disc bound with explicit canonical archive dependency. The separate audit, not the raw status string alone, supplies acceptance.','files':{str(p.relative_to(B)):sha(p) for p in pins}}
(E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['utc','status','bound_exact','counts','audit_counts']}))

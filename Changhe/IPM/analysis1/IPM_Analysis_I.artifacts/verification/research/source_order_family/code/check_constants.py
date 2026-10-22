"""Exact box vertices and two interval engines for topic92; no sampled proof."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys,itertools
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];D=B/'research/source_order_family';E=D/'evidence'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
def qa(x):x=F(x);return arb(fmpq(x.numerator,x.denominator))
def qi(x):x=F(x);return iv.mpf(x.numerator)/x.denominator
def ends(v):
 if isinstance(v,arb):
  assert v.is_finite()
  def cv(z):m,e=z.man_exp();return F(int(m))*F(2)**int(e)
  return cv(v.lower()),cv(v.upper())
 def cv(z):s,m,e,bc=z;assert bc>=0;return F((-1 if s else 1)*int(m))*F(2)**int(e)
 return tuple(map(cv,v._mpi_))
def rec(v):l,u=ends(v);return {'lower_exact':str(l),'upper_exact':str(u)}
files={};pins=0
deps=['source_local_estimate','source_semigroup','canonical_strain_sign','n8_coefficient_closure','source_instance']
for dep in deps:
 p=B/'research'/dep/'evidence/verdict.json';v=json.loads(p.read_text());assert v['status'].startswith('CONFIRMED')
 for rel,h in v['files'].items():assert sha(B/rel)==h,rel;pins+=1
 files[str(p.relative_to(B))]=sha(p)
for rel in ['research/source_order_family/PROOF.md',str(Path(__file__).relative_to(B))]:files[rel]=sha(B/rel)
sl,su=F(61,20),F(31,10);mv,mrho,delta=F(743,2500),F(5059,10000),F(33,2000)
def k(s):return F(1301,200)-F(101,100)*s
def fast(s):return F(7119,200)-F(51,5)*s
def cv(s):return (12*s+F(9,2))*mv+3*mrho
def a(s):return k(s)-delta*cv(s)
rows=[];vc=0;inequalities=0
# Multiaffine dependence attains extrema at vertices: these 16 vertices
# constitute the whole box-times-s-interval check, not a frequency sample.
for s in [sl,F(153,50),su]:
 slow=[];quick=[]
 for A,mu,g in itertools.product([F(10),F(51,5)],[F(99,100),F(101,100)],[F(29),F(30)]):
  slow.append(1+A/2+(F(1,2)-s)*mu);quick.append(1+(F(1,2)-s)*A+mu/2+g);vc+=1
 assert min(slow)==k(s) and min(quick)==fast(s) and fast(s)>k(s)>0
 coefficient=12*s+F(9,2);Eup=delta*cv(s);alow=a(s);db=F(101,100)*s-F(1,100);K=1/alow
 want=F('0.313753') if s==F(153,50) else F('0.3181')
 assert 0<Eup<k(s)/2 and alow>0 and K<want and db>=F(6141,2000)
 ev={}
 for engine,Q,pi in [('arb',qa,arb.pi()),('iv',qi,iv.pi)]:
  # Reconstruct from the pre-substitution cutoff formula, not cv(s).
  ss=Q(s);coeff=3*ss+Q(F(9,2))*(ss+Q(F(1,2)))*2
  C=coeff*Q(mv)+3*Q(mrho);ee=Q(delta)*C
  margin=1+Q(10)/2+(Q(F(1,2))-ss)*Q(F(101,100))
  vals={'coefficient':coeff,'C_upper':C,'E_upper':ee,'a_lower':margin-ee,'K_upper':1/(margin-ee),'d_lower':1+(Q(10)+Q(F(99,100)))/2-margin,'beta_s':1/(2*(pi*(ss-1)*(ss-2))**Q(F(1,2)))}
  exact={'coefficient':coefficient,'C_upper':cv(s),'E_upper':Eup,'a_lower':alow,'K_upper':K,'d_lower':db}
  for name,target in exact.items():lo,up=ends(vals[name]);assert lo<=target<=up;inequalities+=2
  assert ends(vals['K_upper'])[1]<want;inequalities+=1
  ev[engine]={name:rec(value) for name,value in vals.items()}
 rows.append({'s':str(s),'kappa':str(k(s)),'fast_box_minimum':str(fast(s)),'coefficient':str(coefficient),'C_upper':str(cv(s)),'E_upper':str(Eup),'a_lower':str(alow),'K_upper':str(K),'K_decimal_ceiling':str(want),'d_lower':str(db),'engines':ev})
# Exact affine slopes settle all real orders between the endpoints.
kslope=-F(101,100);cslope=12*mv;aslope=kslope-delta*cslope;gapslope=-F(919,100)
assert kslope<0<cslope and aslope<0 and gapslope<0
assert fast(su)-k(su)==F(601,1000)
assert a(su)==F(314446949,100000000)
assert 1/a(su)<F(3181,10000)
assert cv(F(153,50))==F(3442071,250000)<F(1377,100)
assert k(F(153,50))==F(2134,625)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SOURCE_ORDER_FAMILY_CONSTANTS','interval':[str(sl),str(su)],'rows':rows,'affine_slopes':{n:str(z) for n,z in [('kappa',kslope),('C',cslope),('a_lower',aslope),('fast_minus_slow',gapslope)]},'counts':{'dependency_file_pins':pins,'source_box_vertices_with_s':vc,'affine_endpoint_vertices_sufficient':16,'extra_order_vertices':8,'directed_interval_inequalities':inequalities},'scope':'Actual derivative and equilibrium bounds imported from frozen accepted dependencies. Exact multiaffine vertex reduction and affine slopes prove continuum parameter claims; no full IPM inverse. Beta is a separate numerical illustration.','files':files}
(E/'checks.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items() if k not in ['rows','files']}))

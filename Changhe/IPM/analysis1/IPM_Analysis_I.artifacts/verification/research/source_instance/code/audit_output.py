"""Fresh exact target/output audit and complete normalization/dependency linkage."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=1536;ctx.threads=1;iv.dps=250
B=Path(__file__).resolve().parents[3];D=B/'research/source_instance';E=D/'evidence'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
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
c=json.loads((E/'checks_v2.json').read_text());assert c['status']=='PASS_FRESH_SOURCE_AND_LOCAL_INSTANCE'
assert c['counts']=={'frozen_dependency_pins':440,'exact_simple_interior_knots':1557,'axis_mode_divergence_identities':261,'primitive_coefficient_identities':4168,'arb_monomial_tails':12528,'iv_complete_primitives':1044,'source_evaluations':6,'engine_endpoint_signs':4,'engine_whole_interval_bounds':6,'moment_overlap_diagnostics':1566,'whole_bracket_ode_variation_bounds':522}
files={};pins=0
for f,h in c['files'].items():assert sha(B/f)==h,f;pins+=1
assert json.loads((E/'proof_first.json').read_text())['proof_sha256']==sha(D/'PROOF.md')
rp=B/'research/modal_repair/evidence/audit_verdict.json';rv=json.loads(rp.read_text());assert rv['verdict']=='CONFIRMED' and rv['input_and_source_hashes_verified']
for f,h in rv['source_and_evidence_sha256'].items():assert sha(B/f)==h,f;pins+=1
m=json.loads((B/'research/n8_velocity_hessian/evidence/moment_inputs.json').read_text());header=m['source_header']
assert header['hashes']['normalization']==sha(B/'research/modal_repair/evidence/independent_gauss_iv.json')
assert header['hashes']['input']==sha(B/'data_exact/modal_v2.json')
assert m['source_center_bracket_exact']==c['source_bracket_exact'];assert F(m['delta_exact'])==F(c['delta_exact'])==F(33,2000)
a,b=map(F,c['source_bracket_exact']);assert a<b
checks=0;summ={}
for engine,o in c['outputs'].items():
 assert set(o)=={'a','b','whole'}
 for lab,row in o.items():
  assert set(row)=={'w','g','mu','wprime'}
  for val in row.values():assert F(val['lower_exact'])<=F(val['upper_exact']);checks+=1
 assert F(o['a']['w']['upper_exact'])<0<F(o['b']['w']['lower_exact']);checks+=2
 summ[engine]={}
 for name,lo,hi in [('g',F(29),F(30)),('mu',F(99,100),F(101,100)),('wprime',F(10),F(51,5))]:
  v=o['whole'][name];vl,vu=F(v['lower_exact']),F(v['upper_exact']);assert lo<=vl<=vu<=hi;checks+=1
  scale=10**10;floor=(vl*scale).numerator//(vl*scale).denominator;ceil=-((-vu*scale).numerator//(-vu*scale).denominator)
  assert F(floor,scale)<=vl<=vu<=F(ceil,scale)
  summ[engine][name]={'lower_exact':str(F(floor,scale)),'upper_exact':str(F(ceil,scale))}
 assert F(o['whole']['mu']['upper_exact'])<1;checks+=1
 # Recompute the radial interior and source span placement independently at higher precision.
for q,log in [(qa,lambda x:x.log()),(qi,iv.ln)]:
 sp=next(z for z in m['spans'] if z['span']==c['source_span'])
 assert F(sp['a_exact'])<ends(log(q(a)))[0]<=ends(log(q(b)))[1]<F(sp['b_exact']);checks+=1
cv=json.loads((B/'research/n8_coefficient_closure/evidence/verdict.json').read_text());assert cv['status']=='CONFIRMED_SOURCE_COEFFICIENT_SMALLNESS'
v=F(743,2500);r=F(5059,10000);delta=F(33,2000);kappa=F(1687,500);s=F(31,10)
cutoff_D=F(9,2)*2+3;cutoff_div=F(9,2)*2
assert cutoff_D==12 and cutoff_div==9 and cutoff_div/2+s*cutoff_D==F(417,10)
CV=F(417,10)*v+3*r;EU=delta*CV;assert EU==F(cv['exact']['E_upper'])==F(22953051,10**8)
assert 1+(F(10)+F(99,100))/2-kappa==F(c['auxiliary_d_lower_exact'])==F(3121,1000)
assert F(1)/(kappa-EU)==F(cv['exact']['K_1_upper'])<F(3181,10000)
for q in [qa,qi]:
 e=q(delta)*(q(F(9,2))*q(v)+q(s)*q(12)*q(v)+q(3)*q(r))
 assert ends(e)[1]<kappa/2
 inv=1/(q(kappa)-e);assert ends(inv)[1]<F(3181,10000);checks+=2
for p in [Path(__file__),E/'checks_v2.json',D/'PROOF.md',D/'ADDENDUM.md',D/'CLOSURE_NOTES.md',rp,B/'research/source_local_estimate/PROOF.md',B/'research/source_semigroup/PROOF.md',B/'research/n8_coefficient_closure/evidence/verdict.json']:files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SOURCE_INSTANCE_OUTPUT_AND_LINKAGE_AUDIT','counts':{'complete_result_and_normalization_pins':pins,'fresh_record_and_directed_checks':checks},'public_whole_bracket_enclosures':summ,'cutoff_D_constant':'12','cutoff_div_constant':'9','coefficient_MV_constant':'417/10','auxiliary_d_lower':'3121/1000','scope':'Fresh exact output-target, canonical-normalization and actual cutoff-coefficient linkage. No replacement of the two full primary engines and no global inverse.','files':files}
(E/'output_audit.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items() if k!='files'}))

"""Strict non-finite, numeric input-linkage and requested-scale closure."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from datetime import datetime,timezone
from functools import lru_cache
import hashlib,json,importlib.util,sys
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_integrated_inverse';E=D/'evidence';counts=Counter();files={}
@lru_cache(None)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for q in iter(lambda:f.read(1048576),b''):h.update(q)
 return h.hexdigest()
def read(f):
 p=B/f;files[f]=sha(str(p));return json.loads(p.read_text())
def pinall(v):
 for f,h in v['files'].items():assert sha(str(B/f))==h,f;counts['dependency_hash_comparisons']+=1
for name in ('source_explicit_inverse','source_dilation','source_instance','n8_coefficient_closure','n8_density_hessian','n8_velocity_hessian','source_order_family','source_semigroup'):
 v=read('research/'+name+'/evidence/verdict.json');assert v['status'].startswith('CONFIRMED');pinall(v)
c=read('research/n8_coefficient_closure/evidence/checks.json');pinall(c)
for key,value in [('M_V_upper','743/2500'),('M_rho_upper','5059/10000'),('delta','33/2000')]:assert F(c['exact'][key])==F(value);counts['explicit_low_constant_links']+=1
s=read('research/source_instance/evidence/checks_v2.json');pinall(s);assert F(s['delta_exact'])==F(33,2000);counts['explicit_low_constant_links']+=1
s=read('research/source_instance/evidence/output_audit.json');pinall(s)
for eng,out in s['public_whole_bracket_enclosures'].items():
 for name,(lo,hi) in {'wprime':(F(10),F(51,5)),'mu':(F(99,100),F(101,100)),'g':(F(29),F(30))}.items():
  q=out[name];assert lo<=F(q['lower_exact'])<=F(q['upper_exact'])<=hi;counts['explicit_source_box_links']+=1
s=read('research/source_explicit_inverse/evidence/checks.json');pinall(s);assert F(s['delta_exact'])==F(33,2000);counts['explicit_low_constant_links']+=1
assert s['high_derivative_ceilings']=={'rho3':505,'rho4':24381,'rho5':3758450,'U3':6376,'U4':87933};counts['explicit_high_constant_links']=5
s=read('research/source_order_family/evidence/checks.json');pinall(s);assert list(map(F,s['interval']))==[F(61,20),F(31,10)];counts['explicit_order_interval_links']=1
data=read('research/source_integrated_inverse/evidence/checks.json');pinall(data)
for eng in ('arb','iv'):
 groups=[b for r in data['results'][eng]['rows'] for b in r['bounds'].values()]+[b for r in data['results'][eng]['uniform'] for b in r['bounds'].values()]+[b for row in data['results'][eng]['physical_L2_derivative_bounds'] for b in row]
 for box in groups:l,h=map(F,box);assert 0<l<=h;counts['positive_finite_exported_boxes']+=1
spec=importlib.util.spec_from_file_location('topic97_strict_fresh_audit',D/'code/audit_output.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def strict_fi(t):
 sign,mantissa,exponent,bitcount=t
 assert bitcount>=0 and mantissa>=0 and sign in (0,1),'nonfinite or invalid mpf'
 counts['strict_iv_endpoint_decodings']+=1
 return (-1 if sign else 1)*F(int(mantissa))*F(2)**int(exponent)
for text in ('inf','-inf','nan'):
 for t in iv.mpf(text)._mpi_:
  try:strict_fi(t)
  except AssertionError:counts['nonfinite_fault_rejections']+=1
  else:raise AssertionError(('nonfinite accepted',text))
mod.fi=strict_fi
C=[[F(x) for x in row] for row in data['radial_moments_exact']]
for eng in ('arb','iv'):mod.fresh(C,data,eng,counts)
assert counts['arb_fresh_scalar_containments']==counts['iv_fresh_scalar_containments']==2440 and counts['nonfinite_fault_rejections']==6
r=read('research/source_integrated_inverse/evidence/requested_scales.json');pinall(r)
lookup={eng:{(x['s'],x['ell']):x for x in data['results'][eng]['rows']} for eng in ('arb','iv')}
assert len(r['rows'])==10 and len({(x['s'],x['ell']) for x in r['rows']})==10
for row in r['rows']:
 for key,v in row['ceilings'].items():
  top=max(F(lookup[e][(row['s'],row['ell'])]['bounds'][key][1]) for e in ('arb','iv'))
  assert top==F(v['maximum_audited_upper_exact'])<F(v['strict_ceiling_exact'])==F(v['display']);counts['requested_scale_strict_comparisons']+=1
for p in [Path(__file__),D/'CLOSURE_NOTES.md',D/'REQUESTED_SCALES.md',D/'code/audit_output.py']:files[str(p.relative_to(B))]=sha(str(p))
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_STRICT_FINITE_NUMERIC_LINKAGE_AND_REQUESTED_SCALES','counts':dict(counts),'files':files,'scope':'Strict guarded fresh audit of every positive scalar, actual numeric links and all requested scale displays. Auxiliary operator only.'}
(E/'closure_guard.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='files'},indent=2))

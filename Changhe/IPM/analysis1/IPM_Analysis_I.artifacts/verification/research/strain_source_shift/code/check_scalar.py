"""Independent exact, Arb and iv scalar enclosure with existing archive audit."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];D=B/'research/strain_source_shift';E=D/'evidence'
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
paths=['research/canonical_inverse/evidence/audit_verdict.json','research/canonical_inverse/evidence/final_audit_manifest.json','research/modal_repair/evidence/audit_verdict.json','research/source_instance/evidence/verdict.json']
objs=[json.loads((B/p).read_text()) for p in paths];xv,xm,mv,sv=objs
assert xv['verdict']==mv['verdict']=='CONFIRMED' and xm['status']=='PASS' and sv['status']=='CONFIRMED_ACTUAL_LOCAL_SOURCE_INSTANCE'
assert sha(B/paths[1])==xv['audit_manifest_sha256']
for o,key in [(xm,'sha256'),(mv,'source_and_evidence_sha256'),(sv,'files')]:
 for p,h in o[key].items():assert sha(B/p)==h,p;pins+=1
x=json.loads((B/'data_exact/x3.json').read_text());m=json.loads((B/'data_exact/modal_v2.json').read_text())
k=F(float.fromhex(x['scalars_hex']['k']));assert k==F(float.fromhex(m['scalars_hex']['k']))==F(1615536043799051,9007199254740992)
assert sha(Path(x['source']))==x['source_sha256'];pins+=1
assert sha(Path(xm['source_generator_path']))==xm['source_generator_sha256'];pins+=1
# Use the complete previously audited scalar bounds as an explicit dependency.
d0,d1=map(F,xv['normalization_defect_decimal_outward']);assert (d0,d1)==(F('0.0000000103009'),F('0.0000000103014'))
# Reconstruct the same defect from the outward original strain interval and exact normalization.
s0,s1=map(F,xv['enclosure_decimal_outward']);norm=3/k-1
assert d0<norm-s1<=norm-s0<d1
p0,p1=map(F,sv['source_bracket']);assert 0<p0<p1 and 0<d0<d1
low,up=-p1*d1/3,-p0*d0/3
wantlo,wanthi=F('-0.0000000295309'),F('-0.0000000295294');assert wantlo<low<up<wanthi
# Engines independently form the full input rectangle using directed endpoints.
pA=qa(p0).union(qa(p1));dA=qa(d0).union(qa(d1));valA=-(pA*dA)/3
pI=iv.mpf([qi(p0).a,qi(p1).b]);sI=iv.mpf([qi(-d1).a,qi(-d0).b]);valI=(sI/3)*pI
out={}
for tag,val in [('arb',valA),('iv',valI)]:
 l,u=ends(val);assert wantlo<l<=low<=up<=u<wanthi
 out[tag]=rec(val)
# A fresh exact endpoint enumeration checks all monotonic choices, without interval arithmetic.
cs=[-p*d/3 for p in [p0,p1] for d in [d0,d1]];assert min(cs)==low and max(cs)==up
radius=F(22,10**9);assert -up>radius
# This is only a logical cancellation example, not a computed velocity for the actual h.
s=(low+up)/2;v=-s;assert s+v==0
for p in paths+['data_exact/x3.json','data_exact/modal_v2.json','research/canonical_inverse/PROOF.md','research/strain_source_shift/PROOF.md',str(Path(__file__).relative_to(B))]:files[p]=sha(B/p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_STRAIN_SOURCE_SCALAR','dependency_pins_checked':pins,'exact_k':str(k),'source_bracket_exact':[str(p0),str(p1)],'raw_strain_difference_exact':[str(-d1),str(-d0)],'exact_product_extrema':[str(low),str(up)],'requested_decimal_outward':[str(wantlo),str(wanthi)],'strict_endpoint_margins':[str(low-wantlo),str(wanthi-up)],'engines':out,'exact_corner_products_checked':4,'counts':{'archive_pin_groups':3,'directed_whole_rectangle_enclosures':2,'fresh_exact_corner_products':4,'shared_k_comparison':1,'normalization_difference_bounds':2},'scope':'Scalar linear consequence of accepted original-X3 whole-integral enclosure, normalized trial identity and actual source root. No new whole-integral summation. Does not bound U1[h](P) or classify X3 relative to jet-exclusion neighborhood.','files':files}
(E/'checks.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items() if k not in ['files','engines']}))

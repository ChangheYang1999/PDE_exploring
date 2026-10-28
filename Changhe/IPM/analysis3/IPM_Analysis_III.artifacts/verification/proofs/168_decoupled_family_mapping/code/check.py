"""Exact endpoint and normalization audit for the decoupled-weight theorem."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import hashlib, json
from flint import arb, ctx
TOP=Path(__file__).resolve().parents[1]
LANE=TOP.parents[1]
ctx.threads=1
k=F(1615536043799051,9007199254740992)
beta=F(17,2); eta=F(37,20); q=(8-eta)/2
checks={
 'scalar_inner_exponent':8-beta,
 'scalar_outer_exponent':8-eta,
 'scalar_outer_decay':q,
 'positive_scalar_kappa':1+k-eta/2,
 'inner_trace_dual_power':beta/2-2,
 'inner_trace_far_source_radial_power':beta-9,
 'inner_axis_HS_power':4+8-beta,
 'outer_axis_evaluation_power':k+eta/2-5,
 'outer_axis_HS_power':2*(k+eta/2-5)+8-eta,
 'inner_source_HS_radial_power':2*3-6-beta+(beta+2)+1,
 'outer_source_HS_radial_power':2*k-6-eta+(eta+2)+1,
 'outer_to_inner_source_integrability':beta-9,
 'outer_to_inner_output_integrability':11-beta,
 'outer_to_outer_source_power':eta-4,
 'outer_to_outer_output_power':2*k-eta+(eta-4)+1,
 'border_inner_log_radial_power':12-beta,
 'border_outer_log_radial_power':4*k-eta,
 'high_inner_weight_power':2*F(9,5)+8-beta,
 'high_outer_weight_power':-7+8-eta,
 'strain_radial_integral':1/(beta-4)+1/(4-eta),
}
assert checks['scalar_inner_exponent']==F(-1,2)
assert checks['scalar_outer_exponent']==F(123,20)
assert q==F(123,40) and 2<q<6
assert checks['positive_scalar_kappa']>0
assert checks['inner_trace_dual_power']>2
assert checks['inner_trace_far_source_radial_power']>-1
assert checks['inner_axis_HS_power']==F(7,2)>0
assert checks['outer_axis_HS_power']==2*(k-1)<0
assert checks['inner_source_HS_radial_power']==3
assert checks['outer_source_HS_radial_power']==2*k-3<-1
assert checks['outer_to_inner_source_integrability']>-1
assert checks['outer_to_inner_output_integrability']>-1
assert checks['outer_to_outer_output_power']==2*k-3<-1
assert checks['border_inner_log_radial_power']>0
assert checks['border_outer_log_radial_power']<0
assert checks['high_inner_weight_power']>0 and checks['high_outer_weight_power']<0
assert checks['strain_radial_integral']==F(266,387)
for a in (F(18,5),F(4)):
 assert F(5,2)<a<F(9,2) and a>3
 assert 4-2*a<-1 and 8-2*a>-1
 assert F(9,2)-a>0
 assert beta>=eta and 2*a<=beta
 assert a<=F(17,4)

def aa(z):
 z=F(z);return arb(z.numerator)/z.denominator

def compute(bits):
 ctx.prec=bits
 def B(x,y):return x.gamma()*y.gamma()/(x+y).gamma()
 out={}
 for a in (F(18,5),F(4)):
  av=aa(a)
  angular=2*B(aa((9-2*a)/2),aa(F(3,2)))
  strain=2*(16*B(aa(F(3,2)),av+aa(F(5,2)))-8*B(aa(F(3,2)),av+aa(F(3,2)))+B(aa(F(3,2)),av+aa(F(1,2))))
  norm=(strain*aa(F(266,387))).sqrt()/arb.pi()
  out[str(a)]={'I_a':angular,'I_c':strain,'c_R':norm}
 assert out['4']['I_a'].overlaps(arb.pi())
 assert out['4']['I_c'].overlaps(31*arb.pi()/128)
 assert out['4']['c_R'].overlaps((arb(4123)/(24768*arb.pi())).sqrt())
 return out
low=compute(384);high=compute(768)
for a in high:
 for name in high[a]:assert high[a][name].overlaps(low[a][name])
assert high['18/5']['c_R']<aa(F(239392,1000000))
assert high['4']['c_R']<aa(F(230190,1000000))

def exact(z):
 m,e=z.man_exp();return str(F(int(m))*F(2)**int(e))
def rec(z):return {'ball':z.str(50),'lower_exact':exact(z.lower()),'upper_exact':exact(z.upper())}
margin=json.loads((LANE/'proofs/160_family_margin/evidence/audit.json').read_text())
assert margin['status']=='CONFIRMED' and margin['minimum_millionths'][1]>=1105340
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_exponents':{x:str(y) for x,y in checks.items()},'precision_bits':[384,768],'angular_constants':{a:{n:rec(z) for n,z in row.items()} for a,row in high.items()},'proof_sha256':hashlib.sha256((TOP/'PROOF.md').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'margin_audit_sha256':hashlib.sha256((LANE/'proofs/160_family_margin/evidence/audit.json').read_bytes()).hexdigest()}
(TOP/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'date':out['date'],'status':'PASS','constants':{a:{n:z.str(20) for n,z in row.items()} for a,row in high.items()}},indent=2))

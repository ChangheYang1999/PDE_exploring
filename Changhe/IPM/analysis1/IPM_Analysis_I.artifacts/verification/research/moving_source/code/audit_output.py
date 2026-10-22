"""Fresh exact cross-products and Arb1536 beta integrals audit topic94."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys
from flint import arb,ctx,fmpq
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/moving_source';E=D/'evidence';ctx.prec=1536;ctx.threads=1
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def qa(x):x=F(x);return arb(fmpq(x.numerator,x.denominator))
def endpoints(v):
 assert v.is_finite()
 def cv(z):m,e=z.man_exp();return F(int(m))*F(2)**int(e)
 return cv(v.lower()),cv(v.upper())
x=json.loads((E/'checks.json').read_text());assert x['status']=='PASS_MOVING_SOURCE_CONSTANTS_WITH_ONE_CORRECTION';count=0;files={}
for p,h in x['files'].items():assert sha(B/p)==h,p;count+=1
for p in [Path(__file__),D/'PROOF.md',D/'ADDENDUM.md',E/'checks.json']:files[str(p.relative_to(B))]=sha(p)
s=x['source_bounds'];mlow=F(s['A_lo'])-F(743,2500)*F(99,2000)
assert mlow==F(x['m_lower'])>F(x['m_public_lower']);count+=1
assert F(x['m_public_lower'])*F('.09866')>1;count+=1
assert F(x['epsilon_transformed_upper'])<F(x['defect_lower'])-F('4.7e-19');count+=1
assert F(x['actual_mu_margin_upper'])<F(x['refuted_lead_mu_margin']);count+=1
assert F(x['corrected_mu_margin'])<F(x['margins']['mu_to_lower']);count+=1
for row in x['local_rows']:
 m2=F(row['m2']);ee=F(33,2000)*(F(417,10)*(F(743,2500)+m2)+F(15177,10000));den=F(1687,500)-ee
 assert ee==F(row['E_upper']) and den*F(row['K_upper'])==1 and den*F(row['K_decimal_ceiling'])>1;count+=3
r=qa(F(31,10));pi=arb.pi()
# Gamma ratios arise from integrating u^j(1+u)^(-r), independently of
# the rational-product embedding formulas in the primary checker.
fresh={'alpha':((r-1).gamma()/r.gamma()/(4*pi)).sqrt(),'beta':((r-2).gamma()/r.gamma()/(4*pi)).sqrt(),'gamma':((r-3).gamma()/r.gamma()/(2*pi)).sqrt(),'k0':50/pi,'k1':qa(F(800)*F(2000,33))/pi}
pl,pu=F(s['p_lo']),F(s['p_hi']);delta=F(33,2000)
fresh['Cc_lo']=qa(3*delta/(pu-3*delta)**3)/pi.sqrt();fresh['Cc_hi']=qa(3*delta/(pl-3*delta)**3)/pi.sqrt()
records={}
for key,v in fresh.items():
 a,b=endpoints(v);records[key]={'lower_exact':str(a),'upper_exact':str(b)}
 for eng in ['arb512','iv180']:
  z=x['engines'][eng][key];assert F(z['lower_exact'])<=a<=b<=F(z['upper_exact']),(key,eng);count+=1
# The source scalars are imported from the independently audited exact
# moment run; ensure the narrow interval fits the wider unique root box.
old=json.loads((B/'research/modal_source/evidence/source_result.json').read_text());assert list(map(F,old['final_root_endpoints_exact']))==[pl,pu];count+=1
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FRESH_MOVING_SOURCE_AUDIT','checks':count,'fresh_embedding_method':'Arb1536 Gamma-ratio polar beta integrals, compared by full directed-endpoint containment against both earlier engines','fresh':records,'files':files}
(E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['files','fresh']}))

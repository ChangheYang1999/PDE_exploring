"""Fresh high-precision scalar audit and frozen-record verification."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,sys
from flint import arb,ctx,fmpq
assert not sys.flags.optimize
ctx.prec=1536;ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/escape_realization';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def q(v):
 v=F(v);return arb(fmpq(v.numerator,v.denominator))
def endpoints(x):
 assert x.is_finite()
 def convert(y):m,e=y.man_exp();return F(int(m))*F(2)**int(e)
 return convert(x.lower()),convert(x.upper())
c=json.loads((E/'checks.json').read_text());assert c['status']=='PASS_ESCAPE_REALIZATION_IDENTITIES_AND_BETA_BOUND'
assert c['counts']=={'exact_jet_trials':64,'exact_kernel_derivative_norms':66,'exact_resonance_values':16,'signed_cost_pulse_cases':24,'exact_cutoff_and_saddle_comparisons':8,'beta_directed_inequalities':6}
for f,h in c['files'].items():assert sha(B/f)==h,f
# Log-Gamma evaluation with all cancellations delayed in the exponent.
a=q(F(25,4));g=q(F(1129,1000));L=q(F(1,2))
logbeta=(a-2).lgamma()+(2-g).lgamma()-(a-g).lgamma()+(a+q(F(1,2))).lgamma()+q(F(1,2)).lgamma()-(a+1).lgamma()
logC=(a-2)*L.log()+logbeta/2-arb.pi().log();C=logC.exp();lo,hi=endpoints(C)
contains=0
for engine,row in c['beta_bound'].items():
 oldlo,oldhi=F(row['lower_exact']),F(row['upper_exact']);assert oldlo<=lo<=hi<=oldhi;contains+=1
assert F(78147,10**7)<lo<hi<F(78149,10**7) and hi/3<F(521,200000)
assert lo>F(78148,10**7) # .0078148 is inward as an upper bound.
assert F(c['exact']['cutoff_variation_upper'])==F(99,2000)*F(743,2500)<F(99,200)
# The statement concerns the prompt functional c=sigma/3.
for kk in [F(1,7),F(1615536043799051,9007199254740992)]:
 cl=1/kk;sig=F(7,11);cp=sig/3
 assert cl*(-cp/cl**2)+cp*kk==0
 assert cl*(-cp/(3*cl**2))+cp*kk!=0
files={str(p.relative_to(B)):sha(p) for p in [Path(__file__),E/'checks.json',D/'PROOF.md',D/'ADDENDUM.md',D/'CLARIFICATIONS.md']}
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FRESH_ESCAPE_SCALAR_AUDIT','precision_bits':1536,'method':'Arb log-Gamma followed by exponentiation, exact rational full-enclosure containment and independent prompt-functional resonance identities','complete_primary_enclosures_containing_fresh_result':contains,'lower_exact':str(lo),'upper_exact':str(hi),'raw_sigma_safe_upper':'78149/10000000','prompt_c_safe_upper':'521/200000','decimal_0078148_is_inward_upper':True,'files':files}
(E/'output_audit.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items() if k not in ['files','lower_exact','upper_exact']}))

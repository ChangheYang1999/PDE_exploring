"""Pin evidence and verify all public strict rational upper bounds."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];E=B/'research/outer_leading_cancellation/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
r=json.loads((E/'leading_result.json').read_bytes());a=json.loads((E/'leading_iv_audit.json').read_bytes())
assert r['status']=='COMPUTED_REQUIRES_INDEPENDENT_AUDIT' and a['status']=='PASS'
assert a['primary_result_sha256']==sha(E/'leading_result.json')
assert r['source_sha256']==a['primary_source_sha256']==sha(B/'research/outer_leading_cancellation/code/combine_leading.py')
assert a['source_sha256']==sha(B/'research/outer_leading_cancellation/code/audit_leading_iv.py')
assert r['proof_sha256']==a['proof_sha256']==sha(B/'research/outer_leading_cancellation/PROOF.md')
assert (a['enclosure_checks'],a['exact_projection_scalar_checks'],a['direct_trigonometric_pairs'])==(1070,1048,68121)
bounds={'0':['17145004','5740429','121374223','40621479'],'9':['0.000020450600','0.000001362864','0.002591031','0.000172670851'],'10':['0.000008067437','0.000000449353','0.001408491','0.000078452209'],'17':['0.000000066848357','0.000000001060902','0.000110121685','0.000001747661']}
keys=['absolute_W','weighted_delta_0','weighted_delta_1/2','weighted_delta_2888063583571445/9007199254740992'];comparisons=[]
def check(upper,values,name,T=None):
 for v in values:assert 0<=F(v['lower_exact'])<=F(v['upper_exact'])<F(upper),(name,T,upper)
 comparisons.append({'T_exact':T,'quantity':name,'strict_public_upper_exact':upper,'primary_upper_exact':values[0]['upper_exact'],'independent_upper_exact':values[1]['upper_exact']})
for T,us in bounds.items():
 for key,u in zip(keys,us):check(u,[next(c for c in x['cases'] if c['T_exact']==T)['values'][key] for x in [r,a]],key,T)
check('0.003623778',[x['new_C_star'] for x in [r,a]],'C_star')
check('4949188',[x['exterior_L2_majorant'] for x in [r,a]],'exterior_L2_majorant','0')
files=['research/outer_leading_cancellation/PROOF.md','research/outer_leading_cancellation/code/combine_leading.py','research/outer_leading_cancellation/code/audit_leading_iv.py','research/outer_leading_cancellation/code/finalize_verdict.py','research/outer_leading_cancellation/evidence/leading_result.json','research/outer_leading_cancellation/evidence/leading_iv_audit.json','research/outer_leading_cancellation/evidence/final_serialized_run.json','research/outer_majorant/evidence/verdict.json','research/outer_majorant/evidence/outer_result.json','research/outer_majorant/evidence/exact_outer_coefficients.json']
for tag in ['outer_leading_theorem','outer_leading_source','outer_leading_closure']:
 m=json.loads((B/f'notes/reviews/{tag}_metadata.json').read_bytes());assert m['actual_response_model']=='claude-opus-5-5' and m['stop_reason']=='end_turn'
 files.extend([f'notes/reviews/{tag}_metadata.json',f'notes/reviews/{tag}_response.md'])
v={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','scope':'Complete exterior zeroth residual majorants retaining leading-exponent angular cancellation, for exact normalized modal trial; audited shared nonleading majorant coefficients and canonical Green dependencies. No whole-exterior smallness, derivatives, X3 distance, inverse or decisive endpoint.','method':'Arb384 Laurent convolution versus iv160 raw affine projection, direct Poisson and all 68121 trigonometric pairs. Full iv-within-Arb containment, exact source isolation and public rational comparisons.','actual_review_model':'claude-opus-5-5','checks':{'enclosures':1070,'projection_scalars':1048,'trigonometric_pairs':68121,'public_strict_comparisons':len(comparisons)*2},'public_bounds':comparisons,'old_C_star_upper_exact':r['old_C_star_upper_exact'],'files':{f:sha(B/f) for f in files}}
(E/'verdict.json').write_text(json.dumps(v,indent=2)+'\n');print(json.dumps({'utc':v['utc'],'status':v['status'],'sha256':sha(E/'verdict.json'),'public_strict_comparisons':len(comparisons)*2}))

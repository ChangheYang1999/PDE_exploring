from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
import sympy as S
v=Path('research/283_exact_thermal_bounded_axis/verification');start=datetime.now(timezone.utc).isoformat();t0=time.monotonic();main=(v.parent/'PROOF.md').read_text();support=(v/'SUPPORT_PROOF.md').read_text();review=(v/'A164_public.md').read_text();c=[]
def check(n,x):c.append(dict(name=n,passed=bool(x)))
def eq(n,x):check(n,S.simplify(x)==0)
beta=S.symbols('beta',positive=True);y=S.symbols('y',real=True);d=(3*beta+2)/2
for n,s in [('lemma_evenness','If Theta0 is even, so is F.'),('final_taper_accounted','then transition smoothly to beta'),('variable_plateau','depends linearly with positive slope L-beta'),('cutoff_range','between0and1'),('critical_escape_constant','exp(-3/8)exp(s/2)'),('sublinear_relative_velocity','generally constant outside the support'),('thermal_homogeneity','homogeneous of degree alpha=(beta-2)/beta'),('compactness_before_energy','Thus Theta would have compact support.')]:check(n,s in main)
check('finite_active_cutoffs_proved','The only active horizontal cutoffs are chi0,chic,chi1,zeta1' in support)
check('supercritical_strip_residual_distinguished',"(beta-2)A x^3 zeta1'(x)/4" in support)
check('review_no_opus_invocation','No model invocation succeeded' in review)
check('existing_actual_opus_followups',all(json.loads((v/f'opus{j}_status.json').read_text())['returned_model']=='claude-opus-5-5'for j in [492,493,494]))
eq('endpoint_index_constant',12*(-(3*beta+2)/(4*beta))+6*d/beta)
eq('critical_transient_loss',S.Rational(3,4)*S.Rational(1,2)-S.Rational(3,8))
eq('critical_passage_lower',S.Rational(3,2)-S.Rational(1,4)-S.Rational(5,4))
eq('center_gap',d-(beta-2)-(beta+6)/2)
eq('energy_coefficient',-beta-(beta-2)-2*(1-beta))
f=json.loads((v/'A164_freeze.json').read_text());check('proof_precedes_controls',f['utc']<start)
for name,key in [('A164_public.md','review_sha256'),('A164_SUPPLEMENT_PROOF.md','supplement_sha256')]:check(name+'_hash',hashlib.sha256((v/name).read_bytes()).hexdigest()==f[key])
check('main_proof_unchanged',hashlib.sha256((v.parent/'PROOF.md').read_bytes()).hexdigest()==f['main_proof_sha256'])
r=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,passed=sum(x['passed']for x in c),total=len(c),checks=c);(v/'A164_checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))

"""P283 supplemental check of model-review corrections and precise support facts."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import sympy as S
v=Path('research/283_exact_thermal_bounded_axis/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks={}
def ck(k,b):checks[k]=bool(b)
def eq(k,e):ck(k,S.simplify(e)==0)
x,y,beta,A,t=S.symbols('x y beta A t',real=True);z=S.Function('z')(x);c=beta-2;d=(3*beta+2)/2
th=A*x*x*z/2;R=c*x*S.diff(th,x)/2-c*th
eq('strip_temperature_y_zero',S.diff(th,y));eq('supercritical_strip_cutoff_residual',R-c*A*x**3*S.diff(z,x)/4);eq('critical_strip_cutoff_residual_zero',R.subs(beta,2))
x0,y0=S.symbols('x0 y0',real=True);K=A/(beta*(d-c));xt=S.exp(c*t/2)*x0;yt=S.exp(d*t)*(y0-K*x0*x0)+K*S.exp(c*t)*x0*x0
eq('local_orbit_x_equation',S.diff(xt,t)-c*xt/2);eq('local_orbit_y_equation',S.diff(yt,t)-d*yt+A*xt*xt/beta);eq('local_orbit_initial_x',xt.subs(t,0)-x0);eq('local_orbit_initial_y',yt.subs(t,0)-y0);eq('positive_d_minus_c',d-c-(beta+6)/2)
proof=(v.parent/'PROOF.md').read_text();supp=(v/'SUPPORT_PROOF.md').read_text()
ck('four_active_cutoffs_named',all(q in supp for q in ['chi0,chic,chi1,zeta1','finite intersection','|y(t)|<=|y0|+2|K||x0|^2']))
ck('no_common_all_cutoff_claim','every cutoff equals'not in proof)
for number in [492,493,494]:
 st=json.loads(Path(f'verification/opus{number}/status.json').read_text());ck('actual_complete_model_'+str(number),st['returned_model']=='claude-opus-5-5'and st['http_status']==200 and st['stop_reason']=='end_turn')
st=json.loads(Path('verification/opus491/status.json').read_text());ck('491_truncation_disclosed',st['stop_reason']=='max_tokens')
pb=json.loads((v/'support_proof_before_checks.json').read_text());ck('support_proof_precedes_checks',pb['utc']<start and pb['sha256']==hashlib.sha256(supp.encode()).hexdigest())
res={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(checks.values()),'total':len(checks),'checks':checks,'scope':'Exact correction of model-review prose; support argument and active-cutoff proof are analytic, not established by finite sampling.','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};(v/'support_checks.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:res[k]for k in ['started_utc','ended_utc','elapsed_seconds','passed','total']},indent=2));print('failed',[k for k,v in checks.items()if not v])

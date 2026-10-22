from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import sympy as s
r=Path('research/278_all_axis_jets_compact_extension');v=r/'verification';start=datetime.now(timezone.utc).isoformat();t=time.monotonic();checks=[]
def check(n,b):checks.append({'name':n,'passed':bool(b)})
def zero(n,e):check(n,s.simplify(e)==0)
x,y,c0,beta=s.symbols('x y c0 beta',real=True);f=s.Function('f')(x);H=s.Function('H')(x)
psi=c0*x+2*x*y-H;U1=-s.diff(psi,y);U2=s.diff(psi,x).subs(s.diff(H,x),f)
O=(-s.diff(psi,x,2)-s.diff(psi,y,2)).subs(s.diff(H,x,2),s.diff(f,x));W1=2*x+U1;W2=2*y+U2-c0
zero('local_horizontal',W1);zero('local_vertical',W2-(4*y-f));zero('local_vorticity',O-s.diff(f,x))
zero('thermal_PDE',W1*s.diff(f,x)+W2*s.diff(f,y));zero('vorticity_PDE',W1*s.diff(O,x)+W2*s.diff(O,y)+O-s.diff(f,x))
zero('strain',s.diff(psi,x,y)-2);zero('non_sublinear_ray',U1/x+2)
T=s.Function('T')(x,y);w1=s.Function('w1')(x,y);w2=s.Function('w2')(x,y)
expr=s.diff(w1*T*T,x)+s.diff(w2*T*T,y)-2*T*(w1*s.diff(T,x)+w2*s.diff(T,y))-(s.diff(w1,x)+s.diff(w2,y))*T*T
zero('flux_product_rule',expr);zero('flux_factor',2*beta+2*(beta-2)-4*(beta-1));zero('defect_integral_factor',-4*(beta-1)/2-2*(1-beta))
a=json.loads((v/'editorial_changes.json').read_text());check('original_proof_preserved',hashlib.sha256((v/'PROOF_reviewed_v1.md').read_bytes()).hexdigest()==a['original_sha256']);check('current_proof_matches_review',hashlib.sha256((r/'PROOF.md').read_bytes()).hexdigest()==a['updated_sha256'])
for name in ['opus487','opus488']:
 m=json.loads((Path('verification')/name/'status.json').read_text());check(name+'_actual_model',m['returned_model']=='claude-opus-5-5' and m['requested_model']=='us.anthropic.claude-opus-5-5' and m['status']=='COMPLETE')
check('scope_proof_precedes_controls',datetime.fromtimestamp((v/'SCOPE_PROOF.md').stat().st_mtime,timezone.utc).isoformat()<start)
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t,'passed':sum(c['passed']for c in checks),'total':len(checks),'checks':checks,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(v/'scope_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(out['passed'],out['total'],out['elapsed_seconds'])

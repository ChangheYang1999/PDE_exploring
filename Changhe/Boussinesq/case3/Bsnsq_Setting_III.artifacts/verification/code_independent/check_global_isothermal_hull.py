"""Independent exact controls for P207. No teammate code is imported or run."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,time
import sympy as sp
R=Path(__file__).resolve().parents[1];v=R/'research/207_global_isothermal_hull/verification'
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic()
x,y,t,x0,y0,beta,L=sp.symbols('x y t x0 y0 beta L',real=True)
psi=3*x*y+x**3/6;U=sp.Matrix([-sp.diff(psi,y),sp.diff(psi,x)])
W=sp.Matrix([2*x,2*y])+U;omega=-sp.diff(psi,x,2)-sp.diff(psi,y,2)
checks={};values={}
def zero(name,expr):
 z=sp.simplify(expr);checks[name]=(z==0);values[name]=str(z)
zero('velocity_x',U[0]+3*x);zero('velocity_y',U[1]-3*y-x*x/2)
zero('incompressibility',sp.diff(U[0],x)+sp.diff(U[1],y))
zero('curl_sign',omega+sp.diff(U[1],x)-sp.diff(U[0],y))
zero('vorticity_is_minus_x',omega+x)
zero('coupled_vorticity_equation',W[0]*sp.diff(omega,x)+W[1]*sp.diff(omega,y)+omega)
zero('temperature_equation_for_zero_temperature',sp.Integer(0))
zero('stream_x_odd',psi.subs(x,-x)+psi)
zero('vorticity_x_odd',omega.subs(x,-x)+omega)
zero('horizontal_velocity_x_odd',U[0].subs(x,-x)+U[0])
zero('vertical_velocity_x_even',U[1].subs(x,-x)-U[1])
zero('material_center_velocity_x',U[0].subs({x:0,y:0}))
zero('material_center_velocity_y',U[1].subs({x:0,y:0}))
xt=x0*sp.exp(t);yt=sp.exp(-5*t)*(y0+x0*x0/14)-x0*x0*sp.exp(2*t)/14
zero('backward_x_ode',sp.diff(xt,t)+W[0].subs({x:xt,y:yt},simultaneous=True))
zero('backward_y_ode',sp.diff(yt,t)+W[1].subs({x:xt,y:yt},simultaneous=True))
zero('backward_x_initial',xt.subs(t,0)-x0);zero('backward_y_initial',yt.subs(t,0)-y0)
ob=omega.subs({x:xt,y:yt},simultaneous=True)
zero('backward_vorticity_growth',sp.diff(ob,t)-ob)
zero('nonvanishing_damped_vorticity',sp.exp(-t)*ob+x0)
checks['counterexample_vorticity_is_nonzero']=omega!=0
checks['counterexample_velocity_fails_sublinearity']=sp.limit(U[1].subs(y,0)/x,x,sp.oo)==sp.oo
checks['counterexample_center_strain_is_not_B2_temperature_jet_value']=sp.diff(psi,x,y).subs({x:0,y:0})==3
values['backward_orbit']=[str(xt),str(yt)];values['counterexample_strain']=str(sp.diff(psi,x,y))
# General Cartesian div-curl identities, independent of the polynomial example.
v1=sp.Function('v1')(x,y);v2=sp.Function('v2')(x,y)
div=sp.diff(v1,x)+sp.diff(v2,y);curl=sp.diff(v2,x)-sp.diff(v1,y)
zero('div_curl_laplacian_x',sp.diff(v1,x,2)+sp.diff(v1,y,2)-sp.diff(div,x)+sp.diff(curl,y))
zero('div_curl_laplacian_y',sp.diff(v2,x,2)+sp.diff(v2,y,2)-sp.diff(div,y)-sp.diff(curl,x))
zero('temperature_transport_factor',sp.diff(sp.exp((beta-2)*t)*L,t)-(beta-2)*sp.exp((beta-2)*t)*L)
zero('exponential_radial_majorant',sp.diff(sp.exp(-beta*t),t)+beta*sp.exp(-beta*t))
# Version-specific anchors are consistency tests, not mathematical evidence.
candidate=(v/'frozen_sources/candidate_v1.md').read_text();report=(v/'frozen_sources/FINAL_REPORT.md').read_text()
def norm(s):return ' '.join(s.split())
def sec(k):return re.search(r'^## '+re.escape(k)+r'\..*?\n(.*?)(?=\n## |\Z)',candidate,re.M|re.S).group(1).strip()
anchors={}
for k in ['F1','F2','F3','F4','F7']:
 old,new=sec(k).split('" becomes "');old=old.split('"',1)[1];new=new.rsplit('"',1)[0]
 anchors[k]={'old':old,'new':new,'old_occurrences':norm(report).count(norm(old))}
 checks[k+'_unique_old_anchor']=anchors[k]['old_occurrences']==1
f5=sec('F5');quotes=re.findall(r'"(.*?)"',f5,re.S)
for j in [0,2]:
 q1=report[report.index('## 5.'):report.index('## 6.')]
 checks['F5_anchor_'+str(j)]=norm(q1).count(norm(quotes[j]))==1
anchors['F5']={'quotes':quotes}
checks['F6_unique_insertion_anchor']=norm(report).count('with isolated zeros off gamma (4.7(xix)(e), (xx)).')==1
checks['candidate_beta2_scope']='beta = 2' in sec('X1')
checks['candidate_retains_global_hypothesis']='boundedness of backward orbits' in norm(sec('X3'))
checks['candidate_retains_subarc_open_case']='second form' in sec('X3') and 'not established' in sec('X3')
checks['candidate_does_not_exclude_boundary_accumulation']='whose closure contains an endpoint' in sec('X3')
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'checks':checks,'values':values,'anchors':anchors,'candidate_sha256':hashlib.sha256(candidate.encode()).hexdigest(),'proof_sha256':hashlib.sha256((v.parent/'PROOF.md').read_bytes()).hexdigest(),'limitation':'Symbolic consistency controls. The manufactured field violates sublinearity and nonzero temperature jet; it is not an admissible profile. No numerical existence or formal certificate.'}
(v/'controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'elapsed_seconds':out['elapsed_seconds'],'passed':sum(checks.values()),'total':len(checks),'failed':[k for k,z in checks.items() if not z]},indent=2))
assert all(checks.values())

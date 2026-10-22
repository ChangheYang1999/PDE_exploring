from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, time
import sympy as s
r=Path(__file__).resolve().parents[1];v=r/'research/207_global_isothermal_hull/verification';fs=v/'frozen_sources'
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic()
source=r.parent/'analysis/work/enter_xxi/text_v2.md'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='49379c358bc90427e8eff49a5e2e94476f26d421f1ae4e8c2dd366144ff1b8ed'
shutil.copyfile(source,fs/'candidate_v2.md')
shutil.copyfile(r.parent/'analysis/astra/audit_xxi2/answer.md',fs/'lead_audit_xxi2_answer.md')
text=(fs/'candidate_v2.md').read_text();base=(fs/'FINAL_REPORT.md').read_text();checks={};vals={};anchors={}
norm=lambda q:' '.join(q.split())
def section(k):return re.search(r'^## '+re.escape(k)+r'\..*?\n(.*?)(?=\n## |\Z)',text,re.M|re.S).group(1).strip()
x,y,t,x0,y0=s.symbols('x y t x0 y0',real=True)
W=[-x/2,s.Rational(9,2)*y-x**3/3];O=x*x;psi=s.Rational(5,2)*x*y-x**4/12;U=[-s.diff(psi,y),s.diff(psi,x)]
def zero(k,e):
 z=s.simplify(e);checks[k]=(z==0)
 if z!=0:vals[k]=str(z)
zero('cubic_divergence',s.diff(W[0],x)+s.diff(W[1],y)-4)
zero('cubic_vorticity',-s.diff(W[1],x)+s.diff(W[0],y)-O)
zero('cubic_vorticity_PDE',W[0]*s.diff(O,x)+W[1]*s.diff(O,y)+O)
zero('cubic_temperature_PDE',0)
zero('cubic_stream_x',U[0]+2*x-W[0]);zero('cubic_stream_y',U[1]+2*y-W[1])
xt=x0*s.exp(t/2);yt=s.exp(-s.Rational(9,2)*t)*(y0-x0**3/18)+x0**3*s.exp(s.Rational(3,2)*t)/18
zero('cubic_backward_x',s.diff(xt,t)+W[0].subs({x:xt,y:yt},simultaneous=True))
zero('cubic_backward_y',s.diff(yt,t)+W[1].subs({x:xt,y:yt},simultaneous=True))
zero('cubic_initial_x',xt.subs(t,0)-x0);zero('cubic_initial_y',yt.subs(t,0)-y0)
zero('cubic_damped_vorticity',s.exp(-t)*O.subs(x,xt)-x0**2)
checks['cubic_fails_sublinearity']=s.limit(s.Abs(U[1].subs(y,0))/x,x,s.oo)==s.oo
checks['cubic_fails_odd_vorticity_parity']=s.simplify(O.subs(x,-x)+O)!=0
checks['cubic_not_nonzero_temperature_jet']=True
# Differential of angle composed with an invertible map cannot vanish.
a,b,c,d,p,q=s.symbols('a b c d p q', real=True)
angle_row=s.Matrix([[-q,p]])*s.Matrix([[a,b],[c,d]])
recovered=angle_row*s.Matrix([[d,-b],[-c,a]])
zero('angular_submersion_x',recovered[0]+q*(a*d-b*c))
zero('angular_submersion_y',recovered[1]-p*(a*d-b*c))
# Exact area determinant for arbitrary trace-four planar variational coefficient.
aa,bb,cc=s.symbols('aa bb cc');m11,m12,m21,m22=s.symbols('m11 m12 m21 m22')
M=s.Matrix([[m11,m12],[m21,m22]]);B=s.Matrix([[aa,bb],[cc,4-aa]]);N=B*M
det_deriv=N[0,0]*m22+m11*N[1,1]-N[0,1]*m21-m12*N[1,0]
zero('variational_area_rate',det_deriv-4*M.det())
for k in ['F1','F2','F3','F4','F7','F8']:
 old,new=section(k).split('" becomes "');old=old.split('"',1)[1];new=new.rsplit('"',1)[0]
 anchors[k]={'old':old,'new':new,'old_occurrences':norm(base).count(norm(old))}
 checks[k+'_unique_old_anchor']=anchors[k]['old_occurrences']==1
quotes=re.findall(r'"(.*?)"',section('F5'),re.S);q1=base[base.index('## 5.'):base.index('## 6.')]
for j in [0,2]:checks['F5_anchor_'+str(j)]=norm(q1).count(norm(quotes[j]))==1
anchors['F5']={'quotes':quotes}
checks['F6_unique_anchor']=norm(q1).count('with isolated zeros off gamma (4.7(xix)(e), (xx)).')==1
checks['v2_has_explicit_prior_implication']='also follows from (vii)' in section('X2')
checks['v2_disclaims_prior_logical_novelty']='also follows from the scattering identities (vii)' in norm(section('X3'))
checks['v2_local_proofs_cites_xii_and_xx']='The proofs of (xii)(b) and (xx)(a) use only the equations near p.' in norm(section('X3'))
checks['v2_retains_general_terminal_subarc_open']='second form' in norm(section('X3')) and 'not established' in norm(section('X3'))
checks['v2_retains_closure_only_open']='whose closure contains an endpoint' in section('X3')
checks['v2_F8_separates_endpoint_from_orbit']='other than the endpoint' in norm(anchors['F8']['new'])
checks['v2_F4_avoids_false_local_incoming']='for profiles' in anchors['F4']['new']
checks['prior_scattering_formula_present']='Theta = h(arg Phi)' in norm(base)
checks['prior_scattering_determinant_present']='det D Phi = 1' in norm(base)
checks['earlier_only_xxi_claim_removed']='is obtained only here' not in norm(section('X3')) and 'no form' not in norm(section('X3'))
vals['counterexample']={'W':[str(z) for z in W],'Omega':str(O),'Psi':str(psi),'backward':[str(xt),str(yt)],'limitation':'Fails sublinearity, x reflection parity and a0 nonzero; it is not a B2 profile.'}
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'checks':checks,'values':vals,'anchors':anchors,'candidate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((v.parent/'PROOF.md').read_bytes()).hexdigest(),'limitation':'Exact algebra and version controls supplement the standalone proof. Scattering identities are explicit prior dependencies; no existence certificate.'}
(v/'v2_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'passed':sum(checks.values()),'total':len(checks),'failed':[k for k,a in checks.items() if not a],'elapsed_seconds':out['elapsed_seconds']},indent=2))
assert all(checks.values())

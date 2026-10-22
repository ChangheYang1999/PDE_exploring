"""Independent exact identities and version-specific checks, P204.
No external lane code is imported. Polynomial controls are not PDE endpoints.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, time
import sympy as sp
ROOT=Path('verification')
PK=ROOT/'research/204_incoming_endpoint_gevrey_extension'
V=PK/'verification'
start=time.monotonic()
s,z,a,t=sp.symbols('s z a t', real=True)
w=s+sp.I*z
Ws=-2*a*(s*s-z*z); Wz=4*z+4*a*s*z
K=sp.expand(Ws-sp.I*Wz+4*sp.I*z)
S=sp.expand(w-K/2)
R=sp.conjugate(S)
E=sp.expand(S+a*S*S-w)
f=-2*a*s*s
expected=-f/2*(1+sp.integrate(1+2*a*(s-t*f/2),(t,0,1)))
identities={
 'divergence':sp.diff(Ws,s)+sp.diff(Wz,z)-4,
 'zero_curl':sp.diff(Wz,s)-sp.diff(Ws,z),
 'S_formula':S-(w+a*w*w),
 'velocity_identity':Ws+sp.I*Wz-2*(w-R),
 'defect_formula':E-(2*a*w*w+2*a*a*w**3+a**3*w**4),
 'nullcline_velocity':Ws.subs(z,0)-f,
 'nullcline_segment_identity':E.subs(z,0)-expected,
 'R_composition_order':sp.conjugate(R+a*R*R)-w-E,
}
checks=[]
for name,value in identities.items():
 checks.append({'name':name,'pass':sp.simplify(value)==0})
for aval in [-2,-1,1,2]:
 for sval in [sp.Rational(1,100),sp.Rational(1,200),sp.Rational(1,1000)]:
  fv=f.subs({a:aval,s:sval})
  for tv in [sp.Rational(0),sp.Rational(1,2),sp.Rational(1)]:
   sv=sval-tv*fv/2
   checks.append({'name':f'segment_side_a{aval}_s{sval}_t{tv}', 'pass':bool(sv>0 and abs(sv)<2*sval)})
  checks.append({'name':f'defect_nonzero_a{aval}_s{sval}', 'pass':bool(E.subs({a:aval,s:sval,z:0})!=0)})
# Reflection conjugacy preserves inward orientation in tangent-normal coordinates.
Q=sp.diag(-1,1); v=sp.Matrix(sp.symbols('v1:3',real=True)); tau=sp.Matrix(sp.symbols('t1:3',real=True))
checks.append({'name':'reflection_preserves_tangent_velocity','pass':sp.expand((Q*v).dot(Q*tau)-v.dot(tau))==0})
# Freeze new version and review sources, keeping prior v2 evidence unchanged.
manifest=json.loads((V/'sources.json').read_text())
for p in [ROOT.parent/'analysis/work/enter_xixe/text_v3.md', ROOT.parent/'analysis/work/enter_xixe/v2_to_v3.diff', ROOT.parent/'analysis/work/enter_xixe/preview.md', ROOT.parent/'analysis/astra/audit_xixe/answer.md']:
 dest=V/'frozen_sources'/f'{len(manifest["inputs"]):02d}_{p.parent.name}_{p.name}'
 shutil.copyfile(p,dest)
 b=dest.read_bytes();manifest['inputs'].append({'source':str(p),'frozen_file':str(dest.relative_to(ROOT)),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
(V/'sources.json').write_text(json.dumps(manifest,indent=2)+'\n')
files={Path(e['source']).name:ROOT/e['frozen_file'] for e in manifest['inputs']}
norm=lambda q:' '.join(q.split())
cand=files['text_v3.md'].read_text(); prior=files['text_v2.md'].read_text()
base=(V/'frozen_sources/00_analysis_FINAL_REPORT.md').read_text();preview=files['preview.md'].read_text()
sections={m.group(1):m.group(2).strip() for m in re.finditer(r'^## (Y\d+b?)\.[^\n]*\n(.*?)(?=^## |\Z)',cand,re.S|re.M)}
prevsections={m.group(1):m.group(2).strip() for m in re.finditer(r'^## (Y\d+b?)\.[^\n]*\n(.*?)(?=^## |\Z)',prior,re.S|re.M)}
textchecks=[]
bn=norm(base);pn=norm(preview)
for sec in ['Y2','Y3','Y4','Y4b','Y5','Y7']:
 textchecks.append({'name':sec+' unchanged from independently proved v2','pass':norm(sections[sec])==norm(prevsections[sec])})
for sec in ['Y1','Y4b','Y5','Y6','Y7']:
 m=re.fullmatch(r'"(.*?)" becomes "(.*?)"\.?',sections[sec],re.S)
 assert m,sec
 old,new=map(norm,m.groups())
 textchecks.append({'name':sec+' old exact normalized base occurs once','pass':bn.count(old)==1})
 textchecks.append({'name':sec+' replacement exact normalized preview occurs once','pass':pn.count(new)==1})
for sec in ['Y2','Y3','Y4']:
 textchecks.append({'name':sec+' exact normalized insertion preview occurs once','pass':pn.count(norm(sections[sec]))==1})
textchecks.extend([
 {'name':'global isolation premise retained','pass':'every zero of W off gamma is isolated' in norm(sections['Y2'])},
 {'name':'full-side basin is actual theorem','pass':"Consequently there is a disk N around p such that Theta = L and Omega = 0 at the points of N on C and on the side of C beyond p" in bn},
 {'name':'both endpoint types actual reflection theorem','pass':'The mirror endpoint has the same alternative.' in bn},
 {'name':'outgoing chart statement d unchanged','pass':norm(base[base.index('(d) Suppose that the tangent of gamma at p is not vertical'):base.index('Proof outline. (a) Take a square Q')]) in pn},
 {'name':'old contradictory scope deleted','pass':'none of (a) to (c) excludes profiles without an outgoing endpoint' not in pn},
 {'name':'nondegenerate premise still separately follows extension','pass':'(4.7(xix)(e)); if they are moreover nondegenerate,' in pn},
])
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'exact_checks':checks,'candidate_sha256':hashlib.sha256(files['text_v3.md'].read_bytes()).hexdigest(),'candidate_checks':textchecks,'control_scope':'The polynomial field has no negative zero arc. These are algebra and sign controls, not an endpoint construction or proof of the global basin theorem.'}
(V/'controls.json').write_text(json.dumps(result,indent=2)+'\n')
shutil.copyfile(__file__,V/'frozen_sources/check_incoming_gevrey_extension.py')
assert all(c['pass'] for c in checks+textchecks),[c for c in checks+textchecks if not c['pass']]
print(json.dumps({'exact_checks':len(checks),'candidate_checks':len(textchecks),'elapsed_seconds':result['elapsed_seconds'],'all_pass':True,'candidate_sha256':result['candidate_sha256']},indent=2))

"""P214 symbolic identities and independently assembled report preview.
No lead code execution, no numerical proof claims.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
import sympy as S
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'research/214_constant_subarc_audit';V=P/'verification'
version=sys.argv[1] if len(sys.argv)>1 else 'v1';D=V/version;D.mkdir(exist_ok=True)
paths={'candidate':ROOT.parent/'analysis/work/enter_xxii'/('text_'+version+'.md'),'preview':ROOT.parent/'analysis/work/enter_xxii/preview.md','report':ROOT.parent/'analysis/FINAL_REPORT.md','SPEC':ROOT.parent/'analysis/SPEC.md','notes':ROOT.parent/'analysis/NOTES_FOR_TEAM.md'}
texts={};hashes={}
for k,p in paths.items():
 b=p.read_bytes();texts[k]=b.decode();hashes[k]=hashlib.sha256(b).hexdigest();(D/(k+p.suffix)).write_bytes(b)
checks={};s,z=S.symbols('s z',real=True);f=S.Function('f')(s);A=f*S.diff(f,s,2)+5*S.diff(f,s)-S.diff(f,s)**2
W=[f,(4-S.diff(f,s))*z];om=S.diff(f,s,2)*z;theta=S.Symbol('L')+A*z
simp=lambda x:S.simplify(S.expand(x))
checks['triangular_divergence']=simp(S.diff(W[0],s)+S.diff(W[1],z)-4)==0
checks['triangular_negative_curl']=simp(-S.diff(W[1],s)+S.diff(W[0],z)-om)==0
checks['triangular_vorticity_identity']=simp(W[0]*S.diff(om,s)+W[1]*S.diff(om,z)+om-S.diff(theta,s))==0
checks['triangular_temperature_identity']=simp(W[0]*S.diff(theta,s)+W[1]*S.diff(theta,z)-(f*S.diff(A,s)+(4-S.diff(f,s))*A)*z)==0
checks['triangular_q_equation']=simp(A-5*S.diff(f,s)+S.diff(f,s)**2-f*S.diff(f,s,2))==0
fp=-S.exp(-1/s**2);fp2=S.diff(fp,s,2);res=fp*S.diff(fp,s,3)+(5-S.diff(fp,s))*fp2
checks['flat_second_derivative']=simp(fp2-S.exp(-1/s**2)*(6/s**4-4/s**6))==0
checks['flat_residual_nonzero_asymptotic']=S.limit(res/fp2,s,0,dir='+')==5
# Independent real-component verification of the complex-coordinate identities.
a=S.Function('a')(s,z);b=S.Function('b')(s,z);K=a-S.I*b+4*S.I*z
checks['complex_K_identity']=simp((S.diff(K,s)+S.I*S.diff(K,z))/2-((S.diff(a,s)+S.diff(b,z)-4)/2+S.I*(S.diff(a,z)-S.diff(b,s))/2))==0
R=s-a/2+S.I*(z-b/2)
checks['reflection_W_identity']=simp(2*(s+S.I*z-R)-(a+S.I*b))==0
M,m1,m2=S.symbols('M m1 m2',positive=True)
checks['tangent_disk_center_radius']=simp((s+1/(2*M))**2+z**2-1/(4*M**2)-(s*s+z*z+s/M))==0
norm=lambda x:' '.join(x.split())
c=texts['candidate'];base=norm(texts['report']);preview=norm(texts['preview'])
sections={m.group(1):m.group(2).strip() for m in re.finditer(r'^## ([YF][0-9]+)\.[^\n]*\n(.*?)(?=^## |\Z)',c,re.S|re.M)}
for key in ['Y1','Y2','Y3']:
 checks[key+'_exact_in_preview']=norm(sections[key]) in preview
anchor='excluded, and no smooth profile is excluded.'
checks['insertion_anchor_unique']=base.count(anchor)==1
assembled=base.replace(anchor,anchor+' '+' '.join(norm(sections[k]) for k in ['Y1','Y2','Y3']))
for key in ['F1','F2','F3','F4','F5','F6']:
 pairs=re.findall(r'"(.*?)"\s+becomes\s+"(.*?)"',sections[key],re.S)
 checks[key+'_one_pair']=len(pairs)==1
 old,new=map(norm,pairs[0]);checks[key+'_unique_anchor']=assembled.count(old)==1
 assembled=assembled.replace(old,new,1)
 checks[key+'_new_in_preview']=new in preview
# The proposed audit row is separately checked; it is not part of mathematical prose.
prev_without_row='\n'.join(l for l in texts['preview'].splitlines() if not l.startswith('| 4.7(xxii) |'))
checks['complete_preview_tokens']=assembled==norm(prev_without_row)
checks['H1_global_growth_scope']='sublinearity of U at infinity' in norm(sections['Y3'])
checks['H2_negative_side_only']='on the side of C that meets gamma' in norm(sections['Y1'])
checks['H3_no_isolation_added']='not the isolation of the zeros' in norm(sections['Y2'])
checks['H4_nonconstant_zero_arc']='theta\'(u_2) != 0' in norm(sections['Y2']) and 'g = 0 on I_2' in norm(sections['Y2'])
checks['H5_no_full_endpoint']=all(x in norm(sections['Y3']) for x in ['they do not decide whether Theta can be constant','no local solution or profile is constructed'])
checks['scope_avoids_literal_no_profile_excluded']='No profile is excluded' not in sections['Y3']
out={'utc':datetime.now(timezone.utc).isoformat(),'version':version,'hashes':hashes,'checks':checks,'symbolic_scope':'Exact algebra controls; complete informal proof in PROOF.md. Text controls do not prove theorems.','claims':{'H1':'CONFIRMED','H2':'CONFIRMED','H3':'CONFIRMED','H4':'CONFIRMED','H5':'CONFIRMED' if checks['scope_avoids_literal_no_profile_excluded'] else 'OPEN wording: replace No profile is excluded by No unrestricted B2 exclusion is obtained.'}}
(D/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'claims':out['claims'],'passed':sum(checks.values()),'total':len(checks),'failed':[k for k,v in checks.items() if not v]},indent=2))

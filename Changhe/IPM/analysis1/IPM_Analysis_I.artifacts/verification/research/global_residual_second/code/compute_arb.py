"""Direct rational regional assembly and Arb512 square root."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys,os
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/global_residual_second';ctx.prec=512
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def check(v,s):
 if not v:raise ValueError(s)
def dy(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ceil(q):
 q=F(q);check(q>=0,'nonnegative ceiling');n=q.numerator*10**12//q.denominator+1;return {'exact':str(F(n,10**12)),'decimal':str(n//10**12)+'.'+str(n%10**12).zfill(12)}
m=load(D/'data_exact/manifest.json');check(m['status']=='PASS_ACTUAL_ACCEPTED_FULL_MIDDLE_AND_REGIONAL_INPUTS','actual prerequisite');pins=dict(m['files'])
for n,h in pins.items():check(sha(B/n)==h,'source pin')
a=load(B/'research/global_residual_assembly/evidence/primary_assembly_v2.json');f=load(B/'research/middle_second/evidence/full_q16_verdict.json');S=sum([F(a['regions'][reg]['squared_norm_exact']) if reg!='middle' else F(f['L2_squared_upper_exact']) for reg in ['inner','middle','outer']],F(0));check(S>0,'positive total');ball=(arb(S.numerator)/S.denominator).sqrt();check(ball.is_finite(),'finite root');root=[dy(ball.lower()),dy(ball.upper())];check(0<root[0]<=root[1] and root[0]**2<=S<=root[1]**2,'exact Arb enclosure')
k=F(m['k_exact']);mapping={'W':'W_upper_exact','W_over_m':'W_over_m_upper_exact','weighted_1/2':'Wm_times_one_plus_u_power_half_upper_exact','weighted_'+str(F(1,2)-k):'Wm_times_one_plus_u_power_half_minus_k_upper_exact'};sup={}
for key,field in mapping.items():
 region={reg:F(a['global_suprema'][key]['regional_upper_exact'][reg]) if reg!='middle' else F(f['maxima'][field]['upper_exact']) for reg in ['inner','middle','outer']};maximum=max(region.values());sup[key]={'regional_upper_exact':{n:str(v) for n,v in region.items()},'upper_exact':str(maximum),'largest_majorant_regions':[n for n,v in region.items() if v==maximum],'strict_ceiling':ceil(maximum)}
check(a['global_suprema']['weighted_0']==a['global_suprema']['W_over_m'],'old duplicate weighted zero')
for p in [D/'data_exact/manifest.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():check(sha(B/n)==h,'final source digest')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_GLOBAL_SECOND_ASSEMBLY_REQUIRES_IV_AND_EXACT_CHECK','squared_norm_exact':str(S),'root_arb512_exact':list(map(str,root)),'root_ceiling_from_arb_upper':ceil(root[1]),'suprema':sup,'files':dict(sorted(pins.items())),'scope':'Direct scalar assembly with completed second middle evidence. Regional analytic and canonical claims inherited; not a new regional computation.'}
with (D/'evidence/arb_assembly.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'norm_ceiling':out['root_ceiling_from_arb_upper'],'suprema':{k:v['strict_ceiling'] for k,v in sup.items()}}))

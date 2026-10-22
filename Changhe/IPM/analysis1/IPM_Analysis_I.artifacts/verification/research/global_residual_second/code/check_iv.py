"""Separate saved-total replacement arithmetic, iv220 root and integer squaring."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import isqrt
import json,hashlib,sys,os
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/global_residual_second';iv.dps=220
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def need(v,s):
 if not v:raise ValueError(s)
def ends(x):
 out=[]
 for sign,m,e,bc in x._mpi_:need(bc>=0,'finite iv endpoint');out.append((-1 if sign else 1)*F(int(m))*F(2)**int(e))
 need(out[0]<=out[1],'iv endpoint order');return out
m=load(D/'data_exact/manifest.json');p=load(D/'evidence/arb_assembly.json');pins=dict(p['files']);need(p['status']=='COMPUTED_GLOBAL_SECOND_ASSEMBLY_REQUIRES_IV_AND_EXACT_CHECK','actual primary')
for n,h in pins.items():need(sha(B/n)==h,'primary and inherited pin')
a=load(B/'research/global_residual_assembly/evidence/primary_assembly_v2.json');v=load(B/'research/global_residual_assembly/evidence/verdict.json');f=load(B/'research/middle_second/evidence/full_q16_verdict.json');need(v['N2']==a['global_N2'] and v['suprema']==a['global_suprema'],'old accepted assembly');old=F(v['N2']['input_squared_exact']);oldmid=F(a['regions']['middle']['squared_norm_exact']);newmid=F(f['L2_squared_upper_exact']);need(old==sum((F(x['squared_norm_exact']) for x in a['regions'].values()),F(0)),'old exact sum');S=old-oldmid+newmid;need(S==F(p['squared_norm_exact']) and S>0,'replacement arithmetic');need(newmid>=oldmid,'joint middle sum dominates primary')
root=ends(iv.sqrt(iv.mpf(S.numerator)/S.denominator));lo,hi=map(F,p['root_arb512_exact']);need(0<root[0]<=root[1] and root[0]**2<=S<=root[1]**2 and lo**2<=S<=hi**2,'both exact squared enclosures');need(max(lo,root[0])<=min(hi,root[1]),'root overlap')
scale=10**12;index=isqrt(S.numerator*scale*scale//S.denominator);lower=F(index,scale);upper=F(index+1,scale);need(lower**2<=S<upper**2,'strict integer root');adjust=0
while upper<=max(hi,root[1]):adjust+=1;upper+=F(1,scale)
num=(index+1+adjust);decimal=str(num//scale)+'.'+str(num%scale).zfill(12);need(F(decimal)==upper==F(p['root_ceiling_from_arb_upper']['exact'])==F(p['root_ceiling_from_arb_upper']['decimal']),'strict common decimal root')
k=F(m['k_exact']);fields=[('W','W_upper_exact'),('W_over_m','W_over_m_upper_exact'),('weighted_1/2','Wm_times_one_plus_u_power_half_upper_exact'),('weighted_'+str(F(1,2)-k),'Wm_times_one_plus_u_power_half_minus_k_upper_exact')];checks=[]
need(set(p['suprema'])==set(k for k,vv in fields),'exact four distinct quantities')
for key,field in fields:
 q=p['suprema'][key];oldrecord=v['suprema'][key];mid=F(f['maxima'][field]['upper_exact']);need(mid>=F(oldrecord['regional_upper_exact']['middle']),'middle dominance');new=max(F(oldrecord['authoritative_upper_exact']),mid);need(new==F(q['upper_exact']),'independent max replacement')
 for reg in ['inner','outer']:need(F(q['regional_upper_exact'][reg])==F(oldrecord['regional_upper_exact'][reg]),'regional binding')
 need(F(q['regional_upper_exact']['middle'])==mid and max(map(F,q['regional_upper_exact'].values()))==new,'direct three-way maximum');c=F(q['strict_ceiling']['exact']);need(new<c==F(q['strict_ceiling']['decimal']) and c-F(1,scale)<=new,'minimal strict decimal ceiling');checks.append(key)
need(m['cells']=={'inner':54,'middle':7809,'outer':89} and m['actual_full_middle_verdict_sha256']==sha(B/'research/middle_second/evidence/full_q16_verdict.json'),'actual full provenance');need(datetime.fromisoformat(m['utc'])<datetime.fromisoformat(p['utc'])<datetime.now(timezone.utc),'preparation chronology')
for pp in [D/'evidence/arb_assembly.json',Path(__file__)]:pins[str(pp.relative_to(B))]=sha(pp)
for n,h in pins.items():need(sha(B/n)==h,'final digest')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_GLOBAL_SECOND_SCALAR_ASSEMBLY_IV220_AND_EXACT_INTEGER_CHECK','squared_norm_exact':str(S),'root_iv220_exact':list(map(str,root)),'integer_lower_exact':str(lower),'strict_root_ceiling_exact':str(upper),'strict_root_ceiling_decimal':decimal,'integer_ceiling_adjustment_units':adjust,'suprema_checked':checks,'same_shared_canonical_dependency':True,'files':dict(sorted(pins.items())),'scope':'Different arithmetic routes on shared exact scalar inputs, fresh iv220 and Arb512 roots, exact endpoint squares and strict integer ceilings. No regional recomputation, canonical linkage, forcing/inverse/nonlinear or endpoint claim.'}
with (D/'evidence/output_audit.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'norm_ceiling':decimal,'pins':len(pins)}))

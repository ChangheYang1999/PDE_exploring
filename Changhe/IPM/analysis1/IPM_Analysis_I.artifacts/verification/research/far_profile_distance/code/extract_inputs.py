"""Exact leading-tail input extraction. No JS/TS, servers or RLScience."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/far_profile_distance'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def hx(s):
 sign=-1 if s.startswith('-') else 1;s=s.lstrip('+-');a,b=s.split('p');whole,frac=a[2:].split('.');num=int(whole+frac,16);e=int(b)-4*len(frac)
 return sign*Q(num)*(Q(2)**e)
x=json.loads((B/'data_exact/x3.json').read_text());m=json.loads((B/'data_exact/modal_v2.json').read_text());v=json.loads((B/'research/modal_repair/evidence/audit_verdict.json').read_text())
assert v['verdict']=='CONFIRMED'
for f,h in v['source_and_evidence_sha256'].items():assert sha(B/f)==h,f
assert x['integers']['degree']==375 and x['integers']['angular']==200 and x['integers']['singular']==6 and x['integers']['spline_order']==7
assert len(x['z_hex'])==1+201*375+6 and len(x['spline_knots_hex'])==384
assert x['z_hex'][0]==x['scalars_hex']['k']==m['scalars_hex']['k']
assert x['scalars_hex']['L']==m['scalars_hex']['L'];assert m['arrays']['Aout']['shape']==[260,10]
z=x['z_hex'];beta=[z[1+(i+1)*375-1] for i in range(201)];tc=z[-6:];A=m['arrays']['Aout']['hex'][::10]
k=hx(z[0]);p=6+2*k/(2-k);d=sum(map(hx,tc),Q(0));tplus=hx(m['arrays']['knots']['hex'][-1]);bo=hx(m['scalars_hex']['bo']);bi=hx(m['scalars_hex']['bi'])
assert 0<k<Q(1,2) and 6<p<7 and d==Q(78259092636642149,9007199254740992)>0
assert bi>0 and bo>3-k and m['outer_jl'][0]==[0,0] and len(set(map(tuple,m['outer_jl'])))==10
for j,l in m['outer_jl'][1:]:assert j>=0 and l>=0 and j+l>0 and k-3-j*(1-k)-2*l<k-3
inputs=['research/far_profile_distance/source/original_gen_shape.py','research/far_profile_distance/source/evaluator_provenance.json','data_exact/x3.json','data_exact/modal_v2.json','research/modal_repair/evidence/audit_verdict.json','research/modal_repair/evidence/scalar_result.json','research/modal_repair/evidence/independent_gauss_iv.json']
o={'utc':datetime.now(timezone.utc).isoformat(),'definition':'Exact dyadics, except z defined exactly in modal_repair/PROOF.md; its bracket is never the definition.','files':{f:sha(B/f) for f in inputs},'modal_dependency_pins':v['source_and_evidence_sha256'],'source_archives':{'x3':{'path':x['source'],'sha256':x['source_sha256']},'modal':{'path':str((B/'../ipmA-num/data/trial_v2_h0.008.npz').resolve()),'sha256':m['source_npz_sha256']}},'x3_integers':x['integers'],'k':str(k),'L':str(hx(x['scalars_hex']['L'])),'p':str(p),'tplus':str(tplus),'bo':str(bo),'bi':str(bi),'outer_jl':m['outer_jl'],'beta_hex':beta,'chebyshev_hex':tc,'T1_exact':str(d),'modal_A0_hex':A,'z_public_bracket':v['public_decimal_enclosures']['A00_correction'],'z_iv_bracket':{k:v for k,v in json.loads((B/inputs[-1]).read_text())['values']['A00_correction'].items() if k.endswith('dyadic')},'public_strict_enclosures':{'ThetaX':['90.81020983980597','90.81020983980599'],'ThetaM':['90.81020983897880','90.81020983897882'],'Delta':['8.2716924477e-10','8.2716924478e-10'],'D_F0':['80253','80254'],'p':['6.19703','6.19704']},'counts':{'x3_endpoint_coefficients':201,'x3_chebyshev_coefficients':6,'modal_leading_coefficients':260,'outer_exponents':10,'dependency_pins':len(v['source_and_evidence_sha256'])}}
(D/'source/parameters.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps({'utc':o['utc'],'status':'PASS_EXACT_EXTRACTION','T1':str(d),'p':str(p),'pins':len(o['modal_dependency_pins'])}))

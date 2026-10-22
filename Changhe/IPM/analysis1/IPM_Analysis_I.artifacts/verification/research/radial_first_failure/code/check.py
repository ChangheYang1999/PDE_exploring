"""Independent exact range for the first failed source coefficient, unchanged candidate."""
import sys,os
sys.dont_write_bytecode=True
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,struct
from flint import fmpq,ctx
B=Path(__file__).resolve().parents[3];D=B/'research/radial_first_failure'
sys.path.insert(0,str(B/'research/radial_tm_full/code'))
import common,engine_arb as A,engine_iv as V

def need(v,s):
 if not v:raise ValueError(s)
def dump(p,d):
 with p.open('x') as f:json.dump(d,f,indent=1);f.write('\n')
def rat(x):return F.from_float(float(x))
def qdecode(hexbytes):
 bits=int.from_bytes(bytes.fromhex(hexbytes),'little');sign=bits>>63;exp=(bits>>52)&2047;mant=bits&((1<<52)-1)
 need(exp!=2047,'finite')
 power=-1074 if exp==0 else exp-1023-52
 if exp:mant+=1<<52
 if sign:mant=-mant
 return fmpq(mant*(1<<max(power,0)),1<<max(-power,0))
def pairq(z):return fmpq(int(z[0]))*fmpq(2)**int(z[1])
pins=common.current_pins();data=common.Data();c=data.cell(2955);d=c['arrays'];m=134
inputs={'em':float(d['scalar'][1]),'er':float(d['scalar'][2]),'am':float(d['A_mid'][m]),'ar':float(d['A_rad'][m]),'bm':float(d['B_mid'][m]),'br':float(d['B_rad'][m]),'cm':float(d['R_mid'][m,0]),'cr':float(d['R_rad'][m,0])}
record={k:{'hex':v.hex(),'bytes_le':struct.pack('<d',v).hex(),'exact':str(rat(v))} for k,v in inputs.items()};dump(D/'data_exact/coefficient.json',record)
r={k:rat(v) for k,v in inputs.items()};e0,e1=r['em']-r['er'],r['em']+r['er'];a0,a1=r['am']-r['ar'],r['am']+r['ar'];b0,b1=r['bm']-r['br'],r['bm']+r['br'];cl,ch=r['cm']-r['cr'],r['cm']+r['cr'];need(0<e0<=e1 and b0-a1>0,'positive numerator and denominator')
lower=(b0-a1)/(2*e1**2);upper=(b1-a0)/(2*e0**2)
exactcontained=cl<=lower and upper<=ch
q={k:qdecode(v['bytes_le']) for k,v in record.items()}
ql=((q['bm']-q['br'])-(q['am']+q['ar']))/(2*(q['em']+q['er'])**2)
qh=((q['bm']+q['br'])-(q['am']-q['ar']))/(2*(q['em']-q['er'])**2)
need(str(ql)==str(lower) and str(qh)==str(upper),'independent exact range agreement')
ii={k:common.f64_units(inputs[k]) for k in ['em','er','am','ar','bm','br']};args=[135]+[ii[k] for k in ['em','er','am','ar','bm','br']]+[[common.f64_units(x) for x in d['F_mid'][m]],[common.f64_units(x) for x in d['F_rad'][m]]]
ca=A.coefficients(*args)[1][0];av=common.arb_endpoints(ca);cv=V.coefficients(*args)[1][0];vv=common.iv_endpoints(cv)
need(pairq(av[0])<=ql<=qh<=pairq(av[1]),'Arb is outer range');need(pairq(vv[0])<=ql<=qh<=pairq(vv[1]),'iv is outer range')
w=json.loads((B/'research/radial_tm_full/evidence/full_failure.json').read_text())['failed_cell'];need(w['array_manifest']==c['array_manifest'],'same candidate and input bytes');fail=w['failures'][0];need(fail['independent_lo']==list(av[0]) and fail['independent_hi']==list(av[1]),'same failure reproduced')
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'ISOLATED_EXACT_RANGE_CHECK','cell':2955,'mode':135,'family':'R','coefficient':0,'exact_range_contained':exactcontained,'arb_range_contained':common.inside(av,common.f64_units(inputs['cm'])-common.f64_units(inputs['cr']),common.f64_units(inputs['cm'])+common.f64_units(inputs['cr'])),'iv_range_contained':common.inside(vv,common.f64_units(inputs['cm'])-common.f64_units(inputs['cr']),common.f64_units(inputs['cm'])+common.f64_units(inputs['cr'])),'exact_lower':str(lower),'exact_upper':str(upper),'candidate_lower':str(cl),'candidate_upper':str(ch),'lower_margin':str(lower-cl),'upper_margin':str(ch-upper),'relative_margin_to_candidate_radius':float(min(lower-cl,ch-upper)/r['cr']),'arb_endpoints':av,'iv_endpoints':vv,'pins':pins,'scope':'Only this scalar whole-box coefficient. Full radial criterion remains OPEN.'}
need(common.current_pins()==pins,'source stability');dump(D/'evidence/check.json',result);print(json.dumps({k:v for k,v in result.items() if k not in ('pins','exact_lower','exact_upper','lower_margin','upper_margin')},indent=2))

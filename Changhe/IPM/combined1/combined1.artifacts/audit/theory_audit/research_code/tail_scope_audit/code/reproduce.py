from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,hashlib,time,sys
from flint import arb,ctx,fmpq
sys.set_int_max_str_digits(0);ctx.prec=512
ROOT=Path(__file__).resolve().parents[1]
def ar(x):
 x=Fraction(x);return arb(x.numerator)/x.denominator
start=time.monotonic();p=ROOT/'source/stationary_principal.json';d=json.loads(p.read_text())
t=ROOT/'source/N4_pure_model.json';target=json.loads(t.read_text());rows=[]
for v in target['rows']:
 j=v['missing_sector_h'];branch=next(x for x in d['branches'] if x['index']==j)
 e=Fraction(branch['residual_exponent']);A=(arb.pi()*ar(sum((Fraction(x)**2 for x in branch['forcing_sin'].values()),Fraction(0)))).sqrt()
 R=arb(v['radius']);g0=A*R**ar(e+1)/ar(-2*e-2).sqrt();rf=A*R**ar(e+2)/ar(-2*e-4).sqrt() if e < -2 else None
 assert g0.overlaps(arb(v['pure_model_G0']))
 assert (rf is None and v['pure_model_rF']=='INFINITE') or rf.overlaps(arb(v['pure_model_rF']))
 rows.append({'missing_sector_h':j,'last_retained_branch':j-1,'R':v['radius'],'angular_full_circle_norm':A.str(80),'pure_model_G0':g0.str(80),'pure_model_rF':rf.str(80) if rf is not None else 'INFINITE','N4_overlap':True})
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':sha(p),'target_sha256':sha(t),'code_sha256':sha(Path(__file__)),'precision_bits':ctx.prec,'rows':rows,'scope':'Exact pure exterior model only, not a full residual lower bound','elapsed_seconds':time.monotonic()-start}
(ROOT/'verification/reproduction.json').write_text(json.dumps(out,indent=2)+'\n');print('rows',len(rows),'seconds',out['elapsed_seconds'])

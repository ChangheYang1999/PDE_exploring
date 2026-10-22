"""Exact decimal-versus-dyadic audit. Does not validate the saved cell bounds."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import json, hashlib
D=Path(__file__).resolve().parents[1]
rpath=D/'source/runs/forcing/p9_K64_n16_P8_merged.json'; r=json.loads(rpath.read_text())
checks=[]
def check(label, advertised, actual):
    a=F(advertised); b=F.from_float(actual)
    checks.append(dict(label=label,advertised=advertised,raw_float=actual,raw_exact=str(b),ceiling_above_saved_endpoint=a>=b,exact_ceiling_minus_saved=str(a-b)))
for lam,cs in [('1.0',['2.849','2696.2','5.6533']),('500.0',['4.4314','4583.9','8.8717'])]:
    for name,c in zip(['bound_order3','bound_order4','bound_order_3_1'],cs):check(lam+':'+name,c,r['results'][lam][name])
keys=['0_0','1_0','0_1','2_0','1_1','0_2','3_0','2_1','1_2','0_3','4_0','3_1','2_2','1_3','0_4']
public={'B94':['5.055e-7','5.428e-5','4.121e-5','8.311e-3','2.228e-3','2.943e-3','1.495','0.3289','0.1380','0.1984','280.8','54.56','13.62','7.370','10.73'],
'B3':['9.424e-7','7.623e-5','6.299e-5','9.135e-3','2.966e-3','3.535e-3','1.648','0.3289','0.1380','0.2062','311.6','54.56','13.62','7.370','12.70']}
for ball,cs in public.items():
    for k,c in zip(keys,cs):check(ball+':'+k,c,r['sup_D_eps'][ball][k])
up={}
for c in checks:
    # Six significant decimal digits, exact upward ceiling of the saved endpoint.
    b=F(c['raw_exact']); exp=0; scale=F(1)
    while b>=10*scale:scale*=10;exp+=1
    while b<scale:scale/=10;exp-=1
    quantum=scale/F(10**5); n=-((-b.numerator*quantum.denominator)//(b.denominator*quantum.numerator))
    ceil=n*quantum; assert ceil>=b
    up[c['label']]=dict(value=format(float(ceil),'.6g'),exact=str(ceil))
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='EXACT_ENDPOINT_DISPLAY_AUDIT_ONLY',source_sha256=hashlib.sha256(rpath.read_bytes()).hexdigest(),checks=checks,failed_ceiling_count=sum(not c['ceiling_above_saved_endpoint'] for c in checks),total=len(checks),suggested_six_significant_digit_ceilings=up,scope='A failure refutes upward display of the saved endpoint. It does not by itself refute the proposed ceiling for the unknown exact norm. Underlying cell enclosures remain OPEN.')
(D/'evidence/public_bounds_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['utc'],out['failed_ceiling_count'],'of',out['total'],'advertised ceilings below saved endpoints')
for c in checks:
    if not c['ceiling_above_saved_endpoint']: print(c['label'],c['advertised'],'<',c['raw_float'],'; round up to',up[c['label']]['value'])

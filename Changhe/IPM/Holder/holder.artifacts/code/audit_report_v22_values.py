"""Check the changed displays in the frozen report against accepted endpoints."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
base=ROOT/'05_team_audit/report_v22/verification'
report=(base/'FINAL_REPORT.md').read_text()
table=json.loads((ROOT/'data/verified_table.json').read_text())['rows']
checks=[]
for r in table:
    a=Q(r['alpha'])
    line=next(s for s in report.splitlines() if s.startswith('| ') and s.split('|')[1].strip() not in ('','---') and s.split('|')[1].strip()==str(float(a)))
    cols=[s.strip().strip('*') for s in line.split('|')[1:-1]]
    for index,key in [(4,'upper_C'),(5,'upper_D'),(6,'lower_C'),(8,'lower_D')]:
        assert Q(cols[index])==Q(r[key]),(r['alpha'],key)
    assert Q(cols[9])>=Q(r['upper_C'])/Q(r['lower_C'])
    assert Q(cols[10])>=Q(r['upper_D'])/Q(r['lower_D'])
    checks.append(dict(alpha=str(a),table_equal=True,ratios_outward=True))
gaps=['.3092','.2819','.2322','.1739','.0643','.1670','.2419','.2423','.2267','.1547']
for r,gap in zip(table,gaps):
    assert Q(r['selected_lower_D']['exact_safe_endpoint'])-Q(r['selected_upper_C']['exact_safe_endpoint'])>=Q(gap)
audit=json.loads((ROOT/'05_team_audit/table37_lead/verification/independent_audit.json').read_text())
assert [r['worst_phase'] for r in audit['rows']]==[16,16,15,15,14,11]
paths=['a50_prefix376','a75_prefix398','a90_prefix406']
lows=['1.9389659','2.3866494','4.7405340'];highs=['1.9708166','2.4049314','4.7537963']
errors=['.000475','.000825','.002081']
for tag,lo,hi,err in zip(paths,lows,highs,errors):
    r=json.loads((ROOT/f'05_team_audit/note14_certificate/homogeneous_tail/verification/{tag}/independent_audit.json').read_text())
    assert Q(lo)<=Q(r['I0']['lower'])<=Q(r['I0']['upper'])<=Q(hi),(tag,'I0 displayed range')
    assert Q(r['tail_error']['upper'])<=Q(err)
ctx.prec=256
coef=3*arb(3).sqrt()/(4*arb.pi())
r=table[-1]
assert arb(r['upper_C'])-100*coef<=arb('.8757')
assert arb(r['lower_C'])-100*coef>=arb('.6532')
result=dict(time_utc=datetime.now(timezone.utc).isoformat(),checks=checks,all_gaps_outward=True,phases_match=True,
    tail_interval_displays_enclose=True,tail_errors_enclose=True,endpoint_remainder_display_encloses=True,
    report_sha256=hashlib.sha256((base/'FINAL_REPORT.md').read_bytes()).hexdigest(),
    auditor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(base/'numeric_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

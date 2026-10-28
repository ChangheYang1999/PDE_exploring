"""Check changed report v24 displays against immutable accepted evidence."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'05_team_audit/report_v24'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
text=(BASE/'FINAL_REPORT.md').read_text();current=load(ROOT/'data/verified_table.json')['rows']
checks=[]
for r in current:
 a=Q(r['alpha']);tag=str(float(a))
 line=next(s for s in text.splitlines() if s.startswith('| '+tag+' |'))
 c=[s.strip().strip('*') for s in line.split('|')[1:-1]]
 for j,k in [(4,'upper_C'),(5,'upper_D'),(6,'lower_C')]:assert Q(c[j])==Q(r[k]),(a,k)
 assert Q(c[8])<=Q(r['lower_D'])
 assert Q(c[9])>=Q(c[4])/Q(c[6]) and Q(c[10])>=Q(c[5])/Q(c[8])
 checks.append(dict(alpha=str(a),table_upper_and_Clower_equal=True,Dlower_supported=True,ratios_outward=True))
rad=ROOT/'08_improved_upper_bounds/local_disk_transport/balanced_residual/radial_refinement/verification'
r=load(rad/'accepted.json');assert r['verdict']=='CONFIRMED' and r['ledger']=='V161'
for name,h in r['sha256'].items():assert sha(ROOT/name)==h
for row in load(rad/'independent_audit.json')['rows']:assert row['safe_upper_C'] in text
old=ROOT/'05_team_audit/note14_certificate/pole_profile/quadratic_lower/verification'
for tag,lo,hi in [('a50_fine_prefix1788','1.9516960','1.9611734'),('a75_prefix398','2.3870680','2.4046173'),('a90_prefix406','4.7413008','4.7530337')]:
 d=load(old/tag/'independent_audit.json');s=d['selected']
 assert all(Q(x['lower'])>=0 for x in s['condition_margins'])
 assert Q(lo)<=Q(s['I0']['lower'])<=Q(s['I0']['upper'])<=Q(hi)
for frag in ['If moreover','then $J_\\epsilon\\le M+E_s$','The minimum of the lower endpoints','on all $8$ equal','for every partition','0<H<L']:
 assert frag in text,frag
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),checks=checks,radial_values_supported=True,pole_intervals_and_conditions=True,
 report_sha256=sha(BASE/'FINAL_REPORT.md'),auditor_sha256=sha(Path(__file__)),scope='Changed displays and formulas; older accepted claims inherited at exact frozen report revision')
(BASE/'numeric_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

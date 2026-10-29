"""Freeze and audit completed primary critical-branch records, without executing their code."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, hashlib, math
ROOT=Path(__file__).resolve().parent.parent
NUM=ROOT.parent/'e4-num/axisymmetric_euler_24h'
now=datetime.now(timezone.utc)
out=ROOT/'report_audits'/('critical_complete_'+now.strftime('%Y%m%dT%H%M%S.%fZ'))
out.mkdir()
hashes={}
def freeze(p,target):
    b=p.read_bytes();target.parent.mkdir(exist_ok=True,parents=True);target.write_bytes(b)
    hashes[str(p)]=hashlib.sha256(b).hexdigest()
    return b
for p in [NUM/'FAILURE_MAP.csv',NUM/'FAILURE_MAP.md',NUM.parent/'NUM_REPORT.md',NUM/'scripts/failure_map.py']:
    freeze(p,out/p.name)
rows=[r for r in csv.DictReader((out/'FAILURE_MAP.csv').open()) if r['job_id'].startswith(('crit1_','crit2_'))]
checks=[];records=[]
def check(name,truth):
    checks.append({'name':name,'passed':bool(truth)})
    if not truth: raise AssertionError(name)
check('46 completed critical records',len(rows)==46)
for row in rows:
    name=row['job_id'];run=NUM/'runs'/name
    d=json.loads(freeze(run/'validation.json',out/name/'validation.json'))
    r=json.loads(freeze(run/'result.json',out/name/'result.json'))
    freeze(run/'job_resolved.json',out/name/'job_resolved.json')
    check(name+' fixed critical exponent',d['cl']==.5 and r['cl']==.5 and float(row['cl_final'])==.5)
    for key in ['rho_max','m_max','s_core','s_far','a_eff']:
        check(name+' CSV '+key, math.isclose(float(row[key]),float(d[key]),rel_tol=1e-13,abs_tol=1e-14))
    passed=d['s_core']>=.05 and d['s_far']>=.05
    check(name+' magnitude flag',(row['B2']=='True')==passed)
    records.append(dict(job_id=name,family=row['family'],level=row['level'],n_iter=r['n_iter'],optimizer=r['optimizer'],
        magnitude_filter=passed,stage_status=r['stage_status'],**{k:d[k]for k in ['rho_max','m_max','s_core','s_far','a_eff']},
        dominant_equation=row['dominant_eq'],dominant_shell=row['dominant_shell']))
summary={}
for prefix in ['crit1_','crit2_']:
    selected=[r for r in records if r['job_id'].startswith(prefix)]
    filtered=[r for r in selected if r['magnitude_filter']]
    summary[prefix]=dict(count=len(selected),magnitude_count=len(filtered),family_count=len(set(r['family']for r in selected)),
        best_all=min(selected,key=lambda r:r['rho_max']),best_magnitude=min(filtered,key=lambda r:r['rho_max']))
result=dict(recorded_utc=now.isoformat(),scope='Primary JSON and CSV consistency, not independent recomputation of these 46 fields. B2 column means the SPEC9.1 swirl magnitude filter only, not cross-level acceptance stability.',
    source_sha256=hashes,checks=checks,all_passed=all(x['passed']for x in checks),records=records,summary=summary)
(out/'evidence.json').write_text(json.dumps(result,indent=2)+'\n')
text=f'# Completed critical-branch record audit\n\nDate: {now.isoformat()}. Verdict: CONFIRMED for the stated primary-source counts and arithmetic; independent residual evaluation remains OPEN.\n\n'
for prefix,s in summary.items():
    a=s['best_all'];b=s['best_magnitude']
    text+=f"{prefix}: {s['count']} completed records, {s['family_count']} families and {s['magnitude_count']} passing the two swirl magnitude inequalities. The smallest primary rho is {a['rho_max']:.15g} ({a['job_id']}, core swirl {a['s_core']:.15g}, far swirl {a['s_far']:.15g}). Among magnitude-filter records the minimum is {b['rho_max']:.15g} ({b['job_id']}).\n\n"
text+=f'{len(checks)} source checks passed. The 46 records provide unsuccessful finite searches at c_l=1/2. They establish neither a theorem nor a controlled refinement comparison. The claim that 20 records pass full B2 is REFUTED as written: only the magnitude part is evaluated here. The phrase "none below 12" is true only among the 20 magnitude-filter records; several excluded runs have smaller residuals. Keep that qualifier in the final report.\n'
(out/'AUDIT.md').write_text(text)
print(out);print(json.dumps(summary,indent=2));print('checks',len(checks))

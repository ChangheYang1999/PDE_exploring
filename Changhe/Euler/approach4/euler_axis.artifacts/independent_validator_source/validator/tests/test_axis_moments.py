#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,time
from independent_fields import manufactured_power,manufactured_gaussian
from independent_axis_moments import axis_moments
ROOT=Path(__file__).resolve().parents[1]
def main():
    start=time.time();rows=[]
    for i,field in enumerate([manufactured_gaussian(),manufactured_power(.51),manufactured_power(.74)]):
        for z in [0.,.8,-1.2]:
            row=axis_moments(field,z);ref=axis_moments(field,z,nradial=56,nangle=80,cutoff_factor=16)
            error=max(abs(row['phi_moment']-row['phi_analytic']),abs(row['phi_z_moment']-row['phi_z_analytic']))
            refinement=max(abs(row['phi_moment']-ref['phi_moment']),abs(row['phi_z_moment']-ref['phi_z_moment']))
            row.update(field=i,error=error,refinement=refinement,tolerance=2e-9,passed=error<=2e-9 and refinement<=2e-9)
            rows.append(row);print(json.dumps(row),flush=True)
    paths=[Path(__file__),ROOT/'src/independent_axis_moments.py',ROOT/'src/independent_fields.py']
    record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,
            'checks':rows,'all_passed':all(r['passed'] for r in rows),
            'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    (ROOT/'results/axis_moment_tests.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'all_passed':record['all_passed'],'checks':len(rows),'elapsed_seconds':record['elapsed_seconds']}))
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':main()

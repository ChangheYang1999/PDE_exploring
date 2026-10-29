"""Audit retained balance and Cartesian comparison arithmetic for an export."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,time
import numpy as np
ROOT=Path(__file__).resolve().parent.parent;BASE=ROOT/'axisymmetric_euler_24h'
ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path);ap.add_argument('--geometry',type=Path,required=True);ap.add_argument('--balances',type=Path,required=True);ap.add_argument('--cartesian',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
assert a.output.resolve().is_relative_to(ROOT)and not a.output.exists()
start,cpu=time.perf_counter(),time.process_time();checks=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def check(name,passed):
    checks.append(dict(name=name,passed=bool(passed)))
    if not passed:raise AssertionError(name)
def load(p):
    d=json.loads(p.read_text());check(str(p)+' completed',d['phase']=='complete')
    check(str(p)+' candidate',d['candidate_sha256']==sha(a.candidate))
    check(str(p)+' geometry',d['geometry_sha256']==sha(a.geometry))
    for name,h in d['source_sha256'].items():
        q=Path(name)
        if not q.is_absolute():q=(ROOT if name.startswith(('research/','axisymmetric_euler_24h/'))else BASE)/q
        check(str(p)+' source '+name,sha(q)==h)
    return d
b,c=load(a.balances),load(a.cartesian);cl=c['c_l'];rows=[]
check('six balance rows',len(b['rows'])==6)
for r in b['rows']:
    item={k:r[k]for k in ['label','R','radius_over_a_eff','nradial','nangle']}
    for tag,factor in [('energy',5*cl-2),('helicity',4*cl-2)]:
        scale=max(abs(r[tag+'_flux']),abs(factor*r[tag]));defect=r[tag+'_flux']-factor*r[tag]
        corrected=defect-r[tag+'_residual_work']-r[tag+'_interface_jump']
        prefix=f'{r["label"]} {r["radius_over_a_eff"]} {tag}'
        check(prefix+' raw identity',abs(defect-r[tag+'_defect'])<1e-12*max(1,scale))
        check(prefix+' corrected identity',abs(corrected-r[tag+'_corrected_error'])<1e-12*max(1,scale))
        check(prefix+' oriented interface sum',abs(sum(x[tag+'_jump']for x in r['interfaces'])-r[tag+'_interface_jump'])<1e-12*max(1,scale))
        item[tag]=dict(integral=r[tag],flux=r[tag+'_flux'],raw_defect=defect,relative_raw_defect=abs(defect)/scale,corrected_error=corrected,relative_corrected_error=abs(corrected)/scale)
    rows.append(item)
check('fourteen Cartesian points',np.array(c['points_xyz']).shape==(14,3));check('five Cartesian steps',len(c['steps'])==5)
ref=np.array(c['reference_M'])
for row in c['steps']:
    err=abs(np.array(row['M'])-ref);s=str(row['step_factor'])
    check('Cartesian M point errors '+s,np.allclose(err.max(axis=1),row['M_error_by_point'],rtol=2e-13,atol=1e-30))
    check('Cartesian M max '+s,float(err.max())==row['M_max_error'])
    for tag in ['U','DU','M']:check('Cartesian '+tag+' aggregate '+s,max(row[tag+'_error_by_point'])==row[tag+'_max_error'])
result=dict(completed_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED',check_count=len(checks),all_passed=all(x['passed']for x in checks),checks=checks,c_l=cl,balance_rows=rows,pressure_parameters=b['pressure_parameters'],cartesian_steps=[{k:r[k]for k in ['step_factor','U_max_error','DU_max_error','M_max_error','divergence_max']}for r in c['steps']],cartesian_arithmetic=c['arithmetic'],timing=dict(balance=dict(completed=b['updated_utc'],wall=b['elapsed_seconds'],cpu=b['cpu_seconds']),cartesian=dict(completed=c['updated_utc'],wall=c['elapsed_seconds'],cpu=c['cpu_seconds'])),input_sha256={str(p.resolve().relative_to(ROOT)):sha(p)for p in [a.candidate,a.geometry,a.balances,a.cartesian,Path(__file__)]},collector_wall_seconds=time.perf_counter()-start,collector_cpu_seconds=time.process_time()-cpu,scope='Provenance and retained-arithmetic replay. No new field differentiation or quadrature. Balance residual and interface terms verify the identity calculation; they do not repair the field. Cartesian stencils use extended precision before float64 U, DU and final residuals.')
a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in ['checks','input_sha256']},indent=2))

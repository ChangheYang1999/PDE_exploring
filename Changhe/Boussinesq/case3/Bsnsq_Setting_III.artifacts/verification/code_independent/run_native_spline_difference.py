from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,time,hashlib
import native_spline_difference as gen
import check_native_spline_difference as audit
import exact_inverse_constant as inv
r=Path('research/183_certified_native_spline_differences/verification');(r/'inputs').mkdir(exist_ok=True);(r/'certificates').mkdir(exist_ok=True)
rad=Path('verification/L2_radial_tail_20261021T1526Z/inverse_constant_certificates');tight=Path('verification/L2_tolerance_and_radial_20261021T1541Z/inverse_constant_certificates')
labels=['blamL2B24b_beta3.0925','blamL2B32f_beta3.0925','blamL2R84_start','blamL2R84_beta3.0925','blamL2tight_beta3.0925']
started=datetime.now(timezone.utc).isoformat();begin=time.monotonic();inputs={};constants={};rows=[]
for name in labels:
    source=(tight if 'tight' in name else rad);p=r/'inputs'/f'{name}.json';p.write_bytes((source/f'{name}_input.json').read_bytes());inputs[name]=p
    constants[name]=source/f'{name}_certificate.json'
    inv.archive_check(json.loads(p.read_text()))
for name in labels[1:]:
    paths=[inputs[name],inputs[labels[0]]];xs=[json.loads(p.read_text())for p in paths];tic=time.monotonic();ts=datetime.now(timezone.utc).isoformat()
    cert=gen.make(*xs,3);cert['inputs']=[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for p in paths];cert['started_utc']=ts;cert['ended_utc']=datetime.now(timezone.utc).isoformat();cert['elapsed_seconds']=time.monotonic()-tic
    out=r/'certificates'/f'{name}.json';out.write_text(json.dumps(cert,indent=2)+'\n');print(ts,name,'generated',cert['elapsed_seconds'],'seconds',flush=True)
    tic=time.monotonic();check=audit.check(cert,xs);check.update(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tic,certificate_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),checker_sha256=hashlib.sha256(Path(audit.__file__).read_bytes()).hexdigest());out.with_suffix('.check.json').write_text(json.dumps(check,indent=2)+'\n')
    ca=[Q(v)for v in json.loads(constants[name].read_text())['result']['constant_C2']];cb=[Q(v)for v in json.loads(constants[labels[0]].read_text())['result']['constant_C2']];diff=[ca[0]-cb[1],ca[1]-cb[0]]
    assert max(map(abs,diff))<=Q(cert['inverse_difference_upper'])
    row={'new':name,'base':labels[0],'certificate':str(out),'check':str(out.with_suffix('.check.json')),'norms':cert['norm_enclosures'],'norm_float':check['norm_float'],'inverse_difference':[str(v)for v in diff],'inverse_difference_float':[float(v)for v in diff],'inverse_upper_bound':cert['inverse_difference_upper'],'inverse_upper_bound_float':check['inverse_bound_float'],'endpoint_P_derivatives':cert['endpoint_P_derivatives'],'first_z_cell':cert['first_z_cell'],'inverse_certificates':[str(constants[name]),str(constants[labels[0]])],'generator_seconds':cert['elapsed_seconds'],'checker_seconds':check['elapsed_seconds'],'polynomial_node_identities':check['polynomial_node_identities']};rows.append(row)
    print(json.dumps(row),flush=True)
    r.joinpath('summary.json').write_text(json.dumps({'started_utc':started,'updated_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-begin,'complete':len(rows)==4,'rows':rows},indent=2)+'\n')
print(datetime.now(timezone.utc).isoformat(),'ALL COMPLETE',time.monotonic()-begin,flush=True)

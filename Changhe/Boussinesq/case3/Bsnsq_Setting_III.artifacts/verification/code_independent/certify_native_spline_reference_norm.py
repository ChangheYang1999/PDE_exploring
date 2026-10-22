"""Packet183 reference scales: an archived scalar against an explicit zero spline."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import copy,json,time,hashlib
import native_spline_difference as gen
import check_native_spline_difference as audit
import exact_inverse_constant as inv
r=Path('research/183_certified_native_spline_differences/verification')
start=time.monotonic();utc=datetime.now(timezone.utc).isoformat()
p=r/'inputs/blamL2B24b_beta3.0925.json';x=json.loads(p.read_text());inv.archive_check(x)
z=copy.deepcopy(x);z['coefficients']=['0']*len(x['coefficients']);z['synthetic_role']='zero spline; not an archived candidate'
zp=r/'inputs/reference_zero.json';zp.write_text(json.dumps(z,indent=2)+'\n')
assert all(Q(a)==0 for a in z['coefficients'])
assert {k:v for k,v in z.items()if k not in ('coefficients','synthetic_role')}=={k:v for k,v in x.items()if k!='coefficients'}
c=gen.make(x,z,3);c['inputs']=[{'path':str(q),'sha256':hashlib.sha256(q.read_bytes()).hexdigest()}for q in (p,zp)]
c['input_roles']=['archive independently decoded','zero spline independently checked; no corresponding archive claimed']
out=r/'certificates/reference_norm.json';out.write_text(json.dumps(c,indent=2)+'\n')
s=audit.check(c,[x,z],archives=False)
s.update(started_utc=utc,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,certificate_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
out.with_suffix('.check.json').write_text(json.dumps(s,indent=2)+'\n')
summary=json.loads((r/'summary.json').read_text());norms=[[Q(t)for t in pair]for pair in c['norm_enclosures']]
baseinv=json.loads(Path(summary['rows'][0]['inverse_certificates'][1]).read_text())['result']['constant_C2'];baserange=sorted(abs(Q(t))for t in baseinv)
relative=[]
for row in summary['rows']:
    rn=[[Q(pair[0])/base[1],Q(pair[1])/base[0]]for pair,base in zip(row['norms'],norms)]
    dinv=sorted(abs(Q(t))for t in row['inverse_difference'])
    relinv=[dinv[0]/baserange[1],dinv[1]/baserange[0]]
    relative.append({'new':row['new'],'relative_norm_intervals':[[str(t)for t in a]for a in rn],'relative_norm_float':[[float(t)for t in a]for a in rn],'relative_inverse_interval':[str(t)for t in relinv],'relative_inverse_float':[float(t)for t in relinv]})
(r/'relative_scales.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'base':summary['rows'][0]['base'],'reference_norm_certificate':str(out),'reference_norms':c['norm_enclosures'],'reference_norm_float':s['norm_float'],'rows':relative},indent=2)+'\n')
print(json.dumps(s,indent=2))
for row in relative:print(row['new'],row['relative_norm_float'],row['relative_inverse_float'])

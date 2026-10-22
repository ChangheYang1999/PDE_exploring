"""Strict integer certificate for own finite trials, without floating arithmetic."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import datetime,hashlib,json,resource,time
from pathlib import Path
from intervals import Arithmetic,axis_enclosures
resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
resource.setrlimit(resource.RLIMIT_CPU,(530,540))
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
manifest_path=HERE/'data/input_manifest.json';proposal_path=HERE/'data/root_proposals.json'
manifest=json.loads(manifest_path.read_text());proposals=json.loads(proposal_path.read_text())
assert proposals.get('completed_utc')
ar=Arithmetic(3072);nlog=4000
start=time.process_time()
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'proof_sha256':(sha(HERE/'PROOF.md') if (HERE/'PROOF.md').exists() else None),
        'script_sha256':sha(__file__),'intervals_sha256':sha(HERE/'intervals.py'),
        'input_manifest_sha256':sha(manifest_path),'proposal_sha256':sha(proposal_path),
        'precision_bits':ar.bits,'log_terms':nlog,'arithmetic':'Integer operations only; outward dyadic intervals',
        'states':[],'overall':'OPEN until all strict gates and independent review'}
def fmt(a,digits=22):
    scale=10**digits
    return {'lower_scaled_integer':str(ar.floor(a[0]*scale,ar.B)),
            'upper_scaled_integer':str(ar.ceil(a[1]*scale,ar.B)),
            'decimal_denominator_power':digits}
for state,prop in zip(manifest['states'],proposals['states']):
    assert state['compiled_file']==prop['compiled_file']
    path=HERE/'data'/state['compiled_file'];assert sha(path)==state['compiled_sha256']==prop['compiled_sha256']
    assert sha(state['source'])==state['source_sha256']==prop['source_sha256']
    comp=json.loads(path.read_text());b=int(comp['beta'])
    l,u=[ar.rational(int(prop[k]['numerator']),int(prop[k]['denominator']))for k in ('t_lower','t_upper')]
    assert 0<l[0]<=l[1]<u[0]<=u[1]<ar.B
    entire=(l[0],u[1]);left,_=axis_enclosures(comp,l,ar,nlog);right,_=axis_enclosures(comp,u,ar,nlog)
    whole,modes=axis_enclosures(comp,entire,ar,nlog)
    opposite=(left['H'][1]<0<right['H'][0])or(right['H'][1]<0<left['H'][0])
    gates={'opposite_endpoint_H_signs':opposite,'mu_one_strict_sign':ar.excludes_zero(whole['mu']),
           'F_nonzero':ar.excludes_zero(whole['F']),'nu_nonzero':ar.excludes_zero(whole['nu'])}
    accepted=all(gates.values())
    ratio_one=accepted and (b==2 or whole['nu'][1]<0)
    row={'source_sha256':state['source_sha256'],'compiled_file':path.name,'compiled_sha256':sha(path),
         'beta':b,'t_lower_rational':prop['t_lower'],'t_upper_rational':prop['t_upper'],
         'endpoint_enclosures':{'lower':{k:ar.store(v)for k,v in left.items()},'upper':{k:ar.store(v)for k,v in right.items()}},
         'whole_bracket_enclosures':{k:ar.store(v)for k,v in whole.items()},
         'whole_bracket_decimal_enclosures':{k:fmt(whole[k])for k in ('mu','nu','F','radius')},
         'mode_enclosures':modes,'gates':gates,'axis_root_certified_by_integer_gates':accepted,
         'punctured_thermal_ratio_limit_one':ratio_one,
         'status':'INTEGER GATES PASS, independent review pending'if accepted else 'OPEN: failed strict gate',
         'cpu_seconds_to_here':time.process_time()-start}
    record['states'].append(row)
    (HERE/'verification/certificates.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'file':path.name,'gates':gates,'ratio_one':ratio_one,
                      'decimal_enclosures':row['whole_bracket_decimal_enclosures'],
                      'cpu_seconds':row['cpu_seconds_to_here']}),flush=True)
record['completed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
record['cpu_seconds']=time.process_time()-start
record['overall']='All strict integer gates pass; independent review pending'if all(s['axis_root_certified_by_integer_gates']for s in record['states'])else 'OPEN: one or more gates fail'
(HERE/'verification/certificates.json').write_text(json.dumps(record,indent=2)+'\n')

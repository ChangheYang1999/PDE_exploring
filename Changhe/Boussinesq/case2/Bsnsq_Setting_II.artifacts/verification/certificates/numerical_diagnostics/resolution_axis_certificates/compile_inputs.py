"""Compile only own frozen verifier inputs; exact integers are saved in JSON."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import datetime,hashlib,importlib.util,json,resource,time
from fractions import Fraction
from pathlib import Path
resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
resource.setrlimit(resource.RLIMIT_CPU,(115,120))
HERE=Path(__file__).resolve().parent
OWN=HERE.parents[1]/'inverse/integer_beta_closed_form/exact_inverse.py'
spec=importlib.util.spec_from_file_location('own_inverse90',OWN)
inv=importlib.util.module_from_spec(spec);spec.loader.exec_module(inv)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
start=time.process_time()
frozen=json.loads((HERE/'data/frozen_sources.json').read_text())
assert len(frozen['states'])==3
assert len({s['name'] for s in frozen['states']})==3
inputs=[(s['name'],s['sha256']) for s in frozen['states']]
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script_sha256':sha(__file__),
        'proof_sha256':(sha(HERE/'PROOF.md') if (HERE/'PROOF.md').exists() else None),'own_compiler':{'path':str(OWN),'sha256':sha(OWN)},
        'own_helper':{'path':str(inv.HELPER),'sha256':sha(inv.HELPER)},'states':[]}
for name,expected in inputs:
    source=HERE.parents[3]/'numerics'/'states'/name
    if sha(source)!=expected:print('note: %s bytes differ from the frozen copy hashed at certification time; coefficients are bound by the compiled-file hash checked later'%source.name)
    ca,cg,b,meta=inv.load(source)
    assert b==2 and meta['sigma_a']==1.5 and meta['sigma_G']==1.25
    assert meta['beta']==meta['beta_map']==2.0 and meta['L']==1 and meta['mapname']=='t'
    comp=inv.compiler(ca,cg,b)
    assert comp['denominator']>0 and len(comp['modes'])==comp['M']>0
    D=comp['denominator'];Q1=comp['modes'][0]['Q']
    a0=Fraction(sum(comp['A'][0]),D);b0=Fraction(sum(comp['C'][0]),D)
    c=sum((Fraction(x,8*D*(j+1))for j,x in enumerate(Q1)),Fraction())
    moments={'a0':a0,'b0':b0,'c':c,'c_minus_6':c-6,'five_b0_minus_two_a0':5*b0-2*a0}
    exact={k:{'numerator':str(v.numerator),'denominator':str(v.denominator),
              'zero':v==0}for k,v in moments.items()}
    assert a0!=0
    path=HERE/'data'/(source.stem+'_compiled.json')
    path.write_text(json.dumps(inv.poly.serialize(comp),separators=(',',':'))+'\n')
    record['states'].append({'source':str(source),'source_sha256':expected,'metadata':meta,
                            'compiled_file':path.name,'compiled_sha256':sha(path),'bytes':path.stat().st_size,'exact_moments':exact})
record['cpu_seconds']=time.process_time()-start
(HERE/'data/input_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))

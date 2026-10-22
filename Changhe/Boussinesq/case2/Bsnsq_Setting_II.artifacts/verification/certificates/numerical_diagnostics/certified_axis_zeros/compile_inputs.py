"""Compile only own frozen verifier inputs; exact integers are saved in JSON."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import datetime,hashlib,importlib.util,json,resource,time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
resource.setrlimit(resource.RLIMIT_CPU,(115,120))
HERE=Path(__file__).resolve().parent
OWN=HERE.parents[1]/'inverse/integer_beta_closed_form/exact_inverse.py'
spec=importlib.util.spec_from_file_location('own_inverse90',OWN)
inv=importlib.util.module_from_spec(spec);spec.loader.exec_module(inv)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
start=time.process_time()
inputs=[('TL_B2m_N176.npz','92363f7d6a126466610f033a52c71859b6bc3ca9979827069f8d95153b77bcc6'),
        ('TL_Nn6_a0m1_N144.npz','3e80949b5d43657189ba08c20f18492bf2e13eee43241f6c9990e4f094eee143')]
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script_sha256':sha(__file__),
        'proof_sha256':(sha(HERE/'PROOF.md') if (HERE/'PROOF.md').exists() else None),'own_compiler':{'path':str(OWN),'sha256':sha(OWN)},
        'own_helper':{'path':str(inv.HELPER),'sha256':sha(inv.HELPER)},'states':[]}
for name,expected in inputs:
    source=HERE.parents[3]/'numerics'/'states'/name
    if sha(source)!=expected:print('note: %s bytes differ from the frozen copy hashed at certification time; coefficients are bound by the compiled-file hash checked later'%source.name)
    ca,cg,b,meta=inv.load(source);comp=inv.compiler(ca,cg,b)
    path=HERE/'data'/(source.stem+'_compiled.json')
    path.write_text(json.dumps(inv.poly.serialize(comp),separators=(',',':'))+'\n')
    record['states'].append({'source':str(source),'source_sha256':expected,'metadata':meta,
                            'compiled_file':path.name,'compiled_sha256':sha(path),'bytes':path.stat().st_size})
record['cpu_seconds']=time.process_time()-start
(HERE/'data/input_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))

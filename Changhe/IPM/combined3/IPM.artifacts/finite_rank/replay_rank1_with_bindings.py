#!/usr/bin/env python3
"""Replay the actual rank-one coefficient with before/after dependency hashes."""
import hashlib,json,subprocess,sys,tempfile
from pathlib import Path
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
from fields013 import BASE007,PHI013,SOURCE_HASHES
files=[HERE/'source_rank1_certificate.py',HERE/'hermite_gram.py',HERE/'hermite_polar.py',HERE/'interval_matrix.py',
       HERE.parent/'coercivity_residual'/'fields013.py',HERE.parent/'coercivity_residual'/'asymptotics013.py',BASE007,PHI013]
def bindings():return {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
before=bindings();assert before[str(BASE007)]==SOURCE_HASHES['base007'] and before[str(PHI013)]==SOURCE_HASHES['phi013']
destination=HERE/'source_rank1_certificate_replay_v01.json'
with tempfile.TemporaryFile(mode='w+b') as log:
    proc=subprocess.run([sys.executable,'-B',str(HERE/'source_rank1_certificate.py'),'--bits','384','--tolerance','1e-9','--output',str(destination)],stdout=log,stderr=subprocess.STDOUT)
    if proc.returncode:
        log.seek(0);print(log.read().decode(errors='replace'));raise SystemExit(proc.returncode)
after=bindings();assert before==after
result=json.loads(destination.read_text());assert result['status']=='RIGOROUS_A11_AND_GRAM_ONLY'
record={'status':'ACTUAL_RANK1_REPLAY_COMPLETED_WITH_IMMUTABLE_DEPENDENCIES','before':before,'after':after,
        'result_sha256':hashlib.sha256(destination.read_bytes()).hexdigest(),'result_file':destination.name,
        'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'finished_utc':datetime.now(timezone.utc).isoformat()}
(HERE/'rank1_replay_bindings_v01.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'A11':result['A11'],'B11':result['B11'],'finite_rank_C_N':result['finite_rank_C_N']['operator_norm_upper']},indent=2))

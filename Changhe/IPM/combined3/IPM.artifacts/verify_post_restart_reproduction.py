#!/usr/bin/env python3
"""Run the documented independent reproduction into fresh temporary outputs."""
import hashlib
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    consumer=HERE/'operator_theory/assemble_fixed_parameter_closure_v01.py'
    independent=HERE/'verify_final_local_Q_closure.py'
    original=HERE/'operator_theory/fixed_parameter_closure_v01.json'
    frozen={str(p.relative_to(HERE)):sha(p) for p in [consumer,independent,original]}
    work=Path(tempfile.mkdtemp(prefix='ipm-combined3-final-reproduction-'))
    outputs=[work/'join.json',work/'independent.json']
    commands=[
        [sys.executable,'-B',str(consumer),'--selected-M','3/10','--selected-Rb','30000','--output',str(outputs[0])],
        [sys.executable,'-B',str(independent),'--consumer',str(outputs[0]),'--out',str(outputs[1])],
    ]
    statuses=[]
    for command,output in zip(commands,outputs):
        run=subprocess.run(command,capture_output=True,text=True)
        assert run.returncode==0,(command,run.stdout[-3000:],run.stderr[-3000:])
        data=json.loads(output.read_text());statuses.append(data['status'])
    assert statuses==['FINAL_NUMERICAL_CLOSURE_PASS','ROOT_INDEPENDENT_FINAL_LOCAL_Q_NUMERICAL_PASS']
    assert frozen=={str(p.relative_to(HERE)):sha(p) for p in [consumer,independent,original]}
    first=json.loads(outputs[0].read_text());second=json.loads(outputs[1].read_text())
    assert first['selected']['M']=='3/10' and first['selected']['source_split_radius']==30000
    result={'status':'POST_RESTART_DOCUMENTED_REPRODUCTION_PASS',
            'finished_utc':datetime.now(timezone.utc).isoformat(),'program_sha256':sha(Path(__file__)),
            'canonical_bindings_unchanged':frozen,'commands':commands,
            'output_sha256':{str(p):sha(p) for p in outputs},'statuses':statuses,
            'replay_matrix_path':first['matrix_certificate_path'],
            'replayed_exact_selected_M':'3/10','replayed_source_split_radius':30000,
            'selfmap_margin':second['values']['selfmap_energy_margin'],
            'rounded_selfmap_margin':second['values']['rounded_selfmap_margin'],
            'contraction_ratio':second['values']['contraction_ratio'],
            'scope':'Actual documented two-command replay after host restart; published consumers and certificates were not modified.'}
    (HERE/'ROOT_POST_RESTART_REPRODUCTION.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['commands','output_sha256']},indent=2))
if __name__=='__main__':main()

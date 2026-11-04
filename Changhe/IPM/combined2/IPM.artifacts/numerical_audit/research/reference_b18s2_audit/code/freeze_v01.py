"""Freeze the immutable registered007 b18s2 source and accepted base bindings."""
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
import json,os,time
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/reference_b18s2_audit'
def stamp():return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def digest(path):return sha256(path.read_bytes()).hexdigest()
def put(path,data):
    with path.open('x') as f:json.dump(data,f,indent=2);f.write('\n')
def main():
    assert sorted(os.sched_getaffinity(0))==[50];start,tick=stamp(),time.monotonic()
    folder=ROOT.parent/'exchange/candidate_snapshots/C2-N1-013-phi-007-sector-d8-leg24-lat-nf2'
    names=['MANIFEST.json','phi_007_b18s2_phi_exact.json'];blobs={n:(folder/n).read_bytes() for n in names}
    expected=['615f09c58c07ee4845a5e1bc3f321f8cc427f06bfdde5a75b3166f0f95f6c9df','a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a']
    for n,h in zip(names,expected,strict=True):assert sha256(blobs[n]).hexdigest()==h
    manifest,phi=[json.loads(blobs[n]) for n in names]
    assert manifest['id']=='C2-N1-013-phi-007-sector-d8-leg24-lat-nf2'
    assert manifest['correction_file']['sha256']==expected[1]
    assert phi['center']['base_exact_sha256']=='0973c3659f5ad0b5a3b2087a9e91ea61408b4356cee11006773879c13f9bfe20'
    assert phi['schema_version']=='ipm-potential-correction-v1' and len(phi['atoms'])==phi['n_atoms_nonzero']==12273
    assert len(phi['atoms_elementary'])==phi['n_atoms_elementary']==12273
    # Preserve only relative source labels in evidence, while copying exact source bytes.
    def safe_strings(x):
        if isinstance(x,str):assert not any(x.startswith(prefix) for prefix in ['/'+p+'/' for p in ('mnt','home','efs','tmp')])
        elif isinstance(x,list):
            for y in x:safe_strings(y)
        elif isinstance(x,dict):
            for y in x.values():safe_strings(y)
    safe_strings(manifest);safe_strings(phi);files={};source_rows=[]
    for n,b in blobs.items():
        assert (folder/n).read_bytes()==b
        target=BASE/'data'/n
        with target.open('xb') as f:f.write(b)
        relative=str(target.relative_to(ROOT));files[relative]=digest(target)
        source_rows.append({'source':'../exchange/candidate_snapshots/C2-N1-013-phi-007-sector-d8-leg24-lat-nf2/'+n,'path':relative,'sha256':files[relative],'bytes':len(b)})
    template=json.loads((ROOT/'research/fitted_center_constraints/verification/reference_b7_request_v01.json').read_text())
    template['created_utc']=stamp();template['inputs']['phi']={'path':source_rows[1]['path'],'sha256':expected[1]}
    for item in template['inputs'].values():assert digest(ROOT/item['path'])==item['sha256'];files[item['path']]=item['sha256']
    template['proof_dependencies']+=['research/reference_b18s2_audit/PROOF.md','research/reference_b18s2_audit/verification/freeze_v01.json']
    for name in template['proof_dependencies']:
        if name.endswith('/freeze_v01.json'):continue
        files[name]=digest(ROOT/name)
    for name in ['research/legendre_exact_bridge/PROOF.md','research/legendre_exact_bridge/code/convert.py',
                 'research/fitted_center_constraints/PROOF.md','research/fitted_center_constraints/code/check.py',
                 'research/fitted_center_constraints/code/reduce_v02.py','research/reference_b18s2_audit/code/freeze_v01.py',
                 'research/reference_b18s2_audit/code/run_v01.py','research/reference_b18s2_audit/code/publish_v01.py']:
        files[name]=digest(ROOT/name)
    put(BASE/'verification/freeze_v01.json',{'started_utc':start,'finished_utc':stamp(),'elapsed_seconds':time.monotonic()-tick,'passed':True,
        'code_sha256':digest(Path(__file__)),'proof_sha256':digest(BASE/'PROOF.md'),'files':files,'inputs':source_rows,'candidate_id':manifest['id'],
        'scope':'Immutable input registration and accepted-base bindings only. Structural and norm claims not yet checked.'})
    put(BASE/'verification/bridge_request_v01.json',template)
    print(stamp(),'frozen',manifest['id'],expected[1],flush=True)
if __name__=='__main__':main()

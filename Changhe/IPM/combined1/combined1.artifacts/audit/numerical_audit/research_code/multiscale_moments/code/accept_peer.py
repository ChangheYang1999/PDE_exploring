from pathlib import Path
import json, hashlib, shutil, time
from datetime import datetime, timezone
from flint import arb, ctx
ctx.prec=2048
start=time.monotonic()
base=Path(__file__).resolve().parents[1]
peer=base/'peer_review/T4'
source=base.parents[2]/'c1-t4/research/multiscale_moment_audit'
assert source.is_dir(),source
peer.mkdir(parents=True,exist_ok=True)
manifest=json.loads((source/'MANIFEST.json').read_text())
assert manifest['source_inputs_match'] and manifest['eight_replay_rows_identical']
for name,expected in manifest['files'].items():
    data=(source/name).read_bytes()
    assert hashlib.sha256(data).hexdigest()==expected,name
    target=peer/name
    assert not target.exists(),target
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(data)
shutil.copyfile(source/'MANIFEST.json',peer/'MANIFEST.json')
original=json.loads((base/'verification/calibration.json').read_text())
frozen=json.loads((peer/'source/verification/calibration.json').read_text())
replay=json.loads((peer/'replay/verification/calibration.json').read_text())
assert original==frozen
for left,right in zip(original['rows'],replay['rows'],strict=True):
    assert {k:v for k,v in left.items() if k!='elapsed_seconds'}=={k:v for k,v in right.items() if k!='elapsed_seconds'}
assert len(replay['rows'])==8
independent=json.loads((peer/'verification/independent_partial_fractions.json').read_text())
assert len(independent['rows'])==4
for row in independent['rows']:
    lower,upper,ref=(arb(row[k]) for k in ('lower','upper','reference'))
    assert lower<upper and lower<ref and ref<upper,row['case']
    assert row['overlap']
for name,h in independent['inputs'].items():
    assert hashlib.sha256((peer/name).read_bytes()).hexdigest()==h,name
record={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED','peer_audit':'T4-167','frozen_manifest_sha256':hashlib.sha256((peer/'MANIFEST.json').read_bytes()).hexdigest(),'frozen_file_count':len(manifest['files']),'original_source_identical':True,'eight_replay_rows_identical_except_runtime':True,'four_independent_partial_fraction_references_strictly_inside_enclosures':True,'elapsed_seconds':time.monotonic()-start,'scope':'Integration theorem and stated calibration only. No candidate norm. Caller validates integer multiplicities; tolerance is per-factor, and the implementation has a finite work cap.'}
target=base/'verification/T4_confirmation.json'
assert not target.exists()
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
print('result_sha256',hashlib.sha256(target.read_bytes()).hexdigest())

from pathlib import Path
import json,hashlib,time
from datetime import datetime,timezone
from flint import arb,ctx
ctx.prec=2048
start=time.monotonic()
base=Path(__file__).resolve().parents[1]
root=base.parents[1]
peerroot=root.parent/'c1-t4/research/projected_laplacian'
frozen=base/'peer_review/T4_selected'
frozen.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={}
def freeze(src,rel,expected=None):
    data=src.read_bytes();h=hashlib.sha256(data).hexdigest()
    if expected:assert h==expected,(src,h,expected)
    dst=frozen/rel;assert not dst.exists(),dst
    dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(data)
    files[str(rel)]=h
    return dst
manifest=base/'verification/manifest.json';mh=sha(manifest)
weights=['0','1/4','1/2','3/4','1','5/4','3/2']
rows=[]
for n in range(3,16,2):
    p=freeze(peerroot/f'verification/candidate007_mode{n}.json',f'verification/candidate007_mode{n}.json')
    peer=json.loads(p.read_text())
    for rel,h in peer['inputs'].items():
        if rel not in files:freeze(peerroot/rel,rel,h)
        assert files[rel]==h
    if 'code/weak_helper.py' not in files:freeze(peerroot.parent/'weak_probe_audit/code/reproduce.py','code/weak_helper.py',peer['helper_sha256'])
    assert files['code/weak_helper.py']==peer['helper_sha256']
    path=base/f'verification/modes/mode_{n:03d}.json';own=json.loads(path.read_text())
    assert own['manifest_sha256']==mh and own['cartesian_polar_exact'] and own['mixed_derivative_exact']
    left={row['a']:arb(row['norm']) for row in own['weights']}
    right={row['a']:arb(row['projected_norm']) for row in peer['rows']}
    for a in weights:assert left[a].overlaps(right[a]),(n,a)
    rows.append({'mode':n,'comparisons':len(weights),'own_sha256':sha(path),'peer_sha256':sha(p),'all_overlap':True})
partial=[]
for a in weights:
    energy=arb(0)
    for n in range(1,16,2):
        d=json.loads((base/f'verification/modes/mode_{n:03d}.json').read_text())
        r=next(r for r in d['weights'] if r['a']==a)
        e=arb(r['energy']);assert e>0
        energy+=e
    partial.append({'a':a,'modes':list(range(1,16,2)),'partial_norm':energy.sqrt().str(90),'full_norm_lower_bound_only':True})
out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'comparison_count':49,'rows':rows,'partial':partial,'frozen_files':files,'manifest_sha256':mh,'review_sha256':sha(base/'REVIEW_SELECTED_MODES.md'),'code_sha256':sha(Path(__file__)),'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED selected mode norms only; not a complete norm'}
p=base/'verification/selected_mode_confirmation.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print('PASS',out['comparison_count'],'comparisons',out['elapsed_seconds'],'seconds')
print('a0_partial_norm',partial[0]['partial_norm'])
print('sha256',sha(p))

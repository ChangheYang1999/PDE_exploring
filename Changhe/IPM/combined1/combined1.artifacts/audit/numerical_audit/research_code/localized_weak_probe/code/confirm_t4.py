"""Verify frozen peer source identities and all independently computed probe values."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[1];ROOT=BASE.parents[1];PEER=BASE/'peer_review'
def sha(p):return sha256(p.read_bytes()).hexdigest()
start=time.monotonic();ctx.prec=1024;rows=[]
for name in ['d2','Mpen2']:
    pp=PEER/f'T4_{name}_2048.json';peer=json.loads(pp.read_text())
    target=BASE/f'verification/{name}_beta_2048.json';own=json.loads(target.read_text())
    checks={'code':peer['code_sha256']==sha(PEER/'T4_reproduce.py'),
            'helper':peer['helper_sha256']==sha(PEER/'T4_helper.py'),
            'proof':peer['proof_sha256']==sha(PEER/'T4_PROOF.md'),
            'canonical':peer['canonical_sha256']==sha(ROOT/f'research/refit_audit/data/{name}_canonical.json'),
            'target':peer['peer_sha256']==sha(target)}
    assert all(checks.values()),checks
    refs={r['k']:r for r in own['probes']};comparisons=[]
    for row in peer['rows']:
        values={key:bool(arb(row[key]).overlaps(arb(refs[row['k']][key])))
                for key in ['pairing','A','B_weighted','C','D','gradient_sup_upper_ball','L2_radius_lower']}
        assert all(values.values()) and all(row['comparisons'].values())
        comparisons.append({'k':row['k'],'checks':values,'L2_radius_lower':row['L2_radius_lower']})
    rows.append({'candidate':name,'peer_result_sha256':sha(pp),'source_checks':checks,'comparisons':comparisons})
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'peer_audit':'T4-064',
     'rows':rows,'component_comparisons':sum(7*len(r['comparisons']) for r in rows),
     'review_sha256':sha(BASE/'REVIEW_T4.md'),'code_sha256':sha(Path(__file__)),
     'elapsed_seconds':time.monotonic()-start}
p=BASE/'verification/T4_confirmation.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

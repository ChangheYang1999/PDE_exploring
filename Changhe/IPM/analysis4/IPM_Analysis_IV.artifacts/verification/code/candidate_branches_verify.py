"""Check source-candidate pure branch coefficients against Cartesian recursion."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import cartesian_verify as cv

src=Path('../source/combined1/combined1.artifacts/candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json')
raw=src.read_bytes()
data=json.loads(raw)
c=cv.Q(data['cl_exact'])
delta=1-1/c
branches={}
for gen in data['generators']:
    j=gen['j']; mode=2*gen['m']
    branches.setdefault(j,{})
    branches[j][mode]=branches[j].get(mode,cv.Q(0))+cv.Q(gen['coef'])
leading=json.loads(Path('research/02_candidate007/data/leading_exact.json').read_text())
initial={int(m):cv.Q(a) for m,a in leading['density'].items()}
record=cv.recurrence(c,initial,8,require_potential=True)
checks=[]
for row in record['rows']:
    n=row['n']; j=n-1
    assert j in branches
    chi=cv.cos_field(4-n*delta,branches[j])
    rho,psi,_,_=cv.from_potential(chi)
    expected={str(m):cv.qs(v) for m,v in rho.sine().items()}
    actual=row['density']
    differences={m:cv.qs(cv.Q(actual.get(m,0))-cv.Q(expected.get(m,0))) for m in set(actual)|set(expected) if cv.Q(actual.get(m,0))!=cv.Q(expected.get(m,0))}
    same=not differences
    checks.append({'order':n,'source_branch':j,'density_coefficients_equal':same,'difference_count':len(differences),'differences':differences})
    print('branch',j,'all density coefficients equal:',same,flush=True)
out={'checked_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'input':src.as_posix(),'input_sha256':sha256(raw).hexdigest(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'cartesian_engine_sha256':sha256(Path('code/cartesian_verify.py').read_bytes()).hexdigest(),'scope':'Pure far-field branch coefficients only; not an exact full stationary-candidate claim.','checks':checks,'recursion':record}
Path('research/02_candidate007/verification/source_branches_N8.json').write_text(json.dumps(out,indent=2)+'\n')
assert all(row['density_coefficients_equal'] for row in checks)

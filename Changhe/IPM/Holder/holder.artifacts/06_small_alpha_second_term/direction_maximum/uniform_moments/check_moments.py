from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
from pathlib import Path
import json,hashlib
rows=[]
for n in range(1,41):
    ann=-4*sum((Q((-1)**j*comb(2*n-1,j)*comb(3*n-1-j,n-1-j),6*n-1-4*j) for j in range(n)),Q(0))
    R=Q(1)
    for k in range(n):R*=Q(2*n+1+4*k,2*n+3+4*k)
    circular=ann+Q(1,2*n)
    assert circular==(-1)**n*R/(2*n)
    rows.append(dict(n=n,annular=str(ann),circular=str(circular),R=str(R)))
p=Path(__file__).resolve()
out=dict(time_utc=datetime.now(timezone.utc).isoformat(),scope='Exact finite diagnostic for n=1,...,40; the analytic proof covers all n.',rows=rows,script_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),proof_sha256=hashlib.sha256(p.with_name('PROOF.md').read_bytes()).hexdigest())
p.with_name('rational_check.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all 40 exact moment identities')

"""Exact nonzero first leading density harmonic of canonical candidate007."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime,timezone
import json,time,sys
sys.set_int_max_str_digits(0)
start=time.monotonic()
root=Path(__file__).resolve().parents[1]
source=root.parent/'basis_rank_audit/source/canonical007.json'
assert sha256(source.read_bytes()).hexdigest()=='153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
raw=json.loads(source.read_text())
c=Q(4076476460239181,2251799813685248)
gamma=1/c;d=3+gamma
amps={}
for key,value in zip(raw['order'],raw['coefficients']):
    j,m,k=map(int,key)
    if j==0:amps[m]=amps.get(m,Q(0))+Q(value)
b=-amps[0]*d*d*(d-2)+amps[1]*(d*d-4)*d/2
assert 18<b<19
res=dict(utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha256(source.read_bytes()).hexdigest(),c=str(c),gamma=str(gamma),d=str(d),leading_potential_amplitudes={str(k):str(v) for k,v in sorted(amps.items())},first_density_harmonic=str(b),strict_rational_lower_bound='18',strict_rational_upper_bound='19',float_diagnostic=float(b),proof_sha256=sha256((root/'PROOF.md').read_bytes()).hexdigest(),code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_seconds=time.monotonic()-start)
with (root/'verification/candidate007.json').open('x') as f:json.dump(res,f,indent=2)
print(json.dumps({k:v for k,v in res.items() if k not in ('leading_potential_amplitudes','first_density_harmonic')},indent=2))

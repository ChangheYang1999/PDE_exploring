"""Compare the independently factored series to a frozen N1 implementation."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util
import json
import time
from flint import fmpq as Q
from moments import coefficients

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[1]

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

start = time.monotonic()
source = BASE/'source/N1_ipm_exact.py'
spec = importlib.util.spec_from_file_location('frozen_N1_exact',source)
peer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(peer)
c = Q(4076476460239181,2251799813685248)
gamma = 1/c
delta = 1-gamma
rows = []
for j in [0,3,7]:
    p = (3+gamma-j*delta)/2
    for m in [0,2,9]:
        w = max(5-m,0)
        for n in [0,1,5,11]:
            for Qd in [0,4]:
                for R in [Q(1,2),Q(1),Q(3,2),Q(10),Q(100)]:
                    own = coefficients(p,m,w,n,Qd,R,14)
                    old = peer.legqs_moments(peer.Q(str(p)),m,w,n,Qd,peer.Q(str(R)),14)
                    assert own == [Q(str(v)) for v in old], (j,m,w,n,Qd,R)
                    assert all(v == 0 for v in own[:Qd])
                    assert own[Qd] == R**(2*Qd)
                    assert own[Qd+1] == R**(2*Qd)*(p-m-R*R*(w+Qd+n*(n+1)))
                    serial = '\n'.join(str(v) for v in own)+'\n'
                    rows.append({'j':j,'m':m,'w':w,'n':n,'Q':Qd,'R':str(R),
                                 'all_15_coefficients_equal':True,
                                 'first_two_nonzero_formulas_exact':True,
                                 'coefficients_sha256':sha256(serial.encode()).hexdigest()})
result = {'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
          'candidate':'generator family only; no candidate coefficient claim',
          'N1_source_sha256':digest(source),'own_code_sha256':digest(BASE/'code/moments.py'),
          'driver_sha256':digest(Path(__file__)),'proof_sha256':digest(BASE/'PROOF.md'),
          'cases':rows,'number_of_cases':len(rows),'number_of_coefficient_equalities':15*len(rows),
          'elapsed_seconds':time.monotonic()-start}
dest = BASE/'verification/moment_comparisons.json'
assert not dest.exists()
dest.write_text(json.dumps(result,indent=2)+'\n')
print('confirmed',len(rows),'cases',15*len(rows),'coefficient equalities; seconds',result['elapsed_seconds'],flush=True)

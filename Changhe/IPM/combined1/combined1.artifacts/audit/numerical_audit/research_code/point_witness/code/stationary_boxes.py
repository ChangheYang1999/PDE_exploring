"""Exact comparison of point coefficients for the T4-067 parameter boxes."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from hashlib import sha256
import json, time
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/point_witness'
def digest(p):return sha256(p.read_bytes()).hexdigest()
start=time.monotonic()
parameters=BASE/'peer_review/T4_stationary_constants.json'
data=json.loads(parameters.read_text())
prior=BASE/'verification/T4_updates_confirmation.json'
reference=json.loads(prior.read_text())
b6=next(r for r in reference['rows'] if r['candidate']=='C1-A2-b6')
assert b6['excluded'] and all(b6['checks'].values())
s0,R0=Q(1,8192),Q(43,50000)
rows=[]
for entry in data['rows']:
    s,R=Q(entry['s']),Q(entry['R'])
    c0ratio=(R/R0)**2*(1+s0)/(1+s)
    c1ratio=c0ratio*s0/s
    assert 0<c0ratio<=1 and 0<c1ratio<=1
    rows.append({'name':entry['name'],'s':str(s),'R':str(R),
                 'squared_C0R_ratio':str(c0ratio),'squared_C1R_ratio':str(c1ratio),
                 'old_confirmed_gap_remains_a_lower_bound':True})
assert len(rows)==7
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
     'candidate':'C1-A2-b6','point':[0,1],'reference_s':str(s0),'reference_R':str(R0),
     'reference_gap':b6['gap'],'reference_record_sha256':digest(prior),
     'parameter_record_sha256':digest(parameters),'code_sha256':digest(Path(__file__)),
     'proof_sha256':digest(BASE/'PROOF.md'),'rows':rows,
     'scope':'Pointwise necessary inequality only. Every named box has gap at least the old confirmed b6 gap.',
     'elapsed_seconds':time.monotonic()-start}
dest=BASE/'verification/b6_stationary_boxes.json';assert not dest.exists()
dest.write_text(json.dumps(out,indent=2)+'\n')
print('b6 excluded in all',len(rows),'boxes; gap lower bound',b6['gap'],flush=True)

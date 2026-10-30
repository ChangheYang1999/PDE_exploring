from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,time
ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
start=time.monotonic()
params=ROOT.parent/'transient_constant_audit/verification/results.json'
old=ROOT.parent/'sharp_point_remainder_audit/verification/results.json'
peer=ROOT/'source/N4_result.json'
source=json.loads(params.read_text());prior=json.loads(old.read_text());target=json.loads(peer.read_text())
assert sha(params)==target['parameter_record_sha256']
b6=next(x for x in prior['rows'] if x['candidate']=='C1-A2-b6')
assert b6['excluded'] and b6['both_intervals_overlap'] and b6['gap']==target['reference_gap']
s0,R0=Q(1,8192),Q(43,50000)
rows=[]
for row in source['rows']:
    s,R=Q(row['s']),Q(row['R']);A=R*R/(1+s);B=A/s
    A0=R0*R0/(1+s0);B0=A0/s0
    assert A0>A>0 and B0>B>0
    peerrow=next(x for x in target['rows'] if x['name']==row['name'])
    assert Q(peerrow['s'])==s and Q(peerrow['R'])==R
    assert A/A0==Q(peerrow['squared_C0R_ratio']) and B/B0==Q(peerrow['squared_C1R_ratio'])
    rows.append({'name':row['name'],'s':str(s),'R':str(R),'positive_A_difference':str(A0-A),'positive_B_difference':str(B0-B),'both_ratios_exactly_equal':True})
assert len(rows)==7
out={'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':sha(ROOT/'PROOF.md'),'code_sha256':sha(Path(__file__)),'parameter_sha256':sha(params),'prior_point_sha256':sha(old),'peer_sha256':sha(peer),'rows':rows,'safe_gap_lower_bound':'2.9392836795','elapsed_seconds':time.monotonic()-start}
(ROOT/'verification/results.json').write_text(json.dumps(out,indent=2)+'\n')
print('all14 strict rational comparisons confirmed',out['elapsed_seconds'])

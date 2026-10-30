"""Confirm the archived independent uniform-point calculation and its inputs."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json,time
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/point_witness'
def H(p):return sha256(p.read_bytes()).hexdigest()
def run():
 start=time.monotonic();ctx.prec=1024
 dest=BASE/'verification/T4_122_confirmation.json';assert not dest.exists()
 archive=BASE/'peer_review/T4_122';peer=json.loads((archive/'results.json').read_text())
 ownfile=BASE/'verification/candidate007_uniform_graded.json';own=json.loads(ownfile.read_text())
 mapping={'PROOF.md':archive/'PROOF.md','code/check.py':archive/'check.py',
          'data/own_point.json':ROOT/'research/candidate_audits/peer_review/T4_007/point.json',
          'source/N4_result.json':ownfile}
 for k,p in mapping.items():assert peer['inputs'][k]==H(p),(k,p)
 count=0
 for k,v in peer['uniform_values'].items():
  assert arb(v).overlaps(arb(own[k])),k
  count+=1
 for row in peer['finite_boxes']:
  target=next(r for r in own['finite_boxes'] if r['framework']==row['framework'])
  assert row['s']==target['s']
  for k,l in [('radius','H2s_radius_upper'),('upper','point_upper'),('gap','positive_gap')]:
   assert arb(row[k]).overlaps(arb(target[l])),(row['framework'],k)
   count+=1
  assert arb(row['gap'])>0
 assert count==21 and peer['all_21_comparisons_agree']
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'code_sha256':H(Path(__file__)),
      'peer_result_sha256':H(archive/'results.json'),'own_result_sha256':H(ownfile),
      'all_input_hashes_verified':True,'component_overlaps':count,
      'all_gaps_positive':True,'elapsed_seconds':time.monotonic()-start,
      'scope':'Confirms N4-102 for its exact top margin, fixed c and five finite boxes. New margins or parameters are outside scope.'}
 dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':run()

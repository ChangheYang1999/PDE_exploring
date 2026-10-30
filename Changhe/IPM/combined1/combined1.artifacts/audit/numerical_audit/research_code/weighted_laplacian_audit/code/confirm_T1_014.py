"""Preserve and identify the theory review for the audited d2 dyadic cover."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json,time
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/weighted_laplacian_audit'
def H(p):return sha256(p.read_bytes()).hexdigest()
def run():
 start=time.monotonic();dest=BASE/'verification/T1_014_confirmation.json';assert not dest.exists()
 a=BASE/'peer_review/T1_014'
 expected={'REVIEWS_v10.md':'33513ce7d3ea000c58df52f1f37a92bec927b2154c1470df70bf749da45abf21',
           'check_T4107.py':'5722485a34cd67d5ecc8dbddfc67de347df34270c542988462ae3c29b1e8c4b7',
           'check_T4107.out':'3208fb4cddfeb8f51a268ec775beb77af5252410bc591c5dd88ea5a4da86256a'}
 for name,h in expected.items():assert H(a/name)==h,name
 reviewed={BASE/'source/T4_PROOF.md':'516e3d20063b96b21e073638fa532ff861e40c2231b6a7a1fff11e64983fa422',
           BASE/'peer_review/T4_116/UNIFORM_COVER.md':'c7253f73c992f0d87e1d90feb770f6d08ccf0c075935972ca6ef5db5cf9eaab4'}
 for p,h in reviewed.items():assert H(p)==h,p
 assert 'ALL OK' in (a/'check_T4107.out').read_text()
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'code_sha256':H(Path(__file__)),
      'review_archive_sha256':{p.name:H(p) for p in sorted(a.iterdir()) if p.is_file()},
      'reviewed_sources_sha256':{str(p.relative_to(ROOT)):h for p,h in reviewed.items()},
      'all_hashes_match':True,'elapsed_seconds':time.monotonic()-start,
      'review_status':'Full text read; plateau proof, change of variables, seven-cell logic and d2 applicability checked.',
      'directed_arithmetic_source':'verification/T4_116_cover_confirmation.json',
      'scope':'Together with independently confirmed arithmetic and the already reviewed inverse floor, excludes d2 from FW-T-DYADIC-Y-v1 for all 0<a<2, 0<s<1 and finite positive Rw under its hypotheses.',
      'rounding_correction':'The review prints sqrt(10*pi) as an upper bound5.604991. This is false at the last digit; use5.604992. Rounded display columns are illustrative; use the outward ball records for inequalities.'}
 dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':run()

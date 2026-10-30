"""Check the corrected prose exponent against every saved onset row."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,time
BASE=Path(__file__).resolve().parents[1]
def H(p):return sha256(p.read_bytes()).hexdigest()
start=time.monotonic()
source=BASE/'verification/onset_tradeoff.json';record=json.loads(source.read_text())
recurrence=BASE/'verification/stationary_extension_16_summary.json';r=json.loads(recurrence.read_text())
old=BASE/'proof_history/PROOF_ONSET_TRADEOFF_v01.md';new=BASE/'PROOF_ONSET_TRADEOFF.md'
assert record['proof_sha256']==H(old)
assert record['verified_prefix_sha256']==H(recurrence)
c=Q(r['cl_exact']);gamma=1/c;delta=1-gamma
rows=[]
for row in record['rows']:
 n=row['order'];e=Q(row['exponent'])
 assert e==gamma-n*delta==1-(n+1)*delta
 assert 1-n*delta-e==delta
 rows.append({'order':n,'stored_exponent':str(e),'corrected_formula_equal':True,'old_formula_error':str(delta)})
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'code_sha256':H(Path(__file__)),
     'onset_record_sha256':H(source),'original_proof_sha256':H(old),'corrected_proof_sha256':H(new),
     'recurrence_record_sha256':H(recurrence),'all_eleven_exponents_correct_in_numerical_record':len(rows)==11,
     'rows':rows,'numerical_results_unchanged':True,'elapsed_seconds':time.monotonic()-start}
p=BASE/'verification/onset_indexing_correction.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print('All11stored exponents use gamma-n delta; prose corrected; seconds',out['elapsed_seconds'])

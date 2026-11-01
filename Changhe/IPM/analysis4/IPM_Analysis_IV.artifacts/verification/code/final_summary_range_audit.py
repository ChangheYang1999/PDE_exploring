"""Check a stale summary range against an admitted finite fit."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import gzip,json
from fractions import Fraction

base=Path('research/299_final_summary_consistency')
source=Path('research/298_period_ten_floating_audit/verification/checks.json.gz')
obj=json.loads(gzip.decompress(source.read_bytes()))
assert obj['all_checks_pass']
row=next(x for x in obj['results'] if x['root_index']==1)
checks=[]
for fit in row['fits']:
 for channel in fit['channels']:
  center,error=channel['R'].strip('[]').split(' +/- ')
  lower=Fraction(center)-Fraction(error)
  assert lower>10**6
  checks.append(dict(cutoff=fit['lo'],channel=channel['channel'],radius=channel['R'],strictly_above_million=True))
summary=(base/'sources/FINAL_SUMMARY.md').read_text()
assert r'about $0.05$ and $10^6$' in summary
scope=(base/'sources/FARFIELD_CONVERGENCE_THEORY.md').read_text()
assert r'$Q\ge10$' in scope
genericity=Path('research/287_period_ten_genericity/verification/admission.json')
admitted=json.loads(genericity.read_text())
assert admitted.get('verdict')=='PROVED'
result=dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,
 original_range_verdict='REFUTED as a range of all currently reported finite fits',
 original_open_list_verdict='REFUTED as a current list of unadmitted periods',
 checks=checks,source=dict(path=str(source),sha256=sha256(source.read_bytes()).hexdigest()),
 genericity=dict(path=str(genericity),sha256=sha256(genericity.read_bytes()).hexdigest()),
 scope='Only finite fit coverage and the current admission list. No new asymptotic bound.')
(base/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
(base/'sources/final_summary_range_audit.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(result))

from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import hashlib,json
from flint import arb,ctx
ctx.prec=768
root=Path(__file__).resolve().parents[1]
src=root/'source/weighted_weak_sharp_results.json'
fix=root/'source/wws_directed_floor.json'
original=json.loads(src.read_text());corrected=json.loads(fix.read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert corrected['source_sha256']==sha(src)
rows=[]
for kind,data in original.items():
 for row in data:
  cr=[r for r in corrected['rows'] if r['kind']==kind and r['candidate']==row['candidate'] and r['a']==row['a'] and r.get('k')==row.get('k')]
  assert len(cr)==1
  cr=cr[0]
  I=abs(arb(row['pairing']));cu=arb(2) if row['a']=='1' else arb(808233)/500000
  D=arb(row['M'])+cu*arb(row['C'])
  value=2*I/(D+(D*D+4*cu*arb(row['H_upper'])*I).sqrt())
  assert arb(cr['floor8'])<value and arb(cr['floor12'])<value
  assert arb(cr['ball']).overlaps(value)
  rows.append({'kind':kind,'candidate':row['candidate'],'a':row['a'],'k':row.get('k'),'floor8':cr['floor8'],'floor12':cr['floor12'],'checked':True})
assert len(rows)==34
out={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(src),'correction_sha256':sha(fix),'code_sha256':sha(__file__),'precision_bits':ctx.prec,'rows':rows,'scope':'component reconstruction only, not independent field arithmetic'}
dest=root/'verification/directed_floor_fix.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2)+'\n')
print('34 rows: both corrected decimals strictly below formula enclosure; source hash agrees.')

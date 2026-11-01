"""Compare frozen printed necessary bounds with admitted exact lower endpoints."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import re,json,time
started=time.monotonic()
base=Path('research/301_final_claim_audit')
snap=base/'verification/20261031T221828Z'
p=snap/'lead_report.md';text=p.read_text()
refs=[dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest())]
rows=[]
def read(q):
 p=Path('research')/q/'verification/checks.json'
 refs.append(dict(path=str(p),sha256=sha256(p.read_bytes()).hexdigest()))
 d=json.loads(p.read_text());assert d['all_checks_pass'];return d

def check(label,printed,r,location):
 v=F(printed);lo,hi=map(F,r['radius_bounds_exact']);assert 0<v<lo<=hi,(label,printed)
 rows.append(dict(label=label,printed=printed,printed_exact=str(v),certified_lower=str(lo),certified_upper=str(hi),strictly_rounded_down=True,location=location))

pat=r'([0-9]+\.[0-9]+)(?:\\cdot10\^\{(-?\d+)\})?'

def extract(section,marker):
 t=text.split(section,1)[1].split('(d) Necessary radii',1)[1].split(marker,1)[1].split('times',1)[0]
 return [a+('e'+b if b else '') for a,b in re.findall(pat,t)]

groups=read('259_period_seven_eight_necessary_radii')['groups']
for Q in [7,8]:
 vals=extract(f'Corollary T_{Q} (explicit profiles', 'lower bounds are' if Q==7 else '^4$ are')
 source=next(g for g in groups if g['Q']==Q)['rows'];assert len(vals)==len(source)==10
 for v,r in zip(vals,source):check(f'Q{Q} root{r["root_index"]}',v,r,f'Corollary T_{Q}(d)')
for Q,q in [(9,'274_period_nine_necessary_radii'),(10,'288_period_ten_necessary_radii')]:
 vals=extract(f'Corollary T_{Q} (explicit profiles','$R>')
 source=read(q)['rows'];assert len(vals)==len(source)
 for v,r in zip(vals,source):check(f'Q{Q} root{r["root_index"]}',v,r,f'Corollary T_{Q}(d)')
for r,v in zip(read('245_extremal_necessary_radii')['rows'],['0.0902973','0.2365977','0.4954372']):
 assert v in text;check(f'single sin{r["mode"]}',v,r,'summary Section2 and harmonic corollary')
for r,v in zip(read('248_four_sevenths_necessary_radii')['rows'],['0.0127184','0.0430461','0.880537']):
 assert v in text;check(f'delta4/7 root{r["root_index"]}',v,r,'summary Section2')
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
out=dict(checked_at_utc=now,all_checks_pass=True,scope='Printed downward rounding only, relying on the previously admitted exact radius enclosures. No new gamma-function evaluation or sharp-radius assertion.',sources=refs,count=len(rows),rows=rows,elapsed_s=time.monotonic()-started)
(base/'verification/necessary_radius_transcription.json').write_text(json.dumps(out,indent=2)+'\n')
(base/'sources/final_necessary_radius_audit.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps({k:v for k,v in out.items() if k not in ['sources','rows']}))

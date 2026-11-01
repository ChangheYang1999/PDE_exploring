"""Interval check of the replacement conditional canonical radii."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time
from flint import arb,fmpq,ctx
ctx.prec=512
start=time.monotonic()
rows=[]
for R,p in [(109,2),(110,2),(45,1),(46,1)]:
 q=arb(fmpq(204,25))*(-arb(R).log()*2/3).exp()*(arb(R).log().log()*p/3).exp()
 rows.append(dict(radius=R,log_power=str(fmpq(p,3)),q=q.str(70,radius=True),strictly_less_than_one=bool(q<1),strictly_greater_than_one=bool(q>1)))
assert [r['strictly_less_than_one'] for r in rows]==[False,True,False,True]
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
out=Path('research/82_weighted_loss_criterion/verification')/('conditional_H034_'+stamp);out.mkdir()
source=Path('../a4-lead/FARFIELD_CONVERGENCE_THEORY.md').read_text()
startpos=source.index(r'For $\delta=2/3$ and $f_1=\sin\theta$ ($n_r=3$')
endpos=source.index('Relation to Sections 14.5',startpos)
(out/'claim_excerpt.md').write_text(source[startpos:endpos])
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),hypothesis='All-order N_n/M_n <= 17/50 remains OPEN; results below check its conditional numerical radii only.',A='204/25',precision_bits=512,rows=rows,actual_elapsed_s=time.monotonic()-start)
(out/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'code.py.txt').write_bytes(Path(__file__).read_bytes())
files={p.name:dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in out.iterdir()}
(out/'MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
print(json.dumps(dict(output=str(out),**result)),flush=True)

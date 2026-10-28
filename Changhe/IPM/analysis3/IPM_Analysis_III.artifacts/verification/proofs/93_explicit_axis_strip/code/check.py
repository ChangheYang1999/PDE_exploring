from flint import arb,ctx
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
ctx.threads=1
p=Path(__file__).resolve().parents[1]
rows=[]
for prec in (256,384):
 ctx.prec=prec
 a=arb(17)/4
 b1=1/(2*a+1).sqrt()
 b2=((2*a+1).gamma()/arb(2)**(2*a+1)).sqrt()
 assert b2>b1
 B=b2
 C=1+10*arb(2)**(a+arb(1)/2)+64*(1+1/(arb(9)/2-a))+2*sum(1/(a+v) for v in (arb(1)/2,-arb(1)/2,-arb(3)/2,-arb(5)/2))
 D=C+B/(9-2*a).sqrt()
 assert C<593
 assert D<612
 rows.append({'bits':prec,'B':B.str(80),'C':C.str(80),'D':D.str(80),'safe_C':'593','safe_D':'612'})
o={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','rows':rows,'proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(o,indent=2)+'\n')
print(o['date'],o['status'],rows[0])

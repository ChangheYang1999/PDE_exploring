from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib,json
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'source/N4_cartesian_witnesses.json'
a=json.loads(p.read_text())
assert Q(3,200)**2/3 < Q(87,10000)**2
assert Q(1,6000)**2/10 < Q(53,1000000)**2
assert Q(87,10000)*Q(53,1000000)<Q(1,2000000)
rows=[]
for row in a['rows']:
 f=row['fields'];F=abs(arb(f['residual']));V=arb(f['velocity_norm']);D=arb(f['gradient_norm'])
 upper=arb(87)/10000*V+arb(53)/1000000*(1+D)+arb(1)/2000000
 gap=F-upper
 assert gap>0
 rows.append({'candidate':row['candidate'],'point':row['point'],'canonical_sha256':row['canonical_sha256'],
              'absolute_residual':F.str(65),'necessary_upper':upper.str(65),'gap':gap.str(65),'strictly_positive':True})
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
     'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'scope':'Every scalar-gap ball mu-4800s-5r/sqrt(s)>0 with 0<mu<=3/10',
     'constant_relaxations':'exact Fraction square comparisons passed','rows':rows}
(ROOT/'verification/witnesses.json').write_text(json.dumps(out,indent=2)+'\n')
for row in rows:print(row['candidate'],row['gap'])

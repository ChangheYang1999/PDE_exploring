"""Independently compare the last seven printed-multiplier regressions."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
from flint import arb,ctx
import json,time
start=time.monotonic();ctx.prec=768
base=Path('research/305_final_conditional_fit_scope')
source=Path('../a4-num/notes/drift_fit_348_440.txt')
raw=source.read_bytes();(base/'sources/drift_fit_348_440.txt').write_bytes(raw)
orders=list(range(420,439,3))
values=['0.02541','0.02551','0.02562','0.02572','0.02582','0.02593','0.02603']
for n,v in zip(orders,values):assert f'{n}:-{v}' in raw.decode()
def exact(q):
 q=F(q);return arb(q.numerator)/q.denominator
y=[exact(v).log()/arb(10).log() for v in values]
fits={};rmsvals={}
for label,x in [('power',[arb(n).log()/arb(10).log() for n in orders]),('inverse_order',[arb(1)/n for n in orders]),('exponential',[arb(n) for n in orders])]:
 m=len(x);sx=sum(x);sy=sum(y);sxx=sum(t*t for t in x);sxy=sum(u*v for u,v in zip(x,y));syy=sum(t*t for t in y)
 D=sxx-sx*sx/m;assert D>0
 c=(sxy-sx*sy/m)/D;b=(sy-c*sx)/m
 residual=sum((v-b-c*u)**2 for u,v in zip(x,y))/m
 alternate=(syy-sy*sy/m-(sxy-sx*sy/m)**2/D)/m
 assert residual.overlaps(alternate) and residual>0
 rms=residual.sqrt();rmsvals[label]=rms
 fits[label]=dict(intercept=b.str(50),slope=c.str(50),rms=rms.str(50),normal_equation_identity_overlaps=True)
assert rmsvals['power']<rmsvals['exponential']<rmsvals['inverse_order']
now=datetime.now(timezone.utc).isoformat(timespec='seconds')
result=dict(at=now,source=dict(path=str(source),sha256=sha256(raw).hexdigest()),frozen_source=dict(path=str(base/'sources/drift_fit_348_440.txt'),sha256=sha256(raw).hexdigest()),orders=orders,printed_absolute_multipliers=values,arithmetic='768-bit directed real balls; decimals exact rational',fits=fits,strict_order='power < exponential < inverse_order',all_checks_pass=True,scope='Printed-data finite regression only. Universal exponential-fit ranking is false for these inputs; infinite laws remain open.',actual_elapsed_s=time.monotonic()-start)
(base/'verification/printed_fit_checks.json').write_text(json.dumps(result,indent=2)+'\n')
(base/'sources/final_conditional_fit_scope.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(result,indent=2))

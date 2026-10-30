"""Audit frozen quadrature witnesses by a trigonometric recurrence."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import json,hashlib,time
ctx.prec=512
ROOT=Path(__file__).resolve().parents[1]
def A(q):
 q=Q(q);return arb(q.numerator)/q.denominator
start=time.monotonic()
p=ROOT/'source/N4_witness.json'
z=json.loads(p.read_text());rows=[]
for item in z['results']:
 coefs=item['integer_sine_coefficients']
 assert len(coefs)==2*item['M']+2
 exact=arb.pi()/4*sum(c*c for c in coefs)
 quadrature=arb(0)
 assert len(item['nodes'])==len(item['weights'])==item['N']
 for t,w in zip(item['nodes'],item['weights']):
  t=A(t);w=A(w)
  assert w>0
  # sin((2k+1)t) obeys s[k+1]=2cos(2t)s[k]-s[k-1].
  scale=2*(2*t).cos()
  previous=t.sin();current=(1+scale)*previous
  value=coefs[0]*previous+coefs[1]*current
  for coef in coefs[2:]:
   previous,current=current,scale*current-previous
   value+=coef*current
  quadrature+=w*value*value
 ratio=quadrature/exact
 assert ratio>=0 and ratio<arb(1)/10**6
 assert ratio.overlaps(arb(item['quadrature_to_integral_ratio']))
 rows.append({'M':item['M'],'N':item['N'],'quadrature_to_integral_ratio':ratio.str(100),
              'strictly_below_one_millionth':True,'N4_interval_overlap':True})
result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
 'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'method':'Exact rational frozen nodes, weights and coefficients; 512-bit Arb odd-sine recurrence rather than separately evaluating each sine.',
 'rows':rows,'elapsed_seconds':time.monotonic()-start,
 'scope':'Quadrature rule witnesses on the full allowed angular space. No claim that these polynomials are actual candidate residuals, or that a particular candidate loss has this error.'}
(ROOT/'verification/witness_reproduction.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

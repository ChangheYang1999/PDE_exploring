"""Exact frozen quadratic-form audit from source reconstruction, no floats in tests."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
ctx.prec=256
p=ROOT/'source_audit/state131_exact.json';data=json.loads(p.read_text())
c=Q(data['exact_parameters']['cl']);a0=Q(data['exact_parameters']['a0']);d=2*c-2;s=Q(11,5)
a11=c*(s-2)-1-a0/4-d*(s-1)/4
a33=c*(s-2)-1-a0/2
a13=3*(s+1)*(d/4-a0/(4*(s-3)))
a31=(s-3)/3*(d/4-a0/(4*(s+1)))
ray=(a11+a33+a13+a31)/2
simplified=c/5-1+61*d/60+109*a0/96
assert ray==simplified and ray>12

def ar(q):return arb(q.numerator)/q.denominator
# Independent direct source-amplitude formula: h has amplitudes 1 and 3,
# while potential has amplitudes 1 and 1/3 at tau=0.
source={-3:Q(-3),-1:Q(-1),1:Q(1),3:Q(3)}
output={}
for n,v in source.items():
 output[n]=output.get(n,Q(0))+(c*(s-2)-1-a0/2)*v
 up=(s-n-2)*d/4-a0*(s-n-2)/(4*(s+n))
 down=(s+n-2)*d/4-a0*(s+n-2)/(4*(s-n))
 output[n+2]=output.get(n+2,Q(0))+up*v
 output[n-2]=output.get(n-2,Q(0))+down*v
pair=sum((output[n]*source[n]/(n*n) for n in source),Q(0))
norm=sum((v*v/(n*n) for n,v in source.items()),Q(0))
assert pair/norm==ray
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'status':'CONFIRMED','source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'s':str(s),'c':str(c),'a0':str(a0),'matrix':[[str(a11),str(a13)],[str(a31),str(a33)]],'rayleigh_quotient_exact':str(ray),'rayleigh_quotient_arb':ar(ray).str(60),'strict_lower_bound':12,'beurling_norm':12,'velocity_norm_upper':'13/2','independent_source_amplitude_check':True}
(HERE/'matrix_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

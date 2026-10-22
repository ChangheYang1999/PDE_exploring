"""Exact knot multiplicity plus independent ball separation, no spline producer."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
from mpmath import iv
import json,hashlib,collections
D=Path(__file__).resolve().parents[1];B=D.parents[1];ctx.prec=256;iv.dps=100
src=B/'data_exact/modal_v2.json';d=json.loads(src.read_text());ks=[F.from_float(float.fromhex(s)) for s in d['arrays']['knots']['hex']]
assert d['degree']==7 and d['arrays']['knots']['shape']==[1573] and len(ks)==1573
assert all(a<=z for a,z in zip(ks,ks[1:]))
counts=collections.Counter(ks);uniq=sorted(counts);assert counts[uniq[0]]==8 and counts[uniq[-1]]==8
assert len(uniq)==1559 and all(counts[t]==1 for t in uniq[1:-1]);assert ks[7]==uniq[0] and ks[-8]==uniq[-1]
raw=json.loads((D/'source/runs/forcing/p9_K64_n16_P8_merged.json').read_text());lo,hi=[F.from_float(x) for x in raw['x_star_bracket']];R=F(99,2000)
def a(q):return arb(q.numerator)/q.denominator
def v(q):return iv.mpf(q.numerator)/q.denominator
ar=[a(lo-R)-a(uniq[0]).exp(),a(uniq[-1]).exp()-a(hi+R)]
ir=[v(lo-R)-iv.exp(v(uniq[0])),iv.exp(v(uniq[-1]))-v(hi+R)]
assert all(x.lower()>0 for x in ar) and all(x.a>0 for x in ir)
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_MODAL_LOCAL_REGULARITY_DATA','source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'degree':7,'knots':len(ks),'distinct_knots':len(uniq),'simple_interior_knots':len(uniq)-2,'endpoint_multiplicities':[8,8],'arb_margins':list(map(str,ar)),'iv_margins':list(map(str,ir)),'scope':'Modal density C6, canonical velocity C6, residual C5 locally, conditional on the exact canonical modal definition; no numeric Green enclosure.'}
(D/'evidence/regularity.json').write_text(json.dumps(o,indent=2)+'\n');print(o['utc'],o['status'])

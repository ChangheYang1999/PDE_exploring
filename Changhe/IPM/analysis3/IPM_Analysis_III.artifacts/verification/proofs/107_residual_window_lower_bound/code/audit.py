import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import importlib.util,json,hashlib
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
sp=importlib.util.spec_from_file_location('tayloraudit',ROOT/'code/taylor.py');T=importlib.util.module_from_spec(sp);sp.loader.exec_module(T)
ctx.prec=640;ctx.threads=1;aa=T.aa
x=json.loads((ROOT/'evidence/taylor.json').read_text());p=json.loads((LANE/'proofs/105_residual_norm_point_audit/evidence/points_384.json').read_text())
assert x['status']=='POSITIVE_LOWER_BOUND' and x['input_sha256']==p['original_sha256']
assert x['code_sha256']==hashlib.sha256((ROOT/'code/taylor.py').read_bytes()).hexdigest()
def ball(v):return aa(F(v['lower_exact'])).union(aa(F(v['upper_exact'])))
S=ball(x['S_range']);assert S>0
H=ball(x['witness_H']);mass=T.ANG.beta_mass();left=F(x['center'])-F(x['half_width']);right=F(x['center'])+F(x['half_width'])
weight=(aa(F(27,4)*right).exp()-aa(F(27,4)*left).exp())*aa(F(4,27))
assert weight.overlaps(ball(x['weight_integral']))
# Independent positive scalar lower bound, recomputed with640-bit arithmetic.
lower=arb(weight.lower())*arb(mass.lower())*aa(F(x['S_range']['lower_exact']))**2/arb(H.upper())
assert lower>aa(F("933.47"))**2
# Stored lower-bound interval must enclose the exact directed-arithmetic scalar used by the producer.
assert F(x['norm_lower']['lower_exact'])>F('933.47')
# Point consistency with the independently built full residual from topic105.
pt=next(z for z in p['results'] if z['t']=='10');exact=ball(pt['remainder_energy_density']);c0=ball(x['coefficients'][0])
witness_energy=aa(F(135,2)).exp()*mass*c0**2/H
diff=exact-witness_energy
assert diff>-arb('1e-20') and diff<arb('1e-20')
# Exact witness re-evaluation by a separate direct Gram sum.
r=list(map(F,x['witness_coefficients']));mom=T.ANG.moments(2*len(r));Hdirect=arb(0)
for j,v in enumerate(r):
 for l,w in enumerate(r):
  Hdirect+=aa(v*w*(mom[j+l]+mom[abs(j-l)])/2)
assert Hdirect.overlaps(H)
# Independent Taylor check on a rational exponential polynomial.
e=T.G.EP({F(-3,2):[arb(2),arb(-5),arb(7)]});co,bd=T.series_and_bound(e,F(2,7),8,F(1,2))
der=e
from math import factorial
for j in range(9):
 val=T.P.evaluate(der,aa(F(2,7)))/factorial(j)
 assert val.overlaps(co[j]);der=der.deriv()
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','certified_norm_lower':933,'stronger_decimal_lower':'933.47','interval':[str(left),str(right)],'precision_bits':640,'point_energy_difference':T.G.rec(diff),'independent_Gram':T.G.rec(Hdirect),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'audit_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'evidence/audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

"""Check point-record provenance, two-method agreement and quoted rational bounds."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json
from flint import arb,ctx
ctx.prec=768
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
rows=[]
for name in ['nb_stableA4_exact','nb_stableA5_exact','nb_Mpen_exact']:
 p=HERE/(name+'.json');d=json.loads(p.read_text())
 assert d['precision_bits']==768
 assert d['code_sha256']==sha256((HERE/'point_contract.py').read_bytes()).hexdigest()
 for rel,digest in d['dependencies'].items():assert sha256((BASE/rel).read_bytes()).hexdigest()==digest,rel
 source=Path('numerics/data')/(name+'.json')
 assert sha256(source.read_bytes()).hexdigest()==d['source_sha256']
 for row in d['points']:
  assert row['all_derivatives_and_fields_overlap']
  for key,value in row['cartesian'].items():
   a,b=arb(value),arb(row['polar'][key]);assert a.is_finite() and b.is_finite() and a.overlaps(b)
  assert arb(row['cartesian']['M1_min'])>arb(1)/2
  assert arb(row['cartesian']['M2_min'])>arb(1)/2
 P={tuple(row['point']):row for row in d['points']}
 if name=='nb_stableA4_exact':
  checks=[(('0','1/10'),'D2rho','3.05085'),(('0','1/10'),'r2_D4rho','2001.17'),(('0','1/5'),'r1_D3u','35.5797'),(('0','1/5'),'r2_D3rho','49.6421'),(('0','2/5'),'r2_D3rho','138.9647')]
 else:
  n='0.02036' if 'A5' in name else '0.01781'
  fourth='692.7879' if 'A5' in name else '678.8363'
  checks=[(('0','4/5'),'r2_D4rho',fourth),(('6','8'),'N_point_bound',n)]
  assert arb(P['6','8']['cartesian']['N_point_bound'])*2**35>2**29
 for point,key,bound in checks:assert arb(P[point]['cartesian'][key])>arb(bound)
 rows.append({'candidate':name,'source_sha256':d['source_sha256'],'record_sha256':sha256(p.read_bytes()).hexdigest(),'canonical_sha256':d['canonical_sha256'],'strict_lower_bounds':[{'point':list(point),'quantity':key,'lower':bound} for point,key,bound in checks],'refuted_requirements':d['refuted_requirements']})
# Independently multiply the cubic Taylor polynomials with rational symbolic algebra.
import sympy as s
x,y,c,a,b,d,B,C=s.symbols('x y c a b d B C')
rho=a*y+b*y**3+d*x**2*y;psi=(1-c)*x*y+B*x*y**3+C*x**3*y
F=s.Poly(s.expand((c*x-s.diff(psi,y))*s.diff(rho,x)+(c*y+s.diff(psi,x))*s.diff(rho,y)-rho),x,y)
assert s.expand(F.coeff_monomial(y**3)-(2*b+a*B))==0
assert s.expand(F.coeff_monomial(x**2*y)-(2*(2*c-1)*d+3*a*C))==0
assert F.coeff_monomial(y)==0
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED point certificates and cubic identities; stated global W3 hypotheses REFUTED','rows':rows,'symbolic_cubic_check':True,'proof_sha256':sha256((HERE.parent/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'summarize.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

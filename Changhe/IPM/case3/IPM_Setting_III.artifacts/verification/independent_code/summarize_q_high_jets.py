"""Aggregate exact center derivatives with an explicitly conditional scale quotient."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
from decimal import Decimal,localcontext
import math,sys
sys.set_int_max_str_digits(1000000)
root=Path('evidence/q_canonical_high_jets');rows=[]
for path in sorted(root.glob('R1C_CL3P0_N*/diagnostic.json'),key=lambda p:int(p.parent.name.rsplit('N',1)[1])):
 d=json.loads(path.read_text()); assert d['poisson_exact_zero']
 assert hashlib.sha256(Path(d['source']).read_bytes()).hexdigest()==d['source_sha256']
 a=F(d['a_exact']);b=next(F(x['core_exact'])for x in d['rows']if x['field']=='rho'and(x['x_power'],x['y_power'])==(2,1));assert a and b
 inp=json.loads((path.parent/'exact_input.json').read_text());m0=float(F(inp['L']))*2**(-float(F(inp['kappa'])))
 core2=abs(a/b);bydegree=[]
 for field in ['rho','R']:
  for degree in [1,3,5,7]:
   terms=[x for x in d['rows']if x['field']==field and x['degree']==degree]
   raw=sum((abs(F(x['core_exact']))for x in terms),F(0));normalized=raw*core2**((degree-1)//2)/abs(a)
   with localcontext()as ctx:
    ctx.prec=80;physical=sum((abs(Decimal(x['physical_decimal']))for x in terms),Decimal(0))
   bydegree.append(dict(field=field,degree=degree,core_sum_abs_coefficients_exact=str(raw),sum_abs_coefficients=float(physical),core_scaled_sum_over_abs_a_exact=str(normalized),core_scaled_sum_over_abs_a=float(normalized)))
 rows.append(dict(tag=path.parent.name,source=d['source'],source_sha256=d['source_sha256'],diagnostic_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),a=float(a),delta=float(F(d['delta_exact'])),normalized_coordinate_core_squared_exact=str(core2),physical_core_factor='L*2^(-kappa)*sqrt(abs(a/b_core))',core=m0*float(core2)**.5,by_degree=bydegree))
now=datetime.now(timezone.utc).isoformat();out=dict(utc=now,rows=rows,scope='Exact normalized-coordinate Taylor coefficients of five frozen finite Q formulas, with approximate physical conversion. The stored kappa is6755399441055743/4503599627370496, not exactly3/2; nonrational length factors are not relabeled exact. Coefficient sums are not function norms. Core rescaling uses r_star=sqrt(abs(a/b)) only for these states with b!=0; it is not asserted to normalize every admissible profile. Neither raw nor rescaled derivative growth decides regularity of an unknown limiting profile.',code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(root/'SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n')
text=['# Exact Q Taylor refinement diagnostics','',now,'',out['scope'],'','The stored formulas are smooth at zero. A limiting finite-regularity interpretation requires additional convergence evidence; these tables alone do not establish it. The residual polynomial uses the canonical full-plane stream, including the exterior harmonic coefficients. No center relation is repaired.','','| State | a | delta | r_star | sum abs R degree3 | degree5 | degree7 |','|---|---:|---:|---:|---:|---:|---:|']
for row in rows:
 rr={z['degree']:z for z in row['by_degree']if z['field']=='R'}
 text.append('| '+row['tag']+' | '+' | '.join(f'{v:.12g}'for v in [row['a'],row['delta'],row['core'],rr[3]['sum_abs_coefficients'],rr[5]['sum_abs_coefficients'],rr[7]['sum_abs_coefficients']])+' |')
text+=['','After changing variables X=r_star Z and dividing density/residual by a*r_star, a monomial coefficient of degree d is multiplied by r_star^(d-1)/a. These dimensionless absolute coefficient sums remove this particular spatial scale.','','| State | rho degree3 | rho degree5 | rho degree7 | R degree3 | R degree5 | R degree7 |','|---|---:|---:|---:|---:|---:|---:|']
for row in rows:
 z={(x['field'],x['degree']):x for x in row['by_degree']}
 text.append('| '+row['tag']+' | '+' | '.join(f'{z[field,deg]["core_scaled_sum_over_abs_a"]:.12g}'for field in ['rho','R']for deg in [3,5,7])+' |')
text+=['','CONFIRMED: these exact finite-formula derivatives and the stated scaling arithmetic. OPEN: convergence in a smooth topology, a finite Holder exponent of a limit, and the full primary endpoint.','']
(root/'SUMMARY.md').write_text('\n'.join(text));print('\n'.join(text[:14]))

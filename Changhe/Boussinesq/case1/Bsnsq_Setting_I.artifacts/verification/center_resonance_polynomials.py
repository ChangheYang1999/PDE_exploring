"""Exact rational recurrence denominator and Sturm real-root isolation, beta=3."""
import json,datetime
from pathlib import Path
import sympy as s
a=s.Symbol('a');rows=[]
for n in range(1,13):
 coeff=s.Poly(1,a);den=coeff
 for j in range(n):
  i=n-1-j;L=2*n+8*i+8;M=2*n+8*i+5;A=(2*i+3)*(2*i+2);B=(2*j+3)*(2*j+2)
  coeff=coeff*s.Poly(s.Rational(A,B)*(1-a/s.Integer(L*M)),a);den+=coeff
 primitive=den.clear_denoms()[1].primitive()[1]
 if primitive.LC()<0:primitive=-primitive
 roots=s.polys.polytools.intervals(primitive,eps=s.Rational(1,10**12));facts=s.factor_list(primitive.as_expr())
 row={'n':n,'beta':3,'primitive_coefficients_descending':[str(c) for c in primitive.all_coeffs()],'factorization':str(facts),'sturm_real_roots':[{'low':str(t[0]),'high':str(t[1]),'multiplicity':m,'midpoint':float((t[0]+t[1])/2)} for t,m in roots],'real_roots_below_70':int(primitive.count_roots(-s.oo,70)),'denominator_at_0':str(den.eval(0))};rows.append(row);print(json.dumps(row),flush=True)
Path('runs/high_order_jets/resonance_polynomials.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'arithmetic':'exact rational coefficients and Sturm real-root intervals; midpoints only are float','rows':rows},indent=2)+'\n')

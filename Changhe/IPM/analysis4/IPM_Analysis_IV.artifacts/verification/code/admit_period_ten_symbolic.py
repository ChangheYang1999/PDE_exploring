"""Admit the Q10 symbolic response without overstating producer comparison."""
from pathlib import Path
from fractions import Fraction as F
import argparse
from flint import fmpq,fmpq_poly
from certificate_admission import read,ref,checkref,admit
ap=argparse.ArgumentParser();ap.add_argument('--entry',type=int,required=True);a=ap.parse_args()
base=Path('research/282_period_ten_symbolic_response');v=base/'verification';d=read(v/'checks.json');g=read(v/'reduced_generic.json.gz');small=read(v/'small_responses.json.gz');factors=read(v/'factors.json')
assert d['all_checks_pass'] and d['period']==10 and d['distinct_b_values']==[0,1,-1,2,-2,3,-3,4,-4,5,-5]
assert d['direct_generic_matches']==list(range(21,27)) and d['small_degrees']=={str(k):10 for k in range(2,21)}
for r in d['inputs']+d['sources']:checkref(r)
p=lambda c:fmpq_poly([fmpq(x) for x in c]);N=list(map(p,g['numerator_by_b_degree']));D=p(g['denominator']);G=p(g['coefficient_gcd']);assert len(N)==11 and D[D.degree()]==1
calc=fmpq_poly([])
for c in N:calc=calc.gcd(c)
calc=calc/calc[calc.degree()];assert calc==G
for label,target in [('denominator',D),('coefficient_gcd',G)]:
 data=factors['factor_data'][label];q=fmpq_poly([fmpq(data['scalar'])])
 for r in data['factors']:
  f=p(r['coefficients']);assert f.degree()==1 and fmpq(r['root'])==-f[0]/f[1]
  rt=F(r['root']);assert not(rt.denominator==1 and rt>=21);q*=f**r['multiplicity']
 assert q==target
assert all(c.degree()<=D.degree() for c in N)
limit=fmpq_poly([c[D.degree()] for c in N]);assert limit==p(d['limit_coefficients'])==p(factors['limit_coefficients']) and limit.degree()==10
assert [r['k'] for r in small['small']]==list(range(2,21)) and all(p(r['coefficients']).degree()==10 for r in small['small'])
finitepath=Path('research/281_period_ten_finite_algebra/verification/obstruction_admission.json');finite=read(finitepath);assert finite['verdict']=='PROVED_FINITE_ALGEBRA' and finite['degree']==20 and finite['root_count']==14
for k in ['evidence','proof','independent_comparison']:checkref(finite[k])
review=base/'sources/lead_review_20261031T203654Z.md';assert 'agree with them' in review.read_text()
result=f"The eleven exact Cartesian Q(k) calculations give b degree10, minimal denominator degree{D.degree()}, numerator degree{max(c.degree() for c in N)}, and numerator-coefficient gcd degree{G.degree()}. Every denominator and coefficient-gcd factor is exactly reconstructed and has no integer root at least21. All19 small responses at k2..20 and the limiting polynomial have degree10; six actual-integer calculations k21..26 agree with the generic formula. Every response and its limit is nonzero at all fourteen irreducible degree20 compatibility roots, so each root has a positive all-index response infimum. The computation took{d['actual_elapsed_s']:.6f}seconds."
admit(base,a.entry,'Exact period-ten response and qualitative tuning', 'Each of the fourteen period-ten compatibility roots has a positive all-index response infimum and hence a convergent tuned exterior series.', 'Exact Cartesian rational functions, degree-bounded interpolation, independent factor reassembly, direct small-carrier calculations, and the admitted general tuned convergence theorem131.',result,'The symbolic nonvanishing and its qualitative exterior-convergence implication are PROVED. The potential reconstruction follows132 and the mandatory first logarithm follows283. This entry supplies no numerical lower bound, explicit radius or full comparison with the lead response; those are separate checks.',v/'checks.json',review,dict(finite_algebra=ref(finitepath),root_count=14,degree_bound=10,denominator_degree=D.degree(),gcd_degree=G.degree()))
(base/'sources/admit_period_ten_symbolic.py').write_bytes(Path(__file__).read_bytes())

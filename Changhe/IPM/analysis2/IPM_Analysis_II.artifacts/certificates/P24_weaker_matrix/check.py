from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
inside=Q(5,2)-Q(11,5)*Q(37,20)/2
outside=1-Q(31,100)*Q(37,20)
assert inside==Q(93,200)>Q(2,5)
assert outside==Q(853,2000)>Q(2,5)
assert 14000**9<2**124
err=Q(22)+(1+Q(21,2))*186+Q(11,5)*(9*22+2*22+56*Q(5,7))
margin=Q(2,5)-err/14000
assert margin==Q(14093,70000)>Q(1,5)
c=Q(4076476460239181,2251799813685248)
def radius(cc):
 b=Q(3,5)+Q(9,10)*cc
 lo,hi=0,2**31
 while hi-lo>1:
  mid=(lo+hi)//2
  if 208**9<=b**9*mid**4:hi=mid
  else:lo=mid
 assert 208**9<=b**9*hi**4 and 208**9>b**9*(hi-1)**4
 return hi
original_radius=radius(c);uniform_radius=radius(Q(9,5))
assert original_radius<=27057
assert 208**9>(Q(3,5)+Q(9,10)*Q(9,5))**9*27057**4
files=['24_weaker_matrix/PROOF.md','24_weaker_matrix/verification/AUDIT.md','24_weaker_matrix/verification/lead_L1_received.md','07_weighted/LOW_INVERSE_PROOF.md','07_weighted/LOW_INVERSE_FAMILY_PROOF.md','07_weighted/SHARP_WEIGHTED_H2_PROOF.md','16_weighted_fractional/REFERENCE_AUDIT.md','16_weighted_fractional/PROOF.md','16_weighted_fractional/ROUGH_INVERSE_PROOF.md','16_weighted_fractional/SHARP_ROUGH_INVERSE_PROOF.md','18_fractional_constants/PROOF.md','20_real_velocity/PROOF.md','22_axis_constraints/PROOF.md']
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED','interior_constant_baseline':str(inside),'exterior_baseline':str(outside),'low_margin':str(margin),'retained_floor':'2/5+sigma*c*r^2/(R^2+r^2) on r<=2^31','constant_sufficient_floor':'5/2','same_high_and_nonlinear_constants':True,'new_reference_certified':False,'original_cl':str(c),'original_compact_radius':original_radius,'uniform_compact_radius':uniform_radius,'radius_27057_not_uniform_in_c':True,'dependencies':{f:hashlib.sha256((BASE/f).read_bytes()).hexdigest() for f in files},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

"""Admit directed period-ten necessary radii after independent proof review."""
from pathlib import Path
from fractions import Fraction as F
import argparse
from certificate_admission import read,ref,checkref,reviewed,admit
ap=argparse.ArgumentParser();ap.add_argument('--entry',type=int,required=True);ap.add_argument('--review',required=True);a=ap.parse_args();base=Path('research/288_period_ten_necessary_radii');p=base/'verification/checks.json';d=read(p)
assert d['all_checks_pass'] and d['arithmetic_bits']==[512,1024] and d['a']=='10/19' and d['beta']=='30/19' and d['four_d']=='1' and d['boundary_power']=='11/30'
assert len(d['rows'])==14 and len(d['exact_top_checks'])==20
for r in [d['source'],d['prefix_source']]:checkref(r)
for r in d['rows']:assert F(r['quoted_lower'])<F(r['radius_bounds_exact'][0])<F(r['radius_bounds_exact'][1])
review=reviewed(base,a.review)
result='The fourteen exact top-sector recurrences give R_H='+d['R_H']+'. For every branch, uniform weighted termwise convergence through two angular derivatives requires R>(|b_i|/R_H)^5|epsilon|^5. At equality the highest second-angular-derivative coefficient grows as n^(11/30), so the strict boundary is excluded. All20 exact top coefficients agree with the independent Cartesian prefix, both precision evaluations overlap, and all14 rounded-down constants lie strictly below the directed thresholds. The four finite scalar diagnostics at100,400,800,1500 agree with the independently reported rounding. Runtime'+str(d['actual_elapsed_s'])+'seconds.'
admit(base,a.entry,'Necessary radii for all period-ten branches','The stated strict necessary exterior thresholds follow from the highest Fourier sector.', 'Apply the proved scalar generating-function singularity, independently check exact prefix coefficients, and evaluate all root-dependent gamma constants at512 and1024 bits with directed arithmetic.',result,'These necessary radius bounds are PROVED. They are not sufficient conditions, optimal thresholds, or an independent proof of existence.',p,review)
(base/'sources/admit_period_ten_necessary.py').write_bytes(Path(__file__).read_bytes())

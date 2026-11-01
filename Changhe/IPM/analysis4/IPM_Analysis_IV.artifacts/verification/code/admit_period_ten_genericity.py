"""Admit the reviewed period-ten genericity specialization."""
from pathlib import Path
import argparse
from certificate_admission import read,ref,checkref,reviewed,admit
ap=argparse.ArgumentParser();ap.add_argument('--entry',type=int,required=True);ap.add_argument('--review',required=True);a=ap.parse_args();base=Path('research/287_period_ten_genericity');p=base/'verification/checks.json';d=read(p)
assert d['all_checks_pass'] and d['Q']==10 and d['degree']==20 and d['response_degree']==10 and d['root_count']==14 and not d['proper_factor_degree_intersection']
for r in d['checked_references']+[d['finite_evidence'],d['symbolic_evidence']]:checkref(r)
review=reviewed(base,a.review)
result='For every fixed even bandwidth B>=6 at delta1/5, the normalized regular compatibility hypersurface has an open dense, full-chart-measure subset on every connected component where every response is uniformly separated from zero. Each such profile has a unique convergent tuned exterior series; compact subsets admit one common sufficient exterior. For B6 the excluded set is countable and relatively closed, with accumulation only in the finite limiting-response zero set. Nonzero leading amplitude scales the responses by epsilon^10 and the physical radii by |epsilon|^5.'
admit(base,a.entry,'Period-ten genericity on regular compatibility components',result,'Monic full-degree irreducibility specialization, nonzero resultants, analytic zero sets, locally uniform compactified response limit, and the previously admitted tuning theorem. Independently recheck every finite algebraic dependency and proof review.',result,'The genericity and local stability statements are PROVED within the fixed exponent and finite profile spaces stated in287. No singular-point, exponent-open, global-radius or whole-plane assertion is made.',p,review)
(base/'sources/admit_period_ten_genericity.py').write_bytes(Path(__file__).read_bytes())

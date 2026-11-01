"""Admit the replayed Q10 uniform response lower bounds."""
from pathlib import Path
from fractions import Fraction as F
import argparse
from certificate_admission import read,ref,checkref,reviewed,admit
ap=argparse.ArgumentParser();ap.add_argument('--entry',type=int,required=True);ap.add_argument('--review',required=True);a=ap.parse_args()
base=Path('research/285_period_ten_response_bounds');v=base/'verification';d=read(v/'checks.json.gz');r=read(v/'replay.json.gz')
assert d['all_checks_pass'] and d['Q']==10 and d['bits']==1024 and r['all_checks_pass']
assert r['source']==ref(v/'checks.json.gz') and r['inputs']==d['inputs'];assert len(d['rows'])==len(r['rows'])==14
for q in d['inputs']:checkref(q)
for x,y in zip(d['rows'],r['rows']):
 assert x['root_index']==y['root_index'] and x['s']==y['s'] and x['K']==y['K'] and F(x['s'])==F(2)**x['s_power']>0
 assert y['positive_tail_coefficients']+y['zero_tail_coefficients']==y['positive_denominator_coefficients']==x['denominator_degree']+1
 assert y['finite_comparisons']==len(x['finite_checks'])==x['K']-2
symbolicpath=Path('research/282_period_ten_symbolic_response/verification/admission.json');sy=read(symbolicpath);assert sy['verdict']=='PROVED' and sy['root_count']==14
for k in ['evidence','proof','finite_algebra']:checkref(sy[k])
review=reviewed(base,a.review)
slist=','.join(x['s'] for x in d['rows']);Klist=','.join(str(x['K']) for x in d['rows']);positive=sum(x['positive_tail_coefficients'] for x in r['rows']);zero=sum(x['zero_tail_coefficients'] for x in r['rows']);finite=sum(x['finite_comparisons'] for x in r['rows'])
result=f'For the fourteen roots in increasing order, uniform lower bounds s={slist}, with tail starts K={Klist}. The separate rational-endpoint replay passes{positive} nonzero tail coefficients,{zero} exact-zero coefficients and{finite} finite-carrier inequalities. Every denominator coefficient after shifting is strictly positive. Producer runtime{d["actual_elapsed_s"]:.6f}seconds; replay runtime{r["actual_elapsed_s"]:.6f}seconds.'
admit(base,a.entry,'Uniform period-ten response lower bounds','Each stated positive rational bounds every response modulus on the entire corresponding algebraic root interval.', 'Exact polynomial shifts, directed1024-bit Horner arithmetic, then separate exact Fraction endpoint replay of every finite and tail inequality.',result,'The all-index lower bounds are PROVED. Sampled minima only propose targets; no global minimizing index, sharp infimum or exterior radius is asserted here.',v/'checks.json.gz',review,dict(replay=ref(v/'replay.json.gz'),symbolic_admission=ref(symbolicpath),rows=[dict(root_index=x['root_index'],s=x['s'],K=x['K']) for x in d['rows']] ))
(base/'sources/admit_period_ten_bounds.py').write_bytes(Path(__file__).read_bytes())

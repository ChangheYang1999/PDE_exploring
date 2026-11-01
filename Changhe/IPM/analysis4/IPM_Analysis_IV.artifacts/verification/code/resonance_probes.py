"""Exact low-mode resonance counterexamples, independently formed in Cartesian coordinates."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
from math import gcd

from cartesian_verify import Q, qs, Field, sin_field, recurrence


def next_density(record):
    c = Q(record['c'])
    n = len(record['rows'])+1
    p = 1-n*Q(record['delta'])
    rho, psi = {}, {}
    for row in record['rows']:
        k = row['n']
        rho[k] = sin_field(Q(row['p']), {int(m):Q(v) for m,v in row['density'].items()})
        psi[k] = sin_field(Q(row['p'])+1, {int(m):Q(v) for m,v in row['stream'].items()})
    nonlinear = Field(p,{})
    for i in range(1,n):
        j = n-i
        nonlinear = (nonlinear + psi[i].dy().scale(-1)*rho[j].dx()
                     + psi[i].dx()*rho[j].dy())
    f = nonlinear.scale(1/((n-1)*(c-1)))
    h = f.dx().sine()
    resonant = abs(int(p+1))
    assert p+1 == -resonant and resonant > 0 and resonant % 2 == 0
    compatibility = h.get(resonant,Q(0))
    assert compatibility == -resonant*f.sine().get(resonant-1,Q(0))
    assert compatibility != 0
    return {'n':n, 'p':qs(p), 'resonant_stream_frequency':resonant,
            'density':{str(m):qs(v) for m,v in f.sine().items()},
            'poisson_forcing_at_resonance':qs(compatibility),
            'incompatible':True}


base=json.loads(Path('research/01_recurrence/verification/single_mode_c9_5_N8.json').read_text())
a=next_density(base['recursion'])
b_record=recurrence(Q(2), {1:Q(1)}, 7, require_potential=False)
b=next_density(b_record)
row4=b_record['rows'][3]
at_axis=sum((-1)**((int(m)-1)//2)*Q(v) for m,v in row4['density'].items())
assert at_axis != 0
candidate=json.loads(Path('research/02_candidate007/data/leading_exact.json').read_text())
delta=Q(candidate['delta'])
aa,bb=int(delta.numerator),int(delta.denominator)
step=2*bb//gcd(aa,2)
r=aa//gcd(aa,2)
first_stream=step if r>=2 else 2*step
j=int(first_stream*delta/2)-1
assert j>=1 and first_stream*delta==2*(j+1)
result={'date_utc':datetime.now(timezone.utc).isoformat(),
        'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'c9_5_sin1':a, 'c2_sin1':b,
        'c2_n4_density_at_pi_over_2':qs(at_axis),
        'c2_n1_through_n7':b_record,
        'candidate007_first_resonance':{'n':first_stream,'j':j,
          'stream_frequency':2*j,
          'forcing_density_frequency':2*j-1,
          'comment':'Arithmetic location only; compatibility not computed at this enormous order.'}}
out=Path('research/03_resonances/verification/exact_probes.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print('c9/5 resonance forcing',a['poisson_forcing_at_resonance'])
print('c2 resonance forcing',b['poisson_forcing_at_resonance'])
print('c2 n4 density at pi/2',qs(at_axis))
print('Candidate resonance',result['candidate007_first_resonance'])

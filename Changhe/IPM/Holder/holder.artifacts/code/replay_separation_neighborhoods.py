"""Independent logarithmic reevaluation; no import of the producer program."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from hashlib import sha256
import json
from flint import arb, ctx
ctx.prec = 640
root = Path(__file__).resolve().parents[1]
folder = root/'13_transport_duality/exponent_continuity/certified_neighborhoods'
source = folder/'verification/intervals.json'
original = json.loads(source.read_text())
table = {Q(r['alpha']): r for r in json.loads((root/'data/verified_table.json').read_text())['rows']}
def ball(q):
    q=Q(q)
    return arb(q.numerator)/q.denominator
checks=[]
for r in original['rows']:
    alpha, radius, a, b=map(Q,[r['alpha'],r['radius'],r['auxiliary_a'],r['auxiliary_b']])
    assert 0<a<alpha-radius<alpha+radius<b<1
    assert Q(r['interval_left'])==alpha-radius and Q(r['interval_right'])==alpha+radius
    t=table[alpha]
    assert Q(r['U_C'])==Q(t['selected_upper_C']['exact_safe_endpoint'])
    assert Q(r['V_D'])==Q(t['selected_lower_D']['exact_safe_endpoint'])
    gap=Q(r['V_D'])-Q(r['U_C'])
    logeps=-r['cutoff_N']*arb(2).log()
    logR=r['cutoff_M']*arb(2).log()
    eps=logeps.exp()
    # Direct logs in the powers, rather than power of the constructed cutoff.
    inner=2*(ball(a)*logeps).exp()/(arb.pi()*ball(a))
    smooth=(ball(b)*(1+2*eps).log()+2*logeps).exp()/(2*(1-eps)**2)
    tail=(ball(b)*arb(2).log()+ball(b-1)*logR).exp()/(ball(1-b)*(1-(-2*logR).exp()/4)**2)
    mass=2/arb.pi()*(logR+(1+(-logR).exp()/2).log()-logeps)
    slope=arb.max((-arb(1)).exp()/ball(a),(ball(b)*(logR+arb(2).log())).exp()*(logR+arb(2).log()))
    margin=ball(gap)-4*(inner+smooth+tail)-(2*mass+ball('1/2'))*slope*ball(radius)
    lower=Q(str(margin.lower().fmpq())); upper=Q(str(margin.upper().fmpq()))
    assert lower>0
    assert Q(r['separation_margin']['lower'])<=lower<=upper<=Q(r['separation_margin']['upper'])
    assert Q(r['rounded_down_gap'])<=lower
    assert Q(r['rounded_down_gap'])==Q((lower*10000).__floor__(),10000)
    checks.append(dict(alpha=str(alpha),radius=str(radius),rounded_down_gap=r['rounded_down_gap'],margin_lower=str(lower),margin_upper=str(upper),original_enclosure_contains=True))
record=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,verdict='CONFIRMED',row_count=len(checks),method='Separate implementation with logarithmic powers and mass formula; exact rational containment and decimal checks.',checks=checks,sha256={str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),source,folder/'PROOF.md',root/'data/verified_table.json']})
(folder/'verification/independent_replay.json').write_text(json.dumps(record,indent=2)+'\n')
print(record['timestamp_utc'],record['verdict'],len(checks),'rows at',ctx.prec,'bits')

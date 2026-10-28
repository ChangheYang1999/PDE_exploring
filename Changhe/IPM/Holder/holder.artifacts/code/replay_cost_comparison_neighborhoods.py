"""Separate power-form verification of all one-sided endpoint inequalities."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
import json
from flint import arb,ctx
ctx.prec=640
root=Path(__file__).resolve().parents[1]
base=root/'13_transport_duality/exponent_continuity/cost_comparison'
source=base/'verification/intervals.json'
parent=base.parent/'certified_neighborhoods/verification/intervals.json'
old={Q(r['alpha']):r for r in json.loads(parent.read_text())['rows']}
def A(x):
    x=Q(x);return arb(x.numerator)/x.denominator
rows=[]
for r in json.loads(source.read_text())['rows']:
    alpha,rho,a,b,U,V,E,mc,md=map(Q,[r[k] for k in ['alpha','radius','auxiliary_a','auxiliary_b','U_C','V_D','E_exact_upper','mass_C_exact_upper','mass_D_exact_upper']])
    assert 0<a<=alpha-rho<alpha+rho<=b<1
    assert Q(r['interval_left'])==alpha-rho and Q(r['interval_right'])==alpha+rho
    o=old[alpha]
    assert E==Q(o['Ebar']['upper']) and U==Q(o['U_C']) and V==Q(o['V_D'])
    assert r['cutoff_N']==o['cutoff_N'] and r['cutoff_M']==o['cutoff_M']
    assert md==mc+Q(1,2)
    R=arb(2)**r['cutoff_M'];eps=arb(2)**(-r['cutoff_N'])
    mass=2/arb.pi()*((R+A('1/2'))/eps).log()
    assert mass<A(mc)
    u,v=A(U+E),A(V-E)
    upper_plus=(2*R)**A(rho)*u
    upper_minus=u*(A(mc)/u)**A(rho/alpha)
    lower_plus=v*(v/A(md))**A(rho/alpha)
    lower_minus=v/(2*R)**A(rho)
    margin=arb.min(v,arb.min(lower_plus,lower_minus))-arb.max(u,arb.max(upper_plus,upper_minus))-2*A(E)
    lo,hi=Q(str(margin.lower().fmpq())),Q(str(margin.upper().fmpq()))
    assert lo>0 and lo>=Q(r['separation_margin']['lower']) and hi<=Q(r['separation_margin']['upper'])
    assert Q(r['rounded_down_gap'])==Q((lo*10000).__floor__(),10000)
    rows.append(dict(alpha=str(alpha),radius=str(rho),lower_margin=str(lo),upper_margin=str(hi),rounded_down_gap=r['rounded_down_gap'],all_endpoints_and_mass_checked=True))
rec=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,verdict='INDEPENDENT SCALAR REPLAY CONFIRMED; analytic status in verifier ledger',method='Four one-sided power expressions plus center, rather than exponentials of maximum logarithmic coefficients.',rows=rows,sha256={str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),source,parent,base/'PROOF.md']})
(base/'verification/independent_replay.json').write_text(json.dumps(rec,indent=2)+'\n')
print(rec['timestamp_utc'],len(rows),'rows PASS')

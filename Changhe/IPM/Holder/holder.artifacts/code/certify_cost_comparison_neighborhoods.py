"""Exact-scalar application of finite-mass Jensen comparison, no quadrature."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
import json
from flint import arb,ctx
ctx.prec=320
root=Path(__file__).resolve().parents[1]
base=root/'13_transport_duality/exponent_continuity/cost_comparison'
source=base.parent/'certified_neighborhoods/verification/intervals.json'

def A(x):
    x=Q(x);return arb(x.numerator)/x.denominator

def enc(x):
    return dict(display=str(x),lower=str(x.lower().fmpq()),upper=str(x.upper().fmpq()))
rows=[]
for old in json.loads(source.read_text())['rows']:
    a0,a,b,U,V=map(Q,[old['alpha'],old['auxiliary_a'],old['auxiliary_b'],old['U_C'],old['V_D']])
    E=Q(old['Ebar']['upper']);N,M=old['cutoff_N'],old['cutoff_M']
    R=arb(2)**M
    mass=2/arb.pi()*((R+A('1/2'))/(arb(2)**(-N))).log()
    mc=Q(str(mass.upper().fmpq()));md=mc+Q(1,2)
    u0,v0=U+E,V-E
    assert v0>0
    logd=(M+1)*arb(2).log()
    hc=arb.max(logd,arb.max((A(mc)/A(u0)).log()/A(a0),arb(0)))
    hd=arb.max(logd,arb.max((A(md)/A(v0)).log()/A(a0),arb(0)))
    radii={Q(j,10**k) for k in range(1,19) for j in [1,2,5]}
    radii.add(min(a0-a,b-a0))
    selected=None
    for radius in sorted(radii,reverse=True):
        if radius>min(a0-a,b-a0):continue
        clower=A(v0)*(-hd*A(radius)).exp()-A(u0)*(hc*A(radius)).exp()-2*A(E)
        if clower>0:
            selected=radius;break
    assert selected is not None
    lower=Q(str(clower.lower().fmpq()))
    rounded=Q((lower*10000).__floor__(),10000)
    rows.append(dict(alpha=str(a0),auxiliary_a=str(a),auxiliary_b=str(b),radius=str(selected),interval_left=str(a0-selected),interval_right=str(a0+selected),cutoff_N=N,cutoff_M=M,U_C=str(U),V_D=str(V),E_exact_upper=str(E),mass_C_exact_upper=str(mc),mass_D_exact_upper=str(md),H_C=enc(hc),H_D=enc(hd),separation_margin=enc(clower),rounded_down_gap=str(rounded),previous_radius=old['radius']))
    print(str(a0),'radius='+str(selected),'gap='+str(rounded),flush=True)
paths=[Path(__file__),source,base/'PROOF.md',base.parent/'PROOF.md']
record=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,verdict='SCALAR CHECKS PASS; new analytic lemma pending independent cross-read',rows=rows,sha256={str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in paths})
(base/'verification/intervals.json').write_text(json.dumps(record,indent=2)+'\n')
(base/'INTERVALS.md').write_text('# Sufficient closed intervals from the finite-cost comparison\n\nThe new analytic lemma awaits independent cross-read. Scalar inequalities are certified.\n\n| Center | Radius | Minimum gap, rounded down |\n|---|---:|---:|\n'+''.join(f"| {r['alpha']} | {r['radius']} | {float(Q(r['rounded_down_gap'])):.4f} |\n" for r in rows)+'\nAll centers, radii, cutoffs and endpoint inputs are exact. See PROOF.md and verification/intervals.json.\n')
print(record['timestamp_utc'])

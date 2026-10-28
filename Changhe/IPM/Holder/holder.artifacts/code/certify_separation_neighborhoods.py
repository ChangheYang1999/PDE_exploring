"""Scalar interval application of the accepted Holder-norm continuity bound."""
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json, math
from flint import arb, ctx
ctx.prec=320
root=Path(__file__).resolve().parents[1]
base=root/'13_transport_duality/exponent_continuity/certified_neighborhoods'
source=root/'data/verified_table.json'
def A(x):
    x=Q(x); return arb(x.numerator)/x.denominator

def enc(x):
    return dict(display=str(x),lower=str(x.lower().fmpq()),upper=str(x.upper().fmpq()))
def quantities(a,b,N,M):
    eps=arb(2)**(-N); R=arb(2)**M
    E1=2*eps**A(a)/(arb.pi()*A(a))
    E2=(1+2*eps)**A(b)*eps**2/(2*(1-eps)**2)
    E3=arb(2)**A(b)*R**A(b-1)/(A(1-b)*(1-1/(4*R*R))**2)
    E=E1+E2+E3
    m=2/arb.pi()*((R+A(Q(1,2)))/eps).log()
    L=arb.max(1/(arb(1).exp()*A(a)),(2*R)**A(b)*(2*R).log())
    return E1,E2,E3,E,(2*m+A(Q(1,2)))*L
rows=[]
for r in json.loads(source.read_text())['rows']:
    a0=Q(r['alpha']); U=Q(r['selected_upper_C']['exact_safe_endpoint']); V=Q(r['selected_lower_D']['exact_safe_endpoint']); gap=V-U
    assert gap>0
    h=min(a0,1-a0)/100; a=a0-h; b=a0+h
    # Guess only. The final positive interval margin is authoritative.
    N=max(10,math.ceil(math.log2(64/(math.pi*float(a)*float(gap)))/float(a)))
    coef=2**float(b)/(float(1-b)*(15/16)**2)
    M=max(1,math.ceil(math.log2(32*coef/float(gap))/float(1-b)))
    while True:
        E1,E2,E3,E,den=quantities(a,b,N,M)
        if 4*E<A(gap): break
        N+=1;M+=1
    bound=(A(gap)-4*E)/den
    # Use a decade inside both the auxiliary interval and the proved bound.
    lograd=float((arb.min(bound,A(h))/arb(10)).log()/arb(10).log())
    k=max(0,math.ceil(-lograd)); radius=Q(1,10**k)
    margin=A(gap)-4*E-den*A(radius)
    assert radius<h and margin>0
    rows.append(dict(alpha=str(a0),radius=str(radius),radius_decimal_exponent=-k,interval_left=str(a0-radius),interval_right=str(a0+radius),auxiliary_a=str(a),auxiliary_b=str(b),cutoff_N=N,cutoff_M=M,U_C=str(U),V_D=str(V),center_gap=str(gap),error_parts=[enc(x) for x in [E1,E2,E3]],Ebar=enc(E),continuity_coefficient=enc(den),separation_margin=enc(margin),rounded_down_gap=str(Q((Q(str(margin.lower().fmpq()))*10000).__floor__(),10000)),operator_endpoint_sources=[r['selected_upper_C']['source'],r['selected_lower_D']['source']]))
    print(str(a0),'radius=10^'+str(-k),'N='+str(N),'M='+str(M),'margin='+str(margin),flush=True)
paths=[Path(__file__),source,base/'PROOF.md',base.parent/'PROOF.md']
record=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,verdict='PASS: strict separation on every closed interval',rows=rows,sha256={str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in paths})
(base/'verification/intervals.json').write_text(json.dumps(record,indent=2)+'\n')
(base/'INTERVALS.md').write_text('# Explicit sufficient intervals of strict separation\n\nEvery row means C_alpha<D_alpha for |alpha-center|<=radius.\n\n| Center | Radius | Certified minimum gap, rounded down |\n|---|---:|---:|\n'+''.join(f"| {r['alpha']} | 10^{r['radius_decimal_exponent']} | {float(Q(r['rounded_down_gap'])):.4f} |\n" for r in rows)+'\nSee PROOF.md and verification/intervals.json for exact parameters and enclosures.\n')
print(record['timestamp_utc'])

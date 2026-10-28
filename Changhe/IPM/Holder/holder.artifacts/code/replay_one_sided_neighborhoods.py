from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
from flint import arb,ctx
import json
ctx.prec=640
root=Path(__file__).resolve().parents[1]
base=root/'13_transport_duality/exponent_continuity/cost_comparison/one_sided'
source=base/'verification/intervals.json'
parent=base.parent/'verification/intervals.json'
old={Q(r['alpha']):r for r in json.loads(parent.read_text())['rows']}
def A(q):
 q=Q(q);return arb(q.numerator)/q.denominator
def bounds(x):return Q(str(x.lower().fmpq())),Q(str(x.upper().fmpq()))
rows=[]
for row in json.loads(source.read_text())['rows']:
 o=old[Q(row['alpha'])]
 for key in ['alpha','auxiliary_a','auxiliary_b','U_C','V_D','E_exact_upper','mass_C_exact_upper','mass_D_exact_upper','cutoff_N','cutoff_M']:
  assert row[key]==o[key]
 a0,a,b,rho=map(Q,[row[k] for k in ['alpha','auxiliary_a','auxiliary_b','radius']])
 assert 0<a<=a0-rho<a0+rho<=b<1
 assert Q(row['interval_left'])==a0-rho and Q(row['interval_right'])==a0+rho
 U,V,E,mc,md=map(Q,[row[k] for k in ['U_C','V_D','E_exact_upper','mass_C_exact_upper','mass_D_exact_upper']])
 assert mc>0 and md>0 and U+E>0 and V-E>0
 u,v=A(U+E),A(V-E)
 d=arb(2)**(row['cutoff_M']+1)
 c_plus=u*d**A(rho)
 d_plus=v*arb.min(arb(1),(v/A(md))**A(rho/a0))
 c_minus=u*arb.max(arb(1),(A(mc)/u)**A(rho/a0))
 d_minus=v/(d**A(rho))
 gaps={'gap_minus':d_minus-c_minus-2*A(E),'gap_plus':d_plus-c_plus-2*A(E)}
 gaps['gap']=arb.min(gaps['gap_minus'],gaps['gap_plus'])
 for key,value in gaps.items():
  lo,hi=bounds(value)
  assert lo>=Q(row[key]['lower']) and hi<=Q(row[key]['upper']) and lo>0
 lo,hi=bounds(gaps['gap']);assert Q(row['rounded_down_gap'])==Q((lo*10000).__floor__(),10000)
 rows.append(dict(alpha=str(a0),radius=str(rho),lower_margin=str(lo),upper_margin=str(hi),rounded_down_gap=row['rounded_down_gap']))
rec=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,verdict='CONFIRMED',scope='All ten intervals as a direct application of V261; independent one-sided power-form computation and exact rational containment.',rows=rows,sha256={str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),source,parent,base/'PROOF.md',base.parent/'verification/accepted.json']})
(base/'verification/independent_replay.json').write_text(json.dumps(rec,indent=2)+'\n')
text='# Wider intervals from separate one-sided comparisons\n\nThese closed intervals use the same endpoint certificates and cutoffs as V261. Both one-sided margins are positive throughout each interval. All scalar conditions have separate320/640-bit implementations.\n\n| Center | Radius | Minimum gap, rounded down |\n|---|---:|---:|\n'
for r in rows:
 n=int(Q(r['rounded_down_gap'])*10000);gap=f'{n//10000}.{n%10000:04d}'
 text+=f"| {r['alpha']} | {r['radius']} | {gap} |\n"
text+='\nThe proof is in PROOF.md; exact cutoffs, masses, errors, intervals and inputs are in verification/intervals.json. These are sufficient intervals, not maximal ones.\n'
(base/'INTERVALS.md').write_text(text)
print(rec['timestamp_utc'],len(rows),'one-sided intervals PASS')

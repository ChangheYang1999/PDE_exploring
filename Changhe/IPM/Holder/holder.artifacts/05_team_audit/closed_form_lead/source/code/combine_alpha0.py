"""Upper value of the Theorem 3.5 remainder R at alpha=0 for the group-0 plans (reference exponent 1/20), and a check
that the alpha=1/200 rows of the same runs coincide with the stored group-0 node certificates of Theorem 9.2."""
from pathlib import Path
import json, math, hashlib
from fractions import Fraction as Fr
from flint import arb, ctx
ROOT=Path(__file__).resolve().parents[1]; ctx.prec=200
def load(p): return json.loads((ROOT/p).read_text())
r=load('data/refl_a0.json'); f=load('data/far_a0.json')
ru={x['alpha']:x for x in load('data/upper_n384.json')['rows']}
fu={x['alpha']:x for x in load('data/far2_g0.json')['rows']}
R={x['alpha']:x for x in r['rows']}; F={x['alpha']:x for x in f['rows']}
assert R['1/200']['regular_grid']==ru['1/200']['regular_grid'], 'compact part differs from the node certificate'
assert F['1/200']['far_phase_intervals']==fu['1/200']['far_phase_intervals'], 'exterior part differs from the node certificate'
m=r['phase_intervals']
assert m==16 and f['phase_intervals']==16 and r['cells_per_axis']==384 and f['angles']==512 and f['radial_cells']==128
assert f['plan_reference_alpha']=='1/20'
sec=1/(arb.pi()/(4*m)).cos()
def remainder(a):
    vals=[arb(y)+arb(z) for y,z in zip(R[a]['regular_grid'],F[a]['far_phase_intervals'])]
    mx=vals[0]
    for v in vals[1:]: mx=arb.max(mx,v)
    return mx*sec
def up6(b):
    mm,e=b.upper().man_exp(); u=Fr(int(mm))*Fr(2)**int(e); return Fr(math.ceil(u*10**6),10**6)
R0=remainder('0'); R1=remainder('1/200')
files=['data/refl_a0.json','data/far_a0.json','data/upper_n384.json','data/far2_g0.json','code/refl_nodes_a0.py','code/far_nodes_a0.py','code/combine_alpha0.py']
out=dict(alpha='0',R=f"{float(up6(R0)):.6f}",R_enclosure=R0.str(30,more=True),R_1_200=f"{float(up6(R1)):.6f}",
         source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files})
(ROOT/'data/remainder_a0.json').write_text(json.dumps(out,indent=1)+'\n')
print('R(0) <=',out['R'],' R(1/200) <=',out['R_1_200'])

"""Strict recombination check for certify_note14.py outputs with a sidecar (<out>.json.tasks.json).
Checks (all must pass, exit code 1 otherwise): every task carries the JSON's alpha/b/c/lam/maxdepth and a positive ntheta; within each task the
radial edges (exact decimal rationals) are strictly increasing; the tasks of each kind, sorted, are exactly adjacent (last edge of one == first
edge of the next: no gaps, no overlaps, no duplicates); the near annuli cover exactly [rho_min, 1/2] and the m-system exactly [rho_m, rho_max];
the per-task tuples (mid, rad strings) re-sum to the JSON enclosure (agreement of both endpoints to 1e-9), with inner/sliver/tail recomputed
from the recorded parameters; everything finite.  Angular coverage holds by construction (each task loops over the full circle).
Usage: python3 recombine_n14.py ../runs/n14/<tag>.json"""
import sys, json, math, os
from fractions import Fraction
from flint import arb, ctx, fmpq
ctx.prec = 80
fails = []
def check(cond, msg):
    if not cond: fails.append(msg)
d = json.load(open(sys.argv[1]))
side = json.load(open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), os.path.basename(d['sidecar']))))
if isinstance(side, dict):   # format since 08:40Z: {'source_sha256_at_start': ..., 'tasks': [...]}
    check(side.get('source_sha256_at_start') == d.get('source_sha256'), "sidecar start hashes differ from the JSON source_sha256")
    side = side['tasks']
p = d['params']; ALPHA = arb(fmpq(d['alpha'])); PI = arb.pi()
pm = arb(0).union(arb(1)).union(arb(-1))
near = arb(0); rest = arb(0); ncells = 0; errsum = {}
spans = {'near_e1': [], 'm_system': []}
for i, t in enumerate(side):
    tk = t['task']
    check(tk['alpha_q'] == d['alpha'] and tk['b_q'] == d['b'] and tk['c_q'] == d['c'] and tk['lam_q'] == d['lam'], f"task {i}: parameter mismatch")
    check(tk['maxdepth'] == p['maxdepth'], f"task {i}: maxdepth mismatch")
    check(isinstance(tk['ntheta'], int) and tk['ntheta'] > 0, f"task {i}: bad ntheta")
    check(tk['kind'] in spans, f"task {i}: unknown kind")
    ed = [Fraction(s) for s in tk['rho_edges']]
    check(len(ed) >= 2 and all(ed[j] < ed[j+1] for j in range(len(ed)-1)), f"task {i}: edges not strictly increasing")
    v = arb(t['mid']) + arb(0, t['rad'])
    check(v.is_finite(), f"task {i}: nonfinite value")
    ncells += t['cells']
    if tk['kind'] == 'near_e1': near += v
    else: rest += v
    spans[tk['kind']].append((ed[0], ed[-1], i))
    for k, e in t['errors'].items(): errsum[k] = errsum.get(k, arb(0)) + arb(e)
def exact_cover(kind, lo, hi):
    sp = sorted(spans[kind])
    check(len(sp) > 0, f"{kind}: no tasks")
    if not sp: return
    check(sp[0][0] == lo, f"{kind}: first edge {sp[0][0]} != {lo}")
    for (a1, b1, i1), (a2, b2, i2) in zip(sp, sp[1:]):
        check(b1 == a2, f"{kind}: tasks {i1},{i2} not adjacent ({b1} vs {a2})")
    check(sp[-1][1] == hi, f"{kind}: last edge {sp[-1][1]} != {hi}")
exact_cover('near_e1', Fraction(repr(p['rho_min'])), Fraction(1, 2))
exact_cover('m_system', Fraction(repr(p['rho_m'])), Fraction(repr(p['rho_max'])))
rm = arb(repr(p['rho_min']))
inner = (rm**ALPHA/ALPHA + PI*rm*rm/(2*PI*(1 - rm)**2)*(arb(1)/2 + rm**ALPHA))*pm
rmm = arb(repr(p['rho_m'])); C2 = arb(2)**(ALPHA - 1)
sliver = 16*C2*rmm**(ALPHA + 3)/(PI*(ALPHA + 3)*(1 - rmm*rmm).sqrt())*pm
R = arb(repr(p['rho_max']))
tail = arb(2)**ALPHA*(R/(R - arb(1)/2))**3*R**(ALPHA - 1)/(1 - ALPHA)*pm
I0 = 2*(near + inner) + rest + sliver + tail
check(I0.is_finite(), "nonfinite recombined enclosure")
check(ncells == d['cells'], f"cell count {ncells} != json {d['cells']}")
jlo = arb(d['I0_lower']); jup = arb(d['I0_upper']); jD = arb(d['D_lower'])
lo, up = arb(I0.lower()), arb(I0.upper())
check(abs(lo - jlo) < 1e-9 and abs(up - jup) < 1e-9, "recombined endpoints differ from the JSON by more than 1e-9")
check(abs((abs(I0).lower() + arb(1)/2) - jD) < 1e-9, "recombined D_lower differs from the JSON")
print(f"tasks {len(side)}, cells {ncells}; near tasks {len(spans['near_e1'])}, m-system tasks {len(spans['m_system'])}")
print(f"recombined I0 = [{lo.str(15)}, {up.str(15)}];  json [{d['I0_lower'][:17]}, {d['I0_upper'][:17]}]")
print(f"recombined D_lower = {(abs(I0).lower() + arb(1)/2).str(15)};  json {d['D_lower'][:17]}")
print("errors by category:", {k: v.str(6) for k, v in errsum.items()})
print("source hashes:", d.get('source_sha256'))
if fails:
    print("FAIL:"); [print("  " + m) for m in fails]; sys.exit(1)
print("PASS: exact coverage, parameters, finiteness and enclosure agreement")

"""Exact-marginal local transport with globally allocated identity atoms.

The LP chooses a candidate only. Every integer marginal is checked and every
used edge receives an outward ball cost. See radial_atoms/PROOF.md.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, json, hashlib, math, time, warnings
import numpy as np
from scipy.optimize import linprog, OptimizeWarning
from scipy.sparse import coo_matrix
from flint import arb, ctx
from certify_local_circles_greedy import angular_data, UNIT
ROOT = Path(__file__).resolve().parents[1]


def up(x):
    return arb(x.upper())


def propose(masses, points, rows, atom_start, alpha, neighbors, time_limit):
    pos = [i for i, x in enumerate(masses) if x > 0]
    neg = [i for i, x in enumerate(masses) if x < 0]
    assert sum(masses) == 0
    neg_index = {idx: j for j, idx in enumerate(neg)}
    byrow = {}
    atomneg = []
    for j, idx in enumerate(neg):
        if idx >= atom_start:
            atomneg.append(j)
        else:
            byrow.setdefault(rows[idx], []).append(j)
    pp = np.asarray(points)[pos]
    nn = np.asarray(points)[neg]
    edges = set()
    for i, idx in enumerate(pos):
        if idx >= atom_start:
            edges.update((i, j) for j in range(len(neg)))
            continue
        cand = byrow[rows[idx]]
        if neighbors and len(cand) > neighbors:
            d = abs(pp[i] - nn[cand])
            chosen = np.argpartition(d, neighbors - 1)[:neighbors]
            edges.update((i, cand[int(j)]) for j in chosen)
        else:
            edges.update((i, j) for j in cand)
        # Explicit reflection edge guarantees feasibility without an LP.
        half = atom_start // 2
        opposite = idx + half if idx < half else idx - half
        edges.add((i, neg_index[opposite]))
        edges.update((i, j) for j in atomneg)
    pairs = sorted(edges)
    ii = np.asarray([e[0] for e in pairs], dtype=np.int32)
    jj = np.asarray([e[1] for e in pairs], dtype=np.int32)
    costs = abs(pp[ii] - nn[jj]) ** alpha
    ne = len(pairs)
    cols = np.arange(ne)
    A = coo_matrix((np.ones(2 * ne), (np.r_[ii, len(pos) + jj],
                   np.r_[cols, cols])), shape=(len(pos) + len(neg), ne)).tocsr()
    supply = [masses[i] for i in pos]
    demand = [-masses[j] for j in neg]
    rhs = np.asarray(supply + demand, dtype=float) / UNIT
    started = time.monotonic()
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', OptimizeWarning)
        sol = linprog(costs, A_eq=A, b_eq=rhs, bounds=(0, None),
                      method='highs-ds', options={'time_limit': time_limit,
                                                'threads': 1})
    elapsed = time.monotonic() - started
    rems = supply[:]
    remd = demand[:]
    plan = {}
    if sol.success:
        for e in np.flatnonzero(sol.x > 0):
            i, j = pairs[int(e)]
            f = min(max(0, math.floor(float(sol.x[e]) * UNIT)), rems[i], remd[j])
            if f:
                plan[(pos[i], neg[j])] = f
                rems[i] -= f
                remd[j] -= f
    repair = sum(rems)
    i = j = 0
    while i < len(pos) and j < len(neg):
        if not rems[i]:
            i += 1
            continue
        if not remd[j]:
            j += 1
            continue
        f = min(rems[i], remd[j])
        edge = (pos[i], neg[j])
        plan[edge] = plan.get(edge, 0) + f
        rems[i] -= f
        remd[j] -= f
    assert not any(rems) and not any(remd)
    actual = [0] * len(masses)
    for (i, j), f in plan.items():
        assert isinstance(f, int) and f > 0 and masses[i] > 0 and masses[j] < 0
        actual[i] += f
        actual[j] -= f
    assert actual == masses
    info = dict(lp_success=bool(sol.success), lp_message=sol.message,
                lp_seconds=elapsed, proposed_edges=ne, used_edges=len(plan),
                exact_repair_units=repair,
                lp_objective=float(sol.fun) if sol.success else None)
    return plan, info


def run(args, phase_index):
    ctx.prec = args.prec
    pi = arb.pi()
    alpha = arb(args.alpha)
    delta = arb(args.delta)
    phase = pi * phase_index / (2 * args.phases)
    n, nr = args.angles, args.radial
    assert n >= 16 and n % 8 == 0 and nr > 0
    assert 0 < alpha < 1 and 0 < delta < arb(1) / 2
    half = n * nr
    bins, arcs, mids = [], [], []
    right_masses, right_points, residual = [], [], arb(0)
    radial_rows = []
    t0 = time.monotonic()
    for k in range(nr):
        a = (delta.sqrt() + ((arb(1) / 2).sqrt() - delta.sqrt()) * k / nr) ** 2
        b = (delta.sqrt() + ((arb(1) / 2).sqrt() - delta.sqrt()) * (k + 1) / nr) ** 2
        lr = (b / a).log()
        avg = (b ** alpha - a ** alpha) / (alpha * lr)
        signed, tv, aa, mm = angular_data(a, b, phase, n)
        rowmass = []
        for val in signed[:n]:
            count = max(0, int((arb((arb(abs(val)) / UNIT * lr).lower()) * UNIT).floor().unique_fmpz()))
            rowmass.append(count if val >= 0 else -count)
        extracted = arb(sum(abs(x) for x in rowmass)) / UNIT
        loss = tv * lr - extracted
        assert loss >= 0
        residual += loss * (1 + 2 * b) ** alpha
        r = float(((a + b) / 2).mid())
        right_points += [.5 + r * complex(float(z.real.mid()), float(z.imag.mid())) for z in mm]
        right_masses += rowmass
        radial_rows += [k] * n
        bins.append((a, b, lr, avg))
        arcs.append(aa)
        mids.append(mm)
    masses = right_masses + [-v for v in right_masses] + [-UNIT // 2, UNIT // 2]
    points = right_points + [-z for z in right_points] + [.5, -.5]
    rows = radial_rows + radial_rows + [-1, -1]
    plan, info = propose(masses, points, rows, 2 * half, float(alpha.mid()), args.neighbors, args.time_limit)
    chord = [(2 * (pi * min(k + 1, n // 2) / n).sin()) ** alpha for k in range(n // 2 + 1)]
    cost = arb(0)
    other_row_flow = 0
    category = {}
    for (i, j), flow in plan.items():
        iatom, jatom = i >= 2 * half, j >= 2 * half
        if iatom and jatom:
            c, tag = arb(1), 'atom_atom'
        elif not iatom and not jatom:
            ki, kj = rows[i], rows[j]
            if ki != kj:
                c, tag = arb(2) ** alpha, 'cross_row_repair'
                other_row_flow += flow
            else:
                a, b, _, avg = bins[ki]
                ai, aj = i % n, j % n
                if i // half == j // half:
                    d = min(abs(ai - aj), n - abs(ai - aj))
                    c, tag = chord[d] * avg, 'same_pole'
                else:
                    t = arcs[ki][ai] + arcs[ki][aj]
                    dmax = arb.max(up(abs(1 + a * t)), up(abs(1 + b * t)))
                    c, tag = dmax ** alpha, 'opposite_pole'
        else:
            node, atom = (j, i) if iatom else (i, j)
            k = rows[node]
            a, b, _, avg = bins[k]
            if node // half == atom - 2 * half:
                c, tag = avg, 'own_atom'
            else:
                t = arcs[k][node % n]
                dmax = arb.max(up(abs(1 + a * t)), up(abs(1 + b * t)))
                c, tag = dmax ** alpha, 'other_atom'
        assert c >= 0 and c.is_finite()
        piece = arb(flow) / UNIT * c
        cost += piece
        category[tag] = category.get(tag, arb(0)) + piece
    a2 = 2 ** (1 + alpha / 2) / (pi * (alpha + 2))
    small = 2 * a2 * delta ** alpha / alpha + (1 + 2 * delta) ** alpha * delta ** 2 / (2 * (1 - delta) ** 2)
    total = cost + residual
    sources = ['code/certify_global_radial_atoms.py', 'code/certify_local_circles_greedy.py',
               '08_improved_upper_bounds/local_disk_transport/radial_atoms/PROOF.md']
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), args=vars(args), phase_index=phase_index,
                  integer_unit=UNIT, source_hashes={s:hashlib.sha256((ROOT/s).read_bytes()).hexdigest() for s in sources},
                  local_bound=total.str(40,more=True), small_disk=small.str(40,more=True),
                  local_plus_small=(total+small).str(40,more=True), transport=cost.str(40,more=True),
                  residual=residual.str(40,more=True), categories={k:v.str(30,more=True) for k,v in category.items()},
                  cross_row_flow=other_row_flow, info=info, elapsed_seconds=time.monotonic()-t0,
                  status='Local component only; final operator bound requires phase and exterior combination.')
    stem = ROOT / args.out
    stem.parent.mkdir(parents=True, exist_ok=True)
    path = Path(str(stem) + '_phase' + str(phase_index) + '.json')
    output['masses'] = masses
    output['plan'] = [[i,j,f] for (i,j),f in sorted(plan.items())]
    path.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ('masses','plan','source_hashes','args')}), flush=True)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--alpha',default='1/2');p.add_argument('--delta',default='1/100000')
    p.add_argument('--angles',type=int,default=64);p.add_argument('--radial',type=int,default=32)
    p.add_argument('--phases',type=int,default=16);p.add_argument('--indices',type=int,nargs='+',required=True)
    p.add_argument('--neighbors',type=int,default=0);p.add_argument('--time-limit',type=float,default=90)
    p.add_argument('--prec',type=int,default=160);p.add_argument('--out',required=True)
    args=p.parse_args()
    for j in args.indices:
        assert 0 <= j <= 2*args.phases
        run(args,j)

if __name__=='__main__':main()

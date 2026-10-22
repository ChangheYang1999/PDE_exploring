#!/usr/bin/env python3
"""Summary of a finished lm_solve.py run, as used in the numerical study: per-round first/last printed labels (beta, |F|), rebuild betas,
final-dict fields, origin identities, alternating sums q_0(-1) = sum_n c[0, n] (-1)^n of the stored a and G coefficient arrays, and the
derived leading far-field mismatch constants 2 (beta_map - beta)/beta_map and (beta_map - beta)/beta_map from the stored full-precision
values. Usage: python3 code/state_summary.py <name> [<name> ...]   (reads runs/<name>.log, runs/<name>.out, runs/<name>.npz)."""
import sys, re, ast, numpy as np

def summarize(name):
    log = open(f'runs/{name}.log').read().splitlines()
    try:
        out = open(f'runs/{name}.out').read().splitlines()
    except FileNotFoundError:
        out = []
    d = np.load(f'runs/{name}.npz', allow_pickle=True)
    beta, bmap = float(d['beta']), float(d['beta_map'])
    ca, cG = d['ca'], d['cG']
    tgt = float(d['a0_target'])
    print(f'=== {name}: stored beta = {beta!r}, beta_map = {bmap!r}, a0_target = {tgt}, N = {int(d["N"])}, M = {int(d["M"])}')
    its = [(i, l) for i, l in enumerate(log) if l.startswith('it ')]
    rounds, cur = [], []
    for i, l in its:
        lab = int(l.split()[1])
        if lab == 0 and cur:
            rounds.append(cur); cur = []
        cur.append(l)
    if cur: rounds.append(cur)
    rb = [l for l in out if 'rebuilding' in l]
    def fld(l, key):
        m = re.search(key + r'=([-+0-9.e]+)', l)
        return m.group(1) if m else None
    for k, r in enumerate(rounds):
        f, g = r[0], r[-1]
        b0, b1 = float(fld(f, 'beta')), float(fld(g, 'beta'))
        FK = r'\|F\|'
        F0, F1 = fld(f, FK), fld(g, FK)
        print(f'  round {k+1}: labels {f.split()[1]}..{g.split()[1]} ({len(r)} lines): beta {fld(f,"beta")} -> {fld(g,"beta")} (net {b1-b0:+.6f}), '
              f'|F| {F0} -> {F1}; first-label c-2b-2 {fld(f,"c-2b-2")}, a0 {fld(f,"a0")}')
        # monotonicity of printed beta within the round
        bs = [float(fld(l, 'beta')) for l in r]
        inc = [(j, bs[j-1], bs[j]) for j in range(1, len(bs)) if bs[j] > bs[j-1]]
        print(f'           printed beta nonincreasing within round: {not inc}; increases at labels {[j for j,_,_ in inc][:8]}{"..." if len(inc)>8 else ""}')
        if k < len(rb): print(f'           {rb[k].strip()}')
    fin = [l for l in log if l.startswith('final:')]
    if fin:
        F = eval(fin[-1][len('final:'):].strip(), {'nan': float('nan'), 'inf': float('inf'), '__builtins__': {}})
        b = F['beta']; a0 = F['a0']; G0 = F['G0']; c = F['c']
        print(f'  final: beta {b!r}, Fnorm {F["Fnorm"]:.6e} ({F["Fnorm"]!r}), Fmax {F["Fmax"]:.3e}, Ra_max/RG_max {F["Ra_max"]:.4f} / {F["RG_max"]:.4f}, '
              f'R1a_max/R1G_max {F.get("R1a_max", float("nan")):.1f} / {F.get("R1G_max", float("nan")):.1f}, n_unknown {F["n_unknown"]}')
        print(f'  origin identities: c - 2 beta - 2 = {c - 2*b - 2:+.2e} (dict c_minus_2b2 {F["c_minus_2b2"]:+.2e}), a0 - target = {a0 - tgt:+.2e}, '
              f'G0 = {G0:.6f} against 2 a0/(2 beta + 1) = {2*a0/(2*b+1):.6f} (difference {G0 - 2*a0/(2*b+1):+.2e})')
    q0a = float(np.sum(ca[0, :] * (-1.0) ** np.arange(ca.shape[1])))
    q0G = float(np.sum(cG[0, :] * (-1.0) ** np.arange(cG.shape[1])))
    print(f'  q_0(-1): a {q0a:.2f}, G {q0G:.2f}')
    print(f'  mismatch constants from stored values: 2 (beta_map - beta)/beta_map = {2*(bmap-beta)/bmap:+.6f}, (beta_map - beta)/beta_map = {(bmap-beta)/bmap:+.6f}')
    it0 = [l for l in log if l.startswith('it   0 ')]
    if it0: print(f'  first printed label-0 line: {it0[0][:120]}')

for n in sys.argv[1:]:
    summarize(n)

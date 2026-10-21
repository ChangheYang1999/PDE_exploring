"""Table of fixed-c_l (or fixed-amplitude) constrained solves from runs/<tag>_hist.json files: constraint, dc_l from a reference state,
iterations, final |F|_2, |F|_inf, C, x*, h(P)-1, identity, stationarity, removable part. Usage:
python3 src/fixcl_table.py runs/ref_state.npz tag1 tag2 ...   (writes runs/fixcl_table.md)"""
import sys, json, numpy as np
LANE = '.'
ref = np.load(sys.argv[1], allow_pickle=True); cl0 = float(ref['c_l']); F20 = float(ref['F2']) if 'F2' in ref.files else float('nan')
print(f'reference {sys.argv[1]}: c_l {cl0:.10f} |F|_2 {F20:.4e}')
hdr = '| tag | constraint | dc_l | its | |F|_2 min | |F|_inf | C | x* | h(P)-1 | ident | stationarity | removable |\n|---|---|---|---|---|---|---|---|---|---|---|---|'
lines = [hdr]
for t in sys.argv[2:]:
    try: h = json.load(open(f'{LANE}/runs/{t}_hist.json'))
    except FileNotFoundError: lines.append(f'| {t} | (missing) |'); continue
    st = h.get('stagnation', {})
    lines.append(f"| {t} | {h['constraint']} | {h['c_l'] - cl0:+.4f} | {len(h['hist']) - 1} | {h['F2']:.4e} | {h['Finf']:.2e} | {h['C']:.6f} | {st.get('xstar', float('nan')):.6f} | {st.get('hP_minus_1', float('nan')):+.1e} | {h['residual_rows']['ident']:+.1e} | {h['stationarity_AtF']:.1e} | {h['removable_QtF']:.1e} |")
out = '\n'.join(lines); print(out); open(f'{LANE}/runs/fixcl_table.md', 'w').write(out + '\n')

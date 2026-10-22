"""consolidate_audits.py -- one consolidated table per state family from the VERIFIER's independent regional residual audits
(verification/verification/*/REGIONAL_RESIDUALS.json; their own inverse and differentiation, never this lane's code), joined with the
state metadata of the archived coefficient files (beta, lambda or eps, a0, K, Nt) and this lane's diagnostics where they exist
(C2 from constvel, Q_R from runs/axis_*.json). Writes artifacts/consolidated_residuals.csv (every region) and
artifacts/consolidated_residuals.md (per-family tables). Read-only on the verifier's directory.
Usage: python3 code/consolidate_audits.py"""
import json, glob, os, re, csv, numpy as np
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# shift 8: the verifier's audit files are packaged under artifacts/verifier/ (same relative layout as the verifier lane); BQ3_VER overrides
VER = os.environ.get('BQ3_VER') or (f'{HERE}/artifacts/verifier' if os.path.isdir(f'{HERE}/artifacts/verifier') else 'verification')
REG_ORDER = [(0, 0.03), (0.03, 0.3), (0.3, 3), (3, 30), (30, 300), (300, float('inf'))]
REG_NAMES = ['0-0.03', '0.03-0.3', '0.3-3', '3-30', '30-300', '300-1e8']
inv = json.load(open(f'{VER}/verification/regional_inventory_20261021T035630Z.json'))
arch = {s['label']: s['archive'] for s in inv['states']}
DIAG = {'eqb_K24': 'runs/eqb24_lambda0.95.npz', 'eqb_K32': 'runs/eqb32_lambda0.95.npz', 'eqb_K40': 'runs/eqb40_lambda0.95.npz',
        'L2v_L1': 'runs/mapL2v_L1.0_beta3.0952.npz', 'L2v_L1p5': 'runs/mbb_b3.0952_lambda0.989973.npz', 'L2v_L2p5': 'runs/mapL2v_L2.5b_beta3.0952.npz',
        'L1l096_L1': 'runs/mapL1l096_L1.0b_beta3.0060477873545817.npz', 'L1l096_L1p5': 'runs/blam24v_lambda0.96.npz', 'L1l096_L2p5': 'runs/mapL1l096_L2.5_beta3.0060477873545817.npz'}   # shift 8: diagnostic re-solves (7m (iii), (vi))
def find_archive(folder, label):
    if label in DIAG and os.path.exists(f'{HERE}/{DIAG[label]}'): return f'{HERE}/{DIAG[label]}'
    if label in arch and os.path.exists(f'{VER}/{arch[label]}'): return f'{VER}/{arch[label]}'
    if label in arch and os.path.exists(f'verification/{arch[label]}'): return f'verification/{arch[label]}'   # fallback to the verifier lane itself
    m = re.match(r'K(\d+)_l0(\d+)', label)      # verifier label K40_l094 -> blam40v_lambda0.94.npz
    if m:
        for c in (f'{folder}/blam{m.group(1)}v_lambda0.{m.group(2)}.npz', f'{HERE}/runs/blam{m.group(1)}v_lambda0.{m.group(2)}.npz'):
            if os.path.exists(c): return c
    def is_state(c):
        try: return 'beta' in np.load(c).files
        except Exception: return False
    m = re.match(r'([A-Za-z0-9_]+)_beta(\d)p(\d+)$', label)   # shift 8: stems with underscores (quadB40_3076_beta3p076)   # labels like blamL2R84_beta3p085, blamL2tight_beta3p1 -> runs/<stem>_beta3.085.npz (exact join; shift 7 fix of a loose prefix match)
    if m:
        c = f'{HERE}/runs/{m.group(1)}_beta{m.group(2)}.{m.group(3)}.npz'
        if os.path.exists(c): return c
    cands = [c for c in glob.glob(f'{folder}/*.npz') if is_state(c)]
    for c in cands:
        if label in os.path.basename(c) or os.path.basename(c).startswith(label.split('_')[0]): return c
    if len(cands) == 1: return cands[0]
    m = re.match(r'K(\d+)_beta([\d.]+)$', label)   # verifier label K32_beta3.04 -> this lane's runs/blamB32_beta3.04.npz (fate run states)
    if m:
        for stem in ('blamB' + m.group(1), 'blamB' + m.group(1) + 'chk', 'blamB' + m.group(1) + 'ext'):   # K32 -> blamB32; K40 -> blamB40chk (3.0315, 3.04) / blamB40ext
            c = f'{HERE}/runs/{stem}_beta{m.group(2)}.npz'
            if os.path.exists(c): return c
    c = f'{HERE}/runs/{label}.npz'                   # labels equal to this lane's file stems (blamB40ext_beta3.076, mbb_b3.0952_lambda0.989973, ...)
    if os.path.exists(c): return c
    m = re.match(r'L2K24_lambda(0\.9\d)(_FAILED)?$', label)   # verifier labels L2K24_lambda0.99 / L2K24_lambda0.98_FAILED -> runs/blamL2k24_lambda0.99.npz / 0.98.npz
    if m and os.path.exists(f'{HERE}/runs/blamL2k24_lambda{m.group(1)}.npz'): return f'{HERE}/runs/blamL2k24_lambda{m.group(1)}.npz'
    m = re.match(r'L2_beta3p(\d+)$', label)         # verifier label L2_beta3p105 -> runs/blamL2B24b_beta3.105.npz (shift 8, packaged inputs)
    if m:
        for stem in ('blamL2B24b', 'blamL2B24L', 'blamL2B24'):
            c = f'{HERE}/runs/{stem}_beta3.{m.group(1)}.npz'
            if os.path.exists(c): return c
    m = re.match(r'L2K32_beta3p(\d+)$', label)      # verifier label L2K32_beta3p0925 -> runs/blamL2B32f_beta3.0925.npz
    if m:
        for c in glob.glob(f'{HERE}/runs/blamL2B32*_beta3.{m.group(1)}.npz'):
            return c
    return None
def family(label):
    if label.startswith('eqb_'): return 'EQ: equal-budget re-solves at (beta, lambda) = (3.0113961, 0.95), K 24 / 32 / 40, 20 map evaluations each (diagnostic, 7m (iii); converged = False)'
    if re.match(r'(L2v_|L1l096_)', label): return 'MS: map-scale re-solves (L 1.0 / 1.5 / 2.5) of the lineage-2 vertex state and a lineage-1 state (diagnostic, 7m (vi))'
    if label.startswith('quad'): return 'Q: six 48-point quadrature restarts and two separately computed K 32 beta 3.062 secant states at 12 and 48 points (shift 8, 7l QUANTIFICATION; the six restarts inherited lambda at secant 0)'
    if re.match(r'(blam\d+v(95)?_lambda|K\d+_l0)', label): return 'L1: additive-forcing lambda path, retied basis, fixed source block (lineage 1)'
    if re.match(r'(blam\d+[gf]_lambda|blam1_|lamc1_)', label): return 'L0: additive-forcing lambda path, fixed basis or reprojected source (diagnostic only)'
    if re.match(r'(K\d+_beta\d|blamB\d+(ext\d?)?_beta)', label): return 'L1b: lineage 1, beta-parameterized continuation (beta fixed per stage, lambda solved; fate run)'
    if re.match(r'(L2|mbb_|blamL2)', label): return 'L2: lineage 2 (y0 2.5 dipole, a0 1, source strain 1.923; lambda path and beta-parameterized continuation)'
    if re.match(r'(bfree|betafree)', label): return 'G: gauge-fixed forcing path (a0 fixed, beta free)'
    if label in ('S0', 'manufactured_picard'): return 'M: manufactured problem and its reference (controls)'
    return 'F: fixed-beta forcing homotopy and fold states (eps < 1)'
rows = []; summary = {}
for f in sorted(glob.glob(f'{VER}/verification/*/REGIONAL_RESIDUALS.json') + glob.glob(f'{VER}/research/*/verification/REGIONAL_RESIDUALS.json')):   # shift 8: the verifier's later audits live under research/<packet>/verification/
    folder = os.path.dirname(f); d = json.load(open(f))
    fold_name = os.path.basename(folder) if os.path.basename(folder) != 'verification' else os.path.basename(os.path.dirname(folder))   # shift 8: research/<packet>/verification -> <packet>
    for st in d['states']:
        lab = st['label']; a = find_archive(folder, lab); meta = {}
        if a and os.path.exists(a):
            try:
                z = np.load(a, allow_pickle=False)
                for k in ['beta', 'beta_basis', 'lam', 'eps', 'a0', 'K', 'Nt', 'obj', 'continuation_accepted']:
                    if k in z.files and z[k].size == 1: meta[k] = float(z[k])
            except Exception as e: meta['err'] = str(e)[:40]
        tab = {}
        for ru in st['runs']:
            for rg in ru['regions']:
                key = (ru['kind'], rg['field'])
                tab.setdefault(key, [None] * 6)
                i = min(range(6), key=lambda j: abs(REG_ORDER[j][0] - rg['r_min']))
                tab[key][i] = (rg['max_abs'], rg['max_ratio'], rg.get('zero_normalizers', 0), rg.get('infinite_ratios', 0))
                rows.append(dict(folder=fold_name, label=lab, kind=ru['kind'], field=rg['field'], region=REG_NAMES[i], max_abs=rg['max_abs'], max_ratio=rg['max_ratio'],
                                 points=rg.get('points'), zero_normalizers=rg.get('zero_normalizers'), infinite_ratios=rg.get('infinite_ratios'), **{f'meta_{k}': v for k, v in meta.items()}))
        summary[(fold_name, lab)] = dict(meta=meta, tab=tab, forcing=st.get('forcing_description', ''), sha=st.get('source_sha256', '')[:12], archive=(os.path.relpath(a, VER) if a else None))
os.makedirs(f'{HERE}/artifacts', exist_ok=True)
with open(f'{HERE}/artifacts/consolidated_residuals.csv', 'w', newline='') as fh:
    keys = sorted({k for r in rows for k in r}); w = csv.DictWriter(fh, fieldnames=keys); w.writeheader(); [w.writerow(r) for r in rows]
def fmt(x): return '-' if x is None else (f'{x:.2e}' if abs(x) < 1e-2 or abs(x) >= 1e3 else f'{x:.3f}')
def mx(t, kind, field, j):
    v = t.get((kind, field)); 
    if not v: return None
    vals = [r[j] for r in v if r is not None]; return max(vals) if vals else None
out = ['# Consolidated independent residual tables (verifier audits), by state family', '',
       'Source: the verifier lane\'s REGIONAL_RESIDUALS.json files (their own whole-plane inverse and seven-point differentiation; sampled maxima on field-dependent sets of 13630-18144 points,',
       'with 145, 161, 166, 177 or 189 radii from 1e-5 to 1e8, no denominator floor). "forced" = the residual of the forced problem the state was solving (transport kind); "B2-P" = the',
       'residual of the unforced equations with the state\'s own whole-plane velocity (self kind). F, G: desingularized ratios |R_F|/N_F, |R_G|/N_G (equal to the',
       'Cartesian ratios off the axis); Theta, Omega: Cartesian absolute residuals. Regions in r: ' + ', '.join(REG_NAMES) + ' (sampled maxima; the last region ends at the largest evaluated radius, 1e8). Of the 123 audit entries, 121 describe forced-problem states and two are manufactured controls. The entries cover 119 distinct archive hashes; a distinct hash does not establish a mathematically distinct field.',
       'None is a B2-P candidate (B2-P normalized maxima 0.3-1). Metadata (beta, lambda/eps, a0, K, Nt) read from the archived coefficient files.', '']
fams = sorted({family(lab) for (_, lab) in summary})
for fam in fams:
    out += [f'## {fam}', '', '### Summary (maximum over all regions)', '',
            '| audit folder | state | beta | lambda | eps | a0 | K | Nt | forced max ratio F | forced max ratio G | forced max abs Theta | forced max abs Omega | B2-P max ratio F | B2-P max ratio G | B2-P max abs Theta | B2-P max abs Omega |',
            '|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    items = sorted([(k, v) for k, v in summary.items() if family(k[1]) == fam], key=lambda kv: (kv[1]['meta'].get('K', 0), -(kv[1]['meta'].get('lam', 0)), kv[1]['meta'].get('eps', 0), kv[0][1]))
    for (fold, lab), v in items:
        m = v['meta']; t = v['tab']
        g = lambda k: ('-' if k not in m else (f'{m[k]:.6f}' if k in ('beta',) else (f'{m[k]:.4g}' if k in ('lam', 'eps', 'a0') else f'{int(m[k])}')))
        out.append(f"| {fold} | {lab} | {g('beta')} | {g('lam')} | {g('eps')} | {g('a0')} | {g('K')} | {g('Nt')} | {fmt(mx(t,'transport','F',1))} | {fmt(mx(t,'transport','G',1))} | {fmt(mx(t,'transport','Theta',0))} | {fmt(mx(t,'transport','Omega',0))} | {fmt(mx(t,'self','F',1))} | {fmt(mx(t,'self','G',1))} | {fmt(mx(t,'self','Theta',0))} | {fmt(mx(t,'self','Omega',0))} |")
    out += ['', '### B2-P (unforced, own velocity) normalized maxima by region: F ratio / G ratio', '',
            '| state | ' + ' | '.join(REG_NAMES) + ' |', '|---|' + '---:|' * 6]
    for (fold, lab), v in items:
        t = v['tab']; F = t.get(('self', 'F'), [None]*6); G = t.get(('self', 'G'), [None]*6)
        out.append(f"| {lab} | " + ' | '.join(f"{fmt(F[j][1] if F[j] else None)} / {fmt(G[j][1] if G[j] else None)}" for j in range(6)) + ' |')
    out += ['', '### B2-P absolute maxima by region: Theta / Omega (Cartesian)', '',
            '| state | ' + ' | '.join(REG_NAMES) + ' |', '|---|' + '---:|' * 6]
    for (fold, lab), v in items:
        t = v['tab']; F = t.get(('self', 'Theta'), [None]*6); G = t.get(('self', 'Omega'), [None]*6)
        out.append(f"| {lab} | " + ' | '.join(f"{fmt(F[j][0] if F[j] else None)} / {fmt(G[j][0] if G[j] else None)}" for j in range(6)) + ' |')
    out += ['', '### Forced-problem normalized maxima by region: F ratio / G ratio', '',
            '| state | ' + ' | '.join(REG_NAMES) + ' |', '|---|' + '---:|' * 6]
    for (fold, lab), v in items:
        t = v['tab']; F = t.get(('transport', 'F'), [None]*6); G = t.get(('transport', 'G'), [None]*6)
        out.append(f"| {lab} | " + ' | '.join(f"{fmt(F[j][1] if F[j] else None)} / {fmt(G[j][1] if G[j] else None)}" for j in range(6)) + ' |')
    out.append('')
open(f'{HERE}/artifacts/consolidated_residuals.md', 'w').write('\n'.join(out))
print(f'{len(summary)} states, {len(rows)} rows; families: {fams}')
missing = [k for k, v in summary.items() if not v['meta']]
print('states without archive metadata:', missing)

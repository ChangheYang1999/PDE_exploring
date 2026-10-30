"""snap_gpu.py: compose the snapshot description of a GPU-run candidate from its JSON records and write the immutable snapshot.
argv: TAG ID "intro text (basis, objective rows, held-out set, steps)" "notes" [heldout_file_sha_text] [heldin_rows comma list or '-'] [compare tags: 016,017,020,...]"""
import sys, json, os, subprocess, hashlib
sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/lib')
opt = 'RUN_ROOT/numerics_N1N2/numerics/optimization'
TAG, CID, intro, notes = sys.argv[1:5]; hsha = sys.argv[5] if len(sys.argv) > 5 else ''; heldin = [q for q in (sys.argv[6].split(',') if len(sys.argv) > 6 and sys.argv[6] != '-' else [])]
cmp = (sys.argv[7] if len(sys.argv) > 7 else '016,020').split(',')
REF = {'013': 'd2w_j7_n4_E2bal_pairU_cpu_m16', '016': 'quot013_legqs25_m9to15_cpu_m16', '017': 'quot013_legqs50_m9to15_cpu_m16', '020': 'quot013_legqs25p50_m9to15_cpu_m16', '021': 'legqs25p50_heldin14_gpu_m16', '022': 'legqs25_m16to23_gpu_m16', '023': 'legqs25p100_m9to15_gpu_m16', '024': 'quot013_legqs25_m9to15_gpu_m32', '025': 'combined_s25s50s100_m16to23_heldin14_gpu_m16', '026': 'legqs25_m16to23_heldin1e16_gpu_m16', '027': 'legqs25_m16to23_cont60_gpu_m16', '028': 'legqs25_nin24_m9to15_gpu_m16'}
def L(t, kind): p = f'{opt}/candD2/{t}_{kind}.json'; return json.load(open(p)) if os.path.exists(p) else None
w3 = L(TAG, 'weaktests3'); d = L(TAG, 'diag2'); w2 = L(TAG, 'weaktests2'); assert w3 and d, 'missing weaktests3 or diag2'
P = w3['probes']; C = {k: L(REF[k], 'weaktests3')['probes'] for k in cmp}
REG = [f'{n}:{K}' for n in (19, 23, 25, 29, 31) for K in (600, 900, 1200, 1800, 2400)]
K512 = ['19:521', '21:522', '23:523', '25:524', '27:525', '29:526', '31:527']; SMALL = ['19:9', '23:11', '27:13', '31:15', '19:17', '23:19', '27:21']
def fm(D, q): return f"{D[q]['m_lower_bound']:.2e}" if q in D else '-'
def row(q): return f"({q.replace(':', ',')}) " + ' / '.join(fm(C[k], q) for k in cmp) + f" / {fm(P, q)}"
regs = [(q, P[q]['m_lower_bound']) for q in REG]; qb, vb = max(regs, key=lambda x: x[1]); nab = sum(v > 4.5717e-4 for _, v in regs)
hdr = f"HELD-OUT values (FLOAT weak_tests3 rule, MID 32; {' / '.join(cmp)} / {CID.split('-')[2]}): registered probes: " + '; '.join(row(q) for q in REG)
hdr += f". Largest registered held-out value ({qb.replace(':', ', ')}) {vb:.2e}; {nab} of the 25 registered values above the graded ceiling 4.5717e-4"
hdr += " (016: 7, 020: 8). N4-160 K0 = 512 probes" + (" (HELD IN as objective rows for this candidate, reported as such, not as evidence)" if any(q in heldin for q in K512) else " (held out)") + ": " + '; '.join(row(q) for q in K512)
hdr += ". Small-K0 held-out probes: " + '; '.join(row(q) for q in SMALL) + '.'
log = open(f'{opt}/candD2/{TAG}.log').read().strip().splitlines(); acc = [l for l in log if 'ACC' in l]; last = acc[-1] if acc else log[-1]; loss = last.split()[5]
fin = [l for l in open(f'{opt}/logs/{TAG}.out').read().splitlines() if l.startswith('FINAL (')]; fin = fin[-1][fin[-1].index(':')+1:].strip() if fin else 'n/a'
b = d['BL2']
diag = f"Optimizer report (MID 16): {fin}. FLOAT (diag2, MID 32): G0 {d['G0']:.4f} (016 0.3089, 017 0.3209, 020 0.3201), G1 {d['G1']:.3f}, P2 {d['P2']:.1f}, rF {d['rF']:.3f}, H {d['H']:.4f}, sup|F| {d['supF']:.4f}, theta_inner {b['theta_inner_sup']:.4f}, kappa_inner {b['kappa_inner']:.4f} ((B-L2) margin {b['margin_c_plus_1_minus_theta_minus_kappa_minus_2']:+.4f})."
if w2: diag += f" First-mode weak probe (27 sampled k <= 4096, objective rows): largest sampled value {w2['weak_distance_lower_bound_FLOAT']:.2e} at k = {w2.get('k_of_max', '?')}."
desc = f"{intro} LOSS (MID 16) final {float(loss):.5e}. 421 exact rows; ten nonautomatic EXACT-ZERO sectors (first surviving exponent -2.7904). {hdr} {diag} Trial comparison only: no span, mass or stationarity inference (T4-340); not a certification target (registered held-out FLOAT values above the graded ceiling would, if certified, exclude it like 016 to 020)." + (f" Held-out registration file: {hsha}." if hsha else '')
ex = f'{opt}/candD2/{TAG}_exact.json'
cmd = ['python3', '-B', f'{opt}/snap_from_diag2.py', CID, 'C1-A2-d2', ex, f'{opt}/candD2/{TAG}_sectors.json', f'{opt}/candD2/{TAG}_diag2.json', loss, (intro.split(' Objective: ')[-1] if ' Objective: ' in intro else intro), desc, notes] + ([f'{opt}/candD2/{TAG}_weaktests2.json'] if w2 else [])
env = dict(os.environ, CUDA_VISIBLE_DEVICES='', PYTHONDONTWRITEBYTECODE='1')
r = subprocess.run(cmd, capture_output=True, text=True, env=env); print(r.stdout[-300:], r.stderr[-500:])
print('exact sha256', hashlib.sha256(open(ex, 'rb').read()).hexdigest())

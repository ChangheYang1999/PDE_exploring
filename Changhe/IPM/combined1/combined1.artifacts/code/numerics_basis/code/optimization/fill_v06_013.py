# Fill the 013 placeholders of numerics_v06 (stage1 -> published): PAIRSLUG, PAIR_SUMMARY, PAIRSECTION, STATUS, BRIDGE_PENDING. argv: none (reads the pairU JSONs)
import json, os, datetime, hashlib, subprocess, re
root = 'RUN_ROOT/numerics_N1N2'; opt = root+'/numerics/optimization'
src = open(root+'/numerics/NUMERICS_v06_published_stage1.md').read()
T = 'd2w_j7_n4_E2bal_pairU_cpu_m16'
w2 = json.load(open(f'{opt}/candD2/{T}_weaktests2.json')); d = json.load(open(f'{opt}/candD2/{T}_diag2.json')); ex = json.load(open(f'{opt}/candD2/{T}_exact.json'))
w3 = json.load(open(f'{opt}/candD2/{T}_weaktests3.json')) if os.path.exists(f'{opt}/candD2/{T}_weaktests3.json') else None
w3r = json.load(open(f'{opt}/candD2/d2w_j7_n4_E2bal_mid180_weaktests3.json')) if os.path.exists(f'{opt}/candD2/d2w_j7_n4_E2bal_mid180_weaktests3.json') else None
ref2 = json.load(open(f'{opt}/candD2/d2w_j7_n4_E2bal_mid180_weaktests2.json'))
W = {int(k): v for k, v in w2['NORM-T-WEAK-v1_a0'].items()}; Wr = {int(k): v for k, v in ref2['NORM-T-WEAK-v1_a0'].items()}
sha = hashlib.sha256(open(f'{opt}/candD2/{T}_exact.json', 'rb').read()).hexdigest()
log = open(f'{opt}/candD2/{T}.log').read().strip().splitlines(); last = log[-1]
rows = ['| k | I_k (007) | I_k (013) | m_k (007) | m_k (013) |', '|---|---|---|---|---|']
for k in sorted(W):
    rows.append(f"| {k} | {Wr[k]['I_k_signed_mesh']+Wr[k]['I_k_far']:+.3e} | {W[k]['I_k_signed_mesh']+W[k]['I_k_far']:+.3e} | {Wr[k]['m_lower_bound']:.3e} | {W[k]['m_lower_bound']:.3e} |")
kmax = max(W, key=lambda k: W[k]['m_lower_bound']); kmaxr = max(Wr, key=lambda k: Wr[k]['m_lower_bound'])
bl = d['BL2']
mode7 = ''
if w3 and w3r:
    p7 = {q: v for q, v in w3['probes'].items() if v['n'] == 7}; p7r = {q: v for q, v in w3r['probes'].items() if v['n'] == 7}
    mode7 = '\nHeld-out angular probes (weak_tests3.py, N4-160 family, FLOAT): best m by mode for 007 -> 013: ' + '; '.join(f"n = {n}: {w3r['best_m_by_mode'][str(n)]:.2e} -> {w3['best_m_by_mode'][str(n)]:.2e}" for n in (1, 3, 5, 7, 9, 11, 15, 21, 31)) + f".\nMode-7 pairings (n = 7, K = 3 + K0): " + '; '.join(f"K = {v['K']}: I {p7r[q]['I_signed_mesh']:+.3e} -> {v['I_signed_mesh']:+.3e}, m {p7r[q]['m_lower_bound']:.2e} -> {v['m_lower_bound']:.2e}" for q, v in sorted(p7.items(), key=lambda z: z[1]['K'])) + f". Best probe 013: {w3['best_probe']} (m = {w3['best_m']:.3e}); 007: {w3r['best_probe']} ({w3r['best_m']:.3e}). (c1-n4's certified mode-7 value for 007 is 0.004769, T4-185: my FLOAT H bound and A, B, C are not the same construction, so these are comparisons 007 vs 013 under one FLOAT rule, not reproductions of T4-185.)"
else:
    mode7 = '\nHeld-out angular probes (weak_tests3.py): PENDING (running on 013 and 007).'
sec = f"""Run: run_pair.py from the 007 coefficients, balanced E_2 objective of 007 (wlog 2^18*100, wkap 3e6) plus 27 rows sqrt(1e15) I_k, k in {{0..8, 12, ..., 4096}}
(first-mode probes phi_k = y t^k u0^2; uniform weight; MID 16 radial rule, midpoint 180), 12 Gauss-Newton steps on one CPU core (about 285 s per step).
Last step line: {last[:160]}.
Snapshot C1-N1-013-pairU-from007 (exact JSON sha256 {sha}; same basis and 421 exact rows as 007; eleven EXACT-ZERO sectors).
FLOAT (diag2, MID 32): G0 {d['G0']:.4f} (007 0.3767), G1 {d['G1']:.3f} (3.439), P2 {d['P2']:.1f} (190.8), rF {d['rF']:.3f} (7.83), H {d['H']:.4f} (0.636), sup|F| {d['supF']:.4f} (0.138),
theta {bl['theta_inner_sup']:.4f}, kappa {bl['kappa_inner']:.4f} (margin {bl['margin_c_plus_1_minus_theta_minus_kappa_minus_2']:+.3f}), X3 {d['X3_proxy_raw']:.1f}, E2 {d['E2_proxy_raw_with_H']:.1f}, R_nec(2^-18) {d['point_tests']['2^-18']['R_nec']:.3e}.
First-mode weak probes at MID 32 (the optimization rule MID 16 is not used for any reported value; N4-150):
""" + '\n'.join(rows) + f"""
Maximum over the 27 k values: 007 {Wr[kmaxr]['m_lower_bound']:.3e} (k = {kmaxr}) -> 013 {W[kmax]['m_lower_bound']:.3e} (k = {kmax}).
Reading: the penalty rows reduce the first-mode pairings at the k where the basis has leverage (k <= about 1000, r <= 25) by two to three orders of magnitude at
essentially no cost in the other components (the objective parts F, G, P, K changed by less than 1 percent), while the rows with k >= 1536 (r >= 28) barely move:
their Jacobian in this basis is tiny (the same unreachability that made the per-k-weighted and hard-constraint variants explode). So NC-T-DIST with first-mode
probes at small k is a soft constraint of the objective; the mid-field probes (k of order 1e4, r of order 50 to 100) and the angular mode-7 probe (T4-185) are not.
{mode7}
The run with 75 additional angular probes (N4-160 family, n = 3..31) is C1-N1-014 (in progress at publication; see section 7)."""
src = src.replace('PAIRSECTION', sec)
src = src.replace('PAIR_SUMMARY', f"the maximum of m_k over k <= 4096 went from {Wr[kmaxr]['m_lower_bound']:.2e} (007) to {W[kmax]['m_lower_bound']:.2e} (013), with G0 {d['G0']:.4f} and kappa {bl['kappa_inner']:.4f}")
src = src.replace('PAIRSLUG', 'pairU-from007')
src = src.replace('BRIDGE_PENDING', 'running (chainM2) at publication; values in v07')
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
status = f"""Published {now}. Best candidate unchanged: C1-N1-007 (certified G0 0.3767, (B-L2), distance 0.004769 in mode 7). Running: C1-N1-014 run (102 pairing
rows including the 75 angular probes of N4-160, uniform weight 1e12, MID 16, 12 steps, core 52; the 1e15 version was killed after one step because the
angular pairings of 007, of order 1e-4 to 1e-3 each, dominated the objective by 1000x and the Gauss-Newton step raised the F part 20x); high-k and bridge
probes for the remaining candidates (core 53). Next: snapshot 014 with weak_tests2/3 and diag2 (about 05:40Z) and numerics_v07; then NUMERICS_FINAL.md and
artifacts by 08:30Z (H12). Corrections carried from c1-coord 02:48Z: the graded-box exclusion of 007 comes from the N4-102 point gap (N4-145), the 14 percent
difference in v05 section 5b compared k = 8 with k = 128 (N4-146), and every FLOAT value of this lane is CPU float64 (the 'float64 GPU' header of v05 section
5 applies to runs before 00:58Z only). The conditioning statement of section 5 is to be read on the 1922 independent generators (N4-158): the 1022 zero
singular values are exactly the redundant directions and the remaining spectrum is that of the independent problem."""
src = src.replace('STATUS', status)
src = src.replace('# numerics_v06 (batch N publication; author c1-n1) -- DRAFT', '# numerics_v06 (batch N publication; author c1-n1)')
src = re.sub(r'- version: numerics_v06; UTC time: [0-9T:Z-]+;', f'- version: numerics_v06; UTC time: {now};', src)
open(root+'/numerics/NUMERICS_v06_published.md', 'w').write(src)
left = [m for m in re.findall(r'[A-Z_]{7,}', src) if m in ('PAIR_SUMMARY', 'PAIRSECTION', 'BRIDGE_PENDING', 'PAIRSLUG', 'WEAKTABLE', 'FARWEAK')]
print(now, len(src), 'leftover placeholders:', left)

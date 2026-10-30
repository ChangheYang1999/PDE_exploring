# Assemble numerics_v07 from the draft frame and the JSON records that exist at run time (missing records -> 'PENDING' text).
import json, os, re, datetime, hashlib, subprocess, math
root = 'RUN_ROOT/numerics_N1N2'; opt = root+'/numerics/optimization'
src = open(root+'/numerics/NUMERICS_v07_draft.md').read()
def L(p): return json.load(open(f'{opt}/candD2/{p}')) if os.path.exists(f'{opt}/candD2/{p}') else None
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
# ---- 014
T = 'd2w_j7_n4_E2bal_pairB_cpu_m16'
w2 = L(f'{T}_weaktests2.json'); w3 = L(f'{T}_weaktests3.json'); d = L(f'{T}_diag2.json')
r2 = L('d2w_j7_n4_E2bal_mid180_weaktests2.json'); r3 = L('d2w_j7_n4_E2bal_mid180_weaktests3.json'); u2 = L('d2w_j7_n4_E2bal_pairU_cpu_m16_weaktests2.json'); u3 = L('d2w_j7_n4_E2bal_pairU_cpu_m16_weaktests3.json')
if w2 and w3 and d:
    sha = hashlib.sha256(open(f'{opt}/candD2/{T}_exact.json', 'rb').read()).hexdigest(); bl = d['BL2']
    W = {int(k): v for k, v in w2['NORM-T-WEAK-v1_a0'].items()}; Wr = {int(k): v for k, v in r2['NORM-T-WEAK-v1_a0'].items()}; Wu = {int(k): v for k, v in u2['NORM-T-WEAK-v1_a0'].items()}
    kmax = max(W, key=lambda k: W[k]['m_lower_bound'])
    rows = ['| k | m_k 007 | m_k 013 | m_k 014 |', '|---|---|---|---|'] + [f"| {k} | {Wr[k]['m_lower_bound']:.2e} | {Wu[k]['m_lower_bound']:.2e} | {W[k]['m_lower_bound']:.2e} |" for k in sorted(W)]
    modes = ['| mode n | best m 007 | best m 013 | best m 014 |', '|---|---|---|---|'] + [f"| {n} | {r3['best_m_by_mode'][str(n)]:.2e} | {u3['best_m_by_mode'][str(n)]:.2e} | {w3['best_m_by_mode'][str(n)]:.2e} |" for n in range(1, 32, 2)]
    log = open(f'{opt}/candD2/{T}.log').read().strip().splitlines(); last = [l for l in log if 'ACC' in l][-1]
    sec = f"""Run: run_pair.py from the 007 coefficients, balanced E_2 objective of 007 plus 102 rows sqrt(1e12) I (27 first-mode probes k in {{0..8, 12, ..., 4096}} and the 75 angular
probes phi_(n,K) = r v^2 t^K sin(n theta), n = 3..31, K = (n-1)/2 + {{0, 8, 32, 128, 512}} of N4-160), MID 16 radial rule, 12 CPU steps (about 270 s each).
The uniform weight 1e15 (as in 013) was wrong for the angular rows: the angular pairings of 007 are 1e-4 to 2e-3 each, so PAIR = 1.8e10 dominated the 1.7e7
objective and the first Gauss-Newton step raised the F part 20x; at 1e12 the pairing part (3.6e7 at the start) is balanced against the rest. Last accepted
step: {last[:150]}.
Snapshot C1-N1-014-pairB-from007 (exact JSON sha256 {sha}; same basis and 421 exact rows as 007; eleven EXACT-ZERO sectors).
FLOAT (diag2, MID 32): G0 {d['G0']:.4f} (007 0.3767, 013 0.3722), G1 {d['G1']:.3f}, P2 {d['P2']:.1f}, rF {d['rF']:.3f}, H {d['H']:.4f}, sup|F| {d['supF']:.4f}, theta {bl['theta_inner_sup']:.4f},
kappa {bl['kappa_inner']:.4f} (margin {bl['margin_c_plus_1_minus_theta_minus_kappa_minus_2']:+.3f}), X3 {d['X3_proxy_raw']:.1f}, E2 {d['E2_proxy_raw_with_H']:.1f}, R_nec(2^-18) {d['point_tests']['2^-18']['R_nec']:.3e}.
First-mode probes (MID 32; max over k <= 4096: 007 1.31e-4, 013 {u2['weak_distance_lower_bound_FLOAT']:.2e}, 014 {w2['weak_distance_lower_bound_FLOAT']:.2e} at k = {kmax}):
""" + '\n'.join(rows) + "\nHeld-out and in-objective angular probes (weak_tests3, N4-160 family, FLOAT; for 014 the rows n = 3..31 at these K WERE in the objective, so only the first-mode\nprobes not in the list and the comparison with 013 are held-out evidence; 013 had no angular rows):\n" + '\n'.join(modes) + f"\nBest probe: 007 {r3['best_probe']} ({r3['best_m']:.2e}), 013 {u3['best_probe']} ({u3['best_m']:.2e}), 014 {w3['best_probe']} ({w3['best_m']:.2e})."
    src = src.replace('SEC014', sec)
    src = src.replace('PAIR014SUMMARY', f"G0 {d['G0']:.4f}, kappa {bl['kappa_inner']:.4f}; first-mode max m over k <= 4096 {w2['weak_distance_lower_bound_FLOAT']:.2e} (k = {kmax}); best N4-160-family probe {w3['best_probe']} with m = {w3['best_m']:.2e} (007: 2.87e-3 at (7,131); 013: 1.12e-3 at (21,522)).")
else:
    src = src.replace('SEC014', 'PENDING (run in progress at publication).').replace('PAIR014SUMMARY', 'PENDING.')
# ---- newton steps
def newton_block(tag, label):
    out = []
    for lam in ('1e-6', '1e-4'):
        n = L(f'{tag}_newton_step_lam{lam}.json')
        if n: out.append(f"| {label} | {lam} | {n['G0_mesh']:.4f} | {n['linearized_residual_L2']:.4f} | {n['F_after_step_L2']:.4f} | {n['h0_L2']:.3e} | {n['pairings_F']['7:131']:+.3e} -> {n['pairings_linearized']['7:131']:+.3e} | {n['pairings_F']['1:0']:+.3e} -> {n['pairings_linearized']['1:0']:+.3e} |")
    return out
nrows = ['| candidate | LM lam | ||F||_2 | linearized ||F + J delta||_2 | ||F(a + delta)||_2 | ||h0||_2 | mode-7 (7,131) pairing F -> F + J delta | mode-1 k = 0 pairing |', '|---|---|---|---|---|---|---|---|'] + newton_block('007', 'C1-N1-007') + newton_block('013', 'C1-N1-013')
secn = """Definition (theory_v03 R6(b)): min over delta in the constraint null space (421 exact rows and the 5 linearized Taylor rows) of ||F(a) + J delta||_(L^2(0.02 <= r <= 1e4)),
J = dF/da, so J delta = L h0 with h0 the density of delta (the quadratic term is reported separately); solved by the column-scaled normal equations with
Levenberg-Marquardt damping lam (the undamped solve, lam = 1e-10, gives a meaningless step in this rank-deficient basis: linearized residual 0.66 > 0.38,
||h0||_2 0.053, negative predicted reduction). MID 24 rule, midpoint 180. FLOAT.
""" + '\n'.join(nrows) + """
Reading: in the 007 generator span the Galerkin L^2 Newton step has ||h0||_2 of order 1.7e-2 to 1.8e-2 (T4-185 proves > 0.0047694 for every L^2 Newton step from 007;
consistent) and reduces the L^2 residual only from 0.377 to 0.34: this is the L^2 floor of the span, the same limitation as the optimizer plateau. The step
reduces the (7, 131) pairing of the linearized residual by a factor 10 to 40, within R9(e)'s bound |<F + L h0, phi>| >= |I| - D ||h0||_2. These numbers are
the design objective theory_v03 asks for; they say that no basis of this family brings the first Newton step near a registered ball (factor 4e3 to the
largest scalar budget), i.e. the obstruction is the span, not the objective. Note (c1-t1, numerics_v06 ACK): the coordinate-invariant step uses the physical
Gram on the admissible tangent (T4-229); the Euclidean damping used here is basis-dependent, so the two lam values bracket the FLOAT answer."""
src = src.replace('SECNEWTON', secn)
n7 = L('007_newton_step_lam1e-6.json')
src = src.replace('NEWTONSUMMARY', f"for 007 (lam 1e-6) ||h0||_2 = {n7['h0_L2']:.3e}, linearized residual 0.377 -> {n7['linearized_residual_L2']:.3f}, mode-7 (7,131) pairing -1.69e-4 -> {n7['pairings_linearized']['7:131']:+.2e} (FLOAT, MID 24); the span's L^2 floor, not the objective, limits the first Newton step." if n7 else 'PENDING.')
# ---- na cells
cells = []
for S, cid in (('d2w_j7_n4_X3bal_mid180', '008'), ('d2w_j7_n4_X3balK_mid180', '009'), ('d2w_j7_n4_X3bal_legqs_mid180', '010')):
    c = L(f'{S}_na_cells.json')
    if c: cells.append(f"| C1-N1-{cid} | " + ' | '.join(f"{x['N_h_modes_1_3_FLOAT']:.3g} ({x['ratio']:.2f})" for x in c['cells']) + f" | {'all cells excluded (FLOAT)' if c['all_cells_excluded_FLOAT'] else 'NOT all excluded'} |")
secc = ("Cells [l, h] of a: [0,1/4], [1/4,1/2], [1/2,3/4], [3/4,1], [1,5/4], [5/4,3/2], [3/2,7/4]; thresholds at l (theory_v03 section 5): 15.88162, 8.716729, 4.799949, 2.565236, 1.263642, 0.5028299, 0.06411577. Entry: FLOAT mode 1+3 projected N_h at the right end (ratio to the threshold); a cell is excluded when a certified LB exceeds the threshold.\n| candidate | [0,1/4] | [1/4,1/2] | [1/2,3/4] | [3/4,1] | [1,5/4] | [5/4,3/2] | [3/2,7/4] | FLOAT verdict |\n|---|---|---|---|---|---|---|---|---|\n" + '\n'.join(cells) + "\n(c1-n4's N4-186 found 008 fails the seven-cell test exactly; these FLOAT values are proxies for 009 and 010 pending c1-n4.)") if cells else 'PENDING.'
src = src.replace('SECNACELLS', secc).replace('NACELLSUMMARY', ('FLOAT proxies computed for ' + ', '.join(['008', '009', '010'][:len(cells)]) + ' (section 3); every cell ratio above 1 where marked; exact LBs are c1-n4\'s.') if cells else 'PENDING.')
# ---- quotient
q7 = os.path.exists(f'{opt}/logs/quotient_007.out'); qs = L('007_quot_gn_spectrum.json')
qtxt = open(f'{opt}/logs/quotient_007.out').read().strip().splitlines() if q7 else []
secq = ("optimization/quotient_basis.py: block-diagonal exact rref (python-flint) of the canonical-term matrix of the generators, pivot generators kept, coefficients re-expressed exactly; verification: identical merged canonical terms. Output for 007: " + ' / '.join(qtxt[:2]) + (f"\nPhysical Gauss-Newton spectrum on the quotient basis (gn_spectrum.py, MID 16, balanced objective): reduced dimension {qs['reduced_dim']} (constraint rank {qs['constraint_rank']}), scaled singular values: min {qs['scaled_sv_quantiles']['0']:.3e}, 1 percent {qs['scaled_sv_quantiles']['0.01']:.3e}, 10 percent {qs['scaled_sv_quantiles']['0.1']:.3e}, median {qs['scaled_sv_quantiles']['0.5']:.3e}, max {qs['scaled_sv_quantiles']['1']:.3e}; raw condition number {qs['raw_cond']:.3e}; reduced gradient norm relative {qs['reduced_gradient_norm']/(math.sqrt(qs['phi'])*qs['raw_sv_max']):.2e}. Resolution of a binary64 normal-matrix spectrum is about 1.5e-8 of the largest singular value (theory_v03 R9(c)); no inverse bound is claimed (R9(d))." if qs else "\nSpectrum on the quotient basis: PENDING.")) if q7 else 'PENDING.'
src = src.replace('SECQUOT', secq).replace('QUOTSUMMARY', (qtxt[0] if qtxt else 'PENDING') + ('; physical spectrum in section 4.' if qs else ''))
# ---- bridge
br = L('d2w_j7_n4_E2bal_mid180_weaktests2_bridge.json')
if br:
    Wb = {int(k): v for k, v in br['NORM-T-WEAK-v1_a0'].items()}
    fw = L('007_far_weak.json'); fwk = {r['k']: r for r in fw['rows']} if fw else {}
    brows = ['| k | r_peak | I_k mesh (0.02 <= r <= 8356) | m_k mesh | I_far exact sectors | m_far estimate |', '|---|---|---|---|---|---|'] + [f"| {k} | {math.sqrt((2*k-0.7904)/4.7904):.0f} | {Wb[k]['I_k_signed_mesh']:+.3e} | {Wb[k]['m_lower_bound']:.3e} | {fwk[k]['I_far']:.3e} | {fwk[k]['m_far_est']:.3e} |" if k in fwk else f"| {k} | {math.sqrt((2*k-0.7904)/4.7904):.0f} | {Wb[k]['I_k_signed_mesh']:+.3e} | {Wb[k]['m_lower_bound']:.3e} | - | - |" for k in sorted(Wb)]
    secb = "007, first-mode probes k = 1e5 to 1e7 on the mesh (the probe peaks at r 200 to 2600, inside the 8356 mesh) against the exact-sector far-field values of far_weak.py:\n" + '\n'.join(brows) + "\nReading: BRIDGEREADING"
    src = src.replace('SECBRIDGE', secb).replace('BRIDGESUMMARY', 'section 5 (mesh against exact-sector values at k = 1e6 and 3.2e6).')
else:
    src = src.replace('SECBRIDGE', 'PENDING.').replace('BRIDGESUMMARY', 'PENDING.')
src = src.replace('PUBTIME', now)
for ph, lane in (('COORDTIME', 'c1-coord'), ('N4TIME', 'c1-n4'), ('N3TIME', 'c1-n3')):
    t = subprocess.run(['grep', '-m1', '-o', r'^## 2026-10-29T[0-9:.+]*', f'RUN_ROOT/{lane}/NOTES_FOR_TEAM.md'], capture_output=True, text=True).stdout.strip().replace('## ', '')[:20]
    src = src.replace(ph, t or 'latest')
open(root+'/numerics/NUMERICS_v07_stage.md', 'w').write(src)
print(now, len(src), 'placeholders left:', sorted(set(re.findall(r'\b(?:SEC[A-Z0-9]+|[A-Z]+SUMMARY|STATUS|QUOT015|BRIDGEREADING|PENDING)\b', src))))

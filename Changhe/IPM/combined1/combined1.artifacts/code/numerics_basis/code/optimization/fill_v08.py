# Assemble numerics_v08 from numerics/NUMERICS_v08_draft.md and the JSON records (015, 016, gn_svd, bridge). Missing records -> PENDING text.
import json, os, re, datetime, hashlib, subprocess, math
root = 'RUN_ROOT/numerics_N1N2'; opt = root+'/numerics/optimization'
src = open(root+'/numerics/NUMERICS_v08_draft.md').read()
def L(p): return json.load(open(f'{opt}/candD2/{p}')) if os.path.exists(f'{opt}/candD2/{p}') else None
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
r3 = L('d2w_j7_n4_E2bal_mid180_weaktests3b.json') or L('d2w_j7_n4_E2bal_mid180_weaktests3.json'); u3 = L('d2w_j7_n4_E2bal_pairU_cpu_m16_weaktests3b.json') or L('d2w_j7_n4_E2bal_pairU_cpu_m16_weaktests3.json'); b3 = L('d2w_j7_n4_E2bal_pairB_cpu_m16_weaktests3b.json') or L('d2w_j7_n4_E2bal_pairB_cpu_m16_weaktests3.json')
HELD = ['19:521', '21:522', '23:523', '25:524', '27:525', '29:526', '31:527', '23:600', '25:600', '23:1200', '25:1200', '23:1800', '25:1800', '23:2400', '25:2400', '29:2400']   # N4-160 K~520 set and the theory_v04 held-out set (never objective rows)
def cand_section(T, cid, intro, held_note):
    w2 = L(f'{T}_weaktests2.json'); w3 = L(f'{T}_weaktests3.json'); d = L(f'{T}_diag2.json')
    if not (w2 and w3 and d): return None, None
    sha = hashlib.sha256(open(f'{opt}/candD2/{T}_exact.json', 'rb').read()).hexdigest(); bl = d['BL2']
    ex = json.load(open(f'{opt}/candD2/{T}_exact.json')); ngen = len(ex['generators'])
    log = open(f'{opt}/candD2/{T}.log').read().strip().splitlines(); acc = [l for l in log if 'ACC' in l]; last = acc[-1] if acc else log[-1]
    rows = ['| probe (n, K) | r_peak | m 007 | m 013 | m 014 | m ' + cid + ' |', '|---|---|---|---|---|---|']
    for q in HELD:
        n, K = q.split(':'); rp = math.sqrt((2*int(K)+1)/3)
        def g(D): return f"{D['probes'][q]['m_lower_bound']:.2e}" if q in D['probes'] else '-'
        rows.append(f"| ({n}, {K}) | {rp:.0f} | {g(r3)} | {g(u3)} | {g(b3)} | {g(w3)} |")
    modes = '; '.join(f"n = {n}: {w3['best_m_by_mode'][str(n)]:.1e}" for n in range(1, 32, 2))
    sec = f"""{intro}
Snapshot {cid} (exact JSON sha256 {sha}; {ngen} generators; 421 exact rows; eleven EXACT-ZERO sectors). Last accepted step: {last[:150]}.
FLOAT (diag2, MID 32): G0 {d['G0']:.4f} (007 0.3767, 013 0.3722, 014 0.3726), G1 {d['G1']:.3f}, P2 {d['P2']:.1f}, rF {d['rF']:.3f}, H {d['H']:.4f}, sup|F| {d['supF']:.4f},
theta {bl['theta_inner_sup']:.4f}, kappa {bl['kappa_inner']:.4f} (margin {bl['margin_c_plus_1_minus_theta_minus_kappa_minus_2']:+.3f}), R_nec(2^-18) {d['point_tests']['2^-18']['R_nec']:.3e}; first-mode weak probes max over
k <= 4096: {w2['weak_distance_lower_bound_FLOAT']:.3e} at k = {w2['k_of_max']}.
{held_note}
""" + '\n'.join(rows) + f"\nBest m by mode (N4-160 family, FLOAT): {modes}. Best probe {w3['best_probe']} ({w3['best_m']:.2e})."
    summ = f"G0 {d['G0']:.4f}, kappa {bl['kappa_inner']:.4f}; (21, 522) probe m {w3['probes']['21:522']['m_lower_bound']:.2e} (007/013/014: 1.12e-3); best N4-160 probe {w3['best_probe']} {w3['best_m']:.2e}."
    return sec, summ
s16, sm16 = cand_section('quot013_legqs25_m9to15_cpu_m16', 'C1-N1-016-legqs25-quot013',
    "Run (c1-coord 05:33Z item 3): the exact quotient basis of 013 (1922 generators) plus 252 multi-scale legqs functions at scale R0 = 25 (Q = 4 vanishing far-field moments,\n12 radial functions per block) in the blocks j = 1, 2, 3, m = 9..15 (density sine modes 19 to 31), zero start; balanced objective of 007 plus 67 pairing rows\n(27 first-mode probes and the N4-160 angular probes with n <= 17 only), weight 1e12, MID 16, 12 CPU steps (about 175 s each). The probes n = 19..31 at\nK = (n-1)/2 + 512 (r 23 to 32) are HELD OUT (not rows of the objective): they decide whether the mid-field floor of 013/014 was a span limit.",
    "HELD-OUT probes at r 23 to 32 (FLOAT, weak_tests3 rule; 007, 013, 014 values for comparison):")
s15, sm15 = cand_section('quot013_pairQ_cpu_m16', 'C1-N1-015-pairQ-quot013',
    "Run: the exact quotient basis of 013 (1922 generators, no zero-potential directions) with the SAME 102 pairing rows as 014 (angular n >= 19 included), weight 1e12,\nMID 16, 12 CPU steps (about 167 s each): the redundancy of the basis is removed and nothing else changes, so a difference from 014 would attribute the\nimmobility of the r 23 to 32 probes to conditioning.",
    "Probes at r 23 to 32 (IN the objective for 014 and 015; FLOAT):")
src = src.replace('SEC016', s16 or 'PENDING (run in progress at publication).')
src = src.replace('SEC015', s15 or 'PENDING (run in progress at publication).').replace('SUMMARY015', sm15 or 'PENDING.')
s17, sm17 = cand_section('quot013_legqs50_m9to15_cpu_m16', 'C1-N1-017-legqs50-quot013',
    "Run: identical to 016 except the scale R0 = 50 of the 252 added legqs functions (blocks j = 1, 2, 3, m = 9..15), same start, same 67 rows, MID 16, 12 CPU steps:\na controlled comparison of the resolution scale.",
    "HELD-OUT probes at r 23 to 40 (FLOAT; 007, 013, 014 baselines; 016 values in section 1):")
if s17: src = src.replace('## 2. C1-N1-015-pairQ-quot013 (angular rows on the exact quotient basis)', '## 1b. C1-N1-017-legqs50-quot013 (scale comparison, R0 = 50)\n' + s17 + '\n\n## 2. C1-N1-015-pairQ-quot013 (angular rows on the exact quotient basis)')
src = src.replace('SUMMARY016', (sm16 or 'PENDING.') + (' Scale comparison 017 (R0 = 50): ' + sm17 if sm17 else ''))
sv = L('007_quot_gn_svd.json')
if sv:
    cb = sv['scaled_counts_below']
    secsvd = f"""Explicit weighted design matrix J Z on the admissible tangent of the exact quotient basis of 007 ({sv['rows']} rows x {sv['dimZ']} columns; constraint rank {sv['constraint_rank']};
balanced objective weights; MID 16 x 180), column-scaled, singular values by torch.linalg.svdvals (relative resolution about 1e-16): largest {sv['scaled_sv_max']:.3f},
smallest {sv['scaled_sv_quantiles']['0']:.2e}; counts below 1e-4 / 1e-6 / 1e-8 / 1e-10 / 1e-12 of the largest: {cb['0.0001']} / {cb['1e-06']} / {cb['1e-08']} / {cb['1e-10']} / {cb['1e-12']} (of {sv['dimZ']}).
Quantiles (scaled): 1 percent {sv['scaled_sv_quantiles']['0.01']:.2e}, 10 percent {sv['scaled_sv_quantiles']['0.1']:.2e}, median {sv['scaled_sv_quantiles']['0.5']:.2e}, 90 percent {sv['scaled_sv_quantiles']['0.9']:.2e}.
Gram metric (T4-229, theory_v03 R9(c)): the mesh L^2 Gram of the densities on the tangent has eigenvalues from {sv['gram_eig_min']:.2e} to {sv['gram_eig_max']:.2e}, i.e. it is numerically
singular in binary64, so the generalized singular values could not be formed; this means that the densities of the 1922 exactly independent potentials are
nearly dependent as functions on the mesh (the smallest directions of the normal-equation spectrum are combinations of the radial Legendre functions within the
high-m blocks, m = 17 to 19 of branch 1; the cause is OPEN, N4-211 (c)). Reading: the exact quotient removes the 1060 exact zero potentials but the physical problem remains strongly
ill-conditioned (about 40 percent of the tangent has no effect at the 1e-8 level); the Levenberg-Marquardt damping governs a large part of each step, and the
plateaus of the balanced objective cannot be called stationary points from this evidence (supersedes numerics_v06 section 5 and v07 section 4 wording). No
inverse bound of L follows (R9(d)). For the continuation: per-block orthogonalized densities and fewer radial functions at high m."""
else: secsvd = 'PENDING.'
src = src.replace('SECSVD', secsvd)
br = L('d2w_j7_n4_E2bal_mid180_weaktests2_bridge.json'); fw = L('007_far_weak.json'); br8 = L('d2w_j7_n4_X3bal_mid180_weaktests2_bridge.json')
if br and fw:
    Wb = {int(k): v for k, v in br['NORM-T-WEAK-v1_a0'].items()}; fwk = {r['k']: r for r in fw['rows']}
    rows = ['| k | r_peak | mesh I_k (no far correction) | exact-sector sum | ratio | m_k (mesh) | 008 mesh I_k / m_k |', '|---|---|---|---|---|---|---|']
    W8 = {int(k): v for k, v in br8['NORM-T-WEAK-v1_a0'].items()} if br8 else {}
    for k in sorted(Wb):
        f = fwk.get(k); rp = math.sqrt((2*k-0.7904)/4.7904)
        c8 = f"{W8[k]['I_k_signed_mesh']:+.2e} / {W8[k]['m_lower_bound']:.2e}" if k in W8 else '-'
        rows.append(f"| {k} | {rp:.0f} | {Wb[k]['I_k_signed_mesh']:+.3e} | {f['I_far']:.3e} | {abs(Wb[k]['I_k_signed_mesh'])/f['I_far']:.3f} | {Wb[k]['m_lower_bound']:.2e} | {c8} |" if f else f"| {k} | {rp:.0f} | {Wb[k]['I_k_signed_mesh']:+.3e} | - | - | {Wb[k]['m_lower_bound']:.2e} | {c8} |")
    secb = """Mesh pairings of 007 on 0.02 <= r <= 8356 (radial Gauss 32 x midpoint 180, far correction beyond 8356 omitted: relative size below 1e-4 for k <= 3.2e6) against the
exact-sector sums sum_e pi s_1(e) T_e(k) of far_weak.py (31 sectors to exponent -7):
""" + '\n'.join(rows) + """
Reading: at k = 1e6 (r about 650) the exact far-field expansion reproduces the full pairing to 0.2 percent, at k = 1e5 (r about 200) to 3 percent, at k = 3.2e6 the
mesh value is at its cancellation level (1e-12). The model was offered (numerics_v06 section 3) only where the sector series converges (r above about 300 to 600);
N4-209's comparison at K <= 1e4 (r <= 65) lies where the series diverges and the table entries were not estimates, so N4-209 and this validation are
consistent. Conclusions unchanged: the surviving sectors of 007 cancel to 97 to 99.7 percent in the sin theta pairing, 007 has no far-field floor of its first-mode
weak distance, and its maximum over all k is 1.73e-4 at k = 12288 (FLOAT). The 008 column shows the contrast for a candidate optimized without the rF term."""
else: secb = 'PENDING.'
src = src.replace('SECBRIDGE', secb)
src = src.replace('PUBTIME', now)
for ph, lane in (('COORDTIME', 'c1-coord'), ('N4TIME', 'c1-n4'), ('N3TIME', 'c1-n3')):
    t = subprocess.run(['grep', '-m1', '-o', r'^## 2026-10-29T[0-9:.+]*', f'RUN_ROOT/{lane}/NOTES_FOR_TEAM.md'], capture_output=True, text=True).stdout.strip().replace('## ', '')[:20]
    src = src.replace(ph, t or 'latest')
n4last = subprocess.run(['grep', '-o', r'^## N4-[0-9]*', 'audit/numerical_audit/VERDICT_LEDGER.md'], capture_output=True, text=True).stdout.strip().splitlines()
src = src.replace('N4LAST', n4last[-1].replace('## ', '') if n4last else 'latest')
tv4 = 'RUN_ROOT/shared/theory_requirements/theory_v04.md'
src = src.replace('THEORYV4LINE', ('theory_v04.md (c1-t1; sha256 ' + hashlib.sha256(open(tv4, 'rb').read()).hexdigest()[:16] + '...; ACK in RUN_STATUS)') if os.path.exists(tv4) else 'theory_v04 not yet published at this time')
open(root+'/numerics/NUMERICS_v08_stage.md', 'w').write(src)
print(now, len(src), 'left:', sorted(set(re.findall(r'\b(?:SEC[A-Z0-9]+|SUMMARY[0-9]+|STATUS|PENDING)\b', src))))

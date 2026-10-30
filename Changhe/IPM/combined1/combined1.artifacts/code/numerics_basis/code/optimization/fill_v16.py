# Assemble numerics_v16 from numerics/NUMERICS_v16_draft.md: candidate sections for 024, 025 (and 026 if present), per-step norms of 025, the seven-cell table, the 023 mode sweep, the summary table, status.
import json, os, re, datetime, hashlib, subprocess, math, sys, glob
root = 'RUN_ROOT/numerics_N1N2'; opt = root+'/numerics/optimization'
sys.path.insert(0, opt)
src = open(root+'/numerics/NUMERICS_v16_draft.md').read()
def L(p): return json.load(open(f'{opt}/candD2/{p}')) if os.path.exists(f'{opt}/candD2/{p}') else None
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
REF = {'016': 'quot013_legqs25_m9to15_cpu_m16', '020': 'quot013_legqs25p50_m9to15_cpu_m16', '021': 'legqs25p50_heldin14_gpu_m16', '022': 'legqs25_m16to23_gpu_m16', '023': 'legqs25p100_m9to15_gpu_m16', '026': 'legqs25_m16to23_heldin1e16_gpu_m16', '027': 'legqs25_m16to23_cont60_gpu_m16'}
W3 = {k: (L(f'{t}_weaktests3.json') or {}).get('probes', {}) for k, t in REF.items()}
REG = [f'{n}:{K}' for n in (19, 23, 25, 29, 31) for K in (600, 900, 1200, 1800, 2400)]; K512 = ['19:521', '21:522', '23:523', '25:524', '27:525', '29:526', '31:527']; K128 = ['19:137', '21:138', '23:139', '25:140', '27:141', '29:142', '31:143']
SMALL = ['19:9', '21:10', '23:11', '25:12', '27:13', '29:14', '31:15', '19:17', '23:19', '27:21', '29:22']
def g(D, q): return f"{D[q]['m_lower_bound']:.2e}" if q in D else '-'
def last_acc(T):
    try: log = open(f'{opt}/candD2/{T}.log').read().strip().splitlines(); acc = [l for l in log if 'ACC' in l]; return acc[-1] if acc else log[-1]
    except Exception: return 'n/a'
def final_line(T):
    try: return [l for l in open(f'{opt}/logs/{T}.out').read().splitlines() if l.startswith('FINAL (')][-1]
    except Exception: return 'n/a'
def cand(T, cid, intro, heldin=False, cmp=('016', '022', '023')):
    w3 = L(f'{T}_weaktests3.json'); d = L(f'{T}_diag2.json'); w2 = L(f'{T}_weaktests2.json')
    if not w3: return None
    P = w3['probes']; sha = hashlib.sha256(open(f'{opt}/candD2/{T}_exact.json', 'rb').read()).hexdigest(); ex = json.load(open(f'{opt}/candD2/{T}_exact.json'))
    out = [intro, f"Exact JSON sha256 {sha}; {len(ex['generators'])} generators; 421 exact rows; ten nonautomatic EXACT-ZERO sectors. Last accepted step: {last_acc(T)[:150]}.", f"Optimizer report ({'MID 32' if 'm32' in T else 'MID 16'}): {final_line(T).split('): ', 1)[-1]}"]
    if d:
        bl = d['BL2']; out.append(f"FLOAT (diag2, MID 32): G0 {d['G0']:.4f} (016 0.3089, 022 0.2816, 023 0.3228), G1 {d['G1']:.3f}, P2 {d['P2']:.1f}, rF {d['rF']:.3f}, H {d['H']:.4f}, sup|F| {d['supF']:.4f}, theta_inner {bl['theta_inner_sup']:.4f}, kappa_inner {bl['kappa_inner']:.4f} ((B-L2) margin {bl['margin_c_plus_1_minus_theta_minus_kappa_minus_2']:+.4f}).")
    else: out.append('diag2 (MID 32 norms, (B-L2) screening): PENDING.')
    if w2: out.append(f"First-mode weak probes (27 sampled k <= 4096, objective rows): largest sampled value {w2['weak_distance_lower_bound_FLOAT']:.2e} at k = {w2.get('k_of_max', '?')} (a sampled maximum, not a bound; 016 1.50e-4 at k = 2048).")
    hdr = '| probe (n, K) | r_peak | ' + ' | '.join(cmp) + f' | {cid} |'; rows = [hdr, '|' + '---|'*(len(cmp)+3)]
    def R(q, tag):
        n, K = q.split(':'); rp = math.sqrt((2*int(K)+1)/3); return f"| ({n}, {K}) [{tag}] | {rp:.0f} | " + ' | '.join(g(W3[k], q) for k in cmp) + f" | {g(P, q)} |"
    for q in REG: rows.append(R(q, 'registered, HELD OUT'))
    for q in K512: rows.append(R(q, 'N4-160 K0 = 512, ' + ('HELD IN (objective row)' if heldin else 'HELD OUT')))
    for q in K128: rows.append(R(q, 'N4-160 K0 = 128, ' + ('HELD IN (objective row)' if heldin else 'HELD OUT')))
    for q in SMALL: rows.append(R(q, 'N4-160 small K0, HELD OUT'))
    out.append('\n'.join(rows))
    regs = [(q, P[q]['m_lower_bound']) for q in REG if q in P]
    if regs:
        qb, vb = max(regs, key=lambda x: x[1]); out.append(f"Largest held-out value over the 25 registered probes: ({qb.replace(':', ', ')}) {vb:.2e}; {sum(v > 4.5717e-4 for _, v in regs)} of 25 above the graded ceiling 4.5717e-4 (016: (19, 1800) 9.02e-4, 7 of 25; 022: 8.30e-4, 7; 023: 1.62e-3, 10).")
    return '\n'.join(out)
S = {}
S['SEC024'] = cand('quot013_legqs25_m9to15_gpu_m32', '024', "Run: the same start (exact quotient of 013 + 252 legqs R0 = 25 in m = 9..15, zero start; 2174 generators), the same 67 rows (weight 1e12) and the same 12 GN steps as 016, but the optimization objective evaluated on the MID 32 radial rule (016: MID 16) and on the GPU (016: CPU; N4-342 notes the backend change). HELD-OUT: the 25 registered probes and the N4-160 probes n = 19..31 at K0 in {0,8,32,128,512}. Snapshot C1-N1-024-rulem32-legqs25 (11:31:32Z).") or 'PENDING.'
S['SEC025'] = cand('combined_s25s50s100_m16to23_heldin14_gpu_m16', '025', "Run: start 016 + legqs R0 = 50 and R0 = 100 in m = 9..15 (252 + 252) + legqs R0 = 25 in the existing higher blocks m = 16..23 (240): 2918 generators (N4-274-type dimension claim not made); 81 rows = the 67 rows of 016 at weight 1e12 + the 14 mid-field rows n = 19..31 at K0 = 128 and 512 at weight 1e16 (sensitivity run for the 021 question); 60 GN steps, MID 16, GPU 7 (50 s per step). HELD-OUT (never rows): the 25 registered probes and the N4-160 probes n = 19..31 at K0 in {0,8,32}.", heldin=True) or 'PENDING.'
s26 = cand('legqs25_m16to23_heldin1e16_gpu_m16', '026', "Run: the 022 state (2414 generators; no new functions) continued 60 GN steps with the 81 rows of 025 (the 14 mid-field rows at weight 1e16); HELD-OUT as 025 (file heldout/HELDOUT_026.md, sha256 2016d960c982aeffa2b1bef5aaece9b7394e97139d9688b5f6abec3274606d15, written before the 11:31Z launch). Separates the row effect from the scale-100 basis effect of 025.", heldin=True)
s27 = cand('legqs25_m16to23_cont60_gpu_m16', '027', "Run: the 022 state (2414 generators) continued 60 GN steps with the plain 67 rows of 016 (weight 1e12; no held-in rows), MID 16, GPU 7: the control for 026 (same start, steps and rule; only the 14 rows at 1e16 differ). HELD-OUT: the 25 registered probes and the N4-160 probes n = 19..31 at K0 in {0,8,32,128,512}.", cmp=('016', '022', '026'))
src = src.replace('SEC027', s27 or 'PENDING (027 tests running at publication).')
s28 = cand('legqs25_nin24_m9to15_gpu_m16', '028', "Run: the 022 state + 252 legqs R0 = 25 functions n = 12..23 in j = 1..3, m = 9..15 (2666 generators), plain 67 rows, 60 GN steps, MID 16, GPU 7. HELD-OUT: the 25 registered probes and the N4-160 probes n = 19..31 at K0 in {0,8,32,128,512}. Compared per probe with 022 and 027 (same start; 027 has the same steps and no new functions).", cmp=('016', '022', '027'))
src = src.replace('SEC028', s28 or 'PENDING (028 tests running at publication).')
def perprobe(files, head):
    out=[head]
    for fn in files:
        L=open(f'{root}/numerics/{fn}').read().strip().splitlines()
        out.append('- ' + L[0] + ' Counts and factors:' + L[1].strip().rstrip('.') + '; ' + L[2].strip() + '.')
    return '\n'.join(out)
src = src.replace('PERPROBE027', perprobe(['perprobe_027_vs_022.txt', 'perprobe_027_vs_026.txt'], 'Per-probe statements (FLOAT, MID 32; the 25 registered probes, value old -> value new (factor)); 027 against 022 reproduces the N4-375 reading (extrema 0.8259 at (19,600) and 1.3432 at (25,900); 16 decreases, 9 increases; all ten K >= 1800 probes decrease). No uniform statement across the probes is made.'))
src = src.replace('PERPROBE028', perprobe(['perprobe_028_vs_022.txt', 'perprobe_028_vs_027.txt', 'perprobe_028_vs_016.txt'], 'Per-probe statements (FLOAT, MID 32; the 25 registered probes, value old -> value new (factor)). H18 check of this lane (c1-coord 14:29Z part 8): against the matched control 027, 028 moves eleven of the fifteen K <= 1200 probes by more than the 027/022 continuation band (0.826 to 1.343) in both directions and none of the ten K >= 1800 probes except (31,1800) (0.63); the earlier reading that the registered probes "did not respond to any basis change beyond 016\'s scale-25 functions" is therefore amended in NUMERICS_FINAL section 9 to the per-probe statement. No uniform statement across the probes is made.'))
src = src.replace('V16CHANGES', open(root+'/numerics/v16_changes.md').read().strip() if os.path.exists(root+'/numerics/v16_changes.md') else 'V16CHANGES')
src = src.replace('V15CHANGES', open(root+'/numerics/v15_changes.md').read().strip() if os.path.exists(root+'/numerics/v15_changes.md') else 'V15CHANGES')
src = src.replace('STATUS026', open(root+'/numerics/status026.txt').read().strip() if os.path.exists(root+'/numerics/status026.txt') else 'Its replay status at publication: see c1-coord NOTES.')
if s26: src = src.replace('## 2c. C1-N1-027', '## 2b. C1-N1-026 (022 continued with the 14 mid-field rows at weight 1e16; 60 steps)\n' + s26 + '\n\n## 2c. C1-N1-027')
for k, v in S.items(): src = src.replace(k, v)
# per-step norms of 025 (and 026)
def stepnorms(T):
    try: lines = [l for l in open(f'{opt}/candD2/{T}.log').read().splitlines() if ' ACC ' in l and 'dRho2' in l]
    except Exception: return 'n/a'
    vals = [(int(l.split()[1]), float(re.search(r'dRho2 ([0-9.e+-]+)', l).group(1)), float(re.search(r'dCoef ([0-9.e+-]+)', l).group(1))) for l in lines]
    if not vals: return 'n/a'
    tot = sum(v[1] for v in vals); return f"{len(vals)} accepted steps; density L2 step norm ||rho(a_new) - rho(a)||_2 on the mesh (FLOAT): first accepted step {vals[0][1]:.2e}, median {sorted(v[1] for v in vals)[len(vals)//2]:.2e}, last {vals[-1][1]:.2e}, sum over accepted steps {tot:.3e} (an upper bound of the FLOAT mesh norm of the total density change by the triangle inequality; no certified bound on the density change exists: a certificate would need an exact endpoint computation, and this mesh-step sum is not one); coefficient step norms {min(v[2] for v in vals):.1e} to {max(v[2] for v in vals):.1e}. Every reported residual of this lane is either the optimizer's evaluated objective parts (MID 16) or the MID 32 diag2 re-evaluation; linear-model values ||F + J delta||_2 appear only in NUMERICS_FINAL section 4b and are labelled so."
src = src.replace('STEPNORMS', '025: ' + stepnorms('combined_s25s50s100_m16to23_heldin14_gpu_m16') + (' 026: ' + stepnorms('legqs25_m16to23_heldin1e16_gpu_m16') if s26 else '') + ' 024: ' + stepnorms('quot013_legqs25_m9to15_gpu_m32'))
# seven-cell table
C=[('C1-N1-008','d2w_j7_n4_X3bal_mid180'),('C1-N1-009','d2w_j7_n4_X3balK_mid180'),('C1-N1-010','d2w_j7_n4_X3bal_legqs_mid180'),('C1-N1-011','d2w_j7_n4_E2bal_legqs_cpu_m8'),('C1-N1-012','d2w_j7_n4_E2balK_cpu_m8'),('C1-N1-013','d2w_j7_n4_E2bal_pairU_cpu_m16'),('C1-N1-014','d2w_j7_n4_E2bal_pairB_cpu_m16'),('C1-N1-015','quot013_pairQ_cpu_m16'),('C1-N1-016','quot013_legqs25_m9to15_cpu_m16'),('C1-N1-017','quot013_legqs50_m9to15_cpu_m16'),('C1-N1-018','quot013_legqs25_cont12_cpu_m16'),('C1-N1-019','quot013_legqs50_cont12_cpu_m16'),('C1-N1-020','quot013_legqs25p50_m9to15_cpu_m16'),('C1-N1-021','legqs25p50_heldin14_gpu_m16'),('C1-N1-022','legqs25_m16to23_gpu_m16'),('C1-N1-023','legqs25p100_m9to15_gpu_m16'),('C1-N1-024','quot013_legqs25_m9to15_gpu_m32'),('C1-N1-025','combined_s25s50s100_m16to23_heldin14_gpu_m16')]
rows=['| candidate | two-mode value at the right end of the seven cells (thresholds 15.88162, 8.716729, 4.799949, 2.565236, 1.263642, 0.5028299, 0.06411577) | ratios value/threshold | min ratio | every cell excluded if the two-mode LB were certified |','|---|---|---|---|---|']
for cid,t in C:
    d=L(f'{t}_na_cells.json')
    if not d: rows.append(f'| {cid} | PENDING | | | |'); continue
    c=d['cells']; rows.append(f"| {cid} | "+', '.join(f"{x['N_h_modes_1_3_FLOAT']:.2f}" for x in c)+" | "+', '.join(f"{x['ratio']:.2f}" for x in c)+f" | {min(x['ratio'] for x in c):.2f} | {'yes' if all(x['excluded_if_LB_certified'] for x in c) else 'NO'} |")
src = src.replace('NACELLS', '\n'.join(rows)+"\nFLOAT proxy (na_modes_cells.py, MID 32): projected weighted-Laplacian norm of the angular modes 1 and 3 of F at the right end of each cell (a lower bound of the full N_a when certified) against the theory_v03 section 5 thresholds at the left end. A ratio above 1 at every cell means FW-T-DYADIC-Y-v1 would be excluded for that candidate if the two-mode lower bounds were certified (c1-n3 did 008 exactly; c1-n4/T4-248 as well). FLOAT; no verdict; 009's first cell is not excluded by two modes.")
a=L('legqs25p100_m9to15_gpu_m16_weaktests3c_n47.json'); b=L('quot013_legqs25_m9to15_cpu_m16_weaktests3c_n47.json'); c2=L('legqs25_m16to23_gpu_m16_weaktests3c_n47.json')
src = src.replace('N47_023', 'Best FLOAT value per odd mode n = 33 .. 47 (weak_tests3, IPM_NMAX=47; never rows): 016: ' + ', '.join(f"{b['best_m_by_mode'][str(n)]:.1e}" for n in range(33,48,2)) + '; 022: ' + ', '.join(f"{c2['best_m_by_mode'][str(n)]:.1e}" for n in range(33,48,2)) + '; 023: ' + ', '.join(f"{a['best_m_by_mode'][str(n)]:.1e}" for n in range(33,48,2)) + f". Largest held-out value over n <= 47: 023 (19,1800) {a['best_m']:.2e}; 022 {c2['best_m']:.2e}; 016 {b['best_m']:.2e}. Smaller or larger values at the tested probes; no band-mass bound follows.")
src = src.replace('PUBTIME', now)
for ph, lane in (('COORDTIME', 'c1-coord'), ('N4TIME', 'c1-n4'), ('N3TIME', 'c1-n3')):
    hs = subprocess.run(['grep', '-o', r'^## 2026-10-29T[0-9:.+]*', f'RUN_ROOT/{lane}/NOTES_FOR_TEAM.md'], capture_output=True, text=True).stdout.split()
    hs = [h.replace('##', '') for h in hs if h != '##']; t = (max(hs) if hs else '')[:16]  # latest header whatever the file order
    src = src.replace(ph, t or 'latest')
tv7 = 'RUN_ROOT/shared/theory_requirements/theory_v07.md'
src = src.replace('THEORYV7LINE', ('theory_v07.md (c1-t1, 11:20Z; sha256 ' + hashlib.sha256(open(tv7, 'rb').read()).hexdigest()[:16] + '...; ACK 11:52Z in RUN_STATUS)') if os.path.exists(tv7) else 'theory_v07 not yet published at this time')
if len(sys.argv) > 1: src = src.replace('SECTABLE', open(sys.argv[1]).read())
if len(sys.argv) > 2: src = src.replace('STATUS_SECTION', open(sys.argv[2]).read())
if len(sys.argv) > 3: src = src.replace('NEWIDS', sys.argv[3])
open(root+'/numerics/NUMERICS_v16_stage.md', 'w').write(src)
print(now, len(src), 'left:', sorted(set(re.findall(r'\b(?:SEC[A-Z0-9]+|STATUS|NEWIDS|STEPNORMS|NACELLS|N47_023|SECTABLE)\b', src))))

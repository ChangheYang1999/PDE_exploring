# Assemble numerics_v11 from numerics/NUMERICS_v11_draft.md and the JSON records of 021, 022 (s12 and final), 023 (s12 and final). Missing records -> PENDING text.
import json, os, re, datetime, hashlib, subprocess, math, sys
root = 'RUN_ROOT/numerics_N1N2'; opt = root+'/numerics/optimization'
src = open(root+'/numerics/NUMERICS_v11_draft.md').read()
def L(p): return json.load(open(f'{opt}/candD2/{p}')) if os.path.exists(f'{opt}/candD2/{p}') else None
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
REF = {'013': 'd2w_j7_n4_E2bal_pairU_cpu_m16', '016': 'quot013_legqs25_m9to15_cpu_m16', '017': 'quot013_legqs50_m9to15_cpu_m16', '020': 'quot013_legqs25p50_m9to15_cpu_m16'}
W3 = {k: (L(f'{t}_weaktests3.json') or {}).get('probes', {}) for k, t in REF.items()}
REG = [f'{n}:{K}' for n in (19, 23, 25, 29, 31) for K in (600, 900, 1200, 1800, 2400)]
K512 = ['19:521', '21:522', '23:523', '25:524', '27:525', '29:526', '31:527']
SMALL = ['19:9', '21:10', '23:11', '25:12', '27:13', '29:14', '31:15', '19:17', '23:19', '27:21', '29:22']
def g(D, q): return f"{D[q]['m_lower_bound']:.2e}" if q in D else '-'
def last_acc(T):
    try: log = open(f'{opt}/candD2/{T}.log').read().strip().splitlines(); acc = [l for l in log if 'ACC' in l]; return acc[-1] if acc else log[-1]
    except Exception: return 'n/a'
def final_line(T):
    try: return [l for l in open(f'{opt}/logs/{T}.out').read().splitlines() if l.startswith('FINAL (')][-1]
    except Exception: return 'n/a'
def cand(T, cid, intro, heldin=False):
    w3 = L(f'{T}_weaktests3.json'); d = L(f'{T}_diag2.json'); w2 = L(f'{T}_weaktests2.json')
    if not w3: return None
    P = w3['probes']; sha = hashlib.sha256(open(f'{opt}/candD2/{T}_exact.json', 'rb').read()).hexdigest(); ex = json.load(open(f'{opt}/candD2/{T}_exact.json'))
    out = [intro, f"Exact JSON sha256 {sha}; {len(ex['generators'])} generators; 421 exact rows; ten nonautomatic EXACT-ZERO sectors. Last accepted step: {last_acc(T)[:140]}.", f"Optimizer report (MID 16): {final_line(T)[60:]}"]
    if d:
        bl = d['BL2']; out.append(f"FLOAT (diag2, MID 32): G0 {d['G0']:.4f} (016 0.3089, 017 0.3209, 020 0.3201), G1 {d['G1']:.3f}, P2 {d['P2']:.1f}, rF {d['rF']:.3f}, H {d['H']:.4f}, sup|F| {d['supF']:.4f}, theta_inner {bl['theta_inner_sup']:.4f}, kappa_inner {bl['kappa_inner']:.4f} ((B-L2) margin {bl['margin_c_plus_1_minus_theta_minus_kappa_minus_2']:+.4f}).")
    else: out.append('diag2 (MID 32 norms, (B-L2) screening): PENDING.')
    if w2: out.append(f"First-mode weak probe (weak_tests2, 27 sampled k <= 4096): largest sampled value {w2['weak_distance_lower_bound_FLOAT']:.2e} at k = {w2.get('k_of_max', '?')}.")
    rows = ['| probe (n, K) | r_peak | 013 | 016 | 017 | 020 | ' + cid + ' |', '|---|---|---|---|---|---|---|']
    for q in REG:
        n, K = q.split(':'); rp = math.sqrt((2*int(K)+1)/3)
        rows.append(f"| ({n}, {K}) [registered, HELD OUT] | {rp:.0f} | {g(W3['013'], q)} | {g(W3['016'], q)} | {g(W3['017'], q)} | {g(W3['020'], q)} | {g(P, q)} |")
    for q in K512:
        n, K = q.split(':'); rp = math.sqrt((2*int(K)+1)/3); tag = 'HELD IN (objective row)' if heldin else 'HELD OUT'
        rows.append(f"| ({n}, {K}) [N4-160 K0 = 512, {tag}] | {rp:.0f} | {g(W3['013'], q)} | {g(W3['016'], q)} | {g(W3['017'], q)} | {g(W3['020'], q)} | {g(P, q)} |")
    for q in SMALL:
        n, K = q.split(':'); rp = math.sqrt((2*int(K)+1)/3)
        rows.append(f"| ({n}, {K}) [N4-160 small K0, HELD OUT] | {rp:.0f} | {g(W3['013'], q)} | {g(W3['016'], q)} | {g(W3['017'], q)} | {g(W3['020'], q)} | {g(P, q)} |")
    out.append('\n'.join(rows))
    reg_vals = [(q, P[q]['m_lower_bound']) for q in REG if q in P]; 
    if reg_vals:
        qb, vb = max(reg_vals, key=lambda x: x[1]); out.append(f"Largest held-out value over the 25 registered probes: ({qb.replace(':', ', ')}) {vb:.2e} (016: (19, 1800) 9.02e-4; 017: 1.03e-3; 020: 1.14e-3).")
    modes = '; '.join(f"n = {n}: {w3['best_m_by_mode'][str(n)]:.1e}" for n in range(1, 32, 2) if str(n) in w3['best_m_by_mode'])
    out.append(f"Best m by mode over the N4-160 family (FLOAT; rows and held-out mixed, see the tags above): {modes}.")
    return '\n'.join(out)
S = {}
S['SEC021'] = cand('legqs25p50_heldin14_gpu_m16', '021', "Run: start 020 (2426 generators, scales 25 and 50); balanced E_2 objective + 1e12 I^2 over 81 rows = 67 rows of 016..020 + 14 HELD-IN mid-field rows (N4-160 probes n = 19..31 at K0 = 128 and 512); HELD-OUT: the 25 registered probes and the N4-160 probes n >= 19 at K0 in {0, 8, 32}; 40 GN steps, MID 16, GPU 7 (33 s per step with three jobs on the GPU).", heldin=True) or 'PENDING (run or diagnostics in progress at publication).'
s12 = cand('legqs25_m16to23_gpu_m16_s12', '022 (12 steps)', "Phase 1 (controlled comparison with 016 at equal step count and rule): start 016 + 240 legqs R0 = 25 functions in the existing higher blocks j = 1 (m = 16..19), j = 2, 3 (m = 16..23) (2414 generators; density modes 31 to 47); same 67 rows and HELD-OUT set as 016; 12 GN steps, MID 16, GPU.")
s40 = cand('legqs25_m16to23_gpu_m16', '022 (40 steps)', "Phase 2: 28 more steps from the phase 1 state (same rows, same held-out set).")
S['SEC022'] = '\n\n'.join(x for x in (s12, s40) if x) or 'PENDING.'
s12 = cand('legqs25p100_m9to15_gpu_m16_s12', '023 (12 steps)', "Phase 1 (controlled comparison with 016 and 020 at equal step count and rule): start 016 + 252 legqs R0 = 100 functions in j = 1..3, m = 9..15 (scales 25 and 100; 2426 generators); same 67 rows and HELD-OUT set as 016; 12 GN steps, MID 16, GPU.")
s40 = cand('legqs25p100_m9to15_gpu_m16', '023 (40 steps)', "Phase 2: 28 more steps from the phase 1 state (same rows, same held-out set).")
S['SEC023'] = '\n\n'.join(x for x in (s12, s40) if x) or 'PENDING.'
for k, v in S.items(): src = src.replace(k, v)
src = src.replace('PUBTIME', now)
for ph, lane in (('COORDTIME', 'c1-coord'), ('N4TIME', 'c1-n4'), ('N3TIME', 'c1-n3')):
    t = subprocess.run(['grep', '-m1', '-o', r'^## 2026-10-29T[0-9:.+]*', f'RUN_ROOT/{lane}/NOTES_FOR_TEAM.md'], capture_output=True, text=True).stdout.strip().replace('## ', '')[:20]
    src = src.replace(ph, t or 'latest')
tv6 = 'RUN_ROOT/shared/theory_requirements/theory_v06.md'
src = src.replace('THEORYV6LINE', ('theory_v06.md (c1-t1; sha256 ' + hashlib.sha256(open(tv6, 'rb').read()).hexdigest()[:16] + '...; ACK in RUN_STATUS)') if os.path.exists(tv6) else 'theory_v06 not yet published at this time')
if len(sys.argv) > 1: src = src.replace('SECTABLE', open(sys.argv[1]).read()) 
if len(sys.argv) > 2: src = src.replace('STATUS', open(sys.argv[2]).read())
if len(sys.argv) > 3: src = src.replace('NEWIDS', sys.argv[3])
open(root+'/numerics/NUMERICS_v11_stage.md', 'w').write(src)
print(now, len(src), 'left:', sorted(set(re.findall(r'\b(?:SEC[A-Z0-9]+|STATUS|NEWIDS|PENDING)\b', src))))

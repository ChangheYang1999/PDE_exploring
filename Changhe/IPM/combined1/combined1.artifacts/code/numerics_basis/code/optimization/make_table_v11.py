# Summary table for numerics_v11 section 4 / NUMERICS_FINAL: per candidate G0, G1, P2, rF, H, sup|F|, kappa, largest registered held-out probe, (21,522), LOSS. FLOAT (MID 32 diag2; weak_tests3).
import json, os, sys
opt = 'RUN_ROOT/numerics_N1N2/numerics/optimization'
C = [('C1-N1-007', 'd2w_j7_n4_E2bal_mid180'), ('C1-N1-013', 'd2w_j7_n4_E2bal_pairU_cpu_m16'), ('C1-N1-016', 'quot013_legqs25_m9to15_cpu_m16'), ('C1-N1-017', 'quot013_legqs50_m9to15_cpu_m16'),
     ('C1-N1-018', 'quot013_legqs25_cont12_cpu_m16'), ('C1-N1-019', 'quot013_legqs50_cont12_cpu_m16'), ('C1-N1-020', 'quot013_legqs25p50_m9to15_cpu_m16'),
     ('C1-N1-021', 'legqs25p50_heldin14_gpu_m16'), ('022 (12 st.)', 'legqs25_m16to23_gpu_m16_s12'), ('C1-N1-022', 'legqs25_m16to23_gpu_m16'), ('023 (12 st.)', 'legqs25p100_m9to15_gpu_m16_s12'), ('C1-N1-023', 'legqs25p100_m9to15_gpu_m16'),
     ('C1-N1-024', 'quot013_legqs25_m9to15_gpu_m32'), ('C1-N1-025', 'combined_s25s50s100_m16to23_heldin14_gpu_m16'), ('C1-N1-026', 'legqs25_m16to23_heldin1e16_gpu_m16'), ('C1-N1-027', 'legqs25_m16to23_cont60_gpu_m16'), ('C1-N1-028', 'legqs25_nin24_m9to15_gpu_m16')]
REG = [f'{n}:{K}' for n in (19, 23, 25, 29, 31) for K in (600, 900, 1200, 1800, 2400)]
def L(p): return json.load(open(f'{opt}/candD2/{p}')) if os.path.exists(f'{opt}/candD2/{p}') else None
def loss(T):
    try: acc = [l for l in open(f'{opt}/candD2/{T}.log').read().splitlines() if 'ACC' in l]; return acc[-1].split()[5] if acc else '-'
    except Exception: return '-'
rows = ['| candidate | LOSS (MID 16) | G0 | G1 | P2 | rF | H | sup|F| | kappa_inner | largest registered held-out (n,K): m | (21,522) | (19,1800) | (23,2400) |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
for cid, T in C:
    d = L(f'{T}_diag2.json'); w = L(f'{T}_weaktests3.json')
    if not (d or w): continue
    P = (w or {}).get('probes', {})
    reg = [(q, P[q]['m_lower_bound']) for q in REG if q in P]; big = max(reg, key=lambda x: x[1]) if reg else None
    def g(q): return f"{P[q]['m_lower_bound']:.2e}" if q in P else '-'
    dd = (lambda k, f='%.4f': (f % d[k]) if d and d.get(k) is not None else '-')
    kap = ('%.4f' % d['BL2']['kappa_inner']) if d else '-'
    rows.append(f"| {cid} | {loss(T)} | {dd('G0')} | {dd('G1','%.3f')} | {dd('P2','%.1f')} | {dd('rF','%.3f')} | {dd('H')} | {dd('supF')} | {kap} | {('(%s): %.2e' % (big[0].replace(':', ', '), big[1])) if big else '-'} | {g('21:522')} | {g('19:1800')} | {g('23:2400')} |")
out = '\n'.join(rows) + '\nAll FLOAT (diag2 MID 32; weak_tests3 MID 32; LOSS = last accepted objective on the MID 16 rule, comparable only within the same row set: 016 to 020, 022, 023 use 67 rows; 021 and 025 use 81 rows, so their LOSS includes 14 more penalty rows). Certified floors (CONFIRMED): 016 > 0.0014703, 017 > 0.0016718, 018 > 0.0016558, 019 > 0.0016618, 020 > 0.0018553, 021 > 0.0018646 at (19,1800); printed digits rounded down from the certified roots.'
open(sys.argv[1] if len(sys.argv) > 1 else f'{opt}/candD2/table_v11.md', 'w').write(out); print(out)

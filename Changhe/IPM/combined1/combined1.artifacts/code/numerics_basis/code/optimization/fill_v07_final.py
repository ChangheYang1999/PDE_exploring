# Final placeholders of numerics_v07 (STATUS, QUOT015, BRIDGEREADING, PENDING markers for the bridge) -> numerics/NUMERICS_v07_published.md
import os, re, json, datetime, math
root = 'RUN_ROOT/numerics_N1N2'; opt = root+'/numerics/optimization'
s = open(root+'/numerics/NUMERICS_v07_stage.md').read()
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
have015 = os.path.exists(f'{opt}/candD2/quot013_pairQ_cpu_m16_exact.json')
s = s.replace('QUOT015', 'C1-N1-015 (pairing rows on the exact quotient basis of 013; ' + ('snapshot included' if have015 else 'run in progress at publication, snapshot in v08 or in NUMERICS_FINAL') + ')')
s = s.replace('BRIDGEREADING', "at k = 1e6 and 3.2e6 the mesh pairing (full F on 0.02 <= r <= 8356 plus the exact-sector far correction beyond 8356) and the pure exact-sector sum are compared directly; agreement would confirm that the far-field expansion of 007 describes F from r about 650 on, disagreement measures the mid-field remainder that the sectors do not capture.")
status = f"""Published {now}. Best candidate unchanged: C1-N1-007 (certified: G0 0.37669, G1, P2, Q3, (B-L2); distance 0.004769 in mode 7; forcing gap 3.6e6 in sharpw with
c1-n3's complete components). New snapshots: C1-N1-013-pairU-from007 (04:39:56Z) and C1-N1-014-pairB-from007 (05:22:50Z), both design experiments (rows
in the objective; theory_v03 R6(c)) and not certification targets. What they establish (FLOAT): the weak pairings of every tested family (first mode k <= 128,
angular modes 3 to 15 at K <= 131) are removable by one to three orders of magnitude at r <= 10 at no cost in G0, kappa or sup|F|, and every probe localized
at r >= 20 (first mode k >= 384, N4-160 probes at K about 520 for modes 19 to 31, m about 1.1e-3) is unchanged even when it is a row of the objective:
the fixed-c distance of the 007 family has a mid-field floor of order 1e-3 set by the reachability of the inner basis (about r = 10 to 20), consistent with
the Newton-step diagnostic (the span's L^2 floor 0.34, ||h0||_2 about 1.5e-2) and with the dyadic profiles. Running at publication: the first optimization on
the exact quotient basis (1922 generators, 013 start, 102 pairing rows; core 52) -> C1-N1-015, to test whether the redundancy affected the plateaus (N4-178
leaves this OPEN); its result goes to NUMERICS_FINAL.md (and v08 if time permits). Requests to batch T: none new; theory_v04 will be ACKed within the
hour. Requests to c1-n4: held-out exact probes (21, 522), (23, 523), (25, 524) and the frozen T4-182/T4-185 vectors on 013 and 014 (expected about 1e-3 for
the first group); the 009 first cell [0, 1/4] needs modes beyond 1 and 3 or the full N_a (FLOAT ratio 0.889 with modes 1 and 3)."""
s = s.replace('STATUS', status)
s = s.replace('# numerics_v07 (batch N publication; author c1-n1) -- DRAFT', '# numerics_v07 (batch N publication; author c1-n1)')
s = re.sub(r'- version: numerics_v07; UTC time: [0-9T:Z-]+;', f'- version: numerics_v07; UTC time: {now};', s)
open(root+'/numerics/NUMERICS_v07_published.md', 'w').write(s)
print(now, len(s), 'PENDING markers left:', s.count('PENDING'))

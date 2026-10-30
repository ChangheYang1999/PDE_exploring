# Assemble numerics_v06 from the draft and the JSON records (tables from v06_tables.py); placeholders left for 013/014 are filled by fill_v06_013.py
import subprocess, datetime, hashlib, json, os, re, sys
root = 'RUN_ROOT/numerics_N1N2'; opt = root+'/numerics/optimization'
PY = 'python3'
src = open(root+'/numerics/NUMERICS_v06_draft.md').read()
tabs = subprocess.run([PY, '-B', opt+'/v06_tables.py'], capture_output=True, text=True, cwd=opt).stdout
blocks = [b for b in tabs.split('\n\n') if b.strip()]
weak_main = blocks[0]; profile007 = blocks[1]; far = blocks[2] if len(blocks) > 2 else 'FAR_WEAK PENDING'
src = src.replace('WEAKTABLE', weak_main+"\n\nReading: the maximum over k is attained at k of order 1e4 (r of order 50 to 100) for 007 and 008 and at small k for 009, 010, 011, 012 (large\nnear-field pairings); 007's maximum 1.733e-4 is 3.9 times its certified k = 128 value (N4-091) and 46 times the largest scalar budget (3.793e-6), but below the\ncertified first-mode optimized probe 3.1474e-4 (T4-182) and far below the mode-7 probe 0.004769 (T4-185), which remains the binding necessary distance.\n\n"+profile007)
src = src.replace('HIGHK', "Included in the table above (columns k = 8192 to 65536; files candD2/<tag>_weaktests2_highk.json). The mesh (0.02 <= r <= 8356) resolves these probes\n(r_peak <= 185); a bridge list k = 1e5 to 1e7 (r_peak 200 to 2600) for 007 is BRIDGE_PENDING.")
src = src.replace('FARWEAK', far+"""
Reading. (i) The sector amplitudes grow by about a factor 10 per unit of exponent, so the exact far-field expansion of the 007 residual converges only
beyond r of order 300 to 600 (terms at r = 100 increase; at r = 650 they decrease by 0.2 to 0.5 per step). (ii) For k >= 1e6 (r_peak >= 650) the near-field
bound with R = 300 is below 3e-6 and the exact-sector pairing is 1.3e-10 (k = 1e6) to 1.5e-12 (k = 3.2e6): the 31 sectors cancel to 97 to 99.7 percent in
the sin theta pairing (the leading (3,1) term alone is 4.6e-9 at k = 1e6), a consequence of minimizing ||rF||_2 on the mesh out to r = 1e4. (iii) The
resulting far-field m is 4e-5 to 2e-6 (ESTIMATE: B_k and C_k scaled from the mesh values at k = 4096 by (k/4096)^(gamma/2 - 3/2), astra's O-bound), so 007
has no far-field floor of its fixed-c weak distance; the asymptotic law m_k ~ K k^((e+1)/2), K = 458.6 (from the exact (3,1) sine coefficient
s_1 = 724.4 and e = -2.7904), applies only where the leading sector dominates, far beyond k = 1e7. (iv) Candidates without the rF term (008) do not cancel:
their first-mode distance keeps rising to k of order 6000 (0.047) and decays only slowly beyond (0.0165 at k = 65536).""")
src = src.replace('FARWEAK_SUMMARY', "For 007 the exact-sector pairing cancels to 97 to 99.7 percent in the window k = 1e6 to 3e6 (r 650 to 1150), so m_far is 4e-5 to 2e-6\n   (estimate) and there is no far-field floor; the leading-sector law takes over only far beyond k = 1e7.")
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
src = src.replace('PUBTIME', now)
for ph, lane in (('COORDTIME', 'c1-coord'), ('N4TIME', 'c1-n4'), ('N3TIME', 'c1-n3')):
    t = subprocess.run(['grep', '-m1', '-o', r'^## 2026-10-29T[0-9:]*Z', f'RUN_ROOT/{lane}/NOTES_FOR_TEAM.md'], capture_output=True, text=True).stdout.strip().replace('## ', '')
    src = src.replace(ph, t or 'latest')
open(root+'/numerics/NUMERICS_v06_published_stage1.md', 'w').write(src)
print(now, len(src), [m for m in re.findall(r'[A-Z_]{6,}', src) if m in ('PAIR_SUMMARY', 'PAIRSECTION', 'STATUS', 'BRIDGE_PENDING', 'PAIRSLUG')])

"""fix_bg_far.py (lane numerics_agent_1): replace the float-evaluated BASE residual F0 (and its first and second Cartesian derivatives) on the mesh radii r >= R_sw by the
float evaluation of its exact far-field sector series (table from a phi_far.py output JSON: 'sector_table_base', binary64 conversions of the exact rationals,
classes down to exp_min). Reason (WORKLOG 2026-11-03 shift 3): the raw generator sums of the base have an absolute noise floor of about 1e-11 beyond r of a few
thousand, above the corrected residual F_* there; the series is accurate to below 1e-12 absolute at r >= 1000 for the 007 and C5 tables to exp_min = -8.
CLI: fix_bg_far.py <bg.pt> <far_sectors.json> <R_sw> <out.pt>.  Self-check: series against the raw mesh values on the first radii beyond R_sw (relative rms)."""
import sys, json, hashlib, time
import numpy as np, torch
bgpt, farj, R_sw, outpt = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4]
bg = torch.load(bgpt, weights_only=False); J = json.load(open(farj))
s = bg['mesh']['s'].numpy(); th = bg['mesh']['theta'].numpy(); r = np.exp(s); sel = r >= R_sw
tab = J['sector_table_base']
cs, sn = np.cos(th)[None, :], np.sin(th)[None, :]
rr = r[sel][:, None]
f = fr = frr = fth = frth = fthth = 0.0
for e, S in tab:
    ang_s = np.zeros(len(th)); ang_c = np.zeros(len(th)); ang_sN = np.zeros(len(th)); ang_cN = np.zeros(len(th)); ang_sNN = np.zeros(len(th))
    for N, c in S.items():
        N = int(N); ang_s += c*np.sin(N*th); ang_cN += c*N*np.cos(N*th); ang_sNN += c*N*N*np.sin(N*th)
    re = rr**e
    f = f+re*ang_s[None, :]; fr = fr+e*re/rr*ang_s[None, :]; frr = frr+e*(e-1)*re/rr**2*ang_s[None, :]
    fth = fth+re*ang_cN[None, :]; frth = frth+e*re/rr*ang_cN[None, :]; fthth = fthth-re*ang_sNN[None, :]
fx = cs*fr-sn*fth/rr; fy = sn*fr+cs*fth/rr
A = frth/rr-fth/rr**2; B = fr/rr+fthth/rr**2
fxx = cs**2*frr-2*sn*cs*A+sn**2*B; fyy = sn**2*frr+2*sn*cs*A+cs**2*B; fxy = sn*cs*(frr-B)+(cs**2-sn**2)*A
new = {(0, 0): f, (1, 0): fx, (0, 1): fy, (2, 0): fxx, (1, 1): fxy, (0, 2): fyy}
keys = sorted(bg['F0'].keys()); print('F0 keys', keys, 'mesh', len(r), 'x', len(th), 'replacing', int(sel.sum()), 'radii from', float(r[sel].min()))
chk = {}
for k, v in new.items():
    if k not in bg['F0']: continue
    old = bg['F0'][k].numpy()
    i0 = np.where(sel)[0][:8]   # the first eight radii beyond R_sw: raw values still accurate there to about 1e-5
    rel = float(np.sqrt(((old[i0]-v[:8])**2).mean())/np.sqrt((v[:8]**2).mean())); chk[str(k)] = rel
    far = np.where(sel)[0][-4:]; relfar = float(np.sqrt(((old[far]-v[-4:])**2).mean())/np.sqrt((v[-4:]**2).mean()))
    print(f'  {k}: rel rms raw-vs-series on first 8 radii beyond R_sw {rel:.2e}; on the last 4 radii {relfar:.2e}')
    arr = old.copy(); arr[sel] = v; bg['F0'][k] = torch.as_tensor(arr, dtype=bg['F0'][k].dtype)
lap = fxx+fyy; lap_ref = 0.0
for e, S in tab:
    ang = np.zeros(len(th))
    for N, c in S.items(): ang += c*(e*e-int(N)**2)*np.sin(int(N)*th)
    lap_ref = lap_ref+rr**(e-2)*ang[None, :]
print('  Laplacian identity check (rel rms): %.2e' % float(np.sqrt(((lap-lap_ref)**2).mean())/np.sqrt((lap_ref**2).mean())))
assert all(v < 1e-3 for v in chk.values()), chk
bg['meta']['far_fix'] = {'R_sw': R_sw, 'table_json': farj.split('/')[-1], 'table_sha256': hashlib.sha256(open(farj, 'rb').read()).hexdigest(), 'qmax': J.get('qmax'), 'exp_min': J.get('exp_min'),
                         'classes': len(tab), 'replaced_derivs': [str(k) for k in new if k in bg['F0']], 'check_rel_rms_first8': chk, 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                         'note': 'F0 and its first and second derivatives on r >= R_sw are the float evaluation of the exact base sector series (binary64 table); higher derivatives untouched'}
torch.save(bg, outpt); print('written', outpt)

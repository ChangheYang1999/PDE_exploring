"""stage_diag.py -- run the per-stage diagnostics on a saved state (axis_ode.py -> Q_R; axis_drop.py -> a_pl, w, q(r), S; constvel.py -> C2)
unless their JSON outputs already exist, and print ONE summary line for the 7l tables. Usage: python3 code/stage_diag.py runs/<state>.npz [--force]"""
import sys, os, json, subprocess, math, numpy as np
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
st = sys.argv[1]; force = '--force' in sys.argv
tag = os.path.basename(st)[:-4]
d = np.load(st)
beta = float(d['beta']); lam = float(d['lam']) if 'lam' in d.files else float('nan'); a0 = float(d['a0']) if 'a0' in d.files else 1.0
obj = float(d['obj']) if 'obj' in d.files else float('nan'); K = int(d['K']); Nt = int(d['Nt'])
m = float(d['strain_mismatch']) if 'strain_mismatch' in d.files else float('nan')
axis_json = f'{HERE}/runs/axis_{tag}.json'; drop_json = f'{HERE}/runs/drop_{tag}.json'; cv_txt = f'{HERE}/runs/constvel_{tag}.txt'
def run(cmd, out):
    with open(out, 'w') as fh:
        r = subprocess.run(cmd, stdout=fh, stderr=subprocess.PIPE, text=True, cwd=HERE, timeout=900)
    if r.returncode != 0: print('FAILED:', ' '.join(cmd), r.stderr[-500:]); return False
    return True
if force or not os.path.exists(axis_json): run(['python3', 'code/axis_ode.py', st, '--rmax', '1e8', '--n', '60'], axis_json)
if force or not os.path.exists(drop_json): run(['python3', 'code/axis_drop.py', st], drop_json)
if force or not os.path.exists(cv_txt): run(['python3', 'code/constvel.py', st], cv_txt)
A = json.load(open(axis_json)); D = json.load(open(drop_json))
up = A['axis']['up']; dn = A['axis']['down']
QR = up['Q_closed_form_est']; QRd = dn['Q_closed_form_est']; vr = up['v_over_beta_r_at']   # at r = 1, 10, 100, 1e4, 1e6, 1e8
relg = max(up['rel_diff_g']); 
rows = {}
for r, v in D['radii'].items():
    u = v['transported']['up']; w = u['width_90_10_deg'] if u['width_90_10_deg'] is not None else float('nan')   # None: the 10 percent crossing lies below the first angular node (width unresolved)
    rows[r] = (u['a_plateau'], w, u['a_over_angle_first_node'], math.radians(w) * u['a_over_angle_first_node'] / u['a_plateau'] if w == w else float('nan'))
import re
cv = open(cv_txt).read(); mm = re.search(r'C2 = ([-+\d.eE]+)', cv); C2 = float(mm.group(1)) if mm else float('nan')
r_hi = max(rows, key=lambda k: float(k)); r_lo = min(rows, key=lambda k: float(k))
print(f"{tag}: lambda {lam:.6f} beta {beta:.6f} a0 {a0:.6f} K {K} Nt {Nt} floor {obj:.4g} m {m:+.1e} | Q_R up {QR:.2f} down {QRd:.3f} (ODE vs transported g {relg:.1e}) v/(beta r) at 10,100,1e4 {vr[1]:.4f},{vr[2]:.4f},{vr[3]:.4f} | r={r_hi}: a_pl {rows[r_hi][0]:.3f} w {rows[r_hi][1]:.2f} deg q {rows[r_hi][2]:.1f} S {rows[r_hi][3]:.3f}; r={r_lo}: a_pl {rows[r_lo][0]:.3f} w {rows[r_lo][1]:.2f} q {rows[r_lo][2]:.1f} S {rows[r_lo][3]:.3f} | C2 {C2:.2f} | a0^(1/beta) Q_R {a0 ** (1 / beta) * QR:.2f}")

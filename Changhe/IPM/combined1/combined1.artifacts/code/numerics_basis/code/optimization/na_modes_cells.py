"""theory_v03 section 9 item 1 (FLOAT proxy): projected weighted-Laplacian norm of angular modes 1 and 3, N_a^(1,3) = (sum_{n=1,3} ||(1+r^2)^((2-a)/2) (Delta F)_n||^2)^(1/2),
at the cell right ends a = 1/4, 1/2, 3/4, 1, 5/4, 3/2, 7/4 against the thresholds of theory_v03 section 5 (15.88162, 8.716729, 4.799949, 2.565236, 1.263642,
0.5028299, 0.06411577): a cell is excluded when the LB at the right end h exceeds the threshold of the cell.  FLOAT (mesh), not a bound; exact LBs are c1-n4's.
argv: exact_json ANG R out_json [MID]"""
import sys, os; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization'); os.environ['CUDA_VISIBLE_DEVICES'] = ''
from candA_setup import *
import ipm_opt2 as O2, time, hashlib
path = sys.argv[1]; ANG = int(sys.argv[2]); R = float(sys.argv[3]); outp = sys.argv[4]; MID = int(sys.argv[5]) if len(sys.argv) > 5 else 32
dev = torch.device('cpu'); c, gens, coefs_q, _ = OPT.load_candidate_json(path); coefs = np.array([X.qfloat(v) for v in coefs_q])
s, ws, bl = EV.whole_axis_radial(origin_order=48, middle_order=MID); keep = (np.exp(s) >= 0.02) & (s <= math.log(R)+1e-9); s, ws = s[keep], ws[keep]
th, wth = EV.angular_midpoint(ANG); mesh = EV.Mesh(s, ws, th, wth, dev)
prob = O2.Problem2(gens, c, mesh, r_cut=0.02, r_max=R); parts, comp, Fd = prob.objective_parts(coefs)
lap = comp[(2, 0)]+comp[(0, 2)]
Fn = (4/math.pi)*(lap*mesh.wth[None, :])@torch.stack([torch.sin(n*mesh.theta) for n in (1, 3)]).T    # quarter-plane midpoint projection x 4/pi -> full-circle sine coefficients
cells = [(0, 0.25, 15.88162), (0.25, 0.5, 8.716729), (0.5, 0.75, 4.799949), (0.75, 1.0, 2.565236), (1.0, 1.25, 1.263642), (1.25, 1.5, 0.5028299), (1.5, 1.75, 0.06411577)]
res = []
for l, h, thr in cells:
    vals = {n: math.sqrt(float(torch.sum(math.pi*mesh.ws*mesh.r**2*(1+mesh.r**2)**(2-h)*Fn[:, i]**2))) for i, n in enumerate((1, 3))}
    N13 = math.sqrt(vals[1]**2+vals[3]**2)
    res.append({'cell': [l, h], 'threshold_at_l': thr, 'N_h_modes_1_3_FLOAT': N13, 'mode1': vals[1], 'mode3': vals[3], 'excluded_if_LB_certified': N13 > thr, 'ratio': N13/thr})
    print(f'cell [{l}, {h}]: threshold {thr:.6g}; N_h(modes 1+3) FLOAT {N13:.6g} (mode 1 {vals[1]:.4g}, mode 3 {vals[3]:.4g}); ratio {N13/thr:.3f} -> {"excluded (if LB certified)" if N13 > thr else "NOT excluded by modes 1, 3"}', flush=True)
json.dump({'candidate': os.path.basename(path), 'sha256': hashlib.sha256(open(path, 'rb').read()).hexdigest(), 'rule': f'radial Gauss {MID}/panel x midpoint {ANG}, 0.02 <= r <= {R:g}', 'cells': res,
           'all_cells_excluded_FLOAT': all(x['excluded_if_LB_certified'] for x in res), 'label': 'FLOAT proxy of theory_v03 section 9 item 1 (NC-T-ORIGIN-INV / NC-T-DYADIC-LAP cell test with modes 1 and 3); exact LBs by c1-n4'}, open(outp, 'w'), indent=1)

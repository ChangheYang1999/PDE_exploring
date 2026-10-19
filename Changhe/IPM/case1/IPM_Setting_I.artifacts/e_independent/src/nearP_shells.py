"""Lead request 01:57Z: between-node normalised residual (my divided-form normalisation) on shells |X-P| < 0.5, 0.5-1, 1-2, 2-4, 4-8 and
the whole-domain bands, for given states. Usage: python3 src/nearP_shells.py state1.npz [state2.npz ...]"""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import diag, ipm1lsq, charac
dev = 'cuda'
for path in sys.argv[1:]:
    m, b, cl, d = diag.load(path, device=dev); m.k_tail = 1 / cl
    Qr = int(d['Qr']) if 'Qr' in d.files else 2 * m.N; Qth = int(d['Qth']) if 'Qth' in d.files else 2 * m.M + 1
    ls = ipm1lsq.LSQ(m, Qr=Qr, Qth=Qth, chunk=256, verbose=False)
    cl, c, fl = ls.cl_of_b(b, cl); E, q = ls.residual_q(b, cl, fl); den = ls.denominators(b, cl, q); rel = (E / den)
    Pi = charac.FieldEval(m, b, cl).find_P(); xs = Pi['x_star']
    Xq = ls.rq[:, None] * ls.cq[None, :]; Yq = ls.rq[:, None] * ls.sq[None, :]; dP = torch.sqrt((Xq - xs) ** 2 + Yq ** 2)
    out = []
    for lo, hi in [(0, 0.5), (0.5, 1), (1, 2), (2, 4), (4, 8)]:
        mk = (dP >= lo) & (dP < hi); v = rel[mk]
        out.append(f"[{lo},{hi}): n={int(mk.sum())} rms {math.sqrt((v**2).mean().item()):.2e} max {v.abs().max().item():.2e}")
    rq = ls.rq.cpu().numpy(); band = []
    for name, (a_, b_) in {'r<=2': (0, 2), '2-10': (2, 10), '10-100': (10, 100), '>100': (100, np.inf)}.items():
        mk = (rq > a_) & (rq <= b_); v = rel[mk]; band.append(f"{name} {math.sqrt((v**2).mean().item()):.2e}/{v.abs().max().item():.2e}")
    print(f"{path}: c_l {cl:.7f}, x* {xs:.5f}, h(P)-1 {Pi['h']-1:+.2e}; quadrature grid {Qr}x{Qth}")
    print("   shells |X-P|: " + "; ".join(out))
    print("   bands (rms/max): " + "; ".join(band), flush=True)

"""Where the stagnation residual sits: fraction of |F|^2 within distance 2 and 5 of P, and rms per row inside / outside, for the state of a stored Jacobian.
Usage: python3 src/floor_location.py runs/J_<tag>.pt [more J files]"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt
for jpath in sys.argv[1:]:
    J, z, model, ch, D = jt.load_J(jpath, 480); del J; torch.cuda.empty_cache(); N, M = model.N, model.M
    b, cl, C = ch.unpack(z); cl = float(cl)
    s4 = f'{jt.LANE}/runs/s4e_{os.path.basename(D["state"]).replace(".npz", "")}.json'; xstar = float(json.load(open(s4))['xstar']) if os.path.exists(s4) else 8.5774
    r, w, v = model.radii(cl); th = model.ang.theta_np; rr = np.repeat(r[1:], M); tt = np.tile(th, N); dP = np.hypot(rr * np.cos(tt) - xstar, rr * np.sin(tt))
    F = ch.F(z, **jt.RES_KW).cpu().numpy(); tot = (F ** 2).sum()
    m2 = np.concatenate([dP < 2, [True, False]]); m5 = np.concatenate([dP < 5, [True, False]])
    print(f'{os.path.basename(jpath)}: state {os.path.basename(D["state"])} (N,M,L) = ({N},{M},{model.L}) x* {xstar:.6f} |F| {np.sqrt(tot):.4e}; rows within 2 / 5: {m2.sum()} / {m5.sum()} of {len(F)}; '
          f'|F|^2 fraction within 2 / 5: {(F[m2]**2).sum()/tot:.3f} / {(F[m5]**2).sum()/tot:.3f}; rms per row near5 {np.sqrt((F[m5]**2).mean()):.2e} elsewhere {np.sqrt((F[~m5]**2).mean()):.2e}; max |F| row at d = {dP[np.argmax(np.abs(F[:-2]))]:.2f}', flush=True)

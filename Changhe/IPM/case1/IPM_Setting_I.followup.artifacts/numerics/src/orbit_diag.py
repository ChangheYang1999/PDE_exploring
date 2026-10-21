"""Lead's diagnostic (NOTES_FOR_TEAM 01:52Z item 3): for the softest right singular vectors of the collocation Jacobian,
follow delta rho / rho = delta b / b along backward orbits from points inside the mode's band, and compare with
exp(-int (m - 1) dtau), m - 1 = rho W_2/|W|^2 (coupled quasimode rate) and with a constant (pure transport).
Usage: python3 src/orbit_diag.py runs/state.npz nmodes"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, nullspace as ns, charmap as cm

path = sys.argv[1]; kmodes = int(sys.argv[2]) if len(sys.argv) > 2 else 2
model, x, d = ipn.load_state(path); b, cl = model.unpack(x); clf = float(cl); k = 1 / clf
r, w, v = model.radii(clf); th = model.ang.theta_np
J = model.jacobian(x); s, V, U, LU = ns.small_triplets(J, kmodes, 40)
ch = cm.Charac(model); st = ch.prepare(b, cl); xstar, hP, wpP, hpP = ch.find_P(st)
print('c_l %.7f x* %.6f h(P) %.7f' % (clf, float(xstar), float(hP)))
N, M = model.N, model.M

def rho_and_b_at(X):
    rr = np.hypot(X[:, 0], X[:, 1]); tt = np.arctan2(X[:, 1], X[:, 0]); qq = model.q_of_r(rr, clf)
    bb = model.eval_EE(b, qq, tt); ww = (1 + (rr / model.L) ** 2) ** ((k - 3) / 2)
    return rr ** 3 * ww * np.cos(tt) ** 2 * np.sin(tt) * bb, bb, qq, tt

for im in range(kmodes):
    vb = V[:-1, im].reshape(N, M).cpu().numpy(); vfull = np.vstack([np.zeros((1, M)), vb])   # delta b on the grid (row 0 = 0)
    amp = np.abs(vb); 
    # pick starting points: the 4 largest |v|/b entries among nodes with 30 < r < 3000
    rr1 = r[1:]; mask = (rr1 > 30) & (rr1 < 3000)
    ratio = np.where(mask[:, None], np.abs(vb) / np.abs(b[1:].cpu().numpy()), 0)
    idx = np.argsort(-ratio.ravel())[:12]
    picks = []
    for f in idx:
        i, j = f // M, f % M
        if all(abs(np.log(rr1[i] / rr1[pi])) > 0.7 or abs(th[j] - th[pj]) > 0.05 for pi, pj in picks): picks.append((i, j))
        if len(picks) == 4: break
    print('mode %d sigma %.3e c_l comp %.3e; start points:' % (im, s[im].item(), V[-1, im].item()), [(round(rr1[i], 2), round(th[j] * 180 / np.pi, 1)) for i, j in picks])
    X0 = torch.tensor([[rr1[i] * np.cos(th[j]), rr1[i] * np.sin(th[j])] for i, j in picks], device=model.dev)
    # integrate backward, recording every 20 steps
    X = X0.clone(); dt = 0.005; rec = []
    Im1 = torch.zeros(X.shape[0], device=model.dev)   # int (m-1) dtau
    for n in range(6000):
        Xn = X.detach().cpu().numpy()
        rho, bb, qq, tt = rho_and_b_at(Xn)
        dbb = model.eval_EE(torch.tensor(vfull, device=model.dev), qq, tt)
        if n % 40 == 0:
            rec.append((n * dt, Xn.copy(), dbb / bb, Im1.cpu().numpy().copy(), rho.copy()))
        W1, W2, bt = ch.Wfield(st, X)
        rhoT = torch.tensor(rho, device=model.dev)
        m1 = rhoT * W2 / (W1 ** 2 + W2 ** 2)
        # RK2 midpoint for the orbit (cheap), Euler for the integral at the midpoint
        Xm = X - 0.5 * dt * torch.stack([W1, W2], 1)
        W1m, W2m, _ = ch.Wfield(st, Xm)
        X = X - dt * torch.stack([W1m, W2m], 1)
        Im1 = Im1 + dt * m1
        dist = torch.sqrt((X[:, 0] - xstar) ** 2 + X[:, 1] ** 2)
        if bool((dist < 2e-2).all()): break
    print('  tau    ' + '   '.join('orbit%d: x,y | log(db/b) | -int(m-1)' % p for p in range(len(picks))))
    for (tau, Xn, ratio_, I1, rho) in rec[::max(1, len(rec) // 14)] + [rec[-1]]:
        row = '  %5.2f ' % tau
        for p in range(len(picks)):
            row += ' | (%7.3f,%7.3f) %+7.3f %+7.3f' % (Xn[p, 0], Xn[p, 1], np.log(abs(ratio_[p])) if ratio_[p] != 0 else float('nan'), -I1[p])
        print(row)

"""Smallest singular triplets of the Jacobian at a saved state, with their spatial structure.
Usage: python3 src/nullspace.py runs/state.npz [k] [iters]"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn

def small_triplets(J, k=8, iters=40):
    LU = torch.linalg.lu_factor(J)
    n = J.shape[0]
    V = torch.randn(n, k, device=J.device)
    for it in range(iters):
        Y = torch.linalg.lu_solve(*LU, V, adjoint=True); Z = torch.linalg.lu_solve(*LU, Y)      # (J^T J)^-1 V
        V, _ = torch.linalg.qr(Z)
    JV = J @ V
    Uk, sk, Wk = torch.linalg.svd(JV, full_matrices=False)   # JV = Uk sk Wk^T  -> J (V Wk) = Uk sk
    Vk = V @ Wk.T if False else V @ Wk.transpose(0, 1)
    # sort ascending
    idx = torch.argsort(sk)
    return sk[idx], Vk[:, idx], Uk[:, idx], LU

def describe(model, v, r, th, top=8):
    N, M = model.N, model.M
    vb = v[:-1].reshape(N, M).cpu().numpy(); vcl = v[-1].item()
    en = vb ** 2; tot = en.sum() + vcl ** 2
    rr = r[1:]
    rad = {'r<0.3': en[rr < 0.3].sum(), '0.3-1': en[(rr >= 0.3) & (rr < 1)].sum(), '1-3': en[(rr >= 1) & (rr < 3)].sum(), '3-10': en[(rr >= 3) & (rr < 10)].sum(),
           '10-100': en[(rr >= 10) & (rr < 100)].sum(), '100-1e4': en[(rr >= 100) & (rr < 1e4)].sum(), '>1e4': en[rr >= 1e4].sum()}
    thd = th * 180 / np.pi
    ang = {'<3deg': en[:, thd < 3].sum(), '3-10': en[:, (thd >= 3) & (thd < 10)].sum(), '10-80': en[:, (thd >= 10) & (thd < 80)].sum(), '80-87': en[:, (thd >= 80) & (thd < 87)].sum(), '>87': en[:, thd >= 87].sum()}
    flat = np.argsort(-np.abs(vb).ravel())[:top]
    tops = ['(r=%.3g,th=%.1f: %+.3f)' % (rr[f // M], thd[f % M], vb.ravel()[f]) for f in flat]
    s = '  c_l comp %+.3e; radial ' % vcl + ' '.join('%s:%.2f' % (a, b / tot) for a, b in rad.items())
    s += '\n  angular ' + ' '.join('%s:%.2f' % (a, b / tot) for a, b in ang.items()) + '\n  top entries ' + ' '.join(tops)
    # sign structure along radius at the dominant angle
    j0 = flat[0] % M
    s += '\n  radial profile at th=%.1f: ' % thd[j0] + ' '.join('%+.2e' % vb[i, j0] for i in range(min(12, N)))
    return s

if __name__ == '__main__':
    path = sys.argv[1]; k = int(sys.argv[2]) if len(sys.argv) > 2 else 8; iters = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    model, x, d = ipn.load_state(path)
    b, cl = model.unpack(x)
    r, w, v = model.radii(float(cl)); th = model.ang.theta_np
    t0 = time.time(); J = model.jacobian(x); print('J assembled %.1fs' % (time.time() - t0))
    F = model.F(x); print('|F|_inf %.3e' % F.abs().max().item())
    s, V, U, LU = small_triplets(J, k, iters)
    for i in range(k):
        v = V[:, i]; u = U[:, i]
        res = (J @ v - s[i] * u).norm().item()
        uF = (u @ F).item()
        print('sigma_%d = %.4e  (|Jv - s u| %.1e)  u.F = %+.3e  -> Newton component |u.F|/sigma = %.3e' % (i, s[i].item(), res, uF, abs(uF) / s[i].item()))
        print(describe(model, v, r, th))
        # left vector: which rows
        ub = u[:-1].reshape(model.N, model.M).cpu().numpy(); en = ub ** 2; rr = r[1:]
        print('  left vector rows: identity row %.2e; radial r<0.3:%.2f 0.3-1:%.2f 1-10:%.2f 10-100:%.2f >100:%.2f' % (u[-1].item() ** 2, en[rr < 0.3].sum(), en[(rr >= 0.3) & (rr < 1)].sum(), en[(rr >= 1) & (rr < 10)].sum(), en[(rr >= 10) & (rr < 100)].sum(), en[rr >= 100].sum()))

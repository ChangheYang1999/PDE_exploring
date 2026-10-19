"""V29(g): f_0-free consistency check of a forced c_l path.  Every stage k solves R_z[zeta_k] = lambda_k f_0 with the SAME
f_0, so G_k := R_z[zeta_k]/lambda_k must be one function.  With my evaluator (tests/cand_eval.py: own Chebyshev fit, own
power2 tail, own full-plane inverse) R_z is computed at the numerics nodes and at the midpoints between them, retained modes
|m| <= M; reference G = R_z[zeta_ref]/lambda_ref (first file).  Per stage: least-squares ratio mu_k = <R_z[zeta_k], G>/<G, G>
(to compare with lambda_k) and max |R_z[zeta_k] - lambda_k G| by radial band relative to the band max of |lambda_k G|.
usage: python3 tests/cand_ratio.py REF.pt STATE.pt ...   (all with the same Nr, Nth, R, L)"""
import sys, json, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cand_eval as ce
import torch


def rz_nodes(path, nt=128):
    st = torch.load(path, map_location='cpu', weights_only=False)
    Z = ce.ZetaRep(st)
    cl = float(st['cl']); lam = float(st['lam']); p = 1/cl
    Ev = ce.Evaluator(Z.R, nt)
    G = Ev.G; th = G.th; r = G.r; ins = Ev.inside
    zeta = np.zeros_like(G.X); zeta[ins] = Z.field(r[ins], th)
    ta, tb, q1, q2 = ce.tail_fit(Z, p)
    rho = zeta*zeta; rho[~ins] = ce.tail_field(ta, tb, q1, q2, r[~ins], th)
    Rz, c, bb, W1, W2, gx, gy = Ev.transport(zeta, rho, cl, p)
    xm = 0.5*(Z.xn[:-1] + Z.xn[1:])
    rm_ = Z.L*np.sqrt(np.exp(Z.xi_max*(1 + xm)/2) - 1)
    out = {}
    for name, rq in (('nodes', Z.rn), ('mid', rm_)):
        w1 = ce.panel_interp(Ev, W1, rq); w2 = ce.panel_interp(Ev, W2, rq)
        Xq = rq[:, None]*np.cos(th)[None]; Yq = rq[:, None]*np.sin(th)[None]
        z, zx, zy = ce.zeta_grad_rep(Z, rq, th)
        Rq = (cl*Xq + w1)*zx + (cl*Yq + w2)*zy - 0.5*z
        out[name] = (rq, ce.split_modes(Rq, Z.M)[0])
    return dict(cl=cl, lam=lam, compat=cl - 0.5 - c, jet=Z.jet(), R=Z.R, Nr=Z.Nr, Nth=Z.Nth, eps=st['args'].get('eps'),
                jetmode=st['args'].get('jet'), data=out)


bands = [(0, 1), (1, 10), (10, 50), (50, 100), (100, 300), (300, 1000)]
ref = rz_nodes(sys.argv[1])
print(json.dumps(dict(ref=os.path.basename(sys.argv[1]), cl=ref['cl'], lam=ref['lam'], compat=ref['compat'], jet=ref['jet'],
                      eps=ref['eps'], jetmode=ref['jetmode'])), flush=True)
Gn = {k: v[1]/ref['lam'] for k, v in ref['data'].items()}
for path in sys.argv[2:]:
    s = rz_nodes(path)
    row = dict(state=os.path.basename(path), cl=s['cl'], lam=s['lam'], compat=s['compat'], jet=s['jet'])
    A = Gn['nodes'].ravel(); B = s['data']['nodes'][1].ravel()
    row['mu_ls_nodes'] = float(A @ B/(A @ A))
    for name in ('nodes', 'mid'):
        rq, Rk = s['data'][name]
        D = Rk - s['lam']*Gn[name]
        bb = []
        for lo, hi in bands:
            sel = (rq > lo) & (rq <= hi)
            bb.append(float(np.abs(D[sel]).max()/np.abs(s['lam']*Gn[name][sel]).max()) if sel.any() else None)
        row['rel_' + name] = bb
    print(json.dumps(row), flush=True)

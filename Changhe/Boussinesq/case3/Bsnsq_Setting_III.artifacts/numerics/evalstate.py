"""Evaluate residuals of a stored state on an independent (finer, shifted) collocation set."""
import sys, os, json, argparse, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, Problem, DT
from solve import eval_fields_at
torch.set_default_dtype(DT)


def load_state(path, dev='cuda'):
    d = np.load(path)
    cF = torch.tensor(d['cF'], dtype=DT, device=dev); cG = torch.tensor(d['cG'], dtype=DT, device=dev)
    meta = {}
    for k in d.files:
        if k in ('cF', 'cG'): continue
        v = d[k]
        meta[k] = (v.item() if v.ndim == 0 else v)
    return cF, cG, meta


def basis_from_meta(meta, dev='cuda', ngc=None, Nphi=None):
    return Basis(int(meta['Nt']), int(meta['deg']), int(meta['K']), int(meta['Nphi']) if Nphi is None else Nphi,
                 ng_coll=int(meta.get('ngc', 3)) if ngc is None else ngc, m_reg=int(meta['mreg']), device=dev,
                 grade=float(meta.get('grade', 1.0)))


def report(path, ngc=9, Nphi_mult=2):
    dev = 'cuda'
    cF, cG, meta = load_state(path, dev)
    beta, L = meta['beta'], meta['L']
    beta_b = meta.get('beta_basis', beta)
    # evaluation basis: same splines, more Gauss points per interval and more angular nodes (points differ from fit nodes)
    b = basis_from_meta(meta, dev, ngc=ngc, Nphi=int(meta['Nphi']) * Nphi_mult)
    g = Geometry(b, beta_b, L, rmap=str(meta.get('rmap', 'r')))
    p = Problem(g, beta_dyn=beta)
    f = p.fields(cF, cG)
    RF, RG, NF, NG = p.residuals(cF, cG, f)
    nF = (RF / NF).abs(); nG = (RG / NG).abs()
    rr = g.rr; x = g.x
    out = {'file': path, 'beta': beta, 'beta_basis': beta_b, 'L': L, 'c': (g.c_op @ cG).item(), 'c_target': 1 + beta / 2,
           'G0': cG[0].item(), 'G0_target': 4 / beta, 'Npts_eval': int(rr.numel())}
    regions = [(0, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e4), (1e4, 1e99)]
    tab = []
    for lo, hi in regions:
        m = (rr >= lo) & (rr < hi)
        if m.any():
            tab.append(dict(r_lo=lo, r_hi=hi, n=int(m.sum()), maxRF_N=nF[m].max().item(), maxRG_N=nG[m].max().item(),
                            maxRTheta=(RF[m] * x[m] ** 2).abs().max().item(), maxROmega=(RG[m] * x[m]).abs().max().item(),
                            maxTheta=(f['F'][m] * x[m] ** 2).abs().max().item(), maxOmega=(f['G'][m] * x[m]).abs().max().item()))
    out['regions'] = tab
    out['maxRF_N'] = nF.max().item(); out['maxRG_N'] = nG.max().item()
    # where is the max
    i = int(nF.argmax()); j = int(nG.argmax())
    out['argmaxF'] = dict(r=rr[i].item(), x=x[i].item(), y=g.y[i].item())
    out['argmaxG'] = dict(r=rr[j].item(), x=x[j].item(), y=g.y[j].item())
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('state')
    ap.add_argument('--ngc', type=int, default=9)
    ap.add_argument('--nphimult', type=int, default=2)
    a = ap.parse_args()
    o = report(a.state, a.ngc, a.nphimult)
    print(json.dumps({k: v for k, v in o.items() if k != 'regions'}, indent=1))
    print(f"{'r range':>16} {'n':>6} {'max|RF/NF|':>11} {'max|RG/NG|':>11} {'max|RTheta|':>11} {'max|ROmega|':>11} {'max|Theta|':>11} {'max|Omega|':>11}")
    for t in o['regions']:
        print(f"[{t['r_lo']:7.3g},{t['r_hi']:7.3g}) {t['n']:6d} {t['maxRF_N']:11.3e} {t['maxRG_N']:11.3e} {t['maxRTheta']:11.3e} {t['maxROmega']:11.3e} {t['maxTheta']:11.3e} {t['maxOmega']:11.3e}")

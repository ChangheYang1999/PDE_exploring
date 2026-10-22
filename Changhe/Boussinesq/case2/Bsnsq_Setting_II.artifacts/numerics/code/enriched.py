"""LABELLED finite-regularity study (analysis request 14:37Z item 3), NOT a derived smoothness claim:
add to Omega one extra basis function  Omega_f = kappa * chi(r) x^p y,  p = p'_0 = (3 beta + 3)/(beta + 2)
(the first fractional homogeneous mode at the saddle), chi(r) = exp(-(r/Rc)^2), with its canonical
full-plane stream response computed by direct quadrature of the modal Green formula (sine modes k = 2..K of the
angular function cos^p(th) sin(th)). One extra unknown kappa in the least squares; everything else as in lm_solve."""
import sys, time, math, json, numpy as np, torch
sys.path.insert(0, 'code')
from a2core import DT
from lm_solve import LMProblem, load_state, problem_from_state, save_state, lm, dev
from scipy.integrate import quad


class Extra:
    def __init__(self, model, beta, Rc, K=80, nu=6000):
        self.p = (3 * beta + 3) / (beta + 2); p = self.p
        self.Rc, self.K = Rc, K
        th = model.th; r = model.r
        # angular sine coefficients of A(th) = cos^p th sin th (odd-odd extension): c_k = (4/pi) int_0^{pi/2} A sin(k th) dth
        ks = np.arange(2, K + 1, 2)
        self.ks = ks
        ck = np.array([(4 / np.pi) * quad(lambda t: np.cos(t) ** p * np.sin(t) * np.sin(k * t), 0, np.pi / 2, limit=200)[0] for k in ks])
        self.ck = ck
        # radial: b_k(s) = c_k chi(s) s^{p+1};  scaled Green integrals on a fine log grid (trapezoid), per target radius:
        #   r^{-k} I_in(r) = int_0^r (s/r)^k s b ds,   r^k I_out(r) = int_r^inf (r/s)^k s b ds   (integrands <= s b: no overflow)
        u = np.linspace(np.log(1e-5), np.log(400.0), nu); s = np.exp(u); du = u[1] - u[0]
        chi = np.exp(-(s / Rc) ** 2); sb = chi * s ** (p + 1) * s * s     # s * b(s)/c_k * (ds = s du)
        self.h = np.zeros((len(ks), len(r))); self.hd = np.zeros((len(ks), len(r)))
        lr = np.log(r)
        for i, k in enumerate(ks):
            ratio_in = np.exp(np.clip(k * (u[None, :] - lr[:, None]), -700, 0))   # (s/r)^k for s<=r, 0 beyond via mask
            mask_in = (s[None, :] <= r[:, None])
            A_in = np.sum(ratio_in * sb[None, :] * mask_in, axis=1) * du
            ratio_out = np.exp(np.clip(k * (lr[:, None] - u[None, :]), -700, 0))  # (r/s)^k for s>=r
            A_out = np.sum(ratio_out * sb[None, :] * (~mask_in), axis=1) * du
            self.h[i] = ck[i] * (A_in + A_out) / (2 * k)
            self.hd[i] = ck[i] * (-A_in + A_out) / (2 * r)
        # strain contribution: c_f = (1/2) int_0^inf b_2/s ds
        f2 = ck[0] * chi * s ** (p + 1) / s * s       # b_2/s * (ds = s du)
        self.c_f = 0.5 * np.sum(f2) * du
        # velocity on the grid [e, m]
        S = np.sin(np.outer(ks, th)); dS = ks[:, None] * np.cos(np.outer(ks, th))
        Psi_r = self.hd.T @ S; Psi_th = self.h.T @ dS
        c, sn = np.cos(th)[None, :], np.sin(th)[None, :]; rr = r[:, None]
        self.U1 = torch.tensor(-(sn * Psi_r + c * Psi_th / rr), dtype=DT, device=dev)
        self.U2 = torch.tensor(c * Psi_r - sn * Psi_th / rr, dtype=DT, device=dev)
        X = rr * c; Y = rr * sn; chi_r = np.exp(-(rr / Rc) ** 2); dchi = -2 * rr / Rc ** 2 * chi_r
        Gf = chi_r * X ** (p - 1)
        self.G = torch.tensor(Gf, dtype=DT, device=dev)
        self.Gx = torch.tensor(dchi * (X / rr) * X ** (p - 1) + chi_r * (p - 1) * X ** (p - 2), dtype=DT, device=dev)
        self.Gy = torch.tensor(dchi * (Y / rr) * X ** (p - 1), dtype=DT, device=dev)
        self.c_f_t = torch.tensor(self.c_f, dtype=DT, device=dev)


class EnrichedProblem:
    def __init__(self, prob, extra):
        self.prob, self.ex = prob, extra
        self.n_unknown = prob.n_unknown + 1
        for a in ('M', 'N', 'L', 'Ne', 'Me', 'mapname', 'beta_map', 'sigma_a', 'sigma_G', 'a0_target', 'w_origin', 'Rw', 'wmax', 'model', 'fixed_beta', 'wa', 'wG', 'rownorm'):
            setattr(self, a, getattr(prob, a))

    def unpack(self, z):
        ca, cG, beta = self.prob.unpack(z[:-1]); return ca, cG, beta, z[-1]

    def pack(self, ca, cG, beta, kappa):
        return torch.cat([self.prob.pack(ca, cG, beta), torch.tensor([kappa], dtype=DT, device=dev)])

    def fields(self, z):
        ca, cG, beta, kappa = self.unpack(z)
        f = self.prob.model.fields(ca, cG, beta)
        ex = self.ex
        U1 = f['U1'] + kappa * ex.U1; U2 = f['U2'] + kappa * ex.U2
        x, y = f['x'], f['y']
        W1 = beta * x + U1; W2 = beta * y + U2; w1 = beta + U1 / x; w2 = beta + U2 / y
        G = f['G'] + kappa * ex.G; G_x = f['G_x'] + kappa * ex.Gx; G_y = f['G_y'] + kappa * ex.Gy
        Ra = W1 * f['a_x'] + W2 * f['a_y'] + (2 * w1 + w2 - beta + 2) * f['a']
        RG = W1 * G_x + W2 * G_y + (w1 + w2 + 1) * G - 2 * f['a'] - x * f['a_x']
        c = f['c'] + kappa * ex.c_f_t
        out = dict(f); out.update(Ra=Ra, RG=RG, c=c, G=G, U1=U1, U2=U2, W1=W1, W2=W2, w1=w1, w2=w2, kappa=kappa)
        return out

    def F(self, z):
        f = self.fields(z); beta = self.unpack(z)[2]
        rows = [self.wa * f['Ra'].reshape(-1), self.wG * f['RG'].reshape(-1),
                self.w_origin * ((2 * beta - f['c'] + 2) * f['a0']).reshape(1),
                self.w_origin * ((2 * beta + 1) * f['G0'] - 2 * f['a0']).reshape(1),
                self.w_origin * (f['a0'] - self.a0_target).reshape(1)]
        return torch.cat(rows)

    def jac(self, z, chunk=1024):
        return torch.func.jacfwd(self.F)(z)

    def diagnostics(self, z):
        f = self.fields(z); Fv = self.F(z); ca, cG, beta, kappa = self.unpack(z)
        d = dict(beta=float(beta), a0=float(f['a0']), G0=float(f['G0']), c=float(f['c']), c_minus_2b2=float(f['c'] - 2 * beta - 2),
                 Fnorm=float(Fv.norm()), Fmax=float(Fv.abs().max()), Ra_max=float(f['Ra'].abs().max()), RG_max=float(f['RG'].abs().max()),
                 kappa=float(kappa), a_rtail=0.0, a_atail=0.0, G_rtail=0.0, G_atail=0.0, n_unknown=int(self.n_unknown))
        return d


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument('--init', required=True); ap.add_argument('--Rc', type=float, default=9.0)
    ap.add_argument('--K', type=int, default=80); ap.add_argument('--maxit', type=int, default=300); ap.add_argument('--name', default='E1')
    ap.add_argument('--kappa0', type=float, default=0.0)
    args = ap.parse_args()
    d = load_state(args.init); prob, z = problem_from_state(d, fixed_beta=float(d['beta']))
    beta = float(d['beta'])
    t0 = time.time(); ex = Extra(prob.model, beta, args.Rc, args.K); print(f"extra basis built in {time.time()-t0:.0f}s: p={ex.p:.4f}, c_f={ex.c_f:.5f}, first ck={ex.ck[:4]}", flush=True)
    ep = EnrichedProblem(prob, ex)
    ca, cG, b = prob.unpack(z); ze = ep.pack(ca, cG, beta, args.kappa0)
    print("start:", {k: round(v, 6) for k, v in ep.diagnostics(ze).items()}, flush=True)
    log = open(f'runs/{args.name}.log', 'a')
    ze, hist = lm(ep, ze, maxit=args.maxit, log=log)
    dd = ep.diagnostics(ze); print("final:", dd, flush=True)
    ca, cG, b, kappa = ep.unpack(ze)
    save_state(f'runs/{args.name}.npz', prob, ze[:-1], hist, extra=dict(kappa=float(kappa), Rc=args.Rc, K=args.K, p=ex.p, c_f=float(ex.c_f), labelled='finite-regularity study'))

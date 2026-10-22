"""eps = 0 scan with SIGN-CHANGING external vorticity (shift 7; PROMPT sec. 4: 'allowing sign changes may be indispensable').
Omega_ext = A x sum_i a_i exp(-(x^2+(y-y_i)^2)/(2 s_i^2)) with signed relative amplitudes a_i (a_1 = +1 by convention);
A is chosen so that the centre strain of Omega_ext equals c_in (beta = 2(c_in - 1)). As in code/scan_eps0.py (sec. 5 of
NUM_REPORT): W_ext from the canonical inverse, Theta and Omega transported by characteristics from the centre jet, and
the strain c_out of the transported vorticity is compared with c_in. A fixed point of B2-P needs c_out = c_in.
Extra diagnostics: sign structure of Omega_char (min, max, fraction of residual points with Omega_char < 0, weighted
negative fraction of the strain integrand), unfinished trajectories (additional stagnation points of W_ext would show up here).
Case syntax: 'cin|a1,y1,s1|a2,y2,s2|...' (a1 is normally 1) or 'A=..|a1,y1,s1|...'."""
import sys, os, time, json, argparse, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, Problem, DT
from charnewton import CharResidual
torch.set_default_dtype(DT)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--beta_basis', type=float, default=3.0)
    ap.add_argument('--L', type=float, default=1.5)
    ap.add_argument('--Nt', type=int, default=32); ap.add_argument('--K', type=int, default=12)
    ap.add_argument('--Nphi', type=int, default=24); ap.add_argument('--Nphi_res', type=int, default=12)
    ap.add_argument('--ngc', type=int, default=7); ap.add_argument('--grade', type=float, default=1.5)
    ap.add_argument('--dt', type=float, default=0.02); ap.add_argument('--r_in', type=float, default=1e-3)
    ap.add_argument('--max_steps', type=int, default=4000)
    ap.add_argument('--cases', type=str, required=True, help='semicolon list of "cin|a1,y1,s1|a2,y2,s2|..."')
    ap.add_argument('--out', type=str, default='runs/scan_eps0_signed.json')
    ap.add_argument('--savefields', type=str, default='')
    ap.add_argument('--rmap', type=str, default='r', choices=['r', 'r2'])
    args = ap.parse_args()
    dev = 'cuda'
    b = Basis(args.Nt, 5, args.K, args.Nphi, ng_coll=args.ngc, m_reg=2, device=dev, grade=args.grade)
    res = CharResidual(b, args.L, args.beta_basis, Nphi_res=args.Nphi_res, r_in=args.r_in, dt=args.dt, device=dev,
                       max_steps=args.max_steps, rmap=args.rmap)
    g0 = res.g; K, Nb = b.K, b.Nb
    Dt = ((1 - b.t_coll_t) ** g0.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1)
    wfit = 1.0 / Dt
    act = g0.active
    def fitG(vals):
        c = torch.zeros(K * Nb, dtype=DT, device=dev)
        c[act] = torch.linalg.lstsq((g0.Phi0G * wfit[:, None])[:, act], (vals * wfit)[:, None], driver='gels').solution[:, 0]
        return c
    wG = res.wG
    PG = torch.linalg.pinv((res.gres.Phi0G * wG[:, None])[:, act], rtol=1e-12)
    results = []
    for case in args.cases.split(';'):
        parts = case.split('|')
        lobes = []
        Gt = torch.zeros_like(g0.x)
        for lb in parts[1:]:
            a_i, y_i, s_i = [float(v) for v in lb.split(',')]
            lobes.append(dict(a=a_i, y0=y_i, s=s_i))
            Gt = Gt + a_i * torch.exp(-(g0.x ** 2 + (g0.y - y_i) ** 2) / (2 * s_i ** 2))
        cfit = fitG(Gt)
        c_unit = (g0.c_op @ cfit).item()
        if parts[0].startswith('A='):
            A = float(parts[0][2:]); c_in = A * c_unit
        else:
            c_in = float(parts[0]); A = c_in / c_unit
        cG_ext = A * cfit
        fit_err = ((g0.Phi0G @ cfit - Gt) * wfit).abs().max().item()
        Gext_vals = A * Gt
        res.eps = 0.0; res.cG_ext = cG_ext
        t0 = time.time()
        R, info = res.run(torch.zeros(1, K * Nb, dtype=DT, device=dev), return_all=True)
        torch.cuda.synchronize(); dtm = time.time() - t0
        beta = info['beta'].item()
        Gch = info['G_char'][0]; Fch = info['F_char'][0]
        cGfit = torch.zeros(K * Nb, dtype=DT, device=dev); cGfit[act] = PG @ (wG * Gch)
        c_out = (g0.c_op @ cGfit).item()
        Gfit_err = (wG * (res.gres.Phi0G @ cGfit - Gch)).abs().max().item()
        x = res.X0[:, 0]; y = res.X0[:, 1]; rr = torch.sqrt(x ** 2 + y ** 2)
        Om = x * Gch
        wgt = x * y * Om / rr ** 4
        pos = wgt[y > 0].sum().item(); neg = wgt[y < 0].sum().item()
        negfrac = (Gch < 0).double().mean().item()
        # radii where Omega_char is negative (sign change location): report min over points of G and its (r, y) location
        imin = int(torch.argmin(Gch)); imax = int(torch.argmax(Gch))
        r = dict(case=case, lobes=lobes, A=A, c_unit=c_unit, c_in=c_in, beta=beta, c_out=c_out, ratio=c_out / c_in,
                 G0_char=Gch[:res.bres.Nphi].mean().item(), G0_target=4 / beta, maxF=Fch.max().item(), minF=Fch.min().item(),
                 Omega_max=Om.max().item(), Omega_min=Om.min().item(), G_min=Gch.min().item(), G_min_at=(rr[imin].item(), y[imin].item()),
                 G_max=Gch.max().item(), G_max_at=(rr[imax].item(), y[imax].item()), negfrac_G=negfrac,
                 Gext_min=Gext_vals.min().item(), Gext_max=Gext_vals.max().item(),
                 unfinished=res.n_unfinished, steps=res.steps_used,
                 fit_err_ext=fit_err, Gfit_err=Gfit_err, RF_fit=info['RF'][0].abs().max().item(), time=dtm,
                 xyOm_r4_sum_pos=pos, xyOm_r4_sum_neg=neg)
        results.append(r)
        print(json.dumps(r), flush=True)
        if args.savefields:
            np.savez(args.savefields + f"_{len(results)}.npz", x=x.cpu().numpy(), y=y.cpu().numpy(), F=Fch.cpu().numpy(),
                     G=Gch.cpu().numpy(), T=info['T'][0].cpu().numpy(), cG_ext=cG_ext.cpu().numpy(), cGfit=cGfit.cpu().numpy(),
                     cF=info['cF'][0].cpu().numpy(), beta=beta, c_in=c_in, c_out=c_out)
    json.dump(dict(args=vars(args), results=results), open(args.out, 'w'), indent=1)

if __name__ == '__main__':
    main()

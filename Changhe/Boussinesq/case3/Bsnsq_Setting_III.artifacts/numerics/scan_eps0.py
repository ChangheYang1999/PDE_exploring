"""eps = 0 scan: for external vorticity fields Omega_ext = A x exp(-(x^2+(y-y0)^2)/(2 s^2)) (+ optional tail),
compute W_ext (canonical inverse), beta = 2(c_ext - 1), transport Theta and Omega by characteristics from the centre jet,
and report the strain c_out of the transported vorticity versus c_in = c_ext. A fixed point of B2-P needs c_out = c_in."""
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
    ap.add_argument('--cases', type=str, required=True, help='semicolon list of "cin,y0,s" (A chosen for c_in) or "A=..,y0,s"')
    ap.add_argument('--out', type=str, default='runs/scan_eps0.json')
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
        parts = case.split(',')
        y0, sg = float(parts[1]), float(parts[2])
        Gt = torch.exp(-(g0.x ** 2 + (g0.y - y0) ** 2) / (2 * sg ** 2))
        cfit = fitG(Gt)
        c_unit = (g0.c_op @ cfit).item()
        if parts[0].startswith('A='):
            A = float(parts[0][2:]); c_in = A * c_unit
        else:
            c_in = float(parts[0]); A = c_in / c_unit
        cG_ext = A * cfit
        fit_err = ((g0.Phi0G @ cfit - Gt) * wfit).abs().max().item()
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
        # direct quadrature of c_out on the residual grid is not available (Gauss weights); use the fitted operator.
        # diagnostics: where is Omega_char concentrated; fraction of y>0 weight in xy Omega/r^4
        wgt = x * y * Om / rr ** 4
        pos = wgt[y > 0].sum().item(); neg = wgt[y < 0].sum().item()
        r = dict(case=case, A=A, y0=y0, s=sg, c_in=c_in, beta=beta, c_out=c_out, ratio=c_out / c_in,
                 G0_char=Gch[:res.bres.Nphi].mean().item(), G0_target=4 / beta, maxF=Fch.max().item(), minF=Fch.min().item(),
                 Omega_max=Om.max().item(), Omega_min=Om.min().item(), unfinished=res.n_unfinished, steps=res.steps_used,
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

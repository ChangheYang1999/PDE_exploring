"""SVD of a stored dense Jacobian of the hybrid Psi system in two norms (node-value coordinates with c_l per 1/400, as built;
and the SPEC S3 (a) norms: domain grid-L2 of delta H, rows relative), the smallest 20 singular values, counts below thresholds,
and for the softest k right vectors the S3 (c) diagnostics (c_l and C components, radial shells, 10-degree sectors, near-P
fraction, sign changes on r = 5 and theta = 45 deg, streamline alignment) plus the accurate-residual response |dF/ds| along each
(central differences, s = 0.05 in the unscaled unit-vector normalization) with d h(P)/ds, d ident/ds.
Usage: python3 src/svd_report.py runs/J_<tag>.pt tag [k=8] [Npsi=480] [--no-response]"""
import sys, os, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, charmap as cm, jtools as jt

LANE = jt.LANE


def main():
    args = [a_ for a_ in sys.argv[1:] if not a_.startswith('--')]; resp = '--no-response' not in sys.argv
    jpath, tag = args[0], args[1]; k = int(args[2]) if len(args) > 2 else 8; Npsi = int(args[3]) if len(args) > 3 else 480
    J, z, model, ch, D = jt.load_J(jpath, Npsi); n = J.shape[0]; N, M = model.N, model.M
    b, cl, C = ch.unpack(z); clf = float(cl)
    Fz = lambda zz: ch.F(zz, **jt.RES_KW)
    F = Fz(z); nF = F.norm().item()
    out = dict(tag=tag, jpath=jpath, n=n, N=N, M=M, beta=model.beta, L=model.L, Npsi_res=Npsi, c_l=clf, C=float(C), F2=nF, Finf=float(F.abs().max()), hP1=float(F[-2]), ident=float(F[-1]))
    out['stationarity_JtF'] = float((J.T @ F).norm() / (J.norm() * F.norm()))
    print(f'{tag}: n {n} |F|_2 {nF:.3e} |F|_inf {out["Finf"]:.3e} h(P)-1 {out["hP1"]:+.3e} ident {out["ident"]:+.3e} c_l {clf:.10f}; |J^T F|/(|J||F|) {out["stationarity_JtF"]:.3e}', flush=True)
    scale = torch.ones(n, device='cuda'); scale[-2] = 1.0 / 400.0
    Dcol, Drow, Wgt = jt.s3_scalings(model, b, clf, float(C))
    res = {}
    for name, Js in (('node_cl400', J * scale[None, :]), ('S3norm', Drow[:, None] * J * Dcol[None, :])):
        t0 = time.time(); S = torch.linalg.svdvals(Js).cpu().numpy()
        res[name] = dict(smax=float(S[0]), smallest20=[float(s) for s in S[-20:][::-1]],
                         counts={f'<{t:g}': int((S < t).sum()) for t in (1e-8, 1e-6, 1e-4, 1e-3, 1e-2)},
                         counts_rel={f'<{t:g}*smax': int((S < t * S[0]).sum()) for t in (1e-12, 1e-11, 1e-10, 1e-8)}, svd_time=time.time() - t0)
        print(f'  [{name}] smax {S[0]:.4e}; smallest {" ".join("%.3e" % s for s in S[-12:][::-1])}; counts {res[name]["counts"]} rel {res[name]["counts_rel"]}', flush=True)
        sk, Vk = jt.soft_vectors(Js, k)
        dg = jt.Diag(model, ch, b, clf, float(C)); soft = []
        for i in range(k):
            vs = Vk[:, i]
            v = (scale * vs) if name == 'node_cl400' else (Dcol * vs)        # back to unscaled coordinates
            v = v / v.norm()
            d_ = dict(i=i, sigma=float(sk[i])); d_.update(dg.report(v))
            if resp:
                # central differences at two amplitudes: along strongly curved soft directions the cubic term (s^2/6) F''' contaminates
                # the response at s = 0.05 (about 6e-4 at (120,48)); s = 1e-3 resolves first-order actions down to about 1e-7
                for s_ in (1e-4, 1e-3):
                    dF = (Fz(z + s_ * v) - Fz(z - s_ * v)) / (2 * s_)
                    d_[f'dF_ds_{s_:g}'] = float(dF.norm()); d_[f'dF_minus_Jv_{s_:g}'] = float((dF - J @ v).norm())
                d_['dF_ds'] = d_['dF_ds_0.0001']; d_['dhP_ds'] = float(dF[-2]); d_['dident_ds'] = float(dF[-1]); d_['Jv_norm'] = float((J @ v).norm()); d_['dF_minus_Jv'] = d_['dF_minus_Jv_0.0001']
            soft.append(d_)
            print(f'    v{i}: sigma {d_["sigma"]:.3e} dc_l {d_["dcl"]:+.2e} dC {d_["dC"]:+.2e} radial {dict((kk, round(vv, 3)) for kk, vv in d_["radial"].items())} ang>80 {sum(d_["angular10"][8:]):.2f} nearP {d_["nearP_fraction"]:.2f} sc(r5,th45) {d_["sign_changes_r5"]},{d_["sign_changes_th45"]} align {d_["streamline_alignment"]:.3f}' + (f' | |dF/ds| (s 1e-4, 1e-3) {d_["dF_ds_0.0001"]:.3e} {d_["dF_ds_0.001"]:.3e} |Jv| {d_["Jv_norm"]:.3e} |dF-Jv| {d_["dF_minus_Jv_0.0001"]:.2e} {d_["dF_minus_Jv_0.001"]:.2e} dhP {d_["dhP_ds"]:+.1e} dident {d_["dident_ds"]:+.1e}' if resp else ''), flush=True)
        res[name]['soft'] = soft
        Vun = Vk * (scale[:, None] if name == 'node_cl400' else Dcol[:, None]); Vun = Vun / Vun.norm(dim=0, keepdim=True)
        torch.save(dict(Vsoft_unscaled=Vun.cpu(), ssoft=sk.cpu(), norm=name), f'{LANE}/runs/{tag}_softvecs_{name}.pt')
    out['svd'] = res
    json.dump(out, open(f'{LANE}/runs/svd_{tag}.json', 'w'), indent=1); print('saved', f'runs/svd_{tag}.json')


if __name__ == '__main__':
    main()

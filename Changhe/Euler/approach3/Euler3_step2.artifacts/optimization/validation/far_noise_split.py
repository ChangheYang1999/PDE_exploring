#!/usr/bin/env python
"""D6FP far-anchor noise split (lead note 2026-10-28T22:17Z item 3): for coefficient columns whose far-anchor-block derivative is tiny, split the
finite-difference noise of the far rows (the 3 anchor radii 4096, 16384, 65536 R0) into the pressure-gradient contribution and the rest, with the
AD derivative of each part as reference; and the discrete l = 0, 1 moments M^disc of the pressure source and of the derivative source relative to
int s^(l+2) |f_lm| ds (hypothesis: moment rounding amplified by about r^(2 alpha - 1) at the far anchors). Writes validation/far_noise_split_<tag>.json."""
import sys, os, time, json, math, argparse
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, PAIRS, ROOT
from src.optimization.lm import jacobian_fwd
from src.equations import residuals as res


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--tag", required=True); ap.add_argument("--cases", default="S01_own,manu_a"); ap.add_argument("--ncols", type=int, default=6)
    a = ap.parse_args(); dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
    defs = {"S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")), "manu_a": dict(pair=PAIRS["a"], seed=3), "S05_own": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt"))}
    out = dict(tag=a.tag, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), cases={})
    for cname in a.cases.split(","):
        case = Case(cname, dev, **defs[cname]); prob, model = case.prob, case.model
        zo = case.z_opt; n = zo.numel(); Nr, Na = model.Nr, model.Na; nsrc = model.Nr_src
        far_rows = torch.cat([torch.arange(c * Nr * Na + nsrc * Na, c * Nr * Na + Nr * Na, device=dev) for c in range(3)])
        # production Jacobian J_cw; far-block norms of all coefficient columns
        fun = lambda q: prob.residual_vector_wd(case.to_full_opt(q))
        J = jacobian_fwd(fun, zo, chunk=256)
        far_norm = J[far_rows, :].norm(dim=0); whole = J.norm(dim=0)
        cand = [k for k in range(n - 2) if float(whole[k]) > 1e-4]
        cand.sort(key=lambda k: float(far_norm[k]))
        sel = cand[: a.ncols]
        rep = dict(pair=case.pair, selected_columns=sel, far_block_norms={k: float(far_norm[k]) for k in sel}, whole_norms={k: float(whole[k]) for k in sel},
                   far_block_norm_median=float(far_norm[:n - 2].median()), n_far_rows=int(far_rows.numel()))
        del J
        # parts: weighted far rows of grad P and of the rest, as functions of z (weights frozen at the base: the split concerns evaluation noise)
        wn = (prob.w_node[:, None] * prob.w_ang[None, :]).sqrt()
        def parts(q):
            zz = case.to_full_opt(q); tabs = prob.pressure_tables_at(zz)
            F = model.fields_grid(zz, need_vort=False); src = res.pressure_source(F["GU"])
            P, gradP, _, _ = prob.pressure.solve(src, tables=tabs["main"])
            aT, aS, c_l, omega = model.unpack(zz)
            sc = prob.scale_mom(c_l)
            if prob.nl_w_mom is not None:
                sc = sc * prob.nl_w_mom.sqrt()
            W = (wn * sc[:, None])[None]
            from src.equations.linear_stable import linear_velocity
            lin = linear_velocity(model, zz) + torch.einsum('m...,mi...->i...', F["U"], F["GU"])
            gp = (gradP * W).reshape(-1)[far_rows]; rest = (lin * W).reshape(-1)[far_rows]
            return torch.cat([gp, rest])
        base = parts(zo); m = far_rows.numel()
        col_results = {}
        for k in sel:
            e = torch.zeros_like(zo); e[k] = 1.0
            ad = torch.func.jvp(parts, (zo,), (e,))[1]
            r_k = dict(ad_norm_gradP=float(ad[:m].norm()), ad_norm_rest=float(ad[m:].norm()), ladder={})
            for h in (1e-3, 1e-4, 1e-5):
                d = (parts(zo + h * e) - parts(zo - h * e)) / (2 * h)
                r_k["ladder"][f"{h:.0e}"] = dict(err_gradP=float((d[:m] - ad[:m]).norm()), err_rest=float((d[m:] - ad[m:]).norm()),
                                              rel_err_gradP=float((d[:m] - ad[:m]).norm() / max(float(ad[:m].norm()), 1e-300)), rel_err_rest=float((d[m:] - ad[m:]).norm() / max(float(ad[m:].norm()), 1e-300)),
                                              noise_estimate_gradP_per_h=float((d[:m] - ad[:m]).norm() * h), noise_estimate_rest_per_h=float((d[m:] - ad[m:]).norm() * h))
            col_results[k] = r_k
            print(f"  {cname} col {k}: far-block |J| {float(far_norm[k]):.2e} (gradP part {r_k['ad_norm_gradP']:.2e}, rest {r_k['ad_norm_rest']:.2e}); FD-AD abs errors by h: " +
                  ", ".join(f"{h}: gradP {v['err_gradP']:.1e} rest {v['err_rest']:.1e}" for h, v in r_k["ladder"].items()), flush=True)
        rep["columns"] = col_results
        # discrete moments of the source and of the derivative source (c_l direction) at the quadrature points
        ps = prob.pressure; T = ps.tables
        zz = case.to_full_opt(zo)
        def src_of(q):
            F = model.fields_grid(case.to_full_opt(q), need_vort=False); return res.pressure_source(F["GU"])
        f0 = src_of(zo); e = torch.zeros_like(zo); e[n - 2] = 1.0
        fp = torch.func.jvp(src_of, (zo,), (e,))[1]
        mom = {}
        for name, f in (("source", f0), ("d_source/dz_c", fp)):
            flm = ps.analyze(f); ftw = ps.to_twisted_frame(flm) * T["sfac"][:, None] * ps.lfac      # factored smooth source at the nodes (Nr_src, Nqp)
            Phi = ps.q["Phi"]; sg = ps.q["s2"].sqrt(); w = ps.q["w"]; logss = ps.q["logss"]
            fq = Phi @ ftw                                                                          # (Nq_pts, Nqp) factored values at the quadrature points
            mm = {}
            for l in (0, 1):
                idx = [i for i, (ll, m_, t) in enumerate(ps.pmodes) if ll == l]
                for i in idx:
                    le = float(ps.le_l[l]); fac = torch.exp(-T["p0"] * logss + le * (torch.log(sg) - torch.log((sg ** 2 + ps.R0 ** 2).sqrt())))   # (s/R0)^-p0 (r/s)^le
                    integrand = fq[:, i] * fac * sg ** (l + 2) * w
                    M = float(integrand.sum()); A = float(integrand.abs().sum())
                    mm[str(ps.pmodes[i])] = dict(M_disc=M, int_abs=A, ratio=M / max(A, 1e-300))
            mom[name] = mm
        rep["discrete_moments_l0_l1"] = mom
        alpha = (1 - case.pair[0]) / case.pair[0]
        rep["amplification_estimate_r_pow_2alpha_minus_1_at_65536R0"] = (65536.0) ** (2 * alpha - 1)
        print(f"  {cname} moments: " + json.dumps({k: {q: f"{v['ratio']:.1e}" for q, v in mm.items()} for k, mm in mom.items()}), flush=True)
        out["cases"][cname] = rep
        json.dump(out, open(os.path.join(ROOT, "validation", f"far_noise_split_{a.tag}.json"), "w"), indent=1, default=str)
        del case; torch.cuda.empty_cache()
    print("FAR NOISE SPLIT DONE")


if __name__ == "__main__":
    main()

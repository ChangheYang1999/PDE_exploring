"""S12 (lead 2026-10-25T11:27Z, registered before data; d93) implementation tests.
K1: the squares of the S12 rows sum to w times the radial-lambda part of the weighted squared momentum residual (the part along lambda_k U on every
    training sphere), computed independently from the residual tensors, to 1e-12 relative; with w = 0 the rows are absent and the residual vector is unchanged.
K2: the row Jacobian (forward-mode, as the LM uses it) agrees with central differences to 1e-6 relative on a small L2 problem.
K3: the radial-lambda share of nest6 (0.45, 1) p0 on the training grid is printed beside the theory route's export-sample values (share 0.727, pointwise 0.846;
    different sample sets, so no tight assertion; the share must lie in (0, 1) and the negative-pairing fraction below 0.05)."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
ROOT = os.path.join(os.path.dirname(__file__), "..")

def run(device=None):
    device = device or ("cuda:0" if torch.cuda.is_available() else "cpu")
    ok = True
    # K1/K2 on a small L2 problem (random coefficients)
    model = Model(L=2, Nk=8, m_parity="even", R0=0.5, Nr=24, c_l=0.45, omega=0.7, device=device)
    g = torch.Generator(device="cpu").manual_seed(3)
    z = (0.3 * torch.randn(model.n_z, generator=g, dtype=torch.float64)).to(device)
    for w in (0.0, 3.0):
        prob = Problem(model, formulation="mom", radial_lambda_w=w)
        rv = prob.residual_vector(z)
        n_mom = prob.n_pde_residuals(); n_gauge = prob.gauge_residuals(*model.unpack(z), F=prob.evaluate(z)['F'], z=z).numel()
        n_rows = rv.numel() - n_mom - n_gauge
        if w == 0.0:
            okw = (n_rows == 0); print(f"K1 w = 0: no extra rows ({n_rows}): {'PASS' if okw else 'FAIL'}"); ok = ok and okw; continue
        ev = prob.evaluate(z); aT, aS, c_l, om = model.unpack(z)
        rows = prob.radial_lambda_rows(ev, c_l)
        # independent radial-lambda part: for each node, project R_u onto U in the angular L2 (weights w_ang) and take the weighted squared norm
        U = ev['F']['U']; R = ev['R_u']; wa = prob.w_ang
        sc = prob.scale_mom(c_l); q = prob.w_node * sc ** 2
        part = 0.0
        for k in range(model.Nr):
            a = float(((U[:, k, :] * R[:, k, :]).sum(0) * wa).sum()); b = float(((U[:, k, :] ** 2).sum(0) * wa).sum())
            lam = a / b; proj = lam * U[:, k, :]
            part += float(q[k]) * float(((proj ** 2).sum(0) * wa).sum())
        ssq = float((rows ** 2).sum())
        e1 = abs(ssq - w * part) / max(w * part, 1e-300)
        okw = (n_rows == model.Nr) and e1 < 1e-12
        print(f"K1 w = {w:g}: {n_rows} rows (= Nr {model.Nr}); sum of squares {ssq:.12e} vs w x radial-lambda part {w * part:.12e} (rel {e1:.1e}): {'PASS' if okw else 'FAIL'}")
        ok = ok and okw
        # K2 Jacobian of the rows: forward-mode (torch.func.jvp as the LM) against central differences
        def rows_of(zz):
            ev_ = prob.evaluate(zz); return prob.radial_lambda_rows(ev_, model.unpack(zz)[2])
        v = torch.randn(model.n_z, generator=g, dtype=torch.float64).to(device); v = v / v.norm()
        _, jv = torch.func.jvp(rows_of, (z,), (v,))
        errs = []
        for h in (1e-4, 1e-5):
            fd = (rows_of(z + h * v) - rows_of(z - h * v)) / (2 * h)
            errs.append(float((fd - jv).norm() / jv.norm().clamp_min(1e-300)))
        ok2 = min(errs) < 1e-6
        print(f"K2 row Jacobian (JVP vs central differences, h 1e-4 / 1e-5): {errs[0]:.1e} / {errs[1]:.1e}: {'PASS' if ok2 else 'FAIL'}")
        ok = ok and ok2
    # K3 share on nest6 (0.45, 1) p0
    zf = "runs/nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0/starts/start_000.pt"
    S = torch.load(os.path.join(ROOT, zf), map_location="cpu", weights_only=False); cfg = S["config"]; z6 = S["z"].to(device)
    m6 = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg["R0"], Nr=cfg["Nr"], c_l=cfg["c_l"], omega=cfg["omega"], channels=cfg.get("channels"), device=device,
               extra_r=cfg.get("far_radii") if cfg.get("far_merged", True) else None)
    p6 = Problem(m6, formulation="mom", nl_weighting=True)
    d = p6.radial_lambda_diagnostics(z6)
    ok3 = 0.0 < d["radial_lambda_share"] < 1.0 and d["negative_pairing_fraction"] < 0.05
    print(f"K3 nest6 (0.45, 1) p0 training grid (unweighted nl): radial-lambda share {d['radial_lambda_share']:.3f} (theory route on export samples 0.727), pointwise along-U share {d['pointwise_along_U_share']:.3f} (0.846), "
          f"lambda max {d['lambda_max']:.3f} at r {d['r_at_lambda_max']:.3g}, negative-pairing fraction {d['negative_pairing_fraction']:.2e}, octaves with lambda < 0: {d['n_octaves_negative']} of {len(d['lambda_by_octave'])}: {'PASS' if ok3 else 'FAIL'}")
    print("  lambda by octave of r/R0: " + " ".join(f"{k}:{v:+.3f}" for k, v in d["lambda_by_octave"].items()))
    ok = ok and ok3
    print("test_S12_radial_rows:", "PASS" if ok else "FAIL")
    return ok

if __name__ == "__main__":
    sys.exit(0 if run() else 1)

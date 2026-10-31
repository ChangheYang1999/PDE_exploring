#!/usr/bin/env python
"""SPEC 10 candidate exchange: candidates/<id>/ with meta.json, BASIS.md, coeffs.npz, samples.npz (U Cartesian, DU, P, grad P on
the exchange tensor grid r = 2^(j/4) r_core, j = -24..80, theta max(32, 3L/2+1) Gauss-Legendre, phi max(64, 3L+1) uniform;
random points: 65536 uniform on S^2 at radii drawn from the same 105 exchange radii (the Green pressure is evaluated per
radius), seed recorded; axis points theta = 0, pi at the grid radii and y = 0), sha256 of every file.
Usage: export_candidate.py <start_xxx.pt> <candidate_id> [--r_core R] [--device cuda:0]"""
import sys, os, json, argparse, math, hashlib, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model, alpha_of
from src.pressure.poisson_sh import PressureSolver
from src.equations import residuals as res
from src.bases.solid_harmonics import eval_solid

ap = argparse.ArgumentParser(); ap.add_argument("zfile"); ap.add_argument("cid"); ap.add_argument("--r_core", type=float, default=None)
ap.add_argument("--device", default="cuda:0" if torch.cuda.is_available() else "cpu"); ap.add_argument("--seed", type=int, default=20261024)
ap.add_argument("--note", default=None, help="extra note stored in meta.json (e.g. the state's provenance and caveats)")
ap.add_argument("--Nr_src", type=int, default=None, help="radial source nodes of the pressure solver (default max(Nr_train, 3 Nk)); lead 2026-10-25T19:34Z: 6 Nk removes the spurious source monopole of the 3 Nk interpolant (about 1.5x the pressure cost)")
ap.add_argument("--extra_src_factor", type=int, default=0, help="also store P and grad P from a second pressure solve with this many x Nk source nodes (arrays *_src<K>Nk in samples.npz; its M0/M1 in meta.json)")
ap.add_argument("--d2u", default="auto", help="second derivatives D2U_grid[n, m, i] = d_n d_m U_i on the exchange grid by forward-mode AD of DU with respect to the point (lead 2026-10-25T04:33Z item 3): auto (on when L_ext <= 10), on, off")
a = ap.parse_args()
S = torch.load(a.zfile, map_location="cpu", weights_only=False); cfg = S["config"]; z = S["z"].to(a.device)
c_l, om = (float(z[-2]), float(z[-1])) if S.get("free_params") else (cfg["c_l"], cfg["omega"])
L = cfg["L"]
train = Model(L=L, Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=(a.Nr_src or max(cfg.get("Nr") or 0, 3 * cfg["Nk"])),
              c_l=c_l, omega=om, free_params=S.get("free_params", False), channels=cfg.get("channels"), device=a.device)
r_core = a.r_core or ((S.get("spec_diag_holdout") or S.get("spec_diag") or {}).get("guards", {}) or {}).get("N4_r_core") or train.R0
radii = r_core * 2.0 ** (np.arange(-24, 81) / 4.0)
nth, nph = max(32, 3 * L // 2 + 1), max(64, 3 * L + 1)
ex = Model(L=L, Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), r_nodes=radii, ntheta=nth, nphi=nph,
           c_l=c_l, omega=om, free_params=S.get("free_params", False), channels=cfg.get("channels"), device=a.device)
out = os.path.join(ROOT, "candidates", a.cid); os.makedirs(out, exist_ok=True)
t0 = time.time()
F = ex.fields_grid(z, need_vort=True)
ps = PressureSolver(train, p0=2 * alpha_of(c_l) + 2, omega=om, c_l=c_l, eval_model=ex)
f_src = res.pressure_source(train.fields_grid(z, need_vort=False)["GU"])
P, gradP, Plm, dPlm = ps.solve(f_src)
def source_moments(ps_, train_, f_):
    """Monopole M0 = int f dy of the interpolated source (solver volume integral, the quantity that produces the outer-sphere grad P difference
    -M0 n/(4 pi r^2); lead d127) and the first moment M1_i = int y_i f dy as in scripts/pressure_source_moments.py (finite-ball part over the quadrature
    points s <= r_last plus the exterior part with the factored source frozen at x = 1; NOT volume_integral(f y))."""
    with torch.no_grad():
        M0 = float(ps_.volume_integral(f_))
        q = ps_._quad; sg, wsg, Phi, logss = q["s"], q["w"], q["Phi"], q["logss"]; r_last = q["r_last"]
        fn = (f_[: ps_.Nr_src] * ps_.sfac[:, None]).cpu().numpy(); fq = (Phi @ fn) * np.exp(-ps_.p0 * logss)[:, None]
        wa = train_.grid.w.cpu().numpy(); nn_ = train_.n.cpu().numpy(); fin = sg <= r_last + 1e-12
        def integ(g, mask):
            return float(((g[mask] * (sg[mask] ** 2 * wsg[mask])[:, None]) * wa[None, :]).sum())
        M1f = [integ(fq * (sg[:, None] * nn_[None, :, i]), fin) for i in range(3)]; M1e = [integ(fq * (sg[:, None] * nn_[None, :, i]), ~fin) for i in range(3)]
        M0q = dict(finite=integ(fq, fin), exterior=integ(fq, ~fin))
    return dict(Nr_src=int(ps_.Nr_src), r_last=float(r_last), M0_solver_volume_integral=M0, M0_quadrature=dict(finite=M0q["finite"], exterior=M0q["exterior"], total=M0q["finite"] + M0q["exterior"]),
                M1_finite=M1f, M1_exterior=M1e, M1_total=[M1f[i] + M1e[i] for i in range(3)], note="exact source has M0 = 0 and M1 = 0 (lead d122); M0 of the interpolated source is the spurious monopole (-4.09e-12 at 3 Nk on nest8 (0.45, 1) p0 cont150)")
src_meta = source_moments(ps, train, f_src)
print(f"pressure source: Nr_src {src_meta['Nr_src']}, M0 {src_meta['M0_solver_volume_integral']:.3e}, M1 total {['%.3e' % v for v in src_meta['M1_total']]}")
rng = np.random.default_rng(a.seed)
n = rng.normal(size=(65536, 3)); n /= np.linalg.norm(n, axis=1)[:, None]
jr = rng.integers(0, len(radii), 65536); pts = torch.tensor(radii[jr, None] * n, dtype=torch.float64, device=a.device)
Fr = ex.fields_points(z, pts, need_vort=True)
nt = torch.tensor(n, dtype=torch.float64, device=a.device)
A0r, A1r, _ = eval_solid(nt, ps.pmodes, ps.Lf, 1)
Pr = (Plm[jr] * A0r).sum(1)
rj = torch.tensor(radii[jr], dtype=torch.float64, device=a.device)
radial = ((dPlm[jr] - ps.pl[None, :] * Plm[jr] / rj[:, None]) * A0r).sum(1)
gPr = radial[:, None] * nt + torch.einsum('pq,ipq->pi', Plm[jr] / rj[:, None], A1r)
ax = torch.tensor(np.concatenate([np.stack([np.zeros_like(radii), np.zeros_like(radii), radii], 1), np.stack([np.zeros_like(radii), np.zeros_like(radii), -radii], 1), np.zeros((1, 3))]), dtype=torch.float64, device=a.device)
Fa = ex.fields_points(z, ax, need_vort=True)
gP0 = ps.gradP_origin(f_src)
extra = {}; d2u_meta = None; src2_meta = None
if a.extra_src_factor:
    t2 = time.time(); K = a.extra_src_factor
    train2 = Model(L=L, Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=K * cfg["Nk"], c_l=c_l, omega=om, free_params=S.get("free_params", False), channels=cfg.get("channels"), device=a.device)
    ps2 = PressureSolver(train2, p0=2 * alpha_of(c_l) + 2, omega=om, c_l=c_l, eval_model=ex)
    f2 = res.pressure_source(train2.fields_grid(z, need_vort=False)["GU"])
    P2, gradP2, Plm2, dPlm2 = ps2.solve(f2)
    Pr2 = (Plm2[jr] * A0r).sum(1); radial2 = ((dPlm2[jr] - ps2.pl[None, :] * Plm2[jr] / rj[:, None]) * A0r).sum(1)
    gPr2 = radial2[:, None] * nt + torch.einsum('pq,ipq->pi', Plm2[jr] / rj[:, None], A1r); gP02 = ps2.gradP_origin(f2)
    tagK = f"_src{K}Nk"
    extra["P_grid" + tagK] = P2.cpu().numpy().reshape(len(radii), nth, nph); extra["gradP_grid" + tagK] = gradP2.permute(1, 2, 0).cpu().numpy().reshape(len(radii), nth, nph, 3)
    extra["P_rand" + tagK] = Pr2.cpu().numpy(); extra["gradP_rand" + tagK] = gPr2.cpu().numpy(); extra["gradP_origin" + tagK] = gP02.cpu().numpy()
    dg = (gradP2 - gradP); per_r = (dg.reshape(3, len(radii), -1).norm(dim=(0, 2)) / gradP.reshape(3, len(radii), -1).norm(dim=(0, 2)).clamp_min(1e-300))
    src2_meta = dict(source_moments(ps2, train2, f2), arrays=[k for k in extra if k.endswith(tagK)], seconds=round(time.time() - t2, 1),
                     gradP_difference_vs_main=dict(global_rel_L2=float(dg.norm() / gradP.norm()), P_global_rel_L2=float((P2 - P).norm() / P.norm()), per_radius_rel_L2_max=float(per_r.max()), per_radius_rel_L2_at_outermost=float(per_r[-1]),
                                                   note="relative to the local grad P norm per exchange radius; far radii carry the spurious monopole of the coarser source"))
    print(f"second pressure at {K} Nk source nodes: M0 {src2_meta['M0_solver_volume_integral']:.3e}; grad P difference vs main: global {src2_meta['gradP_difference_vs_main']['global_rel_L2']:.2e}, per-radius max {src2_meta['gradP_difference_vs_main']['per_radius_rel_L2_max']:.2e} (outermost {src2_meta['gradP_difference_vs_main']['per_radius_rel_L2_at_outermost']:.2e}); {time.time() - t2:.0f}s")
want_d2u = (a.d2u == "on") or (a.d2u == "auto" and getattr(ex, "L_ext", L) <= 10)
if want_d2u:
    def d2u_points(pts_, chunk):
        outs = []
        for s0 in range(0, pts_.shape[0], chunk):
            pp = pts_[s0:s0 + chunk]; cols = []
            for nn in range(3):
                e = torch.zeros_like(pp); e[:, nn] = 1.0
                _, jg = torch.func.jvp(lambda q: ex.fields_points(z, q, need_vort=False)["GU"], (pp,), (e,))    # (3(m), 3(i), Np): d_n d_m U_i
                cols.append(jg)
            outs.append(torch.stack(cols, 0))
        return torch.cat(outs, -1)                                                                            # (3(n), 3(m), 3(i), Np)
    tq = time.time()
    ygrid = ex.y.reshape(-1, 3)
    D2 = d2u_points(ygrid, chunk=(16384 if getattr(ex, "L_ext", L) <= 6 else 4096))
    sym = float((D2 - D2.transpose(0, 1)).abs().max() / D2.abs().max())
    # central-difference check of d_n DU at 8 random exchange points (h = 1e-5 relative to 1 + r)
    chk = pts[:8]; h = 1e-5 * (1 + chk.norm(dim=1, keepdim=True)); fd_err = 0.0
    D2c = d2u_points(chk, 8)
    for nn in range(3):
        e = torch.zeros_like(chk); e[:, nn] = 1.0
        Gp = ex.fields_points(z, chk + h * e, need_vort=False)["GU"]; Gm = ex.fields_points(z, chk - h * e, need_vort=False)["GU"]
        fd = (Gp - Gm) / (2 * h.T[0])[None, None, :]
        fd_err = max(fd_err, float((fd - D2c[nn]).abs().max() / D2c.abs().max()))
    extra["D2U_grid"] = D2.permute(3, 0, 1, 2).cpu().numpy().reshape(len(radii), nth, nph, 3, 3, 3)
    d2u_meta = dict(convention="D2U_grid[r, theta, phi, n, m, i] = d_n d_m U_i (forward-mode AD of DU with respect to the point)", symmetry_defect_rel=sym, central_difference_check_rel=fd_err, seconds=time.time() - tq)
    print(f"D2U on the exchange grid: symmetry defect {sym:.1e}, central-difference check {fd_err:.1e} ({time.time() - tq:.0f}s)")
np.savez_compressed(os.path.join(out, "samples.npz"), radii=radii, **extra, theta=ex.grid.theta.cpu().numpy().reshape(nth, nph)[:, 0], phi=ex.grid.phi.cpu().numpy().reshape(nth, nph)[0],
                    angular_weights=ex.grid.w.cpu().numpy().reshape(nth, nph),   # Gauss-Legendre x uniform weights summing to 4 pi (lead 23:58Z)
                    y_grid=ex.y.cpu().numpy().reshape(len(radii), nth, nph, 3), U_grid=F["U"].permute(1, 2, 0).cpu().numpy().reshape(len(radii), nth, nph, 3),
                    DU_grid=F["GU"].permute(2, 3, 0, 1).cpu().numpy().reshape(len(radii), nth, nph, 3, 3), Omega_grid=F["Om"].permute(1, 2, 0).cpu().numpy().reshape(len(radii), nth, nph, 3),
                    P_grid=P.cpu().numpy().reshape(len(radii), nth, nph), gradP_grid=gradP.permute(1, 2, 0).cpu().numpy().reshape(len(radii), nth, nph, 3),
                    y_rand=pts.cpu().numpy(), U_rand=Fr["U"].T.cpu().numpy(), DU_rand=Fr["GU"].permute(2, 0, 1).cpu().numpy(), Omega_rand=Fr["Om"].T.cpu().numpy(),
                    P_rand=Pr.cpu().numpy(), gradP_rand=gPr.cpu().numpy(), y_axis=ax.cpu().numpy(), U_axis=Fa["U"].T.cpu().numpy(), DU_axis=Fa["GU"].permute(2, 0, 1).cpu().numpy(),
                    Omega_axis=Fa["Om"].T.cpu().numpy(), gradP_origin=gP0.cpu().numpy(), random_seed=a.seed)
d = train.unpack_all(z)
np.savez_compressed(os.path.join(out, "coeffs.npz"), **{k: v.detach().cpu().numpy() for k, v in d.items() if k not in ("c_l", "omega")},
                    modes=np.array(train.modes), c_l=c_l, omega=om, R0=train.R0, L=L, Nk=cfg["Nk"], channels=json.dumps(train.channels))
basis = open(os.path.join(ROOT, "reports", "CONVENTIONS.md")).read()
open(os.path.join(out, "BASIS.md"), "w").write("# Basis definition (copy of reports/CONVENTIONS.md at export time)\n\n" + basis)
gclos = S.get("G_closure")
if (gclos is None or gclos.get("K_H_required") is None) and (train.channels.get("NkB", 0) > 0 or train.channels.get("NkD", 0) > 0):   # recompute when the stored block predates v1.24
    try:
        from src.optimization.problem import Problem
        from src.far_field.correction import closure_distance
        gclos = closure_distance(Problem(train, formulation="mom"), z)
    except Exception as e:
        gclos = dict(error=repr(e))
meta = dict(candidate_id=a.cid, G_closure=gclos, L_ext=getattr(train, "L_ext", L), channel_modes={k: [train.modes[i] for i in train.chan_cols[k].tolist()] for k in ("B", "D", "E") if train.channels.get("Nk" + k, 0) > 0}, source_start=os.path.relpath(a.zfile, ROOT), c_l=c_l, omega=om, omega_over_c_l=om / c_l, alpha=alpha_of(c_l), L_max=L, Nk=cfg["Nk"], Nr_train=cfg.get("Nr"),
            R0=train.R0, channels=train.channels, m_parity=cfg.get("m_parity", "even"), gauges=dict(dilation="int_S2 |F|^2 = 1 (exact projection applied)", phase=S.get("pivot"), pressure="decaying full space"),
            exchange_grid=dict(r_core=r_core, radii="r_core * 2^(j/4), j = -24..80", ntheta=nth, nphi=nph, random_points=65536, random_seed=a.seed), D2U=d2u_meta,
            pressure_source=src_meta, pressure_source_extra=src2_meta,
            diagnostics=dict(spec_training=(S.get("spec_diag") or {}).get("global_"), spec_holdout=(S.get("spec_diag_holdout") or {}).get("global_"), nonaxi=(S.get("spec_diag") or {}).get("nonaxi"),
                             critical=S.get("critical"), strength=S.get("strength"), tier_S=S.get("tier_S"), status=S.get("status")),
            software=dict(torch=torch.__version__, numpy=np.__version__, python=sys.version.split()[0]), exported=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            note="an approximate state, not an exact profile; see diagnostics", note_extra=a.note)
json.dump(meta, open(os.path.join(out, "meta.json"), "w"), indent=1, default=str)
man = {fn: hashlib.sha256(open(os.path.join(out, fn), "rb").read()).hexdigest() for fn in ["samples.npz", "coeffs.npz", "BASIS.md", "meta.json"]}
json.dump(man, open(os.path.join(out, "SHA256.json"), "w"), indent=1)
print(f"exported {a.cid} in {time.time()-t0:.0f}s: {out} ({sum(os.path.getsize(os.path.join(out, f)) for f in os.listdir(out))/2**20:.1f} MB)")

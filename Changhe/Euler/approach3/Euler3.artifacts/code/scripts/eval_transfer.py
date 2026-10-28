"""Evaluate an independent-route (verifier) SPEC 10 exchange export with the primary lane's diagnostics.

Part A: momentum five-term split directly from the exported samples (their U, DU, grad P on their 105 thin spheres).
        Nothing of the primary basis enters; this checks the exported numbers themselves. DU[i,j] = d_j U_i (their convention).
Part B: re-evaluate their vector-potential basis (BASIS.md) with torch autograd, check it against their random samples,
        fit the primary basis to that field (fit_field), and run the primary SPEC diagnostics (training and holdout grids,
        primary full-space pressure). Labelled "transferred": the fit error bounds what the residual numbers can mean.
Usage: eval_transfer.py EXPORT_DIR OUT_JSON [--device cuda:0] [--L 6 --Nk 16 --Nr 48]
"""
import sys, os, json, math, time, argparse
import numpy as np, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.equations.fields import Model, DT
from src.equations import residuals as res
from src.optimization.problem import Problem
from src.optimization.transfer import fit_field
from src.optimization.tail_constraints import TailConstraints
from src.validation.spec_diagnostics import spec_diagnostics, five_term_split
from src.validation.holdout import HoldoutGrid
from src.pressure.poisson_sh import PressureSolver
from src.equations.fields import alpha_of

ap = argparse.ArgumentParser()
ap.add_argument("export_dir"); ap.add_argument("out_json")
ap.add_argument("--device", default="cuda:0"); ap.add_argument("--L", type=int, default=6); ap.add_argument("--Nk", type=int, default=16)
ap.add_argument("--Nr", type=int, default=48); ap.add_argument("--NkB", type=int, default=4); ap.add_argument("--NkD", type=int, default=4); ap.add_argument("--NkE", type=int, default=4)
ap.add_argument("--levels", default=None, help="comma list L:Nk:Nr, e.g. 6:16:48,8:20:60,10:24:72 (overrides --L/--Nk/--Nr)")
ap.add_argument("--tail_constraints", action="store_true", help="fit in the tail-constrained coordinates (SPEC 11c N1: tail constraints kept)")
ap.add_argument("--source_rho_u", type=float, default=None, help="the source route's holdout rho_u^max for the N1 ratio")
args = ap.parse_args()
dev = args.device
t0 = time.time()
E = args.export_dir
meta = json.load(open(os.path.join(E, "meta.json")))
S = np.load(os.path.join(E, "samples.npz")); C = np.load(os.path.join(E, "coeffs.npz"))
c_l, omega, R0 = float(meta["c_l"]), float(meta["omega"]), float(meta["R0"])
alpha = alpha_of(c_l)
out = dict(export=E, c_l=c_l, omega=omega, R0=R0, state=meta.get("state"), basis_version=meta.get("basis_version"), utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))

# ---------------- Part A: split from the exported samples ----------------
y = torch.tensor(S["y_grid"], dtype=DT)            # (105, 32, 64, 3)
U = torch.tensor(S["U_grid"], dtype=DT).movedim(-1, 0)          # (3, 105, 32, 64)
DU = torch.tensor(S["DU_grid"], dtype=DT)          # (..., i, j) = d_j U_i
GU = DU.permute(4, 3, 0, 1, 2)                     # GU[m, i] = d_m U_i
gP = torch.tensor(S["gradP_grid"], dtype=DT).movedim(-1, 0)
wang = torch.tensor(S["angular_weights"], dtype=DT); wang = wang / wang.sum()
radii = S["radii"]
F = dict(U=U, GU=GU, c_l=c_l, omega=omega, y=y)
T = five_term_split(F, gP); Ru = sum(T)
def sph_rms(X):  # (3, 105, 32, 64) -> (105,)
    return ((X ** 2).sum(0) * wang[None]).sum((1, 2)).sqrt()
rmsT = [sph_rms(t) for t in T]; rmsRu = sph_rms(Ru); den5 = sum(rmsT)
rho_sph = (rmsRu / den5).numpy(); rho_nl_sph = (rmsRu / (rmsT[3] + rmsT[4])).numpy()
maxRu = Ru.norm(dim=0).amax((1, 2)); pi_sph = (maxRu / den5).numpy()
# dyadic shells (volume weights r^3 for log-spaced thin spheres) and a core ball r < R0
edges = [0.0, R0] + [R0 * 2.0 ** k for k in range(1, 40) if R0 * 2.0 ** (k - 1) < radii.max()]
shells = []
for a, b in zip(edges[:-1], edges[1:]):
    m = (radii >= a) & (radii < b)
    if m.sum() == 0: continue
    w = radii[m] ** 3; w = w / w.sum()
    num = math.sqrt(float((rmsRu.numpy()[m] ** 2 * w).sum())); den = sum(math.sqrt(float((rt.numpy()[m] ** 2 * w).sum())) for rt in rmsT)
    dnl = sum(math.sqrt(float((rt.numpy()[m] ** 2 * w).sum())) for rt in rmsT[3:])
    shells.append(dict(r_lo=a, r_hi=b, n_spheres=int(m.sum()), rho_u=num / den, rho_nl=num / dnl, pi_u=float(maxRu.numpy()[m].max()) / den))
divU = res.divergence(GU); rel_div = (sph_rms(divU[None]) / sph_rms(GU.reshape(9, *GU.shape[2:]))).numpy()
out["partA_samples"] = dict(
    description="five-term momentum split from the exported U, DU, grad P on the 105 exported thin spheres (their pressure); "
                "rho_u per sphere = RMS(R_u)/sum_i RMS(T_i); dyadic shells weight spheres by r^3",
    rho_u_max_sphere=float(rho_sph.max()), rho_u_argmax_r=float(radii[rho_sph.argmax()]), rho_u_median_sphere=float(np.median(rho_sph)),
    rho_nl_max_sphere=float(rho_nl_sph.max()), pi_u_max_sphere=float(pi_sph.max()),
    rho_u_max_dyadic=max(s["rho_u"] for s in shells), rho_nl_max_dyadic=max(s["rho_nl"] for s in shells), shells=shells,
    rel_divergence_max_sphere=float(rel_div.max()),
    per_sphere=dict(r=radii.tolist(), rho_u=rho_sph.tolist(), rho_nl=rho_nl_sph.tolist(),
                    rms_terms=[t.numpy().tolist() for t in rmsT], rms_Ru=rmsRu.numpy().tolist()))
print(f"[A] rho_u max over spheres {rho_sph.max():.4e} at r={radii[rho_sph.argmax()]:.4g}; dyadic max {out['partA_samples']['rho_u_max_dyadic']:.4e}; rho_nl max {rho_nl_sph.max():.3e}; rel div max {rel_div.max():.2e}", flush=True)

# ---------------- Part B: re-evaluate their basis, fit the primary basis, primary diagnostics ----------------
coef = torch.tensor(C["coefficients"], dtype=DT, device=dev); comp = torch.tensor(C["components"], device=dev)
pw = torch.tensor(C["powers"], dtype=DT, device=dev); nidx = torch.tensor(C["radial_indices"], device=dev)
twisted = (nidx <= 2)
expo = torch.tensor([0.0, 1.0, (alpha + 1) / 2, (4 - alpha) / 2, (5 - alpha) / 2], dtype=DT, device=dev)[nidx]   # (R0^2/q)^expo
ej = torch.zeros(len(coef), 3, dtype=DT, device=dev); ej[torch.arange(len(coef)), comp] = 1.0

def Apot(yy):   # yy (3,) -> vector potential (3,)
    q = (yy ** 2).sum() + R0 ** 2
    psi = omega / (2 * c_l) * torch.log(q / R0 ** 2)
    cpsi, spsi = torch.cos(psi), torch.sin(psi)
    yn = yy / q.sqrt()
    zt = torch.stack([cpsi * yn[0] - spsi * yn[1], spsi * yn[0] + cpsi * yn[1], yn[2]])      # Q(psi) y / sqrt q
    zu = yn
    Z = torch.where(twisted[:, None], zt[None, :], zu[None, :])                               # (nrow, 3)
    mono = (Z ** pw).prod(-1)                                                                  # z1^a z2^b z3^c (0^0 = 1)
    scal = coef * q ** ((1 - alpha) / 2) * mono * (R0 ** 2 / q) ** expo
    # direction: twisted rows Q(-psi) e_j, untwisted rows e_j
    ejr = torch.stack([cpsi * ej[:, 0] + spsi * ej[:, 1], -spsi * ej[:, 0] + cpsi * ej[:, 1], ej[:, 2]], dim=1)
    vec = torch.where(twisted[:, None], ejr, ej)
    return (scal[:, None] * vec).sum(0)

def curlA(yy):
    DA = torch.func.jacrev(Apot)(yy)       # DA[i, j] = d_j A_i
    return torch.stack([DA[2, 1] - DA[1, 2], DA[0, 2] - DA[2, 0], DA[1, 0] - DA[0, 1]])

def their_U(pts, chunk=8192):
    pts = torch.as_tensor(pts, dtype=DT, device=dev).reshape(-1, 3)
    return torch.cat([torch.func.vmap(curlA)(pts[i:i + chunk]) for i in range(0, len(pts), chunk)])

# check my evaluation of their basis against their random samples
yr = torch.tensor(S["y_rand"][:16384], dtype=DT, device=dev); Ur = torch.tensor(S["U_rand"][:16384], dtype=DT, device=dev)
Umine = their_U(yr)
rel = ((Umine - Ur).norm(dim=1) / Ur.norm(dim=1).clamp_min(1e-300))
out["partB_basis_check"] = dict(n_points=int(len(yr)), max_rel_err=float(rel.max()), median_rel_err=float(rel.median()),
                                note="their BASIS.md evaluated independently with torch autograd curl, against their U_rand samples")
print(f"[B] basis re-evaluation vs U_rand: max rel {rel.max():.2e} median {rel.median():.2e}", flush=True)
# leading tail: replace q by |y|^2, keep n=0 only -> gauge norm check at a large radius: integral_S2 |F|^2 (F = r^alpha U at r -> inf)
results = []
levels = [(args.L, args.Nk, args.Nr)] if not args.levels else [tuple(int(v) for v in t.split(":")) for t in args.levels.split(",")]
for (L, Nk, Nr) in levels:
    t1 = time.time()
    model = Model(L=L, Nk=Nk, m_parity="even", R0=R0, Nr=Nr, device=dev, c_l=c_l, omega=omega,
                  channels=dict(NkB=args.NkB, NkD=args.NkD, NkE=args.NkE))
    z0 = torch.zeros(model.n_coef, dtype=DT, device=dev)
    Fg = model.fields_grid(z0, need_vort=False)
    ygrid = Fg["y"]                               # (Nr, Na, 3)
    Ut = their_U(ygrid.reshape(-1, 3)).reshape(*ygrid.shape[:-1], 3).movedim(-1, 0)   # (3, Nr, Na)
    tc = TailConstraints(model) if args.tail_constraints else None
    z, info = fit_field(model, Ut, expand=(tc.expand if tc else None), n_red=(tc.n_red if tc else None))
    info["tail_constraints"] = bool(tc is not None)
    # independent fit error on their random points (unweighted relative L2 and weighted by (1+r^2/R0^2)^(alpha/2))
    yr_all = torch.tensor(S["y_rand"], dtype=DT, device=dev); Ur_all = torch.tensor(S["U_rand"], dtype=DT, device=dev)
    Ufit = model.fields_points(z, yr_all, need_vort=False)["U"]
    Ufit = Ufit.movedim(0, -1) if Ufit.shape[0] == 3 and Ufit.shape[-1] != 3 else Ufit
    sc = (1 + (yr_all ** 2).sum(-1) / R0 ** 2) ** (alpha / 2)
    rel_fit_rand = float(((Ufit - Ur_all) * sc[:, None]).norm() / (Ur_all * sc[:, None]).norm())
    rel_fit_rand_core = float(((Ufit - Ur_all)[(yr_all.norm(dim=1) < 4 * R0)]).norm() / Ur_all[(yr_all.norm(dim=1) < 4 * R0)].norm())
    print(f"[B] L={L} Nk={Nk}: fit on model grid rel {info['rel_fit_residual']:.3e} (cond {info['cond_est']:.1e}); on their random points scaled rel {rel_fit_rand:.3e}, core (r<4R0) rel {rel_fit_rand_core:.3e}", flush=True)
    prob = Problem(model, formulation="mom", pressure=PressureSolver(model, p0=2 * alpha + 2, omega=omega, c_l=c_l))
    sd = spec_diagnostics(prob, z)
    hg = HoldoutGrid(model, r_core=R0)
    sdh = spec_diagnostics(prob, z, holdout=hg)
    g, gh = sd["global_"], sdh["global_"]
    rnl = sdh.get("rho_nl") or []; edges = getattr(hg, "edges", None)
    inner = [v for v, e in zip(rnl, edges) if v is not None and e[1] <= 4.0] if edges is not None and len(edges) == len(rnl) else None
    rho_nl_inner = max(inner) if inner else None
    n1 = (gh['rho_u_max'] / args.source_rho_u) if (args.source_rho_u and gh.get('rho_u_max') is not None) else None
    print(f"[B] primary diagnostics (transferred, fit error above): training rho_u_max {g['rho_u_max']:.4e} rho_nl_max {g['rho_nl_max']:.3e}; holdout rho_u_max {gh['rho_u_max']:.4e} rho_nl_max {gh['rho_nl_max']:.3e} (shells r_hi <= 4: {rho_nl_inner}) rho_Om_max {gh.get('rho_Om_max')}; N1 ratio to source {n1}; level time {time.time()-t1:.0f}s", flush=True)
    results.append(dict(L=L, Nk=Nk, Nr=Nr, channels=dict(NkB=args.NkB, NkD=args.NkD, NkE=args.NkE), fit=info, rel_fit_rand_scaled=rel_fit_rand, rel_fit_rand_core=rel_fit_rand_core,
                        training_global=g, holdout_global=gh, holdout_rho_u_per_shell=sdh.get("rho_u"), holdout_rho_nl_per_shell=rnl, holdout_edges=edges,
                        holdout_rho_nl_max_inner_r4=rho_nl_inner, N1_ratio_to_source=n1, source_rho_u=args.source_rho_u, level_seconds=time.time() - t1,
                        nonaxi=sdh.get("nonaxi"), guards=sdh.get("guards"), label="transferred (fit of the primary basis to the independent field; not the independent state itself)"))
    cfg_out = dict(L=L, Nk=Nk, Nr=Nr, R0=R0, c_l=c_l, omega=omega, m_parity="even", channels=dict(NkB=args.NkB, NkD=args.NkD, NkE=args.NkE), formulation="mom",
                   tail_constraints=bool(tc is not None), free_params=False)
    # same layout as a worker start file, so scripts/enqueue_continuation.py --src can warm start from it (label transferred)
    torch.save(dict(z=z.cpu(), config=cfg_out, cfg=cfg_out, free_params=False, spec_diag_holdout=sdh, spec_diag=sd, source=E,
                    label="transferred", meta=dict(family="transferred", source=E, fit=info, rel_fit_rand_scaled=rel_fit_rand)),
               args.out_json.replace(".json", f"_L{L}_Nk{Nk}.pt"))
out["partB_transferred"] = results
out["elapsed_s"] = time.time() - t0
def clean(o):
    if isinstance(o, dict): return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [clean(v) for v in o]
    if isinstance(o, (np.floating, np.integer)): return o.item()
    if isinstance(o, torch.Tensor): return o.tolist()
    if isinstance(o, float) and (math.isnan(o) or math.isinf(o)): return None
    return o
json.dump(clean(out), open(args.out_json, "w"), indent=1)
print("wrote", args.out_json, f"elapsed {time.time()-t0:.0f}s", flush=True)

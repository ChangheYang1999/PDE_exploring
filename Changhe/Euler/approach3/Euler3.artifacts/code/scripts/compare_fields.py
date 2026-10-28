#!/usr/bin/env python
"""SPEC 7.10 gauge-aligned field comparison of two saved states (Stage III single-change re-solves, cross-route transfers).

For two states with the same c_l and omega (possibly different L, Nk, channels or R0), both in the F-gauge int_S2 |F|^2 = 1,
the rotation phase about e_3 is aligned by minimizing the comparison norm over the rotation angle b (the rotation is applied
exactly on the coefficients of the second state: it is a symmetry of the equations, Problem.phase_align convention), and
    ||V||_*   = max over shells of RMS_k(U_ref - U_b) / RMS_k(U_ref),
    ||V||_*,1 = the same with DU and with Omega in place of U (both reported, and their maximum),
over the SPEC 7.1 shells (core ball and dyadic shells from R0_ref 2^-5 to the outermost node of the reference state) plus the far
checkpoints (single spheres at the --far radii, in units of R0_ref). U_ref is the FIRST state (SPEC 7.10: the finer state).
Every shell value is printed (RMS of the difference, RMS of the reference, ratio); a near-zero reference RMS is flagged.
Both fields are evaluated on the same fresh grid (Gauss-Legendre radii per shell, rotated azimuth phi0 = pi/(2 nphi), ntheta =
2 L_ext + 12, nphi = 4 L_ext + 18 with L_ext the larger of the two): none of these points is a training node of either state.
Usage: CUDA_VISIBLE_DEVICES=-1 OMP_NUM_THREADS=4 .venv/bin/python scripts/compare_fields.py REF.pt OTHER.pt [--json out.json]
         [--far 4096,16384,65536] [--n_per_shell 6] [--coarse 72] [--no_align] [--device cpu]"""
import sys, os, json, math, argparse, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model, DT
from src.validation.holdout import holdout_radii

ap = argparse.ArgumentParser()
ap.add_argument("ref"); ap.add_argument("other")
ap.add_argument("--json", default=None); ap.add_argument("--far", default="4096,16384,65536")
ap.add_argument("--n_per_shell", type=int, default=6); ap.add_argument("--coarse", type=int, default=72)
ap.add_argument("--no_align", action="store_true"); ap.add_argument("--device", default="cpu")
ap.add_argument("--basins", type=int, default=3, help="number of coarse-grid local minima refined by golden section (the best is kept)")
ap.add_argument("--no_gauge", action="store_true", help="skip the F-gauge check (which builds a Problem for each state)")
a = ap.parse_args()
dev = a.device
t0 = time.time()


def load(path):
    S = torch.load(path, map_location="cpu", weights_only=False)
    cfg = dict(S["config"])
    return S, cfg


def eval_model(cfg, r_nodes, ntheta, nphi, phi0):
    return Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), r_nodes=r_nodes,
                 ntheta=ntheta, nphi=nphi, c_l=cfg["c_l"], omega=cfg["omega"], free_params=False, channels=cfg.get("channels"),
                 device=dev, phi0=phi0)


def rot_z(model, z, gamma):
    """Rotate the state about e_3 by the angle gamma (exact symmetry; the Problem.phase_align convention):
    cos-mode a_c' = a_c cos(m gamma) + a_s sin(m gamma), sin-mode a_s' = -a_c sin(m gamma) + a_s cos(m gamma)."""
    d = model.unpack_all(z)
    m = model.m_arr.to(z.dtype)
    cm, sm = torch.cos(m * gamma), torch.sin(m * gamma)
    sign = model.tw_sign; partner = model.partner
    def rot(arr):
        return arr * cm[None, :] + sign[None, :] * arr[:, partner] * sm[None, :]
    extra = {k: rot(d[k]) for k in ("B", "D", "E") if d[k].numel() > 0}
    return model.pack(rot(d["A"]), rot(d["C"]), d["c_l"], d["omega"], extra=extra)


S1, c1 = load(a.ref); S2, c2 = load(a.other)
z1 = S1["z"].to(dev); z2 = S2["z"].to(dev)
if S1.get("free_params") or S2.get("free_params"):
    # free-parameter states carry (c_l, omega) at the end of z; the fixed-parameter evaluation model uses the saved values
    for S, c, zz in ((S1, c1, z1), (S2, c2, z2)):
        if S.get("free_params"):
            c["c_l"], c["omega"] = float(zz[-2]), float(zz[-1])
    z1 = z1[: -2] if S1.get("free_params") else z1; z2 = z2[: -2] if S2.get("free_params") else z2
same_params = abs(c1["c_l"] - c2["c_l"]) < 1e-12 and abs(c1["omega"] - c2["omega"]) < 1e-12
R0 = float(c1.get("R0", 1.0))
# reference training radii (to size the shells like the worker's holdout: r_core = R0, r_max = outermost node)
m_train = Model(L=c1["L"], Nk=c1["Nk"], m_parity=c1.get("m_parity", "even"), R0=R0, Nr=c1.get("Nr"), c_l=c1["c_l"], omega=c1["omega"],
                channels=c1.get("channels"), device="cpu", extra_r=(c1.get("far_radii") if c1.get("far_merged", True) else None))
r_max = float(m_train.r.max())
edges, r, wv, sid = holdout_radii(R0, r_max, a.n_per_shell)
labels = [f"[{lo:.4g},{hi:.4g})" for (lo, hi) in edges]
far = [float(v) for v in a.far.split(",")] if a.far else []
for k, fr in enumerate(far):
    r = np.concatenate([r, [fr * R0]]); wv = np.concatenate([wv, [1.0]]); sid = np.concatenate([sid, [len(edges) + k]]); labels.append(f"far {fr:g} R0")
n_shells = len(labels)
def lext(cfg):
    """Effective maximum angular degree of a configuration (the Model's L_ext rule: a channel degree counts only when its Nk > 0)."""
    ch = dict(NkB=0, NkD=0, NkE=0, LB=None, LD=None, LE=None); ch.update(cfg.get("channels") or {})
    L = cfg["L"]
    return max(L, ch["LB"] if (ch["LB"] is not None and ch["NkB"] > 0) else L, ch["LD"] if (ch["LD"] is not None and ch["NkD"] > 0) else L,
               ch["LE"] if (ch["LE"] is not None and ch["NkE"] > 0) else L)


Lx = max(lext(c1), lext(c2))
ntheta, nphi = 2 * Lx + 12, 4 * Lx + 18
phi0 = math.pi / (2 * nphi)
M1 = eval_model(c1, r, ntheta, nphi, phi0); M2 = eval_model(c2, r, ntheta, nphi, phi0)
w_ang = (M1.grid.w / (4 * math.pi)).to(dev)
w_vol = torch.tensor(wv, dtype=DT, device=dev); shell = torch.tensor(sid, dtype=torch.long, device=dev)
masks = [shell == k for k in range(n_shells)]


def shell_rms(X):
    """X: (3, Nr, Na) or (3, 3, Nr, Na): RMS over each shell (volume-normalized Gauss weights x angular weights)."""
    sq = (X ** 2).sum(tuple(range(X.dim() - 2)))
    per_node = (sq * w_ang[None, :]).sum(1)
    return torch.stack([((per_node[m] * w_vol[m]).sum() / w_vol[m].sum()).sqrt() for m in masks])


with torch.no_grad():
    F1 = M1.fields_grid(z1, need_vort=True)
    ref = dict(U=shell_rms(F1["U"]), DU=shell_rms(F1["GU"]), Om=shell_rms(F1["Om"]))

    def norms(gamma, full=False):
        zz = rot_z(M2, z2, torch.tensor(gamma, dtype=DT, device=dev)) if gamma != 0.0 else z2
        F2 = M2.fields_grid(zz, need_vort=full)
        dU = shell_rms(F1["U"] - F2["U"]) / ref["U"].clamp_min(1e-300)
        if not full:
            return dU.max().item(), dU
        dDU = shell_rms(F1["GU"] - F2["GU"]) / ref["DU"].clamp_min(1e-300)
        dOm = shell_rms(F1["Om"] - F2["Om"]) / ref["Om"].clamp_min(1e-300)
        return dU, dDU, dOm, shell_rms(F1["U"] - F2["U"]), shell_rms(F1["GU"] - F2["GU"]), shell_rms(F1["Om"] - F2["Om"])

    # rotation period: 2 pi / gcd of the azimuthal orders present in the second state (pi for the even class)
    ms = sorted(set(int(v) for v in M2.m_arr.tolist() if int(v) > 0))
    g = 0
    for v in ms:
        g = math.gcd(g, v)
    period = 2 * math.pi / g if g > 0 else 0.0
    gamma_best, f_best, trace, basins = 0.0, None, [], []
    if a.no_align or period == 0.0:
        f_best = norms(0.0)[0]
    else:
        gs = np.linspace(0.0, period, a.coarse, endpoint=False)
        vals = []
        for gg in gs:
            f, _ = norms(float(gg)); vals.append(f); trace.append((float(gg), f))
        vals = np.asarray(vals)
        # every local minimum of the coarse values (cyclic) is a candidate basin; the best --basins of them are refined by golden section
        # (astra referee 2026-10-26T10:2xZ: a single bracket can pick a near-degenerate wrong basin; the result stays an estimated minimum)
        n = len(gs)
        cand = [i for i in range(n) if vals[i] <= vals[(i - 1) % n] and vals[i] <= vals[(i + 1) % n]]
        cand = sorted(cand, key=lambda i: vals[i])[: max(1, a.basins)]
        phi = (math.sqrt(5) - 1) / 2
        for i in cand:
            lo, hi = gs[i] - period / n, gs[i] + period / n
            x1 = hi - phi * (hi - lo); x2 = lo + phi * (hi - lo)
            f1, _ = norms(float(x1)); f2, _ = norms(float(x2))
            for _ in range(40):
                if f1 < f2:
                    hi, x2, f2 = x2, x1, f1; x1 = hi - phi * (hi - lo); f1, _ = norms(float(x1))
                else:
                    lo, x1, f1 = x1, x2, f2; x2 = lo + phi * (hi - lo); f2, _ = norms(float(x2))
                if hi - lo < 1e-10:
                    break
            xb, fb = (x1, f1) if f1 < f2 else (x2, f2)
            if vals[i] < fb:
                xb, fb = float(gs[i]), float(vals[i])
            basins.append((float(xb % period), float(fb)))
        basins.sort(key=lambda t: t[1])
        gamma_best, f_best = basins[0]
    dU, dDU, dOm, aU, aDU, aOm = norms(gamma_best, full=True)

star = dU.max().item(); star1_DU = dDU.max().item(); star1_Om = dOm.max().item()
flag_small = [i for i in range(n_shells) if ref["U"][i].item() < 1e-6 * ref["U"].max().item()]
flag_small_DU = [i for i in range(n_shells) if ref["DU"][i].item() < 1e-6 * ref["DU"].max().item()]
flag_small_Om = [i for i in range(n_shells) if ref["Om"][i].item() < 1e-6 * ref["Om"].max().item()]
finite = all(math.isfinite(v) for v in (star, star1_DU, star1_Om))
b_phys = -gamma_best    # the coefficient map P(., phi) -> P(., phi + gamma) realizes the field rotation U_gamma(y) = R_{-gamma} U(R_gamma y): physical angle b = -gamma
print(f"compare_fields: ref {a.ref}\n                other {a.other}")
print(f"  c_l {c1['c_l']} / {c2['c_l']}, omega {c1['omega']} / {c2['omega']} (same parameters: {same_params}); R0 {R0} / {c2.get('R0', 1.0)}; "
      f"L {c1['L']} / {c2['L']}, Nk {c1['Nk']} / {c2['Nk']}; grid {len(r)} radii x {ntheta} x {nphi} angles; shells {n_shells} (incl. {len(far)} far spheres)")
print(f"  domains: the worker's holdout shells (core ball below R0_ref 2^-5 rounded down to a dyadic radius, dyadic shells to the outermost node of the reference) plus single spheres at the far anchor radii in units of R0_ref; not the literal SPEC 7.1 r_core / thin-shell definition")
print(f"  rotation alignment: period {period:.6f} (gcd of m = {g}), coefficient angle gamma* = {gamma_best:.9f} rad = physical rotation b = {b_phys:.9f} rad ({'not aligned' if a.no_align else 'minimizing ||U_ref - U_b||_*'}); {len(trace)} coarse values, refined basins {[(round(x, 6), float('%.4e' % f)) for x, f in basins]} (estimated minimum)")
print(f"  ||V||_* (U) = {star:.4e}; ||V||_*,1: DU {star1_DU:.4e}, Omega {star1_Om:.4e} (max {max(star1_DU, star1_Om):.4e}){'' if finite else '  NON-FINITE VALUE: unevaluated'}")
if flag_small_DU or flag_small_Om:
    print(f"  flagged near-zero reference RMS: DU shells {flag_small_DU}, Omega shells {flag_small_Om}")
print("  shell | RMS U_ref | RMS dU | ratio | RMS DU_ref | ratio | RMS Om_ref | ratio")
for i in range(n_shells):
    fl = " (reference RMS near zero: flagged)" if i in flag_small else ""
    print(f"  {labels[i]:>22} | {ref['U'][i].item():.3e} | {aU[i].item():.3e} | {dU[i].item():.3e} | {ref['DU'][i].item():.3e} | {dDU[i].item():.3e} | {ref['Om'][i].item():.3e} | {dOm[i].item():.3e}{fl}")
out = dict(ref=a.ref, other=a.other, c_l=[c1["c_l"], c2["c_l"]], omega=[c1["omega"], c2["omega"]], same_params=same_params, R0=[R0, c2.get("R0", 1.0)],
           L=[c1["L"], c2["L"]], Nk=[c1["Nk"], c2["Nk"]], grid=dict(n_r=int(len(r)), ntheta=ntheta, nphi=nphi, phi0=phi0, n_per_shell=a.n_per_shell, far=far),
           shells=labels, rotation=dict(period=period, gcd_m=g, gamma=gamma_best, physical_angle_b=b_phys, aligned=not a.no_align, basins=basins, coarse_trace=trace), finite=finite,
           domains="worker holdout shells (r_core = R0_ref, dyadic) plus far anchor spheres (units of R0_ref); not the literal SPEC 7.1 r_core / thin-shell definition",
           norm_star_U=star, norm_star1_DU=star1_DU, norm_star1_Om=star1_Om, norm_star1=max(star1_DU, star1_Om),
           per_shell=dict(rms_U_ref=ref["U"].tolist(), rms_dU=aU.tolist(), ratio_U=dU.tolist(), rms_DU_ref=ref["DU"].tolist(), rms_dDU=aDU.tolist(), ratio_DU=dDU.tolist(),
                          rms_Om_ref=ref["Om"].tolist(), rms_dOm=aOm.tolist(), ratio_Om=dOm.tolist()),
           flagged_shells=flag_small, flagged_shells_DU=flag_small_DU, flagged_shells_Om=flag_small_Om, definition="worker-grid aligned field difference: ||V||_* = max_k RMS_k(U_ref - U_b)/RMS_k(U_ref) over the worker holdout shells (R0-based dyadic) and far spheres, b minimizing it; ||.||_*,1 with DU and Omega; U_ref = the first state; the SPEC 7.10 v1 formula on a PROXY domain, NOT a SPEC 7.10 distance on the SPEC 7.1 domains (lead IX, 2026-10-26)"
           "||.||_*,1 with DU and Omega; U_ref = the first state", seconds=None)
if not a.no_gauge:
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("worker", os.path.join(ROOT, "scripts", "worker.py")); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W)
        gauges = []
        for S, c, zz in ((S1, c1, z1), (S2, c2, z2)):
            cfg = dict(c)
            for k in ("core_pin", "nonaxi_pin", "balance_lambda", "radial_lambda_w", "fsw", "efrac", "nu", "pin_c_l"):
                cfg.pop(k, None)
            cfg["closure_lambda"] = 0.0; cfg["free_params"] = False
            model, prob = W.build(cfg, "cpu")
            with torch.no_grad():
                aT, aS, _, _ = model.unpack(zz.cpu().clone())
                n2 = float(prob.tail_norm2(aT, aS, torch.tensor(cfg["c_l"]), torch.tensor(cfg["omega"])))
            gauges.append(n2)
        out["F_norm2"] = gauges; out["F_gauge_within_1e-3"] = bool(all(abs(v - 1.0) <= 1e-3 for v in gauges))
        print(f"  F-gauge int|F|^2: ref {gauges[0]:.6f}, other {gauges[1]:.6f} (both should be 1 in the F-gauge){'' if out['F_gauge_within_1e-3'] else '  WARNING: a gauge value is off by more than 1e-3; the comparison is not gauge-aligned'}")
    except Exception as e:
        out["F_norm2_error"] = repr(e); print(f"  F-gauge check failed: {e!r}")
out["seconds"] = time.time() - t0
print(f"  {out['seconds']:.1f} s")
if a.json:
    json.dump(out, open(a.json, "w"), indent=1); print("wrote", a.json)

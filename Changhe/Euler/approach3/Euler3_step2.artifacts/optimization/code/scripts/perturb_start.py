#!/usr/bin/env python
"""Recorded-seed nearby start for the Stage III R1 replication (PROMPT III.3; lead stage3 plan R1): a Gaussian coefficient perturbation
of the A/C (velocity potential) coefficients in the tail-constrained reduced coordinates, PROJECTED onto the kernel of the leading-tail
map z -> (t_q, s_q) (Problem.tail_amplitudes), so that the leading tail F, the SPEC 6.1 F-gauge int|F|^2 = 1 and the SPEC 6.2 phase
pivot are unchanged exactly (to rounding) and the tail-moment constraints hold; B/D/E (carried far channels) are untouched. The
perturbation is scaled by ONE factor so that ||U_pert - U|| / ||U|| = SIZE in the training-grid quadrature norm (node weights w_node x
angular weights w_ang of the worker's Problem; U is linear in z, so the factor is exact); the same ratio on the worker holdout grid is
recorded for information. No velocity scaling and no second gauge. CPU only; the output is a START (unevaluated), never a reading.
Usage: perturb_start.py SRC.pt --out DST.pt --size 1e-2 --seed 31001 [--job JOB.json]"""
import sys, os, json, math, argparse, time, hashlib
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "scripts"))
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model, DT
from src.optimization.tail_constraints import TailConstraints
from src.validation.holdout import HoldoutGrid
import worker as W

ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("--out", required=True); ap.add_argument("--size", type=float, required=True)
ap.add_argument("--seed", type=int, required=True); ap.add_argument("--job", default=None, help="job JSON whose config builds the Problem (default: the source's config)")
ap.add_argument("--m_select", choices=["all", "odd", "even"], default="all", help="restrict the perturbed A/C coordinates to columns with odd (or even) azimuthal m (Stage III R3: odd-m perturbation in the all-m embedding of an even source; lead IE S3-6)")
a = ap.parse_args(); t0 = time.time()
S = torch.load(a.src, map_location="cpu", weights_only=False)
cfg = dict(json.load(open(a.job))["config"]) if a.job else dict(S["config"])
model, prob = W.build(cfg, "cpu")
if not cfg.get("tail_constraints", False):
    raise SystemExit("perturb_start.py expects a tail-constrained configuration (every production job of Stage II)")
if bool(cfg.get("free_params", False)) or bool(getattr(model, "free_params", False)) or bool(S.get("free_params", False)):
    raise SystemExit("REFUSED: free-parameter model or job (lead S3-15); perturb_start.py serves fixed-parameter starts only")
tc = TailConstraints(model, nu=float(cfg.get("nu", 0.0) or 0.0))
scfg = S["config"]
embedded = False
if (scfg.get("m_parity", "even"), scfg["L"], scfg["Nk"], scfg.get("channels")) != (cfg.get("m_parity", "even"), cfg["L"], cfg["Nk"], cfg.get("channels")):
    from src.optimization.transfer import embed_state
    msrc = Model(L=scfg["L"], Nk=scfg["Nk"], m_parity=scfg.get("m_parity", "even"), R0=scfg.get("R0", 1.0), Nr=scfg.get("Nr"), c_l=scfg["c_l"], omega=scfg["omega"],
                 free_params=S.get("free_params", False), channels=scfg.get("channels"), device="cpu")
    z = embed_state(S["z"].clone(), msrc, model); embedded = True                                  # exact embedding (e.g. even source into the all-m basis; odd coefficients 0)
else:
    z = S["z"].clone()
assert z.numel() == model.n_z if hasattr(model, "n_z") else True
zr0 = tc.reduce(z)
nA = tc.red_sizes["A"] * tc.ncols["A"]; nC = tc.red_sizes["C"] * tc.ncols["C"]; nAC = nA + nC          # reduced layout: A, C first
def tails(zr):
    aT, aS, c_l, omega = model.unpack(tc.expand(zr))
    t, s = prob.tail_amplitudes(aT, aS, c_l)
    return torch.cat([t, s])
M_full = torch.autograd.functional.jacobian(tails, zr0, vectorize=True)                                 # (2 Nq, n_red), linear map
M = M_full[:, :nAC]                                                                                        # S3-15: the leading-tail map restricted to the A/C reduced columns (B/D/E never enter)
bde_cols_nonzero = float(M_full[:, nAC:].abs().max()) if M_full.shape[1] > nAC else 0.0                    # recorded: the B/D/E columns of the tail map (expected 0)
g = torch.Generator().manual_seed(int(a.seed))
dAC = torch.randn(nAC, generator=g, dtype=DT)
if a.m_select != "all":                                                                                    # keep only the columns with the selected parity of m (A block then C block, k-major)
    mA = model.m_arr if tc.ncols["A"] == model.Nq else model.m_arr[tc.cols["A"]]; mC = model.m_arr if tc.ncols["C"] == model.Nq else model.m_arr[tc.cols["C"]]
    want = (lambda mm: (mm % 2 == 1)) if a.m_select == "odd" else (lambda mm: (mm % 2 == 0))
    maskA = want(mA.long()).repeat(tc.red_sizes["A"]); maskC = want(mC.long()).repeat(tc.red_sizes["C"])
    mask = torch.cat([maskA, maskC]).to(torch.bool); assert mask.numel() == nAC
    dAC = dAC * mask.to(DT); n_selected = int(mask.sum())
else:
    n_selected = nAC
MdAC = M @ dAC
rn = M.norm(dim=1); keep = rn > 0
Ms = M[keep] / rn[keep][:, None]                                                                           # row-scaled map (rows differ by R0^(alpha + l) factors)
Us, Ss, Vh = torch.linalg.svd(Ms, full_matrices=False)
rk = int((Ss > 1e-11 * Ss[0]).sum())
corr = Vh[:rk].T @ ((Us[:, :rk].T @ (Ms @ dAC)) / Ss[:rk])                                                 # minimum-norm correction with Ms corr = Ms dAC
dzr = torch.zeros_like(zr0); dzr[:nAC] = dAC
dzr_p = torch.zeros_like(zr0); dzr_p[:nAC] = dAC - corr
Md = MdAC
proj_res = float((M @ dzr_p[:nAC]).norm() / max(float(Md.norm()), 1e-300))
svd_info = dict(rows=int(Ms.shape[0]), rank=rk, s_max=float(Ss[0]), s_min_kept=float(Ss[rk - 1]), s_next=(float(Ss[rk]) if rk < Ss.numel() else 0.0))
with torch.no_grad():
    dz = tc.expand(dzr_p) - tc.expand(torch.zeros_like(dzr_p))                                           # exact if expand is linear; the difference removes any offset
    wn = (prob.w_node[:, None] * prob.w_ang[None, :])
    def wnorm(U):   # U (3, Nr, Na) on the training grid (extra far nodes included as in the worker)
        return float(((U ** 2).sum(0) * wn).sum().sqrt())
    U0 = model.fields_grid(z, need_vort=False)["U"]; Ud = model.fields_grid(dz, need_vort=False)["U"]
    sfac = a.size * wnorm(U0) / wnorm(Ud)
    z_new = z + sfac * dz
    U1 = model.fields_grid(z_new, need_vort=False)["U"]
    rel_train = wnorm(U1 - U0) / wnorm(U0)
    hg = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6)))
    Uh0 = hg.model.fields_grid(z, need_vort=False)["U"]; Uh1 = hg.model.fields_grid(z_new, need_vort=False)["U"]
    rel_hold = float((Uh1 - Uh0).norm() / Uh0.norm())
    aT0, aS0, c_l0, om0 = model.unpack(z); aT1, aS1, _, _ = model.unpack(z_new)
    t0_, s0_ = prob.tail_amplitudes(aT0, aS0, c_l0); t1_, s1_ = prob.tail_amplitudes(aT1, aS1, c_l0)
    tail_change = float(max((t1_ - t0_).abs().max(), (s1_ - s0_).abs().max()))
    F0 = float(prob.tail_norm2(aT0, aS0, c_l0, om0)); F1 = float(prob.tail_norm2(aT1, aS1, c_l0, om0))
    prob.pivot = prob.choose_pivot(z); piv = prob.pivot
    gd0 = prob.gauge_defects(z); gd1 = prob.gauge_defects(z_new)
    piv_new = prob.choose_pivot(z_new)
    tcres = float((tc.expand(tc.reduce(z_new)) - z_new).norm() / z_new.norm())
    maxU0 = float(U0.norm(dim=0).max()); maxU1 = float(U1.norm(dim=0).max())
rec = dict(tool="perturb_start.py", source=a.src, source_sha256=hashlib.sha256(open(a.src, "rb").read()).hexdigest(), seed=int(a.seed), size=a.size,
           norm="SIZE is measured in the training-grid quadrature L2 norm of U (w_node x w_ang, far nodes included); rel_change_holdout_grid is the UNWEIGHTED Frobenius ratio on the worker holdout grid (information only)",
           tail_map_bde_columns_max=bde_cols_nonzero, perturbed_coordinates="A/C reduced coefficients (n = %d of %d)" % (nAC, zr0.numel()),
           kernel_projection=dict(rows=int(M.shape[0]), residual_ratio=proj_res, svd=svd_info), scale_factor=sfac, rel_change_training_grid=rel_train, rel_change_holdout_grid=rel_hold,
           tail_amplitude_max_change=tail_change, F_norm2_before=F0, F_norm2_after=F1, gauge_defects_before=[float(x) for x in gd0], gauge_defects_after=[float(x) for x in gd1],
           pivot=str(piv), pivot_recomputed_on_perturbed=str(piv_new), tail_constraint_residual=tcres, maxU_before=maxU0, maxU_after=maxU1, c_l=float(c_l0), omega=float(om0), L=cfg["L"], Nk=cfg["Nk"], R0=model.R0)
# ACCEPTANCE TESTS (lead d128 HY item 3 (f)): the start is written only if every test passes; otherwise the script exits with the failed tests listed
with torch.no_grad():
    d0 = model.unpack_all(z); d1 = model.unpack_all(z_new)
    bde_change = max([float((d1[k] - d0[k]).abs().max()) if d0[k].numel() else 0.0 for k in ("B", "D", "E")])
    free_change = max(abs(float(d1["c_l"]) - float(d0["c_l"])), abs(float(d1["omega"]) - float(d0["omega"])))
    cfg_keys = ("L", "Nk", "Nr", "R0", "c_l", "omega", "channels", "tail_constraints") + (() if embedded else ("m_parity",))
    cfg_match = all(cfg.get(k) == S["config"].get(k) for k in cfg_keys) and (not S.get("free_params", False)) and (not embedded or (S["config"].get("m_parity", "even") == "even" and cfg.get("m_parity") == "all"))
    try:                                                                                                    # odd-m content of the perturbed start (field RMS fraction on the training grid)
        modd = (model.m_arr.long() % 2 == 1)
        def odd_part(zz):
            dz_ = model.unpack_all(zz); keep = modd.to(DT)[None, :]
            ex = {k: dz_[k] * keep for k in ("B", "D", "E") if dz_[k].numel()}
            return model.pack(dz_["A"] * keep, dz_["C"] * keep, dz_["c_l"], dz_["omega"], extra=ex)
        Uodd = model.fields_grid(odd_part(z_new), need_vort=False)["U"]
        odd_frac_amp = wnorm(Uodd) / wnorm(U1)
    except Exception as e:
        odd_frac_amp = repr(e)
    disc = svd_info["rows"] - svd_info["rank"]                       # discarded singular directions among the non-zero tail rows
    disc_nonzero = int(((Ss > 0) & (Ss <= 1e-11 * Ss[0])).sum())        # discarded directions with a nonzero singular value
    piv_margin = None
    try:                                                              # pivot amplitude margin: the chosen pair against the next largest pair (choose_pivot's criterion)
        aT_, aS_, c_, o_ = model.unpack(z_new); eT, eS = prob.mode_tail_energies(aT_, aS_, c_, o_)
        amps = []
        for qq, (ll, mm, tt) in enumerate(model.modes):
            if mm == 0 or tt != 0: continue
            for pot, amp in (("T", eT.sqrt()), ("S", eS.sqrt())):
                amps.append((math.hypot(amp[qq].item(), amp[qq + 1].item()), pot, qq))
        amps.sort(reverse=True); piv_margin = dict(best=amps[0], second=amps[1], ratio=(amps[0][0] / amps[1][0] if amps[1][0] > 0 else float("inf")))
    except Exception as e:
        piv_margin = repr(e)
tests = dict(free_parameters_unchanged=(free_change == 0.0), configuration_matches=bool(cfg_match), state_finite=bool(torch.isfinite(z_new).all()), bde_unchanged=(bde_change == 0.0),
             no_discarded_nonzero_singular_directions=(disc_nonzero == 0), training_size_check=(abs(rel_train / a.size - 1.0) <= 1e-8), tail_check=(tail_change <= 1e-12 and abs(F1 - F0) <= 1e-12 and abs(F0 - 1.0) <= 1e-12 and abs(F1 - 1.0) <= 1e-12),
             pivot_unchanged=(piv["pot"] == piv_new["pot"] and piv["q"] == piv_new["q"]))
rec_tests = dict(tests=tests, bde_max_change=bde_change, free_change=free_change, discarded_nonzero_singular=disc_nonzero, zero_tail_rows=int(M.shape[0]) - svd_info["rows"],
                 m_select=a.m_select, n_perturbed_coordinates=n_selected, embedded_into_job_basis=embedded, odd_m_field_fraction_amplitude=odd_frac_amp,
                 pivot_before=str(piv), pivot_after=str(piv_new), pivot_amplitude_margin=piv_margin)
if not all(tests.values()):
    print(json.dumps(dict(REFUSED=True, failed=[k for k, v in tests.items() if not v], record=rec_tests), indent=1, default=str)); sys.exit(2)
S2 = dict(S); S2["z"] = z_new.detach().clone()
if embedded:                                                                                                 # the saved config must describe the basis of the saved z (the JOB's basis)
    sc = dict(S["config"]); sc.update({k: cfg[k] for k in ("L", "Nk", "Nr", "m_parity", "channels", "R0") if k in cfg}); S2["config"] = sc; S2["embedded_from_source_config"] = dict(S["config"])
for k in ("spec_diag", "spec_diag_holdout", "two_family", "critical", "core_resolution", "G_closure", "global_balances"):
    S2.pop(k, None)
rec["acceptance"] = rec_tests
S2["meta_perturb"] = rec
os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True); torch.save(S2, a.out)
rec["out"] = a.out; rec["out_sha256"] = hashlib.sha256(open(a.out, "rb").read()).hexdigest(); rec["seconds"] = time.time() - t0
print(json.dumps(rec, indent=1))

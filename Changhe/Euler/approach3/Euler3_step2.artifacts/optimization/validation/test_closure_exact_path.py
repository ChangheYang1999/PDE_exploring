"""D6FP: the exact (jets + double-double tables) evaluation of the closure potentials vs the frozen autograd/float64 path (eval_Y) at S01 and S05:
U, GU of the leading tail on the closure sphere (r = R0, where the twist angle is 0) and off the sphere (r = 2 R0, 0.5 R0: nonzero twist),
the carried patterns V, the first-correction target G_req; timings."""
import sys, os, time, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
from src.far_field import correction as C
from src.equations.fields import alpha_of
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z; out = {}
for cname, fn in (("S01", "S01_nest6_cl0.45_om1.0_p0.pt"), ("S05", "S05_nest6_cl0.45_om0.3_p0.pt")):
    case = Case(cname, dev, start=os.path.join(ROOT, "starts", fn)); prob, model = case.prob, case.model
    aT, aS, c_l, omega = model.unpack(case.z_full); c_lf, omf = float(c_l), float(omega); alpha = alpha_of(c_lf); kappa = omf / c_lf; R0 = model.R0
    t, s = prob.tail_amplitudes(aT.detach(), aS.detach(), torch.tensor(c_lf, device=dev)); t = t.detach(); s = s.detach()
    grid = prob.closure["grid"]; n = grid.n
    rep = {}
    for rad in (1.0, 2.0, 0.5):
        y = rad * R0 * n
        (torch.cuda.synchronize() if torch.cuda.is_available() else None); t0 = time.time(); U1, G1 = C.homogeneous_velocity(y, t[:, None], s[:, None], alpha, alpha - 1.0, model.modes, model.L_ext, kappa, R0); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t1 = time.time() - t0
        t0 = time.time(); U2, G2 = C.homogeneous_velocity_exact(y, t, s, alpha, alpha - 1.0, model.modes, model.L_ext, kappa, R0); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t2 = time.time() - t0
        U1 = U1[0].detach(); G1 = G1[0].detach(); U2 = U2[0]; G2 = G2[0]
        rep[f"r={rad}R0"] = dict(rel_U=float((U1 - U2).norm() / U1.norm()), rel_GU=float((G1 - G2).norm() / G1.norm()), max_abs_U=float((U1 - U2).abs().max()), max_abs_GU=float((G1 - G2).abs().max()),
                                 t_autograd=t1, t_exact=t2)
    # carried patterns
    (torch.cuda.synchronize() if torch.cuda.is_available() else None); t0 = time.time(); V1, labels = C.carried_patterns(model, c_lf, omf, R0 * n); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t1 = time.time() - t0
    mB, mD, allm, Lmax = C.carried_mode_sets(model, None, None)
    cols = []
    if mB:
        E = torch.zeros(len(allm), len(mB), dtype=torch.float64, device=dev)
        for j, q in enumerate(mB):
            E[allm.index(q), j] = 1.0
        VB, _ = C.homogeneous_velocity_exact(R0 * n, E, None, 2 * alpha + 1, 2 * alpha, allm, Lmax, kappa, R0, need_grad=False); cols.append(VB.permute(1, 2, 0))
    if mD:
        E = torch.zeros(len(allm), len(mD), dtype=torch.float64, device=dev)
        for j, q in enumerate(mD):
            E[allm.index(q), j] = 1.0
        VD, _ = C.homogeneous_velocity_exact(R0 * n, None, E, 2 * alpha + 1, 2 * alpha, allm, Lmax, kappa, R0, need_grad=False); cols.append(VD.permute(1, 2, 0))
    (torch.cuda.synchronize() if torch.cuda.is_available() else None); t0 = time.time(); V2 = torch.cat(cols, -1) * (R0 ** (2 * alpha + 1)); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t2 = time.time() - t0
    rep["carried_patterns"] = dict(rel=float((V1 - V2).norm() / V1.norm()), max_abs=float((V1 - V2).abs().max()), t_autograd=t1, t_exact_assembly_only=t2, shape=list(V1.shape))
    # pressure gradient of the first correction: compare twisted_scalar_gradient_exact with the autograd _potential gradient for the actual qcoef
    fc = C.first_correction(prob, case.z_full)
    rep["first_correction_G_norm_autograd"] = fc["G_norm"]
    out[cname] = rep
    print(cname, json.dumps(rep, default=str), flush=True)
    del case; torch.cuda.empty_cache()
json.dump(out, open(os.path.join(ROOT, "validation", "test_closure_exact_path.json"), "w"), indent=1, default=str); print("DONE")

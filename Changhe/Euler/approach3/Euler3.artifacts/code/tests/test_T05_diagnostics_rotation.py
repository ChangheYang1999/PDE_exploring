"""SPEC 7.9 T05 for the DIAGNOSTICS (lead 02:02Z gate G1): rho_u per shell, sigma_u^max, a_max, rho_nl^max of a state and of its image under a
rotation about e_3 by an angle that is not a multiple of pi must agree to quadrature error (the holdout grid is fixed in the lab frame; the
rotated field has the same harmonic degree, so the Gauss shell averages are exact for both). The rotation acts on the coefficient pairs
(cos, sin) of every (l, m) mode as in Problem.phase_align (field rotation by gamma: c' = c cos(m gamma) + s sin(m gamma),
s' = -c sin(m gamma) + s cos(m gamma)) and on the extra channels alike."""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.validation.spec_diagnostics import spec_diagnostics
from src.validation.holdout import HoldoutGrid
from src.equations import residuals as res

def rotate_state(model, z, gamma):
    d = model.unpack_all(z); m = model.m_arr.to(z.dtype)
    cm, sm = torch.cos(m * gamma), torch.sin(m * gamma); sign = model.tw_sign; partner = model.partner
    def rot(a):
        return a * cm[None, :] + sign[None, :] * a[:, partner] * sm[None, :]
    extra = {k: rot(d[k]) for k in ("B", "D", "E") if d[k].numel() > 0}
    return model.pack(rot(d["A"]), rot(d["C"]), d["c_l"], d["omega"], extra=extra)

def run(zfile=None, device=None):
    device = device or ("cuda:0" if torch.cuda.is_available() else "cpu")
    if zfile is None:
        torch.manual_seed(11)
        model = Model(L=4, Nk=8, m_parity="even", R0=0.5, Nr=24, c_l=0.45, omega=0.7, channels=dict(NkB=2, NkD=2, NkE=2), device=device)
        z = torch.randn(model.n_z, device=device) * 0.3
    else:
        S = torch.load(zfile, map_location="cpu", weights_only=False); cfg = S["config"]; z = S["z"].to(device)
        model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"], channels=cfg.get("channels"), device=device)
    prob = Problem(model, formulation="mom")
    gamma = 0.7                                                   # not a multiple of pi
    zr = rotate_state(model, z, gamma)
    # (0) the rotation is exact on the field: U_rot(R y) = R U(y) at random points
    pts = torch.randn(40, 3, device=device) * 0.8
    c, s = math.cos(gamma), math.sin(gamma); Rm = torch.tensor([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]], dtype=torch.float64, device=device)
    U = model.fields_points(z, pts, need_vort=False)["U"]
    errs = {}
    for name, R in (("R(+gamma)", Rm), ("R(-gamma)", Rm.T)):
        Ur = model.fields_points(zr, pts @ R.T, need_vort=False)["U"]          # U_rot(R y) against R U(y)
        errs[name] = ((Ur - R @ U).norm() / U.norm()).item()
    e_field = min(errs.values()); conv = min(errs, key=errs.get)
    print(f"field covariance: the coefficient rotation by gamma = {gamma} equals the field rotation {conv} (relative errors {errs['R(+gamma)']:.2e} / {errs['R(-gamma)']:.2e})")
    assert e_field < 1e-12, errs
    hg = HoldoutGrid(model, r_core=model.R0)
    d0 = spec_diagnostics(prob, z, holdout=hg, extras=False); d1 = spec_diagnostics(prob, zr, holdout=hg, extras=False)
    def rel(a, b):
        return abs(a - b) / max(abs(a), 1e-300)
    worst = 0.0
    for k in range(len(d0["rho_u"])):
        if d0["rho_u"][k] is not None and d1["rho_u"][k] is not None:
            worst = max(worst, rel(d0["rho_u"][k], d1["rho_u"][k]))
    g0, g1 = d0["global_"], d1["global_"]
    out = {}
    for key in ("rho_u_max", "rho_nl_max", "sigma_u_max", "sigma_Om", "a_max", "rho_lin_max", "rho_sp_max", "rho_Om_max"):
        out[key] = rel(g0[key], g1[key]); worst = max(worst, out[key])
    print("diagnostics of the state vs its rotated image (relative differences): " + ", ".join(f"{k} {v:.1e}" for k, v in out.items()) + f"; worst per-shell rho_u {worst:.1e}")
    # roundoff analysis beside the strict SPEC T05 value 1e-12 (lead 2026-10-25T05:42Z; verifier 05:40Z): the ratios rho_nl and rho_sp divide by the
    # RMS of T4 + T5, which on far shells is 1e-4 to 1e-6 of the individual terms, so the relative roundoff of the ratio is about
    # 1e-16 x (term size / denominator); the per-shell size of this amplification is printed. The threshold is the SPEC value and is not lowered.
    T4 = d0["rms"]["T"][3]; T5 = d0["rms"]["T"][4]; T1 = d0["rms"]["T"][0]
    amp = [ (t1 / max(t4 + t5, 1e-300)) for t1, t4, t5 in zip(T1, T4, T5)]
    print(f"roundoff amplification of the nonlinear-denominator ratios per shell (RMS T1 / RMS(T4 + T5)): max {max(amp):.1e} (so 1e-16 x this = {1e-16 * max(amp):.1e})")
    strict = 1e-12
    print(f"T05 strict SPEC threshold {strict:.0e}: {'PASS' if worst < strict else 'FAIL'} (worst {worst:.1e}); quantities within the threshold: " + ", ".join(k for k, v in out.items() if v < strict))
    assert worst < strict, f"rotation covariance of the diagnostics: worst relative difference {worst:.2e} exceeds the SPEC value {strict:.0e} (see the roundoff amplification above)"
    print("test_T05_diagnostics_rotation PASS")

if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else None)

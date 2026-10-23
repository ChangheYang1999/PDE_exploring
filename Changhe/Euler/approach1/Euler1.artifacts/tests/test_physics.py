"""Unit tests for the Euler profile solver (run: python3 -m pytest -q tests  or  python3 tests/test_physics.py)."""
import math, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from euler_ss import physics as ph
from euler_ss.model import ProfileModel, seed_matrix, seed_fields, apply_Q
from euler_ss.losses import nonaxi_ratio
from euler_ss.sampling import Sampler

DEV = "cpu"


def base_cfg(cl=0.45, trainable_cl=False, seed_abc=(0.2, -0.4, 0.7), use_seed=True, width=16, depth=2, zero_last=False):
    return {"cl": cl, "cl_trainable": trainable_cl, "cl_bounds": [0.4, 0.5], "C": 0.0,
            "model": {"width": width, "depth": depth, "zero_last": zero_last, "feature_set": "both"},
            "seed": {"a": seed_abc[0], "b": seed_abc[1], "c": seed_abc[2], "use": use_seed, "trainable": False},
            "loss": {}}


def affine_fields(M):
    MM = M + M @ M
    def f(y):
        My = y @ M.T
        A = -torch.cross(y, My, dim=-1) / 3.0
        P = -0.5 * (y * (y @ MM.T)).sum(-1)
        return torch.cat([A, P.unsqueeze(-1)], -1)
    return f


def test_seed_matrix_facts():
    a, b, c = (torch.tensor(v) for v in (0.2, -0.4, 0.7))
    M = seed_matrix(a, b, c)
    assert abs(torch.trace(M).item()) < 1e-15
    MM = M + M @ M
    assert torch.allclose(MM, MM.T, atol=1e-15)


def test_affine_exact_all_residuals():
    """U = M y, P = -y.(M+M^2)y/2 has zero momentum, divergence, vorticity and pressure residuals for every c_l."""
    M = seed_matrix(*[torch.tensor(v) for v in (0.2, -0.4, 0.7)])
    f = affine_fields(M)
    y = torch.randn(64, 3) * 3
    F, J, H, T = ph.derivs(f, y, order=3)
    U, gU, P, gP, HP = ph.velocity_and_grad(F, J, H)
    assert torch.allclose(U, y @ M.T, atol=1e-13), "curl[-y x (My)/3] must equal M y"
    for cl in (0.41, 0.45, 0.5, 0.7):
        Rm, V, conv = ph.momentum_residual(y, U, gU, gP, cl)
        assert Rm.abs().max().item() < 1e-12, (cl, Rm.abs().max().item())
        Rom, Om, gOm = ph.vorticity_residual(y, U, gU, T, cl)
        assert Rom.abs().max().item() < 1e-12
    assert ph.divergence(gU).abs().max().item() < 1e-13
    RP, lapP, src = ph.pressure_residual(gU, HP)
    assert RP.abs().max().item() < 1e-12
    # cylindrical formulation agrees (zero) away from the axis
    cyl = ph.cylindrical_residual(y, U, gU, gP, 0.45)
    assert cyl.abs().max().item() < 1e-10


def test_seed_properties():
    cl = 0.45
    d = 1 - 1 / cl
    M = seed_matrix(*[torch.tensor(v) for v in (0.2, -0.4, 0.7)])
    def f(y):
        A, P = seed_fields(y, M, cl)
        return torch.cat([A, P.unsqueeze(-1)], -1)
    y = torch.randn(200, 3) * 2
    F, J, H = ph.derivs(f, y, order=2)
    U, gU, P, gP, HP = ph.velocity_and_grad(F, J, H)
    assert ph.divergence(gU).abs().max().item() < 1e-12
    # Q equivariance
    Fq, Jq, Hq = ph.derivs(f, apply_Q(y), order=2)
    Uq = ph.curl_from_jac(Jq[:, :3, :])
    assert torch.allclose(Uq, apply_Q(U), atol=1e-13)
    assert torch.allclose(Fq[:, 3], F[:, 3], atol=1e-13)
    # near zero: U = M y + O(|y|^3)
    eps = torch.tensor([[1e-3, 2e-3, -1e-3], [5e-4, -1e-3, 2e-3]])
    Fe, Je = ph.derivs(f, eps, order=1)
    Ue = ph.curl_from_jac(Je[:, :3, :])
    assert ((Ue - eps @ M.T).abs().max() / eps.norm(dim=-1).max() ** 3).item() < 50.0
    # tail degree: |U| ~ R^d, P ~ R^(2d)
    dirs = torch.randn(5, 3); dirs = dirs / dirs.norm(dim=-1, keepdim=True)
    for Ra, Rb in ((1e3, 1e4),):
        Fa, Ja = ph.derivs(f, Ra * dirs, order=1); Fb, Jb = ph.derivs(f, Rb * dirs, order=1)
        Ua = ph.curl_from_jac(Ja[:, :3, :]).norm(dim=-1); Ub = ph.curl_from_jac(Jb[:, :3, :]).norm(dim=-1)
        slope = (torch.log(Ub) - torch.log(Ua)) / math.log(Rb / Ra)
        assert (slope - d).abs().max().item() < 0.01, slope
        slopeP = (torch.log(Fb[:, 3].abs()) - torch.log(Fa[:, 3].abs())) / math.log(Rb / Ra)
        assert (slopeP - 2 * d).abs().max().item() < 0.01, slopeP
    # smooth-at-origin: gradient at 0 equals M
    F0, J0, H0 = ph.derivs(f, torch.zeros(1, 3), order=2)
    U0, gU0, _, _, _ = ph.velocity_and_grad(F0, J0, H0)
    assert torch.allclose(gU0[0], M, atol=1e-12)


def test_model_symmetry_and_divergence():
    torch.manual_seed(0)
    cfg = base_cfg()
    m = ProfileModel(cfg)
    y = torch.randn(100, 3) * 2
    F, J, H = ph.derivs(lambda p: m.fields(p), y, order=2)
    U, gU, P, gP, HP = ph.velocity_and_grad(F, J, H)
    Fq, Jq, Hq = ph.derivs(lambda p: m.fields(p), apply_Q(y), order=2)
    Uq, gUq, Pq, gPq, _ = ph.velocity_and_grad(Fq, Jq, Hq)
    assert torch.allclose(Uq, apply_Q(U), atol=1e-13)
    assert torch.allclose(Pq, P, atol=1e-13)
    assert ph.divergence(gU).abs().max().item() < 1e-11
    # symmetry-projected correction is Q-equivariant on its own, so projection commutes with curl
    SA, SP = m.corrections(y)
    SAq, SPq = m.corrections(apply_Q(y))
    assert torch.allclose(SAq, apply_Q(SA), atol=1e-14)
    # dtypes
    assert all(p.dtype == torch.float64 for p in m.parameters())
    assert U.dtype == torch.float64 and gU.dtype == torch.float64


def fd_jacobian(f, y, h=1e-5):
    J = torch.zeros(y.shape[0], 4, 3)
    for j in range(3):
        e = torch.zeros(3); e[j] = h
        J[:, :, j] = (f(y + e) - f(y - e)) / (2 * h)
    return J


def test_derivatives_vs_finite_differences():
    torch.manual_seed(1)
    cfg = base_cfg()
    m = ProfileModel(cfg)
    f = lambda p: m.fields(p)
    y = torch.randn(20, 3) * 1.5
    F, J, H = ph.derivs(f, y, order=2)
    Jfd = fd_jacobian(f, y)
    assert (J - Jfd).abs().max().item() < 1e-8, (J - Jfd).abs().max().item()
    # Hessian via FD of AD Jacobian
    h = 1e-5
    for k in range(3):
        e = torch.zeros(3); e[k] = h
        Jp = ph.derivs(f, y + e, order=1)[1]; Jm = ph.derivs(f, y - e, order=1)[1]
        Hfd = (Jp - Jm) / (2 * h)
        assert (H[:, :, :, k] - Hfd).abs().max().item() < 1e-7
    # third derivatives vs FD of Hessian
    F3, J3, H3, T3 = ph.derivs(f, y, order=3)
    assert torch.allclose(H3, H, atol=1e-14)
    k = 1; e = torch.zeros(3); e[k] = h
    Hp = ph.derivs(f, y + e, order=2)[2]; Hm = ph.derivs(f, y - e, order=2)[2]
    assert (T3[:, :, :, :, k] - (Hp - Hm) / (2 * h)).abs().max().item() < 1e-6


def test_cartesian_vs_cylindrical_residual():
    torch.manual_seed(2)
    cfg = base_cfg()
    m = ProfileModel(cfg)
    y = torch.randn(200, 3) * 2
    y = y[(y[:, 0] ** 2 + y[:, 1] ** 2) > 0.05]
    F, J, H = ph.derivs(lambda p: m.fields(p), y, order=2)
    U, gU, P, gP, HP = ph.velocity_and_grad(F, J, H)
    cl = 0.45
    Rm, V, conv = ph.momentum_residual(y, U, gU, gP, cl)
    cyl = ph.cylindrical_residual(y, U, gU, gP, cl)
    # project Cartesian residual onto (er, et, ez)
    r = torch.sqrt(y[:, 0] ** 2 + y[:, 1] ** 2)
    er = torch.stack([y[:, 0] / r, y[:, 1] / r, torch.zeros_like(r)], -1)
    et = torch.stack([-y[:, 1] / r, y[:, 0] / r, torch.zeros_like(r)], -1)
    Rr, Rt, Rz = (Rm * er).sum(-1), (Rm * et).sum(-1), Rm[:, 2]
    scale = Rm.abs().max().item()
    assert (cyl[:, 0] - Rr).abs().max().item() < 1e-10 * scale
    assert (cyl[:, 1] - Rt).abs().max().item() < 1e-10 * scale
    assert (cyl[:, 2] - Rz).abs().max().item() < 1e-10 * scale
    assert cyl[:, 3].abs().max().item() < 1e-10 * gU.abs().max().item()


def test_nonaxi_diagnostic():
    # axisymmetric seed: a = d0 = -1/2, b = -c  -> M = -1/2 I_2 + rotation; U_axi = U
    cfg = base_cfg(seed_abc=(-0.5, -0.7, 0.7), use_seed=True, zero_last=True)
    m = ProfileModel(cfg)
    y = torch.randn(64, 3)
    e_non, e_tot, U0, Ua = nonaxi_ratio(m, y, K=8)
    assert (e_non / e_tot).item() < 1e-20
    cfg2 = base_cfg(seed_abc=(0.2, -0.4, 0.7), zero_last=True)
    m2 = ProfileModel(cfg2)
    e_non, e_tot, _, _ = nonaxi_ratio(m2, y, K=8)
    assert (e_non / e_tot).item() > 1e-2


def test_sampler_weights():
    cfg = {"R_core": 2.0, "R_max": 100.0, "r_tube": 0.1, "R_origin": 0.5, "z_min": 0.01}
    s = Sampler(cfg, 0)
    y, w = s.sample_region("shell", 200000)
    vol = 4 / 3 * math.pi * (100.0 ** 3 - 2.0 ** 3)
    assert abs(w.sum().item() / vol - 1) < 0.05
    R = y.norm(dim=-1)
    assert R.min() >= 2.0 and R.max() <= 100.0
    y, w = s.sample_region("core", 1000)
    assert abs(w.sum().item() - 4 / 3 * math.pi * 8) < 1e-9
    # state save/restore reproduces the stream
    sd = s.state_dict(); a = s.sample_region("core", 5)[0]
    s.load_state_dict(sd); b = s.sample_region("core", 5)[0]
    assert torch.equal(a, b)


def test_cl_trainable_param():
    cfg = base_cfg(cl=0.45, trainable_cl=True)
    m = ProfileModel(cfg)
    assert abs(m.cl().item() - 0.45) < 1e-12
    assert m.cl().requires_grad




# ---- additional tests (EQUATIONS.md section 13: T5 symmetry, T6 scaling, T7 recentering, T8 dtype; v2 tail representation)
def _cfg_v2(cl=0.45, n_tail=2, last_init_std=0.3, use_seed=True, abc=(0.2, -0.4, 0.7)):
    return {"cl": cl, "cl_trainable": False, "C": 0.0,
            "model": {"width": 16, "depth": 2, "feature_set": "dir_tau", "n_tail": n_tail, "last_init_std": last_init_std, "zero_last": True},
            "seed": {"a": abc[0], "b": abc[1], "c": abc[2], "use": use_seed, "trainable": False}, "loss": {}}


def test_T5_residual_symmetry_random_network():
    torch.manual_seed(5)
    m = ProfileModel(_cfg_v2())
    y = torch.randn(64, 3) * 2
    F, J, H = ph.derivs(lambda p: m.fields(p), y, order=2)
    U, gU, P, gP, HP = ph.velocity_and_grad(F, J, H)
    Rm, _, _ = ph.momentum_residual(y, U, gU, gP, 0.45)
    Fq, Jq, Hq = ph.derivs(lambda p: m.fields(p), apply_Q(y), order=2)
    Uq, gUq, Pq, gPq, HPq = ph.velocity_and_grad(Fq, Jq, Hq)
    Rmq, _, _ = ph.momentum_residual(apply_Q(y), Uq, gUq, gPq, 0.45)
    assert torch.allclose(Rmq, apply_Q(Rm), atol=1e-12 * Rm.abs().max().item())
    assert torch.allclose(ph.divergence(gUq), ph.divergence(gU), atol=1e-11)
    assert Rm.abs().max().item() > 1e-3  # random network is not a solution


def test_T6_scaling_symmetry_of_residual():
    """R_m[U_a,P_a](y) = a R_m[U,P](y/a) with U_a(y) = a U(y/a), P_a(y) = a^2 P(y/a) (A_a(y) = a^2 A(y/a))."""
    torch.manual_seed(6)
    m = ProfileModel(_cfg_v2())
    a = 1.7
    f = lambda p: m.fields(p)
    def fa(p):
        F = m.fields(p / a)
        return torch.cat([a * a * F[..., :3], a * a * F[..., 3:]], -1)
    y = torch.randn(32, 3) * 2
    F, J, H = ph.derivs(f, y / a, order=2); U, gU, P, gP, HP = ph.velocity_and_grad(F, J, H)
    Rm, _, _ = ph.momentum_residual(y / a, U, gU, gP, 0.45)
    Fa, Ja, Ha = ph.derivs(fa, y, order=2); Ua, gUa, Pa, gPa, HPa = ph.velocity_and_grad(Fa, Ja, Ha)
    Rma, _, _ = ph.momentum_residual(y, Ua, gUa, gPa, 0.45)
    assert torch.allclose(Ua, a * U, atol=1e-12)
    assert torch.allclose(Rma, a * Rm, atol=1e-11 * Rm.abs().max().item())


def test_T7_recentering():
    """(E_C) residual of the shifted field U(y - h e_z) with C = -c_l h equals the (E) residual of U at y - h e_z."""
    torch.manual_seed(7)
    m = ProfileModel(_cfg_v2())
    cl, h = 0.45, 0.8
    ez = torch.tensor([0.0, 0.0, h])
    f = lambda p: m.fields(p)
    fs = lambda p: m.fields(p - ez)
    y = torch.randn(32, 3) * 2
    F, J, H = ph.derivs(f, y - ez, order=2); U, gU, P, gP, HP = ph.velocity_and_grad(F, J, H)
    Rm, _, _ = ph.momentum_residual(y - ez, U, gU, gP, cl, C=0.0)
    Fs, Js, Hs = ph.derivs(fs, y, order=2); Us, gUs, Ps, gPs, HPs = ph.velocity_and_grad(Fs, Js, Hs)
    Rms, _, _ = ph.momentum_residual(y, Us, gUs, gPs, cl, C=-cl * h)
    assert torch.allclose(Rms, Rm, atol=1e-11 * Rm.abs().max().item())
    cyl = ph.cylindrical_residual(y, Us, gUs, gPs, cl, C=-cl * h)
    r = torch.sqrt(y[:, 0] ** 2 + y[:, 1] ** 2)
    assert torch.allclose(cyl[:, 2], Rms[:, 2], atol=1e-10 * Rm.abs().max().item())


def test_T8_dtypes_and_optimizer_state():
    m = ProfileModel(_cfg_v2(last_init_std=0.1))
    opt = torch.optim.Adam(m.parameters(), lr=1e-3)
    y = torch.randn(16, 3)
    F, J, H = ph.derivs(lambda p: m.fields(p), y, order=2)
    U, gU, P, gP, HP = ph.velocity_and_grad(F, J, H)
    Rm, _, _ = ph.momentum_residual(y, U, gU, gP, 0.45)
    (Rm ** 2).mean().backward(); opt.step()
    for p in m.parameters():
        assert p.dtype == torch.float64 and (p.grad is None or p.grad.dtype == torch.float64)
    for st in opt.state.values():
        for k, v in st.items():
            if torch.is_tensor(v) and v.is_floating_point():
                assert v.dtype == torch.float64, k


def test_v2_tail_degrees_and_smoothness():
    """Each potential term k has U-degree d + k(d-1), pressure term k has degree 2d + k(d-1); fields smooth at 0."""
    cl = 0.45; d = 1 - 1 / cl
    dirs = torch.randn(4, 3); dirs = dirs / dirs.norm(dim=-1, keepdim=True)
    for k in range(3):
        torch.manual_seed(10 + k)
        m = ProfileModel(_cfg_v2(cl=cl, n_tail=3, last_init_std=0.5, use_seed=False))
        # zero out the other tail terms' output rows
        with torch.no_grad():
            W = m.netA.lins[-1].weight; W[[3 * j + i for j in range(3) if j != k for i in range(3)]] = 0.0
            Wp = m.netP.lins[-1].weight; Wp[[j for j in range(3) if j != k]] = 0.0
        f = lambda p: m.fields(p)
        Ra, Rb = 1e3, 1e4
        Fa, Ja = ph.derivs(f, Ra * dirs, order=1); Fb, Jb = ph.derivs(f, Rb * dirs, order=1)
        Ua = ph.curl_from_jac(Ja[:, :3, :]).norm(dim=-1); Ub = ph.curl_from_jac(Jb[:, :3, :]).norm(dim=-1)
        slope = (torch.log(Ub) - torch.log(Ua)) / math.log(Rb / Ra)
        assert (slope - (d + k * (d - 1))).abs().max().item() < 0.02, (k, slope)
        slopeP = (torch.log(Fb[:, 3].abs()) - torch.log(Fa[:, 3].abs())) / math.log(Rb / Ra)
        assert (slopeP - (2 * d + k * (d - 1))).abs().max().item() < 0.02, (k, slopeP)
    # smoothness at origin: third derivatives finite and FD-consistent
    m = ProfileModel(_cfg_v2(cl=cl, n_tail=2, last_init_std=0.5))
    y0 = torch.zeros(1, 3)
    F, J, H, T = ph.derivs(lambda p: m.fields(p), y0, order=3)
    assert torch.isfinite(T).all() and T.abs().max().item() < 1e3


def test_stagnation_finder_and_parity_on_seed():
    from euler_ss.diagnostics import find_stagnation_points, stagnation_starts, parity_defects, ring_fourier_energy
    m = ProfileModel(_cfg_v2(last_init_std=0.0))  # pure seed: V = c_l y + U_seed, zero at origin
    g = torch.Generator(); g.manual_seed(0)
    starts = stagnation_starts(64, 3.0, g, "cpu")
    zeros, nconv, nfail = find_stagnation_points(m, starts, 0.45)
    assert any(z["R"] < 1e-8 for z in zeros), zeros
    z0 = [z for z in zeros if z["R"] < 1e-8][0]
    # eig(grad V(0)) = eig(c_l I + M)
    M = seed_matrix(*[torch.tensor(v) for v in (0.2, -0.4, 0.7)])
    ev = sorted(torch.linalg.eigvals(0.45 * torch.eye(3) + M).real.tolist())
    assert max(abs(a - b) for a, b in zip(sorted(z0["eig_gradV_re"]), ev)) < 1e-6
    y = torch.randn(128, 3)
    inv, zr = parity_defects(m, y)
    assert inv < 1e-12 and zr < 1e-12  # seed has both extra parities
    m2 = ProfileModel(_cfg_v2(last_init_std=0.3))
    inv2, zr2 = parity_defects(m2, y)
    assert inv2 > 1e-3 and zr2 > 1e-3  # released by the random correction
    rf = ring_fourier_energy(m, [0.5, 1.0], [0.0, 0.5], K=32)
    assert rf["odd_frac"] < 1e-20 and rf["n2"] > 0.05





def test_blob_seed_symmetry_and_localization():
    cfg = _cfg_v2(last_init_std=0.0, use_seed=False)
    cfg["blobs"] = {"trainable": True, "list": [{"y0": [1.0, 0.0, 0.3], "m": [0.0, 0.5, 0.2], "sigma": 0.5}]}
    m = ProfileModel(cfg)
    y = torch.randn(64, 3) * 1.5
    F, J, H = ph.derivs(lambda p: m.fields(p), y, order=2)
    U, gU, P, gP, HP = ph.velocity_and_grad(F, J, H)
    Fq, Jq, Hq = ph.derivs(lambda p: m.fields(p), apply_Q(y), order=2)
    Uq = ph.curl_from_jac(Jq[:, :3, :])
    assert torch.allclose(Uq, apply_Q(U), atol=1e-13)
    assert ph.divergence(gU).abs().max().item() < 1e-11
    assert U.norm(dim=-1).max().item() > 1e-2
    far = torch.tensor([[0.0, 0.0, 30.0]])
    Ff, Jf = ph.derivs(lambda p: m.fields(p), far, order=1)
    assert ph.curl_from_jac(Jf[:, :3, :]).norm().item() < 1e-100
    inv, zr = __import__("euler_ss.diagnostics", fromlist=["parity_defects"]).parity_defects(m, y)
    assert inv > 1e-2 and zr > 1e-2  # no extra parities





def test_fastderiv_matches_torch_func():
    from euler_ss.fastderiv import fast_fields_derivs
    for cl_tr in (False, True):
        torch.manual_seed(21)
        cfg = _cfg_v2(cl=0.45, n_tail=2, last_init_std=0.3)
        cfg["cl_trainable"] = cl_tr
        m = ProfileModel(cfg)
        y = torch.cat([torch.randn(40, 3) * 2, torch.randn(8, 3) * 50, torch.zeros(1, 3)])
        F, J, H = ph.derivs(lambda p: m.fields(p), y, order=2)
        F2, J2, H2 = fast_fields_derivs(m, y)
        sc = max(F.abs().max().item(), 1.0)
        assert (F - F2).abs().max().item() < 1e-12 * sc, (F - F2).abs().max().item()
        assert (J - J2).abs().max().item() < 1e-11 * max(J.abs().max().item(), 1.0), (J - J2).abs().max().item()
        assert (H - H2).abs().max().item() < 1e-10 * max(H.abs().max().item(), 1.0), (H - H2).abs().max().item()
        # gradients w.r.t. parameters agree too
        g1 = torch.autograd.grad((H ** 2).sum() + (J ** 2).sum(), [p for p in m.parameters() if p.requires_grad], allow_unused=True)
        g2 = torch.autograd.grad((H2 ** 2).sum() + (J2 ** 2).sum(), [p for p in m.parameters() if p.requires_grad], allow_unused=True)
        for a, b in zip(g1, g2):
            if a is None and b is None:
                continue
            assert (a - b).abs().max().item() < 1e-9 * max(a.abs().max().item(), 1.0)


if __name__ == "__main__":
    import inspect
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    bad = 0
    for fn in fns:
        try:
            fn(); print("PASS", fn.__name__)
        except Exception as e:
            bad += 1; print("FAIL", fn.__name__, repr(e))
    print("failures:", bad)
    sys.exit(1 if bad else 0)

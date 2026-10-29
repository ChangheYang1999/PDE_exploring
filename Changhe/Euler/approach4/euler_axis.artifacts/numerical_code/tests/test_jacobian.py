"""Jacobian-vector products vs independent directional finite differences; GPU timing (PROMPT.md section 3, item 9).
Run: python3 tests/test_jacobian.py [cuda|cpu]
"""
import os, sys, time, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np
import torch
from axi.problem import Problem, Config

torch.set_default_dtype(torch.float64)
dev = sys.argv[1] if len(sys.argv) > 1 else ("cuda" if torch.cuda.is_available() else "cpu")
FAILS = []


def check(name, err, tol):
    ok = err <= tol
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: err={err:.3e} tol={tol:.1e}")
    if not ok:
        FAILS.append(name)


def random_x(prob, seed=0, amp=0.3):
    g = torch.Generator().manual_seed(seed)
    x = amp * torch.randn(prob.nx, generator=g, dtype=torch.float64)
    # decay with basis index inside each element for smoothness
    for i, e in enumerate(prob.elements):
        for cols, off in ((prob.cols_phi[i], prob.off_phi), (prob.cols_q[i], prob.off_q)):
            labs = [e.labels[j] for j in cols]
            lab = np.array([l[0] for l in labs], float)
            kk = np.array([l[1] if e.kind != "exterior" else 0.0 for l in labs], float)
            dec = torch.tensor(np.exp(-0.15 * (lab + 2 * kk)))
            x[off[i]:off[i + 1]] *= dec
    if prob.cfg.free_cl:
        x[prob.ix_cl] = prob.cfg.cl           # (earlier versions set x[-1], which is z0 when S1 rows are present)
    if prob.ix_z0 is not None:
        x[prob.ix_z0] = prob.cfg.z0_init
    if prob.ix_a is not None:
        x[prob.ix_a] = 0.0
    return x.to(prob.device)


def jvp_fd(prob, x, v, h):
    return (prob.residual(x + h * v) - prob.residual(x - h * v)) / (2 * h)


def test_small(free_cl):
    cfg = Config(cl=0.6, free_cl=free_cl, R1=1.5, D=10, nmax=5, shells=[(5.0, 8)], emax=5.0, seed=1)
    prob = Problem(cfg, device=dev)
    print(f"small problem free_cl={free_cl}: nx={prob.nx} rows={prob.n_rows} elements={[e.kind for e in prob.elements]}")
    x = random_x(prob, 3)
    J = prob.jacobian(x)
    for t in range(3):
        v = torch.randn(prob.nx, generator=torch.Generator().manual_seed(10 + t), dtype=torch.float64).to(dev)
        if free_cl:
            v[-1] *= 0.01
        errs = []
        for h in [1e-4, 1e-5, 1e-6]:
            fd = jvp_fd(prob, x, v, h)
            errs.append(float(torch.max(torch.abs(J @ v - fd))) / max(1.0, float(torch.max(torch.abs(J @ v)))))
        check(f"JVP vs central FD (free_cl={free_cl}, dir {t}) best over h", min(errs), 3e-7 if not free_cl else 3e-6)
        print("    errs by h:", ["%.2e" % e for e in errs])
    # residual is finite and float64
    r = prob.residual(x)
    check(f"residual dtype float64 (free_cl={free_cl})", 0.0 if r.dtype == torch.float64 else 1.0, 0)
    check(f"residual finite (free_cl={free_cl})", 0.0 if torch.isfinite(r).all() else 1.0, 0)
    check(f"Jacobian finite (free_cl={free_cl})", 0.0 if torch.isfinite(J).all() else 1.0, 0)


def test_s1(free_cl):
    """S1 rows (phi_z(0,z0) = 1/2, c z0 + 2 phi(0,z0) = 0) with free z0: Jacobian vs finite differences, including
    the z0 column (nonlinear in z0) and, if free, the c_l column."""
    cfg = Config(cl=0.62, free_cl=free_cl, R1=1.5, D=12, nmax=6, shells=[(5.0, 8)], emax=5.0, s1_constraint=True, z0_init=0.37)
    prob = Problem(cfg, device=dev)
    x = random_x(prob, 7)
    x[prob.ix_z0] = 0.37
    J = prob.jacobian(x)
    for t in range(2):
        v = torch.randn(prob.nx, generator=torch.Generator().manual_seed(20 + t), dtype=torch.float64).to(dev)
        if free_cl:
            v[prob.ix_cl] *= 0.01
        errs = []
        for h in [1e-4, 1e-5, 1e-6]:
            fd = jvp_fd(prob, x, v, h)
            errs.append(float(torch.max(torch.abs(J @ v - fd))) / max(1.0, float(torch.max(torch.abs(J @ v)))))
        check(f"S1 rows JVP vs FD (free_cl={free_cl}, dir {t})", min(errs), 3e-6)
    # z0 column alone
    v = torch.zeros(prob.nx, dtype=torch.float64, device=dev); v[prob.ix_z0] = 1.0
    errs = [float(torch.max(torch.abs(J @ v - jvp_fd(prob, x, v, h)))) for h in [1e-4, 1e-5, 1e-6]]
    check(f"S1 z0 column vs FD (free_cl={free_cl})", min(errs), 1e-6)
    # residual rows: exact values
    r = prob.residual(x)
    res, _ = prob.s1_residual_and_jac(x)
    check("S1 residual rows consistent", float(torch.max(torch.abs(r[-2:].cpu() - torch.tensor(res)))), 1e-12)
    # moving the axis point through R1 into the shell element also works
    x2 = x.clone(); x2[prob.ix_z0] = -2.3
    r2 = prob.residual(x2); J2 = prob.jacobian(x2)
    check("S1 rows finite for z0 in shell", 0.0 if torch.isfinite(r2).all() and torch.isfinite(J2).all() else 1.0, 0)


def test_q0_pin():
    cfg = Config(cl=0.62, free_cl=True, R1=1.5, D=12, nmax=6, shells=[(5.0, 8)], emax=5.0, s1_constraint=True, z0_init=0.21, q0_pin=0.8)
    prob = Problem(cfg, device=dev)
    x = random_x(prob, 9); x[prob.ix_z0] = 0.21
    J = prob.jacobian(x)
    r = prob.residual(x)
    check("q0 pin: 3 S1 rows", abs(prob.n_s1_rows - 3), 0)
    for t in range(2):
        v = torch.randn(prob.nx, generator=torch.Generator().manual_seed(40 + t), dtype=torch.float64).to(dev); v[prob.ix_cl] *= 0.01
        errs = [float(torch.max(torch.abs((J @ v - jvp_fd(prob, x, v, h))[-3:]))) for h in [1e-4, 1e-5, 1e-6]]
        check(f"q0 pin rows JVP vs FD (dir {t})", min(errs), 1e-6)
    qv = prob.eval_field(x, "q", np.array([0.21]), np.array([1.0]))[0]
    check("q0 pin row value", abs(float(r[-1]) - cfg.w_s1 * (qv - 0.8)), 1e-12)


def test_amp():
    """Explicit swirl amplitude: q = A qhat, eta rows divided by A^2; Jacobian (including the A column) vs finite differences;
    to_physical reproduces the standard residual structure."""
    cfg = Config(cl=0.62, free_cl=False, R1=1.5, D=12, nmax=6, shells=[(5.0, 8)], emax=5.0, s1_constraint=True, z0_init=0.1, amp_param=True)
    prob = Problem(cfg, device=dev)
    x = random_x(prob, 11); x[prob.ix_z0] = 0.1; x[prob.ix_a] = 0.3
    J = prob.jacobian(x)
    for t in range(2):
        v = torch.randn(prob.nx, generator=torch.Generator().manual_seed(60 + t), dtype=torch.float64).to(dev)
        errs = []
        for h in [1e-4, 1e-5, 1e-6]:
            fd = jvp_fd(prob, x, v, h)
            errs.append(float(torch.max(torch.abs(J @ v - fd))) / max(1.0, float(torch.max(torch.abs(J @ v)))))
        check(f"amp_param JVP vs FD (dir {t})", min(errs), 3e-6)
    v = torch.zeros(prob.nx, dtype=torch.float64, device=dev); v[prob.ix_a] = 1.0
    errs = [float(torch.max(torch.abs(J @ v - jvp_fd(prob, x, v, h)))) / max(1.0, float(torch.max(torch.abs(J @ v)))) for h in [1e-4, 1e-5, 1e-6]]
    check("amp_param A column vs FD", min(errs), 1e-6)
    # physical conversion: q rows of the physical problem equal A x (qhat rows); eta rows equal A^2 x (hat eta rows)
    xp, cfgp = prob.to_physical(x)
    pp = Problem(cfgp, device=dev)
    rp = pp.residual(xp); rh = prob.residual(x)
    A = prob.amp_of(x)
    n0 = prob.n_nodes_per_el[0]
    check("physical q rows = A * hat q rows (element 0)", float(torch.max(torch.abs(rp[:n0] - A * rh[:n0]))), 1e-10)
    check("physical eta rows = A^2 * hat eta rows (element 0)", float(torch.max(torch.abs(rp[n0:2 * n0] - A * A * rh[n0:2 * n0]))), 1e-9)


T2_ROWS = [dict(field="phi", der="z", r=0.0, z=0.0, target_expr="(1 + 3*c)/2", weight=100.0),
           dict(field="phi", der="z", r=1.0, z=0.0, target_expr="c", weight=100.0),
           dict(field="phi", der="sz", r=1.0, z=0.0, target_expr="-(1 + c)/2", weight=100.0),
           dict(field="eta", der="z", r=1.0, z=0.0, target_expr="2*K**2/(3*c)", weight=100.0),
           dict(field="q", der="z", r=1.0, z=0.0, target_expr="K", weight=100.0)]


def test_t2():
    """T2 branch machinery: odd parity masks, five point rows with c_l-dependent targets, q axis rows, free c_l, no gauge row."""
    from axi.init import make_init
    cfg = Config(cl=0.62, free_cl=True, R1=2.0, D=12, nmax=7, shells=[(6.0, 8)], emax=4.0, ball_radial="jacobi", parity_phi="odd", parity_q="odd",
                 point_rows=T2_ROWS, K_param=1.0, axis_rows_q=10, w_gauge=0.0)
    prob = Problem(cfg, device=dev)
    check("T2: odd parity keeps only odd n in the exterior leading set", 0.0 if all(n % 2 == 1 for n in prob.ext_lead_n_phi) else 1.0, 0)
    x = make_init(prob, "ring_t2", 1, extra={"K": 1.0})
    r = prob.residual(x)
    # the seed satisfies the T2 rows approximately (fit error) and is odd
    np_ = np.array([0.3, 0.7, 1.5]); vals_p = prob.eval_field(x, "phi", np.full(3, 1.0), np_ / 1.0 * 0 + 0.5); vals_m = prob.eval_field(x, "phi", np.full(3, 1.0), -np.full(3, 0.5))
    check("T2 seed phi odd in z", float(np.max(np.abs(vals_p + vals_m))), 1e-12)
    pt = prob.Jpt.cpu().numpy() @ x.cpu().numpy() - prob.bpt.cpu().numpy()
    print("    T2 point-row defects of the seed (weighted):", ["%.2e" % v for v in pt[:5]], " axis rows max", "%.2e" % np.max(np.abs(pt[5:])))
    check("T2 seed satisfies phi_z(1,0) = c to the fit accuracy of this small test resolution (D = 12)", abs(pt[1]) / 100.0, 0.1)
    J = prob.jacobian(x)
    for t in range(2):
        v = torch.randn(prob.nx, generator=torch.Generator().manual_seed(80 + t), dtype=torch.float64).to(dev); v[prob.ix_cl] *= 0.01
        errs = [float(torch.max(torch.abs(J @ v - jvp_fd(prob, x, v, h)))) / max(1.0, float(torch.max(torch.abs(J @ v)))) for h in [1e-4, 1e-5, 1e-6]]
        check(f"T2 JVP vs FD incl. c_l-dependent targets (dir {t})", min(errs), 3e-6)
    check("T2 residual finite", 0.0 if torch.isfinite(r).all() else 1.0, 0)


def test_slave():
    """Slaved first far-field correction: slave rows and their Jacobian (autograd), fixed and free c_l; consistency with axi.farfield.first_correction."""
    from axi.farfield import first_correction
    for free in (False, True):
        cfg = Config(cl=0.62, free_cl=free, R1=1.5, D=12, nmax=6, shells=[(5.0, 8)], emax=4.0, ball_radial="jacobi", s1_constraint=True, slave_correction=True)
        prob = Problem(cfg, device=dev)
        x = random_x(prob, 13); x[prob.ix_z0] = 0.2
        r = prob.residual(x); J = prob.jacobian(x)
        check(f"slave rows present (free_cl={free})", abs(prob.n_slave_rows - 2 * (cfg.nmax + 1)), 0)
        for t in range(2):
            v = torch.randn(prob.nx, generator=torch.Generator().manual_seed(100 + t), dtype=torch.float64).to(dev)
            if free: v[prob.ix_cl] *= 0.01
            errs = [float(torch.max(torch.abs(J @ v - jvp_fd(prob, x, v, h)))) / max(1.0, float(torch.max(torch.abs(J @ v)))) for h in [1e-4, 1e-5, 1e-6]]
            check(f"slave JVP vs FD (free_cl={free}, dir {t})", min(errs), 3e-6)
        # the slave map agrees with the numpy first_correction
        a = (x[prob.slave_lead_phi] * prob.Rm ** prob.alpha).cpu().numpy(); b = (x[prob.slave_lead_q] * prob.Rm ** (prob.alpha + 1)).cpu().numpy()
        afull = np.zeros(cfg.nmax + 1); bfull = np.zeros(cfg.nmax + 1); afull[prob.slave_n_phi] = a; bfull[prob.slave_n_q] = b
        a1, b1, info = first_correction(afull, bfull, prob.alpha, nmax_out=cfg.nmax)
        ta, tb = prob.slave_targets(x)
        err = max(float(np.max(np.abs(ta.cpu().numpy() - a1[prob.slave_n_phi] * prob.Rm ** (-(2 * prob.alpha + 1))))),
                  float(np.max(np.abs(tb.cpu().numpy() - b1[prob.slave_n_q] * prob.Rm ** (-(2 * prob.alpha + 2))))))
        check(f"slave map matches first_correction (free_cl={free})", err / max(1e-300, float(np.max(np.abs(a1)) + np.max(np.abs(b1)))), 1e-10)


def bench():
    for (D, nmax, K) in [(24, 12, 16), (40, 20, 24), (60, 30, 32)]:
        cfg = Config(cl=0.6, free_cl=True, R1=2.0, D=D, nmax=nmax, shells=[(10.0, K)], emax=6.0)
        t0 = time.time()
        prob = Problem(cfg, device=dev)
        tb = time.time() - t0
        x = random_x(prob, 5)
        if dev == "cuda":
            torch.cuda.synchronize()
        t0 = time.time()
        for _ in range(3):
            r = prob.residual(x)
        if dev == "cuda":
            torch.cuda.synchronize()
        tr = (time.time() - t0) / 3
        t0 = time.time()
        J = prob.jacobian(x)
        H = J.T @ J
        L = torch.linalg.cholesky(H + 1e-3 * torch.diag(torch.diagonal(H)) + 1e-12 * torch.eye(prob.nx, device=dev))
        if dev == "cuda":
            torch.cuda.synchronize()
        tj = time.time() - t0
        mem = torch.cuda.max_memory_allocated() / 2**30 if dev == "cuda" else float("nan")
        print(f"bench D={D} nmax={nmax} K={K}: nx={prob.nx} rows={prob.n_rows} build {tb:.1f}s residual {tr*1e3:.1f}ms "
              f"jacobian+normal+chol {tj:.2f}s peakmem {mem:.2f}GB")


if __name__ == "__main__":
    print("device", dev, torch.cuda.get_device_name(0) if dev == "cuda" else "")
    test_small(False)
    test_small(True)
    test_s1(False)
    test_s1(True)
    test_q0_pin()
    test_amp()
    test_t2()
    test_slave()
    bench()
    print(f"\n{len(FAILS)} failures")
    if FAILS:
        print("FAILED:", FAILS); sys.exit(1)

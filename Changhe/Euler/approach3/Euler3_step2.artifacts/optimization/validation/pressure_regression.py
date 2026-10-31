"""D6FP regression: new PressureSolver (torch tables) vs the frozen Euler3 solver (numpy tables) on the same model and source;
and a first forward-mode (jvp) check of the table build against central differences in c_l and omega."""
import sys, os, time, importlib.util, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model, alpha_of
from src.pressure.poisson_sh import PressureSolver
import importlib.machinery
_path = os.path.join(os.path.dirname(__file__), "..", "src", "pressure", "poisson_sh.py.frozen_e3")
_loader = importlib.machinery.SourceFileLoader("src.pressure.poisson_frozen", _path)
_spec = importlib.util.spec_from_loader(_loader.name, _loader)
frozen = importlib.util.module_from_spec(_spec); sys.modules[_spec.name] = frozen; _loader.exec_module(frozen)
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z if torch.cuda.is_available() else "cpu"
L, Nk = 6, 16
ch = dict(NkB=4, NkD=4, NkE=4, core_damp=2, LB=15, LD=14, LE=6)
for (c_l, omega) in [(0.45, 1.0), (0.45, 0.3), (0.42, 0.3)]:
    model = Model(L=L, Nk=Nk, Nr=48, m_parity="even", R0=0.3, c_l=c_l, omega=omega, free_params=True, channels=ch, device=dev, extra_r=[4096., 16384., 65536.])
    torch.manual_seed(1)
    z = torch.randn(model.n_z, device=dev) * 0.05; z[-2] = c_l; z[-1] = omega
    F = model.fields_grid(z, need_vort=False)
    GU = F["GU"]; f = torch.einsum('mi...,im...->...', GU, GU)
    p0 = 2 * alpha_of(c_l) + 2
    t0 = time.time(); ps_old = frozen.PressureSolver(model, p0=p0, omega=omega, c_l=c_l); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t_old = time.time() - t0
    t0 = time.time(); ps_same = PressureSolver(model, p0=p0, omega=omega, c_l=c_l, kappa_margin=1.0, alpha_margin=1.0); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t_same = time.time() - t0
    t0 = time.time(); ps_new = PressureSolver(model, p0=p0, omega=omega, c_l=c_l); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t_new = time.time() - t0
    P0, G0, _, _ = ps_old.solve(f); P1, G1, _, _ = ps_same.solve(f); P2, G2, _, _ = ps_new.solve(f)
    g00 = ps_old.gradP_origin(f); g01 = ps_same.gradP_origin(f); g02 = ps_new.gradP_origin(f)
    v0 = ps_old.volume_integral(f.abs()); v1 = ps_same.volume_integral(f.abs()); v2 = ps_new.volume_integral(f.abs())
    rel = lambda a, b: float((a - b).abs().max() / b.abs().max())
    print(f"(c_l, omega) = ({c_l}, {omega}): quad pts frozen {ps_old.n_quad} / same-geometry {ps_same.n_quad} / margins {ps_new.n_quad}; build time frozen {t_old:.1f}s, torch same {t_same:.2f}s, torch margins {t_new:.2f}s")
    print(f"   same geometry: rel diff P {rel(P1, P0):.2e} gradP {rel(G1, G0):.2e} gradP(0) {rel(g01, g00):.2e} volume {abs(float(v1 - v0)) / abs(float(v0)):.2e}")
    print(f"   with margins : rel diff P {rel(P2, P0):.2e} gradP {rel(G2, G0):.2e} gradP(0) {rel(g02, g00):.2e} volume {abs(float(v2 - v0)) / abs(float(v0)):.2e}")
    # jvp of the table build and of the pressure solve w.r.t. c_l and omega, against central differences of the SAME function (fixed geometry)
    def Pfun(cl, om):
        T = ps_new.build_tables(cl, om)
        P, G, _, _ = ps_new.solve(f, tables=T)
        return torch.cat([P.reshape(-1), G.reshape(-1), ps_new.gradP_origin(f, tables=T), ps_new.volume_integral(f.abs(), tables=T)[None]])
    cl_t = torch.tensor(c_l, device=dev); om_t = torch.tensor(omega, device=dev)
    for name, e in (("c_l", (torch.ones((), device=dev), torch.zeros((), device=dev))), ("omega", (torch.zeros((), device=dev), torch.ones((), device=dev)))):
        t0 = time.time(); val, tan = torch.func.jvp(Pfun, (cl_t, om_t), e); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t_j = time.time() - t0
        errs = []
        for h in (1e-3, 1e-4, 1e-5, 1e-6):
            dp = (Pfun(cl_t + h * e[0], om_t + h * e[1]) - Pfun(cl_t - h * e[0], om_t - h * e[1])) / (2 * h)
            errs.append(float((tan - dp).norm() / dp.norm()))
        print(f"   d/d{name}: jvp {t_j:.2f}s; |jvp - FD|/|FD| at h = 1e-3..1e-6: " + ", ".join(f"{v:.2e}" for v in errs) + f"; |tangent| {float(tan.norm()):.3e}")
print("DONE")

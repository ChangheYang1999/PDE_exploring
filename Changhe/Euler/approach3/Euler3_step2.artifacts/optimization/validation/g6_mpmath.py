#!/usr/bin/env python
"""D6FP G6 (scalar level, extended precision): the radial building blocks of the representation and their rho- and parameter-derivatives from the
production code (float64; jets, twist tables, tail-constraint elimination, pressure kernel factors) against mpmath at 50 digits, at 9 radii
(3 per radial group) for two parameter pairs. The field-level G6 (U, DU, U_p, DU_p and the momentum identities in 70 digits) is the verifier's
V010. Writes validation/g6_mpmath.json."""
import sys, os, json, math, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch, mpmath as mp
torch.set_default_dtype(torch.float64)
from src.bases.radial import RadialBasis
from src.bases import jets
from src.optimization.tail_constraints import TailConstraints
from src.equations.fields import Model
mp.mp.dps = 50
R0 = 0.3; Nk = 16
radii = [1e-3 * R0, 1e-2 * R0, 0.05 * R0, 0.5 * R0, 3.0 * R0, 100.0 * R0, 1000.0 * R0, 16384.0 * R0, 65536.0 * R0]
groups = ["near"] * 3 + ["core_intermediate"] * 3 + ["far"] * 3
pairs = [(0.45, 1.0), (0.42, 0.3)]
rng = np.random.default_rng(12)
a = rng.normal(size=Nk) * 0.55 ** np.arange(Nk)
out = dict(dps=50, radii=radii, groups=groups, pairs=pairs, coefficients=a.tolist(), checks=[])
rb = RadialBasis(Nk)
worst = {}
def rec(name, group, pair, prod, ref, cond=None):
    ref_f = float(ref); err = abs(prod - ref_f); scale = max(abs(ref_f), 1e-300)
    rel = err / scale
    entry = dict(quantity=name, group=group, pair=pair, production=prod, reference=mp.nstr(ref, 25), abs_error=err, rel_error=rel)
    if cond is not None:
        entry["condition"] = float(cond); entry["threshold_rule"] = "relative 1e-10" if cond < 1e4 else "absolute 1e-14 x sum of term sizes"
        entry["PASS"] = (rel <= 1e-10) if cond < 1e4 else (err <= 1e-14 * float(cond) * scale)
    else:
        entry["PASS"] = rel <= 1e-10
    out["checks"].append(entry)
    key = (name.split("[")[0], group)
    worst[key] = max(worst.get(key, 0.0), rel)
    return entry["PASS"]
for (c_l, omega) in pairs:
    alpha = (1 - c_l) / c_l; kappa = omega / c_l
    for ri, r in enumerate(radii):
        rho = r * r; g = groups[ri]
        for l, shift, name in ((1, 0.0, "T_l1"), (6, 0.0, "T_l6"), (4, 1.0, "S_l4")):
            # production: derivative arrays d^n/drho^n of (s/R0)^-(alpha+l-shift) sum_k a_k Phi_k(x) at rho, n = 0..4, and d/dc_l of the n = 0..2 values
            def prod_vals(cl_t):
                B = rb.matrices(torch.tensor([rho]), (1 - cl_t) / cl_t, torch.tensor(R0), l, 4, shift=shift)   # (l+1, 5, 1, Nk)
                return torch.einsum('nk,k->n', B[l, :, 0, :], torch.tensor(a))
            v = prod_vals(torch.tensor(c_l))
            vc = torch.func.jvp(prod_vals, (torch.tensor(c_l),), (torch.tensor(1.0),))[1]
            # mpmath reference
            def gfun(rho_, cl_):
                al = (1 - cl_) / cl_; s = mp.sqrt(rho_ + R0 ** 2); x = (s - R0) / (s + R0); t = 2 * x - 1
                env = (s / R0) ** (-(al + l - shift))
                tot = mp.mpf(0)
                for k in range(Nk):
                    tot += mp.mpf(a[k]) * mp.chebyt(k, t)
                return env * tot
            for n_ in range(5):
                ref = mp.diff(lambda q: gfun(q, mp.mpf(c_l)), mp.mpf(rho), n_)
                rec(f"{name}[d^{n_}/drho^{n_}]", g, (c_l, omega), float(v[n_]), ref)
            for n_ in range(3):
                ref = mp.diff(lambda q, cc: gfun(q, cc), (mp.mpf(rho), mp.mpf(c_l)), (n_, 1))
                # cancellation estimate (SPEC G6): the production envelope is u^p R0^(-2p), whose p-derivative is (log u - log R0^2) u^p R0^(-2p);
                # near the origin log u - log R0^2 ~ rho/R0^2 while the two logs are O(1): condition = (|log u| + |log R0^2|)/|log(u/R0^2)|
                u_ = rho + R0 ** 2; cond = (abs(math.log(u_)) + abs(math.log(R0 ** 2))) / abs(math.log1p(rho / R0 ** 2))
                rec(f"{name}[d/dc_l d^{n_}/drho^{n_}]", g, (c_l, omega), float(vc[n_]), ref, cond=cond)
        # twist tables: cos(m beta), sin(m beta) and derivatives, m = 2, 6; d/domega and d/dc_l of the values
        for m_ in (2, 6):
            def tw(cl_t, om_t):
                C, S = RadialBasis.twist_tables(torch.tensor([rho]), om_t, cl_t, torch.tensor(R0), 6, 4)
                return torch.stack([C[m_, :, 0], S[m_, :, 0]])            # (2, 5)
            v = tw(torch.tensor(c_l), torch.tensor(omega))
            vw = torch.func.jvp(tw, (torch.tensor(c_l), torch.tensor(omega)), (torch.tensor(0.0), torch.tensor(1.0)))[1]
            vcl = torch.func.jvp(tw, (torch.tensor(c_l), torch.tensor(omega)), (torch.tensor(1.0), torch.tensor(0.0)))[1]
            beta = lambda q, cc, ww: ww / (2 * cc) * mp.log(1 + q / R0 ** 2)
            for n_ in range(5):
                refc = mp.diff(lambda q: mp.cos(m_ * beta(q, mp.mpf(c_l), mp.mpf(omega))), mp.mpf(rho), n_)
                refs = mp.diff(lambda q: mp.sin(m_ * beta(q, mp.mpf(c_l), mp.mpf(omega))), mp.mpf(rho), n_)
                rec(f"cos(m beta) m{m_}[d^{n_}/drho^{n_}]", g, (c_l, omega), float(v[0, n_]), refc)
                rec(f"sin(m beta) m{m_}[d^{n_}/drho^{n_}]", g, (c_l, omega), float(v[1, n_]), refs)
            refw = mp.diff(lambda ww: mp.sin(m_ * beta(mp.mpf(rho), mp.mpf(c_l), ww)), mp.mpf(omega))
            refcl = mp.diff(lambda cc: mp.sin(m_ * beta(mp.mpf(rho), cc, mp.mpf(omega))), mp.mpf(c_l))
            # the omega derivative of sin(m beta) at tiny rho is tiny: record the scale (cancellation rule not needed: log1p is exact)
            rec(f"sin(m beta) m{m_}[d/domega]", g, (c_l, omega), float(vw[1, 0]), refw)
            rec(f"sin(m beta) m{m_}[d/dc_l]", g, (c_l, omega), float(vcl[1, 0]), refcl)
            refw1 = mp.diff(lambda q, ww: mp.sin(m_ * beta(q, mp.mpf(c_l), ww)), (mp.mpf(rho), mp.mpf(omega)), (1, 1))
            rec(f"sin(m beta) m{m_}[d/domega d/drho]", g, (c_l, omega), float(vw[1, 1]), refw1)
        # pressure kernel factors at a quadrature-like point: (s/R0)^-p0 (r/s)^le and its c_l derivative; beta at the point and d/domega
        s_ = math.sqrt(rho + R0 ** 2)
        def kern(cl_t):
            al = (1 - cl_t) / cl_t; p0 = 2 * al + 2
            return torch.exp(-p0 * torch.log(torch.tensor(s_ / R0)) + 4.0 * (torch.log(torch.tensor(r)) - torch.log(torch.tensor(s_))))
        v = kern(torch.tensor(c_l)); vc = torch.func.jvp(kern, (torch.tensor(c_l),), (torch.tensor(1.0),))[1]
        kref = lambda cc: (mp.mpf(s_) / R0) ** (-(2 * (1 - cc) / cc + 2)) * (mp.mpf(r) / mp.mpf(s_)) ** 4
        rec("pressure kernel factor (s/R0)^-p0 (r/s)^4", g, (c_l, omega), float(v), kref(mp.mpf(c_l)))
        rec("pressure kernel factor [d/dc_l]", g, (c_l, omega), float(vc), mp.diff(kref, mp.mpf(c_l)))
    # tail-constraint elimination: the top two coefficients of a pair as functions of (p, q) and their parameter derivatives (one pair, l = 2, m = 2, T channel)
    dev = "cpu"
    model = Model(L=2, Nk=Nk, Nr=8, m_parity="even", R0=R0, c_l=c_l, omega=omega, free_params=True, device=dev)
    tc = TailConstraints(model)
    free = torch.tensor(rng.normal(size=(Nk - 2, 2)) * 0.6 ** np.arange(Nk - 2)[:, None])
    q_idx = model.modes.index((2, 2, 0))
    def top(cl_t, om_t):
        alpha_t = (1 - cl_t) / cl_t; kap = om_t / cl_t
        p = (alpha_t + 2) / 2.0; q = 2 * kap / 2.0
        aa, bb = tc._solve_pair(free[:, 0], free[:, 1], p, q)
        return torch.stack([aa[-2], aa[-1], bb[-2], bb[-1]])
    v = top(torch.tensor(c_l), torch.tensor(omega)); vc = torch.func.jvp(top, (torch.tensor(c_l), torch.tensor(omega)), (torch.tensor(1.0), torch.tensor(0.0)))[1]
    vw = torch.func.jvp(top, (torch.tensor(c_l), torch.tensor(omega)), (torch.tensor(0.0), torch.tensor(1.0)))[1]
    def top_mp(cc, ww):
        al = (1 - cc) / cc; kap = ww / cc; p = (al + 2) / 2; q = kap
        k = [mp.mpf(i) for i in range(Nk)]; k2 = [ki ** 2 for ki in k]; k4 = [mp.mpf(8) / 3 * ki ** 2 * (ki ** 2 - 1) for ki in k]
        fa = [mp.mpf(float(free[i, 0])) for i in range(Nk - 2)]; fb = [mp.mpf(float(free[i, 1])) for i in range(Nk - 2)]
        # rows: k2.a = 0 ; k2.b = 0 ; (k4 - p).a + q 1.b = 0 ; -q 1.a + (k4 - p).b = 0
        M = mp.matrix([[k2[Nk - 2], k2[Nk - 1], 0, 0], [0, 0, k2[Nk - 2], k2[Nk - 1]], [k4[Nk - 2] - p, k4[Nk - 1] - p, q, q], [-q, -q, k4[Nk - 2] - p, k4[Nk - 1] - p]])
        rhs = mp.matrix([-sum(k2[i] * fa[i] for i in range(Nk - 2)), -sum(k2[i] * fb[i] for i in range(Nk - 2)),
                         -(sum((k4[i] - p) * fa[i] for i in range(Nk - 2)) + sum(q * fb[i] for i in range(Nk - 2))),
                         -(sum(-q * fa[i] for i in range(Nk - 2)) + sum((k4[i] - p) * fb[i] for i in range(Nk - 2)))])
        return mp.lu_solve(M, rhs)
    ref = top_mp(mp.mpf(c_l), mp.mpf(omega))
    for i, nm in enumerate(("a_top2", "a_top1", "b_top2", "b_top1")):
        rec(f"tail constraint {nm}", "coefficients", (c_l, omega), float(v[i]), ref[i])
        rec(f"tail constraint {nm}[d/dc_l]", "coefficients", (c_l, omega), float(vc[i]), mp.diff(lambda cc: top_mp(cc, mp.mpf(omega))[i], mp.mpf(c_l)))
        rec(f"tail constraint {nm}[d/domega]", "coefficients", (c_l, omega), float(vw[i]), mp.diff(lambda ww: top_mp(mp.mpf(c_l), ww)[i], mp.mpf(omega)))
n_pass = sum(1 for c in out["checks"] if c["PASS"]); n_tot = len(out["checks"])
out["summary"] = dict(n_checks=n_tot, n_pass=n_pass, worst_rel_by_quantity_group={f"{k[0]} | {k[1]}": v for k, v in sorted(worst.items(), key=lambda kv: -kv[1])[:25]}, PASS=(n_pass == n_tot))
fails = [c for c in out["checks"] if not c["PASS"]]
json.dump(out, open(os.path.join(os.path.dirname(__file__), "g6_mpmath.json"), "w"), indent=1)
print(f"G6 scalar extended precision: {n_pass}/{n_tot} pass (rel <= 1e-10)")
for c in fails[:30]:
    print("  FAIL", c["quantity"], c["group"], c["pair"], f"prod {c['production']:.15e} ref {c['reference']} rel {c['rel_error']:.2e} abs {c['abs_error']:.2e}")
print("worst relative errors:", json.dumps({k: f"{v:.1e}" for k, v in list(out["summary"]["worst_rel_by_quantity_group"].items())[:12]}))

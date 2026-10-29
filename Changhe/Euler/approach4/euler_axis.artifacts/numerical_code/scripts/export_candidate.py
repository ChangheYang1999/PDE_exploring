"""Export a run's final state in the SPEC 10 exchange format:
  candidates/<branch>/<level>/{candidate.json, coeffs.npz, BASIS.md, field_eval.py, samples.npz}
Usage: python3 scripts/export_candidate.py <run_dir> <branch> <level> [--note "..."]
field_eval.py is numpy-only and self-contained (it reads coeffs.npz next to it); BASIS.md gives the complete definition.
"""
import os, sys, json, math, hashlib, time, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
import numpy as np, torch
from axi.problem import Problem, Config, alpha_of
from axi import ops, pressure
torch.set_default_dtype(torch.float64)

FIELD_EVAL = r'''"""Self-contained numpy evaluator of a candidate (phi, q) from coeffs.npz (SPEC 10). Values only.
Usage: from field_eval import eval_phi_q; phi, q = eval_phi_q(r, z)    (r, z arrays of equal shape)
Definitions: see BASIS.md next to this file. Written by scripts/export_candidate.py of the numerics lane."""
import os, json
import numpy as np
from numpy.polynomial import legendre as _Leg, chebyshev as _Cheb

_HERE = os.path.dirname(os.path.abspath(__file__))
_D = np.load(os.path.join(_HERE, "coeffs.npz"), allow_pickle=False)
_M = json.loads(str(_D["meta_json"]))

def _legendre_matrix(mu, nmax):
    return np.array([_Leg.legval(mu, np.eye(nmax + 1)[n]) for n in range(nmax + 1)]).T          # (npts, nmax+1)

def _jacobi(x, kmax, a, b):
    """P_k^{(a,b)}(x), k = 0..kmax (three-term recurrence); (len(x), kmax+1)."""
    x = np.asarray(x, float); P = np.zeros((x.size, kmax + 1)); P[:, 0] = 1.0
    if kmax >= 1: P[:, 1] = 0.5 * ((a + b + 2) * x + (a - b))
    for k in range(1, kmax):
        c = 2 * k + a + b
        P[:, k + 1] = ((c + 1) * ((c + 2) * c * x + a * a - b * b) * P[:, k] - 2 * (k + a) * (k + b) * (c + 2) * P[:, k - 1]) / (2 * (k + 1) * (k + a + b + 1) * c)
    return P

def _element_basis(el, R, mu):
    """Columns of the element's basis at points (R, mu), in the coefficient order of BASIS.md."""
    nmax = el["nmax"]; P = _legendre_matrix(mu, nmax)
    cols = []
    if el["kind"] == "ball":
        R1 = el["Rhi"]; D = el["D"]; rho = R / R1; x = 2 * rho**2 - 1
        radial = el.get("radial", "cheb")
        for n in range(nmax + 1):
            Kn = (D - n) // 2
            if Kn < 0: continue
            Q = _jacobi(x, Kn, 0.0, n + 0.5) if radial == "jacobi" else None
            for k in range(Kn + 1):
                qk = Q[:, k] if radial == "jacobi" else _Cheb.chebval(x, np.eye(Kn + 1)[k])
                cols.append(P[:, n] * rho**n * qk)
    elif el["kind"] == "shell":
        Rlo, Rhi, K = el["Rlo"], el["Rhi"], el["K"]
        x = 2 * np.log(R / Rlo) / np.log(Rhi / Rlo) - 1
        for n in range(nmax + 1):
            for k in range(K + 1):
                cols.append(P[:, n] * _Cheb.chebval(x, np.eye(K + 1)[k]))
    elif el["kind"] == "exterior":
        Rm = el["Rlo"]
        for n in range(nmax + 1):
            for e in el["exponents"]:
                cols.append(P[:, n] * (R / Rm) ** (-e))
    return np.array(cols).T if cols else np.zeros((len(R), 0))

def eval_phi_q(r, z):
    r = np.asarray(r, float); z = np.asarray(z, float); shp = r.shape
    r = r.ravel(); z = z.ravel()
    R = np.sqrt(r * r + z * z); mu = np.where(R > 0, z / np.where(R > 0, R, 1.0), 1.0)
    phi = np.zeros_like(R); q = np.zeros_like(R)
    els = _M["elements"]
    for i, el in enumerate(els):
        lo = el["Rlo"] if i > 0 else -1.0
        m = (R > lo) & (R <= el["Rhi"]) if el["Rhi"] is not None else (R > lo)
        if not np.any(m): continue
        B = _element_basis(el, R[m], mu[m])
        cphi = _D[f"phi_el{i}"]; cq = _D[f"q_el{i}"]
        Bphi = B[:, el["phi_cols"]]; Bq = B[:, el["q_cols"]]        # column subsets (exponent sets, parity masks)
        phi[m] = Bphi @ cphi; q[m] = Bq @ cq
    return phi.reshape(shp), q.reshape(shp)

if __name__ == "__main__":
    S = np.load(os.path.join(_HERE, "samples.npz"))
    phi, q = eval_phi_q(S["r"], S["z"])
    print("max |phi - samples|:", np.max(np.abs(phi - S["phi"])), " max |q - samples|:", np.max(np.abs(q - S["q"])))
'''


def main():
    run_dir, branch, level = sys.argv[1], sys.argv[2], sys.argv[3]
    note = sys.argv[sys.argv.index("--note") + 1] if "--note" in sys.argv else ""
    d = torch.load(os.path.join(run_dir, "final.pt"), weights_only=False, map_location="cpu")
    prob, x = Problem.from_state(d, device="cpu"); cfg = prob.cfg       # c_l and exponents from the FINAL state (free-c_l runs)
    res = json.load(open(os.path.join(run_dir, "result.json"))) if os.path.exists(os.path.join(run_dir, "result.json")) else {}
    out = os.path.join(ROOT, "candidates", branch, level); os.makedirs(out, exist_ok=True)
    cphi, cq, _ = prob.split(x)
    alpha = prob.alpha
    # coefficient arrays and metadata
    arrays = {}; els = []
    for i, e in enumerate(prob.elements):
        arrays[f"phi_el{i}"] = cphi[i].numpy(); arrays[f"q_el{i}"] = cq[i].numpy()
        el = dict(kind=e.kind, Rlo=float(e.Rlo), Rhi=(None if math.isinf(e.Rhi) else float(e.Rhi)), nmax=int(e.nmax))
        if e.kind == "ball": el["D"] = int(e.params["D"]); el["radial"] = e.params.get("radial", "cheb")
        if e.kind == "shell": el["K"] = int(e.params["K"]); el["map"] = "log"
        el["phi_cols"] = [int(j) for j in prob.cols_phi[i]]; el["q_cols"] = [int(j) for j in prob.cols_q[i]]
        if e.kind == "exterior":
            el["exponents"] = [float(v) for v in e.params["exponents"]]
            el["labels_phi"] = [[int(n), float(ex)] for (n, ex) in prob.ext_labels_phi]; el["labels_q"] = [[int(n), float(ex)] for (n, ex) in prob.ext_labels_q]
            el["exponents_phi"] = sorted(set(float(ex) for (n, ex) in prob.ext_labels_phi)); el["exponents_q"] = sorted(set(float(ex) for (n, ex) in prob.ext_labels_q))
        el["labels"] = [[int(l[0]), float(l[1])] for l in e.labels]
        els.append(el)
    meta = dict(cl=prob.cl, alpha=alpha, elements=els, z0=prob.z0_of(x), s1_constraint=cfg.s1_constraint, q0_pin=cfg.q0_pin,
                parity=dict(phi=cfg.parity_phi, q=cfg.parity_q), point_rows=cfg.point_rows, K_param=cfg.K_param, slave_correction=cfg.slave_correction)
    arrays["meta_json"] = np.array(json.dumps(meta))
    np.savez(os.path.join(out, "coeffs.npz"), **arrays)
    open(os.path.join(out, "field_eval.py"), "w").write(FIELD_EVAL)
    # samples: a grid over core, axis, matching zone and far field, with U, P
    Rs = np.concatenate([np.linspace(0.05, prob.cfg.R1, 20), np.geomspace(prob.cfg.R1, prob.Rm, 15)[1:], np.geomspace(prob.Rm, 1e3 * prob.Rm, 12)[1:]])
    mus = np.concatenate([np.linspace(-1, 1, 17)])
    RR, MM = np.meshgrid(Rs, mus, indexing="ij"); R = RR.ravel(); mu = MM.ravel()
    phi, q = prob.eval_all(x, R, mu)
    g = ops.geom(torch.tensor(R), torch.tensor(mu))
    P = ops.primitive_terms(phi, q, g, prob.cl)
    ps = pressure.solver_for_candidate(prob, x)
    pr = ps.evaluate(R, mu)
    r = R * np.sqrt(np.clip(1 - mu**2, 0, None)); z = R * mu
    np.savez(os.path.join(out, "samples.npz"), r=r, z=z, R=R, mu=mu, phi=phi[(0, 0)].numpy(), q=q[(0, 0)].numpy(), Ur=P["Ur"].numpy(), Utheta=P["Ut"].numpy(),
             Uz=P["Uz"].numpy(), P=pr["P"], eta=ops.eta_and_grad(phi, g)[(0, 0)].numpy())
    # BASIS.md
    ext = els[-1]
    shells_txt = "\n".join(f"  element {i}: shell R in [{el['Rlo']}, {el['Rhi']}], Chebyshev degree K = {el['K']} in x = 2 ln(R/Rlo)/ln(Rhi/Rlo) - 1, Legendre degree nmax = {el['nmax']}; "
                           f"basis column (n, k) = P_n(mu) T_k(x), ordered n-major (n = 0..nmax, k = 0..K): {len(el['labels'])} columns"
                           for i, el in enumerate(els) if el["kind"] == "shell")
    basis_md = f"""# BASIS.md: complete definition of the candidate representation (branch {branch}, level {level})

Generated {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} from {os.path.relpath(run_dir, ROOT)} by scripts/export_candidate.py. {note}

## Coordinates
Spherical R = sqrt(r^2 + z^2), mu = z/R (mu = +1 on the positive z axis). All fields are axisymmetric scalars of (R, mu).
Reduced variables (SPEC 1): U^r = -r d_z phi, U^z = 2 phi + r d_r phi, U^theta = r q; eta = -Delta_5 phi, Delta_5 = d_rr + (3/r) d_r + d_zz.
Formulation B: phi and q are the primary unknowns; eta is derived (R_ell = 0 identically).
c_l = {prob.cl!r} ({'free' if cfg.free_cl else 'fixed'}), alpha = (1 - c_l)/c_l = {alpha!r}.

## Elements (piecewise in R; same Legendre basis P_n(mu), n = 0..nmax = {cfg.nmax}, in every element)
  element 0: ball R in [0, {cfg.R1}]: basis column (n, k) = P_n(mu) rho^n Q_k(2 rho^2 - 1), rho = R/{cfg.R1}, for n + 2k <= D = {cfg.D},
  with Q_k = {'the Jacobi polynomial P_k^(0, n+1/2) (3D Zernike radial family, three-term recurrence as in field_eval.py)' if cfg.ball_radial == 'jacobi' else 'the Chebyshev polynomial T_k'};
  ordered n-major (n = 0..nmax, then k = 0..floor((D - n)/2)): {len(els[0]['labels'])} columns.  Every column is an axisymmetric Cartesian
  polynomial of degree <= D (regular in (r^2, z) at the axis and origin by construction); with nmax < D the span is the subspace
  whose solid-harmonic content has degree <= nmax (solid harmonics of degree nmax+1..D are absent).
{shells_txt}
  element {len(els)-1}: exterior R in [{ext['Rlo']}, infinity): basis column (n, e) = P_n(mu) (R/{ext['Rlo']})^(-e); the fractional power law is factored
  analytically (no compactification).  Exponent set of the node/basis union, ordered n-major then by e ascending:
  e in {ext['exponents']}.
  phi uses only the columns with e in {ext['exponents_phi']} (column indices phi_cols in coeffs.npz meta),
  q uses only the columns with e in {ext['exponents_q']} (q_cols).  The exponents are of the form m alpha + k (m, k integers):
  phi: generated from {{alpha}} U {{3, 4, 5, ...}} under (a, b) -> a + b + 1 up to emax = {cfg.emax}; q: {{alpha + 1}} closed under (a_phi, b_q) -> a + b + 1.
  So the exterior can express R^-alpha, R^-(2 alpha + 1) (first nonlinear correction), R^-3 (5D monopole d_0, kept as a test), R^-4, R^-(3 alpha + 2), ...
  Exponents closer than merge_tol = {cfg.merge_tol} were merged (near-resonant pairs).
  Leading tail: phi -> R^-alpha A(mu) with A(mu) = sum_n a_n P_n(mu), a_n = coefficient(n, alpha) * Rm^alpha; q -> R^-(alpha+1) B(mu) likewise with Rm^(alpha+1).

## Coefficient arrays (coeffs.npz)
phi_el<i>, q_el<i>: float64 vectors in the column order above restricted to the column subsets phi_cols / q_cols of meta_json (exponent
sets for the exterior; Legendre-parity masks {cfg.parity_phi!r} for phi and {cfg.parity_q!r} for q in every element).
meta_json: JSON with c_l, alpha, the element table (Rlo, Rhi, nmax, D or K or exponents, labels [n, k-or-e] per column, phi_cols, q_cols), z0.
Shapes: {', '.join(f'{k}: {v.shape}' for k, v in arrays.items() if k != 'meta_json')}.

## Continuity, gauge, constraints (how the state was obtained; not part of the definition of the fields)
Interface rows impose phi in C^3 and q in C^2 across R = {[el['Rhi'] for el in els[:-1]]} by least squares (weight {cfg.w_int}); the jumps are
reported in the candidate's validation.  Working gauge: int_S2 {'F_theta^2' if cfg.gauge == 'swirl' else '|F|^2'} dS = {prob.cfg.gauge_target!r} on the leading tail; the
conversion factor to the reporting gauge int |F|^2 dS = 1 is L = (int |F|^2 dS)^(-1/(2(1 + alpha))) (fields transform as phi_L(y) = L phi(y/L), q_L(y) = q(y/L)).
{'S1 rows: phi_z(0, z0) = 1/2 and c_l z0 + 2 phi(0, z0) = 0 with z0 = ' + repr(prob.z0_of(x)) + (' and q(0, z0) pinned to ' + repr(cfg.q0_pin) if cfg.q0_pin is not None else '') + '.' if cfg.s1_constraint else 'No S1 rows.'}

## Evaluation
field_eval.py (numpy only) implements exactly the above and reproduces samples.npz (r, z, phi, q, U^r, U^theta, U^z, P, eta).
Nothing in this file is defined by reference to code.
"""
    open(os.path.join(out, "BASIS.md"), "w").write(basis_md)
    val = res.get("validation") or {}
    full, sw, pol = prob.tail_integrals(cphi[-1], cq[-1], alpha)
    cand = dict(id=f"{branch}/{level}", branch=branch, level=level, run_id=os.path.basename(os.path.normpath(run_dir)), cl=prob.cl, cl_free=cfg.free_cl, alpha=alpha,
                working_gauge=dict(kind=cfg.gauge, target=prob.cfg.gauge_target, int_F2=full, int_Ftheta2=sw),
                L_to_reporting_gauge=(full ** (-1.0 / (2 * (1 + alpha))) if full > 0 else None), a_eff=val.get("a_eff"),
                representation="ball(Cartesian polynomial, D) + log-Chebyshev shells + factored power-law exterior; formulation B (phi, q)",
                resolution=dict(D=cfg.D, nmax=cfg.nmax, shells=cfg.shells, emax=cfg.emax, nR_ball=cfg.nR_ball, nR_shell=cfg.nR_shell, nR_ext=cfg.nR_ext, nmu=prob.nmu),
                quadrature="Gauss-Legendre tensor nodes per element (ball in x = 2 rho^2 - 1, shells in log R, exterior in log R to Tmax)",
                created=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), source_hash=hashlib.sha256(open(os.path.join(ROOT, "src", "axi", "problem.py"), "rb").read()).hexdigest()[:16],
                self_measured=dict(rho_max=val.get("rho_max"), m_max=val.get("m_max"), per_equation=val.get("rho_max_by_eq"), s_core=val.get("s_core"), s_far=val.get("s_far"),
                                   cost=res.get("cost"), holdout_rel_Rq=res.get("report", {}).get("rel_Rq_inner"), holdout_rel_Reta=res.get("report", {}).get("rel_Reta_inner")),
                z0=prob.z0_of(x), q0_pin=cfg.q0_pin, note=note, status="pilot state, NOT a candidate solution; exported so that the loader can be exercised" if (val.get("rho_max") or 1) > 1e-2 else "")
    json.dump(cand, open(os.path.join(out, "candidate.json"), "w"), indent=1, default=float)
    # self-test of field_eval against the problem's own evaluation
    sys.path.insert(0, out)
    import importlib, field_eval as fe
    importlib.reload(fe)
    p2, q2 = fe.eval_phi_q(r, z)
    err = max(np.max(np.abs(p2 - phi[(0, 0)].numpy())), np.max(np.abs(q2 - q[(0, 0)].numpy())))
    print(f"exported to {out}; field_eval self-test max abs error {err:.2e}")
    with open(os.path.join(out, "SELFTEST.txt"), "w") as f:
        f.write(f"field_eval.py vs lane evaluation: max abs error {err:.3e} on {len(r)} sample points\n")


if __name__ == "__main__":
    main()

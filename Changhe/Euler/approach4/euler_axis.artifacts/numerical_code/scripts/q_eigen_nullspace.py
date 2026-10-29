"""Lead note 26 item 2: does the frozen-phi swirl operator have a near-null space?  For the frozen (phi, c_l) of a state:
  (a) singular values of the pinned (null-space-reduced), column-normalized q operator AN/cs (the weighted q rows of the job);
      smallest ten relative to the largest, and the fraction of ||q_eig - q_state|| carried by the k smallest singular directions;
      truncated-SVD solutions (k smallest directions removed) with their holdout floor and distance to the state's q;
  (b) near-source jets of the state's q and of the eigen-solved q (q, q_z, q_rr, q_zz at the source (0, z0) by Richardson finite
      differences, h = 2e-3 and 1e-3) against the local closure q_z = 4 K h_2 / delta with h_2 = phi_zz(0, z0)/2, delta = 1 + c_l
      (audit 5e (vii) (d)); the curvature combination 4 q_rr delta and (delta^2 + K^2) q_zz is reported for the lead's identity;
  (c) the eigen-solved and the state's q residual restricted to R < 0.1 (fine polar grid around the origin) and to the source collar
      |y - (0, z0)| < 0.1.
Usage: CUDA_VISIBLE_DEVICES=<gpu> python3 scripts/q_eigen_nullspace.py <run_dir> [...]   -> runs/<id>/q_eigen_nullspace.json"""
import os, sys, json, math
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
import numpy as np, torch
from axi.problem import Problem
from axi import diagnostics
torch.set_default_dtype(torch.float64)
dev = "cuda" if torch.cuda.is_available() else "cpu"


def rz_to_Rmu(r, z):
    R = np.sqrt(r * r + z * z); R = np.maximum(R, 1e-300)
    return R, np.clip(z / R, -1.0, 1.0)


def jet_at_source(prob, x, which, z0, h):
    """value, d/dz, d2/dr2, d2/dz2 at (0, z0) by central differences of step h (q, phi are even in r: f_rr(0) = 2 (f(h) - f(0))/h^2)."""
    pts = np.array([[0.0, z0], [0.0, z0 + h], [0.0, z0 - h], [h, z0]])
    R, mu = rz_to_Rmu(pts[:, 0], pts[:, 1])
    f = prob.eval_field(x, which, R, mu)
    f = np.asarray(f, float)
    return dict(val=f[0], dz=(f[1] - f[2]) / (2 * h), drr=2.0 * (f[3] - f[0]) / h ** 2, dzz=(f[1] - 2 * f[0] + f[2]) / h ** 2)


def richardson(prob, x, which, z0, h=2e-3):
    a = jet_at_source(prob, x, which, z0, h); b = jet_at_source(prob, x, which, z0, h / 2)
    return {k: (4 * b[k] - a[k]) / 3 if k != "val" else a[k] for k in a}, {k: abs(a[k] - b[k]) for k in a}


def rel_res_on(prob, xx, R, mu, cl):
    f = diagnostics.residual_fields(prob, xx.cpu(), R, mu, cl)
    Rq = np.asarray(f["Rq"], float); tq = np.asarray(f["terms_q"], float)
    return float(np.sqrt(np.mean(Rq ** 2)) / max(np.sqrt(np.mean(tq ** 2)), 1e-300)), float(np.max(np.abs(Rq)) / max(np.max(np.abs(tq)), 1e-300))


for run_dir in sys.argv[1:]:
    d = torch.load(os.path.join(run_dir, "final.pt"), weights_only=False, map_location="cpu")
    prob, x = Problem.from_state(d, device=dev)
    cl = prob.cl_of(x); z0 = prob.z0_of(x) or 0.0; q0 = prob.cfg.q0_pin; delta = 1.0 + cl
    J = prob.jacobian(x)
    n0 = 0; rows = []
    for i in range(prob.nel):
        n = prob.n_nodes_per_el[i]; rows += list(range(n0, n0 + n)); n0 += 2 * n
    qcols = list(range(prob.nphi, prob.nphi + prob.nq))
    A = J[rows][:, qcols].cpu().numpy()
    _, _, _, mu0, s_full, _ = prob.axis_phi_rows(z0, with_q=True)
    s = s_full[prob.nphi:prob.nphi + prob.nq]
    c_p = s * (q0 / float(s @ s))
    Qm, _ = np.linalg.qr(s[:, None], mode="complete"); N = Qm[:, 1:]
    AN = A @ N; b = -(A @ c_p)
    cs = np.max(np.abs(AN), axis=0); cs[cs == 0] = 1.0
    M = AN / cs
    U, S, Vt = np.linalg.svd(M, full_matrices=False)
    qs = x[prob.nphi:prob.nphi + prob.nq].cpu().numpy()
    # full least-squares eigen solution
    y_full = Vt.T @ ((U.T @ b) / S); c_eig = c_p + N @ (y_full / cs)
    diff = c_eig - qs
    # the difference in the reduced, normalized coordinates: y-space components along the right singular vectors
    y_state = cs * (N.T @ (qs - c_p))                          # state's q in the reduced normalized coordinates (pin part removed)
    dy = y_full - y_state
    comp = Vt @ dy                                           # components along right singular vectors (ordered by decreasing S)
    frac_smallest = {}
    for k in (1, 2, 3, 5, 10, 20, 50):
        if k < len(S):
            frac_smallest[k] = float(np.sum(comp[-k:] ** 2) / max(np.sum(comp ** 2), 1e-300))
    out = dict(cl=cl, q0=q0, z0=z0, D=prob.cfg.D, nmax=prob.cfg.nmax, n_qrows=A.shape[0], nq=prob.nq,
               sv_largest=float(S[0]), sv_smallest10_rel=[float(v / S[0]) for v in S[-10:]], sv_rel_below=dict(
                   e3=int(np.sum(S / S[0] < 1e-3)), e4=int(np.sum(S / S[0] < 1e-4)), e5=int(np.sum(S / S[0] < 1e-5)), e6=int(np.sum(S / S[0] < 1e-6)), e8=int(np.sum(S / S[0] < 1e-8))),
               condition=float(S[0] / S[-1]), q_coeff_rel_diff_full=float(np.linalg.norm(diff) / np.linalg.norm(qs)),
               frac_of_diff_in_k_smallest_directions=frac_smallest)
    # holdout grids
    H = diagnostics.holdout_points(prob); Rh, muh, kind = H["R"], H["mu"], H["kind"]; inner = kind < 2
    # fine grid R < 0.1 around the origin and the source collar
    Rf = np.exp(np.linspace(np.log(0.004), np.log(0.1), 24)); muf = np.cos(np.linspace(0.02, np.pi - 0.02, 33))
    RR, MM = np.meshgrid(Rf, muf, indexing="ij"); RR = RR.ravel(); MM = MM.ravel()
    rho_c = np.linspace(0.003, 0.1, 20); th_c = np.linspace(0.0, np.pi, 25)
    rr = np.outer(rho_c, np.sin(th_c)).ravel(); zz = z0 + np.outer(rho_c, np.cos(th_c)).ravel()
    Rc, muc = rz_to_Rmu(rr, zz)

    def evaluate(tag, xx):
        rel_in, _ = rel_res_on(prob, xx, Rh[inner], muh[inner], cl)
        rel_R01, max_R01 = rel_res_on(prob, xx, RR, MM, cl)
        rel_col, max_col = rel_res_on(prob, xx, Rc, muc, cl)
        jq, eq = richardson(prob, xx, "q", z0)
        return dict(rel_Rq_inner=rel_in, rel_Rq_R_lt_0p1=rel_R01, relmax_Rq_R_lt_0p1=max_R01, rel_Rq_source_collar=rel_col, relmax_Rq_source_collar=max_col,
                    jet_q=jq, jet_q_fd_err=eq)

    res = {}
    for tag, xx in (("state", x), ("eigen_full", torch.cat([x[:prob.nphi], torch.tensor(c_eig, device=dev), x[prob.nphi + prob.nq:]]))):
        res[tag] = evaluate(tag, xx)
    # truncated SVD: remove the k smallest directions
    tsvd = {}
    for k in (1, 2, 3, 5, 10, 20):
        if k >= len(S):
            continue
        Sk = S.copy(); Sk[-k:] = np.inf
        y_k = Vt.T @ ((U.T @ b) / Sk); c_k = c_p + N @ (y_k / cs)
        xk = torch.cat([x[:prob.nphi], torch.tensor(c_k, device=dev), x[prob.nphi + prob.nq:]])
        r = evaluate("tsvd", xk)
        tsvd[k] = dict(rel_Rq_inner=r["rel_Rq_inner"], rel_Rq_R_lt_0p1=r["rel_Rq_R_lt_0p1"], rel_Rq_source_collar=r["rel_Rq_source_collar"],
                       q_coeff_rel_diff=float(np.linalg.norm(c_k - qs) / np.linalg.norm(qs)), weighted_cost_q_rows=float(0.5 * np.sum((AN @ (y_k / cs) - b) ** 2)))
    out["tsvd"] = tsvd
    # phi jet at the source and the closure prediction
    jphi, ephi = richardson(prob, x, "phi", z0)
    h2 = 0.5 * jphi["dzz"]
    out["phi_jet_at_source"] = dict(phi=jphi["val"], phi_z=jphi["dz"], phi_zz=jphi["dzz"], phi_rr=jphi["drr"], fd_err=ephi, h2=h2,
                                    s1_rows=dict(phi_z_minus_half=jphi["dz"] - 0.5, cl_z0_plus_2phi=cl * z0 + 2 * jphi["val"]))
    K = res["state"]["jet_q"]["val"]
    for tag in res:
        jq = res[tag]["jet_q"]; Kt = jq["val"]
        res[tag]["closure"] = dict(q_z_predicted_4Kh2_over_delta=4 * Kt * h2 / delta, q_z_measured=jq["dz"],
                                   curvature_lhs_4_delta_qrr=4 * delta * jq["drr"], curvature_lhs_delta2_K2_qzz=(delta ** 2 + Kt ** 2) * jq["dzz"],
                                   curvature_rhs=3 * (delta ** 2 + 2 * Kt ** 2) * jq["dz"] ** 2 / (2 * Kt) if Kt != 0 else None)
    out["results"] = res
    out["weighted_cost_q_rows"] = dict(state=float(0.5 * np.sum((A @ qs) ** 2)), eigen_full=float(0.5 * np.sum((A @ c_eig) ** 2)))
    json.dump(out, open(os.path.join(run_dir, "q_eigen_nullspace.json"), "w"), indent=1, default=float)
    jid = os.path.basename(run_dir)
    print(f"== {jid[:50]} c_l {cl:.4f} q0 {q0} z0 {z0:.4f} D{prob.cfg.D}/n{prob.cfg.nmax}: q rows {A.shape[0]} x nq {prob.nq}")
    print("   singular values (smallest 10, relative):", ["%.2e" % v for v in out["sv_smallest10_rel"]], "condition %.2e" % out["condition"])
    print("   count below 1e-3/1e-4/1e-5/1e-6/1e-8:", out["sv_rel_below"])
    print("   |q_eig - q|/|q| = %.3f; fraction of the difference in the k smallest directions:" % out["q_coeff_rel_diff_full"], {k: "%.3f" % v for k, v in frac_smallest.items()})
    for tag, r in res.items():
        print(f"   {tag:11s}: rel R_q inner {r['rel_Rq_inner']:.3e}  R<0.1 {r['rel_Rq_R_lt_0p1']:.3e} (max {r['relmax_Rq_R_lt_0p1']:.2e})  source collar {r['rel_Rq_source_collar']:.3e} (max {r['relmax_Rq_source_collar']:.2e})")
        jq = r["jet_q"]; c = r["closure"]
        print(f"               jet: q {jq['val']:.4f} q_z {jq['dz']:.4f} (closure {c['q_z_predicted_4Kh2_over_delta']:.4f}) q_rr {jq['drr']:.3f} q_zz {jq['dzz']:.3f}; curvature terms 4 delta q_rr {c['curvature_lhs_4_delta_qrr']:.3f}, (delta^2+K^2) q_zz {c['curvature_lhs_delta2_K2_qzz']:.3f}, rhs {c['curvature_rhs']:.3f}")
    print("   phi jet: phi_z - 1/2 = %.2e, c z0 + 2 phi = %.2e, h2 = phi_zz/2 = %.4f" % (out["phi_jet_at_source"]["s1_rows"]["phi_z_minus_half"], out["phi_jet_at_source"]["s1_rows"]["cl_z0_plus_2phi"], h2))
    for k, t in tsvd.items():
        print(f"   TSVD drop {k:2d}: rel R_q inner {t['rel_Rq_inner']:.3e}  R<0.1 {t['rel_Rq_R_lt_0p1']:.3e}  collar {t['rel_Rq_source_collar']:.3e}  |q_k - q|/|q| {t['q_coeff_rel_diff']:.3f}")

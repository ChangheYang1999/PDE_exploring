"""Lead note 29 item 2 and note 30 item 2: value-based comparison of the frozen-phi slaved swirl q* with the state's q, for one state.
  (a) per dyadic shell (units R1): max|q*|, max|q_state|, sup and L2 norms of q* - q_state on the holdout grid; max|grad q*|, max|grad q_state|;
  (b) where the eta-row cost of (phi, q*) sits: weighted eta-row cost per element and per dyadic shell, with the top rows;
  (c) smallest ten singular values of the pinned, column-normalized weighted q operator (PDE q rows) and the support of the right singular
      vectors (fraction of the coefficient-vector norm in the ball, the shells, the exterior leading column, the other exterior columns);
  (d) the leading far-swirl coefficient B(mu) of q* and of the state (Legendre coefficients, min/max on [-1, 1], sign changes);
  (e) note 30: q* - q_state on source-adaptive points (|x - x*| = 1e-1, 1e-2, 1e-3, 1e-4 times a_eff, 64 directions each) with the
      gradient magnitudes there.
Usage: CUDA_VISIBLE_DEVICES= python3 scripts/q_eigen_values.py <run_dir>   -> runs/<id>/q_eigen_values.json and a text summary."""
import os, sys, json, math
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
import numpy as np, torch
from numpy.polynomial import legendre as L
from axi.problem import Problem
from axi import diagnostics, validate, ops
torch.set_default_dtype(torch.float64); torch.set_num_threads(1)
dev = "cpu"


def rz_to_Rmu(r, z):
    R = np.sqrt(r * r + z * z); R = np.maximum(R, 1e-300)
    return R, np.clip(z / R, -1.0, 1.0)


def grad_q(prob, x, R, mu):
    phi, q = prob.eval_all(x, R, mu)
    g = ops.geom(torch.tensor(np.asarray(R, float)), torch.tensor(np.asarray(mu, float)))
    qr, qz = ops.grad_rz(q, g)
    return q[(0, 0)].numpy(), np.sqrt(qr.numpy() ** 2 + qz.numpy() ** 2)


run_dir = sys.argv[1].rstrip("/")
inner_mode = sys.argv[sys.argv.index("--inner") + 1] if "--inner" in sys.argv else "full"
d = torch.load(os.path.join(run_dir, "final.pt"), weights_only=False, map_location="cpu")
prob, x = Problem.from_state(d, device=dev)
cl = prob.cl_of(x); z0 = prob.z0_of(x) or 0.0; q0 = prob.cfg.q0_pin; alpha = prob.alpha
val = json.load(open(os.path.join(run_dir, "validation.json"))) if os.path.exists(os.path.join(run_dir, "validation.json")) else {}
a_eff = val.get("a_eff") or 1.0
# frozen-phi q*: inner rows = PDE q rows (--inner pde: the scripts/q_eigen_floor.py definition, which has NO interface rows and therefore
# gives q* = 0 outside the ball) or PDE q rows + q interface-continuity rows + q Tikhonov rows + q-correction slave rows (--inner full,
# default: the lm.VarProProblem definition; q* continuous across the elements); hard pin by null-space elimination in both cases
J = prob.jacobian(x)
n0 = 0; rows = []
for i in range(prob.nel):
    n = prob.n_nodes_per_el[i]; rows += list(range(n0, n0 + n)); n0 += 2 * n
qcols = list(range(prob.nphi, prob.nphi + prob.nq))
if inner_mode == "full":
    from axi import lm as _lm
    vp = _lm.VarProProblem(prob, full=False, trunc_rel=0.0)
    rows_in = vp.inner
else:
    rows_in = rows
A = J[rows_in][:, qcols].numpy()
_, _, _, mu0, s_full, _ = prob.axis_phi_rows(z0, with_q=True)
s = s_full[prob.nphi:prob.nphi + prob.nq]
c_p = s * (q0 / float(s @ s))
Qm, _ = np.linalg.qr(s[:, None], mode="complete"); N = Qm[:, 1:]
AN = A @ N; b = -(A @ c_p)
cs = np.max(np.abs(AN), axis=0); cs[cs == 0] = 1.0
M = AN / cs
U, S, Vt = np.linalg.svd(M, full_matrices=False)
y = Vt.T @ ((U.T @ b) / S); c_eig = c_p + N @ (y / cs)
qs = x[qcols].numpy()
x_eig = x.clone(); x_eig[qcols] = torch.tensor(c_eig)
out = dict(cl=cl, q0=q0, z0=z0, D=prob.cfg.D, nmax=prob.cfg.nmax, a_eff=a_eff, inner_mode=inner_mode, n_inner_rows=len(rows_in))
# PDE q-row floor of q* (weighted) and holdout relative q residual per shell (the q_eigen_floor numbers, now for this q*)
A_pde = J[rows][:, qcols].numpy()
out["pde_q_rows_cost"] = dict(state=float(0.5 * np.sum((A_pde @ qs) ** 2)), eigen=float(0.5 * np.sum((A_pde @ c_eig) ** 2)))

# (a) per-shell values on the holdout grid
H = diagnostics.holdout_points(prob); R, mu, kind = H["R"], H["mu"], H["kind"]
qv_s, gq_s = grad_q(prob, x, R, mu); qv_e, gq_e = grad_q(prob, x_eig, R, mu)
sid = np.clip(np.floor(np.log2(np.maximum(R / prob.cfg.R1, 1e-300))).astype(int), -6, None)
per = {}
for sh in np.unique(sid):
    m = sid == sh; dq = qv_e[m] - qv_s[m]
    per[int(sh)] = dict(Rlo=float(prob.cfg.R1 * 2.0 ** sh), n=int(m.sum()), max_q_eig=float(np.max(np.abs(qv_e[m]))), max_q_state=float(np.max(np.abs(qv_s[m]))),
                        sup_diff=float(np.max(np.abs(dq))), l2_diff=float(np.sqrt(np.mean(dq ** 2))), l2_state=float(np.sqrt(np.mean(qv_s[m] ** 2))),
                        max_grad_q_eig=float(np.max(gq_e[m])), max_grad_q_state=float(np.max(gq_s[m])))
out["per_shell"] = per
inner = kind < 2
fq_s = diagnostics.residual_fields(prob, x, R, mu, cl); fq_e = diagnostics.residual_fields(prob, x_eig, R, mu, cl)
relq = {}
for sh in np.unique(sid):
    m = sid == sh
    relq[int(sh)] = dict(state=float(np.sqrt(np.mean(fq_s["Rq"][m] ** 2)) / max(np.sqrt(np.mean(fq_s["terms_q"][m] ** 2)), 1e-300)),
                         eigen=float(np.sqrt(np.mean(fq_e["Rq"][m] ** 2)) / max(np.sqrt(np.mean(fq_e["terms_q"][m] ** 2)), 1e-300)))
out["rel_Rq_per_shell"] = relq
out["rel_Rq_inner"] = dict(state=float(np.sqrt(np.mean(fq_s["Rq"][inner] ** 2)) / np.sqrt(np.mean(fq_s["terms_q"][inner] ** 2))),
                           eigen=float(np.sqrt(np.mean(fq_e["Rq"][inner] ** 2)) / np.sqrt(np.mean(fq_e["terms_q"][inner] ** 2))))
out["inner_values"] = dict(sup_diff=float(np.max(np.abs(qv_e[inner] - qv_s[inner]))), l2_diff_rel=float(np.sqrt(np.mean((qv_e[inner] - qv_s[inner]) ** 2)) / np.sqrt(np.mean(qv_s[inner] ** 2))),
                           max_q_eig=float(np.max(np.abs(qv_e[inner]))), max_q_state=float(np.max(np.abs(qv_s[inner]))))

# (b) eta-row cost of (phi, q*) by element and dyadic shell of the node
r_state = prob.residual(x).numpy(); r_eig = prob.residual(x_eig).numpy()
n0 = 0; eta_rows = []; eta_el = []
for i in range(prob.nel):
    n = prob.n_nodes_per_el[i]; eta_rows += list(range(n0 + n, n0 + 2 * n)); eta_el += [i] * n; n0 += 2 * n
eta_rows = np.array(eta_rows); eta_el = np.array(eta_el)
Rn = np.concatenate([np.asarray(e.R, float) for e in prob.elements]); mun = np.concatenate([np.asarray(e.mu, float) for e in prob.elements])
cost_el = {}
for i in range(prob.nel):
    m = eta_el == i
    cost_el[f"el{i}_{prob.elements[i].kind}"] = dict(state=float(0.5 * np.sum(r_state[eta_rows[m]] ** 2)), eigen=float(0.5 * np.sum(r_eig[eta_rows[m]] ** 2)))
sidn = np.clip(np.floor(np.log2(np.maximum(Rn / prob.cfg.R1, 1e-300))).astype(int), -6, None)
cost_sh = {}
for sh in np.unique(sidn):
    m = sidn == sh
    cost_sh[int(sh)] = dict(state=float(0.5 * np.sum(r_state[eta_rows[m]] ** 2)), eigen=float(0.5 * np.sum(r_eig[eta_rows[m]] ** 2)), n=int(m.sum()))
top = np.argsort(-np.abs(r_eig[eta_rows]))[:8]
out["eta_cost"] = dict(total_state=float(0.5 * np.sum(r_state[eta_rows] ** 2)), total_eigen=float(0.5 * np.sum(r_eig[eta_rows] ** 2)), by_element=cost_el, by_shell=cost_sh,
                       top_rows_eigen=[dict(R=float(Rn[t]), mu=float(mun[t]), weighted_res=float(r_eig[eta_rows][t]), state_res=float(r_state[eta_rows][t])) for t in top],
                       cost_all_rows=dict(state=float(0.5 * r_state @ r_state), eigen=float(0.5 * r_eig @ r_eig)))
# other row blocks at (phi, q*)
out["cost_breakdown_eigen"] = prob.cost_breakdown(x_eig); out["cost_breakdown_state"] = prob.cost_breakdown(x)

# (c) singular values and right singular vectors' support (in coefficient space: c = N (v / cs))
supp = []
kinds = []
for i in range(prob.nel):
    kinds += [prob.elements[i].kind] * prob.nb_q[i]
kinds = np.array(kinds)
ext_lead = np.zeros(prob.nq, bool)
ie = prob.nel - 1; off = prob.off_q[ie] - prob.nphi
for t in prob.ext_lead_idx_q:
    ext_lead[off + t] = True
for k in range(1, 11):
    v = Vt[-k]; c = N @ (v / cs); c = c / np.linalg.norm(c)
    supp.append(dict(sigma_rel=float(S[-k] / S[0]), ball=float(np.sum(c[kinds == "ball"] ** 2)), shells=float(np.sum(c[kinds == "shell"] ** 2)),
                     ext_leading=float(np.sum(c[ext_lead] ** 2)), ext_other=float(np.sum(c[(kinds == "exterior") & ~ext_lead] ** 2))))
out["smallest_singular_directions"] = supp
out["sv_largest"] = float(S[0]); out["condition"] = float(S[0] / S[-1])

# (d) leading tail B(mu) of q* and of the state
def B_of(xx):
    cq_ext = xx[prob.off_q[ie]:prob.off_q[ie + 1]].numpy()
    bcoef = cq_ext[prob.ext_lead_idx_q] * prob.Rm ** (alpha + 1)
    full = np.zeros(prob.cfg.nmax + 1)
    for t, n in zip(range(len(bcoef)), prob.ext_lead_n_q):
        full[n] = bcoef[t]
    mu_g = np.linspace(-1, 1, 801); Bv = L.legval(mu_g, full)
    return dict(legendre=full.tolist(), min=float(Bv.min()), max=float(Bv.max()), sign_changes=int(np.sum(np.diff(np.sign(Bv)) != 0)), B_minus1=float(Bv[0]), B_plus1=float(Bv[-1]))
out["B_state"] = B_of(x); out["B_eigen"] = B_of(x_eig)

# (f) source jets of the state's q and of q* (Richardson central differences, h = 2e-3 and 1e-3) against the closure q_z = 4 K h_2/delta
def jet(xx, which, h):
    pts = np.array([[0.0, z0], [0.0, z0 + h], [0.0, z0 - h], [h, z0]]); Rj, muj = rz_to_Rmu(pts[:, 0], pts[:, 1])
    f = np.asarray(prob.eval_field(xx, which, Rj, muj), float)
    return dict(val=f[0], dz=(f[1] - f[2]) / (2 * h), drr=2.0 * (f[3] - f[0]) / h ** 2, dzz=(f[1] - 2 * f[0] + f[2]) / h ** 2)
def rich(xx, which):
    a = jet(xx, which, 2e-3); b_ = jet(xx, which, 1e-3)
    return {k: ((4 * b_[k] - a[k]) / 3 if k != "val" else a[k]) for k in a}
jphi = rich(x, "phi"); h2 = 0.5 * jphi["dzz"]; delta = 1.0 + cl
out["source_jets"] = dict(phi=jphi, h2=h2, closure_q_z=4 * q0 * h2 / delta, q_state=rich(x, "q"), q_eigen=rich(x_eig, "q"))
# (e) source-adaptive points
src = []
th = np.linspace(0, 2 * np.pi, 64, endpoint=False)
for rel in (1e-1, 1e-2, 1e-3, 1e-4):
    rho = rel * a_eff
    rr = np.abs(rho * np.sin(th)); zz = z0 + rho * np.cos(th)
    Rr, mur = rz_to_Rmu(rr, zz)
    qa, ga = grad_q(prob, x, Rr, mur); qb, gb = grad_q(prob, x_eig, Rr, mur)
    src.append(dict(dist_over_a_eff=rel, dist=float(rho), sup_diff=float(np.max(np.abs(qb - qa))), mean_diff=float(np.mean(qb - qa)), max_grad_state=float(ga.max()), max_grad_eig=float(gb.max()),
                    q_state_range=[float(qa.min()), float(qa.max())], q_eig_range=[float(qb.min()), float(qb.max())]))
out["source_adaptive"] = src
json.dump(out, open(os.path.join(run_dir, f"q_eigen_values_{inner_mode}.json"), "w"), indent=1, default=float)

print(f"== {os.path.basename(run_dir)[:50]} c_l {cl:.4f} q0 {q0} z0 {z0:.4f} D{prob.cfg.D}/n{prob.cfg.nmax} a_eff {a_eff:.3f}; inner rows: {inner_mode} ({len(rows_in)})")
print(f"    PDE q-row weighted cost: state {out['pde_q_rows_cost']['state']:.3e}, q* {out['pde_q_rows_cost']['eigen']:.3e}; holdout rel R_q inner: state {out['rel_Rq_inner']['state']:.3e}, q* {out['rel_Rq_inner']['eigen']:.3e}")
print("    holdout rel R_q per shell (state / q*):", {k: ("%.1e/%.1e" % (v["state"], v["eigen"])) for k, v in relq.items() if k <= 4})
print("(a) per shell (R1 units): shell Rlo | max|q*| max|q| | sup diff, L2 diff (L2 q) | max|grad q*| max|grad q|")
for sh, p in per.items():
    print(f"    {sh:3d} {p['Rlo']:9.4g} | {p['max_q_eig']:.3f} {p['max_q_state']:.3f} | {p['sup_diff']:.3f} {p['l2_diff']:.3f} ({p['l2_state']:.3f}) | {p['max_grad_q_eig']:.3f} {p['max_grad_q_state']:.3f}")
iv = out["inner_values"]; print(f"    inner holdout: sup|q* - q| {iv['sup_diff']:.3f}, L2 rel {iv['l2_diff_rel']:.3f}, max|q*| {iv['max_q_eig']:.3f}, max|q| {iv['max_q_state']:.3f}")
ec = out["eta_cost"]; print(f"(b) eta-row weighted cost: state {ec['total_state']:.3e}, (phi, q*) {ec['total_eigen']:.3e}; all rows {ec['cost_all_rows']['state']:.3e} -> {ec['cost_all_rows']['eigen']:.3e}")
print("    by element:", {k: ("%.2e -> %.2e" % (v["state"], v["eigen"])) for k, v in cost_el.items()})
print("    by shell (eigen):", {k: "%.2e" % v["eigen"] for k, v in cost_sh.items() if v["eigen"] > 1e-3 * ec["total_eigen"]})
print("    other blocks at (phi, q*):", {k: "%.2e" % v for k, v in out["cost_breakdown_eigen"].items() if k not in ("total",) and not k.startswith("pde_eta")})
print("    top eta rows at (phi, q*):", [(round(t["R"], 3), round(t["mu"], 3), "%.1e" % t["weighted_res"]) for t in ec["top_rows_eigen"][:5]])
print(f"(c) condition {out['condition']:.2e}; smallest ten directions (sigma_rel: ball / shells / ext leading / ext other):")
for sd in supp:
    print(f"    {sd['sigma_rel']:.2e}: {sd['ball']:.2f} / {sd['shells']:.2f} / {sd['ext_leading']:.2f} / {sd['ext_other']:.2f}")
print(f"(d) B(mu) state: min {out['B_state']['min']:.4f} max {out['B_state']['max']:.4f} sign changes {out['B_state']['sign_changes']}; B(mu) q*: min {out['B_eigen']['min']:.4f} max {out['B_eigen']['max']:.4f} sign changes {out['B_eigen']['sign_changes']}")
sj = out["source_jets"]; print(f"(f) source jets: phi_z - 1/2 {sj['phi']['dz'] - 0.5:.1e}, h2 {h2:.4f}; closure q_z {sj['closure_q_z']:.4f}; state q_z {sj['q_state']['dz']:.4f} q_rr {sj['q_state']['drr']:.3f} q_zz {sj['q_state']['dzz']:.3f}; q* q_z {sj['q_eigen']['dz']:.4f} q_rr {sj['q_eigen']['drr']:.3f} q_zz {sj['q_eigen']['dzz']:.3f}")
print("(e) source-adaptive: dist/a_eff | sup|q* - q| mean | max|grad q| max|grad q*| | q range state, q* range")
for sa in src:
    print(f"    {sa['dist_over_a_eff']:.0e} | {sa['sup_diff']:.4f} {sa['mean_diff']:+.4f} | {sa['max_grad_state']:.3f} {sa['max_grad_eig']:.3f} | {sa['q_state_range']} {sa['q_eig_range']}")

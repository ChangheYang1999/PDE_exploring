"""SPEC S4 (e) row for a state: |F| (collocation and, if available, Psi), c_l, x*, g(P) = rho_y(P), h(P) - 1, the Taylor
coefficients d1, d3, d5, d7 of w(x) = W_1(x, 0) = d1 x + d3 x^3 + d5 x^5 + d7 x^7 + ... at the origin from the modal
representation (w = c_l x - x v(x) P(q(x)), P(q) = sum_nu nu psit_nu(q); derivatives of the Chebyshev interpolant at q = 0 and
the binomial series of q(x), v(x) in x^2), and B_3 by the lead's tool (both forms, one configuration and the 32-variant medians
with ranges).  The trial's own C_0 is 0 for this (analytic-at-0) basis.
Usage: python3 src/s4e_row.py runs/state.npz tag"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, torch, ipm_newton as ipn, run_newton as rn, b3_axis

LANE = '.'


def taylor_w(model, x, order=3):
    """Coefficients d_{2k+1}, k = 0..order, of w(x) at x = 0."""
    b, cl = model.unpack(x); cl = float(cl); k = 1.0 / cl; L = model.L; a = (1.0 - k) / 2.0
    g = model.geom(torch.tensor(cl, device=model.dev)); fl = model.fields(b, torch.tensor(cl, device=model.dev), g)
    psit = fl['psit_n']; Dq = model.Dqpsi
    nf = torch.tensor(model.nf_np, device=model.dev)
    Pq = (psit * nf[None, :]).sum(1)                       # P(q) at the nodes (values of sum nu psit_nu)
    # Taylor coefficients of P at q = 0 from the interpolant: P^(j)(0)/j!
    derivs = [Pq[0].item()]
    cur = Pq.clone()
    for j in range(1, order + 1):
        cur = Dq @ cur; derivs.append(cur[0].item() / math.factorial(j))
    # series in t = u^2 = x^2/L^2: q(t) = a t - a(a+1)/2 t^2 + a(a+1)(a+2)/6 t^3 ; v(t) = 1 - a t + a(a+1)/2 t^2 - a(a+1)(a+2)/6 t^3
    qs = np.array([0.0, a, -a * (a + 1) / 2, a * (a + 1) * (a + 2) / 6])
    vs = np.array([1.0, -a, a * (a + 1) / 2, -a * (a + 1) * (a + 2) / 6])
    # P(q(t)) as a series in t: sum_j derivs[j] q(t)^j, truncated at t^3
    def mul(p, r): return np.convolve(p, r)[:order + 1]
    Pt = np.zeros(order + 1); qpow = np.zeros(order + 1); qpow[0] = 1.0
    for j in range(order + 1):
        Pt += derivs[j] * qpow
        qpow = mul(qpow, qs)
    vP = mul(vs, Pt)                                         # (v P)(t)
    # w = c_l x - x (vP)(x^2/L^2):  d1 = c_l - vP_0, d_{2k+1} = -vP_k / L^(2k)
    d = [cl - vP[0]] + [-vP[kk] / L ** (2 * kk) for kk in range(1, order + 1)]
    return d, derivs


def main():
    path, tag = sys.argv[1], sys.argv[2]
    model, x, dd = ipn.load_state(path); b, cl = model.unpack(x); clf = float(cl)
    row = dict(tag=tag, N=model.N, M=model.M, beta=model.beta, L=model.L, c_l=clf, A=2 * clf - 1)
    E, ident = model.residual(b, cl); E = E.cpu().numpy(); r, w, v = model.radii(clf)
    rel = np.abs(E[1:]) * (1 - model.q_np[1:, None]) / np.abs(b[1:].cpu().numpy())
    row['colloc_rel_max'] = float(rel.max()); row['identity_defect'] = float(ident)
    if 'C' in dd.files:
        import charmap as cm
        ch = cm.Charac(model); z = ch.pack(b, cl, float(dd['C']))
        F = ch.F(z, dt=0.01, dt_near=0.04, far_psi=True, r_far=1e10, n_coll=3, coll_scale=0.02)
        row['F_psi_2'] = float(F.norm()); row['F_psi_inf'] = float(F.abs().max()); row['C'] = float(dd['C'])
    st = rn.stagnation(model, x); row.update({k_: st[k_] for k_ in ('xstar', 'hP_minus_1', 'gP', 'wprimeP_minus_A', 'n_axis_zeros')})
    d, derivs = taylor_w(model, x)
    row['d1'] = d[0]; row['d1_plus_A'] = d[0] + (2 * clf - 1); row['d3'] = d[1]; row['d5'] = d[2]; row['d7'] = d[3]
    row['P_derivs_at_0'] = derivs
    out, (xs, w_ax, wp, wpp) = b3_axis.b3_of_state(model, x, verbose=False)
    row.update({k_: out[k_] for k_ in ('B3_orig', 'B3_ibp', 'median_orig', 'orig_min', 'orig_max', 'median_ibp', 'ibp_min', 'ibp_max', 'gstar')})
    # cross-check d3 against a polynomial fit of w on [1e-3, 0.05]
    sel = xs < 0.05; cf = np.polyfit(xs[sel] ** 2, w_ax[sel] / xs[sel], 3)
    row['d_fit_x<0.05'] = [float(cf[3]), float(cf[2]), float(cf[1]), float(cf[0])]
    row['own_C0'] = 0.0
    # near-origin angular compatibility (Cartesian smoothness): with b = sum_m b_m(q) cos(2 m s), a smooth a has
    # b_m = O(q^m) for the smooth part and O(q^2.1) for the fractional part, so b_m'(0) = 0 for m >= 2 and b_1(0) = 0 (built in).
    # true-theta cosine coefficients a_m(q_i) (the mapped s-modes mix the theta-modes): b on a fine uniform theta grid
    Mt = 4 * model.M; thf = (np.arange(Mt) + 0.5) * np.pi / (2 * Mt)
    Bf = np.stack([model.eval_EE(b, np.full_like(thf, qi), thf) for qi in model.q_np])          # (N+1, Mt)
    mm = np.arange(Mt); Cos = np.cos(np.outer(thf, 2 * mm)); coefT = np.linalg.solve(Cos, Bf.T).T  # (N+1, Mt) theta-mode coefficients
    Dq = model.Dq.cpu().numpy(); dcoef = (Dq @ coefT)[0]; d2coef = (Dq @ (Dq @ coefT))[0]
    row['compat_am_prime0_max_m>=2'] = float(np.abs(dcoef[2:]).max()); row['compat_a1_prime0'] = float(dcoef[1])
    row['compat_am_second0_max_m>=3'] = float(np.abs(d2coef[3:]).max()); row['a0_prime0'] = float(dcoef[0])
    row['compat_am_prime0_m2_m3_m4'] = [float(dcoef[2]), float(dcoef[3]), float(dcoef[4])]
    # SPEC S4 (e) (lead 04:10Z): remainder of w after its 7-jet, and the Hoelder behaviour of w'' at x* (both sides)
    P7 = d[0] * xs + d[1] * xs ** 3 + d[2] * xs ** 5 + d[3] * xs ** 7
    sel = (xs > 2e-3) & (xs < 0.5); R7 = w_ax[sel] - P7[sel]
    beta_ = 2.0 / (2 * clf - 1)
    row['remainder7_max_over_x9_[2e-3,0.5]'] = float(np.max(np.abs(R7) / xs[sel] ** 9))
    row['remainder7_max_over_x7+beta'] = float(np.max(np.abs(R7) / xs[sel] ** (7 + beta_)))
    cfit = np.polyfit(np.log(xs[sel][np.abs(R7) > 0]), np.log(np.abs(R7[np.abs(R7) > 0])), 1)
    row['remainder7_fitted_exponent'] = float(cfit[0])
    xst = float(row['xstar']); wpp_fun = lambda xx: axis_w(model, x, np.asarray(xx, float))[2] if False else None
    import b3_axis as b3a
    deltas = np.array([1e-1, 3e-2, 1e-2, 3e-3, 1e-3])
    xx = np.concatenate([[xst], xst - deltas, xst + deltas])
    _, _, wpp_loc, _ = b3a.axis_w(model, x, xx)
    hol = {}
    for sgn, name in ((-1, 'left'), (+1, 'right')):
        vals = wpp_loc[1:6] if sgn < 0 else wpp_loc[6:]
        hol[name] = [float(v) for v in (vals - wpp_loc[0]) / deltas ** 0.803]
    row['wpp_at_xstar'] = float(wpp_loc[0]); row['wpp_hoelder_ratio_0.803_deltas_1e-1..1e-3'] = hol
    json.dump(row, open(f'{LANE}/runs/s4e_{tag}.json', 'w'), indent=1)
    print(json.dumps(row, indent=1))


if __name__ == '__main__':
    main()

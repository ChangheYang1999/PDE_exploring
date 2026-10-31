#!/usr/bin/env python
"""SPEC v1.22/v1.23/v1.24 3.6 (n) (5): test-only double-double copy of the production gauge row g = w (sqrt(N) - 1), N = Problem.tail_norm2 (analytic modal energy),
for the (k) six-step ladder of a coefficient column at the manu_a base point. REGISTERED BEFORE EVALUATION; the diff against production is this file.
v4.5 (16:2xZ; V370): the validity identity at every stencil point includes the discrete identities of the actual nl_weights_from_ev arithmetic (RMS-floor masks with the 1e-300 clamp over all slots, argmax sets of den and den_nl, floor-branch flags, clamp set, median slot set) beside the production decision fields; the add-on's norm_fd_five_point is tied at 1e-3 too.
v4.4 (16:1xZ): the registered ladder ties use the harness arithmetic exactly (torch norms of the one-row group; v4.3's abs missed five ties by one ulp).
v4.3 (16:1xZ; SPEC v1.25 (1)): the production float64 gauge-row ladder at the six registered steps is recomputed and tied bitwise to the stored gauge-group norms and errors (registered record and (k) add-on); evaluation refuses if any tie fails.
v4.2 (16:0xZ; verifier 15:57:04Z and V366): base ties through every base-dependent quantity of the registered records (cost, pivot, discrete moments, drawn columns, raw and scaled G3 direction hashes; the latter regenerated with the production Jacobian's column norms), with the missing original-vector capture labelled and a lead ruling requested; full active-set evidence (denominators, floors, maxima, weights, median) at every point; exact rational offsets (two-word differences) for the identity derivative and the same-function tolerance; the perturbed power decision saved and required to fail.
v4.1 (SPEC v1.24, 15:5xZ): bitwise binding of |d|, F and the base cost to the registered records; nominal steps read from the records; the pre-input hash written to <inputs>.json.sha256 at prepare and checked at evaluate.
v4 (V358): (1) the map from the reduced coordinates to the full A, C arrays is a HELD-ROW solver inside this file: the dependent coefficients of each A/C column
are solved in 50-digit mpmath from the PRODUCTION float64 constraint rows held exactly (k2, k4 - p*1, q*1 and -q*1 as TailConstraints._solve_pair/_solve_single
form them in float64, with p = fl((a_env + l)/2), q = fl(m kappa/2), alpha = fl((1 - c_l)/c_l), kappa = fl(omega/c_l); all in hex in the inputs record) and the exact
binary64 free coefficients, rounded once to (hi, lo); dd_tables.expand_dd is NOT used (it recomputes alpha, kappa, k4 - p in high precision). (2) 'prepare' writes a
pre-input record (JSON + NPZ, hashed) for BOTH columns 186 and 189 before any evaluation: base A, C, z_opt, every binary64 stencil vector of the six steps, the
production entries d (jvp), the exact rounded constraint rows, mode/layout mappings, constants, the base active set, and the ties to the registered gates record and
the (k) add-on record (sha256, gauge-group norm_d, floor, step scale, nominal steps). 'evaluate <col>' re-reads and re-hashes that record and takes d, F, the step
scale, the nominal steps and the stencil vectors from it (d must equal the registered gauge-group norm_d in magnitude; F the registered floor). (3) the active set is
recorded at every stencil point (production nl_active_set + geometry id); a step is valid only when all four points share the base active set. (4) The record reports
the ladder decision (registered rule with F, and with F = 0), the same-function differences at the base and at ALL six steps (the base and the 1e-2, 1e-3 s_j points
decide, against 1e-3 |d| h with h the ACTUAL stored offset of the point; the fine four are information), the power check, and admitted_n5 = ladder PASS and
same-function success and power success, each flag separate. The arithmetic of the modal chain is double-double (exact_matmul.dd_add / dd_mul_f / dd_div_f,
fields_dd.dd_mul_dd; dd_sqrt = float64 sqrt plus one Newton step in dd), with the production float64 constants R0^(alpha+l), R0^(alpha+l-1), wT, wS, w held exactly;
D_h and D4_h are formed in dd and rounded once; the identity-type derivative at the actual offsets (exact denominator h_plus + h_minus) is recorded as well.
UNCHANGED: d, steps (1e-2 ... 1e-7 s_j), F = 1e-10 |r_gauge| (registered), tau_group = 1e-5, the pass rule and the Richardson rule, the F = 0 variant.
Usage: python validation/gauge_row_dd.py prepare manu_a [device]           -> validation/gauge_row_dd_inputs_manu_a.json + .npz
       python validation/gauge_row_dd.py evaluate manu_a <column> [device] -> validation/gauge_row_dd_manu_a_col<j>.json + _arrays.npz"""
import sys, os, json, time, math, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import numpy as np, torch, mpmath as mp
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False; torch.backends.cudnn.allow_tf32 = False
from validation.gates import Case, PAIRS, ROOT, code_hashes
from src.pressure.exact_matmul import dd_add, dd_mul_f, dd_div_f
from src.equations.fields_dd import dd_mul_dd
from src.equations.fields import alpha_of

STEPS = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7]          # the six-step ladder of (k): the registered five steps plus 1e-2 s_j
TAU_GROUP = 1e-5; DPS = 50
CASES = {"manu_a": dict(pair=PAIRS["a"], seed=3)}
COLUMNS = {"manu_a": [189, 186]}


def hexs(x):
    return float(x).hex()


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def dd_sum(hs, ls):
    H = torch.zeros((), dtype=torch.float64); L = torch.zeros((), dtype=torch.float64)
    for k in range(len(hs)):
        H, L = dd_add(H, L, torch.tensor(float(hs[k])), torch.tensor(float(ls[k])))
    return H, L


def dd_sqrt(h, l):
    s0 = torch.sqrt(h)
    p, pl = dd_mul_dd(s0, torch.zeros_like(s0), s0, torch.zeros_like(s0))
    rh, rl = dd_add(h, l, -p, -pl)
    ch, cl = dd_div_f(rh, rl, 2.0 * s0)
    return dd_add(s0, torch.zeros_like(s0), ch, cl)


def to_dd(x):
    h = float(x); l = float(x - mp.mpf(h)); return h, l


def production_rows(tc, model, c_l, omega):
    """The constraint rows exactly as TailConstraints.expand/_solve_pair/_solve_single form them in float64 (production bits), per channel and pair/single."""
    cl_t = torch.tensor(c_l, dtype=torch.float64); om_t = torch.tensor(omega, dtype=torch.float64)
    alpha = alpha_of(cl_t); kappa = om_t / cl_t
    k2 = tc.k2.detach().cpu(); k4 = tc.k4.detach().cpu(); ones = torch.ones_like(k2)
    rows = {}
    for name, a_env in (("A", alpha), ("C", alpha - 1.0)):
        rows[name] = {}
        for (qc, qs, m, l) in tc.pairs:
            p = (a_env + l) / 2.0; q = m * kappa / 2.0
            ra = torch.stack([k2, torch.zeros_like(k2), k4 - p * ones, -q * ones], 0); rb = torch.stack([torch.zeros_like(k2), k2, q * ones, k4 - p * ones], 0)
            rows[name][f"pair_{qc}_{qs}"] = dict(kind="pair", qc=int(qc), qs=int(qs), m=int(m), l=int(l), p=float(p), q=float(q), ra=ra.numpy(), rb=rb.numpy())
        for (q0, l) in tc.singles:
            p = (a_env + l) / 2.0
            ra = torch.stack([k2, k4 - p * ones], 0)
            rows[name][f"single_{q0}"] = dict(kind="single", q0=int(q0), l=int(l), p=float(p), ra=ra.numpy())
    return rows, float(alpha), float(kappa), k2.numpy(), k4.numpy()


def reduced_blocks(tc, model, z_red):
    """the free-coefficient blocks red[name] (n_free, Nq) exactly as TailConstraints.expand forms them (reshape and scatter: exact)."""
    Nq = model.Nq; off = 0; red = {}
    for name in ("A", "C", "B", "D", "E"):
        n = tc.red_sizes[name]; nc = tc.ncols[name]
        a = z_red[off: off + n * nc].reshape(n, nc) if n > 0 else torch.zeros(0, nc, dtype=torch.float64, device=z_red.device); off += n * nc
        if nc != Nq:
            a = torch.zeros(n, Nq, dtype=torch.float64, device=z_red.device).index_copy(1, tc.cols[name], a)
        red[name] = a.detach().cpu().numpy()
    return red


def held_row_expand(red, rows, Nk, Nq):
    """A, C full columns as (hi, lo) arrays (Nk, Nq): free coefficients exact (lo = 0); the top two of each column solved in mpmath from the HELD float64 rows."""
    out = {}
    for name in ("A", "C"):
        H = np.zeros((Nk, Nq)); L = np.zeros((Nk, Nq)); free = red[name]
        for key, rr in rows[name].items():
            if rr["kind"] == "pair":
                qc, qs = rr["qc"], rr["qs"]; ra = rr["ra"]; rb = rr["rb"]
                fa = [mp.mpf(float(x)) for x in free[:, qc].tolist()]; fb = [mp.mpf(float(x)) for x in free[:, qs].tolist()]
                M = mp.matrix(4, 4); rhs = mp.matrix(4, 1)
                for i in range(4):
                    M[i, 0] = mp.mpf(float(ra[i, Nk - 2])); M[i, 1] = mp.mpf(float(ra[i, Nk - 1])); M[i, 2] = mp.mpf(float(rb[i, Nk - 2])); M[i, 3] = mp.mpf(float(rb[i, Nk - 1]))
                    rhs[i] = -(mp.fsum(mp.mpf(float(ra[i, k])) * fa[k] for k in range(Nk - 2)) + mp.fsum(mp.mpf(float(rb[i, k])) * fb[k] for k in range(Nk - 2)))
                u = mp.lu_solve(M, rhs)
                for k in range(Nk - 2):
                    H[k, qc] = float(fa[k]); H[k, qs] = float(fb[k])
                for i, (col, val) in enumerate(((qc, u[0]), (qc, u[1]), (qs, u[2]), (qs, u[3]))):
                    k = Nk - 2 + (i % 2); h_, l_ = to_dd(val); H[k, col] = h_; L[k, col] = l_
            else:
                q0 = rr["q0"]; ra = rr["ra"]; fa = [mp.mpf(float(x)) for x in free[:, q0].tolist()]
                M = mp.matrix(2, 2); rhs = mp.matrix(2, 1)
                for i in range(2):
                    M[i, 0] = mp.mpf(float(ra[i, Nk - 2])); M[i, 1] = mp.mpf(float(ra[i, Nk - 1])); rhs[i] = -mp.fsum(mp.mpf(float(ra[i, k])) * fa[k] for k in range(Nk - 2))
                u = mp.lu_solve(M, rhs)
                for k in range(Nk - 2):
                    H[k, q0] = float(fa[k])
                for i in range(2):
                    h_, l_ = to_dd(u[i]); H[Nk - 2 + i, q0] = h_; L[Nk - 2 + i, q0] = l_
        out[name] = (H, L)
    return out


def g_dd_from(red, rows, consts, Nk, Nq, w):
    """the gauge row in double-double from the free blocks: held-row expansion, dd radial sums, products with the held float64 constants, squares, mode weights, sum, sqrt, -1, w."""
    ex = held_row_expand(red, rows, Nk, Nq); (Ah, Al), (Ch, Cl) = ex["A"], ex["C"]
    powT, powS, wT, wS = consts
    Nh = torch.zeros((), dtype=torch.float64); Nl = torch.zeros_like(Nh)
    for q_ in range(Nq):
        th, tl = dd_sum(Ah[:, q_], Al[:, q_]); th, tl = dd_mul_f(th, tl, float(powT[q_]))
        sh, sl = dd_sum(Ch[:, q_], Cl[:, q_]); sh, sl = dd_mul_f(sh, sl, float(powS[q_]))
        eTh, eTl = dd_mul_dd(th, tl, th, tl); eTh, eTl = dd_mul_f(eTh, eTl, float(wT[q_]))
        eSh, eSl = dd_mul_dd(sh, sl, sh, sl); eSh, eSl = dd_mul_f(eSh, eSl, float(wS[q_]))
        Nh, Nl = dd_add(Nh, Nl, eTh, eTl); Nh, Nl = dd_add(Nh, Nl, eSh, eSl)
    rh, rl = dd_sqrt(Nh, Nl); rh, rl = dd_add(rh, rl, torch.tensor(-1.0), torch.zeros_like(rh))
    gh, gl = dd_mul_f(rh, rl, w)
    return (float(gh), float(gl)), (float(Nh), float(Nl)), ex


def active_set_evidence(prob, ev):
    """SPEC 3.0 (e) evidence at an evaluation (verifier 15:57:04Z item 2): the production decision (nl_active_set: median shell, clamped shells, geometry id) PLUS the
    quantities it is made of, recomputed with the same lines as Problem.nl_active_set (test-only replication, read only): the per-shell denominators den_k,
    the floor 1e-6 max_k den_k, the far denominators den_nl and their floor, the weights at the occupied shells, the median weight and the clamp cap."""
    a = prob.nl_active_set(ev); a["geometry"] = prob.pressure.geometry_id
    if not prob.nl_weighting or "R_u" not in ev:
        return a
    from src.validation.spec_diagnostics import five_term_split
    with torch.no_grad():
        # v4.5 (V370 item 1): the ACTUAL nl_weights_from_ev / shell_w arithmetic (1e-300 clamps, all shell slots including empty ones) and its DISCRETE identities:
        # the RMS-floor active masks per term and slot, the argmax sets of den and den_nl, the floor-branch flags, the clamp set against the median weight
        F = ev["F"]; Msh = prob._shell_mean; occupied = prob._shell_occupied; nsl = Msh.shape[0]
        T = five_term_split(F, ev["gradP"]); sc = prob.scale_mom(F["c_l"])
        rms_k = []; masks = []
        for t in T:
            per_node = ((t ** 2).sum(0) * prob.w_ang[None, :]).sum(1) * sc ** 2
            raw = Msh @ per_node; masks.append([bool(x) for x in (raw < 1e-300).tolist()]); rms_k.append(raw.clamp_min(1e-300).sqrt())
        den = sum(rms_k); den_max = den.max(); floor_raw = 1e-6 * den_max; floor = torch.clamp(floor_raw, min=1e-300); w = 1.0 / (den + floor) ** 2
        disc = dict(rms_floor_active_masks=masks, den_argmax_set=[int(i) for i in (den == den_max).nonzero().reshape(-1).tolist()], den_floor_branch_clamped=bool(float(floor_raw) < 1e-300))
        ev_ = dict(den_all_slots=[float(x) for x in den.tolist()], den_max=float(den_max), floor=float(floor), occupied_shells=[int(x) for x in occupied.tolist()], n_slots=int(nsl))
        if prob.nl_denominator == "all5far":
            den_nl = rms_k[3] + rms_k[4]; far = torch.tensor([float(e) >= 1.0 for e in prob.shell_edges], dtype=torch.bool, device=den.device); den_nl_max = den_nl.max(); floor_nl_raw = 1e-6 * den_nl_max
            floor_nl = torch.clamp(floor_nl_raw, min=1e-300); sc_far = 1.0 / (den + floor) + prob.far_lambda / (den_nl + floor_nl); w = torch.where(far, sc_far ** 2, w)
            disc.update(den_nl_argmax_set=[int(i) for i in (den_nl == den_nl_max).nonzero().reshape(-1).tolist()], den_nl_floor_branch_clamped=bool(float(floor_nl_raw) < 1e-300), far_mask=[bool(x) for x in far.tolist()])
            ev_.update(den_nl_all_slots=[float(x) for x in den_nl.tolist()], den_nl_max=float(den_nl_max), floor_nl=float(floor_nl))
        wocc = w[occupied]; wmed = wocc.median(); cap = float(prob.nl_weight_cap)
        disc.update(clamped_slots_cap_times_median=[int(i) for i in range(nsl) if float(w[i]) > cap * float(wmed)], median_slot_set=[int(occupied[i]) for i in range(occupied.numel()) if float(wocc[i]) == float(wmed)])
        ev_.update(weights_all_slots=[float(x) for x in w.tolist()], median_weight=float(wmed), clamp_cap=cap, clamp_rule="w = min(w, nl_weight_cap * median over occupied slots)")
    a["evidence"] = ev_; a["discrete_identities"] = disc
    return a


def exact_offset(qj, q0):
    """exact difference of two binary64 values as a rational string and as a two-word (hi, lo) pair (V366: Sterbenz does not apply to every pair)."""
    from fractions import Fraction
    fr = Fraction(float(qj)) - Fraction(float(q0)); hi = float(qj) - float(q0); lo = float(fr - Fraction(hi))
    return dict(rounded=hi, hi=hi, lo=lo, exact=f"{fr.numerator}/{fr.denominator}", rounded_is_exact=(lo == 0.0))


def build_case(cname, dev):
    case = Case(cname, dev, **CASES[cname]); prob, model, tc, pm = case.prob, case.model, case.tc, case.pm
    return case, prob, model, tc, pm


def find_registered(gates, cname, col):
    """the registered G1 coefficient-column record of the case for Jf (path cases/<case>/G1_Jf_coefficient_columns/results[i]/Jf)."""
    res = gates["cases"][cname]["G1_Jf_coefficient_columns"]["results"]
    for r in res:
        rec = r.get("Jf") if isinstance(r.get("Jf"), dict) else r
        if rec.get("column") == col:
            return rec
    raise KeyError(col)


def prepare(cname, dev):
    out_json = os.path.join(ROOT, "validation", f"gauge_row_dd_inputs_{cname}.json"); out_npz = out_json.replace(".json", ".npz")
    for p in (out_json, out_npz):
        if os.path.exists(p):
            raise FileExistsError(p)
    t0 = time.time(); case, prob, model, tc, pm = build_case(cname, dev)
    zo = case.z_opt.detach().clone(); to_full = case.to_full_opt; gr = case.block_slices["gauge"][0]; w = float(prob.gauge_weight)
    zf = to_full(zo).detach(); A, C, cc, ww = model.unpack(zf); c_l = float(cc); omega = float(ww); R0 = float(model.R0)
    l = model.l_arr.to(torch.float64); m = model.m_arr.to(torch.float64); a_prod = float(alpha_of(torch.tensor(c_l, dtype=torch.float64))); a_t = torch.tensor(a_prod, dtype=torch.float64, device=l.device)
    powT = (R0 ** (a_t + l)).detach().cpu().numpy(); powS = (R0 ** (a_t + l - 1)).detach().cpu().numpy(); wT = (l * (l + 1)).detach().cpu().numpy(); wS = (l ** 2 * (l + 1) ** 2 + l * (l + 1) * ((2 - a_t) ** 2 + (m * omega / c_l) ** 2)).detach().cpu().numpy()
    rows, alpha_f, kappa_f, k2, k4 = production_rows(tc, model, c_l, omega)
    gates_p = os.path.join(ROOT, "validation", f"gates_gpu_v1_{cname}.json"); addon_p = os.path.join(ROOT, "validation", f"g1_step_addon_{cname}.json")
    gates = json.load(open(gates_p)); addon = json.load(open(addon_p))
    def act(q):
        zz_ = to_full(q); ev = prob.evaluate(zz_, tables=prob.pressure_tables_at(zz_)); return active_set_evidence(prob, ev)
    base_act = act(zo)
    # v4.2 (verifier 15:57:04Z item 1, V366): the registered records hold no base-vector capture (manufactured field, seed 3, built by Case); the base is tied by construction and
    # by every base-dependent scalar and hash the records DO hold: cost, pivot (pot, q, amplitude), the discrete source moments, the drawn coefficient columns, and the
    # G3 scaled-direction sha256 (a function of the base Jacobian's column norms: regenerated here with seed 11 in the gates order and the production Jacobian)
    greg = gates["cases"][cname]
    from src.optimization.lm import jacobian_fwd, param_columns
    import src.equations.residuals as res_mod
    n = zo.numel(); rng = np.random.default_rng(11); cols_drawn = sorted(rng.choice(n - 2, size=min(20, n - 2), replace=False).tolist())
    Jb = jacobian_fwd(lambda q: prob.residual_vector(to_full(q)), zo, chunk=256); Jpb = param_columns(lambda q: prob.residual_vector(to_full(q), differentiable_pressure=True), zo, [n - 2, n - 1])
    Jb[:, n - 2] = Jpb[:, 0]; Jb[:, n - 1] = Jpb[:, 1]; colnorm = (Jb * Jb).sum(0).clamp_min(1e-30).sqrt(); del Jb, Jpb
    E = {}; e_ = torch.zeros_like(zo); e_[n - 2] = 1.0; E["e_zc(optimizer)"] = e_; e_ = torch.zeros_like(zo); e_[n - 1] = 1.0; E["e_zw(optimizer)"] = e_
    draws = [rng.normal(size=n) for _ in range(5)]
    for i in range(3):
        u = torch.tensor(draws[i], device=dev); u = u / u.norm(); E[f"random_scaled_{i}"] = u / colnorm
    for i in range(2):
        u = torch.tensor(draws[3 + i], device=dev); u = u / u.norm(); u[-2] = 0.3; u[-1] = 0.3; u = u / u.norm(); E[f"mixed_{i}"] = u / colnorm
    raw_sha = hashlib.sha256(b"".join(np.ascontiguousarray(u, dtype=np.float64).tobytes() for u in draws)).hexdigest(); scaled_sha = hashlib.sha256(b"".join(E[k].detach().cpu().numpy().tobytes() for k in E)).hexdigest()
    dm = prob.pressure.discrete_moments(res_mod.pressure_source(model.fields_grid(case.z_full, need_vort=False)["GU"]), lmax=1)
    gh = greg.get("G3_direction_hashes") or {}
    base_tie = dict(original_base_vector_capture_in_registered_records=False,
                    statement="the registered gates record and the (k) add-on record hold no base vector; the base state is the deterministic Case construction (manufactured smooth random field, seed 3, pair a, phase aligned), tied bitwise through every base-dependent quantity the records hold (below); a prospective lead ruling on this binding is requested before evaluation (verifier 15:57:04Z item 1)",
                    cost_equal=(float(greg["cost"]) == case.cost), cost=case.cost, pivot_equal=(json.dumps(greg.get("pivot"), sort_keys=True) == json.dumps(prob.pivot, sort_keys=True, default=float)), pivot=prob.pivot,
                    discrete_moments_equal=(json.dumps(greg.get("discrete_moments"), sort_keys=True, default=str) == json.dumps(dm, sort_keys=True, default=str)), discrete_moments=dm,
                    drawn_columns_equal=(greg.get("G1_coefficient_columns_drawn") == cols_drawn), raw_draws_sha256_equal=(gh.get("raw_draws_sha256") == raw_sha), scaled_directions_sha256_equal=(gh.get("scaled_directions_sha256") == scaled_sha),
                    scaled_directions_sha256=scaled_sha, registered_scaled_directions_sha256=gh.get("scaled_directions_sha256"), field=case.field_desc, n_opt=int(n), n_rows_equal=(int(greg.get("n_rows", -1)) == int(case.r.numel())))
    base_tie["all_available_ties_equal"] = bool(base_tie["cost_equal"] and base_tie["pivot_equal"] and base_tie["discrete_moments_equal"] and base_tie["drawn_columns_equal"] and base_tie["raw_draws_sha256_equal"] and base_tie["scaled_directions_sha256_equal"] and base_tie["n_rows_equal"])
    print("base ties:", {k: v for k, v in base_tie.items() if k.endswith("_equal")}, flush=True)
    arrays = dict(z_opt=zo.cpu().numpy(), A=A.detach().cpu().numpy(), C=C.detach().cpu().numpy(), l=model.l_arr.cpu().numpy(), m=model.m_arr.cpu().numpy(), powT=powT, powS=powS, wT=wT, wS=wS, k2=k2, k4=k4, r_base=case.r.detach().cpu().numpy())
    for name in ("A", "C"):
        for key, rr in rows[name].items():
            arrays[f"row_{name}_{key}_ra"] = rr["ra"]
            if rr["kind"] == "pair":
                arrays[f"row_{name}_{key}_rb"] = rr["rb"]
    red0 = reduced_blocks(tc, model, pm.expand(zo)); arrays["red_A_base"] = red0["A"]; arrays["red_C_base"] = red0["C"]
    cols = {}
    for j in COLUMNS[cname]:
        e = torch.zeros_like(zo); e[j] = 1.0
        d = float(torch.func.jvp(lambda q: prob.residual_vector(to_full(q)), (zo,), (e,))[1][gr])
        reg = find_registered(gates, cname, j); pg = reg.get("per_group", {}); add = addon["jacobians"]["Jf"]["columns"][str(j)]["column_test"]; apg = add.get("per_group", {})
        s_j = float(reg.get("step_scale", 1.0))
        tie = dict(gates_record=os.path.relpath(gates_p, ROOT), gates_sha256=sha(gates_p), addon_record=os.path.relpath(addon_p, ROOT), addon_sha256=sha(addon_p), step_scale_registered=s_j, step_scale_addon=float(add.get("step_scale", 1.0)),
                   registered_steps=sorted(pg.keys(), key=float, reverse=True), addon_steps=sorted(apg.keys(), key=float, reverse=True),
                   gauge_norm_d_registered={h: pg[h]["norm_d"].get("gauge") for h in pg}, gauge_floor_registered={h: pg[h]["floor"].get("gauge") for h in pg},
                   gauge_norm_d_addon={h: apg[h]["norm_d"].get("gauge") for h in apg}, gauge_floor_addon={h: apg[h]["floor"].get("gauge") for h in apg},
                   gauge_second_order_registered={h: pg[h]["second_order"].get("gauge") for h in pg}, gauge_five_point_registered={h: pg[h]["five_point"].get("gauge") for h in pg},
                   gauge_second_order_addon={h: apg[h]["second_order"].get("gauge") for h in apg}, gauge_five_point_addon={h: apg[h]["five_point"].get("gauge") for h in apg},
                   gauge_norm_fd_registered={h: pg[h]["norm_fd"].get("gauge") for h in pg}, gauge_norm_fd_addon={h: apg[h]["norm_fd"].get("gauge") for h in apg})
        # v4.3 (SPEC v1.25 (1)): the production float64 ladder of the gauge row (as gates.stencil_ladder: D = (f(z + h e) - f(z - h e)) / (2h), D4 the five-point stencil,
        # f = residual_vector(to_full(q)) at the float64 stencil points; scaled by s_j = 1) at the six registered steps, tied BITWISE to the stored gauge-group values:
        # norm_fd = |D_h|, norm_fd_five_point = |D4_h|, second_order e = |D - d| / max(|d|, |D|, F), five_point e4 likewise (the registered record: 1e-3 ... 1e-7; the (k) add-on: 1e-2, 1e-3)
        Freg = float(sorted({float(v) for v in list(pg[h]["floor"].get("gauge") for h in pg) + list(apg[h]["floor"].get("gauge") for h in apg) if v is not None})[0])
        lad_tie = {}
        d_t = torch.tensor([d], dtype=torch.float64, device=dev)
        for h in STEPS:
            # v4.4: the harness arithmetic exactly (gates.stencil_ladder on the full residual vector, then gates.group_errors on the one-row gauge group with torch norms:
            # norm() of a one-element tensor is sqrt(x*x), which differs from |x| in the last bit for some x; v4.3 used abs and missed five ties by one ulp)
            hh = h * s_j; f_ = lambda t: prob.residual_vector(to_full((zo + t * e)))
            fp, fm, f2p, f2m = f_(hh), f_(-hh), f_(2 * hh), f_(-2 * hh)
            Dv = (fp - fm) / (2 * hh); D4v = (8 * (fp - fm) - (f2p - f2m)) / (12 * hh)
            dq = Dv[gr:gr + 1]; dq4 = D4v[gr:gr + 1]
            Dp = float(dq[0]); D4p = float(dq4[0])
            den2 = max(float(d_t.norm()), float(dq.norm()), Freg); den4 = max(float(d_t.norm()), float(dq4.norm()), Freg)
            e2 = float((d_t - dq).norm() / den2); e4 = float((d_t - dq4).norm() / den4); nfd = float(dq.norm()); nfd4 = float(dq4.norm())
            src = apg if f"{h:.0e}" in apg and f"{h:.0e}" not in pg else pg; key = f"{h:.0e}"; stored = src.get(key, {})
            lad_tie[key] = dict(source=("addon" if src is apg else "registered"), norm_fd=dict(recomputed=nfd, stored=stored.get("norm_fd", {}).get("gauge"), equal=(stored.get("norm_fd", {}).get("gauge") == nfd)),
                                norm_fd_five_point=dict(recomputed=nfd4, stored=stored.get("norm_fd_five_point", {}).get("gauge"), equal=(stored.get("norm_fd_five_point", {}).get("gauge") == nfd4)),
                                second_order=dict(recomputed=e2, stored=stored.get("second_order", {}).get("gauge"), equal=(stored.get("second_order", {}).get("gauge") == e2)),
                                five_point=dict(recomputed=e4, stored=stored.get("five_point", {}).get("gauge"), equal=(stored.get("five_point", {}).get("gauge") == e4)))
            if f"{h:.0e}" in apg and f"{h:.0e}" in pg:                                                   # 1e-3 appears in both records: both must agree
                lad_tie[key]["also_in_addon_equal"] = (apg[key]["norm_fd"].get("gauge") == nfd and apg[key]["norm_fd_five_point"].get("gauge") == nfd4 and apg[key]["second_order"].get("gauge") == e2 and apg[key]["five_point"].get("gauge") == e4)   # v4.5 (V370 item 2): the add-on's five-point norm too
        lad_tie_all = all(v["norm_fd"]["equal"] and v["norm_fd_five_point"]["equal"] and v["second_order"]["equal"] and v["five_point"]["equal"] and v.get("also_in_addon_equal", True) for v in lad_tie.values())
        print(f"column {j}: registered ladder ties equal at all six steps: {lad_tie_all}", flush=True)
        nd = {float(v) for v in list(tie["gauge_norm_d_registered"].values()) + list(tie["gauge_norm_d_addon"].values()) if v is not None}
        fl_ = {float(v) for v in list(tie["gauge_floor_registered"].values()) + list(tie["gauge_floor_addon"].values()) if v is not None}
        # v4.1 (SPEC v1.24 (n) (5) (ii)): BITWISE binding of |d| to the registered gauge norm_d and of F to the registered floor (the records store the norm of the one-row group);
        # the base is bound through the record's cost (bitwise) and the case construction (manufactured field, seed 3, pair a); the nominal steps are read from the records.
        reg_cost = float(gates["cases"][cname]["cost"]) if "cases" in gates else float(gates[cname]["cost"])
        bind = dict(d_abs_equals_registered_norm_d=(len(nd) == 1 and abs(d) == sorted(nd)[0]), registered_norm_d_values=sorted(nd), floor_values=sorted(fl_), F=(sorted(fl_)[0] if fl_ else None), F_recomputed=1e-10 * abs(float(case.r[gr])),
                    F_equal=(len(fl_) == 1 and sorted(fl_)[0] == 1e-10 * abs(float(case.r[gr]))), base_cost_registered=reg_cost, base_cost_equal=(reg_cost == case.cost), base_cost_case=case.cost,
                    nominal_steps_from_records=sorted({float(h) for h in list(pg.keys()) + list(apg.keys())}, reverse=True), nominal_steps_equal_STEPS=(sorted({float(h) for h in list(pg.keys()) + list(apg.keys())}, reverse=True) == STEPS),
                    registered_ladder_ties=lad_tie, registered_ladder_ties_all_equal=bool(lad_tie_all), rule="SPEC v1.25 (1): the base is tied by equality, as stored, of cost, |d|, F and the gauge group's difference norms and errors at all six steps; if any tie fails the reference is not evaluated")
        stencil = {}
        for h in STEPS:
            hh = h * s_j
            for t in (hh, -hh, 2 * hh, -2 * hh):
                q = (zo + t * e).detach(); key = f"q_{j}_{h:.0e}_{t:+.1e}"; arrays[key] = q.cpu().numpy()
                stencil[f"{h:.0e}:{t:+.1e}"] = dict(array=key, actual_offset_rounded=float(q[j]) - float(zo[j]), actual_offset_exact=exact_offset(q[j], zo[j]), intended=t)
        cols[str(j)] = dict(column=j, d_production_jvp=d, d_hex=hexs(d), step_scale=s_j, ties=tie, binding=bind, stencil_vectors=stencil, direction_key=f"e_{j}")
        arrays[f"e_{j}"] = e.cpu().numpy()
    np.savez_compressed(out_npz, **arrays)
    rec = dict(kind="gauge_row_dd pre-input record (v4, V358 item 2)", case=cname, pair=case.pair, cost=case.cost, device=str(dev), n_opt=int(zo.numel()), gauge_row=int(gr), gauge_weight=w, steps=STEPS, tau_group=TAU_GROUP,
               constants_hex=dict(c_l=hexs(c_l), omega=hexs(omega), R0=hexs(R0), alpha_production=hexs(alpha_f), kappa_production=hexs(kappa_f), w=hexs(w), powT=[hexs(x) for x in powT.tolist()], powS=[hexs(x) for x in powS.tolist()], wT=[hexs(x) for x in wT.tolist()], wS=[hexs(x) for x in wS.tolist()], k2=[hexs(x) for x in k2.tolist()], k4=[hexs(x) for x in k4.tolist()]),
               constraint_rows={name: {key: dict(kind=rr["kind"], **{k: rr[k] for k in rr if k in ("qc", "qs", "q0", "m", "l")}, p_hex=hexs(rr["p"]), q_hex=(hexs(rr["q"]) if "q" in rr else None), ra_hex=[[hexs(x) for x in row] for row in rr["ra"].tolist()], rb_hex=([[hexs(x) for x in row] for row in rr["rb"].tolist()] if "rb" in rr else None)) for key, rr in rows[name].items()} for name in ("A", "C")},
               rows_construction="TailConstraints._solve_pair: ra = [k2, 0, k4 - p*1, -q*1], rb = [0, k2, q*1, k4 - p*1] (float64); M = last two columns of ra and rb; rhs = -(ra[:, :Nk-2] @ free_a + rb[:, :Nk-2] @ free_b); _solve_single: ra = [k2, k4 - p*1]; p = fl((a_env + l)/2), q = fl(m kappa/2), a_env = alpha (A) or alpha - 1.0 (C), alpha = fl((1 - c_l)/c_l), kappa = fl(omega/c_l)",
               mode_lists=dict(modes=[(int(a), int(b), int(c)) for (a, b, c) in model.modes], l=[int(x) for x in model.l_arr.tolist()], m=[int(x) for x in model.m_arr.tolist()], pairs=[(int(a), int(b), int(mm), int(ll)) for (a, b, mm, ll) in tc.pairs], singles=[(int(a), int(ll)) for (a, ll) in tc.singles], Nq=int(model.Nq), Nk=int(model.Nk)),
               reduced_layout=dict(red_sizes={k: int(v) for k, v in tc.red_sizes.items()}, ncols={k: int(v) for k, v in tc.ncols.items()}, layout=[(nm, int(nn)) for nm, nn in model.layout], chan_cols=({k: [int(x) for x in v.tolist()] for k, v in tc.cols.items()} if tc.cols else None),
                                   column_to_coefficient="reduced index i in the A block (i < red_sizes[A] * ncols[A]) -> free row i // ncols[A], channel column i % ncols[A] (scattered to the union mode set by chan_cols[A] if ncols[A] != Nq); then the C block, B, D, E; the last two entries are z_c, z_w"),
               base_active_set=base_act, base_tie=base_tie, columns=cols, arrays_npz=dict(path=os.path.relpath(out_npz, ROOT), sha256=sha(out_npz), keys=sorted(arrays)),
               start=dict(field=case.field_desc), code_sha256=code_hashes(), launcher_manifest=(open(os.path.join(ROOT, "SOURCES_SHA256.txt")).read() if os.path.exists(os.path.join(ROOT, "SOURCES_SHA256.txt")) else None),
               seconds=time.time() - t0, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    with open(out_json, "x") as fh:
        json.dump(rec, fh, indent=1, default=str)
    with open(out_json + ".sha256", "x") as fh:                                                  # v4.1 (v1.24 (i')): the hash of the pre-input file, recorded before the first evaluation
        fh.write(f"{sha(out_json)}  {os.path.basename(out_json)}\n{sha(out_npz)}  {os.path.basename(out_npz)}\n")
    print("PREPARED", out_json, "npz sha", rec["arrays_npz"]["sha256"][:16], {j: (cols[j]["d_production_jvp"], cols[j]["binding"]["d_abs_equals_registered_norm_d"], cols[j]["binding"]["F_equal"]) for j in cols}, f"{time.time() - t0:.0f}s")


def evaluate(cname, j, dev):
    inp_json = os.path.join(ROOT, "validation", f"gauge_row_dd_inputs_{cname}.json"); inp_npz = inp_json.replace(".json", ".npz")
    out_json = os.path.join(ROOT, "validation", f"gauge_row_dd_{cname}_col{j}.json"); out_npz = out_json.replace(".json", "_arrays.npz")
    for p in (out_json, out_npz):
        if os.path.exists(p):
            raise FileExistsError(p)
    t0 = time.time(); inp = json.load(open(inp_json)); inputs_sha = sha(inp_json); npz_sha = sha(inp_npz)
    assert npz_sha == inp["arrays_npz"]["sha256"], "pre-input NPZ hash mismatch"
    Z = np.load(inp_npz); col = inp["columns"][str(j)]
    case, prob, model, tc, pm = build_case(cname, dev)
    zo = torch.as_tensor(Z["z_opt"], device=dev); assert bool(torch.equal(zo, case.z_opt.detach())), "base reduced vector differs from the pre-input record"
    to_full = case.to_full_opt; gr = inp["gauge_row"]; w = float(inp["gauge_weight"])
    d = float(col["d_production_jvp"]); s_j = float(col["step_scale"]); F = float(col["binding"]["F"]); assert col["binding"]["d_abs_equals_registered_norm_d"] and col["binding"]["F_equal"] and col["binding"]["base_cost_equal"], "d, F or the base not bound bitwise to the registered record"
    assert col["binding"].get("registered_ladder_ties_all_equal") and inp.get("base_tie", {}).get("all_available_ties_equal"), "SPEC v1.25 (1): a registered tie fails; the reference is not evaluated"
    assert col["binding"]["nominal_steps_equal_STEPS"], "nominal steps differ from the records"
    rec_hash_file = inp_json + ".sha256"; assert os.path.exists(rec_hash_file) and open(rec_hash_file).read().split()[0] == inputs_sha, "pre-input JSON hash differs from the hash recorded at prepare time"
    consts = (Z["powT"], Z["powS"], Z["wT"], Z["wS"]); Nk = int(inp["mode_lists"]["Nk"]); Nq = int(inp["mode_lists"]["Nq"])
    rows = {}
    for name in ("A", "C"):
        rows[name] = {}
        for key, rr in inp["constraint_rows"][name].items():
            rows[name][key] = dict(kind=rr["kind"], ra=Z[f"row_{name}_{key}_ra"], **({"rb": Z[f"row_{name}_{key}_rb"]} if rr["kind"] == "pair" else {}), **{k: rr[k] for k in rr if k in ("qc", "qs", "q0")})
    def g_dd(q):
        red = reduced_blocks(tc, model, pm.expand(q)); return g_dd_from(red, rows, consts, Nk, Nq, w)
    def g_prod(q):
        return float(prob.residual_vector(to_full(q))[gr])
    def act(q):
        zz_ = to_full(q); ev = prob.evaluate(zz_, tables=prob.pressure_tables_at(zz_)); return active_set_evidence(prob, ev)
    def decision_key(a):
        # v4.5 (V370 item 1): the validity identity = the production decision fields (median shell, clamped shells, geometry) AND the discrete identities of the actual weight arithmetic
        # (RMS-floor masks per term and slot, argmax sets of den and den_nl, floor-branch flags, clamp set, median slot set); floating values are evidence, not identities
        return json.dumps(dict(decision={k: a[k] for k in ("median_shell", "clamped_shells", "geometry")}, discrete=a.get("discrete_identities")), sort_keys=True)
    base_act = act(zo); base_key = decision_key(base_act); assert base_key == decision_key(inp["base_active_set"]), "base active set differs from the pre-input record"
    assert json.dumps(base_act, sort_keys=True) == json.dumps(inp["base_active_set"], sort_keys=True), "base active-set evidence differs from the pre-input record"
    (g0h, g0l), (N0h, N0l), ex0 = g_dd(zo); g0p = g_prod(zo)
    # held-row map against the production map at the base (information): the production A, C vs the hi parts
    A0, C0, _, _ = model.unpack(to_full(zo).detach()); map_diff = dict(A_max_abs_hi_minus_production=float(np.abs(ex0["A"][0] - A0.detach().cpu().numpy()).max()), C_max_abs_hi_minus_production=float(np.abs(ex0["C"][0] - C0.detach().cpu().numpy()).max()), A_lo_max_abs=float(np.abs(ex0["A"][1]).max()), C_lo_max_abs=float(np.abs(ex0["C"][1]).max()))
    def err(D, dref):
        return abs(D - dref) / max(abs(dref), abs(D), F), abs(D - dref) / max(abs(dref), abs(D))
    lad = {}; same = {}; acts = {"base": base_act}; arrays = dict(z_opt=Z["z_opt"], direction=Z[col["direction_key"]])
    for h in STEPS:
        hh = h * s_j; vals = {}; offs = {}; ok = True
        for t in (hh, -hh, 2 * hh, -2 * hh):
            key = f"{h:.0e}:{t:+.1e}"; q = torch.as_tensor(Z[col["stencil_vectors"][key]["array"]], device=dev)
            (gh, gl), (Nh, Nl), ex = g_dd(q); vals[t] = (gh, gl); offs[t] = float(q[j]) - float(zo[j])
            a_ = act(q); acts[key] = a_; ok = ok and (decision_key(a_) == base_key)
            gp = g_prod(q); exo = exact_offset(q[j].cpu(), zo[j].cpu()) if t > 0 else exact_offset(zo[j].cpu(), q[j].cpu())
            from fractions import Fraction as _F
            off = float(abs(_F(exo["exact"])))                                                           # the ACTUAL stored offset (exact rational, to float for the tolerance)
            same[key] = dict(g_dd=gh + gl, g_dd_hi=gh, g_dd_lo=gl, g_production=gp, diff=gh + gl - gp, actual_offset_exact=exo, tolerance_actual=1e-3 * abs(d) * off, within_actual=abs(gh + gl - gp) <= 1e-3 * abs(d) * off, deciding=(h in (1e-2, 1e-3)), N_dd_hi=Nh, N_dd_lo=Nl)
            arrays[f"zA_hi_{h:.0e}_{t:+.1e}"] = ex["A"][0]; arrays[f"zA_lo_{h:.0e}_{t:+.1e}"] = ex["A"][1]; arrays[f"zC_hi_{h:.0e}_{t:+.1e}"] = ex["C"][0]; arrays[f"zC_lo_{h:.0e}_{t:+.1e}"] = ex["C"][1]
        hp, hm = offs[hh], -offs[-hh]
        from fractions import Fraction
        ex_p = exact_offset(torch.as_tensor(Z[col["stencil_vectors"][f"{h:.0e}:{hh:+.1e}"]["array"]])[j], zo[j].cpu()); ex_m = exact_offset(zo[j].cpu(), torch.as_tensor(Z[col["stencil_vectors"][f"{h:.0e}:{-hh:+.1e}"]["array"]])[j])
        span = Fraction(ex_p["exact"]) + Fraction(ex_m["exact"])                                           # exact (h_plus + h_minus) as a rational
        dh, dl = dd_add(torch.tensor(vals[hh][0]), torch.tensor(vals[hh][1]), torch.tensor(-vals[-hh][0]), torch.tensor(-vals[-hh][1]))
        Dh, Dl = dd_div_f(dh, dl, 2 * hh)
        Da_mp = (mp.mpf(float(dh)) + mp.mpf(float(dl))) / (mp.mpf(span.numerator) / mp.mpf(span.denominator))   # identity-type derivative at the EXACT actual offsets (mpmath)
        d2h, d2l = dd_add(torch.tensor(vals[2 * hh][0]), torch.tensor(vals[2 * hh][1]), torch.tensor(-vals[-2 * hh][0]), torch.tensor(-vals[-2 * hh][1]))
        n8h, n8l = dd_mul_f(dh, dl, 8.0); numh, numl = dd_add(n8h, n8l, -d2h, -d2l); D4h, D4l = dd_div_f(numh, numl, 12 * hh)
        D = float(Dh) + float(Dl); D4 = float(D4h) + float(D4l); Da = float(Da_mp)
        e2, e2_0 = err(D, d); e4, e4_0 = err(D4, d)
        lad[h] = dict(valid=ok, D=D, D_hi=float(Dh), D_lo=float(Dl), D4=D4, D4_hi=float(D4h), D4_lo=float(D4l), e_second_order=e2, e_five_point=e4, e_second_order_F0=e2_0, e_five_point_F0=e4_0,
                      actual_offsets=dict(h_plus_rounded=hp, h_minus_rounded=hm, h_plus_exact=ex_p, h_minus_exact=ex_m, span_exact=f"{span.numerator}/{span.denominator}", h2_plus_rounded=offs[2 * hh], h2_minus_rounded=-offs[-2 * hh], intended=hh, rel_asymmetry_rounded=(hp - hm) / hh, note="rounded scalars are float64 differences (rounded, V366); the exact rationals are the two-word/Fraction differences"), D_actual_offsets=Da, e_second_order_actual_offsets=err(Da, d)[0],
                      g_values={f"{t:+.1e}": v for t, v in vals.items()})
        print(f"h {h:.0e}: valid {ok} D {D:.17e} e2 {e2:.3e} | D4 {D4:.17e} e4 {e4:.3e} | same-function max diff {max(abs(same[f'{h:.0e}:{t:+.1e}']['diff']) for t in (hh, -hh, 2 * hh, -2 * hh)):.3e}", flush=True)
    same0 = dict(g_dd=g0h + g0l, g_production=g0p, diff=g0h + g0l - g0p, tolerance=1e-3 * abs(d) * 1e-3 * s_j, within=abs(g0h + g0l - g0p) <= 1e-3 * abs(d) * 1e-3 * s_j)
    def decide(dref, floorF):
        hs = sorted(lad.keys(), reverse=True)
        def e_of(h, four):
            Dv = lad[h]["D4"] if four else lad[h]["D"]; return abs(Dv - dref) / max(abs(dref), abs(Dv), floorF)
        errs = {h: e_of(h, False) for h in hs}; errs4 = {h: e_of(h, True) for h in hs}
        pairs = [(hs[i], hs[i + 1]) for i in range(len(hs) - 1) if lad[hs[i]]["valid"] and lad[hs[i + 1]]["valid"]]
        ok2 = any(errs[a] <= TAU_GROUP and errs[b] <= TAU_GROUP for a, b in pairs); ok4 = any(errs4[a] <= TAU_GROUP and errs4[b] <= TAU_GROUP for a, b in pairs)
        rich = None; pair = None
        for a, b in pairs:
            if errs[a] <= TAU_GROUP and errs[b] <= TAU_GROUP:
                R = lad[b]["D"] + (lad[b]["D"] - lad[a]["D"]) / 99.0; r_ = abs(R - dref) / max(abs(dref), abs(R), floorF)
                if rich is None or r_ < rich:
                    rich = r_; pair = (a, b)
        return dict(errors_second_order={f"{h:.0e}": errs[h] for h in hs}, errors_five_point={f"{h:.0e}": errs4[h] for h in hs}, valid_pairs=[(f"{a:.0e}", f"{b:.0e}") for a, b in pairs], pass_second_order=ok2, pass_five_point=ok4, richardson_error=rich, richardson_pair=pair, OPEN=(len(pairs) == 0), PASS=bool(ok2 and ok4 and rich is not None and rich <= TAU_GROUP))
    reg = decide(d, F); reg0 = decide(d, 0.0); power = decide(d * (1 + 1e-3), F)
    passing = [h for h in STEPS if lad[h]["valid"] and lad[h]["e_second_order"] <= TAU_GROUP]
    power_min = min((power["errors_second_order"][f"{h:.0e}"] for h in passing), default=None)
    same_ok = bool(same0["within"] and all(v["within_actual"] for v in same.values() if v["deciding"]))
    power_ok = bool(power_min is not None and power_min >= 1e-4 and power["PASS"] is False)                       # v4.2 (verifier 15:57:04Z item 3): the perturbed decision must FAIL as a whole and the error bound must hold
    rec = dict(kind="3.6 (n) (5) evaluation (gauge_row_dd v4)", case=cname, column=j, pair=case.pair, cost=case.cost, device=str(dev), gauge_row=int(gr), gauge_weight=w, step_scale=s_j, steps=STEPS, tau_group=TAU_GROUP,
               pre_input_record=dict(path=os.path.relpath(inp_json, ROOT), sha256=inputs_sha, npz_sha256=npz_sha, ts=inp["ts"]), binding=col["binding"], ties=col["ties"], d=d, d_hex=hexs(d), floor=F,
               base=dict(g_dd_hi=g0h, g_dd_lo=g0l, N_dd_hi=N0h, N_dd_lo=N0l, g_production=g0p, same_function=same0, held_row_map_vs_production=map_diff),
               ladder={f"{h:.0e}": v for h, v in lad.items()}, active_sets=acts, n_valid_steps=sum(1 for h in STEPS if lad[h]["valid"]),
               decision_with_floor=reg, decision_F0=reg0, ladder_PASS=reg["PASS"], ladder_PASS_rel=reg0["PASS"], absolute_only=bool(reg["PASS"] and not reg0["PASS"]),
               same_function_check=dict(base=same0, points=same, deciding_points="base (h = 1e-3 s_j) and the 1e-2 and 1e-3 s_j stencil points, tolerance 1e-3 |d| x actual offset; the fine four steps are information", success=same_ok),
               power_check=dict(d_perturbed=d * (1 + 1e-3), min_error_at_passing_steps=power_min, passing_steps=[f"{h:.0e}" for h in passing], perturbed_decision_full=power, perturbed_PASS=power["PASS"], success=power_ok, rule="d (1 + 1e-3) must fail (overall PASS false) with e >= 1e-4 at the steps where the ladder passes"),
               base_tie=inp.get("base_tie"),
               admitted_n5=bool(reg["PASS"] and same_ok and power_ok), label=("pass under the post-result rule 3.6 (n) (5) (ladder, same-function and power)" if (reg["PASS"] and same_ok and power_ok) else "NOT admitted under 3.6 (n) (5)"),
               registered_outcome_unchanged="the registered gauge-group FAIL of the (k) add-on stands in its record; this record is the (n) (5) re-judgement",
               quantities_left_in_float64=["the stencil inputs (binary64 vectors of the pre-input record)", "the constants R0^(alpha+l), R0^(alpha+l-1), wT, wS, w, k2, k4, the rows k4 - p*1, q*1 (production float64 values held exactly, hex in the pre-input record)", "alpha_production, kappa_production inside those constants", "the steps h and the factors 2h, 8, 12h", "d (the production jvp entry, bound to the registered norm_d)", "the final rounding of g_dd, D_h, D4_h to float64 for the decision and the same-function comparison"],
               sources=dict(held_row_solver="this file (mpmath 50 digits on the held float64 rows)", dd_primitives="src/pressure/exact_matmul.py (dd_add, dd_mul_f, dd_div_f), src/equations/fields_dd.py (dd_mul_dd)"), code_sha256=code_hashes(),
               launcher_manifest=(open(os.path.join(ROOT, "SOURCES_SHA256.txt")).read() if os.path.exists(os.path.join(ROOT, "SOURCES_SHA256.txt")) else None), seconds=time.time() - t0, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    np.savez_compressed(out_npz, **arrays); rec["arrays_npz"] = dict(path=os.path.relpath(out_npz, ROOT), sha256=sha(out_npz), keys=sorted(arrays))
    with open(out_json, "x") as fh:
        json.dump(rec, fh, indent=1, default=str)
    print("DECISION", cname, "column", j, "ladder PASS", reg["PASS"], "PASS_rel", reg0["PASS"], "Richardson", reg["richardson_error"], reg["richardson_pair"], "| same-function", same_ok, "| power", power_ok, "| admitted_n5", rec["admitted_n5"], f"{time.time() - t0:.0f}s")
    print("DONE", out_json)


def main():
    mode, cname = sys.argv[1], sys.argv[2]; mp.mp.dps = DPS
    if mode == "prepare":
        dev = sys.argv[3] if len(sys.argv) > 3 else ("cuda:0" if torch.cuda.is_available() else "cpu"); prepare(cname, dev)
    elif mode == "evaluate":
        j = int(sys.argv[3]); dev = sys.argv[4] if len(sys.argv) > 4 else ("cuda:0" if torch.cuda.is_available() else "cpu"); evaluate(cname, j, dev)
    else:
        raise SystemExit("mode: prepare | evaluate")


if __name__ == "__main__":
    main()

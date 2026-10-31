"""D6FP D1 / T3 (lead 00:25Z item 2 T3, 00:38Z item 2): for the eight blocks that failed T2 (ii) (far rows at S01, S05, S09; far anchors at S01,
S05, S09, S20 and the V027 input), the 20 rows of largest |D| (D = r_fp64 - r_dd2 at z) are evaluated in 45-digit decimal arithmetic from the
SAME float64 inputs: coefficient contraction and twist of the radial arrays (float64 basis and twist tables), scalar sets, angular contraction
(float64 angular tables), assembly of DU and the source tr(DU^2) at every source node, angular analysis, twisted frame and factored scaling
(float64 cosb, sinb, sfac, lfac), radial Green sums (float64 Qc, Qs), and the synthesis of grad P at the selected rows (float64 A0p, A1p). The
stable linear and U . grad U terms of a row are the same float64 numbers in both evaluations (they do not touch the pressure; the term split showed
D is grad P only), so the row reference is W_i (lin_i + nl_i + gradP_i^(45 digits)) with the production row weight W_i = r_i / sum_i at z.
Per row: reference, dd2 - reference, fp64 - reference and D, relative to the block norm; adoption condition (lead): dd2 within 1e-12 of the block
norm in every row and |fp64 - reference| within a factor 2 of |D|. Diagnostic a_x = <D(x), D(z)> / ||D(z)||^2 at the five points of Test T.
Output validation/d1_test_T3.json."""
import sys, os, json, time, math
MYROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, MYROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from decimal import Decimal, getcontext
from validation.gates import Case, ROOT
from src.equations.fields import alpha_of
from src.equations.fields_dd import EPS_LIST
import glob
getcontext().prec = 45
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
def Dz(a):
    return np.vectorize(lambda v: Decimal(float(v)), otypes=[object])(np.asarray(a, dtype=float))
def T2np(t):
    return t.detach().cpu().numpy()
def run_state(name, case, want_far, want_anchor):
    prob, model, ps = case.prob, case.model, case.prob.pressure; zf = case.z_full
    t0 = time.time()
    # --- fp64 and dd2 residuals, terms and weights at z ---
    prob.source_precision = "fp64"; prob.pressure.chain_precision = "fp64"
    with torch.no_grad():
        r64 = prob.objective_at(zf, need_aux=False)[0]
        ev = prob.evaluate(zf, tables=prob.pressure_tables_at(zf)); mt = ev["mom_terms"]; F = ev["F"]
        lin = mt["lin_stable"]; adv = torch.einsum('m...,mi...->i...', F["U"], F["GU"]); gP64 = mt["gradP"]; ssum = mt["sum"]
    prob.source_precision = "dd"; prob.pressure.chain_precision = "dd"
    with torch.no_grad():
        rdd = prob.objective_at(zf, need_aux=False)[0]
        evd = prob.evaluate(zf, tables=prob.pressure_tables_at(zf)); gPdd = evd["mom_terms"]["gradP"]
        lin_dd = evd["mom_terms"]["lin_stable"]; adv_dd = torch.einsum('m...,mi...->i...', evd["F"]["U"], evd["F"]["GU"]); ssum_dd_t = evd["mom_terms"]["sum"]
    prob.source_precision = "fp64"; prob.pressure.chain_precision = "fp64"
    Nr, Na = model.Nr, model.Na; npde = 3 * Nr * Na
    Dvec = r64 - rdd
    W = (r64[:npde] / torch.where(ssum.reshape(-1).abs() > 0, ssum.reshape(-1), torch.ones_like(ssum.reshape(-1)))).reshape(3, Nr, Na)
    blocks = {}
    far_mask = (case.row_group == case.group_names.index("far(r>256R0)")) & ~case.anchor_mask
    if want_far:
        blocks["far(r>256R0)"] = far_mask
    if want_anchor:
        blocks["far_anchor_block"] = case.anchor_mask
    sel = {}
    for b, m in blocks.items():
        idx = torch.nonzero(m).flatten()
        top = idx[torch.argsort(Dvec[idx].abs(), descending=True)[:20]]
        sel[b] = dict(rows=top.tolist(), block_norm=float(r64[m].norm()), n_rows=int(m.sum()))
    # --- 45-digit pipeline from the float64 inputs ---
    d = model.unpack_all(zf); K = 4
    with torch.no_grad():
        alpha_t = alpha_of(d["c_l"]); R0t = torch.tensor(model.R0, dtype=torch.float64, device=dev); ch = model.channels
        BT = T2np(model.rb.matrices(model.rho, alpha_t, R0t, model.L_ext, K, shift=0.0)); BS = T2np(model.rb.matrices(model.rho, alpha_t, R0t, model.L_ext, K, shift=1.0))
        BB = T2np(model.rb.matrices(model.rho, alpha_t, R0t, model.L_ext, K, power=lambda l: 2 * alpha_t + 1 + l, core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkB"])) if ch["NkB"] > 0 else None
        BD = T2np(model.rb.matrices(model.rho, alpha_t, R0t, model.L_ext, K, power=lambda l: 2 * alpha_t + l, core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkD"])) if ch["NkD"] > 0 else None
        BE = T2np(model.rb.matrices(model.rho, alpha_t, R0t, model.L_ext, K, power=lambda l: torch.as_tensor(2.0 * l + 1.0, dtype=torch.float64, device=dev), core_damp=ch["core_damp"], R1=ch["R1"], Nk=ch["NkE"], lmask=[0, 1])) if ch["NkE"] > 0 else None
        Ct, St = model.rb.twist_tables(model.rho, d["omega"], d["c_l"], R0t, model.Mmax, K); Ct = T2np(Ct); St = T2np(St)
    lidx = T2np(model.l_idx).astype(int); marr = T2np(model.m_arr).astype(int); partner = T2np(model.partner).astype(int); tws = T2np(model.tw_sign)
    Nq = len(lidx)
    def contract(Btab, coef):
        out = np.empty((K + 1, Nr, Nq), dtype=object)
        Bq = Dz(Btab[lidx]); cD = Dz(coef)                                   # (Nq, K+1, Nr, Nk), (Nk, Nq)
        for q in range(Nq):
            out[:, :, q] = np.dot(Bq[q], cD[:, q])
        return out
    gT = contract(BT, T2np(d["A"])); gS = contract(BS, T2np(d["C"]))
    if BB is not None and d["B"].numel() > 0: gT = gT + contract(BB, T2np(d["B"]))
    if BD is not None and d["D"].numel() > 0: gS = gS + contract(BD, T2np(d["D"]))
    CmD = Dz(Ct[marr]).transpose(1, 2, 0); SmD = Dz(St[marr]).transpose(1, 2, 0) * Dz(tws)[None, None, :]
    def twist(g):
        if model.pair_c.numel() == 0:
            return g
        gp = g[:, :, partner]; out = np.empty_like(g)
        for n in range(K + 1):
            acc = np.zeros_like(g[0])
            for k in range(n + 1):
                acc = acc + Decimal(math.comb(n, k)) * (g[k] * CmD[n - k] + gp[k] * SmD[n - k])
            out[n] = acc
        return out
    gT = twist(gT); gS = twist(gS)
    if BE is not None and d["E"].numel() > 0: gS = gS + contract(BE, T2np(d["E"]))
    lD = Dz(T2np(model.l_arr))[None, :]; rhoD = Dz(T2np(model.rho))[:, None]; rD = Dz(T2np(model.r))[:, None]; rlD = Dz(T2np(model.rl)); nD = Dz(T2np(model.n)).T
    A0 = Dz(T2np(model.A0)); A1 = [Dz(T2np(model.A1[i])) for i in range(3)]; A2 = [[Dz(T2np(model.A2[i, j])) for j in range(3)] for i in range(3)]
    def sets():
        Tset = (gT[0], gT[1], gT[2])
        Kset = ((lD + 1) * gS[0] + 2 * rhoD * gS[1], (lD + 3) * gS[1] + 2 * rhoD * gS[2], (lD + 5) * gS[2] + 2 * rhoD * gS[3])
        Dset = ((6 + 4 * lD) * gS[1] + 4 * rhoD * gS[2], (10 + 4 * lD) * gS[2] + 4 * rhoD * gS[3], (14 + 4 * lD) * gS[3] + 4 * rhoD * gS[4])
        return Tset, Kset, Dset
    def grid(h, need_grad, need_hess, need_val):
        h0, h1, h2 = h
        f = np.dot(rlD * h0, A0.T) if need_val else None
        grad = None; hess = None
        if need_grad:
            G1 = np.dot(rlD * rD * h1, A0.T); Gm1 = rlD / rD * h0
            grad = [2 * G1 * nD[i][None, :] + np.dot(Gm1, A1[i].T) for i in range(3)]
        if need_hess:
            G2 = np.dot(rlD * rD * rD * h2, A0.T); H1 = rlD * h1; H1A0 = np.dot(H1, A0.T); H1A1 = [np.dot(H1, A1[i].T) for i in range(3)]; Hm2 = rlD / (rD * rD) * h0
            hess = [[4 * G2 * nD[i][None, :] * nD[j][None, :] + 2 * ((H1A0 if i == j else 0) + H1A1[j] * nD[i][None, :] + H1A1[i] * nD[j][None, :]) + np.dot(Hm2, A2[i][j].T) for j in range(3)] for i in range(3)]
        return f, grad, hess
    Tset, Kset, Dset = sets()
    _, gT_, hT_ = grid(Tset, True, True, False); _, _, hK = grid(Kset, False, True, False); dD, gD, _ = grid(Dset, True, False, True)
    GU = [[None] * 3 for _ in range(3)]
    for m in range(3):
        for i in range(3):
            v = hK[m][i].copy()
            for k in range(3):
                e = EPS_LIST[i][m][k]
                if e != 0.0: v = v - Decimal(e) * gT_[k]
            for j in range(3):
                for k in range(3):
                    e = EPS_LIST[i][j][k]
                    if e != 0.0: v = v - Decimal(e) * (rD * nD[j][None, :]) * hT_[m][k]
            if m == i: v = v - dD
            v = v - (rD * nD[i][None, :]) * gD[m]
            GU[m][i] = v
    fsrc = sum(GU[m][i] * GU[i][m] for m in range(3) for i in range(3))             # (Nr, Na) 45-digit source
    f64 = T2np(torch.einsum('mi...,im...->...', F["GU"], F["GU"]))
    Na_ = f64.shape[1]
    src_check = max(float(abs(fsrc[j, a] - Decimal(float(f64[j, a])))) / max(abs(float(f64[j, a])), 1e-300) for (j, a) in [(5, 17 % Na_), (24, 600 % Na_), (min(47, ps.Nr_src - 1), 1200 % Na_), (0, 3), (ps.Nr_src - 1, 900 % Na_)])   # in-bounds diagnostic indices (verifier V106)
    t_src = time.time() - t0
    # --- pressure chain in 45 digits ---
    Tb = ps.tables; Nrs = ps.Nr_src
    A0pw = Dz(T2np(ps.A0pw)); cosb = Dz(T2np(Tb["cosb"])); sinb = Dz(T2np(Tb["sinb"])); sfac = Dz(T2np(Tb["sfac"]))[:, None]; lfac = Dz(T2np(ps.lfac))
    ppart = T2np(ps.partner).astype(int); psign = Dz(T2np(ps.sign)); plD = Dz(T2np(ps.pl))
    flm = np.dot(fsrc[:Nrs], A0pw)                                                     # (Nr_src, Nqp)
    if cosb.ndim == 1: cosb = np.broadcast_to(cosb, flm.shape); sinb = np.broadcast_to(sinb, flm.shape)
    ftw = (flm * cosb - psign[None, :] * flm[:, ppart] * sinb) * sfac * lfac
    ftw_p = ftw[:, ppart]
    Qc = Dz(T2np(Tb["Qc"][ps.pl_long, ps.pm])); Qs = Dz(T2np(Tb["Qs"][ps.pl_long, ps.pm]))     # (Nqp, 2, Ne, Nr_src)
    Nqp = ftw.shape[1]; Ne = Qc.shape[2]
    t1 = np.empty((Ne, Nqp), dtype=object); t2 = np.empty((Ne, Nqp), dtype=object)
    for q in range(Nqp):
        t1[:, q] = np.dot(Qc[q, 0], ftw[:, q]) + psign[q] * np.dot(Qs[q, 0], ftw_p[:, q])
        t2[:, q] = np.dot(Qc[q, 1], ftw[:, q]) + psign[q] * np.dot(Qs[q, 1], ftw_p[:, q])
    Plm = t1 + t2; reD = Dz(T2np(ps.eval_model.r))[:, None]
    dPlm = (-(plD[None, :] + 1) * t1 + plD[None, :] * t2) / reD
    A0p = Dz(T2np(ps.A0p)); A1p = [Dz(T2np(ps.A1p[i])) for i in range(3)]; ngrid = Dz(T2np(ps.eval_model.grid.n)).T
    radial_coef = dPlm - plD[None, :] * Plm / reD
    Wn = T2np(W); lin_n = T2np(lin); adv_n = T2np(adv); gP64_n = T2np(gP64); gPdd_n = T2np(gPdd); r64_n = T2np(r64); rdd_n = T2np(rdd)
    ssum_dd = ssum_dd_t.reshape(-1); Wdd = (rdd[:npde] / torch.where(ssum_dd.abs() > 0, ssum_dd, torch.ones_like(ssum_dd))).reshape(3, Nr, Na)
    Wratio = T2np(Wdd / torch.where(W.abs() > 0, W, torch.ones_like(W)))                   # lead 00:54Z / V106: the dd2 residual recomputes the pressure-dependent row weights
    Wdd_n = T2np(Wdd); sum64_n = T2np(ssum); sumdd_n = T2np(ssum_dd_t); lin_dd_n = T2np(lin_dd); adv_dd_n = T2np(adv_dd)
    import hashlib
    def h256(t):
        return hashlib.sha256(T2np(t).tobytes()).hexdigest()[:16]
    tables_identity = dict(statement="every table the 45-digit reference reads is the float64 tensor the dd2 path consumes (radial basis rb.matrices, twist tables, angular A0/A1/A2, pressure A0pw, cosb, sinb, sfac, lfac, Qc, Qs, A0p, A1p); the dd2 path builds none of them in double-double (it accumulates from them)",
                           sha256_16=dict(A0=h256(model.A0), A1=h256(model.A1), A2=h256(model.A2), rl=h256(model.rl), A0pw=h256(ps.A0pw), cosb=h256(Tb["cosb"]), sinb=h256(Tb["sinb"]), sfac=h256(Tb["sfac"]), lfac=h256(ps.lfac), Qc=h256(Tb["Qc"]), Qs=h256(Tb["Qs"]), A0p=h256(ps.A0p), A1p=h256(ps.A1p)))
    out_blocks = {}
    for b, info in sel.items():
        rows = []
        for ridx in info["rows"]:
            c = ridx // (Nr * Na); j = (ridx // Na) % Nr; a = ridx % Na
            radial = sum(radial_coef[j, q] * A0p[a, q] for q in range(Nqp))
            gP_ref = radial * ngrid[c][a] + sum(Plm[j, q] / reD[j, 0] * A1p[c][a, q] for q in range(Nqp))
            # reference with the dd2 row weight (lead 00:54Z item 1): W_dd (lin + nl + gradP_45); lin and nl are the float64 values (shown identical in both paths below)
            ref = Decimal(float(Wdd_n[c, j, a])) * (Decimal(float(lin_n[c, j, a])) + Decimal(float(adv_n[c, j, a])) + gP_ref)
            dd_minus = float(Decimal(float(rdd_n[ridx])) - ref); fp_minus = float(Decimal(float(r64_n[ridx])) - ref); Dv = float(r64_n[ridx] - rdd_n[ridx])
            w_part = float((Wn[c, j, a] - Wdd_n[c, j, a]) * sum64_n[c, j, a]); t_part = float(Wdd_n[c, j, a] * (sum64_n[c, j, a] - sumdd_n[c, j, a]))
            rows.append(dict(row=int(ridx), comp=int(c), node=int(j), r_node=float(model.r[j]), angle=int(a), reference=float(ref), dd2_minus_ref=dd_minus, fp64_minus_ref=fp_minus, D=Dv,
                             dd2_minus_ref_over_block=dd_minus / info["block_norm"], fp64_minus_ref_over_block=fp_minus / info["block_norm"], D_over_block=Dv / info["block_norm"],
                             D_weight_part=w_part, D_term_part=t_part, D_split_check=float(w_part + t_part - Dv),
                             lin_dd2_minus_fp64=float(lin_dd_n[c, j, a] - lin_n[c, j, a]), adv_dd2_minus_fp64=float(adv_dd_n[c, j, a] - adv_n[c, j, a]),
                             gradP_ref=float(gP_ref), gradP_dd2=float(gPdd_n[c, j, a]), gradP_fp64=float(gP64_n[c, j, a]), gradP_dd2_minus_ref_rel=float(Decimal(float(gPdd_n[c, j, a])) - gP_ref) / max(abs(float(gP_ref)), 1e-300),
                             ratio_fp64err_over_D=(abs(fp_minus) / abs(Dv) if Dv != 0 else None)))
        for x in rows:
            x["weight_ratio_dd2_over_fp64_minus_1"] = float(Wratio[x["comp"], x["node"], x["angle"]] - 1.0)
        max_dd = max(abs(x["dd2_minus_ref_over_block"]) for x in rows); ratios = [x["ratio_fp64err_over_D"] for x in rows if x["ratio_fp64err_over_D"] is not None]
        cond1 = max_dd <= 1e-12; cond2 = all(0.5 <= v <= 2.0 for v in ratios)
        out_blocks[b] = dict(block_norm=info["block_norm"], n_rows_block=info["n_rows"], rows=rows, max_abs_dd2_minus_ref_over_block=max_dd, max_abs_weight_ratio_minus_1=max(abs(x["weight_ratio_dd2_over_fp64_minus_1"]) for x in rows),
                             block_max_abs_weight_ratio_minus_1=float(abs(Wratio.reshape(-1)[T2np(blocks[b][:npde]).astype(bool)] - 1.0).max()),      # the block's own mask (verifier V112)
                             max_abs_lin_dd2_minus_fp64=max(abs(x["lin_dd2_minus_fp64"]) for x in rows), max_abs_adv_dd2_minus_fp64=max(abs(x["adv_dd2_minus_fp64"]) for x in rows),
                             D_weight_part_norm_over_block=math.sqrt(sum(x["D_weight_part"] ** 2 for x in rows)) / info["block_norm"], D_term_part_norm_over_block=math.sqrt(sum(x["D_term_part"] ** 2 for x in rows)) / info["block_norm"], max_abs_fp64_minus_ref_over_block=max(abs(x["fp64_minus_ref_over_block"]) for x in rows),
                             max_abs_D_over_block=max(abs(x["D_over_block"]) for x in rows), fp64err_over_D_min_max=(min(ratios), max(ratios)) if ratios else None, cond_dd2_within_1e12=bool(cond1), cond_fp64_within_factor2_of_D=bool(cond2), adopt_block=bool(cond1 and cond2))
        print(f"{name} {b}: |dd2 - ref| / ||r_b|| max {max_dd:.2e}; |fp64 - ref| / ||r_b|| max {out_blocks[b]['max_abs_fp64_minus_ref_over_block']:.2e}; |D| / ||r_b|| max {out_blocks[b]['max_abs_D_over_block']:.2e}; fp64 error / D in [{min(ratios):.3f}, {max(ratios):.3f}]; gradP dd2 vs ref (rel) max {max(abs(x['gradP_dd2_minus_ref_rel']) for x in rows):.1e}; adopt {out_blocks[b]['adopt_block']}", flush=True)
    # --- a_x diagnostic at the five points of Test T ---
    rng = np.random.default_rng(3); zp = case.z_phys; E = []
    for t in range(2):
        e = torch.tensor(rng.normal(size=zp.numel()), device=dev); e[-2:] = 0; E.append(e / e.norm())
    ax = {b: {} for b in blocks}
    with torch.no_grad():
        for lbl, q in (("+1e-08e0", zp + 1e-8 * E[0]), ("-1e-08e0", zp - 1e-8 * E[0]), ("+1e-08e1", zp + 1e-8 * E[1]), ("-1e-08e1", zp - 1e-8 * E[1])):
            prob.source_precision = "fp64"; prob.pressure.chain_precision = "fp64"; ra = prob.objective_at(case.to_full_phys(q), need_aux=False)[0]
            prob.source_precision = "dd"; prob.pressure.chain_precision = "dd"; rb_ = prob.objective_at(case.to_full_phys(q), need_aux=False)[0]
            Dx = ra - rb_
            for b, m in blocks.items():
                ax[b][lbl] = float((Dx[m] @ Dvec[m]) / max(float(Dvec[m] @ Dvec[m]), 1e-300))
    prob.source_precision = "fp64"; prob.pressure.chain_precision = "fp64"
    for b in blocks:
        ax[b]["z"] = 1.0; out_blocks[b]["a_x"] = ax[b]
    return dict(blocks=out_blocks, source_check_rel_fp64_vs_45digit_at_5_nodes=src_check, tables_identity=tables_identity, seconds_source=t_src, seconds_total=time.time() - t0)
import argparse
ap = argparse.ArgumentParser(); ap.add_argument("--cases", default="S01,S05,S09,S20,V027_input"); ap.add_argument("--merge", action="store_true", help="merge into the existing d1_test_T3.json")
args = ap.parse_args(); CASES = args.cases.split(",")
outp = os.path.join(MYROOT, "validation", "d1_test_T3.json")
out = json.load(open(outp)) if (args.merge and os.path.exists(outp)) else dict(started=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), precision_digits=45, cases={})
out["note_weights"] = "row reference = W_dd2 (lin + nl + gradP_45digit) with W_dd2 the production row weight of the dd2 evaluation (lead 00:54Z item 1); lin and nl are the float64 terms (identical in both paths, recorded); the weights are functions of dd2 terms over whole shells and are not recomputed in 45 digits; per row: W_dd2/W_fp64 - 1 and the split of D into the weight part (W64 - Wdd) sum64 and the term part Wdd (sum64 - sumdd)"
starts = dict(S01=("S01_nest6_cl0.45_om1.0_p0.pt", True, True), S05=("S05_nest6_cl0.45_om0.3_p0.pt", True, True), S09=(None, True, True), S20=(None, False, True))
for key in ("S09", "S20"):
    m = sorted(glob.glob(os.path.join(ROOT, "starts", f"{key}_*.pt"))); starts[key] = (os.path.basename(m[0]) if m else None, starts[key][1], starts[key][2])
for key, (fn, wf, wa) in starts.items():
    if fn is None or key not in CASES: continue
    case = Case(key, dev, start=os.path.join(ROOT, "starts", fn)); out["cases"][key] = dict(start=fn, **run_state(key, case, wf, wa)); del case; torch.cuda.empty_cache()
    json.dump(out, open(os.path.join(MYROOT, "validation", "d1_test_T3.json"), "w"), indent=1)
inp = "RUN_ROOT/verifier/artifacts/inputs/manufactured_geometric_even"
dnp = np.load(os.path.join(inp, "coeffs.npz"), allow_pickle=True); TT = lambda a: torch.tensor(np.asarray(a, dtype=float))
arrays = dict(A=TT(dnp["A"]), C=TT(dnp["C"]), B=TT(dnp["B"]), D=TT(dnp["D"]), E=TT(dnp["E"]), channels=json.loads(str(dnp["channels"])), m_parity=str(dnp["m_parity"]), R0=float(dnp["R0"]), Nk=int(dnp["Nk"]), Nr=48, desc="V027 input")
if "V027_input" in CASES:
    case = Case("V027", dev, arrays=arrays, pair=(0.42, 0.3), align=False, grid=(20, 38)); out["cases"]["V027_input"] = dict(start=inp, **run_state("V027_input", case, False, True))
out["adopt_all_blocks"] = all(b["adopt_block"] for c in out["cases"].values() for b in c["blocks"].values())
json.dump(out, open(os.path.join(MYROOT, "validation", "d1_test_T3.json"), "w"), indent=1)
print("DONE adopt_all_blocks:", out["adopt_all_blocks"])

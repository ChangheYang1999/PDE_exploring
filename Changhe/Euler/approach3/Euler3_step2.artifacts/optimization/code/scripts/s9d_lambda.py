#!/usr/bin/env python
"""S9d (lead registration 2026-10-25T17:20:02Z, reports/stage2_plan_draft.md after S9c): balance-row weights for the balance chain from a
chain start Z0 (the end state of an S11 closure-weight-1 rung).
  C0 = plain sum of squares of the weighted momentum rows at Z0 (no pin, closure or balance rows; the same nonlinear shell weights and
       fixed-gauge scaling as the worker's momentum rows, refreshed at Z0 as the worker does at a start),
  b0 = E_ren(Z0)^2 + (H_tot/int|h|)(Z0)^2  (from the ledger start_result of the Z0 run, or recomputed with GlobalBalances when --recompute),
  balance_lambda_k = sqrt(kappa_k C0 / b0), kappa_k in (0.1, 1, 10, 100); lambda_k fixed from Z0, never recomputed along the chain.
Writes reports/s9d_lambda_<job>.json and prints the enqueue lines (100 iterations per step, closure rows at weight 1, core_pin auto,
nonaxi_pin auto, c_l and omega fixed, all5far, the S11 channels; priority 12).
Usage: s9d_lambda.py <Z0 start .pt> [--device cpu|cuda:0] [--recompute]"""
import sys, os, json, math, argparse


def s9d_weights(C0, E_ren, ratio, kappas=(0.1, 1.0, 10.0, 100.0), target=0.05):
    """S9d chain weights (lead 2026-10-25T17:20:02Z; verifier repairs 18:32Z): skip BEFORE any division. Returns a structured record:
    skip (bool), reason, b0, lambda_by_kappa (None when skipped). b0 = E_ren^2 + ratio^2; lambda_k = sqrt(kappa_k C0 / b0)."""
    b0 = float(E_ren) ** 2 + float(ratio) ** 2
    if abs(float(E_ren)) <= target and abs(float(ratio)) <= target:
        return dict(skip=True, reason=f"Z0 already meets both targets (|E_ren| {abs(float(E_ren)):.17g} <= {target:g} and |H_tot|/int|h| {abs(float(ratio)):.17g} <= {target:g})", b0=b0, lambda_by_kappa=None)
    if b0 <= 0.0 or not math.isfinite(b0):
        return dict(skip=True, reason=f"b0 = {b0!r} is zero or not finite: lambda undefined", b0=b0, lambda_by_kappa=None)
    if not (math.isfinite(float(C0)) and float(C0) > 0.0):
        return dict(skip=True, reason=f"C0 = {C0!r} is not positive and finite", b0=b0, lambda_by_kappa=None)
    return dict(skip=False, reason="", b0=b0, lambda_by_kappa={("%g" % k): math.sqrt(k * float(C0) / b0) for k in kappas})


def main():
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "scripts"))
    import torch
    torch.set_default_dtype(torch.float64)
    ap = argparse.ArgumentParser(); ap.add_argument("start"); ap.add_argument("--device", default="cuda:0" if torch.cuda.is_available() else "cpu")
    ap.add_argument("--recompute", action="store_true", help="recompute E_ren and H_tot/int|h| at Z0 instead of reading the ledger record")
    a = ap.parse_args()
    import importlib.util
    spec = importlib.util.spec_from_file_location("worker", os.path.join(ROOT, "scripts", "worker.py")); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W)
    S = torch.load(a.start, map_location="cpu", weights_only=False)
    cfg = dict(S["config"]); job = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(a.start))))
    for k in ("core_pin", "nonaxi_pin", "balance_lambda", "radial_lambda_w", "fsw", "efrac", "nu", "pin_c_l"):
        cfg.pop(k, None)
    cfg["closure_lambda"] = 0.0
    model, prob = W.build(cfg, a.device)
    z = S["z"].to(a.device)
    prob.pivot = S.get("pivot") if S.get("pivot") is not None else prob.choose_pivot(z)
    prob.maybe_rebuild_pressure(z); prob.update_nl_weights(z)
    with torch.no_grad():
        r = prob.residual_vector(z)
    npde = prob.n_pde_residuals()
    C0 = float((r[:npde] ** 2).sum()); C_gauge = float((r[npde:] ** 2).sum())
    rec = None
    rp = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(a.start))), "results.jsonl")
    if os.path.exists(rp):
        for line in open(rp):
            d = json.loads(line)
            if d.get("zfile", "").endswith(os.path.basename(a.start)) or d.get("start") == int(os.path.basename(a.start)[6:9]):
                rec = d
    # b0 from the SAME balance-row object the S9 rows use (Problem.balance_rows -> GlobalBalances.integrals; verifier rule via the lead 17:49Z)
    prob.balance_lambda = 1.0
    with torch.no_grad():
        rows = prob.balance_rows(z)
    E_ren, ratio, src = float(rows[0]), float(rows[1]), "Problem.balance_rows at lambda 1 (GlobalBalances.integrals)"
    ledger_vals = dict(E_ren=(rec or {}).get("E_ren"), H_tot_over_abs=(rec or {}).get("H_tot_over_abs"))
    b0 = E_ren ** 2 + ratio ** 2
    # frozen numeric pins at Z0 (the worker's 'auto' definitions, evaluated here once): core RMS of U on the training nodes r < R0; e_core on the core shells with
    # lower edge <= r_tail (r_tail = Z0's SPEC 7.4 N5_r_tail from its training spec_diag, as the worker's auto branch does) and e_F of the leading tail
    r_tail = float(((S.get("spec_diag") or {}).get("guards") or {}).get("N5_r_tail") or 1.0)
    prob.nonaxi_r_tail = r_tail
    with torch.no_grad():
        F0 = model.fields_grid(z, need_vort=False); aT0, aS0, cl0, om0 = model.unpack(z)
        core_pin = float(prob.core_rms(F0)); e_core0 = float(prob.e_core_training(F0)); e_F0 = float(prob.e_F_tail(aT0, aS0, cl0, om0))
    targets_met = abs(E_ren) <= 0.05 and abs(ratio) <= 0.05
    W = s9d_weights(C0, E_ren, ratio)
    kappas = [0.1, 1.0, 10.0, 100.0]
    lam = W["lambda_by_kappa"]          # None when skipped (no division performed)
    out = dict(job=job, start=os.path.relpath(os.path.abspath(a.start), ROOT), c_l=cfg["c_l"], omega=cfg["omega"], omega_over_c_l=cfg["omega"] / cfg["c_l"], C0_momentum_rows=C0, gauge_rows_cost=C_gauge, n_pde_rows=npde,
               E_ren=E_ren, H_tot_over_abs=ratio, b0=b0, balances_source=src, ledger_values=ledger_vals, balance_lambda_by_kappa=lam, device=a.device,
               pins_frozen_at_Z0=dict(core_pin=core_pin, nonaxi_pin=[e_core0, e_F0], nonaxi_r_tail=r_tail), targets_met_at_Z0=targets_met,
               skip=W["skip"], skip_reason=W["reason"], chain_commands=[],
               definition="lambda_k = sqrt(kappa_k C0 / b0); C0 = sum of squares of the weighted momentum rows at Z0 (no pin/closure/balance rows); b0 = E_ren^2 + (H_tot/int|h|)^2 at Z0 (lead 2026-10-25T17:20:02Z)")
    os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
    op = os.path.join(ROOT, "reports", f"s9d_lambda_{job}.json"); json.dump(out, open(op, "w"), indent=1)
    print(json.dumps(out, indent=1))
    ch = model.channels or {}
    chdeg = "%d,%d,%d" % tuple(int(ch.get(k) or cfg["L"]) for k in ("LB", "LD", "LE"))
    nk = "%d,%d,%d" % tuple(int(ch.get(k) or 0) for k in ("NkB", "NkD", "NkE"))
    if nk == "0,0,0":
        print("NOTE: Z0 has no B/D/E channels; the lines below add --channels 4,4,4 --chdeg 2L+3,2L+2,L (SPEC 4.4) so that the closure rows at weight 1 exist")
        nk = "4,4,4"; chdeg = "%d,%d,%d" % (2 * cfg["L"] + 3, 2 * cfg["L"] + 2, cfg["L"])
    src_path = out["start"]
    if W["skip"]:
        print("SKIP: " + W["reason"] + " -> no chain weights, no enqueue commands (lead 17:49Z; verifier 18:32Z)")
    else:
        pins = f"--core_pin {core_pin:.17g} --nonaxi_pin {e_core0:.17g},{e_F0:.17g} --nonaxi_r_tail {r_tail:.17g}"
        for i, k in enumerate(kappas):
            cmd = (f"scripts/enqueue_continuation.py --src {src_path if i == 0 else '<end state of the previous step>'} --tag s9d --L {cfg['L']} --Nk {cfg['Nk']} --channels {nk} --chdeg {chdeg} --closure_lambda 1 --nl_den all5far "
                   f"--balance_lambda {lam['%g' % k]:.17g} {pins} --max_iter 100 --time_limit 5400 --exclusive --priority 12 --suffix _k{k:g}")
            out["chain_commands"].append(cmd)
            print(cmd + ("   # from Z0" if i == 0 else f"   # --src = the end state of the k{kappas[i-1]:g} step"))
    json.dump(out, open(op, "w"), indent=1)
    print(f"wrote {op}")


if __name__ == "__main__":
    main()

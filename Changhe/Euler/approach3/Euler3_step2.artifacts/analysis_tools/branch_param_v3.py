"""Parameter part of the branch-identity test (lead note 2026-10-29T18:31:20Z item 3). Lead check tool, CPU only.

Usage: branch_param.py SENS_JSON EVAL_NPZ RUN_A RUN_B [LABEL]

RUN_A and RUN_B are run directories with a completed results record (results.jsonl, last "start_result"); state a is
the end state of RUN_A, state b the end state of RUN_B. SENS_JSON is the sensitivity.py (version 6) output for state a,
EVAL_NPZ the J_c EVAL record of state a (its jc_eval.json lies beside it). With cutoff 1e-12:
lambda_i = reduced."1e-12".S_eigvals_scaled, w_i = columns of reduced."1e-12".S_eigvecs_scaled_columns, O1 = the record's
O1, t_i = sqrt(2 x 0.01 x O1 / lambda_i). Delta s = D_p * (z_b - z_a) componentwise, z = (z_c, z_w),
z_c = log(x / (1 - x)), x = (c_l - 0.4) / 0.1, z_w = log(omega), D_p = the EVAL record's D at its two parameter columns
(optimizer coordinates). c_i = w_i . Delta s; agreement at a if |c_i| <= t_i for i = 1, 2. Prints one JSON object.

Binding (version 3, after the verifier's V414 and V425). Any failure prints "parameter part OPEN: <reason>" and exits
with status 2; nothing else is printed. Required:
- every number used is finite (costs, parameters, D_p, the reduced matrix, eigenvalues, eigenvectors, O1);
- the width record has version 6, was made from this EVAL record (same path), J_c kind, optimizer coordinates;
- the EVAL record: J_c kind, optimizer coordinates, parameter columns last and equal to param_positions; its
  jc_eval.json has kind EVAL, status ACCEPTED, the same iteration, parameters and cost, names RUN_A as its run, and its
  checkpoint file (if still present) has the recorded sha256;
- the iteration (integer), c_l, omega and cost are equal (exactly, as stored) between the width record's record_meta,
  the EVAL npz, the jc_eval.json and RUN_A's results record (iterations, params_final, cost_final); O1 of the width
  record equals the npz cost to 1e-12 relative;
- eigenvalues positive, eigenvectors orthonormal to 1e-12, matching the reduced matrix to 1e-10; D_p positive;
- state b: RUN_B's results record has finite params_final c_l in (0.4, 0.5), omega > 0, and an integer iteration count.
Versions 1 and 2 are kept as branch_param_v1.py and branch_param_v2.py."""
import ast
import hashlib
import json
import math
import os
import sys

import numpy as np


def fail(why):
    print("parameter part OPEN: " + why, file=sys.stderr)
    sys.exit(2)


def z(cl, om):
    x = (cl - 0.4) / 0.1
    return np.array([math.log(x / (1.0 - x)), math.log(om)])


def finite(*xs):
    return all(np.all(np.isfinite(np.asarray(x, float))) for x in xs)


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def end_record(run):
    p = os.path.join(run, "results.jsonl")
    if not os.path.isfile(p):
        fail("no results record in %s" % run)
    with open(p) as f:
        recs = [json.loads(l) for l in f if l.strip()]
    recs = [r for r in recs if r.get("kind") == "start_result"]
    if not recs:
        fail("no start_result in %s" % p)
    r = recs[-1]
    pf = r.get("params_final") or {}
    it = r.get("iterations")
    if not isinstance(it, int) or isinstance(it, bool):
        fail("iteration count of %s is not an integer" % run)
    cl, om = pf.get("c_l"), pf.get("omega")
    if not (isinstance(cl, float) and isinstance(om, float) and finite(cl, om) and 0.4 < cl < 0.5 and om > 0):
        fail("params_final of %s not finite and in range" % run)
    return r, cl, om, it


def main():
    if len(sys.argv) < 5:
        fail("usage: branch_param.py SENS_JSON EVAL_NPZ RUN_A RUN_B [LABEL]")
    sens, npz, run_a, run_b = sys.argv[1:5]
    label = sys.argv[5] if len(sys.argv) > 5 else ""
    try:
        S = json.load(open(sens))
        M = S["record_meta"]
        red = S["reduced"]["1e-12"]
        lam = np.array(red["S_eigvals_scaled"], float)
        W = np.array(red["S_eigvecs_scaled_columns"], float)
        Ss = np.array(red["S_scaled"], float)
        O1 = float(S["O1"])
        d = np.load(npz, allow_pickle=False)
        npz_it, npz_cost = int(d["it"]), float(d["cost"])
        npz_cl, npz_om = float(d["c_l"]), float(d["omega"])
        kind, coords = str(d["jacobian_kind"]), str(d["coordinates"])
        pos = np.array(d["param_positions"], int)
        n = int(d["D"].shape[0])
        Dfull = np.array(d["D"], float)
        E = json.load(open(os.path.join(os.path.dirname(npz), "jc_eval.json")))
        meta_cost = float(M["cost"])
        meta_it = M["it"]
        pr = M["params_record"]
        if isinstance(pr, str):
            pr = ast.literal_eval(pr)
        meta_cl, meta_om = float(pr["c_l"]), float(pr["omega"])
    except (KeyError, ValueError, TypeError, OSError, SyntaxError) as e:
        fail("missing or unreadable field: %r" % (e,))
    if S.get("version") != 6:
        fail("width record version %r, not 6" % S.get("version"))
    if os.path.realpath(str(M.get("record", ""))) != os.path.realpath(npz):
        fail("width record was made from %r, not from this EVAL record" % M.get("record"))
    if kind != "J_c" or M.get("jacobian_kind") != "J_c":
        fail("not a J_c record")
    if M.get("param_coords_in_record") != "optimizer" or coords.split()[0] != "optimizer":
        fail("not in optimizer coordinates")
    if not np.array_equal(pos, [n - 2, n - 1]) or Ss.shape != (2, 2) or W.shape != (2, 2) or lam.shape != (2,):
        fail("parameter columns are not last, or the reduced system is not 2 x 2")
    Dp = Dfull[n - 2:]
    if not finite(O1, meta_cost, npz_cost, npz_cl, npz_om, meta_cl, meta_om, lam, W, Ss, Dp):
        fail("a required number is not finite")
    try:
        meta_it = int(str(meta_it)) if str(meta_it).lstrip("-").isdigit() else None
    except ValueError:
        meta_it = None
    if meta_it is None:
        fail("width record iteration is not an integer")
    ra, cla, oma, ita = end_record(run_a)
    rb, clb, omb, itb = end_record(run_b)
    if E.get("kind") != "EVAL" or E.get("status") != "ACCEPTED":
        fail("EVAL json kind or status not EVAL / ACCEPTED")
    if os.path.realpath(str(E.get("run", ""))) != os.path.realpath(run_a):
        fail("EVAL json names run %r, not RUN_A" % E.get("run"))
    ep = E.get("params") or {}
    its = {meta_it, npz_it, E.get("it"), ita}
    if len(its) != 1 or not all(isinstance(i, int) for i in its):
        fail("iterations differ: width %r, npz %r, EVAL json %r, run %r" % (meta_it, npz_it, E.get("it"), ita))
    if len({meta_cl, npz_cl, ep.get("c_l"), cla}) != 1 or len({meta_om, npz_om, ep.get("omega"), oma}) != 1:
        fail("parameters differ between width record, npz, EVAL json and RUN_A")
    if len({meta_cost, npz_cost, E.get("cost"), ra.get("cost_final")}) != 1:
        fail("costs differ between width record, npz, EVAL json and RUN_A")
    if abs(O1 - npz_cost) > 1e-12 * O1:
        fail("width record O1 differs from the npz cost")
    ck = E.get("checkpoint") or {}
    if ck.get("path") and os.path.isfile(ck["path"]) and sha(ck["path"]) != ck.get("sha256"):
        fail("the EVAL checkpoint file no longer has the recorded sha256")
    if not (np.all(lam > 0) and np.all(Dp > 0)):
        fail("eigenvalues or D_p not positive")
    orth = float(np.max(np.abs(W.T @ W - np.eye(2))))
    eig_resid = float(np.max(np.abs(Ss @ W - W * lam)) / np.max(np.abs(lam)))
    if not (orth <= 1e-12 and eig_resid <= 1e-10):
        fail("eigensystem not orthonormal or not matching the reduced matrix")
    t = np.sqrt(2 * 0.01 * O1 / lam)
    ds = Dp * (z(clb, omb) - z(cla, oma))
    c = W.T @ ds
    if not finite(t, ds, c):
        fail("result not finite")
    out = {"label": label, "tool_version": 3,
           "state_a": {"run": os.path.realpath(run_a), "iterations": ita, "c_l": cla, "omega": oma, "O1": O1,
                       "D_p": Dp.tolist()},
           "state_b": {"run": os.path.realpath(run_b), "iterations": itb, "c_l": clb, "omega": omb},
           "lambda": lam.tolist(), "t": t.tolist(), "eigvec_check_rel": eig_resid, "orthonormality_defect": orth,
           "delta_s": ds.tolist(), "c": c.tolist(), "c_over_t": (c / t).tolist(),
           "agree_at_a": bool(np.all(np.abs(c) <= t))}
    print(json.dumps(out, indent=1))


main()

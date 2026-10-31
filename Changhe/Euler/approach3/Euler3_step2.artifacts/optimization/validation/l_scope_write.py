#!/usr/bin/env python
"""Write validation/l_scope.json, the double-double set of the (l) copy, from the screen records (lead 10:15:00Z item 1; rule 09:44:46Z; fail closed
09:43:52Z). A class is float64 only if EVERY screen record present decides 'float64' for it (status 'float64', not OPEN) and the class appears in every
record; any class absent from a record, OPEN, or double-double in any record is double-double. Classes never screened and always double-double by
construction are listed as such. The file names the screen records (sha256) and this script; it is accepted by the lead by a dated note naming its
sha256, and does not change after any (l) outcome. Usage: python validation/l_scope_write.py [--force-dd] validation/l_screen_*.json"""
import sys, os, json, hashlib, time, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ALWAYS_DD = ["coefficient contraction B[l] @ a with (hi, lo) tables", "scalar sets, angular contraction, U and DU", "pressure source tr(DU DU)", "pressure chain (production _solve_dd_core) with (hi, lo) outputs",
             "convection (U . grad) U and the row sum", "row weighting: sqrt(w_node w_ang) exact inputs times scale_mom in double-double", "differences D_h, D4_h formed and divided in double-double, rounded once"]
SCREENED = ["B[l] radial tables", "twist tables", "row scales", "nonlinear row weights", "pressure kernel tables", "stable-linear envelopes", "tail amplitudes", "tail energies",
            "enstrophy and stretching", "closure patterns", "closure target", "tail-reduction solutions"]
INACTIVE = {"far-row scaling (inline, far_model)": "Problem.far_model is None in the production configuration (asserted at run time by the screen)"}
CARRIED_DD_IN_COPY = {"row scales"}      # float64 by the screens but carried in double-double by the copy anyway (scale_mom by mpmath; lead 10:51:08Z item 2: extra double-double never relaxes the rule)


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]; force = "--force-dd" in sys.argv
    recs = []
    for a in args:
        for f in sorted(glob.glob(a)):
            recs.append((f, json.load(open(f))))
    classes = {}
    for name in SCREENED:
        per = []
        for f, r in recs:
            dcl = (r.get("decisions") or {}).get(name)
            per.append(dict(record=os.path.relpath(f, ROOT), sha256=sha(f), status=(dcl or {}).get("status", "absent"), open_reasons=(dcl or {}).get("open_reasons"), every_group_reading=(dcl or {}).get("every_group_reading")))
        inactive_everywhere = bool(per) and all(p["status"] == "inactive" for p in per)
        float64_everywhere = bool(per) and all(p["status"] == "float64" for p in per)
        if force or not recs:
            dec = "double-double"; why = "no accepted screen record (lead 10:15:00Z item 1: unaccepted classes go to double-double)" if not recs else "forced double-double"
        elif inactive_everywhere:
            dec = "inactive"; why = "recorded inactive in every screen record"
        elif float64_everywhere:
            dec = "float64"; why = "every screen record decides float64 under the 09:44:46Z rule"
        else:
            dec = "double-double"; why = "fail closed: at least one record is OPEN, double-double or absent for this class"
        arith = "double-double" if (name in CARRIED_DD_IN_COPY or dec == "double-double") else ("inactive" if dec == "inactive" else "float64 (production quantity)")
        classes[name] = dict(decision=dec, reason=why, arithmetic_in_copy=arith, screen_records=per)
    out = dict(ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), rule="lead 09:44:46Z (failing groups decide), 09:43:52Z (fail closed), 10:15:00Z (scope file; accepted by the lead by sha256; unchanged after any (l) outcome)",
               always_double_double=ALWAYS_DD, screened_classes=classes, inactive=INACTIVE,
               nonlinear_weights_Jf="inactive by construction in J_f (weights frozen); decided on J_cw and J_c (lead 10:10:03Z)",
               notes=["arithmetic_in_copy states the arithmetic l_eval uses for each class: every double-double decision is double-double; row scales are double-double in the copy although float64 by the screens (lead 10:51:08Z item 2); the other float64 classes are the production float64 quantities",
                      "the double-double tables are componentwise about 1e-24 relative for the smallest entries (V234), not uniformly double-double",
                      "the tail-reduction class measures the sensitivity to the rounded solved coefficients, not to rounding inside the constraint solve (V236)"],
               writer=dict(script="validation/l_scope_write.py", sha256=sha(__file__)))
    path = os.path.join(ROOT, "validation", "l_scope.json")
    if os.path.exists(path):
        raise FileExistsError(path + " exists: the scope does not change after it is written; move it aside only before any (l) outcome and with the lead's note")
    json.dump(out, open(path, "x"), indent=1)
    print(json.dumps({k: v["decision"] for k, v in classes.items()}, indent=1)); print("written", path, "sha256", sha(path))


if __name__ == "__main__":
    main()

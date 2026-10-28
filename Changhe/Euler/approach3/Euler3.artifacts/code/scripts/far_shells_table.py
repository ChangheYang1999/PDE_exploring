#!/usr/bin/env python
"""Per-shell holdout residual ratios of several saved states on the outer (far checkpoint) shells, side by side, plus the far remainder
kappa(R) at the finite radii 2^12, 2^14, 2^16 R0 and the all-shell rho_nl^max with the shell where it is attained (lead d128 FN item 2:
'add rho_nl and the far remainder at each far checkpoint shell; say whether the balance reduction is bought with far-field residual').
Reads the states' own holdout diagnostics (spec_diag_holdout: shells.edges, rho_u, rho_nl) and the saved ray/G-closure outputs; no recomputation.
Usage: .venv/bin/python scripts/far_shells_table.py <job_id or start.pt> [...] [--shells 6] (the last --shells dyadic shells of the first state)"""
import sys, os, json, math, argparse
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
import torch
sys.path.insert(0, ROOT)
ap = argparse.ArgumentParser(); ap.add_argument("states", nargs="+"); ap.add_argument("--shells", type=int, default=6); ap.add_argument("--json", default=None)
a = ap.parse_args()


def sha256(p):
    import hashlib
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


FILES = {}


def load(x):
    p = x if x.endswith(".pt") else os.path.join(ROOT, "runs", x, "starts", "start_000.pt")
    S = torch.load(p, map_location="cpu", weights_only=False)
    name = os.path.basename(os.path.dirname(os.path.dirname(p))) if not x.endswith(".pt") else x
    FILES[name] = dict(path=os.path.relpath(p, ROOT), sha256=sha256(p))
    return name, S


states = [load(x) for x in a.states]
ref = states[0][1]["spec_diag_holdout"]
edges = [tuple(e) for e in ref["shells"]["edges"]]
sel = edges[-a.shells:]
# pressure-source provenance (SPEC 7.11 X4; lead d128 FX item 4): the holdout pressure is the Green solution with the source interpolated from the Nr_src
# Chebyshev-Gauss source nodes of the training grid; beyond the last source node r_last the source is the envelope-times-Chebyshev continuation in x
# (an analytic tail model of the source representation), so shells at or beyond r_last are labelled 'model'
c0 = states[0][1]["config"]
from src.equations.fields import Model as _M
_m = _M(L=c0["L"], Nk=c0["Nk"], m_parity=c0.get("m_parity", "even"), R0=c0.get("R0", 1.0), Nr=c0.get("Nr"), c_l=c0["c_l"], omega=c0["omega"], channels=c0.get("channels"),
        device="cpu", extra_r=(c0.get("far_radii") if c0.get("far_merged", True) else None))
r_last = float(_m.r[_m.Nr_src - 1]); n_src = int(_m.Nr_src)
def prov(lo, hi):
    if hi <= r_last:
        return "source table (exterior integral beyond r_last from the source continuation)"
    if lo < r_last < hi:
        return "straddles r_last: model beyond it"
    return "model (source from the envelope-times-Chebyshev continuation beyond the last source node)"
provenance = [dict(shell=[lo, hi], pressure=prov(lo, hi)) for lo, hi in sel]
out = dict(shells=[list(e) for e in sel], states={}, pressure_source=dict(n_source_nodes=n_src, last_source_node_r=r_last, last_source_node_r_over_R0=r_last / float(c0.get("R0", 1.0)),
           far_anchor_eval_radii=[float(v) for v in _m.r[_m.Nr_src:]], note="holdout pressure = Green solution with the source interpolated from the training source nodes (PressureSolver(eval_model=holdout)); beyond r_last the source is the (s/R0)^-p0 envelope times the Chebyshev polynomial continued in x towards 1 (SPEC 4.4 tail model of the source); shells labelled 'model' are evaluated with that continuation",
           per_shell=provenance))
print(f"pressure source: {n_src} source nodes, last source node r_last = {r_last:.4f} ({r_last / float(c0.get('R0', 1.0)):.1f} R0); far anchor evaluation radii {[round(float(v), 1) for v in _m.r[_m.Nr_src:]]}")
for d in provenance:
    print(f"  shell [{d['shell'][0]:.3g}, {d['shell'][1]:.3g}): {d['pressure']}")
print("| state | " + " | ".join(f"rho_u [{lo:.3g},{hi:.3g}){' MODEL' if lo >= r_last else (' straddles r_last' if hi > r_last else '')}" for lo, hi in sel) + " | rho_nl^max (shell) | kappa 2^12 / 2^14 / 2^16 R0 | E_ren | H_tot/int|h| |")
print("|---|" + "---|" * (len(sel) + 4))
for name, S in states:
    h = S["spec_diag_holdout"]; e2 = [tuple(e) for e in h["shells"]["edges"]]
    ru, rn = [], []
    for e in sel:
        if e in e2:
            k = e2.index(e); ru.append(h["rho_u"][k]); rn.append(h["rho_nl"][k])
        else:
            ru.append(None); rn.append(None)
    imax = max(range(len(h["rho_nl"])), key=lambda i: h["rho_nl"][i]); nl_max = h["rho_nl"][imax]; nl_shell = e2[imax]
    kap = None
    fn = os.path.join(ROOT, "reports", f"arm_reading_{name}.json")          # the finite-radius far remainder lives in the ledger row (arm_reading JSON)
    if os.path.exists(fn):
        try:
            kap = json.load(open(fn))["row"].get("kappa_far_finite_radius")
        except Exception:
            kap = None
    gb = S.get("global_balances") or {}
    def f(v):
        return "n/a" if v is None else f"{v:.3e}"
    ks = kap if isinstance(kap, dict) else {}
    kstr = " / ".join(f"{ks[k]:+.3f}" for k in ks) if ks else "n/a"
    print(f"| {name[:48]} | " + " | ".join(f"{f(u)} (nl {f(n)})" for u, n in zip(ru, rn)) + f" | {nl_max:.3e} ({nl_shell[0]:.3g},{nl_shell[1]:.3g}) | {kstr} | {gb.get('E_ren', float('nan')):.4f} | {gb.get('H_tot_over_abs', float('nan')):.4f} |")
    out["states"][name] = dict(rho_u=ru, rho_nl=rn, rho_nl_max=nl_max, rho_nl_max_shell=list(nl_shell), kappa=ks, E_ren=gb.get("E_ren"), H_tot_over_abs=gb.get("H_tot_over_abs"),
                               state_file=FILES[name]["path"], state_sha256=FILES[name]["sha256"])
print("state files: " + "; ".join(f"{n}: {v['path']} sha256 {v['sha256'][:16]}..." for n, v in FILES.items()))
out["script_sha256"] = sha256(os.path.abspath(__file__)); out["note"] = "values read from the states' own holdout batteries (spec_diag_holdout) and ledger rows; no recomputation"
if a.json:
    json.dump(out, open(a.json, "w"), indent=1, default=str); print("wrote", a.json)

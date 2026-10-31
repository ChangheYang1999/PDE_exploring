#!/usr/bin/env python
"""Resolution ladder table requested by the lead (21:09Z): best fresh holdout rho_u^max per L for the c2x2 continuation arms,
fixed vs free parameters, solver versions separate; plus rho_nl^max, Sigma_Z (fine grid), e_F, strain ratio at the located
maximum, W-zero defect, parameter drift for free arms. Writes reports/RESOLUTION_LADDER.md."""
import sys, os, json, time, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
from src.campaign import ledger
recs = [r for r in ledger.merge_reevaluations(ledger.read(os.path.join(ROOT, "status", "ledger.jsonl"))) if r.get("job_id", "").startswith(("c2x2", "d6"))]
groups = collections.defaultdict(list)
for r in recs:
    arm = "free" if r["job_id"].endswith("_free") else "fixed"
    src = r["job_id"].split("_cl")[1].split("_")[0]
    fam = r["job_id"].split("_L")[0]            # c2x2, c2x2b, c2x2c (s1k Sigma_Z states) or d6t, d6tZ, d6u, d6v (fitted D6 state)
    ch = r.get("channels") or ((r.get("config") or {}).get("channels") if isinstance(r.get("config"), dict) else None)
    groups[(fam, r.get("solver_version", "?"), r.get("nl_denominator", "nl"), src, arm, r["L"])].append(r)
import glob
def channels_of(r):
    for d in ("done", "running", "pending", "failed"):
        fjob = os.path.join(ROOT, "queue", d, r["job_id"] + ".json")
        if os.path.exists(fjob):
            try:
                c = json.load(open(fjob))["config"]; ch = c.get("channels") or {}
                return f"B{ch.get('NkB', 0)}/D{ch.get('NkD', 0)}/E{ch.get('NkE', 0)}" + (f" lB{ch['LB']}/lD{ch['LD']}" if ch.get("LB") or ch.get("LD") else "")
            except Exception:
                return "?"
    return "?"
for r in recs:
    r["channels_str"] = channels_of(r)
lines = [f"# Resolution ladder of the continuation experiment (generated {time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime())})", "",
         "Warm starts: the two best Sigma_Z states of s1k (c_l 0.47 omega 1, holdout rho_u 0.359; c_l 0.45 omega 1, 0.405), embedded exactly into the",
         "larger bases; Sigma_Z = 1 (ramped), far anchoring, exact tail-moment constraints (v5), Nr = 3 Nk, channels at L >= 8.",
         "v5 arms started from v4 states are PROJECTED warm starts (reduce/expand changes the parent; see relU_change_holdout in the ledger).",
         "Rows marked 'no movement' ended at their start value (stalled at the first iteration) and carry no L dependence.",
         "Weighting 'nl' = 1/(RMS T4 + RMS T5)^2 per shell (gamed by core inflation, FAILURE_ANALYSIS item 12: the training cost of these",
         "arms is not evidence); 'all5' = five scaled terms (rho_u-like). 'WORSE than start' marks arms whose holdout rho_u rose.",
         "Families: c2x2/c2x2b/c2x2c continue the two best s1k Sigma_Z states (c_l 0.47 and 0.45, omega 1); d6t/d6tZ/d6u/d6v continue the primary-basis fit",
         "of the verifier's released degree-6 state (c_l 0.45, omega 0.3, omega/c_l 2/3; fitted holdout rho_u 0.0740, source 0.0729). d6tZ carries the Sigma_Z = 1 ramp;",
         "d6t/d6u/d6v carry none. 'all5far' = all5 plus the far-imbalance term lambda/den_nl on shells r >= 1 (lead 22:40Z (b)).",
         "SPEC 7.3a: 'half' is the half-offset shell family, 'sphere' the largest single-sphere rho_u on the exchange radii; rho_nl^max is over ALL shells of the standard family.",
         "An ordering claim between two states needs the same order on both families. max|U| start -> end is the core-inflation flag (FAILURE_ANALYSIS item 12).",
         "One row per (family, solver, weighting, source state, arm, L): the best start of that group.", "",
         "| family | solver | weighting | source c_l | arm | L | Nk | channels | start holdout rho_u | best holdout rho_u^max (std) | half | sphere | rho_nl^max (all shells) | max U start -> end | Sigma_Z (fine) | e_F | strain ratio (located max) | min W-zero eigvec defect | c_l, omega at end | status | job/start |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
def f(v, fmt="%.3e"):
    return (fmt % v) if isinstance(v, (int, float)) and v is not None else "n/a"
for key in sorted(groups):
    rows = sorted(groups[key], key=lambda r: (r.get("rho_u_max_holdout") if r.get("rho_u_max_holdout") is not None else 1e9))
    r = rows[0]
    moved = (r.get("iterations") or 0) > 1 and not (r.get("source_rho_u") is not None and r.get("rho_u_max_holdout") is not None and abs(r["rho_u_max_holdout"] - r["source_rho_u"]) < 1e-3 * max(abs(r["source_rho_u"]), 1e-12))
    tag = "" if moved else " (no movement: not a ladder point)"
    if key[3] == "free":
        tag += " (ranks only after a fresh fixed-parameter evaluation at its final c_l, omega)"
    if moved and r.get("source_rho_u") is not None and r.get("rho_u_max_holdout") is not None and r["rho_u_max_holdout"] > r["source_rho_u"] * 1.001:
        tag += " (WORSE than start)"
    ch = r.get("channels_str") or "n/a"
    lines.append(f"| {key[0]} | {key[1]} | {key[2]} | {key[3]} | {key[4]}{tag} | {key[5]} | {r['Nk']} | {ch} | {f(r.get('source_rho_u'))} | {f(r.get('rho_u_max_holdout'))} | {f(r.get('rho_u_max_holdout_half'))} | {f(r.get('sphere_rho_u_max'))} | {f(r.get('rho_nl_max_holdout'))} | {f(r.get('max_U_start'))} -> {f(r.get('max_U'))} | {f(r.get('Sigma_Z'), '%.3f')} | {f(r.get('e_F'), '%.2f')} | {f(r.get('located_strain_ratio'), '%.3f')} | {f(r.get('min_W_eigvec_defect'), '%.3f')} | {r['c_l']:.4f}, {r['omega']:.4f} | {r.get('status')} | {r['job_id']}/{r['start']} |")
if not groups:
    lines.append("| (no continuation results yet) | | | | | | | | | | | | | | | | | | | | |")
lines += ["", "Interpretation rule (lead 19:27Z): a floor that does not move with L means the representation is not the limit; one that falls means refinement."]
os.makedirs(os.path.join(ROOT, "reports"), exist_ok=True)
open(os.path.join(ROOT, "reports", "RESOLUTION_LADDER.md"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))

# ---- nest ladder (the route's own random-start ladder L2 -> L4 -> L6 -> L8; added 2026-10-25T13:00Z for the gate's resolution record) ----
nrecs = [r for r in ledger.merge_reevaluations(ledger.read(os.path.join(ROOT, "status", "ledger.jsonl"))) if str(r.get("job_id", "")).startswith("nest") and r.get("rho_u_max_holdout") is not None and not r.get("failure")]
pts = collections.defaultdict(lambda: collections.defaultdict(list))
for r in nrecs:
    pts[(round(r["c_l"], 3), r["omega"])][int(r.get("L") or 0)].append(r)
nl = ["", "## Nest ladder (route's own random starts promoted L2 -> L4 -> L6 -> L8; best holdout rho_u^max per level, standard / half-offset family; q = ratio of the standard values of successive levels; SPEC-degree channels and closure rows from L6 on)", "",
      "| c_l | omega | omega/c_l | L | Nk | channels | best holdout rho_u^max std / half | q vs previous level (std) | sigma_u^max | sigma_Om | a_max | rho_nl^max | sampled Q_sw | E_ren | H_tot/int abs(h) | K_E ratio | carried mismatch | V10 | iterations | seconds | job/start |",
      "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
def f(v, fmt="%.3g"):
    return (fmt % v) if isinstance(v, (int, float)) and v is not None else "n/a"
for (cl, om), byL in sorted(pts.items()):
    prev = None
    for L in sorted(byL):
        rows = sorted(byL[L], key=lambda r: r["rho_u_max_holdout"])
        b = rows[0]
        q = (b["rho_u_max_holdout"] / prev) if prev else None
        ch = b.get("channels") or {}
        chs = f"B{ch.get('LB') or b.get('L')}/D{ch.get('LD') or b.get('L')}/E{ch.get('LE') or b.get('L')} x Nk{ch.get('NkB')}" if ch.get("NkB") else "none"
        nl.append(f"| {cl} | {om} | {om / cl:.4f} | {L} | {b.get('Nk')} | {chs} | {f(b['rho_u_max_holdout'], '%.4f')} / {f(b.get('rho_u_max_holdout_half'), '%.4f')} | {f(q, '%.3f')} | {f(b.get('sigma_u_max_core') or b.get('sigma_u_max'), '%.3f')} | {f(b.get('sigma_Om'), '%.3f')} | {f(b.get('a_max_core') or b.get('a_max'), '%.3f')} | {f(b.get('rho_nl_max_holdout_both') or b.get('rho_nl_max_holdout'), '%.2f')} | {f(b.get('Q_sw'), '%.3f')} | {f(b.get('E_ren'), '%.3f')} | {f(b.get('H_tot_over_abs'), '%.3f')} | {f(b.get('K_ratio_direct'), '%.2f')} | {f(b.get('G_carried_mismatch_rel'), '%.3f')} | {f(b.get('v10_last_tenth_rel_decrease'), '%.1e')} | {b.get('iterations')} | {f(b.get('seconds'), '%.0f')} | {b.get('job_id')}/{b.get('start')} |")
        prev = b["rho_u_max_holdout"]
nl += ["", "R1 (lead): a branch goes to the next level only if core-resolved and holdout rho_u^max <= 0.1; R2: two successive steps with q > 0.85 floor the branch; a q at the iteration limit (V10 > 1e-3) mixes truncation and budget and is read with its V10 (lead 12:32Z).",
       "", "## R2 status by branch (lead readings of record; dated)",
       "- nest (0.42, 0.3), omega/c_l 5/7: FLOORED at L8 under R2 (lead d128 AW 2026-10-26T00:23:50Z): L4 -> L6 q about 0.87 / 0.96, L6 -> L8 q 0.970 / 0.942 (std / half), two successive steps above 0.85; the 150-iteration continuation changed the L8 holdout by 1.0 / 0.4 per cent (0.06154 / 0.06718, independently read). Resources unchanged; the queued s12 (0.42, 0.3) arm is read against its own start.",
       "- nest (0.45, 1), omega/c_l 20/9: one weak step (L6 -> L8 q 0.955 / 0.940 as recorded; recomputed 0.887 on the standard family after the channel-Nk 8 test, which is NOT ordered ahead of cont150; lead 23:09:17Z); the L10 rung decides (q_10 against cont150 0.04367 / 0.04331; a floor reads 'floored at correction-channel Nk 4').",
       "- nest (0.45, 0.3), omega/c_l 2/3: one weak step (L6 -> L8 q 0.916, cont150 -2.6 per cent); the L10 rung decides (q_10 against cont150 0.0597 / 0.0594).",
       "- D6 lineage (0.45, 0.3): floored at L8 (d6w3_L8 worse than d6w_L8; FAILURE_ANALYSIS 25) and within 4 per cent under Nk 16 -> 32 at L6 (FAILURE_ANALYSIS 33)."]
with open(os.path.join(ROOT, "reports", "RESOLUTION_LADDER.md"), "a") as fh:
    fh.write("\n".join(nl) + "\n")
print("\n".join(nl[:6]))

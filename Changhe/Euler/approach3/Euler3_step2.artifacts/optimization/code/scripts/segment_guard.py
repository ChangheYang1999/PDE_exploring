#!/usr/bin/env python
"""5.3 / 6.3 (a) evidence of a run record for the segment-end and promotion decisions (SPEC v1.25 sections 5.3, 5.4, 6.3 (a), 6.3 (b); lead 17:18:08Z item 3 (b); V391).
v3 (17:5xZ): the REGISTERED fields and thresholds from results.jsonl (first line = the end state): 5.3 saturation (min(c_l - 0.4, 0.5 - c_l) < 0.002, omega < 1e-3 or
> 1e3, or the worker's saturation_stop); 6.3 (a) exclusions: Tier S nontriviality warnings (N_core < 1e-2, N_F < 1e-2, e_core < 1e-4, e_F < 1e-4), core collapse
(max|U| below 0.1 x its start value; the L2 core norm is not in the record: OPEN), the saturation flag, the near-edge label (5.4: min(c_l - 0.4, 0.5 - c_l) < 0.02; the
v1.21 (d) evidence is OPEN in this campaign, so a near-edge state is excluded), core_resolved false (v1.21 (c)), rho_P^max > 1e-3 (if the record has it), G5 at the state
(not in the record: OPEN), and the a_max increase by more than a factor 2 relative to the lineage start together with a rho_u^max decrease (needs the start record:
OPEN unless a start a_max is supplied with --start-record). 6.3 (b) flags from the record: omega < 1e-2; a_eff below half of the start a_eff (needs the start record);
vorticity maximum at radius above 2^8 R0 or inside the innermost shell (r_peak_Omega); r_tail above 4 x the start r_tail (needs the start record); N6/top radial
coefficients (not in the record: OPEN). Fields the record lacks are listed under 'open' and are NOT counted as clean. Reading only.
Usage: python scripts/segment_guard.py <run dir> [--start-record <results.jsonl of the lineage start>]"""
import json, sys, os
run = sys.argv[1].rstrip("/"); start_rec = None
if "--start-record" in sys.argv:
    start_rec = json.loads(open(sys.argv[sys.argv.index("--start-record") + 1]).readline())
rec = json.loads(open(run + "/results.jsonl").readline())
cl, om = float(rec.get("c_l", 0.45)), float(rec.get("omega", 1.0)); edge = min(cl - 0.4, 0.5 - cl)
R0 = 0.3
excl = dict(saturation_5_3=bool(rec.get("saturation_stop")) or edge < 0.002 or om < 1e-3 or om > 1e3,
            tier_S_nontriviality=(rec.get("N_core") is not None and (float(rec["N_core"]) < 1e-2 or float(rec.get("N_F", 1)) < 1e-2 or float(rec.get("e_core", 1)) < 1e-4 or float(rec.get("e_F", 1)) < 1e-4)),
            core_velocity_collapse_maxU=(rec.get("max_U_start") is not None and float(rec["max_U"]) < 0.1 * float(rec["max_U_start"])),
            near_edge_5_4_without_v121d=bool(rec.get("near_edge")) or edge < 0.02,
            core_unresolved_v121c=(rec.get("core_resolved") is False),
            rho_P_max_above_1e_3=(rec.get("rho_P_max") is not None and float(rec["rho_P_max"]) > 1e-3))
open_items = ["||U||_L2(|y|<1) relative to the start (not in the record)", "G5 at the state (not in the record)"]
if rec.get("rho_P_max") is None: open_items.append("rho_P^max (not in the record)")
if start_rec is not None and start_rec.get("a_max") and rec.get("a_max"):
    excl["a_max_increase_x2_with_rho_decrease"] = (float(rec["a_max"]) > 2 * float(start_rec["a_max"])) and (float(rec.get("rho_u_max", 1)) < float(start_rec.get("rho_u_max", 0)))
else:
    open_items.append("a_max relative to the lineage start (start record not supplied)")
flags_b = dict(omega_below_1e_2=(om < 1e-2), vorticity_max_outside_sampled=(float(rec.get("r_peak_Omega") or 0) > 2 ** 8 * R0))
if start_rec is not None:
    if start_rec.get("a_eff") and rec.get("a_eff"): flags_b["a_eff_halved"] = float(rec["a_eff"]) < 0.5 * float(start_rec["a_eff"])
    if start_rec.get("r_tail") and rec.get("r_tail"): flags_b["r_tail_x4"] = float(rec["r_tail"]) > 4 * float(start_rec["r_tail"])
    if start_rec.get("omega"): flags_b["omega_monotone_factor_10"] = (float(start_rec["omega"]) / max(om, 1e-300) > 10)
else:
    open_items += ["a_eff relative to the start", "r_tail relative to the start", "omega monotone decrease by a factor 10 (needs the trajectory)"]
open_items.append("6.3 (b) high-frequency growth (N6 and top radial coefficients: not in the record)")
raised_a = {k: v for k, v in excl.items() if v}; raised_b = {k: v for k, v in flags_b.items() if v}
out = dict(run=os.path.basename(run), status=rec.get("status"), iterations=rec.get("iterations"), cost_final=rec.get("cost_final"), c_l=cl, omega=om, edge_distance=edge,
           fields=dict(N_core=rec.get("N_core"), N_F=rec.get("N_F"), e_core=rec.get("e_core"), e_F=rec.get("e_F"), max_U=rec.get("max_U"), max_U_start=rec.get("max_U_start"), core_resolved=rec.get("core_resolved"), near_edge=rec.get("near_edge"), saturation_stop=rec.get("saturation_stop"),
                       r_peak_Omega=rec.get("r_peak_Omega"), a_eff=rec.get("a_eff"), r_tail=rec.get("r_tail"), a_max=rec.get("a_max"), rho_u_max=rec.get("rho_u_max"), rho_P_max=rec.get("rho_P_max"), monopole_flag_informational=rec.get("monopole_flag"), tier_S=rec.get("tier_S")),
           exclusions_6_3a=excl, raised_exclusions=raised_a, flags_6_3b=flags_b, raised_flags=raised_b, open=open_items,
           clean_on_available_fields=(len(raised_a) == 0 and len(raised_b) == 0), registered_clearance="NOT established while 'open' is non-empty (V391); the available fields raise nothing" if (len(raised_a) == 0 and len(raised_b) == 0) else "a registered exclusion or flag is raised")
print(json.dumps(out))

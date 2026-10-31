#!/usr/bin/env python
"""Summary lines for the NUM_REPORT (l) table from l_eval, l_trig_qual and l_power records (reading only). Usage: python validation/l_row.py <record.json> [...]"""
import sys, json, os, hashlib


def fails(gp, key):
    return sorted(g for g, v in gp.items() if v.get(key) is False)


def l_eval_row(d):
    lo = d["l_outcome"]; rr = d["registered_recomputed"]; gp = lo.get("group_pass", {}); rgp = rr.get("group_pass", {})
    far = gp.get("far_anchor_block", {}); hs = sorted(lo["per_group"].keys(), key=float, reverse=True)
    far_err = [lo["per_group"][h]["second_order"].get("far_anchor_block") for h in hs]
    reg_fail = sorted(set(fails(rgp, "pass_second_order") + fails(rgp, "pass_five_point")))
    l_fail = sorted(set(fails(gp, "pass_second_order") + fails(gp, "pass_five_point"))); l_fail_F0 = sorted(set(fails(gp, "pass_second_order_F0") + fails(gp, "pass_five_point_F0")))
    print(f"{d['case']}, {d['reference']}, {d['column']} | registered: PASS={rr.get('PASS')} PASS_rel={rr.get('PASS_rel')} failing groups {reg_fail} | (l): PASS={lo.get('PASS')} PASS_rel={lo.get('PASS_rel')} failing groups (original floors) {l_fail}, with F=0 {l_fail_F0}")
    print(f"  far-anchor second-order errors (l) h={hs}: {['%.3e' % e if e is not None else None for e in far_err]} | far-anchor Richardson {far.get('richardson_error')} pair {far.get('richardson_pair')} | whole column Richardson {lo.get('richardson_error')} pair {lo.get('richardson_pair')}")
    print(f"  active sets identical: {lo.get('active_sets_identical')} | term split valid: {d.get('far_anchor_term_split', {}).get('term_split_valid')} | same-function check: {os.path.basename(d['same_function_check']['path'])} sha {d['same_function_check']['sha256'][:16]} | scope sha {d.get('scope_sha256', '')[:16]} | l_eval sha {d.get('l_eval_sha256', '')[:16]} | {d.get('seconds', 0):.0f} s | {d.get('ts')}")
    pr = far.get("richardson_all_pairs", {})
    print("  far-anchor pairs: " + "; ".join(f"{k}: err {v['richardson_error']:.3e} passes2nd={v.get('pair_passes_second_order')}" for k, v in pr.items()))


def trig_row(d):
    adm = d.get("admission", {}); tie = d.get("earlier_copy_table_tie") or {}; lt = tie.get("ladder_tie", {})
    pts = d.get("pressure_arg_ranges_per_point", {})
    tot = {}
    for k, v in pts.items():
        ec = v.get("exp_cutoff") or {}
        for f in ("count_k1", "count_k2", "count_wr", "count_mom1", "count_sfac", "count_other", "boundary_ambiguous_total", "boundary_within_1e_12_total"):
            if f in ec:
                tot[f] = tot.get(f, 0) + ec[f]
    worst = max((max(r["change_D"] / r["limit_on_D"] if r["limit_on_D"] else float("inf"), r["change_D4"] / r["limit_on_D"] if r["limit_on_D"] else float("inf")) for row in d["per_step"].values() for r in row.values()), default=None)
    worst_cz = max((max(r["change_D"] / r["limit_on_D"] if r["limit_on_D"] else float("inf"), r["change_D4"] / r["limit_on_D"] if r["limit_on_D"] else float("inf")) for row in d["exp_cutoff_replacement"]["per_step"].values() for r in row.values()), default=None)
    print(f"{d['case']}, {d['column']} qualification | trig within: {d.get('all_within')} (worst change/limit {worst}) | exp replacement within: {d['exp_cutoff_replacement'].get('all_within')} bitwise {d['exp_cutoff_replacement'].get('bitwise_identical_to_dd')} (worst {worst_cz}) | source tie: {adm.get('source_tie')} (ladder tie all bitwise {lt.get('all_bitwise')}) | ADMISSION all three: {adm.get('all_three')}")
    print(f"  mpmath digits global {d.get('mpmath_digits_global')} trig {d.get('mpmath_digits_trig_local')} | differing trig pairs {d.get('differing_pairs')} of {d.get('trig_arguments')} | points {len(pts)} | cutoff counts summed over points {tot} | record sha {d.get('record_sha256', '')[:16]} | {d.get('seconds', 0):.0f} s | {d.get('ts')}")


def main():
    for p in sys.argv[1:]:
        d = json.load(open(p)); print(f"== {p} (sha256 {hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]})")
        if "l_outcome" in d:
            l_eval_row(d)
        elif "exp_cutoff_replacement" in d:
            trig_row(d)
        else:
            print(json.dumps({k: d[k] for k in d if not isinstance(d[k], (dict, list))}, default=str)[:800])


if __name__ == "__main__":
    main()

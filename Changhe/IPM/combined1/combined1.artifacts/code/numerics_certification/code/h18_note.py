"""Print the H18 falsification result of lane c1-n3 from the records (hardy_cover, legqs_hdual, legqs_secondpath) for 016 and 017."""
from pathlib import Path
import json, sys
from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING, getcontext
getcontext().prec = 80; R = Path('certification/results')
def bnd(s, up_, digits=16):
    s = str(s).strip().strip('[]'); mid, _, rad = s.partition(' +/- '); m = Decimal(mid.strip()); r = Decimal(rad.strip() or '0')
    v = m + r if up_ else m - r
    if v == 0: return '0'
    q = Decimal(1).scaleb(v.adjusted() - digits + 1)
    return f'{v.quantize(q, rounding=ROUND_CEILING if up_ else ROUND_FLOOR):.{digits-1}e}'
def lo(s, d=16): return bnd(s, False, d)
def up(s, d=16): return bnd(s, True, d)
def J(name):
    p = R / name
    return json.loads(p.read_text()) if p.exists() else None
for ID, tag in (('C1-N1-016-legqs25-quot013', '016'), ('C1-N1-017-legqs50-quot013', '017')):
    cv = J(f'{ID}_hardy_cover.json'); du = J(f'{ID}_legqs_hdual.json'); sp = J(f'{ID}_legqs_secondpath.json'); hd = J(f'{ID}_legqs_hardy.json')
    print(f'\n{tag} ({ID}):')
    if cv: print(f'  (a) mode cover: keys {cv["n_keys"]}, kinds {cv["kinds"]}, {cv["n_modes"]} modes (odd 1..{cv["modes_first_last"][1]}: {cv["modes_are_all_odd_from_1_to_max"]}); sum_n ||r F_n||^2 = {cv["sum_rFn_sq_ball"][:34]} vs production rF^2 = {cv["production_rF_sq_lo_ball"][:34]}; H recomputed {cv["H_recomputed_ball"][:30]}; checks {sum(cv["checks"].values())}/{len(cv["checks"])} pass; all_pass {cv["all_pass"]} ({cv["utc"]})')
    else: print('  (a) mode cover: pending')
    if du:
        print(f'  (b) duality LB ({du["utc"]}, modes {[m["n"] for m in du["modes"]]}, kmax {du["kmax"]}, up to {du["max_classes"]} classes; self-test overlap {du.get("selftest", {}).get("overlap")}):')
        print('  | mode n | LB of ||F_n||_H >= | Hardy UB <= | LB/UB >= | basis | pairing radius |'); print('  |---|---|---|---|---|---|')
        for m in du['modes']:
            print(f'  | {m["n"]} | {lo(m["LB_lower"], 12)} | {up(m["H_n_UB_hardy"], 12)} | {lo(m["ratio_LB_over_UB"], 5)} | {m["basis_size"]} ({m["chosen"]}) | {m.get("pairing_radius_max", "")[:9]} |')
        if du.get('H_lower'):
            print(f'  total: ||F||_H >= {lo(du["H_lower"], 12)} (sum of the mode squares) against the Hardy UB {up(hd["H_upper"], 15)}: LB <= UB {du["LB_le_UB_total"]}; E_2 >= {lo(du["E2_lower_with_H_lower"], 12)} (with this H; H-free LB {lo(hd["E2_lower_without_H"], 12)}), E_2 <= {up(hd["E2_upper_with_mode_hardy_H"], 12)}')
    else: print('  (b) duality LB: pending')
    for tagname in ('_hres_full', '_hres'):
        hr = J(f'{ID}_legqs_hdual{tagname}.json')
        if hr:
            print(f'  (d) two-sided mode enclosures through the Galerkin residual (legqs_hres.py{tagname}, {hr["utc"]}; k <= {hr["kmax"]}, up to {hr["max_classes"]} classes, no integer class):')
            print('  | mode n | ||grad psi||_2 | ||r g||_2 / n <= | ||F_n||_H >= | ||F_n||_H <= | Hardy UB <= | rF_n check |'); print('  |---|---|---|---|---|---|---|')
            for m in hr['modes']:
                print(f'  | {m["n"]} | {m["grad_psi"].split(" ")[0].strip("[")[:14]} | {up(m["residual_over_n"], 6)} | {lo(m["LB_certified"], 12)} | {up(m["UB_n"], 12)} | {up(m["hardy_UB_n"], 12)} | {m["rFn_check_overlaps_hardy_record"]} |')
            if hr.get('H_upper_new'):
                print(f'  total: H in [{lo(hr["H_lower_new"], 12)}, {up(hr["H_upper_new"], 12)}] (computed modes two-sided, modes outside {hr["modes_computed"][0]}..{hr["modes_computed"][-1]} by their Hardy bounds, sum of squares {up(hr["other_modes_hardy_sq"], 8)}); Hardy-only UB {up(hr["H_upper_hardy"], 12)}; E_2 in [{lo(hr["E2_lower_new"], 12)}, {up(hr["E2_upper_new"], 12)}]')
            break
    if sp: print('  (c) second path: ' + ', '.join(f'{k} overlap {v["intervals_overlap"]}' for k, v in sp['norms'].items()) + f' ({sp.get("elapsed_seconds", "running")} s)')

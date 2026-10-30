"""Print the publication table for a legqs candidate from its records (norms, probes, hardy). Usage: legqs_report.py <ID> [FLOAT G0 rF G1 P2]"""
from pathlib import Path
import json, sys
from flint import arb, ctx
sys.set_int_max_str_digits(0)
ctx.prec = 256
ID = sys.argv[1]; R = Path('certification/results'); fl = dict(zip(('G0', 'rF', 'G1', 'P2'), sys.argv[2:6])) if len(sys.argv) > 5 else {}
from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING
def bnd(s, up, digits=20):
    """Directional decimal rounding of a stored bound string (ball or plain): lower bounds down, upper bounds up."""
    s = str(s).strip('[]'); mid, _, rad = s.partition(' +/- '); m = Decimal(mid); r = Decimal(rad or '0')
    v = m + r if up else m - r; q = Decimal(1).scaleb(v.adjusted() - digits + 1)
    return f'{v.quantize(q, rounding=ROUND_CEILING if up else ROUND_FLOOR):.{digits-1}e}'
nr = json.loads((R / f'{ID}_legqs_norms.json').read_text()) if (R / f'{ID}_legqs_norms.json').exists() else None
if nr:
    print(f"{ID}: status {nr['status']}, source sha256 {nr['source_sha256'][:16]}..., precision {nr['precision_bits']} bits, elapsed {nr.get('elapsed_seconds', 0):.0f} s")
    print('| quantity | LB | UB | FLOAT (c1-n1 diag2) | label |'); print('|---|---|---|---|---|')
    for k, r in nr['norms'].items():
        if r['status'] == 'FINITE':
            ratio = ''
            print(f"| {k} | {bnd(r['norm_lower'], False)} | {bnd(r['norm_upper'], True)} | {fl.get(k, '')} | VALIDATED ({r['n_groups']} groups, {r.get('n_classes', '?')} classes, S radius {r.get('S_ball_radius', '?')}, {r['elapsed_seconds']:.0f} s) |")
        else: print(f"| {k} | INFINITE | | | bad sectors {r.get('n_bad')} |")
    if 'assembly' in nr:
        for k, v in nr['assembly'].items(): print(f"  {k}: {str(v)[:60]}")
hp = R / f'{ID}_legqs_hardy.json'
if hp.exists():
    h = json.loads(hp.read_text()); print(f"H (mode-wise Hardy UB) <= {h['H_upper'][:24]}; E_2 in [{h.get('E2_lower_without_H', '?')[:22]}, {h.get('E2_upper_with_mode_hardy_H', '?')[:22]}]; modes {len(h['modes'])}")
pp = R / f'{ID}_legqs_probe.json'
if pp.exists():
    p = json.loads(pp.read_text()); print('| probe | n | I = |<F, phi>| | M | C | H <= | m >= |'); print('|---|---|---|---|---|---|---|')
    for name, r in p['probes'].items():
        if r.get('status') != 'FINITE': print(f'| {name} | divergent |'); continue
        print(f"| {name} | {r['angular_mode']} | {bnd(r['pairing_abs'], False, 13)} | {bnd(r['M'], True, 13)} | {bnd(r['C'], True, 13)} | {bnd(r['H_upper'], True, 10)} | {bnd(r['radius_LB'], False, 14)} |")

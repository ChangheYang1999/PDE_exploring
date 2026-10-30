"""Assemble registered norm values (theory_v01 norm IDs) from the e2norms and hminus1 records of a candidate.
Outputs <ID>_registered_norms.json and prints a Markdown table. All bounds are derived with the A2-THEOREM / theory_v01
comparison inequalities (cited per row); every number is a rigorous UB or LB of the whole-plane quantity."""
from pathlib import Path
from fractions import Fraction as Q
import json, sys
from flint import arb, ctx
ctx.prec = 256

def A(x): return arb(x)
def _directed(x, digits, upward):
    """Decimal string with `digits` significant digits that is >= x (upward) or <= x (downward); x an exact arb (radius 0).
    N4-181: arb.str(n, radius=False) rounds to nearest, so the printed endpoint could cross the certified one by one unit."""
    from fractions import Fraction
    from decimal import Decimal
    s = x.str(digits, radius=False)
    if 'e' in s or 'E' in s: s = format(Decimal(s), 'f')
    q = Fraction(s)
    # one unit in the last printed digit
    d = Decimal(s); exp = d.as_tuple().exponent if isinstance(d.as_tuple().exponent, int) else 0
    nd = len(d.as_tuple().digits); ulp = Fraction(10) ** (exp + max(0, nd - digits))
    xa = x.upper() if upward else x.lower()
    qa = arb(q.numerator) / q.denominator
    for _ in range(3):
        if upward and qa >= xa: break
        if (not upward) and qa <= xa: break
        q = q + ulp if upward else q - ulp; qa = arb(q.numerator) / q.denominator
    return format(Decimal(q.numerator) / Decimal(q.denominator), 'f') if q.denominator != 1 else str(q.numerator)
def up(x): return _directed(x.upper(), 25, True)
def lo(x): return '0' if x.lower() < 0 else _directed(x.lower(), 25, False)

THRESH = {  # theory_v01 section 7 (sufficient thresholds); frameworks and their forcing norm IDs
    'FW-A2-Db (NORM-A2-Ns18)': ('Ns', Q(1, 2 ** 18), Q(1, 1572864)),
    'FW-A2-Da (NORM-A2-Ns28)': ('Ns', Q(1, 2 ** 28), Q(1, 20 * 2 ** 27)),
    'FW-T-TB-rebal-v1 (NORM-T-Ns16-v1)': ('Ns', Q(1, 2 ** 16), Q(3, 327680)),   # exact threshold 3/327680 = 9.1552734375e-6 (N4-252; c1-n4 17:53Z); the earlier 9.1553e-6 display exceeded it, so the earlier ratios were valid lower bounds
    'FW-T-TB-sharp-v1 (NORM-T-Ns13-v1)': ('Ns', Q(1, 2 ** 13), Q('1.0578e-4')),
    'FW-T-T4L2-v1 (NORM-T-X3-v1, s=2^-17)': ('X3', Q(1, 2 ** 17), Q(1, 163840)),   # exact threshold 1/163840 = 6.103515625e-6 (theory_v03 section 12 item 12; c1-n4 correction 12:3xZ)
}
# theory_v02 section 2 (NORM-T-XSW-v1[s, w1, w2]) and section 7: (s, w1, w2, C_w, threshold); conversion (AUDITED, T2-R3 / T4-042):
#   upper X_(s,w) <= E_w^(1-s) (2 Q3^2 + C_w E_w^2)^(s/2) + 1.92 s E_w,  lower X_(s,w) >= (1 - 1.92 s) E_w,  E_w^2 = P2^2 + w1 G1^2 + w2 G0^2.
XSW = {
    'FW-T-T4L2-sharp-v1 (NORM-T-X7744-v1 = XSW[1/7744, 2^14, 2^18])': (Q(1, 7744), 2 ** 14, 2 ** 18, Q('16386.28'), Q(76219, 10 ** 9)),
    'FW-T-T4L2-sharpw-v1 (NORM-T-Xw5184-v1 = XSW[1/5184, 2^15, 2^20])': (Q(1, 5184), 2 ** 15, 2 ** 20, Q('32770.28'), Q(4207, 2 * 10 ** 7)),
    'FW-T-T4L2-bL-v1[7/5] (XSW[1/5476, 2^15, 2^20])': (Q(1, 5476), 2 ** 15, 2 ** 20, Q('32770.28'), Q(423, 2500000)),
    'FW-T-T4L2-bL-v1[1] (XSW[1/6561, 2^15, 2^20])': (Q(1, 6561), 2 ** 15, 2 ** 20, Q('32770.28'), Q(533, 5000000)),
    'FW-T-T4L2-trans-v1 (NORM-T-X3-v1, s=2^-17; 1.92 s conversion)': (Q(1, 2 ** 17), 2 ** 14, 2 ** 18, Q('16386.28'), Q('7.959492e-6')),
}
GRADED_BOX = {'FW-T-TB-graded-v1 (i), s=5*2^-18': (Q(5, 2 ** 18), ['1.7677e-5', '1.3810e-7', '3.4526e-8', '3.5378e-8']),
              'FW-T-TB-graded-v1 (ii), s=1/50000': (Q(1, 50000), ['1.58946e-5', '1.24176e-7', '3.10441e-8', '3.18202e-8']),
              'FW-T-TB-gradedL2-v1, s=5*2^-18 (no H)': (Q(5, 2 ** 18), ['1.78042e-5', '1.39096e-7', '3.47739e-8', None])}

def assemble(ID, resdir):
    resdir = Path(resdir); f = resdir / f'{ID}_e2norms.json'
    if not f.exists(): f = resdir / f'{ID}_legqs_norms.json'          # legqs candidates (legqs_norms.py records; same norm fields)
    rec = json.loads(f.read_text())
    hm = resdir / f'{ID}_hminus1.json'; hrec = json.loads(hm.read_text()) if hm.exists() else None
    N = rec['norms']; out = {'id': ID, 'source_sha256': rec['source_sha256'], 'canonical_sha256': rec.get('canonical_sha256'), 'record': f.name,
                             'components': {}, 'derived': {}, 'thresholds': {}}
    comp = {}
    for k in ['G0', 'G1', 'P2', 'Q3', 'rF', 'Pw1', 'D2']:
        r = N.get(k)
        if r is None: continue
        if r['status'] == 'FINITE':
            comp[k] = (A(r['norm_lower']), A(r['norm_upper'])); out['components'][k] = {'LB': r['norm_lower'], 'UB': r['norm_upper'], 'label': 'VALIDATED'}
        else: out['components'][k] = {'status': 'INFINITE', 'label': 'EXACT divergence'}
    # H component: hminus1 enclosure if available, else rF proxy as UB (A2-THEOREM parity Hardy)
    if hrec and hrec.get('H_upper'):
        comp['H'] = (A(hrec['H_lower']), A(hrec['H_upper'])); out['components']['H'] = {'LB': hrec['H_lower'], 'UB': hrec['H_upper'], 'label': 'VALIDATED (Galerkin Hdot^-1 enclosure, certification/hminus1.py)'}
    elif 'rF' in comp:
        comp['H'] = (arb(0), comp['rF'][1]); out['components']['H'] = {'LB': '0', 'UB': str(comp['rF'][1].upper()), 'label': 'UB only (||F||_H <= ||rF||_2, A2-THEOREM parity Hardy)'}
    need = ['G0', 'G1', 'P2']
    if not all(k in comp for k in need):
        out['derived']['status'] = 'low-order components infinite: not in L^2; only P2, Q3 (and Pw1, D2) are finite'
        return out
    G0, G1, P2 = comp['G0'], comp['G1'], comp['P2']
    def sq(lohi): return (lohi[0] ** 2, lohi[1] ** 2)
    Estar = ((P2[0] ** 2 + 2 ** 14 * G1[0] ** 2 + 2 ** 18 * G0[0] ** 2).sqrt(), (P2[1] ** 2 + 2 ** 14 * G1[1] ** 2 + 2 ** 18 * G0[1] ** 2).sqrt())
    out['derived']['E_star (P2^2+2^14 G1^2+2^18 G0^2)^(1/2), no H'] = {'LB': lo(Estar[0]), 'UB': up(Estar[1])}
    if 'H' in comp:
        H = comp['H']
        E2 = ((Estar[0] ** 2 + 2 ** 18 * arb(20) / 21 * H[0] ** 2).sqrt(), (Estar[1] ** 2 + 2 ** 18 * arb(20) / 21 * H[1] ** 2).sqrt())
        out['derived']['E_2 (NORM-A2-E2)'] = {'LB': lo(E2[0]), 'UB': up(E2[1])}
        out['derived']['weighted squares UB'] = {'P2^2': up(P2[1] ** 2), '2^14 G1^2': up(2 ** 14 * G1[1] ** 2), '2^18 G0^2': up(2 ** 18 * G0[1] ** 2), '2^18 (20/21) H^2': up(2 ** 18 * arb(20) / 21 * H[1] ** 2)}
    Q3 = comp.get('Q3')
    def conv(Elo, Ehi, s):
        """A2 P8.1 (25),(27): N_s <= E^(1-s)(2 Q3^2 + 16410 E^2)^(s/2) + 34 s E ; N_s >= (1-34 s) E (s < 1/34)."""
        sa = arb(s.numerator) / s.denominator
        ub = Ehi ** (1 - sa) * (2 * Q3[1] ** 2 + 16410 * Ehi ** 2) ** (sa / 2) + 34 * sa * Ehi if Q3 else None
        lb = (1 - 34 * sa) * Elo
        return lb, ub
    for name, (kind, s, thr) in THRESH.items():
        if kind == 'Ns':
            if 'H' not in comp: continue
            lb, ub = conv(E2[0], E2[1], s)
        else:
            lb, ub = conv(Estar[0], Estar[1], s)
        thr_a = arb(thr.numerator) / thr.denominator
        out['thresholds'][name] = {'LB': lo(lb), 'UB': up(ub) if ub is not None else None, 'threshold': str(float(thr)),
                                   'LB/threshold': str((lb / thr_a).lower()), 'UB/threshold': str((ub / thr_a).upper()) if ub is not None else None,
                                   'comparison': 'A2-THEOREM P8.1 (25), (27) via theory_v01 section 2' if kind == 'Ns' else 'T4-019 (13) via theory_v01 NORM-T-X3-v1'}
    for name, (s, w1, w2, Cw, thr) in XSW.items():
        sa = arb(s.numerator) / s.denominator; Cwa = arb(Cw.numerator) / Cw.denominator
        Ew = ((P2[0] ** 2 + w1 * G1[0] ** 2 + w2 * G0[0] ** 2).sqrt(), (P2[1] ** 2 + w1 * G1[1] ** 2 + w2 * G0[1] ** 2).sqrt())
        lb = (1 - arb('1.92') * sa) * Ew[0]
        ub = Ew[1] ** (1 - sa) * (2 * Q3[1] ** 2 + Cwa * Ew[1] ** 2) ** (sa / 2) + arb('1.92') * sa * Ew[1] if Q3 else None
        thr_a = arb(thr.numerator) / thr.denominator
        out['thresholds'][name] = {'E_w LB': lo(Ew[0]), 'E_w UB': up(Ew[1]), 'LB': lo(lb), 'UB': up(ub) if ub is not None else None, 'threshold': str(float(thr)),
                                   'LB/threshold': str((lb / thr_a).lower()), 'UB/threshold': str((ub / thr_a).upper()) if ub is not None else None,
                                   'comparison': 'theory_v02 NORM-T-XSW-v1 comparison inequalities (T2-R3, AUDITED via T4-042); Q3 needed for the UB'}
    # graded vector (theory_v01 (G-a) to (G-d), CLAIMED comparisons): gamma_0 in [G0, G0 + s G1], gamma_1 in [G1, G1 + s D2], gamma_H in [H, H + s G0]
    D2 = comp.get('D2', P2)
    for name, (s, box) in GRADED_BOX.items():
        sa = arb(s.numerator) / s.denominator
        g0 = (G0[0], G0[1] + sa * G1[1]); g1 = (G1[0], G1[1] + sa * D2[1])
        g2ub = conv(Estar[0], Estar[1], s)[1]
        row = {'gamma_2': {'UB': up(g2ub) if g2ub is not None else None, 'box': box[0]},
               'gamma_1': {'LB': lo(g1[0]), 'UB': up(g1[1]), 'box': box[1]},
               'gamma_0': {'LB': lo(g0[0]), 'UB': up(g0[1]), 'box': box[2]}}
        if 'H' in comp and box[3]:
            gH = (comp['H'][0], comp['H'][1] + sa * G0[1]); row['gamma_H'] = {'LB': lo(gH[0]), 'UB': up(gH[1]), 'box': box[3]}
        row['first failing component (LB > box)'] = next((k for k, b in zip(['gamma_1', 'gamma_0', 'gamma_H'], box[1:]) if b and k in row and arb(row[k]['LB']) > arb(b)), None)
        row['comparison'] = 'theory_v01 (G-a)-(G-d), CLAIMED (c1-t1); gamma_2 UB from the A2 (25) conversion of E_*'
        out['thresholds'][name] = row
    return out

def table(out):
    lines = [f"### {out['id']} (source sha256 {out['source_sha256'][:16]}..., canonical {str(out.get('canonical_sha256'))[:16]}...)", '',
             '| quantity | LB | UB | label / comparison |', '|---|---|---|---|']
    for k, v in out['components'].items():
        if 'status' in v: lines.append(f"| {k} | INFINITE | INFINITE | {v['label']} |")
        else: lines.append(f"| {k} | {v['LB'][:22]} | {v['UB'][:22]} | {v['label']} |")
    for k, v in out['derived'].items():
        if isinstance(v, dict) and 'LB' in v: lines.append(f"| {k} | {v['LB'][:22]} | {v['UB'][:22]} | derived (square sums of the components) |")
    for k, v in out['thresholds'].items():
        if 'LB/threshold' in v:
            lines.append(f"| {k} | {v['LB'][:16]} | {str(v['UB'])[:16]} | threshold {v['threshold']}; LB/thr = {float(arb(v['LB/threshold']).mid()):.4e}, UB/thr = {float(arb(v['UB/threshold']).mid()):.4e} |")
        else:
            for g in ['gamma_2', 'gamma_1', 'gamma_0', 'gamma_H']:
                if g in v: lines.append(f"| {k}: {g} | {str(v[g].get('LB','-'))[:16]} | {str(v[g].get('UB'))[:16]} | box {v[g]['box']} |")
    return '\n'.join(lines)

if __name__ == '__main__':
    resdir = sys.argv[1]
    for ID in sys.argv[2:]:
        out = assemble(ID, resdir)
        (Path(resdir) / f'{ID}_registered_norms.json').write_text(json.dumps(out, indent=1) + '\n')
        print(table(out)); print()

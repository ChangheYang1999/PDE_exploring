"""Post-process data/certF_088.jsonl (+ far-field and origin data): certified sup_X <r>^{-p2}|F| and sup_{r<=r0} |F - F_3 - F_5|/r^7."""
import sys, json, math
from collections import defaultdict
def main(path, far_json, origin_json, out_json, p2=0.10586538035904068):
    rows = [json.loads(l) for l in open(path) if l.strip()]
    acc = [r for r in rows if r['status'] == 'ok' and not r.get('split')]
    err = [r for r in rows if r['status'] != 'ok']
    cov = defaultdict(float)
    for r in acc: cov[(r['i'], r['k'])] += (math.log(r['r_hi']) - math.log(r['r_lo']))*(r['t_hi'] - r['t_lo'])
    top = {(r['i'], r['k']): (math.log(r['r_hi']) - math.log(r['r_lo']))*(r['t_hi'] - r['t_lo']) for r in rows if r['depth'] == 0}
    bad = [k for k, v in top.items() if abs(cov.get(k, 0) - v) > 1e-9*v]
    print('rows %d accepted %d errors %d; depth-0 cells %d, uncovered %d' % (len(rows), len(acc), len(err), len(top), len(bad)))
    rlo = min(r['r_lo'] for r in acc); rhi = max(r['r_hi'] for r in acc)
    # sup |F| <r>^-p2 over cells: Fw_hi is |F|/r_lo^p2 >= |F| <r>^-p2 (since <r> >= r >= r_lo)
    w = max(acc, key=lambda r: r['Fw_hi'])
    print('cells cover %g <= r <= %g; max |F| r_lo^-p2 = %.6f at r in [%g,%g] theta in [%.3f,%.3f] regime %s' % (rlo, rhi, w['Fw_hi'], w['r_lo'], w['r_hi'], w['t_lo'], w['t_hi'], w['regime']))
    byr = defaultdict(float)
    for r in acc: byr[round(math.log10(r['r_lo']), 1)] = max(byr[round(math.log10(r['r_lo']), 1)], r['Fw_hi'])
    print('max Fw by log10 r_lo:', {k: round(v, 4) for k, v in sorted(byr.items())})
    far = json.load(open(far_json))
    sharp = {k: v for k, v in far.items() if k.startswith('sharp_')}
    print('far field sharp bounds:', {k: v['bound'] for k, v in sharp.items()})
    # origin disk r <= rlo: |F| <= |F3| + |F5| + 77.45 r^7 (from origin_F7_sums at r0 = rlo) ; <r>^-p2 |F| tiny there
    og = json.load(open(origin_json))
    out = {'cells_max_Fw': w['Fw_hi'], 'cells_range': [rlo, rhi], 'uncovered': len(bad), 'errors': len(err)}
    for r0 in (0.05, 0.1, 0.2, 0.3):
        sel = [r for r in acc if r['r_hi'] <= r0*(1+1e-12) and 'F7_hi' in r]
        if sel:
            m = max(r['F7_hi'] for r in sel)
            print('sup over cells with r <= %g of |F - F3 - F5|/r_lo^7 <= %.4f (origin disk r <= %g: <= %.4f from the exact polynomial)' % (r0, m, rlo, og['sum_r0'][str(rlo)] if str(rlo) in og['sum_r0'] else og['sum_r0']['0.005']))
            out['F7_r0_%g' % r0] = m
    json.dump(out, open(out_json, 'w'), indent=1)
if __name__ == '__main__': main(*sys.argv[1:5])

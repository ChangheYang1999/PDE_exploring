"""Post-process cert_W outputs (W = U - DU(0)X, K_bar = rho[phi_K]): sup |W|/r^3 on disks, K_bar positivity away from the x-axis,
and the phase functional ell_w(K_bar) = int_{annulus} K_bar^2 dX for w = indicator of {R1 <= r <= R2} (lower/upper bounds from cell enclosures)."""
import sys, json, math
def main(paths, out_json):
    rows = []
    for p in paths: rows += [json.loads(l) for l in open(p) if l.strip()]
    acc = [r for r in rows if r['status'] == 'ok']
    print('cells %d ok %d; radial range [%g, %g]' % (len(rows), len(acc), min(r['r_lo'] for r in acc), max(r['r_hi'] for r in acc)))
    out = {}
    for r0 in (0.05, 0.1, 0.2, 0.5, 1.0, 2.0):
        sel = [r for r in acc if r['r_hi'] <= r0*(1+1e-12)]
        if sel:
            m = max(r['W_over_r3_hi'] for r in sel); out['W_over_r3_r0_%g' % r0] = m
            print('sup over cells with r <= %g of |U - DU(0)X| / r_lo^3 <= %.5f' % (r0, m))
    neg = [r for r in acc if r['t_lo'] > 1e-12 and r['K_lo'] <= 0]
    print('K_bar: cells with t_lo > 0 and lower bound <= 0: %d of %d' % (len(neg), sum(1 for r in acc if r['t_lo'] > 1e-12)))
    if neg: print('   worst: r in [%g,%g] theta in [%.4f,%.4f] K in [%.3g, %.3g]' % tuple([neg[0]['r_lo'], neg[0]['r_hi'], neg[0]['t_lo'], neg[0]['t_hi'], neg[0]['K_lo'], neg[0]['K_hi']]))
    for (R1, R2) in ((2.0, 8.0), (2.0, 10.0), (1.0, 2.0), (0.5, 2.0)):
        sel = [r for r in acc if r['r_lo'] >= R1*(1-1e-12) and r['r_hi'] <= R2*(1+1e-12)]
        if not sel: continue
        cov = sum(0.5*(r['r_hi']**2 - r['r_lo']**2)*(r['t_hi'] - r['t_lo']) for r in sel)*4      # full plane area covered (4 quadrants)
        area = math.pi*(R2**2 - R1**2)
        lo = sum(min(r['K_lo']**2, r['K_hi']**2)*(0 if r['K_lo'] < 0 < r['K_hi'] else 1)*0.5*(r['r_hi']**2 - r['r_lo']**2)*(r['t_hi'] - r['t_lo']) for r in sel)*4
        hi = sum(max(r['K_lo']**2, r['K_hi']**2)*0.5*(r['r_hi']**2 - r['r_lo']**2)*(r['t_hi'] - r['t_lo']) for r in sel)*4
        print('ell_w(K_bar) = int_{%g<=r<=%g} K_bar^2 dX in [%.4f, %.4f] (covered area %.4f of %.4f)' % (R1, R2, lo, hi, cov, area))
        out['ell_w_%g_%g' % (R1, R2)] = {'lo': lo, 'hi': hi, 'covered_area': cov, 'area': area}
    json.dump(out, open(out_json, 'w'), indent=1)
if __name__ == '__main__': main(sys.argv[1:-1], sys.argv[-1])

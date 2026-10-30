"""Weak necessary-distance probes for candidates with legqs (multi-scale) functions (lane c1-n3): the T4-064 / T4-185 inequality
|<F, phi>| <= (M + C) m + H m^2 with M = ||V.D phi + (2c+1) phi||_2 (V = cX + u), C = ||phi D rho||_2, H = sup |D phi| (C_U = 1), so
m >= 2 I / (M + C + sqrt((M + C)^2 + 4 H I)). I, M, C from the exact tuple-key fields (legqs_norms: exact rational reduction plus one
transcendental per scale and exponent class for low degrees; for the probe-degree groups the t-monomial ball route, 1536 bits).
H = sup |D phi| depends on the probe only: (a) the probe file's H_upper_exact (frozen T4 vectors; reproduced by general_probe on 007),
(b) for a monomial probe phi = r (1-t)^2 t^K sin(n theta) the closed-form rigorous bound: with g2 = (1-t)^2 t^K and
g1 = d/dr (r g2) = g2 + 2 t (1-t) g2' = (1-t)^2 t^K ((1 + 2K) - (2K + 4) t), |D phi| <= max(|g1|, n |g2|) <= (1 + 2K) sup g2 for n <= 1 + 2K,
and sup_[0,1] (1-t)^2 t^K = (2/(K+2))^2 (K/(K+2))^K (the unique interior critical point); the 4 H I term is negligible against (M + C)^2
for every probe here, so this crude but rigorous H changes m by less than 1e-5 relative; (c) otherwise general_probe.sup_abs (slow).
Works for ordinary candidates too (F records of e2norms format: no scale factors).
Usage: legqs_probe.py <ID> <F record (legqs_norms format)> <exact source> <outdir> <probe json> [...]"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, time, hashlib
from flint import fmpq, fmpq_poly, arb, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E, legqs_e2norms as LS, legqs_norms as LN
from e2norms import fq, Z, OM, ONE
from general_probe import sup_abs

def run(ID, record, source, outdir, probe_files, prec=1024):
    ctx.prec = prec; t0 = time.monotonic(); outdir = Path(outdir)
    logf = open(outdir / f'{ID}_legqs_probe.log', 'a')
    def log(*x):
        msg = ' '.join(str(v) for v in x); print(msg, flush=True); logf.write(msg + '\n'); logf.flush()
    c, A, A_s, src_sha, meta = LS.load_reference_legqs(source); delta = 1 - 1 / c
    F, raw = LN.load_F(record)
    if raw.get('source_sha256'): assert raw['source_sha256'] == src_sha, ('record does not match the source', raw.get('source_sha256'), src_sha)
    if raw.get('canonical_sha256'): assert raw['canonical_sha256'] == E.load_reference(source)[3], 'record does not match the source (canonical)' 
    log(f'[{datetime.now(timezone.utc).isoformat(timespec="seconds")}] {ID}: legqs weak probes from {record}; {len(F)} F components; source {src_sha}')
    fields = LN.fields_t(A, A_s, c, log)
    u1, u2, rx, ry = fields['u1'], fields['u2'], fields['rho_x'], fields['rho_y']
    tables = LN.ScaleTables()
    out = {'id': ID, 'record': str(record), 'source_sha256': src_sha, 'cl': str(c), 'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
           'code_sha256': {f: hashlib.sha256((Path(__file__).parent / f).read_bytes()).hexdigest() for f in ('legqs_probe.py', 'legqs_norms.py', 'legqs_e2norms.py')},
           'method': 'I, M, C exact (rational reduction + I0 balls, 1024 bits) from exact tuple-key fields; H rigorous Bernstein bound; T4-064/T4-185 inequality', 'probes': {}}
    dest = outdir / f'{ID}_legqs_probe.json'
    for pf in probe_files:
        pr = json.load(open(pf)); n = int(pr.get('angular_mode', 1)); t1 = time.monotonic()
        P = fmpq_poly([0])
        for k, v in pr['probe_coefficients'].items(): P += fq(Q(v)) * Z ** int(k)
        g2 = OM ** 2 * P; phi = {(0, 's', n, ()): g2}
        Ik = LN.pair_t(F, phi, delta, tables, prec)
        px = LN.diff_t(phi, 0, 'x', delta); py = LN.diff_t(phi, 0, 'y', delta)
        Lphi = LN.canon_t(LN.plus_t((c, LN.mul_t(LN.CX, px)), (c, LN.mul_t(LN.SY, py)), (1, LN.mul_t(u1, px)), (1, LN.mul_t(u2, py)), (2 * c + 1, phi)))
        M2 = LN.normsq_t([(1, Lphi)], 0, delta, tables=tables, prec=prec)
        C2 = LN.normsq_t([(1, LN.canon_t(LN.mul_t(phi, rx))), (1, LN.canon_t(LN.mul_t(phi, ry)))], 0, delta, tables=tables, prec=prec)
        mono = [(int(k), Q(v)) for k, v in pr['probe_coefficients'].items()]
        if pr.get('H_upper_exact'):
            Hq = Q(pr['H_upper_exact']); Hsup = arb(fmpq(Hq.numerator, Hq.denominator)); Lsup = Hsup; c1 = c2 = 0; hsrc = 'probe file H_upper_exact (T4)'
        elif len(mono) == 1 and mono[0][1] > 0 and n <= 1 + 2 * mono[0][0]:
            K, cf = mono[0]; Kq = arb(K); cfa = arb(fmpq(cf.numerator, cf.denominator))
            supg2 = (2 / (Kq + 2)) ** 2 * (Kq / (Kq + 2)) ** K
            Hsup = cfa * (1 + 2 * K) * supg2; Lsup = cfa * n * supg2; c1 = c2 = 0
            hsrc = 'closed form: (1 + 2K) sup (1-t)^2 t^K, sup at t = K/(K+2)'
        else:
            g1 = g2 + 2 * Z * OM * g2.derivative()
            H1, L1, c1 = sup_abs(g1); H2, L2, c2 = sup_abs(g2 * fq(n))
            Hsup = H1 if H1.upper() >= H2.upper() else H2; Lsup = L1 if L1.lower() >= L2.lower() else L2; hsrc = 'Bernstein (general_probe.sup_abs)' 
        if Ik is None or M2['status'] != 'FINITE' or C2['status'] != 'FINITE':
            out['probes'][Path(pf).name] = {'status': 'divergent'}; log(f'{pf}: divergent'); continue
        I = abs(Ik); M = M2['hi'].sqrt(); C = C2['hi'].sqrt()
        Dn = M + C; m = 2 * I / (Dn + (Dn * Dn + 4 * Hsup * I).sqrt())
        res = {'angular_mode': n, 'probe_coefficients': pr['probe_coefficients'], 'pairing_signed': Ik.str(40), 'pairing_abs': I.str(30), 'M': M.str(30), 'C': C.str(30),
               'H_upper': str(Hsup.upper()), 'H_lower_or_sample': str(Lsup.lower()), 'H_source': hsrc, 'H_cells': c1 + c2,
               'radius_LB': str(m.lower()), 'radius': m.str(30), 'seconds': round(time.monotonic() - t1, 1), 'status': 'FINITE',
               'note': 'rigorous lower bound m for the L^2 distance from F to any exact solution rho + h at the same c (T4-064 / T4-185 hypotheses)'}
        out['probes'][Path(pf).name] = res
        log(f'{Path(pf).name} (n={n}): I={I.str(15)} M={M.str(15)} C={C.str(15)} H<={Hsup.upper().str(10)} ({c1+c2} cells)  m >= {m.lower().str(15)}  ({res["seconds"]}s)')
        dest.write_text(json.dumps(out, indent=1) + '\n')
    out['elapsed_seconds'] = round(time.monotonic() - t0, 1); dest.write_text(json.dumps(out, indent=1) + '\n'); log(f'DONE {time.monotonic()-t0:.0f}s')

if __name__ == '__main__':
    ID, record, source, outdir = sys.argv[1:5]
    run(ID, record, source, outdir, sys.argv[5:])

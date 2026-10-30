"""Weak necessary-distance probes with general radial polynomials and angular modes (reproduction of c1-t4 T4-182 and T4-185).
Probe: phi = r u0^2 P(t) sin(n theta), u0 = 1 - t, n odd, t^((n-1)/2) | P (smooth). Weak inequality (T4-064 / T4-185, AUDITED):
for every exact solution rho + h at the same c with m = ||h||_2,  |<F, phi>| <= (M + C) m + H m^2, with
  M = ||V.D phi + (2c+1) phi||_2 (V = cX + u, exact single norm), C = ||phi D rho||_2, H = ||D phi||_infinity (C_U = 1),
so m >= 2 I/(M + C + sqrt((M + C)^2 + 4 H I)). I, M, C are exact Beta integrals (rational times pi) of the exact compactified
polynomials (F from the stored record, fields from the chi derivatives); H is a rigorous Bernstein bound with adaptive subdivision.
Usage: general_probe.py <ID> <F record> <exact source> <outdir> <probe json> [<probe json> ...]   (probe json: T4 verification format)"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, time, hashlib
from flint import fmpq, fmpq_poly, arb, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E, hminus1 as H, dyadic as DY
from e2norms import fq, aq, Z, OM, ONE
from weak_from_cache import fields_from_source

def ell_to_beta(D, delta): return H.normalize(H.from_ell(D, delta))

def sup_abs(p, tol=Q(1, 100), max_cells=4096):
    """Rigorous UB and sampled LB of sup_[0,1] |p(t)| (Bernstein coefficients, adaptive bisection until UB <= (1+tol) LB).
    Bernstein bounds are cached per cell; only the cells whose bound exceeds the stopping level are bisected."""
    lower = arb(0); bcache = {}
    def sample(z1, z2):
        nonlocal lower
        for s_ in (z1, (z1 + z2) / 2, z2):
            v = abs(aq(Q(str(p(fq(s_))))))
            if v.lower() > lower.lower(): lower = v
    def bound(z1, z2):
        if (z1, z2) not in bcache: bcache[(z1, z2)] = aq(DY.bernstein_sup(p, z1, z2))
        return bcache[(z1, z2)]
    cells = [(Q(0), Q(1))]; sample(Q(0), Q(1))
    for _ in range(80):
        ub = max((bound(z1, z2) for z1, z2 in cells), key=lambda b: float(b.upper()))
        if ub.upper() <= ((1 + aq(tol)) * lower).lower() or len(cells) >= max_cells: return ub, lower, len(cells)
        thresh = (lower.lower() * aq(1 + tol))
        new = []
        for z1, z2 in cells:
            if bound(z1, z2).upper() > thresh and (z2 - z1) > Q(1, 2 ** 40):
                m = (z1 + z2) / 2; new += [(z1, m), (m, z2)]; sample(z1, m); sample(m, z2)
            else: new.append((z1, z2))
        cells = new
    ub = max((bound(z1, z2) for z1, z2 in cells), key=lambda b: float(b.upper()))
    return ub, lower, len(cells)

def run(ID, record, source, outdir, probe_files):
    ctx.prec = 512; t0 = time.monotonic(); outdir = Path(outdir)
    logf = open(outdir / f'{ID}_general_probe.log', 'a')
    def log(*x):
        msg = ' '.join(str(v) for v in x); print(msg, flush=True); logf.write(msg + '\n'); logf.flush()
    c, A, src_sha, can_sha, meta = E.load_reference(source); delta = 1 - 1 / c
    F_ell, delta_rec, can_rec, _ = H.load_F(record, log)
    assert Q(delta_rec) == delta and can_rec == can_sha, ('record does not match the source', can_rec, can_sha)
    log(f'[{datetime.now(timezone.utc).isoformat(timespec="seconds")}] {ID}: general weak probes from {record}; source {src_sha}')
    F = ell_to_beta(F_ell, delta)
    fields = fields_from_source(A, c, log)
    u1, u2, rx, ry = fields['u1'], fields['u2'], fields['rho_x'], fields['rho_y']
    cx = {(0, 'c', 1): ONE}; sy = {(0, 's', 1): ONE}
    out = {'id': ID, 'record': str(record), 'source_sha256': src_sha, 'canonical_sha256': can_sha, 'cl': str(c),
           'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'method': 'I, M, C exact Beta integrals (rational times pi) of exact compactified polynomials; H rigorous Bernstein bound; 512-bit balls', 'probes': {}}
    for pf in probe_files:
        pr = json.load(open(pf)); n = int(pr.get('angular_mode', 1)); t1 = time.monotonic()
        P = fmpq_poly([0]); 
        for k, v in pr['probe_coefficients'].items():
            P += fq(Q(v)) * Z ** int(k)
        g2 = OM ** 2 * P                                             # phi = r g2(t) sin(n theta)
        phi = {(0, 's', n): g2}                                      # degree-0 form (ell = 0)
        # pairing
        Ik = H.pair(F, 0, ell_to_beta(phi, delta), 0)
        # M = ||c X.D phi + u.D phi + (2c+1) phi||_2
        px = E.diff(phi, 0, 'x', delta); py = E.diff(phi, 0, 'y', delta)
        Lphi = E.plus((c, E.mul(cx, px)), (c, E.mul(sy, py)), (1, E.mul(u1, px)), (1, E.mul(u2, py)), (2 * c + 1, phi))
        M2 = H.normB(ell_to_beta(Lphi, delta), 0)
        # C = ||phi D rho||_2
        C2 = H.normB([(1, ell_to_beta(E.mul(phi, rx), delta)), (1, ell_to_beta(E.mul(phi, ry), delta))], 0)
        # H = sup |D phi| = sup_t max(|g1|, n |g2|), g1 = d/dr (r g2) = g2 + 2 t (1-t) g2'
        g1 = g2 + 2 * Z * OM * g2.derivative()
        H1, L1, c1 = sup_abs(g1); H2, L2, c2 = sup_abs(g2 * fq(n))
        Hsup = H1 if H1.upper() >= H2.upper() else H2; Lsup = L1 if L1.lower() >= L2.lower() else L2
        if None in (Ik, M2, C2):
            out['probes'][Path(pf).name] = {'status': 'divergent'}; log(f'{pf}: divergent'); continue
        I = abs(arb.pi() * aq(Q(str(Ik)))); M = (arb.pi() * aq(Q(str(M2)))).sqrt(); C = (arb.pi() * aq(Q(str(C2)))).sqrt()
        D = M + C; m = 2 * I / (D + (D * D + 4 * Hsup * I).sqrt())
        res = {'angular_mode': n, 'pairing_signed_over_pi_exact': str(Ik), 'pairing_abs': I.str(30), 'M': M.str(30), 'C': C.str(30),
               'H_upper': str(Hsup.upper()), 'H_sampled_lower': str(Lsup.lower()), 'H_cells': c1 + c2,
               'radius_LB': str(m.lower()), 'radius': m.str(30), 'seconds': round(time.monotonic() - t1, 1),
               'T4_values': {k: pr.get(k) for k in ('pairing', 'M', 'C', 'H_upper_exact', 'radius', 'strict_lower_exact')}}
        out['probes'][Path(pf).name] = res
        log(f'{Path(pf).name} (n={n}): I={I.str(15)} M={M.str(15)} C={C.str(15)} H<={Hsup.upper().str(10)} (sampled >= {Lsup.lower().str(8)}, {c1+c2} cells)  m >= {m.lower().str(15)}')
        log(f'   T4: pairing {str(pr.get("pairing"))[:24]} M {str(pr.get("M"))[:22]} C {str(pr.get("C"))[:22]} H {pr.get("H_upper_exact")} radius {str(pr.get("radius"))[:22]} strict {pr.get("strict_lower_exact")}')
        (outdir / f'{ID}_general_probe.json').write_text(json.dumps(out, indent=1) + '\n')
    out['elapsed_seconds'] = round(time.monotonic() - t0, 1)
    (outdir / f'{ID}_general_probe.json').write_text(json.dumps(out, indent=1) + '\n'); log(f'DONE {time.monotonic()-t0:.0f}s')

if __name__ == '__main__':
    ID, record, source, outdir = sys.argv[1:5]
    run(ID, record, source, outdir, sys.argv[5:])

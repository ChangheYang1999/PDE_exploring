"""NORM-T-WEAK-v1 (a = 0) for a list of k from a stored exact F record, plus the exact signed weak pairing per dyadic annulus
(theory_v02 section 9 item 6: where the weak distance is created). Lane c1-n3.
The expensive F assembly is read from <ID>_Fpoly.json or the hminus1 cache; the fields u, D rho are recomputed from the exact
source (chi derivatives only, about a minute). Pairings and norms are exact Beta integrals (rational times pi); the per-annulus
pairings use incomplete Beta functions in 512-bit ball arithmetic (dyadic.region_integral) and must add up to the exact total.
Usage: weak_from_cache.py <ID> <F record json> <exact source json> <outdir> [--k 0,1,...,8,128] [--annuli_k 0,8] [--jmin -3] [--jmax 5]"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, time, hashlib, argparse
from flint import fmpq, fmpq_poly, arb, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E, hminus1 as H, dyadic as DY
from e2norms import fq, aq, Z, OM, ONE, endpoint
from candidate_pipeline import weak_stage, ell_to_beta

def fields_from_source(A, c, log):
    t0 = time.monotonic(); j3 = {}; j4 = {}
    for d, save in [(3, j3), (4, j4)]:
        for nx in range(d): save[nx] = E.chi_compact(A, c, d, nx)
    rho = E.plus((-1, j3[0]), (-1, j3[2])); u1 = E.plus((-1, j3[1])); u2 = j3[2]
    rx = E.plus((-1, j4[1]), (-1, j4[3])); ry = E.plus((-1, j4[0]), (-1, j4[2]))
    log(f'fields from chi derivatives ({time.monotonic()-t0:.0f}s)')
    return {'rho': rho, 'u1': u1, 'u2': u2, 'rho_x': rx, 'rho_y': ry}

def pairing_groups(F, k):
    """Groups {b: poly} with int F phi_k dX / pi = sum_b int_0^1 poly_b(t) (1-t)^b dt, phi_k = y t^k u0^2 (both degree-0 forms)."""
    groups = {}
    for (beta, kind, n), p in F.items():
        if kind != 's' or n != 1: continue
        q1, p1 = endpoint(p)
        b = Q(-3) + beta + q1 + 2                        # (1-t)^2 of phi_k is an exact endpoint factor
        poly = p1 * Z ** k * Z * fq(Q(1, 2))
        groups[b] = groups.get(b, fmpq_poly([])) + poly
    return groups

def run(ID, record, source, outdir, k_list, annuli_k, jmin, jmax):
    ctx.prec = 512; t0 = time.monotonic(); outdir = Path(outdir)
    logf = open(outdir / f'{ID}_weak.log', 'a')
    def log(*x):
        msg = ' '.join(str(v) for v in x); print(msg, flush=True); logf.write(msg + '\n'); logf.flush()
    c, A, src_sha, can_sha, meta = E.load_reference(source); delta = 1 - 1 / c
    F_ell, delta_rec, can_rec, _ = H.load_F(record, log)
    assert Q(delta_rec) == delta and can_rec == can_sha, ('record does not match the source', can_rec, can_sha)
    log(f'[{datetime.now(timezone.utc).isoformat(timespec="seconds")}] {ID}: weak probes from {record}; {len(F_ell)} F components; source {src_sha}')
    F = H.normalize(H.from_ell(F_ell, delta))
    fields = fields_from_source(A, c, log)
    rec = {'id': ID, 'record': str(record), 'source_path': str(source), 'source_sha256': src_sha, 'canonical_sha256': can_sha, 'cl': str(c),
           'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'norm': 'NORM-T-WEAK-v1 (a = 0): phi_k = y t^k u0^2; I_k, A_k, B_k, C_k exact Beta integrals (rational times pi), H_k explicit; m_k LB',
           'WEAK_a0': {}, 'annuli': {}}
    dest = outdir / f'{ID}_weak.json'
    def save():
        rec['elapsed_seconds'] = round(time.monotonic() - t0, 1); dest.write_text(json.dumps(rec, indent=1) + '\n')
    weak_stage(F, fields, c, delta, k_list, rec, log, save)
    # per-annulus signed pairing (exact total check)
    edges = [Q(0)] + [Q(4) ** j / (1 + Q(4) ** j) for j in range(jmin, jmax + 2)] + [1]
    labels = [f'r<{2**jmin}'] + [f'[{2**j},{2**(j+1)})' if j >= 0 else f'[{2**j},{2**(j+1)})' for j in range(jmin, jmax + 1)] + [f'r>={2**(jmax+1)}']
    for k in annuli_k:
        if k > 4096:
            log(f'annuli k={k}: skipped (dense shifted polynomials of degree {k} make the incomplete-Beta tables too large; use k <= 4096)'); continue
        groups = pairing_groups(F, k); cache = {}
        exact = fmpq(0); bet = {}
        for b, p in groups.items(): exact += E.integral(p, b, bet)
        vals = []
        for z1, z2 in zip(edges[:-1], edges[1:]):
            s = arb(0)
            for b, p in groups.items(): s += DY.region_integral(p, b, z1, z2 if z2 != 1 else 1, cache)
            vals.append(s * arb.pi())
        tot = sum(vals, arb(0)); ex = arb.pi() * aq(Q(str(exact)))
        ok = tot.contains(ex) or (tot - ex).abs_upper() < arb(10) ** (-30)
        rec['annuli'][str(k)] = {'edges_r': [f'2^{j}' for j in range(jmin, jmax + 2)], 'signed_pairing_pi_times': [v.str(12) for v in vals], 'labels': labels,
                                 'exact_total': ex.str(20), 'sum_of_regions': tot.str(20), 'sum_matches_exact': bool(ok)}
        log(f'annuli k={k}: total {ex.str(15)} (regions sum {tot.str(15)}, match {ok}); ' + '; '.join(f'{l}: {v.str(6)}' for l, v in zip(labels, vals)))
        save()
    log(f'DONE {time.monotonic()-t0:.0f}s'); save()

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('ID'); ap.add_argument('record'); ap.add_argument('source'); ap.add_argument('outdir')
    ap.add_argument('--k', default='0,1,2,3,4,5,6,7,8,128'); ap.add_argument('--annuli_k', default='0,8'); ap.add_argument('--jmin', type=int, default=-3); ap.add_argument('--jmax', type=int, default=5)
    a = ap.parse_args()
    run(a.ID, a.record, a.source, a.outdir, [int(x) for x in a.k.split(',')], [int(x) for x in a.annuli_k.split(',')], a.jmin, a.jmax)

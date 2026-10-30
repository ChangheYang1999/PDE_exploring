"""theory_v02 norms from one exact residual run (lane c1-n3):
  NORM-T-WLAP-v1[a]: N_a(F) = ||(1+r^2)^((2-a)/2) Delta F||_2, exact (rational times pi) for a list of a;
  NORM-T-WL2-v1[a]:  ||(1+r^2)^(-a/2) F||_2, exact, a in {1, 6/5} and more;
  NORM-T-WEAK-v1[k, a=0]: I_k = |int F phi_k|, phi_k = y t^k u0^2, u0 = 1/(1+r^2); A_k = ||phi_k L_k||_2,
     B_k = ||t^k u0^2 G_k u||_2, C_k = ||r t^k u0^2 D rho||_2 (all exact Beta integrals), H_k explicit,
     m_k = 2 I_k/(D_k + sqrt(D_k^2 + 4 H_k I_k)), D_k = A_k + B_k + C_k: every exact solution at fixed c has ||h||_2 >= max_k m_k.
Representation: degree-0 objects r (1-t)^beta P(t) trig; degree-2: r (1-t) (1-t)^beta P; degree 3 (u, rho) and 4 (D rho)
from the chi derivatives (with and without the factor r). t = r^2/(1+r^2), u0 = 1 - t."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, time, hashlib
from flint import fmpq, fmpq_poly, arb, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import e2norms as E, hminus1 as H
from e2norms import fq, aq, Z, OM, ONE

def ell_to_beta(D, delta): return H.normalize(H.from_ell(D, delta))

def scale_poly(D, W):
    """Multiply every component polynomial by the polynomial W(t) (exact)."""
    return {k: p * W for k, p in D.items()}

def S(a, b): return Q(a) ** a * Q(b) ** b / Q(a + b) ** (a + b)

def run(source, ID, outdir, a_list, kmax=0, wl2_list=(Q(1), Q(6, 5))):
    ctx.prec = 512; t0 = time.monotonic(); outdir = Path(outdir)
    logf = open(outdir / f'{ID}_wlap.log', 'a')
    def log(*x):
        msg = ' '.join(str(v) for v in x); print(msg, flush=True); logf.write(msg + '\n'); logf.flush()
    c, A, src_sha, can_sha, meta = E.load_reference(source); delta = 1 - 1 / c
    log(f'[{datetime.now(timezone.utc).isoformat(timespec="seconds")}] {ID}: wlap/wl2/weak norms; {meta}')
    D, fields = E.residual_polynomials(A, c, 2, log)
    F = ell_to_beta(D[0, 0], delta)
    lap = ell_to_beta(E.plus((1, D[2, 0]), (1, D[2, 2])), delta)          # Delta F as a degree-2 object
    rec = {'id': ID, 'source_sha256': src_sha, 'canonical_sha256': can_sha, 'cl': str(c), 'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
           'WLAP': {}, 'WL2': {}, 'WEAK_a0': {}, 'method': 'exact Beta integrals of the exact compactified polynomials (rational times pi), 512-bit balls for the square roots'}
    # NORM-T-WLAP-v1: N_a^2 = pi * sum_b int t P_b (1-t)^(b + a - 2)   [weight^2 = (1+r^2)^(2-a) = (1-t)^(a-2)];
    # the group polynomials of Delta F (as a degree-2 object) are built once and integrated for every a.
    groups = {}; bad = False
    modes = {}
    for (beta, kind, n), p in lap.items():
        q, p2 = H.endpoint(p); modes.setdefault((kind, n), []).append((beta, q, p2))
    for (kind, n), rows in modes.items():
        for i, (beta, q, p) in enumerate(rows):
            for j in range(i, len(rows)):
                beta2, q2, p2 = rows[j]
                b = Q(2 - 3) + beta + beta2 + q + q2
                factor = (2 if (kind == 'c' and n == 0) else 1) * (1 if i == j else 2) * Q(1, 2)
                groups[b] = groups.get(b, fmpq_poly([])) + p * p2 * fq(factor) * Z
    for a in a_list:
        tot = fmpq(0); cache = {}; div = False
        for b, p in groups.items():
            bb = b + Q(a) - 2
            if bb <= -1: div = True; break
            tot += E.integral(p, bb, cache)
        if div: rec['WLAP'][str(a)] = {'status': 'INFINITE'}; log(f'N_a a={a}: INFINITE'); continue
        n = (arb.pi() * aq(Q(str(tot)))).sqrt()
        rec['WLAP'][str(a)] = {'LB': str(n.lower()), 'UB': str(n.upper()), 'sq_over_pi_exact': str(tot)}
        log(f'N_a(F) a={a}: [{n.lower()}, {n.upper()}]  ({time.monotonic()-t0:.0f}s)')
    # NORM-T-WL2-v1: ||w_a F||_2^2 = pi * normB(F, 0, a)   [w_a^2 = (1+r^2)^(-a) = (1-t)^a]
    (outdir / f'{ID}_wlap.json').write_text(json.dumps(rec, indent=1) + '\n')
    for a in wl2_list:
        v = H.normB(F, 0, Q(a))
        n = (arb.pi() * aq(Q(str(v)))).sqrt() if v is not None else None
        rec['WL2'][str(a)] = {'LB': str(n.lower()), 'UB': str(n.upper())} if n is not None else {'status': 'INFINITE'}
        log(f'||w_a F||_2 a={a}: {rec["WL2"][str(a)]}')
    (outdir / f'{ID}_wlap.json').write_text(json.dumps(rec, indent=1) + '\n')
    # NORM-T-WEAK-v1 at a = 0, k = 0..kmax
    u1 = ell_to_beta(fields['u1'], delta); u2 = ell_to_beta(fields['u2'], delta)          # degree-3 form: r (1-t)^beta P trig
    rx = ell_to_beta(fields['rho_x'], delta); ry = ell_to_beta(fields['rho_y'], delta)   # degree-4 form: (1-t)^beta P trig (no r)
    # degree-3 form is my "degree 0" form (r (1-t)^0 (1-t)^beta P): usable directly with d = 0 in normB/pair.
    # degree-4 form is my "odd degree 1" form ((1-t)^0 (1-t)^beta P): usable with d = 1.
    for k in range(kmax + 1):
        W = Z ** k * OM ** 2                                            # t^k u0^2
        phi = {(Q(0), 's', 1): W}                                       # y t^k u0^2 = r sin(theta) t^k (1-t)^2, degree-0 form
        Ik = H.pair(F, 0, phi, 0)                                       # int F phi / pi (exact rational; may be None if divergent)
        Lk = fq(3 * c + 1) * ONE + fq(2 * c * k) * OM - fq(4 * c) * Z    # 3c + 1 + 2ck u0 - 4ct
        Gk = ONE + fq(2 * k) * OM + 4 * Z                               # 1 + 2k u0 + 4t
        Ak2 = H.normB({(Q(0), 's', 1): W * Lk}, 0)                      # ||phi_k L_k||_2^2 / pi
        Bk2 = H.normB([(1, scale_poly(u1, W * Gk)), (1, scale_poly(u2, W * Gk))], 0)      # ||t^k u0^2 G_k u||_2^2/pi (u carries r)
        Ck2 = H.normB([(1, scale_poly(rx, W)), (1, scale_poly(ry, W))], 1, Q(-1), 1)      # ||r t^k u0^2 D rho||_2^2/pi (odd form, extra r)
        Hk = Q(1) if k == 0 else S(k, 2) + 2 * k * S(k, 3) + 4 * S(k + 1, 2)
        if None in (Ik, Ak2, Bk2, Ck2):
            rec['WEAK_a0'][str(k)] = {'status': 'divergent'}; log(f'k={k}: divergent'); continue
        I = abs(arb.pi() * aq(Q(str(Ik)))); Ak = (arb.pi() * aq(Q(str(Ak2)))).sqrt(); Bk = (arb.pi() * aq(Q(str(Bk2)))).sqrt(); Ck = (arb.pi() * aq(Q(str(Ck2)))).sqrt()
        Dk = Ak + Bk + Ck; Hk_a = aq(Hk)
        m = 2 * I / (Dk + (Dk ** 2 + 4 * Hk_a * I).sqrt())
        rec['WEAK_a0'][str(k)] = {'I_k_signed_over_pi_exact': str(Ik), 'I_k': str(I.lower()), 'A_k_UB': str(Ak.upper()), 'B_k_UB': str(Bk.upper()), 'C_k_UB': str(Ck.upper()),
                                  'H_k': str(Hk), 'm_k_LB': str(m.lower())}
        log(f'k={k}: I_k={I.str(12)} A_k={Ak.str(10)} B_k={Bk.str(10)} C_k={Ck.str(10)} H_k={float(Hk):.4f}  m_k >= {m.lower()}  ({time.monotonic()-t0:.0f}s)')
    ms = [arb(v['m_k_LB']) for v in rec['WEAK_a0'].values() if 'm_k_LB' in v]
    if ms:
        best = max(ms, key=lambda x: float(x.lower())); rec['weak_distance_LB_a0'] = str(best.lower()); log(f'weak L^2 distance (a = 0) >= {best.lower()}')
    rec['elapsed_seconds'] = time.monotonic() - t0; rec['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (outdir / f'{ID}_wlap.json').write_text(json.dumps(rec, indent=1) + '\n'); log(f'DONE {ID} {rec["elapsed_seconds"]:.0f}s')

if __name__ == '__main__':
    source, ID, outdir = sys.argv[1:4]
    a_list = [Q(x) for x in (sys.argv[4].split(',') if len(sys.argv) > 4 else ['0', '1/5', '1/4', '2/5', '1/2', '3/5', '3/4', '4/5', '1', '5/4', '3/2'])]
    kmax = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    run(source, ID, outdir, a_list, kmax)

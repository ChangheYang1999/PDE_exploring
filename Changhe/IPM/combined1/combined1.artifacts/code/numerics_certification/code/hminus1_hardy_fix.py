"""Sharpen the per-mode Hdot^-1 upper bounds of an hminus1 record by the direct parity Hardy bound ||F_n||_H <= ||r F_n||_2
(A2-THEOREM, S1_CLOSURE section 7a: valid for functions without angular mode 0; F_n is a single sin(n theta) mode, n odd).
For every exact mode row the new UB is min(Galerkin identity UB, exact Hardy bound); totals are recomputed. Lane c1-n3.
Usage: hminus1_hardy_fix.py <ID> <F record> <outdir>"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, time, hashlib
from flint import arb, ctx
sys.set_int_max_str_digits(0)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import hminus1 as H
from e2norms import aq

def run(ID, record, outdir):
    ctx.prec = 512; t0 = time.monotonic(); outdir = Path(outdir)
    recp = outdir / f'{ID}_hminus1.json'; rec = json.loads(recp.read_text())
    logf = open(outdir / f'{ID}_hminus1.log', 'a')
    def log(*x):
        msg = ' '.join(str(v) for v in x); print(msg, flush=True); logf.write(msg + '\n'); logf.flush()
    F_ell, delta, can_sha, _ = H.load_F(record, log)
    assert can_sha == rec['canonical_sha256'], (can_sha, rec['canonical_sha256'])
    F = H.normalize(H.from_ell(F_ell, Q(delta)))
    log(f'[{datetime.now(timezone.utc).isoformat(timespec="seconds")}] {ID}: Hardy fix of the per-mode UBs ({len(F)} F components)')
    changed = []
    for r in rec['rows']:
        if 'mode_norm_UB' not in r: continue
        n = int(r['n']); v = H.normB(H.mode_component(F, n), 0, Q(-1), 1)          # ||r F_n||_2^2 / pi, exact
        if v is None: continue
        hardy = (arb.pi() * aq(Q(str(v)))).sqrt()
        old = arb(r['mode_norm_UB'])
        r['hardy_direct_UB'] = str(hardy.upper())
        if hardy.upper() < old.upper():
            r['mode_norm_UB_galerkin'] = r['mode_norm_UB']; r['mode_norm_UB'] = str(hardy.upper()); r['ub_source'] = 'direct parity Hardy bound ||r F_n||_2'
            changed.append((n, float(old.mid()), float(hardy.mid())))
        log(f'  mode {n}: LB {arb(r["mode_norm_LB"]).str(8)} Galerkin UB {old.str(8)} Hardy UB {hardy.str(8)} -> UB {arb(r["mode_norm_UB"]).str(8)}')
    rec['H_lower'], rec['H_upper'] = H.totals_from_rows(rec['rows'], rec.get('tail'))
    rec.setdefault('fixes', []).append({'type': 'per-mode min(Galerkin UB, direct Hardy UB)', 'modes_changed': [c[0] for c in changed],
                                        'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    recp.write_text(json.dumps(rec, indent=1) + '\n')
    log(f'RESULT after Hardy fix {ID}: ||F||_H in [{rec["H_lower"]}, {rec["H_upper"]}] ({len(changed)} modes changed, {time.monotonic()-t0:.0f}s)')

if __name__ == '__main__':
    run(*sys.argv[1:4])

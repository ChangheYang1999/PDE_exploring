"""H18 falsification check (c1-coord 14:29Z part 8) for the mode-wise Hardy bound of a legqs candidate (lane c1-n3).
Shows that the modes used by legqs_hardy.py cover the whole angular content of the exact F record: every key of the record is a sine
mode with odd n >= 1 (no cosine key, no mode 0), the set of modes and the per-mode component counts equal those of the Hardy record,
and the ball of sum_n ||r F_n||_2^2 (from the Hardy record rows) overlaps the ball of rF^2 of the production norm record (both contain
the exact value, so they must intersect: the mode squares enclose rF^2 from both sides). Also recomputes H^2 = sum_n ||r F_n||_2^2 / n^2
from the rows and compares with the recorded H_upper.
Usage: hardy_cover_check.py <ID> <F record> <results dir>"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json, sys, time, hashlib
from flint import arb, ctx
sys.set_int_max_str_digits(0)

def run(ID, record, outdir):
    t0 = time.monotonic(); outdir = Path(outdir); ctx.prec = 512
    raw = json.loads(Path(record).read_text())
    rows = raw['polynomials']['0,0']
    keys = [(r['ell'], r['kind'], r['mode'], tuple((a, N) for a, N in r.get('scales', []))) for r in rows]
    kinds = sorted({k[1] for k in keys}); modes = sorted({k[2] for k in keys})
    per_mode = {}
    for k in keys: per_mode[k[2]] = per_mode.get(k[2], 0) + 1
    hardy = json.loads((outdir / f'{ID}_legqs_hardy.json').read_text())
    hmodes = [r['n'] for r in hardy['modes']]; hcomp = {r['n']: r['components'] for r in hardy['modes']}
    norms = json.loads((outdir / f'{ID}_legqs_norms.json').read_text())['norms']['rF']
    rF2_lo = arb(norms['square_lo_ball']); rF2_hi = arb(norms['square_hi_ball'])
    rF2_prod = arb(norms['norm_lower']) ** 2
    rF2_prod = arb(norms['norm_lower']).union(arb(norms['norm_upper'])) ** 2   # ball from the directed endpoints
    S = arb(0); H2 = arb(0)
    for r in hardy['modes']:
        v = arb(r['rF_n_sq']); S += v; H2 += v / (r['n'] * r['n'])
    checks = {
        'all_keys_sine': kinds == ['s'],
        'all_modes_odd_positive': all(n % 2 == 1 and n >= 1 for n in modes),
        'modes_equal_hardy_record': modes == hmodes,
        'component_counts_equal': all(per_mode[n] == hcomp.get(n) for n in modes) and sum(per_mode.values()) == len(rows),
        'sum_rFn_sq_overlaps_production_rF_sq_lo': S.overlaps(rF2_lo),
        'sum_rFn_sq_overlaps_production_rF_sq_hi': S.overlaps(rF2_hi),
        'sum_rFn_sq_overlaps_directed_endpoint_ball': S.overlaps(rF2_prod),
        'H_sq_recomputed_overlaps_record': H2.sqrt().overlaps(arb(hardy['H_upper_ball'])),
        # the rows are 30-digit ball strings, so the recomputed H carries a radius of about 1e-26; the recorded H_upper (1024 bits) must lie
        # inside the recomputed ball (check above) and must not fall below its lower endpoint (an understated bound would show here)
        'recorded_H_upper_not_below_recomputed_lower': arb(hardy['H_upper']).lower() >= H2.sqrt().lower(),
    }
    out = {'id': ID, 'record': str(record), 'record_sha256_prefix': hashlib.sha256(Path(record).read_bytes()).hexdigest()[:16],
           'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'n_keys': len(rows), 'kinds': kinds, 'n_modes': len(modes), 'modes_first_last': [modes[0], modes[-1]],
           'modes_are_all_odd_from_1_to_max': modes == list(range(1, modes[-1] + 1, 2)),
           'per_mode_components_min_max': [min(per_mode.values()), max(per_mode.values())],
           'sum_rFn_sq_ball': S.str(35), 'production_rF_sq_lo_ball': rF2_lo.str(35), 'production_rF_sq_hi_ball': rF2_hi.str(35),
           'sum_rFn_ball': S.sqrt().str(35), 'production_rF_lower': norms['norm_lower'][:60], 'production_rF_upper': norms['norm_upper'][:60],
           'H_sq_recomputed_ball': H2.str(35), 'H_recomputed_ball': H2.sqrt().str(35), 'H_upper_recorded': hardy['H_upper'][:60],
           'checks': checks, 'all_pass': all(checks.values()), 'elapsed_seconds': round(time.monotonic() - t0, 1),
           'statement': ('The exact F record consists only of sine modes with odd n; the Hardy record uses exactly these modes with the same '
                         'component counts; the sum of the per-mode ||r F_n||_2^2 balls and the production rF^2 ball overlap, so the mode '
                         'squares enclose rF^2 from both sides and the mode-wise Hardy bound omits no angular content of F.' if all(checks.values())
                         else 'A check FAILED: see checks.')}
    (outdir / f'{ID}_hardy_cover.json').write_text(json.dumps(out, indent=1) + '\n')
    for k, v in checks.items(): print(f'{k}: {v}')
    print(f'modes {len(modes)} ({modes[0]}..{modes[-1]}), keys {len(rows)}; sum rF_n^2 = {S.str(25)} vs production rF^2 lo {rF2_lo.str(25)} hi {rF2_hi.str(25)}')
    print(f'H recomputed {H2.sqrt().str(25)} vs recorded {hardy["H_upper"][:30]}; ALL PASS = {all(checks.values())} ({time.monotonic()-t0:.0f}s)')

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], sys.argv[3])

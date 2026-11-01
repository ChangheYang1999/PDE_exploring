"""Synthetic monitor checks and independent dyadic checkpoint precision audit."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import importlib.util
import json
import math
import pickle
import sys
import time
sys.dont_write_bytecode = True
from flint import arb, fmpz, ctx

TARGET = Path('research/53_stream_precision')


def clean(x):
    if isinstance(x, float) and not math.isfinite(x):
        return str(x)
    if isinstance(x, dict):
        return {str(k): clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [clean(v) for v in x]
    return x


def synthetic():
    hashes = {}
    for name in ('logff.py', 'ffcore.py'):
        raw = (Path('../a4-num/code') / name).read_bytes()
        (TARGET / 'sources' / (name + '.txt')).write_bytes(raw)
        hashes[name] = sha256(raw).hexdigest()
    spec = importlib.util.spec_from_file_location('audited_logff', '../a4-num/code/logff.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    obj = module.LogFarField(module.make_ring('arb', 512), 2, 3, ['1'])
    rows = []
    for name, F, G in (
        ('wide_stream', [[arb(1)]], [[arb(0), arb(1, '0.1')]]),
        ('zero_midpoint_density', [[arb(1)], [arb(0, '1e-20')]], [[arb(0), arb(1)]]),
        ('exact_control', [[arb(1)]], [[arb(0), arb(1)]]),
    ):
        obj.f[2], obj.g[2] = F, G
        obj._stats(2)
        rows.append(dict(case=name, density=[[str(x) for x in col] for col in F],
                         stream=[[str(x) for x in col] for col in G],
                         observed=clean(obj.stats[2])))
    return hashes, rows


def dyadic(m, e):
    out = arb(fmpz(int(m))) * arb(2) ** int(e)
    assert out.is_exact()
    return out


def unpack(record):
    m, e, r = record
    mid = dyadic(m, e)
    if r == '0':
        radius = arb(0)
    else:
        rm, re = r.split('*2^')
        radius = dyadic(rm, re)
    assert radius >= 0
    return mid, radius


def text(x):
    return x.str(24, radius=True)


def column(packed, log10):
    mids, radii = zip(*(unpack(x) for x in packed))
    M, R = max(map(abs, mids)), max(radii)
    S, T = sum(map(abs, mids), arb(0)), sum(radii, arb(0))
    uncertain_zero = M == 0 and R != 0
    if M == 0:
        rel = arb(0) if R == 0 else None
        normrel = arb(0) if T == 0 else None
    else:
        rel, normrel = R / M, T / S
    balls = [arb(m, r) for m, r in zip(mids, radii)]
    norm = sum(map(abs, balls), arb(0))
    lnorm = norm.log() / log10 if norm > 0 else None
    row = dict(count=len(packed), exact_zero=bool(M == 0 and R == 0),
               uncertain_zero=bool(uncertain_zero), norm_ball=text(norm),
               log10_norm_ball=text(lnorm) if lnorm is not None else None,
               maximum_scale_relative_radius=text(rel) if rel is not None else 'undefined',
               wiener_relative_radius=text(normrel) if normrel is not None else 'undefined')
    return row, rel, normrel, lnorm


def main():
    start = time.monotonic()
    hashes, synthetic_rows = synthetic()
    ctx.prec = 640
    checkpoint = Path('../a4-num/ckpt/log_sin1_c3_p512.pkl')
    raw = checkpoint.read_bytes()
    digest = sha256(raw).hexdigest()
    state = pickle.loads(raw)
    size = len(raw)
    del raw
    assert state['ring'] == 'arb' and state['prec'] == 512
    assert (state['A'], state['B']) == ('2', '3')
    maximum = max(state['f'])
    selected = {maximum, maximum - 1, 140, 160}
    saved = {key: {str(n): value for n, value in state[key].items() if n in selected}
             for key in ('f', 'g')}
    (TARGET / 'verification/selected_packed_coefficients.json').write_text(
        json.dumps(dict(checkpoint_sha256=digest, delta='2/3', precision_bits=512, **saved)) + '\n')
    log10 = arb(10).log()
    result = {}
    for kind in ('f', 'g'):
        rows = []
        maxrel, maxnormrel = arb(0), arb(0)
        maxlocation, maxnormlocation = None, None
        uncertain_zeros = []
        count = 0
        all_radius_bounds = True
        for n, columns in sorted(state[kind].items()):
            order = []
            lognorms = []
            for q, packed in enumerate(columns):
                row, rel, normrel, lnorm = column(packed, log10)
                count += len(packed)
                order.append(row)
                lognorms.append(lnorm)
                all_radius_bounds = all_radius_bounds and rel is not None and normrel is not None and bool(rel < arb('1e-70')) and bool(normrel < arb('1e-70'))
                if row['uncertain_zero']:
                    uncertain_zeros.append([n, q])
                if rel is not None and rel > maxrel:
                    maxrel, maxlocation = rel, [n, q]
                if normrel is not None and normrel > maxnormrel:
                    maxnormrel, maxnormlocation = normrel, [n, q]
            summary = dict(n=n, columns=order)
            if n in selected and lognorms[0] is not None:
                factorial_deltas = [(arb(math.factorial(q)).log() / log10 + l - lognorms[0], q)
                                    for q, l in enumerate(lognorms) if q > 0 and l is not None]
                if factorial_deltas:
                    winner, q = max(factorial_deltas, key=lambda x: float(x[0].mid()))
                    summary['max_nonconstant_factorial_log10_ratio'] = text(winner)
                    summary['max_nonconstant_factorial_column'] = q
                    summary['maximizer_certified'] = all(bool(winner > other) for other, other_q in factorial_deltas if other_q != q)
            rows.append(summary)
        result[kind] = dict(coefficient_count=count, all_column_relative_radii_below_1e_70=all_radius_bounds, uncertain_zero_columns=uncertain_zeros,
                            maximum_scale_relative_radius=text(maxrel),
                            maximum_scale_location=maxlocation,
                            maximum_wiener_relative_radius=text(maxnormrel),
                            maximum_wiener_location=maxnormlocation,
                            all_maximum_scale_relative_radii_below_1e_60=bool(maxrel < arb('1e-60')),
                            all_wiener_relative_radii_below_1e_60=bool(maxnormrel < arb('1e-60')),
                            orders=rows)
    output = dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                  elapsed_seconds=time.monotonic()-start, checkpoint=str(checkpoint),
                  checkpoint_sha256=digest, checkpoint_bytes=size, maximum_order=maximum,
                  source_hashes=hashes, code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                  arithmetic='Independent exact dyadic reconstruction; 640-bit Arb norm/error enclosures',
                  scope='Precision of stored balls; conditional on coefficient enclosure correctness',
                  synthetic_cases=synthetic_rows, actual_checkpoint=result)
    (TARGET / 'verification/checks.json').write_text(json.dumps(output, indent=2, allow_nan=False) + '\n')
    brief = {k: v for k, v in output.items() if k not in ('actual_checkpoint', 'synthetic_cases')}
    brief['actual_checkpoint'] = {k: {kk: vv for kk, vv in v.items() if kk != 'orders'} for k, v in result.items()}
    brief['selected_order_profiles'] = {k: [{kk: vv for kk, vv in row.items() if kk != 'columns'}
                                           for row in v['orders'] if row['n'] in selected]
                                        for k, v in result.items()}
    brief['synthetic_reported_radius'] = {x['case']: x['observed']['rad_over_max'] for x in synthetic_rows}
    print(json.dumps(brief, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()

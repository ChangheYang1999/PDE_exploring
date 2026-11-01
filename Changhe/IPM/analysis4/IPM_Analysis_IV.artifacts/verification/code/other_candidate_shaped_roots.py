"""Independent all-index response and radius certificates for the other roots."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from fractions import Fraction as F
import argparse
import json
import sys
import time
import traceback
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
from gmpy2 import mpq
from flint import arb, ctx
from candidate_shaped_response import CandidateResponse, cover, pack, unpack
from pure_cartesian_ball import ball, refine_root
from general_rational_majorant import RationalMajorant
from general_component_radius import stringify


ROOT = Path('research/163_other_candidate_shaped_roots')


def one(index):
    start = time.monotonic()
    out = ROOT/'verification'
    source = Path('research/156_candidate_shaped_compatibility/verification/polynomial.json')
    roots = Path('research/156_candidate_shaped_compatibility/verification/checks.json')
    data, rootdata = json.loads(source.read_text()), json.loads(roots.read_text())
    b, interval = refine_root(data['primitive_coefficients_ascending'],
                              rootdata['roots'][index-1]['interval'], 832)
    response = CandidateResponse(b, data['fixed_normalized_coefficients'])
    finite = []
    for k in range(1, 53):
        value = response.full(k)
        assert not value.contains(0), ('finite_zero', k, str(value))
        if k >= 46:
            compact = response.dense(ball(mpq(1, 4*k-2)))
            assert compact is not None and compact.overlaps(value), ('full_dense', k)
        finite.append(dict(k=k, sigma=value.str(65, radius=True),
                           exact_dyadic=pack(value)))
        if k % 10 == 0:
            print(json.dumps(dict(root=index, stage='finite', k=k,
                                  actual_elapsed_s=time.monotonic()-start)), flush=True)
    limit = response.dense(arb(0))
    assert not limit.contains(0)
    for t in [mpq(0), mpq(1, 182), mpq(1, 256)]:
        dense, sparse = response.dense(ball(t)), response.compact(ball(t))
        assert dense is not None and sparse is not None and dense.overlaps(sparse)
    values = [unpack(v['exact_dyadic']) for v in finite] + [unpack(pack(limit))]
    least = min(abs(m)-r for m, r in values)
    assert least > 0
    s = F(1)
    while s >= least/4:
        s /= 2
    assert all(abs(m)-r > s for m, r in values)
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
                  root_index=index, arithmetic_bits=ctx.prec, root_interval=interval,
                  root_ball=b.str(65, radius=True), finite=finite,
                  sigma_infinity=limit.str(65, radius=True),
                  sigma_infinity_exact_dyadic=pack(limit), lower_bound=str(s),
                  finite_minimum_lower_bound=str(least), starting_tail_index=46,
                  full_dense_overlap_indices=list(range(46, 53)),
                  sparse_dense_overlap_count=3, all_finite_checks_pass=True,
                  source_sha256=sha256(source.read_bytes()).hexdigest(),
                  root_source_sha256=sha256(roots.read_bytes()).hexdigest(),
                  actual_elapsed_s=time.monotonic()-start)
    destination = out/f'root{index}_checks.json'
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(root=index, stage='finite_complete',
                          lower_bound=str(s), limit=str(limit))), flush=True)
    covered = cover(response, mpq(str(s)), out/f'root{index}_coverage.json')
    result['coverage'] = {k: v for k, v in covered.items() if k != 'nodes'}
    result['all_index_lower_bound_proved'] = True
    lower, upper = map(F, interval)
    norm_upper = 1 + max(abs(lower), abs(upper)) + sum(
        abs(F(value)) for mode, value in data['fixed_normalized_coefficients'].items()
        if mode != '1')
    a = F((norm_upper*1000).__floor__()+1, 1000)
    assert norm_upper < a
    majorant = RationalMajorant(2, 9, 20, a, s)
    box = [2*v for v in majorant.Y0]
    q = 1
    while any(v >= b for v, b in zip(majorant.transformed(F(1, 2**q), box), box)):
        q *= 2
    lo, hi = q//2, q
    while hi-lo > 1:
        mid = (hi+lo)//2
        if all(v < b for v, b in zip(majorant.transformed(F(1, 2**mid), box), box)):
            hi = mid
        else:
            lo = mid
    q = hi
    image = majorant.transformed(F(1, 2**q), box)
    previous = majorant.transformed(F(1, 2**(q-1)), box)
    assert all(v < b for v, b in zip(image, box))
    assert any(v >= b for v, b in zip(previous, box))
    original_amplitude = F(data['original_amplitude'])
    assert original_amplitude**9 < 2**38
    radius = dict(a=a, s=s, exact_leading_norm_upper=norm_upper,
                  kappa=majorant.kappa, L=majorant.L, constant=majorant.constant,
                  J=majorant.J, Y0=majorant.Y0, box=box, image=image,
                  previous_image=previous,
                  maximum_ratio=max(v/b for v, b in zip(image, box)),
                  previous_maximum_ratio=max(v/b for v, b in zip(previous, box)),
                  z_dyadic_exponent=q, radius_dyadic_exponent=F(9*q, 4),
                  restored_amplitude_radius_upper_exponent=F(9*q+38, 4),
                  restored_amplitude_sufficient_integer_exponent=(9*q+38)//4+1,
                  original_amplitude=original_amplitude)
    (out/f'root{index}_radius.json').write_text(json.dumps(stringify(radius), indent=2)+'\n')
    result['radius_summary'] = {k: stringify(v) for k, v in radius.items()
                               if k in ['a', 's', 'maximum_ratio', 'z_dyadic_exponent',
                                        'radius_dyadic_exponent',
                                        'restored_amplitude_sufficient_integer_exponent']}
    result['checked_at_utc'] = datetime.now(timezone.utc).isoformat(timespec='seconds')
    result['actual_elapsed_s'] = time.monotonic()-start
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(root=index, all_index_lower_bound_proved=True,
                          radius=result['radius_summary'],
                          coverage=result['coverage'],
                          actual_elapsed_s=result['actual_elapsed_s'])), flush=True)
    return dict(root_index=index, all_index_lower_bound_proved=True,
                radius=result['radius_summary'], actual_elapsed_s=result['actual_elapsed_s'])


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--roots', default='2,4,1,5,6,7')
    args = parser.parse_args()
    ctx.prec = 768
    start = time.monotonic()
    results = []
    for index in map(int, args.roots.split(',')):
        try:
            results.append(one(index))
        except Exception as exc:
            failure = dict(root_index=index,
                           checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
                           error_type=type(exc).__name__, error=str(exc),
                           frames=[dict(file=Path(v.filename).name, line=v.lineno)
                                   for v in traceback.extract_tb(exc.__traceback__)])
            (ROOT/f'verification/root{index}_FAILURE.json').write_text(
                json.dumps(failure, indent=2)+'\n')
            print(json.dumps(failure), flush=True)
            results.append(dict(root_index=index, all_index_lower_bound_proved=False,
                                error_type=type(exc).__name__, error=str(exc)))
        (ROOT/'verification/progress.json').write_text(json.dumps(dict(
            checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
            roots=results, actual_elapsed_s=time.monotonic()-start), indent=2)+'\n')
    for name in ['other_candidate_shaped_roots.py', 'candidate_shaped_response.py',
                 'pure_cartesian_ball.py', 'compact_response_bounds.py',
                 'general_rational_majorant.py', 'general_component_radius.py']:
        (ROOT/'sources'/name).write_bytes(Path('code', name).read_bytes())
    files = {str(p.relative_to(ROOT)): dict(bytes=p.stat().st_size,
             sha256=sha256(p.read_bytes()).hexdigest()) for p in ROOT.rglob('*')
             if p.is_file() and p.name != 'MANIFEST.json' and p.suffix != '.log'}
    (ROOT/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files), indent=2)+'\n')
    print(json.dumps(dict(complete=True, roots=results,
                          actual_elapsed_s=time.monotonic()-start)), flush=True)


if __name__ == '__main__':
    run()

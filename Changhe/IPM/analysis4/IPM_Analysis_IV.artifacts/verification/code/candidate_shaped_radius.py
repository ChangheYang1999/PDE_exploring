"""Exact radius and independent majorant-map comparison for Candidate-shaped root3."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from hashlib import sha256
import ast
import json
import sys
import time
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
from general_rational_majorant import RationalMajorant
from general_component_radius import stringify


def main():
    start = time.monotonic()
    root = Path('research/158_candidate_shaped_response')
    source = Path('../a4-lead/code/tuned/tq_boxh.py')
    text = source.read_text()
    # Load definitions without invoking the peer's command-line driver.
    tree = ast.parse(text)
    tree.body = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef))]
    namespace = dict(Q=9, H=2, B=4)
    exec(compile(tree, 'peer_tq_boxh.py', 'exec'), namespace)
    comparisons = []
    for B, a, s in [(4, F(133, 125), F(1, 2**29)),
                    (20, F(1139, 1000), F(1, 2**28))]:
        namespace['B'] = B
        phi, kappa = namespace['make_phi_h'](a, s)
        m = RationalMajorant(2, 9, B, a, s)
        assert kappa == m.kappa
        zero = [F(0)] * 10
        constant = phi(F(0), zero)
        J = [[F(0)] * 10 for _ in range(10)]
        for j in range(10):
            e = zero.copy()
            e[j] = F(1)
            column = phi(F(0), e)
            for i in range(10):
                J[i][j] = column[i] - constant[i]
        assert constant == m.constant and J == m.J
        cases = 0
        for z in [F(0), F(1, 128), F(1, 2**240)]:
            for Y in [zero, [F(j+2, j+1) for j in range(10)],
                      [2*v for v in m.Y0]]:
                assert phi(z, Y) == m.phi(z, Y)
                cases += 1
        comparisons.append(dict(B=B, a=a, s=s, kappa=kappa,
                                constant=constant, J=J, map_test_vectors=cases,
                                all_equal=True))

    finite_path = root/'verification/root3_checks.json'
    polynomial_path = Path('research/156_candidate_shaped_compatibility/verification/polynomial.json')
    data = json.loads(finite_path.read_text())
    polynomial = json.loads(polynomial_path.read_text())
    assert data['all_index_lower_bound_proved']
    a, s = F(1139, 1000), F(data['lower_bound'])
    lower, upper = map(F, data['root_interval'])
    assert lower > 0
    rest = sum(abs(F(v)) for k, v in polynomial['fixed_normalized_coefficients'].items() if k != '1')
    norm_upper = 1 + upper + rest
    assert norm_upper < a
    m = RationalMajorant(2, 9, 20, a, s)
    box = [2*v for v in m.Y0]
    q = 1
    while any(v >= b for v, b in zip(m.transformed(F(1, 2**q), box), box)):
        q *= 2
    lo, hi = q//2, q
    while hi-lo > 1:
        mid = (hi+lo)//2
        if all(v < b for v, b in zip(m.transformed(F(1, 2**mid), box), box)):
            hi = mid
        else:
            lo = mid
    q = hi
    image = m.transformed(F(1, 2**q), box)
    previous = m.transformed(F(1, 2**(q-1)), box)
    assert all(v < b for v, b in zip(image, box))
    assert any(v >= b for v, b in zip(previous, box))
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
                  all_checks_pass=True, root_index=3, a=a, s=s,
                  exact_leading_norm_upper=norm_upper,
                  kappa=m.kappa, L=m.L, constant=m.constant, J=m.J,
                  Y0=m.Y0, box=box, image=image, previous_image=previous,
                  maximum_ratio=max(v/b for v,b in zip(image,box)),
                  previous_maximum_ratio=max(v/b for v,b in zip(previous,box)),
                  z_dyadic_exponent=q, radius_dyadic_exponent=F(9*q,4),
                  original_amplitude=polynomial['original_amplitude'],
                  map_comparisons=comparisons,
                  source_checks_sha256=sha256(finite_path.read_bytes()).hexdigest(),
                  peer_source_sha256=sha256(text.encode()).hexdigest(),
                  actual_elapsed_s=time.monotonic()-start)
    (root/'verification/root3_radius.json').write_text(json.dumps(stringify(result), indent=2)+'\n')
    (root/'sources/peer_tq_boxh.py').write_text(text)
    for name in ['candidate_shaped_radius.py', 'general_rational_majorant.py', 'general_component_radius.py']:
        (root/'sources'/name).write_bytes(Path('code', name).read_bytes())
    print(json.dumps({k:stringify(result[k]) for k in ['all_checks_pass','z_dyadic_exponent',
                      'radius_dyadic_exponent','maximum_ratio','actual_elapsed_s']}), flush=True)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        import traceback
        failure = dict(error_type=type(exc).__name__, error=str(exc),
                       frames=[dict(file=Path(f.filename).name, line=f.lineno)
                               for f in traceback.extract_tb(exc.__traceback__)])
        Path('research/158_candidate_shaped_response/verification/radius_FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n')
        print(json.dumps(failure), flush=True)
        raise SystemExit(1)

"""Exact controlled test of midpoint accuracy in Arb polynomial products."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
from hashlib import sha256
from random import Random
import json
import time
import sys
sys.dont_write_bytecode = True
from flint import arb, arb_poly, ctx


def rational(x):
    m, e = x.man_exp()
    return F(int(m))*F(2)**int(e)


def pack(x):
    m, e = x.mid().man_exp()
    r, re = x.rad().man_exp()
    return [str(m), int(e), str(r), int(re)]


def main():
    start = time.monotonic()
    ctx.prec = 512
    rng = Random(417)
    u = [rng.randrange(-2**30, 2**30) for _ in range(16)]
    v = [rng.randrange(-2**30, 2**30) for _ in range(16)]
    exact = [sum(u[i]*v[k-i] for i in range(16) if 0 <= k-i < 16)
             for k in range(31)]
    a = [arb(i)/2**30 for i in u]
    b = [arb(i)/2**30 for i in v]
    control = arb_poly(a)*arb_poly(b)
    assert all(control[k].is_exact() and rational(control[k]) == F(x, 2**60)
               for k, x in enumerate(exact))
    rows = []
    for q in [8, 20, 80]:
        radius = arb(2)**(-q)
        product = arb_poly([arb(x, radius) for x in a])*arb_poly([arb(x, radius) for x in b])
        errors = []
        for k, numerator in enumerate(exact):
            target = F(numerator, 2**60)
            midpoint, rad = rational(product[k].mid()), rational(product[k].rad())
            err = abs(midpoint-target)
            assert err <= rad
            errors.append(err)
        if q < 80:
            assert max(errors) > F(1, 2**80)
        rows.append(dict(input_radius_power=q,
                         all_exact_products_enclosed=True,
                         nonzero_midpoint_errors=sum(x != 0 for x in errors),
                         maximum_midpoint_error=str(max(errors)),
                         error_location=errors.index(max(errors)),
                         output_exact_dyadic=[pack(product[k]) for k in range(31)]))
    root = Path('research/160_interval_midpoint_precision')
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
                  precision_context_bits=512, seed=417, input_denominator=2**30,
                  first_integer_coefficients=u, second_integer_coefficients=v,
                  exact_product_numerators=exact, exact_product_denominator=2**60,
                  zero_radius_product_exact=True, rows=rows,
                  actual_elapsed_s=time.monotonic()-start,
                  scope='Finite controlled polynomial test; no estimate of individual IPM coefficients.')
    (root/'verification/checks.json').write_text(json.dumps(result, indent=2)+'\n')
    (root/'sources/interval_midpoint_precision.py').write_bytes(Path(__file__).read_bytes())
    files = {str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest())
             for p in root.rglob('*') if p.is_file() and p.name != 'MANIFEST.json'}
    (root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
    print(json.dumps(dict(checked_at_utc=result['checked_at_utc'],
                         actual_elapsed_s=result['actual_elapsed_s'],
                         rows=[{k:v for k,v in row.items() if k != 'output_exact_dyadic'} for row in rows])),flush=True)


if __name__ == '__main__':
    main()

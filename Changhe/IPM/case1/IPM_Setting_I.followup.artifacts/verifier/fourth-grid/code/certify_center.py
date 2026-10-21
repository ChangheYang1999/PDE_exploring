"""Two separate exact whole-plane center formulas for a frozen input table."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import importlib.util
import json
import sys
import time
import numpy as np
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / 'exact-data/code'))
from nodal_input import export, load


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('--tag')
    args = parser.parse_args()
    source = Path(args.source).resolve()
    assert source.is_relative_to(ROOT.parent.parent)
    tag = args.tag or source.stem
    assert tag.replace('_', '').replace('-', '').isalnum()
    outpath = ROOT / 'verification' / (tag + '_center_certificate.json')
    assert not outpath.exists(), 'Keep completed certificates immutable.'
    first_path = ROOT.parent / 'center-moment/code/certify.py'
    second_path = ROOT.parent / 'center-moment-trapezoid/code/certify.py'
    first = module('primary_center_formula', first_path)
    second = module('periodic_center_formula', second_path)
    ctx.prec = 256
    start = datetime.now(timezone.utc).isoformat()
    ticks = time.monotonic()
    exact = ROOT / 'data' / (tag + '_exact.json')
    export(source, exact)
    meta, table, params, exact_sha = load(exact)
    assert np.all(table[0] == 1)
    L, cl, beta = [first.binary(params[k]) for k in ('L', 'c_l', 'beta')]
    assert L > 0 and cl > 1 and abs(beta) < 1
    co = first.tensor_coefficients(table)
    c64 = first.moment(co, L, cl, beta, 64)
    c96 = first.moment(co, L, cl, beta, 96)
    assert c64.is_finite() and c96.is_finite()
    assert (c64 - c96).contains(0)
    print('BESSEL_CERTIFIED', c96.str(50), flush=True)
    radial_coeffs = second.integrated_coefficients(table)
    periodic, detail = second.enclose(radial_coeffs, L, cl, beta, 512)
    assert periodic.is_finite() and (periodic - c96).contains(0)
    d1 = 3 * cl - 1 - c96
    d2 = 3 * cl - 1 - periodic
    deps = [Path(__file__), ROOT / 'PROOF.md', first_path, second_path,
            ROOT.parent / 'center-moment/PROOF.md',
            ROOT.parent / 'center-moment-trapezoid/PROOF.md',
            ROOT.parent / 'inner-cutoff/code/hessian.py',
            ROOT.parent / 'exact-data/code/nodal_input.py', source, exact]
    record = {
        'date_start': start, 'date_end': datetime.now(timezone.utc).isoformat(),
        'precision_bits': ctx.prec, 'source': str(source.relative_to(ROOT.parent.parent)),
        'source_md5': hashlib.md5(source.read_bytes()).hexdigest(),
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'exact_json': str(exact.relative_to(ROOT)), 'exact_json_sha256': exact_sha,
        'N': meta['N'], 'M': meta['M'], 'c_l': params['c_l'],
        'c64': c64.str(50), 'c96': c96.str(50), 'periodic': detail,
        'certificates_overlap': True,
        'first_self_consistency_ball': d1.str(50),
        'second_self_consistency_ball': d2.str(50),
        'self_consistency_contains_zero': d1.contains(0) or d2.contains(0),
        'c_midpoint_float': float(c96.mid()),
        'self_consistency_midpoint_float': float(d1.mid()),
        'seconds': time.monotonic() - ticks,
        'scope': 'Exact represented field at ideal nodes; each formula has its own truncation bound. Overlap is a consistency check. This certifies only the canonical center moment, not a full residual or a profile.',
        'dependencies': [{'file': str(p.relative_to(ROOT.parent.parent)),
                          'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in deps],
        'complete': True}
    outpath.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record, indent=2), flush=True)


if __name__ == '__main__':
    main()

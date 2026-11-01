"""Independent Cartesian checks of packed logarithmic products and exact prefix."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import importlib.util
import json
import random
import sys
import time
sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)
from laurent_log_audit import Q, L, parse


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def cols_to_laurent(cols, exponent, even):
    data = {}
    for power, col in enumerate(cols):
        for k, value in enumerate(col):
            mode = 2*k if even else 2*k+1
            if not mode or not value:
                continue
            data.setdefault(str(mode), [Q(0)] * len(cols))[power] += value
    return parse(exponent, data)


def compare_exact_columns(columns, modes, even):
    modes = {int(m): [Q(v) for v in vals] for m, vals in modes.items()}
    power_count = max(len(columns), max(map(len, modes.values()), default=0))
    slot_count = max(max(map(len, columns), default=0),
                     max(((m//2+1) if even else ((m+1)//2) for m in modes), default=0))
    count = 0
    for power in range(power_count):
        for k in range(slot_count):
            mode = 2*k if even else 2*k+1
            actual = columns[power][k] if power < len(columns) and k < len(columns[power]) else Q(0)
            expected = modes.get(mode, [])
            value = expected[power] if power < len(expected) else Q(0)
            assert actual == value, (power, mode, str(actual), str(value))
            count += 1
    return count


def main():
    start = time.monotonic()
    target = Path('research/33_packed_log_products')
    (target/'sources').mkdir(parents=True, exist_ok=True)
    (target/'verification').mkdir(exist_ok=True)
    hashes = {}
    for filename in ['ffcore.py', 'logff.py']:
        raw = (Path('../a4-num/code')/filename).read_bytes()
        (target/'sources'/filename).write_bytes(raw)
        hashes[filename] = sha256(raw).hexdigest()
    load_module('ffcore', target/'sources/ffcore.py')
    mod = load_module('audited_packed_logff', target/'sources/logff.py')
    ring = mod.make_ring('fmpq', 512)
    obj = mod.LogFarField(ring, 4, 9, ['1'])
    rng = random.Random(731927)
    random_rows = []
    for trial in range(80):
        delta = Q(rng.randrange(1, 10), 11)
        i, j = rng.randrange(1, 20), rng.randrange(1, 20)
        P, p = 2-i*delta, 1-j*delta
        def columns(even):
            out = []
            for _ in range(rng.randrange(1, 6)):
                out.append([Q(rng.randrange(-9, 10), rng.randrange(1, 10))
                            for _ in range(rng.randrange(1, 10))])
                if even:
                    out[-1][0] = Q(0)
            return out
        Gi, Fj = columns(True), columns(False)
        Gt = mod.col_add(ring, mod.col_scale(ring, Gi, P), mod.col_T(ring, Gi))
        Ft = mod.col_add(ring, mod.col_scale(ring, Fj, p), mod.col_T(ring, Fj))
        got = cols_to_laurent(obj._block_products(Gt, Fj, Gi, Ft), P+p-2, False)
        gl, fl = cols_to_laurent(Gi, P, True), cols_to_laurent(Fj, p, False)
        expected = gl.X()*fl.Y()-gl.Y()*fl.X()
        assert (got-expected).zero(), ('random Cartesian product', trial)
        random_rows.append(dict(trial=trial, delta=str(delta), i=i, j=j,
                                stream_column_lengths=list(map(len, Gi)),
                                density_column_lengths=list(map(len, Fj)),
                                cartesian_identity=True))
    print('80 exact random Cartesian products passed', flush=True)
    source = Path('research/21_logarithmic_data_audit/sources/lead_exact_log_data.json')
    raw = source.read_bytes()
    exact = json.loads(raw)
    counts = {'density': 0, 'stream': 0}
    verified = []
    for n in range(1, 74):
        if n > 1:
            assert obj.step_fast() == n
        counts['density'] += compare_exact_columns(obj.f[n], exact['density'][str(n)], False)
        counts['stream'] += compare_exact_columns(obj.g[n], exact['stream'][str(n)], True)
        verified.append(n)
        result = dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                      source_sha256=hashes, audit_code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                      exact_reference=str(source), exact_reference_sha256=sha256(raw).hexdigest(),
                      random_seed=731927, random_cartesian_cases=random_rows,
                      prefix_parameter='delta=4/9, f1=sin(theta), total resonant constant zero',
                      exact_prefix_verified_through=n, exact_scalar_comparison_counts=counts,
                      actual_elapsed_seconds=time.monotonic()-start)
        (target/'verification/checks.json').write_text(json.dumps(result, indent=2)+'\n')
        if n % 10 == 0 or n == 73:
            print(json.dumps(dict(n=n, counts=counts, elapsed_s=time.monotonic()-start)), flush=True)


if __name__ == '__main__':
    main()

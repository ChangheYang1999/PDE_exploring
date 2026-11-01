"""Counterexamples for premature float conversion in logarithmic statistics."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import importlib.util
import json
import math
import sys
sys.dont_write_bytecode = True


def clean(value):
    if isinstance(value, float) and not math.isfinite(value):
        return str(value)
    if isinstance(value, dict):
        return {k: clean(v) for k, v in value.items()}
    if isinstance(value, list):
        return [clean(v) for v in value]
    return value


def main():
    target = Path('research/29_log_statistics')
    hashes = {}
    for name in ('logff.py', 'ffcore.py'):
        source = Path('../a4-num/code') / name
        raw = source.read_bytes()
        (target / 'sources' / (name + '.txt')).write_bytes(raw)
        hashes[name] = sha256(raw).hexdigest()
    spec = importlib.util.spec_from_file_location('audited_logff', '../a4-num/code/logff.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    ring = mod.make_ring('arb', 512)
    obj = mod.LogFarField(ring, 4, 9, ['1'])
    cases = [
        ('ordinary_control', [[mod.arb(1)], [mod.arb('1e-40', '1e-45')]]),
        ('tiny_nonzero_column', [[mod.arb(1)], [mod.arb('1e-400', '1e-405')]]),
        ('all_columns_tiny', [[mod.arb('1e-400', '1e-405')]])]
    rows = []
    for name, columns in cases:
        obj.f[2] = columns
        exact_log_norms = [str(sum((abs(x) for x in col), mod.arb(0)).log() / mod.arb(10).log()) for col in columns]
        exact_rel_rads = [str(max((x.rad() for x in col)) / max((abs(x).mid() for x in col))) for col in columns]
        try:
            obj._stats(2)
            observed = clean(obj.stats[2])
        except Exception as err:
            observed = {'exception': type(err).__name__, 'message': str(err)}
        rows.append(dict(case=name, columns=[[str(x) for x in col] for col in columns],
                         certified_log_norms=exact_log_norms,
                         certified_column_rad_over_max=exact_rel_rads,
                         observed=observed))
    result = dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                  source_hashes=hashes,
                  code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                  method='Three synthetic coefficient states, not a claimed IPM checkpoint failure',
                  arithmetic='Arb 512-bit input and exact source code execution', cases=rows)
    (target / 'verification/counterexamples.json').write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
    print(json.dumps(rows, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()

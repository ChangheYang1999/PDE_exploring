"""Use the actual binary64 leading amplitude for the floating twin comparison."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
from hashlib import sha256
import gzip
import json
import sys
import time
sys.dont_write_bytecode = True
from flint import arb, fmpq, ctx


def run():
    start = time.monotonic()
    ctx.prec = 512
    root = Path('research/165_shared_float_error')
    text = lambda x: x.str(50, radius=True)
    path = root/'sources/log23_full_float_pert.jsonl.gz'
    lines = gzip.decompress(path.read_bytes()).decode().splitlines()
    header = json.loads(lines[0])
    assert header['ring'] == 'float'
    decimal = header['f1'][0]
    amplitude = Fraction.from_float(float(decimal))
    assert amplitude == Fraction(562949953477607, 562949953421312)
    conversion = Path('../a4-num/code/ffcore.py').read_text()
    scalar = conversion.split('class RingF:', 1)[1].split('    zero =', 1)[0]
    assert 'return float(x)' in scalar
    init = Path('../a4-num/code/logff.py').read_text()
    assert 'self.f = {1: [[R.scalar(x) for x in f1]]}' in init
    (root/'sources/binary_input_conversion.txt').write_text(
        'Source: ../a4-num/code/ffcore.py, RingF.scalar\n'
        + scalar.strip()+'\n\nSource: ../a4-num/code/logff.py, LogFarField.__init__\n'
        + 'self.f = {1: [[R.scalar(x) for x in f1]]}\n')
    data = json.loads((root/'verification/checks.json').read_text())
    logratio = (arb(fmpq(str(amplitude)))/arb(decimal)).log()/arb(10).log()
    rows = []
    for row in data['rows']:
        n = row['n']
        correction = n*logratio
        output = dict(n=n, decimal_to_binary_log_correction=text(correction))
        for label in ['M', 'N']:
            if label in row:
                old = arb(row[label]['normalized_twin_difference_log10'])
                value = old-correction
                output[label] = dict(decimal_normalized_difference=text(old),
                                     actual_binary_normalized_difference=text(value))
        rows.append(output)
    final = next(row for row in rows if row['n'] == 300)
    for label in ['M', 'N']:
        assert abs(arb(final[label]['actual_binary_normalized_difference'])) < arb('0.000001')
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
        all_checks_pass=True, amplitude_decimal=decimal, amplitude_exact_binary=str(amplitude),
        correction_per_order=text(logratio), rows=rows,
        actual_elapsed_s=time.monotonic()-start,
        source_conversion_sha256=sha256(conversion.encode()).hexdigest(),
        source_initializer_sha256=sha256(init.encode()).hexdigest(),
        previous_check_sha256=sha256((root/'verification/checks.json').read_bytes()).hexdigest(),
        scope='Corrected normalization only; the six-decade counterexample and exact norm errors are unchanged.')
    (root/'verification/actual_binary_normalization.json').write_text(json.dumps(result, indent=2)+'\n')
    (root/'sources/shared_float_binary_normalization.py').write_bytes(Path(__file__).read_bytes())
    print(json.dumps(dict(all_checks_pass=True, correction_per_order=text(logratio),
                         order300=final, actual_elapsed_s=result['actual_elapsed_s'])), flush=True)


if __name__ == '__main__':
    try:
        run()
    except Exception as exc:
        import traceback
        failure = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
            error_type=type(exc).__name__, error=str(exc),
            frames=[dict(file=Path(v.filename).name, line=v.lineno)
                    for v in traceback.extract_tb(exc.__traceback__)])
        Path('research/165_shared_float_error/verification/binary_normalization_FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n')
        print(json.dumps(failure), flush=True)
        raise SystemExit(1)

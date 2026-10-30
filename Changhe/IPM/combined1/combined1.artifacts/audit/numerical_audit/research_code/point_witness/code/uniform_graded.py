"""All-box graded point obstruction from an independently checked point."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from fractions import Fraction
import json
import time
from flint import arb, ctx, fmpq as Q

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/point_witness'
NAME = 'C1-N1-007-d2w-j7-e2bal'

def ar(q):
    q = Q(q)
    return arb(q.numerator) / q.denominator

def decimal(s):
    f = Fraction(s)
    return ar(Q(f.numerator, f.denominator))

def digest(p):
    return sha256(p.read_bytes()).hexdigest()

def run():
    start = time.monotonic()
    ctx.prec = 1024
    path = ROOT / f'research/candidate_audits/verification/{NAME}_point.json'
    canonical = ROOT / f'research/candidate_audits/data/{NAME}/canonical.json'
    target = BASE / 'verification/candidate007_uniform_graded.json'
    assert not target.exists()
    d = json.loads(path.read_text())
    assert d['canonical_sha256'] == digest(canonical)
    f = {key: arb(value) for key, value in d['fields'].items()}
    F, V, D = abs(f['residual']), f['velocity_norm'], f['gradient_norm']
    # Exact cubic maximum: derivative is 1/2-14124v^2.
    v2 = Q(1, 28248)
    assert Q(1, 2) - 14124 * v2 == 0
    nmax = ar(Q(50, 651)) / arb(28248).sqrt()
    numax = ar(Q(25, 217))
    b0, b1 = nmax / (4 * arb.pi()).sqrt(), numax / (8 * arb.pi()).sqrt()
    bound = b1 * V + b0 * (1 + D) + b0 * b1
    gap = F - bound
    assert gap > 0
    cases = [
        ('FW-T-T4L2-sharp-v1', Q(1, 7744), ar(Q(147, 200000))),
        ('FW-T-T4L2-sharpw-v1', Q(1, 5184), ar(Q(1351, 1000000))),
        ('FW-T-TB-graded-v1-box-i', Q(5, 262144),
         (decimal('2.022e-4')**2 + 2 * decimal('3.347e-7')**2 + decimal('1.899e-8')**2).sqrt()),
        ('FW-T-TB-graded-v1-box-ii', Q(1, 50000),
         (ar(Q(1, 5000))**2 + 2 * ar(Q(1, 3000000))**2 + ar(Q(1, 50000000))**2).sqrt()),
        ('FW-T-TB-gradedL2-v1-instance', Q(5, 262144),
         (decimal('2.023e-4')**2 + 2 * decimal('3.32e-7')**2 + decimal('1.84e-8')**2).sqrt()),
    ]
    rows = []
    for name, s, radius in cases:
        C0 = 1 / (4 * arb.pi() * ar(1 + s)).sqrt()
        C1 = 1 / (8 * arb.pi() * ar(s * (1 + s))).sqrt()
        B, A = C1 * V + C0 * (1 + D), C0 * C1
        upper = radius * B + radius**2 * A
        difference = F - upper
        assert difference > 0
        rows.append({'framework': name, 's': str(s), 'H2s_radius_upper': radius.str(90),
                     'point_upper': upper.str(90), 'positive_gap': difference.str(90)})
    out = {'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'candidate': NAME,
           'point': d['point'], 'precision_bits': ctx.prec,
           'point_record_sha256': digest(path), 'canonical_sha256': digest(canonical),
           'code_sha256': digest(Path(__file__)), 'proof_sha256': digest(BASE/'PROOF_UNIFORM_GRADED.md'),
           'frozen_dependencies': {p.name: digest(p) for p in sorted((BASE/'peer_review/uniform_graded').iterdir())},
           'n_uniform_upper': nmax.str(90), 'nu_uniform_upper': numax.str(90),
           'C0n_uniform_upper': b0.str(90), 'C1n_uniform_upper': b1.str(90),
           'uniform_point_upper': bound.str(90), 'uniform_positive_gap': gap.str(90),
           'finite_boxes': rows, 'elapsed_seconds': time.monotonic()-start,
           'scope': 'All original graded and gradedL2 boxes with the stated positive top margin; fixed exact c and candidate. New comparison awaits peer.'}
    target.write_text(json.dumps(out, indent=2)+'\n')
    print('uniform gap', gap.str(40), flush=True)
    for row in rows:
        print(row['framework'], row['positive_gap'], flush=True)

if __name__ == '__main__':
    run()

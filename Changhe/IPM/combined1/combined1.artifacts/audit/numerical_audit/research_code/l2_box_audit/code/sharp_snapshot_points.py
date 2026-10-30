"""Independent rational interval check of T4-055's six point exclusions."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime, timezone
import json
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/l2_box_audit'
sys.path.insert(0, str(ROOT / 'research/graded_box_audit/code'))
from check import I, atan


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def parse(text):
    values = text.strip('[]').split('+/-')
    if len(values) == 1:
        return I(values[0].strip())
    center, radius = (Q(v.strip()) for v in values)
    return I(center-radius, center+radius)


def absolute(value):
    if value.a >= 0:
        return value
    if value.b <= 0:
        return -value
    return I(0, max(-value.a, value.b))


def overlap(left, right):
    return max(left.a, right.a) <= min(left.b, right.b)


def run():
    start = time.monotonic()
    peer_path = BASE/'peer_review/T4_sharp_numeric_results.json'
    peer = json.loads(peer_path.read_text())
    targets = {(r['framework'], r['candidate']): r for r in peer['point_exclusions']}
    pi = 16*atan(Q(1, 5), 80)-4*atan(Q(1, 239), 20)
    rows = []
    for label, s, radius in [('sharp', Q(1, 7744), Q(147, 200000)),
                             ('sharpw', Q(1, 5184), Q(1351, 1000000))]:
        framework = 'FW-T-T4L2-'+label+'-v1'
        C0 = 1/(4*pi*(1+s)).sqrt()
        C1 = 1/(8*pi*s*(1+s)).sqrt()
        for name in ['C1-N1-002-7branch-frf', 'C1-N1-003-8branch-frf', 'C1-N1-004-4branch-l2fw']:
            path = ROOT/f'research/candidate_audits/verification/{name}_point.json'
            data = json.loads(path.read_text())
            canonical = ROOT/f'research/candidate_audits/data/{name}/canonical.json'
            assert data['canonical_sha256'] == digest(canonical)
            f = {key: parse(data['fields'][key]) for key in ['residual', 'velocity_norm', 'gradient_norm']}
            upper = (C1*f['velocity_norm']+C0*(1+f['gradient_norm']))*radius+C0*C1*radius*radius
            gap = absolute(f['residual'])-upper
            assert gap.a > 0
            target = targets[framework, name]
            assert target['point'] == data['point']
            comparisons = {
                'upper': overlap(upper, parse(target['necessary_upper'])),
                'gap': overlap(gap, parse(target['positive_gap'])),
            }
            assert all(comparisons.values())
            rows.append({
                'framework': framework, 'candidate': name, 's': str(s), 'R': str(radius),
                'point': data['point'], 'canonical_sha256': digest(canonical),
                'point_record_sha256': digest(path), 'necessary_upper': upper.record(),
                'positive_gap': gap.record(), 'strictly_excludes_closed_ball': True,
                'T4_comparisons': comparisons,
            })
            print(framework, name, 'gap', float((gap.a+gap.b)/2), flush=True)
    result = {
        'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'method': 'Exact rational interval arithmetic, 70-decimal integer square roots and Machin pi enclosure; own Cartesian field inputs.',
        'proof_sha256': digest(BASE/'PROOF.md'), 'code_sha256': digest(Path(__file__)),
        'T4_result_sha256': digest(peer_path), 'rows': rows,
        'elapsed_seconds': time.monotonic()-start,
        'scope': 'Six pointwise necessary-condition exclusions at the specified fixed c; no sufficient background hypothesis is used.',
    }
    dest = BASE/'verification/sharp_snapshot_points.json'
    assert not dest.exists()
    dest.write_text(json.dumps(result, indent=2)+'\n')
    print('seconds', result['elapsed_seconds'], flush=True)


if __name__ == '__main__':
    run()

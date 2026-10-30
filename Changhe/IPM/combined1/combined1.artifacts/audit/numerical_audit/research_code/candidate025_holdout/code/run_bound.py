"""Record own executable source closure around each actual025 audit step."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from types import ModuleType
import importlib.util, json, sys, time
R = Path(__file__).resolve().parents[3]
B = R / 'research/candidate025_holdout'
CANDIDATE = 'C1-N1-025-combined-heldin1e16'
sha = lambda p: sha256(Path(p).read_bytes()).hexdigest()
now = lambda: datetime.now(timezone.utc).isoformat()
def save(p, data):
    with Path(p).open('x') as f:
        json.dump(data, f, indent=2)
        f.write('\n')
def closure(module):
    todo = [module] + list(sys.modules.values())
    seen, paths = set(), set()
    while todo:
        m = todo.pop()
        if not isinstance(m, ModuleType) or id(m) in seen:
            continue
        seen.add(id(m))
        path = getattr(m, '__file__', None)
        if not path:
            continue
        path = Path(path).resolve()
        if not path.is_relative_to(R) or path.suffix != '.py':
            continue
        paths.add(path)
        todo.extend(v for v in vars(m).values() if isinstance(v, ModuleType))
    return paths

def main():
    started = time.monotonic()
    label = sys.argv[1]
    records = {
        'shape': ('research/candidate025_holdout/code/check.py', 'research/candidate025_holdout/verification/result.json'),
        'point': ('research/generator_sector_audit/code/audit_candidate.py', f'research/generator_sector_audit/verification/{CANDIDATE}_direct.json'),
        'prefix': ('research/candidate025_prefix/code/check.py', 'research/candidate025_prefix/verification/result.json'),
        'weak': ('research/joint_scaled_factored_weak/code/check_candidates.py', f'research/joint_scaled_factored_weak/verification/{CANDIDATE}_n019_K01800.json'),
    }
    script, result = records[label]
    entry = R / script
    sys.path.insert(0, str(entry.parent))
    spec = importlib.util.spec_from_file_location('own_025_bound_' + label, entry)
    C = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(C)
    paths = closure(C)
    # The shape audit imports this own generator module inside main().
    paths |= {R / 'research/joint_scaled_factored_weak/code/fields_joint.py',
              B / 'PROOF.md', B / 'verification/PREPARE.json',
              B / 'verification/SNAPSHOT.json', Path(__file__).resolve()}
    paths |= set((R / 'research/candidate_audits/data' / CANDIDATE).iterdir())
    manifest = json.loads((B / 'source/MANIFEST_v01.json').read_text())
    paths.add(B / 'source/MANIFEST_v01.json')
    paths |= {R / rel for rel in manifest['files']}
    before = {str(p.relative_to(R)): sha(p) for p in sorted(paths)}
    index = 1
    while (B / f'verification/bound_{label}_v{index:02d}_start.json').exists():
        index += 1
    prefix = B / f'verification/bound_{label}_v{index:02d}'
    startp = Path(str(prefix) + '_start.json')
    save(startp, {'utc': now(), 'label': label, 'entry': script, 'sources': before,
                  'candidate': CANDIDATE, 'code_imported_before_major_arithmetic': True,
                  'foreign_implementation_executed': False})
    print(now(), 'BOUND_START', label, 'sources', len(before), flush=True)
    if label in ['shape', 'prefix']:
        C.main()
    elif label == 'point':
        C.run(CANDIDATE)
    else:
        C.run(CANDIDATE, [(19, 1800)], B / 'verification/result.json')
    assert closure(C).issubset(paths), [str(p) for p in closure(C) - paths]
    assert all(sha(R / rel) == h for rel, h in before.items())
    rp = R / result
    record = json.loads(rp.read_text())
    for rel, h in record.get('inputs', record.get('dependency_sha256', {})).items():
        assert sha(R / rel) == h, rel
    out = {'utc': now(), 'label': label, 'candidate': CANDIDATE,
           'start_sha256': sha(startp), 'result': result, 'result_sha256': sha(rp),
           'all_before_hashes_unchanged': True, 'source_count': len(before),
           'no_additional_own_executable_module_outside_bound_set': True,
           'elapsed_seconds': time.monotonic() - started,
           'verdict': 'CONFIRMED before/after own executable-source and frozen025 bindings; numerical status remains in the bound result'}
    save(Path(str(prefix) + '_result.json'), out)
    print(now(), 'BOUND_DONE', label, sha(Path(str(prefix) + '_result.json')), flush=True)
if __name__ == '__main__':
    main()

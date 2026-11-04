"""Extend completed, independently audited regional theorems; no field execution."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from datetime import datetime, timezone
import argparse, gzip, json, os, re, time
R = Path(__file__).resolve().parents[3]
C = R.parent
A = C / 'theory_audit'
B = R / 'research/background_progressive_union'
p = argparse.ArgumentParser()
p.add_argument('--base-sha256', required=True)
p.add_argument('--at-base-sha256', required=True)
p.add_argument('--max-inner', required=True, type=int)
p.add_argument('--version', required=True, type=int)
a = p.parse_args()
assert 55 <= a.max_inner <= 97 and 1 <= a.version <= 99
assert all(re.fullmatch('[0-9a-f]{64}', x) for x in (a.base_sha256, a.at_base_sha256))
assert os.sched_getaffinity(0) == {50} and os.getpriority(os.PRIO_PROCESS, 0) >= 19
assert all(os.environ.get(k) == '1' for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'))
START = datetime.now(timezone.utc)
TICK = time.monotonic()
N = 0
FILES = {}
CACHE = {}

def ck(value, label):
    global N
    N += 1
    assert value, label

def digest(path, fresh=False):
    path = Path(os.path.normpath(path))
    if fresh or path not in CACHE:
        h = sha256()
        with path.open('rb') as f:
            for block in iter(lambda: f.read(1048576), b''):
                h.update(block)
        CACHE[path] = h.hexdigest()
    return CACHE[path]

def bind(path, expected=None):
    path = Path(os.path.normpath(path))
    ck(path.resolve().is_relative_to(C), 'campaign input containment')
    h = digest(path)
    ck(expected is None or h == expected, 'input identity: ' + path.name)
    key = os.path.relpath(path, R)
    ck(key not in FILES or FILES[key] == h, 'consistent duplicate identity')
    FILES[key] = h
    return path

def load(path, expected=None):
    return json.loads(bind(path, expected).read_text())

def imports(base, files):
    ck(type(files) is dict and bool(files), 'nonempty binding map')
    for name, h in files.items():
        ck(not Path(name).is_absolute() and '\\' not in name, 'relative evidence path')
        bind(base / name, h)

def when(value):
    t = datetime.fromisoformat(value.replace('Z', '+00:00'))
    ck(t.tzinfo is not None and t.utcoffset().total_seconds() == 0, 'UTC evidence time')
    return t

source = dict(id='C2-N1-013', raw_sha256='a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a',
              canonical_sha256='2531d462643034e1083b40f5e60a6c4b0fa3ba84425cea3cadb68c767847fc33',
              fields_sha256='3d5f08e06859af2577f6e099374a8ce5e139a0b66280055ada847745943bf8cb',
              fixed_c_exact='4076476460239181/2251799813685248')
base_path = R / 'research/background_slabs_union/verification/check_v01.json'
at_path = A / 'research/background_86_roots_union_audit/verification/check_v01.json'
base = load(base_path, a.base_sha256)
at = load(at_path, a.at_base_sha256)
ck(base['status'] == 'CONFIRMED_EXACT_SLAB_UNION' and at['status'] == 'PASS', 'completed base unions')
ck(base['source'] == at['source'] == source, 'same fixed source')
ck(base['source_archive_sha256'] == at['source_archive_sha256'] ==
   '2e3c649402c72ad50836f41f35c5657f50232a877557a5641038262355fa689d', 'same complete archive')
ck(base['at_actual_sha256'] == at['actual_slab_audit_sha256'] and
   base['own_recount_sha256'] == at['other_recount_sha256'], 'same completed slab recounts')
ck(base['distinct_indices'] == 86 and base['whole_plane'] is False and at['whole_plane'] is False,
   'regional base scope')
ck(when(base['finished_utc']) < START and when(at['finished_utc']) < START, 'completed unions precede extension')
for key in ('gradient_1_4', 'gradient_71_500'):
    for field in ('roots', 'distinct_indices', 't_closed_components', 'r_squared_components', 'r_squared_open_gaps'):
        ck(base['coverage'][key][field] == at['coverage'][key][field], 'matching independent base coverage')
imports(R, base['files'])
imports(A, at['files'])
selected = [dict(row) for row in base['selected']]
ck([row['index'] for row in selected] == list(range(56)) + list(range(98, 128)), 'complete base index inventory')
root_dir = R / 'research/source013_background_admission/roots'
new = []
for i in range(56, a.max_inner + 1):
    folder = root_dir / f'root_{i:03d}_v02'
    pub_path = folder / 'verification/bindings_v01.json'
    pub = load(pub_path)
    ck(pub['status'] == 'CONFIRMED_LOCAL_RESULT' and pub['index'] == i and pub['source'] == source,
       'complete adopted local theorem')
    imports(R, pub['files'])
    def unique(suffix):
        names = [name for name in pub['files'] if name.endswith(suffix)]
        ck(len(names) == 1, 'unique local dependency: ' + suffix)
        return R / names[0]
    result_path = unique('/result.json.gz')
    receipt_path = unique('/execution.json')
    review_path = unique('/actual_review_v01.json')
    with gzip.open(result_path, 'rt') as f:
        result = json.load(f)
    receipt = load(receipt_path)
    review = load(review_path)
    ck(result['status'] == 'ADMITTED_BACKGROUND_ROOT' and result['index'] == i, 'completed root result')
    ck(result['source'] == source and result['source_counts'] == {'branches':45, 'polynomial_coefficients':621400},
       'same full source')
    ck(result['precision_bits'] == 2048 and result['complete_angular_partition'] is True, 'actual precision and complete angle cover')
    ck(result['root']['index'] == i and Q(result['root']['left_exact']) == Q(i,128) and
       Q(result['root']['right_exact']) == Q(i+1,128), 'exact root domain')
    ck(receipt['status'] == 'COMPLETED' and receipt['reason'] is None and receipt['old_process_signals'] == 0,
       'successful finite execution')
    ck(len(receipt['stages']) == 1 and receipt['stages'][0]['exit_code'] == 0, 'successful single stage')
    ck(review['status'] == 'BOUND' and review['result_sha256'] == digest(result_path) and
       review['execution_sha256'] == digest(receipt_path) and review['request_sha256'] == receipt['request_sha256'],
       'adopted actual independent review')
    ck(when(receipt['finished_utc']) <= when(review['received_utc']) <= when(pub['created_utc']) < START,
       'successful execution then review then publication')
    imports(R, review['own_bindings'])
    imports(R, review['external_dependencies'])
    flags = {key: result['aggregates'][key]['all_leaves_pass']
             for key in ('primary','small_strain','small_gradient','both_small')}
    ck(all(type(value) is bool for value in flags.values()), 'typed joint flags')
    ck(flags == pub['flags'] and result['root'] == pub['root'], 'publication agrees with actual result')
    ck(flags['small_strain'] is True, 'new root establishes weaker conjunction')
    ck(not flags['both_small'] or flags['small_strain'], 'stronger conjunction implies weaker')
    bind(folder / 'PROOF.md')
    selected.append(dict(index=i, route='adopted_ordinary_root', flags=flags,
                         publication=os.path.relpath(pub_path,R), publication_sha256=digest(pub_path),
                         actual_adoption=os.path.relpath(review_path,R), actual_adoption_sha256=digest(review_path)))
    new.append(i)
selected.sort(key=lambda row:row['index'])
ck(len(selected) == len({row['index'] for row in selected}) == a.max_inner + 31, 'unique complete extended inventory')

def radial(t):
    return 'infinity' if t == 1 else str(t/(1-t))

def cover(flag):
    indices = [row['index'] for row in selected if row['flags'][flag]]
    original = [(Q(i,128), Q(i+1,128)) for i in indices]
    merged = []
    for lo,hi in original:
        if merged and lo <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], hi)
        else:
            merged.append([lo,hi])
    ck(merged[0][0] == 0 and merged[-1][1] == 1, 'origin and exterior included')
    for t in [Q(j,128) for j in range(128)] + [Q(2*j+1,256) for j in range(128)]:
        ck(any(lo<=t<=hi for lo,hi in original) == any(lo<=t<=hi for lo,hi in merged),
           'exact elementary membership')
    gaps = [[one[1],two[0]] for one,two in zip(merged,merged[1:])]
    ck(all(lo<hi for lo,hi in gaps), 'strict evidence gaps')
    whole = merged == [[Q(0),Q(1)]]
    ck(whole == (indices == list(range(128))), 'whole-plane cover equivalence')
    return dict(roots=indices, distinct_indices=len(indices),
                t_closed_components=[[str(x) for x in row] for row in merged],
                r_squared_components=[[radial(x) for x in row] for row in merged],
                t_open_gaps=[[str(x) for x in row] for row in gaps],
                r_squared_open_gaps=[[radial(x) for x in row] for row in gaps],
                whole_plane=whole,
                terminal_endpoint_convention='t=1 is a formal endpoint; infinity is not a finite included point')
coverage = dict(gradient_1_4=cover('small_strain'), gradient_71_500=cover('both_small'))
expected = [] if a.max_inner == 97 else [[str(Q(a.max_inner+1,127-a.max_inner)), '49/15']]
ck(coverage['gradient_1_4']['r_squared_open_gaps'] == expected, 'exact remaining weaker gap')
ck(coverage['gradient_1_4']['whole_plane'] == (a.max_inner == 97), 'weaker completion criterion')
for path in (Path(__file__), B/'PROOF.md', B/'formal/README.md'):
    bind(path)
for name,h in FILES.items():
    ck(digest(R/name, True) == h, 'unchanged final dependency')
record = dict(status='CONFIRMED_EXACT_PROGRESSIVE_UNION', started_utc=START.isoformat(),
              finished_utc=datetime.now(timezone.utc).isoformat(), elapsed_seconds=time.monotonic()-TICK,
              checks=N, source=source, base_sha256=a.base_sha256, at_base_sha256=a.at_base_sha256,
              max_inner=a.max_inner, new_indices=new, selected=selected, distinct_indices=len(selected),
              coverage=coverage, whole_plane=coverage['gradient_1_4']['whole_plane'],
              scientific_executions=0, files=FILES,
              scope='Exact union of complete independently reviewed regional theorems. Whole-plane refers only to the displayed background conjunction. Near, inverse, invariant-ball and stationary-existence conclusions remain separate.')
output = B / f'verification/check_v{a.version:02d}.json'
with output.open('x') as f:
    json.dump(record,f,indent=2)
    f.write('\n')
print(json.dumps(dict(status=record['status'], checks=N, elapsed_seconds=record['elapsed_seconds'],
                     distinct_indices=len(selected), whole_plane=record['whole_plane'],
                     sha256=digest(output))), flush=True)

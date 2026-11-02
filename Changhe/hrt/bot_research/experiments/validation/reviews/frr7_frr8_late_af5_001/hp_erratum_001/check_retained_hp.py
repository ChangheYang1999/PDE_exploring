"""New retained-byte audit for the frr8 prose erratum. Standard library only."""
import copy
import gzip
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

BASE = Path('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001')
OUT = BASE / 'hp_erratum_001'
START = datetime.now(timezone.utc).isoformat()
sha = lambda b: hashlib.sha256(b).hexdigest()
now = lambda: datetime.now(timezone.utc).isoformat()
inputs = {}
errors = []

def require(ok, message):
    if not ok:
        errors.append(message)

def read(path):
    path = Path(path)
    b = path.read_bytes()
    key = path.as_posix()
    e = {'sha256': sha(b), 'bytes': len(b)}
    if key in inputs:
        require(inputs[key] == e, 'input changed while reading: ' + key)
    inputs[key] = e
    return b

def save(path, data):
    b = (json.dumps(data, indent=2, sort_keys=True) + '\n').encode()
    with Path(path).open('xb') as f:
        f.write(b)
    return {'sha256': sha(b), 'bytes': len(b)}

manifest = json.loads(read(BASE / 'input_manifest_final_001.json'))
prior_seal = json.loads(read(BASE / 'seal_001.json'))
prior_output_checks = []
for rel, e in prior_seal['outputs'].items():
    b = read(BASE / rel)
    same = sha(b) == e['sha256'] and len(b) == e['bytes']
    require(same, 'prior sealed output changed: ' + rel)
    prior_output_checks.append({'path': (BASE / rel).as_posix(), 'unchanged': same})

archive_edges = {}
def archived(name):
    e = manifest['files'][name]
    z = read(BASE / e['archive'])
    b = gzip.decompress(z)
    require(sha(z) == e['archive_sha256'], 'compressed identity: ' + name)
    require(sha(b) == e['sha256'] and len(b) == e['bytes'], 'original identity: ' + name)
    current = read(name)
    require(current == b, 'current original differs from sealed archive: ' + name)
    archive_edges[name] = copy.deepcopy(e)
    return b

rows = {}
for campaign in ('frr5', 'frr8'):
    rows[campaign] = [json.loads(x) for x in archived('bot_research/runs/lead/' + campaign + '/results.jsonl').splitlines()]
audit = json.loads(read(BASE / 'record_audit_final_001.json'))
spec = audit['specs']
require(len(rows['frr8']) == 2, 'frr8 row count')
require({r['candidate_side'] for r in rows['frr8']} == {0, 1}, 'frr8 physical seats')

def decode(row):
    rr = [json.loads(x) for x in archived(row['log']).splitlines()]
    require(len(rr) == 102, 'complete round count: ' + row['log'])
    keys = [(r['round'], r['player']) for r in rr]
    require(len(set(keys)) == len(keys) and set(keys) == {(r, s) for r in range(51) for s in (0, 1)}, 'complete record grid: ' + row['log'])
    for r in rr:
        require(r['snapshot']['name'] == row['spec_a' if r['player'] == 0 else 'spec_b'], 'snapshot identity: ' + row['log'])
    for r in rr:
        if r['round'] == 0:
            require(r['match']['research_specs'] == [row['spec_a'], row['spec_b']], 'initial specification identity: ' + row['log'])
            require(r['match']['research_scenario'] is None, 'standard scenario identity: ' + row['log'])
    return rr

def canonical(rr):
    # No side relabeling. Exact original physical-seat comparison.
    out = []
    for r in sorted(rr, key=lambda x: (x['round'], x['player'])):
        c = copy.deepcopy(r)
        c.pop('match', None)
        c['snapshot'].pop('name', None)
        out.append(c)
    return out

def digest(value):
    return sha(json.dumps(value, sort_keys=True, separators=(',', ':')).encode())

conditions = []
for row in sorted(rows['frr8'], key=lambda x: x['candidate_side']):
    side = row['candidate_side']
    require(row['spec_a' if side == 0 else 'spec_b'] == spec['AF5'], 'AF5 full specification')
    require(row['spec_b' if side == 0 else 'spec_a'] == spec['V48'], 'V48 full specification')
    require(row['scenario'] is None and row['rounds'] == 50 and row['winner'] == side, 'standard frr8 outcome')
    rr = decode(row)
    terminal = {r['player']: r for r in rr if r['round'] == 50}
    hp = [terminal[side]['snapshot']['hp'], terminal[1-side]['snapshot']['hp']]
    result_hp = [row['hp_a' if side == 0 else 'hp_b'], row['hp_b' if side == 0 else 'hp_a']]
    require(hp == result_hp == [790, 735], 'correct AF5-first terminal HP')
    require(row['hp_diff_a'] * (1 - 2 * side) == 55, 'AF5 margin')
    require(all(t['result'] == {'winner': side, 'reason': 'round_limit'} for t in terminal.values()), 'terminal result fields')
    detail = [d for d in audit['campaigns']['frr8']['conditions'] if d['candidate_side'] == side]
    require(len(detail) == 1, 'sealed audit condition count')
    require(detail[0]['candidate_hp'] == 790 and detail[0]['opponent_hp'] == 735, 'sealed audit already correct')
    matches = [r for r in rows['frr5'] if r['scenario'] is None and
               r['spec_a' if side == 0 else 'spec_b'] == spec['G1'] and
               r['spec_b' if side == 0 else 'spec_a'] == spec['V48']]
    require(len(matches) == 1, 'unique full-spec g1 same-physical-seat comparator')
    ref = matches[0]
    require(ref['candidate_side'] == 1-side, 'frr5 reversed candidate role')
    ref_records = decode(ref)
    left, right = canonical(rr), canonical(ref_records)
    same = left == right
    require(same, 'complete g1/frr5 canonical history')
    require(digest(left) == detail[0]['raw_check']['canonical_sha256'], 'previous canonical digest')
    conditions.append({'physical_AF5_or_G1_side': side, 'frr8_log': row['log'], 'frr5_log': ref['log'],
       'frr8_row': row, 'frr5_row': ref, 'terminal_HP_AF5_first': hp,
       'terminal_snapshot_fields': [{k: t['snapshot'][k] for k in ('hp', 'gold', 'n_factories', 'n_walls', 'n_turrets', 'length_path')} for t in (terminal[side], terminal[1-side])],
       'terminal_results': [terminal[side]['result'], terminal[1-side]['result']],
       'rounds': 50, 'outcome_AF5': 'W', 'HP_margin_AF5': 55,
       'sealed_audit_already_correct': True, 'compared_records_per_history': len(left),
       'same_complete_canonical_history': same, 'AF5_canonical_sha256': digest(left), 'G1_canonical_sha256': digest(right)})

# Inspect exact prose-like copies, including original upstream text retained in gzip archives.
# This searches serialized 795:740 / 795,740 pairs, not arbitrary independent HP fields.
pattern = re.compile(r'795\s*[:,]\s*740')
scan = []
occurrences = []
for path in sorted(BASE.rglob('*')):
    if not path.is_file() or OUT in path.parents:
        continue
    b = read(path)
    original = gzip.decompress(b) if path.suffix == '.gz' else b
    try:
        text = original.decode('utf-8')
    except UnicodeDecodeError:
        continue
    scan.append({'path': path.as_posix(), 'stored_sha256': sha(b), 'decoded_sha256': sha(original), 'decoded_bytes': len(original)})
    for number, line in enumerate(text.splitlines(), 1):
        if pattern.search(line):
            occurrences.append({'path': path.as_posix(), 'line': number, 'text': line,
                                'sealed_original_output': path.relative_to(BASE).as_posix() in prior_seal['outputs']})

require([x['path'] for x in occurrences if x['sealed_original_output']] == [(BASE / 'REVIEW.md').as_posix()], 'exact original sealed prose occurrence set')
# Preserve copies of the erroneous prose and the detection artifacts without modifying originals.
(OUT / 'inputs').mkdir(exist_ok=True)
preserved = []
for path in sorted({Path(x['path']) for x in occurrences} | {BASE / 'seal_001.json'}):
    b = read(path)
    destination = OUT / 'inputs' / (sha(b) + '.gz')
    z = gzip.compress(b, mtime=0)
    with destination.open('xb') as f:
        f.write(z)
    preserved.append({'path': path.as_posix(), 'sha256': sha(b), 'bytes': len(b),
                      'archive': destination.relative_to(OUT).as_posix(), 'archive_sha256': sha(z), 'archive_bytes': len(z)})

# Recheck the used originals and original sealed files after the reads.
for name, e in archive_edges.items():
    require(sha(Path(name).read_bytes()) == e['sha256'], 'end current original identity: ' + name)
for rel, e in prior_seal['outputs'].items():
    require(sha((BASE / rel).read_bytes()) == e['sha256'], 'end original sealed output identity: ' + rel)

completed = now()
evidence = {'schema': 1, 'started_utc': START, 'completed_utc': completed, 'reviewer_model': 'GPT-6 Astra',
 'execution': 'Standard-library source/text/JSON reading and hashing only. No policy constructors or decisions, Engine, game, replay, or existing project checker execution.',
 'original_review_sha256': inputs[(BASE/'REVIEW.md').as_posix()]['sha256'],
 'original_seal_sha256': inputs[(BASE/'seal_001.json').as_posix()]['sha256'],
 'error': 'REVIEW.md line 27 and the prior handoff message said AF5 795:740. Both retained terminal HP values were overstated by 5.',
 'correction': 'AF5 790:735, margin +55, round 50, both physical seats.',
 'errors': errors, 'audit_completed': not errors, 'verdict': 'CONFIRMED' if not errors else 'OPEN',
 'conditions': conditions, 'archive_edges': archive_edges, 'input_sha256_and_bytes': inputs,
 'original_sealed_output_checks': prior_output_checks, 'literal_search_expression': pattern.pattern,
 'literal_search_scope': 'All readable files and gzip-decoded retained inputs under the original review directory, excluding this new erratum directory. Parent-owned detection files are read and retained, not modified.',
 'literal_search_inputs': scan, 'literal_occurrences': occurrences, 'preserved_error_and_detection_bytes': preserved,
 'unchanged_scope': ['2W0D0L for frr8', '+55 margins and round 50', 'two exact g1/frr5 complete canonical histories', 'original raw-record and source JSON identities', 'AF5 matrix proof and WDL certificate identities'],
 'limitations': ['The original seal authenticated bytes and arithmetic JSON but failed to detect this prose transcription error.', 'This erratum does not certify all prose claims automatically.', 'The complete-history comparison is of these retained records only, with no fresh-policy reproduction or timing-invariance claim.']}
evidence_id = save(OUT/'EVIDENCE.json', evidence)
text = f'''# frr8 terminal HP erratum\n\nPrepared {completed}. Reviewer: GPT-6 Astra. This addendum corrects the original sealed review without replacing its bytes.\n\n**Claim.** [The original review](../REVIEW.md), line 27, says that AF5 beats v48 795:740 in both standard-start frr8 games. **Verdict: REFUTED.** The exact result rows and terminal raw records instead give **AF5 790:735, +55 at round 50 in both physical seats**. My earlier handoff repeated the same error. Both absolute HP values in that prose were too large by 5.\n\n**Method.** Read both frr8 result rows and terminal records from their previously sealed gzip archives, authenticate their original and compressed hashes, and compare them byte for byte with the current original files. The [new evidence](EVIDENCE.json) retains full row identities, terminal snapshot fields and results, and the exact archive edges. The original result rows and `record_audit_final_001.json` already contained 790:735. This was a prose transcription error, not a change in the underlying game evidence.\n\n**Claim.** The g1/frr5 canonical-history comparison remains valid. **Method.** Join the exact opponent specification, standard scenario and physical g1/AF5 seat, taking account of frr5 recording v48 as its candidate. Compare all 102 records in each complete history after removing only match identity metadata and snapshot policy names. All other fields and ordered actions remain. **Result.** Both comparisons are exactly equal, with g1 also finishing 790:735. **Verdict: CONFIRMED for these four retained histories.** This makes no fresh-policy or clock-invariance claim.\n\nThe literal-copy search covered original readable review files and gzip-decoded retained inputs. Among original sealed outputs, only `REVIEW.md` contains the wrong pair. The parent's later `root_review_001.py` assertion and its failure transcript also contain that pair as detection evidence; those files are separately identified and preserved. The original review, seal, and every original sealed output remain byte-identical.\n\nThe frr8 total of 2W0D0L, +55 margins, round counts, retained-action totals, and finite WDL matrix remain unchanged. The original seal authenticated bytes and numerical artifacts but did not detect this prose defect. Its existence must not be read as certification of the incorrect sentence. The corrected statement and this evidence take precedence for terminal HP reporting. No original sealed file was edited.\n'''
with (OUT/'ERRATUM.md').open('x') as f:
    f.write(text)
with (OUT/'INDEX.md').open('x') as f:
    f.write('# Reading order\n\n1. [ERRATUM.md](ERRATUM.md) states the exact correction and its scope.\n2. [EVIDENCE.json](EVIDENCE.json) binds archived/current rows, terminal records, both full-history comparisons and the literal-copy search.\n3. [check_retained_hp.py](check_retained_hp.py) is the independent standard-library reader.\n4. [seal.json](seal.json) binds these new artifacts. Original sealed files remain unchanged.\n')
outputs = {}
for path in sorted(OUT.rglob('*')):
    if path.is_file():
        b = path.read_bytes()
        outputs[path.relative_to(OUT).as_posix()] = {'sha256': sha(b), 'bytes': len(b)}
seal = {'schema': 1, 'sealed_utc': now(), 'reviewer_model': 'GPT-6 Astra', 'verdict': 'CONFIRMED' if not errors else 'OPEN',
        'errors': errors, 'original_seal_sha256': evidence['original_seal_sha256'], 'original_outputs_unchanged': not any(not x['unchanged'] for x in prior_output_checks),
        'outputs': outputs, 'evidence': evidence_id, 'terminal_HP_AF5_first_both_seats': [790, 735], 'equal_complete_g1_histories': sum(c['same_complete_canonical_history'] for c in conditions)}
seal_id = save(OUT/'seal.json', seal)
print(json.dumps({'path': (OUT/'seal.json').as_posix(), 'seal': seal_id, 'sealed_utc': seal['sealed_utc'], 'verdict': seal['verdict'],
 'errors': errors, 'occurrences': occurrences, 'equal_histories': seal['equal_complete_g1_histories'], 'erratum_sha256': outputs['ERRATUM.md']['sha256']}, indent=2))

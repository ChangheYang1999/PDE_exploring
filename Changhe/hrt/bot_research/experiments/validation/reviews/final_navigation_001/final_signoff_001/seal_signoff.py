"""Authenticate static navigation snapshots and issue a dated usability signoff."""
import argparse
import datetime
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys

ROOT = Path('bot_research/experiments/validation/reviews/final_navigation_001')
OUT = ROOT / 'final_signoff_001'
INDEX = 'bot_research/experiments/validation/analysis/README.md'
REPORT = 'bot_research/reports/REPORT.md'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def write_new(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)

def json_bytes(path):
    raw = Path(path).read_bytes()
    return raw, json.loads(raw)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inspection', required=True)
    parser.add_argument('--expected-inspection-sha', required=True)
    parser.add_argument('--latest-publication', required=True)
    parser.add_argument('--expected-latest-sha', required=True)
    args = parser.parse_args()
    assert os.sched_getaffinity(0) == {28}
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 19
    assert sys.dont_write_bytecode and not sys.flags.optimize
    assert all(os.environ.get(k) == '1' for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'))
    assert Path(os.environ['TMPDIR']).resolve() == (Path.cwd() / 'bot_research/tmp').resolve()
    started = stamp()
    originals = [
        (ROOT / 'inspection-001/INSPECTION.json', '5027da354614bfc3ca7184fce5c762803db96c66465df6b1898b9b724cb5e298'),
        (ROOT / 'inspection-final-002/INSPECTION.json', '5aff41d2d1cf05245bb9e67b75b2e7c73a7d7183aaf8560bee4232b6664de62f'),
        (Path(args.inspection), args.expected_inspection_sha),
    ]
    archived = []
    scans = []
    for path, expected in originals:
        raw, obj = json_bytes(path)
        assert sha(raw) == expected, str(path)
        verified = 0
        for source, item in obj['input_documents'].items():
            packed = Path(item['archive']).read_bytes()
            assert sha(packed) == item['archive_sha256'], source
            data = gzip.decompress(packed)
            assert sha(data) == item['sha256'] and len(data) == item['bytes'], source
            verified += 1
        archived.append({'path': str(path), 'sha256': sha(raw), 'markdown_archive_edges_authenticated': verified})
        scans.append(obj)
    final = scans[-1]
    assert not final['missing_links'] and not final['missing_anchors'] and not final['unreachable_proofs']
    for name in ('missing_local_targets', 'missing_atx_or_explicit_anchors', 'standalone_proofs_unreachable_from_root'):
        assert final['counts'][name] == 0
    old_docs = scans[0]['input_documents']
    new_docs = final['input_documents']
    common = sorted(set(old_docs) & set(new_docs))
    changes = [{'path': p, 'before_sha256': old_docs[p]['sha256'], 'after_sha256': new_docs[p]['sha256']} for p in common if old_docs[p]['sha256'] != new_docs[p]['sha256']]
    assert {item['path'] for item in changes} <= {INDEX, REPORT}
    assert len(common) == len(old_docs)
    current_differences = []
    for source, item in new_docs.items():
        digest = sha(Path(source).read_bytes())
        if digest != item['sha256']:
            current_differences.append({'path': source, 'snapshot_sha256': item['sha256'], 'current_sha256': digest})
    assert {item['path'] for item in current_differences} <= {REPORT}
    pins = [
        ('bot_research/experiments/validation/analysis/VALIDATION_FINDINGS.md', 'fb4931c66944cfa59058a2947214681d90d05d927b5ecd58b92875df340c19f2'),
        ('bot_research/experiments/validation/analysis/ADAPTATION_FINDINGS.md', 'b371dd4205158191d72499c8efe57a35b33d1ff418467ca725356f1228891cba'),
        (str(ROOT / 'scan_navigation.py'), '0288e80622c5dd96bb87ea21ded4d65df993b912727d1adbdd5df8154804ce18'),
        ('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001/root_review_002.json', '2494c99caf1970368b043be9cd89f72679d8a002f15866a6ce3109ea1753e5b0'),
        ('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001/root_hp_erratum_review_002.json', '7dfb575ec6e7e87042695167b9e316e030fc37c8ca7cdc0b36d208d23775db3b'),
        ('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001/root_foreign_gate_review_001.json', 'ee646bb88fe245bb3ebdf27665892d7e55370d66ce1470f561d38be7c62d5215'),
        ('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001/foreign_attack_control_flow_001/PROOF.md', '30dc386a91057b5a635ee3acfdbec4d7b8fd0a60dd8563be94254fb1bfc6b6ca'),
    ]
    pin_checks = []
    for source, expected in pins:
        raw = Path(source).read_bytes()
        assert sha(raw) == expected, source
        pin_checks.append({'path': source, 'sha256': expected, 'bytes': len(raw)})
    publications = [
        (ROOT / 'root_publication_002/RECEIPT.json', '75113778f48ac7fe668c73dd018a559fccd96282bd84e99b489fedcf4fafedeb'),
        (ROOT / 'root_publication_003/RECEIPT.json', 'c97f2b8f8730d359bbb813cbd5e60f86a5f92d13bffed73f901bc87336fb73bf'),
        (Path(args.latest_publication), args.expected_latest_sha),
    ]
    publication_checks = []
    receipt_sources = []
    preceding = old_docs[INDEX]['sha256']
    for path, expected in publications:
        raw, obj = json_bytes(path)
        assert sha(raw) == expected, str(path)
        assert obj['index_before_sha256'] == preceding
        before = gzip.decompress((path.parent / 'index_before.md.gz').read_bytes())
        after = gzip.decompress((path.parent / 'index_after.md.gz').read_bytes())
        assert sha(before) == obj['index_before_sha256']
        assert sha(after) == obj['index_after_sha256']
        assert after.startswith(before), str(path)
        diff_bytes = (path.parent / 'index.diff').read_bytes()
        links = []
        for item in obj['added_links']:
            target = item['project_path']
            actual = sha(Path(target).read_bytes())
            assert actual == item['sha256'], target
            links.append({'path': target, 'sha256': actual})
        publication_checks.append({'path': str(path), 'sha256': expected, 'published_utc': obj['published_utc'], 'index_before_sha256': sha(before), 'index_after_sha256': sha(after), 'append_only_bytes': True, 'index_diff_sha256': sha(diff_bytes), 'added_target_hashes_authenticated': links})
        receipt_sources.extend([path, path.parent / 'index_before.md.gz', path.parent / 'index_after.md.gz', path.parent / 'index.diff'])
        preceding = sha(after)
    assert new_docs[INDEX]['sha256'] == preceding == sha(Path(INDEX).read_bytes())
    # Archive only new receipt and script bindings here. The independently verified
    # lossless Markdown snapshots remain in each immutable inspection directory.
    additional = []
    for path in receipt_sources + [Path(p) for p, _ in pins]:
        raw = path.read_bytes()
        archive = OUT / 'inputs' / (str(path) + '.gz')
        if any(item['source'] == str(path) for item in additional):
            continue
        packed = gzip.compress(raw, mtime=0)
        write_new(archive, packed)
        additional.append({'source': str(path), 'sha256': sha(raw), 'bytes': len(raw), 'archive': str(archive), 'archive_sha256': sha(packed)})
    counts = final['counts']
    report = f'''# Final navigation signoff 001

Prepared at {started}. This GPT-6 Astra source-only review authenticates the navigation published through {publication_checks[-1]['published_utc']}. The fixed [final inspection]({os.path.relpath(args.inspection, OUT)}) ran from {final['started_utc']} to {final['completed_utc']}; its exact input bytes and every recognized edge are archived. The preceding [168-proof snapshot](../inspection-final-002/INSPECTION.json) remains unchanged. This is usability and publication-integrity work, not additional strength evidence.

**CONFIRMED within the inspected graph.** The main index, SHA256 `{preceding}`, provides a clickable route to all {counts['standalone_proofs']} identified standalone proofs. The scan read and archived {counts['documents_read_and_archived']} Markdown documents, checked {counts['local_link_occurrences']} local link occurrences, and found no missing target or unresolved recognized heading anchor. It followed {counts['root_local_links']} root links to {counts['root_distinct_markdown_targets']} distinct Markdown targets. Linked non-Markdown files were checked for existence and size only, except the separately named publication and review receipts authenticated here.

The earlier two matrix-extension omissions are repaired. The root now links the [frr3 index](../../frr3_extension_review_001/INDEX.md) and [standalone proof](../../frr3_extension_review_001/PROOF.md), the [frr5/frr6 finite extension](../../frr5_frr6_final_fortress_001/finite_matrix_extension/INDEX.md), and the [AF5 matrix proof and reading order](../../frr7_frr8_late_af5_001/af5_matrix_extension/INDEX.md). The descriptions preserve the finite-payoff hypotheses, imposed zero diagonal and unmeasured fortress-mutual-entry scope. They do not assert optimality in the unrestricted game.

The AF5 route also links the [HP erratum](../../frr7_frr8_late_af5_001/hp_erratum_001/ERRATUM.md) directly and states its precedence over the retained erroneous pair. The correction is 790:735 in both seats; +55 and round 50 remain unchanged. The separate [foreign attack control-flow topic](../../frr7_frr8_late_af5_001/foreign_attack_control_flow_001/INDEX.md) has a readable index and standalone proof. Its conditional source claim is explicitly distinguished from a legal-game witness, which remains open in that review. This signoff reads that scope; it does not rerun its source/record checker.

Completed T, U, V, fourth-decision ambiguity and terminal D result pages now have direct routes beside the preserved preparation material. Dated OPEN preparation statements remain historical. Both the [validation guide](../../../analysis/VALIDATION_FINDINGS.md) and [adaptation guide](../../../analysis/ADAPTATION_FINDINGS.md) retain their independently reviewed hashes and explicit timing scope. No sealed proof, guide, result or preparation page in the {len(common)}-document original inspection changed: the only shared-byte differences are the appended root index and mutable lead report. The two earlier publication receipts and latest receipt authenticate an append-only chain, with all listed target hashes still matching.

Of {counts['result_pages']} result pages in the inventory, {counts['result_pages_unreachable_from_root']} older pages remain outside the recognized clickable graph. This disclosed catalogue limitation is unchanged by the requested minimum additions and does not make a dated historical OPEN statement a current scientific contradiction. A future result catalogue can link them without rewriting sealed texts. No further minimum navigation repair is identified in this snapshot.

[RECEIPT.json](RECEIPT.json) records all checks, current-versus-snapshot differences, exact publication identities and additional input archives. The scanner inventories analysis Markdown outside source/archive subtrees, includes the explicitly named review topics, and follows existing local Markdown links. “All proofs” means all standalone proofs in that inspected inventory, not an unrestricted filesystem search. ATX and explicit anchors are checked statically; no browser rendering or complete semantic re-verification of the earlier proofs occurred. Input hashes establish retained byte identity at the recorded times, not continuous historical identity or runtime provenance. No policy import, constructor, decision, Engine call, game, replay, simulation, project checker or test ran. No JavaScript/TypeScript, server, cluster, remote compute, GPU or formal prover was used. Actual Opus 5.5 collaboration remains through lead/economy notes and root's exchanges.
'''
    write_new(OUT / 'REVIEW.md', report.encode())
    completed = stamp()
    receipt = {
        'schema': 'final-navigation-signoff-001', 'started_utc': started, 'completed_utc': completed,
        'verdict': 'CONFIRMED_WITH_DECLARED_STATIC_INVENTORY_SCOPE', 'actual_model': 'GPT-6 Astra',
        'affinity': sorted(os.sched_getaffinity(0)), 'nice': os.getpriority(os.PRIO_PROCESS, 0),
        'inspections_authenticated': archived, 'final_counts': counts,
        'original_documents_retained_in_final_inspection': len(common), 'original_snapshot_byte_changes': changes,
        'current_files_differing_from_final_snapshot': current_differences,
        'publication_chain': publication_checks, 'explicit_prior_pins_authenticated': pin_checks,
        'additional_archived_inputs': additional,
        'review_sha256': sha((OUT / 'REVIEW.md').read_bytes()), 'script_sha256': sha(Path(__file__).read_bytes()),
        'policy_constructor_decision_engine_game_replay_simulation_test_calls': 0,
        'scope': 'Dated static navigation and publication-integrity signoff. No new strength evidence, semantic proof verification or runtime provenance assertion.',
    }
    write_new(OUT / 'RECEIPT.json', (json.dumps(receipt, indent=2, sort_keys=True) + '\n').encode())
    print(json.dumps({'completed_utc': completed, 'review_sha256': receipt['review_sha256'], 'receipt_sha256': sha((OUT / 'RECEIPT.json').read_bytes()), 'script_sha256': receipt['script_sha256'], 'counts': counts, 'original_snapshot_changes': changes, 'current_snapshot_differences': current_differences}, indent=2))

if __name__ == '__main__':
    main()

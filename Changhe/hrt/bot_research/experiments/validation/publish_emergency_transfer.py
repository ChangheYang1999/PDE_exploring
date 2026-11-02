"""Publish all 90 emergency-transfer comparisons, retaining every regression."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
AREA = E/'analysis/emergency_transfer'
INVERSE = {'W':'L', 'D':'D', 'L':'W'}
RANK = {'L':0, 'D':1, 'W':2}


def canonical_records(row):
    records = [json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
    side = row['condition']['candidate_side']
    for rec in records:
        rec.pop('match', None)
        rec['player'] ^= side
        rec['snapshot']['name'] = 'target' if rec['player'] == 0 else 'counter'
        for event in rec['event']:
            event.pop('order', None)
        if rec.get('result', {}).get('winner') is not None:
            rec['result']['winner'] ^= side
    return sorted(records, key=lambda rec:(rec['round'],rec['player']))


def main():
    inputs = {}
    def digest(path):
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    def read(path):
        inputs[str(path)] = digest(path)
        return json.loads(path.read_text())
    histories, expected, fresh, early_calls, activations = {}, 0, 0, 0, 0
    for name in ('emergency-transfer-a001', 'emergency-transfer-b001', 'emergency-transfer-c001'):
        manifest = read(E/(name+'.json'))
        for path, sha in manifest['input_sha256'].items():
            assert digest(path) == sha, path
        audits = {kind: read(R/(name+'-'+kind+'.json')) for kind in
                  ('strict','replay','summary','data','histories','activation')}
        size = manifest['expected_conditions']; expected += size
        assert audits['strict']['valid_conditions'] == size
        summary = audits['summary']
        assert summary['valid_conditions'] == size and summary['unresolved_conditions'] == 0
        assert summary['complete_assignment_pairs'] == summary['identical_assignment_pairs'] == size//2
        assert not summary['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['replay']['count'] == size
        assert audits['data']['all_passed'] and audits['activation']['all_passed']
        assert audits['activation']['games'] == size
        early_calls += audits['activation']['checked_early_calls']
        activations += audits['activation']['emergency_activations']
        history = audits['histories']
        assert all(history[k] for k in ('all_fresh_actions_legal','all_observations_unchanged',
            'all_public_selections_verified','all_replayed','exact_counter_policy_reproduction'))
        for path, sha in history['input_sha256'].items():
            assert digest(path) == sha, path
        for case in history['cases']:
            assert case['result'] not in histories
            histories[case['result']] = case
            fresh += len(case['rounds'])
    declared = read(E/'emergency-transfer-controls-001.json')
    assert len(declared['pairs']) == expected == 90
    comparisons = []
    old_counts, new_counts, transitions = Counter(), Counter(), Counter()
    for pair in declared['pairs']:
        old, new = checked_row(pair['old'], inputs), checked_row(pair['new'], inputs)
        for row in (old,new):
            c = row['condition']
            assert c['candidate_id'] == pair['target'] and c['candidate_spec'] == pair['target_spec']
            assert c['candidate_side'] == pair['candidate_side']
        old_outcome, new_outcome = INVERSE[old['outcome']], INVERSE[new['outcome']]
        old_counts[old_outcome] += 1; new_counts[new_outcome] += 1
        transitions[old_outcome+'->'+new_outcome] += 1
        raw_old, raw_new = read(Path(pair['old'])), read(Path(pair['new']))
        a, b = canonical_records(raw_old), canonical_records(raw_new)
        equal = a == b
        assert equal == (old['canonical_replay_sha256'] == new['canonical_replay_sha256'])
        differing = next((min(x['round'],y['round']) for x,y in zip(a,b) if x != y), None)
        if differing is None and len(a) != len(b):
            differing = min(a[len(b):]+b[len(a):], key=lambda rec:rec['round'])['round']
        case = histories[pair['new']]
        emergency = [q['round'] for q in case['emergency_checks'] if q['emergency_activated']]
        if equal:
            assert differing is None
        comparisons.append(dict(**pair, old_outcome=old_outcome, new_outcome=new_outcome,
            old_hp_counter_first=old['hp_candidate_first'][::-1], new_hp_counter_first=new['hp_candidate_first'][::-1],
            old_final_round=old['rounds'], new_final_round=new['rounds'],
            same_complete_trajectory=equal, first_differing_round=differing,
            selected=case['selected'], emergency_activation_rounds=emergency,
            worsened=RANK[new_outcome] < RANK[old_outcome], improved=RANK[new_outcome] > RANK[old_outcome]))
    no_regressions = not any(row['worsened'] for row in comparisons)
    all_repaired = not new_counts['L']
    now = datetime.now(timezone.utc).isoformat()
    table = []
    for target in sorted({row['target'] for row in comparisons}):
        rows = [row for row in comparisons if row['target'] == target]
        assert len(rows) == 2
        keys = ('old_outcome','new_outcome','old_hp_counter_first','new_hp_counter_first','old_final_round',
                'new_final_round','same_complete_trajectory','first_differing_round','selected','emergency_activation_rounds')
        assert all(rows[0][key] == rows[1][key] for key in keys)
        row = rows[0]
        hp = ':'.join(map(str,row['new_hp_counter_first']))
        table.append(f'| {target} | {row["selected"]} | {row["old_outcome"]} | {row["new_outcome"]} | {hp} | '
                     f'{row["new_final_round"]} | {row["emergency_activation_rounds"]} | {row["first_differing_round"]} |')
    verdict = ('CONFIRMED' if no_regressions and all_repaired else 'REFUTED')+': the complete claim of preserving all outcomes and repairing every route-builder loss.'
    count_text = lambda counts: f'{counts["W"]}W/{counts["D"]}D/{counts["L"]}L'
    exact = sum(row['same_complete_trajectory'] for row in comparisons)
    text = f'''# Emergency continuation transfer results

Checked {now}.

{verdict}

The new policy has {count_text(new_counts)} across the 90 declared conditions. The old adaptive selector has {count_text(old_counts)} on the matched prior conditions. There are {sum(row['improved'] for row in comparisons)} improved and {sum(row['worsened'] for row in comparisons)} worsened W/D/L outcomes. Exactly {exact} complete normalized histories agree with their old controls. The condition union and the new policy were fixed before these games, but all targets are previously disclosed development opponents.

Each row represents both assignments, which agree on every displayed result. Outcomes and HP are from the counter perspective. A null first-difference round means the complete history is unchanged. Trigger timing is not itself proof that the trigger caused a changed outcome; the full trajectory comparison supplies the paired observation.

| Target | Selected branch | Old | New | New HP counter:target | Final round | Emergency rounds | First differing round |
|---|---|---|---|---|---:|---|---|
'''+ '\n'.join(table)+f'''

All 90 new games pass strict/source/data accounting, original-engine replay and fresh counter regeneration. All {fresh} fresh decisions agree, observations remain unchanged, and there are no rejected submitted actions or bot errors. A separate implementation reconstructs {early_calls} early-branch calls and {activations} emergency activations directly from public snapshots and original combat, then checks the old HP trigger and recorded activation state. All 45 assignment pairs have identical complete normalized trajectories. The 90 old result/replay pairs are rehashed and their source attestations rechecked during comparison.

The delayed tier-five route-builder failures, if present in the table, remain part of this result. The added rule can only affect defense before the old HP trigger begins it; it cannot undo a prior investment or predict hidden purchases. This is an empirical development comparison, not a population estimate or held-out validation. It leaves best_v9e and its final pool-C evidence unchanged.

Reproduction: run the three emergency-transfer manifests with run_data_development and the standard project-root environment. Then use audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, check_emergency_histories, and audit_emergency_activation for each campaign. This publisher matches all 90 pairs declared in emergency-transfer-controls-001.json. verification/full_games.json records the input hashes, complete comparisons and this publisher.
'''
    output_path = AREA/'RESULTS.md'
    with output_path.open('x') as handle:handle.write(text)
    for path in (output_path,AREA/'PROOF.md',Path(__file__).relative_to(Path.cwd())):
        inputs[str(path)] = digest(path)
    receipt = dict(time_utc=now, all_audits_passed=True, verdict=verdict, games=90,
        old_outcomes=dict(old_counts),new_outcomes=dict(new_counts),transitions=dict(transitions),
        no_wdl_regressions=no_regressions,all_previous_losses_repaired=all_repaired,
        fresh_counter_decisions=fresh,independent_early_calls=early_calls,emergency_activations=activations,
        exact_control_trajectories=exact,comparisons=comparisons,input_sha256=inputs)
    with (AREA/'verification/full_games.json').open('x') as handle:json.dump(receipt,handle,indent=2,sort_keys=True);handle.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as handle:
        handle.write(f'\n## {now}: Emergency continuation transfer on 45 prior targets\n\n'
            f'Claim and verdict: {verdict}\n\nMethod: 90 newly declared games, both assignments, compared against all 90 matched '
            f'old adaptive controls. Result: old {count_text(old_counts)}, new {count_text(new_counts)}; transitions {dict(transitions)}; '
            f'{exact} complete histories unchanged. All audits pass: {fresh} fresh decisions, {early_calls} independently reconstructed '
            f'early calls, {activations} emergency activations. Development only; best_v9e unchanged. Evidence: {output_path}.\n')
    print(json.dumps({key:value for key,value in receipt.items() if key not in ('comparisons','input_sha256')}))

if __name__ == '__main__':
    main()

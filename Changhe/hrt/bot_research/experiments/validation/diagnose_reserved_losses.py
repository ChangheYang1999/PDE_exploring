"""Attribute recorded loss margins to prescribed and policy-controlled rounds.

This is trajectory accounting, not a counterfactual claim that a loss was
unavoidable or that one observed purchase caused the final outcome.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign-audit', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    audit = json.loads(Path(args.campaign_audit).read_text())
    inputs = {args.campaign_audit: digest(args.campaign_audit)}
    losses = []
    for case in audit['cases']:
        if case['outcome'] != 'L':
            continue
        path = Path(case['result_path'])
        replay = Path(case['replay_path'])
        for filename in (path, replay):
            value = digest(filename)
            if audit['input_sha256'][str(filename)] != value:
                raise ValueError('Previously audited input changed: ' + str(filename))
            inputs[str(filename)] = value
        row = json.loads(path.read_text())
        job_path = path.parent.parent / 'jobs' / (path.stem + '.json')
        inputs[str(job_path)] = digest(job_path)
        job = json.loads(job_path.read_text())
        prefix_rounds = max(map(len, job.get('prefixes', [[], []])))
        side = case['condition']['candidate_side']
        initial_hp = row['rules']['globals']['initial_hp']
        history = row['history']
        initial_margin = 0
        prefix_margin = initial_margin
        if prefix_rounds:
            before = next(h for h in history if h['round'] == prefix_rounds)
            prefix_margin = before['players'][side]['hp'] - before['players'][1 - side]['hp']
        damage = []
        post_damage = [0, 0]
        for record in history:
            players = [record['players'][side], record['players'][1 - side]]
            values = [p['combat']['base_damage'] for p in players]
            if any(values):
                damage.append({'round': record['round'], 'base_damage_candidate_first': values,
                               'hp_candidate_first': [p['hp'] for p in players],
                               'prescribed_round': record['round'] <= prefix_rounds})
            if record['round'] > prefix_rounds:
                post_damage = [a + b for a, b in zip(post_damage, values)]
        summed = [sum(d['base_damage_candidate_first'][p] for d in damage) for p in (0, 1)]
        if [initial_hp - value for value in summed] != case['hp_candidate_first']:
            raise ValueError('Base damage does not account for final HP.')
        selected = {0, 1, 2, 3, 4, row['rounds']}
        for d in damage:
            selected.update((max(0, d['round'] - 1), d['round']))
        timeline = []
        for line in replay.open():
            record = json.loads(line)
            if record['round'] not in selected:
                continue
            actions = [e['action'] for e in record['event'] if e['kind'] == 'action']
            timeline.append({'round': record['round'],
                'role': 'candidate' if record['player'] == side else 'opponent',
                'snapshot': record['snapshot'], 'actions': actions})
        final_margin = case['hp_candidate_first'][0] - case['hp_candidate_first'][1]
        losses.append({'job': case['job'], 'condition': case['condition'],
            'result_path': str(path), 'replay_path': str(replay),
            'prefix_rounds': prefix_rounds, 'first_underlying_policy_round': prefix_rounds + 1,
            'prefix_margin_candidate_first': prefix_margin,
            'final_margin_candidate_first': final_margin,
            'postprefix_margin_change': final_margin - prefix_margin,
            'postprefix_base_damage_candidate_first': post_damage,
            'no_postprefix_damage': not any(post_damage),
            'damage_rounds': damage, 'selected_round_details': timeline})
    output = {'time_utc': now(), 'checker_sha256': digest(__file__),
        'candidate': audit['candidate'], 'candidate_sha256': audit['candidate_sha256'],
        'pool': audit['pool'], 'input_sha256': inputs, 'losses': losses,
        'scope': 'Exact accounting of the recorded loss trajectories. This does not prove that a loss was unavoidable or identify the outcome of a different decision.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'losses': len(losses),
        'entire_margin_inherited_with_no_later_damage': sum(c['no_postprefix_damage'] for c in losses)}))


if __name__ == '__main__':
    main()

"""Audit public-signature elimination without executing any opponent policy."""
from collections import Counter
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qsl
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.identifying_counter import purchase_signature
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.replay_audit import check, normalized
from bot_research.experiments.validation.source_closure import static_closure

EXPECTED = {
    'best_v9b': ('bot_research.experiments.lead.frozen.best_v9b', {}),
    'economy17': ('bot_research.bots.economy.frozen.v17.econ17',
                  dict(free_fallback='zero', foreign_attack_from=11)),
    'economy19': ('bot_research.bots.economy.frozen.v19.econ19',
                  dict(free_fallback='zero', foreign_attack_from=11, doom='next',
                       fac_cap=400, sat_reach=True)),
}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def known_target(spec):
    module, separator, tail = spec.partition(':')
    name, _, query = tail.partition('?')
    if separator != ':' or name != '@make': return None
    parameters = {key: json.loads(value) for key, value in parse_qsl(query)}
    return next((key for key, (mod, params) in EXPECTED.items()
                 if mod == module and params == parameters), None)


def audit_trace(row, records):
    side = row['condition']['candidate_side']
    trace = row['catalogue_trace']
    ids = row['catalogue_ids']
    check(len(ids) == len(set(ids)) and set(ids) <= set(EXPECTED), 'Invalid initial catalogue.')
    check([t['round'] for t in trace] == list(range(1, row['rounds']+1)), 'Trace rounds differ.')
    check(len(records) == 2*(row['rounds']+1), 'Trace replay length differs.')
    actual_target = known_target(row['condition']['opponent_spec'])
    in_catalogue = actual_target in ids
    active, pending = list(ids), {}
    calls = dict.fromkeys(ids, 0)
    config = config_from_dict(row['rules'])
    singleton_mismatches = []
    details = []
    known_exact_rounds = 0
    for t in trace:
        rnd = t['round']
        check(t['before_active'] == active, 'Active set was reset or changed before elimination.')
        snapshot = records[2*(rnd-1)+(1-side)]['snapshot']
        signature = normalized(purchase_signature(snapshot, rnd-1)) if pending else None
        check(t['observed_previous_signature'] == signature, 'Observed signature differs.')
        eliminated = [name for name in active if pending[name] != signature] if pending else []
        active = [name for name in active if name not in eliminated]
        check(t['eliminated'] == eliminated and t['active'] == active, 'Elimination rule differs.')
        check(set(t['predictions']) == set(active), 'Predictions differ from the active catalogue.')
        check(t['fallback'] == (not active), 'Fallback does not match empty catalogue.')
        actual_actions = [e['action'] for e in records[2*rnd+(1-side)]['event'] if e['kind'] == 'action']
        matching = []
        pending = {}
        for name in active:
            prediction = t['predictions'][name]
            state = player_from_snapshot(snapshot)
            for action in prediction['actions']:
                check(apply_action(state, action, rnd, config)['accepted'], 'Model predicted a rejected action.')
            predicted_signature = normalized(purchase_signature(state, rnd))
            check(prediction['signature'] == predicted_signature, 'Predicted signature differs from its actions.')
            pending[name] = predicted_signature
            calls[name] += 1
            check(calls[name] == rnd, 'Retained clone was not advanced once per round.')
            if prediction['actions'] == actual_actions: matching.append(name)
        check(t['call_counts'] == calls, 'Recorded call counts differ.')
        if in_catalogue:
            check(actual_target in active, 'True catalogue member was eliminated.')
            check(actual_target in matching, 'True catalogue forecast differs from the action list.')
            known_exact_rounds += 1
        if len(active) == 1 and not matching: singleton_mismatches.append(rnd)
        details.append(dict(round=rnd, active=list(active), matching_actions=matching, fallback=not active))
    return dict(target_model=actual_target, target_in_selected_catalogue=in_catalogue,
                known_exact_rounds=known_exact_rounds, total_model_calls=sum(calls.values()),
                unpruned_model_calls=len(ids)*row['rounds'], final_model_calls=calls,
                first_singleton_round=next((t['round'] for t in details if len(t['active']) == 1), None),
                first_fallback_round=next((t['round'] for t in details if t['fallback']), None),
                singleton_forecast_mismatch_rounds=singleton_mismatches, rounds=details)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict-audit', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    strict = json.loads(Path(args.strict_audit).read_text())
    inputs = {args.strict_audit: digest(args.strict_audit)}
    sources = set(static_closure({'bot_research.experiments.validation.audit_stateful_catalogue'}))
    sources.add(Path('td_game/balanced.json'))
    source_hashes = {str(p): digest(p) for p in sources}
    primary = {(c['directory'], c['job']) for c in strict['cases']}
    cases = []
    for case in strict['attempts']:
        if case['status'] != 'valid': continue
        path = case['result_path']
        inputs[path] = digest(path)
        check(inputs[path] == strict['input_sha256'][path], 'Result changed after strict audit.')
        row = json.loads(Path(path).read_text())
        replay = row['replay_path']
        inputs[replay] = digest(replay)
        check(inputs[replay] == row['trajectory_sha256'], 'Replay digest differs.')
        records = [json.loads(line) for line in Path(replay).read_text().splitlines()]
        cases.append(dict(result_path=path, primary=(case['directory'], case['job']) in primary,
                          condition=row['condition'], audit=audit_trace(row, records)))
    changed = [p for p, h in {**inputs, **source_hashes}.items() if digest(p) != h]
    check(not changed, 'Audit inputs or sources changed.')
    output = dict(time_utc=now(), input_sha256=inputs, source_sha256=source_hashes,
                  source_changed_during_run=changed, all_passed=True,
                  valid_conditions=strict['valid_conditions'], expected_conditions=strict['expected_conditions'],
                  attempt_counts=strict['attempt_counts'], cases=cases,
                  scope='Signature reconstruction, monotone elimination, recorded call counts and exact true-model actions for targets matching the declared catalogue parameters. Full original-engine replay and policy provenance are separate audits. Outside-catalogue singleton errors are retained, not hidden.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps(dict(all_passed=True, checked_valid_attempts=len(cases), known_target_games=sum(c['audit']['target_in_selected_catalogue'] for c in cases))), flush=True)


if __name__ == '__main__': main()

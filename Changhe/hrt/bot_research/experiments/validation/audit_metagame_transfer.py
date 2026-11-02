"""Exact weighted outcomes against a previously certified policy mixture.

Missing or failed component games retain their full [-1,1] payoff uncertainty.
They are never silently omitted or scored as losses.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now, read_result
from bot_research.experiments.validation.source_closure import static_closure
from bot_research.experiments.validation.summarize_identifying import canonical_replay


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def q(value):
    return Fraction(value['numerator'], value['denominator'])


def encoded(value):
    return {'numerator': value.numerator, 'denominator': value.denominator}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--certificate', required=True)
    parser.add_argument('--original-results', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    hashes = {}
    def load(path):
        path = Path(path)
        hashes[str(path)] = sha(path)
        return json.loads(path.read_text())
    directory = Path(args.input)
    manifest = load(args.manifest)
    certificate = load(args.certificate)
    matrix = load(certificate['matrix_path'])
    if hashes[certificate['matrix_path']] != certificate['matrix_sha256']:
        raise ValueError('The original payoff matrix changed.')
    weights = {item['policy']: q(item['probability']) for item in certificate['support']}
    if sum(weights.values(), Fraction(0)) != 1 or any(w <= 0 for w in weights.values()):
        raise ValueError('Invalid mixture probabilities.')
    declared = {item['spec']: q(item['probability']) for item in manifest['opponents']}
    if weights != declared:
        raise ValueError('Experiment components differ from the certified mixture.')
    original_path = Path(args.original_results)
    hashes[str(original_path)] = sha(original_path)
    if matrix['input_sha256'].get(str(original_path)) != hashes[str(original_path)]:
        raise ValueError('Original round-robin results changed.')
    original = [json.loads(line) for line in original_path.read_text().splitlines()]
    components = {}
    for spec in weights:
        rows = [r for r in original if spec in (r['spec_a'], r['spec_b'])]
        component_sources, missing, changed = {}, [], []
        for path in static_closure({spec.partition(':')[0]}):
            name = str(path)
            old = {r['sources'][name] for r in rows if name in r['sources']}
            if len(old) > 1:
                raise ValueError('A component dependency changed in the original matrix.')
            if not old:
                missing.append(name)
                continue
            expected = next(iter(old))
            component_sources[name] = expected
            if sha(path) != expected:
                changed.append(name)
        components[spec] = {'recorded_dependency_sha256': component_sources,
                            'unattested_static_dependencies': missing,
                            'changed_since_original': changed}
    metadata = load(directory / 'freeze.json')
    jobs = load(directory / 'jobs.json')
    if metadata['manifest_sha256'] != hashes[args.manifest]:
        raise ValueError('The declared manifest differs from the campaign freeze.')
    expected = {(c['id'], o['spec'], side) for c in manifest['candidates']
                for o in manifest['opponents'] for side in (0, 1)}
    found, cases, unresolved = set(), [], []
    counts = defaultdict(Counter)
    for job in jobs:
        c = job['condition']
        identity = (c['candidate_id'], c['opponent_spec'], c['candidate_side'])
        if identity in found or identity not in expected:
            raise ValueError('Duplicate or undeclared condition.')
        found.add(identity)
        if c['initial_state'] != 'standard' or c['engine_seed'] is not None:
            raise ValueError('This comparison requires the original standard condition.')
        result = directory / 'results' / (job['id'] + '.json')
        failure = directory / 'results' / (job['id'] + '.failure.json')
        if failure.exists() or not result.exists():
            unresolved.append({'condition': c, 'failure': load(failure) if failure.exists() else None})
            continue
        hashes[str(result)] = sha(result)
        row = read_result(result, job, metadata['source_sha256'])
        if any(row['bot_errors']) or any(row['rejected_actions']) or row['source_changed_during_match']:
            raise ValueError('Invalid completed game.')
        for name, old in components[c['opponent_spec']]['recorded_dependency_sha256'].items():
            if metadata['source_sha256'].get(name) != old:
                raise ValueError('A frozen component dependency differs from the original policy: ' + name)
            for field in ('source_sha256', 'source_sha256_at_end'):
                # Static closure includes conditional imports. Their frozen
                # bytes must agree even when this game never imports them.
                if name in row[field] and row[field][name] != old:
                    raise ValueError('A loaded component dependency differs from the original policy: ' + name)
        side = c['candidate_side']
        counts[c['candidate_id']][row['candidate_outcome']] += 1
        cases.append({'condition': c, 'outcome': row['candidate_outcome'],
                      'payoff': {'W': 1, 'D': 0, 'L': -1}[row['candidate_outcome']],
                      'hp_candidate_first': row['hp'][::1 if side == 0 else -1],
                      'rounds': row['rounds'], 'runtime_seconds': row['runtime_seconds'],
                      'result_path': str(result), 'replay_path': row['replay_path'],
                      'canonical_replay_sha256': canonical_replay(row['replay_path'], side)})
    if found != expected:
        raise ValueError('Campaign jobs do not cover the declaration.')
    intervals, pairs = [], []
    for candidate in manifest['candidates']:
        selected = [r for r in cases if r['condition']['candidate_id'] == candidate['id']]
        known, completed_weight = Fraction(0), Fraction(0)
        for row in selected:
            weight = weights[row['condition']['opponent_spec']] / 2
            known += weight * row['payoff']
            completed_weight += weight
        missing_weight = 1 - completed_weight
        intervals.append({'candidate': candidate['id'], 'completed_weight': encoded(completed_weight),
                          'payoff_lower': encoded(known - missing_weight),
                          'payoff_upper': encoded(known + missing_weight),
                          'strictly_beats_mixture_even_if_unresolved_lose': known - missing_weight > 0,
                          'complete': not missing_weight})
        for spec in weights:
            group = [r for r in selected if r['condition']['opponent_spec'] == spec]
            pairs.append({'candidate': candidate['id'], 'opponent': spec,
                          'sides': sorted(r['condition']['candidate_side'] for r in group),
                          'same_complete_trajectory': len(group) == 2 and len({r['canonical_replay_sha256'] for r in group}) == 1})
    output = {'time_utc': now(), 'checker_sha256': sha(__file__), 'input_sha256': hashes,
              'components': components, 'source_identity_complete': all(not c['unattested_static_dependencies'] and not c['changed_since_original'] for c in components.values()),
              'valid_completed': len(cases), 'planned': len(jobs), 'unresolved': unresolved,
              'outcomes': {k: dict(v) for k, v in counts.items()}, 'weighted_payoff_intervals': intervals,
              'cases': cases, 'pairs': pairs,
              'scope': 'Candidate payoff against the component mixture, averaged across player assignments. Exact arithmetic on these empirical games, not a population win-rate estimate.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('valid_completed', 'planned', 'source_identity_complete', 'outcomes', 'weighted_payoff_intervals')}))


if __name__ == '__main__':
    main()

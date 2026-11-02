"""Verify predeclared late jobs without importing or invoking any bot policy."""
from copy import deepcopy
import argparse
import json
from pathlib import Path
import sys
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import digest, now
from bot_research.experiments.validation.late_validation import MANIFEST, make_jobs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text())
    original = deepcopy(manifest)
    # An intentionally nonexistent module makes accidental policy loading fail.
    candidate = 'unloaded_reserved_candidate.module:decide'
    jobs = make_jobs(candidate, 'C', manifest, Path('bot_research/runs/validation/unexecuted_late_probe'), True)
    assert len(jobs) == manifest['planned_conditions'] == 72
    assert len({j['id'] for j in jobs}) == len(jobs)
    assert sum(j['condition']['strength_score_eligible'] for j in jobs) == 24
    checks = []
    for a, b in zip(jobs[::2], jobs[1::2]):
        assert a['condition']['candidate_side'] == 0 and b['condition']['candidate_side'] == 1
        assert a['bots'] == b['bots'][::-1] and a['names'] == b['names'][::-1]
        assert a['condition']['opponent'] == b['condition']['opponent']
        if 'prefixes' in a:
            assert a['prefixes'] == b['prefixes'][::-1]
            assert a['condition']['prefix_policy_calls'] == b['condition']['prefix_policy_calls'] == 'skipped'
            assert a['condition']['prefix_lengths_candidate_first'] == [len(p) for p in a['prefixes']]
        checks.append(dict(scenario=a['condition']['scenario'], opponent=a['condition']['opponent'],
                           paired=True, prefix_lengths=[len(p) for p in a.get('prefixes', [])]))
    assert manifest == original
    assert not any(name.startswith('unloaded_reserved_candidate') for name in sys.modules)
    assert not any(name.startswith('bot_research.bots.') for name in sys.modules)
    assert all(digest(name) == sha for name, sha in manifest['source_sha256'].items())
    assert digest(manifest['prefix_check']) == manifest['prefix_check_sha256']
    rejected = False
    try:
        make_jobs(candidate, 'B', manifest, Path('bot_research/runs/validation/unexecuted_late_probe'), True)
    except ValueError:
        rejected = True
    assert rejected
    output = dict(time_utc=now(), all_passed=True, paired_conditions=len(checks), checks=checks,
        policy_modules_loaded=False, games_executed=0, candidate_module_exists=False,
        source_sha256={str(MANIFEST): digest(MANIFEST), __file__.split('/hrt-project/')[-1]: digest(__file__),
                       'bot_research/experiments/validation/late_validation.py': digest('bot_research/experiments/validation/late_validation.py')},
        scope='Job construction, declared input integrity, and candidate-relative seat swaps only; no candidate outcomes and no bot execution.')
    # __file__ may be absolute; the artifact always uses project-relative paths.
    output['source_sha256'] = {str(Path(k).relative_to(Path.cwd())) if Path(k).is_absolute() else k: v
                               for k, v in output['source_sha256'].items()}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('time_utc', 'all_passed', 'paired_conditions', 'games_executed')}))


if __name__ == '__main__':
    main()

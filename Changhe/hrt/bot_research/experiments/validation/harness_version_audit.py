"""Independent static-version and aggregation audit; no strength matches."""
from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import tempfile

from bot_research.harness.match import import_closure, spec_version
from bot_research.harness.tournament import summarize
from bot_research.experiments.validation.artifact_io import atomic_json


def synthetic_row(*, scenario=None, winner=0, changed=False, error=False):
    stats = {'n_rejected': 0, 'bot_errors': []}
    players = [deepcopy(stats), deepcopy(stats)]
    if error:
        players[1]['bot_errors'].append({'round': 1, 'reason': 'synthetic failure'})
    return {'spec_a': 'audit_candidate:decide', 'spec_b': 'audit_opponent:decide',
            'version_a': 'constant_a', 'version_b': 'constant_b', 'candidate_side': 0,
            'winner': winner, 'scenario': scenario, 'rounds': 50,
            'hp_diff_a': 5 if winner == 0 else -5, 'players': players,
            'decide_seconds': [0, 0], 'decide_max_seconds': [0, 0],
            'reason': 'max_rounds', 'source_changed': changed}


def main():
    base = Path('bot_research/experiments/validation')
    with tempfile.TemporaryDirectory(dir=base, prefix='version_fixture_') as temporary:
        fixture = Path(temporary)
        files = {
            '__init__.py': 'from . import support\n',
            'entry.py': 'from .nested import direct\nfrom .support import VALUE\n',
            'support.py': 'VALUE = 1\n',
            'nested/__init__.py': 'from . import direct\n',
            'nested/direct.py': 'from .. import support\n',
            'dynamic.py': 'import importlib\ndef get():\n    return importlib.import_module(__package__ + ".dynamic_leaf")\n',
            'dynamic_leaf.py': 'VALUE = 1\n',
        }
        for relative, text in files.items():
            path = fixture / relative
            path.parent.mkdir(exist_ok=True)
            path.write_text(text)
        name = '.'.join(fixture.resolve().relative_to(Path.cwd()).parts)
        entry = name + '.entry:decide'
        closure = set(import_closure(name + '.entry'))
        expected = {fixture.joinpath(p).resolve() for p in files if p not in ('dynamic.py', 'dynamic_leaf.py')}
        assert expected <= closure
        before = spec_version(entry)
        (fixture / 'support.py').write_text('VALUE = 2\n')
        changed = spec_version(entry)
        assert before != changed
        (fixture / 'support.py').write_text(files['support.py'])
        assert spec_version(entry) == before
        dynamic = name + '.dynamic:decide'
        dynamic_before = spec_version(dynamic)
        (fixture / 'dynamic_leaf.py').write_text('VALUE = 2\n')
        dynamic_after = spec_version(dynamic)
        assert dynamic_before == dynamic_after
        fixture_result = {
            'static_imports_relative_imports_and_package_initializers_included': True,
            'cross_directory_dependency_mutation_changes_version': True,
            'restoring_dependency_restores_version': True,
            'dynamic_import_dependency_is_not_in_static_version': True,
            'fixture_source': files,
            'scope': 'version digests only; no fixture bot was executed',
        }

    target = 'bot_research.bots.counters.forecast_schedule'
    paths = [str(p.relative_to(Path.cwd())) for p in import_closure(target)]
    for required in ('bot_research/bots/counters/snapshots/lead_planner_003.py',
                     'bot_research/bots/economy/frozen/v2/defense_plan.py',
                     'bot_research/bots/economy/frozen/v2/fastsim.py',
                     'bot_research/bots/economy/frozen/v2/threat.py',
                     'bot_research/harness/gamekit.py'):
        assert required in paths

    mixed = summarize([synthetic_row(), synthetic_row(scenario='eco:1', winner=1)])
    merged = next(s for s in mixed.splitlines() if s.startswith('| audit_candidate:decide | audit_opponent:decide |'))
    assert '| 2 | 1 | 0 | 1 |' in merged
    invalid = summarize([synthetic_row(changed=True), synthetic_row(error=True)])
    scored = next(s for s in invalid.splitlines() if s.startswith('| audit_candidate:decide | audit_opponent:decide |'))
    assert '| 2 | 2 | 0 | 0 |' in scored
    result = {
        'time_utc': datetime.now(timezone.utc).isoformat(),
        'purpose': 'independent version and synthetic aggregation audit; not match evidence',
        'sources': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in
                    (Path('bot_research/harness/match.py'), Path('bot_research/harness/tournament.py'), Path(__file__).relative_to(Path.cwd()))},
        'static_version_checks': fixture_result,
        'real_counter_import_closure': paths,
        'scenario_pooling_summary': mixed,
        'invalid_rows_still_scored_summary': invalid,
        'conclusions': {'static_dependency_fix_passes': True,
                        'summary_pools_scenarios': True,
                        'summary_counts_source_drift_and_opponent_error_rows': True},
    }
    atomic_json('bot_research/runs/validation/harness-audit-003.json', result, exclusive=True)
    print(json.dumps(result['conclusions'], sort_keys=True))


if __name__ == '__main__':
    main()

"""Check model persistence and call-order guards without running game combat."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from bot_research.bots.counters.public_factory import PublicFactoryModel
from bot_research.bots.counters.stateful_public import PersistentFactoryModel
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


class CountingPolicy:
    def __init__(self):
        self.calls = 0

    def __call__(self, observation):
        self.calls += 1
        return [{'op': 'buy_factory'} for _ in range(self.calls)]


def make_fixture():
    return CountingPolicy()


def main():
    spec = 'bot_research.experiments.validation.check_persistent_factory:@make_fixture'
    persistent = PersistentFactoryModel(spec)
    fresh = PublicFactoryModel(spec)
    checks = []

    def check(name, condition):
        checks.append({'name': name, 'passed': bool(condition)})
        if not condition:
            raise AssertionError(name)

    def rejects(name, model, observation):
        try:
            model(observation)
        except ValueError:
            check(name, True)
        else:
            check(name, False)

    check('first_outputs_equal', persistent({'round': 1, 'player': 0}) == fresh({'round': 1, 'player': 0}))
    check('persistent_advances', len(persistent({'round': 2, 'player': 0})) == 2)
    check('fresh_resets', len(fresh({'round': 2, 'player': 0})) == 1)
    rejects('duplicate_round_rejected', persistent, {'round': 2, 'player': 0})
    rejects('skipped_round_rejected', persistent, {'round': 4, 'player': 0})
    rejects('changed_side_rejected', persistent, {'round': 3, 'player': 1})
    check('rejections_do_not_advance_policy', len(persistent({'round': 3, 'player': 0})) == 3)
    second = PersistentFactoryModel(spec)
    rejects('cannot_begin_after_round_one', second, {'round': 2, 'player': 1})
    check('new_game_independent', len(second({'round': 1, 'player': 1})) == 1)
    check('first_game_state_independent', len(persistent({'round': 4, 'player': 0})) == 4)
    sources = static_closure({'bot_research.experiments.validation.check_persistent_factory'})
    out = {'time_utc': datetime.now(timezone.utc).isoformat(), 'checks': checks,
           'all_passed': all(c['passed'] for c in checks),
           'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
           'scope': 'Pure policy-state component checks. No game outcome or bot-strength claim.'}
    atomic_json(Path('bot_research/runs/validation/persistent-factory-check-001.json'), out, exclusive=True)
    print(json.dumps({'checks': len(checks), 'all_passed': out['all_passed']}))


if __name__ == '__main__':
    main()

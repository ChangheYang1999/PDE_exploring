"""Cross-check the independent loop against the unmodified official runner."""
from __future__ import annotations
import json
import tempfile
from pathlib import Path
from td_game.config import balanced_config
from td_game.runner import run_match
from bot_research.bots.counters.archetypes import make
from bot_research.experiments.validation.evaluate import evaluate


def main():
    output = Path('bot_research/runs/validation/evaluator-crosscheck-001.json')
    pairs = [('rush_t1', 'rush_t2'), ('splash_t2', 'eco5_t3')]
    results = []
    with tempfile.TemporaryDirectory(prefix='validation-crosscheck-') as directory:
        for i, pair in enumerate(pairs):
            independent_path = Path(directory) / f'independent-{i}.jsonl'
            official_path = Path(directory) / f'official-{i}.jsonl'
            result = evaluate(pair, replay_path=str(independent_path))
            official = run_match(balanced_config(), [make(p) for p in pair], pair, official_path)
            left = [json.loads(line) for line in independent_path.read_text().splitlines()]
            right = [json.loads(line) for line in official_path.read_text().splitlines()]
            assert left == right, pair
            assert result['hp'] == [p.hp for p in official.players], pair
            assert result['result'] == official.result, pair
            assert not result['source_changed_during_match']
            repeated = evaluate(pair)
            assert repeated['trajectory_sha256'] == result['trajectory_sha256'], pair
            results.append({'pair': pair, 'records_equal': True, 'record_count': len(left),
                            'trajectory_sha256': result['trajectory_sha256'],
                            'deterministic_repeat_identical': True, 'hp': result['hp'],
                            'result': result['result']})
    with output.open('x') as stream:
        json.dump(results, stream, indent=2)
        stream.write('\n')
    print(json.dumps(results))


if __name__ == '__main__':
    main()

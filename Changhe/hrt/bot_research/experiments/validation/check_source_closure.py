"""Dependency freeze checks with isolated synthetic source files; no games."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import tempfile
from datetime import datetime, timezone
from bot_research.experiments.validation.source_closure import static_closure
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    args=p.parse_args()
    checks={}
    with tempfile.TemporaryDirectory(dir='bot_research/experiments/validation', prefix='closure_fixture_') as tmp:
        root=Path(tmp)
        sources={
            'bot_research/__init__.py':'VALUE = 1\n',
            'bot_research/pkg/__init__.py':'from . import leaf\n',
            'bot_research/pkg/leaf.py':'VALUE = 1\n',
            'bot_research/pkg/sub/__init__.py':'\n',
            'bot_research/pkg/sub/entry.py':'from .. import leaf\nfrom . import sibling\nfrom bot_research.util import value\n',
            'bot_research/pkg/sub/sibling.py':'from ..leaf import VALUE\n',
            'bot_research/util.py':'value = 3\n',
            'bot_research/unrelated.py':'VALUE = 0\n',
            'bot_research/dynamic.py':'import importlib\nvalue=importlib.import_module("bot_research.runtime_leaf")\n',
            'bot_research/runtime_leaf.py':'VALUE = 6\n'}
        for name,text in sources.items():
            path=root/name
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(text)
        def freeze(modules):
            return {str(path):hashlib.sha256((root/path).read_bytes()).hexdigest()
                    for path in static_closure(modules,root)}
        seeds=['bot_research.pkg.sub.entry']
        before=freeze(seeds)
        expected={name for name in sources if '/pkg/' in name} | {'bot_research/__init__.py','bot_research/util.py'}
        checks['direct_relative_and_initializers']=set(before)==expected
        (root/'bot_research/unrelated.py').write_text('VALUE = 2\n')
        checks['unrelated_change_ignored']=freeze(seeds)==before
        leaf=root/'bot_research/pkg/leaf.py'
        leaf.write_text('VALUE = 2\n')
        checks['relevant_change_detected']=freeze(seeds)!=before
        leaf.write_text(sources['bot_research/pkg/leaf.py'])
        checks['restore_restores_hashes']=freeze(seeds)==before
        (root/'bot_research/pkg/sub/newleaf.py').write_text('VALUE=9\n')
        checks['unimported_new_sibling_ignored']=freeze(seeds)==before
        entry=root/'bot_research/pkg/sub/entry.py'
        entry.write_text(sources['bot_research/pkg/sub/entry.py']+'from . import newleaf\n')
        checks['new_dependency_included']='bot_research/pkg/sub/newleaf.py' in freeze(seeds)
        dynamic=freeze(['bot_research.dynamic'])
        checks['dynamic_dependency_not_inferred']='bot_research/runtime_leaf.py' not in dynamic
        declared=freeze(['bot_research.dynamic','bot_research.runtime_leaf'])
        checks['declared_dynamic_root_included']='bot_research/runtime_leaf.py' in declared
    real=set(map(str,static_closure(['bot_research.experiments.validation.isolated_match',
                                   'bot_research.bots.counters.known_policy'])))
    checks['real_counter_frozen_models_included']=all(path in real for path in (
        'bot_research/bots/counters/snapshots/lead_planner_003.py',
        'bot_research/bots/defense/frozen/v6/fortress.py',
        'bot_research/bots/economy/frozen/v4/econ.py',
        'td_game/engine.py','td_game/combat.py'))
    result={'time_utc':datetime.now(timezone.utc).isoformat(),'checks':checks,
            'all_passed':all(checks.values()),'real_closure':sorted(real),
            'interpretation':'Static import freeze fixtures only; no heldout games.'}
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps(result,sort_keys=True))
    assert result['all_passed']


if __name__=='__main__':
    main()

"""Declare 34 new games and identify all 76 reused records before new play."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure
E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
ORDER = ['B', 'C', 'D', 'G', 'H', 'I', 'J', 'L', 'M', 'N']


def main():
    stamp = datetime.now(timezone.utc).isoformat()
    parents = [E/'analysis/eight_policy_game/verification/full_games.json',
               E/'analysis/screened_roster_guarded_policy/verification/full_check.json',
               E/'analysis/screened_guard_transfer/verification/full_check.json',
               E/'analysis/ten_policy_game/verification/arithmetic_components.json']
    policies = json.loads((E/'shared-prefix-campaigns-001.json').read_text())['policies']
    policies['L'] = dict(id='L', spec='bot_research.bots.counters.wall_signal_repair:@make')
    policies['M'] = dict(id='M', spec='bot_research.bots.counters.screened_roster_guarded:@make')
    policies['N'] = dict(id='N', spec='bot_research.experiments.lead.frozen.best_v9e:@make?attack_share=1.0&catch_up_share=0.5')
    policies = {k: dict(id=k, spec=policies[k]['spec']) for k in ORDER}
    reused_extra = []
    for opponent, campaign in [('B', 'screened-roster-guarded-fortress38-001'),
                              ('N', 'screened-guard-transfer-00-001')]:
        for side in (0, 1):
            reused_extra.append(dict(a='M', b=opponent, result=str(R/campaign/'results'/f'case{side:04d}.json')))
    modules = ['declare_ten_policy_game', 'publish_ten_policy_game', 'run_data_development',
               'audit_development_strict', 'replay_audit', 'audit_data_archives',
               'check_fixed_game_histories', 'summarize_plain_campaign', 'finite_table_certificate']
    modules = {'bot_research.experiments.validation.' + m for m in modules}
    modules |= {p['spec'].partition(':')[0] for p in policies.values()}
    paths = set(static_closure(modules)) | {E/'analysis/ten_policy_game/PROOF.md',
                                            Path('td_game/balanced.json'), Path('configs/balanced.json')}
    for name in ('early_wall_guard', 'maze_layouts', 'screened_guard', 'staged_guards', 'screened_roster_guard'):
        paths.add(Path('bot_research/bots/counters/data')/(name+'_001.json'))
    assert Path('bot_research/bots/best.py') not in paths
    inputs = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    campaigns = []
    for i, (a, opponents) in enumerate([('M', ['C', 'D', 'G', 'H']),
                                       ('M', ['I', 'J', 'L', 'M']),
                                       ('N', ['B', 'C', 'D', 'G']),
                                       ('N', ['H', 'I', 'J', 'L', 'N'])]):
        name = f'ten-policy-extension-{i:02d}-001'
        manifest = dict(declared_utc=stamp, candidates=[policies[a]],
                        opponents=[policies[b] for b in opponents], input_sha256=inputs,
                        purpose='Selected fixed ten-policy table extension; no reserved pool D use.')
        atomic_json(E/(name+'.json'), manifest, exclusive=True)
        campaigns.append(dict(name=name, a=a, opponents=opponents, expected=2*len(opponents)))
    declaration = dict(declared_utc=stamp, order=ORDER, policies=policies, campaigns=campaigns,
                       new_games=34, reused_games=76, reused_extra=reused_extra,
                       input_sha256=inputs,
                       parent_sha256={str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in parents})
    atomic_json(E/'ten-policy-game-declaration-001.json', declaration, exclusive=True)
    print(json.dumps(dict(time_utc=stamp, new_games=34, reused_games=76, pins=len(inputs))))


if __name__ == '__main__':
    main()

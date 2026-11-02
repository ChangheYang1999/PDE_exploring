"""Require actual engine and declared bot entries in source attestations."""
from bot_research.experiments.validation.source_closure import module_file


CORE_SOURCES = frozenset({
    'td_game/engine.py', 'td_game/combat.py', 'td_game/actions.py',
    'td_game/config.py', 'td_game/state.py', 'td_game/pathfinding.py',
    'td_game/balanced.json', 'td_bots/protocol.py',
    'bot_research/experiments/validation/evaluate.py',
})


def validate_required_sources(result, job, frozen):
    required = set(CORE_SOURCES)
    if len(job.get('bots', [])) != 2:
        raise ValueError('A source-attested match must declare both bots.')
    for bot in job['bots']:
        if 'spec' in bot:
            path = module_file(bot['spec'].partition(':')[0])
        elif 'profile' in bot:
            path = module_file('bot_research.bots.counters.archetypes')
        else:
            raise ValueError('Unknown bot description.')
        if path is None:
            raise ValueError('Declared bot entry module has no local source.')
        required.add(str(path))
    if required - set(frozen):
        raise ValueError('Freeze omits required engine or bot sources.')
    for field in ('source_sha256', 'source_sha256_at_end'):
        actual = result.get(field)
        if not isinstance(actual, dict) or not actual:
            raise ValueError('Empty or missing source attestation: ' + field)
        absent = sorted(required - set(actual))
        if absent:
            raise ValueError('Source attestation omits required files: ' + repr(absent))

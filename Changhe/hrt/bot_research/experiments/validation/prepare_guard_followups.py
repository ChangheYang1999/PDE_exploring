"""Register two development transfers without using reserved conditions."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qsl, urlencode
from bot_research.experiments.validation.artifact_io import atomic_json


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def spec(entry, params):
    return entry + '?' + urlencode({k: json.dumps(v, separators=(',', ':')) for k, v in params.items()})


base = Path('bot_research/experiments/validation')
guard_path = base/'guard-geometry-transfer-001.json'
lead_path = base/'lead-seventeen-mid5-standard-001.json'
guards = json.loads(guard_path.read_text())
lead = json.loads(lead_path.read_text())
stamp = datetime.now(timezone.utc).isoformat()
input_sha256 = {str(p): digest(p) for p in (guard_path, lead_path)}
models = []
for tier, rnd in [('tier3', 3), ('tier3', 5), ('tier4', 5), ('tier4', 6)]:
    models.append(dict(id=f'half_budget_{tier}_r{rnd}', spec=spec(
        'bot_research.bots.counters.budget_timing:@make',
        dict(tier=tier, attack_round=rnd, budget_fraction=0.5))))
models += [c for c in guards['candidates'] if c['id'].startswith('corner_')]
economy = next(c for c in guards['opponents'] if c['id']=='economy17')
models.append(dict(id='direct_economy17', spec=economy['spec']))
assert len(models)==10
atomic_json(base/'lead-seventeen-model-free-001.json', dict(
    declared_utc=stamp, candidates=models, opponents=lead['opponents'],
    purpose='Four half-budget timings and five corner-gun openings, plus direct economy17, against the Lead17 revision in both assignments: 20 development games.',
    hypothesis='The round-three tier3 counter transfers without an exact opponent model; cheap guarded pokes may retain a final HP lead.',
    input_sha256=input_sha256,
    scope='Development transfer selected from disclosed earlier results. No reserved conditions and no universal strength inference.'), exclusive=True)

candidates = []
for roster, label in [(['tier1'], 't1'), (['tier2'], 't2')]:
    for x, hold in [(3, None), (9, None), (10, None), (9, 11)]:
        candidates.append(dict(id=f'x{x}_{label}_hold{hold}', spec=spec(
            'bot_research.bots.counters.guard_geometry:@make',
            dict(roster=roster, x=x, y=1, parameters=dict(foreign_attack_from=hold)))))
atomic_json(base/'guard-hold-coordinate-001.json', dict(
    declared_utc=stamp, candidates=candidates, opponents=guards['opponents'],
    purpose='Separate the guarded opening coordinate and inherited foreign-map attack hold, for one-tier1 and one-tier2 openings against V4, economy17 and fortress24 in both assignments: 48 new development games.',
    hypothesis='A fresh economy continuation treats the opening gun as foreign, so disabling that attack hold may change the early leak exchanges. The alternative zero-leak opening gun at (9,1) may preserve more useful later defense than (10,1).',
    previous_controls=['bot_research/runs/validation/guard-roster-transfer-002', 'bot_research/runs/validation/guard-geometry-transfer-001'],
    input_sha256=input_sha256,
    scope='Coordinate (9,1) had zero opening damage in the exhaustive one-gun check. Only the two small previously useful rosters are selected. This is development tuning, not a holdout.'), exclusive=True)
print(json.dumps(dict(declared_utc=stamp, lead17_conditions=20, guard_intervention_conditions=48)))

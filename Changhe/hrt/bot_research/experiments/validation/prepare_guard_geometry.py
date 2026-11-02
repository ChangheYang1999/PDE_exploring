"""Declare geometry transfer only after both component checks pass."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


checks = ['bot_research/runs/validation/guard-geometry-component-001.json',
          'bot_research/runs/validation/guard-geometry-rosters-001.json']
for path in checks:
    data = json.loads(Path(path).read_text())
    assert data['all_passed']
    assert all(digest(p)==expected for p,expected in data['source_sha256'].items())
base = json.loads(Path('bot_research/experiments/validation/guard-roster-transfer-002.json').read_text())
candidates = [dict(id=c['id'].replace('guard_','corner_'),
                   spec=c['spec'].replace('counters.guard_roster:', 'counters.guard_geometry:'))
              for c in base['candidates'] if c['id'].startswith('guard_')]
original = next(c for c in base['candidates'] if c['id']=='guard_t1')
candidates.append(dict(id='original_t1_control',spec=original['spec'].replace('counters.guard_roster:',
    'counters.guard_geometry:')+'&x=3&y=1'))
paths = ['bot_research/bots/counters/guard_geometry.py',
         'bot_research/experiments/validation/check_guard_geometry.py',
         'bot_research/experiments/validation/search_guard_geometry.py',
         'bot_research/experiments/validation/prepare_guard_geometry.py', *checks]
out = dict(declared_utc=datetime.now(timezone.utc).isoformat(),candidates=candidates,
    opponents=base['opponents'],purpose='Five opening rosters with a corner gun, plus the original-coordinate one-tier1 control, against V4, economy17 and fortress24 in both seats: 36 development games.',
    hypothesis='The same-cost corner gun blocks the third opening tier1 and improves full-game results without an extra factory sacrifice.',
    scope='Geometry selected from a source argument and original-engine opening enumeration. All five prior rosters retained; no held-out conditions. Fortress24 has a three-second internal cutoff.',
    control_campaign='bot_research/runs/validation/guard-roster-transfer-002',
    source_sha256={p:digest(p) for p in paths})
atomic_json('bot_research/experiments/validation/guard-geometry-transfer-001.json',out,exclusive=True)
print(json.dumps(dict(declared_utc=out['declared_utc'],planned=36)))

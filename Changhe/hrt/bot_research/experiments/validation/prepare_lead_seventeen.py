"""Snapshot the public Lead17 revision and declare a timing-counter screen.

Only research-policy imports are rewritten. Engine sources stay unchanged.
The original and copied bytes are registered before any games are run.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from urllib.parse import parse_qsl, urlencode
from bot_research.experiments.validation.artifact_io import atomic_json


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def spec(entry, params):
    return entry+'?'+urlencode({k:json.dumps(v,separators=(',',':')) for k,v in params.items()})


def main():
    base=Path('bot_research/bots/counters/snapshots')
    original15=Path('bot_research/experiments/lead/v15.py')
    copied15=base/'lead_fifteen_001.py'
    assert original15.read_bytes()==copied15.read_bytes()
    changes=[
        ('v16.py','lead_sixteen_001.py','from bot_research.experiments.lead import v15',
         'from bot_research.bots.counters.snapshots import lead_fifteen_001 as v15'),
        ('v17.py','lead_seventeen_001.py','from bot_research.experiments.lead import v15, v16',
         'from bot_research.bots.counters.snapshots import lead_fifteen_001 as v15\nfrom bot_research.bots.counters.snapshots import lead_sixteen_001 as v16')]
    originals={str(original15):digest(original15)}
    copies={str(copied15):digest(copied15)}
    rewrites=[]
    for srcname,dstname,before,after in changes:
        src=Path('bot_research/experiments/lead')/srcname
        dst=base/dstname
        contents=src.read_text()
        assert contents.count(before)==1
        originals[str(src)]=digest(src)
        with dst.open('x') as f:
            f.write(contents.replace(before,after))
        copies[str(dst)]=digest(dst)
        rewrites.append(dict(source=str(src),copy=str(dst),before=before,after=after))
    assert all(digest(p)==sha for p,sha in originals.items())
    params=dict(big_threat=100,gun_cap=120,poke_until=3,poke_reactive='turret',
                big_partial=True,r1_poke=3,attack_mode='adaptive',fortress_n=4,
                immune_attack=True,mid_until=5,foreign_policy='econ17')
    model='bot_research.bots.counters.snapshots.lead_seventeen_001:@make'
    old_path=Path('bot_research/experiments/validation/lead-fifteen-V4-standard-001.json')
    old=json.loads(old_path.read_text())
    candidates=[]
    for row in old['candidates']:
        entry,_,query=row['spec'].partition('?')
        options={k:json.loads(v) for k,v in parse_qsl(query)}
        options.update(model_spec=model,model_parameters=params)
        candidates.append(dict(id=row['id'],spec=spec(entry,options)))
    out=dict(declared_utc=datetime.now(timezone.utc).isoformat(),candidates=candidates,
        opponents=[dict(id='lead17_mid5',spec=spec(model,params))],
        purpose='Transfer the thirteen predeclared timing/schedule counters to the Lead17 early-insurance revision, both assignments: 26 standard-start development games.',
        hypothesis='Adding mid-tier insurance through round five removes some tier3 windows but may leave tier4 or later windows.',
        source_family=str(old_path),source_family_sha256=digest(old_path),
        original_source_sha256=originals,snapshot_sha256=copies,import_rewrites=rewrites,
        scope='Public revision snapshot, not final candidate validation. Choices inherited from the prior V4 matrix; no reserved opponents or scenarios.')
    atomic_json('bot_research/experiments/validation/lead-seventeen-mid5-standard-001.json',out,exclusive=True)
    print(json.dumps(dict(declared_utc=out['declared_utc'],games=26,snapshot_sha256=copies)))


if __name__=='__main__':
    main()

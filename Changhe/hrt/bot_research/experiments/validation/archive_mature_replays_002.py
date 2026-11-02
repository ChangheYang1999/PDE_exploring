"""Losslessly archive closed early replays while preserving exact restoration."""
from datetime import datetime,timezone
from pathlib import Path
import gzip,hashlib,json,os
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
NAMES=['best-v9b-free-scenarios-fullretry450-001','guard-continuation-econ19-001',
'lead-thirteen-fortress4-001','compiled-transfer-001','lead-fifteen-V4-free-scenarios-001',
'lead-thirteen-splash-001','identifier-transfer-001-shard0','identifier-transfer-001-shard1',
'identifier-transfer-001-shard2','best-v9a-targeted-001-shard0','best-v9a-targeted-001-shard1',
'lead-nine-roster-ablation-001-shard0','lead-nine-roster-ablation-001-shard1',
'lead-nine-bluff-001-shard0','lead-nine-bluff-001-shard1','fortress15-forecast-001',
'passive-guard-grid-001']
def digest(b):return hashlib.sha256(b).hexdigest()
def main():
    protected=set();pins={}
    # Keep all active/final and recent counter-chain inputs directly readable.
    paths=[E/name for name in ('terminal-candidate-declaration-001.json','wall-prefix-selector-001.json',
        'wall-prefix-selector-checker-amendment-001.json','delayed-wall-counter-001.json',
        'reserved-wall-counter-001.json','support-only-certificate-001.json')]
    paths += [E/'analysis'/name/'verification/full_games.json' for name in ('wall_prefix_selector','delayed_wall_counter','reserved_wall_counter')]
    paths += [E/'analysis/support_only_certificate/verification/full_check.json']
    for p in paths:
        d=json.loads(p.read_text());protected.update(d.get('input_sha256',{}));pins[str(p)]=digest(p.read_bytes())
    files=[];skipped=[]
    for name in NAMES:
        for p in sorted((R/name/'replays').glob('*.jsonl')):
            if str(p) in protected:skipped.append(str(p));continue
            target=p.with_suffix(p.suffix+'.gz')
            assert not target.exists(),str(target)
            original=p.read_bytes();compressed=gzip.compress(original,compresslevel=6,mtime=0)
            with target.open('xb') as f:f.write(compressed);f.flush();os.fsync(f.fileno())
            restored=gzip.decompress(target.read_bytes())
            assert restored==original
            files.append(dict(original_path=str(p),archived_path=str(target),original_bytes=len(original),
                archived_bytes=len(compressed),original_sha256=digest(original),archived_sha256=digest(compressed)))
    stamp=datetime.now(timezone.utc).isoformat()
    manifest=R/'archived-mature-replays-002.json'
    atomic_json(manifest,dict(time_utc=stamp,files=files,protected_inputs_skipped=skipped,
        declaration_sha256=pins,archive_program_sha256=digest(Path(__file__).read_bytes()),
        scope='Lossless archive of closed early replay streams; original hashes preserved; no result or source changed.'),exclusive=True)
    # Publish complete restoration metadata before removing redundant originals.
    for r in files:
        p=Path(r['original_path']);a=Path(r['archived_path'])
        assert digest(p.read_bytes())==r['original_sha256'] and digest(a.read_bytes())==r['archived_sha256']
        p.unlink()
    saved=sum(x['original_bytes']-x['archived_bytes'] for x in files)
    text=f'''# Closed replay archive 002

Recorded {stamp}. Archived {len(files)} closed early replay streams, saving {saved} bytes. The gzip stream of each replay decompresses byte for byte to its original hash; the original and compressed hashes are in `archived-mature-replays-002.json`. Current terminal and counter-chain inputs were excluded. No result, source or game record content was edited.

Restore a named original replay before running an older tool that requires its uncompressed path, from the project root:

```sh
PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" .venv/bin/python -B -m bot_research.experiments.validation.restore_archived_replay --manifest bot_research/runs/validation/archived-mature-replays-002.json --replay ORIGINAL_RELATIVE_PATH
```

Replace `ORIGINAL_RELATIVE_PATH` with one `original_path` entry in the manifest. Restoration verifies both hashes and refuses to overwrite an existing file. Archive-aware audit tools can read the compressed streams directly.
'''
    with (R/'ARCHIVED_MATURE_REPLAYS_002.md').open('x') as f:f.write(text)
    print(json.dumps(dict(time_utc=stamp,files=len(files),saved_bytes=saved,protected_skipped=len(skipped))))
if __name__=='__main__':main()

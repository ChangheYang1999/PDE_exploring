"""Inventory owned artifacts and detect absolute local paths in text evidence."""
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args=parser.parse_args()
    roots=[Path('bot_research/bots/counters'),Path('bot_research/experiments/validation'),
           Path('bot_research/runs/validation'),Path('bot_research/notes/validation.md')]
    pattern=re.compile(r'(?<![A-Za-z0-9_.-])/(?:'+ '|'.join(('mnt','home','efs','tmp'))+r')(?:/|\b)')
    matched=[]
    inventory={}
    checked=0
    for root in roots:
        files=0
        size=0
        for path in ([root] if root.is_file() else root.rglob('*')):
            if not path.is_file():
                continue
            files+=1
            size+=path.stat().st_size
            if path.suffix.lower() in ('.py','.json','.jsonl','.md','.txt','.log','.out','.csv'):
                checked+=1
                try:
                    with path.open() as f:
                        for number,line in enumerate(f,1):
                            if pattern.search(line):
                                matched.append({'path':str(path),'line':number})
                                break
                except UnicodeError:
                    matched.append({'path':str(path),'issue':'non-text content with text suffix'})
        inventory[str(root)]={'files':files,'bytes':size}
    lane=Path.cwd().parent/'hrt-w3'
    lane_bytes=sum(p.stat().st_size for p in lane.rglob('*') if p.is_file())
    free=shutil.disk_usage('.').free
    out={'time_utc':datetime.now(timezone.utc).isoformat(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'owned_project_files':inventory,'lane_bytes':lane_bytes,'filesystem_free_bytes':free,
         'scanned_text_files':checked,'absolute_path_matches':matched,
         'scope':'Owned project text artifacts only. Active logs can grow after this check; lane files are included in byte accounting, not publication text scans.'}
    atomic_json(Path(args.output),out,exclusive=True)
    print(json.dumps(out))
    if matched or free<20_000_000_000 or sum(v['bytes'] for v in inventory.values())+lane_bytes>=3_000_000_000:
        raise SystemExit(2)


if __name__=='__main__':
    main()

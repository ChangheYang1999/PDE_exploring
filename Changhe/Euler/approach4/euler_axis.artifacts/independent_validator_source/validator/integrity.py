#!/usr/bin/env python3
"""Write or check a lane-local, explicit SHA256 manifest."""
import argparse,datetime,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
EXCLUDE={'.venv','__pycache__','cache','matplotlib','tmp','.git','shifts'}

def files():
    selected=[]
    for p in ROOT.rglob('*'):
        rel=p.relative_to(ROOT)
        if p.is_file() and not any(part in EXCLUDE for part in rel.parts) and p.name not in ['INTEGRITY.json','INTEGRITY_CHECK.json']:
            selected.append(p)
    return sorted(selected)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    manifest=ROOT/'INTEGRITY.json'
    if args.check:
        data=json.loads(manifest.read_text());bad=[]
        for rel,info in data['files'].items():
            p=ROOT/rel
            if not p.exists():bad.append({'path':rel,'reason':'missing'})
            elif hashlib.sha256(p.read_bytes()).hexdigest()!=info['sha256']:bad.append({'path':rel,'reason':'hash mismatch'})
        print(json.dumps({'checked':len(data['files']),'mismatches':bad}));raise SystemExit(bool(bad))
    data={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'scope':'Snapshot of lane-owned files excluding virtualenv, caches, shift logs and this manifest.',
          'files':{str(p.relative_to(ROOT)):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in files()}}
    manifest.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps({'manifest':str(manifest),'files':len(data['files'])}))
if __name__=='__main__':main()

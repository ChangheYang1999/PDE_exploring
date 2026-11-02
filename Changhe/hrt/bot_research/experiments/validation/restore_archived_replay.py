"""Restore one archived replay to its original path, after verifying both hashes."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os
from pathlib import Path

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--manifest',default='bot_research/runs/validation/archived-poolA-replays-001.json')
 p.add_argument('--replay',required=True,help='Original project-relative replay path from the manifest')
 a=p.parse_args();rows=json.loads(Path(a.manifest).read_text())['files']
 matches=[r for r in rows if r['original_path']==a.replay]
 if len(matches)!=1:raise SystemExit('Replay is not uniquely listed in the archive manifest')
 r=matches[0];target=Path(r['original_path']);archive=Path(r['archived_path'])
 for q in (target,archive):
  if q.is_absolute() or '..' in q.parts or not str(q).startswith('bot_research/runs/validation/'):
   raise SystemExit('Unexpected archive path')
 if target.exists():raise SystemExit('Refusing to overwrite an existing replay')
 if hashlib.sha256(archive.read_bytes()).hexdigest()!=r['archived_sha256']:raise SystemExit('Compressed hash mismatch')
 free=os.statvfs(target.parent);available=free.f_bavail*free.f_frsize
 if available<r['original_bytes']+20_000_000_000:raise SystemExit('Insufficient free disk headroom')
 # Read and verify fully before publishing. Maximum original file here is 39 MB.
 data=gzip.decompress(archive.read_bytes())
 if len(data)!=r['original_bytes'] or hashlib.sha256(data).hexdigest()!=r['original_sha256']:raise SystemExit('Original replay hash mismatch')
 with target.open('xb') as f:f.write(data)
 print(json.dumps(dict(restored=str(target),bytes=len(data),sha256=r['original_sha256'])))
if __name__=='__main__':main()

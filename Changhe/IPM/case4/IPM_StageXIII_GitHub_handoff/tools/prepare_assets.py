#!/usr/bin/env python3
"""Restore exact hash-bound compressed coordinate inputs, without numerical imports."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for b in iter(lambda:stream.read(1048576),b''):h.update(b)
    return h.hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=ROOT);a=p.parse_args()
    root=a.root.resolve();record=json.loads((root/'metadata/assets.json').read_text());results=[]
    for asset in record['assets']:
        src=root/asset['compressed'];dst=root/asset['destination']
        if sha(src)!=asset['compressed_sha256']:raise ValueError('Compressed asset changed')
        if dst.exists():
            if sha(dst)!=asset['sha256']:raise ValueError('Existing input differs; refusing overwrite')
            results.append({'path':asset['destination'],'status':'already_verified'});continue
        dst.parent.mkdir(parents=True,exist_ok=True);temporary=dst.with_name(dst.name+'.asset_partial')
        if temporary.exists():raise ValueError('Preserve incomplete asset; use a clean checkout')
        with gzip.open(src,'rb') as source,temporary.open('xb') as target:
            for b in iter(lambda:source.read(1048576),b''):target.write(b)
        if sha(temporary)!=asset['sha256'] or temporary.stat().st_size!=asset['bytes']:
            raise ValueError('Decompressed asset differs')
        temporary.rename(dst);results.append({'path':asset['destination'],'status':'restored_exact_bytes'})
    print(json.dumps({'passed':True,'assets':results},indent=2))


if __name__=='__main__':main()

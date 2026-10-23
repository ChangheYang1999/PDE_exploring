#!/usr/bin/env python3
"""Archive full current derivative-audit arrays separately from Git; no computation."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import tarfile


def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for b in iter(lambda:stream.read(1048576),b''):h.update(b)
    return h.hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();src=a.source_root.resolve()/'independent_assessment_20261022_2313/results/stationarity278_01'
    check=json.loads((src/'checks.json').read_text())
    if not check['completed'] or not check['selected_derivative_checks_passed']:
        raise ValueError('Complete current derivative assessment required')
    output=a.output.resolve();output.parent.mkdir(parents=True,exist_ok=True)
    if output.exists():raise ValueError('Preserve existing artifact')
    rows=[{'path':'stationarity/'+str(f.relative_to(src)),'bytes':f.stat().st_size,'sha256':sha(f)} for f in sorted(src.rglob('*')) if f.is_file()]
    manifest=output.with_suffix(output.suffix+'.files.json');manifest.write_text(json.dumps({'files':rows,'optional':True,'required_for_resume':False,'scope':'Complete accepted278 derivative-audit arrays and selected probe leaves; no redundant optimization checkpoints.'},indent=2)+'\n')
    with output.open('xb') as raw,gzip.GzipFile(filename='',fileobj=raw,mode='wb',compresslevel=1,mtime=0) as z,tarfile.open(fileobj=z,mode='w|',format=tarfile.PAX_FORMAT) as tar:
        for row in rows:
            f=src/Path(row['path']).relative_to('stationarity');info=tar.gettarinfo(str(f),row['path']);info.uid=info.gid=0;info.uname=info.gname=''
            with f.open('rb') as data:tar.addfile(info,data)
        info=tar.gettarinfo(str(manifest),'EVIDENCE_FILES.json');info.uid=info.gid=0;info.uname=info.gname=''
        with manifest.open('rb') as data:tar.addfile(info,data)
    record={'filename':output.name,'bytes':output.stat().st_size,'sha256':sha(output),'files':len(rows),'uncompressed_bytes':sum(r['bytes'] for r in rows),'optional':True,'required_for_reconstruction':False,'required_for_independent_recomputation':False,'required_for_resume':False,'purpose':'Inspect the original complete derivative-audit matrices/probe arrays without rerunning the audit. Main repository already supplies reproducible source and scalar results.'}
    output.with_suffix(output.suffix+'.sha256').write_text(record['sha256']+'  '+output.name+'\n')
    output.with_suffix(output.suffix+'.metadata.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))


if __name__=='__main__':main()

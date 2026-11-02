"""Losslessly compress explicit failed-attempt partial logs, retaining accounting."""
import argparse,gzip,hashlib,json,os,shutil,time
from datetime import datetime,timezone
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json


def digest_file(path,opener=open):
    h=hashlib.sha256();size=0
    with opener(path,'rb') as stream:
        while data:=stream.read(1024*1024):h.update(data);size+=len(data)
    return h.hexdigest(),size


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--partials',nargs='+',required=True);parser.add_argument('--output',required=True);args=parser.parse_args();start=time.perf_counter()
    if Path(args.output).exists():raise FileExistsError(args.output)
    rows=[]
    for name in args.partials:
        source=Path(name)
        if source.is_absolute() or '..' in source.parts or source.parts[:3]!=('bot_research','runs','validation') or source.parent.name!='replays' or source.suffix!='.jsonl':raise ValueError('Expected explicit owned partial replay.')
        root=source.parent.parent;failure=root/'results'/(source.stem+'.failure.json');success=root/'results'/(source.stem+'.json')
        if not failure.is_file() or success.exists():raise ValueError('Only failed attempts without completed results may be archived.')
        failure_data=json.loads(failure.read_text());assert failure_data['job']==source.stem
        archive=source.with_suffix(source.suffix+'.gz')
        if archive.exists():raise FileExistsError(str(archive))
        before,size=digest_file(source)
        with source.open('rb') as incoming,archive.open('xb') as raw:
            with gzip.GzipFile(filename='',mode='wb',compresslevel=9,fileobj=raw,mtime=0) as compressed:shutil.copyfileobj(incoming,compressed,1024*1024)
            raw.flush();os.fsync(raw.fileno())
        restored,restored_size=digest_file(archive,gzip.open)
        assert (restored,restored_size)==(before,size)
        zipped,zsize=digest_file(archive)
        rows.append(dict(original=str(source),original_sha256=before,original_bytes=size,archive=str(archive),archive_sha256=zipped,archive_bytes=zsize,restored_bytes_verified=True,failure_record=str(failure),failure_sha256=digest_file(failure)[0],failure=failure_data))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,entries=rows,scope='Lossless storage change for incomplete timed-out attempts only. Failure records, declared jobs, successful retries, selected results and valid replays remain unchanged. Original bytes can be restored by decompressing the named gzip archive to its original relative path.')
    atomic_json(args.output,out,exclusive=True)
    for row in rows:
        assert digest_file(row['original'])==(row['original_sha256'],row['original_bytes'])
        Path(row['original']).unlink()
    print(json.dumps(dict(time_utc=out['time_utc'],all_passed=True,files=len(rows),saved_bytes=sum(r['original_bytes']-r['archive_bytes'] for r in rows))))

if __name__=='__main__':main()

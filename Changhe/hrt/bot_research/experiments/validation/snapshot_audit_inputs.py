"""Preserve exact bytes named by an audit, including old append-only prefixes."""
from datetime import datetime,timezone
from pathlib import Path
import argparse,gzip,hashlib,json,time
from bot_research.experiments.validation.artifact_io import atomic_json


def recover_input_bytes(path, expected):
    path=Path(path)
    if path.exists():
        raw=path.read_bytes();method='current_complete_file'
    elif path.with_suffix(path.suffix+'.gz').exists():
        with gzip.open(path.with_suffix(path.suffix+'.gz'),'rb') as f:raw=f.read()
        method='lossless_gzip_archive'
    else:
        raise ValueError('Input and lossless archive are absent: '+str(path))
    if hashlib.sha256(raw).hexdigest()==expected:
        return raw,method,len(raw)
    if path.suffix=='.jsonl':
        h=hashlib.sha256();offset=0
        if h.hexdigest()==expected:return b'','empty_append_only_prefix',len(raw)
        for line in raw.splitlines(keepends=True):
            h.update(line);offset+=len(line)
            if h.hexdigest()==expected:
                return raw[:offset],'verified_append_only_prefix',len(raw)
    raise ValueError('Recorded bytes cannot be recovered exactly: '+str(path))


def main():
    p=argparse.ArgumentParser();p.add_argument('--audits',nargs='+',required=True)
    p.add_argument('--output-dir',required=True);args=p.parse_args()
    out=Path(args.output_dir)
    if out.is_absolute() or '..' in out.parts or out.parts[:3]!=('bot_research','runs','validation'):
        p.error('Use a relative owned validation output directory.')
    out.mkdir(parents=True,exist_ok=False);blobs=out/'blobs';blobs.mkdir()
    start=time.perf_counter();audit_hashes={};expected_inputs={};source_audits={}
    for name in args.audits:
        raw=Path(name).read_bytes();audit_hashes[name]=hashlib.sha256(raw).hexdigest()
        record=json.loads(raw)
        for source,expected in record['input_snapshot_sha256'].items():
            # Two audits may read different complete prefixes of the same live stream.
            key=(source,expected);expected_inputs[key]=None
            source_audits.setdefault(key,[]).append(name)
    rows=[];unique={}
    for source,expected in sorted(expected_inputs):
        if Path(source).is_absolute() or '..' in Path(source).parts:
            raise ValueError('Audit contains an unsafe input path.')
        raw,method,current_size=recover_input_bytes(source,expected)
        blob=blobs/(expected+'.gz')
        if expected not in unique:
            encoded=gzip.compress(raw,compresslevel=6,mtime=0)
            with blob.open('xb') as f:f.write(encoded)
            assert hashlib.sha256(gzip.decompress(blob.read_bytes())).hexdigest()==expected
            unique[expected]=dict(archive=str(blob),uncompressed_bytes=len(raw),compressed_bytes=len(encoded),archive_sha256=hashlib.sha256(encoded).hexdigest())
        row=dict(source=source,source_sha256=expected,audits=source_audits[(source,expected)],
            recovery_method=method,current_source_bytes=current_size,**unique[expected])
        rows.append(row)
    assert all(hashlib.sha256(Path(name).read_bytes()).hexdigest()==sha for name,sha in audit_hashes.items())
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        all_inputs_preserved=True,audit_sha256=audit_hashes,input_versions=len(rows),unique_blobs=len(unique),
        append_only_prefix_recoveries=sum(r['recovery_method']=='verified_append_only_prefix' for r in rows),
        uncompressed_unique_bytes=sum(r['uncompressed_bytes'] for r in unique.values()),
        compressed_unique_bytes=sum(r['compressed_bytes'] for r in unique.values()),rows=rows,
        checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        scope='Byte identity with previously recorded audit hashes. This does not strengthen the audit coverage or outcome claims.')
    atomic_json(out/'manifest.json',result,exclusive=True)
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','audit_sha256')}),flush=True)

if __name__=='__main__':main()

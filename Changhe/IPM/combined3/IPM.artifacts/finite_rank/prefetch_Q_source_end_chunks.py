#!/usr/bin/env python3
"""Compute disjoint future chunks with the frozen original source producer.

Completed records are installed by exclusive atomic hardlink. Existing data
are never overwritten. A safety gap avoids entering the master's active range.
"""
import argparse,json,hashlib,os,tempfile,time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime,timezone
import certify_Q_source_constants as P
HERE=Path(__file__).resolve().parent
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('--folder',type=Path,default=HERE/'Q_source_certificate_v01')
ap.add_argument('--workers',type=int,default=6);ap.add_argument('--last-chunks',type=int,default=6)
args=ap.parse_args();cfgpath=args.folder/'configuration.json';cfg=json.loads(cfgpath.read_text())
assert cfg['code_hashes']==P.bindings();N=cfg['panels'];size=16
starts=list(range(0,N,size))[-args.last_chunks:][::-1]
record={'configuration_sha256':sha(cfgpath),'original_producer_bindings':P.bindings(),
        'helper_sha256':sha(__file__),'chunks':[],'started_utc':datetime.now(timezone.utc).isoformat()}
manifest=HERE/'Q_source_end_prefetch_manifest.json';st=time.time()
with ProcessPoolExecutor(args.workers,initializer=P.initialize,initargs=(cfg,)) as pool:
    for first in starts:
        ids=list(range(first,min(first+size,N)));dest=args.folder/f'chunk_{ids[0]:05d}_{ids[-1]:05d}.json'
        if dest.exists():
            old=json.loads(dest.read_text());assert old['configuration']==cfg and [r['index']for r in old['rows']]==ids
            continue
        completed=[]
        for f in args.folder.glob('chunk_*.json'):
            old=json.loads(f.read_text());assert old['configuration']==cfg
            completed.extend(r['index']for r in old['rows'])
        # Keep two complete chunks between helper work and the master frontier.
        frontier=max((i for i in completed if i<first),default=-1)
        if frontier>=first-32:
            print('skip safety-gap chunk',first,'frontier',frontier,flush=True);continue
        rows=list(pool.map(P.panel,ids,chunksize=1))
        data=json.dumps({'configuration':cfg,'rows':rows,
                         'finished_utc':datetime.now(timezone.utc).isoformat()},indent=2)+'\n'
        fd,name=tempfile.mkstemp(prefix='.prefetch_completed_',dir=args.folder)
        temporary=Path(name)
        try:
            with os.fdopen(fd,'w')as stream:
                stream.write(data);stream.flush();os.fsync(stream.fileno())
            try:os.link(temporary,dest)
            except FileExistsError:
                old=json.loads(dest.read_text());assert old['configuration']==cfg and [r['index']for r in old['rows']]==ids
        finally:temporary.unlink(missing_ok=True)
        record['chunks'].append({'first':first,'last':ids[-1],'sha256':sha(dest)})
        record['updated_utc']=datetime.now(timezone.utc).isoformat();manifest.write_text(json.dumps(record,indent=2)+'\n')
        print('prefetched',first,'through',ids[-1],'seconds',round(time.time()-st,2),flush=True)
assert cfg['code_hashes']==P.bindings()
record['status']='COMPLETED_DISJOINT_END_PREFETCH';record['finished_utc']=datetime.now(timezone.utc).isoformat()
manifest.write_text(json.dumps(record,indent=2)+'\n')

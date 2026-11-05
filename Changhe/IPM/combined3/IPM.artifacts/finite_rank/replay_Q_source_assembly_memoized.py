#!/usr/bin/env python3
"""Separate exact assembly replay with a pure rational-binomial memoization.

The running original producer, its files, and every dependency remain unchanged.
Only the replay process caches repeated return values of the exact binom(a,n).
"""
import argparse,functools,hashlib,json,os,sys,time
from pathlib import Path
from datetime import datetime,timezone
import certify_Q_source_constants as P
import asymptotics013 as AS
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
    for attempt in range(20):
        try:return json.loads(Path(p).read_text())
        except json.JSONDecodeError:
            if attempt==19:raise
            time.sleep(.05)
ap=argparse.ArgumentParser();ap.add_argument('--original',type=Path,default=HERE/'Q_source_certificate_v01')
ap.add_argument('--replay',type=Path,default=HERE/'Q_source_certificate_assembly_replay_v01')
args=ap.parse_args();args.replay.mkdir(parents=True,exist_ok=True)
cfg=load(args.original/'configuration.json');assert cfg['code_hashes']==P.bindings()
paths=[args.original/'configuration.json']+sorted(args.original.glob('chunk_*.json'))
before={p.name:sha(p) for p in paths}
for p in paths:
    dest=args.replay/p.name
    if dest.exists():assert sha(dest)==before[p.name]
    else:os.link(p,dest)
record={'original_configuration_sha256':sha(args.original/'configuration.json'),
        'original_producer_bindings':P.bindings(),'input_record_sha256':before,
        'replay_helper_sha256':sha(__file__),
        'optimization':'Process-local memoization of exact pure binom(a,n); no arithmetic expression, coefficient, radius, degree, or source file is altered.'}
start=time.time();result=args.replay/'result.json'
if not result.exists():
    AS.binom=functools.lru_cache(maxsize=None)(AS.binom)
    P.assemble(args.replay)
    record['exact_binomial_cache']=AS.binom.cache_info()._asdict()
assert before=={p.name:sha(p) for p in paths}
assert cfg['code_hashes']==P.bindings()
replayed=load(result);assert replayed['status']=='CERTIFIED_WHOLE_PLANE_Q_SOURCE_CONSTANTS'
record['replay_result_sha256']=sha(result)
original=args.original/'result.json'
if original.exists():
    adopted=load(original);assert adopted['status']==replayed['status']
    aa={k:v for k,v in adopted.items() if k!='finished_utc'}
    bb={k:v for k,v in replayed.items() if k!='finished_utc'}
    assert aa==bb
    record['status']='SOURCE_ASSEMBLY_REPLAY_IDENTICAL'
    record['original_result_sha256']=sha(original)
    record['all_non_timestamp_fields_identical']=True
else:record['status']='SOURCE_ASSEMBLY_REPLAY_COMPLETE_ORIGINAL_PENDING'
record['elapsed_seconds_this_invocation']=time.time()-start
record['finished_utc']=datetime.now(timezone.utc).isoformat()
(HERE/'Q_source_assembly_replay_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='input_record_sha256'},indent=2))

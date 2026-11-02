"""Audit a complete native wall-set enumeration against the original router."""
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import gzip
import hashlib
import json
import math
import shutil
import struct
import subprocess
import sys
import time

from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure

E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
A=E/'analysis/screened_guard_minimum';O=R/'screened-guard-minimum-001'
D=E/'screened-guard-minimum-001.json'
CPP=A/'sources/enumerate.cpp';EXE=A/'sources/enumerate'
W=R/'affordable-roster-coverage-001/witnesses/standard-02-side0-r6.jsonl'
TOWERS=((10,1),(1,0),(1,1),(1,2))
CELLS=[v for v in range(144) if v not in (0,143) and (v%12,v//12) not in TOWERS]
INDEX={v:i for i,v in enumerate(CELLS)}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def declare():
    assert not D.exists() and not EXE.exists() and not O.exists()
    command=['g++','-std=c++17','-O3',str(CPP),'-o',str(EXE)]
    compiler=shutil.which('g++');assert compiler
    version=subprocess.run(['g++','--version'],capture_output=True,text=True,timeout=30,check=True).stdout
    start=time.perf_counter();compiled=subprocess.run(command,capture_output=True,text=True,timeout=120)
    if compiled.returncode:
        print(public_diagnostic(compiled.stdout+compiled.stderr));raise RuntimeError('Native compilation failed.')
    paths=set(static_closure({'bot_research.experiments.validation.screened_guard_minimum'}))|{CPP,EXE,A/'PROOF.md',W,Path('td_game/balanced.json'),E/'analysis/screened_roster_wall_guard/verification/full_check.json'}
    sources={str(p):sha(p) for p in sorted(paths)}
    d=dict(time_utc=now(),source_and_input_sha256=sources,available_cells=CELLS,
        cardinalities=list(range(5)),expected_by_cardinality=[math.comb(138,k) for k in range(5)],
        expected_records=sum(math.comb(138,k) for k in range(5)),record_format='five unsigned bytes: up to four sorted grid cell indices, pad255, then exposure_count+1; zero means no path',
        shards=3,python_router_check_stride=9973,compiler_name='g++',compiler_version=version,
        compiler_sha256=sha(compiler),compile_command=command,compile_seconds=time.perf_counter()-start,
        previous_native_enumerations=0,scope='All wall sets of at most four cells on one selected fixed-action state. No new games or policy calls.')
    atomic_json(D,d,exclusive=True);O.mkdir()
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {now()}: Exact wall-cost enumeration declared\n\nH1: five walls are necessary for zero incoming damage in the fixed C02 round6 state while retaining the180gold screened attack. OPEN. The declaration covers {d["expected_records"]} wall sets of size0 through4, split into three disjoint native scans. Source correspondence, exact set coverage and original-router/Engine checks are required before a conclusion. No policy calls or full strength games.\n')
    print(json.dumps(dict(time_utc=now(),records=d['expected_records'],pins=len(sources))))
def verify():
    d=json.loads(D.read_text())
    assert all(sha(p)==h for p,h in d['source_and_input_sha256'].items())
    return d
def route_check(walls,value):
    blocked=set(TOWERS)|{(v%12,v//12) for v in walls}
    route=shortest_path(12,12,blocked,(0,0),(11,11))
    score=-1 if route is None else sum(max(abs(x-tx),abs(y-ty))==1 for x,y in route[:-1] for tx,ty in TOWERS)
    assert value==score,(walls,value,score)
    return dict(walls=walls,exposure_count=score,original_route_sha256=hashlib.sha256(json.dumps(route,separators=(',',':')).encode()).hexdigest())
def audit():
    start=time.perf_counter();d=verify();expected=d['expected_by_cardinality']
    counts=Counter();invalid=Counter();maxima={};samples=0;inputs={str(D):sha(D)};shards=[]
    sampled=O/'original-router-checks.jsonl.gz'
    with gzip.open(sampled,'xt',encoding='utf-8') as checks:
        for shard in range(3):
            binary=O/f'shard{shard}.bin';meta=O/f'shard{shard}.json'
            inputs[str(binary)]=sha(binary);inputs[str(meta)]=sha(meta)
            metadata=json.loads(meta.read_text());assert metadata['shard']==shard
            previous=None;n=0;local=Counter();bad=Counter();best={}
            with binary.open('rb') as stream:
                while True:
                    data=stream.read(5*100000)
                    if not data:break
                    assert len(data)%5==0
                    for a,b,c,e,encoded in struct.iter_unpack('5B',data):
                        padded=(a,b,c,e);walls=tuple(v for v in padded if v!=255);k=len(walls)
                        assert padded==walls+(255,)*(4-k)
                        assert all(v in INDEX for v in walls)
                        assert all(walls[i]<walls[i+1] for i in range(k-1))
                        assert (INDEX[walls[0]]%3==shard) if walls else shard==0
                        key=(k,walls);assert previous is None or key>previous;previous=key
                        assert encoded<=33;value=encoded-1
                        local[k]+=1;counts[k]+=1;n+=1
                        if value<0:bad[k]+=1;invalid[k]+=1
                        if k not in best or value>best[k][0]:best[k]=(value,walls)
                        if k not in maxima or value>maxima[k][0]:maxima[k]=(value,walls)
                        if k<=2 or (n-1)%d['python_router_check_stride']==0:
                            checks.write(json.dumps(route_check(walls,value),sort_keys=True)+'\n');samples+=1
            assert binary.stat().st_size==5*n
            for row in metadata['cardinalities']:
                k=row['k'];assert row['count']==local[k] and row['invalid']==bad[k]
                if local[k]:
                    assert row['maximum_score']==best[k][0] and tuple(row['witness'])==best[k][1]
                    checks.write(json.dumps(route_check(best[k][1],best[k][0]),sort_keys=True)+'\n');samples+=1
            shards.append(dict(shard=shard,records=n,metadata=metadata,original_router_samples_so_far=samples))
            print(json.dumps(dict(time_utc=now(),shard_completed=shard,records=n,router_checks=samples)),flush=True)
    assert [counts[k] for k in range(5)]==expected
    inputs[str(sampled)]=sha(sampled)
    records=[json.loads(s) for s in W.read_text().splitlines()];cfg=balanced_config()
    names=tuple(r['snapshot']['name'] for r in records[:2]);engine=Engine(cfg,names)
    assert normalized(engine.initial_records(names))==records[:2]
    for rnd in range(1,6):
        pair=records[2*rnd:2*rnd+2];actions=[[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair]
        assert normalized(engine.play_round(actions))==pair
    target=[e['action'] for e in records[12]['event'] if e['kind']=='action']
    screened=[dict(op='buy_minion',type=t) for t in ('tier2','tier2','tier3')]
    witnesses=[]
    chosen_five=json.loads((E/'analysis/screened_roster_wall_guard/verification/full_check.json').read_text())['minimum_successful_in_family']['walls']
    candidates=[(k,*maxima[k]) for k in range(5)]+[(5,19,tuple(y*12+x for x,y in chosen_five))]
    for k,value,walls in candidates:
        checked=route_check(walls,value);probe=deepcopy(engine)
        actions=screened+[dict(op='build_wall',x=v%12,y=v//12) for v in walls]
        pair=normalized(probe.play_round([target,actions]))
        assert all(e['accepted'] for r in pair for e in r['event'] if e['kind']=='action')
        incoming=next(e['base_damage'] for e in pair[1]['event'] if e['kind']=='combat')
        predicted=15*(value<2)+26*(value<18)
        assert incoming==predicted
        assert probe.players[0].hp==774
        path=O/f'maximum-k{k}.jsonl'
        with path.open('x') as f:
            for r in records[:12]+pair:f.write(json.dumps(r,sort_keys=True)+'\n')
        inputs[str(path)]=sha(path)
        witnesses.append(dict(k=k,**checked,per_copy_splash=10*value,incoming_damage=incoming,counter_hp=probe.players[1].hp,target_hp=probe.players[0].hp,replay=str(path)))
    verify();assert all(sha(p)==h for p,h in inputs.items())
    minimum=next((k for k in range(5) if maxima[k][0]>=18),5)
    result=dict(time_utc=now(),elapsed_seconds=time.perf_counter()-start,source_and_input_sha256=d['source_and_input_sha256'],evidence_sha256=inputs,total_wall_sets=sum(counts.values()),counts_by_cardinality=[counts[k] for k in range(5)],invalid_by_cardinality=[invalid[k] for k in range(5)],maximum_exposure_by_cardinality=[maxima[k][0] for k in range(5)],original_python_router_checks=samples,original_engine_witnesses=witnesses,minimum_walls=minimum,h1='CONFIRMED' if minimum==5 else 'REFUTED',shards=shards,policy_calls=0,new_strength_games=0,scope='Exact fixed-state wall-only defensive cost, conditional on the audited native/original routing correspondence; no formal proof assistant or verified compiler.')
    atomic_json(A/'verification/full_check.json',result,exclusive=True)
    lines=['# Exact wall-cost verification results','',f"Completed {result['time_utc']}. H1: **{result['h1']}**. Minimum wall cost: **{minimum}**.",'',f"The complete scan contains {result['total_wall_sets']} distinct wall sets of cardinality0 through4. Strict ordering, disjoint shard membership and binomial counts check coverage. The independent audit checked {samples} routes through original Python shortest_path, and six maximum/five-wall witnesses through the unchanged Engine. No policy calls or strength games were run.",'','| Wall count | Sets | Invalid paths | Maximum splash damage per copy |','| --- | --- | --- | --- |']
    for k in range(5):lines.append(f'| {k} | {counts[k]} | {invalid[k]} | {10*maxima[k][0]} |')
    lines+=['',f'The existing five-wall witness gives190 splash damage per copy and800:774 round6HP. The smallest feasible count under the exact stated restrictions is {minimum}. See PROOF.md for the reduction, source correspondence argument and scope. This is a finite computational verification, with no proof-assistant or verified-compiler claim. Every wall-set score is retained in the compact binary records and decoded by the independent checker.','']
    with (A/'RESULTS.md').open('x') as f:f.write('\n'.join(lines))
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f"\n## {now()}: Exhaustive wall-cost result\n\nClaim: five walls are necessary on the fixed C02 state with the screened attack. Method: all {result['total_wall_sets']} wall sets of size0 through4, exact domain checks, {samples} original-router checks and six original-engine witnesses. Result: minimum {minimum}, maxima {[10*maxima[k][0] for k in range(5)]}. Verdict: H1{result['h1']}, under the source correspondence argument in analysis/screened_guard_minimum/PROOF.md. No formal proof assistant, policy calls or new strength games.\n")
    print(json.dumps({k:result[k] for k in ('time_utc','elapsed_seconds','total_wall_sets','original_python_router_checks','minimum_walls','h1')}))
if __name__=='__main__':{'declare':declare,'audit':audit}[sys.argv[1]]()

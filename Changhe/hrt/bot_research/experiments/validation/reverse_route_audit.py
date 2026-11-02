"""Independent backward-distance verification of all retained wall-set scores."""
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
import gzip
import hashlib
import json
import shutil
import subprocess
import sys
import time
from td_game.pathfinding import shortest_path
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.source_closure import static_closure
E=Path('bot_research/experiments/validation'); R=Path('bot_research/runs/validation')
A=E/'analysis/reverse_route_audit'; O=R/'reverse-route-audit-001'
P=E/'analysis/screened_guard_minimum/verification/full_check.json'
D=E/'reverse-route-audit-001.json'
CPP=A/'sources/check_reverse.cpp'; EXE=A/'sources/check_reverse'
TOWERS={(10,1),(1,0),(1,1),(1,2)}
DIRECTIONS=((1,0),(0,1),(-1,0),(0,-1))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def declare():
    assert not D.exists() and not O.exists() and not EXE.exists()
    compiler=shutil.which('g++');assert compiler
    command=['g++','-std=c++17','-O3',str(CPP),'-o',str(EXE)]
    start=time.perf_counter();result=subprocess.run(command,capture_output=True,text=True,timeout=120)
    if result.returncode:
        print(public_diagnostic(result.stdout+result.stderr));raise RuntimeError('Compilation failed.')
    compile_seconds=time.perf_counter()-start
    parent=json.loads(P.read_text())
    inputs={str(P):sha(P),**parent['source_and_input_sha256'],**parent['evidence_sha256']}
    for p in set(static_closure({'bot_research.experiments.validation.reverse_route_audit'}))|{CPP,EXE,A/'PROOF.md'}:
        inputs[str(p)]=sha(p)
    assert all(sha(p)==h for p,h in inputs.items())
    version=subprocess.run(['g++','--version'],capture_output=True,text=True,timeout=30,check=True).stdout
    atomic_json(D,dict(time_utc=now(),input_sha256=inputs,compiler_name='g++',compiler_sha256=sha(compiler),compiler_version=version,compile_command=command,compile_seconds=compile_seconds,expected_records=parent['total_wall_sets'],expected_original_cases=parent['original_python_router_checks']),exclusive=True)
    O.mkdir();print(json.dumps(dict(time_utc=now(),pins=len(inputs),expected_records=parent['total_wall_sets'])))
def check_pins():
    d=json.loads(D.read_text());assert all(sha(p)==h for p,h in d['input_sha256'].items());return d

def backward(walls):
    blocked=TOWERS|{(v%12,v//12) for v in walls}
    base=(11,11);dist={base:0};queue=deque([base])
    while queue:
        x,y=queue.popleft()
        for dx,dy in reversed(DIRECTIONS):
            q=x+dx,y+dy
            if 0<=q[0]<12 and 0<=q[1]<12 and q not in blocked and q not in dist:
                dist[q]=dist[(x,y)]+1;queue.append(q)
    if (0,0) not in dist:return None
    path=[(0,0)]
    while path[-1]!=base:
        x,y=path[-1]
        choices=[(x+dx,y+dy) for dx,dy in DIRECTIONS if dist.get((x+dx,y+dy),-1)==dist[(x,y)]-1]
        assert choices
        path.append(choices[0])
    return path

def fixtures():
    d=check_pins();start=time.perf_counter();count=0
    parent=R/'screened-guard-minimum-001/original-router-checks.jsonl.gz'
    with gzip.open(parent,'rt') as stream:
        for line in stream:
            row=json.loads(line);walls=row['walls']
            old=shortest_path(12,12,TOWERS|{(v%12,v//12) for v in walls},(0,0),(11,11))
            new=backward(walls)
            assert new==old,(count,walls)
            assert hashlib.sha256(json.dumps(old,separators=(',',':')).encode()).hexdigest()==row['original_route_sha256']
            count+=1
    assert count==d['expected_original_cases']
    check_pins()
    output=dict(time_utc=now(),elapsed_seconds=time.perf_counter()-start,all_passed=True,full_paths_checked=count,input_sha256={str(D):sha(D),str(parent):sha(parent)})
    atomic_json(O/'fixtures.json',output,exclusive=True);print(json.dumps(output))
def shard(index):
    check_pins();output=O/f'shard{index}.json';assert not output.exists()
    command=[str(EXE),str(R/'screened-guard-minimum-001'/f'shard{index}.bin'),str(output)]
    result=subprocess.run(command,capture_output=True,text=True,timeout=550)
    print(public_diagnostic(result.stdout+result.stderr),end='')
    print(json.dumps(dict(time_utc=now(),shard=index,command=command,returncode=result.returncode)),flush=True)
    assert result.returncode==0
    check_pins()
def publish():
    d=check_pins();parent=json.loads(P.read_text());fixture=json.loads((O/'fixtures.json').read_text())
    assert fixture['all_passed'] and fixture['full_paths_checked']==d['expected_original_cases']
    rows=[];counts=[0]*5;invalid=[0]*5;maximum=[-1]*5;histogram=[[0]*34 for _ in range(5)]
    inputs={str(D):sha(D),str(O/'fixtures.json'):sha(O/'fixtures.json')}
    for i in range(3):
        path=O/f'shard{i}.json';inputs[str(path)]=sha(path);row=json.loads(path.read_text())
        assert row['records']==parent['shards'][i]['records'] and row['mismatches']==0
        for c in row['cardinalities']:
            k=c['k'];assert sum(c['histogram'])==c['count'] and c['histogram'][0]==c['invalid']
            counts[k]+=c['count'];invalid[k]+=c['invalid'];maximum[k]=max(maximum[k],c['maximum'])
            histogram[k]=[x+y for x,y in zip(histogram[k],c['histogram'])]
        rows.append(row)
    assert counts==parent['counts_by_cardinality'] and invalid==parent['invalid_by_cardinality'] and maximum==parent['maximum_exposure_by_cardinality']
    assert sum(counts)==d['expected_records']
    result=dict(time_utc=now(),all_passed=True,h1='CONFIRMED',records=sum(counts),counts_by_cardinality=counts,invalid_by_cardinality=invalid,maximum_exposure_by_cardinality=maximum,histogram_by_cardinality=histogram,full_python_paths_checked=fixture['full_paths_checked'],native_seconds=sum(r['elapsed_seconds'] for r in rows),shards=rows,input_sha256={**d['input_sha256'],**inputs},policy_calls=0,new_games=0)
    atomic_json(A/'verification/full_check.json',result,exclusive=True)
    with (A/'RESULTS.md').open('x') as stream:
        stream.write(f'# Backward-distance audit results\n\nCompleted {result["time_utc"]}. H1 **CONFIRMED**: every one of the{result["records"]} retained wall-set scores matches the independently implemented backward-distance checker. All{result["full_python_paths_checked"]} retained original-router cases also match in their complete paths. No mismatch occurred.\n\nCounts, disconnected cases and cardinality maxima equal the parent certificate. Maximum per-copy splash damage for0,1,2,3,4walls is100,100,100,100,150. The existing five-wall witness reaches190. This adds an independent all-record routing check to the fixed-state minimum-five-wall result.\n\nThe native shard durations sum to{result["native_seconds"]:.6f}seconds. This is active checker time, not a new game count or the duration of the entire lane. The audit ran no policy calls or new games, duplicated no large binary table, and did not touch final best.py or pool D. See PROOF.md for the route tie-break argument and ordinary-compilation limitation.\n')
    with Path('bot_research/notes/validation.md').open('a') as stream:stream.write(f'\n## {now()}: Independent all-score routing audit\n\nClaim: every one of the14,901,218 retained wall-set scores agrees with a backward-distance route algorithm. Method: full native rescoring,11,097 complete original-Python path comparisons and parent hash/domain rechecks. Result:0mismatches; maxima unchanged. Verdict: CONFIRMED under the route correspondence argument, without a proof-assistant or verified-compiler claim. No games or policy calls. Evidence: experiments/validation/analysis/reverse_route_audit/RESULTS.md.\n')
    print(json.dumps({k:result[k] for k in ('time_utc','all_passed','h1','records','full_python_paths_checked','native_seconds')}))
if __name__=='__main__':
    if sys.argv[1]=='shard':shard(int(sys.argv[2]))
    else:{'declare':declare,'fixtures':fixtures,'publish':publish}[sys.argv[1]]()

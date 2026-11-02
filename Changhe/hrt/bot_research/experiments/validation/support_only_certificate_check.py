"""Check a support-only certificate for every completion of a partial game."""
from collections import defaultdict
from copy import deepcopy
from datetime import datetime,timezone
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse,gzip,hashlib,json,time
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.finite_table_certificate import verify as certificate
from bot_research.experiments.validation.final_validation_strict import read_result
from bot_research.experiments.validation.publish_ten_policy_game_v2 import norm
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure
from td_game.config import balanced_config
from td_game.engine import Engine
E=Path('bot_research/experiments/validation');A=E/'analysis/support_only_certificate'
D=E/'support-only-certificate-001.json'
ORDER=['B','C','D','G','H','I','J','L','M','N','O','P']
PARENTS=[E/'analysis'/area/'verification/full_games.json' for area in ('ten_policy_game','wall_prefix_selector','delayed_wall_counter')]

def sha(data):return hashlib.sha256(data).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def declare():
    paths=set(static_closure({'bot_research.experiments.validation.support_only_certificate_check'}))
    paths|=set(PARENTS)|{A/'PROOF.md',E/'analysis/wall_prefix_selector/verification/provenance_supplement.json',
        E/'analysis/wall_prefix_selector/PROOF.md',E/'analysis/delayed_wall_counter/PROOF.md',
        E/'wall-prefix-selector-001.json',E/'delayed-wall-counter-001.json',
        Path('td_game/balanced.json'),Path('configs/balanced.json')}
    atomic_json(D,dict(declared_utc=now(),new_games=0,new_policy_calls=0,order=ORDER,
        expected_existing_support_games=46,expected_completions=729,
        input_sha256={str(p):sha(p.read_bytes()) for p in sorted(paths)}),exclusive=True)
    print(json.dumps(dict(time_utc=now(),pins=len(paths),new_games=0)),flush=True)

def check():
    start=time.perf_counter();inputs={};compressed={};edges=0
    def data(path,expected=None):
        p=Path(path)
        if p.is_file():value=p.read_bytes()
        else:
            q=Path(str(p)+'.gz');packed=q.read_bytes();value=gzip.decompress(packed)
            compressed[str(p)]=dict(archive=str(q),archive_sha256=sha(packed))
        digest=sha(value)
        assert expected is None or digest==expected,str(p)
        assert str(p) not in inputs or inputs[str(p)]==digest,str(p)
        inputs[str(p)]=digest
        return value
    def read(path):return json.loads(data(path))
    def pins(mapping):
        nonlocal edges
        for p,h in mapping.items():data(p,h);edges+=1
    declaration=read(D);pins(declaration['input_sha256'])
    parents=[read(p) for p in PARENTS]
    for parent in parents:
        assert parent['all_passed'];pins(parent['input_sha256'])
    provenance=read(E/'analysis/wall_prefix_selector/verification/provenance_supplement.json')
    assert provenance['all_passed'];pins(provenance['input_sha256'])
    old,o,p=parents
    assert old['order']==ORDER[:10] and len(old['cases'])==110
    assert o['order']==ORDER[:11]
    assert len(o['cases'])==22 and len(p['cases'])==10
    assert old['payoff']==[row[:10] for row in o['payoff'][:10]]
    policies=dict(read(E/'wall-prefix-selector-001.json')['policies'])
    policies['P']=read(E/'delayed-wall-counter-001.json')['policies']['P']
    all_cases=[dict(a=c['a'],b=c['b'],result=c['result'],side=c['candidate_side']) for c in old['cases']]
    all_cases += [dict(a='O',b=c['opponent'],result=c['result'],side=c['side']) for c in o['cases']]
    all_cases += [dict(a='P',b=c['opponent'],result=c['result'],side=c['side']) for c in p['cases']]
    assert len(all_cases)==len({c['result'] for c in all_cases})==142
    support=[c for c in all_cases if c['a'] in ('G','O') or c['b'] in ('G','O')]
    assert len(support)==46
    groups=defaultdict(list);checked=[]
    for c in support:
        path=Path(c['result']);root=path.parent.parent
        row=read(path);job=read(root/'jobs'/(path.stem+'.json'));freeze=read(root/'freeze.json')
        # Result files themselves are retained uncompressed in these campaigns.
        validated=read_result(path,job,freeze['source_sha256']);assert validated==row
        assert not any(row['bot_errors']) and not any(row['rejected_actions']) and not row['source_changed_during_match']
        assert norm(row['condition']['candidate_spec'])==norm(policies[c['a']]['spec'])
        assert norm(row['condition']['opponent_spec'])==norm(policies[c['b']]['spec'])
        assert row['condition']['candidate_side']==c['side']
        records=[json.loads(line) for line in data(row['replay_path'],row['trajectory_sha256']).splitlines()]
        rounds=row['rounds'];assert len(records)==2*(rounds+1)
        assert all(r['round']==i//2 and r['player']==i%2 for i,r in enumerate(records))
        assert all(r.get('result') is None for r in records[:-2])
        assert records[-1]['result'] is not None and records[-1]['result']==records[-2]['result']==row['result']
        engine=Engine(balanced_config(),tuple(row['bot_specs']))
        assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
        for rnd in range(1,rounds+1):
            pair=records[2*rnd:2*rnd+2]
            actions=[[e['action'] for e in r['event'] if e['kind']=='action'] for r in pair]
            assert normalized(engine.play_round(actions))==pair
        assert engine.result==row['result']
        canon=deepcopy(records)
        for r in canon:
            r.pop('match',None);r['player']^=c['side']
            r['snapshot']['name']='counter' if r['player']==0 else 'opponent'
            for event in r['event']:event.pop('order',None)
            if r.get('result') is not None and r['result']['winner'] is not None:r['result']['winner']^=c['side']
        canon.sort(key=lambda r:(r['round'],r['player']))
        detail=dict(**c,outcome=row['candidate_outcome'],rounds=rounds,
            canonical_replay_sha256=sha(json.dumps(canon,sort_keys=True,separators=(',',':')).encode()),
            all_replayed=True,terminal_boundary=True)
        checked.append(detail);groups[(c['a'],c['b'])].append(detail)
    assert len(groups)==23
    rows={a:[None]*12 for a in ('G','O')}
    for (a,b),pair in groups.items():
        assert len(pair)==2 and {r['side'] for r in pair}=={0,1}
        assert pair[0]['canonical_replay_sha256']==pair[1]['canonical_replay_sha256']
        assert pair[0]['outcome']==pair[1]['outcome']
        v={'W':1,'D':0,'L':-1}[pair[0]['outcome']]
        if a==b:assert v==0
        if a in rows:rows[a][ORDER.index(b)]=v
        if b in rows:rows[b][ORDER.index(a)]=-v
    expected={'G':[1,1,0,0,-1,1,-1,1,1,1,0,1], 'O':[1,0,1,0,1,0,1,1,1,1,0,-1]}
    assert rows==expected
    weights=[Fraction(1,2) if k in rows else Fraction(0) for k in ORDER]
    means=[sum(weights[ORDER.index(k)]*row[j] for k,row in rows.items()) for j in range(12)]
    assert min(means)>=0
    matrix=[list(row)+[None] for row in o['payoff']]+[[None]*12];matrix[-1][-1]=0
    for target in ('G','O'):
        j=ORDER.index(target);matrix[j][-1]=rows[target][-1];matrix[-1][j]=-rows[target][-1]
    # The three further P pairs are already observed, but not needed by the certificate.
    for target in ('B','L','N'):
        pair=[c for c in p['cases'] if c['opponent']==target]
        assert len(pair)==2 and {c['side'] for c in pair}=={0,1}
        assert pair[0]['outcome']==pair[1]['outcome']
        v={'W':1,'D':0,'L':-1}[pair[0]['outcome']];j=ORDER.index(target)
        matrix[-1][j]=v;matrix[j][-1]=-v
    assert all(matrix[ORDER.index(k)]==rows[k] for k in ('G','O'))
    missing=[(i,j) for i in range(12) for j in range(i+1,12) if matrix[i][j] is None]
    assert [(ORDER[i],ORDER[j]) for i,j in missing]==[(k,'P') for k in ('C','D','H','I','J','M')]
    count=0
    for values in product((-1,0,1),repeat=len(missing)):
        completed=deepcopy(matrix)
        for (i,j),v in zip(missing,values):completed[i][j]=v;completed[j][i]=-v
        assert certificate(completed,list(map(str,weights)))
        count+=1
    assert count==729
    fixtures={}
    fixtures['zero_weights_rejected']=not certificate(completed,['0']*12)
    bad=list(map(str,weights));bad[3]='-1/2';bad[10]='3/2'
    fixtures['negative_weights_rejected']=not certificate(completed,bad)
    badmat=deepcopy(completed);badmat[3][11]=-1
    fixtures['asymmetry_rejected']=not certificate(badmat,list(map(str,weights)))
    badmat[11][3]=1
    fixtures['changed_G_P_pair_rejected']=not certificate(badmat,list(map(str,weights)))
    assert all(fixtures.values())
    stamp=now();lines=['# Half G, half O with incomplete payoff information','',f'Checked {stamp}.','',
        'CONFIRMED: the equal G/O mixture is an exact value-zero certificate for every skew-symmetric completion consistent with the measured support rows. It is the unique such mixture supported only on G/O. The proof applies to real missing payoffs; the executable cross-check covers all729 ternary completions.','',
        '| Opponent | G payoff | O payoff | Equal-mixture payoff |','| --- | ---: | ---: | ---: |']
    lines += [f'| {k} | {rows["G"][i]} | {rows["O"][i]} | {means[i]} |' for i,k in enumerate(ORDER)]
    lines += ['', 'The checker replays46 existing games covering23 support pairs and confirms equal role-normalized complete histories in every pair. All retained streams have exactly one final pair of terminal records. Parent receipt hashes, declared policy specifications and source attestations are rechecked. There are zero new games and zero new policy decisions.', '',
        'The six unplayed P pairs are C,D,H,I,J,M. P self play is also unplayed; zero diagonal belongs to the skew-symmetric completion hypothesis. The certificate does not claim a fully measured twelve-policy table, a universal equilibrium or load-independent policy behavior. Q and reserved D are excluded. P changes both the opening signal and economy; the successful counter is not a pure-signal intervention.','']
    with (A/'RESULTS.md').open('x') as f:f.write('\n'.join(lines))
    data(A/'RESULTS.md')
    # Recheck retained inputs after computation, including lossless compressed bytes.
    for path,digest in list(inputs.items()):data(path,digest)
    result=dict(time_utc=stamp,all_passed=True,order=ORDER,support_rows=rows,
        weights=list(map(str,weights)),column_payoffs=list(map(str,means)),exact_value='0',
        existing_games_replayed=46,assignment_pairs=23,new_games=0,new_policy_calls=0,
        missing_unordered_pairs=[[ORDER[i],ORDER[j]] for i,j in missing],unplayed_self_pair='P/P',
        completions_checked=count,fixtures=fixtures,cases=checked,input_sha256=inputs,
        compressed_inputs=compressed,input_edges_checked=edges,elapsed_seconds=time.perf_counter()-start)
    atomic_json(A/'verification/full_check.json',result,exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Support-only finite certificate complete\n\nCONFIRMED under the stated skew-completion hypotheses: half G/half O has value0 and is unique on that two-policy support. Replayed46existing games/23assignment pairs; checked all729ternary completions. Zero new games or decisions. Six P off-diagonal pairs and P/P remain explicitly unplayed. Source, proof and limitations: experiments/validation/analysis/support_only_certificate/RESULTS.md.\n')
    print(json.dumps({k:result[k] for k in ('time_utc','all_passed','existing_games_replayed','completions_checked','column_payoffs','elapsed_seconds')}),flush=True)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['declare','check']);args=parser.parse_args();globals()[args.mode]()
if __name__=='__main__':main()

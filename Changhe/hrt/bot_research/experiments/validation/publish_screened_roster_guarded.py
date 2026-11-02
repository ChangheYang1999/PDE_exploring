"""Compare six new guarded policies to six explicitly reused controls."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.publish_screened_roster_continuation import canonical

E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
A=E/'analysis/screened_roster_guarded_policy'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    path=E/'screened-roster-guarded-campaigns-001.json';declared=json.loads(path.read_text())
    inputs={str(path):sha(path),**declared['input_sha256']}
    assert all(sha(p)==h for p,h in inputs.items())
    rows=[];calls=0
    guard=json.loads(Path('bot_research/bots/counters/data/screened_roster_guard_001.json').read_text())['walls']
    for item in declared['campaigns']:
        name=item['name'];c=item['continuation'];audits={}
        for kind in ('strict','replay','summary','data','fresh'):
            p=R/(name+'-'+kind+'.json');inputs[str(p)]=sha(p);audits[kind]=json.loads(p.read_text())
        strict=audits['strict'];fresh=audits['fresh']
        assert strict['valid_conditions']==2 and strict['attempt_counts']=={'valid':2}
        assert all(p['same_complete_trajectory'] for p in strict['pairs'])
        assert audits['replay']['all_passed'] and audits['data']['all_passed'] and fresh['exact_policy_reproduction']
        calls+=sum(sum(len(t) for t in x['decision_seconds']) for x in fresh['cases'])
        for case in strict['cases']:
            p=Path(case['result_path']);inputs[str(p)]=sha(p);row=json.loads(p.read_text());side=row['condition']['candidate_side']
            old_path=declared['controls'][c][str(side)];old=json.loads(Path(old_path).read_text())
            r=[]
            for value in (row,old):
                replay=Path(value['replay_path']);assert sha(replay)==value['trajectory_sha256'];inputs[str(replay)]=sha(replay)
                r.append(canonical([json.loads(s) for s in replay.read_text().splitlines()],side))
            new_records,old_records=r
            assert new_records[:12]==old_records[:12]
            def actions(record):return [e['action'] for e in record['event'] if e['kind']=='action']
            assert actions(new_records[13])==actions(old_records[13])
            assert actions(new_records[12])==actions(old_records[12])+[dict(op='build_wall',x=x,y=y) for x,y in guard]
            assert [x['snapshot']['hp'] for x in new_records[12:14]]==[800,774]
            assert [x['snapshot']['hp'] for x in old_records[12:14]]==[774,774]
            hp=row['hp'][::1 if side==0 else -1];oldhp=old['hp'][::1 if side==0 else -1]
            margin=hp[0]-hp[1];oldmargin=oldhp[0]-oldhp[1]
            rows.append(dict(continuation=c,side=side,outcome=row['candidate_outcome'],hp=hp,rounds=row['rounds'],margin=margin,old_outcome=old['candidate_outcome'],old_hp=oldhp,old_rounds=old['rounds'],old_margin=oldmargin,nondecreasing_margin=margin>=oldmargin,result=str(p),control=old_path,common_prefix=True,common_round6_target_action=True,round6_guard_exact=True))
    assert len(rows)==6
    h1=any(all(r['outcome']=='W' for r in rows if r['continuation']==c) for c in declared['controls'])
    h2=all(r['nondecreasing_margin'] for r in rows)
    assert all(sha(p)==h for p,h in inputs.items())
    stamp=datetime.now(timezone.utc).isoformat()
    result=dict(time_utc=stamp,input_sha256=inputs,new_games=6,reused_games=6,new_fresh_policy_calls=calls,rows=rows,h1='CONFIRMED' if h1 else 'REFUTED',h2='CONFIRMED' if h2 else 'REFUTED',scope='Selected finite full-policy comparison, no terminal D use and no general strength guarantee.')
    atomic_json(A/'verification/full_check.json',result,exclusive=True)
    lines=['# Guarded screened-roster policy results','',f'Completed {stamp}.', '',f"H1 (a guarded continuation wins both seats): **{result['h1']}**. H2 (every final HP margin is nondecreasing): **{result['h2']}**.",'',f'Six new games and six explicitly reused controls. Every new game passes strict accounting, full original-engine replay, source/archive checks and fresh reproduction of both policies ({calls}actual calls). All three new assignment pairs agree exactly. All six paired old/new checks preserve the round1-5 history and actual target round6 action; the guard changes own round6HP from774 to800 while keeping target HP774.','','| Continuation | Guarded result | Guarded HP | Round | Control result | Control HP | Round |','| --- | --- | --- | --- | --- | --- | --- |']
    for r in rows:
        if r['side']==0:lines.append(f"| {r['continuation']} | {r['outcome']} | {r['hp'][0]}:{r['hp'][1]} | {r['rounds']} | {r['old_outcome']} | {r['old_hp'][0]}:{r['old_hp'][1]} | {r['old_rounds']} |")
    lines+=['','Both seats agree on every table entry. The construction was selected from the prior component search and tested against a known fixed candidate. Later effects include map geometry, path income, HP and policy responses. No held-out or unrestricted-strength claim is made. The source-level Fortress38 wall-clock cutoff remains a limitation beyond the exactly reproduced calls.','','See PROOF.md and verification/full_check.json for hypotheses, exact inputs, actions and paired comparisons.','']
    with (A/'RESULTS.md').open('x') as f:f.write('\n'.join(lines))
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f"\n## {stamp}: Five-wall screened counter complete\n\nClaim: a guarded continuation wins both seats (H1), and no continuation loses final HP margin relative to its unguarded control (H2). Method:6new games,6reused controls, original-engine replay and {calls}fresh calls; all common prefixes and round6target actions checked. Result: guard gives800:774 at round6 in every match. Verdict: H1{result['h1']}, H2{result['h2']}. The complete table is experiments/validation/analysis/screened_roster_guarded_policy/RESULTS.md. Selected development only; final candidate bytes and D remain unchanged.\n")
    print(json.dumps({k:result[k] for k in ('time_utc','new_games','reused_games','new_fresh_policy_calls','h1','h2')}))
if __name__=='__main__':main()

"""Compare every declared P/Q control without rerunning a policy."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation'); A=E/'analysis/reserved_wall_counter'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    inputs={}; edges=0
    def checked(p):
        nonlocal edges
        inputs[str(p)]=sha(p); d=json.loads(Path(p).read_text())
        for q,h in d.get('input_sha256',{}).items():
            assert sha(q)==h,q
            assert q not in inputs or inputs[q]==h,q
            inputs[q]=h; edges+=1
        return d
    p=checked(E/'analysis/delayed_wall_counter/verification/full_games.json')
    q=checked(A/'verification/full_games.json')
    for x in (p,q):assert x['all_passed'] and x['new_games']==10 and all(t['same_history'] for t in x['transfers'])
    rows=[];score={'L':-1,'D':0,'W':1}
    for target in ['O','L','G','B','N']:
        for side in (0,1):
            old=next(c for c in p['cases'] if c['opponent']==target and c['side']==side)
            new=next(c for c in q['cases'] if c['opponent']==target and c['side']==side)
            rows.append(dict(opponent=target,side=side,P_outcome=old['outcome'],Q_outcome=new['outcome'],
                P_hp=old['hp_P_first'],Q_hp=new['hp_Q_first'],P_rounds=old['rounds'],Q_rounds=new['rounds'],
                score_difference=score[new['outcome']]-score[old['outcome']],
                P_result=old['result'],Q_result=new['result']))
    assert len(rows)==10
    stamp=datetime.now(timezone.utc).isoformat()
    lines=['# Complete matched P/Q comparison','',f'Checked {stamp}.','',
        'All five declared opponents are included, in both player assignments. This is selected development evidence on the unchanged standard-start engine. P and Q share the delayed twenty-wall opening and Fortress38 continuation; Q withholds two round-three factories to fund the round-four tier4. Both policies were fixed before their respective games. Q was motivated after the P/B and P/N losses were seen; its protocol records that the P/O wins were also known before Q games.','',
        '| Opponent | P outcome, HP, round | Q outcome, HP, round |','| --- | --- | --- |']
    for target in ['O','L','G','B','N']:
        a,b=[r for r in rows if r['opponent']==target]
        assert all(a[k]==b[k] for k in ('P_outcome','Q_outcome','P_hp','Q_hp','P_rounds','Q_rounds','score_difference'))
        lines.append(f'| {target} | {a["P_outcome"]}, {a["P_hp"][0]}:{a["P_hp"][1]}, {a["P_rounds"]} | {a["Q_outcome"]}, {a["Q_hp"][0]}:{a["Q_hp"][1]}, {a["Q_rounds"]} |')
    lines+=['','Each row has identical outcomes and HP in the two assignments. Q improves the W/D/L score on six of ten conditions, ties four and worsens none. It takes three more rounds to beat O and L, despite the more negative final opponent HP. The comparison therefore does not claim uniformly earlier wins or treat overkill as an independent strength measure. Across the five selected targets, P has four wins and six losses; Q has eight wins and two draws. These ten conditions are deterministic paired cases, not independent population samples.','',
        'The retained audit inputs, source hashes and ten result pairs are rechecked in `verification/PQ_controls.json`. This comparison adds zero games and zero policy decisions. Both source-policy audits already include strict action, original-engine replay, fresh decision and O/L logical-state checks. It does not change the final candidate, the terminal reserve or the twelve-policy certificate, which excluded Q.']
    report=A/'PQ_CONTROLS.md'
    with report.open('x') as f:f.write('\n'.join(lines)+'\n')
    inputs[str(report)]=sha(report);inputs[str(Path(__file__).relative_to(Path.cwd()))]=sha(__file__)
    assert all(sha(p)==h for p,h in inputs.items())
    result=dict(time_utc=stamp,all_passed=True,conditions=rows,improved=sum(r['score_difference']>0 for r in rows),
        tied=sum(r['score_difference']==0 for r in rows),worsened=sum(r['score_difference']<0 for r in rows),
        checked_input_edges=edges,new_games=0,policy_calls=0,input_sha256=inputs)
    atomic_json(A/'verification/PQ_controls.json',result,exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','all_passed','improved','tied','worsened','checked_input_edges')}))
if __name__=='__main__':main()

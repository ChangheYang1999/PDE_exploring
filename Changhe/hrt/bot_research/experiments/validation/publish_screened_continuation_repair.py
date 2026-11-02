"""Audit the exact common prefix and publish twelve fixed continuation games."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.publish_screened_roster_continuation import canonical
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
A=E/'analysis/screened_continuation_repair'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    d=E/'screened-continuation-repair-campaigns-001.json';dec=json.loads(d.read_text())
    pins={str(d):sha(d),**dec['input_sha256']};rows=[];calls=0;pairs=[]
    assert all(sha(p)==h for p,h in pins.items())
    for campaign in dec['campaigns']:
        name=campaign['name'];audits={}
        for kind in ('strict','replay','data','fresh'):
            p=R/(name+'-'+kind+'.json');pins[str(p)]=sha(p);audits[kind]=json.loads(p.read_text())
        strict=audits['strict'];fresh=audits['fresh']
        assert strict['valid_conditions']==4 and strict['attempt_counts']=={'valid':4}
        assert not strict['unresolved'] and not strict['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['data']['all_passed']
        assert fresh['exact_policy_reproduction'] and fresh['all_observations_unchanged'] and fresh['all_fresh_actions_legal']
        calls+=sum(sum(map(len,c['decision_seconds'])) for c in fresh['cases']);pairs+=strict['pairs']
        for case in strict['cases']:
            p=case['result_path'];checked_row(p,pins);row=json.loads(Path(p).read_text())
            c=row['condition'];side=c['candidate_side'];target=c['opponent_id']
            control=dec['controls'][target][str(side)];checked_row(control,pins);old=json.loads(Path(control).read_text())
            def records(r):return canonical([json.loads(s) for s in Path(r['replay_path']).read_text().splitlines()],side)
            same=records(row)[:14]==records(old)[:14]
            hp=row['hp'][::1 if side==0 else -1]
            rows.append(dict(continuation=c['candidate_id'],opponent=target,side=side,outcome=row['candidate_outcome'],hp=hp,rounds=row['rounds'],prefix_equal=same,result=p,control=control,decision_seconds=row['decision_seconds'][side]))
    assert len(rows)==12
    winners=[c['continuation'] for c in dec['campaigns'] if all(r['outcome']=='W' for r in rows if r['continuation']==c['continuation'] and r['opponent']=='AS1C')]
    both=[c for c in winners if all(r['outcome']=='W' for r in rows if r['continuation']==c and r['opponent']=='best_v9e')]
    stamp=datetime.now(timezone.utc).isoformat()
    result=dict(time_utc=stamp,new_games=12,reused_control_games=4,fresh_policy_calls=calls,rows=rows,assignment_pairs=pairs,
        h1='CONFIRMED' if winners else 'REFUTED',h2='CONFIRMED' if both else 'REFUTED',h3='CONFIRMED' if all(r['prefix_equal'] for r in rows) else 'REFUTED',AS1C_winners=winners,both_winners=both,input_sha256=pins)
    assert all(sha(p)==h for p,h in pins.items())
    atomic_json(A/'verification/full_check.json',result,exclusive=True)
    lines=['# Screened continuation results','',f'Completed {stamp}. H1: **{result["h1"]}**. H2: **{result["h2"]}**. H3: **{result["h3"]}**.','', '| Continuation | Opponent | Seat | Outcome | Own:enemy HP | Ending round |','| --- | --- | --- | --- | --- | --- |']
    for r in rows:lines.append(f'| {r["continuation"]} | {r["opponent"]} | {r["side"]} | {r["outcome"]} | {r["hp"][0]}:{r["hp"][1]} | {r["rounds"]} |')
    lines+=['',f'All12 new games and {calls} fresh policy calls pass replay, source, data, legal-action and observation-immutability checks. All common prefixes are compared with the four declared reused controls. {sum(p["same_complete_trajectory"] for p in pairs)} of {len(pairs)} assignment pairs have identical normalized full histories.','', 'This is selected development evidence. The delegates have different decision rules and resource use; no single-mechanism attribution is made. Exact reproduction does not remove their source-level clock-cutoff caveat. Final best.py and D are unchanged.','']
    with (A/'RESULTS.md').open('x') as f:f.write('\n'.join(lines))
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {stamp}: Stronger screened continuations complete\n\nClaim and verdict: some continuation wins AS1C (H1 {result["h1"]}); a successful one retains both best_v9e wins (H2 {result["h2"]}); all first-six-round histories match (H3 {result["h3"]}). Method:12 new games,4 reused controls,{calls} fresh calls and full independent replay. Result: AS1C winners {winners}; joint winners {both}. Full table: experiments/validation/analysis/screened_continuation_repair/RESULTS.md. Selected development only; best.py and D unchanged.\n')
    print(json.dumps({k:result[k] for k in ('time_utc','new_games','fresh_policy_calls','h1','h2','h3','AS1C_winners','both_winners')}))
if __name__=='__main__':main()

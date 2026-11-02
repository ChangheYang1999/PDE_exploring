"""Publish the frozen local defensive repair with explicitly reused controls."""
from collections import defaultdict
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation');A=E/'analysis/wall_signal_repair'

def prefix(path, side, stop):
    records=[json.loads(line) for line in Path(path).read_text().splitlines()]
    records=[r for r in records if r['round']<stop]
    for row in records:
        row.pop('match',None);row['player']^=side
        row['snapshot']['name']='counter' if row['player']==0 else 'opponent'
        for event in row['event']:event.pop('order',None)
        if 'result' in row and row['result']['winner'] is not None:row['result']['winner']^=side
    return sorted(records,key=lambda row:(row['round'],row['player']))

def main():
    inputs={};digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):inputs[str(p)]=digest(p);return json.loads(Path(p).read_text())
    def verify(mapping):
        for p,h in mapping.items():assert digest(p)==h,p;inputs[p]=h
    declaration=read(E/'wall-signal-repair-campaigns-001.json');verify(declaration['input_sha256'])
    component=read(A/'verification/components.json');assert component['all_passed'] and len(component['cases'])==6;verify(component['input_sha256'])
    name='wall-signal-repair-001';root=R/name
    audits={k:read(R/(name+'-'+k+'.json')) for k in ('strict','replay','data','fresh','forecasts')}
    s=audits['strict'];assert s['valid_conditions']==s['expected_conditions']==6 and s['attempt_counts']=={'valid':6} and not s['unresolved'] and not s['repeat_disagreements']
    assert audits['replay']['all_passed'] and audits['replay']['count']==6 and audits['data']['all_passed']
    for key in ('fresh','forecasts'):
        a=audits[key];assert all(a[k] for k in ('all_passed','all_replayed','all_actions_legal','all_observations_unchanged'));verify(a['input_sha256'])
    assert audits['fresh']['checked_calls']==2*audits['forecasts']['checked_calls']
    freeze=read(root/'freeze.json');verify({str(root/'sources'/p):h for p,h in freeze['source_sha256'].items()})
    traces={x['result_path']:x for x in audits['forecasts']['cases']};rows=[];groups=defaultdict(list)
    for job in read(root/'jobs.json'):
        path=str(root/'results'/(job['id']+'.json'));record=checked_row(path,inputs);raw=read(path)
        target=record['condition']['opponent_id'];side=record['condition']['candidate_side']
        control_path=declaration['controls'][target][str(side)];old=checked_row(control_path,inputs);old_raw=read(control_path)
        assert old['condition']['opponent_spec']==record['condition']['opponent_spec']
        trace=traces[path]['rounds'];selected=[t['round'] for t in trace if t['repair']['selected']]
        stop=min(selected) if selected else max(record['rounds'],old['rounds'])+1
        a=prefix(raw['replay_path'],side,stop);b=prefix(old_raw['replay_path'],side,stop);assert a==b
        item=dict(target=target,record=record,control=old,repair_rounds=selected,unchanged_before_round=stop,prefix_sha256=hashlib.sha256(json.dumps(a,sort_keys=True,separators=(',',':')).encode()).hexdigest(),forecast_mismatch_rounds=[t['round'] for t in trace if not t['model_matches']])
        rows.append(item);groups[target].append(item)
    assert len(rows)==6
    for pair in groups.values():
        assert len(pair)==2 and {x['record']['condition']['candidate_side'] for x in pair}=={0,1}
        for k in ('outcome','hp_candidate_first','rounds','canonical_replay_sha256'):assert pair[0]['record'][k]==pair[1]['record'][k]
        assert pair[0]['repair_rounds']==pair[1]['repair_rounds']
    j,h,i=(groups[t][0]['record'] for t in ('J','H','I'));assert j['canonical_replay_sha256']==h['canonical_replay_sha256']
    h1=j['outcome']=='W';scores={'W':1,'D':0,'L':-1};h2=scores[j['outcome']]>scores[i['outcome']]
    stamp=datetime.now(timezone.utc).isoformat();fresh=audits['fresh']['checked_calls'];extra=audits['forecasts']['checked_calls']
    lines=['# Full-policy test of the defensive repair','',f'Checked {stamp}.','','H1 L wins against J on the exact H-control history: '+('CONFIRMED' if h1 else 'REFUTED')+'.','H2 L has a better outcome against J than against I: '+('CONFIRMED' if h2 else 'REFUTED')+'.','','Six new standard-start games follow the fixed pre-call clarification in PROOF.md. Six K20 games are explicitly reused old controls, selected after their losses and the one-round feasibility diagnosis. This is development evidence, not held-out validation.','','| Opponent | K20 result, HP, round | L result, HP, round | First repair | Repairs |','|---|---|---|---:|---:|']
    for target in ('J','H','I'):
        row=groups[target][0];old=row['control'];new=row['record'];rep=row['repair_rounds']
        fmt=lambda r:f'{r["outcome"]}, {r["hp_candidate_first"][0]}:{r["hp_candidate_first"][1]}, {r["rounds"]}'
        lines.append(f'| {target} | {fmt(old)} | {fmt(new)} | {min(rep) if rep else "none"} | {len(rep)} |')
    lines+=['',f'Each row represents both assignments, whose full normalized histories are identical. All six new games pass strict accounting, original-engine replay, source/data checks, {fresh} fresh external decisions, and {extra} extra attacker/forecast checks. The six prefix cases passed before full games. All old/new histories are equal before the first selected repair. There are no submitted rejections, bot errors, source drift or observation mutations.','','The public selector chooses H, and its complete histories equal the fixed H controls. Forecast mismatches against I are retained in verification/full_games.json. A local damage reduction does not prove long-horizon optimality, and these three opponents do not certify a general best response. The policy uses public observations and its own private clone only; no installed best.py or pool D data is used.','']
    output=A/'RESULTS.md';output.write_text('\n'.join(lines));inputs[str(output)]=digest(output)
    result=dict(time_utc=stamp,all_passed=True,new_games=6,reused_controls=6,h1=h1,h2=h2,fresh_calls=fresh,forecast_checks=extra,rows=rows,input_sha256=inputs)
    atomic_json(A/'verification/full_games.json',result,exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {stamp}: Wall-signal defensive repair complete\n\nH1 win against J: '+('CONFIRMED' if h1 else 'REFUTED')+'; H2 better J than I: '+('CONFIRMED' if h2 else 'REFUTED')+f'. Six new games, six reused K20 controls, {fresh} fresh external calls and {extra} forecast checks pass. All unchanged-prefix and paired-history checks pass. See experiments/validation/analysis/wall_signal_repair/RESULTS.md. Selected development only.\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','input_sha256')}),flush=True)
if __name__=='__main__':main()

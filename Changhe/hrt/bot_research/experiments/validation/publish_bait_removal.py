"""Check and report the complete paired deletion intervention."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E=Path('bot_research/experiments/validation')
R=Path('bot_research/runs/validation')
AREA=E/'analysis/bait_removal'


def main():
    inputs={}
    def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        inputs[str(p)]=digest(p)
        return json.loads(Path(p).read_text())
    def verify(mapping):
        for p,h in mapping.items():
            assert digest(p)==h,p
            inputs[p]=h
    declaration=read(E/'bait-removal-campaigns-001.json')
    control=read(declaration['control_receipt'])
    assert control['all_passed'] and control['games']==24
    verify(control['input_sha256'])
    component=read(AREA/'verification/component.json')
    assert component['all_passed'] and component['checked_rounds']==100
    verify(component['source_sha256'])
    calls=0
    for item in declaration['campaigns']:
        name=item['name']
        manifest=read(E/(name+'.json')); verify(manifest['input_sha256'])
        audit={k:read(R/(name+'-'+k+'.json')) for k in ('strict','replay','data','fresh','summary')}
        assert audit['strict']['valid_conditions']==4
        assert audit['strict']['attempt_counts']=={'valid':4}
        assert not audit['strict']['unresolved'] and not audit['strict']['repeat_disagreements']
        assert audit['replay']['all_passed'] and audit['replay']['count']==4
        assert audit['data']['all_passed'] and audit['fresh']['all_passed']
        assert audit['fresh']['games']==4
        verify(audit['fresh']['input_sha256'])
        calls+=audit['fresh']['checked_calls']
    def detail(filename):
        checked=checked_row(filename,inputs)
        raw=read(filename)
        records=[json.loads(s) for s in Path(raw['replay_path']).read_text().splitlines()]
        side=checked['condition']['candidate_side']
        rounds=[]
        for rnd in range(1,checked['rounds']+1):
            pair={rec['player']:rec for rec in records[2*rnd:2*rnd+2]}
            row={'round':rnd}
            for label,p in (('defender',side),('attacker',1-side)):
                rec=pair[p]
                snapshot=rec['snapshot']
                row[label]=dict(actions=[x['action'] for x in rec['event'] if x['kind']=='action'],
                    gold=snapshot['gold'],factories=snapshot['n_factories'],hp=snapshot['hp'],
                    path_length=snapshot['length_path'],
                    incoming_damage=sum(x['base_damage'] for x in rec['event'] if x['kind']=='combat'))
            rounds.append(row)
        return checked,rounds
    rows=[]
    for pair in declaration['pairs']:
        old,old_history=detail(pair['old']);new,new_history=detail(pair['new'])
        assert old['condition']['candidate_spec']==new['condition']['candidate_spec']
        assert old['condition']['candidate_side']==new['condition']['candidate_side']==pair['side']
        assert old['condition']['candidate_id']==new['condition']['candidate_id']==pair['defender']
        assert old_history[0]==new_history[0],pair
        common=min(len(old_history),len(new_history))
        defender_first_difference=None
        for i in range(common):
            a,b=old_history[i],new_history[i]
            original=a['attacker']['actions'];intervention=b['attacker']['actions']
            if i==1:
                assert original==[{'op':'buy_minion','type':'tier1'}]*3+[{'op':'buy_factory'}]*2
                assert intervention==[{'op':'buy_factory'}]*2
            else: assert original==intervention,(pair,i+1)
            if defender_first_difference is None and a['defender']['actions']!=b['defender']['actions']:
                defender_first_difference=i+1
        rows.append(dict(**{k:v for k,v in pair.items() if k not in ('old','new')},old=old,new=new,common_completed_rounds=common,
            first_defender_action_difference=defender_first_difference,
            histories={'original':old_history,'without_bait':new_history},
            transition=old['outcome']+'->'+new['outcome']))
    assert len(rows)==24
    assert calls==sum(2*r['new']['rounds'] for r in rows)
    repairs=[r for r in rows if r['old']['outcome']=='L' and r['new']['outcome']!='L']
    regressions=[r for r in rows if {'L':0,'D':1,'W':2}[r['new']['outcome']]<{'L':0,'D':1,'W':2}[r['old']['outcome']]]
    grouped=defaultdict(list)
    for row in rows:grouped[row['defender']].append(row)
    formerly_all_lost=[key for key,rr in grouped.items() if all(r['old']['outcome']=='L' for r in rr)]
    h2_names=[key for key in formerly_all_lost if all(r['new']['outcome']!='L' for r in grouped[key])]
    assignments=[]
    for key,rr in grouped.items():
        for variant in ('A','B'):
            pp=sorted((r for r in rr if r['variant']==variant),key=lambda r:r['side'])
            assert len(pp)==2 and [r['side'] for r in pp]==[0,1]
            assignments.append(dict(defender=key,variant=variant,original_identical=pp[0]['old']['canonical_replay_sha256']==pp[1]['old']['canonical_replay_sha256'],
                intervention_identical=pp[0]['new']['canonical_replay_sha256']==pp[1]['new']['canonical_replay_sha256']))
    stamp=datetime.now(timezone.utc).isoformat()
    h1=bool(repairs);h2=bool(h2_names)
    lines=['# Removing three round-two tier1 purchases','',f'Checked {stamp}.','',
        f'H1, at least one previous defender loss becomes a draw or win: {"CONFIRMED" if h1 else "REFUTED"}. H2, at least one defender avoids its former four A/B losses: {"CONFIRMED" if h2 else "REFUTED"}.',
        '',f'All 24 new conditions and all 24 audited controls are included. There are {len(repairs)} repaired defender losses and {len(regressions)} worsened W/D/L outcomes. All retained actions are legal in these executions.','',
        'Each cell gives the defender outcome, defender:attacker HP and ending round. Both assignments are shown together only when these quantities agree.','',
        '| Defender | Schedule | Original | Without three tier1 | First defender action difference |','|---|---|---|---|---|']
    for key,rr in grouped.items():
        for variant in ('A','B'):
            pp=sorted((r for r in rr if r['variant']==variant),key=lambda r:r['side'])
            cells=[]
            for mode in ('old','new'):
                texts=[f'{r[mode]["outcome"]} {r[mode]["hp_candidate_first"][0]}:{r[mode]["hp_candidate_first"][1]} r{r[mode]["rounds"]}' for r in pp]
                cells.append(texts[0] if texts[0]==texts[1] else 'seat0 '+texts[0]+'; seat1 '+texts[1])
            changes=[r['first_defender_action_difference'] for r in pp]
            change=str(changes[0]) if changes[0]==changes[1] else str(changes)
            lines.append('| '+key+' | '+variant+' | '+' | '.join(cells)+' | '+change+' |')
    transitions=dict(Counter(r['transition'] for r in rows))
    lines+=['',f'Transitions, counted from the defender perspective: {json.dumps(transitions,sort_keys=True)}. All {calls} new-game decisions were independently regenerated for both actual policies. All 12 assignment pairs have original histories checked; '+str(sum(x['intervention_identical'] for x in assignments))+' new assignment pairs have identical complete canonical histories.','',
        'The only requested-schedule intervention is deleting the three tier1 purchases. The receipt checks this at every common completed round; policy-level equality at later, censored rounds is covered by the 100-round component check. Round-one records agree exactly. The receipt retains every defender and attacker action, gold balance, factory count, path length, HP and incoming damage.','',
        'This intervention changes direct damage, hit bounties and the defender\'s observable history together. Its result does not isolate bait-induced defensive spending from those other effects. A first defender action difference can also follow a changed HP comparison or budget. These are development conditions with known targets, not an estimate against unknown opponents.','',
        'Reproduce the six bait-removal manifests using the commands retained in runs/validation/bait-removal-001-pipeline.log. Independent original-engine replay, strict source and result accounting, complete data archives, action legality and observation immutability all pass.','']
    output=AREA/'RESULTS.md'
    with output.open('x') as f:f.write('\n'.join(lines))
    for p in (output,AREA/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    result=dict(time_utc=stamp,all_passed=True,new_games=24,control_games=24,fresh_decisions=calls,
        h1_repair=h1,h2_previously_all_lost_defender_repaired=h2,h2_defenders=h2_names,
        transitions=transitions,repair_count=len(repairs),regression_count=len(regressions),
        rows=rows,assignments=assignments,input_sha256=inputs)
    with (AREA/'verification/full_games.json').open('x') as f:json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Bait-removal ablation complete\n\nClaim and verdict: at least one previous defender loss repaired {"CONFIRMED" if h1 else "REFUTED"}; at least one formerly all-losing defender avoids four losses {"CONFIRMED" if h2 else "REFUTED"}. All24newgames,24controls,{calls}fresh decisions and all original-engine/source/legality checks pass. Transitions {transitions}. Full table and per-round causal diagnostics: {output}. Only the three round-two tier1 purchases were removed, with no replacement spending. This includes bounty and direct-damage effects and does not isolate psychological bait.\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','assignments','input_sha256')}))


if __name__=='__main__':main()

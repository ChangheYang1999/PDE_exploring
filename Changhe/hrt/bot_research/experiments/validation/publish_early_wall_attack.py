"""Publish every paired fourth-round intervention and its diagnostics."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
A=E/'analysis/early_wall_attack_ablation';RANK={'L':0,'D':1,'W':2}


def main():
    inputs={}
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(path):
        inputs[str(path)]=digest(path)
        return json.loads(Path(path).read_text())
    def verify(pins):
        for path,sha in pins.items():
            assert digest(path)==sha,path
            inputs[path]=sha
    declaration=read(E/'early-wall-attack-campaigns-001.json')
    verify(declaration['component_input_sha256'])
    component=read(A/'verification/component.json')
    assert component['all_passed'] and component['control_prefixes']==8 and component['variant_prefixes']==16
    assert component['filtered_proposals']==0
    verify(component['input_sha256'])
    for source in declaration['control_receipts']:
        control=read(source)
        assert control['all_audits_passed'],source
        verify(control['input_sha256'])
    old_dirs={Path(pair['old']).parent.parent for pair in declaration['pairs']}
    for directory in sorted(old_dirs):
        freeze=read(directory/'freeze.json')
        for path,sha in freeze['source_sha256'].items():
            archive=directory/'sources'/path
            assert digest(archive)==sha,path
            inputs[str(archive)]=sha
    calls=filtered=0;fresh_cases={}
    for item in declaration['campaigns']:
        name=item['name'];n=item['expected']
        manifest=read(E/(name+'.json'));verify(manifest['input_sha256'])
        audits={key:read(R/(name+'-'+key+'.json')) for key in ('strict','replay','summary','data','fresh')}
        assert audits['strict']['valid_conditions']==n and audits['strict']['attempt_counts']=={'valid':n}
        assert not audits['strict']['unresolved'] and not audits['strict']['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['replay']['count']==n
        assert audits['data']['all_passed']
        f=audits['fresh']; assert f['all_passed'] and f['games']==n
        assert f['all_replayed'] and f['all_actions_legal'] and f['all_observations_unchanged']
        verify(f['input_sha256'])
        calls+=f['checked_calls'];filtered+=f['filtered_proposals']
        for case in f['cases']:fresh_cases[case['result']]=case
    def timeline(path):
        row=read(path);side=row['condition']['candidate_side'];replay=Path(row['replay_path'])
        inputs[str(replay)]=digest(replay)
        records=[json.loads(line) for line in replay.read_text().splitlines()]
        out=[]
        for rnd in range(1,row['rounds']+1):
            record_pair={r['player']:r for r in records[2*rnd:2*rnd+2]}
            detail={'round':rnd}
            for label,s in (('guard',side),('target',1-side)):
                rec=record_pair[s]
                snapshot={k:v for k,v in rec['snapshot'].items() if k!='name'}
                actions=[event['action'] for event in rec['event'] if event['kind']=='action']
                detail[label]=dict(actions=actions,snapshot=snapshot,combat=[event for event in rec['event'] if event['kind']=='combat'])
            out.append(detail)
        return out
    rows=[];byarm=defaultdict(list)
    for pair in declaration['pairs']:
        old=checked_row(pair['old'],inputs);new=checked_row(pair['new'],inputs)
        assert old['condition']['candidate_side']==new['condition']['candidate_side']==pair['side']
        assert old['condition']['opponent_spec']==new['condition']['opponent_spec']==pair['target_spec']
        assert new['condition']['candidate_id']==pair['arm']
        old_history=timeline(pair['old']);new_history=timeline(pair['new'])
        assert old_history[:3]==new_history[:3],pair
        fresh=fresh_cases[pair['new']]
        assert fresh['witness']=='guard00'
        row=dict(arm=pair['arm'],target=pair['target'],side=pair['side'],old=old,new=new,
            transition=old['outcome']+'->'+new['outcome'],histories={'control':old_history,'intervention':new_history},
            filtered_proposals=fresh['filtered_proposals'])
        rows.append(row);byarm[pair['arm']].append(row)
    assert len(rows)==28 and calls==sum(2*r['new']['rounds'] for r in rows)
    metrics={};assignments=[]
    for arm,rr in byarm.items():
        improvements=[dict(target=r['target'],side=r['side'],transition=r['transition']) for r in rr if RANK[r['new']['outcome']]>RANK[r['old']['outcome']]]
        regressions=[dict(target=r['target'],side=r['side'],transition=r['transition']) for r in rr if RANK[r['new']['outcome']]<RANK[r['old']['outcome']]]
        metrics[arm]=dict(games=len(rr),old_counts=Counter(r['old']['outcome'] for r in rr),new_counts=Counter(r['new']['outcome'] for r in rr),
            transitions=Counter(r['transition'] for r in rr),improvements=improvements,regressions=regressions,
            paired_improvement=bool(improvements) and not regressions)
        for target in sorted({r['target'] for r in rr}):
            pp=sorted((r for r in rr if r['target']==target),key=lambda r:r['side'])
            assert len(pp)==2 and [r['side'] for r in pp]==[0,1]
            assignments.append(dict(arm=arm,target=target,identical_control=pp[0]['old']['canonical_replay_sha256']==pp[1]['old']['canonical_replay_sha256'],
                identical_intervention=pp[0]['new']['canonical_replay_sha256']==pp[1]['new']['canonical_replay_sha256']))
    hp=[r for r in rows if r['arm']=='none' and r['target']=='lead8']
    assert len(hp)==2 and all(r['old']['outcome']=='L' for r in hp)
    h1=all(r['new']['outcome']!='L' for r in hp);h2=any(m['paired_improvement'] for m in metrics.values())
    stamp=datetime.now(timezone.utc).isoformat()
    lines=['# Round-four offense or additional factories','',f'Checked {stamp}.','',
        f'H1, no round-four purchase avoids both hp_handoff losses: {"CONFIRMED" if h1 else "REFUTED"}. H2, one variant weakly improves every condition and strictly improves at least one: {"CONFIRMED" if h2 else "REFUTED"}.','',
        'The no-purchase and tier3 variants retain the early walls, round-three splash and round-five Fortress38 continuation. Remaining round-four gold follows the original factory loop. All 28 new games and fourteen reused control conditions are included.','',
        '| Target | Round-four choice | Control | Intervention |','|---|---|---|---|']
    for arm,rr in byarm.items():
        for target in sorted({r['target'] for r in rr}):
            pp=sorted((r for r in rr if r['target']==target),key=lambda r:r['side']);cells=[]
            for mode in ('old','new'):
                values=[f'{r[mode]["outcome"]} {r[mode]["hp_candidate_first"][0]}:{r[mode]["hp_candidate_first"][1]} r{r[mode]["rounds"]}' for r in pp]
                cells.append(values[0] if values[0]==values[1] else 'seat0 '+values[0]+'; seat1 '+values[1])
            lines.append('| '+target+' | '+arm+' | '+' | '.join(cells)+' |')
    lines+=['',f'The first three complete rounds agree with the original control in all 28 comparisons. All {calls} freshly regenerated decisions agree with the recorded actions; original-engine replay, source archives, exact data registration, action legality and observation immutability pass. There were {filtered} filtered proposals. '+str(sum(p['identical_intervention'] for p in assignments))+' of fourteen new assignment pairs have identical complete canonical histories.','',
        'The component check includes eight control prefixes and sixteen intervention prefixes. The tier4 implementation exactly reproduces the original on all eight five-round fixtures. Full per-round snapshots, actions, combat summaries, W/D/L transitions and any regressions are retained in verification/full_games.json.','',
        'Changes include outgoing damage, bounty income, additional factories and all later responses. Shared continuation code does not isolate any one of those mechanisms. These targets and intervention choices were selected using previous development outcomes, so this is a controlled development comparison, not untouched validation or evidence of universal superiority.','',
        'Reproduce the four manifests listed in early-wall-attack-campaigns-001.json and run the component, source, replay and fresh-policy audits shown in runs/validation/early-wall-attack-001-pipeline.log. Use the supplied Python with bytecode disabled, research-local temporary files, one low-priority assigned core and one numerical thread.','']
    output=A/'RESULTS.md'
    with output.open('x') as f:f.write('\n'.join(lines))
    for path in (output,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(path)]=digest(path)
    result=dict(time_utc=stamp,all_passed=True,new_games=28,control_conditions=14,fresh_decisions=calls,filtered_proposals=filtered,
        h1_hp_handoff_repaired=h1,h2_paired_improvement=h2,metrics=metrics,assignment_pairs=assignments,rows=rows,input_sha256=inputs)
    with (A/'verification/full_games.json').open('x') as f:json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {stamp}: Early-wall round-four ablation complete\n\nClaim and verdict: no-purchase repairs both hp_handoff losses {"CONFIRMED" if h1 else "REFUTED"}; one tested variant improves all fourteen controls in W/D/L order {"CONFIRMED" if h2 else "REFUTED"}. All28newgames,14controls,{calls}fresh calls and all source/data/legality/replay checks pass. Per-variant results: '+str({k:dict(v['new_counts']) for k,v in metrics.items()})+f'. {filtered} filtered proposals. Full paired table and histories: {output}.\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','input_sha256','assignment_pairs')}))


if __name__=='__main__':main()

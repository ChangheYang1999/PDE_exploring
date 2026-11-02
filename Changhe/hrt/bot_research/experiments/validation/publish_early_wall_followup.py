"""Publish all predeclared round-five package comparisons and failures."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E=Path('bot_research/experiments/validation')
R=Path('bot_research/runs/validation')
A=E/'analysis/early_wall_followup'
RANK={'L':0,'D':1,'W':2}


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
    declaration=read(E/'early-wall-followup-campaigns-001.json')
    verify(declaration['component_input_sha256'])
    component=read(A/'verification/component.json')
    assert component['all_passed'] and component['control_prefixes']==8 and component['variant_prefixes']==24
    assert component['filtered_proposals']==0
    verify(component['input_sha256'])
    for path in declaration['control_receipts']:
        receipt=read(path)
        assert receipt['all_audits_passed']
        verify(receipt['input_sha256'])
    for directory in sorted({Path(p['old']).parent.parent for p in declaration['pairs']}):
        freeze=read(directory/'freeze.json')
        for path,sha in freeze['source_sha256'].items():
            archive=directory/'sources'/path
            assert digest(archive)==sha,path
            inputs[str(archive)]=sha
    calls=filtered=0
    fresh={}
    for item in declaration['campaigns']:
        name=item['name'];size=item['expected']
        manifest=read(E/(name+'.json'));verify(manifest['input_sha256'])
        audits={key:read(R/(name+'-'+key+'.json')) for key in ('strict','replay','summary','data','fresh')}
        assert audits['strict']['valid_conditions']==size and audits['strict']['attempt_counts']=={'valid':size}
        assert not audits['strict']['unresolved'] and not audits['strict']['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['replay']['count']==size
        assert audits['data']['all_passed']
        f=audits['fresh']
        assert f['all_passed'] and f['games']==size and f['all_replayed']
        assert f['all_actions_legal'] and f['all_observations_unchanged']
        verify(f['input_sha256']);calls+=f['checked_calls'];filtered+=f['filtered_proposals']
        for case in f['cases']:fresh[case['result']]=case
    def history(path):
        result=read(path);side=result['condition']['candidate_side'];replay=Path(result['replay_path'])
        inputs[str(replay)]=digest(replay)
        records=[json.loads(s) for s in replay.read_text().splitlines()]
        output=[]
        for rnd in range(1,result['rounds']+1):
            pair={r['player']:r for r in records[2*rnd:2*rnd+2]};entry={'round':rnd}
            for label,s in (('guard',side),('opponent',1-side)):
                rec=pair[s]
                entry[label]=dict(snapshot={k:v for k,v in rec['snapshot'].items() if k!='name'},
                    actions=[e['action'] for e in rec['event'] if e['kind']=='action'],
                    combat=[e for e in rec['event'] if e['kind']=='combat'])
            output.append(entry)
        return output
    rows=[];groups=defaultdict(list)
    for pair in declaration['pairs']:
        old=checked_row(pair['old'],inputs);new=checked_row(pair['new'],inputs)
        assert old['condition']['candidate_side']==new['condition']['candidate_side']==pair['side']
        assert old['condition']['opponent_spec']==new['condition']['opponent_spec']==pair['target_spec']
        assert new['condition']['candidate_id']==pair['arm']
        oldh=history(pair['old']);newh=history(pair['new'])
        assert oldh[:4]==newh[:4]
        case=fresh[pair['new']]
        assert case['witness']=='guard00' and len(case['followup_trace'])==1
        trace=case['followup_trace'][0]
        assert trace['round']==5 and trace['package']==pair['arm']
        enemy=newh[3]['opponent']['snapshot']['roster']
        expected_trigger=not any(e['bought_round']<=5 and (e['expires_after_round'] is None or e['expires_after_round']>=5) for e in enemy)
        assert trace['triggered']==expected_trigger
        same=old['canonical_replay_sha256']==new['canonical_replay_sha256']
        row=dict(arm=pair['arm'],target=pair['target'],side=pair['side'],old=old,new=new,
            transition=old['outcome']+'->'+new['outcome'],trigger=trace,
            complete_control_agreement=same,histories=dict(control=oldh,intervention=newh),
            filtered_proposals=case['filtered_proposals'])
        rows.append(row);groups[pair['arm']].append(row)
    assert len(rows)==30 and calls==sum(2*r['new']['rounds'] for r in rows)
    metrics={};assignments=[]
    for arm,rr in groups.items():
        regressions=[dict(target=r['target'],side=r['side'],transition=r['transition']) for r in rr if RANK[r['new']['outcome']]<RANK[r['old']['outcome']]]
        repairs=[r for r in rr if r['target'] in ('lead8','P5M_poke0')]
        assert len(repairs)==4 and all(r['old']['outcome']=='L' for r in repairs)
        times=[r['new']['decision_seconds_candidate_first'][0] for r in rr]
        metrics[arm]=dict(games=len(rr),old_counts=Counter(r['old']['outcome'] for r in rr),
            new_counts=Counter(r['new']['outcome'] for r in rr),transitions=Counter(r['transition'] for r in rr),
            regressions=regressions,repairs_all_four=all(r['new']['outcome']!='L' for r in repairs),
            h1_success=all(r['new']['outcome']!='L' for r in repairs) and not regressions,
            triggered=sum(r['trigger']['triggered'] for r in rr),
            policy_calls=sum(t['calls'] for t in times),decision_seconds=sum(t['total'] for t in times),
            maximum_decision_seconds=max(t['max'] for t in times))
        for target in sorted({r['target'] for r in rr}):
            pp=sorted((r for r in rr if r['target']==target),key=lambda r:r['side'])
            assert len(pp)==2 and [r['side'] for r in pp]==[0,1]
            assignments.append(dict(arm=arm,target=target,
                identical_intervention=pp[0]['new']['canonical_replay_sha256']==pp[1]['new']['canonical_replay_sha256']))
    h1=any(m['h1_success'] for m in metrics.values())
    other=[r for r in rows if r['target'] not in ('lead8','P5M_poke0')]
    assert len(other)==18
    h2=all(not r['trigger']['triggered'] and r['complete_control_agreement'] for r in other)
    stamp=datetime.now(timezone.utc).isoformat()
    lines=['# An additional round-five attack after the defended opening','',f'Checked {stamp}.','',
        f'H1, at least one package repairs both targeted losses without another W/D/L regression: {"CONFIRMED" if h1 else "REFUTED"}. H2, every non-targeted control history stays unchanged: {"CONFIRMED" if h2 else "REFUTED"}.','',
        'The three packages are one tier3, two tier3, and one tier4. Each is attempted only in round five, when the opponent has no active public roster. The same frozen Fortress38 continuation then plans with the remaining gold and updated own roster. Every other decision uses the original early-wall policy. Thirty new games and ten reused controls cover five fixed opponents in both assignments.','',
        '| Opponent | Package | Original guard | Follow-up | Triggered |','|---|---|---|---|---|']
    for arm,rr in groups.items():
        for target in sorted({r['target'] for r in rr}):
            pp=sorted((r for r in rr if r['target']==target),key=lambda r:r['side']);cells=[]
            for mode in ('old','new'):
                values=[f'{r[mode]["outcome"]} {r[mode]["hp_candidate_first"][0]}:{r[mode]["hp_candidate_first"][1]} r{r[mode]["rounds"]}' for r in pp]
                cells.append(values[0] if values[0]==values[1] else 'seat0 '+values[0]+'; seat1 '+values[1])
            lines.append('| '+target+' | '+arm+' | '+' | '.join(cells)+' | '+str([r['trigger']['triggered'] for r in pp])+' |')
    lines+=['',f'All {calls} fresh policy decisions agree with their records. Every game passes original-engine replay, source/data archive checks, legal-action checks and observation immutability. There are {filtered} filtered proposals. '+str(sum(r['identical_intervention'] for r in assignments))+' of fifteen assignment pairs have identical complete canonical histories.','',
        'The first four complete rounds agree with the controls in every comparison. Eight disabled-package component prefixes reproduce the original through six rounds; twenty-four package prefixes check the predicate, purchases and legal continuation. These component checks use legal original-engine states.','',
        'Extra attack changes outgoing damage, bounty income, factories and later defenses. A favorable outcome would establish a targeted repair on this declared set only. The chosen failures were already known, so this is development evidence and does not support an untouched-validation claim. All outcomes, traces, timings, paired changes and source hashes are in verification/full_games.json.','',
        'Reproduce the six manifests in early-wall-followup-campaigns-001.json with run_data_development, then audit_development_strict, replay_audit, audit_data_archives and check_early_wall_followup_histories. The component checker is check_early_wall_followup_components. Exact bounded commands and real times are retained in runs/validation/early-wall-followup-001-pipeline.log. Use the existing Python from the project root with disabled bytecode, the research temporary directory, one assigned low-priority core and one numerical thread.','']
    output=A/'RESULTS.md'
    with output.open('x') as f:f.write('\n'.join(lines))
    for path in (output,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(path)]=digest(path)
    result=dict(time_utc=stamp,all_passed=True,new_games=30,control_conditions=10,fresh_decisions=calls,
        filtered_proposals=filtered,h1_targeted_repair=h1,h2_nontrigger_equality=h2,
        metrics=metrics,assignment_pairs=assignments,rows=rows,input_sha256=inputs)
    with (A/'verification/full_games.json').open('x') as f:json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Public-roster follow-up complete\n\nClaim and verdict: a package repairs both targeted losses without other regressions {"CONFIRMED" if h1 else "REFUTED"}; the eighteen non-targeted histories stay unchanged {"CONFIRMED" if h2 else "REFUTED"}. All thirty games, ten controls and {calls} freshly regenerated policy calls pass the complete checks, with {filtered} filtered proposals. Per-package W/D/L: '+str({k:dict(v['new_counts']) for k,v in metrics.items()})+f'. Full outcomes and scope: {output}.\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','input_sha256','assignment_pairs')}))


if __name__=='__main__':main()

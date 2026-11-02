"""Publish the full paired mode intervention, with correctly updated public models."""
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import parse_qs
import hashlib,json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
A=E/'analysis/forced_early_forecaster'
INVERSE={'W':'L','D':'D','L':'W'};RANK={'L':0,'D':1,'W':2}


def main():
    inputs={}
    def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        p=Path(p);inputs[str(p)]=digest(p);return json.loads(p.read_text())
    def records(row):
        p=Path(row['replay_path']);inputs[str(p)]=digest(p)
        out=[json.loads(line) for line in p.read_text().splitlines()]
        for item in out:item.pop('match',None)
        return out
    declared=read(E/'forced-early-forecaster-campaigns-001.json')
    component=read(A/'verification/component.json')
    assert component['all_passed'] and component['prefixes']==4
    assert declared['expected']==40 and len(declared['controls'])==40 and len(declared['campaigns'])==5
    policies={};counts={mode:Counter() for mode in ('adaptive','early')};transitions=Counter()
    calls={mode:dict(counter=0,forecaster=0,independent=0,handoffs=0,identical_assignment_pairs=0) for mode in counts}
    timing={mode:{who:dict(calls=0,total_seconds=0.0,maximum_seconds=0.0) for who in ('counter','forecaster')} for mode in counts}
    for item in declared['campaigns']:
        for mode,key in (('early','name'),('adaptive','old')):
            name=item[key];manifest=read(E/(name+'.json'))
            for p,h in manifest['input_sha256'].items():assert digest(p)==h,p
            audits={k:read(R/(name+'-'+k+'.json')) for k in ('strict','replay','summary','data','forecast','histories','delegation','fresh-forecaster')}
            summary,hist,ff,forecast,delegation=(audits[k] for k in ('summary','histories','fresh-forecaster','forecast','delegation'))
            assert audits['strict']['valid_conditions']==8 and audits['replay']['all_passed'] and audits['replay']['count']==8
            assert summary['valid_conditions']==8 and summary['unresolved_conditions']==0 and summary['complete_assignment_pairs']==4 and not summary['repeat_disagreements']
            assert audits['data']['all_passed'] and delegation['all_passed'] and delegation['games']==8
            assert forecast['valid_completed']==8 and forecast['games_with_forecast_mismatch']==0 and not forecast['failures'] and not forecast['pending']
            assert all(hist[k] for k in ('exact_counter_policy_reproduction','all_fresh_actions_legal','all_observations_unchanged','all_public_selections_verified','all_replayed'))
            assert all(ff[k] for k in ('all_fresh_actions_agree','all_predictions_exact','all_observations_unchanged','all_fresh_actions_legal','all_original_combat_agrees'))
            for audit in (hist,ff):
                for p,h in audit['input_sha256'].items():assert digest(p)==h,p
            calls[mode]['forecaster']+=ff['checked_calls'];calls[mode]['independent']+=delegation['checked_calls']
            calls[mode]['handoffs']+=delegation['handoffs'];calls[mode]['identical_assignment_pairs']+=summary['identical_assignment_pairs']
            for case in hist['cases']:
                assert case['result'] not in policies
                policies[case['result']]=case;calls[mode]['counter']+=len(case['rounds'])
    assert len(policies)==80
    for mode,c in calls.items():assert c['counter']==c['forecaster']==c['independent']
    comparisons=[];improved=worsened=repaired=0
    for pair in declared['controls']:
        checked={mode:checked_row(pair[key],inputs) for mode,key in (('adaptive','old'),('early','new'))}
        raw={mode:read(row['result_path']) for mode,row in checked.items()}
        old,new=checked['adaptive'],checked['early'];oc,nc=old['condition'],new['condition']
        assert oc['candidate_id']==nc['candidate_id'] and oc['candidate_side']==nc['candidate_side'] and oc['opponent_id']==nc['opponent_id']
        op={k:json.loads(v[0]) for k,v in parse_qs(oc['candidate_spec'].partition('?')[2]).items()}
        np={k:json.loads(v[0]) for k,v in parse_qs(nc['candidate_spec'].partition('?')[2]).items()}
        assert np['model_parameters'].pop('mode')=='early' and op==np
        old_target={k:json.loads(v[0]) for k,v in parse_qs(oc['opponent_spec'].partition('?')[2]).items()}
        new_target={k:json.loads(v[0]) for k,v in parse_qs(nc['opponent_spec'].partition('?')[2]).items()}
        assert new_target.pop('mode')=='early' and old_target==new_target=={'delegate':'fortress38'}
        assert records(raw['adaptive'])[:8]==records(raw['early'])[:8],(oc['candidate_id'],oc['candidate_side'])
        outcome={mode:INVERSE[row['outcome']] for mode,row in checked.items()}
        for mode,row in checked.items():
            counts[mode][outcome[mode]]+=1
            for who,tm in zip(('forecaster','counter'),row['decision_seconds_candidate_first']):
                dest=timing[mode][who];dest['calls']+=tm['calls'];dest['total_seconds']+=tm['total'];dest['maximum_seconds']=max(dest['maximum_seconds'],tm['max'])
        a,b=outcome['adaptive'],outcome['early'];transitions[a+'->'+b]+=1
        improved+=RANK[b]>RANK[a];worsened+=RANK[b]<RANK[a];repaired+=a=='L' and b!='L'
        comparisons.append(dict(identity=oc['candidate_id'],side=oc['candidate_side'],**pair,
            adaptive_outcome=a,early_outcome=b,adaptive_hp=old['hp_candidate_first'][::-1],early_hp=new['hp_candidate_first'][::-1],
            adaptive_rounds=old['rounds'],early_rounds=new['rounds'],adaptive_selected=policies[pair['old']]['selected'],
            early_selected=policies[pair['new']]['selected'],adaptive_handoff=policies[pair['old']]['delegate_started'],
            early_handoff=policies[pair['new']]['delegate_started'],
            adaptive_attack_count=sum(t['attack_count'] for t in raw['adaptive']['forecast_trace']),early_attack_count=sum(t['attack_count'] for t in raw['early']['forecast_trace']),
            same_complete_trajectory=old['canonical_replay_sha256']==new['canonical_replay_sha256']))
    assert len(comparisons)==40
    verdict='CONFIRMED' if repaired and not worsened else 'REFUTED'
    no_losses='CONFIRMED' if counts['early']['L']==0 else 'REFUTED'
    def cell(rows,mode):
        values=[f'{v[mode+"_outcome"]} {v[mode+"_hp"][0]}:{v[mode+"_hp"][1]} r{v[mode+"_rounds"]}, handoff {v[mode+"_handoff"]}' for v in sorted(rows,key=lambda x:x['side'])]
        assert len(values)==2
        return values[0] if values[0]==values[1] else '; '.join(f'seat{i}: {v}' for i,v in enumerate(values))
    table=[]
    for identity in sorted({v['identity'] for v in comparisons}):
        rows=[v for v in comparisons if v['identity']==identity]
        table.append(f'| {identity} | {cell(rows,"adaptive")} | {cell(rows,"early")} |')
    now=datetime.now(timezone.utc).isoformat();score=lambda c:f'{c["W"]}W/{c["D"]}D/{c["L"]}L'
    text=f'''# Forced early branch against matching public clones

Checked {now}.

The paired repair claim is {verdict}: {repaired} old target losses become nonlosses, with {worsened} W/D/L regressions. The stricter no-target-loss claim is {no_losses}.

From the target counter's perspective, adaptive mode scores {score(counts['adaptive'])}; forced early scores {score(counts['early'])}. There are {improved} improved conditions. All twenty timing configurations and both assignments are included. The attacker forecasts the corresponding mode in each experiment, so this comparison changes both the target's branch policy and the attacker's correct private model. It does not pretend that a stale forecast is an exact one.

Each cell gives target outcome, HP target:attacker, final round and first delegate round. None means the delegate was never called. Equal physical assignments share a cell.

| Attacker configuration | Adaptive target | Forced early target |
|---|---|---|
'''+ '\n'.join(table)+f'''

All eighty underlying games pass strict accounting, original-engine replay, registered-source/data checks and exact actual forecast diagnostics. Four component prefixes passed {component['checked_rounds']} reached rounds before the new game manifests. Fresh checks reproduce {calls['early']['counter']} new target and {calls['early']['forecaster']} new attacker decisions, plus {calls['adaptive']['counter']} corresponding adaptive target and attacker decisions. Every submitted action is legal, observations remain unchanged, and original incoming damage agrees with forecast residuals. Independent handoff reconstruction agrees in every reached round. All forty paired histories are exactly equal through round three after removing only the run identifier.

These are deterministic targeted development conditions, not independent samples or reserved final validation. The complete transition table, attack counts, handoff rounds and measured low-priority decision times are in verification/full_games.json. Exact reproduction on these histories does not establish load-independent behavior for planners with wall-clock cutoffs. This experiment does not modify the installed best bot.

Reproduce the five forced-early-forecaster manifests with run_data_forecasts and the audit sequence in their pipeline log. The comparison also needs the five adaptive Fortress 38 campaigns from delegated_forecaster version 002. Use the original project environment, disabled bytecode, the research temporary directory, fixed affinity, one numerical thread and low priority.
'''
    output=A/'RESULTS.md'
    with output.open('x') as f:f.write(text)
    for p in (output,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    receipt=dict(time_utc=now,all_audits_passed=True,new_games=40,old_controls=40,repair_verdict=verdict,no_losses_verdict=no_losses,
        target_outcomes=counts,transitions=transitions,improved=improved,worsened=worsened,repaired_losses=repaired,exact_first_three_round_pairs=40,
        calls=calls,timing=timing,comparisons=comparisons,input_sha256=inputs)
    with (A/'verification/full_games.json').open('x') as f:json.dump(receipt,f,indent=2,sort_keys=True);f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {now}: Forced early branch challenge complete\n\nClaim and verdict: {verdict}, at least one public-clone loss repaired with no W/D/L regression; eliminating every target loss is {no_losses}. Method: forty new games against correctly updated public-clone models, paired with all forty adaptive controls; identical first-three-round histories. Result: adaptive {score(counts["adaptive"])}, early {score(counts["early"])}, {improved} improvements, {worsened} regressions. All replay, exact forecast, fresh-policy, legality and independent handoff checks pass. Development ablation, not reserved validation. Evidence: {output}.\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ('comparisons','input_sha256')}))

if __name__=='__main__':main()

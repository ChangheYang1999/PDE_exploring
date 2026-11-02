"""Publish the fixed public-clone challenge, including all non-winning settings."""
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
AREA=E/'analysis/delegated_forecaster'


def canonical(records,side):
    records=json.loads(json.dumps(records))
    for r in records:
        r.pop('match',None);r['player']^=side
        r['snapshot']['name']='forecaster' if r['player']==0 else 'target'
        for event in r['event']:event.pop('order',None)
        if r.get('result',{}).get('winner') is not None:r['result']['winner']^=side
    return sorted(records,key=lambda r:(r['round'],r['player']))


def main():
    inputs={}
    def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        p=Path(p);inputs[str(p)]=digest(p);return json.loads(p.read_text())
    def records(row):
        p=Path(row['replay_path']);inputs[str(p)]=digest(p)
        return [json.loads(line) for line in p.read_text().splitlines()]
    declared=read(E/'delegated-forecaster-campaigns-002.json')
    component=read(AREA/'verification/component.json')
    assert component['all_passed'] and component['prefixes']==8
    assert declared['expected']==80 and len(declared['campaigns'])==10
    allrows={};fresh_counter=fresh_forecaster=independent=0;handoffs=0;pair_agreements=0
    outcomes={mode:Counter() for mode in ('template','fortress38')}
    timing={mode:{who:dict(calls=0,total_seconds=0.0,maximum_seconds=0.0) for who in ('forecaster','target')} for mode in outcomes}
    for item in declared['campaigns']:
        name,mode=item['name'],item['delegate'];assert item['expected']==8
        manifest=read(E/(name+'.json'))
        for p,h in manifest['input_sha256'].items():assert digest(p)==h,p
        audits={k:read(R/(name+'-'+k+'.json')) for k in ('strict','replay','summary','data','forecast','histories','delegation','fresh-forecaster')}
        assert audits['strict']['valid_conditions']==8 and audits['replay']['all_passed'] and audits['replay']['count']==8
        summary=audits['summary'];hist=audits['histories'];ff=audits['fresh-forecaster'];forecast=audits['forecast'];delegation=audits['delegation']
        assert summary['valid_conditions']==8 and summary['unresolved_conditions']==0 and summary['complete_assignment_pairs']==4
        assert not summary['repeat_disagreements'];pair_agreements+=summary['identical_assignment_pairs']
        assert audits['data']['all_passed'] and delegation['all_passed'] and delegation['games']==8
        assert forecast['valid_completed']==8 and forecast['games_with_forecast_mismatch']==0 and not forecast['failures'] and not forecast['pending']
        assert all(hist[k] for k in ('exact_counter_policy_reproduction','all_fresh_actions_legal','all_observations_unchanged','all_public_selections_verified','all_replayed'))
        assert all(ff[k] for k in ('all_fresh_actions_agree','all_predictions_exact','all_observations_unchanged','all_fresh_actions_legal','all_original_combat_agrees'))
        for audit in (hist,ff):
            for p,h in audit['input_sha256'].items():assert digest(p)==h,p
        fresh_forecaster+=ff['checked_calls'];independent+=delegation['checked_calls'];handoffs+=delegation['handoffs']
        for case in hist['cases']:
            fresh_counter+=len(case['rounds']);checked=checked_row(case['result'],inputs);raw=read(case['result'])
            condition=checked['condition'];identity=condition['candidate_id'];side=condition['candidate_side'];key=(mode,identity,side)
            assert key not in allrows
            traces=raw['forecast_trace'];assert len(traces)==raw['rounds']
            allrows[key]=dict(**checked,mode=mode,selected=case['selected'],delegate_started=case['delegate_started'],
                attack_rounds=[t['round'] for t in traces if t.get('attack_count',0)],
                actual_attack_count=sum(t.get('attack_count',0) for t in traces),
                predicted_attack_gains=[dict(round=t['round'],gain=t['forecast_attack_gain']) for t in traces if t.get('attack_count',0)])
            outcomes[mode][checked['outcome']]+=1
            for who,tm in zip(('forecaster','target'),checked['decision_seconds_candidate_first']):
                dest=timing[mode][who];dest['calls']+=tm['calls'];dest['total_seconds']+=tm['total'];dest['maximum_seconds']=max(dest['maximum_seconds'],tm['max'])
    assert len(allrows)==80 and fresh_forecaster==fresh_counter==independent
    assert sum(v['forecaster']['calls'] for v in timing.values())==fresh_forecaster
    assert sum(v['target']['calls'] for v in timing.values())==fresh_counter
    identities=sorted({key[1] for key in allrows});assert len(identities)==20
    comparisons=[];table=[];wins={mode:[] for mode in outcomes}
    for identity in identities:
        for mode in outcomes:
            group=[allrows[mode,identity,side] for side in (0,1)]
            if all(row['outcome']=='W' for row in group):wins[mode].append(identity)
        for side in (0,1):
            old,new=allrows['template',identity,side],allrows['fortress38',identity,side]
            a,b=records(read(old['result_path'])),records(read(new['result_path']))
            for record in a+b:record.pop('match',None)
            assert a[:10]==b[:10],(identity,side)
            same=canonical(a,side)==canonical(b,side)
            assert same==(old['canonical_replay_sha256']==new['canonical_replay_sha256'])
            assert old['selected']==new['selected']
            if new['selected']=='growth':assert same
            comparisons.append(dict(identity=identity,side=side,old=old['result_path'],new=new['result_path'],same_complete_trajectory=same,selected=new['selected']))
        def cell(mode):
            group=[allrows[mode,identity,side] for side in (0,1)]
            text=[f'{r["outcome"]} {r["hp_candidate_first"][0]}:{r["hp_candidate_first"][1]} r{r["rounds"]}, buy {r["actual_attack_count"]}' for r in group]
            return text[0] if text[0]==text[1] else '; '.join(f'seat{i} {v}' for i,v in enumerate(text))
        table.append(f'| {identity} | {cell("template")} | {cell("fortress38")} |')
    repeat_controls=[]
    assert len(declared['initial_repeat_controls'])==8
    for pair in declared['initial_repeat_controls']:
        old,new=checked_row(pair['a'],inputs),checked_row(pair['b'],inputs)
        assert old['condition']==new['condition']
        assert old['canonical_replay_sha256']==new['canonical_replay_sha256']
        repeat_controls.append(dict(**pair,same_complete_trajectory=True))
    read(E/'delegated-forecaster-campaigns-001.json')
    for p in (AREA/'TRACE_CORRECTION.md',R/'delegated-forecaster-001-pipeline.log'):
        inputs[str(p)]=digest(p)
    verdict='CONFIRMED' if wins['fortress38'] else 'REFUTED'
    now=datetime.now(timezone.utc).isoformat();output=AREA/'RESULTS.md'
    score=lambda c:f'{c["W"]}W/{c["D"]}D/{c["L"]}L'
    text=f'''# Public-clone timing challenge

Checked {now}.

The finite-family claim is {verdict}: at least one of the twenty declared public-clone timing attackers defeats the Fortress 38 continuation in both physical assignments.

From the forecaster's perspective, the forty games against the template continuation give {score(outcomes['template'])}; the forty against Fortress 38 give {score(outcomes['fortress38'])}. Every declared timing and defense-first setting is included. The settings that win in both assignments are recorded explicitly in the verification receipt. Failure of this finite family would not prove that the target is unexploitable.

Each cell gives the forecaster outcome, HP forecaster:target, final round and actual minion-purchase count. Equal assignments share a cell; differing assignments are explicit. The model parameters match the actual target. Its independently initialized private copy receives one copied public observation per reached round and never reads pending target actions.

| Forecaster setting | Against template continuation | Against Fortress 38 continuation |
|---|---|---|
'''+ '\n'.join(table)+f'''

All eighty games pass strict accounting, original-engine replay and source/data archive checks. The eight component prefixes passed {component['checked_rounds']} reached rounds before the game manifests were declared. Fresh checks reproduce {fresh_forecaster} forecaster decisions and {fresh_counter} independent target decisions. All actual target forecasts agree, and original incoming damage equals the predicted residual on every round. Observations are unchanged and submitted actions are legal. The handoff checker independently reconstructs {independent} target calls and {handoffs} starts. {pair_agreements} of forty assignment pairs have identical complete canonical histories.

The corresponding template/Fortress 38 experiments have exactly equal complete records through round four in all forty pairs after removing only their run identifier. Selected growth-branch histories agree completely. These are direct checks on the observed histories, not an arbitrary-load determinism guarantee. The conditional induction in PROOF.md requires deterministic policy transitions; teammate planner deadlines make that hypothesis a separate issue from the exact agreement actually measured here.

These are targeted development opponents with access to public target source, not hidden information and not untouched final validation. Measured decision-call totals and maxima for both players are retained by target mode. The experiment does not change best.py or its reserved-pool evidence.

The first eight version 001 games omitted forecast traces because the initial driver used isolated_match. They passed engine replay but could not validate forecasts. Version 002 used forecast_match via run_data_forecasts, with unchanged policies and conditions. All eight repeated complete histories agree exactly. TRACE_CORRECTION.md and the retained initial failure log record this instrument correction; those repeats are not additional strength evidence.

Reproduce the ten version 002 delegated-forecaster manifests with run_data_forecasts, then the strict, replay, summary, archive, forecast, target-policy, handoff and fresh-forecaster checks named in the campaign logs. Use the original project environment, disabled bytecode, the research temporary directory, assigned affinity, one numerical thread and low priority. verification/full_games.json pins the evidence and publisher.
'''
    with output.open('x') as f:f.write(text)
    for p in (output,AREA/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    receipt=dict(time_utc=now,all_audits_passed=True,verdict=verdict,games=80,forecaster_outcomes=outcomes,
        winning_settings_both_assignments=wins,fresh_forecaster_calls=fresh_forecaster,fresh_target_calls=fresh_counter,
        independent_handoff_calls=independent,handoffs=handoffs,identical_assignment_pairs=pair_agreements,
        exact_first_four_round_pairs=40,initial_repeat_controls=repeat_controls,rows=list(allrows.values()),comparisons=comparisons,timing=timing,input_sha256=inputs)
    with (AREA/'verification/full_games.json').open('x') as f:json.dump(receipt,f,indent=2,sort_keys=True);f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {now}: Public-clone timing challenge complete\n\n'
        f'Claim and verdict: {verdict}, at least one declared public-clone timing setting defeats the Fortress 38 continuation in both assignments. '
        f'Method: eighty games with both target continuations, all twenty settings, unchanged engine and exact public forecasts. '
        f'Result from forecaster perspective: template {score(outcomes["template"])}, Fortress38 {score(outcomes["fortress38"])}. '
        f'All {fresh_forecaster} fresh forecaster decisions and {fresh_counter} fresh target decisions agree, with exact original incoming combat and independent handoff checks. '
        f'Targeted development only. Evidence: {output}.\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ('rows','comparisons','input_sha256')}))

if __name__=='__main__':main()

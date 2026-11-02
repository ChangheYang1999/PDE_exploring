"""Publish the entire fixed timing grid and preserve its initial data-audit failure."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E=Path('bot_research/experiments/validation')
R=Path('bot_research/runs/validation')
AREA=E/'analysis/delegated_timing'
INV={'W':'L','D':'D','L':'W'}
RANK={'L':0,'D':1,'W':2}


def canonical(records, side):
    records=json.loads(json.dumps(records))
    for rec in records:
        rec.pop('match',None)
        rec['player'] ^= side
        rec['snapshot']['name']='target' if rec['player']==0 else 'counter'
        for event in rec['event']:
            event.pop('order',None)
        if rec.get('result',{}).get('winner') is not None:
            rec['result']['winner'] ^= side
    return sorted(records,key=lambda rec:(rec['round'],rec['player']))


def main():
    inputs={}
    def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        p=Path(p);inputs[str(p)]=digest(p)
        return json.loads(p.read_text())
    def records(row):
        p=Path(row['replay_path']);inputs[str(p)]=digest(p)
        return [json.loads(line) for line in p.read_text().splitlines()]
    declared=read(E/'delegated-timing-controls-002.json')
    assert len(declared['pairs'])==60 and len(declared['campaigns'])==10
    cases={};fresh=independent=handoffs=0;campaigns=[]
    for item in declared['campaigns']:
        name=item['name'];assert item['expected']==12
        manifest=read(E/(name+'.json'))
        for p,h in manifest['input_sha256'].items():assert digest(p)==h,p
        audits={k:read(R/(name+'-'+k+'.json')) for k in ('strict','replay','summary','data','histories','delegation')}
        assert audits['strict']['valid_conditions']==12
        summary=audits['summary'];history=audits['histories'];delegation=audits['delegation']
        assert summary['valid_conditions']==12 and summary['unresolved_conditions']==0
        assert summary['complete_assignment_pairs']==6 and not summary['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['replay']['count']==12
        assert audits['data']['all_passed'] and delegation['all_passed'] and delegation['games']==12
        assert all(history[k] for k in ('exact_counter_policy_reproduction','all_fresh_actions_legal',
            'all_observations_unchanged','all_public_selections_verified','all_replayed'))
        for p,h in history['input_sha256'].items():assert digest(p)==h,p
        for case in history['cases']:
            assert case['result'] not in cases
            cases[case['result']]=case;fresh+=len(case['rounds'])
        independent+=delegation['checked_calls'];handoffs+=delegation['handoffs']
        campaigns.append(dict(name=name,delegate=item['delegate'],games=12,
                              identical_assignment_pairs=summary['identical_assignment_pairs']))
    assert len(cases)==120 and fresh==independent
    stats={mode:dict(outcomes=Counter(),branches=Counter(),calls=0,total_seconds=0.0,maximum_seconds=0.0)
           for mode in ('template','fortress38')}
    comparisons=[];transitions=Counter();growth=exact_growth=exact_all=0
    for pair in declared['pairs']:
        old,new=checked_row(pair['old'],inputs),checked_row(pair['new'],inputs)
        oldraw,newraw=read(pair['old']),read(pair['new'])
        for row in (old,new):
            c=row['condition']
            assert c['candidate_id']==pair['target'] and c['candidate_spec']==pair['target_spec']
            assert c['candidate_side']==pair['candidate_side'] and c['opponent_id']=='route_adaptive'
        a,b=records(oldraw),records(newraw)
        for rec in a+b:rec.pop('match',None)
        assert a[:10]==b[:10],pair['target']
        aa,bb=canonical(a,pair['candidate_side']),canonical(b,pair['candidate_side'])
        same=aa==bb
        assert same==(old['canonical_replay_sha256']==new['canonical_replay_sha256'])
        exact_all+=same
        assert cases[pair['old']]['selected']==cases[pair['new']]['selected']
        selected=cases[pair['new']]['selected']
        if selected=='growth':growth+=1;exact_growth+=same
        was,now=INV[old['outcome']],INV[new['outcome']];transitions[was+'->'+now]+=1
        params={k:json.loads(v[0]) for k,v in parse_qs(pair['target_spec'].partition('?')[2]).items()}
        attack_counts={}
        for mode,row,raw,recs,path in (('template',old,oldraw,a,pair['old']),('fortress38',new,newraw,b,pair['new'])):
            stats[mode]['outcomes'][INV[row['outcome']]]+=1
            stats[mode]['branches'][cases[path]['selected']]+=1
            t=row['decision_seconds_candidate_first'][1]
            stats[mode]['calls']+=t['calls'];stats[mode]['total_seconds']+=t['total']
            stats[mode]['maximum_seconds']=max(stats[mode]['maximum_seconds'],t['max'])
            purchases=[]
            for rec in recs:
                if rec['player']!=pair['candidate_side']:continue
                for event in rec['event']:
                    if event['kind']=='action' and event['action']['op']=='buy_minion':
                        assert rec['round']==params['attack_round'] and event['action']['type']==params['tier']
                        purchases.append(event['action'])
            attack_counts[mode]=len(purchases)
        comparisons.append(dict(**pair,old_outcome=was,new_outcome=now,
            old_hp_counter_first=old['hp_candidate_first'][::-1],new_hp_counter_first=new['hp_candidate_first'][::-1],
            old_final_round=old['rounds'],new_final_round=new['rounds'],selected=selected,
            new_delegate_started=cases[pair['new']]['delegate_started'],same_complete_trajectory=same,
            actual_timed_purchase_counts=attack_counts))
    assert growth==exact_growth
    assert sum(s['calls'] for s in stats.values())==fresh
    repeat=[]
    for pair in declared['initial_repeat_controls']:
        old,new=checked_row(pair['old'],inputs),checked_row(pair['new'],inputs)
        assert old['condition']==new['condition']
        side=old['condition']['candidate_side']
        same=canonical(records(read(pair['old'])),side)==canonical(records(read(pair['new'])),side)
        assert same and old['canonical_replay_sha256']==new['canonical_replay_sha256']
        repeat.append(dict(**pair,same_complete_trajectory=True))
    assert len(repeat)==12
    worsened=[r for r in comparisons if RANK[r['new_outcome']]<RANK[r['old_outcome']]]
    no_losses=stats['fortress38']['outcomes']['L']==0
    preserves=not worsened
    verdicts=dict(no_defeats='CONFIRMED' if no_losses else 'REFUTED',
                  no_outcome_regressions='CONFIRMED' if preserves else 'REFUTED')
    def score(c):return f'{c["W"]}W/{c["D"]}D/{c["L"]}L'
    table=[]
    for target in sorted({r['target'] for r in comparisons}):
        rows=sorted((r for r in comparisons if r['target']==target),key=lambda r:r['candidate_side'])
        assert len(rows)==2
        def cell(prefix):
            text=[f'{r[prefix+"_outcome"]} {r[prefix+"_hp_counter_first"][0]}:{r[prefix+"_hp_counter_first"][1]} r{r[prefix+"_final_round"]}' for r in rows]
            return text[0] if text[0]==text[1] else '; '.join(f'seat{i} {v}' for i,v in enumerate(text))
        counts=[r['actual_timed_purchase_counts'] for r in rows]
        count_text=(f'{counts[0]["template"]}/{counts[0]["fortress38"]}' if counts[0]==counts[1] else json.dumps(counts))
        selected='/'.join(sorted({r['selected'] for r in rows}))
        table.append(f'| {target} | {cell("old")} | {cell("new")} | {selected} | {count_text} |')
    now=datetime.now(timezone.utc).isoformat()
    output=AREA/'RESULTS.md'
    text=f'''# Timing challenge results

Checked {now}.

The no-defeat claim is {verdicts['no_defeats']}. The no-W/D/L-regression claim is {verdicts['no_outcome_regressions']}.

The emergency-template control scores {score(stats['template']['outcomes'])}; the frozen Fortress 38 handoff scores {score(stats['fortress38']['outcomes'])}. All sixty conditions per continuation are included. W/D/L transitions are {dict(transitions)}. These are thirty deliberately selected development targets in both physical assignments, not samples from an opponent population.

Each outcome cell gives counter outcome, HP counter:target and final round. Equal assignments share a cell; differences are explicit. The last column gives the target's actual minion-purchase count against template/Fortress 38. The target parameter is a proposed attack round; an unaffordable or unproductive attack can result in zero purchases. Its budget fraction controls defensive forecasting.

| Target | Emergency template | Fortress 38 handoff | Selected branch | Actual target purchases old/new |
|---|---|---|---|---|
'''+ '\n'.join(table)+f'''

All 120 games pass strict accounting, original-engine replay, registered source/data checks, and {fresh} freshly regenerated counter decisions. Every submitted action is legal, observations remain unchanged, and no bot error is recorded. An independent implementation checks {independent} public handoff decisions and {handoffs} actual starts. Every paired game has exactly the same first four complete rounds after removing only the run identifier. All {growth} selected growth-branch pairs have identical complete histories; {exact_all} of sixty pairs agree completely overall.

The first 001 attempt stopped after twelve games when its archive audit found three unregistered JSON dependencies. These files already had constructor-level hash checks, but that did not satisfy explicit data registration. The full unchanged grid was redeclared as002 with all three files registered and archived. All twelve completed initial histories agree exactly with the corresponding corrected runs. Both attempts and the audit failure are retained. Only the complete002 grid supplies the table above.

Measured counter decision costs are summarized in the receipt as call counts, summed wall time and maximum call time. They are low-priority measurements on shared hardware. Frozen teammate planners may use wall-clock cutoffs; observed equality does not guarantee equality under arbitrary load. No installed-candidate change or held-out claim follows.

Reproduce the ten delegated-timing-*-002 manifests using run_data_development, then audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, check_delegated_histories and audit_delegation. Run this publisher after all campaigns finish. Use the existing project Python, disabled bytecode, research temporary directory, assigned affinity, one numerical thread and low priority. Exact commands are in the corrected pipeline log; verification/full_games.json pins all result inputs and the publisher.
'''
    with output.open('x') as f:f.write(text)
    for p in (output,AREA/'PROOF.md',AREA/'MANIFEST_CORRECTION.md',R/'delegated-timing-001-pipeline.log',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    receipt=dict(time_utc=now,all_audits_passed=True,verdicts=verdicts,games=120,
        initial_attempt_games=12,initial_exact_repeat_controls=repeat,statistics=stats,transitions=transitions,
        fresh_counter_decisions=fresh,independent_handoff_calls=independent,handoffs=handoffs,
        exact_first_four_round_pairs=60,growth_pairs=growth,exact_growth_pairs=exact_growth,
        exact_complete_pairs=exact_all,comparisons=comparisons,campaigns=campaigns,input_sha256=inputs)
    with (AREA/'verification/full_games.json').open('x') as f:json.dump(receipt,f,indent=2,sort_keys=True);f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {now}: Timing challenge complete\n\n'
        f'Claim and verdict: no defeats {verdicts["no_defeats"]}; no W/D/L regressions {verdicts["no_outcome_regressions"]}. '
        f'Method: 120 games, thirty fixed timing/defensive-budget settings, two continuations and both assignments. '
        f'Result: template {score(stats["template"]["outcomes"])}, Fortress38 {score(stats["fortress38"]["outcomes"])}; '
        f'{fresh} fresh decisions, all independent handoffs and sixty identical first-four-round prefixes pass. '
        f'Twelve initial games with incomplete data registration are retained and exactly reproduced by the corrected manifest set. Development only. Evidence: {output}.\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ('comparisons','campaigns','input_sha256','initial_exact_repeat_controls')}))


if __name__=='__main__':main()

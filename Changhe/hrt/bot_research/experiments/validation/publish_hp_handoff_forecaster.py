"""Publish every matching-model attack on fixed H, including declined purchases."""
from collections import Counter,defaultdict
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import parse_qs
import hashlib,json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation');A=E/'analysis/hp_handoff_forecaster'

def main():
    inputs={}
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        inputs[str(p)]=digest(p);return json.loads(Path(p).read_text())
    def verify(mapping):
        for p,h in mapping.items():assert digest(p)==h;inputs[p]=h
    d=read(E/'hp-handoff-forecaster-campaigns-001.json');verify(d['input_sha256'])
    previous=read(d['previous_table']);assert previous['all_passed'];verify(previous['input_sha256'])
    assert previous['certificate']['weights']==['0','0','0','0','1']
    component=read(A/'verification/component.json');verify(component['input_sha256'])
    assert component['all_passed'] and component['prefixes']==4 and component['filtered_proposals']==0
    cases=[];calls=predictions=0
    for item in d['campaigns']:
        name=item['name'];directory=R/name;size=item['expected']
        m=read(E/(name+'.json'));verify(m['input_sha256'])
        audits={key:read(R/(name+'-'+key+'.json')) for key in ('strict','replay','data','fresh','predictions')}
        assert audits['strict']['valid_conditions']==size and audits['strict']['attempt_counts']=={'valid':size}
        assert not audits['strict']['unresolved'] and not audits['strict']['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['replay']['count']==size
        assert audits['data']['all_passed']
        fresh=audits['fresh'];pred=audits['predictions']
        assert all(fresh[k] for k in ('all_passed','all_replayed','all_actions_legal','all_observations_unchanged'))
        assert fresh['games']==size
        assert all(pred[k] for k in ('all_fresh_actions_agree','all_predictions_exact','all_observations_unchanged','all_fresh_actions_legal','all_original_combat_agrees'))
        verify(fresh['input_sha256']);verify(pred['input_sha256'])
        calls+=fresh['checked_calls'];predictions+=pred['checked_calls']
        for i in range(size):
            path=directory/'results'/f'case{i:04d}.json';raw=read(path);r=checked_row(str(path),inputs)
            c=r['condition'];assert c['opponent_spec']==d['target']['spec']
            params={k:json.loads(v[0]) for k,v in parse_qs(c['candidate_spec'].partition('?')[2]).items()}
            assert params['model_spec']=='bot_research.bots.counters.hp_handoff:@make'
            targetparams={k:json.loads(v[0]) for k,v in parse_qs(d['target']['spec'].partition('?')[2]).items()}
            assert params['model_parameters']==targetparams
            assert not raw['forecast_mismatch_rounds'] and not raw['forecast_trace_missing_rounds']
            buy=[t for t in raw['forecast_trace'] if t['round']==params['attack_round']]
            assert len(buy)==1
            cases.append(dict(result=str(path),condition=c,attacker_parameters=params,
                target_outcome={'W':'L','D':'D','L':'W'}[r['outcome']],target_first_hp=list(reversed(r['hp_candidate_first'])),
                rounds=r['rounds'],purchase=buy[0],canonical_replay_sha256=r['canonical_replay_sha256'],
                decision_seconds_target_first=list(reversed(r['decision_seconds_candidate_first']))))
    assert len(cases)==24 and calls==sum(2*c['rounds'] for c in cases) and predictions==sum(c['rounds'] for c in cases)
    groups=defaultdict(list)
    for c in cases:groups[c['condition']['candidate_id']].append(c)
    pairs=[]
    for key,rr in groups.items():
        rr.sort(key=lambda c:c['condition']['candidate_side'])
        assert [c['condition']['candidate_side'] for c in rr]==[0,1]
        assert rr[0]['target_outcome']==rr[1]['target_outcome']
        pairs.append(dict(setting=key,identical_complete_trajectory=rr[0]['canonical_replay_sha256']==rr[1]['canonical_replay_sha256']))
    counts=Counter(c['target_outcome'] for c in cases);h1=counts['L']==0
    stamp=datetime.now(timezone.utc).isoformat()
    lines=['# A targeted timing challenge to the HP-triggered grower','',f'Checked {stamp}.','',
        f'H1, no H loss on the twelve declared matching-model settings in both assignments: {"CONFIRMED" if h1 else "REFUTED"}. H scores {counts["W"]}W/{counts["D"]}D/{counts["L"]}L in the twenty-four games.','',
        'H is unchanged from the completed five-policy table. Each attacker privately models that same H policy from public observations. The six round/tier settings and both defensive orderings were fixed before execution. This directly challenges the scope of the earlier finite-table result; the attackers were not members of that table.','',
        '| Attack setting | H outcome | HP H:attacker | End round | Units bought |','|---|---|---|---:|---:|']
    for key,rr in groups.items():
        c=rr[0]
        assert all((x['target_first_hp'],x['rounds'],x['purchase']['attack_count'])==(c['target_first_hp'],c['rounds'],c['purchase']['attack_count']) for x in rr)
        lines.append(f'| {key} | {c["target_outcome"]} | {c["target_first_hp"][0]}:{c["target_first_hp"][1]} | {c["rounds"]} | {c["purchase"]["attack_count"]} |')
    lines+=['',f'Each row represents both assignments. {sum(p["identical_complete_trajectory"] for p in pairs)} of twelve pairs have identical complete canonical histories. All {calls} external policy decisions are freshly regenerated; {predictions} additional attacker regenerations verify the saved trace, exact target predictions and original incoming combat. No observation is mutated, no submitted action is rejected, and no bot or source error is recorded. Four prefix components passed before the full games.','',
        'Exact prediction is conditional on these reached histories and computations. It does not prove best-response optimality, and repeated deterministic histories are not independent random evidence. The actual attack count is reported even if the attacker declined a nonprofitable or unaffordable purchase. All results, timings, declarations and hashes are retained in verification/full_games.json.','',
        'Reproduce the six hp-handoff-forecaster manifests with run_data_forecasts, followed by audit_development_strict, replay_audit, audit_data_archives, check_fixed_game_histories and check_timing_forecaster_histories. The component checker is check_hp_forecast_components. The bounded commands and real timestamps are in runs/validation/hp-handoff-forecaster-001-pipeline.log. Use the supplied environment from the project root with disabled bytecode, research-local temporary files, a free assigned low-priority core and one numerical thread.','']
    output=A/'RESULTS.md'
    with output.open('x') as f:f.write('\n'.join(lines))
    for p in (output,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    result=dict(time_utc=stamp,all_passed=True,games=24,counts=counts,h1_target_has_no_loss=h1,
        fresh_external_decisions=calls,additional_prediction_checks=predictions,pairs=pairs,cases=cases,input_sha256=inputs)
    atomic_json(A/'verification/full_games.json',result,exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {stamp}: Fixed H clone challenge complete\n\nClaim and verdict: H avoids every declared timing attack {"CONFIRMED" if h1 else "REFUTED"}. H scores{dict(counts)} on24games. All{calls}external decisions and{predictions}additional prediction/combat checks pass. Twelve measured assignment pairs, all outcomes and actual purchase counts retained. This does not change the earlier five-policy certificate; the attackers are new selected development opponents. See {output}.\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('cases','input_sha256','pairs')}),flush=True)

if __name__=='__main__':main()

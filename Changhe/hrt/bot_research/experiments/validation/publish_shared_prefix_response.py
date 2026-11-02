"""Publish independently checked public-response selection results."""
from collections import defaultdict
from datetime import datetime,timezone
from fractions import Fraction
from pathlib import Path
import hashlib,json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.publish_extended_counter_game import norm
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation');A=E/'analysis/shared_prefix_response'


def main():
    inputs={};digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        inputs[str(p)]=digest(p);return json.loads(Path(p).read_text())
    def verify(mapping):
        for p,h in mapping.items():assert digest(p)==h,p;inputs[p]=h
    d=read(E/'shared-prefix-campaigns-001.json');verify(d['input_sha256'])
    component=read(A/'verification/components.json');assert component['all_passed'] and len(component['cases'])==6;verify(component['input_sha256'])
    old=read(E/'analysis/six_policy_game/verification/full_games.json');assert old['all_passed']
    assert all(d['policies'][k]==old['policies'][k] for k in old['policies'])
    assert old['certificate']['weights']==['0','0','0','1/3','1/3','1/3']
    cases=[];fresh_calls=reference_calls=0;groups=defaultdict(list)
    for campaign in d['campaigns']:
        name=campaign['name'];size=campaign['expected'];root=R/name
        m=read(E/(name+'.json'));verify(m['input_sha256'])
        audits={k:read(R/(name+'-'+k+'.json')) for k in ('strict','replay','data','fresh','branches')}
        strict=audits['strict'];assert strict['valid_conditions']==size and strict['attempt_counts']=={'valid':size}
        assert not strict['unresolved'] and not strict['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['replay']['count']==size and audits['data']['all_passed']
        for kind in ('fresh','branches'):
            a=audits[kind]
            assert all(a[k] for k in ('all_passed','all_replayed','all_actions_legal','all_observations_unchanged'))
            verify(a['input_sha256'])
        assert audits['fresh']['games']==size and audits['branches']['all_reference_actions_agree']
        fresh_calls+=audits['fresh']['checked_calls'];reference_calls+=audits['branches']['checked_calls']
        branches={x['result_path']:x for x in audits['branches']['cases']}
        freeze=read(root/'freeze.json');verify({str(root/'sources'/p):h for p,h in freeze['source_sha256'].items()})
        for job in read(root/'jobs.json'):
            p=root/'results'/(job['id']+'.json');r=checked_row(str(p),inputs);raw=read(p)
            target=next(k for k,v in d['policies'].items() if norm(v['spec'])==norm(r['condition']['opponent_spec']))
            assert norm(r['condition']['candidate_spec'])==norm(d['policies']['J']['spec'])
            b=branches[str(p)];assert len(b['rounds'])==r['rounds']
            case=dict(result_path=str(p),opponent=target,candidate_side=r['condition']['candidate_side'],outcome=r['outcome'],payoff={'W':1,'D':0,'L':-1}[r['outcome']],hp_J_first=r['hp_candidate_first'],rounds=r['rounds'],selected_branch=b['selected_branch'],round2_opponent_walls=b['round2_opponent_walls'],round2_opponent_roster=b['round2_opponent_roster'],canonical_replay_sha256=r['canonical_replay_sha256'],decision_seconds_J_first=r['decision_seconds_candidate_first'])
            cases.append(case);groups[target].append(case)
    assert len(cases)==14 and set(groups)==set(d['policies'])
    for target,pair in groups.items():
        assert len(pair)==2 and {x['candidate_side'] for x in pair}=={0,1}
        assert all(pair[0][k]==pair[1][k] for k in ('outcome','hp_J_first','rounds','selected_branch','canonical_replay_sha256'))
    assert fresh_calls==2*sum(c['rounds'] for c in cases) and reference_calls==sum(c['rounds'] for c in cases)
    score={k:rows[0]['payoff'] for k,rows in groups.items()}
    mean=sum(Fraction(score[k],3) for k in ('G','H','I'))
    h1=all(score[k]>=0 for k in ('G','H','I')) and mean>0
    h2=all(score[k]>=0 for k in ('B','C','D','G','H','I'))
    stamp=datetime.now(timezone.utc).isoformat()
    lines=['# Public response selection after a shared first move','',f'Checked {stamp}.','',
      f'H1, nonloss against G,H,I and a positive payoff against their uniform mixture: {"CONFIRMED" if h1 else "REFUTED"}. The exact mean payoff is {mean}.',
      f'H2, nonloss against every prior policy B,C,D,G,H,I: {"CONFIRMED" if h2 else "REFUTED"}.','',
      'J processes the first observation through both H and I and requires their first action lists to agree. On round two it chooses H when the opponent has at least twenty walls and an empty roster; otherwise it chooses I. The choice then stays fixed. It reads no opponent name or private state. This rule was selected after inspecting the earlier table and is development evidence.','',
      '| Opponent | Selected response | Outcome | HP J:opponent | End round | Walls after round 1 |','|---|---|---|---|---:|---:|']
    for target in ('B','C','D','G','H','I','J'):
        x=groups[target][0];lines.append(f'| {target} | {x["selected_branch"]} | {x["outcome"]} | {x["hp_J_first"][0]}:{x["hp_J_first"][1]} | {x["rounds"]} | {x["round2_opponent_walls"]} |')
    lines += ['',f'Each row represents both physical assignments, with identical complete canonical histories. Fourteen new games pass independent original-engine replay, source/data archival checks, legal-action checks and fresh regeneration of all {fresh_calls} external decisions. An additional {reference_calls} standalone-response calls agree with every recorded J action, including round one. Six prefix component cases passed before the full games.','',
      f'The older uniform G,H,I mixture has payoff {-mean} against J under the measured pairwise outcomes. Its exact six-policy certificate remains correct on its original six columns. This seventh-policy challenge shows why that certificate cannot be extended to an unrestricted game guarantee.','',
      'The selected response consumes the actual public history from the first move; it is not reset at the branch. The conditional proof in PROOF.md explains why matching shared prefixes suffice, and the full-history checks account for wall-clock-bounded dependencies on these runs. This does not establish optimality against unknown policies or altered starting states.','',
      'Reproduction: the two shared-prefix manifests, run_data_development, audit_development_strict, replay_audit, audit_data_archives, check_fixed_game_histories, check_shared_prefix_histories, and this publisher. Bounded commands and real timestamps are in runs/validation/shared-prefix-001-pipeline.log.','']
    output=A/'RESULTS.md'
    with output.open('x') as f:f.write('\n'.join(lines))
    for p in (output,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    result=dict(time_utc=stamp,all_passed=True,new_games=14,fresh_decisions=fresh_calls,standalone_reference_calls=reference_calls,h1_nonloss_support_positive_mean=h1,h2_nonloss_all_prior=h2,uniform_GHI_payoff=str(mean),cases=cases,input_sha256=inputs)
    atomic_json(A/'verification/full_games.json',result,exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {stamp}: Shared-prefix selector complete\n\nH1 nonloss against G,H,I with positive uniform-mixture payoff: {"CONFIRMED" if h1 else "REFUTED"}; exact payoff {mean}. H2 nonloss against all six prior policies: {"CONFIRMED" if h2 else "REFUTED"}. Fourteen new games, seven identical assignment pairs, {fresh_calls} fresh external calls and {reference_calls} exact standalone-response calls. Scores J against B,C,D,G,H,I,J: {[score[k] for k in ("B","C","D","G","H","I","J")]}. Details: experiments/validation/analysis/shared_prefix_response/RESULTS.md. The criterion was selected from public first-round geometry after the six-policy table, so this is a targeted adaptive counter, not held-out evidence.\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('cases','input_sha256')}),flush=True)


if __name__=='__main__':main()

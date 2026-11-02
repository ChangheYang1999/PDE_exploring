"""Check a six-policy table with a fixed private-model transfer ablation."""
from collections import defaultdict
from datetime import datetime,timezone
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import hashlib,json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.publish_extended_counter_game import exact_certificate,norm
from bot_research.experiments.validation.artifact_io import atomic_json
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
A=E/'analysis/six_policy_game';ORDER=['B','C','D','G','H','I']


def main():
    inputs={}
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        inputs[str(p)]=digest(p);return json.loads(Path(p).read_text())
    def verify(mapping):
        for p,h in mapping.items():assert digest(p)==h,p;inputs[p]=h
    d=read(E/'six-policy-game-campaigns-001.json');verify(d['receipt_sha256'])
    assert d['new_games']==10 and d['reused_games']==32 and set(d['policies'])==set(ORDER)
    arithmetic=read(A/'verification/arithmetic_components.json')
    assert arithmetic['all_passed'] and len(arithmetic['cases'])==3;verify(arithmetic['input_sha256'])
    old=read(d['receipts']['five']);assert old['all_passed'];verify(old['input_sha256'])
    ih={kind:read(d['receipts']['ih_'+kind]) for kind in ('strict','replay','data','fresh','predictions')}
    assert ih['strict']['valid_conditions']==4 and ih['strict']['attempt_counts']=={'valid':4}
    assert not ih['strict']['unresolved'] and not ih['strict']['repeat_disagreements']
    assert ih['replay']['all_passed'] and ih['replay']['count']==4 and ih['data']['all_passed']
    for k in ('all_passed','all_replayed','all_actions_legal','all_observations_unchanged'):assert ih['fresh'][k]
    for k in ('all_fresh_actions_agree','all_predictions_exact','all_observations_unchanged','all_fresh_actions_legal','all_original_combat_agrees'):assert ih['predictions'][k]
    verify(ih['fresh']['input_sha256']);verify(ih['predictions']['input_sha256'])
    cp=norm(d['policies']['C']['spec']);ip=norm(d['policies']['I']['spec'])
    assert cp[0]==ip[0]
    ignore={'model_spec','model_parameters'}
    assert {k:v for k,v in cp[1].items() if k not in ignore}=={k:v for k,v in ip[1].items() if k not in ignore}
    records=[dict(item,reused=True) for item in d['reused']];calls=0
    for item in d['campaigns']:
        name=item['name'];m=read(E/(name+'.json'));verify(m['input_sha256'])
        audits={k:read(R/(name+'-'+k+'.json')) for k in ('strict','replay','data','fresh')}
        strict=audits['strict'];fresh=audits['fresh']
        assert strict['valid_conditions']==2 and strict['attempt_counts']=={'valid':2}
        assert not strict['unresolved'] and not strict['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['replay']['count']==2 and audits['data']['all_passed']
        assert all(fresh[k] for k in ('all_passed','all_replayed','all_actions_legal','all_observations_unchanged'))
        assert fresh['games']==2;verify(fresh['input_sha256']);calls+=fresh['checked_calls']
        records.extend(dict(a=item['a'],b=item['b'],reused=False,result=str(R/name/'results'/f'case{i:04d}.json')) for i in range(2))
    assert len(records)==42 and len({r['result'] for r in records})==42
    archives=set();cases=[];groups=defaultdict(list)
    for item in records:
        row=checked_row(item['result'],inputs);c=row['condition'];a,b=item['a'],item['b']
        assert norm(c['candidate_spec'])==norm(d['policies'][a]['spec'])
        assert norm(c['opponent_spec'])==norm(d['policies'][b]['spec'])
        directory=Path(item['result']).parent.parent
        if directory not in archives:
            freeze=read(directory/'freeze.json')
            verify({str(directory/'sources'/p):h for p,h in freeze['source_sha256'].items()});archives.add(directory)
        out=dict(item,candidate_side=c['candidate_side'],outcome=row['outcome'],hp_a_first=row['hp_candidate_first'],
            rounds=row['rounds'],canonical_replay_sha256=row['canonical_replay_sha256'],
            decision_seconds_a_first=row['decision_seconds_candidate_first'])
        cases.append(out);groups[(a,b)].append(out)
    matrix=[[None]*6 for _ in ORDER];edges=[]
    for (a,b),pair in groups.items():
        pair.sort(key=lambda r:r['candidate_side']);assert [r['candidate_side'] for r in pair]==[0,1]
        for k in ('outcome','hp_a_first','rounds','canonical_replay_sha256'):assert pair[0][k]==pair[1][k],(a,b,k)
        value={'W':1,'D':0,'L':-1}[pair[0]['outcome']];i,j=ORDER.index(a),ORDER.index(b)
        assert matrix[i][j] is None and matrix[j][i] is None
        if i==j:assert value==0
        matrix[i][j]=value;matrix[j][i]=-value
        edges.append(dict(a=a,b=b,value=value,hp_a_first=pair[0]['hp_a_first'],rounds=pair[0]['rounds'],reused=pair[0]['reused']))
    assert len(edges)==21 and all(v is not None for row in matrix for v in row)
    assert [row[:5] for row in matrix[:5]]==old['payoff']
    assert calls==sum(2*r['rounds'] for r in cases if not r['reused'])
    gaps=[matrix[5][j]-matrix[1][j] for j in range(5)]
    h1=min(gaps)>=0 and max(gaps)>0
    certificate=exact_certificate(matrix)
    if certificate:
        p=list(map(Fraction,certificate['weights']))
        assert len(p)==6 and sum(p)==1 and min(p)>=0
        assert all(sum(p[i]*matrix[i][j] for i in range(6))>=0 for j in range(6))
    pure=[ORDER[i] for i in range(6) if min(matrix[i])>=0]
    cycles=[[ORDER[i],ORDER[j],ORDER[k]] for i,j,k in permutations(range(6),3)
            if i<j and i<k and matrix[i][j]==matrix[j][k]==matrix[k][i]==1]
    stamp=datetime.now(timezone.utc).isoformat()
    lines=['# Six fixed policies and a changed private model','',f'Checked {stamp}.','',
        f'H1, I weakly improves on C against every prior policy with at least one strict improvement, is {"CONFIRMED" if h1 else "REFUTED"}. The payoff differences I minus C against B,C,D,G,H are '+', '.join(map(str,gaps))+'.','',
        'B is frozen best_v9e, C is the round-three tier2 attacker with a fixed private D model, D is the adaptive Fortress38 continuation, G is early-wall guard00, and H is the HP-triggered grower with lead_from=8 and deadline=12. I changes only C’s private model to that same H. Each attacker retains its one model on all edges.','',
        '| Row | '+' | '.join(ORDER)+' |','|---|'+'---:|'*6]
    lines += ['| '+name+' | '+' | '.join(map(str,row))+' |' for name,row in zip(ORDER,matrix)]
    lines += ['', 'Payoffs are +1 for a win, 0 for a draw and -1 for a loss. Each cell pair comes from both physical assignments of the same standard start. Thirty-two games are explicitly reused; ten are new. All twenty-one assignment pairs have identical canonical histories. These are selected development conditions, not independent samples.','',
        '| New or directly reused I edge | Outcome | HP I:opponent | End round | Source |','|---|---|---|---:|---|']
    for edge in edges:
        if edge['a']!='I':continue
        lines.append(f'| I vs {edge["b"]} | '+{1:'W',0:'D',-1:'L'}[edge['value']]+f' | {edge["hp_a_first"][0]}:{edge["hp_a_first"][1]} | {edge["rounds"]} | '+('Reused' if edge['reused'] else 'New')+' |')
    lines += ['', 'Pure policies with nonnegative payoffs in every column: '+(', '.join(pure) if pure else 'none')+'.',
        'Measured directed three-policy cycles: '+('; '.join(' > '.join(c+[c[0]]) for c in cycles) if cycles else 'none')+'.','']
    if certificate:
        lines += ['Exact rational arithmetic verifies finite-game value zero with weights '+', '.join(f'{x}={w}' for x,w in zip(ORDER,certificate['weights']))+'. Its column payoffs are '+', '.join(certificate['column_payoffs'])+'. The saved receipt contains every feasible vertex found by the proposal search and the direct inequality checks.']
    else:lines += ['The exact search produced no certificate. No value or optimal-mixture claim is made.']
    lines += ['',f'All {calls} new external action decisions were independently regenerated and matched the recorded histories. Submitted actions are legal, observations are unchanged, source/data archives match and original-engine replays agree. The reused table and the I-H source, replay, fresh-decision and prediction receipts were also rechecked. Wrong internal forecasts on other edges do not invalidate a fixed policy and are not reported as exact predictions.','',
        'Changing a private model can change all later observations and actions. This is a comparison of two complete policies, not an isolated intervention at an otherwise fixed history. A finite-table certificate proves no guarantee against a seventh policy or a different start.','',
        'Reproduction uses the five six-policy-game manifests with run_data_development, audit_development_strict, replay_audit, audit_data_archives and check_fixed_game_histories, followed by check_six_policy_arithmetic and publish_six_policy_game. Restore archived old inputs before rechecking their receipts. The bounded commands and real timestamps are retained in runs/validation/six-policy-game-001-pipeline.log.','']
    output=A/'RESULTS.md'
    with output.open('x') as f:f.write('\n'.join(lines))
    for p in (output,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    result=dict(time_utc=stamp,all_passed=True,new_games=10,reused_games=32,fresh_new_decisions=calls,
        policies=d['policies'],order=ORDER,payoff=matrix,h1_I_weakly_improves_C=h1,I_minus_C=gaps,
        pure_nonnegative_policies=pure,directed_three_cycles=cycles,certificate=certificate,cases=cases,input_sha256=inputs)
    atomic_json(A/'verification/full_games.json',result,exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Six-policy table complete\n\nClaim H1, I weakly improves on C across the previous five policies: {"CONFIRMED" if h1 else "REFUTED"}. Differences I minus C are {gaps}. Ten new games and thirty-two reused games form twenty-one identical assignment pairs; {calls} new decisions pass fresh regeneration. Pure nonnegative rows: {pure}. '+('Exact finite maximin weights in B,C,D,G,H,I order: '+str(certificate['weights'])+'. ' if certificate else 'No finite certificate found. ')+f'The private model is the only specification difference between C and I. All outcomes and limits: {output}.\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('cases','input_sha256','policies')}),flush=True)

if __name__=='__main__':main()

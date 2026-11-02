"""Recheck all six fixed policy pairs and assemble their finite empirical game."""
from datetime import datetime, timezone
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import argparse, hashlib, json, time
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import audit_row
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    start=time.perf_counter();e=Path('bot_research/experiments/validation');r=Path('bot_research/runs/validation')
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    inputs={str(p):digest(p) for p in static_closure({'bot_research.experiments.validation.assemble_nominee_counter_game'})}
    nom_path=e/'nominee-handoff-001.json';early_path=e/'early-heavy-handoff-001.json'
    inputs.update({str(p):digest(p) for p in (nom_path,early_path,e/'nominee-cross-001.json',e/'counter-cross-001.json')})
    nom=json.loads(nom_path.read_text());early=json.loads(early_path.read_text())
    policies=[*nom['candidates'],next(x for x in early['opponents'] if x['id']=='early1_handoff6'),
              next(x for x in nom['opponents'] if x['id']=='lead8')]
    specs=[p['spec'] for p in policies];assert len(set(specs))==4
    declarations=[(0,1,'nominee-cross'),(0,2,'nominee-cross'),(0,3,'nominee-handoff'),
                  (1,2,'early-heavy-handoff'),(1,3,'nominee-handoff'),(2,3,'counter-cross')]
    matrix=[[Fraction(0) for _ in specs] for _ in specs];pairs=[];source_hashes={}
    for i,j,name in declarations:
        root=r/(name+'-001');jobs=json.loads((root/'jobs.json').read_text())
        freeze=json.loads((root/'freeze.json').read_text())
        for p,h in freeze['source_sha256'].items():
            assert digest(p)==h,p
            if p in source_hashes:assert source_hashes[p]==h,p
            source_hashes[p]=h
        selected=[job for job in jobs if job['condition']['candidate_spec']==specs[i]
                  and job['condition']['opponent_spec']==specs[j]]
        assert len(selected)==2 and {x['condition']['candidate_side'] for x in selected}=={0,1}
        outcomes=[];games=[]
        for job in sorted(selected,key=lambda x:x['condition']['candidate_side']):
            condition=job['condition'];assert condition['initial_state']=='standard' and condition['engine_seed'] is None
            path=root/'results'/(job['id']+'.json');checked=checked_row(str(path),inputs)
            row=json.loads(path.read_text());audit=audit_row(row)
            side=condition['candidate_side'];winner=audit['result']['winner']
            outcome=0 if winner is None else (1 if winner==side else -1)
            assert outcome=={'W':1,'D':0,'L':-1}[checked['outcome']]
            outcomes.append(outcome);games.append(dict(checked,original_replay=audit))
        assert games[0]['canonical_replay_sha256']==games[1]['canonical_replay_sha256']
        value=Fraction(sum(outcomes),2);matrix[i][j]=value;matrix[j][i]=-value
        pairs.append(dict(row_policy=policies[i]['id'],column_policy=policies[j]['id'],games=games,
                          both_assignment_payoffs=outcomes,source_campaign=str(root)))
    rat=lambda q:dict(numerator=q.numerator,denominator=q.denominator)
    cycles=[]
    for size in (3,4):
        for seq in permutations(range(4),size):
            if seq[0]!=min(seq):continue
            if all(matrix[seq[k]][seq[(k+1)%size]]==1 for k in range(size)):
                cycles.append([policies[k]['id'] for k in seq])
    inputs.update(source_hashes)
    assert all(digest(p)==h for p,h in inputs.items())
    output=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        policies=[p['id'] for p in policies],policy_specs=specs,matrix=[[rat(q) for q in row] for row in matrix],
        pairs=pairs,directed_cycles=cycles,all_replays_passed=True,all_assignment_histories_identical=True,
        input_sha256=inputs,scope='Six fixed standard-start pairs, twelve original-engine replays. Six games were already recorded; six fill missing pairs. Reuse adds no independent samples. Diagonal zero is the symmetric payoff convention, not a measured self-play result.')
    atomic_json(args.output,output,exclusive=True)
    print(json.dumps(dict(time_utc=output['time_utc'],policies=output['policies'],matrix=[[float(q) for q in row] for row in matrix],cycles=cycles)))

if __name__=='__main__':main()

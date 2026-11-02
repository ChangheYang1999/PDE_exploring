"""Bind a current-best counter cycle to six already audited trajectories.

No new games or self-play entries are inferred. This is an evidence index.
"""
from datetime import datetime,timezone
import argparse
import hashlib
import json
from pathlib import Path
import time
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

ROOT=Path('bot_research/runs/validation')
SELECTIONS=[
    ('best-v9b-counter-model-free','corner_t1','actual_best_v9b','W','guard','best_v9b'),
    ('best-v9b-counter-model-free','direct_economy17','actual_best_v9b','L','economy17','best_v9b'),
    ('guard-geometry-transfer','corner_t1','economy17','L','guard','economy17'),
]

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
    started=time.perf_counter();inputs={};specs={};edges=[]
    for stem,candidate,opponent,expected,cname,oname in SELECTIONS:
        strictpath=ROOT/(stem+'-strict-001.json')
        replaypath=ROOT/(stem+'-replay-001.json')
        for path in (strictpath,replaypath):inputs[str(path)]=digest(path)
        strict=json.loads(strictpath.read_text());replay=json.loads(replaypath.read_text())
        assert not strict['unresolved'] and replay['all_passed']
        pair=[c for c in strict['cases'] if c['condition']['candidate_id']==candidate and c['condition']['opponent_id']==opponent]
        assert len(pair)==2 and {c['condition']['candidate_side'] for c in pair}=={0,1}
        checked=[]
        for c in pair:
            filename=c['result_path']
            assert strict['input_sha256'][filename]==digest(filename)
            row=json.loads(Path(filename).read_text())
            check=checked_row(filename,inputs)
            assert check['outcome']==c['outcome']==expected
            assert check['hp_candidate_first']==c['hp_candidate_first']
            assert check['canonical_replay_sha256']==c['canonical_replay_sha256']
            receipts=[r for r in replay['cases'] if r['condition']==row['condition']]
            assert len(receipts)==1 and receipts[0]['passed']
            assert receipts[0]['trajectory_sha256']==row['trajectory_sha256']
            receipt=receipts[0];stream=receipt['input']
            assert replay['input_sha256'][stream]==digest(stream)
            inputs[stream]=digest(stream)
            assert row['condition']['initial_state']=='standard'
            assert row['condition']['engine_seed'] is None
            for key,name in [('candidate_spec',cname),('opponent_spec',oname)]:
                spec=row['condition'][key]
                assert specs.setdefault(name,spec)==spec
            checked.append(check)
        assert checked[0]['canonical_replay_sha256']==checked[1]['canonical_replay_sha256']
        winner,loser=(cname,oname) if expected=='W' else (oname,cname)
        hp=checked[0]['hp_candidate_first']
        if expected=='L':hp=list(reversed(hp))
        edges.append(dict(winner=winner,loser=loser,hp_winner_first=hp,rounds=checked[0]['rounds'],both_assignment_histories_equal=True,cases=checked))
    assert {(e['winner'],e['loser']) for e in edges}=={('guard','best_v9b'),('best_v9b','economy17'),('economy17','guard')}
    frozen='bot_research/experiments/lead/frozen/best_v9b.py'
    actual='bot_research/bots/best.py'
    assert digest(frozen)==digest(actual)=='dc96ac422078fd2cadafcc72fce10bb1d22bbb50b9c19a4bbe7937a2fba85ee7'
    for path in (frozen,actual):inputs[path]=digest(path)
    assert all(digest(p)==h for p,h in inputs.items())
    output=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-started,
        all_passed=True,policy_specs=specs,edges=edges,new_games=0,selected_existing_games=6,
        independent_paired_conditions=3,self_play_measured=False,input_sha256=inputs,
        checker_sha256=digest(__file__),scope='Retrospectively selected development cycle on a standard start. Six already audited games establish three directed counter edges. No new samples, self-play values, policy mixture, or broader equilibrium are claimed.')
    atomic_json(a.output,output,exclusive=True)
    print(json.dumps({k:output[k] for k in ('all_passed','runtime_seconds','selected_existing_games','independent_paired_conditions')}))

if __name__=='__main__':main()

"""Check prescribed actions, repeated guards and an independent lane's replay."""
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.summarize_identifying import canonical_replay


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.perf_counter();inputs={}
    def read(path):
        path=Path(path);raw=path.read_bytes();inputs[str(path)]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
    data=read('bot_research/bots/counters/data/heavy_drip_001.json');schedule={r['round']:r['actions'] for r in data['schedule']}
    folder=Path('bot_research/runs/validation/guard-heavy-transfer-001');jobs=read(folder/'jobs.json');heavy=[];repeats=[];target={}
    old=Path('bot_research/runs/validation/staged-guards-grid-001');old_jobs=read(old/'jobs.json')
    for job in jobs:
        c=job['condition'];path=folder/'results'/(job['id']+'.json');row=read(path);checked=checked_row(str(path),inputs);target[(c['candidate_id'],c['opponent_id'],c['candidate_side'])]=checked
        if c['opponent_id']=='fixed_heavy_drip':
            records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()];counter=1-c['candidate_side'];rounds=[]
            for record in records:
                if record['player']!=counter or not record['round']:continue
                actions=[e['action'] for e in record['event'] if e['kind']=='action']
                assert actions==schedule.get(record['round'],[]),(job['id'],record['round'])
                rounds.append(record['round'])
            heavy.append(dict(result=str(path),candidate=c['candidate_id'],side=c['candidate_side'],verified_rounds=rounds,all_prescribed_actions_submitted=True))
        elif c['candidate_id'] in ('economy21','fortress33'):
            match=[j for j in old_jobs if j['condition']['candidate_id']==c['candidate_id'] and j['condition']['candidate_side']==c['candidate_side'] and j['condition']['opponent_spec']==c['opponent_spec']]
            assert len(match)==1
            control=checked_row(str(old/'results'/(match[0]['id']+'.json')),inputs)
            assert control['canonical_replay_sha256']==checked['canonical_replay_sha256']
            repeats.append(dict(current=checked,control=control,same_complete_trajectory=True))
    assert len(heavy)==14 and len(repeats)==4
    external=Path('bot_research/runs/defense/x117_astra33/results.jsonl');raw=external.read_bytes();inputs[str(external)]=hashlib.sha256(raw).hexdigest();w1=[]
    spec='bot_research.bots.defense.frozen.v33.fortress:@make';opponent='bot_research.bots.defense.counter_astra33:@make'
    for line in raw.splitlines():
        row=json.loads(line);specs=[row['spec_a'],row['spec_b']]
        if set(specs)!={spec,opponent}:continue
        side=specs.index(spec);path=Path(row['log']);inputs[str(path)]=hashlib.sha256(path.read_bytes()).hexdigest()
        for name,h in row['sources'].items():
            assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==h,name
            inputs[name]=h
        expected=target[('fortress33','fixed_heavy_drip',side)]
        assert canonical_replay(path,side)==expected['canonical_replay_sha256']
        w1.append(dict(external_replay=str(path),side=side,our_result=expected['result_path'],same_complete_trajectory=True,external_hp=[row['hp_a'],row['hp_b']],rounds=row['rounds']))
    assert len(w1)==2
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),all_passed=True,input_sha256=inputs,heavy_prescription_checks=heavy,staged_repetitions=repeats,external_fortress33_repetitions=w1,scope='The budget filter changes no submitted action in any of these fourteen heavy-drip games. Four guard games and two external lane games reproduce entire trajectories; these are reproducibility evidence, not independent samples.')
    atomic_json(a.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()

"""Publish every fixed bait/guard transfer condition after independent checks."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E=Path('bot_research/experiments/validation')
R=Path('bot_research/runs/validation')
AREA=E/'analysis/bait_guard_transfer'


def main():
    inputs={}
    def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        inputs[str(p)]=digest(p)
        return json.loads(Path(p).read_text())
    declaration=read(E/'bait-guard-transfer-campaigns-001.json')
    rows=[];calls=0;pairs=[]
    for item in declaration['campaigns']:
        name=item['name'];m=read(E/(name+'.json'))
        for p,h in m['input_sha256'].items():
            assert digest(p)==h,p
            inputs[p]=h
        a={k:read(R/(name+'-'+k+'.json')) for k in ('strict','replay','data','fresh','summary')}
        assert a['strict']['valid_conditions']==4 and a['strict']['attempt_counts']=={'valid':4}
        assert not a['strict']['unresolved'] and not a['strict']['repeat_disagreements']
        assert a['replay']['all_passed'] and a['replay']['count']==4
        assert a['data']['all_passed'] and a['fresh']['all_passed']
        assert a['fresh']['games']==4
        calls+=a['fresh']['checked_calls']
        for p,h in a['fresh']['input_sha256'].items():
            assert digest(p)==h,p
            inputs[p]=h
        local=defaultdict(list)
        for job in read(R/name/'jobs.json'):
            path=R/name/'results'/(job['id']+'.json')
            row=checked_row(str(path),inputs);raw=read(path);c=row['condition']
            assert c['candidate_id']==item['defender']
            rp=Path(raw['replay_path']);inputs[str(rp)]=digest(rp)
            records=[json.loads(s) for s in rp.read_text().splitlines()]
            damage=[]
            for rec in records:
                if rec['player']==c['candidate_side'] and rec['round']>0:
                    amount=sum(e['base_damage'] for e in rec['event'] if e['kind']=='combat')
                    if amount:damage.append(dict(round=rec['round'],base_damage=amount))
            x=dict(defender=c['candidate_id'],defender_spec=c['candidate_spec'],opponent=c['opponent_id'],opponent_spec=c['opponent_spec'],side=c['candidate_side'],outcome=row['outcome'],hp=row['hp_candidate_first'],rounds=row['rounds'],result=str(path),canonical_replay_sha256=row['canonical_replay_sha256'],decision_seconds=row['decision_seconds_candidate_first'],defender_damage=damage)
            rows.append(x);local[x['opponent']].append(x)
        for opponent,rr in local.items():
            assert len(rr)==2 and {x['side'] for x in rr}=={0,1}
            pairs.append(dict(defender=item['defender'],opponent=opponent,same_history=rr[0]['canonical_replay_sha256']==rr[1]['canonical_replay_sha256'],outcomes=[x['outcome'] for x in sorted(rr,key=lambda x:x['side'])]))
    assert len(rows)==24 and len(pairs)==12
    control=all(r['outcome']=='L' and r['hp'][0]-r['hp'][1]==(-275 if r['opponent']=='bait_guard_A' else -260) for r in rows if r['defender']=='fortress41')
    assert len([r for r in rows if r['defender']=='fortress41'])==4
    targets={'best_v9e','V33C','delegated_adaptive'}
    successful=[p for p in pairs if p['defender'] in targets and p['outcomes']==['L','L']]
    assert {r['defender'] for r in rows} >= targets
    stamp=datetime.now(timezone.utc).isoformat()
    lines=['# Bait and guard schedules transfer across defenders','',f'Checked {stamp}.','',
        f'Fortress41 margin reproduction: {"CONFIRMED" if control else "REFUTED"}. Transfer to at least one of best_v9e, V33C and the adaptive delegated counter: {"CONFIRMED" if successful else "REFUTED"}. All 24 declared conditions are included.','',
        'Cells give defender outcome, defender:attacker HP and ending round. Equal physical assignments share a cell; differences are explicit.','',
        '| Defender | Schedule A | Schedule B |','|---|---|---|']
    for item in declaration['campaigns']:
        cells=[]
        for opponent in ('bait_guard_A','bait_guard_B'):
            rr=sorted((r for r in rows if r['defender']==item['defender'] and r['opponent']==opponent),key=lambda r:r['side'])
            values=[f'{r["outcome"]} {r["hp"][0]}:{r["hp"][1]} r{r["rounds"]}' for r in rr]
            cells.append(values[0] if values[0]==values[1] else 'seat0 '+values[0]+'; seat1 '+values[1])
        lines.append('| '+item['defender']+' | '+' | '.join(cells)+' |')
    lines+=['',f'All {calls} freshly regenerated decisions across both policies agree with the recorded action lists. Original-engine replay, complete source/data archives, observation immutability and action legality checks pass. {sum(p["same_history"] for p in pairs)} of 12 assignment pairs have identical complete canonical histories. These pairs are reproducibility checks, not independent random samples.','',
        'The schedules were proposed in the defense lane and are used here unchanged. Both send three tier1 copies in round two, add guard turrets, buy three tier5 copies in round eight and then construct a splash defense. This test measures transfer of that concrete schedule. It does not show that bait causes each individual defender failure; the full receipt records damage rounds for further diagnosis.','',
        'Fortress41 was a known design target. The other five defender specifications were declared here before testing, but all are development targets and none belongs to the reserved validation pool. Teammate planners may use wall-clock limits, so exact repeat agreement is an observed property of these executions.','',
        'Reproduce the six bait-guard-transfer manifests with run_data_development, followed by audit_development_strict, replay_audit, audit_data_archives and check_fixed_game_histories. The complete bounded commands are in runs/validation/bait-guard-transfer-001-pipeline.log. Use the existing Python, disabled bytecode, research temporary directory, assigned affinity, low priority and one numerical thread.','']
    out=AREA/'RESULTS.md'
    with out.open('x') as f:f.write('\n'.join(lines))
    for p in (out,AREA/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    data=dict(time_utc=stamp,all_passed=True,control_reproduction=control,transfer_confirmed=bool(successful),successful_transfer_pairs=successful,games=24,fresh_decisions=calls,pairs=pairs,rows=rows,input_sha256=inputs)
    with (AREA/'verification/full_games.json').open('x') as f:json.dump(data,f,indent=2,sort_keys=True);f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Bait/guard transfer complete\n\nClaim and verdict: fortress margin reproduction {"CONFIRMED" if control else "REFUTED"}; transfer to at least one declared primary target {"CONFIRMED" if successful else "REFUTED"}. All24games and {calls} fresh decisions pass independent replay, source, legality and action checks. Both-seat losses occur in '+', '.join(p['defender']+'/'+p['opponent'] for p in successful)+f'. Exact complete table: {out}. These are development results.\n')
    print(json.dumps({k:v for k,v in data.items() if k not in ('rows','pairs','input_sha256')}))


if __name__=='__main__':main()

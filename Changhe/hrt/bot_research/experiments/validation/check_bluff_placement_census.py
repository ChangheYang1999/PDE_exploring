"""Validate an exhaustive placement family and classify its defensive effects."""
from collections import Counter,defaultdict
from copy import deepcopy
from datetime import datetime,timezone
import argparse,hashlib,json,time
from pathlib import Path
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState,RosterEntry
from bot_research.harness import gamekit as gk
from bot_research.bots.counters.snapshots.v23_candidate_001.v15 import _covering_turret
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    for name in ('manifest','strict','replay','output'):parser.add_argument('--'+name,required=True)
    args=parser.parse_args();start=time.perf_counter()
    manifest=json.loads(Path(args.manifest).read_text())
    strict=json.loads(Path(args.strict).read_text())
    replay=json.loads(Path(args.replay).read_text())
    inputs={p:digest(p) for p in (args.manifest,args.strict,args.replay)}
    inputs.update(manifest['input_sha256'])
    sources={str(p):digest(p) for p in static_closure({'bot_research.experiments.validation.check_bluff_placement_census'})}
    sources['td_game/balanced.json']=digest('td_game/balanced.json')
    assert all(digest(p)==h for p,h in inputs.items())
    assert not strict['unresolved'] and not strict['repeat_disagreements']
    assert replay['all_passed'] and not replay['source_changed_during_run']
    replayed={r['trajectory_sha256'] for r in replay['cases'] if r['passed']}
    cfg=balanced_config();rules=gk.Rules.from_observation(Engine(cfg,('a','b')).observation(0))
    legal={}
    for x in range(cfg.globals.width):
        for y in range(cfg.globals.height):
            state=PlayerState('defender',800,100)
            if apply_action(state,dict(op='build_turret',type='gun1',x=x,y=y),1,cfg)['accepted']:
                legal[x,y]=state
    assert set(legal)=={tuple(p) for p in manifest['legal_positions']}
    assert len(manifest['legal_positions'])==len(legal)
    assert strict['valid_conditions']==len(legal)*2==replay['count']
    declared={x['id']:x['spec'] for x in manifest['opponents']}
    assert len(declared)==len(legal)==len(manifest['opponents'])
    cases={}
    for c in strict['cases']:
        cond=c['condition'];key=(cond['opponent_id'],cond['candidate_side'])
        assert key not in cases
        assert cond['candidate_spec']==manifest['candidates'][0]['spec']
        assert cond['opponent_spec']==declared[cond['opponent_id']]
        assert cond['initial_state']=='standard' and cond['engine_seed'] is None
        p=c['result_path'];inputs[p]=digest(p)
        assert inputs[p]==strict['input_sha256'][p]
        row=json.loads(Path(p).read_text())
        assert row['trajectory_sha256'] in replayed
        inputs[row['replay_path']]=digest(row['replay_path'])
        assert inputs[row['replay_path']]==row['trajectory_sha256']
        cases[key]=c
    assert set(cases)=={(f'gun1_{x}_{y}',s) for x,y in legal for s in (0,1)}
    blank=shortest_path(12,12,set(),cfg.globals.spawn,cfg.globals.base)
    rows=[];groups=defaultdict(Counter)
    for (x,y),state in legal.items():
        path=shortest_path(12,12,{(x,y)},cfg.globals.spawn,cfg.globals.base)
        assert path is not None
        coverage=bool(_covering_turret([dict(x=x,y=y,type='gun1')],rules))
        cells=[p for p in path[:-1] if (p[0]-x)**2+(p[1]-y)**2<=cfg.turrets['gun1'].range**2]
        assert coverage==bool(cells)
        diagnostics=[]
        for kinds in manifest['diagnostic_rosters']:
            attacker=PlayerState('attacker',800,0,roster=[RosterEntry(i,k,1,None) for i,k in enumerate(kinds)])
            outcome=simulate_map(attacker,deepcopy(state),path,1,cfg)
            diagnostics.append(dict(roster=kinds if len(kinds)<=5 else [kinds[0],len(kinds)],damage=outcome.damage,killed=outcome.killed,hits=outcome.hits,cleared=outcome.cleared))
        label='no_coverage' if not coverage else ('covers_kills_solo_t1' if diagnostics[0]['killed'] else 'covers_cannot_kill_solo_t1')
        matches=[]
        for side in (0,1):
            c=cases[f'gun1_{x}_{y}',side]
            groups[label][c['outcome']]+=1
            matches.append(dict(side=side,outcome=c['outcome'],hp=c['hp_candidate_first'],rounds=c['rounds'],result_path=c['result_path'],canonical_replay_sha256=c['canonical_replay_sha256']))
        rows.append(dict(position=[x,y],coverage=coverage,attackable_cells=cells,empty_route_unchanged=path==blank,classification=label,diagnostics=diagnostics,matches=matches,same_seat_trajectory=matches[0]['canonical_replay_sha256']==matches[1]['canonical_replay_sha256']))
    assert all(digest(p)==h for p,h in {**inputs,**sources}.items())
    output=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,
        legal_positions=len(legal),checked_games=len(cases),groups={k:dict(v) for k,v in groups.items()},
        identical_assignment_pairs=sum(r['same_seat_trajectory'] for r in rows),rows=rows,input_sha256=inputs,source_sha256=sources,
        scope='Exhaustive only over the declared one-gun placement family. Diagnostic-map groups are descriptive; full-game outcomes are not a causal isolation of coverage or solo kills.')
    atomic_json(args.output,output,exclusive=True)
    print(json.dumps({k:output[k] for k in ('time_utc','runtime_seconds','all_passed','legal_positions','checked_games','groups','identical_assignment_pairs')}),flush=True)


if __name__=='__main__':main()

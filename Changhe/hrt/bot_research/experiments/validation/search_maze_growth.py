"""Finite seeded wall-map search, scored by exact no-hit factory cash."""
from datetime import datetime, timezone
import argparse, hashlib, json, random, time
from pathlib import Path
from td_game.pathfinding import shortest_path
from bot_research.experiments.validation.artifact_io import atomic_json


def growth(cost, length, horizon=9):
    gold=100-cost; factories=0; rows=[]
    for rnd in range(1,horizon+1):
        bought=gold//20; gold-=20*bought; factories+=bought
        gold+=length+15*factories
        rows.append(dict(round=rnd,factories=factories,gold=gold))
    return rows


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--report',required=True)
    p.add_argument('--seed-replay',required=True);p.add_argument('--seed',type=int,default=310126)
    p.add_argument('--steps',type=int,default=1800);args=p.parse_args();start=time.perf_counter()
    rng=random.Random(args.seed);cells=[(x,y) for x in range(12) for y in range(12) if (x,y) not in ((0,0),(11,11))]
    records=[json.loads(l) for l in Path(args.seed_replay).read_text().splitlines()]
    seed_record=next(r for r in records if r['round']==1 and r['player']==0)
    seed_walls=frozenset((b['x'],b['y']) for b in seed_record['snapshot']['buildings'])
    seeds=[frozenset(),seed_walls]
    for count in (1,2,3,4,5):
        for transpose in (False,True):
            fence={(x,y) for i,x in enumerate(range(1,1+2*count,2)) for y in range(12) if y!=(11 if i%2==0 else 0)}
            if transpose:fence={(y,x) for x,y in fence}
            seeds.append(frozenset(fence))
    cache={};best_by_shape={};checks=0
    def assess(walls):
        nonlocal checks
        if walls in cache:return cache[walls]
        checks+=1
        if len(walls)>100:cache[walls]=None;return None
        path=shortest_path(12,12,walls,(0,0),(11,11))
        if path is None:cache[walls]=None;return None
        length=len(path)-1;rows=growth(len(walls),length)
        score=(rows[5]['gold'],rows[8]['gold'],length,-len(walls))
        cache[walls]=(score,rows,length)
        key=(len(walls),length)
        if key not in best_by_shape or tuple(sorted(walls))<tuple(sorted(best_by_shape[key])):best_by_shape[key]=walls
        return cache[walls]
    traces=[]
    for n,seed in enumerate(seeds):
        current=seed;value=assess(current);best=(value[0],current)
        for step in range(args.steps):
            change=rng.randrange(3)
            trial=set(current)
            if change==0 or not trial:trial.add(rng.choice(cells))
            elif change==1:trial.remove(rng.choice(sorted(trial)))
            else:
                trial.remove(rng.choice(sorted(trial)));trial.add(rng.choice(cells))
            trial=frozenset(trial);result=assess(trial)
            if result is None:continue
            if result[0]>=value[0] or (step%300<40 and rng.random()<0.02):current=trial;value=result
            if value[0]>best[0]:best=(value[0],current)
            if step%300==299:current=best[1];value=assess(current)
        traces.append(dict(seed_index=n,initial_cost=len(seed),initial_length=assess(seed)[2],best_score=list(best[0])))
    ranked=sorted(best_by_shape.values(),key=lambda w:assess(w)[0],reverse=True)
    chosen=[frozenset(),seed_walls]
    for walls in ranked:
        if walls not in chosen:chosen.append(walls)
        if len(chosen)>=12:break
    data=dict(schema=1,selection='Finite development search. No global optimality claim.',layouts=[])
    for i,walls in enumerate(chosen):
        _,rows,length=assess(walls)
        name='empty' if i==0 else 'lead_opening' if i==1 else f'cash_rank_{i-1}'
        data['layouts'].append(dict(id=name,walls=[list(c) for c in sorted(walls)],cost=len(walls),length=length,no_hit_growth=rows))
    atomic_json(args.output,data,exclusive=True)
    report=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,random_seed=args.seed,
        steps_per_seed=args.steps,starts=len(seeds),unique_maps_evaluated=checks,legal_cost_length_pairs=len(best_by_shape),traces=traces,
        selected=[dict(id=x['id'],cost=x['cost'],length=x['length'],round6_gold=x['no_hit_growth'][5]['gold']) for x in data['layouts']],
        input_sha256={args.seed_replay:hashlib.sha256(Path(args.seed_replay).read_bytes()).hexdigest(),str(Path(__file__).relative_to(Path.cwd())):hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
        output_sha256=hashlib.sha256(Path(args.output).read_bytes()).hexdigest(),scope='Deterministic finite heuristic search for factory cash without hits. No strength or optimality claim.')
    atomic_json(args.report,report,exclusive=True);print(json.dumps({k:report[k] for k in ('runtime_seconds','unique_maps_evaluated','selected')}))

if __name__=='__main__':main()

"""Check the declared bait's affordability, visibility and unchanged prefixes."""
from copy import deepcopy
from datetime import datetime,timezone
import argparse,hashlib,json,time
from pathlib import Path
from urllib.parse import parse_qsl
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.harness.match import resolve_spec
from bot_research.bots.counters.feature_bluff import FeatureBluff
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    for key in ('manifest','output'):parser.add_argument('--'+key,required=True)
    args=parser.parse_args();start=time.perf_counter()
    manifest=json.loads(Path(args.manifest).read_text())
    inputs={args.manifest:digest(args.manifest),**manifest['input_sha256']}
    sources={str(p):digest(p) for p in static_closure({'bot_research.experiments.validation.check_roster_bait_grid'})}
    assert all(digest(p)==h for p,h in inputs.items())
    cases=[]
    for candidate in manifest['candidates']:
      for opponent in manifest['opponents']:
       params={k:json.loads(v) for k,v in parse_qsl(opponent['spec'].partition('?')[2])}
       for side in (0,1):
        policy=resolve_spec(candidate['spec']);bait=resolve_spec(opponent['spec'])
        plain=FeatureBluff(**{k:v for k,v in params.items() if k not in ('bait','bait_round')})
        engine=Engine(balanced_config(),('a','b'))
        entry=dict(candidate=candidate['id'],opponent=opponent['id'],side=side)
        for rnd in range(1,5):
          obs=engine.observation(1-side);saved=deepcopy(obs)
          actual=bait(obs)
          assert obs==saved
          if rnd!=2 or not params['bait']:assert actual==plain.decide(deepcopy(obs))
          if rnd==2:
            bought=[a['type'] for a in actual if a['op']=='buy_minion']
            assert bought==params['bait'], 'A declared bait was not affordable.'
            entry['bait_purchased']=bought
          if rnd==3:
            enemy=engine.observation(side)['players'][1-side]
            matching=[e for e in enemy['roster'] if e['bought_round']>=2 and saved['rules']['minions'][e['type']]['hp']<=70]
            assert bool(matching)==bool(params['bait'])
            entry['roster_predicate']=bool(matching)
          pair=[None,None];pair[side]=policy(engine.observation(side));pair[1-side]=actual
          records=engine.play_round(pair)
          assert all(e['accepted'] for r in records for e in r['event'] if e['kind']=='action')
        cases.append(entry)
    assert len(cases)==2*len(manifest["candidates"])*len(manifest["opponents"]) and all(digest(p)==h for p,h in {**inputs,**sources}.items())
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,cases=cases,input_sha256=inputs,source_sha256=sources,scope='Every declared actual-engine four-round prefix; exact unchanged grower output outside round two, affordable declared bait, visibility at round three, input immutability and all action legality. No full-game result follows.')
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','runtime_seconds','all_passed')}),flush=True)


if __name__=='__main__':main()

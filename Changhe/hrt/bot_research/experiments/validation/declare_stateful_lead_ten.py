"""Declare fresh versus persistent forecasts before executing these games."""
from datetime import datetime, timezone
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    model='bot_research.bots.counters.snapshots.lead_ten_001:@make'
    params=dict(big_threat=100,gun_cap=120,poke_until=3,poke_reactive='turret',
                big_partial=True,r1_poke=3,attack_mode='adaptive')
    target=model+'?'+'&'.join(k+'='+json.dumps(v,separators=(',',':')) for k,v in params.items())
    candidates=[]
    for style in ('fresh','persistent'):
        entry=('bot_research.bots.counters.public_factory:@timing' if style=='fresh'
               else 'bot_research.bots.counters.stateful_public:@timing')
        for tier,rnd in [('tier3',3),('tier3',5),('tier4',5),('tier4',7),('tier4',9),
                         ('tier5',7),('tier5',8),('tier5',9),('tier5',10),('tier5',11)]:
            settings=dict(model_spec=model,model_parameters=params,attack_round=rnd,tier=tier,
                          attack_share=1.0,count_cap=1000)
            spec=entry+'?'+'&'.join(k+'='+json.dumps(v,separators=(',',':')) for k,v in settings.items())
            candidates.append({'id':f'{style}_{tier}_r{rnd}','spec':spec})
    manifest={'declared_utc':datetime.now(timezone.utc).isoformat(),
              'purpose':'Development audit of fresh versus persistent public forecasts against adaptive Lead10; exactness checked against every actual action list.',
              'candidates':candidates,'opponents':[{'id':'lead10_C2_adaptive','spec':target}],
              'scope':'Forty standard games, two assignments per timing and model type. Reserved pools A and B are not used. A fresh clone is not presumed exact.'}
    atomic_json(Path('bot_research/experiments/validation/stateful-lead-ten-001.json'),manifest,exclusive=True)
    print(json.dumps({'declared_utc':manifest['declared_utc'],'games':40,'target':target}))

if __name__=='__main__':
    main()

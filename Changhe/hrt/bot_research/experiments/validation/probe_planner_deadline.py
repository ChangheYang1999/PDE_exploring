"""Controlled scheduler-pause probe of the frozen v9 wall-clock deadline.

Only this script's child process is paused. The engine and planner are imported
unchanged. This is a reproducibility diagnostic, not a strength tournament.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


def child():
    from td_game.config import balanced_config
    from td_game.engine import Engine
    from bot_research.bots.defense.frozen.v9 import plan
    config=balanced_config()
    engine=Engine(config,('deadline_probe','one_tier3'))
    obs=engine.observation(0)
    print(json.dumps({'phase':'calling_planner','observation':obs}),flush=True)
    started=time.perf_counter()
    actions=plan.plan_defense(obs,100,threat_types=[['tier3']])
    elapsed=time.perf_counter()-started
    records=engine.play_round([actions,[{'op':'buy_minion','type':'tier3'}]])
    rejected=[e for r in records for e in r['event'] if e['kind']=='action' and not e['accepted']]
    assert not rejected
    combat=next(e for e in records[0]['event'] if e['kind']=='combat')
    print(json.dumps({'actions':actions,'planner_wall_seconds':elapsed,
                      'incoming_damage':combat['base_damage'],'records':records,
                      'planner_time_budget':plan.TIME_BUDGET}),flush=True)


def one_run(pause_delay=None,pause_seconds=0):
    command=[sys.executable,'-B','-m','bot_research.experiments.validation.probe_planner_deadline','--child']
    process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,bufsize=1)
    first=json.loads(process.stdout.readline())
    paused=False
    if pause_delay is not None:
        time.sleep(pause_delay)
        if process.poll() is None:
            os.kill(process.pid,signal.SIGSTOP)
            try:
                time.sleep(pause_seconds)
            finally:
                os.kill(process.pid,signal.SIGCONT)
            paused=True
    rest,error=process.communicate(timeout=30)
    if process.returncode:
        raise RuntimeError('Deadline-probe child failed.')
    lines=rest.splitlines()
    if len(lines)!=1:
        raise ValueError('Unexpected child output.')
    result=json.loads(lines[0])
    result.update({'observation':first['observation'],'pause_applied':paused,
                   'requested_pause_delay_seconds':pause_delay,'requested_pause_seconds':pause_seconds})
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--child',action='store_true')
    p.add_argument('--output')
    a=p.parse_args()
    if a.child:
        child()
        return
    if not a.output:
        p.error('--output required')
    from bot_research.experiments.validation.source_closure import static_closure
    from bot_research.experiments.validation.artifact_io import atomic_json
    sources=static_closure(['bot_research.bots.defense.frozen.v9.plan',
                           'bot_research.experiments.validation.probe_planner_deadline'])
    before={str(path):hashlib.sha256(path.read_bytes()).hexdigest() for path in sources}
    normal=one_run()
    paused=one_run(0.03,3.3)
    assert normal['observation']==paused['observation']
    changed=[path for path,digest in before.items() if hashlib.sha256(Path(path).read_bytes()).hexdigest()!=digest]
    assert not changed
    result={'time_utc':datetime.now(timezone.utc).isoformat(),'normal':normal,'paused':paused,
            'actions_differ':normal['actions']!=paused['actions'],
            'incoming_damage_differs':normal['incoming_damage']!=paused['incoming_damage'],
            'identical_input':True,'source_sha256':before,'source_changed':changed,
            'interpretation':'Controlled scheduler pause of our own child; unchanged planner and engine. Not a match win-rate claim.'}
    atomic_json(a.output,result,exclusive=True)
    print(json.dumps({key:result[key] for key in ('time_utc','actions_differ','incoming_damage_differs','identical_input')}))
    print(json.dumps({'normal_damage':normal['incoming_damage'],'paused_damage':paused['incoming_damage'],
                      'normal_seconds':normal['planner_wall_seconds'],'paused_seconds':paused['planner_wall_seconds']}))


if __name__=='__main__':
    main()

"""Freeze the twelve-game continuation matrix and four audited controls."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.source_closure import static_closure
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation')
def main():
    stamp=datetime.now(timezone.utc).isoformat();inputs={};controls={}
    for target,campaign in [('best_v9e','screened-roster-guarded-fortress38-001'),('AS1C','screened-guard-transfer-00-001')]:
        controls[target]={}
        for p in sorted((R/campaign/'results').glob('case*.json')):
            row=json.loads(p.read_text());c=row['condition']
            if campaign.endswith('00-001') and (c['candidate_id']!='guard' or c['opponent_id']!='AS1C'):continue
            checked_row(str(p),inputs);controls[target][str(c['candidate_side'])]=str(p)
        assert set(controls[target])=={'0','1'}
    modules={'bot_research.bots.counters.screened_continuation_repair','bot_research.experiments.lead.frozen.best_v9e'}
    modules|={'bot_research.experiments.validation.'+m for m in ('declare_screened_continuation_repair','publish_screened_continuation_repair','run_data_development','audit_development_strict','replay_audit','audit_data_archives','check_declared_policy_histories','summarize_plain_campaign')}
    paths=set(static_closure(modules))|{E/'analysis/screened_continuation_repair/PROOF.md',Path('td_game/balanced.json'),Path('configs/balanced.json'),Path('bot_research/bots/counters/data/maze_layouts_001.json'),Path('bot_research/bots/counters/data/screened_roster_guard_001.json')}
    for p in paths:inputs[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
    opponents=[dict(id='AS1C',spec='bot_research.experiments.lead.frozen.best_v9e:@make?attack_share=1.0&catch_up_share=0.5'),dict(id='best_v9e',spec='bot_research.experiments.lead.frozen.best_v9e:@make')]
    campaigns=[]
    for i,continuation in enumerate(('fortress41','v29_g1','fortress38_full')):
        name=f'screened-continuation-repair-{i:02d}-001'
        candidate=dict(id=continuation,spec='bot_research.bots.counters.screened_continuation_repair:@make?continuation='+json.dumps(continuation))
        atomic_json(E/(name+'.json'),dict(declared_utc=stamp,candidates=[candidate],opponents=opponents,input_sha256=inputs,purpose='Fixed stronger continuations after a common screened opening; selected development only.'),exclusive=True)
        campaigns.append(dict(name=name,continuation=continuation,expected=4))
    atomic_json(E/'screened-continuation-repair-campaigns-001.json',dict(declared_utc=stamp,campaigns=campaigns,input_sha256=inputs,controls=controls,new_games=12,reused_controls=4),exclusive=True)
    print(json.dumps(dict(time_utc=stamp,pins=len(inputs),new_games=12,controls=controls)))
if __name__=='__main__':main()

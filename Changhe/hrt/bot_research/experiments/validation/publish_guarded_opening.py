"""Publish a bounded component search and export its selected JSON witnesses."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

AREA = Path('bot_research/experiments/validation/analysis/guarded_opening_budget')
DATA = Path('bot_research/bots/counters/data/guarded_opening_001.json')


def main():
    source = AREA/'verification/search.json'
    digest = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    d = json.loads(source.read_text())
    inputs = {str(source):digest(source)}
    for p,h in d['input_sha256'].items():
        assert digest(p)==h,p
        inputs[p]=h
    assert len(d['layouts'])==12
    assert d['counts']['budget_feasible_maps']==d['counts']['original_combat_checks']
    assert d['counts'].get('zero_damage_maps',0)==d['total_zero_damage_maps']
    assert len(d['selected'])==min(8,d['total_zero_damage_maps'])
    witnesses=[]
    for i,w in enumerate(d['selected']):
        assert w['round4_gold']==309-w['cost']-5*w['round3_new_factories']+w['length']
        assert w['round4_gold']>=260 and w['combat']['damage']==0
        rr=w['round3_records']
        assert len(rr)==2 and rr[0]['round']==3 and rr[0]['player']==0
        assert rr[0]['snapshot']['hp']==800 and rr[0]['snapshot']['gold']==w['round4_gold']
        assert all(e.get('accepted',True) for r in rr for e in r['event'])
        assert len(w['components'])==16
        assert next(c for c in w['components'] if c['tier']=='tier2' and c['count']==4)['damage']==0
        witnesses.append(dict(id=f'guard{i:02d}',**{k:w[k] for k in
             ('layout','walls','turrets','cost','round3_new_factories','round4_gold','path','length','components')}))
    stamp=datetime.now(timezone.utc).isoformat()
    with DATA.open('x') as f:
        json.dump(dict(time_utc=stamp,witnesses=witnesses,input_sha256=inputs),f,indent=2,sort_keys=True)
        f.write('\n')
    lines=['# Early defense and a round-four heavy purchase','',f'Checked {stamp}.','',
        f'The finite existence claim is {d["verdict"]}. The search found {d["total_zero_damage_maps"]} maps that stop the four-tier2 component and retain at least 260 gold at the next decision. This is a component result. No full-game outcome is inferred.','',
        f'The unchanged combat code checked every one of the {d["counts"]["budget_feasible_maps"]} budget-feasible maps. The enumeration crossed all twelve registered wall layouts with one or two distinct turret cells and every assignment of gun1, gun2 or splash. Walls and occupied turret cells retain a legal route.','',
        '| Wall layout | Legal cell/type assignments | Budget-feasible maps | Zero-damage maps |',
        '|---|---:|---:|---:|']
    for row in d['layouts']:
        c=row['counts']
        lines.append(f'| {row["layout"]} | {c.get("legal_map_type_assignments",0)} | {c.get("budget_feasible_maps",0)} | {c.get("zero_damage_maps",0)} |')
    lines += ['',('No witness survived: all budget-feasible maps leaked. Consequently no selected engine fixture or additional roster component was run. This refutes the finite existence claim while leaving earlier construction schedules open.' if not witnesses else 'The selected witnesses follow the ranking declared before the search: most additional factories, most round-four gold, least construction cost, then deterministic layout and serialized turret order. Every selected construction was also submitted to the original engine after two legitimate factory rounds by both players. The opponent spent 160 gold on four tier2 copies. The defended player took no damage, and its computed next-round gold matched the engine exactly.'),'',
        '| Witness | Layout | Turrets | Cost | New factories | Next gold | Route length |',
        '|---|---|---|---:|---:|---:|---:|']
    for w in witnesses:
        turrets=', '.join(f'{t["type"]}({t["x"]},{t["y"]})' for t in w['turrets'])
        lines.append(f'| {w["id"]} | {w["layout"]} | {turrets} | {w["cost"]} | {w["round3_new_factories"]} | {w["round4_gold"]} | {w["length"]} |')
    lines += ['',f'The search took {d["runtime_seconds"]:.6f} seconds at low priority on one assigned core of the shared machine. The source receipt pins the actual code and exact input JSON. All sixteen extra component results per selected witness are retained, including damage against larger or heavier rosters.','',
        'The budget formula in PROOF.md applies only to the specified first-two-round factory opening, no own minions or hit bounties, and a surviving player. Four-copy defense is not an arbitrary-roster guarantee. A gun still chooses a single target; every multi-copy claim here comes from original combat execution. An eventual counter using this map will require separate full-game evaluation with the public attacker model updated to that counter.','',
        'Reproduce from the project root with the existing Python environment, disabled bytecode, research temporary directory, one numerical thread, assigned affinity and low priority: run module bot_research.experiments.validation.design_guarded_opening with --output set to a new JSON path, then compare its complete counts and selected witnesses. The actual command is in runs/validation/guarded-opening-search-001.log.','']
    out=AREA/'RESULTS.md'
    with out.open('x') as f:f.write('\n'.join(lines))
    for p in (DATA,out,Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    with (AREA/'verification/publication.json').open('x') as f:
        json.dump(dict(time_utc=stamp,verdict=d['verdict'],witnesses=len(witnesses),input_sha256=inputs),f,indent=2,sort_keys=True)
        f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Defended-opening budget component complete\n\nClaim and verdict: {d["verdict"]}, existence within the declared finite map family. Method: all {d["counts"]["budget_feasible_maps"]} budget-feasible maps checked by original combat after the proved cash identity. Result: {d["total_zero_damage_maps"]} zero-damage maps; {len(witnesses)} selected original-engine fixtures and sixteen extra roster components each. Full-game strength remains OPEN. Evidence: {out}.\n')
    print(json.dumps(dict(time_utc=stamp,verdict=d['verdict'],selected=len(witnesses),successful_maps=d['total_zero_damage_maps'])))


if __name__=='__main__':main()

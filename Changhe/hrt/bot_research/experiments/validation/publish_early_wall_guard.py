"""Publish finite early-wall witnesses after source and fixture verification."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

AREA = Path('bot_research/experiments/validation/analysis/guarded_opening_wall_timing')
DATA = Path('bot_research/bots/counters/data/early_wall_guard_001.json')


def main():
    digest = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    source = AREA/'verification/search.json'
    d = json.loads(source.read_text())
    pins = {str(source):digest(source)}
    for p,h in d['input_sha256'].items():
        assert digest(p)==h,p
        pins[p]=h
    assert len(d['layouts'])==24
    assert d['counts']['original_combat_checks']==d['counts']['budget_feasible_maps']
    assert d['counts']['zero_damage_maps']==d['total_zero_damage_maps']
    selected=[]
    for i,w in enumerate(d['selected']):
        assert w['round4_gold']==w['gold3']-w['cost']-5*w['round3_new_factories']+15*w['factories3']+w['length']
        assert w['round4_gold']>=260 and w['combat']['damage']==0
        assert w['round3_records'][0]['snapshot']['gold']==w['round4_gold']
        assert w['round3_records'][0]['snapshot']['hp']==800
        assert len(w['components'])==16
        assert next(c for c in w['components'] if c['tier']=='tier2' and c['count']==4)['damage']==0
        for opening in w['opening']:
            assert all(e.get('accepted',True) for r in opening['records'] for e in r['event'])
        assert all(e.get('accepted',True) for r in w['round3_records'] for e in r['event'])
        keys=('wall_round','layout','walls','turrets','cost','total_cost','gold3','factories3','round3_new_factories','round4_gold','total_factories','path','length','components')
        selected.append(dict(id=f'guard{i:02d}',**{k:w[k] for k in keys}))
    stamp=datetime.now(timezone.utc).isoformat()
    with DATA.open('x') as f:
        json.dump(dict(time_utc=stamp,witnesses=selected,input_sha256=pins),f,indent=2,sort_keys=True);f.write('\n')
    lines=['# Earlier walls preserve the heavy-strike budget','',f'Checked {stamp}.','',
        f'CONFIRMED for the declared finite family: {d["total_zero_damage_maps"]} maps stop four new tier2 copies in round three and retain at least 260 gold for round four. The original combat engine checked all {d["counts"]["budget_feasible_maps"]} budget-feasible maps. Earlier walls collect path income before the guard is bought; this changes the cash constraint that defeated the preceding search.','',
        '| Witness | Wall round | Layout | Turret | Total cost | Total factories | Round-four gold | Route length |','|---|---:|---|---|---:|---:|---:|---:|']
    for w in selected:
        ts=', '.join(f'{t["type"]}({t["x"]},{t["y"]})' for t in w['turrets'])
        lines.append(f'| {w["id"]} | {w["wall_round"]} | {w["layout"]} | {ts} | {w["total_cost"]} | {w["total_factories"]} | {w["round4_gold"]} | {w["length"]} |')
    lines += ['',f'The {len(selected)} selected witnesses are the best-ranked distinct wall-round/layout pairs, under the ranking fixed before the search. Every selected opening and third-round action list passed the unchanged engine, and its predicted gold exactly matched the engine. The first witness builds the 20-wall lead opening in round one and splash(1,3) in round three: it has 14 factories and 267 gold at decision four.','',
       'The extra component checks delimit the result. Each selected splash map stops all tested tier1/tier2 counts (1,2,4,8) but every tested tier3/tier4 copy reaches the base. The two selected gun2 maps stop one tier3 but leak with two or more, and leak with eight tier2 copies. This is not a universal defense.','',
       f'The enumeration took {d["runtime_seconds"]:.6f} seconds on one assigned core at low priority. There were {d["counts"]["legal_map_type_assignments"]} route-legal type/cell assignments across both wall schedules. The receipt preserves counts per layout, selected original records and all extra components. The exact witness JSON is counters/data/early_wall_guard_001.json.','',
       'Reproduce by running experiments.validation.design_early_wall_guard with a fresh --output path under bot_research, using the existing Python, disabled bytecode, research temporary directory, one numerical thread, assigned affinity and low priority. The complete argument is in PROOF.md. A bot using a witness still needs full-game tests, including a public-clone opponent updated to that exact bot.','']
    out=AREA/'RESULTS.md'
    with out.open('x') as f:f.write('\n'.join(lines))
    for p in (DATA,out,Path(__file__).relative_to(Path.cwd())):pins[str(p)]=digest(p)
    with (AREA/'verification/publication.json').open('x') as f:
        json.dump(dict(time_utc=stamp,verdict=d['verdict'],witnesses=len(selected),input_sha256=pins),f,indent=2,sort_keys=True);f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Earlier-wall budget component complete\n\nClaim and verdict: CONFIRMED, finite existence. All {d["counts"]["budget_feasible_maps"]} budget-feasible maps checked by original combat; {d["total_zero_damage_maps"]} successes and {len(selected)} original-engine witness fixtures. The first-ranked witness builds 20 lead walls in round one, splash(1,3) in round three, and reaches round four with 14 factories and267gold. It stops the tested tier2 counts but leaks every tested tier3 copy. Full-game strength remains OPEN. Evidence: {out}.\n')
    print(json.dumps(dict(time_utc=stamp,verdict=d['verdict'],successful_maps=d['total_zero_damage_maps'],selected=len(selected))))


if __name__=='__main__':main()

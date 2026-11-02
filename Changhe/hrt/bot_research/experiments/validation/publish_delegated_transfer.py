"""Publish every registered frozen-delegate transfer and its paired control."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
AREA = E/'analysis/delegated_transfer'
INVERSE = {'W':'L', 'D':'D', 'L':'W'}
RANK = {'L':0, 'D':1, 'W':2}


def canonical(records, side):
    records = json.loads(json.dumps(records))
    for rec in records:
        rec.pop('match', None)
        rec['player'] ^= side
        rec['snapshot']['name'] = 'target' if rec['player'] == 0 else 'counter'
        for event in rec['event']:
            event.pop('order', None)
        if rec.get('result', {}).get('winner') is not None:
            rec['result']['winner'] ^= side
    return sorted(records, key=lambda rec:(rec['round'],rec['player']))


def main():
    inputs = {}
    def digest(p):
        return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        inputs[str(p)] = digest(p)
        return json.loads(p.read_text())
    def records(row):
        p = Path(row['replay_path'])
        inputs[str(p)] = digest(p)
        return [json.loads(line) for line in p.read_text().splitlines()]
    declared = read(E/'delegated-transfer-controls-001.json')
    assert len(declared['pairs']) == 180 and len(declared['campaigns']) == 10
    histories = {}
    campaign_rows = []
    fresh = 0
    independent = 0
    handoffs = 0
    for campaign in declared['campaigns']:
        name, size = campaign['name'], campaign['expected']
        manifest = read(E/(name+'.json'))
        assert manifest['expected_conditions'] == size == 18
        for p, h in manifest['input_sha256'].items():
            assert digest(p) == h, p
        audits = {kind:read(R/(name+'-'+kind+'.json')) for kind in
                  ('strict','replay','summary','data','histories','delegation')}
        summary, history = audits['summary'], audits['histories']
        assert audits['strict']['valid_conditions'] == size
        assert summary['valid_conditions'] == size and summary['unresolved_conditions'] == 0
        assert summary['complete_assignment_pairs'] == size//2
        assert not summary['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['replay']['count'] == size
        assert audits['data']['all_passed'] and audits['delegation']['all_passed']
        assert audits['delegation']['games'] == size
        assert all(history[k] for k in ('all_fresh_actions_legal','all_observations_unchanged',
            'all_public_selections_verified','all_replayed','exact_counter_policy_reproduction'))
        for p, h in history['input_sha256'].items():
            assert digest(p) == h, p
        independent += audits['delegation']['checked_calls']
        handoffs += audits['delegation']['handoffs']
        for case in history['cases']:
            assert case['result'] not in histories
            histories[case['result']] = case
            fresh += len(case['rounds'])
        campaign_rows.append(dict(name=name,delegate=campaign['delegate'],games=size,
            identical_assignment_pairs=summary['identical_assignment_pairs']))
    assert len(histories) == 180 and fresh == independent
    stats = {mode:dict(old=Counter(),new=Counter(),transitions=Counter(),improved=0,worsened=0,
                      exact_histories=0,old_losses=0,old_losses_now_won=0,growth_cases=0,growth_exact=0)
             for mode in ('econ20','fortress38')}
    timings = defaultdict(list)
    comparisons = []
    for pair in declared['pairs']:
        old, new = checked_row(pair['old'],inputs), checked_row(pair['new'],inputs)
        old_raw, new_raw = read(Path(pair['old'])), read(Path(pair['new']))
        for checked in (old,new):
            c = checked['condition']
            assert c['candidate_id'] == pair['target'] and c['candidate_spec'] == pair['target_spec']
            assert c['candidate_side'] == pair['candidate_side']
            assert c['opponent_id'] == 'route_adaptive'
        a, b = records(old_raw), records(new_raw)
        for rec in a+b:
            rec.pop('match', None)
        assert a[:10] == b[:10], (pair['target'],pair['delegate'],'changed public prefix')
        aa, bb = canonical(a,pair['candidate_side']), canonical(b,pair['candidate_side'])
        same = aa == bb
        assert same == (old['canonical_replay_sha256'] == new['canonical_replay_sha256'])
        differing = next((min(x['round'],y['round']) for x,y in zip(aa,bb) if x != y), None)
        if differing is None and len(aa) != len(bb):
            differing = min(aa[len(bb):]+bb[len(aa):],key=lambda r:r['round'])['round']
        was, now = INVERSE[old['outcome']], INVERSE[new['outcome']]
        mode = pair['delegate']
        s = stats[mode]
        s['old'][was] += 1; s['new'][now] += 1; s['transitions'][was+'->'+now] += 1
        s['improved'] += RANK[now] > RANK[was]
        s['worsened'] += RANK[now] < RANK[was]
        s['exact_histories'] += same
        s['old_losses'] += was == 'L'
        s['old_losses_now_won'] += was == 'L' and now == 'W'
        case = histories[pair['new']]
        if case['selected'] == 'growth':
            s['growth_cases'] += 1
            s['growth_exact'] += same
        timings[mode].append(new['decision_seconds_candidate_first'][1])
        comparisons.append(dict(**pair,selected=case['selected'],delegate_started=case['delegate_started'],
            old_outcome=was,new_outcome=now,old_hp_counter_first=old['hp_candidate_first'][::-1],
            new_hp_counter_first=new['hp_candidate_first'][::-1],old_final_round=old['rounds'],
            new_final_round=new['rounds'],same_complete_trajectory=same,first_differing_round=differing))
    assert len(comparisons) == 180
    for s in stats.values():
        assert sum(s['old'].values()) == sum(s['new'].values()) == 90
        assert s['old_losses'] == 6
        assert s['growth_exact'] == s['growth_cases']
        s['strict_success'] = s['worsened'] == 0 and s['old_losses_now_won'] == s['old_losses']
    score = lambda c:f'{c["W"]}W/{c["D"]}D/{c["L"]}L'
    table = []
    def cell(rows, mode):
        selected = sorted((r for r in rows if r['delegate']==mode), key=lambda r:r['candidate_side'])
        assert len(selected)==2
        pieces = [f'{r["new_outcome"]} {r["new_hp_counter_first"][0]}:{r["new_hp_counter_first"][1]} r{r["new_final_round"]}' for r in selected]
        return pieces[0] if pieces[0]==pieces[1] else 'seat0 '+pieces[0]+'; seat1 '+pieces[1]
    for target in sorted({r['target'] for r in comparisons}):
        rows = [r for r in comparisons if r['target']==target]
        old = {(r['old_outcome'],tuple(r['old_hp_counter_first']),r['old_final_round']) for r in rows}
        assert len(old)==1
        outcome,hp,end = next(iter(old))
        table.append(f'| {target} | {outcome} {hp[0]}:{hp[1]} r{end} | {cell(rows,"econ20")} | {cell(rows,"fortress38")} |')
    checked_at = datetime.now(timezone.utc).isoformat()
    verdict = ('CONFIRMED' if any(s['strict_success'] for s in stats.values()) else 'REFUTED')+': at least one tested continuation preserves every old nonloss and turns all six old losses into wins.'
    summary_lines = [f'- {mode}: {score(s["new"])} against old {score(s["old"])}; {s["improved"]} improved and {s["worsened"]} worsened W/D/L outcomes, {s["exact_histories"]} unchanged complete histories. All {s["growth_cases"]} growth-branch histories are unchanged.' for mode,s in stats.items()]
    timing = {mode:dict(calls=sum(v['calls'] for v in values),total_seconds=sum(v['total'] for v in values),maximum_seconds=max((v['max'] for v in values),default=0))
              for mode,values in timings.items()}
    assert sum(t['calls'] for t in timing.values()) == fresh
    timing_lines = [f'- {mode}: {t["calls"]} calls, {t["total_seconds"]:.6f} seconds summed, maximum {t["maximum_seconds"]:.6f} seconds.' for mode,t in timing.items()]
    output = AREA/'RESULTS.md'
    text = f'''# Complete frozen-delegate transfer

Checked {checked_at}.

{verdict}

All 180 declared games are included. The two continuations each face exactly the same 45 disclosed targets, with both assignments. The old control is the completed emergency-template selector. The stricter success criterion here requires a win on each old loss; a draw is reported separately, even though it avoids defeat.

'''+ '\n'.join(summary_lines)+f'''

Each cell gives the counter outcome, HP counter:target and final round. Equal physical assignments share a cell; any difference is shown explicitly. These are deterministic development conditions, not independent draws from an opponent population.

| Target | Old emergency template | Frozen econ20 | Frozen fortress38 |
|---|---|---|---|
'''+ '\n'.join(table)+f'''

All strict/source/data checks and original-engine replays pass. All {fresh} freshly regenerated counter decisions agree and leave observations unchanged; submitted actions are legal and no bot errors are recorded. A separate implementation checks {independent} public handoff decisions and {handoffs} actual starts without importing the controller or trigger helper. Every new game has exactly the same first four complete rounds as its old control, removing only the run identifier. All old result/replay pairs are rehashed with their source attestations. The complete paired results and every transition are retained in verification/full_games.json.

Measured counter decision costs, low-priority wall time on shared hardware:

'''+ '\n'.join(timing_lines)+'''

The reached-map handoff differs from playing either teammate bot from round one. Their source may use wall-clock search cutoffs, so observed exact reproduction does not establish load-independent behavior. No withheld condition is used for these improvements. The installed best_v9e and its independent final pool-C validation are unchanged.

Reproduce each delegated-transfer manifest with run_data_development, then audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, check_delegated_histories and audit_delegation. Run this publisher after all ten campaigns pass. Use new output paths, the existing project Python, disabled bytecode, the research temporary directory, assigned affinity, one numerical thread and low priority. The campaign logs retain exact commands; verification/full_games.json pins the evidence and publisher.
'''
    with output.open('x') as f:f.write(text)
    for p in (output,AREA/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    receipt = dict(time_utc=checked_at,all_audits_passed=True,verdict=verdict,games=180,
        fresh_counter_decisions=fresh,independent_handoff_calls=independent,handoffs=handoffs,
        exact_first_four_round_pairs=180,campaigns=campaign_rows,statistics=stats,counter_timing=timing,
        comparisons=comparisons,input_sha256=inputs)
    with (AREA/'verification/full_games.json').open('x') as f:json.dump(receipt,f,indent=2,sort_keys=True);f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {checked_at}: Complete frozen-delegate transfer\n\n'
        f'Claim and verdict: {verdict}\n\nMethod: 180 declared games, two continuations on all 45 prior targets in both assignments; paired with 90 old controls. '
        f'Result: '+ '; '.join(f'{mode} {score(s["new"])}, {s["improved"]} improvements and {s["worsened"]} regressions' for mode,s in stats.items())+
        f'. All {fresh} fresh decisions, {independent} independently reconstructed handoff calls and 180 identical first-four-round prefixes pass. Development only. Evidence: {output}.\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ('comparisons','input_sha256','campaigns')}))


if __name__ == '__main__':
    main()

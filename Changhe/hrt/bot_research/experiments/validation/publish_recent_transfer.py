"""Publish all recent-target conditions using specification-aware grouping."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
AREA = E/'analysis/recent_transfer'
INVERSE = {'W':'L', 'D':'D', 'L':'W'}
RANK = {'L':0, 'D':1, 'W':2}
MODES = ('adaptive', 'early', 'growth')


def main():
    inputs = {}
    def digest(p):
        return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        inputs[str(p)] = digest(p)
        return json.loads(Path(p).read_text())
    def records(row):
        p = Path(row['replay_path'])
        inputs[str(p)] = digest(p)
        answer = [json.loads(s) for s in p.read_text().splitlines()]
        for rec in answer:
            rec.pop('match', None)
        return answer
    declared = read(E/'recent-transfer-campaigns-001.json')
    assert declared['expected'] == 36 and len(declared['campaigns']) == 6
    results = []
    pairs = []
    comparisons = []
    fresh = independent = handoffs = 0
    for item in declared['campaigns']:
        name = item['name']
        m = read(E/(name+'.json'))
        assert m['expected_conditions'] == item['expected'] == 6
        for p, sha in m['input_sha256'].items():
            assert digest(p) == sha, p
            inputs[p] = sha
        audits = {k:read(R/(name+'-'+k+'.json')) for k in
                  ('strict','replay','summary','data','histories','delegation')}
        assert audits['strict']['valid_conditions'] == 6
        assert audits['strict']['attempt_counts'] == {'valid':6}
        assert not audits['strict']['unresolved'] and not audits['strict']['repeat_disagreements']
        assert audits['summary']['valid_conditions'] == 6
        assert audits['replay']['all_passed'] and audits['replay']['count'] == 6
        assert audits['data']['all_passed'] and audits['delegation']['all_passed']
        h = audits['histories']
        assert all(h[k] for k in ('all_fresh_actions_legal','all_observations_unchanged',
             'all_public_selections_verified','all_replayed','exact_counter_policy_reproduction'))
        for p, sha in h['input_sha256'].items():
            assert digest(p) == sha, p
            inputs[p] = sha
        by_mode = {}
        recorded = {}
        for case in h['cases']:
            row = checked_row(case['result'], inputs)
            raw = read(case['result'])
            c = row['condition']
            assert c['candidate_id'] == item['target'] and c['candidate_spec'] == item['target_spec']
            assert c['opponent_id'] == 'route_adaptive'
            params = {k:json.loads(v[0]) for k,v in parse_qs(c['opponent_spec'].partition('?')[2]).items()}
            assert params['delegate'] == 'fortress38' and set(params) == {'mode','delegate'}
            mode, side = params['mode'], c['candidate_side']
            assert mode in MODES and (mode,side) not in by_mode
            result = dict(target=item['target'],target_spec=item['target_spec'],mode=mode,
                counter_spec=c['opponent_spec'],candidate_side=side,result=case['result'],
                outcome=INVERSE[row['outcome']],hp_counter_first=row['hp_candidate_first'][::-1],
                rounds=row['rounds'],selected=case['selected'],delegate_started=case['delegate_started'],
                canonical_replay_sha256=row['canonical_replay_sha256'],
                counter_decision_seconds=row['decision_seconds_candidate_first'][1])
            results.append(result)
            by_mode[mode,side] = result
            recorded[mode,side] = records(raw)
            fresh += len(case['rounds'])
        assert len(by_mode) == 6
        independent += audits['delegation']['checked_calls']
        handoffs += audits['delegation']['handoffs']
        for mode in MODES:
            a, b = by_mode[mode,0], by_mode[mode,1]
            pairs.append(dict(target=item['target'],mode=mode,
                same_complete_trajectory=a['canonical_replay_sha256']==b['canonical_replay_sha256'],
                outcomes=[a['outcome'],b['outcome']],results=[a['result'],b['result']]))
        for side in (0,1):
            a, e, g = [by_mode[mode,side] for mode in MODES]
            ra, re, rg = [recorded[mode,side] for mode in MODES]
            assert min(len(ra),len(re),len(rg)) >= 8
            assert ra[:8] == re[:8] == rg[:8], (item['target'],side,'prefix disagreement')
            chosen = a['selected']
            assert chosen in ('early','growth')
            fixed = by_mode[chosen,side]
            assert ra == recorded[chosen,side], (item['target'],side,'chosen-branch disagreement')
            assert a['canonical_replay_sha256'] == fixed['canonical_replay_sha256']
            better = [r['mode'] for r in (e,g) if RANK[r['outcome']] > RANK[a['outcome']]]
            comparisons.append(dict(target=item['target'],candidate_side=side,selected=chosen,
                same_first_three_rounds=True,same_chosen_branch_history=True,
                adaptive_outcome=a['outcome'],early_outcome=e['outcome'],growth_outcome=g['outcome'],
                better_fixed_modes=better,both_fixed_lose=e['outcome']=='L' and g['outcome']=='L'))
    assert len(results) == 36 and len(pairs) == 18 and len(comparisons) == 12
    assert fresh == independent
    counts = {mode:Counter(r['outcome'] for r in results if r['mode']==mode) for mode in MODES}
    timing = {}
    for mode in MODES:
        values = [r['counter_decision_seconds'] for r in results if r['mode']==mode]
        timing[mode] = dict(calls=sum(t['calls'] for t in values),
            total_seconds=sum(t['total'] for t in values),maximum_seconds=max(t['max'] for t in values))
    assert sum(t['calls'] for t in timing.values()) == fresh
    verdict = ('CONFIRMED' if counts['adaptive']['L']==0 else 'REFUTED')+': adaptive avoids defeat on all six declared recent targets in both assignments.'
    stamp = datetime.now(timezone.utc).isoformat()
    lines = ['# Recent teammate transfer and branch ablation','',f'Checked {stamp}.','',verdict,'',
       'All 36 declared games are included. Each cell gives counter outcome, HP counter:target and ending round. Equal physical assignments share a cell; differences are explicit. These six targets were disclosed before evaluation. This is development coverage, not a fresh held-out result.','',
       '| Target | Adaptive | Forced early | Forced growth | Adaptive selection |',
       '|---|---|---|---|---|']
    def cell(target,mode):
        rr = sorted((r for r in results if r['target']==target and r['mode']==mode),key=lambda r:r['candidate_side'])
        assert len(rr)==2
        values = [f'{r["outcome"]} {r["hp_counter_first"][0]}:{r["hp_counter_first"][1]} r{r["rounds"]}' for r in rr]
        return values[0] if values[0]==values[1] else 'seat0 '+values[0]+'; seat1 '+values[1]
    for item in declared['campaigns']:
        target = item['target']
        chosen = [r['selected'] for r in results if r['target']==target and r['mode']=='adaptive']
        lines.append('| '+target+' | '+' | '.join(cell(target,mode) for mode in MODES)+' | '+('/'.join(sorted(set(chosen))))+' |')
    lines += ['','Mode totals and measured low-priority wall time on shared hardware:','']
    for mode in MODES:
        c,t = counts[mode],timing[mode]
        lines.append(f'- {mode}: {c["W"]}W/{c["D"]}D/{c["L"]}L; {t["calls"]} calls, {t["total_seconds"]:.6f} seconds summed, maximum {t["maximum_seconds"]:.6f} seconds.')
    selection_failures = [c for c in comparisons if c['better_fixed_modes']]
    universal_failures = [c for c in comparisons if c['both_fixed_lose']]
    lines += ['',f'Another fixed branch improves W/D/L in {len(selection_failures)} of the twelve adaptive conditions. Both fixed branches lose in {len(universal_failures)} conditions. The full receipt identifies each condition without selecting a favorable subset.','',
       f'All {fresh} freshly regenerated counter decisions agree, all observations remain unchanged, and all submitted actions are legal. Original-engine replay, source/data archives and strict accounting pass for every game. Independent reconstruction agrees on {independent} handoff calls and {handoffs} starts. The twelve three-way groups have exactly equal complete records through round three. Each adaptive game has exactly the same complete history as its selected fixed-mode control. Of eighteen assignment pairs, {sum(p["same_complete_trajectory"] for p in pairs)} have identical canonical histories. Neither these pairs nor repeated histories are independent samples.','',
       'All three modes deliberately use the same display name to keep observations comparable. The legacy per-campaign generic summary groups by display name, so its assignment-pair count and abbreviated Markdown table do not distinguish the three specifications. This publication instead keys all conditions by full specification and physical assignment. The strict audit retains all six conditions per target; its condition accounting is unaffected. Use this table and verification/full_games.json for the complete comparison.','',
       'The empirical agreement does not prove load-independent policy behavior: teammate planners contain wall-clock search cutoffs. The result concerns the frozen sources and recorded conditions only. It does not promote a counter to best.py.','',
       'Reproduce each recent-transfer manifest through run_data_development, audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, check_delegated_histories and audit_delegation, then run publish_recent_transfer. The exact bounded commands are retained in runs/validation/recent-transfer-001-pipeline.log. Use new output names, the existing environment, disabled bytecode, the research temporary directory, one numerical thread, assigned affinity and low priority.','']
    output = AREA/'RESULTS.md'
    with output.open('x') as f:f.write('\n'.join(lines))
    for p in (output,AREA/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    receipt = dict(time_utc=stamp,all_audits_passed=True,verdict=verdict,games=36,counts=counts,
        fresh_counter_decisions=fresh,independent_handoff_calls=independent,handoffs=handoffs,
        same_first_three_round_groups=12,same_chosen_branch_histories=12,assignment_pairs=pairs,
        counter_timing=timing,results=results,comparisons=comparisons,input_sha256=inputs)
    with (AREA/'verification/full_games.json').open('x') as f:json.dump(receipt,f,indent=2,sort_keys=True);f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {stamp}: Recent teammate branch comparison complete\n\nClaim and verdict: {verdict}\n\nMethod: all36declared games, six targets x three modes x two assignments. Result: '+ '; '.join(f'{mode} {c["W"]}W/{c["D"]}D/{c["L"]}L' for mode,c in counts.items())+f'. All{fresh}fresh decisions and independent handoffs pass; twelve common-prefix groups and twelve exact chosen-branch controls agree. Another fixed branch improves{len(selection_failures)}adaptive conditions; both fixed branches lose in{len(universal_failures)}. Development only. Complete specification-aware table: {output}.\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ('results','comparisons','input_sha256','assignment_pairs')}))


if __name__ == '__main__':
    main()

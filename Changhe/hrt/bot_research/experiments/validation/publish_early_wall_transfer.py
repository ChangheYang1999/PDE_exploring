"""Pair the complete early-wall transfer with its earlier fixed control."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E=Path('bot_research/experiments/validation')
R=Path('bot_research/runs/validation')
A=E/'analysis/early_wall_transfer'
INVERSE={'W':'L','L':'W','D':'D'}
RANK={'L':0,'D':1,'W':2}


def main():
    inputs={}
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        inputs[str(p)]=digest(p)
        return json.loads(Path(p).read_text())
    declaration=read(E/'early-wall-transfer-campaigns-001.json')
    assert declaration['games']==98 and len(declaration['pairs'])==98
    control_receipt=read(E/'analysis/delegated_transfer/verification/full_games.json')
    assert control_receipt['all_audits_passed'] and control_receipt['games']==180
    for p,h in control_receipt['input_sha256'].items():
        assert digest(p)==h,p
        inputs[p]=h
    old_directories={Path(p['old']).parent.parent for p in declaration['pairs'] if p['old']}
    for directory in sorted(old_directories):
        metadata=read(directory/'freeze.json')
        for p,h in metadata['source_sha256'].items():
            archived=directory/'sources'/p
            assert digest(archived)==h,p
            inputs[str(archived)]=h
    calls=filtered=0
    cases={}
    for item in declaration['campaigns']:
        name=item['name'];size=item['expected']
        m=read(E/(name+'.json'))
        for p,h in m['input_sha256'].items():
            assert digest(p)==h,p
            inputs[p]=h
        aa={k:read(R/(name+'-'+k+'.json')) for k in ('strict','replay','summary','data','fresh')}
        assert aa['strict']['valid_conditions']==size and aa['strict']['attempt_counts']=={'valid':size}
        assert not aa['strict']['unresolved'] and not aa['strict']['repeat_disagreements']
        assert aa['replay']['all_passed'] and aa['replay']['count']==size
        assert aa['data']['all_passed']
        fresh=aa['fresh']
        assert all(fresh[k] for k in ('all_passed','all_replayed','all_actions_legal','all_observations_unchanged'))
        assert fresh['games']==size
        for p,h in fresh['input_sha256'].items():
            assert digest(p)==h,p
            inputs[p]=h
        calls+=fresh['checked_calls'];filtered+=fresh['filtered_proposals']
        for c in fresh['cases']:
            assert c['result'] not in cases and c['witness']=='guard00'
            cases[c['result']]=c
    rows=[];old_counts=Counter();new_counts=Counter();extra_counts=Counter();transitions=Counter()
    improvements=[];regressions=[]
    for pair in declaration['pairs']:
        n=checked_row(pair['new'],inputs);nc=n['condition']
        assert nc['candidate_id']=='guard00' and nc['candidate_side']==pair['guard_side']
        assert nc['opponent_id']==pair['target'] and nc['opponent_spec']==pair['target_spec']
        fc=cases[pair['new']]
        row=dict(pair,outcome=n['outcome'],hp=n['hp_candidate_first'],rounds=n['rounds'],
            timing=n['decision_seconds_candidate_first'],canonical_replay_sha256=n['canonical_replay_sha256'],
            filtered_proposals=fc['filtered_proposals'])
        if pair['old']:
            o=checked_row(pair['old'],inputs);oc=o['condition']
            assert oc['candidate_id']==pair['target'] and oc['candidate_side']==1-pair['guard_side']
            if pair['target']=='best_v9e':
                eq=declaration['best_equivalence']
                old_freeze=read(Path(pair['old']).parent.parent/'freeze.json')
                assert old_freeze['source_sha256'][eq['old_source']]==eq['sha256']
                assert digest(eq['new_source'])==eq['sha256']
                assert oc['candidate_spec']=='bot_research.bots.best:@make'
            else:
                assert oc['candidate_spec']==pair['target_spec']
            before=INVERSE[o['outcome']]
            row.update(old_outcome=before,old_hp=o['hp_candidate_first'][::-1],old_rounds=o['rounds'])
            old_counts[before]+=1;new_counts[n['outcome']]+=1
            transitions[before+'->'+n['outcome']]+=1
            delta=RANK[n['outcome']]-RANK[before]
            if delta>0:improvements.append(dict(target=pair['target'],side=pair['guard_side'],before=before,after=n['outcome']))
            if delta<0:regressions.append(dict(target=pair['target'],side=pair['guard_side'],before=before,after=n['outcome']))
        else:
            extra_counts[n['outcome']]+=1
        rows.append(row)
    assert len(rows)==98 and sum(old_counts.values())==sum(new_counts.values())==90
    assert old_counts==Counter(W=80,D=10) and sum(extra_counts.values())==8
    assert calls==sum(2*r['rounds'] for r in rows)
    pairs=[]
    for target in sorted({r['target'] for r in rows}):
        rr=sorted((r for r in rows if r['target']==target),key=lambda r:r['guard_side'])
        assert len(rr)==2 and [r['guard_side'] for r in rr]==[0,1]
        pairs.append(dict(target=target,same_history=rr[0]['canonical_replay_sha256']==rr[1]['canonical_replay_sha256']))
    h1=not regressions and bool(improvements)
    h2=extra_counts['L']==0
    stamp=datetime.now(timezone.utc).isoformat()
    score=lambda c:f'{c["W"]}W/{c["D"]}D/{c["L"]}L'
    lines=['# Early-wall transfer over the complete development union','',f'Checked {stamp}.','',
        f'The strict paired improvement claim is {"CONFIRMED" if h1 else "REFUTED"}: the old delegated counter scored {score(old_counts)}, and guard00 scored {score(new_counts)} on the same ninety target-and-seat conditions. There are {len(improvements)} improvements and {len(regressions)} regressions in W/D/L order. The separate no-loss claim on four additional counter policies is {"CONFIRMED" if h2 else "REFUTED"}: {score(extra_counts)}.','',
        'The policy, component-selected witness and target set were fixed before this matrix. This is development evidence after guard00 performed well on four current teammates; it is not an estimate from an untouched opponent sample.','',
        '| Target | Earlier delegated counter | Early-wall guard00 |','|---|---|---|']
    for target in sorted({r['target'] for r in rows}):
        rr=sorted((r for r in rows if r['target']==target),key=lambda r:r['guard_side'])
        cells=[]
        for old in (True,False):
            vals=[]
            for r in rr:
                if old and not r['old']:vals.append('not in paired control');continue
                outcome=r['old_outcome'] if old else r['outcome']
                hp=r['old_hp'] if old else r['hp'];rnd=r['old_rounds'] if old else r['rounds']
                vals.append(f'{outcome} {hp[0]}:{hp[1]} r{rnd}')
            cells.append(vals[0] if vals[0]==vals[1] else 'seat0 '+vals[0]+'; seat1 '+vals[1])
        lines.append('| '+target+' | '+' | '.join(cells)+' |')
    tt=[r['timing'][0] for r in rows]
    timing=dict(calls=sum(x['calls'] for x in tt),total_seconds=sum(x['total'] for x in tt),maximum_seconds=max(x['max'] for x in tt))
    lines+=['',f'All {calls} fresh action-generating calls across both policies agree with recorded actions. Original-engine replay, explicit source and JSON archives, observation immutability and legal submissions pass. There are {filtered} filtered guard proposals, zero rejected submitted actions and zero bot errors. {sum(p["same_history"] for p in pairs)} of 49 assignment pairs have identical complete canonical histories.','',
        f'Actual guard decisions took {timing["total_seconds"]:.6f} seconds across {timing["calls"]} calls; the largest single call was {timing["maximum_seconds"]:.6f} seconds. These measurements use one assigned CPU core at low priority, one numerical thread, and the shared-machine load. Audit time is excluded.','',
        'The old control used best.py at the frozen best_v9e hash. The new target imports its byte-identical frozen copy, allowing the lead to work without changing this comparison. The receipt verifies that equivalence from the old source attestation. Forty-four other old target specifications are unchanged. Earlier control results and their original audits are reused explicitly; they are not additional new games.','',
        'A favorable aggregate does not establish dominance over every tested opponent: the paired regression list in verification/full_games.json is authoritative. Nor does this test cover the full public-clone timing grid or arbitrary randomized opponents.','',
        'Reproduce every manifest listed in early-wall-transfer-campaigns-001.json using bot_research.experiments.validation.run_data_development, then audit_development_strict, replay_audit, audit_data_archives and check_early_wall_histories. The pipeline log retains exact bounded commands. Restore any archived old replay before pairing controls. Use the existing Python with bytecode disabled, research temporary directory, assigned affinity, low priority and one numerical thread.','']
    out=A/'RESULTS.md'
    with out.open('x') as f:f.write('\n'.join(lines))
    for p in (out,A/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    data=dict(time_utc=stamp,all_audits_passed=True,games=98,fresh_decisions=calls,filtered_proposals=filtered,
        old_counts=old_counts,new_counts=new_counts,extra_counts=extra_counts,transitions=transitions,
        paired_improvement_confirmed=h1,extra_no_loss_confirmed=h2,improvements=improvements,regressions=regressions,
        pairs=pairs,rows=rows,timing=timing,input_sha256=inputs)
    with (A/'verification/full_games.json').open('x') as f:json.dump(data,f,indent=2,sort_keys=True);f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {stamp}: Early-wall transfer complete\n\nClaim and verdict: paired strict improvement {"CONFIRMED" if h1 else "REFUTED"}, additional-counter no-loss {"CONFIRMED" if h2 else "REFUTED"}. On90old conditions: delegated {score(old_counts)}, guard00 {score(new_counts)}, {len(improvements)} improvements and {len(regressions)} regressions. Additional8games: {score(extra_counts)}. All {calls} fresh decisions pass. Complete target table, losses and timing: {out}.\n')
    print(json.dumps({k:v for k,v in data.items() if k not in ('pairs','rows','input_sha256')}))


if __name__=='__main__':main()

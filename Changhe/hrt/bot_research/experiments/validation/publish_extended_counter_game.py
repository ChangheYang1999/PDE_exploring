"""Validate a fixed five-policy table and a rational maximin certificate."""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
from urllib.parse import parse_qs
import hashlib
import json
from bot_research.experiments.validation.compare_recorded_controls import checked_row

E=Path('bot_research/experiments/validation')
R=Path('bot_research/runs/validation')
AREA=E/'analysis/extended_counter_game'
ORDER=['B','C','D','G','H']


def norm(spec):
    base,_,query=spec.partition('?')
    params={k:json.loads(v[0]) for k,v in parse_qs(query).items()}
    if base=='bot_research.bots.counters.delegated_defense:@make':
        params.setdefault('mode','adaptive')
        params.setdefault('delegate','econ20')
    return base,params


def linear_solve(rows, rhs):
    n=len(rows)
    m=[[Fraction(v) for v in row]+[Fraction(value)] for row,value in zip(rows,rhs)]
    assert all(len(row)==n+1 for row in m)
    for col in range(n):
        pivot=next((i for i in range(col,n) if m[i][col]),None)
        if pivot is None:return None
        m[col],m[pivot]=m[pivot],m[col]
        div=m[col][col]
        m[col]=[v/div for v in m[col]]
        for i in range(n):
            if i==col:continue
            div=m[i][col]
            m[i]=[v-div*w for v,w in zip(m[i],m[col])]
    return [row[-1] for row in m]


def exact_certificate(matrix):
    n=len(matrix)
    columns=[[matrix[i][j] for i in range(n)] for j in range(n)]
    constraints=[[int(i==j) for j in range(n)] for i in range(n)]+columns
    feasible=set()
    for active in combinations(range(2*n),n-1):
        p=linear_solve([[1]*n]+[constraints[i] for i in active],[1]+[0]*(n-1))
        if p is None or any(v<0 for v in p):continue
        if any(sum(x*y for x,y in zip(p,col))<0 for col in columns):continue
        assert sum(p)==1
        feasible.add(tuple(p))
    if not feasible:return None
    p=min(feasible,key=lambda x:(sum(v>0 for v in x),x))
    payoffs=[sum(p[i]*Fraction(matrix[i][j]) for i in range(n)) for j in range(n)]
    assert all(v>=0 for v in p) and sum(p)==1 and all(v>=0 for v in payoffs)
    assert all(matrix[i][j]==-matrix[j][i] for i in range(n) for j in range(n))
    assert all(sum(Fraction(matrix[i][j])*p[j] for j in range(n))<=0 for i in range(n))
    return dict(weights=[str(v) for v in p],column_payoffs=[str(v) for v in payoffs],
                exact_value='0',feasible_vertices=[[str(v) for v in q] for q in sorted(feasible)],
                checked_active_sets=comb(2*n,n-1))


def main():
    inputs={}
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(path):
        inputs[str(path)]=digest(path)
        return json.loads(Path(path).read_text())
    def verify(mapping):
        for path,sha in mapping.items():
            assert digest(path)==sha,path
            inputs[path]=sha
    d=read(E/'extended-counter-game-campaigns-001.json')
    arithmetic=read(AREA/'verification/arithmetic_components.json')
    assert arithmetic['all_passed'] and arithmetic['checker_sha256']==digest(__file__)
    assert set(d['policies'])==set(ORDER) and d['new_games']==10 and d['reused_games']==20
    verify(d['receipt_sha256'])
    receipts={key:read(path) for key,path in d['receipts'].items()}
    for key,receipt in receipts.items():
        assert receipt.get('all_passed',receipt.get('all_audits_passed',False)),key
        verify(receipt['input_sha256'])
    records=list(dict(item,reused=True) for item in d['reused'])
    fresh_new=0
    for item in d['campaigns']:
        name=item['name']
        manifest=read(E/(name+'.json'));verify(manifest['input_sha256'])
        audits={k:read(R/(name+'-'+k+'.json')) for k in ('strict','replay','data','fresh')}
        strict=audits['strict'];fresh=audits['fresh']
        assert strict['valid_conditions']==2 and strict['attempt_counts']=={'valid':2}
        assert not strict['unresolved'] and not strict['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['replay']['count']==2
        assert audits['data']['all_passed']
        assert all(fresh[k] for k in ('all_passed','all_replayed','all_actions_legal','all_observations_unchanged'))
        assert fresh['games']==2
        verify(fresh['input_sha256']);fresh_new+=fresh['checked_calls']
        for i in range(2):
            records.append(dict(a=item['a'],b=item['b'],reused=False,
                result=str(R/name/'results'/f'case{i:04d}.json')))
    assert len(records)==30 and len({r['result'] for r in records})==30
    archived=set();cases=[];groups=defaultdict(list)
    for item in records:
        a,b=item['a'],item['b'];row=checked_row(item['result'],inputs);c=row['condition']
        assert norm(c['candidate_spec'])==norm(d['policies'][a]['spec']),(a,item['result'])
        assert norm(c['opponent_spec'])==norm(d['policies'][b]['spec']),(b,item['result'])
        directory=Path(item['result']).parent.parent
        if directory not in archived:
            meta=read(directory/'freeze.json')
            verify({str(directory/'sources'/p):h for p,h in meta['source_sha256'].items()})
            archived.add(directory)
        r=dict(item,candidate_side=c['candidate_side'],outcome=row['outcome'],
            hp_a_first=row['hp_candidate_first'],rounds=row['rounds'],
            canonical_replay_sha256=row['canonical_replay_sha256'],
            decision_seconds_a_first=row['decision_seconds_candidate_first'])
        cases.append(r);groups[(a,b)].append(r)
    matrix=[[None]*5 for _ in ORDER];edges=[]
    for (a,b),pair in groups.items():
        pair.sort(key=lambda x:x['candidate_side'])
        assert [r['candidate_side'] for r in pair]==[0,1]
        for key in ('outcome','hp_a_first','rounds','canonical_replay_sha256'):
            assert pair[0][key]==pair[1][key],(a,b,key)
        value={'W':1,'D':0,'L':-1}[pair[0]['outcome']]
        i,j=ORDER.index(a),ORDER.index(b)
        assert matrix[i][j] is None and matrix[j][i] is None
        if i==j:assert value==0
        matrix[i][j]=value;matrix[j][i]=-value
        edges.append(dict(a=a,b=b,value=value,hp_a_first=pair[0]['hp_a_first'],
                          rounds=pair[0]['rounds'],reused=pair[0]['reused']))
    assert len(edges)==15 and all(v is not None for row in matrix for v in row)
    assert fresh_new==sum(2*c['rounds'] for c in cases if not c['reused'])
    old_weights=[Fraction(1,3)]*3+[Fraction(0)]*2
    old_payoffs=[sum(old_weights[i]*matrix[i][j] for i in range(5)) for j in range(5)]
    h1=all(v>=0 for v in old_payoffs[3:])
    gaps=[matrix[3][j]-matrix[2][j] for j in range(5)]
    h2=min(gaps)>=0 and max(gaps)>0
    certificate=exact_certificate(matrix)
    stamp=datetime.now(timezone.utc).isoformat()
    table=['| Row policy | '+' | '.join(ORDER)+' |','|---|'+'---:|'*5]
    table += ['| '+a+' | '+' | '.join(map(str,row))+' |' for a,row in zip(ORDER,matrix)]
    detail=['| Pair | Outcome | Final HP | Round | Source |','|---|---|---|---:|---|']
    for edge in edges:
        detail.append(f'| {edge["a"]} vs {edge["b"]} | '+{1:'W',0:'D',-1:'L'}[edge['value']]+f' | {edge["hp_a_first"][0]}:{edge["hp_a_first"][1]} | {edge["rounds"]} | '+('Reused' if edge['reused'] else 'New')+' |')
    lines=['# Five fixed policies after two counter revisions','',f'Checked {stamp}.','',
        f'H1, the original uniform B/C/D mixture remains nonnegative against G and H, is {"CONFIRMED" if h1 else "REFUTED"}. Its exact payoff against G is {old_payoffs[3]}, and against H is {old_payoffs[4]}. H2, G weakly improves on D in every column with at least one strict improvement, is {"CONFIRMED" if h2 else "REFUTED"}.','',
        'B is frozen best_v9e, C is the round-three tier2 attacker retaining its original private D model, D is the adaptive Fortress38 continuation, G is early-wall guard00 and H is the HP-triggered grower with lead_from=8 and deadline=12. This is a deliberately extended development table, not an unseen opponent sample.','']+table+['',
        'Every cell uses the original engine outcome: +1 win, 0 draw, -1 loss. All fifteen pairings, including five self-play cases, have two measured physical assignments. Ten games are new and twenty are explicitly reused. Each assignment pair has the same canonical history.','']+detail+['']
    if certificate:
        lines += ['Exact rational arithmetic certifies the following optimal mixture for this five-policy table: '+', '.join(f'{name}={weight}' for name,weight in zip(ORDER,certificate['weights']))+'. Its expected payoffs against B,C,D,G,H are '+', '.join(certificate['column_payoffs'])+'. The finite value is exactly zero. This does not certify play against a sixth policy or a changed start.']
    else:
        lines += ['The exact search did not produce a feasible certificate. No optimal-mixture conclusion is made.']
    lines += ['',f'All {fresh_new} new action-generating decisions are independently regenerated, with legal actions, unchanged observations, matching original-engine replays and verified source/data archives. All old receipts and their input hashes are rechecked. No game or audit failure is omitted. The complete receipt records policy specifications, every result path, HP, round and actual decision timings.','',
        'Reproduce the five extended-counter-game manifests with run_data_development, audit_development_strict, replay_audit, audit_data_archives and check_fixed_game_histories, then run publish_extended_counter_game. Restore archived old inputs before rechecking their receipts. The exact fraction calculation is local and deterministic. A hidden mixture draw would occur before a match; it cannot be revealed to an opponent before that opponent selects its policy.','']
    output=AREA/'RESULTS.md'
    with output.open('x') as f:f.write('\n'.join(lines))
    for p in (output,AREA/'PROOF.md',Path(__file__).relative_to(Path.cwd())):inputs[str(p)]=digest(p)
    result=dict(time_utc=stamp,all_passed=True,new_games=10,reused_games=20,fresh_new_decisions=fresh_new,
        policies=d['policies'],order=ORDER,payoff=matrix,old_mixture_payoffs=[str(v) for v in old_payoffs],
        old_mixture_retains_guarantee=h1,guard_weakly_dominates_delegate=h2,guard_minus_delegate=gaps,
        certificate=certificate,cases=cases,input_sha256=inputs)
    with (AREA/'verification/full_games.json').open('x') as f:json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {stamp}: Five-policy extension complete\n\nClaim and verdict: H1 old uniform mixture guarantee {"CONFIRMED" if h1 else "REFUTED"}; H2 G weakly dominates D {"CONFIRMED" if h2 else "REFUTED"}. Old mixture payoffs against G/H: {old_payoffs[3]}, {old_payoffs[4]}. Ten new and twenty reused games, all fifteen assignment pairs identical, {fresh_new} fresh new decisions checked. '+('Exact finite maximin weights in B,C,D,G,H order: '+str(certificate['weights'])+'. ' if certificate else 'No mixture certificate found. ')+f'All claims are restricted to this fixed development table: {output}.\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('cases','input_sha256','policies')}))


if __name__=='__main__':main()

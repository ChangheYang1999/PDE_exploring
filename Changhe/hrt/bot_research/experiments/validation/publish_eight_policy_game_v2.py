"""Assemble the predeclared eight-policy game and check rational certificates."""
from collections import defaultdict
from datetime import datetime,timezone
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import gzip,hashlib,json,traceback
from bot_research.experiments.validation.artifact_io import atomic_json,public_diagnostic
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.publish_extended_counter_game import exact_certificate,norm
E=Path('bot_research/experiments/validation');R=Path('bot_research/runs/validation');A=E/'analysis/eight_policy_game'
ORDER=['B','C','D','G','H','I','J','L']

def main():
    inputs={};compressed={}
    def checked_bytes(name,expected=None):
        p=Path(name)
        if p.is_file():data=p.read_bytes()
        else:
            q=Path(str(p)+'.gz');stored=q.read_bytes();data=gzip.decompress(stored)
            compressed[str(p)]=dict(archive=str(q),archive_sha256=hashlib.sha256(stored).hexdigest())
        sha=hashlib.sha256(data).hexdigest()
        if expected is not None:assert sha==expected,str(p)
        inputs[str(p)]=sha;return data
    def read(p):return json.loads(checked_bytes(p))
    def verify(mapping):
        for p,h in mapping.items():checked_bytes(p,h)
    declaration=read(E/'eight-policy-analysis-002.json');verify(declaration['input_sha256'])
    old=read(E/'analysis/seven_policy_game/verification/full_games.json');assert old['all_passed'] and old['order']==ORDER[:7];verify(old['input_sha256'])
    repair=read(E/'analysis/wall_signal_repair/verification/full_games.json');assert repair['all_passed'] and len(repair['rows'])==6;verify(repair['input_sha256'])
    components=read(A/'verification/arithmetic_components.json');assert components['all_passed'] and len(components['cases'])==3;verify(components['input_sha256'])
    arithmetic=read(E/'eight-policy-arithmetic-001.json');verify(arithmetic['input_sha256'])
    campaign='eight-policy-extension-001';root=R/campaign;m=read(E/(campaign+'.json'));verify(m['input_sha256'])
    policies=read(E/'shared-prefix-campaigns-001.json')['policies'];policies['L']=m['candidates'][0]
    audits={k:read(R/(campaign+'-'+k+'.json')) for k in ('strict','replay','data','fresh')}
    s=audits['strict'];assert s['valid_conditions']==s['expected_conditions']==10 and s['attempt_counts']=={'valid':10} and not s['unresolved'] and not s['repeat_disagreements']
    assert audits['replay']['all_passed'] and audits['replay']['count']==10 and audits['data']['all_passed']
    fresh=audits['fresh'];assert fresh['games']==10 and all(fresh[k] for k in ('all_passed','all_replayed','all_actions_legal','all_observations_unchanged'));verify(fresh['input_sha256'])
    freeze=read(root/'freeze.json');verify({str(root/'sources'/p):h for p,h in freeze['source_sha256'].items()})
    cases=[dict(c,reused=True) for c in old['cases']]
    def append(r,reused):
        c=r['condition'];assert norm(c['candidate_spec'])==norm(policies['L']['spec'])
        aliases=[name for name in ORDER if norm(policies[name]['spec'])==norm(c['opponent_spec'])]
        assert len(aliases)==1, (c['opponent_id'], aliases)
        cases.append(dict(a='L',b=aliases[0],result=r['result_path'],candidate_side=c['candidate_side'],outcome=r['outcome'],hp_a_first=r['hp_candidate_first'],rounds=r['rounds'],canonical_replay_sha256=r['canonical_replay_sha256'],reused=reused))
    for row in repair['rows']:append(row['record'],True)
    for job in read(root/'jobs.json'):append(checked_row(str(root/'results'/(job['id']+'.json')),inputs),False)
    assert len(cases)==72 and len({c['result'] for c in cases})==72
    assert sum(not c['reused'] for c in cases)==10 and fresh['checked_calls']==2*sum(c['rounds'] for c in cases if not c['reused'])
    groups=defaultdict(list)
    for c in cases:assert c['result'] in inputs;groups[(c['a'],c['b'])].append(c)
    matrix=[[None]*8 for _ in ORDER]
    for (a,b),pair in groups.items():
        assert len(pair)==2 and {c['candidate_side'] for c in pair}=={0,1}
        for k in ('outcome','hp_a_first','rounds','canonical_replay_sha256'):assert pair[0][k]==pair[1][k],(a,b,k)
        i,j=ORDER.index(a),ORDER.index(b);assert matrix[i][j] is None and matrix[j][i] is None
        v={'W':1,'D':0,'L':-1}[pair[0]['outcome']]
        if i==j:assert v==0
        matrix[i][j],matrix[j][i]=v,-v
    assert len(groups)==36 and all(v is not None for row in matrix for v in row)
    assert [row[:7] for row in matrix[:7]]==old['payoff']
    certificate=exact_certificate(matrix);assert certificate is not None
    weights=list(map(Fraction,certificate['weights']));assert len(weights)==8 and min(weights)>=0 and sum(weights)==1
    column=[sum(weights[i]*matrix[i][j] for i in range(8)) for j in range(8)];assert min(column)>=0
    assert [str(x) for x in column]==certificate['column_payoffs']
    assert all(sum(matrix[i][j]*weights[j] for j in range(8))<=0 for i in range(8))
    previous=list(map(Fraction,old['certificate']['weights']))+[Fraction(0)]
    prior=[sum(previous[i]*matrix[i][j] for i in range(8)) for j in range(8)]
    h1=min(matrix[-1])>=0;h2=prior[-1]>=0
    pure=[ORDER[i] for i in range(8) if min(matrix[i])>=0]
    cycles=[[ORDER[i],ORDER[j],ORDER[k]] for i,j,k in permutations(range(8),3) if i<j and i<k and matrix[i][j]==matrix[j][k]==matrix[k][i]==1]
    stamp=datetime.now(timezone.utc).isoformat()
    lines=['# A fixed eight-policy table after the signal repair','',f'Checked {stamp}.','','H1 L is nonnegative against every included policy: '+('CONFIRMED' if h1 else 'REFUTED')+'.','H2 the old B/H/J mixture remains nonnegative against L: '+('CONFIRMED' if h2 else 'REFUTED')+f'. Its payoff against L is {prior[-1]}.','','B is frozen best_v9e, C is the private-D timing attacker, D the adaptive Fortress38 delegate, G the early-wall guard, H the HP-triggered grower, I the private-H timing attacker, J the common-prefix response selector, and L the repaired twenty-wall signal attacker. Sources and exact parameters are pinned in the parent declarations. B is a frozen earlier nominee, not a claim about whichever bot is finally installed.','','| Row | '+' | '.join(ORDER)+' |','|---|'+'---:|'*8]
    lines+=['| '+name+' | '+' | '.join(map(str,row))+' |' for name,row in zip(ORDER,matrix)]
    lines+=['',f'This table contains ten new games and 62 explicitly reused records, for 72 games and 36 assignment pairs. Every pair has identical normalized histories. The ten new games pass strict accounting, original-engine replay, source/data checks and {fresh["checked_calls"]} fresh external decisions. The reused parent receipts and their inputs are rechecked, including exact decompression of archived replays. No extra games are counted from arithmetic verification.','','An exact optimal mixture in B,C,D,G,H,I,J,L order is '+str(certificate['weights'])+'. Its column payoffs are '+str(certificate['column_payoffs'])+'. The finite value is zero. Exact normalization, nonnegativity, column lower bounds and skew-symmetric opposing upper bounds are independently checked after the solver proposes the vector. The three eight-dimensional fixtures also pass.','','Pure policies nonnegative against every column: '+(', '.join(pure) if pure else 'none')+'. Directed three-policy cycles: '+'; '.join(' > '.join(c+[c[0]]) for c in cycles)+'.','','The old certificate remains valid on its original seven columns. Any failure on L limits its extension, not that earlier restricted proof. This new certificate is likewise limited to the eight fixed policies, measured standard start and checked histories. It does not prove a full-game equilibrium, robustness to changed starts or invariant behavior under different clock-limited search outcomes. The extension was selected after development results and is not held out. Pool D is unchanged.','']
    output=A/'RESULTS.md'
    with output.open('x') as f:f.write('\n'.join(lines))
    checked_bytes(output)
    result=dict(time_utc=stamp,all_passed=True,new_games=10,reused_games=62,order=ORDER,payoff=matrix,h1=h1,h2=h2,prior_mixture_payoffs=[str(v) for v in prior],certificate=certificate,pure_nonnegative_policies=pure,directed_three_cycles=cycles,fresh_calls=fresh['checked_calls'],cases=cases,input_sha256=inputs,compressed_inputs=compressed)
    atomic_json(A/'verification/full_games.json',result,exclusive=True)
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {stamp}: Eight-policy extension complete\n\nH1 L nonnegative everywhere: '+('CONFIRMED' if h1 else 'REFUTED')+'; H2 old B/H/J mixture nonnegative against L: '+('CONFIRMED' if h2 else 'REFUTED')+f' (payoff {prior[-1]}). Ten new games, 62 reused records, 36 matching assignment pairs, {fresh["checked_calls"]} fresh external calls. Exact restricted value-zero certificate CONFIRMED with weights {certificate["weights"]}. See experiments/validation/analysis/eight_policy_game/RESULTS.md. This is selected finite-table evidence, not held-out or unrestricted strength.\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('cases','input_sha256','compressed_inputs')}),flush=True)
if __name__=='__main__':
    try:main()
    except Exception:
        print(public_diagnostic(traceback.format_exc()),flush=True);raise SystemExit(1)

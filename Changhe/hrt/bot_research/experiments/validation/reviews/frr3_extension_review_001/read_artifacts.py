"""Read retained JSON/source only; no project imports, policy calls or Engine execution."""
import ast
import collections
import gzip
import hashlib
import json
import re
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

OUT = Path('bot_research/experiments/validation/reviews/frr3_extension_review_001')
started = datetime.now(timezone.utc).isoformat()
def sha(raw): return hashlib.sha256(raw).hexdigest()
def canon(x): return json.dumps(x, sort_keys=True, separators=(',', ':')).encode()
pins = {}
def read(path):
    p = Path(path)
    raw = p.read_bytes()
    pins[p.as_posix()] = sha(raw)
    return raw

def module_file(name):
    base = Path(*name.split('.'))
    return next((p for p in (base.with_suffix('.py'), base / '__init__.py') if p.is_file()), None)
def closure(spec):
    seen = {}
    todo = [spec.partition(':')[0]]
    while todo:
        name = todo.pop()
        if name in seen or not name.startswith('bot_research'): continue
        path = module_file(name)
        if path is None: continue
        seen[name] = path
        parts = name.split('.')
        todo.extend('.'.join(parts[:i]) for i in range(1, len(parts)))
        package = name if path.name == '__init__.py' else '.'.join(parts[:-1])
        for node in ast.walk(ast.parse(read(path))):
            if isinstance(node, ast.Import): todo.extend(a.name for a in node.names)
            elif isinstance(node, ast.ImportFrom):
                parts = package.split('.')
                target = '.'.join(parts[:len(parts)-node.level+1] + ([node.module] if node.module else [])) if node.level else node.module or ''
                todo.append(target)
                todo.extend(target + '.' + a.name for a in node.names)
    return set(seen.values()) | set(Path('bot_research/harness').glob('*.py'))

report = read('bot_research/reports/REPORT.md')
(OUT / 'REPORT.snapshot.md').write_bytes(report)
frr1 = json.loads(read('bot_research/experiments/validation/analysis/frr1_equilibrium/verification/independent_audit_001.json'))
assert sha(read('bot_research/runs/lead/frr1/results.jsonl')) == frr1['input_hashes']['bot_research/runs/lead/frr1/results.jsonl']
read('bot_research/experiments/validation/analysis/frr1_equilibrium/PROOF.md')
read('bot_research/experiments/validation/reviews/frr1-equilibrium-review-001.md')
names = frr1['names']
specs = [frr1['policy_entries'][n]['spec'] for n in names]
v46 = 'bot_research.bots.defense.frozen.v46.fortress:@make'
rows = [json.loads(s) for s in read('bot_research/runs/lead/frr3/results.jsonl').splitlines()]
expected = [(i, s, (v46, spec) if s == 0 else (spec, v46)) for i, spec in enumerate(specs) for s in (0, 1)]
assert [(r['pair'], r['candidate_side'], (r['spec_a'], r['spec_b'])) for r in rows] == expected
balanced = json.loads(read('td_game/balanced.json'))
initial = dict(hp=800, gold=100, n_factories=0, n_turrets=0, n_walls=0, length_path=22, buildings=[], roster=[])
loaded = {}
log_hashes = {}
record_count = 0
event_counts = collections.Counter()
raw_timing_count = 0
raw_max = collections.defaultdict(float)
summaries = []
for r in rows:
    assert r['scenario'] is None and r['scenario_errors'] == [[], []]
    assert r['error'] is None and r['source_changed'] is False and r['experiment'] == 'frr3'
    assert all(p['n_rejected'] == 0 and not p['rejected'] and not p['bot_errors'] for p in r['players'])
    for path, h in r['sources'].items():
        assert loaded.setdefault(path, h) == h and sha(read(path)) == h
    raw = read(r['log']); log_hashes[r['log']] = sha(raw)
    recs = [json.loads(s) for s in raw.splitlines()]; record_count += len(recs)
    assert [(x['round'], x['player']) for x in recs] == [(q,s) for q in range(r['rounds']+1) for s in (0,1)]
    assert all('result' not in x for x in recs[:-2])
    for side,k in enumerate('ab'):
        first,last = recs[side], recs[-2+side]
        m = first['match']
        assert m == recs[1-side]['match']
        assert m['bots'] == m['research_specs'] == [r['spec_a'],r['spec_b']]
        assert m['research_scenario'] is None and m['research_metadata'] == r['metadata'] == {'pair':r['pair'],'candidate_side':r['candidate_side']}
        assert m['rules'] == balanced
        assert m['action_order'] == 'A[0], B[0], A[1], B[1], ...'
        assert m['neighbor_order'] == ['right','down','left','up']
        assert m['tick_order'] == ['spawn','move older minions','base hits','turrets','remove dead']
        assert first['event'] == [{'kind':'initial'}]
        assert {k:v for k,v in first['snapshot'].items() if k != 'name'} == initial
        assert all(x['snapshot']['name'] == r['spec_'+k] for x in recs if x['player']==side)
        assert last['result'] == {'winner':r['winner'],'reason':r['reason']}
        assert last['snapshot']['hp'] == r['hp_'+k]
        assert all(last['snapshot'][f] == r['players'][side][f] for f in ('name','gold','n_factories','n_turrets','n_walls','length_path'))
    assert r['hp_diff_a'] == r['hp_a']-r['hp_b']
    a,b = r['hp_a'],r['hp_b']
    expected_winner = None if (a<=0 and b<=0) or a==b else (0 if a>b else 1)
    assert r['winner'] == expected_winner
    assert (r['rounds']==50 and r['reason']=='round_limit') if min(a,b)>0 else r['reason'] in ('base_destroyed','both_bases_destroyed')
    for x in recs:
        for event in x['event']:
            event_counts[event['kind']] += 1
            assert event['kind'] != 'bot_error'
            if event['kind']=='action': assert event['accepted'] is True
            if event['kind']=='decision':
                raw_timing_count += 1
                raw_max[r['spec_'+'ab'[x['player']]]] = max(raw_max[r['spec_'+'ab'[x['player']]]], event.get('seconds',0))
    side=r['candidate_side']; opp=names[r['pair']]
    summaries.append({'opponent':opp,'v46_side':side,'v46_hp':r['hp_'+'ab'[side]],'opponent_hp':r['hp_'+'ab'[1-side]],'rounds':r['rounds'],'v46_payoff':0 if r['winner'] is None else 1 if r['winner']==side else -1,'v46_max_call_seconds':r['decide_max_seconds'][side],'opponent_max_call_seconds':r['decide_max_seconds'][1-side],'game_wall_seconds':r['wall_seconds'],'log':r['log']})
assert set(log_hashes) == {p.as_posix() for p in Path('bot_research/runs/lead/frr3/logs').iterdir()}
versions={}; static={}
for spec in specs+[v46]:
    smap={p.as_posix():sha(read(p)) for p in sorted(closure(spec))}; static.update(smap)
    digest=sha(''.join(p+'\0'+h+'\n' for p,h in smap.items()).encode())
    versions[spec]=digest
    assert {r['version_'+k] for r in rows for k in 'ab' if r['spec_'+k]==spec}=={digest}
    assert {r['hash_'+k] for r in rows for k in 'ab' if r['spec_'+k]==spec}=={sha(read(module_file(spec.partition(':')[0])))}
M=frr1['matrix_row_payoff_WDL']; vrow=[]
for i in range(10):
    pair=summaries[2*i:2*i+2]
    assert pair[0]['v46_payoff']==pair[1]['v46_payoff']
    assert pair[0]['v46_hp']-pair[0]['opponent_hp']==pair[1]['v46_hp']-pair[1]['opponent_hp']
    vrow.append(pair[0]['v46_payoff'])
assert vrow==M[names.index('v41')]
N=[M[i]+[-vrow[i]] for i in range(10)]+[vrow+[0]]
assert N[names.index('v41')]==N[10] and all(N[i][j]==-N[j][i] for i in range(11) for j in range(11))
certs={}
for arm in ('AS1C','best_v9f','P5TNUBM'):
    p=[Fraction(1,3) if n in ('g1','guard00',arm) else Fraction(0) for n in names+['v46']]
    value=[sum(p[i]*N[i][j] for i in range(11)) for j in range(11)]
    assert min(value)==0 and value[-1]>=Fraction(2,3)
    certs[arm]={'mixture':list(map(str,p)),'column_payoffs':list(map(str,value))}
for path in ('bot_research/experiments/lead/queue_h17.sh','bot_research/experiments/lead/rr_specs.sh','bot_research/runs/lead/frr3/summary.md','bot_research/runs/lead/frr3.out','bot_research/runs/lead/queue_h17.log','bot_research/harness/tournament.py','td_game/runner.py','bot_research/experiments/validation/analysis/immune_runtime_shortcut/RESULTS.md','bot_research/experiments/validation/analysis/immune_shortcut_followup/RESULTS.md'):
    read(path)
q=Path('bot_research/runs/lead/queue_h17.log').read_text()
assert 'start frr3 2026-10-31T22:08:43Z' in q and 'end frr3 exit 0 2026-10-31T22:36:52Z' in q
out=Path('bot_research/runs/lead/frr3.out').read_text().splitlines()
assert len(out)==22 and [int(re.match(r'\[(\d+)/20\]',s).group(1)) for s in out[1:-1]]==list(range(1,21))
# Source and retained summaries for the earlier x215 reproduction claims; no log replay.
x215=[json.loads(s) for s in read('bot_research/runs/defense/x215_v46_lead/results.jsonl').splitlines()]
xstd=[r for r in x215 if r['scenario'] is None]
xbrief=[]
for r in xstd:
    for path,h in r['sources'].items(): assert sha(read(path))==h
    xbrief.append({k:r[k] for k in ('spec_a','spec_b','hp_a','hp_b','rounds','hash_a','hash_b','decide_max_seconds','log')})
# Rules may be embedded, but historical transitive JSON witness identities are not established by the Python digest.
assert all(sha(Path(p).read_bytes())==h for p,h in {**loaded,**static}.items())
result={'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),'model':'GPT-6 Astra','report_snapshot_sha256':sha(report),'input_sha256':pins,'loaded_source_sha256':loaded,'static_source_sha256':static,'recorded_versions':versions,'games':20,'records':record_count,'event_counts':dict(event_counts),'raw_decision_event_count':raw_timing_count,'raw_decision_event_max':dict(raw_max),'log_sha256':log_hashes,'self_play_games':0,'diagonal':'all eleven entries imposed zero; no v46 self-play measured','v46_row_on_ten_frr1_columns':vrow,'matrix':N,'vertex_certificates':certs,'v46_outcomes':dict(collections.Counter(x['v46_payoff'] for x in summaries)),'games_by_physical_seat':summaries,'x215_standard_summary_rows':xbrief,'policy_imports_constructors_decisions_games_engine_replays':0,'limits':['Retained JSON/source inspection only, no Engine replay or fresh policy reproduction.','Python source digests do not authenticate historical transitive runtime JSON witnesses.','No independent durable process attempt journal; erased attempts and transient edits are not excluded.','Whole-execution load independence not established.']}
(OUT/'audit.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:result[k] for k in ('finished_utc','report_snapshot_sha256','games','records','event_counts','raw_decision_event_count','v46_outcomes')},indent=2))
print(json.dumps({'loaded_sources':len(loaded),'static_sources':len(static),'combined':len(set(loaded)|set(static)),'receipt_sha256':sha((OUT/'audit.json').read_bytes()),'games':summaries,'x215':xbrief},indent=2))

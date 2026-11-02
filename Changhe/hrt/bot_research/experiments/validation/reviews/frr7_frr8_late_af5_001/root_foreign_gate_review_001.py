"""Independent archive, source and accepted-record check; no project imports."""
import ast
from collections import Counter
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path

BASE = Path('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001')
SUB = BASE / 'foreign_attack_control_flow_001'
OUT = BASE / 'root_foreign_gate_review_001.json'
def sha(b): return hashlib.sha256(b).hexdigest()
def now(): return datetime.now(timezone.utc).isoformat()
started = now()
assert not OUT.exists()
raw_seal = (SUB/'seal.json').read_bytes()
assert sha(raw_seal) == '69c673713641361e04ec92a2a5e48bf259cc7792d3a56d08941c3c7b2c3aceb2'
seal = json.loads(raw_seal)
assert not seal['errors']
for rel, e in seal['outputs'].items():
    b = (SUB/rel).read_bytes()
    assert len(b) == e['bytes'] and sha(b) == e['sha256'], rel
E = json.loads((SUB/'EVIDENCE.json').read_bytes())
assert E['audit_completed'] and not E['errors']
inputs = {}
archive_count = 0
snapshot_differences = []
for name, e in E['input_manifest'].items():
    if 'archive' in e:
        z = (SUB/e['archive']).read_bytes()
        assert sha(z) == e['archive_sha256'] and len(z) == e['archive_bytes'], name
        b = gzip.decompress(z)
        archive_count += 1
    else:
        b = Path(name).read_bytes()
    assert sha(b) == e['sha256'] and len(b) == e['bytes'], name
    inputs[name] = b
    if Path(name).read_bytes() != b:
        assert name == 'bot_research/notes/economy.md', name
        snapshot_differences.append(name)
for name, e in E['prior_archive_edges'].items():
    z = (BASE/e['archive']).read_bytes()
    assert sha(z) == e['archive_sha256'] and len(z) == e['archive_bytes'], name
    b = gzip.decompress(z)
    assert sha(b) == e['sha256'] and len(b) == e['bytes'], name
    assert b == inputs[name], name
    archive_count += 1
prior = json.loads(inputs[str(BASE/'seal_001.json')])
for rel, e in prior['outputs'].items():
    b = (BASE/rel).read_bytes()
    assert sha(b) == e['sha256'] and len(b) == e['bytes'], rel

source_path = 'bot_research/bots/economy/frozen/v29/econ29.py'
source = inputs[source_path].decode()
assert sha(inputs[source_path]) == '0c71ec9bc7b772313cc302ed1296b586cdcf98ea3bc2cdf1044e60f5220c855c'
tree = ast.parse(source)
make = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'make')
decide = next(n for n in make.body if isinstance(n, ast.FunctionDef) and n.name == 'decide')
attack = next(n for n in decide.body if isinstance(n, ast.FunctionDef) and n.name == 'attack')
assert ast.unparse(attack.body[0]) == 'if hold:\n    return'
defs = {a.arg: ast.literal_eval(d) for a,d in zip(make.args.args[-len(make.args.defaults):],make.args.defaults)}
parameters = {}
for name, a in [('AF5',5),('G1',7)]:
    sp = E['full_specs'][name]
    params = {**defs, **{k: json.loads(v) for k,v in (part.split('=',1) for part in sp.partition('?')[2].split('&'))}}
    assert params == E['resolved_parameters'][name]
    assert params['attack_from'] == a
    for k, v in {'foreign_attack_from':11,'foreign_open':True,'hold_income':None,'lift_idle':None,'finish':'opt','doom':'next','none_from':4,'none_first':True,'none_frac':1.0}.items():
        assert params[k] == v
    parameters[name] = params
branches = {}
for name in ['finish','doom']:
    node = next(n for n in decide.body if isinstance(n,ast.If) and ast.unparse(n.test).startswith(name+' and'))
    assert not any(isinstance(n,ast.Name) and n.id == 'hold' for n in ast.walk(node))
    assert any(isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id == 'add' for n in ast.walk(node))
    branches[name] = {'line':node.lineno,'test':ast.unparse(node.test)}
op = next(n for n in decide.body if isinstance(n,ast.If) and 'none_first' in ast.unparse(n.test))
assert ast.unparse(op.body[0]) == 'attack(none_frac)'
assert ast.unparse(op.body[1]) == 'attacked = True'
assert branches['finish']['line'] < op.lineno < branches['doom']['line']
assert ast.unparse(decide.body[-1]) == 'return actions'

histories = E['retained_history_scan']
assert Counter(h['campaign'] for h in histories) == {'scnaf5':17,'frr7':28}
assert len({h['log'] for h in histories}) == 45
checked_rounds = total_records = 0
for h in histories:
    b = inputs[h['log']]
    assert sha(b) == h['sha256']
    records = [json.loads(line) for line in b.splitlines()]
    assert len(records) == h['records']
    total_records += len(records)
    by = {(r['round'],r['player']):r for r in records}
    assert len(by) == len(records)
    for side in [0,1]:
        init = by[(0,side)]['snapshot']
        assert all(init[k] == 0 for k in ['n_walls','n_turrets','n_factories'])
        assert not init['roster']
    rounds = range(h['scripted_rounds']+1,h['through_round']+1)
    for rnd in rounds:
        r = by[(rnd,h['side'])]
        assert not any(e['kind']=='action' and e['accepted'] and e['action']['op']=='buy_minion' for e in r['event'])
        checked_rounds += 1
assert not E['postscript_pre11_purchases']
assert len(E['not_retained_rows']) == 103
assert all(x['campaign']=='scnaf5' for x in E['not_retained_rows'])
result = {'schema':'root-foreign-gate-review-001','started_utc':started,'completed_utc':now(),
 'reviewer_model':'GPT-6 Astra','verdict':'CONFIRMED','seal_sha256':sha(raw_seal),
 'evidence_sha256':sha((SUB/'EVIDENCE.json').read_bytes()),'source_sha256':sha(inputs[source_path]),
 'sealed_outputs_checked':len(seal['outputs']),'inputs_checked':len(inputs),'archive_edges_checked':archive_count,
 'original_sealed_outputs_checked':len(prior['outputs']),'mutable_snapshot_differences':snapshot_differences,
 'source_branches':branches,'retained_histories':45,'retained_records':total_records,
 'candidate_rounds_after_script_and_before_11_checked':checked_rounds,'accepted_minion_purchases_in_interval':0,
 'scope':'Independent static source/AST and retained JSON checks. Missing shared guard is a control-flow fact, not a legal-game reachability witness. 103 scnaf5 histories unavailable. No policy, engine, replay, game or existing checker executed.',
 'manual_reading':'Root read complete new proof, review and checker, and the relevant frozen decision body; verified that add retains minion actions and no final hold filter removes them.',
 'script_sha256':sha(Path(__file__).read_bytes())}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
print('RECEIPT_SHA256',sha(OUT.read_bytes()))

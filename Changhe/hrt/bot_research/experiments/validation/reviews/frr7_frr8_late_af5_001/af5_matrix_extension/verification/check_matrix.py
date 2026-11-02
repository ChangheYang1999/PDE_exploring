"""Authenticate retained rows and exact rational certificates. Standard library only.

No imports, constructors, decisions, games, simulations or replays from the project.
The informal proof was written first. This check does not replace its necessity proof.
"""
import gzip
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path

OUT = Path('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001')
TOPIC = OUT / 'af5_matrix_extension'
DEST = TOPIC / 'verification'
UTC = lambda: datetime.now(timezone.utc).isoformat()
sha = lambda b: hashlib.sha256(b).hexdigest()
started = UTC()
files = {}
archive_edges = []
current_sources = {}
errors = []

def require(ok, text):
    if not ok:
        raise ValueError(text)

def archive(name, data, provenance='current physical bytes'):
    h = sha(data)
    q = OUT / 'inputs' / (h + '.gz')
    if not q.exists():
        with q.open('xb') as f:
            f.write(gzip.compress(data, compresslevel=6, mtime=0))
    z = q.read_bytes()
    require(gzip.decompress(z) == data, 'archive round trip ' + name)
    item = {'path': name, 'sha256': h, 'bytes': len(data),
            'archive': q.relative_to(OUT).as_posix(), 'archive_sha256': sha(z),
            'archive_bytes': len(z), 'provenance': provenance}
    key = name + '@' + h
    files[key] = item
    return data

def retain(name, expected=None):
    data = Path(name).read_bytes()
    require(expected is None or sha(data) == expected, 'current input identity ' + name)
    return archive(name, data)

def js(name, expected=None):
    return json.loads(retain(name, expected))

def save(name, value):
    p = DEST / name
    with p.open('x') as f:
        json.dump(value, f, indent=2, sort_keys=True)
        f.write('\n')
    return {'path': p.as_posix(), 'sha256': sha(p.read_bytes()), 'bytes': p.stat().st_size}

proof = retain((TOPIC / 'PROOF.md').as_posix(), '2d82fbdb2c2fc1f91f0f09656ab07489c73f60dc6a758432fe9ee3453e5d0240')
proof_hash = sha(proof)
main_manifest_path = OUT / 'input_manifest_final_001.json'
main_manifest = js(main_manifest_path.as_posix())
main_audit = js((OUT / 'record_audit_final_001.json').as_posix(), '518a8593bea8e590ecfdec22ee5e4fc1bfa7d720e3b67aeed9fe7db0a05febc7')
require(not main_audit['raw_or_source_errors'], 'main retained record audit errors')
for key in ['frr5', 'frr8']:
    c = main_audit['campaigns'][key]
    require(c['complete_grid'] and not c['metadata_errors'], 'main complete grid ' + key)
specs = main_audit['specs']
names = ['BEST_V9E', 'BEST_V9F', 'AF2G', 'P5TNUBM', 'V41', 'V29', 'G1', 'GUARD00', 'TDEF', 'AS1C', 'AF5']
name_by_spec = {specs[n]: n for n in names + ['V46', 'V48']}
require(len(name_by_spec) == 13, 'distinct full specifications')
base_receipt_path = 'bot_research/experiments/validation/analysis/frr1_equilibrium/verification/independent_audit_001.json'
base_receipt = js(base_receipt_path, '118f08bc7d87f3ff536368a60c51e6879bf273c6bd7e5c431d56ad1a2fbbd08d')
retain('bot_research/experiments/validation/analysis/frr1_equilibrium/PROOF.md')
require(base_receipt['matches'] == 90 and base_receipt['all_current_source_identity_checks_passed'], 'base receipt status')
require(all(base_receipt[k] == 0 for k in ['bot_errors', 'rejected_actions', 'scenario_errors', 'source_changed_rows']), 'base receipt error accounting')
for name, h in base_receipt['log_hashes'].items():
    retain(name, h)
for kind in ['loaded_sources', 'static_digest_sources']:
    for name, h in base_receipt[kind].items():
        retain(name, h)
        current_sources[name] = h
# Current report/spec additions need not match historical report/spec hashes. The
# frozen base row bytes and original source/log identities are required exactly.
base_rows_bytes = retain('bot_research/runs/lead/frr1/results.jsonl', base_receipt['input_hashes']['bot_research/runs/lead/frr1/results.jsonl'])
parent = 'bot_research/experiments/validation/reviews/economy_final_gate_001/afrr-20261031T233750162131Z/'
afr = js(parent + 'inspection.json', '6659ba2e0bb9a8c7ac693b1898099a34b9c9d2899f66cb57deb1d63e9112aa43')
afm = js(parent + 'inputs.json', '00e25bf0757561eab6b8f36eed90b35a8a947e2df558de5acdc6f747fe1d49b8')
require(afr['audit_completed_without_findings'] and afr['afrr']['complete_condition_and_completion_evidence'], 'afrr audit status')
require(afr['candidate_spec'] == specs['AF5'], 'afrr exact AF5 spec')
require(all(x == 0 for x in afr['errors'].values()), 'afrr receipt errors')
af_archived = {}
for name, item in afm['inputs'].items():
    z = Path(item['snapshot']).read_bytes()
    b = gzip.decompress(z)
    require(sha(z) == item['gzip_sha256'] and sha(b) == item['sha256'] and len(b) == item['bytes'], 'afrr historical archive ' + name)
    archive(name, b, 'exact existing afrr input archive ' + item['snapshot'])
    af_archived[name] = b
    archive_edges.append({'path': name, 'archive': item['snapshot'], 'sha256': sha(b), 'compressed_sha256': sha(z), 'bytes': len(b)})
require(len(archive_edges) == afm['all_archives_verified'] == 94, 'afrr archive count')
afr_path = 'bot_research/runs/economy/afrr/results.jsonl'
require(afr_path in af_archived, 'afrr results archived')
retain(afr_path, sha(af_archived[afr_path]))
# The earlier fortress review supplies full raw accounting; here its source
# hashes, exact retained rows, and all archive edges are independently bound.
prior = 'bot_research/experiments/validation/reviews/frr5_frr6_final_fortress_001/'
for name in ['REVIEW.md', 'seal_001.json', 'root_review_001.json', 'finite_matrix_extension/PROOF.md',
             'finite_matrix_extension/verification/row_certificate.json']:
    retain(prior + name)
prior_m = js(prior + 'input_manifest_final.json', '0945e5be0a393ea06998db0dfec28ce1acc8983e256a2c8692695e9cf5c1c1d5')
# Row snapshots for frr3 and frr5 are immutable and fully preserved by the prior
# sealed review; do not require its evolving report to match today's report.
for run in ['frr3', 'frr5']:
    path = 'bot_research/runs/lead/' + run + '/results.jsonl'
    e = prior_m['files'][path]
    z = Path(prior + e['archive']).read_bytes()
    require(sha(z) == e['archive_sha256'], 'prior compressed row identity ' + run)
    b = gzip.decompress(z)
    require(sha(b) == e['sha256'] and len(b) == e['bytes'], 'prior row identity ' + run)
    retain(path, sha(b))

rowbytes = {'frr1': base_rows_bytes, 'afrr': af_archived[afr_path]}
for run in ['frr3', 'frr5', 'frr8']:
    path = 'bot_research/runs/lead/' + run + '/results.jsonl'
    rowbytes[run] = retain(path)
    if run in ['frr5', 'frr8']:
        require(sha(rowbytes[run]) == main_manifest['files'][path]['sha256'], 'main snapshot row identity ' + run)
rows = {run: [json.loads(x) for x in b.splitlines() if x.strip()] for run, b in rowbytes.items()}
conditions = []
edge = defaultdict(list)
missing_raw = []
for run, rr in rows.items():
    planned = 90 if run == 'frr1' else 2 if run == 'frr8' else 20
    require(len(rr) == planned, 'row count ' + run)
    seen = set()
    for line, row in enumerate(rr, 1):
        sa, sb = row['spec_a'], row['spec_b']
        require(sa in name_by_spec and sb in name_by_spec, 'full-spec membership ' + run)
        a, b = name_by_spec[sa], name_by_spec[sb]
        key = (sa, sb, row['scenario'])
        require(key not in seen, 'duplicate exact ordered condition ' + run)
        seen.add(key)
        require(row['scenario'] is None, 'standard start ' + run)
        require(row.get('error') is None and row['scenario_errors'] == [[], []] and row['source_changed'] is False, 'row errors ' + run)
        require(all(p['n_rejected'] == 0 and p['bot_errors'] == [] for p in row['players']), 'player errors ' + run)
        require(row['hp_diff_a'] == row['hp_a'] - row['hp_b'], 'HP difference ' + run)
        w = row['winner']
        require(w is None or w in [0, 1], 'winner domain')
        score = 0 if w is None else 1 if w == 0 else -1
        require(score == ((row['hp_diff_a'] > 0) - (row['hp_diff_a'] < 0)), 'terminal ordering ' + run)
        for name, h in row['sources'].items():
            require(name not in current_sources or current_sources[name] == h, 'inter-campaign source identity ' + name)
            retain(name, h)
            current_sources[name] = h
        for side in ['a', 'b']:
            path = row['spec_' + side].partition(':')[0].replace('.', '/') + '.py'
            require(sha(retain(path)) == row['hash_' + side], 'entry identity ' + run)
            require(row['version_' + side] == main_manifest['current_static_versions'][row['spec_' + side]]['version'], 'static version ' + run)
        retained = Path(row['log']).is_file()
        if retained:
            retain(row['log'])
        else:
            require(run == 'afrr' and w == row['candidate_side'], 'unexpected missing retained log')
            missing_raw.append({'run': run, 'line': line, 'path': row['log'], 'reason': 'afrr kept losses only'})
        item = {'run': run, 'line': line, 'spec_a': sa, 'spec_b': sb, 'name_a': a, 'name_b': b,
                'candidate_side': row['candidate_side'], 'scenario': None, 'winner': w,
                'row_player0_payoff': score, 'hp_a': row['hp_a'], 'hp_b': row['hp_b'],
                'rounds': row['rounds'], 'log': row['log'], 'raw_log_present': retained}
        conditions.append(item)
        edge[(a, b)].append((score, item))
        edge[(b, a)].append((-score, item))
    # Exact full-spec grid, not a count-only check.
    if run == 'frr1':
        expected = {(specs[a], specs[b], None) for a in names[:10] for b in names[:10] if a != b}
    else:
        candidate = {'afrr': 'AF5', 'frr3': 'V46', 'frr5': 'V48', 'frr8': 'AF5'}[run]
        opponents = ['V48'] if run == 'frr8' else names[:10]
        expected = {(specs[a], specs[b], None) for op in opponents for a, b in [(candidate, op), (op, candidate)]}
        require(all(r['spec_a' if r['candidate_side'] == 0 else 'spec_b'] == specs[candidate] for r in rr), 'candidate role ' + run)
    require(seen == expected, 'complete exact ordered grid ' + run)
require(len(missing_raw) == 0, 'all twenty afrr original raw histories are present')


def raw_require(ok, desc, errors):
    if not ok:
        errors.append(desc)
def canonical(rec):
    # Full events (including action order), all snapshot fields except policy name,
    # player/round/schema/result; identity metadata in match is independently checked.
    return {k:({kk:vv for kk,vv in v.items() if kk!='name'} if k=='snapshot' else v)
            for k,v in rec.items() if k!='match'}
def raw_check_afrr(row):
    errors=[];records=[json.loads(x) for x in retain(row['log']).splitlines()];turns={};stats=[]
    for rec in records:
        k=(rec['round'],rec['player']);raw_require(k not in turns,'duplicate turn '+str(k),errors);turns[k]=rec
        raw_require(rec.get('schema_version')==1,'schema',errors)
        raw_require(rec['snapshot']['name']==row['spec_a' if rec['player']==0 else 'spec_b'],'snapshot policy identity',errors)
    raw_require(set(turns)=={(r,s) for r in range(row['rounds']+1) for s in (0,1)},'complete turn grid',errors)
    for side in (0,1):
        initial=turns[(0,side)];match=initial['match']
        raw_require(match['rules']==rules,'exact balanced rules',errors)
        for field in ['bots','research_specs']:raw_require(match[field]==[row['spec_a'],row['spec_b']],'initial '+field,errors)
        raw_require(match['research_scenario']==row['scenario'],'initial scenario',errors)
        raw_require(match['research_metadata']==row['metadata'],'initial metadata',errors)
        accepted=Counter();rejected=Counter();spent=Counter();bot_errors=[];damage=hits=0;first=None
        for rnd in range(1,row['rounds']+1):
            rec=turns[(rnd,side)];prev=turns[(rnd-1,side)]['snapshot'];snap=rec['snapshot'];cost=0;new=Counter();combat=[];income=[]
            for e in rec['event']:
                if e['kind']=='action':
                    a=e['action'];op=a.get('op') if isinstance(a,dict) else None
                    if e['accepted']:
                        accepted[str(op)]+=1;new[str(op)]+=1;typ=a.get('type');c=e.get('cost',0);cost+=c
                        spent[op if op in ('buy_factory','build_wall') else str(op)+':'+str(typ)]+=c
                        ec={'buy_factory':rules['globals']['factory_cost'],'build_wall':rules['wall_cost']}.get(op)
                        if op=='buy_minion':ec=rules['minions'][typ]['cost']
                        if op=='build_turret':ec=rules['turrets'][typ]['cost']
                        raw_require(c==ec,'accepted cost '+str((rnd,side,op)),errors)
                    else:rejected[e.get('reason','?')]+=1
                elif e['kind']=='bot_error':bot_errors.append({'round':rnd,'reason':e.get('reason')})
                elif e['kind']=='combat':
                    combat.append(e);damage+=e['damage_dealt'];hits+=e['outgoing_hits']
                    if first is None and e['base_damage']>0:first=rnd
                elif e['kind']=='income':income.append(e)
            raw_require(len(combat)==1 and len(income)==1,'one combat/income '+str((rnd,side)),errors)
            if len(combat)!=1 or len(income)!=1:continue
            c=combat[0];i=income[0]
            raw_require(snap['hp']==prev['hp']-c['base_damage'],'HP accounting '+str((rnd,side)),errors)
            raw_require(snap['gold']==prev['gold']-cost+i['total'],'gold accounting '+str((rnd,side)),errors)
            raw_require(i['total']==i['path']+i['factories']+i['hits'],'income sum '+str((rnd,side)),errors)
            raw_require(i['path']==snap['length_path']*rules['globals']['path_income_per_step'],'path income '+str((rnd,side)),errors)
            raw_require(i['factories']==snap['n_factories']*rules['globals']['factory_income'],'factory income '+str((rnd,side)),errors)
            raw_require(i['hits']==c['outgoing_hits']*rules['globals']['base_hit_bounty'],'hit income '+str((rnd,side)),errors)
            for field,op in [('n_factories','buy_factory'),('n_turrets','build_turret'),('n_walls','build_wall')]:
                raw_require(snap[field]==prev[field]+new[op],field+' accounting '+str((rnd,side)),errors)
        snap=turns[(row['rounds'],side)]['snapshot'];value={k:snap.get(k) for k in ['name','hp','gold','n_factories','n_turrets','n_walls','length_path']}
        value.update(accepted=dict(accepted),rejected=dict(rejected),n_rejected=sum(rejected.values()),bot_errors=bot_errors,
                     damage_dealt=damage,hits=hits,spent=dict(spent),first_damage_taken_round=first)
        raw_require(value==row['players'][side],'complete player summary '+str(side),errors)
        raw_require(turns[(row['rounds'],side)].get('result')=={'winner':row['winner'],'reason':row['reason']},'terminal result '+str(side),errors)
        raw_require(snap['hp']==row['hp_a' if side==0 else 'hp_b'],'terminal HP '+str(side),errors);stats.append(value)
    for rnd in range(1,row['rounds']+1):
        evs=[turns[(rnd,s)]['event'] for s in (0,1)]
        orders=sorted(e['order'] for ee in evs for e in ee if e['kind']=='action')
        raw_require(orders==list(range(len(orders))),'interleaved action order '+str(rnd),errors)
        c=[[e for e in ee if e['kind']=='combat'] for ee in evs]
        if all(len(x)==1 for x in c):
            for s in (0,1):
                raw_require(c[s][0]['damage_dealt']==c[1-s][0]['base_damage'],'cross-player damage '+str((rnd,s)),errors)
                raw_require(c[s][0]['outgoing_hits']==c[1-s][0]['incoming_hits'],'cross-player hits '+str((rnd,s)),errors)
    raw_require(row['hp_diff_a']==row['hp_a']-row['hp_b'],'HP difference',errors)
    raw_require(row.get('error') is None,'row error',errors);raw_require(row.get('scenario_errors')==[[],[]],'discarded-call exception',errors)
    raw_require(not any(p['n_rejected'] or p['bot_errors'] for p in stats),'rejected/error count',errors)
    norm=[canonical(turns[k]) for k in sorted(turns)]
    digest=sha(json.dumps(norm,sort_keys=True,separators=(',',':')).encode())
    byround=[sha(json.dumps([canonical(turns[(r,s)]) for s in (0,1)],sort_keys=True,separators=(',',':')).encode()) for r in range(row['rounds']+1)]
    return {'errors':errors,'records':len(records),'accepted_total':sum(sum(p['accepted'].values()) for p in stats),
            'accepted_counts':dict(sum((Counter(p['accepted']) for p in stats),Counter())),
            'rejected_total':sum(p['n_rejected'] for p in stats),'bot_error_total':sum(len(p['bot_errors']) for p in stats),
            'canonical_sha256':digest,'canonical_round_sha256':byround}

rules_raw = json.loads(retain('td_game/balanced.json', base_receipt['input_hashes']['td_game/balanced.json']))
rules = {'label': rules_raw.get('label', 'custom rules'), 'demo': rules_raw.get('demo', False),
         'wall_cost': rules_raw['wall_cost'], 'wall_damage': rules_raw.get('wall_damage', 0),
         'wall_range': rules_raw.get('wall_range', 0.0), 'wall_cooldown': rules_raw.get('wall_cooldown', 1),
         'globals': {'width': 12, 'height': 12, 'spawn': [0, 0], 'base': [11, 11], 'initial_hp': 800,
                     'initial_gold': 100, 'max_rounds': 50, 'ticks_per_round': 250, 'roster_lifespan': 12,
                     'factory_cost': 20, 'factory_income': 15, 'path_income_per_step': 1, 'base_hit_bounty': 5},
         'minions': {}, 'turrets': {}}
rules['globals'].update(rules_raw.get('globals', {}))
for k, value in rules_raw['minions'].items():
    rules['minions'][k] = {'speed': 1.0, **value}
for k, value in rules_raw['turrets'].items():
    rules['turrets'][k] = {'cooldown': 1, 'aoe': 0, **value}
afrr_raw_checks = []
for line, row in enumerate(rows['afrr'], 1):
    checked = raw_check_afrr(row)
    require(not checked['errors'], 'afrr raw accounting ' + str(line))
    afrr_raw_checks.append({'line': line, 'log': row['log'], **checked})

def payoff(a, b):
    if a == b:
        return 0
    ee = edge[(a, b)]
    require(len(ee) == 2 and len({x[0] for x in ee}) == 1, 'two agreeing physical seats ' + a + '/' + b)
    return ee[0][0]
A = [[payoff(a, b) for b in names] for a in names]
require(A[:10] != [], 'nonempty matrix')
M = [row[:10] for row in A[:10]]
base_names = base_receipt['names']
# The receipt's displayed semantic names use a different capitalization only.
require(len(base_names) == 10 and base_receipt['matrix_row_payoff_WDL'] == M, 'base matrix receipt')
proof_rows = [line for line in proof.decode().splitlines() if line.startswith('| ')][2:]
proof_M = [[int(x.strip()) for x in line.strip('|').split('|')[1:]] for line in proof_rows]
require(proof_M == M, 'proof table matches retained matrix')
require(A[-1][:-1] == [1, 1, 1, -1, 1, 1, 1, 1, 1, -1], 'AF5 proof row matches retained outcomes')
require(all(A[i][j] == -A[j][i] for i in range(11) for j in range(11)), 'skew symmetry')
fortress = {name: [payoff(name, other) for other in names[:10]] for name in ['V46', 'V48']}
require(all(row == M[4] for row in fortress.values()), 'fortress old-ten rows equal v41')
alpha48 = payoff('AF5', 'V48')
# Exact rational witnesses. Large tables are generated from records, not copied
# into code. The small symbolic certificates in PROOF.md are tested here.
def vector(entries, n=11):
    return [F(entries.get(name, 0)) for name in names[:n]]
def rowprod(x, matrix):
    return [sum(x[i] * matrix[i][j] for i in range(len(x))) for j in range(len(matrix[0]))]
def colprod(matrix, x):
    return [sum(row[j] * x[j] for j in range(len(x))) for row in matrix]
z = vector({'GUARD00': F(1, 3), 'AS1C': F(1, 3), 'AF5': F(1, 3)})
az = colprod(A, z)
require(az == [F(-1), F(-2, 3), F(-1), F(0), F(-1), F(-1), F(-1, 3), F(0), F(-1), F(0), F(0)], 'strict dual displayed vector')
require(all(v <= 0 for v in az) and all(v >= 0 for v in rowprod(z, A)), 'value zero certificate')
vertices = []
for split in ['P5TNUBM', 'AS1C']:
    x = vector({'GUARD00': F(1, 3), 'AF5': F(1, 3), split: F(1, 3)})
    c = x[names.index('AS1C')]
    expected = [F(2, 3) + c, F(2, 3), F(2, 3) + c, F(0), F(2, 3) + c, F(1), F(1, 3), F(0), F(1), F(0), F(0)]
    require(rowprod(x, A) == expected and min(expected) >= 0, 'new segment endpoint ' + split)
    vertices.append({'split': split, 'weights': list(map(str, x)), 'payoff': list(map(str, expected))})
old = []
for split in ['BEST_V9F', 'P5TNUBM', 'AS1C']:
    x = vector({'G1': F(1, 3), 'GUARD00': F(1, 3), split: F(1, 3)}, n=10)
    require(min(rowprod(x, M)) == 0, 'old endpoint feasibility ' + split)
    score = sum(F(A[-1][j]) * x[j] for j in range(10))
    d = x[names.index('BEST_V9F')]
    require(score == F(1, 3) + 2 * d and score > 0, 'AF5 against old endpoint ' + split)
    old.append({'split': split, 'weights': list(map(str, x)), 'AF5_payoff': str(score)})
# The fortress expressions are affine in alpha and c. Their endpoint checks,
# together with the explicitly proved affine dependence, cover the interval.
fortress_cert = []
for alpha in [F(-1), F(1)]:
    dual = (F(-2) - alpha) / 3
    require(dual <= F(-1, 3), 'strict fortress dual endpoint')
    for c in [F(0), F(1, 3)]:
        primal = (1 + alpha) / 3 + c
        require(primal >= 0, 'fortress primal endpoint')
        fortress_cert.append({'alpha': str(alpha), 'c': str(c), 'dual': str(dual), 'primal': str(primal)})
# Input/source integrity is checked again at the end, with no archive fallback
# for currently executed source identities or immutable completed result rows.
for name, h in current_sources.items():
    require(sha(Path(name).read_bytes()) == h, 'final source drift ' + name)
for run, b in rowbytes.items():
    path = afr_path if run == 'afrr' else 'bot_research/runs/lead/' + run + '/results.jsonl'
    require(Path(path).read_bytes() == b, 'final result drift ' + run)
require((TOPIC / 'PROOF.md').read_bytes() == proof, 'proof drift')
mat = {'schema': 1, 'created_utc': UTC(), 'names': names, 'full_specs': {n: specs[n] for n in names + ['V46', 'V48']},
       'matrix': A, 'payoff': {'W': 1, 'D': 0, 'L': -1}, 'diagonal': 'imposed zero; no self-play measured',
       'source_conditions': conditions, 'base_campaign_counts': {'frr1': 90, 'afrr': 20},
       'optional_fortress_campaign_counts': {'frr3': 20, 'frr5': 20, 'frr8': 2},
       'fortress_rows_against_original_ten': fortress, 'AF5_vs_V48': alpha48,
       'unmeasured_edges': [{'row': 'AF5', 'column': 'V46', 'symbol': 'alpha_v46', 'interval': [-1, 1]},
                            {'row': 'V46', 'column': 'V48', 'symbol': 'q', 'condition': 'arbitrary skew-symmetric completion'}],
       'proof_sha256': proof_hash, 'afrr_raw_checks': afrr_raw_checks}
mat_pin = save('matrix.json', mat)
input_pin = save('inputs.json', {'schema': 1, 'created_utc': UTC(), 'files': files,
    'afrr_original_archive_edges': archive_edges, 'current_source_hashes': current_sources,
    'missing_raw_histories': missing_raw, 'scope': 'All 94 afrr original archives authenticated; base original 90 log hashes authenticated; current closed rows and source identities checked. Historical mutable report bytes remain historical.'})
receipt = {'schema': 1, 'started_utc': started, 'finished_utc': UTC(), 'reviewer_model': 'GPT-6 Astra',
    'verdict': 'CONFIRMED for the defined retained matrix and rational certificates',
    'execution': 'standard-library source/JSON reads and exact Fraction arithmetic only; zero project policy imports, constructors, decisions, engines, replays or new games',
    'proof_precedes_this_check': True, 'proof_sha256': proof_hash,
    'checker_sha256': sha(Path(__file__).read_bytes()), 'matrix': mat_pin, 'inputs': input_pin,
    'record_rows_joined': len(conditions), 'base_rows': 90, 'AF5_rows': 20,
    'optional_fortress_rows': 42, 'full_spec_ordered_condition_duplicates': 0,
    'both_seats_agree_each_measured_edge': True, 'afrr_archive_edges_verified': len(archive_edges),
    'base_original_log_hashes_verified': len(base_receipt['log_hashes']), 'current_source_paths': len(current_sources),
    'afrr_raw_histories_absent': len(missing_raw), 'afrr_raw_records': sum(x['records'] for x in afrr_raw_checks),
    'afrr_accepted_actions': sum(x['accepted_total'] for x in afrr_raw_checks), 'afrr_raw_errors': [], 'value': '0',
    'strict_dual_Az': list(map(str, az)), 'optimal_segment_endpoints': vertices,
    'old_optimal_vertices_AF5_exploit': old, 'fortress_affine_endpoint_checks': fortress_cert,
    'AF5_V48_observed_payoff': alpha48,
    'necessity_proof': 'The standalone informal proof, including strict dual exclusion and a>=t>=b>=a, proves completeness; endpoint checks alone do not.',
    'limits': ['Only the retained standard-start WDL object is certified. Self-play diagonals are conventions.',
               'No full game replay, fresh policy reproduction, timed-controller coupling or causal latency claim is made.',
               'AF5 was selected in research; repeat observations are not fresh independent opponents.',
               'All twenty afrr raw histories are retained and checked here. Earlier source/result inspection did not archive those histories; this is later added evidence.',
               'AF5-v46 and v46-v48 remain unmeasured, with the theorem uniform over their stated completions.'],
    'errors': []}
receipt_pin = save('receipt.json', receipt)
print(json.dumps({'matrix': mat_pin, 'inputs': input_pin, 'receipt': receipt_pin, 'finished_utc': receipt['finished_utc'],
                  'verdict': receipt['verdict'], 'rows': len(conditions), 'value': '0', 'AF5_V48': alpha48}, indent=2))

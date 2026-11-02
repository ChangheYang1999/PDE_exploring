"""Independent stdlib aggregation of archived result and log bytes; no project imports."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import gzip, hashlib, json, shlex

OUT = Path('bot_research/experiments/validation/reviews/frr4_final_fortress_001')
sha = lambda b: hashlib.sha256(b).hexdigest()
UTC = lambda: datetime.now(timezone.utc).isoformat()
m = json.loads((OUT/'input_manifest_001.json').read_text())

def read(name):
    entry = m['files'][name]
    z = (OUT/entry['archive']).read_bytes()
    b = gzip.decompress(z)
    if sha(z) != entry['archive_sha256'] or sha(b) != entry['sha256'] or len(b) != entry['bytes']:
        raise ValueError('input archive identity failure: '+name)
    return b

def rows(run):
    return [json.loads(line) for line in read(run+'/results.jsonl').splitlines()]

def require(ok, description, errors):
    if not ok: errors.append(description)

def outcome(row, side):
    return 'D' if row['winner'] is None else ('W' if row['winner']==side else 'L')

def key(row):
    side=row['candidate_side']
    return (row['spec_b' if side==0 else 'spec_a'], row['scenario'], side)

def entry_path(spec):
    return spec.partition(':')[0].replace('.','/')+'.py'

specs = {}
for line in read('bot_research/experiments/lead/rr_specs.sh').decode().splitlines():
    if not line or line.startswith('#') or '=' not in line: continue
    name,val = line.split('=',1)
    values=shlex.split(val)
    if len(values)!=1: raise ValueError('nonliteral assignment '+name)
    val=values[0]
    for k,v in specs.items(): val=val.replace('$'+k,v)
    specs[name]=val
aliases={v:k for k,v in specs.items()}

def source_check(row):
    errors=[]
    require(row.get('source_changed') is False,'recorded source_changed not false',errors)
    mismatches=[]
    for name,digest in row.get('sources',{}).items():
        if name not in m['files'] or m['files'][name]['sha256']!=digest:
            mismatches.append(name)
    for side in ['a','b']:
        spec=row['spec_'+side]
        p=entry_path(spec)
        require(m['files'].get(p,{}).get('sha256')==row['hash_'+side], 'entry hash '+side,errors)
        require(m['current_static_versions'][spec]['version']==row['version_'+side], 'static version '+side,errors)
    require(not mismatches,'recorded loaded source mismatch',errors)
    return {'errors':errors,'loaded_source_count':len(row.get('sources',{})), 'loaded_source_mismatches':mismatches}

# Bind the bundled rules separately: this immutable source was not included in the original run's Python-only digest.
p=Path('td_game/balanced.json'); b=p.read_bytes(); q=OUT/'inputs'/f'{sha(b)}.gz'
if not q.exists():
    with q.open('xb') as f:f.write(gzip.compress(b,compresslevel=6,mtime=0))
rules_raw=json.loads(b)
rule_source={'path':p.as_posix(),'sha256':sha(b),'bytes':len(b),'archive':q.relative_to(OUT).as_posix(),
             'archive_sha256':sha(q.read_bytes()),'read_utc':UTC()}
# Source defaults read from config.py, not obtained by importing it.
rules={'label':rules_raw.get('label','custom rules'),'demo':rules_raw.get('demo',False),'wall_cost':rules_raw['wall_cost'],
       'wall_damage':rules_raw.get('wall_damage',0),'wall_range':rules_raw.get('wall_range',0.0),'wall_cooldown':rules_raw.get('wall_cooldown',1),
       'globals':{'width':12,'height':12,'spawn':[0,0],'base':[11,11],'initial_hp':800,'initial_gold':100,'max_rounds':50,'ticks_per_round':250,
                  'roster_lifespan':12,'factory_cost':20,'factory_income':15,'path_income_per_step':1,'base_hit_bounty':5},
       'minions':{},'turrets':{}}
rules['globals'].update(rules_raw.get('globals',{}))
for k,v in rules_raw['minions'].items():rules['minions'][k]={'speed':1.0,**v}
for k,v in rules_raw['turrets'].items():rules['turrets'][k]={'cooldown':1,'aoe':0,**v}

runtimes=defaultdict(list)
all_frr4_action_counts=Counter();all_frr4_spend=Counter();all_frr4_errors=[]
prefixes=defaultdict(list)

def raw_check(row, collect_frr4=False):
    errors=[]
    records=[json.loads(line) for line in read(row['log']).splitlines()]
    turns={}
    for rec in records:
        k=(rec['round'],rec['player'])
        require(k not in turns,'duplicate record '+str(k),errors)
        turns[k]=rec
        require(rec.get('schema_version')==1,'schema',errors)
        require(rec['snapshot']['name']==row['spec_a' if rec['player']==0 else 'spec_b'],'snapshot identity',errors)
    expected={(r,s) for r in range(row['rounds']+1) for s in (0,1)}
    require(set(turns)==expected,'missing or unexpected round/player records',errors)
    require(len(records)==2*(row['rounds']+1),'record count',errors)
    computed=[]
    for side in (0,1):
        initial=turns[(0,side)]
        match=initial['match']
        require(match['rules']==rules,'bundled balanced rules content',errors)
        require(match['research_specs']==[row['spec_a'],row['spec_b']],'initial full spec',errors)
        require(match['bots']==[row['spec_a'],row['spec_b']],'initial bots',errors)
        require(match['research_scenario']==row['scenario'],'initial scenario',errors)
        require(match['research_metadata']==row['metadata'],'initial metadata',errors)
        accepted=Counter();rejected=Counter();spent=Counter();bot_errors=[];damage=0;hits=0;first=None
        for rnd in range(1,row['rounds']+1):
            rec=turns[(rnd,side)];prev=turns[(rnd-1,side)]['snapshot'];snap=rec['snapshot']
            cost=0;combat=[];income=[];new=Counter()
            for event in rec['event']:
                kind=event['kind']
                if kind=='action':
                    action=event['action'];op=action.get('op') if isinstance(action,dict) else None
                    if event['accepted']:
                        accepted[str(op)]+=1;new[str(op)]+=1
                        typ=action.get('type');cat=op if op in ('buy_factory','build_wall') else str(op)+':'+str(typ)
                        c=event.get('cost',0);cost+=c;spent[cat]+=c
                        expected_cost={'buy_factory':rules['globals']['factory_cost'],'build_wall':rules['wall_cost']}.get(op)
                        if op=='buy_minion':expected_cost=rules['minions'][typ]['cost']
                        if op=='build_turret':expected_cost=rules['turrets'][typ]['cost']
                        require(c==expected_cost,'accepted cost '+str((rnd,side,op)),errors)
                    else:rejected[event.get('reason','?')]+=1
                elif kind=='bot_error':bot_errors.append({'round':rnd,'reason':event.get('reason')})
                elif kind=='combat':
                    combat.append(event);damage+=event['damage_dealt'];hits+=event['outgoing_hits']
                    if first is None and event['base_damage']>0:first=rnd
                elif kind=='income':income.append(event)
                elif kind not in ('roster_expired',):
                    # Unknown kinds are retained, never silently treated as successful action evidence.
                    pass
            require(len(combat)==1 and len(income)==1,'one combat and income event '+str((rnd,side)),errors)
            c=combat[0];i=income[0]
            require(snap['hp']==prev['hp']-c['base_damage'],'HP accounting '+str((rnd,side)),errors)
            require(snap['gold']==prev['gold']-cost+i['total'],'gold accounting '+str((rnd,side)),errors)
            require(i['total']==i['path']+i['factories']+i['hits'],'income sum '+str((rnd,side)),errors)
            require(i['path']==snap['length_path']*rules['globals']['path_income_per_step'],'path income '+str((rnd,side)),errors)
            require(i['factories']==snap['n_factories']*rules['globals']['factory_income'],'factory income '+str((rnd,side)),errors)
            require(i['hits']==c['outgoing_hits']*rules['globals']['base_hit_bounty'],'hit income '+str((rnd,side)),errors)
            for field,op in [('n_factories','buy_factory'),('n_turrets','build_turret'),('n_walls','build_wall')]:
                require(snap[field]==prev[field]+new[op],field+' accounting '+str((rnd,side)),errors)
        snap=turns[(row['rounds'],side)]['snapshot']
        value={k:snap.get(k) for k in ['name','hp','gold','n_factories','n_turrets','n_walls','length_path']}
        value.update(accepted=dict(accepted),rejected=dict(rejected),n_rejected=sum(rejected.values()),bot_errors=bot_errors,
                     damage_dealt=damage,hits=hits,spent=dict(spent),first_damage_taken_round=first)
        computed.append(value)
        require(value==row['players'][side],'full player summary '+str(side),errors)
        require(turns[(row['rounds'],side)].get('result')=={'winner':row['winner'],'reason':row['reason']},'terminal result '+str(side),errors)
        require(snap['hp']==row['hp_a' if side==0 else 'hp_b'],'terminal HP field '+str(side),errors)
        if collect_frr4:
            all_frr4_action_counts.update(accepted);all_frr4_spend.update(spent)
    for rnd in range(1,row['rounds']+1):
        evs=[turns[(rnd,s)]['event'] for s in (0,1)]
        orders=sorted(e['order'] for es in evs for e in es if e['kind']=='action')
        require(orders==list(range(len(orders))),'interleaved action order '+str(rnd),errors)
        c=[[e for e in es if e['kind']=='combat'][0] for es in evs]
        for s in (0,1):
            require(c[s]['damage_dealt']==c[1-s]['base_damage'],'cross-player combat damage '+str((rnd,s)),errors)
            require(c[s]['outgoing_hits']==c[1-s]['incoming_hits'],'cross-player hits '+str((rnd,s)),errors)
    require(row['hp_diff_a']==row['hp_a']-row['hp_b'],'HP difference',errors)
    require(row.get('error') is None,'row error',errors)
    require(row['scenario_errors']==[[],[]],'scripted-round policy exceptions',errors)
    require(not any(p['n_rejected'] or p['bot_errors'] for p in computed),'rejected/error count',errors)
    if collect_frr4:
        prefix=[]
        for rec in records:
            if rec['round']>2:continue
            snap={k:v for k,v in rec['snapshot'].items() if k!='name'}
            prefix.append({'round':rec['round'],'player':rec['player'],'event':rec['event'],'snapshot':snap})
        digest=sha(json.dumps(prefix,sort_keys=True,separators=(',',':')).encode())
        prefixes[row['scenario']].append(digest)
    return {'log':row['log'],'records':len(records),'rounds':row['rounds'],'errors':errors,
            'accepted_total':sum(sum(p['accepted'].values()) for p in computed),
            'rejected_total':sum(p['n_rejected'] for p in computed),'bot_error_total':sum(len(p['bot_errors']) for p in computed)}

def campaign(run, candidate_alias, opponent_aliases, scenarios, raw=False):
    rr=rows(run);candidate=specs[candidate_alias]
    expected={(specs[o],sc,s) for o in opponent_aliases for sc in scenarios for s in (0,1)}
    got=Counter(key(r) for r in rr)
    errors=[];details=[];wdl=Counter()
    for row in rr:
        side=row['candidate_side'];opp,sc,_=key(row)
        require(row['spec_a' if side==0 else 'spec_b']==candidate,'candidate full spec',errors)
        require(row['metadata']=={'pair':row['pair'],'candidate_side':side},'metadata fields',errors)
        require(row['pair']==opponent_aliases.index(aliases[opp]),'pair mapping',errors)
        sc_check=source_check(row)
        raw_result=raw_check(row,collect_frr4=run.endswith('/frr4')) if raw else None
        w=outcome(row,side);wdl[w]+=1
        details.append({'opponent_alias':aliases[opp],'opponent':opp,'scenario':sc,'candidate_side':side,'outcome':w,
                        'candidate_hp':row['hp_a' if side==0 else 'hp_b'],'opponent_hp':row['hp_b' if side==0 else 'hp_a'],
                        'hp_difference':row['hp_diff_a']*(1-2*side),'rounds':row['rounds'],'source_check':sc_check,'raw_check':raw_result})
        for s in (0,1):
            runtimes[(run,row['spec_a' if s==0 else 'spec_b'])].append({'max_seconds':row['decide_max_seconds'][s],
                'total_seconds':row['decide_seconds'][s],'scenario':sc,'candidate_side':side,'physical_side':s,
                'rounds':row['rounds'],'log':row['log']})
    return {'rows':len(rr),'planned_conditions':len(expected),'wdl':dict(wdl),'distinct_conditions':len(got),
            'missing_conditions':[{'opponent':o,'scenario':sc,'candidate_side':s} for o,sc,s in sorted(expected-set(got),key=str)],
            'unexpected_conditions':[list(k) for k in set(got)-expected],
            'duplicates':[{'condition':list(k),'count':n} for k,n in got.items() if n!=1],
            'metadata_errors':errors,'conditions':details,'round_sum':sum(r['rounds'] for r in rr),
            'call_count_implied_by_harness':2*sum(r['rounds'] for r in rr),
            'recorded_total_wall_seconds':sum(r['wall_seconds'] for r in rr)}

six=['BEST_V9E','BEST_V9F','V41','V29','G1','AS1C']
ten=['BEST_V9E','BEST_V9F','AF2G','P5TNUBM','V41','V29','G1','GUARD00','TDEF','AS1C']
result={'schema':1,'generated_utc':UTC(),'reviewer_model':'GPT-6 Astra','input_manifest_sha256':sha((OUT/'input_manifest_001.json').read_bytes()),
        'rules_source':rule_source,'specs':specs,'frr4':campaign('bot_research/runs/lead/frr4','V46',six,['mirror:1:2','asym:23:2'],True),
        'frr5_initial_prefix':campaign('bot_research/runs/lead/frr5','V48',ten,[None],True),
        'frr3_result_rows_only':campaign('bot_research/runs/lead/frr3','V46',ten,[None],False)}
result['frr4']['action_counts']=dict(all_frr4_action_counts);result['frr4']['spent']=dict(all_frr4_spend)
result['frr4']['first_two_round_public_prefix_sha256']={k:{'distinct':len(set(v)),'hashes':sorted(set(v)),'games':len(v)} for k,v in prefixes.items()}
result['runtime_maxima']=[]
for (run,spec),values in sorted(runtimes.items()):
    mx=max(v['max_seconds'] for v in values)
    result['runtime_maxima'].append({'run':run,'spec':spec,'alias':aliases.get(spec,spec),'max_seconds':mx,
        'max_game_locations':[v for v in values if v['max_seconds']==mx],
        'round_of_maximum_recoverable':False,'sum_decide_seconds':sum(v['total_seconds'] for v in values)})

# Complete frr2+frr4 round robin, identifying pairs by full specs and physical seats.
frr2=rows('bot_research/runs/lead/frr2');frr4=rows('bot_research/runs/lead/frr4')
full_counts=Counter();standings=defaultdict(Counter);asym_without_v41=[];seat1_wins=[]
for row in frr2+frr4:
    pair=tuple(sorted([row['spec_a'],row['spec_b']]))
    # physical assignment retained; reversal is a different condition.
    full_counts[(row['spec_a'],row['spec_b'],row['scenario'])]+=1
    for s in (0,1):standings[aliases[row['spec_a' if s==0 else 'spec_b']]][outcome(row,s)]+=1
    if row['scenario']=='asym:23:2':
        if row['winner']==1:seat1_wins.append({'spec_a':row['spec_a'],'spec_b':row['spec_b'],'experiment':row['experiment']})
        if row in frr2 and specs['V41'] not in pair:asym_without_v41.append(row['winner']==0)
seven=six+['V46']
expected_rr={(specs[a],specs[b],sc) for a in seven for b in seven if a!=b for sc in ['mirror:1:2','asym:23:2']}
result['frr2_plus_frr4']={'rows':len(frr2)+len(frr4),'distinct_conditions':len(full_counts),'expected_conditions':len(expected_rr),
    'missing':len(expected_rr-set(full_counts)),'unexpected':len(set(full_counts)-expected_rr),
    'duplicates':[{'condition':list(k),'count':n} for k,n in full_counts.items() if n!=1],
    'standings':{k:dict(v) for k,v in standings.items()},'frr2_asym_without_v41_count':len(asym_without_v41),
    'frr2_asym_without_v41_all_physical_seat0_wins':all(asym_without_v41),
    'asym_physical_seat1_wins':seat1_wins,
    'frr2_current_source_check_errors':[{'index':i,'check':source_check(r)} for i,r in enumerate(frr2) if source_check(r)['errors']]}

# Compare retained defense-lane results, never infer unretained full-history identity.
x215=rows('bot_research/runs/defense/x215_v46_lead');x230=rows('bot_research/runs/defense/x230_v48_lead')
def norm(row):
    side=row['candidate_side']; return {'outcome':outcome(row,side),'rounds':row['rounds'],
        'candidate_hp':row['hp_a' if side==0 else 'hp_b'],'opponent_hp':row['hp_b' if side==0 else 'hp_a'],
        'hp_difference':row['hp_diff_a']*(1-2*side)}
for label,aa,bb in [('v46_x215_vs_frr4',x215,frr4),('v46_x215_vs_v48_x230',x215,x230),('v46_frr3_vs_initial_v48_frr5',rows('bot_research/runs/lead/frr3'),rows('bot_research/runs/lead/frr5'))]:
    ma={key(r):r for r in aa};mb={key(r):r for r in bb};common=sorted(set(ma)&set(mb),key=str)
    result[label]={'common_conditions':len(common),'duplicate_a':len(aa)-len(ma),'duplicate_b':len(bb)-len(mb),
        'comparisons':[{'opponent':k[0],'scenario':k[1],'candidate_side':k[2],'a':norm(ma[k]),'b':norm(mb[k]),'same':norm(ma[k])==norm(mb[k])} for k in common]}
result['defense_lane_result_identity_errors']={name:[{'row':i,'check':source_check(r)} for i,r in enumerate(rr) if source_check(r)['errors']] for name,rr in [('x215',x215),('x230',x230)]}
result['finished_utc']=UTC()
with (OUT/'record_audit_001.json').open('x') as f:json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
for name in ['frr4','frr5_initial_prefix','frr3_result_rows_only']:
    r=result[name]; print(name, json.dumps({k:r[k] for k in ['rows','planned_conditions','wdl','distinct_conditions','round_sum','call_count_implied_by_harness']}))
    print('raw_error_conditions',sum(bool(c['raw_check'] and c['raw_check']['errors']) for c in r['conditions']),
          'source_error_conditions',sum(bool(c['source_check']['errors']) for c in r['conditions']))
    for c in r['conditions']:
        if c['source_check']['errors'] or (c['raw_check'] and c['raw_check']['errors']): print(json.dumps(c))
print('combined',json.dumps(result['frr2_plus_frr4']))
print('frr4_actions',dict(all_frr4_action_counts))
print('frr4_maxima',[(x['alias'],x['max_seconds']) for x in result['runtime_maxima'] if x['run'].endswith('/frr4')])
print('comparisons',[(label,result[label]['common_conditions'],sum(x['same'] for x in result[label]['comparisons'])) for label in ['v46_x215_vs_frr4','v46_x215_vs_v48_x230','v46_frr3_vs_initial_v48_frr5']])
print('defense_identity_errors',json.dumps(result['defense_lane_result_identity_errors']))
print('audit_sha256',sha((OUT/'record_audit_001.json').read_bytes()))

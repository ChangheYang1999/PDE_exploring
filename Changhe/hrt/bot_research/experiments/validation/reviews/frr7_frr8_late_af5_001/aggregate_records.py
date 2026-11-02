"""Independent archived-record audit. No project imports, game reconstruction or policy calls."""
import gzip,hashlib,json,shlex,sys
from collections import Counter,defaultdict
from datetime import datetime,timezone
from pathlib import Path
OUT=Path('bot_research/experiments/validation/reviews/frr7_frr8_late_af5_001');label=sys.argv[1]
sha=lambda b:hashlib.sha256(b).hexdigest();UTC=lambda:datetime.now(timezone.utc).isoformat()
manpath=OUT/('input_manifest_'+label+'.json');m=json.loads(manpath.read_bytes())
def read(name):
    e=m['files'][name];z=(OUT/e['archive']).read_bytes();b=gzip.decompress(z)
    if sha(z)!=e['archive_sha256'] or sha(b)!=e['sha256'] or len(b)!=e['bytes']:raise ValueError('input mismatch '+name)
    return b
def require(ok,desc,errors):
    if not ok:errors.append(desc)
specs={}
for line in read('bot_research/experiments/lead/rr_specs.sh').decode().splitlines():
    if not line or line.startswith('#') or '=' not in line:continue
    name,val=line.split('=',1);tokens=shlex.split(val)
    if len(tokens)!=1:raise ValueError('spec assignment syntax '+name)
    val=tokens[0]
    for k,v in specs.items():val=val.replace('$'+k,v)
    specs[name]=val
aliases={v:k for k,v in specs.items()}
ten=['BEST_V9E','BEST_V9F','AF2G','P5TNUBM','V41','V29','G1','GUARD00','TDEF','AS1C'];six=['BEST_V9E','BEST_V9F','V41','V29','G1','AS1C']
rules_raw=json.loads(read('td_game/balanced.json'))
rules={'label':rules_raw.get('label','custom rules'),'demo':rules_raw.get('demo',False),'wall_cost':rules_raw['wall_cost'],
'wall_damage':rules_raw.get('wall_damage',0),'wall_range':rules_raw.get('wall_range',0.0),'wall_cooldown':rules_raw.get('wall_cooldown',1),
'globals':{'width':12,'height':12,'spawn':[0,0],'base':[11,11],'initial_hp':800,'initial_gold':100,'max_rounds':50,'ticks_per_round':250,
'roster_lifespan':12,'factory_cost':20,'factory_income':15,'path_income_per_step':1,'base_hit_bounty':5},'minions':{},'turrets':{}}
rules['globals'].update(rules_raw.get('globals',{}))
for k,v in rules_raw['minions'].items():rules['minions'][k]={'speed':1.0,**v}
for k,v in rules_raw['turrets'].items():rules['turrets'][k]={'cooldown':1,'aoe':0,**v}
def outcome(row,side):return 'D' if row['winner'] is None else ('W' if row['winner']==side else 'L')
def key(row):
    side=row['candidate_side'];return (row['spec_b' if side==0 else 'spec_a'],row['scenario'],side)
def canonical(rec):
    # Full events (including action order), all snapshot fields except policy name,
    # player/round/schema/result; identity metadata in match is independently checked.
    return {k:({kk:vv for kk,vv in v.items() if kk!='name'} if k=='snapshot' else v)
            for k,v in rec.items() if k!='match'}
def raw_check(row):
    errors=[];records=[json.loads(x) for x in read(row['log']).splitlines()];turns={};stats=[]
    for rec in records:
        k=(rec['round'],rec['player']);require(k not in turns,'duplicate turn '+str(k),errors);turns[k]=rec
        require(rec.get('schema_version')==1,'schema',errors)
        require(rec['snapshot']['name']==row['spec_a' if rec['player']==0 else 'spec_b'],'snapshot policy identity',errors)
    require(set(turns)=={(r,s) for r in range(row['rounds']+1) for s in (0,1)},'complete turn grid',errors)
    for side in (0,1):
        initial=turns[(0,side)];match=initial['match']
        require(match['rules']==rules,'exact balanced rules',errors)
        for field in ['bots','research_specs']:require(match[field]==[row['spec_a'],row['spec_b']],'initial '+field,errors)
        require(match['research_scenario']==row['scenario'],'initial scenario',errors)
        require(match['research_metadata']==row['metadata'],'initial metadata',errors)
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
                        require(c==ec,'accepted cost '+str((rnd,side,op)),errors)
                    else:rejected[e.get('reason','?')]+=1
                elif e['kind']=='bot_error':bot_errors.append({'round':rnd,'reason':e.get('reason')})
                elif e['kind']=='combat':
                    combat.append(e);damage+=e['damage_dealt'];hits+=e['outgoing_hits']
                    if first is None and e['base_damage']>0:first=rnd
                elif e['kind']=='income':income.append(e)
            require(len(combat)==1 and len(income)==1,'one combat/income '+str((rnd,side)),errors)
            if len(combat)!=1 or len(income)!=1:continue
            c=combat[0];i=income[0]
            require(snap['hp']==prev['hp']-c['base_damage'],'HP accounting '+str((rnd,side)),errors)
            require(snap['gold']==prev['gold']-cost+i['total'],'gold accounting '+str((rnd,side)),errors)
            require(i['total']==i['path']+i['factories']+i['hits'],'income sum '+str((rnd,side)),errors)
            require(i['path']==snap['length_path']*rules['globals']['path_income_per_step'],'path income '+str((rnd,side)),errors)
            require(i['factories']==snap['n_factories']*rules['globals']['factory_income'],'factory income '+str((rnd,side)),errors)
            require(i['hits']==c['outgoing_hits']*rules['globals']['base_hit_bounty'],'hit income '+str((rnd,side)),errors)
            for field,op in [('n_factories','buy_factory'),('n_turrets','build_turret'),('n_walls','build_wall')]:
                require(snap[field]==prev[field]+new[op],field+' accounting '+str((rnd,side)),errors)
        snap=turns[(row['rounds'],side)]['snapshot'];value={k:snap.get(k) for k in ['name','hp','gold','n_factories','n_turrets','n_walls','length_path']}
        value.update(accepted=dict(accepted),rejected=dict(rejected),n_rejected=sum(rejected.values()),bot_errors=bot_errors,
                     damage_dealt=damage,hits=hits,spent=dict(spent),first_damage_taken_round=first)
        require(value==row['players'][side],'complete player summary '+str(side),errors)
        require(turns[(row['rounds'],side)].get('result')=={'winner':row['winner'],'reason':row['reason']},'terminal result '+str(side),errors)
        require(snap['hp']==row['hp_a' if side==0 else 'hp_b'],'terminal HP '+str(side),errors);stats.append(value)
    for rnd in range(1,row['rounds']+1):
        evs=[turns[(rnd,s)]['event'] for s in (0,1)]
        orders=sorted(e['order'] for ee in evs for e in ee if e['kind']=='action')
        require(orders==list(range(len(orders))),'interleaved action order '+str(rnd),errors)
        c=[[e for e in ee if e['kind']=='combat'] for ee in evs]
        if all(len(x)==1 for x in c):
            for s in (0,1):
                require(c[s][0]['damage_dealt']==c[1-s][0]['base_damage'],'cross-player damage '+str((rnd,s)),errors)
                require(c[s][0]['outgoing_hits']==c[1-s][0]['incoming_hits'],'cross-player hits '+str((rnd,s)),errors)
    require(row['hp_diff_a']==row['hp_a']-row['hp_b'],'HP difference',errors)
    require(row.get('error') is None,'row error',errors);require(row.get('scenario_errors')==[[],[]],'discarded-call exception',errors)
    require(not any(p['n_rejected'] or p['bot_errors'] for p in stats),'rejected/error count',errors)
    norm=[canonical(turns[k]) for k in sorted(turns)]
    digest=sha(json.dumps(norm,sort_keys=True,separators=(',',':')).encode())
    byround=[sha(json.dumps([canonical(turns[(r,s)]) for s in (0,1)],sort_keys=True,separators=(',',':')).encode()) for r in range(row['rounds']+1)]
    return {'errors':errors,'records':len(records),'accepted_total':sum(sum(p['accepted'].values()) for p in stats),
            'accepted_counts':dict(sum((Counter(p['accepted']) for p in stats),Counter())),
            'rejected_total':sum(p['n_rejected'] for p in stats),'bot_error_total':sum(len(p['bot_errors']) for p in stats),
            'canonical_sha256':digest,'canonical_round_sha256':byround}
def source_check(row):
    errors=[];mismatches=[p for p,h in row['sources'].items() if m['files'].get(p,{}).get('sha256')!=h]
    require(not mismatches,'loaded source mismatch',errors);require(row['source_changed'] is False,'source_changed flag',errors)
    for side in ['a','b']:
        spec=row['spec_'+side];p=spec.partition(':')[0].replace('.','/')+'.py'
        require(m['files'][p]['sha256']==row['hash_'+side],'entry '+side,errors)
        require(m['current_static_versions'][spec]['version']==row['version_'+side],'static closure '+side,errors)
    return {'errors':errors,'loaded_paths':len(row['sources']),'mismatched_paths':mismatches}
allrows={};alldetails={};out={'schema':1,'started_utc':UTC(),'reviewer_model':'GPT-6 Astra','input_manifest':manpath.as_posix(),
'input_manifest_sha256':sha(manpath.read_bytes()),'execution':'archived text/JSON arithmetic only; no game/policy execution',
'specs':specs,'campaigns':{},'runtime_maxima':[]}
config=[('frr2',[(six[i],six[j]) for i in range(6) for j in range(i+1,6)],['mirror:1:2','asym:23:2']),
 ('frr4',[('V46',x) for x in six],['mirror:1:2','asym:23:2']),
 ('frr5',[('V48',x) for x in ten],[None]),
 ('frr6',[('V48',x) for x in six],['mirror:1:2','asym:23:2']),
 ('frr7',[('AF5',x) for x in six+['V48']],['mirror:1:2','asym:23:2']),
 ('frr8',[('AF5','V48')],[None])]
for run,pairs,scenarios in config:
    base='bot_research/runs/lead/'+run
    rr=[json.loads(x) for x in read(base+'/results.jsonl').splitlines()] if base+'/results.jsonl' in m['files'] else []
    allrows[run]=rr
    expect={(specs[c],specs[o],sc,s) for c,o in pairs for sc in scenarios for s in (0,1)}
    errors=[];details=[];wdl=Counter();times=defaultdict(list);got=Counter()
    for r in rr:
        side=r['candidate_side'];cand=r['spec_a' if side==0 else 'spec_b'];opp=r['spec_b' if side==0 else 'spec_a'];sc=r['scenario']
        condition=(cand,opp,sc,side);got[condition]+=1
        require(r['metadata']=={'pair':r['pair'],'candidate_side':side},'metadata',errors)
        require(0<=r['pair']<len(pairs) and pairs[r['pair']]==(aliases.get(cand),aliases.get(opp)),'pair order',errors)
        rc=raw_check(r);src=source_check(r);w=outcome(r,side);wdl[w]+=1
        d={'condition':list(condition),'candidate_alias':aliases[cand],'opponent_alias':aliases[opp],
           'candidate_side':side,'scenario':sc,'outcome':w,'candidate_hp':r['hp_a' if side==0 else 'hp_b'],
           'opponent_hp':r['hp_b' if side==0 else 'hp_a'],'hp_difference':r['hp_diff_a']*(1-2*side),
           'rounds':r['rounds'],'log':r['log'],'raw_check':rc,'source_check':src}
        details.append(d)
        for s in (0,1):times[r['spec_a' if s==0 else 'spec_b']].append({'max_seconds':r['decide_max_seconds'][s],
          'total_seconds':r['decide_seconds'][s],'log':r['log'],'physical_side':s,'scenario':sc,'end_round':r['rounds']})
    alldetails[run]=details
    out['campaigns'][run]={'observed_rows':len(rr),'planned_conditions':len(expect),'summary_present':base+'/summary.md' in m['files'],
      'complete_grid':set(got)==expect and all(v==1 for v in got.values()),
      'wdl_of_declared_first_pair_member':{k:wdl[k] for k in ['W','D','L']},
      'missing_conditions':[list(k) for k in sorted(expect-set(got),key=str)],
      'unexpected_conditions':[list(k) for k in sorted(set(got)-expect,key=str)],
      'duplicates':[{'condition':list(k),'count':n} for k,n in got.items() if n!=1],
      'metadata_errors':errors,'conditions':details,'sum_rounds':sum(r['rounds'] for r in rr),
      'sum_records':sum(d['raw_check']['records'] for d in details),'accepted_total':sum(d['raw_check']['accepted_total'] for d in details),
      'accepted_counts':dict(sum((Counter(d['raw_check']['accepted_counts']) for d in details),Counter())),
      'rejected_total':sum(d['raw_check']['rejected_total'] for d in details),'bot_error_total':sum(d['raw_check']['bot_error_total'] for d in details),
      'implied_underlying_calls':2*sum(r['rounds'] for r in rr),'recorded_wall_seconds_sum':sum(r['wall_seconds'] for r in rr)}
    for spec,vals in times.items():
        mx=max(v['max_seconds'] for v in vals)
        out['runtime_maxima'].append({'run':run,'spec':spec,'alias':aliases[spec],'max_call_seconds':mx,
          'locations':[v for v in vals if v['max_seconds']==mx],'round_of_maximum_recoverable':False,
          'total_decision_seconds':sum(v['total_seconds'] for v in vals)})
def perspective(run,alias):
    result={};duplicates=[]
    for d,r in zip(alldetails[run],allrows[run]):
        for side in (0,1):
            if r['spec_a' if side==0 else 'spec_b']!=specs[alias]:continue
            opp=r['spec_b' if side==0 else 'spec_a'];k=(opp,r['scenario'],side)
            if k in result:duplicates.append(list(k))
            result[k]={'run':run,'log':r['log'],'candidate_alias':alias,'opponent_alias':aliases[opp],
              'outcome':outcome(r,side),'candidate_hp':r['hp_a' if side==0 else 'hp_b'],
              'opponent_hp':r['hp_b' if side==0 else 'hp_a'],'hp_difference':r['hp_diff_a']*(1-2*side),
              'rounds':r['rounds'],'canonical_sha256':d['raw_check']['canonical_sha256'],
              'canonical_round_sha256':d['raw_check']['canonical_round_sha256']}
    if duplicates:raise ValueError('duplicate perspective '+run+' '+alias+str(duplicates))
    return result
out['matched_comparisons']={}
for title,newrun,alias,oldruns in [('scripted_AF5_vs_V29','frr7','V29',['frr2','frr6']),
 ('scripted_AF5_vs_G1','frr7','G1',['frr2','frr6']),('scripted_AF5_vs_V46','frr7','V46',['frr4']),
 ('scripted_AF5_vs_V48','frr7','V48',['frr6']),('standard_AF5_vs_V29','frr8','V29',['frr5']),
 ('standard_AF5_vs_G1','frr8','G1',['frr5'])]:
    aa={}
    for run in oldruns:
        p=perspective(run,alias)
        if set(aa)&set(p):raise ValueError('duplicate baseline condition')
        aa.update(p)
    bb=perspective(newrun,'AF5');comp=[];rank={'W':1,'D':0,'L':-1}
    for k in sorted(set(aa)&set(bb),key=str):
        a,b=aa[k],bb[k];first=next((i for i,(x,y) in enumerate(zip(a['canonical_round_sha256'],b['canonical_round_sha256'])) if x!=y),None)
        if first is None and a['rounds']!=b['rounds']:first=min(a['rounds'],b['rounds'])+1
        comp.append({'condition':list(k),'opponent_alias':b['opponent_alias'],
          'wdl_comparison':'better' if rank[b['outcome']]>rank[a['outcome']] else 'worse' if rank[b['outcome']]<rank[a['outcome']] else 'same',
          'same_wdl_hp_rounds':all(a[x]==b[x] for x in ['outcome','candidate_hp','opponent_hp','rounds']),
          'baseline':{x:a[x] for x in ['run','log','outcome','candidate_hp','opponent_hp','hp_difference','rounds']},
          'af5':{x:b[x] for x in ['run','log','outcome','candidate_hp','opponent_hp','hp_difference','rounds']},
          'same_canonical_history':a['canonical_sha256']==b['canonical_sha256'],'first_different_round':first})
    w=Counter(x['wdl_comparison'] for x in comp)
    out['matched_comparisons'][title]={'baseline_alias':alias,'matched_conditions':len(comp),
      'wdl_comparison':{x:w[x] for x in ['better','same','worse']},
      'af5_wdl':dict(Counter(x['af5']['outcome'] for x in comp)),
      'baseline_wdl':dict(Counter(x['baseline']['outcome'] for x in comp)),
      'same_wdl_hp_rounds':sum(x['same_wdl_hp_rounds'] for x in comp),
      'same_canonical_history':sum(x['same_canonical_history'] for x in comp),
      'af5_unmatched_conditions':[list(k) for k in sorted(set(bb)-set(aa),key=str)],
      'baseline_unmatched_conditions':[list(k) for k in sorted(set(aa)-set(bb),key=str)],'conditions':comp}
out['frozen_packages']={}
for family,version in [('defense','v46'),('defense','v48'),('economy','v29')]:
    base='bot_research/bots/'+family+'/frozen/'+version;checks=[]
    for line in read(base+'/SHA256SUMS').decode().splitlines():
        h,name=line.split(maxsplit=1);p=base+'/'+Path(name).name
        checks.append({'path':p,'sha256':m['files'][p]['sha256'],'expected':h,'matches':m['files'][p]['sha256']==h})
    out['frozen_packages'][version]=checks
out['raw_or_source_errors']=[{'run':run,'condition':d['condition'],'raw_errors':d['raw_check']['errors'],'source_errors':d['source_check']['errors']}
 for run,c in out['campaigns'].items() for d in c['conditions'] if d['raw_check']['errors'] or d['source_check']['errors']]
out['finished_utc']=UTC();p=OUT/('record_audit_'+label+'.json')
with p.open('x') as f:json.dump(out,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'path':p.as_posix(),'sha256':sha(p.read_bytes()),'finished_utc':out['finished_utc'],
 'campaigns':{k:{x:v[x] for x in ['observed_rows','planned_conditions','complete_grid','wdl_of_declared_first_pair_member','sum_rounds','sum_records','accepted_total','rejected_total','bot_error_total']} for k,v in out['campaigns'].items()},
 'comparisons':{k:{x:v[x] for x in ['matched_conditions','wdl_comparison','same_wdl_hp_rounds','same_canonical_history']} for k,v in out['matched_comparisons'].items()},
 'errors':out['raw_or_source_errors']},indent=2))

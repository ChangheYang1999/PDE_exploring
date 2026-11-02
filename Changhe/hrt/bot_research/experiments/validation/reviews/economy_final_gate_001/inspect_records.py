"""Posthoc retained-record review. Standard library only; imports no project code.
Run from project root. Writes a new dated inspection under this owned folder.
All numerical inputs are retained exactly in content-addressed gzip objects.
"""
import ast
import collections
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys

OUT = Path('bot_research/experiments/validation/reviews/economy_final_gate_001')
E = Path('bot_research/experiments/economy')
R = Path('bot_research/runs/economy')
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')
start = now()
phase = OUT / ('inspection-' + start.replace(':','').replace('-','').replace('.',''))
phase.mkdir(parents=True, exist_ok=False)
objects = OUT/'inputs'; objects.mkdir(exist_ok=True)
pins = {}; hashcache = {}; trees = {}; versions = {}; problems = []
def sha(b): return hashlib.sha256(b).hexdigest()
def capture(path):
    path=Path(path); b=path.read_bytes(); h=sha(b); f=objects/(h+'.gz')
    if not f.exists():
        z=gzip.compress(b, compresslevel=6, mtime=0); f.write_bytes(z)
        if gzip.decompress(z)!=b: raise ValueError('gzip verification failed')
    pins[str(path)]={'sha256':h,'bytes':len(b),'snapshot':str(f),'gzip_sha256':sha(f.read_bytes())}
    return b

def data(path): return json.loads(capture(path))
def lines(path): return [l.strip() for l in capture(path).decode().splitlines() if l.strip() and not l.startswith('#')]
def read_rows(path):
    b=capture(path); good=[]; bad=[]
    for i,l in enumerate(b.splitlines(),1):
        try: good.append(json.loads(l))
        except Exception as ex: bad.append({'line':i,'error':type(ex).__name__})
    return good,bad

def chk(cond,msg):
    if not cond: problems.append(msg)

def current_hash(path):
    if path not in hashcache:
        p=Path(path);hashcache[path]=sha(p.read_bytes()) if p.exists() else None
    return hashcache[path]

def module_file(name):
    p=Path(*name.split('.'))
    for q in (p.with_suffix('.py'),p/'__init__.py'):
        if q.is_file():return q

def version(module):
    if module in versions:return versions[module]
    seen={};todo=[module]
    while todo:
        name=todo.pop()
        if name in seen or not name.startswith('bot_research'):continue
        p=module_file(name)
        if p is None:continue
        seen[name]=p
        parts=name.split('.')
        todo.extend('.'.join(parts[:i]) for i in range(1,len(parts)))
        package=name if p.name=='__init__.py' else '.'.join(parts[:-1])
        if str(p) not in trees:trees[str(p)]=ast.parse(p.read_text())
        for n in ast.walk(trees[str(p)]):
            if isinstance(n,ast.Import):todo.extend(a.name for a in n.names)
            if isinstance(n,ast.ImportFrom):
                if n.level:
                    pp=package.split('.');pp=pp[:len(pp)-(n.level-1)]
                    target='.'.join(pp+([n.module] if n.module else []))
                else:target=n.module or ''
                todo.append(target);todo.extend(target+'.'+a.name for a in n.names)
    files=set(seen.values())|set(Path('bot_research/harness').glob('*.py'))
    h=hashlib.sha256()
    for p in sorted(files):h.update((str(p)+'\0'+current_hash(str(p))+'\n').encode())
    ans={'digest':h.hexdigest(),'paths':[str(p) for p in sorted(files)]};versions[module]=ans;return ans

def norm(r):
    s=r['candidate_side'];o=r['spec_b'] if s==0 else r['spec_a'];c=r['spec_a'] if s==0 else r['spec_b']
    k=(o,r.get('scenario'),s)
    if r.get('error'):return c,k,None
    w=r['winner'];return c,k,(1.0 if w==s else .5 if w is None else 0.0,r['hp_diff_a']*(1 if s==0 else -1),r['rounds'])

def wdl(d,keys):
    a=[d[k][0] for k in keys];return [a.count(x) for x in (1.0,.5,0.0)]

def boot(keys,a,b):
    keys=sorted(keys,key=lambda k:(k[0],str(k[1]),k[2]));opp=sorted({k[0] for k in keys});by=collections.defaultdict(list)
    for k in keys:by[k[0]].append(a[k][0]-b[k][0])
    mean=sum(sum(by[o]) for o in opp)/len(keys);rng=random.Random(1);ms=[]
    for _ in range(4000):
        sample=[rng.choice(opp) for _ in opp]
        ms.append(sum(sum(by[o]) for o in sample)/sum(len(by[o]) for o in sample))
    ms.sort()
    return {'mean':mean,'lo':ms[100],'hi':ms[3899],'opponents':len(opp),'conditions':len(keys),'resamples':4000,'seed':1,'sorted_indices':[100,3899]}

for path in [E/'dec22.py',E/'pooltab.py',E/'gate_vs_base.py',E/'run_tourn.sh',Path('bot_research/harness/tournament.py'),Path('bot_research/harness/match.py')]:capture(path)
notes=capture('bot_research/notes/economy.md').decode(); section=notes[notes.index('### 18.22'):]
(phase/'notes-from-18.22.md').write_text(section)
specs={tag:capture(E/'specs'/(tag+'.spec')).decode().strip() for tag in ['af5','af6','g1','v29']}
sweep=lines(E/'opp_afsweep.txt');agree=lines(E/'opp_afagree.txt');fresh5=lines(E/'opp_fresh5.txt');fresh6=lines(E/'opp_fresh6.txt');fresh=lines(E/'opp_fresh56.txt')
spools=data(E/'opp_afsweep_pools.json');fpools=data(E/'opp_fresh56_pools.json')
chk(len(sweep)==len(set(sweep))==145,'sweep spec count or uniqueness')
chk(len(agree)==len(set(agree))==257,'agree spec count or uniqueness')
chk(not set(sweep)&set(agree),'sweep and remainder overlap')
chk(fresh==fresh5+fresh6 and len(set(fresh))==43,'fresh56 concatenation or uniqueness')
chk(set(sweep)=={x for ss in spools.values() for x in ss},'sweep pool membership')
GATE=[('PCS','bot_research/runs/lead/g13pc/results.jsonl','best_v9e:@make',8),('TIMING','bot_research/runs/lead/bse_tm/results.jsonl','best_v9e:@make',32),('TIMING2','bot_research/runs/lead/tm2/results.jsonl','foreign_target',40),('STRIKE1',str(R/'strike1b/results.jsonl'),'best_v9e:@make',40),('TARGETED2','bot_research/tmp/base_t8f_v18f.jsonl','fortress_guns=true&catch_up=true',48),('f5t','bot_research/runs/lead/ab1/results.jsonl','best_v9e:@make',76),('PUNISH','bot_research/runs/lead/pu1/results.jsonl','foreign_target',34),('BLUFFCOV','bot_research/tmp/base_b9a_v18f.jsonl','foreign_target',16),('TARGETED3_P5TF','bot_research/runs/lead/t9k/results.jsonl','foreign_target',30),('HANDOFF','bot_research/runs/lead/bse_hd/results.jsonl','best_v9e:@make',36),('SCREENED','bot_research/runs/lead/bse_sg/results.jsonl','best_v9e:@make',60),('GROWERS','bot_research/runs/lead/g9a/results.jsonl','foreign_target',142),('GUARDED_MAZE','bot_research/tmp/base_gm2_v18f.jsonl','foreign_target',144),('STAGED','bot_research/tmp/base_st1_v18f.jsonl','foreign_target',140)]
bases={};base_conflicts=[];baserefs={}
for pool,path,sub,n in GATE:
    rr,bad=read_rows(path);chk(not bad,'invalid JSON in '+path);d={};refs={}
    for i,r in enumerate(rr):
        c,k,v=norm(r)
        if sub not in c or 'catch_up_share=1.0' in c or v is None:continue
        if k in d and d[k]!=v:base_conflicts.append([pool,list(k),d[k],v])
        d[k]=v;refs[k]={'path':path,'line':i+1}
    chk(len(d)==n,'base pool count '+pool);bases[pool]=d;baserefs[pool]=refs
union=set().union(*(set(v) for v in bases.values()));gate_spec={k[0] for k in union}
chk(gate_spec==set(sweep)|set(agree),'gate union differs from sweep plus remainder')
chk(all(k[1] is None and k[2] in (0,1) for k in union),'unexpected gate setting')
# Complete source result captures also preserve original row order and any duplicated results.
run_names=['gate1','fam2b','g1chk','grow1','gmaze1','hand3','hand4','pcs1','afs6','afs5','fresh5a','fresh6','afq56','afg5']
allrows={};runstatus={};missing={};d={t:{} for t in specs};refs={t:{} for t in specs};conflicts=[];duplicates=[]
source_claims=collections.defaultdict(set);entry_claims=collections.defaultdict(set);version_claims=collections.defaultdict(set)
for run in run_names:
    p=R/run/'results.jsonl'
    if not p.exists():runstatus[run]={'status':'absent','rows':0};continue
    rr,bad=read_rows(p);allrows[run]=rr
    summary=p.with_name('summary.md'); log=R/(run+'.log')
    if summary.exists():capture(summary)
    if log.exists():rawlog=capture(log).decode(errors='replace');done='done in ' in rawlog
    else:done=False
    rs={'rows':len(rr),'summary_exists':summary.exists(),'completion_line':done,'json_errors':bad,'by_candidate':{},'harness_errors':0,'rejects':0,'bot_errors':0,'source_changed':0,'scenario_errors':0}
    byc=collections.defaultdict(list)
    for i,r in enumerate(rr):
        c,k,v=norm(r);byc[c].append((k,v));rs['harness_errors']+=bool(r.get('error'))
        if v is None:continue
        chk(r['hp_a']-r['hp_b']==r['hp_diff_a'],'HP arithmetic '+run+':'+str(i+1))
        chk(r['winner'] in (0,1,None),'winner type')
        rs['source_changed']+=bool(r.get('source_changed'));rs['rejects']+=sum(x['n_rejected'] for x in r['players']);rs['bot_errors']+=sum(len(x['bot_errors']) for x in r['players']);rs['scenario_errors']+=sum(len(x) for x in r.get('scenario_errors',[]))
        for path,h in r.get('sources',{}).items():source_claims[path].add(h)
        for side in 'ab':
            module=r['spec_'+side].split(':')[0];entry_claims[module].add(r['hash_'+side]);version_claims[module].add(r['version_'+side])
        for tag,spec in specs.items():
            if c!=spec:continue
            if k in d[tag]:
                if d[tag][k]!=v:conflicts.append({'tag':tag,'condition':k,'first':refs[tag][k],'second':[run,i+1],'values':[d[tag][k],v]})
                else:duplicates.append({'tag':tag,'condition':k,'first':refs[tag][k],'second':[run,i+1]})
            else:d[tag][k]=v;refs[tag][k]=[run,i+1]
    for c,a in byc.items():
        dd={k:v for k,v in a if v is not None};opps={k[0] for k in dd}; paired=[]
        for o in sorted(opps):
            aa=dd.get((o,None,0));bb=dd.get((o,None,1))
            if aa is not None and bb is not None and aa!=bb:paired.append(o)
        rs['by_candidate'][c]={'rows':len(a),'unique':len(dd),'wdl':wdl(dd,dd),'paired_outcome_margin_round_disagreements':paired,'max_call':max((r['decide_max_seconds'][r['candidate_side']] for r in rr if not r.get('error') and (r['spec_a'] if r['candidate_side']==0 else r['spec_b'])==c),default=None)}
    runstatus[run]=rs
for item in conflicts:d[item['tag']].pop(tuple(item['condition']),None)

expected={'afs5':('af5',sweep),'afs6':('af6',sweep),'afq56':('af5',fresh),'afg5':('af5',agree)}
for run,(tag,opps) in expected.items():
    target={(o,None,s) for o in opps for s in (0,1)}
    rows=allrows.get(run,[]);actual=[norm(r)[1] for r in rows if norm(r)[0]==specs[tag] and norm(r)[2] is not None]
    state=runstatus[run];state.update({'expected':len(target),'completed_conditions':len(set(actual)),'duplicate_conditions':len(actual)-len(set(actual)),'unexpected_conditions':[list(k) for k in set(actual)-target],'missing_conditions':[list(k) for k in sorted(target-set(actual))]})
    state['complete']=len(actual)==len(target) and set(actual)==target and not state.get('json_errors') and not state.get('harness_errors') and state.get('summary_exists',False) and state.get('completion_line',False)

# Per-pool counts preserve the lead's overlapping named pools; union table deduplicates them.
def table(keys,tags):
    kk=set(keys)
    for tag in tags:kk &= set(d[tag])
    out={'conditions':len(kk),'opponents':len({k[0] for k in kk}),'wdl':{t:wdl(d[t],kk) for t in tags},'paired':{}}
    for tag in tags[1:]:
        if kk:out['paired'][tags[0]+'-'+tag]=boot(kk,d[tags[0]],d[tag])
    return out
sweepkeys={(o,None,s) for o in sweep for s in (0,1)}
sweeptables={pool:table({(o,None,s) for o in ss for s in (0,1)},['af5','af6','g1','v29']) for pool,ss in spools.items()};sweeptables['ALL']=table(sweepkeys,['af5','af6','g1','v29'])
qual={}
for tag in ['af6','af5']:
    deficits={pool:wdl(d[tag],{(o,None,s) for o in ss for s in (0,1)}&set(d[tag]))[0]-wdl(d['g1'],{(o,None,s) for o in ss for s in (0,1)}&set(d['g1']))[0] for pool,ss in spools.items()}
    total=wdl(d[tag],sweepkeys&set(d[tag]))[0];qual[tag]={'wins':total,'pool_win_difference_to_g1':deficits,'qualifies':sweepkeys<=set(d[tag]) and total>wdl(d['g1'],sweepkeys&set(d['g1']))[0] and min(deficits.values())>=-2}
chosen=max((t for t in ['af6','af5'] if qual[t]['qualifies']),key=lambda t:(qual[t]['wins'],t=='af6'),default=None)
gate_tables={pool:table(keys,['af5','g1','v29']) for pool,keys in bases.items()};gate_tables['UNIQUE']=table(union,['af5','g1','v29'])
freshkeys={(o,None,s) for o in fresh for s in (0,1)}
fresh_tables={pool:table({k for k in freshkeys if pool in fpools[k[0]]},['af5','g1','v29']) for pool in sorted({p for v in fpools.values() for p in v})};fresh_tables['ALL']=table(freshkeys,['af5','g1','v29'])
agreekeys={(o,None,s) for o in agree for s in (0,1)}
base_disagree=[list(k) for k in sorted(agreekeys) if k not in d['g1'] or k not in d['v29'] or d['g1'][k][0]!=d['v29'][k][0]]
observedagree=agreekeys&set(d['af5'])&set(d['g1'])
agree_diff=[list(k) for k in sorted(observedagree) if d['af5'][k][0]!=d['g1'][k][0]]
sourcechecks=[]
for path,hs in sorted(source_claims.items()):sourcechecks.append({'path':path,'recorded':sorted(hs),'current':current_hash(path),'all_recorded_equal_current':hs=={current_hash(path)}})
entrychecks=[]
for module,hs in sorted(entry_claims.items()):
    p=module_file(module);h=current_hash(str(p)) if p else None;v=version(module)
    entrychecks.append({'module':module,'path':str(p),'entry_recorded':sorted(hs),'entry_current':h,'entry_match':hs=={h},'versions_recorded':sorted(version_claims[module]),'current_version':v['digest'],'all_versions_equal_current':version_claims[module]=={v['digest']}})
source_scope={'loaded':sourcechecks,'entries':entrychecks,'static_closures':versions,'current_source_hashes':hashcache}
# Retain the exact current source bytes used by current-identity and static checks.
for path in sorted(hashcache):
    if hashcache[path] is not None:capture(path)

result={'started_utc':start,'finished_utc':now(),'reviewer':'GPT-6 Astra','mode':'posthoc source/result JSON only; no project imports, policy, Engine, replay, game or test calls','specs':specs,'run_status':runstatus,'problems':problems,'base_conflicts':base_conflicts,'duplicate_lane_rows':duplicates,'conflicting_lane_rows':conflicts,'denominators':{'pool_occurrence_conditions':sum(len(v) for v in bases.values()),'unique_gate_conditions':len(union),'unique_gate_specs':len(gate_spec),'sweep_specs':len(sweep),'remaining_specs':len(agree),'fresh_specs':len(fresh),'fresh_gate_overlap':sorted(set(fresh)&gate_spec),'sweep_pool_occurrence_specs':sum(len(v) for v in spools.values())},'sweep':sweeptables,'selection':{'qualifications':qual,'choice':chosen},'gate':gate_tables,'fresh56':fresh_tables,'remainder':{'base_outcome_disagreements':base_disagree,'observed_conditions':len(observedagree),'changed_outcomes':len(agree_diff),'changed_conditions':agree_diff,'complete':runstatus['afg5']['complete'],'prediction_pass_if_complete':len(agree_diff)<=25 if runstatus['afg5']['complete'] else None},'source_identity':source_scope,'notes_snapshot':pins['bot_research/notes/economy.md']}
(phase/'inspection.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
(phase/'inputs.json').write_text(json.dumps({'captured_utc':now(),'inputs':pins,'inspector_sha256':sha(Path(__file__).read_bytes())},indent=2,sort_keys=True)+'\n')
print(json.dumps({'folder':str(phase),'finished':result['finished_utc'],'counts':result['denominators'],'selection':result['selection'],'run_status':{k:{a:v for a,v in v.items() if a in ['rows','complete','expected','completed_conditions']} for k,v in runstatus.items()},'problems':problems,'conflicts':len(conflicts),'loaded_source_mismatches':sum(not x['all_recorded_equal_current'] for x in sourcechecks),'version_mismatches':sum(not x['all_versions_equal_current'] for x in entrychecks),'sweep_all':sweeptables['ALL']},indent=2))

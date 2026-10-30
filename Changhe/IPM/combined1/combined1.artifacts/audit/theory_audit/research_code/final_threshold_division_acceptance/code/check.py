"""Independent Fraction replay of N4-429 threshold divisions."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import ast,hashlib,json,re,time
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads((B/p).read_text())
def need(n,x):
 assert bool(x),n
 checks.append(n)
def endpoints(s):
 m=re.fullmatch(r'\[([^\[\]]+) \+/- ([^\[\]]+)\]',s);need('ball syntax '+s[:24],m is not None);a,b=map(Q,m.groups());need('nonnegative ball radius '+s[:24],b>=0);return a-b,a+b
for x in load('data/manifest.json'):need('input '+x['local'],sha(B/x['local'])==x['sha256'])
need('proof first',not load('data/PROOF_FIRST.json')['checker_exists']);ast.parse((B/'source/N4_check.py').read_text());j=load('source/N4_result.json');need('N4_42937checks',j['check_count']==len(j['checks'])==37 and all(j['checks'].values()))
bindings=load('data/external_bindings.json');need('completeproducerbindings',{x['producer_relative']:x['sha256'] for x in bindings}==j['inputs'])
for x in load('data/initial_sources.json')['sources']:
 rel=x['source'].split('/c1-n4/',1)[1]
 if rel in j['inputs']:need('frozen producer source '+rel,x['sha256']==j['inputs'][rel])
o=load('source/N3_old.json');n=load('source/N3_new.json');p=load('data/parameters.json');text=(B/'source/N3_summary.md').read_text();rows=[]
need('candidate007',o['id']==n['id']=='C1-N1-007-d2w-j7-e2bal')
need('same raw candidate',o['source_sha256']==n['source_sha256']=='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21')
for key in ['components','derived']:need('unchanged '+key,o[key]==n[key])
for role in ['X3','Ns']:
 param=p[role];name=param['framework'];tau=Q(param['threshold']);floor=Q(param['floor']);a=o['thresholds'][name];b=n['thresholds'][name];L,U=Q(b['LB']),Q(b['UB']);ratio=L/tau
 need(role+'positive exact threshold',tau==Q(b['threshold']) and L>0 and tau>0)
 need(role+'unchanged bounds',L==Q(a['LB']) and U==Q(a['UB']))
 need(role+'exact integer floor',floor<ratio<floor+1)
 lo,hi=endpoints(b['LB/threshold']);need(role+'rounded lower compatible',0<lo-ratio<Q(1,10**15) and floor<lo<hi)
 line=next(x for x in text.splitlines() if x.startswith('| '+name+' |'));cells=[x.strip() for x in line.split('|')[1:-1]]
 need(role+'summarythreshold',Q(cells[3])==tau)
 need(role+'summaryfloor',Q(cells[4])==floor)
 need(role+'summaryoutwardbounds',Q(cells[1])<=L and Q(cells[2])>=U)
 peer=next(x for x in j['rows'] if x['role']==role)
 need(role+'peer exact data',L==Q(peer['L_exact']) and tau==Q(peer['threshold_exact']) and ratio==Q(peer['ratio_of_printed_L_exact']) and floor==Q(peer['repaired_floor_exact']))
 rows.append({'role':role,'L_exact':str(L),'upper_comparison_exact':str(U),'threshold_exact':str(tau),'ratio_exact':str(ratio),'floor_exact':str(floor),'ball_lower_exact':str(lo),'printed_lower_gap_exact':str(lo-ratio)})
x,nold=[o['thresholds'][p[k]['framework']] for k in ['X3','Ns']];tx,tn=map(Q,[p['X3']['threshold'],p['Ns']['threshold']]);LX,LN=Q(x['LB']),Q(nold['LB'])
need('oldXthreshold',Q(x['threshold'])-tx==-Q(1,64000000000))
need('oldNthreshold',Q(nold['threshold'])-tn==Q(17,640000000000))
need('oldXunsupportedquotient',LX/tx<Q(84699902)<LX/Q(x['threshold']))
need('oldNconservative',LN/Q(nold['threshold'])<LN/tn)
base=load('source/N4_252_result.json');rr=next(x for x in base['instances'] if x['framework']=='FW-T-TB-rebal-v1')
need('accepted252threshold',Q(rr['threshold_exact'])==tn)
need('accepted252factor',Q(rr['lower_comparison']['strict_lower_exact'])/tn>Q(p['Ns']['floor']))
counts={}
for name in ['report.md','matrix.md','numerics.md']:
 txt=(B/'source'/name).read_text();counts[name]={sp:txt.count(sp) for sp in p['old_spellings']};need(name+'named spellings absent',not any(counts[name].values()));need(name+'sameproducercounts',counts[name]==j['old_literal_occurrences'][name])
for x in load('data/manifest.json'):need('unchanged '+x['local'],sha(B/x['local'])==x['sha256'])
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(B/'code/check.py'),'producer_inputs_rehashed':len(bindings),'rows':rows,'old_spellings':counts,'foreign_code_executed':False,'candidate_integrals_repeated':False,'verdict':'CONFIRMED N4-429 exact divisions and finite spelling scope; old84699902 refuted only as the same lower-comparison quotient, not as an actual norm bound.'}
with (B/'verification/result.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print(r['utc'],len(checks),'checks',r['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))

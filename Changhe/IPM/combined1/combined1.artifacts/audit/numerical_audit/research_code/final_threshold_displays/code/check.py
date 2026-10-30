"""Exact comparison of final threshold displays; no PDE source promotion."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json,re,os,time
R=Path(__file__).resolve().parents[3];B=R/'research/final_threshold_displays'
assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
start=time.monotonic();inputs={};checks={}
def bind(p,h=None):
 p=Path(p);p=p if p.is_absolute() else R/p
 assert p.resolve().is_relative_to(R);value=hashlib.sha256(p.read_bytes()).hexdigest();assert h is None or value==h
 inputs[str(p.relative_to(R))]=value;return p
def read(p,h=None):return json.loads(bind(p,h).read_text())
def ck(name,test):assert name not in checks;checks[name]=bool(test)
def ball(s):
 m=re.fullmatch(r'\[([^\[\]]+) \+/- ([^\[\]]+)\]',s);assert m
 a,b=map(Q,m.groups());assert b>=0;return a-b,a+b
assert not (B/'verification/result.json').exists()
p=read(B/'verification/PROOF_FIRST.json');assert not p['checker_exists'] and not p['result_exists'];bind(B/'PROOF.md',p['proof_sha256']);bind(Path(__file__))
m=read(B/'source/MANIFEST.json')
for rel,h in m['files'].items():bind(rel,h)
old=read(B/'source/N3_old.json');new=read(B/'source/N3_new.json');summary=(B/'source/N3_summary.md').read_text()
ck('identity',old['id']==new['id']=='C1-N1-007-d2w-j7-e2bal')
ck('raw007',old['source_sha256']==new['source_sha256']=='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21')
ck('same_components',old['components']==new['components']);ck('same_derived',old['derived']==new['derived'])
labels={'X3':'FW-T-T4L2-v1 (NORM-T-X3-v1, s=2^-17)','Ns':'FW-T-TB-rebal-v1 (NORM-T-Ns16-v1)'}
thresholds={'X3':Q(1,163840),'Ns':Q(3,327680)};floors={'X3':Q(84699685),'Ns':Q(66246337)};rows=[]
for role,label in labels.items():
 o,n=old['thresholds'][label],new['thresholds'][label];tau=thresholds[role];L=Q(n['LB']);oldL=Q(o['LB']);ck(role+'positive',L>0 and tau>0)
 ck(role+'unchanged_LB',oldL==L);ck(role+'unchanged_UB',Q(o['UB'])==Q(n['UB']));ck(role+'exact_threshold',Q(n['threshold'])==tau)
 lo,hi=ball(n['LB/threshold']);ck(role+'stored_ratio_consistent_with_rounded_L',0<lo-L/tau<Q(1,10**15))
 ck(role+'repaired_floor',floors[role]<L/tau);ck(role+'stored_ball_floor',floors[role]<lo)
 line=next(line for line in summary.splitlines() if line.startswith('| '+label+' |'));cells=[x.strip() for x in line.split('|')[1:-1]]
 ck(role+'summary_exact_threshold',Q(cells[3])==tau);ck(role+'summary_repaired_floor',Q(cells[4])==floors[role])
 ck(role+'summary_L_directed',Q(cells[1])<=L);ck(role+'summary_U_directed',Q(cells[2])>=Q(n['UB']))
 rows.append({'role':role,'L_exact':str(L),'threshold_exact':str(tau),'ratio_of_printed_L_exact':str(L/tau),'repaired_floor_exact':str(floors[role]),'source_ratio_ball':n['LB/threshold'],'summary_line':line})
x=old['thresholds'][labels['X3']];n=old['thresholds'][labels['Ns']]
ck('old_X3_error',Q(x['threshold'])-thresholds['X3']==-Q(1,64000000000))
ck('old_Ns_error',Q(n['threshold'])-thresholds['Ns']==Q(17,640000000000))
ck('old_X3_inflates',Q(x['LB'])/Q(x['threshold'])>Q(x['LB'])/thresholds['X3'])
ck('old_Ns_conservative',Q(n['LB'])/Q(n['threshold'])<Q(n['LB'])/thresholds['Ns'])
ck('old_display_unsupported_by_same_L',Q(84699902)>Q(x['LB'])/thresholds['X3'])
ck('old_display_below_old_division',Q(84699902)<Q(x['LB'])/Q(x['threshold']))
e=read(R/'research/negative_norm_forcing_assembly/verification/result.json');rebal=next(r for r in e['instances'] if r['framework']=='FW-T-TB-rebal-v1')
ck('own252_exact_threshold',Q(rebal['threshold_exact'])==thresholds['Ns'])
ck('own252_actual_lower_supports_new_floor',Q(rebal['lower_comparison']['strict_lower_exact'])/thresholds['Ns']>floors['Ns'])
spellings=['8.4699902e+7','8.4699902e7','84699902'];absences={}
for name in ['report.md','matrix.md','numerics.md']:
 text=(B/'source'/name).read_text();absences[name]={s:text.count(s) for s in spellings};ck(name+'no_old_literal',not any(absences[name].values()))
out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':inputs,'checks':checks,'check_count':len(checks),'rows':rows,'old_literal_occurrences':absences,'old_X3_transcription':'REFUTED as a quotient of the same saved lower comparison by exact1/163840; no upper statement about the actual norm','verdict':'CONFIRMED listed corrected divisions and finite literal scope' if all(checks.values()) else 'OPEN: inspect failed checks','underlying_integrals_recomputed':False,'peer_code_executed':False,'elapsed_seconds':time.monotonic()-start}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'checks':len(checks),'inputs':len(inputs),'failed':[k for k,v in checks.items() if not v],'sha256':hashlib.sha256((B/'verification/result.json').read_bytes()).hexdigest(),'elapsed_seconds':out['elapsed_seconds']},indent=2))

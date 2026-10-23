"""Source endpoint and finite-record counting; no producer code execution."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from collections import Counter
import ast,json,hashlib
R=Path('research/hydrostatic_common_residual_audit');V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[];bindings={}
def ck(n,b):
 checks.append({'name':n,'passed':bool(b)})
 if not b:raise AssertionError(n)
def literals(n):
 if isinstance(n,(ast.List,ast.Tuple)):return [literals(x) for x in n.elts]
 if isinstance(n,ast.Constant) and type(n.value) in (int,float):return n.value
 if isinstance(n,ast.BinOp) and isinstance(n.op,ast.Add):
  a,b=literals(n.left),literals(n.right)
  if type(a) in (int,float) and type(b) in (int,float):return a+b
 raise ValueError(ast.dump(n))
p=V/'producer_definition_static.py';tree=ast.parse(p.read_text());assignments=[n.value for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='regs' for x in n.targets)]
ck('unique interval assignment',len(assignments)==1);intervals=literals(assignments[0]);ck('full source interval list',intervals==[[0,.1],[.1,1],[1,100],[100,1e4],[1e4,1000001]])
ck('outer ring included',intervals[-1][0]<=1000000<intervals[-1][1]);bindings[str(p)]=sha(p)
p=V/'FINAL_SCOPE_CHECKS.json';scope=json.loads(p.read_text());bindings[str(p)]=sha(p);ck('parent completed',scope['status']=='PASS_SCOPED_FINITE_ARRAYS' and scope['count']==259 and all(x['passed'] for x in scope['checks']))
for p,h in scope['bindings'].items():ck('bound '+p,sha(p)==h);bindings[p]=h
rows=[]
def triple(t):return (t['tag'],t['region'],t['metric'])
def kind(changed):return 'both' if all(changed) else 'fixed_only' if changed[0] else 'adaptive_only' if changed[1] else 'neither'
for t in scope['tokens']:
 center=F(t['printed']);half=F(t['half_width']);base=[abs(F(t[k]['value'])-center)<=half for k in ['fixed','adaptive']];baseval=[t[k]['value_float'] for k in ['fixed','adaptive']]
 changed=[s for s in t['counterfactual_masks'] if s['changes_pair']];labels=[[s['interval_membership_pair'][i]!=base[i] for i in range(2)] for s in changed]
 ck('counterfactual pair '+str(len(rows)),all(any(x) for x in labels) and bool(changed)==(t['unexported_producer_mask_comparison']=='OPEN'))
 values=[[s['fixed_value']!=baseval[0],s['adaptive_subset_value']!=baseval[1]] for s in changed]
 overall=[any(x[i] for x in labels) for i in range(2)]
 rows.append({'version':t['version'],'source':t['source'],'triple':list(triple(t)),'printed':t['printed'],'mask_sensitive':bool(changed),'label_change_class':kind(overall),'changed_scenario_label_classes':dict(Counter(kind(x) for x in labels)),'changed_scenario_value_classes':dict(Counter(kind(x) for x in values)),'fixed_max_index':t['fixed']['index'],'adaptive_max_index':t['adaptive']['index'],'axis':t['vertical_axis_maximum'],'interior_boundary':t['region_boundary_maximum'],'outer_ring':[t[k]['index']//9==36 for k in ['fixed','adaptive']],'posthoc_cut_to_halfwidth':str(F('1e-3')*abs(center)/half)})
ck('all records',len(rows)==187);affected=[x for x in rows if x['mask_sensitive']];distinct=set(tuple(x['triple']) for x in rows);affected_distinct=set(tuple(x['triple']) for x in affected)
ck('parent84reproduced',len(affected)==84)
counts={'records':len(rows),'distinct_triples':len(distinct),'mask_sensitive_records':len(affected),'mask_sensitive_distinct_triples':len(affected_distinct),'affected_record_label_classes':dict(Counter(x['label_change_class'] for x in affected)),'changed_scenario_label_classes':dict(sum((Counter(x['changed_scenario_label_classes']) for x in rows),Counter())),'changed_scenario_value_classes':dict(sum((Counter(x['changed_scenario_value_classes']) for x in rows),Counter()))}
for key in ['axis','interior_boundary','outer_ring']:
 counts[key]={}
 for meth,which in [('fixed',0),('adaptive',1),('either',None)]:
  selected=[x for x in rows if any(x[key]) if which is None] if which is None else [x for x in rows if x[key][which]]
  counts[key][meth]={'records':len(selected),'distinct_triples':len(set(tuple(x['triple']) for x in selected))}
counts['any_boundary']={}
for meth,which in [('fixed',0),('adaptive',1),('either',None)]:
 selected=[x for x in rows if any(x['interior_boundary']) or any(x['outer_ring'])] if which is None else [x for x in rows if x['interior_boundary'][which] or x['outer_ring'][which]]
 counts['any_boundary'][meth]={'records':len(selected),'distinct_triples':len(set(tuple(x['triple']) for x in selected))}
zeroT=[{'region':reg,'zero_T_rows':sum(x['region']==reg and F(x['T'])==0 for x in scope['bridge_witnesses']),'total_rows':sum(x['region']==reg for x in scope['bridge_witnesses'])} for reg in range(5)]
ck('all295bridge rows',sum(x['total_rows'] for x in zeroT)==295)
ck('zero T ratios handled',all((all(y is None for y in x['absolute_over_T'].values()) if F(x['T'])==0 else all(y is not None for y in x['absolute_over_T'].values())) for x in scope['bridge_witnesses']))
ck('inverse_only present',all('inverse_only' in x['absolute_over_T'] for x in scope['bridge_witnesses']))
for p in [Path(__file__),R/'SECOND_NUMERICAL_REVIEW_RESOLUTION_PROOF.md',V/'opus_numerical_followup/metadata.json',V/'opus_numerical_followup/answer.md']:bindings[str(p)]=sha(p)
out={'status':'PASS_SCOPED_FINITE_ARRAYS','utc':datetime.now(timezone.utc).isoformat(),'count':len(checks),'checks':checks,'bindings':bindings,'source_intervals':intervals,'source_outer_endpoint':intervals[-1][1],'producer_execution_endpoints':'not exported','counts':counts,'zero_T_by_region':zeroT,'tokens':rows,'axis_perturbation_sensitivity':'UNTESTED; counts only','bridge_key_map':{'inverse_only':'held-local-jet velocity contribution'},'timestamp_scope':'ordering and hashes consistent with checkpoint-writer account, not evidence for or against post-run editing','cut_scope':'post hoc descriptive relative excess1e-3, no accuracy bound','scope':'finite represented values only; true auxiliary inverse error OPEN; primary full-plane UNRESOLVED'}
(V/'SCOPE_COUNT_CHECKS.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(out['status'],out['count']);print(json.dumps(counts,indent=2));print(zeroT)

from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,math
import numpy as np
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';checks=[];bindings={};outputs={}
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e));assert b,(n,e)
def bind(p,h=None):
 p=str(p);hh=hashlib.sha256(Path(p).read_bytes()).hexdigest();ck('binding '+p,(h is None or hh==h)and(p not in bindings or bindings[p]==hh));bindings[p]=hh;return Path(p)
def f(x):return F.from_float(float(x))
def gap(a,b):
 z=abs(a-b);den=max(abs(a),abs(b));return z,z/den if den else None
def rec(z):return dict(exact=str(z)if z is not None else None,value=float(z)if z is not None else None)
def resid(x,y,j,v):return(2*x+v[0])*j[1]+(2*y+v[1])*j[2]-j[0]
def firstmax(values):return max(range(len(values)),key=lambda i:values[i]if values[i]is not None else F(-1))
bind(__file__);bind(R/'FINAL_COMPONENT_AND_INTERPRETATION_PROOF.md')
ck('hand signed pair',gap(F(-2),F(3))==(F(5),F(5,3)))
ck('hand bothzero',gap(F(0),F(0))==(F(0),None))
ck('hand exacttie',firstmax([F(1),F(2),F(2)])==1)
ck('hand orthogonal projection',3*2-2*3==0 and gap(F(3),F(0))[0]==3)
s=json.loads(bind(V/'FINAL_SUMMARY_CHECKS.json','35cf718cf57daedec9c2ff9e0203e6a1a45e9a736a3c79840c4e725c89669f58').read_text());ck('summary PASS',s['status']=='PASS_FINITE_RECOMPUTATION_REQUIRES_ACTUAL_REVIEW'and s['count']==60871 and all(z['passed']for z in s['checks']))
for p,h in s['bindings'].items():bind(p,h)
z={tag:np.load(V/'candidate_inverse'/f'{tag}.npz',allow_pickle=False)for tag in ['A','B','C']}
rules=json.loads((V/'candidate_inverse/RULES_COMPLETE.json').read_text());sel=json.loads((V/'candidate_inverse/SELECTION.json').read_text());exp=np.load(V/'source_nodes_maps.npz',allow_pickle=False);jet=np.load(V/'actual_node_jets.npz',allow_pickle=False)
X=jet['X'];Y=jet['Y'];J=[[f(a)for a in row[:3]]for row in jet['own_jet']];vm=[[f(exp['V1_map'][i]),f(exp['V2_map'][i])]for i in range(2304)];vp=[[f(exp['V1_ref'][i]),f(exp['V2_ref'][i])]for i in range(2304)];vel={t:{int(i):list(map(f,row))for i,row in zip(z[t]['indices'],z[t]['velocity'])}for t in z}
outs=[]
for t in ['A','B']:
 for name,ref in [('Vm',vm),('Vp',vp)]:
  for k in range(2):
   diffs=[gap(vel[t][i][k],ref[i][k])for i in range(2304)];row=dict(rule=t,reference=name,component=k+1,count=2304,both_zero_count=sum(q[1]is None for q in diffs))
   for metric,col in [('absolute',0),('pure_relative',1)]:
    vals=[a[col]for a in diffs];i=firstmax(vals);row[metric]=dict(index=i,x=float(X[i]),y=float(Y[i]),**rec(vals[i]),rule_value=str(vel[t][i][k]),reference_value=str(ref[i][k]))
    ck('selected component maximum '+str((t,name,k,metric)),i in sel['indices'])
   outs.append(row)
outputs['all_node_component_maxima']=outs
pairs=[]
for rr in rules['stability']:
 i=rr['index'];calculated=[]
 for k in range(2):
  for a,b in [('C','B'),('C','A'),('A','B')]:
   ab,rel=gap(vel[a][i][k],vel[b][i][k]);p=dict(component=k+1,pair=[a,b],absolute=float(ab),pure_relative=float(rel)if rel is not None else None,both_zero=rel is None);calculated.append(p);pairs.append(dict(index=i,x=float(X[i]),y=float(Y[i]),component=k+1,pair=[a,b],absolute=rec(ab),pure_relative=rec(rel),both_zero=rel is None))
 ck('all exact recorded component pairs '+str(i),calculated==rr['component_spreads'])
 ss=F(rr['exact_operands'][0]);rb=resid(f(X[i]),f(Y[i]),J[i],vel['B'][i]);ck('separate spread-to-B criterion '+str(i),rr['zero_R_B']==(rb==0)and rr['within_one_percent_of_abs_R_B']==(ss<=abs(rb)/100 if rb else None))
outputs['witness_component_pairs']=pairs
outputs['witness_component_maxima']=[]
for k in [1,2]:
 pp=[x for x in pairs if x['component']==k]
 for metric in ['absolute','pure_relative']:
  best=max(pp,key=lambda p:F(p[metric]['exact'])if p[metric]['exact']is not None else F(-1));outputs['witness_component_maxima'].append(dict(component=k,metric=metric,**best))
ro=[];rb=[];dv=[]
for i in range(2304):
 x,y=f(X[i]),f(Y[i]);a=resid(x,y,J[i],vm[i]);b=resid(x,y,J[i],vel['B'][i]);c=sum((vel['B'][i][k]-vm[i][k])*J[i][k+1]for k in range(2));ck('exact samejet identity '+str(i),b==a+c);ro.append(a);rb.append(b);dv.append(c)
ck('fixed-map residual bound 4e-8',max(map(abs,ro))<F(4,10**8));outputs['fixed_map_max_absolute']=rec(max(map(abs,ro)));outputs['headline_decompositions']=[]
for region in s['outputs']['regional_summaries']['B']:
 for name,mx in region['metrics'].items():
  i=mx['index'];outputs['headline_decompositions'].append(dict(region=region['region'],maximized_quantity=name,index=i,x=float(X[i]),y=float(Y[i]),R_B=rec(rb[i]),R_own_map=rec(ro[i]),velocity_projection=rec(dv[i]),map_residual_over_B_abs=rec(abs(ro[i])/abs(rb[i])if rb[i]else None)))
outputs['metadata']={}
for t,a in z.items():
 meta=json.loads(str(a['manifest']));names=meta['columns']['metadata'];out={}
 for j,name in enumerate(names):
  vals=a['metadata'][:,j];ck('finite metadata '+str((t,name)),np.isfinite(vals).all());lo=int(np.argmin(vals));hi=int(np.argmax(vals));out[name]=dict(min=float(vals[lo]),min_index=int(a['indices'][lo]),max=float(vals[hi]),max_index=int(a['indices'][hi]),sum=float(vals.sum()))
 outputs['metadata'][t]=out
 ck('positive minimum panels and no axis '+t,out['minimum_panel_width']['min']>0 and out['x_axis_imposed']['sum']==0 and out['y_axis_imposed']['sum']==0)
# Exact reproduction of the decimal table (numeric fields parsed as floats).
import csv
rows=list(csv.DictReader(bind(V/'B_REGIONAL_MAXIMA.csv').open()))
ck('table row count',len(rows)==12)
for row,mx in zip(rows,outputs['headline_decompositions']):
 i=mx['index'];ck('table location '+str(i),int(row['index'])==i and f(row['x'])==f(X[i])and f(row['y'])==f(Y[i]))
 ck('table exact rounded fields '+str(i),[f(row[k])for k in ['R','Nf','Nv','Rf','Rv']]==list(map(f,z['B']['residual'][i])))
for p,h in list(bindings.items()):ck('stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='PASS_FINITE_COMPONENTS_AND_MAP_DECOMPOSITION',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,outputs=outputs,scope='Exact finite stored-operand component and residual differences; no inverse error enclosure or causal conclusion.')
(V/'FINAL_COMPONENT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],len(bindings),out['utc'])
for p in outputs['all_node_component_maxima']:
 if p['reference']=='Vm':print('MAP',p['rule'],p['component'],[(k,p[k]['value'],p[k]['index'])for k in ['absolute','pure_relative']])
for p in outputs['witness_component_maxima']:print('PAIR',p['component'],p['metric'],p[p['metric']]['value'],p['index'],p['pair'])
print('headline map fraction',[x['map_residual_over_B_abs']['value']for x in outputs['headline_decompositions']])
print('meta',outputs['metadata'])

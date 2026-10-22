"""Independent exact identities and saved-column comparisons; no physical field inference."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import ast,hashlib,json,math
from flint import arb,ctx
from mpmath import iv
ctx.prec=384;iv.dps=140
B=Path(__file__).resolve().parents[3];D=B/'research/x3_closure_diagnostics'
def need(x,s):
 if not x:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def scalar(x):
 need(type(x) is float and math.isfinite(x),'finite binary64 scalar');return F.from_float(x)
def ab(x):return arb(x.numerator)/arb(x.denominator)
def ib(x):return iv.mpf(x.numerator)/iv.mpf(x.denominator)
def endpoint(t):
 s,m,e,b=t;need(b>=0,'finite interval endpoint');return (-1)**s*F(m)*F(2)**e
def enclose(x,y):
 q=y/x;v=ab(y)/ab(x);w=ib(y)/ib(x);l,h=F(str(v.lower().fmpq())),F(str(v.upper().fmpq()));il,ih=map(endpoint,w._mpi_);need(l<=q<=h and il<=q<=ih,'exact ratio in both interval engines');return {'exact':str(q),'arb':[str(l),str(h)],'iv':[str(il),str(ih)],'display':float(q)}
r=load(D/'evidence/check.json');need(r['status']=='PASS_SAVED_MAXIMA_REPORT_AND_EXACT_FAR_POWER_ORDER','prior independent actual check');pins=dict(r['files'])
for n,h in pins.items():need(sha(B/n)==h,'prior pin')
m=load(D/'data_exact/manifest.json');origin={Path(x['copy']).name:x for x in m['origins']}
need(all(origin['x3_resid.py']['original_mtime_ns']>origin[n+'.json']['original_mtime_ns'] for n in ['base']+m['variants']),'captured evaluator postdates all lead outputs')
need(all(origin['inverse.py']['original_mtime_ns']>origin[n]['original_mtime_ns'] for n in ['resid_N16875_q512.json','resid_N22500_q768.json']),'inverse postdates both original outputs')
p=load(D/'data_exact/parameters.json');k=F(p['k']);exactp=F(p['p']);need(exactp==6+2*k/(2-k) and exactp.denominator%2==1 and exactp.denominator>1,'derived non-dyadic p identity')
def dd(x):return ast.dump(x,include_attributes=False)
tree=ast.parse((D/'sources/num/x3_resid.py').read_text())
for s in ['rho_x[:, -1] = 0.0','eps[:, -1] = 0.0','eps[:, 0] = 0.0']:
 target=dd(ast.parse(s).body[0]);need(any(dd(n)==target for n in ast.walk(tree)),'explicit axis assignment')
base=load(D/'sources/lead/base.json');names=['base','td05','td20','ext1e11','tp_none','tp_lead'];records=[];equality=[];nr=0
for name in names:
 v=load(D/'sources/lead'/f'{name}.json');rr={lab:{x['region']:x for x in v['results'][lab]['rows']} for lab in ['stored','identity']};bb={lab:{x['region']:x for x in base['results'][lab]['rows']} for lab in ['stored','identity']}
 near={}
 for col in m['columns']:
  x=scalar(rr['stored']['r<=0.1'][col][0]);y=scalar(rr['identity']['r<=0.1'][col][0]);need(x>0 and y>0,'positive near-center maxima');near[col]={'stored_exact':str(x),'identity_exact':str(y),'stored_display':float(x),'identity_display':float(y),'identity_over_stored':enclose(x,y)};nr+=1
 records.append({'name':name,'computed_c_exact':str(scalar(v['c'])),'computed_c_display':v['c'],'delta_c_from_baseline_exact':str(scalar(v['c'])-scalar(base['c'])),'same_computed_c_as_baseline':v['c']==base['c'],'near_center_maxima':near})
 if name in ['td05','ext1e11']:
  for lab in ['stored','identity']:
   same=[];different=[]
   for g in m['regions']:
    for col in m['columns']:
     old=scalar(bb[lab][g][col][0]);new=scalar(rr[lab][g][col][0]);record={'region':g,'column':col}
     if old==new:same.append(record)
     else:
      record.update(base_exact=str(old),variant_exact=str(new),ratio=enclose(old,new));different.append(record);nr+=1
   equality.append({'name':name,'label':lab,'equal_maxima_count':len(same),'changed_maxima_count':len(different),'equal_maxima':same,'changed_maxima':different})
need(all(e['equal_maxima_count']==23 and e['changed_maxima_count']==1 for e in equality),'actual exact equalities in both columns')
need(records[0]['computed_c_exact']==records[1]['computed_c_exact']==records[2]['computed_c_exact']==records[3]['computed_c_exact'],'computed c identical across baseline/window/extension files')
for lab in ['stored','identity']:
 q=[e for e in equality if e['label']==lab];need(q[0]['changed_maxima']==q[1]['changed_maxima'],'td05/ext1e11 changed entries exactly agree')
zero=load(D/'sources/lead/tp_none.json');edge=[]
for lab in ['stored','identity']:
 row=next(t for t in zero['results'][lab]['rows'] if t['region']=='r>1000L')
 for col in m['columns']:
  if row[col][1]==zero['rmax']:edge.append({'label':lab,'column':col,'radius_exact':str(scalar(zero['rmax']))})
need(len(edge)==6,'six far maxima at outermost gridpoint in zero-source file')
for pp in [Path(__file__),D/'ADDENDUM.md',D/'evidence/check.json',D/'evidence/check_v2.log',D/'code/check.py',D/'evidence/check.log']:pins[str(pp.relative_to(B))]=sha(pp)
for n,h in pins.items():need(sha(B/n)==h,'unchanged inputs')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SAVED_IDENTITY_COLUMNS_PROVENANCE_ORDER_AND_EQUALITY_COUNTS','derived_p_exact':str(exactp),'provenance_order':{'evaluator_postdates_all_lead_outputs':True,'inverse_postdates_original_outputs':True},'counts':{'exact_ratios':nr,'interval_enclosures':2*nr,'explicit_axis_assignments':3,'far_zero_source_edge_maxima':len(edge)},'records':records,'exact_equality_observations':equality,'zero_source_far_edge_observations':edge,'files':dict(sorted(pins.items())),'scope':'Saved finite scalars and captured AST only. No runtime attestation, independent field extrema, cause of equalities, certified fit accuracy or physical cancellation measurement.'}
with (D/'evidence/supplement.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k] for k in ['utc','status','counts','records']},indent=2))

"""Finalize exact saved scalar sums and conditional norm theorem, not physical/global bounds."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,re,os
B=Path(__file__).resolve().parents[3];D=B/'research/weighted_derivative_scalar_norms';R=B/'notes/reviews'
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def overlap(a,b):
 a=list(map(F,a));b=list(map(F,b));need(a[0]<=a[1] and b[0]<=b[1] and max(a[0],b[0])<=min(a[1],b[1]),'ordered overlapping aggregate intervals')
p=load(D/'evidence/arb.json');v=load(D/'evidence/independent.json');g=load(D/'evidence/graph_dependency.json');par=load(D/'data_exact/parameters.json');manifest=load(D/'data_exact/manifest.json');modal=load(B/'data_exact/modal_v2.json')
need(p['status']=='PASS_ARB_FINITE_SAVED_CELL_MAJORANT_SUMS_ONLY' and v['status']=='PASS_INDEPENDENT_SAVED_SCALAR_NORMS_GEOMETRY_AND_ROUNDING_ONLY','two actual complete engines');need(p['rows']==19389 and p['scalar_coefficients']==96945 and p['per_cell_energy_enclosures']==38778 and v['manual_ieee_scalar_checks']==135723 and v['cell_interval_overlaps']==38778 and v['region_selection_checks']==19389 and v['aggregate_interval_overlaps']==24,'complete counts')
need(p['arb_bits']>=320 and v['iv_dps']>=110,'precision');need(sha(D/'data_exact/rows.jsonl.gz')==par['rowfile_sha256'] and sha(D/'data_exact/manifest.json')==par['captured_manifest_sha256'],'exact archive/manifest pins')
for n in ['k','L']:need(F.from_float(float.fromhex(modal['scalars_hex'][n]))==F(par['params'][n]['exact'])==F(p['parameters_exact'][n]),'same exact graph/trial/weight parameters')
need(par['rows']==19389 and par['fields']==['t_a','h','W_0_0','W_1_0','W_2_0','W_0_1','W_1_1'],'exact field semantics')
ceilings={'inner':['0.000000886954','0.0000389562'],'middle':['0.385651','585.873'],'outer':['0.00168303','0.00380058'],'middle_rlt2':['0.00142514','0.0339214'],'middle_lobe':['0.385195','585.864'],'total':['0.385655','585.873']};counts={'inner':2632,'middle':7809,'outer':8948,'middle_rlt2':3172,'middle_lobe':937,'total':19389}
need(v['strict_scalar_ceilings']==ceilings and set(p['groups'])==set(v['norm_majorants_iv'])==set(ceilings),'six fixed groups')
for n,row in ceilings.items():
 need(p['groups'][n]['cells']==counts[n],'group cell count')
 for j,ceiling in enumerate(row):
  a=p['groups'][n]['norm_majorants_arb'][j];b=v['norm_majorants_iv'][n][j];overlap(a,b);need(F(ceiling)>max(F(a[1]),F(b[1])),'strict outward ceiling for both engines')
  s=list(map(F,p['groups'][n]['squared_norm_majorants_arb'][j]));need(s[0]>0 and F(a[0])**2<=s[1] and F(a[1])**2>=s[0],'positive compatible norm/square intervals')
need(len(v['saved_inflated_values_checked'])==12 and {(x['group'],x['column']) for x in v['saved_inflated_values_checked']}=={(n,j) for n in ceilings for j in [0,1]},'complete saved values')
for x in v['saved_inflated_values_checked']:
 n=x['group'];j=x['column'];q=F(x['saved_exact']);need(q>max(F(v['norm_majorants_iv'][n][j][1]),F(p['groups'][n]['norm_majorants_arb'][j][1])) and F(x['saved_minus_scalar_lower_bound'])>0,'saved inflation actually exceeds both results')
need(len(v['inward_printed_bounds'])==4 and {(x['group'],x['column']) for x in v['inward_printed_bounds']}=={(n,j) for n in ['middle','total'] for j in [0,1]},'four inward claims')
for x in v['inward_printed_bounds']:
 n=x['group'];j=x['column'];need(F(x['printed_exact'])==F(['0.38565','585.87'][j])<min(F(p['groups'][n]['norm_majorants_arb'][j][0]),F(v['norm_majorants_iv'][n][j][0])),'printed scalar ceiling rounds inward')
for n,expected in {'inner':(2631,405,2226,0),'middle':(7808,0,7808,0),'outer':(8947,1563,7383,1)}.items():
 a=p['literal_interval_geometry'][n];b=v['literal_interval_geometry'][n];need(tuple(a[x] for x in ['adjacencies','positive_gaps','overlaps','exact_joins'])==expected,'literal geometry counts')
 for key in ['adjacencies','positive_gaps','overlaps','exact_joins','max_gap','min_gap','total_positive_gap','first_t_exact','last_t_exact']:need(a[key]==b[key],'independent exact geometry')
 for key in ['first_radius','last_radius']:overlap(a[key+'_arb'],b[key+'_iv'])
need(p['cross_region_joins']==v['cross_region_joins'] and len(p['cross_region_joins'])==2 and all(F(x['exact_gap'])<0 for x in p['cross_region_joins']),'cross joins overlap')
need((D/'SOURCE_EXCERPT.md').read_text().split('\n\n',1)[1].rstrip() in (D/'sources/NUM_REPORT.md').read_text(),'captured excerpt verbatim')
pins={}
for d in [p,v,g]:
 for n,h in d['files'].items():
  need(n not in pins or pins[n]==h,'consistent inherited pins');need(not Path(n).is_absolute() and '..' not in Path(n).parts,'own-lane pin');pins[n]=h
for n,h in pins.items():need(sha(B/n)==h,'all inherited current pins')
gp=B/'research/modal_graph_scaling/evidence/verdict.json';gv=load(gp);need(sha(gp)==g['inherited_verdict_sha256'] and gv['status']==g['inherited_status']=='CONFIRMED_ACTUAL_MODAL_GRAPH_SCALING_AND_NONZERO_IMAGE' and len(gv['files'])==g['checked_pins']==77 and len(g['files'])==78,'actual inherited graph verdict');need(all(g['files'].get(n)==h for n,h in gv['files'].items()),'complete inherited graph inputs')
tag='weighted_derivative_norm_complete';m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));q=(R/(tag+'_request.txt')).read_text();text='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n';need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn','actual complete Opus5.5');need(hashlib.sha256(q.encode()).hexdigest()==m['input_sha256'] and text==(R/(tag+'_response.md')).read_text(),'actual review bytes');need(q[q.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'current actual reviewed bundle')
verdict='CONFIRM_CONDITIONAL_NORM_IDENTITIES_AND_SAVED_SCALAR_AUDIT_ONLY';need(re.findall(r'^\W*VERDICT\W*:\W*(\w+)',text,re.M|re.I)==[verdict] and [s.strip() for s in text.splitlines() if s.strip()][-1]=='VERDICT: '+verdict,'unique final scoped verdict')
required=['PROOF.md','ADDENDUM.md','RESULTS.md','SOURCE_EXCERPT.md','code/compute_arb.py','code/check_iv.py','code/finalize.py','data_exact/parameters.json','evidence/arb.json','evidence/independent.json','evidence/graph_dependency.json'];need({str((D/n).relative_to(B)) for n in required}<=set(m['files']),'required actual review outputs');need({'research/modal_graph_scaling/PROOF.md','research/modal_graph_scaling/ADDENDUM.md','research/modal_graph_scaling/NONZERO_IMAGE.md','notes/reviews/weighted_derivative_norm_proof_response.md'}<=set(m['files']),'graph correction review supplied')
post=load(D/'evidence/postreview_record.json');ap=D/'POSTREVIEW_ADJUDICATION.md';need(post['status']=='CONFIRMED_AFTER_INDEPENDENT_READING_OF_ACTUAL_COMPLETE_REVIEW' and post['review_request_id']==m['request_id'] and post['review_input_sha256']==m['input_sha256'] and post['review_response_sha256']==sha(R/(tag+'_response.json')) and post['adjudication_sha256']==sha(ap) and post['substantive_objections_resolved_or_explicitly_outside_claim'] is True,'separate postreview');need(m['request_id'] in ap.read_text() and sha(R/(tag+'_response.json')) in ap.read_text(),'written actual review identity');w=datetime.fromisoformat;need(w(par['utc'])<w(p['start_utc'])<w(p['utc'])<w(v['start_utc'])<w(v['utc'])<w(g['utc'])<w(m['start_utc'])<=w(m['end_utc'])<w(post['utc'])<=datetime.now(timezone.utc),'actual chronology');need(str(ap.relative_to(B)) not in m['files'],'separate postreview not prereviewed')
for n in m['files']:pins[n]=sha(B/n)
for x in [ap,D/'evidence/postreview_record.json',D/'evidence/independent.log']+[R/(tag+s) for s in ['_metadata.json','_response.json','_response.md','_request.txt']]:pins[str(x.relative_to(B))]=sha(x)
for n,h in pins.items():need(sha(B/n)==h,'all final pins')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONDITIONAL_WEIGHTED_NORM_IDENTITIES_AND_EXACT_SAVED_SCALAR_AUDIT_ONLY','rows':19389,'manual_ieee_scalar_checks':135723,'cell_interval_overlaps':38778,'aggregate_interval_overlaps':24,'strict_scalar_ceilings':ceilings,'inward_printed_majorant_bounds':4,'positive_literal_adjacent_gaps':1968,'actual_review':{k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']},'files':dict(sorted(pins.items())),'scope':'Conditional norm theorem and exact evaluation of saved scalar sums on the union of literal intervals. Physical derivative W validation, complete cover, both infinite tails and numerical global inverse lower bound remain OPEN. Actual graph K and its nonzero image are inherited from accepted138. No IPM endpoint.'}
with (D/'evidence/verdict.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(D/'evidence/verdict.json')}))

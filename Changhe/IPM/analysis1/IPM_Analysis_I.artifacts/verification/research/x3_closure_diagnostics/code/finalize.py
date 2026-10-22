"""Accept analytic identities and a saved-scalar audit after actual review; no physical residual claim."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,os,re
B=Path(__file__).resolve().parents[3];D=B/'research/x3_closure_diagnostics';R=B/'notes/reviews'
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
r=load(D/'evidence/check.json');s=load(D/'evidence/supplement.json');e=load(D/'evidence/review_extract.json');need(e['status']=='ACTUAL_SAVED_SCALAR_AUDIT_EXTRACT_REQUIRES_REVIEW','actual extract');need(r['status']=='PASS_SAVED_MAXIMA_REPORT_AND_EXACT_FAR_POWER_ORDER' and s['status']=='PASS_SAVED_IDENTITY_COLUMNS_PROVENANCE_ORDER_AND_EQUALITY_COUNTS','actual independent checks')
for k in ['utc','status','counts']:need(e['primary_'+k]==r[k] and e['supplement_'+k]==s[k],'actual check fields')
for k in ['parameters','summary']:need(e[k]==r[k],'actual primary values')
for k in ['derived_p_exact','provenance_order']:need(e[k]==s[k],'actual supplement values')
rec=[{k:v for k,v in x.items() if k!='near_center_maxima'}|{'near_center_maxima':{k:{a:b for a,b in v.items() if a!='identity_over_stored'}|{'identity_over_stored_exact':v['identity_over_stored']['exact']} for k,v in x['near_center_maxima'].items()}} for x in s['records']]
need(e['near_center_records']==rec and e['equalities']==[{k:v for k,v in a.items() if k not in ['equal_maxima','changed_maxima']} for a in s['exact_equality_observations']],'extracted actual records')
need(r['counts']=={'source_ast_matches':16,'grid_point_diagnostics':1100,'relative_changes':192,'rounding_cells':336,'interval_enclosures':384,'saved_location_triples':48} and s['counts']=={'exact_ratios':24,'interval_enclosures':48,'explicit_axis_assignments':3,'far_zero_source_edge_maxima':6},'complete expected counts')
need(len(r['relative_changes'])==192 and len(r['rounding_checks'])==336 and len(s['records'])==6 and len(s['exact_equality_observations'])==4,'actual list counts')
for v in r['relative_changes']:
 x,y=F(v['base_exact']),F(v['variant_exact']);q=F(v['relative_change_exact']);need(q==(y-x)/x,'actual exact saved ratio');al,ah,il,ih=map(F,v['intervals_arb_iv']);need(al<=q<=ah and il<=q<=ih,'both recorded independent intervals');need(F(v['printed'])!=0 or q==0,'printed zero really exact for these observations')
for v in r['rounding_checks']:need(abs(F(v['exact_value'])-F(v['printed']))<=F(v['step'])/2,'all recorded decimal cells')
for x in s['records']:
 for v in x['near_center_maxima'].values():
  q=F(v['identity_over_stored']['exact']);need(q==F(v['identity_exact'])/F(v['stored_exact']),'supplement exact ratio')
  for engine in ['arb','iv']:
   lo,hi=map(F,v['identity_over_stored'][engine]);need(lo<=q<=hi,'supplement interval')
pins=dict(e['files'])
for check in [r,s]:
 for n,h in check['files'].items():need(n in pins and pins[n]==h,'extract inherited pin')
for n,h in pins.items():need(not Path(n).is_absolute() and '..' not in Path(n).parts and sha(B/n)==h,'all lane-only captured dependency pins')
tag='x3_closure_complete';m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));q=(R/(tag+'_request.txt')).read_text();t='\n\n'.join(v['text'] for v in raw['content'] if v['type']=='text')+'\n';need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn','actual completed Opus5.5');need(hashlib.sha256(q.encode()).hexdigest()==m['input_sha256'] and t==(R/(tag+'_response.md')).read_text(),'actual review bytes');need(q[q.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'current full review bundle')
lines=[x.strip() for x in t.splitlines() if x.strip()];matches=re.findall(r'^\W*VERDICT\W*:\W*(\w+)',t,re.M|re.I);need(matches==['CONFIRM_IDENTITIES_AND_SAVED_SCALAR_AUDIT_ONLY'] and lines[-1]=='VERDICT: CONFIRM_IDENTITIES_AND_SAVED_SCALAR_AUDIT_ONLY','unique final scoped verdict')
required=['PROOF.md','ADDENDUM.md','RESULT_INTERPRETATION.md','data_exact/manifest.json','code/check_v2.py','code/check_supplement_v2.py','code/review_extract.py','code/finalize.py','evidence/review_extract.json','sources/num/inverse.py','sources/num/x3_resid.py','sources/lead/run2.py','sources/lead/SUMMARY.md'];need({str((D/p).relative_to(B)) for p in required}<=set(m['files']),'required review bundle')
post=load(D/'evidence/postreview_record.json');ap=D/'POSTREVIEW_ADJUDICATION.md';need(post['status']=='CONFIRMED_AFTER_INDEPENDENT_READING_OF_ACTUAL_COMPLETE_REVIEW' and post['review_request_id']==m['request_id'] and post['review_input_sha256']==m['input_sha256'] and post['review_response_sha256']==sha(R/(tag+'_response.json')) and post['adjudication_sha256']==sha(ap) and post['substantive_objections_resolved_or_explicitly_outside_claim'] is True,'separate actual postreview');need(m['request_id'] in ap.read_text() and sha(R/(tag+'_response.json')) in ap.read_text(),'written actual review identity');w=datetime.fromisoformat;need(w(r['utc'])<w(s['utc'])<=w(e['utc'])<w(m['start_utc'])<=w(m['end_utc'])<w(post['utc'])<=datetime.now(timezone.utc),'chronology');need(str(ap.relative_to(B)) not in m['files'] and str((D/'evidence/postreview_record.json').relative_to(B)) not in m['files'],'postreview outside previous bundle')
for n in m['files']:pins[n]=sha(B/n)
for p in [D/'evidence/review_extract.json',ap,D/'evidence/postreview_record.json']+[R/(tag+sfx) for sfx in ['_metadata.json','_response.json','_response.md','_request.txt']]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'final unchanged pin')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_FAR_POWERS_EXTERIOR_SOURCE_IDENTITIES_AND_SAVED_SCALAR_AUDIT_ONLY','mathematical_verdict':'CONFIRMED under stated exact formula and integrability assumptions','source_density_cutoff_label_verdict':'REFUTED: captured wrapper manipulates exterior rho_x source modes','primary_counts':r['counts'],'supplement_counts':s['counts'],'summary':r['summary'],'actual_review':{k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']},'files':dict(sorted(pins.items())),'scope':e['scope']+' Exact far expansion has unevaluated remainder constant. No physical cancellation measurement, fit accuracy, inverse or IPM endpoint.'}
with (D/'evidence/verdict.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(D/'evidence/verdict.json')}))

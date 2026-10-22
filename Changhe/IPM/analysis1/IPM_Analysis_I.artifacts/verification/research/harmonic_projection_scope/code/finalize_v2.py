"""Accept a narrow reporting audit after actual model review and own assessment."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,os,re
B=Path(__file__).resolve().parents[3];D=B/'research/harmonic_projection_scope';R=B/'notes/reviews'
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
r=load(D/'evidence/check.json');need(r['status']=='PASS_SAVED_ARTIFACTS_AND_INDEPENDENT_FLOATING_HARMONIC_DIAGNOSTIC','actual diagnostic');pins=dict(r['files']);man=load(D/'data_exact/manifest.json');need(len(r['records'])==len(man['cases'])==4,'four preselected vectors')
for rec,case in zip(r['records'],man['cases'],strict=True):
 need(rec['family']==case['family'] and rec['rows']==case['rows'],'case binding');sh=load(B/case['summary'])['sections']['Fminus']['smallest5_shares'][0];pr=load(B/case['profile'])['shells'][0];need(rec['sigma']==sh['sigma']==pr['sigma'] and rec['saved_projection_m0']==sh['modes'][0] and rec['saved_low_harmonic_fraction']==pr['harmonic_energy_fractions']['N=0..1'],'scalar identity');need(F.from_float(rec['saved_low_harmonic_fraction'])-F.from_float(rec['saved_projection_m0'])==F(rec['exact_saved_gap'])>0 and rec['exact_saved_projection_le_harmonic'] is True,'exact saved comparison');need([v['order'] for v in rec['runs']]==[20,32],'two quadrature orders')
need(F(86,100)<F.from_float(r['records'][0]['saved_low_harmonic_fraction'])<F(87,100),'M24 H1 saved fraction');need(F(80,100)<F.from_float(r['records'][1]['saved_low_harmonic_fraction'])<F(81,100),'M24 H1q saved fraction')
tag='harmonic_projection_scope_followup';m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));q=(R/(tag+'_request.txt')).read_text();t='\n\n'.join(v['text'] for v in raw['content'] if v['type']=='text')+'\n';need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn','actual completed Opus5.5');need(hashlib.sha256(q.encode()).hexdigest()==m['input_sha256'] and t==(R/(tag+'_response.md')).read_text(),'actual review bytes');need(q[q.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'current full review bundle');lines=[x.strip() for x in t.splitlines() if x.strip()];matches=re.findall(r'^\W*VERDICT\W*:\W*(\w+)',t,re.M|re.I);need(matches==['CONFIRM_PROJECTION_NESTING_AND_SCOPED_REPORT_CORRECTION'] and lines[-1]=='VERDICT: CONFIRM_PROJECTION_NESTING_AND_SCOPED_REPORT_CORRECTION','unique final scoped verdict')
req=['PROOF.md','SOURCE_SCOPE.md','RESULT_INTERPRETATION.md','data_exact/manifest.json','code/check.py','code/finalize_v2.py','evidence/check.json','REVIEW_CORRECTIONS.md','sources/report_excerpt.txt'];need({str((D/p).relative_to(B)) for p in req}<=set(m['files']),'required review bundle');post=load(D/'evidence/postreview_record.json');need(post['status']=='CONFIRMED_AFTER_INDEPENDENT_READING_OF_ACTUAL_COMPLETE_REVIEW' and post['review_input_sha256']==m['input_sha256'] and post['review_response_sha256']==sha(R/(tag+'_response.json')) and post['review_request_id']==m['request_id'] and post['adjudication_sha256']==sha(D/'POSTREVIEW_ADJUDICATION.md'),'post-review assessment binding');w=datetime.fromisoformat;need(w(r['utc'])<w(m['start_utc'])<=w(m['end_utc'])<w(post['utc'])<=datetime.now(timezone.utc),'chronology')
need('research/harmonic_projection_scope/POSTREVIEW_ADJUDICATION.md' not in m['files'] and 'research/harmonic_projection_scope/evidence/postreview_record.json' not in m['files'],'post files excluded from reviewed bundle')
need(m['request_id'] in (D/'POSTREVIEW_ADJUDICATION.md').read_text() and sha(R/(tag+'_response.json')) in (D/'POSTREVIEW_ADJUDICATION.md').read_text(),'written actual review identity')
for n in m['files']:pins[n]=sha(B/n)
for p in [D/'evidence/check.json',D/'evidence/check.log',D/'POSTREVIEW_ADJUDICATION.md',D/'evidence/postreview_record.json']+[R/(tag+s) for s in ['_metadata.json','_response.json','_response.md','_request.txt']]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'final unchanged source pin')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_PROJECTION_NESTING_AND_SAVED_REPORT_CORRECTION_ONLY','report_claim_verdict':'REFUTED: captured M24 H1 profile gives0.86866965, not approximately0.81','cases':[{k:v for k,v in x.items() if k!='runs'} for x in r['records']],'actual_review':{k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']},'files':dict(sorted(pins.items())),'scope':'Exact projection nesting theorem and exact saved scalar comparisons. Fresh two-rule field integrations are floating diagnostics only. The m=0 projections themselves were not regenerated; no certified energy enclosure, column admissibility, spectral limit, inverse or IPM endpoint.'}
p=D/'evidence/verdict.json'
with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))

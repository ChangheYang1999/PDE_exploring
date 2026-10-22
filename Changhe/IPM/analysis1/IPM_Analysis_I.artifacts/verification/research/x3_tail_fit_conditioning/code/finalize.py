"""Finalize analytic identities and literal synthetic moments; retain floating diagnostic limits."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,re,math,os
B=Path(__file__).resolve().parents[3];D=B/'research/x3_tail_fit_conditioning';R=B/'notes/reviews'
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
v=load(D/'evidence/diagnostic.json');c=load(D/'evidence/independent_check.json');s=load(D/'evidence/moments.json');poly=load(D/'data_exact/last_span_polynomials.json')
need(v['status']=='FLOATING_DIAGNOSTICS_ONLY_REQUIRES_REVIEW' and c['status']=='PASS_EXACT_LAST_SPAN_POLYNOMIAL_AND_FLOATING_SOURCE_DIAGNOSTIC' and s['status']=='PASS_EXACT_SYNTHETIC_TAIL_MOMENTS_ONLY','actual completed diagnostics and exact checks');need(v['exact_endpoint_formula_checks']==c['exact_endpoint_checks']==603 and c['complete_exact_polynomial_coefficients']==1608 and c['source_scalar_comparisons']==60 and s['exact_quantities']==9 and s['interval_enclosures']==18,'complete counts')
need(len(poly['polynomial_coefficients'])==201 and poly['angular_modes']==list(range(201)) and poly['coordinate']=='delta=q-1','exact polynomial metadata')
for j,row in enumerate(poly['polynomial_coefficients']):
 need(len(row)==8,'eight coefficients per mode')
 for n in range(3):need(F(row[n])*math.factorial(n)==F(v['endpoint_exact_ratios'][n][j]),'all603endpoint equalities')
need([x['name'] for x in v['fits']]==['base','td05','td20','ext1e11','tp_lead'] and len(s['moments'])==5 and len(s['same_radius_changes'])==4,'five fits and four same-radius changes');mom={};rad={}
for fit,rec in zip(v['fits'],s['moments'],strict=True):
 need(fit['name']==rec['name'],'moment fit identity');q=list(map(F.from_float,fit['powers']));aa=[F.from_float(x[0]) for x in fit['fitted_coefficients']];need(len(q)==len(aa) and all(x<0 for x in q),'negative synthetic exponents');m=sum((a/(-b) for a,b in zip(aa,q)),F(0))/2;need(m==F(rec['moment']['exact']),'literal exact synthetic moment');mom[fit['name']]=m;rad[fit['name']]=rec['outer_radius_exact'];need(F.from_float(fit['outer_radius'])==F(rec['outer_radius_exact']),'outer radius binding')
 for engine in ['arb','iv']:
  lo,hi=map(F,rec['moment'][engine]);need(lo<=m<=hi,'synthetic moment interval')
for rec in s['same_radius_changes']:
 n=rec['name'];q=-mom['base'] if n=='tp_none' else mom[n]-mom['base'];need(q==F(rec['synthetic_change']['exact']),'same-radius exact difference');need(n=='tp_none' or rad[n]==rad['base'],'equal outer radius')
 for engine in ['arb','iv']:
  lo,hi=map(F,rec['synthetic_change'][engine]);need(lo<=q<=hi,'difference interval')
pins=dict(s['files'])
for out in [v,c]:
 for n,h in out['files'].items():need(n in pins and pins[n]==h,'complete inherited diagnostic pins')
for n,h in pins.items():need(not Path(n).is_absolute() and '..' not in Path(n).parts and sha(B/n)==h,'lane-only captured inputs unchanged')
tag='x3_tail_coefficients_complete';m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));q=(R/(tag+'_request.txt')).read_text();text='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n';need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn','actual complete Opus5.5');need(hashlib.sha256(q.encode()).hexdigest()==m['input_sha256'] and text==(R/(tag+'_response.md')).read_text(),'actual review bytes');need(q[q.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'current reviewed files')
verdicts=re.findall(r'^\W*VERDICT\W*:\W*(\w+)',text,re.M|re.I);lines=[x.strip() for x in text.splitlines() if x.strip()];need(verdicts==['CONFIRM_COEFFICIENT_IDENTITIES_AND_SYNTHETIC_MOMENTS_ONLY'] and lines[-1]=='VERDICT: CONFIRM_COEFFICIENT_IDENTITIES_AND_SYNTHETIC_MOMENTS_ONLY','unique final scoped verdict')
required=['PROOF.md','INDEPENDENT_CHECK_PROOF.md','RECORDED_MOMENT_PROOF.md','RESULT_INTERPRETATION.md','code/diagnose_v2.py','code/check_independent.py','code/audit_moments.py','code/finalize.py','data_exact/manifest.json','evidence/diagnostic.json','evidence/independent_check.json','evidence/moments.json'];need({str((D/p).relative_to(B)) for p in required}<=set(m['files']),'required actual-output review bundle')
post=load(D/'evidence/postreview_record.json');ap=D/'POSTREVIEW_ADJUDICATION.md';need(post['status']=='CONFIRMED_AFTER_INDEPENDENT_READING_OF_ACTUAL_COMPLETE_REVIEW' and post['review_request_id']==m['request_id'] and post['review_input_sha256']==m['input_sha256'] and post['review_response_sha256']==sha(R/(tag+'_response.json')) and post['adjudication_sha256']==sha(ap) and post['substantive_objections_resolved_or_explicitly_outside_claim'] is True,'separate own postreview identity');need(m['request_id'] in ap.read_text() and sha(R/(tag+'_response.json')) in ap.read_text(),'written actual review binding');w=datetime.fromisoformat;need(w(v['utc'])<w(c['utc'])<w(s['utc'])<w(m['start_utc'])<=w(m['end_utc'])<w(post['utc'])<=datetime.now(timezone.utc),'chronology');need(str(ap.relative_to(B)) not in m['files'] and str((D/'evidence/postreview_record.json').relative_to(B)) not in m['files'],'postreview outside previous bundle')
for n in m['files']:pins[n]=sha(B/n)
for p in [ap,D/'evidence/postreview_record.json',D/'evidence/moments.log']+[R/(tag+x) for x in ['_metadata.json','_response.json','_response.md','_request.txt']]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'final pins')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_ANALYTIC_FAR_COEFFICIENTS_AND_EXACT_RECORDED_SYNTHETIC_MOMENTS_ONLY','exact_counts':{'last_span_polynomial_coefficients':1608,'endpoint_equalities':603,'synthetic_moments_and_changes':9,'interval_enclosures':18},'diagnostic_source_scalar_comparisons':60,'actual_review':{k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']},'files':dict(sorted(pins.items())),'scope':'Exact analytic far-coefficient identities and rational moments for literal recorded synthetic sources. Quadrature, QR fits, condition numbers, physical source comparisons, coefficient drifts and annulus integration are floating diagnostics. No certified fit accuracy or X3 tail error, physical residual enclosure, inverse or IPM endpoint.'}
with (D/'evidence/verdict.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(D/'evidence/verdict.json')}))

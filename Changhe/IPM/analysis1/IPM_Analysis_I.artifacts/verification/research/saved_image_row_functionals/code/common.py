"""Source, actual output and complete model-response binding for literal geometry."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,re,os
B=Path(__file__).resolve().parents[3];D=B/'research/saved_image_row_functionals';R=B/'notes/reviews'
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def now():return datetime.now(timezone.utc).isoformat()
def pin(pins,p):
 p=Path(p).resolve();need(p.is_relative_to(B),'lane input');n=str(p.relative_to(B));h=sha(p);need(n not in pins or pins[n]==h,'pin conflict');pins[n]=h

def auth(pins,tag,verdict,required):
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));q=(R/(tag+'_request.txt')).read_text();text='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n';need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn','actual complete Opus5.5');need(hashlib.sha256(q.encode()).hexdigest()==m['input_sha256'] and text==(R/(tag+'_response.md')).read_text(),'actual review bytes');need(q[q.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'current complete review bundle');need(set(required)<=set(m['files']),'mandatory reviewed files');need(all(s in q for s in ['no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster']),'delegated restrictions');need(re.findall(r'^\W*VERDICT\W*:\W*(\w+)',text,re.M|re.I)==[verdict] and [x.strip() for x in text.splitlines() if x.strip()][-1]=='VERDICT: '+verdict,'unique scoped verdict')
 for n in m['files']:pin(pins,B/n)
 for x in ['_metadata.json','_response.json','_response.md','_request.txt']:pin(pins,R/(tag+x))
 return {k:m[k] for k in ['requested_model','actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
def write(p,v):
 with p.open('x') as f:json.dump(v,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def outward(bounds,places=9):
 lo=min(F(b[0]) for b in bounds);hi=max(F(b[1]) for b in bounds);unit=10**places;a=lo.numerator*unit//lo.denominator;b=-((-hi.numerator*unit)//hi.denominator);need(F(a,unit)<=lo<=hi<=F(b,unit),'decimal outward rounding');return [str(F(a,unit)),str(F(b,unit))]
def collect():
 a=load(D/'evidence/arb.json');b=load(D/'evidence/independent.json');m=load(D/'data_exact/manifest.json');need(a['status']=='PASS_ARB_EXACT_SAVED_IMAGE_FUNCTIONALS_ONLY' and b['status']=='PASS_INDEPENDENT_ORIGINAL_IMAGE_IMPORT_AND_EDGE_FUNCTIONALS_ONLY','actual both outputs');need(a['arb_bits']==320 and b['iv_dps']==100 and a['selected_directions']==b['selected_directions']==m['selected_directions']==6 and a['image_values']==b['image_values']==m['selected_image_values']==174160 and a['edge_differences']==b['edge_differences']==173920 and b['manual_ieee_source_checks']==m['exported_scalars']==179484 and a['quotient_enclosures']==24 and b['interval_overlaps']==54,'all exact actual coverage counts');pins=dict(b['files'])
 for v in [a,m]:
  for n,h in v['files'].items():need(pins.get(n)==h,'complete input pin inheritance')
 for n,h in pins.items():need(not Path(n).is_absolute() and '..' not in Path(n).parts and sha(B/n)==h,'immutable lane captured inputs')
 selection=[('M16_s8_o40_p4','L2q',0),('M16_s8_o40_p4','L2q',2),('M16_s8_o40_p4','L2q',4),('M16_s8_o40_p4','H1q',0),('M24_s16_o40_p4','L2q',0),('M24_s16_o40_p4','H1q',0)];need([(r['case'],r['row_mode'],r['index']) for r in a['results']]==[(r['case'],r['row_mode'],r['index']) for r in b['results']]==selection,'all preselected source identities');summ=[];maxerr=F(0);overlaps=0
 for p,q in zip(a['results'],b['results'],strict=True):
  g=F(p['g_exact']);need(g>0 and p['Mout']==40 and p['Ne']==(855 if p['case'].startswith('M16_') else 467),'literal denominator/shape');rr={}
  for name in ['L2','L2q','H1','H1q']:
   x=p['rows'][name];y=q['rows'][name];saved=F(x['saved_exact']);err=F(y['saved_absolute_error_bound']);maxerr=max(maxerr,err)
   for kind in ['energy','quotient']:
    l,h=map(F,x[kind+'_arb']);a0,b0=map(F,y[kind+'_iv']);need(0<l<=h and 0<a0<=b0 and max(l,a0)<=min(h,b0),'positive independent enclosure overlap');overlaps+=1
   lo,hi=map(F,y['quotient_iv']);need(err==max(abs(lo-saved),abs(hi-saved))<F(2,10**12),'exact tighter saved discrepancy bound');need(max(abs(F(x['quotient_arb'][0])-saved),abs(F(x['quotient_arb'][1])-saved))<F(2,10**12),'same Arb discrepancy bound');rr[name]={'outward_9place_window_exact':outward([x['quotient_arb'],y['quotient_iv']]),'saved_exact':str(saved),'saved_absolute_error_upper':str(err)}
  ar=list(map(F,p['H1q_over_L2q_arb']));ir=list(map(F,q['H1q_over_L2q_iv']));need(max(ar[0],ir[0])<=min(ar[1],ir[1]),'ratio overlap');overlaps+=1;summ.append({'case':p['case'],'row_mode':p['row_mode'],'index':p['index'],'Ne':p['Ne'],'Mout':40,'g_exact':str(g),'sigma_exact':p['sigma_exact'],'quotients':rr,'H1q_over_L2q_outward_9place_window_exact':outward([p['H1q_over_L2q_arb'],q['H1q_over_L2q_iv']])})
 need(overlaps==54,'all final interval comparisons');proof=auth(pins,'saved_image_functionals_proof','CONFIRM_FINITE_ROW_FUNCTIONAL_IDENTITIES',['research/saved_image_row_functionals/PROOF.md'])
 for n in ['PROOF.md','ADDENDUM.md','code/capture.py','code/compute_arb.py','code/check_iv.py','code/common.py','code/extract.py','code/finalize.py','data_exact/manifest.json','evidence/arb.json','evidence/independent.json','evidence/arb.log','evidence/independent.log','sources/c2_img_eval.py']:pin(pins,D/n)
 return pins,{'utc':now(),'status':'PASS_ACTUAL_FINITE_IMAGE_FUNCTIONAL_REVIEW_EXTRACT_NOT_FINAL','selected_directions':6,'original_image_values':174160,'edge_differences':173920,'original_source_scalar_checks':179484,'independent_interval_overlaps':54,'maximum_saved_quotient_absolute_discrepancy_upper':str(maxerr),'strict_all_saved_absolute_discrepancy_ceiling':'1/500000000000','results':summ,'primary_results':a['results'],'independent_results':b['results'],'engine_times':[a['utc'],b['utc']],'proof_review':proof,'files':dict(sorted(pins.items())),'scope':'Exact literal finite data, selected six directions only, no actual operator image/g norm/minimum/coercivity certificate.'}

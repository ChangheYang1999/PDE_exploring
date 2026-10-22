import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,re,os
B=Path(__file__).resolve().parents[3];D=B/'research/saved_image_high_band';R=B/'notes/reviews'
def need(x,s):
 if not x:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def now():return datetime.now(timezone.utc).isoformat()
def pin(pins,p):
 p=Path(p).resolve();need(p.is_relative_to(B),'lane source');n=str(p.relative_to(B));h=sha(p);need(n not in pins or pins[n]==h,'unchanged input');pins[n]=h
def write(p,x):
 with p.open('x') as f:json.dump(x,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def window(b):
 lo=min(F(x[0]) for x in b);hi=max(F(x[1]) for x in b);unit=10**12;a=lo.numerator*unit//lo.denominator;c=-((-hi.numerator*unit)//hi.denominator);need(F(a,unit)<=lo<=hi<=F(c,unit),'outward window');return [str(F(a,unit)),str(F(c,unit))]
def auth(pins,tag,verdict,required):
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text();text='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n';need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn','actual full Opus5.5');need(sha(R/(tag+'_request.txt'))==m['input_sha256'] and text==(R/(tag+'_response.md')).read_text(),'actual request/response bytes');need(req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'complete current bundle');need(set(required)<=set(m['files']),'all mandatory reviewed inputs');need(all(s in req for s in ['no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds']),'all delegated restrictions');need(re.findall(r'^\W*VERDICT\W*:\W*(\w+)',text,re.M|re.I)==[verdict] and [x.strip() for x in text.splitlines() if x.strip()][-1]=='VERDICT: '+verdict,'unique exact verdict')
 for n in m['files']:pin(pins,B/n)
 for suf in ['_metadata.json','_request.txt','_response.json','_response.md']:pin(pins,R/(tag+suf))
 return {k:m[k] for k in ['requested_model','actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
REQUIRED=['PROOF.md','ADDENDUM.md','code/capture.py','code/compute_arb.py','code/check_iv_v2.py','code/common.py','code/extract.py','code/finalize.py','data_exact/manifest.json','data_exact/summaries.json','evidence/review_extract.json']
def collect():
 a=load(D/'evidence/arb.json');b=load(D/'evidence/independent_v2.json');m=load(D/'data_exact/manifest.json');need(a['status']=='PASS_ARB_OBSERVED_HIGH_BAND_ONLY' and b['status']=='PASS_INDEPENDENT_LITERAL_HIGH_BAND_AND_SUMMARIES_ONLY','actual outputs');need(a['arb_bits']==320 and b['iv_dps']==100 and a['image_values']==b['image_values']==37360 and a['edge_differences']==b['edge_differences']==37280 and b['manual_ieee_scalars']==39243 and a['energy_enclosures']==16 and a['fraction_enclosures']==8 and b['interval_overlaps']==24 and b['exact_summary_comparisons']==10,'all coverage counts');pins=dict(b['files'])
 for x in [a,m]:
  for n,h in x['files'].items():need(pins.get(n)==h,'all inherited source pins')
 for n,h in pins.items():need(not Path(n).is_absolute() and '..' not in Path(n).parts and sha(B/n)==h,'unchanged pinned source')
 need([r['row_mode'] for r in a['results']]==[r['row_mode'] for r in b['results']]==['L2q','H1q'],'selected two images');res=[];overlaps=0
 for p,q in zip(a['results'],b['results'],strict=True):
  need(p['index']==q['index']==0 and p['Ne']==467 and p['Mout']==40,'selected dimensions');rows={}
  for key in ['L2','L2q','H1','H1q']:
   for kind in ['total','high','fraction']:
    l,h=map(F,p['rows'][key][kind+'_arb']);u,v=map(F,q['rows'][key][kind+'_iv']);need(0<l<=h and 0<u<=v and max(l,u)<=min(h,v),'positive intersecting enclosures');overlaps+=1
    if kind=='fraction':need(max(h,v)<1,'proper observed fraction')
   rows[key]={'outward_fraction_window_exact':window([p['rows'][key]['fraction_arb'],q['rows'][key]['fraction_iv']])}
  res.append({'row_mode':p['row_mode'],'index':0,'rows':rows})
 need(overlaps==24,'all24 overlaps');need(len(a['summary_differences'])==len(b['summary_differences'])==10,'all10 summary changes')
 for p,q in zip(a['summary_differences'],b['summary_differences'],strict=True):need({k:v for k,v in p.items() if k!='relative_display'}==q and F(q['relative_exact'])>0,'exact positive stored change')
 proof=auth(pins,'saved_high_band_proof','CONFIRM_FINITE_BAND_AND_VARIATIONAL_IDENTITIES',['research/saved_image_high_band/PROOF.md','research/saved_image_row_functionals/PROOF.md'])
 for n in REQUIRED[:-1]+['evidence/arb.json','evidence/independent_v2.json','evidence/arb.log','evidence/independent_v2.log']:pin(pins,D/n)
 return pins,{'utc':now(),'status':'PASS_ACTUAL_OBSERVED_HIGH_BAND_REVIEW_EXTRACT_NOT_FINAL','images':2,'image_values':37360,'edge_differences':37280,'manual_ieee_scalars':39243,'interval_overlaps':24,'summary_comparisons':10,'results':res,'exact_summary_changes':b['summary_differences'],'primary_results':a['results'],'independent_results':b['results'],'engine_times':[a['utc'],b['utc']],'proof_review':proof,'files':dict(sorted(pins.items())),'scope':'Literal stored modes32..39 of two M24 images. No unobserved N>=40 tail, nested matrix validation, certified minimum, continuous norm or convergence.'}

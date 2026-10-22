"""Source, actual output and complete model-response binding for literal geometry."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,re,os
B=Path(__file__).resolve().parents[3];D=B/'research/literal_derivative_cell_union';R=B/'notes/reviews'
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
def collect():
 a=load(D/'evidence/merge.json');b=load(D/'evidence/sweep.json');c=load(D/'evidence/decimal.json');need(a['status']=='PASS_EXACT_RUNNING_MAXIMUM_UNION_ONLY' and b['status']=='PASS_INDEPENDENT_INTEGER_EVENT_SWEEP_AND_ALL_EXACT_GAPS' and c['status']=='PASS_ALL_ORIGINAL_DECIMAL_ROUNDING_CELLS_AND_EXACT_EXPORT_BINDING','actual all three outputs');need(a['source_scalar_checks']==b['manual_ieee_source_checks']==c['source_tokens']==c['manual_bit_export_equalities']==38778 and c['midpoint_ties']==0 and b['common_grid_denominator_power']==67,'all source/rounding checks');pins=dict(c['files'])
 for v in [a,b]:
  for n,h in v['files'].items():need(pins.get(n)==h,'complete inherited pins')
 for n,h in pins.items():need(not Path(n).is_absolute() and '..' not in Path(n).parts and sha(B/n)==h,'actual frozen source files')
 need(pins['research/weighted_derivative_scalar_norms/evidence/verdict.json']=='536c7886967dfbe139a8bcb8bb5827e5165fd6100e3d5a3f095c1e1bfb5ae742','actual topic152 dependency');expected={'inner':(2632,405,F(92977,576460752303423488)),'middle':(7809,0,F(0)),'outer':(8948,1563,F(4550477,4611686018427387904)),'all':(19389,1968,F(5294293,4611686018427387904))};summ={}
 for n,(count,gaps,missing) in expected.items():
  x=a['regions'][n];y=b['regions'][n];need(x['intervals']==y['intervals']==count and len(x['gaps'])==x['gap_count']==y['gap_count']==gaps and len(x['components'])==x['union_components']==y['union_components']==gaps+1,'all actual interval/components counts');need(x['strictly_increasing_starts'] is True and x['strictly_increasing_ends'] is True,'both endpoint monotonicities');need(F(x['missing_log_length'])==F(y['missing_log_length'])==missing==sum((F(hi)-F(lo) for lo,hi in x['gaps']),F(0)),'exact missing length');need(F(x['max_gap'])==F(y['max_gap'])==max([F(0)]+[F(hi)-F(lo) for lo,hi in x['gaps']]),'largest gap');need(all(F(lo)<F(hi) for lo,hi in x['gaps']),'all positive gaps');need(x['components']==[[lo,hi] for lo,hi in zip([x['hull'][0]]+[hi for lo,hi in x['gaps']],[lo for lo,hi in x['gaps']]+[x['hull'][1]],strict=True)],'complete complementary components');summ[n]={k:v for k,v in x.items() if k not in ['gaps','components']};summ[n]['sweep']=y
 need(F(summ['all']['max_gap'])==F(4151,2305843009213693952),'exact maximum gap');proof=auth(pins,'literal_cell_union_proof','CONFIRM_CONDITIONAL_EXACT_UNION_ARGUMENT',['research/literal_derivative_cell_union/PROOF.md','research/weighted_derivative_scalar_norms/PROOF.md','research/weighted_derivative_scalar_norms/POSTREVIEW_ADJUDICATION.md'])
 for n in ['PROOF.md','ADDENDUM.md','code/merge.py','code/sweep.py','code/check_decimal.py','code/common.py','code/extract.py','code/finalize.py','evidence/merge.json','evidence/sweep.json','evidence/decimal.json','evidence/merge.log','evidence/sweep.log','evidence/decimal.log']:pin(pins,D/n)
 return pins,{'utc':now(),'status':'PASS_ACTUAL_LITERAL_UNION_REVIEW_EXTRACT_NOT_FINAL','regions':summ,'decimal_check':{k:v for k,v in c.items() if k!='files'},'engine_times':[a['utc'],b['utc'],c['utc']],'proof_review':proof,'files':dict(sorted(pins.items())),'scope':'Actual finite saved interval-union complement only, no physical residual estimate or intended certification interval comparison.'}

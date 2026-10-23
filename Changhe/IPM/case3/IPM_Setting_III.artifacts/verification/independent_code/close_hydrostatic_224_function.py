"""Bind completed finite comparison and actual reviews; no new numerical run."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path('research/hydrostatic_224_function_difference');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();checks=[];bindings={}
def ck(n,b):
 checks.append({'name':n,'passed':bool(b)})
 if not b:raise AssertionError(n)
for f,count in [('MANUFACTURES.json',23),('RUN.json',231),('MAXIMIZER_MP.json',118)]:
 p=V/f;j=json.loads(p.read_text());ck(f+' completed',j['status']=='PASS' and j['count']==count and len(j['checks'])==count and all(x['passed'] for x in j['checks']));bindings[str(p)]=sha(p)
 for p,h in j.get('bindings',{}).items():ck('bound '+p,sha(p)==h);bindings[p]=h
reviews=[]
for name in ['design','followup','closure','results','results_followup']:
 d=V/('opus_'+name);m=json.loads((d/'metadata.json').read_text());s=json.loads((d/'response.json').read_text());ck(name+' actual model',m['returned_model']==s['model']=='claude-opus-5-5');ck(name+' complete',m['stop_reason']=='end_turn' and m['answer_nonempty']);ck(name+' request',sha(d/'request.txt')==m['request_sha256']);ck(name+' text', '\n'.join(x['text'] for x in s['content'] if x['type']=='text').strip()==(d/'answer.md').read_text().strip());reviews.append({'name':name,**m})
 for f in ['metadata.json','response.json','request.txt','answer.md']:bindings[str(d/f)]=sha(d/f)
for p in [Path(__file__),R/'RESULTS.md',R/'CLOSURE_PROOF.md',R/'RESULT_REVIEW_RESOLUTION_PROOF.md',Path('independent_code/check_hydrostatic_224_maximizer_mp.py'),V/'PREPARATION.json']:bindings[str(p)]=sha(p)
run=json.loads((V/'RUN.json').read_text());mp=json.loads((V/'MAXIMIZER_MP.json').read_text());ck('15tokens',len(run['tokens'])==15 and run['token_disagreement_count']==0);ck('13 coordinates and39states',len(mp['rows'])==39 and len(set((x['x'],x['y']) for x in mp['rows']))==13);ck('18metricrecords',len(mp['metric_records'])==18)
for conv in ['common_nominal','common_hypot','shifted']:
 for key in ['field','gradient','pointwise_relative']:
  a=next(x for x in mp['metric_records'] if x['pair']=='baseline' and x['convention']==conv and x['metric']==key);b=next(x for x in mp['metric_records'] if x['pair']=='comparisons' and x['convention']==conv and x['metric']==key);ck('finite increase '+conv+' '+key,b['stored_value']>a['stored_value']>0)
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'count':len(checks),'checks':checks,'bindings':bindings,'actual_model':'claude-opus-5-5','reviews':reviews,'verdict':'CONFIRMED finite sampled annulus increase, by factors3.90..4.20 in nine metric/convention cells','scope':'231comparison+23manufacture+118MPsupplement assertions; closure counts bookkeeping separately. No continuum supremum, infinite convergence, inverse validity or IPM endpoint. Primary UNRESOLVED.'}
(V/'FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',out['count'],out['utc'])

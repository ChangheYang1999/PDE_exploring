"""Close the exact-pair audit only after two actual reviews and later own adjudication."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/projection_source_constraints';E=D/'evidence';R=B/'notes/reviews'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def when(s):return datetime.fromisoformat(s)
pins={}
def pin(p,h=None):
 p=Path(p);p=p if p.is_absolute() else B/p;n=str(p.relative_to(B));a=sha(p)
 assert h is None or h==a,n
 assert n not in pins or pins[n]==a,n
 pins[n]=a
c=load(E/'checks.json');s=load(E/'supplement.json')
assert c['status']=='PASS_TWO_METHOD_EXACT_SOURCE_CONSTRAINTS_ONLY' and s['status']=='PASS_EXACT_CANCELLATION_LEVELS_AND_SOURCE_CONVENTION_DIAGNOSTICS'
assert c['counts']['independent_row_equalities']==c['counts']['nonzero_rows']==s['counts']['exact_ratio_checks']==160
assert c['counts']['two_method_trace_equalities']==s['counts']['source_endpoint_float_diagnostics']==7812
assert [(r['NJ'],r['free'],len(r['rows'])) for r in c['families']]==[(0,False,32),(1,False,64),(1,True,64)]
assert all(r['zero_denominator_rows']==0 and r['nonzero_matrix_rows']==len(r['rows']) for r in s['families'])
for out in [c,s]:
 for n,h in out['files'].items():pin(n,h)
reviews=[]
for tag in ['projection_source_constraints_proof','projection_source_constraints_followup']:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text();text='\n\n'.join(v['text'] for v in raw['content'] if v['type']=='text')+'\n'
 assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5'
 assert m['stop_reason']==raw['stop_reason']=='end_turn' and text==(R/(tag+'_response.md')).read_text()
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert all(v in req for v in ['no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds'])
 assert req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files'])
 for n in m['files']:pin(n)
 for suff in ['_metadata.json','_request.txt','_response.json','_response.md']:pin(R/(tag+suff))
 if tag.endswith('_proof'):assert '**Verdict: OBJECTIONS.**' in text
 else:
  assert m['files']==load(D/'review_files.json')
  assert re.findall(r'^VERDICT: (\w+)\s*$',text,re.M)==['CONFIRM_EXPLICIT_PAIR_SOURCE_CONSTRAINTS_ONLY']
  assert [l for l in text.splitlines() if l.strip()][-1]=='VERDICT: CONFIRM_EXPLICIT_PAIR_SOURCE_CONSTRAINTS_ONLY'
  mandatory=['PROOF.md','REVIEW_RESOLUTION.md','MANUFACTURED_CORRECTION.md','RESULTS.md','code/check.py','code/check_supplement.py','code/finalize.py','evidence/checks.json','evidence/supplement.json']
  assert all(str((D/n).relative_to(B)) in m['files'] for n in mandatory)
  assert when(s['utc'])<when(m['start_utc'])
 reviews.append(m)
post=load(E/'postreview.json');m=reviews[-1]
assert when(m['end_utc'])<when(post['utc']) and post['status']=='CONFIRMED_AFTER_COMPLETE_REVIEW_AND_OWN_ADJUDICATION'
assert post['request_id']==m['request_id'] and post['input_sha256']==m['input_sha256'] and post['response_sha256']==sha(R/'projection_source_constraints_followup_response.json')
assert post['adjudication_sha256']==sha(D/'POSTREVIEW_ADJUDICATION.md') and post['all_substantive_objections_resolved'] is True
for p in sorted(D.rglob('*')):
 if p.is_file() and p.name!='verdict.json':pin(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_EXPLICIT_PAIR_SOURCE_CONSTRAINTS_ONLY','counts':c['counts'],'supplement_counts':s['counts'],'actual_reviews':[{k:m[k] for k in ['requested_model','actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']} for m in reviews],'postreview':post,'scope':'The three specified frozen-column/stored-vector pairs fail their exact-arithmetic source-only function-column constraints. New vector metadata omit joins/pickle hash, so no producer-run identity is attested. Exact cancellation levels are literal diagnostics. No physical join, ideal projection, Sobolev norm, inverse or PDE endpoint follows.','files':dict(sorted(pins.items()))}
with (E/'verdict.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(E/'verdict.json')}))

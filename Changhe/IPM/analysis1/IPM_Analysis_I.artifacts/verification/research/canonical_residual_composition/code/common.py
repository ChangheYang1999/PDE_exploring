from check import *
R=B/"notes/reviews"
def when(s):return datetime.fromisoformat(s)
def auth(pins,tag,verdict,required):
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));text=(R/(tag+'_response.md')).read_text();req=(R/(tag+'_request.txt')).read_text()
 need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn' and 'availability_error' not in m,'actual completed Opus5.5')
 need(len(m['files'])==len(set(m['files'])) and set(required)<=set(m['files']),'mandatory complete review bundle')
 pre=req.split('\n\nFILE ',1)[0];need(all(v in pre for v in ['no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds','no outside writes','no people contact']),'all delegated restrictions')
 need(req==pre+'\n\n'+'\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']) and hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'],'unchanged actual full request')
 need(text=='\n\n'.join(v['text'] for v in raw['content'] if v['type']=='text')+'\n','actual full response bytes')
 need(re.findall(r'(?m)^VERDICT:\s*(\w+)\s*$',text)==[verdict] and text.rstrip().splitlines()[-1]=='VERDICT: '+verdict,'unique exact scoped final verdict')
 need(when(m['start_utc'])<=when(m['end_utc'])<=datetime.now(timezone.utc),'actual review chronology')
 for n in m['files']:pin(pins,n)
 for suf in ['metadata.json','request.txt','response.json','response.md']:pin(pins,R/(tag+'_'+suf))
 return {k:m[k] for k in ['requested_model','actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
def post(pins,tag,review,record,assessment):
 v=load(record);rh=sha(R/(tag+'_response.json'));need(v['status']=='CONFIRMED_AFTER_COMPLETE_ACTUAL_REVIEW_AND_OWN_ADJUDICATION' and v['request_id']==review['request_id'] and v['input_sha256']==review['input_sha256'] and v['response_sha256']==rh and v['adjudication_sha256']==sha(assessment) and v['all_substantive_objections_resolved'] is True,'independent postreview record')
 need(review['request_id'] in assessment.read_text() and rh in assessment.read_text(),'written actual review binding');need(when(review['end_utc'])<when(v['utc'])<=datetime.now(timezone.utc),'actual later adjudication')
 m=load(R/(tag+'_metadata.json'));need(str(assessment.relative_to(B)) not in m['files'] and str(record.relative_to(B)) not in m['files'],'separately later post outside bundle');pin(pins,record);pin(pins,assessment);return v

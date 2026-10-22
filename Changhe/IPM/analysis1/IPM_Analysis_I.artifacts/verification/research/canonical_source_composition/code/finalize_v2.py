from common import *
def validate_extract():
 pins,p,v=full();z=load(E/'completion_extract.json');need(z['checks_sha256']==sha(E/'checks.json') and z['checks']=={k:x for k,x in v.items() if k!='files'},'literal completed169 projection')
 n='research/canonical_archive_second/evidence/verdict.json';d=load(B/n)
 need(z['156_verdict_sha256']==sha(B/n) and z['156_verdict']=={k:x for k,x in d.items() if k!='files'},'literal accepted156 projection')
 for name,h in z['distinguished_trial_pins'].items():need(d['files'][name]==h and sha(B/name)==h,'literal distinguished normalization pin')
 with (B/'research/canonical_archive_second/evidence/full_spans.jsonl').open() as f:head=load_line(f.readline())
 need(z['156_stream_header']==head,'verbatim actual complete156 header')
 pin(pins,E/'completion_extract.json');return pins,p,v

def load_line(s):return json.loads(s,object_pairs_hook=unique)
if __name__=='__main__':
 pins,p,v=validate_extract();tag='canonical_source_composition_actual_v2';review=auth(pins,tag,'CONFIRM_CANONICAL_SOURCE_ARCHIVE_PREMISE_DISCHARGED',load(D/'actual_files_v2.json'));old=load(R/'canonical_source_composition_actual_metadata.json')
 need(when(v['utc'])<when(old['start_utc'])<when(old['end_utc'])<when(review['start_utc']),'actual followup after original objections and completed application')
 for suffix in ['metadata.json','request.txt','response.json','response.md']:pin(pins,R/('canonical_source_composition_actual_'+suffix))
 postrecord=post(pins,tag,review,E/'postreview_record.json',D/'POSTREVIEW_ADJUDICATION.md')
 for n,h in pins.items():need(sha(B/n)==h,'immutable final pins')
 x={'utc':now(),'status':'CONFIRMED_CANONICAL_SOURCE_ARCHIVE_PREMISE_DISCHARGED','counts':v['counts'],'accepted_dependencies':v['accepted_dependencies'],'actual_output_review':review,'postreview':postrecord,'files':dict(sorted(pins.items())),'scope':v['scope']+' Physical source conclusions concern only the distinguished exactly normalized trial; auxiliary family uniform inclusion does not normalize every z in Z.'};write(E/'verdict.json',x);print(json.dumps({'utc':x['utc'],'status':x['status'],'pins':len(pins),'sha256':sha(E/'verdict.json')}))

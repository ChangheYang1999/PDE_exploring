from common import *
p,v=complete();out={k:x for k,x in v.items() if k not in ['files','proof_review']};out['checks_sha256']=sha(E/'checks.json');out['extract_utc']=now();write(E/'review_extract.json',out);print(json.dumps({'utc':out['extract_utc'],'status':'COMPLETE_CANONICAL_TAIL_REVIEW_EXTRACT','sha256':sha(E/'review_extract.json')}))

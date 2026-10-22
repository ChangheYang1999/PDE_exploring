from common import *
p,v=complete();x={k:z for k,z in v.items() if k not in ['files','proof_review']};x.update(checks_sha256=sha(E/'checks.json'),extract_utc=now());write(E/'review_extract.json',x);print(json.dumps({'utc':x['extract_utc'],'status':v['status'],'ceilings':v['strict_decimal_ceilings']}))

from common import *
p,v=complete();out={k:z for k,z in v.items() if k!='files'};out.update(extract_utc=now(),checks_sha256=sha(E/'checks.json'));write(E/'review_extract.json',out);print(json.dumps({'utc':out['extract_utc'],'sha256':sha(E/'review_extract.json')}))

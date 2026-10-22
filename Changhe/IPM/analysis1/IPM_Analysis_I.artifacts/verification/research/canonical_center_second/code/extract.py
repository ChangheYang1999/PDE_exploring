from common import *
p,deps,prep,s,a,q=collect();out={'utc':now(),**projection(deps,prep,s,a,q)};rehash(p);write(E/'review_extract.json',out);print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(p),'sha256':sha(E/'review_extract.json')}))

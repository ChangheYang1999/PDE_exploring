from common import *
pins,x=collect();write(D/'evidence/review_extract.json',x);print(json.dumps({'utc':x['utc'],'status':x['status'],'pins':len(pins)}))

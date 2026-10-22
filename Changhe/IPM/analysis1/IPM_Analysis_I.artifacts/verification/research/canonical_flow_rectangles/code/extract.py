from common import *
p,deps,v,targets=collect();write(E/'review_extract.json',{'utc':now(),**projection(deps,v,targets)});print('EXTRACT',sha(E/'review_extract.json'),len(p))

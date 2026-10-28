from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import requests,json
queries=['sharp Holder norm Beurling Ahlfors transform','exact norm singular integral Holder space','Holder norm estimate Hilbert transform Clifford analysis','singular integrals Lipschitz spaces sharp constants']
out=Path('04_literature/sources')
def run(q):
 r=requests.get('https://api.crossref.org/works',params={'query':q,'rows':8},timeout=35);r.raise_for_status();d=r.json();name='crossref_0507_'+str(queries.index(q))+'.json';(out/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 return {'query':q,'file':name,'results':[{'title':x.get('title'), 'DOI':x.get('DOI'),'URL':x.get('URL'),'link':x.get('link',[])} for x in d['message']['items']]}
with ThreadPoolExecutor(max_workers=4) as ex:
 results=list(ex.map(run,queries))
manifest={'time_utc':datetime.now(timezone.utc).isoformat(),'results':results,'status':'Discovery metadata only. No theorem claim has been checked from these results.'}
(out/'crossref_0507_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n');print(json.dumps(manifest,ensure_ascii=False,indent=2))

from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
import hashlib,json,time,xml.etree.ElementTree as E
v=Path('research/193_recent_literature_search/verification')
urls={f'abs_{k}':f'https://arxiv.org/abs/{k}' for k in ['2610.27650','2610.28403','2607.19700','2509.14185']}
urls['Boussinesq_last_updated_api']='https://export.arxiv.org/api/query?search_query=all%3ABoussinesq&start=0&max_results=100&sortBy=lastUpdatedDate&sortOrder=descending'
def run(item):
 name,url=item;t=time.monotonic();d={'name':name,'url':url,'start_utc':datetime.now(timezone.utc).isoformat()}
 try:
  with urlopen(Request(url,headers={'User-Agent':'B2-independent-research-audit/1.0'}),timeout=35) as r:
   b=r.read();p=v/(name+'.txt');p.write_bytes(b);d.update(status=r.status,final_url=r.url,headers={k:r.headers.get(k) for k in ['Date','Last-Modified','Content-Type','Content-Length']},bytes=len(b),path=str(p),sha256=hashlib.sha256(b).hexdigest())
 except Exception as e:d.update(error=repr(e))
 d.update(end_utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-t);return d
start=time.monotonic()
with ThreadPoolExecutor(max_workers=4) as ex:out=list(ex.map(run,urls.items()))
(v/'followup_retrieval.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-start,'results':out},indent=2)+'\n')
ns={'a':'http://www.w3.org/2005/Atom'}
p=v/'Boussinesq_last_updated_api.txt'
if p.exists():
 root=E.fromstring(p.read_bytes());rows=[]
 for x in root.findall('a:entry',ns):rows.append({k:' '.join((x.findtext('a:'+k,default='',namespaces=ns)).split()) for k in ['id','title','published','updated','summary']})
 (v/'updated_entries.json').write_text(json.dumps(rows,indent=2)+'\n')
 print(json.dumps({'latest':rows[:12],'count':len(rows)},indent=2))
print(json.dumps(out,indent=2))

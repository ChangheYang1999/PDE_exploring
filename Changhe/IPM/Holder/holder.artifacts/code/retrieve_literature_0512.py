from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import requests,json,subprocess
sources=[('clifford_holder_2010','https://link.springer.com/content/pdf/10.1007/s00574-010-0017-9.pdf'),('douglis_holder_2017','https://link.springer.com/content/pdf/10.1186/s13660-017-1488-7.pdf')]
root=Path('04_literature/sources')
def get(item):
 name,url=item
 try:
  r=requests.get(url,timeout=40);pdf=r.content.startswith(b'%PDF');p=root/(name+('.pdf' if pdf else '.html'));p.write_bytes(r.content)
  if pdf:subprocess.run(['pdftotext','-layout',str(p),str(root/(name+'.txt'))],check=True,timeout=25)
  return dict(name=name,url=url,status=r.status_code,pdf=pdf,file=str(p),bytes=len(r.content))
 except Exception as e:return dict(name=name,url=url,error=str(e))
with ThreadPoolExecutor(max_workers=2) as ex:results=list(ex.map(get,sources))
d=dict(time_utc=datetime.now(timezone.utc).isoformat(),results=results);(root/'retrieval_0512.json').write_text(json.dumps(d,indent=2)+'\n');print(d)

from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
import hashlib,json,xml.etree.ElementTree as E
v=Path('research/193_recent_literature_search/verification');checks=[]
for fn in ['retrieval.json','followup_retrieval.json']:
 d=json.loads((v/fn).read_text())
 for x in d['results']:
  p=Path(x['path']);assert x['status']==200 and p.stat().st_size==x['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'];checks.append(x['name'])
a=json.loads((v/'availability_retrieval.json').read_text());assert hashlib.sha256((v/'arxiv_availability.html').read_bytes()).hexdigest()==a['sha256'];checks.append('official_availability_hash')
for name,count in [('search_entries',50),('daily_entries',91),('atom_entries',33),('updated_entries',100)]:
 d=json.loads((v/(name+'.json')).read_text());assert len(d)==count;checks.append(name+'_count')
u=json.loads((v/'updated_entries.json').read_text());assert all(datetime.fromisoformat(x['updated'])<datetime(2026,10,21,3,tzinfo=timezone.utc) for x in u);checks.append('all100_versions_prethreshold')
a=json.loads((v/'atom_entries.json').read_text());assert not any('2509.14185' in json.dumps(x) for x in a);checks.append('known_related_positive_control_missing_from_narrow_query')
source=(v/'abs_2607.19700_visible.txt').read_text();assert 'main theorem and proof unchanged, added Proposition 4.3' in source;checks.append('author_comment_present')
announcement=datetime(2026,10,21,20,tzinfo=ZoneInfo('America/New_York')).astimezone(timezone.utc);assert announcement==datetime(2026,10,22,0,tzinfo=timezone.utc);checks.append('announcement_time_zone_conversion')
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'count':len(checks),'earliest_normal_postthreshold_announcement_UTC':announcement.isoformat(),'max_returned_Boussinesq_updated':max(x['updated']for x in u),'scope':'Provenance/count/date controls, not tests of literature exhaustiveness or mathematical theorems.'};(v/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

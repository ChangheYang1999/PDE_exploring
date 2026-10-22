from common import *
def build():
 rows={}
 for key,n in [('main','checks.json'),('chain','chain_checks.json'),('scope','scope_checks.json')]:
  p=E/n;v=load(p);rows[key]={'sha256':sha(p),'value':{k:x for k,x in v.items() if k!='files'}}
 for key,n in DEPS.items():
  p=B/n[0];v=load(p);rows[key]={'path':n[0],'sha256':sha(p),'value':{k:x for k,x in v.items() if k!='files'}}
 with (B/'research/canonical_archive_second/evidence/full_spans.jsonl').open() as f:rows['156_stream_header']=parse(next(f))
 return rows
if __name__=='__main__':write(E/'completion_extract.json',build());print(json.dumps({'utc':now(),'bytes':(E/'completion_extract.json').stat().st_size}))

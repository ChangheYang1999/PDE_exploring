"""Extract the final canonical span while checking the complete archive provenance."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import gzip,json,hashlib,time
from pathlib import Path
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/outer_majorant/evidence';M=BASE/'research/middle_residual/evidence'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
start=time.monotonic();p=M/'original_knots.jsonl.gz';archive='c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648'
assert sha(p)==archive
audit=json.loads((M/'knot_audit.json').read_bytes());assert audit['status']=='PASS' and audit['archive_sha256']==archive and audit['footer_read']
assert sha(M/'knot_audit.json')=='decad65da9e0f347f63f2bd89f3317de2afc4a88500b6fb45b89b7a1869f5eeb'
assert sha(M/'knot_manifest.json')==audit['manifest_sha256'];assert sha(M/'partition_exact.json')==audit['partition_sha256']
with gzip.open(p,'rb') as f:
 head=json.loads(next(f));prev=None;last=None;lines=0
 for line in f:
  assert line.endswith(b'\n');prev,last=last,line;lines+=1
assert lines==1559 and head['spans']==1558 and head['stream_modes']==261
row=json.loads(prev);footer=json.loads(last);assert row['type']=='span' and row['span']==1557 and footer['type']=='complete' and footer['spans']==1558 and footer['cells']==7809
part=json.loads((M/'partition_exact.json').read_bytes())['spans'][-1];assert all(row[k]==v for k,v in part.items())
(E/'final_span.json').write_bytes(prev)
r={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':sha(__file__),'archive_sha256':archive,'archive_audit_sha256':sha(M/'knot_audit.json'),'final_span_sha256':sha(E/'final_span.json'),'header':head,'footer':footer,'full_gzip_footer_read':True,'seconds':time.monotonic()-start,'scope':'Extracted canonical boundary data; no fresh whole-archive integration.'}
(E/'final_span_extract.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'utc':r['utc'],'status':'PASS','seconds':r['seconds']}))

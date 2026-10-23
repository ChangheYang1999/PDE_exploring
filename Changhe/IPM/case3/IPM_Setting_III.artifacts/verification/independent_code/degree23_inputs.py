"""Read exact compressed snapshots for the independent degree23 audit."""
from pathlib import Path
import gzip,json,hashlib
ROOT=Path('research/degree23_grouped_moment_obstruction');VERIFY=ROOT/'verification'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(rel):
 manifest=json.loads((VERIFY/'INPUTS.json').read_text());p=VERIFY/'external'/(rel+'.gz')
 record=next(r for r in manifest['files']if r['frozen']==str(p));raw=p.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==record['compressed_sha256']
 decoded=gzip.decompress(raw);assert len(decoded)==record['bytes']and hashlib.sha256(decoded).hexdigest()==record['sha256']
 return json.loads(decoded)if rel.endswith('.json')else decoded.decode()
def certificate(name):return load('d23/certificates/'+name+'.json')

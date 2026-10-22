"""Finalize only the reviewed primary assembly and authenticate all actual model reviews."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys
if sys.flags.optimize:raise ValueError('optimization forbidden')
B=Path(__file__).resolve().parents[3];D=B/'research/global_residual_assembly';R=B/'notes/reviews'
def require(x,s):
 if not x:raise ValueError(s)
def load(p):return json.loads(p.read_text())
def sha(p):
 with p.open('rb') as h:return hashlib.file_digest(h,'sha256').hexdigest()
a=load(D/'evidence/primary_assembly_v2.json');c=load(D/'evidence/assembly_checks_v2.json')
require(a['status']=='COMPUTED_PRIMARY_REGIONAL_ASSEMBLY_REQUIRES_REVIEW','assembly status')
require(c['status']=='PASS_DIRECT_ARITHMETIC_PINS_AND_SUBJECT_CONTRACTS' and c['categories']=={'direct_saved_output_arithmetic':48,'sha256_rechecks':182,'synthetic_subject_contracts':37},'checker categories')
require(c['assembly_sha256']==sha(D/'evidence/primary_assembly_v2.json') and c['assembly_source_sha256']==sha(D/'code/assemble_primary_v2.py'),'checker output/source binding')
pins=dict(a['files']);require(len(pins)==182,'expected distinct assembly inputs')
for f,h in pins.items():require(sha(B/f)==h,'input hash '+f)
for name in ['dependency_extract.json','dependency_extract_v2.json']:
 x=load(D/'evidence'/name)
 if name=='dependency_extract.json':continue
 for item in x['entries']:
  p=B/item['file'];require(sha(p)==item['sha256'],'extract digest')
  if 'selected_fields' in item:
   full=load(p)
   for k,v in item['selected_fields'].items():require(full[k]==v,'extract field '+k)
  if 'verbatim_excerpt' in item:require('\n'.join(p.read_text().splitlines()[item['first_line']-1:item['last_line']])==item['verbatim_excerpt'],'extract text')
  if 'all_top_level_keys' in item:require(list(load(p))==item['all_top_level_keys'],'extract full key set')
  pins[item['file']]=item['sha256']
reviews={}
for tag,expected in [('global_residual_first','c80ed871ab917da126abbbe4ec9ddd6b00419923b5e41a3af72a25708ade5e36'),('global_residual_completed','aad96a2c7e75469bc401204c53ff257462927666c0b32096caed95b49c9f09e7'),('global_residual_repaired','f03c7c7889f7bded0aa9699329d1a72814188cf5396ab95bd86974556146b8e8')]:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 require(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn','actual model/stop')
 require(hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']==expected,'review request hash')
 require(req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']),'review current bundle')
 text='\n\n'.join(q['text'] for q in raw['content'] if q['type']=='text')+'\n'
 require(text==(R/(tag+'_response.md')).read_text(),'review raw text')
 if tag.endswith('repaired'):require('FINAL is justified' in text and 'PRIMARY_ONLY' in text and 'OPEN' in text,'final review scope')
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_request.txt','_response.json','_response.md']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for root in [D,D/'code',D/'evidence']:
 for p in root.iterdir():
  if not p.is_file() or p.is_symlink() or p.name=='verdict.json':continue
  f=str(p.relative_to(B));h=sha(p);require(f not in pins or pins[f]==h,'final pin collision');pins[f]=h
E=sum((F(q['squared_norm_exact']) for q in a['regions'].values()),F(0))
require(E==F(a['global_N2']['input_squared_exact']) and E<F(a['global_N2']['strict_upper_decimal'])**2,'final exact norm')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_PRIMARY_ONLY_WHOLE_PLANE_ZEROTH_RESIDUAL_ASSEMBLY','cells':{'inner':54,'middle':7809,'outer':89},'suprema':a['global_suprema'],'N2':a['global_N2'],'independent_scalar_checks':a['middle_scalar_checks'],'reviews':reviews,'files':dict(sorted(pins.items())),'scope':'Mandatory FINAL_ADJUDICATION. Accepted regional and canonical archive dependencies; scalar recomputation only. Full topic46 coefficient check and queued canonical linkage remain OPEN, as do derivative/forcing/distance/inverse/nonlinear/exponent and both PDE endpoints. No early finish.'}
p=D/'evidence/verdict.json';p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))

"""Exact original decimal-token rounding cells and independent bit/export binding."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal
from fractions import Fraction as F
import json,gzip,math,struct,hashlib,time
B=Path(__file__).resolve().parents[3];D=B/'research/literal_derivative_cell_union';S=B/'research/weighted_derivative_scalar_norms'
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def bitq(v):
 bits=struct.unpack('>Q',struct.pack('>d',v))[0];e=(bits>>52)&2047;m=bits&((1<<52)-1);need(e!=2047,'finite binary64');return (-1 if bits>>63 else 1)*F(((1<<52)+m) if e else m)*F(2)**(e-1075 if e else -1074),bits
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();p=json.loads((D/'evidence/sweep.json').read_text());pins=dict(p['files']);checks=0;ties=0
for n,h in pins.items():need(sha(B/n)==h,'all immutable source pins')
with gzip.open(S/'data_exact/rows.jsonl.gz','rt') as f:
 for reg in ['inner','middle','outer']:
  text=(S/'sources'/('derivative_'+reg+'.json')).read_text();raw=json.loads(text,parse_float=Decimal)['rows'];binary=json.loads(text)['rows'];need(len(raw)==len(binary),'all source tokens')
  for j,(rr,br) in enumerate(zip(raw,binary,strict=True)):
   er=json.loads(next(f));need(er['region']==reg and er['index']==rr['ci']==br['ci']==j,'complete ordered source identity')
   for name in ['t_a','h']:
    need(type(rr[name]) is Decimal and type(br[name]) is float,'decimal versus binary token');v,bits=bitq(br[name]);prev,_=bitq(math.nextafter(br[name],-math.inf));nxt,_=bitq(math.nextafter(br[name],math.inf));lo,hi=(v+prev)/2,(v+nxt)/2;original=F(rr[name]);need(prev<v<nxt and lo<=original<=hi,'exact nearest binary64 rounding cell')
    if original in [lo,hi]:need(bits&1==0,'ties to even');ties+=1
    need(v==F(er['exact'][name]),'manual bit decode equals immutable exact row export');checks+=1
 need(next(f,None) is None,'full export consumed')
need(checks==38778,'all geometry scalar tokens')
for x in [Path(__file__),D/'ADDENDUM.md',D/'evidence/sweep.json',D/'evidence/sweep.log']:pins[str(x.relative_to(B))]=sha(x)
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ALL_ORIGINAL_DECIMAL_ROUNDING_CELLS_AND_EXACT_EXPORT_BINDING','source_tokens':checks,'manual_bit_export_equalities':checks,'midpoint_ties':ties,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick}
with (D/'evidence/decimal.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k!='files'},indent=2))

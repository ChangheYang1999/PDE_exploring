"""Atomic finite MP row chunks. No derivative or quadrature error certification."""
from pathlib import Path
from fractions import Fraction as F
import gzip,json,hashlib,re
import mpmath as mp

DECIMAL=re.compile(r'^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$')
def digest_rows(rows):return hashlib.sha256(json.dumps(rows,separators=(',',':'),ensure_ascii=True).encode()).hexdigest()
def decimal_value(s):
 if not isinstance(s,str)or len(s)>2048 or not DECIMAL.fullmatch(s):raise ValueError('invalid finite decimal string')
 if 'e' in s.lower() and abs(int(s.lower().split('e')[1]))>1000:raise ValueError('decimal exponent outside finite artifact contract')
 q=F(s)
 if q.denominator<=0:raise ValueError('invalid rational denominator')
 return q
def encode_values(values,digits,width):
 if len(values)!=width:raise ValueError('wrong row width')
 out=[]
 for a in values:
  if not mp.isfinite(a):raise ArithmeticError('nonfinite MP value')
  s=mp.nstr(a,digits+20);decimal_value(s)
  if mp.mpf(s)!=a:raise ArithmeticError('decimal failed precision roundtrip')
  out.append(s)
 return out

class MPChunkStore:
 def __init__(self,directory,total,digits,width,bindings,chunk_size=64):
  if type(total)is not int or total<1 or type(digits)is not int or digits<20 or type(width)is not int or width<1 or type(chunk_size)is not int or chunk_size<1:raise ValueError('invalid chunk dimensions')
  self.directory=Path(directory);self.directory.mkdir(exist_ok=True,parents=True)
  self.total=total;self.digits=digits;self.width=width;self.bindings=bindings;self.chunk_size=chunk_size
  self.signature=dict(schema='FINITE_MP_DECIMALS_V1',total=total,digits=digits,width=width,chunk_size=chunk_size,bindings=bindings)
  expected={self.name(i)for i in range(0,total,chunk_size)}
  if set(p.name for p in self.directory.glob('chunk_*.json.gz'))-expected:raise ValueError('unexpected chunk filename')
 def name(self,start):return f'chunk_{start:07d}.json.gz'
 def read(self,start):
  path=self.directory/self.name(start)
  with gzip.open(path,'rt')as f:d=json.load(f)
  if set(d)!=set(self.signature)|{'start','stop','rows','rows_sha256'}or any(d[k]!=v for k,v in self.signature.items()):raise ValueError('chunk schema/signature mismatch')
  if type(d['start'])is not int or type(d['stop'])is not int or d['start']!=start or d['stop']!=min(start+self.chunk_size,self.total):raise ValueError('wrong chunk interval')
  rows=d['rows']
  if not isinstance(rows,list)or len(rows)!=d['stop']-start or any(not isinstance(row,list)or len(row)!=self.width for row in rows):raise ValueError('wrong chunk row shape')
  for row in rows:
   for v in row:decimal_value(v)
  if d['rows_sha256']!=digest_rows(rows):raise ValueError('chunk row digest mismatch')
  return rows
 def run(self,compute,after_checkpoint=None):
  all_rows=[]
  for start in range(0,self.total,self.chunk_size):
   stop=min(start+self.chunk_size,self.total);path=self.directory/self.name(start)
   with mp.workdps(self.digits):
    if path.exists():
     rows=self.read(start)
     if rows[-1]!=encode_values(compute(stop-1),self.digits,self.width):raise ValueError('MP boundary replay differs')
    else:
     rows=[encode_values(compute(i),self.digits,self.width)for i in range(start,stop)]
     d=dict(self.signature,start=start,stop=stop,rows=rows,rows_sha256=digest_rows(rows));raw=json.dumps(d,sort_keys=True,separators=(',',':'),allow_nan=False).encode();tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_bytes(gzip.compress(raw,mtime=0));tmp.replace(path)
   all_rows.extend(rows)
   if after_checkpoint is not None:after_checkpoint(stop)
  return all_rows

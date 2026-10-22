from pathlib import Path
from datetime import datetime,timezone
from flint import fmpq
import json,hashlib,struct,zipfile,ast,math
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parents[1]
D=json.loads((ROOT/'evidence/check.json').read_text());M=json.loads((ROOT/'data_exact/manifest.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for p,s in M['sources'].items():assert sha(BASE.parent/p)==s
for p,s in M['copied'].items():assert sha(BASE/p)==s
for row in M['source_arrays'].values():assert list(row)==D['keys']
def rat(x):
 bits=int.from_bytes(struct.pack('>d',x),'big');b=bits>>63;e=(bits>>52)&2047;m=bits&((1<<52)-1)
 assert e<2047
 n=m if e==0 else (1<<52)+m;shift=-1074 if e==0 else e-1075
 n=-n if b else n
 return fmpq(n*(1<<max(0,shift)),1<<max(0,-shift))
def qr(s):
 p=s.split('/');return fmpq(int(p[0]),int(p[1]) if len(p)==2 else 1)
rows={'L2':'NJ0','L2q':'NJ1_rowsL2q','H1':'NJ1_rowsH1','H1q':'NJ1_rowsH1q'}
lookup={};counts=0
for row,tail in rows.items():
 for pp,stem in [(2,'p2'),(4,'p4_re2'),(6,'p6')]:
  v=json.loads((ROOT/'sources'/f'c2gram2_M16_s16_{stem}_H1m_{tail}.json').read_text())
  lookup[row,pp]=list(map(rat,v['sections']['Fminus']['sigma_small5']))
  sec=v['sections']['Fminus'];nj=0 if row=='L2' else 1
  assert v['ppc']==pp and v['NJ']==nj and v['Mh']==16 and v['stride']==16 and v['Mout']==40
  assert sec['ncol']==1955 and sec['n_constraints']==32*(nj+1) and sec['constraint_rank']==32*(nj+1)
  assert sec['nfree']==1955-32*(nj+1)
  assert (sec['n_kept'],sec['n_kept_at_1em12'])==((1866,1887) if nj==0 else (1834,1855))
  assert v['n_collocation_rows']==40*v['Ne']
  assert v['nrows']==(40*v['Ne'] if row.startswith('L2') else 40*(2*v['Ne']-1))
for x in D['records']:
 a=lookup[x['row'],x['p']][x['j']];b=lookup[x['row'],x['q']][x['j']];assert a>0 and b>0 and a!=b
 for k,v in [('old',a),('new',b),('delta',b-a),('relative',abs(b-a)/a),('relative_to_new',abs(b-a)/b)]:assert qr(x[k])==v
 counts+=1
for x in D['maxima']:
 values=[abs(b-a)/a for a,b in zip(lookup[x['row'],x['p']],lookup[x['row'],x['q']])]
 mx=max(values);assert qr(x['maximum'])==mx and values[x['index']]==mx
 lo,hi=map(qr,x['window']);assert lo<=mx<=hi and hi-lo==fmpq(1,10**12)
array_count=0;byte_count=0;base_arrays=None
for ident,vp in M['vectors'].items():
 arrays={}
 with zipfile.ZipFile(BASE.parent/vp) as z:
  for k,s in M['source_arrays'][ident].items():
   raw=z.read(k+'.npy');assert raw[:6]==b'\x93NUMPY';version=raw[6:8];assert version in [b'\x01\x00',b'\x02\x00']
   sz=2 if version[0]==1 else 4;nl=int.from_bytes(raw[8:8+sz],'little');off=8+sz+nl
   header=ast.literal_eval(raw[8+sz:off].decode('latin1').strip());assert header['fortran_order'] is False
   assert list(header['shape'])==s['shape'] and header['descr']==s['dtype']
   payload=raw[off:];assert len(payload)==s['bytes'] and hashlib.sha256(payload).hexdigest()==s['sha256']
   arrays[k]=(header['shape'],header['descr'],payload);array_count+=1;byte_count+=len(payload)
 if base_arrays is None:base_arrays=arrays
 assert arrays==base_arrays
opaque=[(BASE.parent/p).read_bytes() for p in M['metadata'].values()];assert opaque[0]==opaque[1]==opaque[2]
assert counts==D['comparisons']==40 and array_count==D['array_comparisons']==228 and byte_count==D['payload_bytes']
ans=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_INDEPENDENT_IEEE_FMPQ_AND_RAW_NPY',comparisons=counts,maxima=8,array_comparisons=array_count,payload_bytes=byte_count,source_pins=len(M['sources']),copied_pins=len(M['copied']),pickle_executed=False)
(ROOT/'evidence/audit.json').write_text(json.dumps(ans,indent=2)+'\n');print(json.dumps(ans,indent=2))

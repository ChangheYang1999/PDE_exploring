from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import ast,struct,pickle,io,json,hashlib,sys,zipfile,math
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_internal_jumps'
def check(v,s):
 if not v:raise ValueError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
class DT:
 def __init__(self,code,*args):self.code=code;self.endian='<'
 def __setstate__(self,state):self.endian=state[1]
class AR:
 def __setstate__(self,s):
  ver,shape,dt,order,blob=s;check(ver==1 and isinstance(shape,tuple) and len(shape)==1 and shape[0]<10000 and dt.code=='f8' and dt.endian in ('<','=','>') and len(blob)==8*shape[0],'array state')
  self.values=struct.unpack(dt.endian+'d'*shape[0],blob)
 def __iter__(self):return iter(self.values)
 def __len__(self):return len(self.values)
 def __getitem__(self,i):return self.values[i]
def recon(cls,shape,code):
 check(cls is AR and shape==(0,) and code==b'b','reconstruct signature');return AR()
def scalar(dt,blob):
 check(dt.code=='f8' and dt.endian in ('<','=','>') and len(blob)==8,'scalar');return struct.unpack(dt.endian+'d',blob)[0]
class Reader(pickle.Unpickler):
 globals=[]
 def find_class(self,m,n):
  self.globals.append([m,n]);allowed={('numpy','dtype'):DT,('numpy','ndarray'):AR}
  for mod in ['numpy._core.multiarray','numpy.core.multiarray']:allowed[mod,'_reconstruct']=recon;allowed[mod,'scalar']=scalar
  check((m,n) in allowed,'unapproved global');return allowed[m,n]
def dy(x):
 bits=struct.unpack('>Q',struct.pack('>d',x))[0];sign=-1 if bits>>63 else 1;exp=(bits>>52)&2047;mant=bits&((1<<52)-1);check(exp!=2047,'finite dyadic')
 if exp:mant+=1<<52;power=exp-1075
 else:power=-1074
 return F(sign*mant*(1<<max(power,0)),1<<max(-power,0))
def enc(x):return str(x.numerator)+'/'+str(x.denominator)
def poly(c,x):return sum((dy(z)*x**j for j,z in enumerate(c)),F(0))
manifest=json.loads((D/'evidence/manifest.json').read_text());records=[];scalars=[];pins={}
for rr in manifest['files'][:4]:
 p=B/rr['copy'];check(sha(p)==rr['sha256'],'pickle source');pins[rr['copy']]=sha(p);meta=Reader(io.BytesIO(p.read_bytes())).load();cells=list(meta['cells']);check(all(math.isfinite(z) for z in cells) and all(dy(a)<dy(b) for a,b in zip(cells,cells[1:])),'cells');lo,hi=cells[0],cells[-1]
 raw=Path(rr['source'].replace('_cols.pkl','.npz'))
 if raw.exists():
  st=raw.stat()
  with zipfile.ZipFile(raw) as z:
   for key,value in [('tmin',lo),('t0',hi)]:
    info=z.getinfo(key+'.npy');check(info.file_size<1024,'scalar npy size');blob=z.read(info);check(blob[:8]==b'\x93NUMPY\x01\x00','npy version')
    hlen=struct.unpack('<H',blob[8:10])[0];header=ast.literal_eval(blob[10:10+hlen].decode('ascii').strip());check(header=={'descr':'<f8','fortran_order':False,'shape':()},'npy scalar descriptor')
    body=blob[10+hlen:];check(len(body)==8,'npy scalar body');v=struct.unpack('<d',body)[0];check(dy(v)==dy(value),'actual raw scalar equals metadata endpoint')
    dest=D/'sources'/(raw.stem+'__'+key+'.npy');check(not dest.exists(),'immutable scalar snapshot');dest.write_bytes(blob);pins[str(dest.relative_to(B))]=sha(dest)
    scalars.append({'source_raw':str(raw),'raw_size':st.st_size,'raw_mtime_ns':st.st_mtime_ns,'member':key+'.npy','member_CRC32':info.CRC,'member_header_offset':info.header_offset,'copy':str(dest.relative_to(B)),'sha256':sha(dest),'exact_value':enc(dy(v)),'hex':v.hex(),'scope':'Only this member is pinned, not the full raw matrix or its historical execution.'})
  check(raw.stat().st_size==st.st_size and raw.stat().st_mtime_ns==st.st_mtime_ns,'raw changed during scalar extraction')
 else:scalars.append({'source_raw':str(raw),'status':'OPEN_MISSING_RAW_MATRIX','scope':'No historical external-join scalar linkage claimed for this absent raw file.'})
 stats={'columns':len(meta['cols']),'eligible_m0_interior_sp_columns':0,'tested_endpoints':0,'nonzero_endpoints':0,'columns_with_nonzero_jump':0};witness=None
 for ci,(mode,pcs,lab) in enumerate(meta['cols']):
  if mode!=0 or lab[:2]!='sp' or not pcs:continue
  if not all(dy(lo)<dy(a)<dy(b)<dy(hi) and dy(al)==0 for a,b,al,c in pcs):continue
  for a,b,al,c in pcs:check(0<len(c)<=8 and all(math.isfinite(x) for x in c),'polynomial length/finite')
  check(all(dy(pcs[i][1])<=dy(pcs[i+1][0]) for i in range(len(pcs)-1)),'sorted disjoint')
  stats['eligible_m0_interior_sp_columns']+=1;bad=0
  ends=sorted(set([a for a,b,al,c in pcs]+[b for a,b,al,c in pcs]))
  for t in ends:
   left=F(0);right=F(0)
   for a,b,al,c in pcs:
    if dy(b)==dy(t):left+=poly(c,dy(t)-dy(a))
    if dy(a)==dy(t):right+=dy(c[0])
   delta=right-left;stats['tested_endpoints']+=1
   if delta:
    bad=1;stats['nonzero_endpoints']+=1
    if witness is None and dy(pcs[0][0])<dy(t)<dy(pcs[-1][1]):
     check(F(1,10**22)<abs(delta)<F(1,10**14),'rational bound')
     witness={'column_index_zero_based':ci,'mode':mode,'label':lab,'tmin_hex':lo.hex(),'t0_hex':hi.hex(),'tstar_hex':t.hex(),'pieces':[{'a_hex':a.hex(),'b_hex':b.hex(),'alpha_hex':al.hex(),'coefficients_hex':[x.hex() for x in c]} for a,b,al,c in pcs],'left_exact':enc(left),'right_exact':enc(right),'delta_right_minus_left_exact':enc(delta)}
  stats['columns_with_nonzero_jump']+=bad
 check(witness is not None,'witness');records.append({'source':rr['copy'],'statistics':stats,'witness':witness})
# Compare to the first implementation only after all data calculations.
primary=json.loads((D/'evidence/compute.json').read_text());check(primary['status']=='PASS_EXACT_HORNER_INTERNAL_JUMP_WITNESSES','primary status')
for a,b in zip(records,primary['records'],strict=True):
 check(a['source']==b['source'] and a['statistics']==b['statistics'],'independent counts')
 for k,v in a['witness'].items():check(v==b['witness'][k],'independent witness '+k)
for n,h in primary['files'].items():check(sha(B/n)==h,'primary pin');pins[n]=h
for p in [Path(__file__),D/'evidence/compute.json']:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_BIT_DECODE_DIRECT_POWER_SUM_AND_RAW_ENDPOINT_LINKAGE','method':'No NumPy imported; restricted pickle proxy decodes raw f8 bytes; binary64 bit extraction and direct exact polynomial power sums; zip member scalar extraction only. All eligible mode-zero columns recomputed before primary comparison.','loaded_globals':Reader.globals,'records':records,'raw_scalar_linkage':scalars,'files':pins,'scope':'All four saved metadata sets encode internal jump directions strictly within their cells endpoints. M24 raw external-join endpoints linked exactly; M16 raw matrices absent, their scalar linkage remains OPEN. Retained Gram subspace and singular vectors untested.'}
check(not(D/'evidence/independent.json').exists(),'immutable');(D/'evidence/independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'files':len(pins),'raw_scalars':len(scalars),'unique_pickle_hashes':len(set(r['sha256'] for r in manifest['files'][:4])),'statistics':[r['statistics'] for r in records]}))

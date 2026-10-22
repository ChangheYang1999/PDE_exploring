from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import ast,struct,pickle,io,json,hashlib,sys,zipfile,math
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_jump_rank'
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
V=B/'research/gram_internal_jumps';outrows=[];pins={};piece_count=0
for stem in ['c2raw_M16_s16_p4_cols','c2raw_M24_s8_p4_cols']:
 p=V/'sources'/(stem+'.pkl');meta=Reader(io.BytesIO(p.read_bytes())).load();M=len(set(m for m,pc,lab in meta['cols']));columns=[pc for m,pc,lab in meta['cols']]+[meta['kp_pieces'],meta['tau_pieces']]
 for pcs in columns:
  check(bool(pcs),'nonempty pieces')
  for a,b,al,c in pcs:
   check(not math.isnan(a) and not math.isnan(b) and a<b and math.isfinite(al) and bool(c) and all(math.isfinite(v) for v in c),'locally finite piecewise smooth coefficients');piece_count+=1
 outrows.append({'source':str(p.relative_to(B)),'mode_count':M,'function_columns':len(meta['cols']),'KP_TAU':'Both saved radial piece lists have finite coefficients/exponents and ordered endpoints; arbitrary finite angular coefficients yield locally piecewise smooth functions.'});pins[str(p.relative_to(B))]=sha(p)
raw=B.parent/'ipmA-num/runs/c2/c2raw_M24_s8_p4.npz';st=raw.stat();(D/'sources').mkdir(exist_ok=True)
with zipfile.ZipFile(raw) as z:
 info=z.getinfo('Mh.npy');check(info.file_size<1024,'small Mh member');blob=z.read(info)
check(blob[:8]==b'\x93NUMPY\x01\x00','npy header');length=struct.unpack('<H',blob[8:10])[0];header=ast.literal_eval(blob[10:10+length].decode().strip());check(header=={'descr':'<i8','fortran_order':False,'shape':()},'integer scalar');body=blob[10+length:];check(len(body)==8,'int64 scalar');mh=struct.unpack('<q',body)[0];check(mh==outrows[-1]['mode_count']==24,'actual M24 Mh count');check(raw.stat().st_size==st.st_size and raw.stat().st_mtime_ns==st.st_mtime_ns,'raw stable');dst=D/'sources/M24_Mh.npy';check(not dst.exists(),'immutable member');dst.write_bytes(blob);pins[str(dst.relative_to(B))]=sha(dst)
# The captured integer can also be decoded by direct positional bytes.
check(sum(b<<(8*j) for j,b in enumerate(body))==24,'independent byte integer')
for p in [Path(__file__),D/'evidence/summary.json']:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_LOCAL_PIECE_REGULARITY_AND_ACTUAL_M24_FREE_COLUMN_COUNT','pieces_checked':piece_count,'records':outrows,'raw_Mh':{'value':mh,'source':str(raw),'raw_size':st.st_size,'raw_mtime_ns':st.st_mtime_ns,'member':'Mh.npy','member_CRC32':info.CRC,'member_header_offset':info.header_offset,'copy':str(dst.relative_to(B)),'scope':'Only this tiny member pinned; no historical full matrix certificate.'},'files':pins};p=D/'evidence/extra_columns.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pieces_checked':piece_count,'Mh':mh}))

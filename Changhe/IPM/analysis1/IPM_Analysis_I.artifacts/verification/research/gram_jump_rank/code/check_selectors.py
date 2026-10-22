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
srcp=B/'research/gram_internal_jumps/sources/src__c2_gram.py';src=srcp.read_text();tree=ast.parse(src);main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main');loop=[n for n in ast.walk(main) if isinstance(n,ast.For) and ast.unparse(n.target)=='(name, sel)'];check(len(loop)==1,'selector loop');expr='[("Fminus", list(range(nF + 2))), ("Fminus_noJ", [i for i in range(nF + 2) if i not in jidx]), ("free", list(range(ntot))), ("free_noJ", [i for i in range(ntot) if i not in jidx])]';check(ast.dump(loop[0].iter)==ast.dump(ast.parse(expr,mode='eval').body),'complete selector AST');check('ntot = nF + 2 + Mh' in src and 'Mh = int(d["Mh"])' in src,'total/mode binding')
b=json.loads((D/'evidence/independent.json').read_text());pins={};outrecords=[]
for r in b['records']:
 p=B/r['source'];meta=Reader(io.BytesIO(p.read_bytes())).load();cols=meta['cols'];nf=len(cols);M=r['M'];jidx={i for i,(_,_,label) in enumerate(cols) if label=='J'};check(jidx=={0},'one actual J');selected={i for row in r['pivots'] for i in row['column_indices']};check(len(selected)==r['selected_coordinate_columns'],'selected count');sets={'Fminus':set(range(nf+2)),'Fminus_noJ':set(range(nf+2))-jidx,'free':set(range(nf+2+M)),'free_noJ':set(range(nf+2+M))-jidx}
 for name,s in sets.items():check(selected<=s and len(s)==r['section_column_counts'][name],'actual selector containment/count')
 outrecords.append({'source':r['source'],'selected':len(selected),'all_four_selectors_contain_all_selected_coordinates':True,'actual_jidx':sorted(jidx),'section_counts':r['section_column_counts']});pins[r['source']]=sha(p)
raw=B.parent/'ipmA-num/runs/c2/c2raw_M24_s8_p4.npz';st=raw.stat();headers={}
with zipfile.ZipFile(raw) as z:
 for name in ['Mat','KP','TAU','tails']:
  info=z.getinfo(name+'.npy')
  with z.open(info) as f:
   prefix=f.read(10);check(prefix[:8]==b'\x93NUMPY\x01\x00','npy version');size=struct.unpack('<H',prefix[8:])[0];check(size<4096,'small header');header=f.read(size);check(len(header)==size,'header complete');h=ast.literal_eval(header.decode().strip());check(h['descr']=='<f8' and not h['fortran_order'],'matrix f8 C order')
  headers[name]={'shape':list(h['shape']),'header_hex':(prefix+header).hex(),'zip_member_file_size':info.file_size,'zip_member_CRC32':info.CRC,'zip_member_header_offset':info.header_offset,'scope':'Header only; array values not read or hashed.'}
check(raw.stat().st_size==st.st_size and raw.stat().st_mtime_ns==st.st_mtime_ns,'raw stable');ne,nf=headers['Mat']['shape'];check(nf==b['records'][-1]['n_function_columns'] and headers['tails']['shape']==[ne,24] and headers['KP']['shape']==headers['TAU']['shape']==[ne],'raw current shape binding')
for p in [Path(__file__),srcp,D/'evidence/independent.json',D/'evidence/extra_columns.json']:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ALL_SELECTED_COORDINATES_IN_ALL_SECTIONS_AND_RAW_SHAPES','records':outrecords,'raw':{'path':str(raw),'size':st.st_size,'mtime_ns':st.st_mtime_ns,'headers':headers},'files':pins};p=D/'evidence/selectors.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'M24rows':ne,'nF':nf}))

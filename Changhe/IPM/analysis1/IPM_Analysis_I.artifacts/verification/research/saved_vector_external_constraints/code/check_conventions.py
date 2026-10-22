"""Complete source convention, stored scalar types, manual metadata and incidence audit."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import Counter
import ast,hashlib,json,pickle,io,zipfile,struct,math,os,time
import numpy as np
import sympy as sp
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/saved_vector_external_constraints'
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def utc():return datetime.now(timezone.utc).isoformat()
class Reader(pickle.Unpickler):
 def find_class(self,m,n):
  table={('numpy','ndarray'):np.ndarray,('numpy','dtype'):np.dtype}
  for prefix in ['numpy.core.multiarray','numpy._core.multiarray']:
   table[prefix,'scalar']=np._core.multiarray.scalar;table[prefix,'_reconstruct']=np._core.multiarray._reconstruct
  need((m,n) in table,'restricted pickle class');return table[m,n]
def ieee(word):
 s=-1 if word>>63 else 1;e=(word>>52)&2047;m=word&((1<<52)-1);need(e!=2047,'finite binary64 word')
 return s*F(m if e==0 else (1<<52)+m)*F(2)**(-1074 if e==0 else e-1075)
def npy(raw):
 need(raw[:6]==b'\x93NUMPY' and tuple(raw[6:8]) in [(1,0),(2,0),(3,0)],'NPY header magic/version');off=10 if raw[6]==1 else 12;n=int.from_bytes(raw[8:off],'little');text=raw[off:off+n].decode('utf8' if raw[6]==3 else 'latin1');node=ast.parse(text.strip(),mode='eval').body;need(isinstance(node,ast.Dict) and len(node.keys)==3,'literal unique header');keys=[ast.literal_eval(v) for v in node.keys];need(set(keys)=={'descr','fortran_order','shape'},'header keys');h=ast.literal_eval(node);need(type(h['fortran_order']) is bool and type(h['shape']) is tuple and all(type(v) is int and v>=0 for v in h['shape']),'header shape/order');desc=h['descr'];need(type(desc) is str and desc[0] in '<>' and desc[1] in 'fiU','fixed permitted dtype');endian='little' if desc[0]=='<' else 'big';count=math.prod(h['shape']);payload=raw[off+n:]
 if desc[1] in 'fi':
  need(desc[2:]=='8' and len(payload)==8*count,'8-byte metadata');vals=[int.from_bytes(payload[j:j+8],endian,signed=desc[1]=='i') for j in range(0,len(payload),8)]
  if desc[1]=='f':vals=[ieee(v) for v in vals]
 else:
  width=int(desc[2:]);need(width>0 and len(payload)==4*width*count,'UTF32 fixed width');vals=[payload[j:j+4*width].decode('utf-32-le' if endian=='little' else 'utf-32-be').rstrip('\x00') for j in range(0,len(payload),4*width)]
 return h,vals
def member(path,name):
 with zipfile.ZipFile(path) as z:need(z.namelist().count(name)==1,'unique NPZ member');raw=z.read(name)
 return npy(raw)
start=utc();tick=time.monotonic();m=load(D/'data_exact/manifest.json');a=load(D/'evidence/output_audit.json');c=load(D/'data_exact/constraints.json');pins=dict(a['files'])
for n,h in pins.items():need(sha(B/n)==h,'inherited digest')
need(sha(B/'research/external_constraint_rank/evidence/verdict.json')=='e569bd20c174f863d6ba47ef3e16070870f3ea10fcff6ea79d5f2c98ed433542','accepted source matrix');rank=load(B/'research/external_constraint_rank/data_exact/minors.json');source=load(B/'research/external_constraint_rank/evidence/source_audit_v2.json');need(source['status']=='PASS_STATIC_EXTERNAL_CONSTRAINT_AND_COORDINATE_SOURCE_BINDING','inherited complete source binding')
for n,h in source['files'].items():need(sha(B/n)==h,'source binding input');need(n not in pins or pins[n]==h,'source pin conflict');pins[n]=h
# Rebind complete bodies to originals, then compile only the inspected pure piece evaluator.
source_specs=[('piece_jet','notes/constraint_rank_watch/c2_gram2.py','research/external_constraint_rank/sources/snapshot_v3__piece_jet.txt',ast.FunctionDef),('ExpPolyBasis','research/gram_internal_jumps/sources/src__lin_assembly.py','research/external_constraint_rank/sources/ExpPolyBasis.txt',ast.ClassDef)]
source_records=[];jet=None
for name,original,extracted,kind in source_specs:
 text=(B/original).read_text();tree=ast.parse(text);nodes=[v for v in ast.walk(tree) if isinstance(v,kind) and v.name==name];need(len(nodes)==1,'unique complete evaluator');v=nodes[0];small=(B/extracted).read_text();need(ast.get_source_segment(text,v)+'\n'==small and ast.dump(v,include_attributes=False)==ast.dump(ast.parse(small).body[0],include_attributes=False),'complete evaluator AST equality');source_records.append({'name':name,'source':original,'extract':extracted,'sha256':sha(B/extracted)})
 if name=='piece_jet':
  namespace={'np':np};exec(compile(ast.Module(body=[v],type_ignores=[]),'<frozen pure piece_jet>','exec'),namespace);jet=namespace[name]
need(jet is not None,'pure endpoint evaluator')
x,alpha=sp.symbols('x alpha');coeff=sp.symbols('c0:8');symbolic=0
for degree in range(8):
 P=sum(coeff[k]*x**k for k in range(degree+1));source_transform=sum((alpha*coeff[k]+((k+1)*coeff[k+1] if k<degree else 0))*x**k for k in range(degree+1));need(sp.expand(source_transform-alpha*P-sp.diff(P,x))==0,'symbolic coefficient derivative')
 horner=sp.Integer(0)
 for k in range(degree,-1,-1):horner=horner*x+coeff[k]
 need(sp.expand(horner-P)==0,'symbolic ascending Horner');symbolic+=2
rawjoins=[]
for key in ['tmin','t0']:
 p=B/f'research/gram_internal_jumps/sources/c2raw_M24_s8_p4__{key}.npy';h,v=npy(p.read_bytes());need(h['shape']==() and h['descr']=='<f8' and len(v)==1,'raw join scalar');rawjoins.append(v[0]);pins[str(p.relative_to(B))]=sha(p)
checks={'guarded_piece_scalars':0,'manual_metadata_scalars':0,'manual_column_labels':0,'manual_column_modes':0,'endpoint_contributions':0,'exact_trace_rechecks':0,'source_float_trace_comparisons':0,'symbolic_identities':symbolic};types=Counter();breakdown=Counter();familyrows=[];largest_error=F(0)
def rat(v,endpoint=False):
 need(type(v) in [float,np.float64],'stored scalar is binary64 type');types[type(v).__module__+'.'+type(v).__name__]+=1;checks['guarded_piece_scalars']+=1;vv=float(v);need(not math.isnan(vv) and (endpoint or math.isfinite(vv)),'finite scalar or infinity sentinel');return vv if math.isinf(vv) else F.from_float(vv)
for fam,record,rr in zip(m['families'],c['records'],rank['records'],strict=True):
 M,nf=fam['M'],fam['nF'];need(rr['M']==M and record['M']==M,'family order');p=B/fam['vector_path'];cols=Reader(io.BytesIO((B/fam['cols_path']).read_bytes())).load()['cols'];need(len(cols)==nf,'full column count');scalars={}
 for key in ['tmin','t0','Mh','nF','NJ','ROWS','ntot','next','script_sha256']:
  h,v=member(p,key+'.npy');need(h['shape']==() and len(v)==1,'scalar metadata shape');expected_type='f' if key in ['tmin','t0'] else 'U' if key in ['ROWS','script_sha256'] else 'i';need(h['descr'][1]==expected_type,'metadata dtype');scalars[key]=v[0];checks['manual_metadata_scalars']+=1
 joins=[scalars['tmin'],scalars['t0']];need(joins==rawjoins==list(map(F,rr['joins_exact']))==list(map(F,record['joins_exact']))==[F.from_float(float.fromhex(v)) for v in fam['joins_hex']],'four-way exact join binding');need([scalars[k] for k in ['Mh','nF','NJ','ROWS','ntot','next']]==[M,nf,1,'H1q',nf+2+M,nf+2+M+4],'manual integer/string family');need(scalars['script_sha256']==fam['script_sha256_claim']==sha(B/'notes/constraint_rank_watch/c2_gram2.py'),'manual claimed source hash')
 h,labels=member(p,'col_label.npy');need(h['shape']==(nf,) and h['descr'][1]=='U' and labels==[v[2] for v in cols],'manual complete label array');checks['manual_column_labels']+=nf
 h,modes=member(p,'col_m.npy');need(h['shape']==(nf,) and h['descr'][1:]=='i8' and modes==[v[0] for v in cols],'manual complete mode array');checks['manual_column_modes']+=nf
 localcount=0;localbreak=Counter();localerror=F(0)
 for i,((mode,pcs,label),saved) in enumerate(zip(cols,record['columns'],strict=True)):
  traces=[F(0)]*4
  for aa,bb,al,cc in pcs:
   aa=rat(aa,True);bb=rat(bb,True);al=rat(al);cc=[rat(v) for v in cc];need(0<len(cc)<=8 and aa<bb,'valid polynomial/support')
   for j,t in enumerate(joins):
    if aa==t:sign=-1;xx=F(0)
    elif bb==t:sign=1;xx=F(0) if aa==-math.inf else t-aa
    else:continue
    need(al*xx==0,'endpoint exponent zero');value=sum((v*xx**k for k,v in enumerate(cc)),F(0));derivative=al*value+sum((k*cc[k]*xx**(k-1) for k in range(1,len(cc))),F(0));traces[2*j]+=sign*value;traces[2*j+1]+=sign*derivative;localcount+=1
    category=f'degree={len(cc)-1};x={"zero" if xx==0 else "nonzero"};alpha={"zero" if al==0 else "nonzero"}';localbreak[category]+=1
  need(traces==list(map(F,saved['traces_exact'])),'complete exact convention trace agreement');checks['exact_trace_rechecks']+=4
  for j,t in enumerate(joins):
   for nu in [0,1]:
    # Source-only floating endpoint diagnostic on the already pinned exact columns.
    vf=jet(pcs,float(t),'-',nu)-jet(pcs,float(t),'+',nu);need(math.isfinite(vf),'finite source float trace');error=abs(F.from_float(vf)-traces[2*j+nu]);localerror=max(localerror,error);checks['source_float_trace_comparisons']+=1
 need(localcount==sum(localbreak.values()),'complete incidence accounting');breakdown.update(localbreak);checks['endpoint_contributions']+=localcount;largest_error=max(largest_error,localerror);familyrows.append({'M':M,'endpoint_contributions':localcount,'breakdown':dict(localbreak),'max_source_float_trace_error_exact':str(localerror),'manual_joins_exact':list(map(str,joins))})
need(checks['endpoint_contributions']==1286==c['counts']['endpoint_contributions'],'independent full incidence count');need(checks['exact_trace_rechecks']==checks['source_float_trace_comparisons']==28840 and checks['manual_column_labels']==checks['manual_column_modes']==7210 and checks['manual_metadata_scalars']==18,'full supplemental coverage')
for pp in [Path(__file__),D/'CONVENTION_AND_METADATA_PROOF.md',D/'evidence/output_audit.json',B/'research/external_constraint_rank/evidence/source_audit_v2.json']:
 pins[str(pp.relative_to(B))]=sha(pp)
for n,h in pins.items():need(sha(B/n)==h,'final input digest')
out={'start_utc':start,'utc':utc(),'status':'PASS_COMPLETE_CONVENTION_TYPES_MANUAL_METADATA_AND_INCIDENCE_AUDIT','counts':checks,'scalar_types':dict(types),'families':familyrows,'incidence_breakdown':dict(breakdown),'max_source_float_trace_error_exact':str(largest_error),'source_bodies':source_records,'files':dict(sorted(pins.items())),'seconds':time.monotonic()-tick,'scope':'Complete explicit ascending-coefficient and shifted-t convention proof, all stored piece scalar types guarded, independently decoded metadata and joins, all28840 exact trace rechecks and1286 incidence recount. Pure frozen piece_jet execution is a finite floating diagnostic only. No external execution attestation, physical omitted-component traces, ideal SVD or PDE result.'}
with (D/'evidence/convention_audit.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({k:v for k,v in out.items() if k not in ['files','source_bodies']}))

"""Manual IEEE754/NPY decoding and direct monomial trace sums; fresh iv220 boxes."""
from pathlib import Path
from fractions import Fraction as R
from datetime import datetime,timezone
import json,hashlib,pickle,io,sys,os,time,math,struct,zipfile,ast
import numpy as np
from mpmath import iv
assert not sys.flags.optimize
iv.dps=220
B=Path(__file__).resolve().parents[3];D=B/'research/saved_vector_external_constraints'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def need(v,s):
 if not v:raise ValueError(s)
class Unpickler(pickle.Unpickler):
 def find_class(self,module,name):
  table={('numpy','ndarray'):np.ndarray,('numpy','dtype'):np.dtype}
  for module_ in ('numpy.core.multiarray','numpy._core.multiarray'):
   table[module_,'_reconstruct']=np._core.multiarray._reconstruct;table[module_,'scalar']=np._core.multiarray.scalar
  need((module,name) in table,'restricted pickle class');return table[module,name]
def ieee(bits):
 sign=-1 if bits>>63 else 1;ex=(bits>>52)&2047;mant=bits&((1<<52)-1);need(ex!=2047,'nonfinite binary64')
 return sign*R(mant if ex==0 else (1<<52)+mant)*R(2)**(-1074 if ex==0 else ex-1075)
def rat(x):return ieee(int.from_bytes(struct.pack('>d',float(x)),'big'))
def endpoint(x):
 v=float(x);need(not math.isnan(v),'nan endpoint');return v if math.isinf(v) else rat(v)
def npy(p,name):
 with zipfile.ZipFile(p) as z:
  need(z.namelist().count(name)==1,'unique zip member');raw=z.read(name)
 need(raw[:6]==b'\x93NUMPY' and tuple(raw[6:8]) in [(1,0),(2,0),(3,0)],'NPY magic version');wide=raw[6]!=1;off=12 if wide else 10;ln=int.from_bytes(raw[8:off],'little');hdr=ast.literal_eval(raw[off:off+ln].decode('utf-8' if raw[6]==3 else 'latin1'));need(set(hdr)=={'descr','fortran_order','shape'} and type(hdr['fortran_order']) is bool and type(hdr['shape']) is tuple and all(type(x) is int and x>=0 for x in hdr['shape']),'NPY literal header');need(hdr['descr'] in ['<f8','>f8','<i8','>i8'],'fixed 8-byte dtype');payload=raw[off+ln:];need(len(payload)==math.prod(hdr['shape'])*8,'exact payload length');order='little' if hdr['descr'][0]=='<' else 'big';ints=[int.from_bytes(payload[j:j+8],order,signed=hdr['descr'][1]=='i') for j in range(0,len(payload),8)];vals=[ieee(v) for v in ints] if hdr['descr'][1]=='f' else ints;return hdr,vals
def ivends(x):
 result=[]
 for s,m,e,bc in x._mpi_:need(bc>=0,'finite interval endpoint');result.append((-1 if s else 1)*R(int(m))*R(2)**int(e))
 return result
start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();producer=json.loads((D/'data_exact/constraints.json').read_text());man=json.loads((D/'data_exact/manifest.json').read_text());need(producer['status']=='COMPUTED_EXACT_SAVED_VECTOR_EXTERNAL_CONSTRAINTS_REQUIRES_INDEPENDENT_CHECK','producer status');pins=dict(producer['files'])
for n,h in pins.items():need(sha(B/n)==h,'primary input binding')
checks={'column_traces':0,'function_coefficients':0,'functionals':0,'iv220_magnitude_checks':0,'decimal_checks':0,'nonzero_functionals':0,'manual_vector_entries':0};summaries=[]
need(len(producer['records'])==len(man['families'])==2,'both preselected families')
for record,fam in zip(producer['records'],man['families'],strict=True):
 M,nf=fam['M'],fam['nF'];need((record['M'],record['nF'],record['vector_path'],record['cols_path'])==(M,nf,fam['vector_path'],fam['cols_path']),'family identity');joins=[rat(float.fromhex(v)) for v in fam['joins_hex']];need(record['joins_exact']==list(map(str,joins)),'join identity')
 hdr,vv=npy(B/fam['vector_path'],'Fminus_h.npy');need(hdr['descr'][1:]=='f8' and hdr['shape']==(fam['n_extended'],5),'complete vector dtype/shape');nr=hdr['shape'][0];H=[[vv[i+nr*v if hdr['fortran_order'] else 5*i+v] for v in range(5)] for i in range(nr)];checks['manual_vector_entries']+=len(vv);need(all(v==0 for r in H[nf+2:] for v in r),'source extra coefficients zero');hm,mm=npy(B/fam['vector_path'],'col_m.npy');need(hm['shape']==(nf,) and hm['descr'][1:]=='i8','mode array shape/type');cols=Unpickler(io.BytesIO((B/fam['cols_path']).read_bytes())).load()['cols'];need(len(cols)==len(record['columns'])==nf,'full column coverage');acc={(v,m,j,nu):R(0) for v in range(5) for m in range(M) for j in range(2) for nu in range(2)}
 for i,((mode,pcs,label),saved) in enumerate(zip(cols,record['columns'],strict=True)):
  need(type(mm[i]) is int and mm[i]==int(mode)==mode and 0<=mm[i]<M,'exact mode identity');mode=mm[i];need((saved['column'],saved['mode'],saved['label'])==(i,mode,label),'saved column identity');need(len(saved['h_exact'])==5 and [R(v) for v in saved['h_exact']]==H[i],'manual coefficients equal saved exact export');checks['function_coefficients']+=5
  pieces=[(endpoint(a),endpoint(b),rat(alpha),[rat(v) for v in c]) for a,b,alpha,c in pcs];need(all(a<b and a!=math.inf and b!=-math.inf and not(a==-math.inf and b==math.inf) and len(c)>0 for a,b,al,c in pieces),'valid complete pieces')
  for i1,p in enumerate(pieces):
   for q in pieces[i1+1:]:need(p[1]<=q[0] or q[1]<=p[0],'pairwise disjoint interiors')
  traces=[]
  for j,join in enumerate(joins):
   need(sum(b==join for a,b,al,c in pieces)<=1 and sum(a==join for a,b,al,c in pieces)<=1,'unique left/right trace')
   for nu in range(2):
    value=R(0)
    for a,b,al,c in pieces:
     if b==join:sign=1
     elif a==join:sign=-1
     else:continue
     x=join-b if a==-math.inf else join-a;need(al*x==0,'zero exponential argument')
     if nu==0:term=sum((coef*x**k for k,coef in enumerate(c)),R(0))
     else:term=sum((al*coef*x**k for k,coef in enumerate(c)),R(0))+sum((k*c[k]*x**(k-1) for k in range(1,len(c))),R(0))
     value+=sign*term
    traces.append(value)
    for v in range(5):acc[v,mode,j,nu]+=H[i][v]*value
  need(len(saved['traces_exact'])==4 and list(map(R,saved['traces_exact']))==traces,'independent monomial trace');checks['column_traces']+=4
 need(len(record['vectors'])==5,'all five saved vectors');sums=[]
 for v,vec in enumerate(record['vectors']):
  need(vec['vector']==v and len(vec['constraints'])==4*M,'complete vector rows');maximum=R(0);nonzero=0
  for index,q in enumerate(vec['constraints']):
   mode=index//4;join=(index%4)//2;nu=index%2;need((q['mode'],q['join_index'],q['order'])==(mode,join,nu),'ordered exact matrix rows');value=acc[v,mode,join,nu];need(value==R(q['value_exact']),'independent source-functional sum');checks['functionals']+=1;nonzero+=value!=0;absolute=abs(value);maximum=max(maximum,absolute);fresh=ivends(iv.mpf(absolute.numerator)/absolute.denominator);lo,hi=map(R,q['abs_arb512_exact']);need(lo<=fresh[0]<=absolute<=fresh[1]<=hi,'fresh interval in Arb output');checks['iv220_magnitude_checks']+=1;dl,du=R(q['abs_decimal']['lower_exact']),R(q['abs_decimal']['upper_exact']);need(dl<=absolute<du and du-dl==R(1,10**30) and dl*10**30==absolute.numerator*10**30//absolute.denominator,'strict magnitude decimal');checks['decimal_checks']+=1
  need(nonzero==vec['nonzero'] and maximum==R(vec['max_abs_exact']),'complete vector summary');dl,du=map(R,[vec['max_abs_decimal']['lower_exact'],vec['max_abs_decimal']['upper_exact']]);need(dl<=maximum<du and du-dl==R(1,10**30),'max decimal');checks['nonzero_functionals']+=nonzero;sums.append({'vector':v,'nonzero':nonzero,'max_abs_exact':str(maximum),'max_abs_decimal':vec['max_abs_decimal']})
 summaries.append({'M':M,'vectors':sums})
need(checks['column_traces']==4*(1953+5257) and checks['function_coefficients']==5*(1953+5257) and checks['functionals']==checks['iv220_magnitude_checks']==checks['decimal_checks']==5*4*(16+24),'complete independent counts');need(checks['nonzero_functionals']==producer['counts']['nonzero_functionals'],'same nonzero count')
for p in [D/'data_exact/constraints.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():need(sha(B/n)==h,'final digest')
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_SAVED_VECTOR_EXTERNAL_CONSTRAINTS_INDEPENDENT_IEEE_MONOMIAL_AND_IV220','counts':checks,'summaries':summaries,'seconds':time.monotonic()-tick,'files':dict(sorted(pins.items())),'scope':'Two algorithms share frozen column pickle inputs and source-defined functional. Vector import is independent manual NPY/IEEE decoding. No source execution attestation, ideal exact SVD, physical-component cancellation, global membership or PDE endpoint.'}
with (D/'evidence/output_audit.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'counts':checks,'seconds':out['seconds']}))

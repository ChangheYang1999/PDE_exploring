"""Independent original-NPY reads and exact margin/provenance audit."""
import sys,os
sys.dont_write_bytecode=True
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import ast,json,hashlib,zipfile,platform,math
from datetime import datetime,timezone
import flint,mpmath
from flint import fmpq as Q
B=Path(__file__).resolve().parents[3];D=B/'research/radial_first_failure'
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def exactbits(bits):
 sig=bits>>63;e=(bits>>52)&2047;m=bits&((1<<52)-1);need(e!=2047,'finite original')
 if e:m+=1<<52
 exp=-1074 if e==0 else e-1075
 return (-1 if sig else 1)*Q(m)*Q(2)**exp
def member(path,name,index,shape):
 with zipfile.ZipFile(path) as z:
  with z.open(name+'.npy') as f:
   hdr=f.read(8);need(hdr[:6]==b'\x93NUMPY','NPY');v=hdr[6:8];need(v in [b'\x01\x00',b'\x02\x00'],'version');length=int.from_bytes(f.read(2 if v==b'\x01\x00' else 4),'little');h=ast.literal_eval(f.read(length).decode('latin1'));need(h['descr']=='<f8' and h['fortran_order'] is False and h['shape']==shape,'shape and dtype');need(0<=index<math.prod(shape),'index')
   remain=8*index
   while remain:
    chunk=f.read(min(remain,1<<20));need(chunk,'not truncated');remain-=len(chunk)
   b=f.read(8);need(len(b)==8,'element');return exactbits(int.from_bytes(b,'little')),b.hex()
first=json.loads((D/'evidence/check.json').read_text());j=json.loads((D/'data_exact/coefficient.json').read_text());q={k:Q(v['exact']) for k,v in j.items()}
for k,v in j.items():need(q[k]==exactbits(int.from_bytes(bytes.fromhex(v['bytes_le']),'little')),'independent JSON bytes')
green=B.parent/'ipmA-num/data/cert_green.npz';scalar=B/'research/flow_scalars/evidence/scalar_arrays.npz';checks=[]
for key,name in [('am','A_mid'),('ar','A_rad'),('bm','B_mid'),('br','B_rad')]:
 val,b=member(green,name,2955*261+134,(7810,261));need(val==q[key] and b==j[key]['bytes_le'],'original '+key);checks.append(key)
for key,col in [('em',1),('er',2)]:
 val,b=member(scalar,'middle',2955*36+col,(7809,36));need(val==q[key] and b==j[key]['bytes_le'],'original '+key);checks.append(key)
e0=q['em']-q['er'];e1=q['em']+q['er'];a0=q['am']-q['ar'];a1=q['am']+q['ar'];b0=q['bm']-q['br'];b1=q['bm']+q['br'];need(e0>0 and b0-a1>0,'positive family');lo=(b0-a1)/(2*e1*e1);hi=(b1-a0)/(2*e0*e0);cl=q['cm']-q['cr'];ch=q['cm']+q['cr'];need(cl<lo<hi<ch,'strict exact containment')
for key,value in [('exact_lower',lo),('exact_upper',hi),('candidate_lower',cl),('candidate_upper',ch),('lower_margin',lo-cl),('upper_margin',ch-hi)]:need(Q(first[key])==value,'exact saved '+key)
need(min(lo-cl,ch-hi)/q['cr']>Q(1,100000),'margin greater than1e-5 radius')
failpath=B/'research/radial_tm_full/evidence/full_failure.json';fail=json.loads(failpath.read_text());w=fail['failed_cell']['failures'][0];need((w['engine'],w['family'],w['n'],w['j'])==('arb512','R',135,0) and fail['failed_cell']['cell']==2955,'failure indexing');need(w['independent_lo']==first['arb_endpoints'][0] and w['independent_hi']==first['arb_endpoints'][1],'same exact failed endpoints')
for name,entry in first['pins'].items():need(sha(entry['path'])==entry['sha256'],'unchanged original '+name)
pins={str(failpath.relative_to(B)):sha(failpath)}
for name in ['PROOF.md','RESULTS.md','PROVENANCE.md','code/check.py','code/audit.py','data_exact/coefficient.json','evidence/check.json']:
 p=D/name;pins[str(p.relative_to(B))]=sha(p)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ORIGINAL_INPUTS_AND_EXACT_MARGINS','original_input_elements':checks,'strict_exact_containment':True,'relative_margin_lower_bound':'1/100000','original_pin_count':len(first['pins']),'pins':pins,'runtime':{'python':sys.version,'python_flint':flint.__version__,'mpmath':mpmath.__version__,'platform':platform.platform()},'scope':'One finite box coefficient only; shared regenerated candidate; no independent full producer or radial coverage.'}
with (D/'evidence/audit.json').open('x') as f:json.dump(result,f,indent=1);f.write('\n')
print(json.dumps(result,indent=2))

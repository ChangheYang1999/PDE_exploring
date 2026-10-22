"""Fresh NPY byte parser, exact complex homogeneous monomials, Arb1536 via r^-10."""
import os
for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
import sys,json,hashlib,zipfile,ast,struct,math,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,fmpq,ctx
assert not sys.flags.optimize
ctx.prec=1536;ctx.threads=1
B=Path(__file__).resolve().parents[3];D=B/'research/n7_center';E=D/'evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def parse_member(z,name):
 raw=z.read(name+'.npy');assert raw[:6]==b'\x93NUMPY';major,minor=raw[6:8]
 if major==1:hl=struct.unpack('<H',raw[8:10])[0];off=10
 elif major in (2,3):hl=struct.unpack('<I',raw[8:12])[0];off=12
 else:raise AssertionError((name,major,minor))
 head=ast.literal_eval(raw[off:off+hl].decode('latin1'));assert head['descr']=='<f8',head
 payload=raw[off+hl:];shape=head['shape'];N=math.prod(shape);assert len(payload)==8*N
 out=[]
 for (bits,) in struct.iter_unpack('<Q',payload):
  sign=-1 if bits>>63 else 1;ex=(bits>>52)&2047;fr=bits&((1<<52)-1);assert ex!=2047
  mant=fr if ex==0 else fr+(1<<52);pw=-1074 if ex==0 else ex-1075
  out.append(sign*F(mant)*F(2)**pw)
 if head['fortran_order'] and len(shape)>1:
  import itertools
  strides=[];stride=1
  for dim in shape:strides.append(stride);stride*=dim
  out=[out[sum(i*st for i,st in zip(index,strides))] for index in itertools.product(*(range(dim) for dim in shape))]
 return shape,out

def ep(v):m,e=v.man_exp();return F(int(m))*F(2)**int(e)
def aq(v):v=F(v);return arb(fmpq(v.numerator,v.denominator))
def main():
 start=time.monotonic();inputs=json.loads((E/'exact_inputs.json').read_text());c=json.loads((E/'checks.json').read_text());sourcecounts=0;files={}
 for p,h in c['files'].items():assert sha(B/p)==h;files[p]=h
 for p,h in inputs['source_files'].items():assert sha(p)==h
 read={}
 for tag,item in inputs['data'].items():
  p=Path(item['path'])
  with p.open('rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==item['sha256']
  with zipfile.ZipFile(p) as z:
   shape,vals=parse_member(z,'D');assert shape==tuple(item['D_shape']);expected=[F(v) for row in item['D'] for v in row];assert vals==expected;sourcecounts+=len(vals)
   read[tag]=[vals[j:j+7] for j in range(0,len(vals),7)]
   for field,key in [('bi','bi'),('k','k'),('knots','tmin'),('rmin','stored_rmin')]:
    shape,vals=parse_member(z,field);assert vals[0]==F(item[key]);sourcecounts+=1
 n=inputs['data']['n7'];new,old=read['n7'],read['original'];zero=0;complement=0
 for j in range(7):
  for m in range(260):
   if j<4 and m>=j+2:assert new[m][j]==0 and old[m][j]!=0;zero+=1
   else:assert new[m][j]==old[m][j];complement+=1
 assert zero==1026 and complement==794
 # Laurent complex monomials: represent 2i H/r^13 by frequencies with signed real coefficients.
 coeff={}
 def add(dic,n,v):dic[n]=dic.get(n,F(0))+v
 for m in range(260):
  v=new[m][4]/8
  for a in [1,3]:
   for freq in [a+2*m,a-2*m]:add(coeff,freq,v);add(coeff,-freq,-v)
 coeff={n:v for n,v in coeff.items() if v};L=max(coeff);assert L==521 and coeff[L]==new[259][4]/8
 k=F(n['k']);lx=1-2/k;ly=4/k-1;result={}
 for freq,v in coeff.items():
  a=F(13+freq,2);b=F(13-freq,2);assert a.denominator==b.denominator==1
  add(result,freq,((lx+ly)*F(13,2)-1)*v)
  add(result,freq-2,(lx-ly)*a*v/2);add(result,freq+2,(lx-ly)*b*v/2)
 assert max(q for q,v in result.items() if v)==523
 pref=result[523];assert pref==F(c['exact']['residual_prefactor']) and pref>0
 r=aq(n['tmin']).exp();scale=1/r**10
 vals={'rminus':r,'rminus_inverse10':scale,'factor_top':aq(new[259][4])*scale,'density_top':aq(coeff[L])*scale,'residual_top':aq(pref)*scale,'max_scaled_D5':aq(max(abs(row[4]) for row in new[6:]))};contains=0
 for name,v in vals.items():
  rec=c['bounds'][name];assert F(rec['lower_exact'])<=ep(v.lower())<=ep(v.upper())<=F(rec['upper_exact']),name;contains+=1
 assert ep(vals['residual_top'].lower())>1 and F(c['exact']['homogeneity_margin'])==13-(F(129,20)+F(307,100)-1)
 files[str(Path(__file__).relative_to(B))]=sha(__file__);files[str((E/'checks.json').relative_to(B))]=sha(E/'checks.json')
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_NPY_LAURENT_AUDIT','counts':{'exact_binary64_values_compared':sourcecounts,'full_npz_hashes':2,'mask_zeros':zero,'unchanged_complement':complement,'density_Laurent_frequencies':len(coeff),'residual_Laurent_frequencies':sum(bool(v) for v in result.values()),'full_ball_contains':contains},'method':'Manual zip/NPY header and raw binary64 bit-to-rational parsing, no numpy. Exact z,zbar homogeneous differentiation produces highest residual coefficient. Independent Arb1536 using reciprocal tenth power of exp(tmin), not exp(-10tmin).','files':files,'seconds':time.monotonic()-start}
 (E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='files'},indent=2))
if __name__=='__main__':main()

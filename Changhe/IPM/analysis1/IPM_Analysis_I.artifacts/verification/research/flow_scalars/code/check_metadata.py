"""Supplementary source geometry and metadata obligations from model review."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import json,sys,zipfile,ast,struct,math,hashlib,time
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from flint import arb,fmpq,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/flow_scalars/evidence';ctx.prec=1536;ctx.threads=1
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def qa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def fr(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def header(path,key):
 with zipfile.ZipFile(path) as z:
  with z.open(key+'.npy') as f:
   magic=f.read(8);assert magic[:6]==b'\x93NUMPY' and magic[-2:] in (b'\x01\x00',b'\x02\x00',b'\x03\x00')
   fmt='<H' if magic[-2:]==b'\x01\x00' else '<I';n=struct.unpack(fmt,f.read(struct.calcsize(fmt)))[0]
   d=ast.literal_eval(f.read(n).decode());assert d['descr']=='<f8' and not d['fortran_order'];return list(d['shape'])
def main():
 start=time.monotonic();arrays=np.load(E/'scalar_arrays.npz');trial=B.parent/'ipmA-num/data/trial_v2_h0.008.npz';tr=np.load(trial);kn=tr['knots'];extra={};checks=0;maxx=0
 first=json.loads((E/'checks.json').read_text());assert sha(E/'scalar_arrays.npz')==first['array_sha256']
 for reg,nc in [('middle',7809),('outer',8948),('inner',2632)]:
  p=B.parent/'ipmA-num/data'/('cert_green.npz' if reg=='middle' else 'cert_'+reg+'_green.npz');d=np.load(p);a=arrays[reg]
  assert sha(p)==first['files'][str(p)]
  shapes={key:header(p,key) for key in ('A_mid','A_rad','B_mid','B_rad')};assert all(v==[nc+1,261] for v in shapes.values())
  hsub=float(d['hsub']);assert F(hsub)==F(0.0019)
  base=F(0)
  if reg=='middle':tm,rr=d['tb'],d['tb_rad'];assert F(float(tm[0]))==F(float(kn[0])) and F(float(tm[-1]))==F(float(kn[-1]))
  else:
   base=F(float(d['t0' if reg=='outer' else 'tmin']));br=F(float(d['t0_rad' if reg=='outer' else 'tmin_rad']));assert br==0 and base==F(float(kn[-1] if reg=='outer' else kn[0]))
   tm,rr=d['tau'],d['tau_rad'];extent=17.0 if reg=='outer' else 5.0;assert int(np.ceil(extent/hsub))==nc
   assert F(float(tm[0]))==(0 if reg=='outer' else -5) and F(float(tm[-1]))==(17 if reg=='outer' else 0)
  for i,row in enumerate(a):
   h,em,er,_,_,rl,rh,_,_=map(lambda x:F(float(x)),row[:9]);assert rl<=em-er;checks+=1
   lo=base+F(float(tm[i]))-F(float(rr[i]));hi=base+F(float(tm[i+1]))+F(float(rr[i+1]))
   assert rl<=fr(qa(lo).exp().lower()) and fr(qa(hi).exp().upper())<=rh;checks+=2
   x=np.nextafter(522.*row[0],np.inf);assert F(float(x))<=1 and F(float(x))>=522*h;maxx=max(maxx,float(x));checks+=2
  extra[reg]={'npz_sha256':sha(p),'shapes':shapes,'hsub_exact':str(F(hsub)),'count':nc,'base_exact':str(base)}
  d.close()
 assert checks==96945
 for p,h in first['files'].items():assert sha(p)==h,p
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_METADATA_AND_FULL_EXPORTED_ENDPOINTS','checks':checks,'regions':extra,'max_rounded_ode_x_exact':str(F(maxx)),'max_rounded_ode_x_display':maxx,'source_formula':'succ(522.0*h)','self_sha256':sha(__file__),'addendum_sha256':sha(B/'research/flow_scalars/ADDENDUM.md'),'arrays_sha256':sha(E/'scalar_arrays.npz'),'seconds':time.monotonic()-start}
 (E/'metadata_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()

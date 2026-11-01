"""Extend the independent Cartesian tuned-series audit beyond the frozen order150 base."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from functools import lru_cache
import gzip,json,pickle,sys,time
sys.dont_write_bytecode=True
from gmpy2 import mpq as Q
from flint import arb,arb_poly,fmpq,ctx
from stream_precision_audit import unpack
ctx.prec=1536;zero=arb(0);start=time.monotonic()
root=Path('research/141_tuned_completed_prefix');out=root/'verification';out.mkdir(exist_ok=True)
text=lambda x:x.str(40,radius=True)
def put(name,obj):
 p=out/name;q=p.with_name(p.name+'.new');q.write_text(json.dumps(obj,indent=2)+'\n');q.replace(p)
@lru_cache(None)
def rb(q):return arb(fmpq(str(q)))
class L:
 def __init__(self,lo=0,coeff=None):self.lo=lo;self.p=arb_poly([] if coeff is None else coeff)
 def scale(self,c):return L(self.lo,self.p*c)
 def __add__(self,o):
  lo=min(self.lo,o.lo)
  return L(lo,arb_poly([zero]*(self.lo-lo)+self.p.coeffs())+arb_poly([zero]*(o.lo-lo)+o.p.coeffs()))
 def __sub__(self,o):return self+o.scale(-1)
 def __mul__(self,o):return L(self.lo+o.lo,self.p*o.p)
 def diff(self,q,Y=False):
  c=self.p.coeffs();r=[zero]*(len(c)+2)
  for j,v in enumerate(c):
   m=self.lo+j;r[j]+=v*rb((q+m)/2);r[j+2]+=v*rb((q-m)/2)*(-1 if Y else 1)
  return L(self.lo-1,r)
def p(n):return Q(1)-Q(2*n,3)
def field(coeff,odd):
 degree=2*(len(coeff)-1)+(1 if odd else 0);v=[zero]*(2*degree+1)
 for j,x in enumerate(coeff):
  m=2*j+(1 if odd else 0)
  if not m:assert x.is_zero();continue
  v[degree+m]=x/2;v[degree-m]=-x/2
 return L(-degree,v)
try:
 src=Path('../a4-num/ckpt/tuned_b1_p1024.pkl');raw=src.read_bytes();srcsha=sha256(raw).hexdigest();srcbytes=len(raw);state=pickle.loads(raw);del raw
 Nsrc=max(state['f']);assert Nsrc%3==0 and state['ring']=='arb' and state['prec']==1024
 N=Nsrc-1
 hpath=Path('../a4-num/ckpt/tuned_b1_p1024_H.json');hraw=hpath.read_bytes();hdata=json.loads(hraw)
 assert str(Nsrc) not in hdata['H'] and all(str(n) in hdata['H'] for n in range(6,N+1,3))
 base=Path('research/128_tuned_finite_audit/verification/20261031T101608Z/selected_checkpoint.pkl.gz');bpacked=gzip.decompress(base.read_bytes());bs=pickle.loads(bpacked)
 assert max(bs['f'])==150
 for key in ['f','g']:
  for n in range(1,151):assert state[key][n]==bs[key][n],('base_mismatch',key,n)
 extension={k:v for k,v in state.items() if k not in ['f','g','stats']};extension['N']=N
 for key in ['f','g','stats']:extension[key]={n:v for n,v in state[key].items() if 151<=n<=N}
 selected=dict(extension)
 for key in ['f','g','stats']:selected[key]={**{n:v for n,v in bs[key].items() if n<=150},**extension[key]}
 assert all(selected[key][n]==state[key][n] for key in ['f','g'] for n in range(1,N+1))
 packed=pickle.dumps(extension,protocol=4);compressed=gzip.compress(packed,compresslevel=6,mtime=0)
 allocated=sum(p.stat().st_blocks*512 for p in Path('.').rglob('*') if p.is_file())
 assert allocated+len(compressed)<2995000000,('storage_budget',allocated,len(compressed))
 (out/'extension_checkpoint.pkl.gz').write_bytes(compressed)
 selection=dict(source_path=str(src),source_sha256=srcsha,source_bytes=srcbytes,source_maximum_order=Nsrc,selected_maximum_order=N,base_archive=str(base),base_uncompressed_sha256=sha256(bpacked).hexdigest(),base_maximum_order=150,extension_archive='extension_checkpoint.pkl.gz',extension_uncompressed_sha256=sha256(packed).hexdigest(),extension_uncompressed_bytes=len(packed),extension_compressed_sha256=sha256(compressed).hexdigest(),extension_compressed_bytes=len(compressed),selected_uncompressed_sha256=sha256(pickle.dumps(selected,protocol=4)).hexdigest(),selection_rule='completed prefix through source maximum minus1; every lower resonant H is present; base plus extension combines f,g,stats dictionaries')
 put('reconstruction.json',selection);del packed,compressed,bpacked,bs,selected,extension
 for name in ['tuned_c3.py','ffcore.py']:
  new=Path('../a4-num/code',name).read_bytes();old=base.parent/(name+'.source.txt');assert new==old.read_bytes(),('source_changed',name);(root/'sources'/name).write_bytes(new)
 (root/'sources/tuned_harmonics.json').write_bytes(hraw)
 f={n:[arb(*unpack(v)) for v in state['f'][n]] for n in range(1,N+1)};g={n:[arb(*unpack(v)) for v in state['g'][n]] for n in range(1,N+1)};del state
 b=f[1][1];assert f[1][0]==1
 exactroot=json.loads(Path('research/119_tuned_rational_series/verification/algebraic_numeric_values.json').read_text())['rows'][0]['root_interval'];lo,hi=map(Q,exactroot)
 P=[10532171936,-243275209320,2783057141280,-20675598499400,96180432855375,-222533688701250,176703765525000]
 def peval(x):
  v=Q(0)
  for c in reversed(P):v=v*x+c
  return v
 fl=peval(lo)
 for _ in range(1600):
  mid=(lo+hi)/2;fm=peval(mid)
  if fl*fm<0:hi=mid
  else:lo=mid;fl=fm
 assert b.contains(rb(lo).union(rb(hi)))
 F={n:field(f[n],True) for n in f};G={n:field(g[n],False) for n in g}
 FX={n:F[n].diff(p(n)) for n in F};FY={n:F[n].diff(p(n),True) for n in F}
 GX={n:G[n].diff(p(n)+1) for n in G};GY={n:G[n].diff(p(n)+1,True) for n in G}
 counts=dict(bit_identical_lower_coefficients=sum(len(f[n])+len(g[n]) for n in range(1,151)),new_poisson_coefficients=0,new_nonlinear_coefficients=0,new_ordered_pairs=0,new_compatibility_projections=0,individual_coefficients_tested=0,structural_zero_intervals=0,unresolved_other_coefficients=0)
 normrows=[];unresolved=[];maxrel=zero;maxindividual=zero;hsigns=[]
 for n in range(1,N+1):
  M=sum(map(abs,f[n]),zero);S=sum(map(abs,g[n]),zero)
  row=dict(n=n,density_norm=text(M),stream_norm=text(S),density_root=text((M.log()/n).exp()),stream_root=text((S.log()/n).exp()),density_norm_relative_radius=text(M.rad()/abs(M.mid())),stream_norm_relative_radius=text(S.rad()/abs(S.mid())))
  for key,series in [('density',f),('stream',g)]:
   for j,x in enumerate(series[n]):
    counts['individual_coefficients_tested']+=1
    structural=(key=='stream' and j==0) or (key=='density' and n>=6 and n%3==0 and j==n//3-2)
    if structural:
     assert x.contains(0),(key,n,j,'structural_zero');counts['structural_zero_intervals']+=1
    elif x.contains(0):
     counts['unresolved_other_coefficients']+=1;unresolved.append(dict(field=key,n=n,j=j,value=text(x)))
    else:maxindividual=maxindividual.max(x.rad()/abs(x.mid()))
  if n>=6 and n%3==0:
   H=g[n][n//3-1];assert not H.contains(0);hsigns.append(dict(k=n//3,n=n,sign=1 if H>0 else -1,value=text(H),root=text((abs(H).log()/n).exp())))
  normrows.append(row)
  if n<=150:continue
  rr=GX[n].diff(p(n)).scale(-1)+GY[n].diff(p(n),True)-FX[n]
  for v in rr.p.coeffs():assert v.contains(0),('poisson',n,text(v));counts['new_poisson_coefficients']+=1
  acc=L()
  for i in range(1,n):
   j=n-i;acc=acc+GX[i]*FY[j]-GY[i]*FX[j];counts['new_ordered_pairs']+=1
  rr=acc-F[n].scale(2*(n-1))
  for v in rr.p.coeffs():assert v.contains(0),('nonlinear',n,text(v));counts['new_nonlinear_coefficients']+=1
  rel=sum((abs(v) for v in rr.p.coeffs()),zero)/(2*(n-1)*M);maxrel=maxrel.max(rel)
  if n%3==0:assert f[n][n//3-2].contains(0);counts['new_compatibility_projections']+=1
  if n%10==0 or n==N:
   progress=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),completed_order=n,target_order=N,counts=counts,norm_rows=normrows,maximum_relative_nonlinear_residual=text(maxrel),maximum_individual_relative_radius=text(maxindividual),unresolved=unresolved,H_signs=hsigns,actual_elapsed_s=time.monotonic()-start)
   put('progress.json',progress);print(json.dumps({k:progress[k] for k in ['checked_at_utc','completed_order','target_order','actual_elapsed_s']}),flush=True)
 result={**progress,'all_finite_equations_pass':True,'selection':selection,'arithmetic_bits':ctx.prec,'scope':'Finite completed prefix only; infinite convergence and its conservative radius are supplied by119 and126.'}
 put('checks.json',result)
 for name in ['tuned_completed_audit.py','stream_precision_audit.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'};put('MANIFEST.json',dict(files=files))
 print(json.dumps(dict(all_finite_equations_pass=True,completed_order=N,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
except Exception as exc:
 import traceback
 fail=dict(error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)],actual_elapsed_s=time.monotonic()-start);put('FAILURE.json',fail);print(json.dumps(fail),flush=True);raise SystemExit(1)

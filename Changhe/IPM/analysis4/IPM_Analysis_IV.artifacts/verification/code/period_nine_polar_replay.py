"""Independent polar, two-continuation replay of longer tuned prefixes."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from hashlib import sha256
from functools import lru_cache
import argparse,gzip,json,sys,time,traceback
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import arb,arb_poly,fmpq,ctx
ROOT=Path('research/280_period_nine_prefixes')
def stamp():return datetime.now(timezone.utc).isoformat(timespec='seconds')
@lru_cache(None)
def a(q):return arb(fmpq(str(q)))
def unpack(v):
 m=F(v[0])*F(2)**v[1];r=F(v[2])*F(2)**v[3]
 return arb(a(m),a(r))
def upper(v):
 m,e=v.mid().man_exp();r,re=v.rad().man_exp()
 return F(int(m))*F(2)**int(e)+F(int(r))*F(2)**int(re)
def pack(v):
 m,e=v.mid().man_exp();r,re=v.rad().man_exp();return [str(m),int(e),str(r),int(re)]
def refine(c,I,bits):
 lo,hi=map(F,I)
 def val(t):
  v=F(0)
  for x in reversed(c):v=v*t+int(x)
  return v
 fl=val(lo);assert fl*val(hi)<0
 for _ in range(bits):
  mid=(lo+hi)/2;fm=val(mid);assert fm
  if fl*fm<0:hi=mid
  else:lo,fl=mid,fm
 return a(lo).union(a(hi)),[str(lo),str(hi)]
class Polar:
 def __init__(self,Q):self.Q=Q;self.delta=F(2,Q);self.counts=dict(ordered_products=0,poisson_columns=0,symmetry_checks=0,structural_zeros=0,compatibility_projections=0,continuations=0)
 def add(self,d,m,v):
  if m==0:return
  if m<0:m,v=-m,-v
  d[m]=d.get(m,arb(0))+v
 def sc(self,f):
  M=max(f,default=0);s=[arb(0)]*(2*M+1);c=s.copy()
  for m,v in f.items():s[M+m]=v/2;s[M-m]=-v/2;c[M+m]=v*m/2;c[M-m]=v*m/2
  return M,arb_poly(s),arb_poly(c)
 def poisson(self,f,n,H=None):
  p=1-n*self.delta;P=p+1;rhs={};g={}
  for l,v in f.items():self.add(rhs,l+1,v*a((p-l)/2));self.add(rhs,l-1,v*a((p+l)/2))
  for m,v in rhs.items():
   den=m*m-P*P
   if den:g[m]=v/a(den);assert (a(den)*g[m]-v).contains(0);self.counts['poisson_columns']+=1
   else:assert v.contains(0);self.counts['compatibility_projections']+=1
  if H is not None:g[2*(n//self.Q)-2]=H
  return g
 def order(self,n,ff,gg):
  f={};total={}
  for i in range(1,n):
   j=n-i;Mg,sg,cg=self.sc(gg[i]);Mf,sf,cf=self.sc(ff[j]);lo=Mg+Mf
   prod=sg*cf*a(2-i*self.delta)-cg*sf*a(1-j*self.delta)
   for k,v in enumerate(prod.coeffs()):total[k-lo]=total.get(k-lo,arb(0))+v
   self.counts['ordered_products']+=1
  factor=F(self.Q-2,2*(n-1))
  for m,v in total.items():
   if m<=0:continue
   if m%2==0 or m>4*n-1:assert v.contains(0);self.counts['structural_zeros']+=1
   else:
    assert v.overlaps(-total.get(-m,arb(0)));self.counts['symmetry_checks']+=1;f[m]=2*v*a(factor)
  assert total.get(0,arb(0)).contains(0)
  return f
 def continuation(self,n,ff,gg,H):
  f=dict(ff);g=dict(gg);g[n]=self.poisson(f[n],n,H)
  for m in range(n+1,n+self.Q+1):
   f[m]=self.order(m,f,g)
   if m<n+self.Q:g[m]=self.poisson(f[m],m)
  self.counts['continuations']+=1
  return f[n+self.Q].get(2*((n+self.Q)//self.Q)-3,arb(0))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--Q',type=int,required=True);ap.add_argument('--root',type=int,required=True);ap.add_argument('--bits',type=int,default=2048);args=ap.parse_args();ctx.prec=args.bits;start=time.monotonic()
 p=ROOT/f'verification/Q{args.Q}_root{args.root}_checks.json.gz';raw=p.read_bytes();d=json.loads(gzip.decompress(raw));N=d['maximum_order'];Q=args.Q
 obs=json.loads(Path(d['inputs'][0]['path']).read_bytes());b,I=refine(obs['primitive_coefficients'],obs['real_roots'][args.root-1]['interval'],args.bits+64)
 assert b.overlaps(unpack(d['root_ball']))
 solver=Polar(Q);ff={1:{1:arb(1),3:b}};gg={1:solver.poisson(ff[1],1)};norms={r['n']:r for r in d['norms']};hs={r['n']:r for r in d['harmonics']};rows=[];harm=[]
 for n in range(1,N+1):
  if n>1:
   ff[n]=solver.order(n,ff,gg)
   if n%Q==0 and n>=2*Q:
    m=2*(n//Q)-3;assert ff[n].get(m,arb(0)).contains(0);ff[n][m]=arb(0)
    R=solver.continuation(n,ff,gg,arb(0));one=solver.continuation(n,ff,gg,arb(1));sigma=one-R
    assert not sigma.contains(0) and sigma.overlaps(unpack(hs[n]['sigma']));H=-R/sigma
    assert H.overlaps(unpack(hs[n]['H']));assert n*upper(abs(H))<F(hs[n]['bound'])
    gg[n]=solver.poisson(ff[n],n,H);harm.append(dict(n=n,H=pack(H),sigma=pack(sigma)))
    print(json.dumps(dict(at=stamp(),Q=Q,root=args.root,n=n,stage='polar_tuned',actual_elapsed_s=time.monotonic()-start)),flush=True)
   else:gg[n]=solver.poisson(ff[n],n)
  fn=sum((abs(v) for v in ff[n].values()),arb(0));gn=sum((abs(v) for v in gg[n].values()),arb(0))
  assert fn.overlaps(unpack(norms[n]['F'])) and gn.overlaps(unpack(norms[n]['G'])),('norm',n)
  assert n*upper(fn)<F(norms[n]['density_bound'])
  rows.append(dict(n=n,F=pack(fn),G=pack(gn)))
 out=dict(checked_at_utc=stamp(),all_checks_pass=True,Q=Q,root_index=args.root,maximum_order=N,bits=args.bits,root_interval=I,norms=rows,harmonics=harm,counts=solver.counts,independent_norm_comparisons=2*N,independent_tuning_comparisons=len(harm),source=dict(path=str(p),sha256=sha256(raw).hexdigest()),actual_elapsed_s=time.monotonic()-start)
 target=ROOT/f'verification/Q{Q}_root{args.root}_polar_replay.json.gz';target.write_bytes(gzip.compress(json.dumps(out,separators=(',',':')).encode(),mtime=0));(ROOT/'sources/period_polar_prefix_replay.py').write_bytes(Path(__file__).read_bytes())
 print(json.dumps({k:v for k,v in out.items() if k not in ['norms','harmonics','root_interval']}),flush=True)
if __name__=='__main__':
 try:main()
 except Exception as exc:
  out=dict(checked_at_utc=stamp(),error_type=type(exc).__name__,error=str(exc),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(exc.__traceback__)])
  print(json.dumps(out),flush=True);raise SystemExit(1)

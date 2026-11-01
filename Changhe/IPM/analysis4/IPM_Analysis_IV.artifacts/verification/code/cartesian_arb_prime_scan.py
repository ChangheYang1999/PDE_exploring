"""Independent pure Cartesian Laurent interval recursion for prime resonance data."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,sys,time
sys.dont_write_bytecode=True
from flint import arb,arb_poly,fmpq,ctx

class L:
 def __init__(self,q,M,p):self.q=fmpq(q);self.M=M;self.p=p
 def diff(self,Y=False):
  vals=self.p.coeffs();v=[arb(0)]*(len(vals)+2)
  for idx,c in enumerate(vals):
   k=idx-self.M;v[idx]+=c*arb(self.q+k)/2
   h=c*arb(self.q-k)/2;v[idx+2]+=(-h if Y else h)
  return L(self.q-1,self.M+1,arb_poly(v))
 def X(self):return self.diff()
 def Y(self):return self.diff(True)


def project_sine(q,M,raw,rawM,parity):
 vals=raw.coeffs();out=[arb(0)]*(2*M+1);checks=0
 value=lambda k:vals[rawM+k] if 0<=rawM+k<len(vals) else arb(0)
 for k in range(-rawM,len(vals)-rawM):
  if k==0 or abs(k)>M or k%2!=parity:
   assert value(k).contains(0),('forbidden',k);checks+=1
 for k in range(1,M+1):
  if k%2!=parity:continue
  pos=value(k);assert (pos+value(-k)).contains(0);checks+=1
  out[M+k]=pos;out[M-k]=-pos
 return L(q,M,arb_poly(out)),checks


def compute(p,a):
 start=time.monotonic();delta=fmpq(a,p);c=1/(1-delta)
 F={};G={};XF={};YF={};XG={};YG={};checks=0
 for n in range(1,p+1):
  q=1-n*delta
  if n==1:A=L(q,1,arb_poly([arb(-1)/2,arb(0),arb(1)/2]))
  else:
   total=arb_poly()
   for i in range(1,n):
    j=n-i;assert XG[i].q+YF[j].q==q
    total+=XG[i].p*YF[j].p-YG[i].p*XF[j].p
   total*=1/arb((n-1)*(c-1))
   A,num=project_sine(q,2*n-1,total,2*n+1,1);checks+=num
  F[n]=A;XF[n]=A.X();YF[n]=A.Y()
  if n<p:
   H=XF[n];P=q+1;v=[arb(0)]*(4*n+1)
   for m in range(2,2*n+1,2):
    den=fmpq(m*m)-P*P;assert den!=0
    amp=H.p[H.M+m]/arb(den);v[2*n+m]=amp;v[2*n-m]=-amp
   B=L(P,2*n,arb_poly(v));G[n]=B;XG[n]=B.X();YG[n]=B.Y()
 m=a-2;kappa=2*F[p].p[F[p].M+m-1];force=2*XF[p].p[XF[p].M+m]
 assert (force+m*kappa).contains(0)
 return kappa,dict(p=p,a=a,delta_exact=str(delta),first_resonance_order=p,resonant_stream_frequency=m,forbidden_and_symmetry_checks=checks,forcing_nonzero=not force.contains(0),actual_elapsed_s=time.monotonic()-start)


def pack(v):
 m,e=v.mid().man_exp();r,re=v.rad().man_exp()
 return [str(m),int(e),str(r)+'*2^'+str(re)]


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--pairs',default='');ap.add_argument('--seconds',type=float,default=520);ap.add_argument('--skip',type=int,default=0);ap.add_argument('--max-cases',type=int,default=10000);args=ap.parse_args()
 ctx.prec=512;start=time.monotonic();stamp=datetime.now(timezone.utc)
 root=Path('research/80_compatibility_size_criterion/verification')/('cartesian_arb_scan_'+stamp.strftime('%Y%m%dT%H%M%SZ'));root.mkdir();(root/'sources').mkdir()
 path=Path('../a4-num/notes/kappa_scan_arb.jsonl');raw=path.read_bytes();reports=[json.loads(line) for line in raw.splitlines()];refs={(r['p'],r['a']):r for r in reports}
 pairs=[tuple(map(int,x.split(':'))) for x in args.pairs.split(',')] if args.pairs else list(refs)[args.skip:args.skip+args.max_cases]
 (root/'sources/numerics_scan.jsonl').write_bytes(raw);(root/'sources/cartesian_arb_prime_scan.py.txt').write_bytes(Path(__file__).read_bytes())
 exactroot=Path('research/80_compatibility_size_criterion/verification/extended_scan_20261031T065233Z');rows=[]
 for p,a in pairs:
  if time.monotonic()-start>args.seconds:break
  kap,row=compute(p,a);ref=refs[(p,a)];resolved=not kap.contains(0)
  log=abs(kap).log()/arb(10).log() if resolved else None
  assert resolved and row['forcing_nonzero']
  difference=abs(log-arb(ref['log10_abs_kappa']));assert difference<arb('1e-9')
  exact=exactroot/f'p{p}_a{a}.json'
  if exact.exists():
   q=fmpq(json.loads(exact.read_text())['kappa_exact']);assert kap.contains(arb(q));row['independent_exact_value_contained']=True
  row.update(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),kappa_dyadic_ball=pack(kap),certified_nonzero=resolved,log10_abs_kappa=log.str(36,radius=True),log10_abs_kappa_over_p=(log/p).str(36,radius=True),relative_radius=(kap.rad()/abs(kap.mid())).str(20,radius=True),reported_float_difference=difference.str(20,radius=True),reported_certified_nonzero=ref['certified_nonzero'])
  rows.append(row);(root/f'p{p}_a{a}.json').write_text(json.dumps(row,indent=2)+'\n')
  summary=dict(checked_at_utc=stamp.isoformat(timespec='seconds'),precision_bits=512,source_path=str(path),source_sha256=sha256(raw).hexdigest(),requested_pairs=pairs,completed_count=len(rows),complete=len(rows)==len(pairs),rows=[{k:v for k,v in x.items() if k!='kappa_dyadic_ball'} for x in rows],actual_elapsed_s=time.monotonic()-start)
  (root/'checks.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({k:v for k,v in row.items() if k!='kappa_dyadic_ball'}),flush=True)
 print(json.dumps(dict(output_directory=str(root),completed_count=len(rows),actual_elapsed_s=time.monotonic()-start)),flush=True)

if __name__=='__main__':
 try:main()
 except Exception as exc:
  print(json.dumps(dict(error_type=type(exc).__name__,message=str(exc))),flush=True);raise SystemExit(1)

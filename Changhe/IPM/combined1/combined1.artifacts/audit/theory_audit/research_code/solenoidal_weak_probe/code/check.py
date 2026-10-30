"""Exact scalar-gradient subtraction, with a second direct Fourier-vector square."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from functools import lru_cache
import argparse,hashlib,importlib.util,json,sys,time
from flint import arb,arb_poly,ctx,fmpq as Q
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
HELPER=ROOT.parent/'localized_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('t4_polar',HELPER)
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
T,W,Z=f.T,f.W,f.ZERO
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ap(p):return arb_poly([f.ar(v) for v in p])
def accum(d,k,v):d[k]=d.get(k,arb_poly([]))+v
@lru_cache(None)
def moments(b,n):
 b=Q(b)
 assert b>-1
 return [f.ar(1/((b+j+1)*(b+j+2))) for j in range(n)]
def integ(p,b):
 q=p(arb_poly([arb(1),arb(-1)]))
 return sum((v*m for v,m in zip(q,moments(str(b),len(q)))),arb(0))
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--mode',type=int,default=7);parser.add_argument('--a',default='0');parser.add_argument('--bits',type=int,default=2048)
 args=parser.parse_args();ctx.prec=args.bits;N=args.mode;a=Q(args.a);start=time.monotonic()
 source=ROOT.parent/'projected_laplacian/data/candidate007_canonical.json'
 probe=ROOT.parent/'optimized_probe_007/verification'/f'n{N}_a{str(a).replace("/","_")}.json'
 peer=json.loads(probe.read_text());c,delta,rho,stream=f.fields(json.loads(source.read_text()))
 assert sha(source)==peer['input_sha256']
 P=sum((Q(v)*T**int(k) for k,v in peer['probe_coefficients'].items()),Z)
 Pp=ap(P);Qp=ap((1-4*T)*P+2*T*W*P.derivative());P2=Pp*Pp;Q2=Qp*Qp;PQ=Pp*Qp
 rr={k:ap(v) for k,v in rho.items()}
 tr={k:ap(f.td(v,(k[0]+1)*delta/2,1)) for k,v in rho.items()}
 CC={};BQ={};BP={};XPQ={};XPP={}
 for (i,l),r in rr.items():
  for (j,m),s in rr.items():
   same=int(l==m);diff=int(abs(l-m)==2*N);sm=int(l+m==2*N)
   aa=2*same-diff+sm;bb=2*same-diff-sm;dd=2*same+diff-sm
   xx=sm+(1 if m>l else -1 if m<l else 0)*diff
   key=i+j
   if aa:
    accum(CC,key,tr[i,l]*tr[j,m]*aa)
    accum(BQ,key,r*s*aa)
    accum(XPQ,key,tr[i,l]*s*aa)
   if bb:accum(CC,key,r*s*(bb*l*m))
   if dd:accum(BP,key,r*s*(dd*N*N))
   if xx:accum(XPP,key,r*s*(xx*N*l))
 def sumint(d,p):return sum((integ(v*p,1-a+(k+2)*delta/2) for k,v in d.items()),arb(0))
 C2=arb.pi()/8*sumint(CC,P2)
 B2=arb.pi()/8*(sumint(BQ,Q2)+sumint(BP,P2))
 X=arb.pi()/8*(sumint(XPQ,PQ)+sumint(XPP,P2))
 assert C2>0 and B2>0 and C2.sqrt().overlaps(arb(peer['C']))
 S=C2+2*X+B2;assert S>0
 lopt=(C2+X)/S
 rational=Fraction(lopt.mid().str(32,radius=False));lam=Q(rational.numerator,rational.denominator)
 projected2=C2-2*f.ar(lam)*(C2+X)+f.ar(lam*lam)*S
 assert projected2>0
 print('scalar form ready',time.monotonic()-start,'lambda',lam,flush=True)
 # Independent direct square: collect radial cosine and tangential sine modes.
 radial={};tangent={};half=Q(1,2)
 def cosadd(d,j,m,v):accum(d,(j,abs(m)),v)
 def sinadd(d,j,m,v):
  if m:accum(d,(j,abs(m)),v*(1 if m>0 else -1))
 for (j,l),r in rr.items():
  A=(f.ar(1-lam)*Pp*tr[j,l]-f.ar(lam)*Qp*r)*f.ar(half)
  cosadd(radial,j,N-l,A);cosadd(radial,j,N+l,-A)
  A=f.ar((1-lam)*l*half)*Pp*r
  B=-f.ar(lam*N*half)*Pp*r
  sinadd(tangent,j,N+l,A);sinadd(tangent,j,N-l,A)
  sinadd(tangent,j,l+N,B);sinadd(tangent,j,l-N,B)
 direct=arb(0)
 for modes in (radial,tangent):
  byn={}
  for (j,n),v in modes.items():byn.setdefault(n,[]).append((j,v))
  sq={}
  for n,rows in byn.items():
   for ii,(j,p) in enumerate(rows):
    for k,q in rows[ii:]:accum(sq,j+k,p*q*((2 if n==0 else 1)*(1 if j==k else 2)))
  direct+=arb.pi()/2*sumint(sq,arb_poly([arb(1)]))
 assert direct.overlaps(projected2),(direct,projected2)
 cap=projected2.sqrt();M=arb(peer['M']);I=abs(arb(peer['pairing']));H=f.ar(Q(peer['H_upper_exact']));CU=f.ar(Q(peer['C_U_exact']))
 D=M+CU*cap
 radius=2*I/(D+(D*D+4*CU*H*I).sqrt())
 floor=Q(int((radius.lower()*arb(10**12)).floor().unique_fmpz()),10**12)
 assert f.ar(floor)<radius
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':peer['candidate'],'angular_mode':N,'a':str(a),'precision_bits':ctx.prec,'source_sha256':sha(source),'probe_sha256':sha(probe),'code_sha256':sha(__file__),'helper_sha256':sha(HELPER),'lambda_exact':str(lam),'lambda_optimal_enclosure':lopt.str(80),'C2':C2.str(100),'B2':B2.str(100),'cross':X.str(100),'projected_C2':projected2.str(100),'direct_C2':direct.str(100),'direct_comparison':True,'projected_C':cap.str(100),'original_C':peer['C'],'M':peer['M'],'pairing':peer['pairing'],'H_upper_exact':peer['H_upper_exact'],'C_U_exact':peer['C_U_exact'],'D':D.str(100),'radius':radius.str(100),'strict_lower_exact':str(floor),'elapsed_seconds':time.monotonic()-start,'status':'OPEN independent peer review'}
 dest=ROOT/'verification'/f'n{N}_a{str(a).replace("/","_")}.json';assert not dest.exists();dest.write_text(json.dumps(out,indent=2)+'\n')
 print('finished',dest,'C',cap.str(15),'radius',radius.str(30),'floor',floor,'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

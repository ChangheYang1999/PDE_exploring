"""Cosine-mode decay of the residual and profile quotients of the residual and profile quotients Q (NUMERICAL diagnostic, unweighted Parseval sums)."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import importlib.util,json,hashlib,bisect,argparse,time
from flint import arb,arb_poly,ctx
ROOT=Path('data/farres');LANE=Path('verification')
def load(name,path):
 sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
G=load('own_global',LANE/'proofs/68_independent_global_coefficients/code/global_check.py')
ANG=load('own_angle',LANE/'proofs/98_exact_angular_norm/code/angular.py')
aa=G.aa

def evaluate(ep,s):
 return sum((G.C.horner(p,s)*(aa(e)*s).exp() for e,p in ep.terms.items()),arb(0))

def j_part(H,b):
 out=G.EP()
 for e,p in H.terms.items():
  if e==b:out.addterm(e,[arb(0)]+[-v/(j+1) for j,v in enumerate(p)])
  else:out=out+G.EP({e:p}).particular(-b).scale(-1)
 return out

def endpoint(d,cache,t,side):
 H=G.density_eps(d,side);s=aa(t-(d.tm if side=='inner' else d.tp))
 if side=='outer':P,Q,_,_=G.outer_eps(d,cache)
 else:
  fac=(2*aa(d.tm)).exp();j0=list(map(arb,cache['J_inner']));P=[];Q=[]
  for n in range(1,262):
   I=H[n-1].particular(2*n+4);b=2*n-4;J=j_part(H[n],b)
   hom=j0[n-1]-J.atzero()
   if n==1:
    central=fac*hom;target=3/aa(d.k)-1
    assert central.overlaps(target)
    hom=target/fac
   J.addterm(b,[hom])
   P.append((J+I.scale(-1)).expmul(2).scale(n*fac))
   Q.append(((J+I).scale(n)+(H[n]+H[n-1]).scale(F(-1,2))).expmul(2).scale(fac))
 rh=[evaluate(v,s) for v in H];drh=[evaluate(v.deriv(),s) for v in H]
 return rh,drh,[evaluate(v,s) for v in P],[evaluate(v,s) for v in Q],[evaluate(v.deriv(),s) for v in P]

def point(d,cache,t):
 if t<d.tm:return endpoint(d,cache,t,'inner')
 if t>d.tp:return endpoint(d,cache,t,'outer')
 span=bisect.bisect_right(d.knots,t)-1;ix=d.spans.index(span);a,b=d.knots[span:span+2]
 rows=d.poly(span).tolist();IL=list(map(arb,cache['I_left'][ix]));JR=list(map(arb,cache['J_right'][ix]))
 H,Sf,errs=G.C.local_series(rows,IL,JR,a,b,aa(t),arb(0))
 fac=(2*aa(t)).exp()
 rh=H[0];drh=H[1]
 P=[2*n*fac*Sf[n-1][0] for n in range(1,262)]
 Q=[fac*(4*v[0]+v[1]) for v in Sf]
 Pt=[2*n*fac*(2*Sf[n-1][0]+Sf[n-1][1]) for n in range(1,262)]
 return rh,drh,P,Q,Pt

def residual_sines(rh,drh,P,Q,ell):
 # All Laurent arrays use the same center. Products then have center2L.
 L=523
 def poly(items,kind):
  out=[arb(0) for _ in range(2*L+1)]
  for k,c in items:
   if k==0:out[L]+=c
   else:out[L+k]+=c;out[L-k]+=c if kind=='cos' else -c
  return arb_poly(out)
 vr=poly([(0,ell)]+[(2*n,-v/2) for n,v in enumerate(P,1)],'cos')
 sd=poly([(2*j+1,3*v+drh[j]) for j,v in enumerate(rh)],'sin')
 sq=poly([(2*n,v) for n,v in enumerate(Q,1)],'sin')
 ct=poly([(2*j+1,(2*j+1)*v/2) for j,v in enumerate(rh)],'cos')
 sr=poly([(2*j+1,v) for j,v in enumerate(rh)],'sin')
 shift=arb_poly([arb(0)]*L+[arb(1)])
 out=vr*sd+sq*ct-sr*shift
 return [out[2*L+2*j+1] for j in range(523)]

def cofactor(sines):
 # sin((2n+1)theta)/sin(theta)=1+2 sum_{j=1}^n cos(2jtheta).
 tail=arb(0);A=[arb(0) for _ in sines]
 for j in range(len(sines)-1,-1,-1):
  tail+=sines[j];A[j]=tail*(1 if j==0 else 2)
 assert ANG.axis(A).contains(0)
 return ANG.quotient(A)



def main():
 p=argparse.ArgumentParser();p.add_argument('--bits',type=int,default=128);p.add_argument('--points',default='0,2,4,8');args=p.parse_args()
 ctx.prec=args.bits;ctx.threads=1;start=time.monotonic()
 import math
 d=G.M.Data();G.check_hash(d);cache=G.load_cache(d);ell=1/aa(d.k)
 for ts in args.points.split(','):
  t=F(ts);rh,drh,P,Q,Pt=point(d,cache,t);sines=residual_sines(rh,drh,P,Q,ell);B=cofactor(sines)
  qq=[float(x.mid()) for x in ANG.quotient(B)]
  prof=cofactor(list(rh)+[arb(0)]*(523-len(rh)));pq=[float(x.mid()) for x in ANG.quotient(prof)]
  rr=[float(x.mid()) for x in rh]
  def band(c,lo,hi):return math.sqrt(sum(v*v for v in c[lo:hi])/(hi-lo))
  out={'t':ts}
  for name,c in (('profile_sines',rr),('profile_Q',pq),('residual_Q',qq)):
   bands=[(10,20),(20,40),(40,80),(80,160),(160,250)]
   vals=[band(c,a,b) for a,b in bands]
   slopes=[math.log(vals[i+1]/vals[i])/math.log(2) if vals[i]>0 and vals[i+1]>0 else None for i in range(len(vals)-1)]
   out[name]={'rms_bands':['%.3e'%v for v in vals],'log2_slopes':['%.2f'%s if s is not None else None for s in slopes]}
  print(json.dumps(out),flush=True)
if __name__=='__main__':main()

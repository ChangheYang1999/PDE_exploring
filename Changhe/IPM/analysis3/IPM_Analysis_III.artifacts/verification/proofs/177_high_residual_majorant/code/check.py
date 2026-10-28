"""Single-thread directed bound for the explicit high target norm."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
 os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
from datetime import datetime,timezone
import importlib.util,json,hashlib,argparse,time
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
def load(name,path):
 sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
I=load('high_integrator',LANE/'proofs/134_residual_green_taylor/code/integrate.py')
G=I.G;aa=G.aa
G.M.SOURCE=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
def now():return datetime.now(timezone.utc).isoformat()
def log(**kw):print(json.dumps({'date':now(),**kw}),flush=True)
def up(x):return arb(x.abs_upper())
def rec(x):return G.rec(x)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def coeff_major(ep,rate,left):
 out=arb(0)
 for e,p in ep.terms.items():
  if all(v==0 for v in p):continue
  gap=e-rate if left else rate-e
  assert gap>=0,(str(e),str(rate),left)
  if gap==0:
   assert all(v==0 for v in p[1:]),(str(e),len(p))
   out+=up(p[0])
  else:
   out+=sum((up(v)*factorial(j)/aa(gap)**j for j,v in enumerate(p)),arb(0))
 return up(out)
def derivatives(eps,rate,left,count):
 out=[]
 for j in range(count):
  out.append(sum((coeff_major(ep,rate,left) for ep in eps),arb(0)))
  eps=[ep.deriv() for ep in eps]
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--bits',type=int,default=512);ap.add_argument('--tag',default='production_512');ap.add_argument('--inner-method',choices=['ep','green'],default='ep');args=ap.parse_args()
 ctx.prec=args.bits;ctx.threads=1;start=time.monotonic();log(stage='start',bits=args.bits)
 d=G.M.Data();G.check_hash(d);assert d.tm<0<d.tp;cache=G.load_cache(d);log(stage='source_loaded',seconds=time.monotonic()-start)
 delta=F(9,5);nu=F(53,10);sig=F(25,4);k=d.k;ell=1/aa(k);c=3*ell-1;v=F(19,10);N=1044;div=2*522**2*(2*522+1)
 # Exact rational polynomial coefficients for derivatives of 1/a_*.
 polys=[[F(1)]];Cs=[F(1)]
 for j in range(7):
  p=polys[-1];q=[F(0)]*(len(p)+1)
  for n,x in enumerate(p):q[n]+=(-delta+n)*x;q[n+1]+=(nu-n)*x
  polys.append(q);Cs.append(sum(map(abs,q),F(0)))
 assert polys[1]==[-delta,nu]
 # Bound raw spline controls via exact binary rational source data.
 raw=G.M.np.load(G.M.SOURCE,allow_pickle=False)
 H0=sum((max(F.from_float(float(x)) if float(x)>=0 else -F.from_float(float(x)) for x in row) for row in raw['S']),F(0))/2
 hmin=min(d.knots[i+1]-d.knots[i] for i in d.spans);L=d.tp-d.tm
 hh=[aa(H0*2**j*F(factorial(7),factorial(7-j))/hmin**j) for j in range(8)]+[arb(0)]
 fac=(2*aa(d.tp)).exp();eg=(2*aa(L)).exp()
 ii=[fac*(sum((up(z) for z in d.initial('I')),arb(0))+hh[0]/6)]
 jj=[fac*(eg*sum((up(z) for z in d.initial('J')),arb(0))+hh[0]*(eg-1)/2)]
 rr=[fac*sum((comb(j,l)*2**(j-l)*hh[l] for l in range(j+1)),arb(0)) for j in range(8)]
 for j in range(1,8):ii.append(524*ii[-1]+rr[j-1]);jj.append(520*jj[-1]+rr[j-1])
 pp=[261*(x+y) for x,y in zip(ii,jj)];qq=[pp[j]+rr[j] for j in range(8)]
 def residual_bounds(h,p,q,linear=None,inner=False):
  out=[]
  for j in range(8):
   val=linear[j] if linear is not None else up(3*ell-1)*h[j]+ell*h[j+1]
   if inner:val+=up(c)*(3*h[j]+h[j+1]+523*h[j])
   for l in range(j+1):
    hd=3*h[j-l]+h[j-l+1];ht=523*h[j-l]
    if inner and j==l:hd+=aa(F(3,2));ht+=1
    val+=comb(j,l)*(p[l]*hd+q[l]*ht)
   out.append(up(val))
  return out
 def weighted(S,fac):
  return [up(div*fac*sum((comb(j,l)*aa(Cs[l])*S[j-l] for l in range(j+1)),arb(0))) for j in range(8)]
 two_nu=(aa(2).log()*aa(nu)).exp()
 mfac=two_nu*max((-aa(delta*d.tm)).exp(),(aa(F(7,2)*d.tp)).exp())
 middle=weighted(residual_bounds(hh,pp,qq),mfac)
 log(stage='middle',bound=middle[7].str(12),seconds=time.monotonic()-start)
 # Inner nonconstant terms. Constants removed only after verifying their known identity.
 he,pe,qe=I.inner_eps(d,cache)
 for idx,ep in enumerate(he):
  assert all(x==0 for x in ep.terms.get(F(0),[arb(0)])[1:]);val=ep.terms.get(F(0),[arb(0)])[0];target=aa(F(1,4)) if idx in (0,1) else arb(0)
  assert val.overlaps(target)
 for eps in (pe,qe):
  for idx,ep in enumerate(eps):
   assert all(x==0 for x in ep.terms.get(F(0),[arb(0)])[1:]);val=ep.terms.get(F(0),[arb(0)])[0];target=c if idx==0 else arb(0)
   assert val.overlaps(target)
 def remove(eps):return [G.EP({e:p for e,p in ep.terms.items() if e!=0}) for ep in eps]
 hi=derivatives(remove(he),v,True,9)
 if args.inner_method=='ep':
  pi=derivatives(remove(pe),v,True,8);qi=derivatives(remove(qe),v,True,8)
 else:
  facm=(2*aa(d.tm)).exp()
  ri=[facm*(aa(F(2**j,2))+sum((comb(j,l)*2**(j-l)*hi[l] for l in range(j+1)),arb(0))) for j in range(8)]
  ib=[ri[0]/aa(4+v)]
  jb=[ri[0]/aa(v)+facm*sum((up(arb(z)) for z in cache['J_inner'][1:]),arb(0))+ri[0]/aa(2-v)]
  for j in range(1,8):ib.append(524*ib[-1]+ri[j-1]);jb.append(520*jb[-1]+ri[j-1])
  pi=[261*(ib[j]+jb[j]) for j in range(8)];qi=[pi[j]+ri[j] for j in range(8)]
 inner=weighted(residual_bounds(hi,pi,qi,inner=True),two_nu*(-aa(delta*d.tm)).exp())
 log(stage='inner',bound=inner[7].str(12),seconds=time.monotonic()-start)
 # Outer linear part combined with exact rational exponent factors, not interval cancellation.
 ho=G.density_eps(d,'outer');po,qo,_,_=G.outer_eps(d,cache);lin=[];lead_removed=0
 for ep in ho:
  le=G.EP()
  for e,p in ep.terms.items():
   cf=(3+e)/k-1
   vals=[aa(cf)*x+((j+1)*p[j+1]/aa(k) if j+1<len(p) else arb(0)) for j,x in enumerate(p)]
   if e==k-3:assert cf==0 and len(p)==1;lead_removed+=1;continue
   le.addterm(e,vals)
  lin.append(le)
 hbo=derivatives(ho,k-3,False,9);pbo=derivatives(po,k-1,False,8);qbo=derivatives(qo,k-1,False,8)
 lbo=derivatives(lin,2*k-4,False,8)
 outer=weighted(residual_bounds(hbo,pbo,qbo,linear=lbo),two_nu*(aa(F(7,2)*d.tp)).exp())
 dm=aa(v-delta);dp=aa(F(1,2)-2*k);assert dm>0 and dp>0
 A=up(aa(L)*middle[0]+inner[0]/dm+outer[0]/dp)
 B=up(aa(L)*middle[7]+inner[7]/dm+outer[7]/dp+2*len(d.spans)*middle[6]+inner[6]+outer[6])
 log(stage='radial',A=A.str(12),B=B.str(12),seconds=time.monotonic()-start)
 # Explicit smooth angular cutoff multiplier bound.
 H=[arb(1)]+[aa(factorial(j)*(9*j)**j) for j in range(1,9)];e2=aa(2).exp();R=[e2]
 for j in range(1,9):R.append(e2*sum((comb(j,l)*2*H[l]*R[j-l] for l in range(1,j+1)),arb(0)))
 S=[sum((comb(j,l)*H[l]*R[j-l] for l in range(j+1)),arb(0)) for j in range(9)]
 Q=[arb(0)]+[aa(F(72,7)*2**j) for j in range(1,9)]
 bell={(0,0):arb(1)}
 for n in range(1,9):
  for l in range(1,n+1):bell[n,l]=sum((comb(n-1,j-1)*Q[j]*bell.get((n-j,l-1),arb(0)) for j in range(1,n-l+2)),arb(0))
 M8=sum((S[l]*bell[8,l] for l in range(1,9)),arb(0));ps=(aa(2).log()*aa(sig)).exp()
 Cchi=ps.sqrt()*(1+2*ps.sqrt()*aa(F(7,3))*M8)
 R2=ps/arb.pi()*(A*A+2*B*B)
 def cyl(L):return 2*arb.pi()*(aa(1+L*L).log()*aa(sig)).exp()*R2
 CN2=cyl(N);CN32=cyl(N+3);eta2=R2+ps*ps*CN32+4*Cchi*Cchi*CN2
 eta=eta2.sqrt();strong=CN2.sqrt()
 # Use an integer decimal-power bound, tested by a directed comparison.
 exponent=1
 while not eta<aa(10)**exponent:exponent+=1
 out={'date':now(),'status':'COMPUTED_PENDING_INDEPENDENT_AUDIT','precision_bits':ctx.prec,'inner_method':args.inner_method,'input_sha256':d.sha,'scalar_sha256':sha(G.M.SCALAR),'cache_sha256':sha(G.CACHE),'script_sha256':sha(Path(__file__)),'proof_sha256':sha(ROOT/'PROOF.md'),'seconds':time.monotonic()-start,'h_min':str(hmin),'t_minus':str(d.tm),'t_plus':str(d.tp),'k':str(k),'spline_spans':len(d.spans),'H0_exact':str(H0),'weight_polynomials':[[str(x) for x in p] for p in polys],'weight_derivative_bounds':[str(x) for x in Cs],'middle_M':[rec(x) for x in middle],'inner_M':[rec(x) for x in inner],'outer_M':[rec(x) for x in outer],'inner_rate':str(v-delta),'outer_decay':str(F(1,2)-2*k),'outer_leading_terms_removed':lead_removed,'A':rec(A),'B':rec(B),'M8':rec(M8),'C_chi':rec(Cchi),'scalar_H_bound':rec(R2.sqrt()),'cofactor_H_bound':rec(strong),'eta_star_bound':rec(eta),'eta_star_less_than_power10':exponent}
 (ROOT/'evidence'/f'{args.tag}.json').write_text(json.dumps(out,indent=2)+'\n');log(stage='complete',eta=eta.str(16),decimal_power=exponent,seconds=out['seconds'])
if __name__=='__main__':main()

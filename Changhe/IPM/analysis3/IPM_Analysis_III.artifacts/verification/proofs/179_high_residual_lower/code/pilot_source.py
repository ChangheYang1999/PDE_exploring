import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import comb,factorial
import importlib.util,hashlib,json,bisect,argparse,time
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
def load(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
I=load('hlower_i',LANE/'proofs/134_residual_green_taylor/code/integrate.py');P=I.P;G=I.G;M=I.M;aa=I.aa

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--bits',type=int,default=384);ap.add_argument('--points',default='2,4');ap.add_argument('--tag',default='pilot');args=ap.parse_args();ctx.prec=args.bits;ctx.threads=1;start=time.monotonic()
 M.SOURCE=LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz';d=M.Data();cache=G.load_cache(d);ell=1/aa(d.k);D=4*ell-1;sig=aa(F(25,4));rows=[]
 polys=[[F(1)]]
 for j in range(5):
  q=[F(0)]*(len(polys[-1])+1)
  for n,x in enumerate(polys[-1]):q[n]+=(n-F(9,5))*x;q[n+1]+=(F(53,10)-n)*x
  polys.append(q)
 constants=[(aa(F(2*j+1,2)).gamma()*aa(F(25,4)-j-F(1,2)).gamma()/(2*arb.pi()*sig.gamma())).sqrt() for j in range(6)]
 for ts in args.points.split(','):
  t=F(ts);rh,drh,pp,qq,ppt=P.point(d,cache,t)
  if d.tm<t<d.tp:
   span=bisect.bisect_right(d.knots,t)-1;a,b=d.knots[span:span+2];hc=M.shift_rows(d.poly(span).tolist(),aa(t-a)/aa(b-a),aa(b-a));hs=[[factorial(j)*hc[j][n] for n in range(262)] for j in range(7)]
  else:
   side='inner' if t<=d.tm else 'outer';he=G.density_eps(d,side);x=aa(t-(d.tm if side=='inner' else d.tp));hs=[]
   for j in range(7):hs.append([P.evaluate(ep,x) for ep in he]);he=[ep.deriv() for ep in he]
  assert all(a.overlaps(b) for a,b in zip(hs[0],rh));assert all(a.overlaps(b) for a,b in zip(hs[1],drh))
  fac=(2*aa(t)).exp();rs=[[fac*sum((comb(j,l)*2**(j-l)*hs[l][n] for l in range(j+1)),arb(0)) for n in range(262)] for j in range(6)]
  pjets=[[arb(0)]*261 for _ in range(7)]
  for n in range(1,262):
   base=qq[n-1]+(rs[0][n-1]+rs[0][n])/2;ii=(base-pp[n-1])/(2*n);jj=(base+pp[n-1])/(2*n);pjets[0][n-1]=pp[n-1]
   for j in range(6):ii=-(2*n+2)*ii+rs[j][n-1];jj=(2*n-2)*jj-rs[j][n];pjets[j+1][n-1]=n*(jj-ii)
  assert all(a.overlaps(b) for a,b in zip(pjets[1],ppt))
  A=[-sum(((-1)**n*(2*n+1)**2*x/2 for n,x in enumerate(row)),arb(0)) for row in hs]
  dj=[-sum(((-1)**n*x for n,x in enumerate(row,1)),arb(0)) for row in pjets];dj[0]+=ell
  gam=[D*A[j]+sum((comb(j,l)*(dj[l]*A[j-l+1]-dj[l]*A[j-l]-2*dj[l+1]*A[j-l]) for l in range(j+1)),arb(0)) for j in range(6)]
  direct=I.ANG.axis(P.cofactor(P.residual_sines(rh,drh,pp,qq,ell)));assert gam[0].overlaps(direct)
  et=aa(t).exp();z=et/(1+et);mf=(-aa(F(9,5)*t)).exp()*((1+et).log()*aa(F(53,10))).exp();mj=[mf*G.C.horner([aa(v) for v in row],z) for row in polys]
  weighted=[sum((comb(j,l)*mj[l]*gam[j-l] for l in range(j+1)),arb(0)) for j in range(6)]
  bounds=[abs(x)/c for x,c in zip(weighted,constants)]
  row={'t':str(t),'gamma_derivatives':[G.rec(x) for x in gam],'weighted_derivatives':[G.rec(x) for x in weighted],'sobolev_lower_bounds':[G.rec(x) for x in bounds],'first_velocity_derivative_overlap':'PASS','axis_formula_overlap':'PASS'};rows.append(row)
  print(json.dumps({'date':datetime.now(timezone.utc).isoformat(),'t':str(t),'bounds':[x.str(12) for x in bounds],'seconds':time.monotonic()-start}),flush=True)
 out={'date':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_PENDING_AUDIT','bits':args.bits,'input_sha256':d.sha,'cache_sha256':sha(G.CACHE),'scalar_sha256':sha(M.SCALAR),'code_sha256':sha(Path(__file__)),'proof_sha256':sha(ROOT/'PROOF.md'),'constants':[G.rec(x) for x in constants],'weight_polynomials':[[str(x) for x in row] for row in polys],'rows':rows,'seconds':time.monotonic()-start};(ROOT/'evidence'/f'{args.tag}.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()

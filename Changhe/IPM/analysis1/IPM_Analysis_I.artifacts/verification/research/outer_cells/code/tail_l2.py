"""Complete exterior L2 half-line: finite binomial Arb vs iv recurrence."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,math,time,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[3];E=B/'research/outer_cells/evidence';LV='6a56059e5b9e2041ad94aed5be982b19b94d0b23f0c00563a20452b314ba89f9'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def dy(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def rf(t):s,m,e,b=t;assert b>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ae(x):assert x.is_finite();return dy(x.lower()),dy(x.upper())
def ie(x):
 assert not iv.isnan(x) and not iv.isinf(x);return tuple(map(rf,x._mpi_))
def record(x,method):
 lo,hi=ae(x) if method=='arb' else ie(x);assert lo<=hi;return {'lower_exact':str(lo),'upper_exact':str(hi),'display':x.str(26) if method=='arb' else str(x)}
def run(T=F(17)):
 start=time.monotonic();T=F(T);assert T>=0;ctx.prec=384;iv.dps=160
 vp=B/'research/outer_leading_cancellation/evidence/verdict.json';assert sha(vp)==LV;v=json.loads(vp.read_bytes());assert v['status']=='CONFIRMED'
 lp=B/'research/outer_leading_cancellation/evidence/leading_result.json';op=B/'research/outer_majorant/evidence/outer_result.json'
 for p in [lp,op]:assert sha(p)==v['files'][str(p.relative_to(B))]
 lead=json.loads(lp.read_bytes());old=json.loads(op.read_bytes());k=F(old['scalars_exact']['k']);L=F(old['scalars_exact']['L']);tb=F(old['tb_exact']);gamma=2*k-1
 C=[];replaced=0
 for row in old['majorant']:
  g=F(row['gamma_exact']);coeffs=[F(x['upper_exact']) for x in row['coefficients']]
  if g==gamma:assert len(coeffs)==1;coeffs=[F(lead['new_C_star']['upper_exact'])];replaced+=1
  assert k-g>0 and all(c>=0 for c in coeffs);C.append((g,coeffs))
 assert replaced==1 and len(C)==1864 and sum(len(c) for g,c in C)==3508
 sa=arb(0);si=iv.mpf(0);checks=0
 for g,coeffs in C:
  lam=2*(k-g);expa=aa(-lam*T).exp();expi=iv.exp(iq(-lam*T));moments=[expi/iq(lam)]
  for n in range(1,2*len(coeffs)-1):moments.append(iq(T**n)*expi/iq(lam)+n*moments[-1]/iq(lam))
  for l,c in enumerate(coeffs):
   n=2*l
   exactpoly=sum((F(math.comb(n,j)*math.factorial(j))*T**(n-j)/lam**(j+1) for j in range(n+1)),F(0));ma=expa*aa(exactpoly);mi=moments[n];al,au=ae(ma);il,iu=ie(mi);assert 0<al<=au and 0<il<=iu and max(al,il)<=min(au,iu),('moment',str(g),l);checks+=1
   sa+=aa(c)*ma.sqrt();si+=iq(c)*iv.sqrt(mi)
 ua=aa(tb).exp()/aa(L);ui=iv.exp(iq(tb))/iq(L);ka=ua**aa(-k)*(1+ua**(-2)*aa(-2*T).exp())**aa((3-k)/2);ki=iv.exp(-iq(k)*iv.log(ui)+iq((3-k)/2)*iv.log(1+iv.exp(iq(-2*T))/(ui*ui)))
 na=arb.pi().sqrt()*aa(L)*ka*sa;ni=iv.sqrt(iv.pi)*iq(L)*ki*si;al,au=ae(na);il,iu=ie(ni);assert 0<=al<=au and 0<=il<=iu and max(al,il)<=min(au,iu)
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_REQUIRES_SOURCE_REVIEW','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/outer_cells/PROOF.md'),'leading_verdict_sha256':LV,'leading_result_sha256':sha(lp),'outer_result_sha256':sha(op),'T_exact':str(T),'moment_overlap_checks':checks,'Arb_bits':ctx.prec,'iv_dps':iv.dps,'arb_L2_bound':record(na,'arb'),'iv_L2_bound':record(ni,'iv'),'published_upper_exact':str(max(au,iu)),'seconds':time.monotonic()-start,'scope':'L2 on r>=R exp(T), measure dX/(1+(r/L)^2), using exact rational audited leading/nonleading coefficient upper endpoints.'};return result
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--T',default='17');args=ap.parse_args();r=run(F(args.T));(E/'tail_l2.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r),flush=True)

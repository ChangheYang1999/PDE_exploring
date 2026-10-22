"""Whole log-cell residual bounds using outward Arb polynomial products.
Only independently computed center moments enter. No numerics implementation imports.
All radial polynomials use z=(t-tc)/h, |z|<=1.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,math,time,resource,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,arb_poly,arb_mat,ctx
BASE=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(BASE/'research/ball_transport/code'))
from dyadic_ball import import_ball,export_ball
E=BASE/'research/residual_cells/evidence'
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(x):x=F(x);return arb(x.numerator)/x.denominator
def ff(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ends(x):return ff(x.mid())-ff(x.rad()),ff(x.mid())+ff(x.rad())
def upper(x):assert x.is_finite();return x.abs_upper()
def out(x):a,b=ends(x);return {'display':x.str(30),'lower_exact':str(a),'upper_exact':str(b)}
def emit(**kw):print(json.dumps({'utc':utc(),**kw}),flush=True)
def add(p,q):return [a+b for a,b in zip(p,q)]
def scale(p,c):return [c*a for a in p]
def norm(p):return sum((upper(v) for v in p),arb(0)).upper()
def exp_poly(c,lam,tc,h,Q):
 """c already contains the coefficients of P(h*z)."""
 d=len(c)-1;assert Q>=d
 ell=aa(lam)*h;coeff=[arb(1)]
 for j in range(1,Q+1):coeff.append(coeff[-1]*ell/j)
 fac=(aa(lam)*tc).exp();p=[fac*sum((c[l]*coeff[q-l] for l in range(min(q,d)+1)),arb(0)) for q in range(Q+1)]
 radius=fac*upper(ell).exp()*sum((upper(c[l])*upper(ell)**(Q-l+1)/math.factorial(Q-l+1) for l in range(d+1)),arb(0))
 return p,radius.upper()
def ode(y0,lam,sig,G,h,Q):
 g,rg=G;ell=aa(lam)*h;p=[y0]
 for q in range(Q):p.append((ell*p[-1]+sig*h*g[q])/(q+1))
 radius=upper(ell).exp()*(upper(ell*p[Q]+sig*h*g[Q])/(Q+1)+h*rg)
 return p,radius.upper()
def mul(a,b,Q):
 p,rp=a;q,rq=b;prod=arb_poly(p)*arb_poly(q);c=[prod[j] for j in range(Q+1)]
 radius=sum((upper(prod[j]) for j in range(Q+1,2*Q+1)),arb(0))+norm(p)*rq+norm(q)*rp+rp*rq
 return c,radius.upper()
def tmadd(a,b):return add(a[0],b[0]),(a[1]+b[1]).upper()
def tmscale(a,c):return scale(a[0],c),(a[1]*upper(c)).upper()
def angular(models,frequencies,center,sine,Q):
 base=2*Q+1;coeff=[arb(0) for _ in range((2*center)*base+Q+1)]
 for (p,rem),n in zip(models,frequencies):
  assert 0<n<=center
  for j,v in enumerate(p):
   coeff[(center-n)*base+j]+=v/2
   coeff[(center+n)*base+j]+=(-v if sine else v)/2
 return arb_poly(coeff),sum((norm(p) for p,r in models),arb(0)).upper(),sum((r for p,r in models),arb(0)).upper()
def bernstein_matrix(Q):
 # row k, column l, for p(2u-1), all rational until outward conversion.
 vals=[[sum((F(2**i*(-1)**(l-i)*math.comb(l,i)*math.comb(k,i),math.comb(Q,i)) for i in range(min(k,l)+1)),F(0)) for l in range(Q+1)] for k in range(Q+1)]
 return vals,arb_mat([[aa(v) for v in row] for row in vals])
def product_tail(a,b):return (a[1]*b[2]+b[1]*a[2]+a[2]*b[2]).upper()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--degree',type=int,default=16);ap.add_argument('--cells',default='all');ap.add_argument('--tag',default='q16');args=ap.parse_args();Q=args.degree;assert 7<=Q<=40
 ctx.prec=384;ctx.threads=1;resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=time.monotonic()
 rp=BASE/'research/residual_samples/evidence/sample_result.json';raw=rp.read_bytes();assert hashlib.sha256(raw).hexdigest()=='0608fe74dbeef4eaf21e26aedffe61453f558e25e0e902dd72fda6b3084f630c';res=json.loads(raw)
 dep=BASE/'research/residual_samples/evidence/laurent_output_audit.json';audit=json.loads(dep.read_bytes());assert audit['status']=='PASS' and audit['sample_result_sha256']==sha(rp)
 dp=BASE/'data_exact/modal_v2.json';assert sha(dp)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';tr=json.loads(dp.read_bytes());k,L=[F.from_float(float.fromhex(tr['scalars_hex'][v])) for v in ('k','L')];assert 0<k<1 and L>0
 knots=sorted(set(F.from_float(float.fromhex(v)) for v in tr['arrays']['knots']['hex']))
 pubpath=BASE/'research/residual_samples/evidence/published_residual_snapshot.json';assert sha(pubpath)=='439df9893cf99ee0389e04358ff79146e7a95e71a061d1d09d025879ddacc331';pub=json.loads(pubpath.read_bytes(),parse_float=F)
 exactB,Bern=bernstein_matrix(Q);odd=list(range(1,522,2));even=list(range(2,523,2));base=2*Q+1
 selected=None if args.cells=='all' else set(map(int,args.cells.split(',')));records=[]
 for row in res['samples']:
  ci=row['cell']
  if selected is not None and ci not in selected:continue
  cellstart=time.monotonic();left,right=map(F,row['cell_endpoints_exact']);tc=F(row['t_exact']);h=(right-left)/2
  assert h>0 and tc==(left+right)/2 and any(a<=left<right<=b for a,b in zip(knots[:-1],knots[1:]));assert pub['rows'][ci]['ci']==ci
  tca,ha=aa(tc),aa(h);hp=[ha**j for j in range(8)];jets=[[import_ball(v) for v in r] for r in row['density_polynomial_at_point']];assert len(jets)==262 and all(len(r)==8 for r in jets) and all(v==0 for v in jets[-1])
  R=[[v*hp[j] for j,v in enumerate(p)] for p in jets];Rp=[[(j+1)*p[j+1]*hp[j] for j in range(7)]+[arb(0)] for p in jets]
  I=list(map(import_ball,row['i']));J=list(map(import_ball,row['j']));assert len(I)==len(J)==261
  rho=[exp_poly(R[j],3,tca,ha,Q) for j in range(261)]
  densdt=[exp_poly(add(scale(R[j],arb(3)),Rp[j]),3,tca,ha,Q) for j in range(261)]
  denstheta=[tmscale(v,arb(n)) for v,n in zip(rho,odd)]
  e4=(4*tca).exp();expneg2=exp_poly([arb(1)],-2,tca,ha,Q);pv=[];qv=[];max_green_tail=arb(0)
  for n in range(1,262):
   m=2*n;Fpoly=scale(add(add(Rp[n-1],Rp[n]),add(scale(R[n-1],arb(4-m)),scale(R[n],arb(4+m)))),arb(F(1,2).numerator)/F(1,2).denominator)
   G=exp_poly(Fpoly,4,tca,ha,Q);A0=e4*((jets[n-1][0]+jets[n][0])/2-m*I[n-1]);B0=e4*(m*J[n-1]-(jets[n-1][0]+jets[n][0])/2)
   Atm=ode(A0,-m,1,G,ha,Q);Btm=ode(B0,m,-1,G,ha,Q)
   pv.append(tmscale(mul(expneg2,tmadd(Atm,Btm),Q),arb(-1)/2))
   qv.append(tmscale(mul(expneg2,tmadd(Btm,tmscale(Atm,arb(-1))),Q),arb(1)/2))
   max_green_tail=max(max_green_tail,Atm[1],Btm[1])
  D=angular(densdt,odd,521,True,Q);H=angular(denstheta,odd,521,False,Q);P=angular(pv,even,522,False,Q);Qf=angular(qv,even,522,True,Q)
  linear=[tmadd(tmscale(d,1/aa(k)),tmscale(r,arb(-1))) for d,r in zip(densdt,rho)];Lin=angular(linear,odd,521,True,Q)
  nonlinear=P[0]*D[0]+Qf[0]*H[0];shift=arb_poly([arb(0)]*(522*base)+list(Lin[0]));poly=nonlinear+shift;assert poly.degree()<=2086*base+2*Q
  nonpoly=(product_tail(P,D)+product_tail(Qf,H)+Lin[2]).upper()
  discarded=sum((upper(poly[(freq+1043)*base+j]) for freq in range(-1043,1044) for j in range(Q+1,2*Q+1)),arb(0)).upper()
  coeffs=[[poly[(1043-nu)*base+j]-poly[(1043+nu)*base+j] for j in range(Q+1)] for nu in range(1,1044,2)]
  # Center coefficients must overlap the separately reconstructed point values.
  for coeff,old in zip(coeffs,row['residual_coefficients']):assert coeff[0].overlaps(import_ball(old))
  bb=arb_mat(coeffs)*Bern.transpose();bounds=[max(upper(bb[n,j]) for j in range(Q+1)) for n in range(522)]
  polynorm=sum(bounds,arb(0)).upper();W=(polynorm+nonpoly+discarded).upper();uleft=aa(left).exp()/aa(L);mleft=uleft**3*(1+uleft**2)**aa((k-3)/2);assert mleft>0
  Wm=(W/mleft.lower()).upper();pw,pwm=pub['rows'][ci]['W'],pub['rows'][ci]['W_over_m'];wu,mu=ff(W),ff(Wm)
  rec={'cell':ci,'left_exact':str(left),'right_exact':str(right),'tc_exact':str(tc),'h_exact':str(h),'degree':Q,'r_left':out(aa(left).exp()),'r_right':out(aa(right).exp()),'W_upper_exact':str(wu),'W_upper_display':W.str(24),'W_over_m_upper_exact':str(mu),'W_over_m_upper_display':Wm.str(24),'m_left':out(mleft),'retained_Bernstein_sum':out(polynorm),'nonpolynomial_remainder':out(nonpoly),'discarded_polynomial_remainder':out(discarded),'max_abs_lambda_h_exact':str(522*h),'max_Green_remainder':out(max_green_tail),'published_W_exact':str(pw),'published_Wm_exact':str(pwm),'W_comparison':'CONFIRMED_SELECTED_CELL' if wu<=pw else 'NOT_SHARP_ENOUGH','Wm_comparison':'CONFIRMED_SELECTED_CELL' if mu<=pwm else 'NOT_SHARP_ENOUGH','residual_coefficients_z':[[export_ball(v) for v in rr] for rr in coeffs],'seconds':time.monotonic()-cellstart};records.append(rec)
  emit(stage='cell_complete',cell=ci,W=rec['W_upper_display'],Wm=rec['W_over_m_upper_display'],tail=nonpoly.str(8),discard=discarded.str(8),comparison=rec['W_comparison'],weighted=rec['Wm_comparison'],seconds=rec['seconds'])
  summary={'utc':utc(),'status':'COMPUTED_REQUIRES_SOURCE_AND_OUTPUT_AUDIT','method':'384-bit Arb scaled Taylor models, Kronecker polynomial products, exact rational Bernstein conversion','degree':Q,'source_sha256':sha(__file__),'sample_result_sha256':sha(rp),'sample_audit_sha256':sha(dep),'data_sha256':sha(dp),'ball_transport_sha256':sha(BASE/'research/ball_transport/code/dyadic_ball.py'),'comparison_sha256':sha(pubpath),'cells':records,'seconds':time.monotonic()-start,'scope':'Selected full cells only; no global or tail residual bound.'}
  (E/(args.tag+'_result.json')).write_text(json.dumps(summary,indent=2)+'\n')
 emit(stage='done',cells=len(records),seconds=time.monotonic()-start)
if __name__=='__main__':main()

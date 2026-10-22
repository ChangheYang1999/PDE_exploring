"""Independent source-disc velocity Hessian bounds using density moments."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib,math,time,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];D=B/'research/n8_velocity_hessian';E=D/'evidence'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
def qa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def qi(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def aq(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def mq(x):s,m,e,b=x;assert b>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ends(x):
 lo,hi=(aq(x.lower()),aq(x.upper())) if isinstance(x,arb) else tuple(map(mq,x._mpi_));assert lo<=hi;return lo,hi
def hull(a,b,q):assert a<=b;return qa(a).union(qa(b)) if q==qa else iv.mpf([qi(a).a,qi(b).b])
def mag(x):lo,hi=ends(x);return max(abs(lo),abs(hi))
def decode(v):
 assert v['schema']=='arb-dyadic-mid-radius-v1';m=F(int(v['mid_m']))*F(2)**int(v['mid_e']);r=F(int(v['rad_m']))*F(2)**int(v['rad_e']);assert r>=0
 return m-r,m+r

def shift(p,delta,q):
 return [sum((p[j]*q(math.comb(j,l)*delta**(j-l)) for j in range(l,len(p))),q(0)) for l in range(len(p))]
def differentiate(p,j):
 return [p[l+j]*(math.factorial(l+j)//math.factorial(l)) for l in range(len(p)-j)]
def polynomial_value(p,x,q):
 y=q(0)
 for c in reversed(p):y=y*x+c
 return y

def series_moments(H,lam,N):
 # All eight exact monomial moments with a rigorous geometric tail.
 assert H>=0 and abs(lam*H)<N+2
 if H==0:return [arb(0)]*8
 z=F(lam*H);power=arb(1);sums=[arb(0)]*8
 for k in range(N+1):
  for j in range(8):sums[j]+=power/(j+k+1)
  power=power*qa(z)/(k+1)
 tailbase=abs(z)**(N+1)/F(math.factorial(N+1))/(1-abs(z)/F(N+2))
 result=[]
 for j in range(8):
  tail=H**(j+1)*tailbase/F(j+N+2)
  result.append(qa(H**(j+1))*sums[j]+hull(-tail,tail,qa))
 return result

def antiderivative(p,H,lam):
 assert H>=0
 if H==0:return iv.mpf(0)
 if lam==0:return sum((v*qi(H**(j+1)/F(j+1)) for j,v in enumerate(p)),iv.mpf(0))
 coeff=[sum((p[j]*qi((-1)**(j-l)*F(math.factorial(j),math.factorial(l))/lam**(j-l+1)) for j in range(l,len(p))),iv.mpf(0)) for l in range(len(p))]
 return iv.exp(qi(lam*H))*polynomial_value(coeff,qi(H),qi)-coeff[0]

def ode_model(y0,lam,sgn,g,h,Q,q):
 assert Q>=8 and len(g)<=8 and h>0
 ell=F(lam*h);co=[y0]
 for k in range(Q):co.append((q(ell)*co[-1]+q(sgn*h)*(g[k] if k<len(g) else q(0)))/(k+1))
 rem=mag(q(ell)*co[-1])
 expmag=qa(abs(ell)).exp() if q==qa else iv.exp(qi(abs(ell)))
 radius=ends(q(rem)*expmag/(Q+1))[1]
 return co,radius

def operator_model(P,m,jtm,itm,Hplus,Hminus,h,Q,q):
 lj=F(m-4);li=F(-m-4)
 pj=sum((F(a)*lj**k for k,a in enumerate(P)),F());pi=sum((F(a)*li**k for k,a in enumerate(P)),F())
 poly=[q(pj)*x-q(pi)*y for x,y in zip(jtm[0],itm[0])]
 # P(D)J-P(D)I: both forcing signs are negative.
 for k in range(1,len(P)):
  for j in range(k):
   cj=F(P[k])*lj**(k-1-j);ci=F(P[k])*li**(k-1-j)
   dj=differentiate(Hplus,j);di=differentiate(Hminus,j)
   for l in range(len(dj)):poly[l]-=q(h**l)*(q(cj)*dj[l]+q(ci)*di[l])
 rem=abs(pj)*jtm[1]+abs(pi)*itm[1]
 return poly,rem

def op_polys(m):
 a=[24,26,9,1];b=[6*m,5*m,m,0];c=[8-2*m*m,6-m*m,1,0];d=[m*(10-m*m),3*m,0,0]
 primary=[a,b,c,d];secondary=[[x+y for x,y in zip(a,c)],[x+y for x,y in zip(b,d)],[x-3*y for x,y in zip(a,c)],[3*x-y for x,y in zip(b,d)]]
 return primary,secondary

def bernstein_range(model):
 p,r=model;N=len(p)-1
 # u=2v-1, v in [0,1], complete degree-N transformation.
 power=[sum((p[i]*qa(math.comb(i,l)*(-1)**(i-l)*2**l) for i in range(l,N+1)),arb(0)) for l in range(N+1)]
 coeff=[sum((power[l]*qa(F(math.comb(k,l),math.comb(N,l))) for l in range(k+1)),arb(0)) for k in range(N+1)]
 return hull(min(ends(x)[0] for x in coeff)-r,max(ends(x)[1] for x in coeff)+r,qa)
def horner_range(model):
 p,r=model;v=polynomial_value(p,hull(F(-1),F(1),qi),qi)
 return v+hull(-r,r,qi)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--cells',type=int,default=13);ap.add_argument('--tag',default='full');args=ap.parse_args();assert 1<=args.cells<=13
 start=time.monotonic();data=json.loads((E/'moment_inputs.json').read_text())
 for rel,h in data['files'].items():assert sha(B/rel)==h,rel
 cells=data['cells'];pmn,pmx=map(F,data['source_center_bracket_exact']);R=3*F(data['delta_exact']);theta=F(data['theta_max_exact']);N=data['ntheta'];K=data['radial_subdivisions'];Q=data['Q'];SN=data['series_degree'];assert N==160 and K==4 and Q==16 and SN==80
 for q,ex,si in [(qa,lambda x:x.exp(),lambda x:x.sin()),(qi,iv.exp,iv.sin)]:
  assert pmn>R and 0<theta<F(1,2) and ends(ex(q(F(cells[0]['a_exact']))))[1]<pmn-R and ends(ex(q(F(cells[-1]['b_exact']))))[0]>pmx+R and ends(si(q(theta)))[0]>R/pmn
 spans={x['span']:x for x in data['spans']};decoded={}
 for si,sp in spans.items():
  assert F(sp['polynomial_mid_exact'])==(F(sp['a_exact'])+F(sp['b_exact']))/2
  assert len(sp['density_polynomials'])==262 and len(sp['i_left'])==len(sp['j_right'])==261
  assert all(decode(x)==(F(),F()) for x in sp['density_polynomials'][-1])
  decoded[si]={}
  for name,q in [('arb',qa),('iv',qi)]:decoded[si][name]={'H':[[hull(*decode(v),q) for v in p] for p in sp['density_polynomials']],'I':[hull(*decode(v),q) for v in sp['i_left']],'J':[hull(*decode(v),q) for v in sp['j_right']]}
 sa=[];ca=[];sv=[];cv=[]
 for i in range(N):
  aa=hull(theta*i/N,theta*(i+1)/N,qa);ii=hull(theta*i/N,theta*(i+1)/N,qi)
  sa.append([(aa*(2*n)).sin() for n in range(1,262)]);ca.append([(aa*(2*n)).cos() for n in range(1,262)])
  sv.append([iv.sin(ii*(2*n)) for n in range(1,262)]);cv.append([iv.cos(ii*(2*n)) for n in range(1,262)])
 maxa=F();maxi=F();rows=[];counts={'cells':0,'radial_subcells':0,'angular_radial_boxes':0,'canonical_moment_overlap_diagnostics':0,'independent_monomial_series_tails':0,'complete_antiderivatives':0,'ode_model_remainders':0,'tensor_model_remainders':0};where={};maxrema=F();maxremi=F();maxanchorwidth=F()
 for cell in cells[:args.cells]:
  si=cell['span'];sp=spans[si];left,right=map(F,[cell['a_exact'],cell['b_exact']]);spana,spanb,spanc=map(F,[sp['a_exact'],sp['b_exact'],sp['polynomial_mid_exact']]);assert spana<=left<right<=spanb
  rowa=F();rowi=F()
  for kk in range(K):
   a=left+(right-left)*kk/K;b=left+(right-left)*(kk+1)/K;tc=(a+b)/2;hh=(b-a)/2;hl=tc-spana;hr=spanb-tc
   HA=[shift(p,tc-spanc,qa) for p in decoded[si]['arb']['H']];HI=[shift(p,tc-spanc,qi) for p in decoded[si]['iv']['H']]
   rangesA=[[] for _ in range(4)];rangesI=[[] for _ in range(4)]
   for n in range(1,262):
    m=2*n;li=F(-m-4);lj=F(m-4)
    ml=series_moments(hl,li,SN);mr=series_moments(hr,-lj,SN);counts['independent_monomial_series_tails']+=16
    ia=qa(li*hl).exp()*decoded[si]['arb']['I'][n-1]+sum((v*x*((-1)**j) for j,(v,x) in enumerate(zip(HA[n-1],ml))),arb(0))
    ja=qa(-lj*hr).exp()*decoded[si]['arb']['J'][n-1]+sum((v*x for v,x in zip(HA[n],mr)),arb(0))
    ii=iv.exp(qi(li*hl))*decoded[si]['iv']['I'][n-1]+antiderivative([v*((-1)**j) for j,v in enumerate(HI[n-1])],hl,li)
    ji=iv.exp(qi(-lj*hr))*decoded[si]['iv']['J'][n-1]+antiderivative(HI[n],hr,-lj);counts['complete_antiderivatives']+=2
    for x,y in [(ia,ii),(ja,ji)]:
     al,au=ends(x);il,iu=ends(y);assert max(al,il)<=min(au,iu);counts['canonical_moment_overlap_diagnostics']+=1;maxanchorwidth=max(maxanchorwidth,au-al,iu-il)
    ga=[[v*qa(hh**j) for j,v in enumerate(p)] for p in [HA[n-1],HA[n]]];gi=[[v*qi(hh**j) for j,v in enumerate(p)] for p in [HI[n-1],HI[n]]]
    ita=ode_model(ia,li,1,ga[0],hh,Q,qa);jta=ode_model(ja,lj,-1,ga[1],hh,Q,qa);iti=ode_model(ii,li,1,gi[0],hh,Q,qi);jti=ode_model(ji,lj,-1,gi[1],hh,Q,qi);counts['ode_model_remainders']+=4
    PA,PI=op_polys(m)
    for k,P in enumerate(PA):
     tm=operator_model(P,m,jta,ita,HA[n],HA[n-1],hh,Q,qa);rangesA[k].append(bernstein_range(tm));maxrema=max(maxrema,tm[1])
    for k,P in enumerate(PI):
     tm=operator_model(P,m,jti,iti,HI[n],HI[n-1],hh,Q,qi);rangesI[k].append(horner_range(tm));maxremi=max(maxremi,tm[1])
    counts['tensor_model_remainders']+=8
   era=qa(2*b).exp()/4;eri=iv.exp(qi(2*b))/16
   for i in range(N):
    valsA=[sum((x*y for x,y in zip(v,sa[i] if k%2==0 else ca[i])),arb(0)) for k,v in enumerate(rangesA)]
    valsI=[sum((x*y for x,y in zip(v,sv[i] if k%2==0 else cv[i])),iv.mpf(0)) for k,v in enumerate(rangesI)]
    # Squaring finite endpoint magnitudes avoids generic Arb real-power failures.
    va=era*sum((qa(mag(v))**2*c for v,c in zip(valsA,[1,3,3,1])),arb(0))
    vi=eri*sum((v*v*c for v,c in zip(valsI,[3,3,1,1])),iv.mpf(0))
    ua,ui=ends(va)[1],ends(vi)[1];assert ua>=0 and ui>=0;rowa=max(rowa,ua);rowi=max(rowi,ui)
    if ua>maxa:maxa=ua;where['arb']={'ci':cell['ci'],'k':kk,'theta_index':i,'squared_upper_exact':str(ua)}
    if ui>maxi:maxi=ui;where['iv']={'ci':cell['ci'],'k':kk,'theta_index':i,'squared_upper_exact':str(ui)}
    counts['angular_radial_boxes']+=1
   counts['radial_subcells']+=1
  counts['cells']+=1;row={'ci':cell['ci'],'a_exact':str(left),'b_exact':str(right),'arb_squared_upper_exact':str(rowa),'iv_squared_upper_exact':str(rowi)};rows.append(row)
  report={'utc':datetime.now(timezone.utc).isoformat(),'ci':cell['ci'],'completed_cells':counts['cells'],'arb_upper_display':math.sqrt(float(rowa)),'iv_upper_display':math.sqrt(float(rowi)),'seconds':time.monotonic()-start};print(json.dumps(report),flush=True)
  (E/(args.tag+'_progress.json')).write_text(json.dumps(report,indent=2)+'\n')
 upper=max(maxa,maxi);num=math.ceil(math.sqrt(float(upper))*10000)
 while F(num,10000)**2<=upper:num+=1
 bound=F(num,10000);assert bound**2>upper
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FULL_INDEPENDENT_VELOCITY_HESSIAN_BOUND' if args.cells==13 else 'PASS_PARTIAL_VELOCITY_HESSIAN_SMOKE','bound_exact':str(bound),'bound_display':str(num/10000),'arb_squared_upper_exact':str(maxa),'iv_squared_upper_exact':str(maxi),'where':where,'counts':counts,'cells':rows,'max_arb_tensor_model_remainder_exact':str(maxrema),'max_iv_tensor_model_remainder_exact':str(maxremi),'max_canonical_center_moment_width_exact':str(maxanchorwidth),'seconds':time.monotonic()-start,'scope':'Full enclosing rectangle when all13cells complete. Canonical archive is an imported dependency. Moment overlap is diagnostic only; each own interval computation and complete norm bound is sufficient. No producer N8 derivatives or filter, no global inverse.','files':{str(p.relative_to(B)):sha(p) for p in [Path(__file__),E/'moment_inputs.json',D/'PROOF.md',E/'proof_first.json']}}
 (E/(args.tag+'_checks.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['utc','status','bound_exact','counts','seconds']}),flush=True)
if __name__=='__main__':main()

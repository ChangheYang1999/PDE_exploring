"""Inner cells using physical Green ODEs and stable finite upper integrals."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,math,time,argparse
from pathlib import Path
from fractions import Fraction as F
from flint import arb,arb_poly,arb_mat,ctx
B=Path(__file__).resolve().parents[3];E=B/'research/inner_cells/evidence'
sys.path.insert(0,str(B/'research/middle_residual/code'));import cell_core as core
sys.path.insert(0,str(B/'research/inner_majorant/code'));import certify_inner as moments
IV='69923605fab0dad07205705e32b52f26770053cf7392cfd919d1fb2ff415a0fc';CORE='a7679c9586f83e203d09fe3f8028e150f7da41082d769fa495840a82be71fdc1'
assert sys.flags.optimize==0

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def dy(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def out(x):
 assert x.is_finite();return {'lower_exact':str(dy(x.lower())),'upper_exact':str(dy(x.upper())),'display':x.str(24)}
def upper(x):assert x.is_finite();return x.abs_upper()
def inverse(p,lam):
 assert lam>0;q=[F(0)]*len(p)
 for l in range(len(p)-1,-1,-1):q[l]=(p[l]-(l+1)*q[l+1] if l+1<len(p) else p[l])/lam
 return q

def setup(Q=16):
 ctx.prec=384;ctx.threads=1;assert 7<=Q<=32 and sha(B/'research/middle_residual/code/cell_core.py')==CORE
 vp=B/'research/inner_majorant/evidence/verdict.json';assert sha(vp)==IV;ver=json.loads(vp.read_text());assert ver['status']=='CONFIRMED'
 for f,h in ver['files'].items():assert sha(B/f)==h
 co=json.loads((B/'research/inner_majorant/evidence/exact_inner_coefficients.json').read_text());old=json.loads((B/'research/inner_majorant/evidence/inner_result.json').read_text());ta=F(co['ta_exact']);bi=F(co['bi_exact']);k=F(old['k_exact']);L=F(old['L_exact']);assert k==F(1615536043799051,9007199254740992) and bi>=49
 alpha=[F(0)]+[F(2*l+2) for l in range(7)]+[bi];cs=[]
 for j,row in enumerate(co['rows']):
  assert row['j']==j;C=F(row['C']);assert C==(F(1,4) if j in [0,1] else 0)
  cs.append([[C]]+[[F(x)] for x in row['D']]+[list(map(F,row['Ei']))])
 assert len(cs)==262 and all(x==0 for p in cs[-1] for x in p)
 forcing=[];lower=[];b1=[]
 for n in range(1,262):
  m=2*n;fs=[];qs=[]
  for a,cm,cp in zip(alpha,cs[n-1],cs[n]):
   assert len(cm)==len(cp)
   f=[((a+4-m)*cm[l]+(a+4+m)*cp[l]+((l+1)*(cm[l+1]+cp[l+1]) if l+1<len(cm) else 0))/2 for l in range(len(cm))]
   fs.append(f);qs.append(inverse(f,a+4+m))
   if n==1:b1.append([-x for x in inverse(f,a+2)])
  forcing.append(fs);lower.append(qs)
 case=next(c for c in old['cases'] if c['T_exact']=='0');upper_boundary=[None]
 for n,row in enumerate(case['upper_Green'],2):
  assert row['n']==n;v=row['B_over_R4'];upper_boundary.append(aa(F(v['lower_exact'])).union(aa(F(v['upper_exact']))))
 assert len(upper_boundary)==261
 return {'Q':Q,'k':k,'L':L,'ta':ta,'alpha':alpha,'cs':cs,'forcing':forcing,'lower':lower,'b1':b1,'B0':upper_boundary,'R2':aa(2*ta).exp(),'R3':aa(3*ta).exp(),'R4':aa(4*ta).exp(),'Bern':core.bernstein_matrix(Q)[1]}

def bound_cell(data,left,right,keep=False):
 start=time.monotonic();a,b=F(left),F(right);assert a<b<=0;tc=(a+b)/2;h=(b-a)/2;Q=data['Q'];ha=aa(h);tca=aa(tc);alpha=data['alpha'];ta=data['ta'];k=data['k'];L=data['L'];cache={};hp=[ha**j for j in range(7)];tp=[tca**j for j in range(7)];zero=([arb(0)]*(Q+1),arb(0))
 def term(p,lam):
  if not any(p):return zero
  if lam not in cache:
   ell=aa(lam*h);fac=aa(lam*tc).exp();power=[arb(1)]
   for q in range(1,Q+1):power.append(power[-1]*ell/q)
   tails=[fac*upper(ell).exp()*upper(ell)**(Q-l+1)/math.factorial(Q-l+1) for l in range(7)];cache[lam]=(power,fac,tails)
  power,fac,tails=cache[lam];d=len(p)-1;c=[hp[l]*sum((aa(p[j])*math.comb(j,l)*tp[j-l] for j in range(l,d+1)),arb(0)) for l in range(d+1)]
  poly=[fac*sum((c[l]*power[q-l] for l in range(min(q,d)+1)),arb(0)) for q in range(Q+1)];rem=sum((upper(x)*tails[l] for l,x in enumerate(c)),arb(0)).upper();return poly,rem
 def combine(ps,offset,scale):
  acc=zero
  for p,al in zip(ps,alpha):acc=core.tmadd(acc,term(p,al+offset))
  return core.tmscale(acc,scale)
 def point_sum(ps,offset):return sum((aa((al+offset)*tc).exp()*sum((aa(v)*tp[l] for l,v in enumerate(p)),arb(0)) for p,al in zip(ps,alpha)),arb(0))
 def derivative(ps):return [[(3+al)*v+((l+1)*p[l+1] if l+1<len(p) else 0) for l,v in enumerate(p)] for p,al in zip(ps,alpha)]
 rho=[];D=[];H=[];Eta=[];ED=[]
 for j,ps in enumerate(data['cs'][:261]):
  rho.append(combine(ps,3,data['R3']));D.append(combine(derivative(ps),3,data['R3']));H.append(core.tmscale(rho[-1],arb(2*j+1)))
  es=[[F(0)]]+ps[1:];Eta.append(combine(es,3,data['R3']));ED.append(combine(derivative(es),3,data['R3']))
 Lin=[zero for _ in range(262)];c=aa(3/k-1)
 for j,(eta,dt) in enumerate(zip(Eta,ED)):
  nu=2*j+1;Lin[j]=core.tmadd(Lin[j],core.tmadd(core.tmscale(dt,1/aa(k)),core.tmscale(eta,arb(-1))))
  high=core.tmscale(core.tmadd(core.tmscale(eta,arb(nu)),core.tmscale(dt,arb(-1))),c/2);Lin[j+1]=core.tmadd(Lin[j+1],high)
  low=core.tmscale(core.tmadd(dt,core.tmscale(eta,arb(nu))),c/2 if nu==1 else -c/2);dest=(abs(nu-2)-1)//2;Lin[dest]=core.tmadd(Lin[dest],low)
 P=[];S=[];max_ode=arb(0);expneg2=term([F(1)],F(-2));expneg2=core.tmscale(expneg2,1/data['R2'])
 for n in range(1,262):
  m=2*n;fs=data['forcing'][n-1];A0=data['R4']*point_sum(data['lower'][n-1],4)
  if n==1:B0=data['R4']*point_sum(data['b1'],4)
  else:
   v=aa(m*tc).exp()*data['B0'][n-1]
   for al,p in zip(alpha,fs):
    if any(p):v+=aa((4+al)*tc).exp()*moments.integ([aa(x) for x in p],tc,-tc,4+al-m)
   B0=data['R4']*v
  G=combine(fs,4,data['R4']);A=core.ode(A0,-m,1,G,ha,Q);Bh=core.ode(B0,m,-1,G,ha,Q);max_ode=aa(max(dy(max_ode),dy(A[1].upper()),dy(Bh[1].upper())));P.append(core.tmscale(core.mul(expneg2,core.tmadd(A,Bh),Q),arb(-1)/2));S.append(core.tmscale(core.mul(expneg2,core.tmadd(Bh,core.tmscale(A,arb(-1))),Q),arb(1)/2))
 base=2*Q+1;odd=list(range(1,522,2));even=list(range(2,523,2));Pe=core.angular(P,even,522,False,Q);Se=core.angular(S,even,522,True,Q);De=core.angular(D,odd,521,True,Q);He=core.angular(H,odd,521,False,Q);Le=core.angular(Lin,list(range(1,524,2)),523,True,Q)
 prod=Pe[0]*De[0]+Se[0]*He[0]+arb_poly([arb(0)]*(520*base)+list(Le[0]));assert prod.degree()<=2086*base+2*Q
 coeffs=[[prod[(1043-nu)*base+l]-prod[(1043+nu)*base+l] for l in range(2*Q+1)] for nu in range(1,1044,2)];high=sum((upper(row[l]) for row in coeffs for l in range(Q+1,2*Q+1)),arb(0)).upper();nonpoly=(core.product_tail(Pe,De)+core.product_tail(Se,He)+Le[2]).upper();bb=arb_mat([row[:Q+1] for row in coeffs])*data['Bern'].transpose();poly=sum((max(upper(bb[j,l]) for l in range(Q+1)) for j in range(522)),arb(0)).upper();W=(poly+high+nonpoly).upper();ul=aa(ta+a).exp()/aa(L);ur=aa(ta+b).exp()/aa(L);ml=ul**3*(1+ul*ul)**aa((k-3)/2);assert ml>0;wm=(W/ml.lower()).upper();weights={str(d):out((wm*(1+ur)**aa(d)).upper()) for d in [F(0),F(1,2),F(1,2)-k]}
 l2sq=(arb.pi()*wm*wm*aa(L*L/2)*((1+ur*ur).log()-(1+ul*ul).log())).upper()
 r={'left_exact':str(a),'right_exact':str(b),'tc_exact':str(tc),'h_exact':str(h),'Q':Q,'max_abs_ODE_lambda_h_exact':str(522*h),'W':out(W),'W_over_m':out(wm),'weighted':weights,'L2_squared':out(l2sq),'retained_Bernstein_sum':out(poly),'discarded_polynomial_remainder':out(high),'nonpolynomial_remainder':out(nonpoly),'max_ODE_remainder':out(max_ode),'seconds':time.monotonic()-start}
 if keep:r['coefficients']=[[out(v) for v in row] for row in coeffs]
 return r
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--left',required=True);ap.add_argument('--right',required=True);ap.add_argument('--tag',required=True);ap.add_argument('--keep',action='store_true');args=ap.parse_args();assert args.tag.replace('_','').isalnum();d=setup();r=bound_cell(d,args.left,args.right,args.keep);outdata={'status':'COMPUTED_REQUIRES_INDEPENDENT_AUDIT','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/inner_cells/PROOF.md'),'inner_verdict_sha256':IV,'cell':r};(E/(args.tag+'_arb.json')).write_text(json.dumps(outdata,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='coefficients'},indent=2))

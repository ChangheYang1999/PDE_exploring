"""Arb exterior Taylor cells, retaining all angular and radial constituents."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,math,time,resource,argparse
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,arb_poly,arb_mat,ctx
B=Path(__file__).resolve().parents[3];E=B/'research/outer_cells/evidence'
sys.path.insert(0,str(B/'research/middle_residual/code'))
import cell_core as core
OV='7857fb1b2347ec5ec1e1206db7272c5144d903b0209f23e2a5d46cad9664d1ac'
CORE='a7679c9586f83e203d09fe3f8028e150f7da41082d769fa495840a82be71fdc1'
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def dy(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def out(x):
 assert x.is_finite();return {'lower_exact':str(dy(x.lower())),'upper_exact':str(dy(x.upper())),'display':x.str(24)}
def upper(x):assert x.is_finite();return x.abs_upper()
def pairadd(a,b):return a[0]+b[0],a[1]+b[1]
def pairscale(a,q):return a[0]*q,a[1]*q
Z=(F(0),F(0))
def setup(Q=16):
 assert 6<=Q<=32;ctx.prec=384
 assert sha(B/'research/middle_residual/code/cell_core.py')==CORE
 vp=B/'research/outer_majorant/evidence/verdict.json';assert sha(vp)==OV;ver=json.loads(vp.read_bytes());assert ver['status']=='CONFIRMED'
 op=B/'research/outer_majorant/evidence/outer_result.json';cp=B/'research/outer_majorant/evidence/exact_outer_coefficients.json'
 assert sha(op)==ver['files'][str(op.relative_to(B))] and sha(cp)==ver['files'][str(cp.relative_to(B))]
 old=json.loads(op.read_bytes());co=json.loads(cp.read_bytes());beta=list(map(F,co['beta_exact']));k=F(old['scalars_exact']['k']);L=F(old['scalars_exact']['L']);tb=F(co['tb_exact'])
 assert k==F(1615536043799051,9007199254740992) and L>0 and len(beta)==11 and beta[0]==k
 zlo,zhi=map(F,co['correction_parameter_exact_interval']);z=aa(zlo).union(aa(zhi))
 def ev(pair):return aa(pair[0])+aa(pair[1])*z
 def evaluate(poly):return [ev(v) for v in poly]
 density=[];dt=[];linear=[];pv=[];sv=[];hs=[]
 assert len(co['rows'])==262 and len(old['green'])==261
 for j,row in enumerate(co['rows']):
  assert row['j']==j and len(row['basis'])==11
  cs=[[tuple(map(F,v)) for v in poly] for poly in row['basis']]
  assert all(len(c)==(7 if b==10 else 1) for b,c in enumerate(cs))
  if j==261:assert all(v==Z for c in cs for v in c);continue
  density.append([evaluate(c) for c in cs]);dcs=[];ecs=[]
  for b,c in enumerate(cs):
   dc=[pairadd(pairscale(v,beta[b]),pairscale(c[l+1],F(l+1)) if l+1<len(c) else Z) for l,v in enumerate(c)]
   ec=[pairadd(pairscale(v,beta[b]/k-1),pairscale(c[l+1],F(l+1)/k) if l+1<len(c) else Z) for l,v in enumerate(c)]
   if b==0:assert all(v==Z for v in ec)
   dcs.append(evaluate(dc));ecs.append(evaluate(ec))
  dt.append(dcs);linear.append(ecs)
 for n,row in enumerate(old['green'],1):
  assert row['n']==n and len(row['plus_exact'])==len(row['minus_exact'])==11
  ps=[];ss=[]
  for qp,qm in zip(row['plus_exact'],row['minus_exact']):
   assert len(qp)==len(qm)
   qp=[tuple(map(F,x)) for x in qp];qm=[tuple(map(F,x)) for x in qm]
   ps.append(evaluate([pairscale(pairadd(x,y),F(-1,2)) for x,y in zip(qp,qm)]))
   ss.append(evaluate([pairscale(pairadd(y,pairscale(x,-1)),F(1,2)) for x,y in zip(qp,qm)]))
  pv.append(ps);sv.append(ss);hb=row['H_over_R4'];lo,hi=F(hb['lower_exact']),F(hb['upper_exact']);assert lo<=hi;hs.append(-(aa(lo).union(aa(hi)))/2)
 return {'Q':Q,'k':k,'L':L,'tb':tb,'beta':beta,'density':density,'dt':dt,'linear':linear,'pv':pv,'sv':sv,'hs':hs,'r2':aa(2*tb).exp(),'r3':aa(3*tb).exp(),'old_result_sha256':sha(op),'coefficient_sha256':sha(cp),'Bern':core.bernstein_matrix(Q)[1]}
def bound_cell(data,left,right,keep=False):
 start=time.monotonic();a,b=F(left),F(right);assert 0<=a<b;tc=(a+b)/2;h=(b-a)/2;Q=data['Q'];base=2*Q+1;tca,ha=aa(tc),aa(h);k=data['k'];L=data['L'];tb=data['tb']
 cache={};hp=[ha**l for l in range(7)];tp=[tca**l for l in range(7)]
 def term(c,lam):
  if all(v.is_zero() for v in c):return [arb(0)]*(Q+1),arb(0)
  if lam not in cache:
   ell=aa(lam)*ha;power=[arb(1)];absell=upper(ell)
   for q in range(1,Q+2):power.append(power[-1]*ell/q)
   fac=(aa(lam)*tca).exp();tails=[fac*absell.exp()*absell**(Q-l+1)/math.factorial(Q-l+1) for l in range(7)];cache[lam]=(power,fac,tails)
  power,fac,tails=cache[lam];d=len(c)-1
  shifted=[hp[l]*sum((math.comb(v,l)*c[v]*tp[v-l] for v in range(l,d+1)),arb(0)) for l in range(d+1)]
  poly=[fac*sum((shifted[l]*power[q-l] for l in range(min(q,d)+1)),arb(0)) for q in range(Q+1)]
  rem=sum((upper(v)*tails[l] for l,v in enumerate(shifted)),arb(0)).upper();return poly,rem
 def combine(polys,lams,scale):
  p=[arb(0)]*(Q+1);rem=arb(0)
  for c,lam in zip(polys,lams):
   q,r=term(c,lam);p=[x+y for x,y in zip(p,q)];rem+=r
  return [x*scale for x in p],(rem*upper(scale)).upper()
 beta=data['beta'];rho=[combine(cs,beta,data['r3']) for cs in data['density']];D=[combine(cs,beta,data['r3']) for cs in data['dt']];H=[core.tmscale(x,arb(2*j+1)) for j,x in enumerate(rho)];Lin=[combine(cs,beta,data['r3']) for cs in data['linear']]
 rates=[v-1 for v in beta];P=[];S=[]
 for n in range(1,262):
  trans=core.tmscale(term([data['hs'][n-1]],F(-2*n-2)),data['r2'])
  P.append(core.tmadd(combine(data['pv'][n-1],rates,data['r2']),trans));S.append(core.tmadd(combine(data['sv'][n-1],rates,data['r2']),trans))
 odd=list(range(1,522,2));even=list(range(2,523,2));De=core.angular(D,odd,521,True,Q);He=core.angular(H,odd,521,False,Q);Pe=core.angular(P,even,522,False,Q);Se=core.angular(S,even,522,True,Q);Le=core.angular(Lin,odd,521,True,Q)
 product=Pe[0]*De[0]+Se[0]*He[0];product+=arb_poly([arb(0)]*(522*base)+list(Le[0]));assert product.degree()<=2086*base+2*Q
 coeffs=[[product[(1043-nu)*base+l]-product[(1043+nu)*base+l] for l in range(2*Q+1)] for nu in range(1,1044,2)]
 discarded=sum((upper(row[l]) for row in coeffs for l in range(Q+1,2*Q+1)),arb(0)).upper();nonpoly=(core.product_tail(Pe,De)+core.product_tail(Se,He)+Le[2]).upper()
 bb=arb_mat([row[:Q+1] for row in coeffs])*data['Bern'].transpose();polynorm=sum((max(upper(bb[n,l]) for l in range(Q+1)) for n in range(522)),arb(0)).upper();W=(polynorm+discarded+nonpoly).upper()
 uleft=aa(tb+a).exp()/aa(L);uright=aa(tb+b).exp()/aa(L);ml=uleft**3*(1+uleft**2)**aa((k-3)/2);assert ml>0;Wm=(W/ml.lower()).upper()
 weights={str(d):out((Wm*(1+uright)**aa(d)).upper()) for d in [F(0),F(1,2),F(1,2)-k]}
 l2sq=(arb.pi()*Wm**2*aa(L*L/2)*((1+uright**2)/(1+uleft**2)).log()).upper()
 rec={'left_exact':str(a),'right_exact':str(b),'tc_exact':str(tc),'h_exact':str(h),'Q':Q,'max_abs_lambda_h_exact':str(h*max(abs(x) for x in beta+rates+[F(-2*n-2) for n in range(1,262)])),'W':out(W),'W_over_m':out(Wm),'weighted':weights,'L2_squared':out(l2sq),'retained_Bernstein_sum':out(polynorm),'discarded_polynomial_remainder':out(discarded),'nonpolynomial_remainder':out(nonpoly),'seconds':time.monotonic()-start}
 if keep:rec['coefficients']=[[out(x) for x in row] for row in coeffs]
 return rec
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--left',required=True);ap.add_argument('--right',required=True);ap.add_argument('--tag',required=True);ap.add_argument('--degree',type=int,default=16);ap.add_argument('--keep',action='store_true');args=ap.parse_args();assert args.tag.replace('_','').isalnum();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));st=time.monotonic();data=setup(args.degree);r=bound_cell(data,args.left,args.right,args.keep)
 outdata={'utc':utc(),'status':'COMPUTED_REQUIRES_INDEPENDENT_AUDIT','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/outer_cells/PROOF.md'),'core_sha256':CORE,'outer_verdict_sha256':OV,'old_result_sha256':data['old_result_sha256'],'coefficient_sha256':data['coefficient_sha256'],'precision_bits':ctx.prec,'cell':r,'total_seconds':time.monotonic()-st};(E/(args.tag+'_arb.json')).write_text(json.dumps(outdata,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='coefficients'}),flush=True)

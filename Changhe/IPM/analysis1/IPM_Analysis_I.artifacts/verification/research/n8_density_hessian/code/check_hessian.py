"""Two complete density Hessian upper bounds, with independent tensor/range formulas."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,json,hashlib,math,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];D=B/'research/n8_density_hessian';E=D/'evidence'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
def qa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def qi(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def aq(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def mq(x):s,m,e,b=x;assert b>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ends(x):return (aq(x.lower()),aq(x.upper())) if isinstance(x,arb) else tuple(map(mq,x._mpi_))
def hull(a,b,q):return qa(a).union(qa(b)) if q==qa else iv.mpf([qi(a).a,qi(b).b])
def out(x):lo,hi=ends(x);return {'lower_exact':str(lo),'upper_exact':str(hi),'display':[float(lo),float(hi)]}
def decode(v):
 assert v['schema']=='arb-dyadic-mid-radius-v1';m=F(int(v['mid_m']))*F(2)**int(v['mid_e']);r=F(int(v['rad_m']))*F(2)**int(v['rad_e']);assert r>=0
 return m-r,m+r

def bernstein(p,a,b):
 n=len(p)-1;h=b-a;v=[]
 for l in range(n+1):v.append(qa(h**l)*sum((p[i]*qa(math.comb(i,l)*a**(i-l)) for i in range(l,n+1)),arb(0)))
 bs=[sum((v[l]*qa(F(math.comb(k,l),math.comb(n,l))) for l in range(k+1)),arb(0)) for k in range(n+1)]
 return qa(min(ends(v)[0] for v in bs)).union(qa(max(ends(v)[1] for v in bs)))
def horner_center(p,a,b):
 n=len(p)-1;c=(a+b)/2;h=(b-a)/2
 shifted=[sum((p[i]*qi(math.comb(i,l)*c**(i-l)) for i in range(l,n+1)),iv.mpf(0)) for l in range(n+1)]
 x=hull(-h,h,qi);v=iv.mpf(0)
 for c in reversed(shifted):v=v*x+c
 return v

def combine(p,f,kind,q):
 zero=q(0);pp=[(i+1)*p[i+1] if i+1<len(p) else zero for i in range(len(p))];ppp=[(i+2)*(i+1)*p[i+2] if i+2<len(p) else zero for i in range(len(p))]
 if kind=='A':return [z+5*y+6*x for x,y,z in zip(p,pp,ppp)]
 if kind=='B':return [f*(y+2*x) for x,y in zip(p,pp)]
 if kind=='C':return [y+(3-f*f)*x for x,y in zip(p,pp)]
 if kind=='L':return [z+6*y+(9-f*f)*x for x,y,z in zip(p,pp,ppp)]
 if kind=='T':return [z+4*y+(3+f*f)*x for x,y,z in zip(p,pp,ppp)]
 raise AssertionError(kind)

start=time.monotonic();p=E/'density_inputs.json';data=json.loads(p.read_text())
for rel,h in data['files'].items():assert sha(B/rel)==h,rel
cells=data['cells'];pmn,pmx=map(F,data['source_center_bracket_exact']);R=3*F(data['delta_exact']);theta=F(data['theta_max_exact']);N=data['ntheta'];K=data['radial_subdivisions']
assert pmn>R and 0<theta<F(1,2)
for q,ex,si in [(qa,lambda x:x.exp(),lambda x:x.sin()),(qi,iv.exp,iv.sin)]:
 assert ends(ex(q(F(cells[0]['a_exact']))))[1]<pmn-R and ends(ex(q(F(cells[-1]['b_exact']))))[0]>pmx+R and ends(si(q(theta)))[0]>R/pmn
spans={x['span']:x for x in data['spans']};polysA={};polysI={};countpol=0
for si,sp in spans.items():
 assert F(sp['a_exact'])<F(sp['b_exact']) and F(sp['polynomial_mid_exact'])==(F(sp['a_exact'])+F(sp['b_exact']))/2
 pa=[];pi=[]
 for j,row in enumerate(sp['density_polynomials'][:-1]):
  rr=[decode(v) for v in row];assert len(rr)==8
  pa.append([hull(a,b,qa) for a,b in rr]);pi.append([hull(a,b,qi) for a,b in rr]);countpol+=1
 polysA[si]={kind:[combine(p,2*j+1,kind,qa) for j,p in enumerate(pa)] for kind in ['A','B','C']}
 polysI[si]={kind:[combine(p,2*j+1,kind,qi) for j,p in enumerate(pi)] for kind in ['L','T','B']}
# Exact all-mode angular cells, independently evaluated in each library.
sa=[];ca=[];sv=[];cv=[]
for i in range(N):
 lo,hi=theta*i/N,theta*(i+1)/N;aa=hull(lo,hi,qa);ii=hull(lo,hi,qi)
 sa.append([(aa*(2*j+1)).sin() for j in range(261)]);ca.append([(aa*(2*j+1)).cos() for j in range(261)])
 sv.append([iv.sin(ii*(2*j+1)) for j in range(261)]);cv.append([iv.cos(ii*(2*j+1)) for j in range(261)])
maxa=F();maxi=F();rows=[];globalwhere={};radialcount=0;angularboxes=0;componentenclosures=0
for cell in cells:
 si=cell['span'];sp=spans[si];center=F(sp['polynomial_mid_exact']);left,right=F(cell['a_exact']),F(cell['b_exact']);assert F(sp['a_exact'])<=left<right<=F(sp['b_exact'])
 rowmaxa=F();rowmaxi=F()
 for k in range(K):
  a=left+(right-left)*k/K;b=left+(right-left)*(k+1)/K;za,zb=a-center,b-center
  ba={kind:[bernstein(p,za,zb) for p in ps] for kind,ps in polysA[si].items()}
  bi={kind:[horner_center(p,za,zb) for p in ps] for kind,ps in polysI[si].items()}
  era=qa(2*b).exp();eri=iv.exp(qi(2*b))
  for i in range(N):
   aa=sum((x*y for x,y in zip(ba['A'],sa[i])),arb(0));bb=sum((x*y for x,y in zip(ba['B'],ca[i])),arb(0));cc=sum((x*y for x,y in zip(ba['C'],sa[i])),arb(0))
   ll=sum((x*y for x,y in zip(bi['L'],sv[i])),iv.mpf(0));tt=sum((x*y for x,y in zip(bi['T'],sv[i])),iv.mpf(0));bv=sum((x*y for x,y in zip(bi['B'],cv[i])),iv.mpf(0))
   va=era*(abs(aa)**2+2*abs(bb)**2+abs(cc)**2);vi=eri*(ll**2+tt**2+4*bv**2)/2
   ua,ui=ends(va)[1],ends(vi)[1];assert ua>=0 and ui>=0
   rowmaxa=max(rowmaxa,ua);rowmaxi=max(rowmaxi,ui)
   if ua>maxa:maxa=ua;globalwhere['arb']={'ci':cell['ci'],'k':k,'theta_index':i,'squared_upper_exact':str(ua)}
   if ui>maxi:maxi=ui;globalwhere['iv']={'ci':cell['ci'],'k':k,'theta_index':i,'squared_upper_exact':str(ui)}
   angularboxes+=1;componentenclosures+=6
  radialcount+=1
 row={'ci':cell['ci'],'a_exact':str(left),'b_exact':str(right),'arb_squared_upper_exact':str(rowmaxa),'iv_squared_upper_exact':str(rowmaxi)};rows.append(row)
 print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'ci':cell['ci'],'arb_upper_display':math.sqrt(float(rowmaxa)),'iv_upper_display':math.sqrt(float(rowmaxi)),'seconds':time.monotonic()-start}),flush=True)
 (E/'progress.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'completed_cells':len(rows),'global_squared_upper_exact':str(max(maxa,maxi)),'seconds':time.monotonic()-start},indent=2)+'\n')
# Report a decimal rational ceiling at 1e-4, checked by exact squaring.
upper=max(maxa,maxi);n=math.ceil(math.sqrt(float(upper))*10000)
while F(n,10000)**2<=upper:n+=1
bound=F(n,10000);assert bound**2>upper
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_DENSITY_HESSIAN_BOUND','bound_exact':str(bound),'bound_display':str(n/10000),'arb_squared_upper_exact':str(maxa),'iv_squared_upper_exact':str(maxi),'where':globalwhere,'counts':{'source_spans':len(spans),'complete_density_polynomials':countpol,'cells':len(cells),'radial_subcells':radialcount,'angular_radial_boxes':angularboxes,'summed_component_enclosures':componentenclosures,'angular_factor_enclosures':4*N*261},'cells':rows,'seconds':time.monotonic()-start,'scope':'Full enclosing rectangle, all261 nonzero-density mode positions; no mask filtering, Green moments, velocity derivative or global inverse claim.','files':{str(x.relative_to(B)):sha(x) for x in [p,Path(__file__),D/'PROOF.md',E/'proof_first.json']}}
(E/'checks.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:obj[k] for k in ['utc','status','bound_exact','counts','seconds']}),flush=True)

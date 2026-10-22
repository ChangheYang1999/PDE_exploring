"""Independent exact-density moments for selected exported modal Green values."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,math,hashlib,time,resource,argparse,itertools
from pathlib import Path
from fractions import Fraction as F
from types import SimpleNamespace
from datetime import datetime,timezone
import numpy as np
from flint import arb,ctx,fmpq,fmpq_mat
BASE=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
from exact_audit import exact_poly
sys.path.insert(0,str(BASE/'research/exponential_moments/code'))
from moments import aa,phi
E=BASE/'research/modal_green/evidence'
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for v in iter(lambda:f.read(1024**2),b''):h.update(v)
 return h.hexdigest()
def exact(v):return F.from_float(float.fromhex(v))
def fq(v):return fmpq(v.numerator,v.denominator)
def dyad(x):
 m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def bounds(x):return dyad(x.lower()),dyad(x.upper())
def ball(x):
 lo,hi=bounds(x);return {'display':x.str(30),'lower_exact':str(lo),'upper_exact':str(hi)}
def output(**kw):print(json.dumps({'utc':utc(),**kw}),flush=True)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--green',default=str(BASE.parent/'ipmA-num/data/cert_green.npz'));ap.add_argument('--bits',type=int,default=320);ap.add_argument('--modes',default='1,2,3,4,16,64,128,260,261');args=ap.parse_args()
 ctx.prec=args.bits;ctx.threads=1;ctx.cap=8;resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));start=time.monotonic()
 path=BASE/'data_exact/modal_v2.json';assert sha(path)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 d=json.loads(path.read_text());ar=d['arrays'];M,nb=ar['S']['shape'];t=[exact(v) for v in ar['knots']['hex']];sc={k:exact(v) for k,v in d['scalars_hex'].items()};k,bi,bo=(sc[q] for q in ('k','bi','bo'))
 assert d['degree']==7 and len(t)==nb+8 and t[:8]==[t[0]]*8 and t[-8:]==[t[-1]]*8
 assert all(t[i]<t[i+1] for i in range(7,nb)) and 0<k<1 and bi>0
 original=[(t[i],t[i+1]) for i in range(7,nb)];alpha=[k-3-j*(1-k)-2*l for j,l in d['outer_jl']]
 def get(name,m,j):return exact(ar[name]['hex'][m*ar[name]['shape'][1]+j])
 ns=sorted(set(int(v) for v in args.modes.split(',')));assert min(ns)>=1 and max(ns)<=M+1
 js=sorted(set(j for n in ns for j in (n-1,n)));jd={j:i for i,j in enumerate(js)}
 weights={j:{} for j in js}
 for m in range(M):
  for freq in (1+2*m,1-2*m,3+2*m,3-2*m):
   j=(abs(freq)-1)//2
   if j in weights:weights[j][m]=weights[j].get(m,F(0))+F(1 if freq>0 else -1,8)
 weights={j:{m:w for m,w in v.items() if w} for j,v in weights.items()}
 sd=[[sum((w*get('S',m,l) for m,w in weights[j].items()),F(0)) for j in js] for l in range(nb)]
 def jet(c,kn,right):
  vals=[]
  for p in range(7,0,-1):
   vals.append(c[-1] if right else c[0]);c=[p*(c[i+1]-c[i])/(kn[i+p+1]-kn[i+1]) for i in range(len(c)-1)];kn=kn[1:-1]
  return vals
 def corr(J,P,b):return [sum(((-b)**(i-l)*(J[l]-P[l])/math.factorial(l)/math.factorial(i-l) for l in range(i+1)),F(0)) for i in range(7)]
 zi=json.loads((BASE/'research/modal_repair/evidence/independent_gauss_iv.json').read_text())['values']['A00_correction'];z=aa(F(zi['lower_exact_dyadic'])).union(aa(F(zi['upper_exact_dyadic'])))
 inner={};outer={};lower={};upper={}
 for j in js:
  ws=weights[j];C=ws.get(0,F(0));D=[sum((w*get('D',m,l) for m,w in ws.items()),F(0)) for l in range(7)];A=[sum((w*get('Aout',m,l) for m,w in ws.items()),F(0)) for l in range(len(alpha))]
  ji=jet([sd[l][jd[j]] for l in range(8)],t[:16],False);jo=jet([sd[l][jd[j]] for l in range(nb-8,nb)],t[-16:],True)
  pi=[sum((D[l]*(2*l+2)**v for l in range(7)),C if v==0 else F(0)) for v in range(7)];po=[sum((A[l]*alpha[l]**v for l in range(len(alpha))),F(0)) for v in range(7)]
  ei=corr(ji,pi,bi);eo=corr(jo,po,-bo);A=[aa(v) for v in A];eo=[aa(v) for v in eo]
  A[0]+=aa(C)*z
  for l in range(7):eo[l]-=aa(C*(alpha[0]+bo)**l/F(math.factorial(l)))*z
  inner[j]=(C,D,ei);outer[j]=(A,eo);lower[j]=aa(ji[0]);upper[j]=aa(jo[0])
 # Comparison artifact is read only. All exact boundaries are reconstructed from parent counts.
 green=Path(args.green);gsha=sha(green);gg=np.load(green,allow_pickle=False);parent=gg['parent'];tbm=gg['tb'];tbr=gg['tb_rad'];assert len(tbm)==len(parent)+1 and len(tbr)==len(tbm)
 groups=[(int(i),len(list(gr))) for i,gr in itertools.groupby(parent)];assert [i for i,c in groups]==list(range(len(original)))
 tb=[]
 for (a,b),(i,count) in zip(original,groups):tb.extend(a+(b-a)*F(v,count) for v in range(count))
 tb.append(t[-1]);assert len(tb)==len(tbm)
 for i,v in enumerate(tb):
  mid,rad=F.from_float(float(tbm[i])),F.from_float(float(tbr[i]));assert rad>=0 and mid-rad<=v<=mid+rad,('nonenclosing boundary',i)
 selected=sorted(set([0,len(tb)-1]+[min(range(len(tb)),key=lambda i:abs(float(tb[i])-math.log(r))) for r in (.01,.1,1.,7.,8.6,10.,100.,1000.)]))
 selected_t={tb[i]:i for i in selected};br=sorted(set(t)|set(selected_t));assert br[0]==t[0] and br[-1]==t[-1]
 output(stage='prepared',green_sha256=gsha,modes=ns,selected_boundary_indices=selected,total_boundaries_audited=len(tb),integration_cells=len(br)-1)
 dummy=SimpleNamespace(t=t,deg=7);polys=[];density={};powers_cache={}
 for count,(a,b) in enumerate(zip(br[:-1],br[1:]),1):
  span,B=exact_poly(dummy,a,b);T=B*fmpq_mat([[fq(v) for v in row] for row in sd[span-7:span+1]]);h=b-a;mid=[[F(str(T[q,col])) for q in range(8)] for col in range(len(js))]
  left=[[aa(sum((math.comb(l,q)*c[l]*(-h/2)**(l-q) for l in range(q,8)),F(0))) for q in range(8)] for c in mid]
  right=[[aa((-1)**q*sum((math.comb(l,q)*c[l]*(h/2)**(l-q) for l in range(q,8)),F(0))) for q in range(8)] for c in mid]
  polys.append((h,left,right))
  if a in selected_t:density[a]=[v[0] for v in left]
  if b in selected_t:density[b]=[v[0] for v in right]
  if count%200==0:output(stage='exact_polynomials',done=count,seconds=time.monotonic()-start)
 # Taylor moments with |lambda h|<128+1, explicit geometric tails and outward arithmetic.
 N=128
 def moments(rate,h):
  key=(rate,h)
  if key not in powers_cache:
   z0=aa(rate*h);assert abs(z0)<N+1
   powers_cache[key]=[aa(h)**(q+1)*phi(q,z0,N) for q in range(8)]
  return powers_cache[key]
 def integrate(rate,h,c):return sum((v*w for v,w in zip(c,moments(rate,h))),arb(0))
 iv={};jv={}
 for n in ns:
  m=2*n;C,D,ei=inner[n-1];A,eo=outer[n]
  assert m+4>0 and m+4+bi>0 and all(m-4-v>0 for v in alpha) and m-4+bo>0
  iv[n]=aa(C/F(m+4)+sum((D[l]/(m+6+2*l) for l in range(7)),F(0))+sum((ei[l]*(-1)**l*math.factorial(l)/(m+4+bi)**(l+1) for l in range(7)),F(0)))
  jv[n]=sum((A[l]/aa(m-4-alpha[l]) for l in range(len(alpha))),arb(0))+sum((eo[l]*math.factorial(l)/aa(m-4+bo)**(l+1) for l in range(7)),arb(0))
 Avals={br[0]:{n:(4*aa(br[0])).exp()*((lower[n-1]+lower[n])/2-2*n*iv[n]) for n in ns}}
 Bvals={br[-1]:{n:(4*aa(br[-1])).exp()*(2*n*jv[n]-(upper[n-1]+upper[n])/2) for n in ns}}
 for count,(a,b,pol) in enumerate(zip(br[:-1],br[1:],polys),1):
  h,left,right=pol
  for n in ns:iv[n]=aa(-(2*n+4)*h).exp()*iv[n]+integrate(-(2*n+4),h,right[jd[n-1]])
  if b in selected_t:Avals[b]={n:(4*aa(b)).exp()*((density[b][jd[n-1]]+density[b][jd[n]])/2-2*n*iv[n]) for n in ns}
  if count%200==0:output(stage='forward_density',done=count,seconds=time.monotonic()-start)
 for count,i in enumerate(range(len(polys)-1,-1,-1),1):
  a=br[i];h,left,right=polys[i]
  for n in ns:jv[n]=aa((4-2*n)*h).exp()*jv[n]+integrate(4-2*n,h,left[jd[n]])
  if a in selected_t:Bvals[a]={n:(4*aa(a)).exp()*(2*n*jv[n]-(density[a][jd[n-1]]+density[a][jd[n]])/2) for n in ns}
  if count%200==0:output(stage='backward_density',done=count,seconds=time.monotonic()-start)
 comparisons=[];counts={'CONTAINED':0,'OVERLAP_ONLY':0,'DISJOINT':0}
 for name,vals in [('A',Avals),('B',Bvals)]:
  mids,rads=gg[name+'_mid'],gg[name+'_rad'];assert mids.shape==rads.shape==(len(tb),M+1)
  for i in selected:
   for n in ns:
    lo,hi=bounds(vals[tb[i]][n]);mid,rad=F.from_float(float(mids[i,n-1])),F.from_float(float(rads[i,n-1]));assert rad>=0
    status='CONTAINED' if mid-rad<=lo<=hi<=mid+rad else ('DISJOINT' if max(mid-rad,lo)>min(mid+rad,hi) else 'OVERLAP_ONLY');counts[status]+=1
    comparisons.append({'array':name,'boundary_index':i,'log_boundary_exact':str(tb[i]),'stream_index_n':n,'independent':ball(vals[tb[i]][n]),'exported_mid_hex':float(mids[i,n-1]).hex(),'exported_rad_hex':float(rads[i,n-1]).hex(),'verdict':status})
 gg.close();assert sha(green)==gsha, 'Comparison artifact changed during audit'
 out={'utc':utc(),'status':'COMPUTED_REQUIRES_SOURCE_AND_OUTPUT_AUDIT','method':'exact density projection, exact Cox polynomial reconstruction, independent inner/outer density moments and scaled Taylor series with full tails','input_sha256':sha(path),'green_path_read_only':str(green),'green_sha256':gsha,'code_sha256':sha(Path(__file__)),'moments_source_sha256':sha(BASE/'research/exponential_moments/code/moments.py'),'scalar_input_sha256':sha(BASE/'research/modal_repair/evidence/independent_gauss_iv.json'),'bits':args.bits,'Taylor_terms':N,'all_exported_boundary_enclosures_checked':len(tb),'original_spans':len(original),'integration_cells':len(polys),'mode_indices':ns,'selected_boundary_indices':selected,'counts':counts,'comparisons':comparisons,'seconds':time.monotonic()-start,'scope':'Selected Green entries only; no untested entries or residual norms certified.'}
 (E/'selected_boundaries.json').write_text(json.dumps(out,indent=2)+'\n');output(stage='done',counts=counts,seconds=out['seconds'])
if __name__=='__main__':main()

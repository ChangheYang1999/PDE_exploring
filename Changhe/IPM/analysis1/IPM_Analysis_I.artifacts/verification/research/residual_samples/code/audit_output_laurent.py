"""Independent finite residual products via Laurent polynomial multiplication."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,time,resource,math,itertools
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from flint import arb,arb_poly,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[3];E=B/'research/residual_samples/evidence'
sys.path.insert(0,str(B/'research/ball_transport/code'))
from dyadic_ball import import_ball
ctx.prec=384;ctx.threads=1;iv.dps=90

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(x):x=F(x);return arb(x.numerator)/x.denominator
def ff(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ends(x):m,r=ff(x.mid()),ff(x.rad());return m-r,m+r

def out(x):
 a,b=ends(x);return {'display':x.str(32),'lower_exact':str(a),'upper_exact':str(b)}
def iq(x):x=F(x);return iv.mpf(x.numerator)/x.denominator
def toiv(x):a,b=ends(x);return iv.mpf([iq(a).a,iq(b).b])
def fi(x):sg,m,e,_=x;return (-1 if sg else 1)*F(int(m))*F(2)**int(e)
def ie(x):return tuple(map(fi,x._mpi_))
def overlap(a,b):al,au=ends(a);bl,bu=ends(b);return max(al,bl)<=min(au,bu)
def ii_overlap(a,b):al,au=ie(a);bl,bu=ie(b);return max(al,bl)<=min(au,bu)
def comparison(v,bound):
 lo,hi=ends(v)
 return 'SAMPLE_CONSISTENT' if hi<=bound else ('REFUTED_AT_SAMPLE' if lo>bound else 'OVERLAP_ONLY')
def laurent(values,frequencies,center,sine=False):
 c=[arb(0) for _ in range(2*center+1)]
 for v,n in zip(values,frequencies):
  assert 0<n<=center;c[center-n]+=v/2;c[center+n]+=(-v if sine else v)/2
 return arb_poly(c)
def main():
 start=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
 rp=E/'sample_result.json';raw=rp.read_bytes();res=json.loads(raw);source=B/'research/residual_samples/code/certify_samples.py';assert res['source_sha256']==sha(source)
 expected={'input_sha256':('data_exact/modal_v2.json','57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'),'scalar_input_sha256':('research/modal_repair/evidence/independent_gauss_iv.json','0985679510dfa1fbfceccddd19566d85452599c4b37ecde4c84adbd5aa5f0a2a'),'moments_sha256':('research/exponential_moments/code/moments.py','6f9aa03d5f7f4f2dff22e5bc8319a861148313e96d89991c16ee979dfdf0489c'),'Cox_sha256':('research/canonical_inverse/code/exact_audit.py','331771590a0dd764208306640b4b3af63aec8cfe966ed6a0d086ec512d617b42'),'ball_transport_sha256':('research/ball_transport/code/dyadic_ball.py','6525060f436bf553f3b4a42e403ad2c27dc69d6a82a1460634995f95e755e3c3')}
 for field,(name,h) in expected.items():assert res[field]==sha(B/name)==h,(field,res[field],sha(B/name))
 pn=E/'published_residual_snapshot.json';psha=sha(pn);assert psha==res['published_residual_sha256']=='439df9893cf99ee0389e04358ff79146e7a95e71a061d1d09d025879ddacc331'
 nr=json.loads(pn.read_bytes(),parse_float=F);tr=json.loads((B/'data_exact/modal_v2.json').read_text());k,L=[F.from_float(float.fromhex(tr['scalars_hex'][v])) for v in ('k','L')]
 assert res['stream_modes']==261 and len(res['samples'])==13 and F(res['max_abs_moment_argument_exact'])<129
 gg=B.parent/'ipmA-num/data/cert_green.npz';assert sha(gg)==res['green_comparison_sha256']=='c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1';g=np.load(gg,allow_pickle=False)
 knots=[F.from_float(float.fromhex(v)) for v in tr['arrays']['knots']['hex']];ts=sorted(set(knots));groups=[(int(i),len(list(v))) for i,v in itertools.groupby(g['parent'])];assert [i for i,c in groups]==list(range(len(ts)-1));tb=[]
 for i,c in groups:tb.extend(ts[i]+(ts[i+1]-ts[i])*F(j,c) for j in range(c))
 tb.append(ts[-1]);maxrad=F(0);maxulp=F(0)
 for i,t in enumerate(tb):
  mf=float(g['tb'][i]);m,r=F.from_float(mf),F.from_float(float(g['tb_rad'][i]));assert m-r<=t<=m+r;maxrad=max(maxrad,r);maxulp=max(maxulp,r/F.from_float(math.ulp(mf)))
 assert maxulp<10
 records=[];total_coeff=0;angular=0
 for row in res['samples']:
  ci=row['cell'];assert 0<=ci<len(nr['rows']) and nr['rows'][ci]['ci']==ci;tc=F(row['t_exact']);assert tc==(tb[ci]+tb[ci+1])/2;assert list(map(F,row['cell_endpoints_exact']))==[tb[ci],tb[ci+1]]
  jets=[[import_ball(v) for v in c] for c in row['density_polynomial_at_point']];assert len(jets)==262 and all(len(c)==8 for c in jets) and all(v==0 for v in jets[-1]);R=[v[0] for v in jets[:-1]];D=[3*v[0]+v[1] for v in jets[:-1]]
  I=list(map(import_ball,row['i']));J=list(map(import_ball,row['j']));assert len(I)==len(J)==261
  rr=aa(tc).exp();e4=rr**4;Rextra=R+[arb(0)]
  Av=[e4*((Rextra[n-1]+Rextra[n])/2-2*n*I[n-1]) for n in range(1,262)]
  Bv=[e4*(2*n*J[n-1]-(Rextra[n-1]+Rextra[n])/2) for n in range(1,262)]
  odd=list(range(1,522,2));even=list(range(2,523,2));lin=[rr**3*(d/aa(k)-r) for d,r in zip(D,R)]
  ld=laurent(D,odd,521,True);lrc=laurent([n*r for n,r in zip(odd,R)],odd,521);la=laurent([a+b for a,b in zip(Av,Bv)],even,522);lb=laurent([b-a for a,b in zip(Av,Bv)],even,522,True)
  ll=laurent(lin,odd,521,True);shifted=arb_poly([arb(0)]*522+list(ll));prod=(-la*ld+lb*lrc)*(rr/2)+shifted;assert prod.degree()<=2086
  vals=[];old=list(map(import_ball,row['residual_coefficients']));assert len(old)==522
  for nu in range(1,1044,2):
   neg,pos=prod[1043-nu],prod[1043+nu];v=neg-pos;assert overlap(-2*pos,2*neg);assert overlap(v,old[(nu-1)//2]);vals.append(v);total_coeff+=1
  for freq in range(-1043,1044):
   if freq%2==0:assert prod[1043+freq].contains(0)
  W=sum(map(abs,vals),arb(0));u=rr/aa(L);weight=u**3*(1+u*u)**aa((k-3)/2);Wm=W/weight;L2=arb.pi()*sum((v**2 for v in vals),arb(0))
  for name,v in [('W',W),('W_over_m',Wm),('angular_L2_squared',L2)]:
   lower,upper=F(row[name]['lower_exact']),F(row[name]['upper_exact']);a,b=ends(v);assert max(a,lower)<=min(b,upper),(ci,name,'nonoverlap')
  rv=toiv(rr);kk=iq(k);ir=list(map(toiv,R));dd=list(map(toiv,D));av=list(map(toiv,Av));bv=list(map(toiv,Bv));vv=list(map(toiv,vals));angles=[]
  for af in [F(1,97),F(1,7),F(1,4),F(13,31),F(1,2)]:
   theta=iq(af)*iv.pi;sodd=[iv.sin(n*theta) for n in odd];codd=[iv.cos(n*theta) for n in odd];seven=[iv.sin(n*theta) for n in even];ceven=[iv.cos(n*theta) for n in even]
   rhos=rv**3*sum((r*f for r,f in zip(ir,sodd)),iv.mpf(0));rhor=rv**2*sum((r*f for r,f in zip(dd,sodd)),iv.mpf(0));rhotheta=rv**3*sum((n*r*f for n,r,f in zip(odd,ir,codd)),iv.mpf(0));ur=-sum(((a+b)*f for a,b,f in zip(av,bv,ceven)),iv.mpf(0))/(2*rv);ut=sum(((b-a)*f for a,b,f in zip(av,bv,seven)),iv.mpf(0))/(2*rv)
   direct=(rv/kk+ur)*rhor+ut*rhotheta/rv-rhos;fourier=sum((v*iv.sin((2*n+1)*theta) for n,v in enumerate(vv)),iv.mpf(0));assert ii_overlap(direct,fourier),(ci,str(af));angular+=1;angles.append({'theta_over_pi':str(af),'direct_residual':str(direct),'Fourier_residual':str(fourier)})
  pub,pubm=nr['rows'][ci]['W'],nr['rows'][ci]['W_over_m'];rec={'cell':ci,'t_exact':str(tc),'r':out(rr),'W':out(W),'W_over_m':out(Wm),'angular_L2_squared':out(L2),'published_W_exact_decimal':str(pub),'published_W_over_m_exact_decimal':str(pubm),'W_comparison':comparison(W,pub),'weighted_comparison':comparison(Wm,pubm),'angular_checks':angles};records.append(rec);print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'stage':'point_audited','cell':ci,'W':W.str(16),'Wm':Wm.str(16),'comparison':rec['W_comparison'],'weighted_comparison':rec['weighted_comparison']}),flush=True)
 outres={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','method':'384-bit Arb Laurent polynomial multiplication, exact dyadic input moments, exact decimal comparison, mpmath.iv90 direct polar substitutions','source_sha256':sha(__file__),'sample_result_sha256':hashlib.sha256(raw).hexdigest(),'sample_source_sha256':sha(source),'published_residual_sha256':psha,'dependencies':expected,'max_boundary_radius_exact':str(maxrad),'max_boundary_radius_in_ulps_exact':str(maxulp),'coefficients_audited':total_coeff,'direct_angular_checks':angular,'max_abs_moment_argument_exact':res['max_abs_moment_argument_exact'],'samples':records,'seconds':time.monotonic()-start,'scope':'Finite samples only. No whole-cell or global residual upper bound.'}
 (E/'laurent_output_audit.json').write_text(json.dumps(outres,indent=2)+'\n');print(json.dumps({'stage':'done','seconds':outres['seconds'],'status':'PASS'}),flush=True)
if __name__=='__main__':main()

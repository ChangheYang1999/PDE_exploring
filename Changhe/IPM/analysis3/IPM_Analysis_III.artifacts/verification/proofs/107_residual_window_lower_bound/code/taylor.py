import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import importlib.util,json,gzip,hashlib,time
from flint import arb,arb_poly,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
sp=importlib.util.spec_from_file_location('windowbase',ROOT/'code/window.py');W=importlib.util.module_from_spec(sp);sp.loader.exec_module(W)
P=W.P;G=W.G;ANG=W.ANG;aa=W.aa
CENTER=523

def poly(v,kind,angular):
 out=[arb(0)]*(2*CENTER+1)
 for j,c in enumerate(v):
  freq=2*(j+1) if angular=='even' else 2*j+1
  out[CENTER+freq]=c
  out[CENTER-freq]=c if kind=='cos' else -c
 return arb_poly(out)

def cross(a,b,mm):
 n=max(len(a),len(b))-1
 def pol(v):
  arr=[arb(0)]*(2*n+1);arr[n]=v[0]
  for j in range(1,len(v)):arr[n+j]=arr[n-j]=v[j]/2
  return arb_poly(arr)
 pr=pol(a)*pol(b)
 return pr[2*n]+sum((2*pr[2*n+j]*aa(mm[j]) for j in range(1,2*n+1)),arb(0))

def series_and_bound(ep,center,order,radius):
 shift=ep.shift(center);co=[arb(0)]*(order+1);bd=arb(0)
 for e,p in shift.terms.items():
  ex=[arb(1)]
  for j in range(1,order+1):ex.append(ex[-1]*aa(e)/j)
  for j in range(order+1):co[j]+=sum((p[i]*ex[j-i] for i in range(min(j,len(p)-1)+1)),arb(0))
  bd+=(aa(abs(e)*radius)).exp()*sum((arb(v.abs_upper())*aa(radius)**i for i,v in enumerate(p)),arb(0))
 return co,arb(bd.upper())

def transpose(a):return [list(x) for x in zip(*a)]

def main():
 ctx.prec=512;ctx.threads=1;start=time.monotonic();degree=20;mid=F(10);radius=F(1);half=F(1,10)
 d=G.M.Data();G.check_hash(d);cache=G.load_cache(d);assert mid-half>d.tp
 H=G.density_eps(d,'outer');Pe,Qe,_,_=G.outer_eps(d,cache);LH=[W.linear(h,d.k) for h in H];c=mid-d.tp
 def batch(eps,order):
  vals=[series_and_bound(ep,c,order,radius) for ep in eps]
  return transpose([v[0] for v in vals]),[v[1] for v in vals]
 hs,hbd=batch(H,degree+1);ps,pbd=batch(Pe,degree);qs,qbd=batch(Qe,degree);ls,lbd=batch(LH,degree)
 dhbd=[series_and_bound(ep.deriv(),c,0,radius)[1] for ep in H]
 sd=[poly([3*hs[j][n]+(j+1)*hs[j+1][n] for n in range(262)],'sin','odd') for j in range(degree+1)]
 ct=[poly([(2*n+1)*hs[j][n]/2 for n in range(262)],'cos','odd') for j in range(degree+1)]
 pc=[poly([v/2 for v in ps[j]],'cos','even') for j in range(degree+1)]
 qq=[poly(qs[j],'sin','even') for j in range(degree+1)]
 mm=ANG.moments(1044);qseries=[]
 for j in range(degree+1):
  pp=arb_poly()
  for i in range(j+1):pp+=qq[i]*ct[j-i]-pc[i]*sd[j-i]
  sins=[pp[2*CENTER+2*n+1]+(ls[j][n] if n<262 else 0) for n in range(523)]
  qseries.append(ANG.quotient(P.cofactor(sins)))
  if j%5==0:print(json.dumps({'date':datetime.now(timezone.utc).isoformat(),'taylor_order':j,'seconds':time.monotonic()-start}),flush=True)
 h0=ANG.normalized_square(qseries[0],mm);assert h0>0;scale=h0.sqrt()
 rf=[F.from_float(float((v/scale).mid())) for v in qseries[0]];r=list(map(aa,rf));hr=ANG.normalized_square(r,mm);assert hr>0
 coeff=[cross(v,r,mm) for v in qseries]
 poly_range=G.C.horner(coeff,arb(0,aa(half).upper()))
 N=522;Cnorm=aa(4*N**4*(2*N+1));rl1=sum((abs(v) for v in rf),F(0))
 sl1=sum(pbd,arb(0))*sum((3*hbd[n]+dhbd[n] for n in range(262)),arb(0))
 sl1+=sum(qbd,arb(0))*sum(((2*n+1)*hbd[n] for n in range(262)),arb(0))+sum(lbd,arb(0))
 disk=Cnorm*aa(rl1)*sl1;tail=disk*aa(half/radius)**(degree+1)/aa(1-half/radius)
 S=poly_range+arb(0,tail.upper());dist=arb(0) if S.contains(0) else arb(S.abs_lower())
 weight=((aa(F(27,4)*(mid+half))).exp()-(aa(F(27,4)*(mid-half))).exp())*aa(F(4,27))
 bound=arb(weight.lower())*arb(ANG.beta_mass().lower())*dist**2/arb(hr.upper())
 out={'date':datetime.now(timezone.utc).isoformat(),'status':'POSITIVE_LOWER_BOUND' if bound>0 else 'INCONCLUSIVE','input_sha256':d.sha,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'precision_bits':512,'center':str(mid),'half_width':str(half),'complex_radius':str(radius),'taylor_degree':degree,'S_range':G.rec(S),'polynomial_range':G.rec(poly_range),'disk_bound':G.rec(disk),'taylor_error':G.rec(tail),'witness_H':G.rec(hr),'witness_coefficient_l1':str(rl1),'angular_operator_bound':str(4*N**4*(2*N+1)),'weight_integral':G.rec(weight),'norm_square_lower':G.rec(bound),'norm_lower':G.rec(bound.sqrt()),'coefficients':[G.rec(v) for v in coeff],'witness_coefficients':[str(v) for v in rf],'seconds':time.monotonic()-start}
 (ROOT/'evidence/taylor.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:out[k] for k in ['date','status','S_range','taylor_error','norm_lower','seconds']}),flush=True)
if __name__=='__main__':main()

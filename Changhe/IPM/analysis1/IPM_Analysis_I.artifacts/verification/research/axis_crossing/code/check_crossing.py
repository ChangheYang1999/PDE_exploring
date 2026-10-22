"""All-mode axis crossing using closed ODE points plus C2 bounds, and iv Q16."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import sys,json,math,time,hashlib,resource
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/axis_crossing/evidence'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
utc=lambda:datetime.now(timezone.utc).isoformat()
def dyad(m,e):return F(int(m))*F(2)**int(e)
def mpfrac(x):
 sign,man,ex,bc=x
 return (-1 if sign else 1)*dyad(man,ex)
def bounds(x):
 if isinstance(x,arb):return tuple(dyad(*v.man_exp()) for v in (x.lower(),x.upper()))
 return tuple(mpfrac(v) for v in x._mpi_)
def record(x):
 a,b=bounds(x);assert a<=b
 return {'lower_exact':str(a),'upper_exact':str(b),'display':[float(a),float(b)]}
def rec_bounds(x):return F(x['lower_exact']),F(x['upper_exact'])
def qarb(x):
 x=F(x);return arb(fmpq(x.numerator,x.denominator))
def qiv(x):
 x=F(x);return iv.mpf(x.numerator)/x.denominator
def hull(a,b,which):
 if which=='arb':return qarb(a).union(qarb(b))
 return iv.mpf([qiv(a).a,qiv(b).b])
def getball(x,which):
 assert x['schema']=='arb-dyadic-mid-radius-v1'
 m=dyad(x['mid_m'],x['mid_e']);r=dyad(x['rad_m'],x['rad_e']);assert r>=0
 y=hull(m-r,m+r,which);l,u=bounds(y);assert l<=m-r and m+r<=u;return y

def horner(p,x):
 y=x*0
 for c in p[::-1]:y=y*x+c
 return y

def load_data():
 path=B/'research/residual_samples/evidence/sample_result.json'
 assert sha(path)=='0608fe74dbeef4eaf21e26aedffe61453f558e25e0e902dd72fda6b3084f630c'
 raw=json.loads(path.read_text());r=next(v for v in raw['samples'] if v['cell']==4102)
 a,b=map(F,r['cell_endpoints_exact']);tc=F(r['t_exact']);h=(b-a)/2;assert tc==(a+b)/2 and a<b
 assert len(r['i'])==len(r['j'])==261 and len(r['density_polynomial_at_point'])==262
 assert all(len(v)==8 for v in r['density_polynomial_at_point'])
 assert all(x['mid_m']==x['rad_m']=='0' for x in r['density_polynomial_at_point'][-1])
 return r,a,b,tc,h

def make_closed(c,lam,s,y0):
 # Only exact rational scalar operations on integer factorial ratios.
 p=None if lam==0 else [-s*sum((c[l]*(math.factorial(l)//math.factorial(j))/lam**(l-j+1) for l in range(j,8)),arb(0)) for j in range(8)]
 def value(d):
  z=qarb(d)
  if lam==0:return y0+sum((s*c[l]*z**(l+1)/(l+1) for l in range(8)),arb(0))
  return horner(p,z)+(lam*z).exp()*(y0-p[0])
 return value

def make_taylor(c,lam,s,y0,h,Q):
 hh=qiv(h);ell=lam*hh;g=[c[j]*hh**j for j in range(8)]
 p=[y0*ell**q/math.factorial(q)+s*hh*sum((g[j]*math.factorial(j)*ell**(q-1-j)/math.factorial(q) for j in range(min(8,q))),qiv(0)) for q in range(Q+1)]
 rem=iv.exp(abs(ell))*abs(ell*p[-1])/(Q+1) # g_Q=0, Q>=8
 assert Q>=8;R=bounds(rem)[1];assert R>=0
 return p,hull(-R,R,'iv'),str(R)

def main():
 start=time.monotonic();ctx.prec=512;ctx.threads=1;iv.dps=180
 resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3))
 r,a,b,tc,h=load_data();K=64;Q=16;cl=F(9007199254740992,1615536043799051)
 ac=[[getball(z,'arb') for z in c] for c in r['density_polynomial_at_point']];ic=[[getball(z,'iv') for z in c] for c in r['density_polynomial_at_point']]
 ai=[getball(x,'arb') for x in r['i']];aj=[getball(x,'arb') for x in r['j']];ii=[getball(x,'iv') for x in r['i']];ij=[getball(x,'iv') for x in r['j']]
 closed=[];taylor=[];rem_bounds=[]
 for n in range(1,262):
  m=2*n;row=[];tr=[]
  for offset,lam,s,y0,iy0 in [(n-1,-(m+4),1,ai[n-1],ii[n-1]),(n,m-4,-1,aj[n-1],ij[n-1])]:
   row.append(make_closed(ac[offset],lam,s,y0));p,e,rem=make_taylor(ic[offset],lam,s,iy0,h,Q);tr.append((p,e));rem_bounds.append(rem)
  closed.append(row);taylor.append(tr)
 def finite_point(d):
  x=(qarb(tc+d)).exp();vv=[f(d) for row in closed for f in row]
  Fval=qarb(cl)*x**2+x**4/2*sum((2*n*(vv[2*n-2]-vv[2*n-1]) for n in range(1,262)),arb(0))
  dens=[horner(c,qarb(d)) for c in ac]
  mu=qarb(cl)+x**2/2*sum((2*n*((2*n+1)*vv[2*n-2]+(2*n-1)*vv[2*n-1]-dens[n-1]-dens[n]) for n in range(1,262)),arb(0))
  return {'F':record(Fval),'wprime':record(2*qarb(cl)-mu),'r':record(x)}
 output=[]
 for j in range(K):
  dl=-h+2*h*j/K;du=-h+2*h*(j+1)/K;dc=(dl+du)/2;d=(du-dl)/2;darb=qarb(d);z=hull(-d,d,'arb');domain=hull(dl,du,'arb');v=hull(dl/h,du/h,'iv')
  arange=[horner(c,domain) for c in ac];irange=[horner(c,v*qiv(h)) for c in ic];cp=[horner([l*c[l] for l in range(1,8)],domain) for c in ac]
  av=[];bv=[]
  for n in range(1,262):
   m=2*n
   for pos,offset,lam,s in [(0,n-1,-(m+4),1),(1,n,m-4,-1)]:
    yc=closed[n-1][pos](dc);cc=horner(ac[offset],qarb(dc));MC=abs(arange[offset]);MCP=abs(cp[offset]);MY=(abs(lam)*darb).exp()*(abs(yc)+darb*MC)
    RR=darb**2*(lam**2*MY+abs(lam)*MC+MCP)/2;rad=bounds(RR)[1]
    av.append(yc+(lam*yc+s*cc)*z+hull(-rad,rad,'arb'))
    p,e=taylor[n-1][pos];bv.append(horner(p,v)+e)
  vals={}
  for name,vv,dens,q,exp,dom in [('arb',av,arange,qarb,lambda x:x.exp(),domain),('iv',bv,irange,qiv,iv.exp,v*qiv(h))]:
   r2=exp(2*(q(tc)+dom));mu=q(cl)+r2/2*sum((2*n*((2*n+1)*vv[2*n-2]+(2*n-1)*vv[2*n-1]-dens[n-1]-dens[n]) for n in range(1,262)),q(0));wp=2*q(cl)-mu
   vals[name]=record(wp)
  al,au=rec_bounds(vals['arb']);bl,bu=rec_bounds(vals['iv']);assert max(al,bl)<=min(au,bu)
  output.append({'subcell':j,'delta_exact':[str(dl),str(du)],'arb':vals['arb'],'iv':vals['iv']})
  if j%16==15:print(json.dumps({'utc':utc(),'done':j+1,'total':K,'last_arb':vals['arb']['display'],'last_iv':vals['iv']['display']}),flush=True)
 endpoints=[finite_point(-h),finite_point(h)]
 ivends=[]
 for v0 in [-1,1]:
  vv=[horner(p,qiv(v0))+e for row in taylor for p,e in row];x=iv.exp(qiv(tc+v0*h));ff=qiv(cl)*x**2+x**4/2*sum((2*n*(vv[2*n-2]-vv[2*n-1]) for n in range(1,262)),qiv(0));ivends.append(record(ff))
 global_bounds={}
 for name in ['arb','iv']:
  lo=min(rec_bounds(v[name])[0] for v in output);hi=max(rec_bounds(v[name])[1] for v in output);global_bounds[name]={'lower_exact':str(lo),'upper_exact':str(hi),'display':[float(lo),float(hi)]};assert lo>10
 assert rec_bounds(endpoints[0]['F'])[1]<0<rec_bounds(endpoints[1]['F'])[0]
 assert rec_bounds(ivends[0])[1]<0<rec_bounds(ivends[1])[0]
 rootpath=B/'research/modal_source/evidence/source_result.json';assert sha(rootpath)=='51f283cd4ea7145f633e5449236cdd0bc2879b9ccf922d9fbadb6a609afa4691'
 root=json.loads(rootpath.read_text())['final_root_endpoints_exact'];root=list(map(F,root))
 assert rec_bounds(endpoints[0]['r'])[1]<root[0]<root[1]<rec_bounds(endpoints[1]['r'])[0]
 pub=json.loads((E/'num_axis_cell.json').read_text(),parse_float=F);assert len(pub['cells'])==1 and pub['cells'][0]['ci']==4102
 row=pub['cells'][0];excess=qarb(row['r_hi'])-qarb(tc+h).exp();assert bounds(excess)[0]>0
 comparisons={}
 for name,zs in [('arb',endpoints),('iv',[{'F':v} for v in ivends])]:
  contained=[]
  for v,key in zip(zs,['xV1_left','xV1_right']):
   l,u=rec_bounds(v['F']);pl,pu=row[key];contained.append(pl<=l<=u<=pu)
  comparisons[name]={'num_endpoint_intervals_contain_ours':contained,'our_lower_exceeds_num_claim':rec_bounds(global_bounds[name])[0]>row['wprime_lower']}
 out={'utc':utc(),'status':'PASS','methods':['Arb512 finite exact polynomial ODE at centers plus second derivative bounds','mpmath.iv180 density ODE order16 with residual variation-of-constants remainder'],'code_sha256':sha(__file__),'proof_sha256':sha(B/'research/axis_crossing/PROOF.md'),'sample_sha256':sha(B/'research/residual_samples/evidence/sample_result.json'),'source_result_sha256':sha(rootpath),'num_snapshot_sha256':sha(E/'num_axis_cell.json'),'cell':4102,'t_endpoints_exact':[str(a),str(b)],'t_center_exact':str(tc),'h_exact':str(h),'K':K,'Q':Q,'modes':261,'subcells':output,'moment_remainders_upper_exact':rem_bounds,'global_wprime':global_bounds,'arb_endpoints':endpoints,'iv_endpoint_F':ivends,'root_bracket_exact':[str(z) for z in root],'num_printed_rhi_minus_true_endpoint':record(excess),'num_comparisons':comparisons,'seconds':time.monotonic()-start,'scope':'Exactly one axis zero in exact cell4102. Other axis signs/global flow and full inverse are not established.'}
 (E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'wprime':{k:v['display'] for k,v in global_bounds.items()},'num_comparisons':comparisons,'excess':record(excess)['display'],'seconds':out['seconds']}),flush=True)
if __name__=='__main__':main()
